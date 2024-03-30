from flask import Flask, jsonify, request, abort, Request, Response

from service.services_auth import *
from service.services_custom import SystemStateService
from service.services_list import service_list_base
from service.services_object import *
from controller.controller_base import RequestSession, ResponseSession


# class with list of services binded to DAOs
class service_list(service_list_base):
    all_services: list[service_base] = []
    # custom services
    login_service = LoginService()
    permission_service = PermissionService()
    key_service = KeyService()
    state_service = SystemStateService()
    def __init__(self):
        super().__init__()
    # get type of base object
    def get_base_object_type(self) -> str:
        return "Services"
    # get name of base object
    def get_base_object_name(self) -> str:
        return "service_list"
    # initialize all services
    def initialize_services(self):
        print("Initializing services after DB connections")
        self.login_service.initialize()
        self.permission_service.initialize()
        self.key_service.initialize()
        self.state_service.initialize()
        self.register_all_services()
        #self.account_division_service_inst.initialize()

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
