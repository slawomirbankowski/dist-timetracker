from service.service_base import service_base
from dao.daos import daos
from dao.daos_full import *

class account_division_service(service_base):
    dao: account_division_full_dao = daos.account_division_dao_instance
    def __init__(self):
        super().__init__()


class account_group_service(service_base):
    dao: account_group_full_dao = daos.account_group_dao_instance
    def __init__(self):
        super().__init__()


class account_instance_service(service_base):
    dao: account_instance_full_dao = daos.account_instance_dao_instance
    def __init__(self):
        super().__init__()


class account_title_service(service_base):
    dao: account_title_full_dao = daos.account_title_dao_instance
    def __init__(self):
        super().__init__()


class account_type_service(service_base):
    dao: account_type_full_dao = daos.account_type_dao_instance
    def __init__(self):
        super().__init__()


class auth_identity_service(service_base):
    dao: auth_identity_full_dao = daos.auth_identity_dao_instance
    def __init__(self):
        super().__init__()


class auth_password_service(service_base):
    dao: auth_password_full_dao = daos.auth_password_dao_instance
    def __init__(self):
        super().__init__()


class auth_permission_service(service_base):
    dao: auth_permission_full_dao = daos.auth_permission_dao_instance
    def __init__(self):
        super().__init__()


class auth_request_service(service_base):
    dao: auth_request_full_dao = daos.auth_request_dao_instance
    def __init__(self):
        super().__init__()


class auth_role_service(service_base):
    dao: auth_role_full_dao = daos.auth_role_dao_instance
    def __init__(self):
        super().__init__()


class auth_token_service(service_base):
    dao: auth_token_full_dao = daos.auth_token_dao_instance
    def __init__(self):
        super().__init__()


class client_instance_service(service_base):
    dao: client_instance_full_dao = daos.client_instance_dao_instance
    def __init__(self):
        super().__init__()


class client_type_service(service_base):
    dao: client_type_full_dao = daos.client_type_dao_instance
    def __init__(self):
        super().__init__()


class country_service(service_base):
    dao: country_full_dao = daos.country_dao_instance
    def __init__(self):
        super().__init__()


class currency_service(service_base):
    dao: currency_full_dao = daos.currency_dao_instance
    def __init__(self):
        super().__init__()


class entry_final_service(service_base):
    dao: entry_final_full_dao = daos.entry_final_dao_instance
    def __init__(self):
        super().__init__()


class entry_save_service(service_base):
    dao: entry_save_full_dao = daos.entry_save_dao_instance
    def __init__(self):
        super().__init__()


class event_channel_service(service_base):
    dao: event_channel_full_dao = daos.event_channel_dao_instance
    def __init__(self):
        super().__init__()


class event_instance_service(service_base):
    dao: event_instance_full_dao = daos.event_instance_dao_instance
    def __init__(self):
        super().__init__()


class event_subscription_service(service_base):
    dao: event_subscription_full_dao = daos.event_subscription_dao_instance
    def __init__(self):
        super().__init__()


class invoice_instance_service(service_base):
    dao: invoice_instance_full_dao = daos.invoice_instance_dao_instance
    def __init__(self):
        super().__init__()


class notification_instance_service(service_base):
    dao: notification_instance_full_dao = daos.notification_instance_dao_instance
    def __init__(self):
        super().__init__()


class project_budget_service(service_base):
    dao: project_budget_full_dao = daos.project_budget_dao_instance
    def __init__(self):
        super().__init__()


class project_group_service(service_base):
    dao: project_group_full_dao = daos.project_group_dao_instance
    def __init__(self):
        super().__init__()


class project_instance_service(service_base):
    dao: project_instance_full_dao = daos.project_instance_dao_instance
    def __init__(self):
        super().__init__()


class project_milestone_service(service_base):
    dao: project_milestone_full_dao = daos.project_milestone_dao_instance
    def __init__(self):
        super().__init__()


class system_attribute_service(service_base):
    dao: system_attribute_full_dao = daos.system_attribute_dao_instance
    def __init__(self):
        super().__init__()


class system_change_service(service_base):
    dao: system_change_full_dao = daos.system_change_dao_instance
    def __init__(self):
        super().__init__()


class system_database_service(service_base):
    dao: system_database_full_dao = daos.system_database_dao_instance
    def __init__(self):
        super().__init__()


class system_exception_service(service_base):
    dao: system_exception_full_dao = daos.system_exception_dao_instance
    def __init__(self):
        super().__init__()


class system_instance_service(service_base):
    dao: system_instance_full_dao = daos.system_instance_dao_instance
    def __init__(self):
        super().__init__()


class system_object_service(service_base):
    dao: system_object_full_dao = daos.system_object_dao_instance
    def __init__(self):
        super().__init__()


class system_object_type_service(service_base):
    dao: system_object_type_full_dao = daos.system_object_type_dao_instance
    def __init__(self):
        super().__init__()


class system_setting_service(service_base):
    dao: system_setting_full_dao = daos.system_setting_dao_instance
    def __init__(self):
        super().__init__()


class system_state_service(service_base):
    dao: system_state_full_dao = daos.system_state_dao_instance
    def __init__(self):
        super().__init__()


class system_version_service(service_base):
    dao: system_version_full_dao = daos.system_version_dao_instance
    def __init__(self):
        super().__init__()

