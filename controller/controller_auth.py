import datetime
import json
import logging
from dataclasses import asdict
from logging import config
from flask import Flask, jsonify, abort, Request, Response

from base.cache import cache
from dao.daos import daos
from dto.dtos import base_dto
from service.services import services
from controller.controller_base import RequestSession, ResponseSession, BaseController
import hashlib


# Auth controller
class AuthController(BaseController):
    #
    def __init__(self):
        super().__init__()

    # get name of base object
    def get_base_object_name(self) -> str:
        return "AuthController"

    def info(self, session: RequestSession) -> ResponseSession:
        return ResponseSession.not_implemented(session)

    def get_auth_method(self, session: RequestSession) -> ResponseSession:
        username = session.get_query_or_body_param("username")
        #cache.with_cache("get_auth_method" + username, lambda x: {
        #})
        account_dto = daos.account_dao_instance.get_account_by_name(username)
        if account_dto is None:
            return ResponseSession.not_found(session)
        else:
            ident_dto = daos.auth_identity_dao_instance.select_row_read_by_uid(account_dto.auth_identity_uid)
            ident = {
                "account_uid": account_dto.account_uid,
                "auth_identity_name": ident_dto.auth_identity_name,
                "auth_identity_uid": ident_dto.auth_identity_uid,
                "auth_identity_url": "http://localhost/auth/login"
            }
            return ResponseSession.ok(session, ident)

    def token(self, session: RequestSession) -> ResponseSession:
        # session.request.data
        grant_type = session.get_query_param("grant_type")
        username = session.get_query_or_body_param("username")
        password = session.get_query_or_body_param("password")
        logging.debug("Token request for grant_type: " + grant_type + ", username: " + username)
        return services.login_service.token(session, grant_type, username, password)

    def logout(self, session: RequestSession) -> ResponseSession:
        """logout - destroy session"""
        # session.request.data
        return services.login_service.logout(session)

    def set_password(self, session: RequestSession) -> ResponseSession:
        account_uid = session.get_query_param("username")
        password = session.get_query_param("password")
        return services.login_service.set_password(session, account_uid, password)

    def my_set_password(self, session: RequestSession) -> ResponseSession:
        password = session.get_query_param("password")
        return services.login_service.set_password(session, session.account_session.account_uid, password)

    def request_reset_password(self, session: RequestSession) -> ResponseSession:
        account_uid = session.get_query_param("username")
        return services.login_service.request_reset_password(session, account_uid)

    def check_password(self, session: RequestSession) -> ResponseSession:
        account_uid = session.get_query_param("username")
        password = session.get_query_param("password")
        return services.login_service.check_password(session, account_uid, password)

    def produce_hash(self, session: RequestSession) -> ResponseSession:
        password = session.get_query_param("password")
        return services.login_service.produce_hash(session, password)

    def myself(self, session: RequestSession) -> ResponseSession:
        #session.account_permission
        return ResponseSession.ok(session, session.to_myself_dict())

    def permission_add(self, session: RequestSession) -> ResponseSession:
        return ResponseSession.not_implemented(session)

    def userinfo(self, session: RequestSession) -> ResponseSession:
        return self.myself(session)

    def roles_list(self, session: RequestSession) -> ResponseSession:
        roles = daos.auth_role_dao_instance.select_rows_write_active()
        return ResponseSession.ok(session, {"roles": roles.dtos})

    def roles_list_thin(self, session: RequestSession) -> ResponseSession:
        daos.auth_role_dao_instance.select_rows_write_active()
        roles = daos.auth_role_dao_instance.select_rows_read_active().to_list_by_name("auth_role_uid")
        return ResponseSession.ok(session, {"roles": roles})

    def roles_hierarchy(self, session: RequestSession) -> ResponseSession:
        #
        #
        return ResponseSession.ok(session, {"roles": services.role_service.all_roles.dtos})



