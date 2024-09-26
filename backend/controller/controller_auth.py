import datetime
import json
import logging
from dataclasses import asdict
from logging import config
from flask import Flask, jsonify, abort, Request, Response

from base.base_objects import objects
from base.cache import cache
from dao.daos import daos
from dto.dtos import base_dto
from dto.dtos_read_list import auth_token_read_dtos
from service import services
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
        """get authentication method for given user/account"""
        username = session.get_query_or_body_param("username")
        #cache.with_cache("get_auth_method" + username, lambda x: {
        #})
        account_dto = daos.account_dao_instance.get_account_by_name(username)
        ident_dto = None
        if account_dto is None:
            ident_dto = daos.auth_identity_dao_instance.select_row_read_by_uid("Internal")
        else:
            ident_dto = daos.auth_identity_dao_instance.select_row_read_by_uid(account_dto.auth_identity_uid)
        ident = {
            "auth_identity_name": ident_dto.auth_identity_name,
            "auth_identity_uid": ident_dto.auth_identity_uid,
            "auth_identity_url": f"{objects.app_base_url}/auth/login"
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
        return services.login_service.logout(session)

    def set_password(self, session: RequestSession) -> ResponseSession:
        account_uid = session.get_query_param("username")
        password = session.get_query_param("password")
        return services.login_service.set_password(session, account_uid, password)

    def my_set_password(self, session: RequestSession) -> ResponseSession:
        password = session.get_query_param("password")
        password = session.get_query_param("password")
        return services.login_service.set_password(session, session.account_session.account_uid, password)

    def change_password(self, session: RequestSession) -> ResponseSession:
        current_password = session.get_query_param("current_password")
        new_password = session.get_query_param("new_password")
        return services.login_service.change_password(session, session.account_session.account_uid, current_password, new_password)

    def request_password(self, session: RequestSession) -> ResponseSession:
        account_uid = session.get_query_or_body_param("username")
        return services.login_service.request_password(session, account_uid)

    def reset_check(self, session: RequestSession) -> ResponseSession:
        account_uid = session.get_query_or_body_param("username")
        reset_guid = session.get_query_or_body_param("reset_guid")
        return services.login_service.reset_check(session, account_uid, reset_guid)

    def reset_password(self, session: RequestSession) -> ResponseSession:
        account_uid = session.get_query_or_body_param("username")
        reset_guid = session.get_query_or_body_param("reset_guid")
        return services.login_service.reset_password(session, account_uid, reset_guid)

    def check_password(self, session: RequestSession) -> ResponseSession:
        account_uid = session.get_query_param("username")
        password = session.get_query_param("password")
        return services.login_service.check_password(session, account_uid, password)

    def produce_hash(self, session: RequestSession) -> ResponseSession:
        password = session.get_query_param("password")
        return services.login_service.produce_hash(session, password)

    def produce_passwords_tab(self, session: RequestSession) -> ResponseSession:
        return services.login_service.produce_passwords_tab(session)

    def me(self, session: RequestSession) -> ResponseSession:
        return ResponseSession.ok(session, session.to_me_dict())

    def myself(self, session: RequestSession) -> ResponseSession:
        #session.account_permission
        return ResponseSession.ok(session, session.to_myself_dict())

    def permission_add(self, session: RequestSession) -> ResponseSession:
        return ResponseSession.not_implemented(session)

    def userinfo(self, session: RequestSession) -> ResponseSession:
        return self.myself(session)

    def reload_session(self, session: RequestSession) -> ResponseSession:
        objects.destroy_session(session.account_session)
        return self.myself(session)

    def sessions_list(self, session: RequestSession) -> ResponseSession:
        all_sessions: list[dict] = []
        for session_key in objects.account_sessions:
            all_sessions.append(objects.account_sessions[session_key].to_dict())
        return ResponseSession.ok(session, {"sessions": all_sessions, "sessions_count": len(all_sessions)})

    def token_list_to_sessions(self, session: RequestSession, tokens: auth_token_read_dtos):
        all_sessions: list[dict] = []
        # sessions.map_to_string(lambda x: x.)
        for session_dto in tokens.dtos:
            all_sessions.append({"account_uid": session_dto.account_uid, "session_id": session_dto.auth_token_name, "created_date": str(session_dto.created_date), "valid_till_date": str(session_dto.valid_till_date)})
        return ResponseSession.ok(session, {"sessions": all_sessions, "sessions_count": len(all_sessions)})

    def sessions_db_list(self, session: RequestSession) -> ResponseSession:
        sessions: auth_token_read_dtos = daos.auth_token_dao_instance.select_rows_read_active()
        return self.token_list_to_sessions(session, sessions)

    def sessions_db_latest(self, session: RequestSession) -> ResponseSession:
        sessions: auth_token_read_dtos = daos.auth_token_dao_instance.select_rows_read_all_latest()
        return self.token_list_to_sessions(session, sessions)

    def sessions_by_account(self, session: RequestSession) -> ResponseSession:
        account_uid: str = session.get_query_param("account_uid", "")
        sessions: auth_token_read_dtos = daos.auth_token_dao_instance.select_rows_read_by_account_uid(account_uid)
        return self.token_list_to_sessions(session, sessions)

    def roles_list(self, session: RequestSession) -> ResponseSession:
        roles_dtos = daos.auth_role_dao_instance.select_rows_write_active()
        roles_list = daos.auth_role_dao_instance.select_rows_read_active().to_list_by_name("auth_role_uid")
        hier = objects.role_hierarchy.to_hierarchy()
        list_info = objects.role_hierarchy.to_list_info()
        return ResponseSession.ok(session, {
            "root": objects.role_hierarchy.root.role.auth_role_uid,
            "roles_list": roles_list,
            "roles": roles_dtos.dtos,
            "hierarchy": hier,
            "info": list_info
        })

    def roles_info(self, session: RequestSession) -> ResponseSession:
        roles = daos.auth_role_dao_instance.select_rows_write_active()
        return ResponseSession.ok(session, {"roles": roles.dtos})

    def roles_list_thin(self, session: RequestSession) -> ResponseSession:
        daos.auth_role_dao_instance.select_rows_write_active()
        roles = daos.auth_role_dao_instance.select_rows_read_active().to_list_by_name("auth_role_uid")
        return ResponseSession.ok(session, {"roles": roles})

    def roles_hierarchy(self, session: RequestSession) -> ResponseSession:
        return ResponseSession.ok(session, objects.role_hierarchy.to_hierarchy())

    def password_reset_request(self, session: RequestSession) -> ResponseSession:
        account_uid: str = session.get_query_param("account_uid", "")
        account_dto = daos.account_dao_instance.get_account_by_name(account_uid)

        ResponseSession.ok(session, "")
        sessions: auth_token_read_dtos = daos.auth_token_dao_instance.select_rows_read_by_account_uid(account_uid)
        return self.token_list_to_sessions(session, sessions)

    def menu_for_user(self, session: RequestSession) -> ResponseSession:
        md = objects.menu.get_menu_as_dictionary_by_session(session.account_permission)
        return ResponseSession.ok(session, md)

    def menu_full(self, session: RequestSession) -> ResponseSession:
        md = objects.menu.get_menu_as_dictionary_by_session(session.account_permission)
        return ResponseSession.ok(session, md)
