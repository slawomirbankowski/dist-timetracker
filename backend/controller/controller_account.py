# from __future__ import annotations
from typing import Dict, Callable
import logging
from logging import config
from flask import jsonify, abort, Request, Response
from dao.daos_instances import *
from backend.dao.daos import daos
from backend.service import services
from controller.controller_base import RequestSession, ResponseSession, BaseController


# account controller to
class AccountController(BaseController):
    #
    def __init__(self):
        super().__init__()
    # get name of base object
    def get_base_object_name(self) -> str:
        return "AccountController"

    def create_account(self, session: RequestSession) -> ResponseSession:
        account_uid = session.get_query_or_body_param("account_uid")
        account_name = session.get_query_or_body_param("account_name")
        account_type_uid = session.get_query_or_body_param("account_type_uid", "Test")
        account_title_uid = "DEF"
        account_division_uid = "Default"
        account_group_uid = "Everyone"
        auth_identity_uid = ""
        account_email = ""
        account_display_name = ""
        account_address = ""
        daos.account_dao_instance.insert_row(account_uid, account_name, session.account_session.tenant_uid, account_type_uid,
                                             account_title_uid, account_division_uid, account_group_uid, auth_identity_uid, account_email, account_display_name, account_address, 0, 0)
        return ResponseSession.ok(session, {"table_name": "", "rows_count": 0})

    def list_accounts(self, session: RequestSession) -> ResponseSession:
        #
        # session.account_permission.roles
        table_name: str = session.get_query_or_body_param("table_name").lower()
        # TODO: NotFound when incorrect table_name
        rows_count = daos.account_group_dao_instance.count_by_table_all(table_name)
        objs = daos.account_dao_instance.select_rows_read_by_tenant_uid(session.account_session.tenant_uid)
        return ResponseSession.ok(session, {"table_name": table_name, "objects": objs})

