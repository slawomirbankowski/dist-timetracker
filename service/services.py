from flask import Flask, jsonify, request, abort, Request, Response

from service.services_auth import *
from service.services_custom import SystemStateService
from service.services_object import *
from controller.controller_base import RequestSession, ResponseSession


# class with list of services binded to DAOs
class service_list(base_object):
    # custom services
    login_service = LoginService()
    permission_service = PermissionService()
    key_service = KeyService()
    state_service = SystemStateService()
    # auto-generated - ServiceList - START
    account_division_service_inst = account_division_service()
    account_group_service_inst = account_group_service()
    account_instance_service_inst = account_instance_service()
    account_title_service_inst = account_title_service()
    account_type_service_inst = account_type_service()
    auth_identity_service_inst = auth_identity_service()
    auth_password_service_inst = auth_password_service()
    auth_permission_service_inst = auth_permission_service()
    auth_request_service_inst = auth_request_service()
    auth_role_service_inst = auth_role_service()
    auth_token_service_inst = auth_token_service()
    client_instance_service_inst = client_instance_service()
    client_type_service_inst = client_type_service()
    country_service_inst = country_service()
    currency_service_inst = currency_service()
    entry_final_service_inst = entry_final_service()
    entry_save_service_inst = entry_save_service()
    event_channel_service_inst = event_channel_service()
    event_instance_service_inst = event_instance_service()
    event_subscription_service_inst = event_subscription_service()
    invoice_instance_service_inst = invoice_instance_service()
    notification_instance_service_inst = notification_instance_service()
    project_budget_service_inst = project_budget_service()
    project_group_service_inst = project_group_service()
    project_instance_service_inst = project_instance_service()
    project_milestone_service_inst = project_milestone_service()
    system_attribute_service_inst = system_attribute_service()
    system_change_service_inst = system_change_service()
    system_database_service_inst = system_database_service()
    system_exception_service_inst = system_exception_service()
    system_instance_service_inst = system_instance_service()
    system_object_service_inst = system_object_service()
    system_object_type_service_inst = system_object_type_service()
    system_setting_service_inst = system_setting_service()
    system_state_service_inst = system_state_service()
    system_version_service_inst = system_version_service()
    # auto-generated - ServiceList - END
    all_services: list[service_base] = []
    def __init__(self):
        super().__init__()
    # get type of base object
    def get_base_object_type(self) -> str:
        return "Services"
    # get name of base object
    def get_base_object_name(self) -> str:
        return "service_list"
    def register_all_services(self):
        # auto-generated - ServiceRegister - START
        self.all_services.append(self.account_division_service_inst)
        self.all_services.append(self.account_group_service_inst)
        self.all_services.append(self.account_instance_service_inst)
        self.all_services.append(self.account_title_service_inst)
        self.all_services.append(self.account_type_service_inst)
        self.all_services.append(self.auth_identity_service_inst)
        self.all_services.append(self.auth_password_service_inst)
        self.all_services.append(self.auth_permission_service_inst)
        self.all_services.append(self.auth_request_service_inst)
        self.all_services.append(self.auth_role_service_inst)
        self.all_services.append(self.auth_token_service_inst)
        self.all_services.append(self.client_instance_service_inst)
        self.all_services.append(self.client_type_service_inst)
        self.all_services.append(self.country_service_inst)
        self.all_services.append(self.currency_service_inst)
        self.all_services.append(self.entry_final_service_inst)
        self.all_services.append(self.entry_save_service_inst)
        self.all_services.append(self.event_channel_service_inst)
        self.all_services.append(self.event_instance_service_inst)
        self.all_services.append(self.event_subscription_service_inst)
        self.all_services.append(self.invoice_instance_service_inst)
        self.all_services.append(self.notification_instance_service_inst)
        self.all_services.append(self.project_budget_service_inst)
        self.all_services.append(self.project_group_service_inst)
        self.all_services.append(self.project_instance_service_inst)
        self.all_services.append(self.project_milestone_service_inst)
        self.all_services.append(self.system_attribute_service_inst)
        self.all_services.append(self.system_change_service_inst)
        self.all_services.append(self.system_database_service_inst)
        self.all_services.append(self.system_exception_service_inst)
        self.all_services.append(self.system_instance_service_inst)
        self.all_services.append(self.system_object_service_inst)
        self.all_services.append(self.system_object_type_service_inst)
        self.all_services.append(self.system_setting_service_inst)
        self.all_services.append(self.system_state_service_inst)
        self.all_services.append(self.system_version_service_inst)
        # auto-generated - ServiceRegister - END

    # initialize all services
    def initialize_services(self):
        print("Initializing services after DB connections")
        self.login_service.initialize()
        self.permission_service.initialize()
        self.key_service.initialize()
        self.state_service.initialize()
        self.register_all_services()

    # handler for closing application
    def close(self):
        print("Closing services")

    # wrap request with session and run controller method
    def with_session(self, req: Request, method_name: str, contr_method):
        print("Creating user session and running controller method for request")
        # decoding request into AppRequest with session, request ID, user, method, token, permissions, ...
        session = RequestSession(req, method_name)
        #session.get_authorization_token()
        #session.get_authorization_method()
        resp = contr_method(session)
        return resp


# initializing singleton to store all services
services = service_list()
