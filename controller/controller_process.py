from flask import Flask, jsonify, request, abort, Request, Response
import logging
from logging import config
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
        logging.debug("Auth")
        return ResponseSession.not_implemented(session)
