from __future__ import annotations
import datetime
import os
import socket
import string
import threading
import uuid
from dataclasses import asdict
from typing import Callable

import base.base_utils
import base.base_interfaces
from base.base_constants import Roles
from base.base_interfaces import *
from abc import abstractmethod
from time import sleep
from flask import Flask, jsonify, request, abort
import logging

httpflaskapp: Flask = Flask(__name__)


class base_object:
    """base object that will be registered in ObjectManager; every single object inside app that is not data should extend this class"""
    object_id: str
    usage_count: int
    created_date: datetime.datetime
    def __init__(self):
        self.created_date = datetime.datetime.now()
        self.usage_count = 0
        self.object_id = str(type(self).__name__) + "_" + str(self.created_date)[:10].replace("-", "_") + "_" + str(uuid.uuid4())[:13].replace("-", "_")
        objects.register_object(self)
        logging.debug("Creating new base object, UUID: " + self.object_id + ", created: " + str(self.created_date))
    # get type of base object
    @abstractmethod
    def get_base_object_type(self) -> str:
        """get type of this object - that is logical type name like DTO, Dao, Service, Controller"""
        pass
    # get name of base object
    @abstractmethod
    def get_base_object_name(self) -> str:
        """get friendly name of this object; friendly name is a simple name to identify that object"""
        pass
    def get_base_dict_custom_info(self) -> dict[str, any]:
        """to be overridden by any class - returning custom specific info """
        return {}
    def has_name(self, name: str) -> bool:
        return name == "" or name == type(self).__name__ or name == self.object_id or name == self.get_base_object_type() or name == self.get_base_object_name()

    def get_base_dict_info(self) -> dict[str, any]:
        """get base information about this object as dictionary with class name, object_id, usages count and many other values"""
        d = {
            "class_name": type(self).__name__,
            "class_qual_name": type(self).__qualname__,
            "object_id": self.object_id,
            "created_date": str(self.created_date),
            "usage_count": self.usage_count,
            "base_type": self.get_base_object_type(),
            "base_name": self.get_base_object_name()
        }
        d.update(self.get_base_dict_custom_info())
        return d


class DictOfList(dict[str, list[str]]):
    """dictionary with list as values"""
    def add(self, key: str, value: str) -> None:
        values = self.get(key)
        if values is None:
            values = []
            self[key] = values
        values.append(value)
    def get_or_empty(self, key: str) -> list[str]:
        value = self[key]
        if value:
            return value
        else:
            return []


class DictOfDict(dict[str, dict[str, str]]):
    def add(self, key1: str, key2: str, value: str) -> None:
        values = self.get(key1)
        if values is None:
            values = {}
            self[key1] = values
        values[key2] = value
    pass


class AccountRole:
    """single role within hierarchy"""
    role: auth_role_interface_dto  # role
    parent: AccountRole | None  # parent role
    children: dict[str, AccountRole]  # children roles
    roles_below: set[str]
    level: int = 0  # level in hierarchy
    def __init__(self, r: auth_role_interface_dto):
        self.role = r
        self.parent = None
        self.children = {}
        self.roles_below = set()
        self.level = 0
    def calculate_roles_below(self) -> set[str]:
        below_roles = set()
        for r in self.children:
            for b in self.children[r].calculate_roles_below():
                below_roles.add(b)
        self.roles_below = below_roles
        return below_roles
    def to_hierarchy(self) -> dict[str, dict]:
        if len(self.children) == 0:
            return {self.role.auth_role_uid: {}}
        else:
            h = {}

            # TODO: finish returning hierarchy of roles
            return {self.role.auth_role_uid: h}


class AccountRolesHierarchy:
    """hierarchy of roles"""
    all_roles: list[auth_role_interface_dto]
    roles_dict: dict[str, AccountRole]
    roles_list: list[AccountRole]
    root: AccountRole

    def __init__(self, roles: list[auth_role_interface_dto]):
        self.all_roles = roles
        self.roles_dict = {}
        self.roles_list = []
        logging.info(f"Producing roles hierarchy from list, count: {len(roles)}")
        for role in roles:
            r = AccountRole(role)
            self.roles_dict[role.auth_role_uid] = r
            self.roles_list.append(r)
            if role.auth_role_uid == Roles.SystemAdministrator:
                self.root = r
        for role in self.roles_list:
            if role.role.parent_auth_role_uid is not None and role.role.parent_auth_role_uid != "" and role.role.parent_auth_role_uid != role.role.auth_role_uid:
                if self.roles_dict.__contains__(role.role.parent_auth_role_uid):
                    parent = self.roles_dict[role.role.parent_auth_role_uid]
                    role.parent = parent
                    parent.children[role.role.auth_role_uid] = role

    def get_roles_below(self, role_uid: str) -> set[str]:
        # TODO: get roles below this role
        return set()

    def get_roles_above(self, role_uid: str) -> set[str]:
        # TODO: get roles above this role
        return set()

    def to_hierarchy(self) -> dict[str, any]:
        # TODO: create simple hierarchy for roles
        return {}


class ThreadWrapper(base_object):
    """wrapper for threads used in threading classes"""
    thread: threading.Thread
    object: base_object
    is_working: bool = True
    ticks_count: int = 0
    sleep_time: int = 60
    end_time: datetime.datetime | None = None
    def __init__(self, thread: threading.Thread, object: base_object, sleep_time: int = 60):
        super().__init__()
        self.thread = thread
        self.object = object
        self.sleep_time = sleep_time
    def get_base_object_type(self) -> str:
        """get type of this class"""
        return "ThreadWrapper"
    # get name of base object
    def get_base_object_name(self) -> str:
        return self.object.get_base_object_name()
    def tick(self) -> int:
        """increment ticks in current thread, ticks are counters per thread to see how many times thread executed runnable funcion"""
        self.ticks_count = self.ticks_count + 1
        return self.ticks_count
    def get_base_dict_custom_info(self) -> dict[str, any]:
        """get custom dictionary information with thread specific values"""
        return {
            "object_id": self.object_id,
            "created_date": self.created_date,
            "thread_name": self.thread.name,
            "thread_native_id": self.thread.native_id,
            "is_working": self.is_working,
            "ticks_count": self.ticks_count,
            "sleep_time": self.sleep_time
        }
    def is_thread_active(self) -> int:
        """returns 1 if thread is still active or 0 is inactive"""
        # TODO: implement this
        return 1


# base class for all services
class ThreadBase(base_object):
    """base class for any thread class with thread_work method executed in separated dedicated thread"""
    thread: ThreadWrapper
    def __init__(self):
        super().__init__()

    @abstractmethod
    def thread_work(self, tick: int) -> bool:
        """work in separated thread - to be overridden"""
        pass
    def get_thread_sleep_time(self) -> int:
        """get sleep time in seconds"""
        return 60
    def thread_run(self) -> None:
        """running thread and executing thread_work method, then sleep for thread sleep time, works until thread_is_working"""
        logging.info("Starting work in separated thread, UUID: " + self.object_id)
        while (self.thread.is_working):
            tick = self.thread.tick()
            self.thread_work(tick)
            logging.debug("..... thread working for object: " + self.object_id)
            sleep(self.thread.sleep_time)
        logging.warning("Thread ended: " + self.object_id)
        self.thread.end_time = datetime.datetime.now()

    def initialize_thread(self) -> None:
        """initialize this thread, make is a daemon and register thread in object manager"""
        th = threading.Thread(target=self.thread_run,daemon=True)
        self.thread = ThreadWrapper(th, self, self.get_thread_sleep_time())
        logging.info("Initialize separated thread for object: " + self.object_id + ", native_id: " + str(th.native_id) + ", name: " + th.name)
        th.start()
        objects.register_thread(self.thread)


# watch dogs
class WatchDog(ThreadBase):
    """class to watch for threads, objects, other processes, able to restart killed threads"""
    threads: list[ThreadWrapper]
    def __init__(self, threads: list[ThreadWrapper]):
        super().__init__()
        logging.info("Initializing new WatchDog, object_id: " + self.object_id + ", threads: " + str(len(threads)))
        self.threads = threads
        self.initialize_thread()
    def thread_work(self, tick: int) -> bool:
        """separated thread to """
        # TODO: implement checking threads in ObjectManager and processes
        logging.debug("Watchdog is checking threads: " + str(len(self.threads)))
        return True
    def get_base_object_type(self) -> str:
        return "WatchDog"
    # get name of base object
    def get_base_object_name(self) -> str:
        return "WatchDog"


class Cleaner(ThreadBase):
    """cleaner class to clean after processes, remove old rows, create backups and copies"""
    clean_method: Callable[[int], bool]
    def __init__(self, clean_method: Callable[[int], bool]):
        super().__init__()
        self.clean_method = clean_method
    def thread_work(self, tick: int) -> bool:
        logging.debug("Cleaner is cleaning")
        return True
    def get_base_object_type(self) -> str:
        return "Cleaner"
    # get name of base object
    def get_base_object_name(self) -> str:
        return "Cleaner"


# main Flask application
class FlaskApplicationWrapper(base_object):
    """wrapper class for Flask application to have HTTP endpoints"""
    httpflaskapp: Flask
    def __init__(self, httpflaskapp: Flask):
        super().__init__()
        logging.info("Initializing Flask WRAPPER, object_id: " + self.object_id)
        self.httpflaskapp = httpflaskapp
    # get type of base object
    def get_base_object_type(self) -> str:
        return "FlaskApplicationWrapper"
    # get name of base object
    def get_base_object_name(self) -> str:
        return "FlaskApplicationWrapper"
    def thread_work(self, tick: int) -> bool:
        logging.debug("Flask is working")
        #self.httpflaskapp.blueprints
        return True

class CacheManagerBase(ThreadBase):
    """base class for CacheManager"""
    def put(self, key: str, obj: any, method: any, ttl_seconds: int = 60):
        pass
    def get(self, key: str):
        pass
    # get type of base object
    def get_base_object_type(self) -> str:
        return "CacheManagerBase"
    # get name of base object
    def get_base_object_name(self) -> str:
        return "CacheManagerBase"


class DaoConnectionBase(base_object):
    """base class for DAOConnection - connection pool to single database"""
    def initialize_connection(self, db_url: str, db_host: str, db_name: str, db_user: str, db_pass: str,
                              min_conns: int = 2, max_conns: int = 20):
        pass
    def get_connection(self):
        pass
    def close(self, db_conn):
        pass
    def get_url(self):
        pass


# DAO connections to main database and all other client databases
class DaoConnectionsBase(base_object):
    """base class for DaoConnections - many connections to tenant databases """
    def create_tenant_connection(self, db_url: str, db_host: str, db_name: str, db_user: str, db_pass: str):
        pass
    def get_connection(self):
        pass
    def close_connections(self):
        pass
    def close(self, db_conn):
        pass
    def get_tenant_connection(self, db_name: str) -> DaoConnectionBase:
        pass
    def close_tenant_connection(self, db_name: str, db_conn):
        pass


class base_model(base_object):
    """model class for given table - contains all metadata info about model in database"""
    table_name: str  # name of table in database
    key_column_name: str  # name of UID column, typically it is table_uid
    all_columns: list[str]  # list od all column names
    attr_columns: list[str]  # list of attribute columns
    rich_columns: list[str]
    insert_columns: list[str]  # list of attribute columns
    insert_columns_list: str  #
    insert_columns_question_marks: str  #
    attr_no_uid_columns: list[str]
    attr_no_uid_columns_eq: list[str]
    all_columns_list: str  # all column comma separated list like id,col1,col2,col3,created_date,...
    attr_columns_list: str  # list of attributes list like col1,col2,col3,...
    attr_no_uid_columns_list: str  # list of attributes list like col1,col2,col3,...
    attr_no_uid_columns_eq_list: str
    all_question_marks: str  # question marks like ?,?,?,?,?
    attr_question_marks: str  #
    insert_attrs_sql: str
    update_attrs_sql: str
    upsert_columns: list[str]
    upsert_columns_exclude_list: str
    upsert_attrs_sql: str
    select_all_sql: str
    attr_types: dict[str, str]
    fks: dict[str, str]
    table_comment: str
    thin_columns: list[str]
    thin_column_list: str


# session for account - mapping between token and account_uid with validation date, created date
class AccountSessionBase:
    """base class for session account - connecting token with account"""
    session_id: str
    created_date: datetime.datetime
    valid_till_date: datetime.datetime
    tenant_uid: str
    account_uid: str
    token: str
    token_salt: str
    token_hash: str
    session_load_date: datetime.datetime
    def __init__(self, tenant_uid: str, account_uid: str, token: str, token_salt: str, token_hash: str, valid_till_date: datetime.datetime):
        self.created_date = datetime.datetime.now()
        self.session_id = base.base_utils.get_random_uid()
        self.tenant_uid = tenant_uid
        self.account_uid = account_uid
        logging.debug("Initializing session for Account, session_id: " + self.session_id + ", account: " + self.account_uid + ", tenant: " + self.tenant_uid)
        self.token = token
        self.token_salt = token_salt
        self.token_hash = token_hash
        self.valid_till_date = valid_till_date
        self.session_load_date = datetime.datetime.now()

    def is_valid(self) -> bool:
        return datetime.datetime.now() > self.valid_till_date


class AccountPermissionsBase:
    """base class for permission class connecting account with tenant and permissions"""
    created_date: datetime.datetime
    account_uid: str
    account_dto: account_interface_dto
    tenant_dto: tenant_interface_dto
    roles: set[str]
    permission_load_date: datetime.datetime
    def __init__(self, account_uid: str, account_dto: account_interface_dto, tenant_dto: tenant_interface_dto, roles: set[str]):
        self.created_date = datetime.datetime.now()
        self.account_uid = account_uid
        self.account_dto = account_dto
        self.tenant_dto = tenant_dto
        self.roles = roles
        self.permission_load_date = datetime.datetime.now()


class RequestBase:
    """base class for request - single request is representing HTTP request"""
    url: str
    method_name: str
    request_id: str
    created_date: datetime.datetime
    authorization_header: str
    authorization_method: str
    authorization_token: str
    account_session: AccountSessionBase | None
    account_permission: AccountPermissionsBase | None
    body_as_text: str | None
    body_as_dict: dict | None
    def get_account_uid(self) -> str | None:
        if self.account_session is None:
            return None
        else:
            return self.account_session.account_uid


class ResponseBase:
    """base class for HTTP response; each response is directly connected with request; response could be successfull (2xx) or failure (4xx, 5xx)"""
    code: int = 200
    req_session: RequestBase
    obj: dict[str, any] | None
    end_time: datetime.datetime | None
    error_message: str
    def request_time_seconds(self) -> float:
        return (self.req_session.created_date - self.end_time).total_seconds()


#
@dataclass(frozen=False)
class AppMenuItemDto:
    """single item in menu - DTO class"""
    menu_name: str
    menu_url: str
    menu_roles: str
    menu_parent_name: str


@dataclass(frozen=False)
class AppMenuItem:
    """single item in menu - part of hierarchy to produce menu"""
    menu_name: str
    menu_url: str
    menu_roles: set[str]
    menu_subitems: list[AppMenuItem]
    def __init__(self, name: str, url: str, roles: set[str], submenus: list[AppMenuItem]):
        self.menu_name = name
        self.menu_url = url
        self.menu_roles = roles
        self.menu_roles = roles
    def to_dict(self) -> dict[str, any]:
        return {
            "menu_name": self.menu_name,
            "menu_url": self.menu_url,
            "menu_roles": self.menu_roles,
            "menu_subitems": [item.to_dict() for item in self.menu_subitems],
        }


@dataclass(frozen=False)
class AppMenuItems:
    menu: list[AppMenuItem]
    loaded_menu: list[AppMenuItem]

    def __init__(self):
        self.menu = self.create_full_menu()

    def get_menu_full(self) -> list[AppMenuItem]:
        return self.menu

    def get_menu_by_request(self, req: RequestBase) -> list[AppMenuItem]:
        # TODO: filter menu based on roles
        return self.menu

    def load_menu(self, dtos: list[AppMenuItemDto]) -> str:
        # TODO: parse items from dtos and create loaded_menu
        return ""

    def create_full_menu(self) -> list[AppMenuItem]:
        return [
            AppMenuItem("Tenant", "/app/tenant", {Roles.TenantViewer}, []),
            AppMenuItem("Client", "/app/tenant", {Roles.ClientSupervisor}, []),
            AppMenuItem("Account", "/app/account", {Roles.AccountViewer}, []),
            AppMenuItem("Time", "/app/time", {Roles.AccountViewer}, [
                AppMenuItem("Entry", "/app/time-entry", {Roles.AccountViewer}, []),
                AppMenuItem("Approval", "/app/time-approval", {Roles.AccountViewer}, []),
                AppMenuItem("Summary", "/app/time-summary", {Roles.AccountViewer}, []),
                AppMenuItem("Report", "/app/time-report", {Roles.AccountViewer}, [])
            ]),
            AppMenuItem("Project", "/app/project", {Roles.AccountViewer}, []),
            AppMenuItem("HR", "/app/hr", {Roles.AccountViewer}, []),
            AppMenuItem("Calendar", "/app/calendar", {Roles.AccountViewer}, [
                AppMenuItem("Project", "/app/project", {Roles.AccountViewer}, []),
                AppMenuItem("Project", "/app/project", {Roles.AccountViewer}, [])
            ]),
            AppMenuItem("Administration", "/app/hr", {Roles.AccountViewer}, [
                AppMenuItem("Reports", "/app/report", {Roles.AccountViewer}, []),
                AppMenuItem("Synchronization", "/app/sync", {Roles.AccountViewer}, []),
                AppMenuItem("Licenses", "/app/license", {Roles.AccountViewer}, [])
            ]),
            AppMenuItem("My", "/app/myself", {Roles.AccountViewer}, [])
        ]


class ObjectManager:
    """Manager of all objects and threads in application"""
    object_uid: str
    created_date: datetime.datetime
    all_objects: dict[str, base_object]  # all base objects registered
    threads: list[ThreadWrapper]  # all threads registered
    cache_managers: list[CacheManagerBase]  # all cache managers registered
    system_version_uid: str = "1.0.0"  # UID of system version
    system_instance_uid: str = base.base_utils.get_random_uid_with_prefix("SI")
    any_instance_value: str = "any_value"
    http_port: int = 8080
    host_name: str
    host_ip: str
    local_path: str
    app_version: str = "1.0.0"
    created_by_default: str = "system"  # default account that is creating
    settings_by_name: dict[str, str]
    account_sessions: dict[str, AccountSessionBase]  # sessions of user, key=token, value=session with user
    account_permissions: dict[str, AccountPermissionsBase]  # set of permissions per account
    dao_connections: DaoConnectionsBase  # DAO connections
    watchdogs = []  # list of watchdogs
    cleaners = []  # list of cleaners
    flask_wrapper: FlaskApplicationWrapper  # flast wrapper
    exception_handler: Callable[[Exception], bool]
    thread_handler: Callable[[ThreadWrapper], bool]
    request_handler: Callable[[ResponseBase], bool]
    requests_count: int
    menu: AppMenuItems
    role_hierarchy: AccountRolesHierarchy

    def __init__(self):
        self.created_date = datetime.datetime.now()
        self.object_uid = base.base_utils.get_random_uid_with_prefix("SI")
        logging.info("Creating ObjectManager, creation time: " + str(self.created_date) + ", object_id: " + self.object_uid + ", system_instance_uid: " + self.system_instance_uid)
        self.all_objects = {}
        self.host_name = socket.gethostname()
        self.host_ip = socket.gethostname()
        self.local_path = os.path.dirname(os.path.realpath(__file__))
        self.threads = []
        self.account_sessions = {}
        self.account_permissions = {}
        self.requests_count = 0
        self.settings_by_name = {}

    # initialize
    def initialize(self) -> None:
        logging.info("Initializing ObjectManager, version: " + self.system_version_uid + ", system_instance_uid: " + self.system_instance_uid)
        self.watchdogs.append(WatchDog(self.threads))
        self.watchdogs.append(WatchDog(self.threads))
        self.flask_wrapper = FlaskApplicationWrapper(httpflaskapp)
        self.menu = AppMenuItems()

    def register_object(self, obj: base_object) -> None:
        self.all_objects[obj.object_id] = obj
    def register_thread(self, thread: ThreadWrapper) -> None:
        logging.debug("Register Thread in Object Manager, parent: " + self.system_instance_uid + ", object: " + thread.object_id)
        self.threads.append(thread)
        self.handle_thread(thread)
    def register_event(self, event) -> None:
        """register new event in Object Manager"""
        logging.debug("Register event ")
    def register_cache(self, cm: CacheManagerBase) -> None:
        #self.cache_managers.append(cm)
        logging.debug("Register cache in Object Manager, parent: " + self.system_instance_uid + ", object: " + cm.object_id)
    def register_connections(self, dao_connections: DaoConnectionsBase) -> None:
        logging.debug("Register connections in Object Manager, parent: " + self.system_instance_uid + ", object: " + dao_connections.object_id)
        self.dao_connections = dao_connections
    def register_roles(self, roles: list[auth_role_interface_dto]):
        """register all roles to create hierarchy"""
        self.role_hierarchy = AccountRolesHierarchy(roles)
    def get_life_time_seconds(self):
        x = datetime.datetime.now() - self.created_date
        return x.total_seconds()
    def get_base_objects_list(self, name: str = ""):
        return list(filter(lambda o: o.has_name(name), self.all_objects.values()))

    def get_base_object_infos(self, name: str = "") -> list[dict[str, any]]:
        return list(map(lambda o: o.get_base_dict_info(), self.get_base_objects_list(name)))

    def get_threads_infos(self) -> list[dict[str, any]]:
        return list(map(lambda o: o.get_base_dict_info(), self.threads))
    # get account HTTP session by token
    def get_account_session_by_token(self, token: str) -> AccountSessionBase | None:
        return self.account_sessions.get(token)
        # return self.account_sessions[token]
    def create_user_session(self, tenant_uid: str, account_uid: str, token: str, token_salt: str, token_hash: str, valid_till_date: datetime.datetime) -> AccountSessionBase:
        session = AccountSessionBase(tenant_uid, account_uid, token, token_salt, token_hash, valid_till_date)
        self.account_sessions[token] = session
        self.account_sessions[token_hash] = session
        return session
    def get_account_permission_by_account(self, account_uid: str) -> AccountPermissionsBase | None:
        return self.account_permissions.get(account_uid)
    def register_exception_handler(self, exception_handler: Callable[[Exception], bool]):
        self.exception_handler = exception_handler
    def register_settings(self, s: dict[str, str]):
        self.settings_by_name = s
    def register_thread_handler(self, thread_handler: Callable[[ThreadWrapper], bool]):
        self.thread_handler = thread_handler
    def register_request_handler(self, request_handler: Callable[[ResponseBase], bool]):
        self.request_handler = request_handler
    def handle_exception(self, ex: Exception) -> bool:
        """handle any exception inside application, log it to DB table and create an event from it"""
        try:
            return self.exception_handler(ex)
        except Exception as ex:
            logging.error(f"Cannot handle Exception, reason: {ex}")
            return False
    def handle_thread(self, ex: ThreadWrapper) -> bool:
        """handle thread change inside application, log it to DB table and create an event from it"""
        try:
            return self.thread_handler(ex)
        except Exception as ex:
            logging.error(f"Cannot handle Thread, reason: {ex}")
            return False
    def handle_request(self, req: ResponseBase) -> bool:
        try:
            self.requests_count += 1
            return self.request_handler(req)
        except Exception as ex:
            logging.error(f"Cannot handle request, reason: {ex}")
            return False


# all the most important objects in application
objects = ObjectManager()
