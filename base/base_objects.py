import datetime
import os
import string
import threading
import uuid
from abc import abstractmethod
from time import sleep
from flask import Flask, jsonify, request, abort

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
        print("Creating new base object, UUID: " + self.object_id + ", created: " + str(self.created_date))
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
    def thread_run(self):
        print("Starting work in separated thread, UUID: " + self.object_id)
        while (self.thread.is_working):
            tick = self.thread.tick()
            self.thread_work(tick)
            print("..... thread working for object: " + self.object_id)
            sleep(self.thread.sleep_time)
        print("Thread ended: " + self.object_id)
        self.thread.end_time = datetime.datetime.now()

    # initialize this service
    def initialize_thread(self):
        print("Initialize separated thread for object: " + self.object_id)
        th = threading.Thread(target=self.thread_run,daemon=True)
        self.thread = ThreadWrapper(th, self, self.get_thread_sleep_time())
        th.start()
        objects.register_thread(self.thread)


# watch dogs
class WatchDog(thread_base):
    threads: list[ThreadWrapper]
    def __init__(self, threads: list[ThreadWrapper]):
        super().__init__()
        self.threads = threads
        self.initialize_thread()
    def thread_work(self, tick: int) -> bool:
        print("Watchdog is checking threads: " + str(len(self.threads)))
        return True
    def get_base_object_type(self) -> str:
        return "WatchDog"
    # get name of base object
    def get_base_object_name(self) -> str:
        return "WatchDog"

# main Flask application


#
class FlaskApplicationWrapper(base_object):
    httpflaskapp: Flask
    def __init__(self, httpflaskapp: Flask):
        super().__init__()
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


# Manager of all objects and threads
class ObjectManager:
    created_date: datetime.datetime
    all_objects: dict[str, base_object]
    threads: list[ThreadWrapper]
    cache_managers: list[CacheManagerBase]
    system_version_uid: str = "1.0.0"
    system_instance_uid: str = "1.0.0"  # TODO: create instance UID
    any_instance_value: str = "any_value"
    created_by_default: str = "system"
    dao_connections: DaoConnectionsBase
    watchdogs = []
    flask_wrapper: FlaskApplicationWrapper

    def __init__(self):
        self.created_date = datetime.datetime.now()
        print("Creating object manager, creation time: " + str(self.created_date))
        self.all_objects = {}
        self.threads = []

    # initialize
    def initialize(self):
        print("Initializing object manager")
        self.watchdogs.append(WatchDog(self.threads))
        self.watchdogs.append(WatchDog(self.threads))
        self.flask_wrapper = FlaskApplicationWrapper(httpflaskapp)

    def register_object(self, obj: base_object):
        self.all_objects[obj.object_id] = obj
    def register_thread(self, thread: ThreadWrapper):
        self.threads.append(thread)
    def register_event(self, event):
        print("Register event ")
    def register_cache(self, cm: CacheManagerBase):
        #self.cache_managers.append(cm)
        print("Register cache")
    def register_connections(self, dao_connections: DaoConnectionsBase):
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



# all the most important objects in application
objects = ObjectManager()
