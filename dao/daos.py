import dao.dao_connection
from typing import TypeVar, Generic, List, Iterable, Any

from dao.daos_list import DaosList
from dao.daos_read import *
from dao.daos_full import *
import socket
import os

# DB connections t obe used by DAOs
db_connections = dao.dao_connection.db_connections


# DAOs
class Daos(DaosList):
    # constant values initialized
    system_instance_uid: str = base_dto.get_random_uid_with_name("SI")
    host_name: str = socket.gethostname()
    host_ip: str = socket.gethostname()
    local_path = os.path.dirname(os.path.realpath(__file__))
    app_version = "1.0.0"
    system_instance_dto: system_instance_read_dto | None
    system_database_dto: system_database_read_dto | None
    settings_by_name: dict[str, system_setting_read_dto]
    def __init__(self):
        super().__init__()

    # get name of base object
    def get_base_object_name(self) -> str:
        return "Daos"
    # get type of base object
    def get_base_object_type(self) -> str:
        return "Daos"
    def get_base_dict_custom_info(self) -> dict[str, any]:
        return {
            "system_instance_uid": self.system_instance_uid,
            "host_name": self.host_name,
            "host_ip": self.host_ip,
            "local_path": self.local_path,
            "app_version": self.app_version
        }

    def initialize_daos(self):
        siw = system_instance_write_dto(self.system_instance_uid, self.system_instance_uid, "1.0.0", self.host_name, self.host_ip, self.local_path, "DEV", 0)
        # system_instance_uid: str, system_instance_name: str, system_version_uid: str, host_name: str, host_ip: str, local_path: str, mode_name: str, ticks_count: int, custom_attributes: str = "{}"
        self.system_instance_dto = self.system_instance_dao_instance.insert_and_get(siw, "system")
        self.system_database_dto = self.system_database_dao_instance.upsert_row_and_get("main", "", db_connections.db_url, "", "", "", objects.system_instance_uid)
        #elf.settings_by_name = self.system_setting_dao_instance.get_items_active().to_dict_by_setting_name()
        self.register_all_standard_daos()
        print("End of DAOs initialization, system instance: ")
    # handler for closing application
    def close(self):
        print("Closing DAOs")


# instance of Daos with all DAOs instances
daos = Daos()
