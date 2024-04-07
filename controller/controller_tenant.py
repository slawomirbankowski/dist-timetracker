#from __future__ import annotations
from typing import Dict, Callable
import logging
from logging import config
from flask import jsonify, abort, Request, Response
from dao.daos_instances import *
from dao.daos import daos
from service.services import services
from controller.controller_base import RequestSession, ResponseSession, BaseController


# account controller to
class TenantController(BaseController):
    #
    def __init__(self):
        super().__init__()
    # get name of base object
    def get_base_object_name(self) -> str:
        return "AccountController"

    def create_tenant(self, session: RequestSession) -> ResponseSession:
        logging.info("get_object_by_id")
        table_name: str = session.get_query_or_body_param("table_name").lower()
        # TODO: NotFound when incorrect table_name
        rows_count = daos.account_group_dao_instance.count_by_table_all(table_name)
        return ResponseSession.ok(session, {"table_name": table_name, "rows_count": rows_count})

    def list_tenants(self, session: RequestSession) -> ResponseSession:
        logging.info("get_object_by_id")
        #
        # session.account_permission.roles
        table_name: str = session.get_query_or_body_param("table_name").lower()
        # TODO: NotFound when incorrect table_name
        rows_count = daos.account_group_dao_instance.count_by_table_all(table_name)

        daos.account_dao_instance.select_rows_read_by_tenant_uid(session.account_session.tenant_uid)

        return ResponseSession.ok(session, {"table_name": table_name, "rows_count": rows_count})

