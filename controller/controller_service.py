from flask import Flask, jsonify, request, abort, Request, Response

from base.base_objects import objects
from base.cache import cache
from dao.dao_connection import db_connections
from service.services import service_list
from dao.daos_instances import *
from dao.daos import daos
from controller.controller_base import RequestSession, ResponseSession, BaseController


# service controller to
class ServiceController(BaseController):
    #
    def __init__(self):
        super().__init__()
    # get name of base object
    def get_base_object_name(self) -> str:
        return "ServiceController"
    def ping(self, session: RequestSession) -> ResponseSession:
        print("Token")
        return ResponseSession(jsonify({'ping': "pong"}))

    def version(self, session: RequestSession) -> ResponseSession:
        return ResponseSession(jsonify(daos.system_instance_dto.to_read_dict()))

    def dao(self, session: RequestSession) -> ResponseSession:
        return ResponseSession(jsonify(daos.get_base_dict_info()))

    def models(self, session: RequestSession) -> ResponseSession:
        return ResponseSession(jsonify(asdict(db_models)))

    def connections(self, session: RequestSession) -> ResponseSession:
        return ResponseSession(jsonify(db_connections.get_base_dict_info()))

    def objs(self, session: RequestSession) -> ResponseSession:
        return ResponseSession(jsonify(objects.get_base_object_infos()))

    def settings(self, session: RequestSession) -> ResponseSession:
        return ResponseSession(jsonify(daos.settings_by_name))

    def threads(self, session: RequestSession) -> ResponseSession:
        return ResponseSession(jsonify(objects.get_threads_infos()))

    def caches(self, session: RequestSession) -> ResponseSession:
        return ResponseSession(jsonify(cache.get_infos()))

    # defined routes for router
    routes = {
        "ping": ping,
        "version": version,
        "dao": dao,
        "connections": connections,
        "objects": objs,
        "models": models,
        "threads": threads,
        "settings": settings,
        "caches": caches
    }

    def route(self, session: RequestSession) -> ResponseSession:
        print("Route OAuth with URL: " + session.request.url)
        contr_method = self.routes.get(session.method_name)
        # print("Found method" + str(type(contr_method)))
        if contr_method is not None:
            try:
                return contr_method(self, session)
            except:
                #abort(404, )
                return ResponseSession(jsonify({'status': "BAD_REQUEST"}))
        else:
            return ResponseSession(jsonify({'status': "NOT_FOUND"}))
