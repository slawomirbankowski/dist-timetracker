import dao.dao_connection
from typing import TypeVar, Generic, List, Iterable
from dao.dao_base import base_dao
from dao.daos_read import *
from dto.dtos_models import db_models
db_connections = dao.dao_connection.db_connections


class account_division_full_dao(account_division_dao):
    def __init__(self):
        super().__init__()


class account_group_full_dao(account_group_dao):
    def __init__(self):
        super().__init__()


class account_instance_full_dao(account_instance_dao):
    def __init__(self):
        super().__init__()
    def get_account_by_name(self, username: str) -> account_instance_read_dto | None:
        return self.get_item_dto_first("select * from account_instance where account_instance_uid=%s or account_name=%s and account_email=%s order by created_date desc limit 1", [username, username, username])

class account_title_full_dao(account_title_dao):
    def __init__(self):
        super().__init__()


class account_type_full_dao(account_type_dao):
    def __init__(self):
        super().__init__()


class auth_identity_full_dao(auth_identity_dao):
    def __init__(self):
        super().__init__()


class auth_password_full_dao(auth_password_dao):
    def __init__(self):
        super().__init__()
    def check_password(self, username: str, password_hash: str) -> bool:
        return True

class auth_permission_full_dao(auth_permission_dao):
    def __init__(self):
        super().__init__()


class auth_request_full_dao(auth_request_dao):
    def __init__(self):
        super().__init__()


class auth_role_full_dao(auth_role_dao):
    def __init__(self):
        super().__init__()


class auth_token_full_dao(auth_token_dao):
    def __init__(self):
        super().__init__()


class client_instance_full_dao(client_instance_dao):
    def __init__(self):
        super().__init__()


class client_type_full_dao(client_type_dao):
    def __init__(self):
        super().__init__()


class country_full_dao(country_dao):
    def __init__(self):
        super().__init__()


class currency_full_dao(currency_dao):
    def __init__(self):
        super().__init__()


class entry_final_full_dao(entry_final_dao):
    def __init__(self):
        super().__init__()


class entry_save_full_dao(entry_save_dao):
    def __init__(self):
        super().__init__()


class event_channel_full_dao(event_channel_dao):
    def __init__(self):
        super().__init__()


class event_instance_full_dao(event_instance_dao):
    def __init__(self):
        super().__init__()


class event_subscription_full_dao(event_subscription_dao):
    def __init__(self):
        super().__init__()


class invoice_instance_full_dao(invoice_instance_dao):
    def __init__(self):
        super().__init__()


class notification_instance_full_dao(notification_instance_dao):
    def __init__(self):
        super().__init__()


class project_budget_full_dao(project_budget_dao):
    def __init__(self):
        super().__init__()


class project_group_full_dao(project_group_dao):
    def __init__(self):
        super().__init__()


class project_instance_full_dao(project_instance_dao):
    def __init__(self):
        super().__init__()


class project_milestone_full_dao(project_milestone_dao):
    def __init__(self):
        super().__init__()


class system_attribute_full_dao(system_attribute_dao):
    def __init__(self):
        super().__init__()


class system_change_full_dao(system_change_dao):
    def __init__(self):
        super().__init__()


class system_database_full_dao(system_database_dao):
    def __init__(self):
        super().__init__()


class system_exception_full_dao(system_exception_dao):
    def __init__(self):
        super().__init__()


class system_instance_full_dao(system_instance_dao):
    def __init__(self):
        super().__init__()

class system_object_full_dao(system_object_dao):
    def __init__(self):
        super().__init__()


class system_object_type_full_dao(system_object_type_dao):
    def __init__(self):
        super().__init__()


class system_setting_full_dao(system_setting_dao):
    def __init__(self):
        super().__init__()
    def get_settings_global(self) -> list[system_setting_read_dto]:
        return self.get_items("select * from system_setting where account_instance_uid is null")


class system_state_full_dao(system_state_dao):
    def __init__(self):
        super().__init__()


class system_version_full_dao(system_version_dao):
    def __init__(self):
        super().__init__()
