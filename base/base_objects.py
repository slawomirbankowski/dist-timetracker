import datetime
import os
import string
import threading
import uuid
from abc import abstractmethod
from time import sleep

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


# Manager of all objects and threads
class ObjectManager:
    created_date: datetime.datetime
    all_objects: dict[str, base_object]
    threads: list[ThreadWrapper]
    def __init__(self):
        self.created_date = datetime.datetime.now()
        print("Creating object manager, creation time: " + str(self.created_date))
        self.all_objects = {}
        self.threads = []
    def initialize(self):
        print("Initializing object manager")
    def register_object(self, obj: base_object):
        self.all_objects[obj.object_id] = obj
    def register_thread(self, thread: ThreadWrapper):
        self.threads.append(thread)

    def get_life_time_seconds(self):
        x = datetime.datetime.now() - self.created_date
        return x.total_seconds()
    def get_base_objects_list(self, name: str = ""):
        return list(filter(lambda o: o.has_name(name), self.all_objects.values()))

    def get_base_object_infos(self, name: str = "") -> list[dict[str, any]]:
        return list(map(lambda o: o.get_base_dict_info(), self.get_base_objects_list(name)))

    def get_threads_infos(self) -> list[dict[str, any]]:
        return list(map(lambda o: o.get_base_dict_info(), self.threads))



objects = ObjectManager()
