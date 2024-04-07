import datetime
import os
import string
import threading
import uuid
from dataclasses import asdict
from typing import Callable

import base.base_utils
import base.base_interfaces
from base.base_interfaces import *
from abc import abstractmethod
from time import sleep
from flask import Flask, jsonify, request, abort
import logging

httpflaskapp: Flask = Flask(__name__)


# base object that will be registered in ObjectManager
# every single object inside app that is not data should extend this class
class base_object:
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
        pass
    # get name of base object
    @abstractmethod
    def get_base_object_name(self) -> str:
        pass
    def get_base_dict_custom_info(self) -> dict[str, any]:
        return {}
    def has_name(self, name: str) -> bool:
        return name == "" or name == type(self).__name__ or name == self.object_id or name == self.get_base_object_type() or name == self.get_base_object_name()
    # get base information about this object
    def get_base_dict_info(self) -> dict[str, any]:
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

# wrapper for threads used in threading classes
class ThreadWrapper(base_object):
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
        return "ThreadWrapper"
    # get name of base object
    def get_base_object_name(self) -> str:
        return self.object.get_base_object_name()
    def tick(self) -> int:
        self.ticks_count = self.ticks_count + 1
        return self.ticks_count
    def get_base_dict_custom_info(self) -> dict[str, any]:
        return {
            "object_id": self.object_id,
            "created_date": self.created_date,
            "thread_name": self.thread.name,
            "thread_native_id": self.thread.native_id,
            "is_working": self.is_working,
            "ticks_count": self.ticks_count,
            "sleep_time": self.sleep_time
        }


# base class for all services
class thread_base(base_object):
    thread: ThreadWrapper
    def __init__(self):
        super().__init__()

    # work in separated thread
    @abstractmethod
    def thread_work(self, tick: int) -> bool:
        pass
    def get_thread_sleep_time(self) -> int:
        return 60
    def thread_run(self) -> None:
        logging.info("Starting work in separated thread, UUID: " + self.object_id)
        while (self.thread.is_working):
            tick = self.thread.tick()
            self.thread_work(tick)
            logging.debug("..... thread working for object: " + self.object_id)
            sleep(self.thread.sleep_time)
        logging.warning("Thread ended: " + self.object_id)
        self.thread.end_time = datetime.datetime.now()

    # initialize this service
    def initialize_thread(self) -> None:
        th = threading.Thread(target=self.thread_run,daemon=True)
        self.thread = ThreadWrapper(th, self, self.get_thread_sleep_time())
        logging.info("Initialize separated thread for object: " + self.object_id + ", native_id: " + str(th.native_id) + ", name: " + th.name)
        th.start()
        objects.register_thread(self.thread)


# watch dogs
class WatchDog(thread_base):
    threads: list[ThreadWrapper]
    def __init__(self, threads: list[ThreadWrapper]):
        super().__init__()
        logging.info("Initializing new WatchDog, object_id: " + self.object_id + ", threads: " + str(len(threads)))
        self.threads = threads
        self.initialize_thread()
    def thread_work(self, tick: int) -> bool:
        logging.debug("Watchdog is checking threads: " + str(len(self.threads)))
        return True
    def get_base_object_type(self) -> str:
        return "WatchDog"
    # get name of base object
    def get_base_object_name(self) -> str:
        return "WatchDog"


class Cleaner(thread_base):
    clean_method: Callable[[int], bool]
    def __init__(self, clean_method: Callable[[int], bool]):
        self.clean_method = clean_method

# main Flask application
class FlaskApplicationWrapper(base_object):
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


class CacheManagerBase(thread_base):
    def put(self, key: str, obj: any, method: any, ttl_seconds: int = 60):
        pass
    def get(self, key: str):
        pass

class DaoConnectionBase(base_object):
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
    session_id: str
    created_date: datetime.datetime
    valid_till_date: datetime.datetime
    tenant_uid: str
    account_uid: str
    token: str
    token_salt: str
    token_hash: str
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
    def is_valid(self) -> bool:
        return datetime.datetime.now() > self.valid_till_date


class AccountPermissionsBase:
    created_date: datetime.datetime
    valid_till_date: datetime.datetime
    account_uid: str
    account_dto: account_interface_dto
    tenant_dto: tenant_interface_dto
    roles: set[str]
    def __init__(self, account_uid: str, account_dto: account_interface_dto, tenant_dto: tenant_interface_dto, roles: set[str]):
        self.created_date = datetime.datetime.now()
        self.account_uid = account_uid
        self.account_dto = account_dto
        self.tenant_dto = tenant_dto
        self.roles = roles
    def to_myself_dict(self) -> dict:
        return {"account": asdict(self.account_dto.to_normal()),
                "tenant": asdict(self.tenant_dto.to_normal()),
                "roles": list(self.roles)}


class RequestBase:
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


# Manager of all objects and threads in application
class ObjectManager:
    object_uid: str
    created_date: datetime.datetime
    all_objects: dict[str, base_object]  # all base objects registered
    threads: list[ThreadWrapper]  # all threads registered
    cache_managers: list[CacheManagerBase]  # all cache managers registered
    system_version_uid: str = "1.0.0"  # UID of system version
    system_instance_uid: str = base.base_utils.get_random_uid_with_prefix("SI")
    any_instance_value: str = "any_value"
    http_port: int = 8080
    created_by_default: str = "system"  # default account that is creating
    account_sessions: dict[str, AccountSessionBase]  # sessions of user, key=token, value=session with user
    account_permissions: dict[str, AccountPermissionsBase]  # set of permissions per account
    dao_connections: DaoConnectionsBase  # DAO connections
    watchdogs = []  # list of watchdogs
    cleaners = []  # list of cleaners
    flask_wrapper: FlaskApplicationWrapper  # flast wrapper
    exception_handler: Callable[[Exception], bool]
    thread_handler: Callable[[ThreadWrapper], bool]
    request_handler: Callable[[RequestBase], bool]

    def __init__(self):
        self.created_date = datetime.datetime.now()
        self.object_uid = base.base_utils.get_random_uid_with_prefix("SI")
        logging.info("Creating ObjectManager, creation time: " + str(self.created_date) + ", object_id: " + self.object_uid + ", system_instance_uid: " + self.system_instance_uid)
        self.all_objects = {}
        self.threads = []
        self.account_sessions = {}
        self.account_permissions = {}

    # initialize
    def initialize(self) -> None:
        logging.info("Initializing ObjectManager, version: " + self.system_version_uid + ", system_instance_uid: " + self.system_instance_uid)
        self.watchdogs.append(WatchDog(self.threads))
        self.watchdogs.append(WatchDog(self.threads))
        self.flask_wrapper = FlaskApplicationWrapper(httpflaskapp)

    def register_object(self, obj: base_object) -> None:
        self.all_objects[obj.object_id] = obj
    def register_thread(self, thread: ThreadWrapper) -> None:
        logging.debug("Register Thread in Object Manager, parent: " + self.system_instance_uid + ", object: " + thread.object_id)
        self.threads.append(thread)
    def register_event(self, event) -> None:
        logging.debug("Register event ")
    def register_cache(self, cm: CacheManagerBase) -> None:
        #self.cache_managers.append(cm)
        logging.debug("Register cache in Object Manager, parent: " + self.system_instance_uid + ", object: " + cm.object_id)
    def register_connections(self, dao_connections: DaoConnectionsBase) -> None:
        logging.debug("Register connections in Object Manager, parent: " + self.system_instance_uid + ", object: " + dao_connections.object_id)
        self.dao_connections = dao_connections
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
    def register_thread_handler(self, thread_handler: Callable[[ThreadWrapper], bool]):
        self.thread_handler = thread_handler
    def register_request_handler(self, request_handler: Callable[[RequestBase], bool]):
        self.request_handler = request_handler
    def handle_exception(self, ex: Exception) -> bool:
        return self.exception_handler(ex)
    def handle_thread(self, ex: ThreadWrapper) -> bool:
        return self.thread_handler(ex)
    def handle_request(self, req: RequestBase) -> bool:
        return self.request_handler(req)


# all the most important objects in application
objects = ObjectManager()
