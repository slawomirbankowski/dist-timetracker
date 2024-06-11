#from __future__ import annotations
from typing import Dict, Callable
import logging
from logging import config
from flask import jsonify, abort, Request, Response
from dao.daos_instances import *
from dao.daos import daos
from service.services import services
from controller.controller_base import RequestSession, ResponseSession, BaseController


# object controller to table endpoints
class ObjectController(BaseController):
    #
    def __init__(self):
        super().__init__()
    # get name of base object
    def get_base_object_name(self) -> str:
        return "ObjectController"

    def info(self, session: RequestSession) -> ResponseSession:

        return ResponseSession.not_implemented(session)

    def get_object_count(self, session: RequestSession) -> ResponseSession:
        logging.info("get_object_by_id")
        table_name: str = session.get_query_or_body_param("table_name").lower()
        # TODO: NotFound when incorrect table_name
        rows_count = daos.account_group_dao_instance.count_by_table_all(table_name)
        return ResponseSession.ok(session, {"table_name": table_name, "rows_count": rows_count})

    def get_object_by_uid(self, session: RequestSession) -> ResponseSession:
        logging.info("get_object_by_id")
        table_name: str = session.get_query_or_body_param("table_name")
        uid: str = session.get_query_or_body_param("uid")
        # TODO: get any object by table name and UID
        dao = daos.get_dao_for_table(table_name)
        obj = dao.select_row_read_by_uid(uid)
        if obj is None:
            logging.info("Non existing object for UID: " + uid)
            return ResponseSession.not_found(session)
        else:
            logging.info("Got object for UID, obj: " + str(type(obj)))
            return ResponseSession.ok(session, obj.to_read_dict())

    def get_objects_list(self, session: RequestSession) -> ResponseSession:
        # TODO: get any object by table name and UID
        table_name: str = session.get_query_or_body_param("table_name")
        objs = daos.get_dao_for_table(table_name).select_rows_read_active(100).to_list_dict()
        return ResponseSession.ok(session, {"objects": objs})
