#from __future__ import annotations
from typing import Dict, Callable
import logging
from logging import config
from flask import jsonify, abort, Request, Response
from dao.daos_instances import *
from backend.dao.daos import daos
from backend.service import services
from controller.controller_base import RequestSession, ResponseSession, BaseController


# invoice controller
class InvoiceController(BaseController):
    #
    def __init__(self):
        super().__init__()
    # get name of base object
    def get_base_object_name(self) -> str:
        return "InvoiceController"

    def info(self, session: RequestSession) -> ResponseSession:
        return ResponseSession.not_implemented(session)

    def create_invoice(self, session: RequestSession) -> ResponseSession:
        return ResponseSession.not_implemented(session)

    def list_invoices(self, session: RequestSession) -> ResponseSession:
        return ResponseSession.not_implemented(session)

