import logging
from logging import config
from base.base_objects import base_object
from controller.controller_account import AccountController
from controller.controller_auth import AuthController
from controller.controller_client import ClientController
from controller.controller_connection import ConnectionController
from controller.controller_event import EventController
from controller.controller_invoice import InvoiceController
from controller.controller_monitor import MonitorController
from controller.controller_object import ObjectController
from controller.controller_process import ProcessController
from controller.controller_project import ProjectController
from controller.controller_report import ReportController
from controller.controller_service import ServiceController
from controller.controller_tenant import TenantController


# class with all controllers
class Controllers(base_object):
    account_controller = AccountController()
    auth_controller = AuthController()
    client_controller = ClientController()
    connection_controller = ConnectionController()
    event_controller = EventController()
    invoice_controller = InvoiceController()
    monitor_controller = MonitorController()
    object_controller = ObjectController()
    process_controller = ProcessController()
    project_controller = ProjectController()
    report_controller = ReportController()
    service_controller = ServiceController()
    tenant_controller = TenantController()

    def __init__(self):
        super().__init__()

    # get name of base object
    def get_base_object_name(self) -> str:
        return "Controllers"
    # get type of base object
    def get_base_object_type(self) -> str:
        return "Controllers"
    def initialize_controllers(self):
        logging.debug("Initialization of Controller classes, object_id: " + self.object_id)
    # handler for closing application
    def close(self) -> None:
        logging.info("Closing controllers, object_id: " + self.object_id)


# all known controllers for HTTP requests/responses
controllers = Controllers()
