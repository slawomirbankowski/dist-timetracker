#from __future__ import annotations
from typing import Dict, Callable
import logging
from logging import config
from flask import jsonify, abort, Request, Response
from dao.daos_instances import *
from dao.daos import daos
from service.services import services
from controller.controller_base import RequestSession, ResponseSession, BaseController


# connection controller
class ConnectionController(BaseController):
    #
    def __init__(self):
        super().__init__()
    # get name of base object
    def get_base_object_name(self) -> str:
        return "ConnectionController"

    def info(self, session: RequestSession) -> ResponseSession:
        return ResponseSession.not_implemented(session)

    def create_connection(self, session: RequestSession) -> ResponseSession:
        return ResponseSession.not_implemented(session)

    def list_connections(self, session: RequestSession) -> ResponseSession:
        return ResponseSession.not_implemented(session)

