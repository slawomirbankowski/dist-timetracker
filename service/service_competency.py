import logging
from logging import config
import hashlib
import datetime
from flask import jsonify

from base.base_objects import objects
from base.base_utils import get_random_uid
from controller.controller_base import ResponseSession, RequestSession
from dto.dtos import base_dto
from dto.dtos_read import auth_password_read_dto, account_read_dto
from service.services_base import service_base, service_thread_base
from dao.daos import daos


class CompetencyService(service_thread_base):
    def __init__(self):
        super().__init__()
    # get name of base object
    def get_base_object_name(self) -> str:
        return "CompetencyService"
    # work in separated thread
    def thread_work(self, tick: int) -> bool:
        return True
