import logging

from flask import Flask, jsonify, request, abort, Request, Response
from typing import Dict, Callable

from base.base_objects import AccountPermissionsBase, AccountSessionBase
from service.services_auth import *
from service.services_custom import SystemStateService
from service.service_base_list import service_list_base
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
    def initialize_services(self) -> None:
        logging.debug("Initializing services after DB connections")
        self.login_service.initialize()
        self.permission_service.initialize()
        self.key_service.initialize()
        self.state_service.initialize()
        self.register_all_services()

    # handler for closing application
    def close(self) -> None:
        logging.info("Closing services")

    def get_permissions_by_account(self, account_uid: str) -> AccountPermissionsBase:
        perm_set = AccountPermissionsBase(account_uid)
        return perm_set

    def read_account_permission(self, account_session: AccountSessionBase) -> AccountPermissionsBase:
        account_permission = objects.get_account_permission_by_account(account_session.account_uid)
        if account_permission is None:
            logging.info("Reading permissions for account: " + account_session.account_uid)
            account_dto = daos.account_dao_instance.select_row_read_by_uid(account_session.account_uid)
            tenant_dto = daos.tenant_dao_instance.select_row_read_by_uid(account_session.tenant_uid)
            perms = daos.auth_permission_dao_instance.select_rows_read_by_account_uid(account_session.account_uid)
            # perms.dtos
            roles = perms.filter(lambda dto: dto.is_active == 1).map_to_string(lambda dto: dto.auth_role_uid)
            account_permission = AccountPermissionsBase(account_session.account_uid, account_dto, tenant_dto, set(roles))
        else:
            logging.info("Got permissions in memory for account: " + account_session.account_uid)
        return account_permission

    def create_session_from_request(self, req: Request, controller_name: str, method_name: str) -> RequestSession:
        logging.debug("Creating user session and running controller method for request")
        # decoding request into AppRequest with session, request ID, user, method, token, permissions, ...
        session = RequestSession(req, controller_name, method_name)
        token = session.get_authorization_token()
        logging.info("!!!!!!!!! Searching for TOKEN: " + token)
        account_session: AccountSessionBase | None = objects.get_account_session_by_token(token)
        if account_session is None:
            logging.debug("No TOKEN in MEMORY")
            if token == "":
                logging.info("EMPTY TOKEN")
            else:
                auth_token_dto = daos.auth_token_dao_instance.select_row_read_by_uid(token)
                if auth_token_dto is not None:
                    logging.debug("Read account session with token from database, account: " + auth_token_dto.account_uid)
                    account_session = objects.create_user_session(auth_token_dto.tenant_uid, auth_token_dto.account_uid,
                                                                  auth_token_dto.auth_token_uid, auth_token_dto.token_salt,
                                                                  auth_token_dto.token_hash, auth_token_dto.valid_till_date)
                else:
                    logging.info("No token found in DB")
        else:
            logging.debug("Found active account session in memory: " + account_session.account_uid)
        session.set_account_session(account_session)
        if account_session is not None:
            permission_session = self.read_account_permission(account_session)
            session.set_account_permission(permission_session)
            logging.info("GOT FULL SESSION WITH PERMISSIONS !!!!! account: " + account_session.account_uid + ", tenant: " + permission_session.tenant_dto.tenant_uid)
        return session


# initializing singleton to store all services
services = service_list()
