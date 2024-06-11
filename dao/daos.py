import socket
import os
import logging
from logging import config
from typing import TypeVar, Generic, List, Iterable, Any
import dao.dao_connection
from base.base_objects import ThreadWrapper, RequestBase, ResponseBase
from dao.daos_list import DaosList
from dao.daos_read import *
from dao.daos_full import *

# DB connections t obe used by DAOs
db_connections = dao.dao_connection.db_connections


# DAOs
class Daos(DaosList):
    """class to have all DAO objects and basic data initialized in DB"""
    # constant values initialized
    system_instance_uid: str = objects.system_instance_uid
    system_instance_dto: system_instance_read_dto | None
    system_database_dto: system_database_read_dto | None
    settings_by_name: dict[str, str]
    account_skills: account_skill_read_dtos
    account_titles: account_title_read_dtos

    def __init__(self):
        super().__init__()
        # objects.host_name
        #

    def get_dao_for_table(self, table_name: str) -> base_dao | None:
        return self.all_daos.get(table_name + "_dao")
    def get_count_for_table(self, table_name: str) -> int:
        return self.system_instance_dao_instance.count_by_table_all(table_name)
    def get_items_by_table(self, table_name: str) -> list[dict]:
        return self.get_dao_for_table(table_name).select_rows_read_active(1000).to_list_dict()
    def get_items_by_table_uid(self, table_name: str, uid: str) -> dict:
        return self.get_dao_for_table(table_name).select_row_read_by_uid(uid).to_read_dict()
    def insert_row_by_table(self, table_name: str, obj: dict) -> dict:
        #return self.get_dao_for_table(table_name).insert_single()
        return {}

    # get name of base object
    def get_base_object_name(self) -> str:
        return "Daos"
    # get type of base object
    def get_base_object_type(self) -> str:
        return "Daos"
    def get_base_dict_custom_info(self) -> dict[str, any]:
        return {
            "system_instance_uid": objects.system_instance_uid,
            "host_name": objects.host_name,
            "host_ip": objects.host_ip,
            "local_path": objects.local_path,
            "app_version": objects.app_version
        }

    def handle_exception(self, ex: Exception) -> bool:
        self.system_exception_dao_instance.insert_row_random_uid(ex.__cause__, type(ex).__name__, ex.__module__, str(ex.args))
        return True
    def handle_thread(self, th: ThreadWrapper) -> bool:
        self.system_thread_dao_instance.insert_row_random_uid("", th.thread.name, th.thread.native_id, th.object_id, th.ticks_count, th.is_thread_active(), th.sleep_time)
        return True
    def handle_request(self, resp: ResponseBase) -> bool:
        self.system_request_dao_instance.insert_row_random_uid(resp.req_session.request_id, resp.req_session.get_account_uid(), resp.req_session.method_name, resp.req_session.url, -1, "host", 2000, resp.code)
        return True

    def read_settings(self) -> dict[str, str]:
        return self.system_setting_dao_instance.select_rows_read_active().to_dict_by_key_name("system_setting_name", "setting_value")

    def initialize_daos(self) -> None:
        """initialize all DAOs classes and main objects"""
        siw = system_instance_write_dto(objects.system_instance_uid, objects.system_instance_uid, "1.0.0", objects.host_name, objects.host_ip, objects.local_path, "DEV", 0)
        # system_instance_uid: str, system_instance_name: str, system_version_uid: str, host_name: str, host_ip: str, local_path: str, mode_name: str, ticks_count: int, custom_attributes: str = "{}"
        self.system_instance_dto = self.system_instance_dao_instance.insert_and_get(siw, "system")
        #self.system_database_dto = self.system_database_dao_instance.upsert_row_and_get("main", "", db_connections.db_url, "", "", "", objects.system_instance_uid)
        self.settings_by_name = self.read_settings()
        self.register_all_standard_daos()
        # register handlers to
        objects.register_settings(self.settings_by_name)
        objects.register_exception_handler(self.handle_exception)
        objects.register_thread_handler(self.handle_thread)
        objects.register_request_handler(self.handle_request)
        objects.register_roles(self.auth_role_dao_instance.select_rows_read_all())
        logging.debug("End of DAOs initialization, system instance: " + self.system_instance_dto.system_instance_uid)

    def read_dictionaries(self) -> None:
        self.account_skills = self.account_skill_dao_instance.select_rows_read_all()
        self.account_titles = self.account_title_dao_instance.select_rows_read_all()


    # handler for closing application
    def close(self) -> None:
        logging.info("Closing DAOs")


# instance of Daos with all DAOs custom
daos = Daos()
