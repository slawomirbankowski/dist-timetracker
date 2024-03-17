from base.base_objects import base_object
from controller.controller_auth import AuthController
from controller.controller_object import ObjectController
from controller.controller_process import ProcessController
from controller.controller_report import ReportController
from controller.controller_service import ServiceController


# class with all controllers
class Controllers(base_object):
    auth_controller = AuthController()
    object_controller = ObjectController()
    process_controller = ProcessController()
    report_controller = ReportController()
    service_controller = ServiceController()

    def __init__(self):
        super().__init__()

    # get name of base object
    def get_base_object_name(self) -> str:
        return "Controllers"
    # get type of base object
    def get_base_object_type(self) -> str:
        return "Controllers"
    def initialize_controllers(self):
        print("Initialization of Controller classes")
    # handler for closing application
    def close(self):
        print("Closing controllers")


# all known controllers for HTTP requests/responses
controllers = Controllers()
