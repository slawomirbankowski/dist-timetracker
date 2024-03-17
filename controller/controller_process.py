from flask import Flask, jsonify, request, abort, Request, Response
from dao.daos_instances import *
from dao.daos import daos
from service.services import services
from controller.controller_base import RequestSession, ResponseSession, BaseController


# process controller
class ProcessController(BaseController):
    #
    def __init__(self):
        super().__init__()
    # get name of base object
    def get_base_object_name(self) -> str:
        return "ProcessController"
    def check_process(self, session: RequestSession) -> ResponseSession:
        print("Auth")
        return ResponseSession(jsonify({'process': "abc123"}))

    routes = {
        "check_process": check_process
    }

    # route in Process controller - select method and run it
    def route(self, session: RequestSession) -> ResponseSession:
        print("Route OAuth with URL: " + session.request.url)
        contr_method = self.routes.get(session.method_name)
        print("Found method" + str(type(contr_method)))
        if contr_method is not None:
            print("Found method")
            return contr_method(self, session)
        else:
            return ResponseSession(abort(404))
