#from __future__ import annotations
from typing import Dict, Callable
import logging
from logging import config
from flask import jsonify, abort, Request, Response
from dao.daos_instances import *
from dao.daos import daos
from service.services import services
from controller.controller_base import RequestSession, ResponseSession, BaseController


# tenant controller to manage tenants
class TenantController(BaseController):
    #
    def __init__(self):
        super().__init__()
    # get name of base object
    def get_base_object_name(self) -> str:
        return "TenantController"

    def info(self, session: RequestSession) -> ResponseSession:
        return ResponseSession.not_implemented(session)

    def create_tenant(self, session: RequestSession) -> ResponseSession:
        logging.info("create_tenant")
        tenant_data = session.get_body_as_dict()
        tenant_uid = tenant_data.get("tenant_uid", "")
        tenant_name = tenant_data.get("tenant_name", "")
        country_uid = tenant_data.get("country_uid", "")
        tenant_type_uid = tenant_data.get("tenant_type_uid", "")
        tenant_category_uid = tenant_data.get("tenant_category_uid", "")
        tenant_code = tenant_data.get("tenant_code", "")
        tenant_description = tenant_data.get("tenant_description", "")
        start_date = datetime.datetime.now()
        dto = tenant_write_dto(tenant_uid, tenant_uid, country_uid, tenant_type_uid, tenant_category_uid, tenant_code, tenant_description, start_date, None, 1, 0, 0, None, "{}")
        read_dto = daos.tenant_dao_instance.insert_and_get(dto)
        return ResponseSession.ok(session, {"write_dto": dto, "read_dto": read_dto})

    def list_tenants(self, session: RequestSession) -> ResponseSession:
        logging.info("list_tenants")
        tenants: tenant_read_dtos = daos.tenant_dao_instance.select_rows_read_all()
        return ResponseSession.ok(session, {"tenants": tenants.dtos})

    def list_tenants_thin(self, session: RequestSession) -> ResponseSession:
        logging.info("list_tenants_thin")
        tenants = daos.tenant_dao_instance.select_rows_thin_all()
        return ResponseSession.ok(session, {"tenants": tenants.dtos})

    def tenant_dictionaries(self, session: RequestSession) -> ResponseSession:
        logging.info("list_tenants_thin")
        # TODO: return all dictionaries for tenants
        tenants = daos.tenant_dao_instance.select_rows_thin_all()
        return ResponseSession.ok(session, {"tenants": tenants.dtos})

