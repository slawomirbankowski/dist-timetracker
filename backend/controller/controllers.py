import logging
from base.base_objects import base_object
from controller.controller_account import AccountController
from controller.controller_auth import AuthController
from controller.controller_base import BaseController
from controller.controller_calendar import CalendarController
from controller.controller_client import ClientController
from controller.controller_competency import CompetencyController
from backend.controller.controller_connection import ConnectionController
from controller.controller_event import EventController
from controller.controller_invoice import InvoiceController
from controller.controller_monitor import MonitorController
from controller.controller_object import ObjectController
from controller.controller_process import ProcessController
from controller.controller_project import ProjectController
from controller.controller_report import ReportController
from controller.controller_service import ServiceController
from controller.controller_storage import StorageController
from controller.controller_synchronization import SynchronizationController
from controller.controller_system import SystemController
from controller.controller_tenant import TenantController


class Controllers(base_object):
    """class with all controllers"""
    all_controllers: list[BaseController] = []
    account_controller = AccountController()
    auth_controller = AuthController()
    client_controller = ClientController()
    calendar_controller = CalendarController()
    competency_controller = CompetencyController()
    connection_controller = ConnectionController()
    event_controller = EventController()
    invoice_controller = InvoiceController()
    monitor_controller = MonitorController()
    object_controller = ObjectController()
    process_controller = ProcessController()
    project_controller = ProjectController()
    report_controller = ReportController()
    service_controller = ServiceController()
    storage_controller = StorageController()
    synchronization_controller = SynchronizationController()
    system_controller = SystemController()
    tenant_controller = TenantController()
    time_controller = TenantController()

    def __init__(self):
        super().__init__()

    # get name of base object
    def get_base_object_name(self) -> str:
        return "Controllers"
    # get type of base object
    def get_base_object_type(self) -> str:
        return "Controllers"
    def initialize_controllers(self) -> None:
        """initialize all controllers and add to all_controllers"""
        logging.debug("Initialization of Controller classes, object_id: " + self.object_id)
        self.all_controllers.append(self.account_controller)
        self.all_controllers.append(self.auth_controller)
        self.all_controllers.append(self.client_controller)
        self.all_controllers.append(self.calendar_controller)
        self.all_controllers.append(self.competency_controller)
        self.all_controllers.append(self.connection_controller)
        self.all_controllers.append(self.event_controller)
        self.all_controllers.append(self.invoice_controller)
        self.all_controllers.append(self.monitor_controller)
        self.all_controllers.append(self.object_controller)
        self.all_controllers.append(self.process_controller)
        self.all_controllers.append(self.project_controller)
        self.all_controllers.append(self.report_controller)
        self.all_controllers.append(self.service_controller)
        self.all_controllers.append(self.storage_controller)
        self.all_controllers.append(self.synchronization_controller)
        self.all_controllers.append(self.system_controller)
        self.all_controllers.append(self.tenant_controller)
        self.all_controllers.append(self.time_controller)

    # handler for closing application
    def close(self) -> None:
        logging.info("Closing controllers, object_id: " + self.object_id)


# all known controllers for HTTP requests/responses
controllers = Controllers()
