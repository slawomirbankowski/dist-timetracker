import datetime
from datetime import datetime
from abc import abstractmethod
from dataclasses import dataclass
from dto.dtos import *
from dto.dtos_write import *


@dataclass(frozen=False)
class account_division_thin_dto(base_dto):
    account_division_uid: str
    row_guid: str
    is_active: int
    def __init__(self, account_division_uid: str , row_guid: str , is_active: int):
        self.account_division_uid = account_division_uid
        self.row_guid = row_guid
        self.is_active = is_active


@dataclass(frozen=False)
class account_group_thin_dto(base_dto):
    account_group_uid: str
    row_guid: str
    is_active: int
    def __init__(self, account_group_uid: str , row_guid: str , is_active: int):
        self.account_group_uid = account_group_uid
        self.row_guid = row_guid
        self.is_active = is_active


@dataclass(frozen=False)
class account_instance_thin_dto(base_dto):
    account_instance_uid: str
    row_guid: str
    is_active: int
    def __init__(self, account_instance_uid: str , row_guid: str , is_active: int):
        self.account_instance_uid = account_instance_uid
        self.row_guid = row_guid
        self.is_active = is_active


@dataclass(frozen=False)
class account_title_thin_dto(base_dto):
    account_title_uid: str
    row_guid: str
    is_active: int
    def __init__(self, account_title_uid: str , row_guid: str , is_active: int):
        self.account_title_uid = account_title_uid
        self.row_guid = row_guid
        self.is_active = is_active


@dataclass(frozen=False)
class auth_identity_thin_dto(base_dto):
    auth_identity_uid: str
    row_guid: str
    is_active: int
    def __init__(self, auth_identity_uid: str , row_guid: str , is_active: int):
        self.auth_identity_uid = auth_identity_uid
        self.row_guid = row_guid
        self.is_active = is_active


@dataclass(frozen=False)
class auth_password_thin_dto(base_dto):
    auth_password_uid: str
    row_guid: str
    is_active: int
    def __init__(self, auth_password_uid: str , row_guid: str , is_active: int):
        self.auth_password_uid = auth_password_uid
        self.row_guid = row_guid
        self.is_active = is_active


@dataclass(frozen=False)
class auth_permission_thin_dto(base_dto):
    auth_permission_uid: str
    row_guid: str
    is_active: int
    def __init__(self, auth_permission_uid: str , row_guid: str , is_active: int):
        self.auth_permission_uid = auth_permission_uid
        self.row_guid = row_guid
        self.is_active = is_active


@dataclass(frozen=False)
class auth_request_thin_dto(base_dto):
    auth_request_uid: str
    row_guid: str
    is_active: int
    def __init__(self, auth_request_uid: str , row_guid: str , is_active: int):
        self.auth_request_uid = auth_request_uid
        self.row_guid = row_guid
        self.is_active = is_active


@dataclass(frozen=False)
class auth_role_thin_dto(base_dto):
    auth_role_uid: str
    row_guid: str
    is_active: int
    def __init__(self, auth_role_uid: str , row_guid: str , is_active: int):
        self.auth_role_uid = auth_role_uid
        self.row_guid = row_guid
        self.is_active = is_active


@dataclass(frozen=False)
class auth_token_thin_dto(base_dto):
    auth_token_uid: str
    row_guid: str
    is_active: int
    def __init__(self, auth_token_uid: str , row_guid: str , is_active: int):
        self.auth_token_uid = auth_token_uid
        self.row_guid = row_guid
        self.is_active = is_active


@dataclass(frozen=False)
class client_instance_thin_dto(base_dto):
    client_instance_uid: str
    row_guid: str
    is_active: int
    def __init__(self, client_instance_uid: str , row_guid: str , is_active: int):
        self.client_instance_uid = client_instance_uid
        self.row_guid = row_guid
        self.is_active = is_active


@dataclass(frozen=False)
class country_thin_dto(base_dto):
    country_uid: str
    row_guid: str
    is_active: int
    def __init__(self, country_uid: str , row_guid: str , is_active: int):
        self.country_uid = country_uid
        self.row_guid = row_guid
        self.is_active = is_active


@dataclass(frozen=False)
class currency_thin_dto(base_dto):
    currency_uid: str
    row_guid: str
    is_active: int
    def __init__(self, currency_uid: str , row_guid: str , is_active: int):
        self.currency_uid = currency_uid
        self.row_guid = row_guid
        self.is_active = is_active


@dataclass(frozen=False)
class entry_final_thin_dto(base_dto):
    entry_final_uid: str
    row_guid: str
    is_active: int
    def __init__(self, entry_final_uid: str , row_guid: str , is_active: int):
        self.entry_final_uid = entry_final_uid
        self.row_guid = row_guid
        self.is_active = is_active


@dataclass(frozen=False)
class entry_save_thin_dto(base_dto):
    entry_save_uid: str
    row_guid: str
    is_active: int
    def __init__(self, entry_save_uid: str , row_guid: str , is_active: int):
        self.entry_save_uid = entry_save_uid
        self.row_guid = row_guid
        self.is_active = is_active


@dataclass(frozen=False)
class event_channel_thin_dto(base_dto):
    event_channel_uid: str
    row_guid: str
    is_active: int
    def __init__(self, event_channel_uid: str , row_guid: str , is_active: int):
        self.event_channel_uid = event_channel_uid
        self.row_guid = row_guid
        self.is_active = is_active


@dataclass(frozen=False)
class event_instance_thin_dto(base_dto):
    event_instance_uid: str
    row_guid: str
    is_active: int
    def __init__(self, event_instance_uid: str , row_guid: str , is_active: int):
        self.event_instance_uid = event_instance_uid
        self.row_guid = row_guid
        self.is_active = is_active


@dataclass(frozen=False)
class event_subscription_thin_dto(base_dto):
    event_subscription_uid: str
    row_guid: str
    is_active: int
    def __init__(self, event_subscription_uid: str , row_guid: str , is_active: int):
        self.event_subscription_uid = event_subscription_uid
        self.row_guid = row_guid
        self.is_active = is_active


@dataclass(frozen=False)
class invoice_instance_thin_dto(base_dto):
    invoice_instance_uid: str
    row_guid: str
    is_active: int
    def __init__(self, invoice_instance_uid: str , row_guid: str , is_active: int):
        self.invoice_instance_uid = invoice_instance_uid
        self.row_guid = row_guid
        self.is_active = is_active


@dataclass(frozen=False)
class notification_instance_thin_dto(base_dto):
    notification_instance_uid: str
    row_guid: str
    is_active: int
    def __init__(self, notification_instance_uid: str , row_guid: str , is_active: int):
        self.notification_instance_uid = notification_instance_uid
        self.row_guid = row_guid
        self.is_active = is_active


@dataclass(frozen=False)
class project_budget_thin_dto(base_dto):
    project_budget_uid: str
    row_guid: str
    is_active: int
    def __init__(self, project_budget_uid: str , row_guid: str , is_active: int):
        self.project_budget_uid = project_budget_uid
        self.row_guid = row_guid
        self.is_active = is_active


@dataclass(frozen=False)
class project_group_thin_dto(base_dto):
    project_group_uid: str
    row_guid: str
    is_active: int
    def __init__(self, project_group_uid: str , row_guid: str , is_active: int):
        self.project_group_uid = project_group_uid
        self.row_guid = row_guid
        self.is_active = is_active


@dataclass(frozen=False)
class project_instance_thin_dto(base_dto):
    project_instance_uid: str
    row_guid: str
    is_active: int
    def __init__(self, project_instance_uid: str , row_guid: str , is_active: int):
        self.project_instance_uid = project_instance_uid
        self.row_guid = row_guid
        self.is_active = is_active


@dataclass(frozen=False)
class project_milestone_thin_dto(base_dto):
    project_milestone_uid: str
    row_guid: str
    is_active: int
    def __init__(self, project_milestone_uid: str , row_guid: str , is_active: int):
        self.project_milestone_uid = project_milestone_uid
        self.row_guid = row_guid
        self.is_active = is_active


@dataclass(frozen=False)
class system_attribute_thin_dto(base_dto):
    system_attribute_uid: str
    row_guid: str
    is_active: int
    def __init__(self, system_attribute_uid: str , row_guid: str , is_active: int):
        self.system_attribute_uid = system_attribute_uid
        self.row_guid = row_guid
        self.is_active = is_active


@dataclass(frozen=False)
class system_change_thin_dto(base_dto):
    system_change_uid: str
    row_guid: str
    is_active: int
    def __init__(self, system_change_uid: str , row_guid: str , is_active: int):
        self.system_change_uid = system_change_uid
        self.row_guid = row_guid
        self.is_active = is_active


@dataclass(frozen=False)
class system_exception_thin_dto(base_dto):
    system_exception_uid: str
    row_guid: str
    is_active: int
    def __init__(self, system_exception_uid: str , row_guid: str , is_active: int):
        self.system_exception_uid = system_exception_uid
        self.row_guid = row_guid
        self.is_active = is_active


@dataclass(frozen=False)
class system_instance_thin_dto(base_dto):
    system_instance_uid: str
    row_guid: str
    is_active: int
    def __init__(self, system_instance_uid: str , row_guid: str , is_active: int):
        self.system_instance_uid = system_instance_uid
        self.row_guid = row_guid
        self.is_active = is_active


@dataclass(frozen=False)
class system_object_thin_dto(base_dto):
    system_object_uid: str
    row_guid: str
    is_active: int
    def __init__(self, system_object_uid: str , row_guid: str , is_active: int):
        self.system_object_uid = system_object_uid
        self.row_guid = row_guid
        self.is_active = is_active


@dataclass(frozen=False)
class system_setting_thin_dto(base_dto):
    system_setting_uid: str
    row_guid: str
    is_active: int
    def __init__(self, system_setting_uid: str , row_guid: str , is_active: int):
        self.system_setting_uid = system_setting_uid
        self.row_guid = row_guid
        self.is_active = is_active


@dataclass(frozen=False)
class system_state_thin_dto(base_dto):
    system_state_uid: str
    row_guid: str
    is_active: int
    def __init__(self, system_state_uid: str , row_guid: str , is_active: int):
        self.system_state_uid = system_state_uid
        self.row_guid = row_guid
        self.is_active = is_active

