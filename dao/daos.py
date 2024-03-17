import dao.dao_connection
from typing import TypeVar, Generic, List, Iterable, Any

from dao.daos_read import *
from dao.daos_full import *
import socket
import os

# DB connections t obe used by DAOs
db_connections = dao.dao_connection.db_connections


class Daos(base_object):
    # auto-generated - Daos - START
    account_division_dao_instance = account_division_full_dao()
    account_group_dao_instance = account_group_full_dao()
    account_instance_dao_instance = account_instance_full_dao()
    account_title_dao_instance = account_title_full_dao()
    account_type_dao_instance = account_type_full_dao()
    auth_identity_dao_instance = auth_identity_full_dao()
    auth_password_dao_instance = auth_password_full_dao()
    auth_permission_dao_instance = auth_permission_full_dao()
    auth_request_dao_instance = auth_request_full_dao()
    auth_role_dao_instance = auth_role_full_dao()
    auth_token_dao_instance = auth_token_full_dao()
    client_instance_dao_instance = client_instance_full_dao()
    client_type_dao_instance = client_type_full_dao()
    country_dao_instance = country_full_dao()
    currency_dao_instance = currency_full_dao()
    entry_final_dao_instance = entry_final_full_dao()
    entry_save_dao_instance = entry_save_full_dao()
    event_channel_dao_instance = event_channel_full_dao()
    event_instance_dao_instance = event_instance_full_dao()
    event_subscription_dao_instance = event_subscription_full_dao()
    invoice_instance_dao_instance = invoice_instance_full_dao()
    notification_instance_dao_instance = notification_instance_full_dao()
    project_budget_dao_instance = project_budget_full_dao()
    project_group_dao_instance = project_group_full_dao()
    project_instance_dao_instance = project_instance_full_dao()
    project_milestone_dao_instance = project_milestone_full_dao()
    system_attribute_dao_instance = system_attribute_full_dao()
    system_change_dao_instance = system_change_full_dao()
    system_database_dao_instance = system_database_full_dao()
    system_exception_dao_instance = system_exception_full_dao()
    system_instance_dao_instance = system_instance_full_dao()
    system_object_dao_instance = system_object_full_dao()
    system_object_type_dao_instance = system_object_type_full_dao()
    system_setting_dao_instance = system_setting_full_dao()
    system_state_dao_instance = system_state_full_dao()
    system_version_dao_instance = system_version_full_dao()
    # auto-generated - Daos - END
    all_daos: dict[str, base_dao] = {}
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
    def register_all_standard_daos(self):
        # auto-generated - DaoRegister - START
        self.all_daos["account_division_dao"] = self.account_division_dao_instance
        self.all_daos["account_group_dao"] = self.account_group_dao_instance
        self.all_daos["account_instance_dao"] = self.account_instance_dao_instance
        self.all_daos["account_title_dao"] = self.account_title_dao_instance
        self.all_daos["account_type_dao"] = self.account_type_dao_instance
        self.all_daos["auth_identity_dao"] = self.auth_identity_dao_instance
        self.all_daos["auth_password_dao"] = self.auth_password_dao_instance
        self.all_daos["auth_permission_dao"] = self.auth_permission_dao_instance
        self.all_daos["auth_request_dao"] = self.auth_request_dao_instance
        self.all_daos["auth_role_dao"] = self.auth_role_dao_instance
        self.all_daos["auth_token_dao"] = self.auth_token_dao_instance
        self.all_daos["client_instance_dao"] = self.client_instance_dao_instance
        self.all_daos["client_type_dao"] = self.client_type_dao_instance
        self.all_daos["country_dao"] = self.country_dao_instance
        self.all_daos["currency_dao"] = self.currency_dao_instance
        self.all_daos["entry_final_dao"] = self.entry_final_dao_instance
        self.all_daos["entry_save_dao"] = self.entry_save_dao_instance
        self.all_daos["event_channel_dao"] = self.event_channel_dao_instance
        self.all_daos["event_instance_dao"] = self.event_instance_dao_instance
        self.all_daos["event_subscription_dao"] = self.event_subscription_dao_instance
        self.all_daos["invoice_instance_dao"] = self.invoice_instance_dao_instance
        self.all_daos["notification_instance_dao"] = self.notification_instance_dao_instance
        self.all_daos["project_budget_dao"] = self.project_budget_dao_instance
        self.all_daos["project_group_dao"] = self.project_group_dao_instance
        self.all_daos["project_instance_dao"] = self.project_instance_dao_instance
        self.all_daos["project_milestone_dao"] = self.project_milestone_dao_instance
        self.all_daos["system_attribute_dao"] = self.system_attribute_dao_instance
        self.all_daos["system_change_dao"] = self.system_change_dao_instance
        self.all_daos["system_database_dao"] = self.system_database_dao_instance
        self.all_daos["system_exception_dao"] = self.system_exception_dao_instance
        self.all_daos["system_instance_dao"] = self.system_instance_dao_instance
        self.all_daos["system_object_dao"] = self.system_object_dao_instance
        self.all_daos["system_object_type_dao"] = self.system_object_type_dao_instance
        self.all_daos["system_setting_dao"] = self.system_setting_dao_instance
        self.all_daos["system_state_dao"] = self.system_state_dao_instance
        self.all_daos["system_version_dao"] = self.system_version_dao_instance
        # auto-generated - DaoRegister - END

    def initialize_daos(self):
        self.system_instance_dto = self.system_instance_dao_instance.insert_and_get(
            system_instance_write_dto(self.system_instance_uid, "1.0.0", self.host_name, self.host_ip, self.local_path, "DEV"),
            "system")
        self.system_database_dto = self.system_database_dao_instance.upsert_row_and_get("main", db_connections.db_url, "", "", "")
        self.settings_by_name = self.system_setting_dao_instance.get_items_active().to_dict_by_setting_name()
        self.register_all_standard_daos()
        print("End of DAOs initialization, system instance: ")
    # handler for closing application
    def close(self):
        print("Closing DAOs")


# instance of Daos with all DAOs instances
daos = Daos()
