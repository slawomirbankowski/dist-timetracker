#from __future__ import annotations
from typing import Dict, Callable
import logging
from logging import config
from flask import jsonify, abort, Request, Response
from dao.daos_instances import *
from dao.daos import daos
from service.services import services
from controller.controller_base import RequestSession, ResponseSession, BaseController


# monitor controller
class MonitorController(BaseController):
    #
    def __init__(self):
        super().__init__()
    # get name of base object
    def get_base_object_name(self) -> str:
        return "MonitorController"

    def create_monitor(self, session: RequestSession) -> ResponseSession:
        return ResponseSession.not_implemented(session)

    def list_monitors(self, session: RequestSession) -> ResponseSession:
        return ResponseSession.not_implemented(session)

