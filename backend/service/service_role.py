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
from dto.dtos_read_list import auth_role_read_dtos
from backend.service import service_base, ServiceThreadBase
from backend.dao.daos import daos


class RoleService(ServiceThreadBase):
    all_roles: auth_role_read_dtos
    roles_set: set[str]
    roles_by_parent: dict[str, list[str]]
    roles_by_child: dict[str, list[str]]
    roles_hierarchy: dict[str, list[str]]

    def __init__(self):
        super().__init__()

    # get name of base object
    def get_base_object_name(self) -> str:
        return "RoleService"
    # work in separated thread
    def thread_work(self, tick: int) -> bool:
        return True

    # initialize this service
    def on_initialize(self) -> None:
        logging.info("")
        self.all_roles = daos.auth_role_dao_instance.select_rows_read_active()
        self.roles_set =  self.all_roles.to_set_by_name("auth_role_uid")
        # self.roles_by_parent.add("", "")
        # for role in self.all_roles.dtos:
        #     role.auth_role_uid
        #     role.parent_auth_role_uid
        pass


