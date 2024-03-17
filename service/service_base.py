import datetime
import threading
from abc import abstractmethod
from time import sleep

from base.base_objects import base_object, objects, ThreadWrapper, thread_base
from dao.dao_base import base_dao


# base class for all services
class service_base(base_object):
    dao: base_dao
    def __init__(self):
        super().__init__()
    # get name of base object
    def get_base_object_name(self) -> str:
        return "service_base"
    def initialize(self):
        print("")
    # get type of base object
    def get_base_object_type(self) -> str:
        return "Service"


# base class for all services
class service_thread_base(service_base, thread_base):
    def __init__(self):
        super().__init__()
    # get type of base object
    def get_base_object_type(self) -> str:
        return "service_thread_base"
    # initialize this service
    def initialize(self):
        self.initialize_thread()
