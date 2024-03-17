#from __future__ import annotations
from typing import Dict, Callable
from flask import jsonify, abort, Request, Response
from dao.daos_instances import *
from dao.daos import daos
from service.services import services
from controller.controller_base import RequestSession, ResponseSession, BaseController


# object controller to
class ObjectController(BaseController):
    #
    def __init__(self):
        super().__init__()
    # get name of base object
    def get_base_object_name(self) -> str:
        return "ObjectController"
    def get_object_by_id(self, session: RequestSession) -> ResponseSession:
        print("get_object_by_id")
        # TODO: get any object by table name and UID
        daos.account_group_dao_instance.count_by_table_all("")
        return None

    def get_object_count(self, session: RequestSession) -> ResponseSession:
        print("get_object_by_id")
        # TODO: count of rows by table name
        daos.account_group_dao_instance.count_by_table_all("")
        return None

    def auth(self):
        print("Auth")
        # : dict[str, any]

    routes: dict[str, any] = { # Callable[[ObjectController, Request], Response]
        "get_object_by_id": get_object_by_id,
        "get_object_count": get_object_count
    }


    def route(self, session: RequestSession) -> ResponseSession:
        #session.request.method
        print("Route with URL: " + session.request.url)
        contr_method = self.routes.get(session.request.method + ":/" + session.method_name)
        #print("Found method" + str(type(contr_method)))
        if contr_method is not None:
            return contr_method(self, session)
        else:
            return ResponseSession(abort(404))
