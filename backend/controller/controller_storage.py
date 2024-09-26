from flask import Flask, jsonify, Request, Response
import logging
from logging import config
from dao.daos_instances import *
from backend.dao.daos import daos
from backend.service import services
from controller.controller_base import RequestSession, ResponseSession, BaseController


# storage controller
class StorageController(BaseController):
    #
    def __init__(self):
        super().__init__()

    # get name of base object
    def get_base_object_name(self) -> str:
        return "StorageController"

    def info(self, session: RequestSession) -> ResponseSession:
        return ResponseSession.not_implemented(session)

