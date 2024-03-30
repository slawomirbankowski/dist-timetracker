from flask import Flask, jsonify, Request, Response
from dao.daos_instances import *
from dao.daos import daos
from service.services import services
from controller.controller_base import RequestSession, ResponseSession, BaseController


# report controller
class ReportController(BaseController):
    #
    def __init__(self):
        super().__init__()

    # get name of base object
    def get_base_object_name(self) -> str:
        return "ReportController"

    # route in Process controller - select method and run it
    def route(self, session: RequestSession) -> ResponseSession:
        print("Route from Flask: " + session.request.url)
        return ResponseSession(jsonify({'access_token': "123456"}))
