import logging

from base.base_objects import base_object, ThreadBase
from backend.dao.dao_base import base_dao


# base class for all services
class service_base(base_object):
    dao: base_dao
    def __init__(self):
        super().__init__()
    # get name of base object
    def get_base_object_name(self) -> str:
        return "service_base"
    def initialize(self) -> None:
        logging.info("")
    # get type of base object
    def get_base_object_type(self) -> str:
        return "Service"


# base class for all services
class ServiceThreadBase(service_base, ThreadBase):
    def __init__(self):
        super().__init__()
    # get type of base object
    def get_base_object_type(self) -> str:
        return "service_thread_base"
    # initialize this service
    def initialize(self) -> None:
        self.initialize_thread()
        self.on_initialize()
    def on_initialize(self) -> None:
        pass