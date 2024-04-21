from flask import Flask, jsonify, request, abort, Request, Response
import logging
from logging import config
from base.base_objects import objects
from base.cache import cache
from dao.dao_connection import db_connections
from service.services import service_list
from dao.daos_instances import *
from dao.daos import daos
from controller.controller_base import RequestSession, ResponseSession, BaseController


# service controller to manage internal endpoints like ping, version
class ServiceController(BaseController):
    #
    def __init__(self):
        super().__init__()
    # get name of base object
    def get_base_object_name(self) -> str:
        return "ServiceController"

    def info(self, session: RequestSession) -> ResponseSession:
        return ResponseSession.not_implemented(session)

    def ping(self, session: RequestSession) -> ResponseSession:
        logging.info("Token")
        return ResponseSession.ok(session, {'ping': "pong"})

    def version(self, session: RequestSession) -> ResponseSession:
        ver = {
            "system_instance_uid": daos.system_instance_dto.system_instance_uid,
            "system_instance_name": daos.system_instance_dto.system_instance_name,
            "system_version_uid": daos.system_instance_dto.system_version_uid,
            "object_manager_uid": objects.object_uid,
            "created_date": str(daos.system_instance_dto.created_date),
            "last_updated_date": str(daos.system_instance_dto.last_updated_date)
        }
        return ResponseSession.ok(session, ver)

    def dao(self, session: RequestSession) -> ResponseSession:
        return ResponseSession.ok(session, daos.get_base_dict_info())

    def models(self, session: RequestSession) -> ResponseSession:
        models = {
            "models": db_models.all_models.values()
        }
        return ResponseSession.ok(session, models)

    def connections(self, session: RequestSession) -> ResponseSession:
        return ResponseSession.ok(session, db_connections.get_base_dict_info())

    def objs(self, session: RequestSession) -> ResponseSession:
        return ResponseSession.ok(session, objects.get_base_object_infos())

    def settings(self, session: RequestSession) -> ResponseSession:
        return ResponseSession.ok(session, daos.settings_by_name)

    def threads(self, session: RequestSession) -> ResponseSession:
        return ResponseSession.ok(session, objects.get_threads_infos())

    def caches(self, session: RequestSession) -> ResponseSession:
        return ResponseSession.ok(session, cache.get_infos())

