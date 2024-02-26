import datetime
from abc import abstractmethod
from dataclasses import dataclass


# base model class to keep objects representing tables in database
@dataclass(frozen=False)
class ModelBase:
    tableName: str
    allColumns: list[str]

    def __init__(self, tableName: str, allColumns: list[str]):
        self.tableName = tableName
        self.allColumns = allColumns
        print("Nothing to be done here")

    def get_key_column_name(self):
        return self.tableName + "_uid"

    def get_insert_sql(self):
        return "insert into " + self.tableName + "() values ()"

    def get_select_all_limit_sql(self, n: int = 10):
        return "select * from " + self.tableName + " limit 100" + n

    def get_select_all_latest_sql(self, n: int = 10):
        return "select * from " + self.tableName + " order by created_date desc limit 100"

    def get_select_count_all_sql(self):
        return "select count(*) as cnt from " + self.tableName

    def get_select_count_active_sql(self):
        return "select count(*) as cnt from " + self.tableName + " where is_active=1"

    def get_select_by_key(self):
        return "select * from " + self.tableName + " where " + self.get_key_column_name() + "=? order by created_date desc limit 100"

    def get_select_by_id(self):
        return "select * from " + self.tableName + " where id=? limit 1"

    def get_select_active_only(self):
        return "select * from " + self.tableName + " where is_active=1 order by created_date desc limit 100"

    def get_select_active_by_any_column(self, column_name: str):
        return "select * from " + self.tableName + " where is_active=1 and " + column_name + "=? order by created_date desc limit 100"


# list of all models defined in database to be used by DAOs, Services, Controllers
account_division_model = ModelBase('account_division', ['id', 'account_division_uid', 'division_name', 'division_description', 'row_guid', 'is_active', 'created_date', 'created_by', 'last_updated_date', 'last_updated_by', 'removed_date', 'removed_by', 'custom_attributes'])
account_group_model = ModelBase('account_group', ['id', 'account_group_uid', 'account_group_name', 'account_group_description', 'row_guid', 'is_active', 'created_date', 'created_by', 'last_updated_date', 'last_updated_by', 'removed_date', 'removed_by', 'custom_attributes'])
account_instance_model = ModelBase('account_instance', ['id', 'account_instance_uid', 'account_title_uid', 'account_division_uid', 'account_group_uid', 'auth_identity_uid', 'account_email', 'account_name', 'display_name', 'is_system', 'row_guid', 'is_active', 'created_date', 'created_by', 'last_updated_date', 'last_updated_by', 'removed_date', 'removed_by', 'custom_attributes'])
account_title_model = ModelBase('account_title', ['id', 'account_title_uid', 'title_name', 'title_description', 'row_guid', 'is_active', 'created_date', 'created_by', 'last_updated_date', 'last_updated_by', 'removed_date', 'removed_by', 'custom_attributes'])
auth_identity_model = ModelBase('auth_identity', ['id', 'auth_identity_uid', 'identity_name', 'identity_type', 'identity_parameters', 'last_status_name', 'row_guid', 'is_active', 'created_date', 'created_by', 'last_updated_date', 'last_updated_by', 'removed_date', 'removed_by', 'custom_attributes'])
auth_password_model = ModelBase('auth_password', ['id', 'auth_password_uid', 'account_instance_uid', 'password_hash', 'password_salt', 'date_from', 'date_to', 'usage_count', 'row_guid', 'is_active', 'created_date', 'created_by', 'last_updated_date', 'last_updated_by', 'removed_date', 'removed_by', 'custom_attributes'])
auth_permission_model = ModelBase('auth_permission', ['id', 'auth_permission_uid', 'account_instance_uid', 'auth_role_uid', 'client_instance_uid', 'project_instance_uid', 'valid_from_date', 'valid_till_date', 'row_guid', 'is_active', 'created_date', 'created_by', 'last_updated_date', 'last_updated_by', 'removed_date', 'removed_by', 'custom_attributes'])
auth_request_model = ModelBase('auth_request', ['id', 'auth_request_uid', 'by_account_instance_uid', 'account_instance_uid', 'reset_guid', 'valid_till_date', 'lock_guid', 'lock_by', 'lock_date', 'is_checked', 'is_used', 'check_date', 'use_date', 'row_guid', 'is_active', 'created_date', 'created_by', 'last_updated_date', 'last_updated_by', 'removed_date', 'removed_by', 'custom_attributes'])
auth_role_model = ModelBase('auth_role', ['id', 'auth_role_uid', 'parent_auth_role_uid', 'role_name', 'role_description', 'access_uris', 'is_project', 'is_client', 'is_custom', 'row_guid', 'is_active', 'created_date', 'created_by', 'last_updated_date', 'last_updated_by', 'removed_date', 'removed_by', 'custom_attributes'])
auth_token_model = ModelBase('auth_token', ['id', 'auth_token_uid', 'account_instance_uid', 'token_seq', 'token_hash', 'token_salt', 'valid_till_date', 'last_use_date', 'is_last', 'row_guid', 'is_active', 'created_date', 'created_by', 'last_updated_date', 'last_updated_by', 'removed_date', 'removed_by', 'custom_attributes'])
client_instance_model = ModelBase('client_instance', ['id', 'client_instance_uid', 'country_uid', 'client_name', 'client_code', 'client_description', 'start_date', 'end_date', 'is_internal', 'is_system', 'is_test', 'row_guid', 'is_active', 'created_date', 'created_by', 'last_updated_date', 'last_updated_by', 'removed_date', 'removed_by', 'custom_attributes'])
country_model = ModelBase('country', ['id', 'country_uid', 'continent_name', 'continent_code', 'country_name', 'country_iso3', 'country_code', 'phone_code', 'currency_code', 'capital_name', 'region_name', 'subregion_name', 'region_code', 'latitude', 'longitude', 'currency_name', 'population', 'languages', 'area', 'bar_code', 'top_level_domain', 'is_focused', 'row_guid', 'is_active', 'created_date', 'created_by', 'last_updated_date', 'last_updated_by', 'removed_date', 'removed_by', 'custom_attributes'])
currency_model = ModelBase('currency', ['id', 'currency_uid', 'currency_name', 'is_focused', 'row_guid', 'is_active', 'created_date', 'created_by', 'last_updated_date', 'last_updated_by', 'removed_date', 'removed_by', 'custom_attributes'])
entry_final_model = ModelBase('entry_final', ['id', 'entry_final_uid', 'account_instance_uid', 'project_instance_uid', 'project_milestone_uid', 'invoice_instance_uid', 'entry_period', 'entry_note', 'lock_uid', 'start_date', 'end_date', 'entry_minutes', 'is_approved', 'row_guid', 'is_active', 'created_date', 'created_by', 'last_updated_date', 'last_updated_by', 'removed_date', 'removed_by', 'custom_attributes'])
entry_save_model = ModelBase('entry_save', ['id', 'entry_save_uid', 'account_instance_uid', 'project_instance_uid', 'project_milestone_uid', 'invoice_instance_uid', 'entry_period', 'entry_note', 'lock_uid', 'start_date', 'end_date', 'entry_minutes', 'is_approved', 'row_guid', 'is_active', 'created_date', 'created_by', 'last_updated_date', 'last_updated_by', 'removed_date', 'removed_by', 'custom_attributes'])
event_channel_model = ModelBase('event_channel', ['id', 'event_channel_uid', 'channel_type', 'channel_name', 'channel_definition', 'row_guid', 'is_active', 'created_date', 'created_by', 'last_updated_date', 'last_updated_by', 'removed_date', 'removed_by', 'custom_attributes'])
event_instance_model = ModelBase('event_instance', ['id', 'event_instance_uid', 'event_type', 'event_object', 'event_method', 'event_parameters', 'event_signature', 'published_count', 'event_date', 'row_guid', 'is_active', 'created_date', 'created_by', 'last_updated_date', 'last_updated_by', 'removed_date', 'removed_by', 'custom_attributes'])
event_subscription_model = ModelBase('event_subscription', ['id', 'event_subscription_uid', 'event_channel_uid', 'subscription_name', 'subscription_filter', 'subscription_topic', 'subscription_template', 'row_guid', 'is_active', 'created_date', 'created_by', 'last_updated_date', 'last_updated_by', 'removed_date', 'removed_by', 'custom_attributes'])
invoice_instance_model = ModelBase('invoice_instance', ['id', 'invoice_instance_uid', 'client_instance_uid', 'account_instance_uid', 'period_code', 'invoice_number', 'invoice_details', 'invoice_status', 'invoice_currency', 'invoice_amount', 'row_guid', 'is_active', 'created_date', 'created_by', 'last_updated_date', 'last_updated_by', 'removed_date', 'removed_by', 'custom_attributes'])
notification_instance_model = ModelBase('notification_instance', ['id', 'notification_instance_uid', 'account_instance_uid', 'notification_type', 'notification_topic', 'notification_format', 'notification_content', 'sending_status', 'row_guid', 'is_active', 'created_date', 'created_by', 'last_updated_date', 'last_updated_by', 'removed_date', 'removed_by', 'custom_attributes'])
project_budget_model = ModelBase('project_budget', ['id', 'project_budget_uid', 'project_instance_uid', 'budget_name', 'budget_currency', 'budget_value', 'is_current', 'row_guid', 'is_active', 'created_date', 'created_by', 'last_updated_date', 'last_updated_by', 'removed_date', 'removed_by', 'custom_attributes'])
project_group_model = ModelBase('project_group', ['id', 'project_group_uid', 'project_group_name', 'project_group_description', 'row_guid', 'is_active', 'created_date', 'created_by', 'last_updated_date', 'last_updated_by', 'removed_date', 'removed_by', 'custom_attributes'])
project_instance_model = ModelBase('project_instance', ['id', 'project_instance_uid', 'client_instance_uid', 'manager_account_instance_uid', 'project_group_uid', 'project_name', 'project_code', 'is_billable', 'start_date', 'end_date', 'current_billed', 'budget', 'row_guid', 'is_active', 'created_date', 'created_by', 'last_updated_date', 'last_updated_by', 'removed_date', 'removed_by', 'custom_attributes'])
project_milestone_model = ModelBase('project_milestone', ['id', 'project_milestone_uid', 'project_instance_uid', 'project_budget_uid', 'milestone_name', 'start_date', 'end_date', 'status_name', 'row_guid', 'is_active', 'created_date', 'created_by', 'last_updated_date', 'last_updated_by', 'removed_date', 'removed_by', 'custom_attributes'])
system_attribute_model = ModelBase('system_attribute', ['id', 'system_attribute_uid', 'system_object_uid', 'column_name', 'attribute_name', 'attribute_type', 'attribute_label', 'attribute_description', 'row_guid', 'is_active', 'created_date', 'created_by', 'last_updated_date', 'last_updated_by', 'removed_date', 'removed_by', 'custom_attributes'])
system_change_model = ModelBase('system_change', ['id', 'system_change_uid', 'account_instance_uid', 'change_type', 'change_name', 'change_json', 'row_guid', 'is_active', 'created_date', 'created_by', 'last_updated_date', 'last_updated_by', 'removed_date', 'removed_by', 'custom_attributes'])
system_exception_model = ModelBase('system_exception', ['id', 'system_exception_uid', 'system_instance_uid', 'exception_class', 'exception_message', 'exception_stacktrace', 'row_guid', 'is_active', 'created_date', 'created_by', 'last_updated_date', 'last_updated_by', 'removed_date', 'removed_by', 'custom_attributes'])
system_instance_model = ModelBase('system_instance', ['id', 'system_instance_uid', 'host_name', 'host_ip', 'local_path', 'app_version', 'mode_name', 'row_guid', 'is_active', 'created_date', 'created_by', 'last_updated_date', 'last_updated_by', 'removed_date', 'removed_by', 'custom_attributes'])
system_object_model = ModelBase('system_object', ['id', 'system_object_uid', 'object_name', 'object_type', 'table_name', 'key_name', 'parent_system_object_uid', 'row_guid', 'is_active', 'created_date', 'created_by', 'last_updated_date', 'last_updated_by', 'removed_date', 'removed_by', 'custom_attributes'])
system_setting_model = ModelBase('system_setting', ['id', 'system_setting_uid', 'account_instance_uid', 'setting_name', 'setting_value', 'row_guid', 'is_active', 'created_date', 'created_by', 'last_updated_date', 'last_updated_by', 'removed_date', 'removed_by', 'custom_attributes'])
system_state_model = ModelBase('system_state', ['id', 'system_state_uid', 'system_instance_uid', 'host_name', 'host_ip', 'local_path', 'app_version', 'mode_name', 'row_guid', 'is_active', 'created_date', 'created_by', 'last_updated_date', 'last_updated_by', 'removed_date', 'removed_by', 'custom_attributes'])


# base class for DTO classes
class BaseDto:
    id: int
    row_guid: str
    is_active: int
    created_date: datetime
    created_by: str
    last_updated_date: datetime
    last_updated_by: str
    removed_date: datetime
    removed_by: str
    custom_attributes: str

    def __init__(self):
        print("Nothing to be done here")

    def get_id(self) -> int:
        return self.id

    def get_created_date(self) -> datetime:
        return self.created_date

    def get_last_updated_date(self) -> datetime:
        return self.last_updated_date

    def is_actve(self) -> bool:
        return self.is_active == 1

    def is_removed(self) -> bool:
        return self.removed_date is not None

    @abstractmethod
    def get_key(self) -> str:
        pass

    @abstractmethod
    def get_model(self) -> ModelBase:
        pass


@dataclass(frozen=False)
class account_division_dto(BaseDto):
    id: int
    account_division_uid: str
    division_name: str
    division_description: str
    row_guid: str
    is_active: int
    created_date: datetime
    created_by: str
    last_updated_date: datetime
    last_updated_by: str
    removed_date: datetime
    removed_by: str
    custom_attributes: str

    def __init__(self, id: int, account_division_uid: str, division_name: str, division_description: str, row_guid: str, is_active: int, created_date: datetime, created_by: str, last_updated_date: datetime, last_updated_by: str, removed_date: datetime, removed_by: str, custom_attributes: str):
        self.id=id
        self.account_division_uid=account_division_uid
        self.division_name=division_name
        self.division_description=division_description
        self.row_guid=row_guid
        self.is_active=is_active
        self.created_date=created_date
        self.created_by=created_by
        self.last_updated_date=last_updated_date
        self.last_updated_by=last_updated_by
        self.removed_date=removed_date
        self.removed_by=removed_by
        self.custom_attributes=custom_attributes

    def get_model(self) -> ModelBase:
        return account_division_model

    def get_key(self) -> str:
        return self.account_division_uid


@dataclass(frozen=False)
class account_group_dto(BaseDto):
    id: int
    account_group_uid: str
    account_group_name: str
    account_group_description: str
    row_guid: str
    is_active: int
    created_date: datetime
    created_by: str
    last_updated_date: datetime
    last_updated_by: str
    removed_date: datetime
    removed_by: str
    custom_attributes: str

    def __init__(self, id: int, account_group_uid: str, account_group_name: str, account_group_description: str, row_guid: str, is_active: int, created_date: datetime, created_by: str, last_updated_date: datetime, last_updated_by: str, removed_date: datetime, removed_by: str, custom_attributes: str):
        self.id=id
        self.account_group_uid=account_group_uid
        self.account_group_name=account_group_name
        self.account_group_description=account_group_description
        self.row_guid=row_guid
        self.is_active=is_active
        self.created_date=created_date
        self.created_by=created_by
        self.last_updated_date=last_updated_date
        self.last_updated_by=last_updated_by
        self.removed_date=removed_date
        self.removed_by=removed_by
        self.custom_attributes=custom_attributes

    def get_model(self) -> ModelBase:
        return account_group_model

    def get_key(self) -> str:
        return self.account_group_uid


@dataclass(frozen=False)
class account_instance_dto(BaseDto):
    id: int
    account_instance_uid: str
    account_title_uid: str
    account_division_uid: str
    account_group_uid: str
    auth_identity_uid: str
    account_email: str
    account_name: str
    display_name: str
    is_system: int
    row_guid: str
    is_active: int
    created_date: datetime
    created_by: str
    last_updated_date: datetime
    last_updated_by: str
    removed_date: datetime
    removed_by: str
    custom_attributes: str

    def __init__(self, id: int, account_instance_uid: str, account_title_uid: str, account_division_uid: str, account_group_uid: str, auth_identity_uid: str, account_email: str, account_name: str, display_name: str, is_system: int, row_guid: str, is_active: int, created_date: datetime, created_by: str, last_updated_date: datetime, last_updated_by: str, removed_date: datetime, removed_by: str, custom_attributes: str):
        self.id=id
        self.account_instance_uid=account_instance_uid
        self.account_title_uid=account_title_uid
        self.account_division_uid=account_division_uid
        self.account_group_uid=account_group_uid
        self.auth_identity_uid=auth_identity_uid
        self.account_email=account_email
        self.account_name=account_name
        self.display_name=display_name
        self.is_system=is_system
        self.row_guid=row_guid
        self.is_active=is_active
        self.created_date=created_date
        self.created_by=created_by
        self.last_updated_date=last_updated_date
        self.last_updated_by=last_updated_by
        self.removed_date=removed_date
        self.removed_by=removed_by
        self.custom_attributes=custom_attributes

    def get_model(self) -> ModelBase:
        return account_instance_model

    def get_key(self) -> str:
        return self.account_instance_uid


@dataclass(frozen=False)
class account_title_dto(BaseDto):
    id: int
    account_title_uid: str
    title_name: str
    title_description: str
    row_guid: str
    is_active: int
    created_date: datetime
    created_by: str
    last_updated_date: datetime
    last_updated_by: str
    removed_date: datetime
    removed_by: str
    custom_attributes: str

    def __init__(self, id: int, account_title_uid: str, title_name: str, title_description: str, row_guid: str, is_active: int, created_date: datetime, created_by: str, last_updated_date: datetime, last_updated_by: str, removed_date: datetime, removed_by: str, custom_attributes: str):
        self.id=id
        self.account_title_uid=account_title_uid
        self.title_name=title_name
        self.title_description=title_description
        self.row_guid=row_guid
        self.is_active=is_active
        self.created_date=created_date
        self.created_by=created_by
        self.last_updated_date=last_updated_date
        self.last_updated_by=last_updated_by
        self.removed_date=removed_date
        self.removed_by=removed_by
        self.custom_attributes=custom_attributes

    def get_model(self) -> ModelBase:
        return account_title_model

    def get_key(self) -> str:
        return self.account_title_uid


@dataclass(frozen=False)
class auth_identity_dto(BaseDto):
    id: int
    auth_identity_uid: str
    identity_name: str
    identity_type: str
    identity_parameters: str
    last_status_name: str
    row_guid: str
    is_active: int
    created_date: datetime
    created_by: str
    last_updated_date: datetime
    last_updated_by: str
    removed_date: datetime
    removed_by: str
    custom_attributes: str

    def __init__(self, id: int, auth_identity_uid: str, identity_name: str, identity_type: str, identity_parameters: str, last_status_name: str, row_guid: str, is_active: int, created_date: datetime, created_by: str, last_updated_date: datetime, last_updated_by: str, removed_date: datetime, removed_by: str, custom_attributes: str):
        self.id=id
        self.auth_identity_uid=auth_identity_uid
        self.identity_name=identity_name
        self.identity_type=identity_type
        self.identity_parameters=identity_parameters
        self.last_status_name=last_status_name
        self.row_guid=row_guid
        self.is_active=is_active
        self.created_date=created_date
        self.created_by=created_by
        self.last_updated_date=last_updated_date
        self.last_updated_by=last_updated_by
        self.removed_date=removed_date
        self.removed_by=removed_by
        self.custom_attributes=custom_attributes

    def get_model(self) -> ModelBase:
        return auth_identity_model

    def get_key(self) -> str:
        return self.auth_identity_uid


@dataclass(frozen=False)
class auth_password_dto(BaseDto):
    id: int
    auth_password_uid: str
    account_instance_uid: str
    password_hash: str
    password_salt: str
    date_from: datetime
    date_to: datetime
    usage_count: int
    row_guid: str
    is_active: int
    created_date: datetime
    created_by: str
    last_updated_date: datetime
    last_updated_by: str
    removed_date: datetime
    removed_by: str
    custom_attributes: str

    def __init__(self, id: int, auth_password_uid: str, account_instance_uid: str, password_hash: str, password_salt: str, date_from: datetime, date_to: datetime, usage_count: int, row_guid: str, is_active: int, created_date: datetime, created_by: str, last_updated_date: datetime, last_updated_by: str, removed_date: datetime, removed_by: str, custom_attributes: str):
        self.id=id
        self.auth_password_uid=auth_password_uid
        self.account_instance_uid=account_instance_uid
        self.password_hash=password_hash
        self.password_salt=password_salt
        self.date_from=date_from
        self.date_to=date_to
        self.usage_count=usage_count
        self.row_guid=row_guid
        self.is_active=is_active
        self.created_date=created_date
        self.created_by=created_by
        self.last_updated_date=last_updated_date
        self.last_updated_by=last_updated_by
        self.removed_date=removed_date
        self.removed_by=removed_by
        self.custom_attributes=custom_attributes

    def get_model(self) -> ModelBase:
        return auth_password_model

    def get_key(self) -> str:
        return self.auth_password_uid


@dataclass(frozen=False)
class auth_permission_dto(BaseDto):
    id: int
    auth_permission_uid: str
    account_instance_uid: str
    auth_role_uid: str
    client_instance_uid: str
    project_instance_uid: str
    valid_from_date: datetime
    valid_till_date: datetime
    row_guid: str
    is_active: int
    created_date: datetime
    created_by: str
    last_updated_date: datetime
    last_updated_by: str
    removed_date: datetime
    removed_by: str
    custom_attributes: str

    def __init__(self, id: int, auth_permission_uid: str, account_instance_uid: str, auth_role_uid: str, client_instance_uid: str, project_instance_uid: str, valid_from_date: datetime, valid_till_date: datetime, row_guid: str, is_active: int, created_date: datetime, created_by: str, last_updated_date: datetime, last_updated_by: str, removed_date: datetime, removed_by: str, custom_attributes: str):
        self.id=id
        self.auth_permission_uid=auth_permission_uid
        self.account_instance_uid=account_instance_uid
        self.auth_role_uid=auth_role_uid
        self.client_instance_uid=client_instance_uid
        self.project_instance_uid=project_instance_uid
        self.valid_from_date=valid_from_date
        self.valid_till_date=valid_till_date
        self.row_guid=row_guid
        self.is_active=is_active
        self.created_date=created_date
        self.created_by=created_by
        self.last_updated_date=last_updated_date
        self.last_updated_by=last_updated_by
        self.removed_date=removed_date
        self.removed_by=removed_by
        self.custom_attributes=custom_attributes

    def get_model(self) -> ModelBase:
        return auth_permission_model

    def get_key(self) -> str:
        return self.auth_permission_uid


@dataclass(frozen=False)
class auth_request_dto(BaseDto):
    id: int
    auth_request_uid: str
    by_account_instance_uid: str
    account_instance_uid: str
    reset_guid: str
    valid_till_date: datetime
    lock_guid: str
    lock_by: str
    lock_date: datetime
    is_checked: int
    is_used: int
    check_date: datetime
    use_date: datetime
    row_guid: str
    is_active: int
    created_date: datetime
    created_by: str
    last_updated_date: datetime
    last_updated_by: str
    removed_date: datetime
    removed_by: str
    custom_attributes: str

    def __init__(self, id: int, auth_request_uid: str, by_account_instance_uid: str, account_instance_uid: str, reset_guid: str, valid_till_date: datetime, lock_guid: str, lock_by: str, lock_date: datetime, is_checked: int, is_used: int, check_date: datetime, use_date: datetime, row_guid: str, is_active: int, created_date: datetime, created_by: str, last_updated_date: datetime, last_updated_by: str, removed_date: datetime, removed_by: str, custom_attributes: str):
        self.id=id
        self.auth_request_uid=auth_request_uid
        self.by_account_instance_uid=by_account_instance_uid
        self.account_instance_uid=account_instance_uid
        self.reset_guid=reset_guid
        self.valid_till_date=valid_till_date
        self.lock_guid=lock_guid
        self.lock_by=lock_by
        self.lock_date=lock_date
        self.is_checked=is_checked
        self.is_used=is_used
        self.check_date=check_date
        self.use_date=use_date
        self.row_guid=row_guid
        self.is_active=is_active
        self.created_date=created_date
        self.created_by=created_by
        self.last_updated_date=last_updated_date
        self.last_updated_by=last_updated_by
        self.removed_date=removed_date
        self.removed_by=removed_by
        self.custom_attributes=custom_attributes

    def get_model(self) -> ModelBase:
        return auth_request_model

    def get_key(self) -> str:
        return self.auth_request_uid


@dataclass(frozen=False)
class auth_role_dto(BaseDto):
    id: int
    auth_role_uid: str
    parent_auth_role_uid: str
    role_name: str
    role_description: str
    access_uris: str
    is_project: int
    is_client: int
    is_custom: int
    row_guid: str
    is_active: int
    created_date: datetime
    created_by: str
    last_updated_date: datetime
    last_updated_by: str
    removed_date: datetime
    removed_by: str
    custom_attributes: str

    def __init__(self, id: int, auth_role_uid: str, parent_auth_role_uid: str, role_name: str, role_description: str, access_uris: str, is_project: int, is_client: int, is_custom: int, row_guid: str, is_active: int, created_date: datetime, created_by: str, last_updated_date: datetime, last_updated_by: str, removed_date: datetime, removed_by: str, custom_attributes: str):
        self.id=id
        self.auth_role_uid=auth_role_uid
        self.parent_auth_role_uid=parent_auth_role_uid
        self.role_name=role_name
        self.role_description=role_description
        self.access_uris=access_uris
        self.is_project=is_project
        self.is_client=is_client
        self.is_custom=is_custom
        self.row_guid=row_guid
        self.is_active=is_active
        self.created_date=created_date
        self.created_by=created_by
        self.last_updated_date=last_updated_date
        self.last_updated_by=last_updated_by
        self.removed_date=removed_date
        self.removed_by=removed_by
        self.custom_attributes=custom_attributes

    def get_model(self) -> ModelBase:
        return auth_role_model

    def get_key(self) -> str:
        return self.auth_role_uid


@dataclass(frozen=False)
class auth_token_dto(BaseDto):
    id: int
    auth_token_uid: str
    account_instance_uid: str
    token_seq: int
    token_hash: str
    token_salt: str
    valid_till_date: datetime
    last_use_date: datetime
    is_last: int
    row_guid: str
    is_active: int
    created_date: datetime
    created_by: str
    last_updated_date: datetime
    last_updated_by: str
    removed_date: datetime
    removed_by: str
    custom_attributes: str

    def __init__(self, id: int, auth_token_uid: str, account_instance_uid: str, token_seq: int, token_hash: str, token_salt: str, valid_till_date: datetime, last_use_date: datetime, is_last: int, row_guid: str, is_active: int, created_date: datetime, created_by: str, last_updated_date: datetime, last_updated_by: str, removed_date: datetime, removed_by: str, custom_attributes: str):
        self.id=id
        self.auth_token_uid=auth_token_uid
        self.account_instance_uid=account_instance_uid
        self.token_seq=token_seq
        self.token_hash=token_hash
        self.token_salt=token_salt
        self.valid_till_date=valid_till_date
        self.last_use_date=last_use_date
        self.is_last=is_last
        self.row_guid=row_guid
        self.is_active=is_active
        self.created_date=created_date
        self.created_by=created_by
        self.last_updated_date=last_updated_date
        self.last_updated_by=last_updated_by
        self.removed_date=removed_date
        self.removed_by=removed_by
        self.custom_attributes=custom_attributes

    def get_model(self) -> ModelBase:
        return auth_token_model

    def get_key(self) -> str:
        return self.auth_token_uid


@dataclass(frozen=False)
class client_instance_dto(BaseDto):
    id: int
    client_instance_uid: str
    country_uid: str
    client_name: str
    client_code: str
    client_description: str
    start_date: datetime
    end_date: datetime
    is_internal: int
    is_system: int
    is_test: int
    row_guid: str
    is_active: int
    created_date: datetime
    created_by: str
    last_updated_date: datetime
    last_updated_by: str
    removed_date: datetime
    removed_by: str
    custom_attributes: str

    def __init__(self, id: int, client_instance_uid: str, country_uid: str, client_name: str, client_code: str, client_description: str, start_date: datetime, end_date: datetime, is_internal: int, is_system: int, is_test: int, row_guid: str, is_active: int, created_date: datetime, created_by: str, last_updated_date: datetime, last_updated_by: str, removed_date: datetime, removed_by: str, custom_attributes: str):
        self.id=id
        self.client_instance_uid=client_instance_uid
        self.country_uid=country_uid
        self.client_name=client_name
        self.client_code=client_code
        self.client_description=client_description
        self.start_date=start_date
        self.end_date=end_date
        self.is_internal=is_internal
        self.is_system=is_system
        self.is_test=is_test
        self.row_guid=row_guid
        self.is_active=is_active
        self.created_date=created_date
        self.created_by=created_by
        self.last_updated_date=last_updated_date
        self.last_updated_by=last_updated_by
        self.removed_date=removed_date
        self.removed_by=removed_by
        self.custom_attributes=custom_attributes

    def get_model(self) -> ModelBase:
        return client_instance_model

    def get_key(self) -> str:
        return self.client_instance_uid


@dataclass(frozen=False)
class country_dto(BaseDto):
    id: int
    country_uid: str
    continent_name: str
    continent_code: str
    country_name: str
    country_iso3: str
    country_code: str
    phone_code: str
    currency_code: str
    capital_name: str
    region_name: str
    subregion_name: str
    region_code: str
    latitude: str
    longitude: str
    currency_name: str
    population: str
    languages: str
    area: str
    bar_code: str
    top_level_domain: str
    is_focused: int
    row_guid: str
    is_active: int
    created_date: datetime
    created_by: str
    last_updated_date: datetime
    last_updated_by: str
    removed_date: datetime
    removed_by: str
    custom_attributes: str

    def __init__(self, id: int, country_uid: str, continent_name: str, continent_code: str, country_name: str, country_iso3: str, country_code: str, phone_code: str, currency_code: str, capital_name: str, region_name: str, subregion_name: str, region_code: str, latitude: str, longitude: str, currency_name: str, population: str, languages: str, area: str, bar_code: str, top_level_domain: str, is_focused: int, row_guid: str, is_active: int, created_date: datetime, created_by: str, last_updated_date: datetime, last_updated_by: str, removed_date: datetime, removed_by: str, custom_attributes: str):
        self.id=id
        self.country_uid=country_uid
        self.continent_name=continent_name
        self.continent_code=continent_code
        self.country_name=country_name
        self.country_iso3=country_iso3
        self.country_code=country_code
        self.phone_code=phone_code
        self.currency_code=currency_code
        self.capital_name=capital_name
        self.region_name=region_name
        self.subregion_name=subregion_name
        self.region_code=region_code
        self.latitude=latitude
        self.longitude=longitude
        self.currency_name=currency_name
        self.population=population
        self.languages=languages
        self.area=area
        self.bar_code=bar_code
        self.top_level_domain=top_level_domain
        self.is_focused=is_focused
        self.row_guid=row_guid
        self.is_active=is_active
        self.created_date=created_date
        self.created_by=created_by
        self.last_updated_date=last_updated_date
        self.last_updated_by=last_updated_by
        self.removed_date=removed_date
        self.removed_by=removed_by
        self.custom_attributes=custom_attributes

    def get_model(self) -> ModelBase:
        return country_model

    def get_key(self) -> str:
        return self.country_uid


@dataclass(frozen=False)
class currency_dto(BaseDto):
    id: int
    currency_uid: str
    currency_name: str
    is_focused: int
    row_guid: str
    is_active: int
    created_date: datetime
    created_by: str
    last_updated_date: datetime
    last_updated_by: str
    removed_date: datetime
    removed_by: str
    custom_attributes: str

    def __init__(self, id: int, currency_uid: str, currency_name: str, is_focused: int, row_guid: str, is_active: int, created_date: datetime, created_by: str, last_updated_date: datetime, last_updated_by: str, removed_date: datetime, removed_by: str, custom_attributes: str):
        self.id=id
        self.currency_uid=currency_uid
        self.currency_name=currency_name
        self.is_focused=is_focused
        self.row_guid=row_guid
        self.is_active=is_active
        self.created_date=created_date
        self.created_by=created_by
        self.last_updated_date=last_updated_date
        self.last_updated_by=last_updated_by
        self.removed_date=removed_date
        self.removed_by=removed_by
        self.custom_attributes=custom_attributes

    def get_model(self) -> ModelBase:
        return currency_model

    def get_key(self) -> str:
        return self.currency_uid


@dataclass(frozen=False)
class entry_final_dto(BaseDto):
    id: int
    entry_final_uid: str
    account_instance_uid: str
    project_instance_uid: str
    project_milestone_uid: str
    invoice_instance_uid: str
    entry_period: str
    entry_note: str
    lock_uid: str
    start_date: datetime
    end_date: datetime
    entry_minutes: int
    is_approved: int
    row_guid: str
    is_active: int
    created_date: datetime
    created_by: str
    last_updated_date: datetime
    last_updated_by: str
    removed_date: datetime
    removed_by: str
    custom_attributes: str

    def __init__(self, id: int, entry_final_uid: str, account_instance_uid: str, project_instance_uid: str, project_milestone_uid: str, invoice_instance_uid: str, entry_period: str, entry_note: str, lock_uid: str, start_date: datetime, end_date: datetime, entry_minutes: int, is_approved: int, row_guid: str, is_active: int, created_date: datetime, created_by: str, last_updated_date: datetime, last_updated_by: str, removed_date: datetime, removed_by: str, custom_attributes: str):
        self.id=id
        self.entry_final_uid=entry_final_uid
        self.account_instance_uid=account_instance_uid
        self.project_instance_uid=project_instance_uid
        self.project_milestone_uid=project_milestone_uid
        self.invoice_instance_uid=invoice_instance_uid
        self.entry_period=entry_period
        self.entry_note=entry_note
        self.lock_uid=lock_uid
        self.start_date=start_date
        self.end_date=end_date
        self.entry_minutes=entry_minutes
        self.is_approved=is_approved
        self.row_guid=row_guid
        self.is_active=is_active
        self.created_date=created_date
        self.created_by=created_by
        self.last_updated_date=last_updated_date
        self.last_updated_by=last_updated_by
        self.removed_date=removed_date
        self.removed_by=removed_by
        self.custom_attributes=custom_attributes

    def get_model(self) -> ModelBase:
        return entry_final_model

    def get_key(self) -> str:
        return self.entry_final_uid


@dataclass(frozen=False)
class entry_save_dto(BaseDto):
    id: int
    entry_save_uid: str
    account_instance_uid: str
    project_instance_uid: str
    project_milestone_uid: str
    invoice_instance_uid: str
    entry_period: str
    entry_note: str
    lock_uid: str
    start_date: datetime
    end_date: datetime
    entry_minutes: int
    is_approved: int
    row_guid: str
    is_active: int
    created_date: datetime
    created_by: str
    last_updated_date: datetime
    last_updated_by: str
    removed_date: datetime
    removed_by: str
    custom_attributes: str

    def __init__(self, id: int, entry_save_uid: str, account_instance_uid: str, project_instance_uid: str, project_milestone_uid: str, invoice_instance_uid: str, entry_period: str, entry_note: str, lock_uid: str, start_date: datetime, end_date: datetime, entry_minutes: int, is_approved: int, row_guid: str, is_active: int, created_date: datetime, created_by: str, last_updated_date: datetime, last_updated_by: str, removed_date: datetime, removed_by: str, custom_attributes: str):
        self.id=id
        self.entry_save_uid=entry_save_uid
        self.account_instance_uid=account_instance_uid
        self.project_instance_uid=project_instance_uid
        self.project_milestone_uid=project_milestone_uid
        self.invoice_instance_uid=invoice_instance_uid
        self.entry_period=entry_period
        self.entry_note=entry_note
        self.lock_uid=lock_uid
        self.start_date=start_date
        self.end_date=end_date
        self.entry_minutes=entry_minutes
        self.is_approved=is_approved
        self.row_guid=row_guid
        self.is_active=is_active
        self.created_date=created_date
        self.created_by=created_by
        self.last_updated_date=last_updated_date
        self.last_updated_by=last_updated_by
        self.removed_date=removed_date
        self.removed_by=removed_by
        self.custom_attributes=custom_attributes

    def get_model(self) -> ModelBase:
        return entry_save_model

    def get_key(self) -> str:
        return self.entry_save_uid


@dataclass(frozen=False)
class event_channel_dto(BaseDto):
    id: int
    event_channel_uid: str
    channel_type: str
    channel_name: str
    channel_definition: str
    row_guid: str
    is_active: int
    created_date: datetime
    created_by: str
    last_updated_date: datetime
    last_updated_by: str
    removed_date: datetime
    removed_by: str
    custom_attributes: str

    def __init__(self, id: int, event_channel_uid: str, channel_type: str, channel_name: str, channel_definition: str, row_guid: str, is_active: int, created_date: datetime, created_by: str, last_updated_date: datetime, last_updated_by: str, removed_date: datetime, removed_by: str, custom_attributes: str):
        self.id=id
        self.event_channel_uid=event_channel_uid
        self.channel_type=channel_type
        self.channel_name=channel_name
        self.channel_definition=channel_definition
        self.row_guid=row_guid
        self.is_active=is_active
        self.created_date=created_date
        self.created_by=created_by
        self.last_updated_date=last_updated_date
        self.last_updated_by=last_updated_by
        self.removed_date=removed_date
        self.removed_by=removed_by
        self.custom_attributes=custom_attributes

    def get_model(self) -> ModelBase:
        return event_channel_model

    def get_key(self) -> str:
        return self.event_channel_uid


@dataclass(frozen=False)
class event_instance_dto(BaseDto):
    id: int
    event_instance_uid: str
    event_type: str
    event_object: str
    event_method: str
    event_parameters: str
    event_signature: str
    published_count: int
    event_date: datetime
    row_guid: str
    is_active: int
    created_date: datetime
    created_by: str
    last_updated_date: datetime
    last_updated_by: str
    removed_date: datetime
    removed_by: str
    custom_attributes: str

    def __init__(self, id: int, event_instance_uid: str, event_type: str, event_object: str, event_method: str, event_parameters: str, event_signature: str, published_count: int, event_date: datetime, row_guid: str, is_active: int, created_date: datetime, created_by: str, last_updated_date: datetime, last_updated_by: str, removed_date: datetime, removed_by: str, custom_attributes: str):
        self.id=id
        self.event_instance_uid=event_instance_uid
        self.event_type=event_type
        self.event_object=event_object
        self.event_method=event_method
        self.event_parameters=event_parameters
        self.event_signature=event_signature
        self.published_count=published_count
        self.event_date=event_date
        self.row_guid=row_guid
        self.is_active=is_active
        self.created_date=created_date
        self.created_by=created_by
        self.last_updated_date=last_updated_date
        self.last_updated_by=last_updated_by
        self.removed_date=removed_date
        self.removed_by=removed_by
        self.custom_attributes=custom_attributes

    def get_model(self) -> ModelBase:
        return event_instance_model

    def get_key(self) -> str:
        return self.event_instance_uid


@dataclass(frozen=False)
class event_subscription_dto(BaseDto):
    id: int
    event_subscription_uid: str
    event_channel_uid: str
    subscription_name: str
    subscription_filter: str
    subscription_topic: str
    subscription_template: str
    row_guid: str
    is_active: int
    created_date: datetime
    created_by: str
    last_updated_date: datetime
    last_updated_by: str
    removed_date: datetime
    removed_by: str
    custom_attributes: str

    def __init__(self, id: int, event_subscription_uid: str, event_channel_uid: str, subscription_name: str, subscription_filter: str, subscription_topic: str, subscription_template: str, row_guid: str, is_active: int, created_date: datetime, created_by: str, last_updated_date: datetime, last_updated_by: str, removed_date: datetime, removed_by: str, custom_attributes: str):
        self.id=id
        self.event_subscription_uid=event_subscription_uid
        self.event_channel_uid=event_channel_uid
        self.subscription_name=subscription_name
        self.subscription_filter=subscription_filter
        self.subscription_topic=subscription_topic
        self.subscription_template=subscription_template
        self.row_guid=row_guid
        self.is_active=is_active
        self.created_date=created_date
        self.created_by=created_by
        self.last_updated_date=last_updated_date
        self.last_updated_by=last_updated_by
        self.removed_date=removed_date
        self.removed_by=removed_by
        self.custom_attributes=custom_attributes

    def get_model(self) -> ModelBase:
        return event_subscription_model

    def get_key(self) -> str:
        return self.event_subscription_uid


@dataclass(frozen=False)
class invoice_instance_dto(BaseDto):
    id: int
    invoice_instance_uid: str
    client_instance_uid: str
    account_instance_uid: str
    period_code: str
    invoice_number: str
    invoice_details: str
    invoice_status: str
    invoice_currency: str
    invoice_amount: str
    row_guid: str
    is_active: int
    created_date: datetime
    created_by: str
    last_updated_date: datetime
    last_updated_by: str
    removed_date: datetime
    removed_by: str
    custom_attributes: str

    def __init__(self, id: int, invoice_instance_uid: str, client_instance_uid: str, account_instance_uid: str, period_code: str, invoice_number: str, invoice_details: str, invoice_status: str, invoice_currency: str, invoice_amount: str, row_guid: str, is_active: int, created_date: datetime, created_by: str, last_updated_date: datetime, last_updated_by: str, removed_date: datetime, removed_by: str, custom_attributes: str):
        self.id=id
        self.invoice_instance_uid=invoice_instance_uid
        self.client_instance_uid=client_instance_uid
        self.account_instance_uid=account_instance_uid
        self.period_code=period_code
        self.invoice_number=invoice_number
        self.invoice_details=invoice_details
        self.invoice_status=invoice_status
        self.invoice_currency=invoice_currency
        self.invoice_amount=invoice_amount
        self.row_guid=row_guid
        self.is_active=is_active
        self.created_date=created_date
        self.created_by=created_by
        self.last_updated_date=last_updated_date
        self.last_updated_by=last_updated_by
        self.removed_date=removed_date
        self.removed_by=removed_by
        self.custom_attributes=custom_attributes

    def get_model(self) -> ModelBase:
        return invoice_instance_model

    def get_key(self) -> str:
        return self.invoice_instance_uid


@dataclass(frozen=False)
class notification_instance_dto(BaseDto):
    id: int
    notification_instance_uid: str
    account_instance_uid: str
    notification_type: str
    notification_topic: str
    notification_format: str
    notification_content: str
    sending_status: str
    row_guid: str
    is_active: int
    created_date: datetime
    created_by: str
    last_updated_date: datetime
    last_updated_by: str
    removed_date: datetime
    removed_by: str
    custom_attributes: str

    def __init__(self, id: int, notification_instance_uid: str, account_instance_uid: str, notification_type: str, notification_topic: str, notification_format: str, notification_content: str, sending_status: str, row_guid: str, is_active: int, created_date: datetime, created_by: str, last_updated_date: datetime, last_updated_by: str, removed_date: datetime, removed_by: str, custom_attributes: str):
        self.id=id
        self.notification_instance_uid=notification_instance_uid
        self.account_instance_uid=account_instance_uid
        self.notification_type=notification_type
        self.notification_topic=notification_topic
        self.notification_format=notification_format
        self.notification_content=notification_content
        self.sending_status=sending_status
        self.row_guid=row_guid
        self.is_active=is_active
        self.created_date=created_date
        self.created_by=created_by
        self.last_updated_date=last_updated_date
        self.last_updated_by=last_updated_by
        self.removed_date=removed_date
        self.removed_by=removed_by
        self.custom_attributes=custom_attributes

    def get_model(self) -> ModelBase:
        return notification_instance_model

    def get_key(self) -> str:
        return self.notification_instance_uid


@dataclass(frozen=False)
class project_budget_dto(BaseDto):
    id: int
    project_budget_uid: str
    project_instance_uid: str
    budget_name: str
    budget_currency: str
    budget_value: str
    is_current: int
    row_guid: str
    is_active: int
    created_date: datetime
    created_by: str
    last_updated_date: datetime
    last_updated_by: str
    removed_date: datetime
    removed_by: str
    custom_attributes: str

    def __init__(self, id: int, project_budget_uid: str, project_instance_uid: str, budget_name: str, budget_currency: str, budget_value: str, is_current: int, row_guid: str, is_active: int, created_date: datetime, created_by: str, last_updated_date: datetime, last_updated_by: str, removed_date: datetime, removed_by: str, custom_attributes: str):
        self.id=id
        self.project_budget_uid=project_budget_uid
        self.project_instance_uid=project_instance_uid
        self.budget_name=budget_name
        self.budget_currency=budget_currency
        self.budget_value=budget_value
        self.is_current=is_current
        self.row_guid=row_guid
        self.is_active=is_active
        self.created_date=created_date
        self.created_by=created_by
        self.last_updated_date=last_updated_date
        self.last_updated_by=last_updated_by
        self.removed_date=removed_date
        self.removed_by=removed_by
        self.custom_attributes=custom_attributes

    def get_model(self) -> ModelBase:
        return project_budget_model

    def get_key(self) -> str:
        return self.project_budget_uid


@dataclass(frozen=False)
class project_group_dto(BaseDto):
    id: int
    project_group_uid: str
    project_group_name: str
    project_group_description: str
    row_guid: str
    is_active: int
    created_date: datetime
    created_by: str
    last_updated_date: datetime
    last_updated_by: str
    removed_date: datetime
    removed_by: str
    custom_attributes: str

    def __init__(self, id: int, project_group_uid: str, project_group_name: str, project_group_description: str, row_guid: str, is_active: int, created_date: datetime, created_by: str, last_updated_date: datetime, last_updated_by: str, removed_date: datetime, removed_by: str, custom_attributes: str):
        self.id=id
        self.project_group_uid=project_group_uid
        self.project_group_name=project_group_name
        self.project_group_description=project_group_description
        self.row_guid=row_guid
        self.is_active=is_active
        self.created_date=created_date
        self.created_by=created_by
        self.last_updated_date=last_updated_date
        self.last_updated_by=last_updated_by
        self.removed_date=removed_date
        self.removed_by=removed_by
        self.custom_attributes=custom_attributes

    def get_model(self) -> ModelBase:
        return project_group_model

    def get_key(self) -> str:
        return self.project_group_uid


@dataclass(frozen=False)
class project_instance_dto(BaseDto):
    id: int
    project_instance_uid: str
    client_instance_uid: str
    manager_account_instance_uid: str
    project_group_uid: str
    project_name: str
    project_code: str
    is_billable: int
    start_date: datetime
    end_date: datetime
    current_billed: str
    budget: str
    row_guid: str
    is_active: int
    created_date: datetime
    created_by: str
    last_updated_date: datetime
    last_updated_by: str
    removed_date: datetime
    removed_by: str
    custom_attributes: str

    def __init__(self, id: int, project_instance_uid: str, client_instance_uid: str, manager_account_instance_uid: str, project_group_uid: str, project_name: str, project_code: str, is_billable: int, start_date: datetime, end_date: datetime, current_billed: str, budget: str, row_guid: str, is_active: int, created_date: datetime, created_by: str, last_updated_date: datetime, last_updated_by: str, removed_date: datetime, removed_by: str, custom_attributes: str):
        self.id=id
        self.project_instance_uid=project_instance_uid
        self.client_instance_uid=client_instance_uid
        self.manager_account_instance_uid=manager_account_instance_uid
        self.project_group_uid=project_group_uid
        self.project_name=project_name
        self.project_code=project_code
        self.is_billable=is_billable
        self.start_date=start_date
        self.end_date=end_date
        self.current_billed=current_billed
        self.budget=budget
        self.row_guid=row_guid
        self.is_active=is_active
        self.created_date=created_date
        self.created_by=created_by
        self.last_updated_date=last_updated_date
        self.last_updated_by=last_updated_by
        self.removed_date=removed_date
        self.removed_by=removed_by
        self.custom_attributes=custom_attributes

    def get_model(self) -> ModelBase:
        return project_instance_model

    def get_key(self) -> str:
        return self.project_instance_uid


@dataclass(frozen=False)
class project_milestone_dto(BaseDto):
    id: int
    project_milestone_uid: str
    project_instance_uid: str
    project_budget_uid: str
    milestone_name: str
    start_date: datetime
    end_date: datetime
    status_name: str
    row_guid: str
    is_active: int
    created_date: datetime
    created_by: str
    last_updated_date: datetime
    last_updated_by: str
    removed_date: datetime
    removed_by: str
    custom_attributes: str

    def __init__(self, id: int, project_milestone_uid: str, project_instance_uid: str, project_budget_uid: str, milestone_name: str, start_date: datetime, end_date: datetime, status_name: str, row_guid: str, is_active: int, created_date: datetime, created_by: str, last_updated_date: datetime, last_updated_by: str, removed_date: datetime, removed_by: str, custom_attributes: str):
        self.id=id
        self.project_milestone_uid=project_milestone_uid
        self.project_instance_uid=project_instance_uid
        self.project_budget_uid=project_budget_uid
        self.milestone_name=milestone_name
        self.start_date=start_date
        self.end_date=end_date
        self.status_name=status_name
        self.row_guid=row_guid
        self.is_active=is_active
        self.created_date=created_date
        self.created_by=created_by
        self.last_updated_date=last_updated_date
        self.last_updated_by=last_updated_by
        self.removed_date=removed_date
        self.removed_by=removed_by
        self.custom_attributes=custom_attributes

    def get_model(self) -> ModelBase:
        return project_milestone_model

    def get_key(self) -> str:
        return self.project_milestone_uid


@dataclass(frozen=False)
class system_attribute_dto(BaseDto):
    id: int
    system_attribute_uid: str
    system_object_uid: str
    column_name: str
    attribute_name: str
    attribute_type: str
    attribute_label: str
    attribute_description: str
    row_guid: str
    is_active: int
    created_date: datetime
    created_by: str
    last_updated_date: datetime
    last_updated_by: str
    removed_date: datetime
    removed_by: str
    custom_attributes: str

    def __init__(self, id: int, system_attribute_uid: str, system_object_uid: str, column_name: str, attribute_name: str, attribute_type: str, attribute_label: str, attribute_description: str, row_guid: str, is_active: int, created_date: datetime, created_by: str, last_updated_date: datetime, last_updated_by: str, removed_date: datetime, removed_by: str, custom_attributes: str):
        self.id=id
        self.system_attribute_uid=system_attribute_uid
        self.system_object_uid=system_object_uid
        self.column_name=column_name
        self.attribute_name=attribute_name
        self.attribute_type=attribute_type
        self.attribute_label=attribute_label
        self.attribute_description=attribute_description
        self.row_guid=row_guid
        self.is_active=is_active
        self.created_date=created_date
        self.created_by=created_by
        self.last_updated_date=last_updated_date
        self.last_updated_by=last_updated_by
        self.removed_date=removed_date
        self.removed_by=removed_by
        self.custom_attributes=custom_attributes

    def get_model(self) -> ModelBase:
        return system_attribute_model

    def get_key(self) -> str:
        return self.system_attribute_uid


@dataclass(frozen=False)
class system_change_dto(BaseDto):
    id: int
    system_change_uid: str
    account_instance_uid: str
    change_type: str
    change_name: str
    change_json: str
    row_guid: str
    is_active: int
    created_date: datetime
    created_by: str
    last_updated_date: datetime
    last_updated_by: str
    removed_date: datetime
    removed_by: str
    custom_attributes: str

    def __init__(self, id: int, system_change_uid: str, account_instance_uid: str, change_type: str, change_name: str, change_json: str, row_guid: str, is_active: int, created_date: datetime, created_by: str, last_updated_date: datetime, last_updated_by: str, removed_date: datetime, removed_by: str, custom_attributes: str):
        self.id=id
        self.system_change_uid=system_change_uid
        self.account_instance_uid=account_instance_uid
        self.change_type=change_type
        self.change_name=change_name
        self.change_json=change_json
        self.row_guid=row_guid
        self.is_active=is_active
        self.created_date=created_date
        self.created_by=created_by
        self.last_updated_date=last_updated_date
        self.last_updated_by=last_updated_by
        self.removed_date=removed_date
        self.removed_by=removed_by
        self.custom_attributes=custom_attributes

    def get_model(self) -> ModelBase:
        return system_change_model

    def get_key(self) -> str:
        return self.system_change_uid


@dataclass(frozen=False)
class system_exception_dto(BaseDto):
    id: int
    system_exception_uid: str
    system_instance_uid: str
    exception_class: str
    exception_message: str
    exception_stacktrace: str
    row_guid: str
    is_active: int
    created_date: datetime
    created_by: str
    last_updated_date: datetime
    last_updated_by: str
    removed_date: datetime
    removed_by: str
    custom_attributes: str

    def __init__(self, id: int, system_exception_uid: str, system_instance_uid: str, exception_class: str, exception_message: str, exception_stacktrace: str, row_guid: str, is_active: int, created_date: datetime, created_by: str, last_updated_date: datetime, last_updated_by: str, removed_date: datetime, removed_by: str, custom_attributes: str):
        self.id=id
        self.system_exception_uid=system_exception_uid
        self.system_instance_uid=system_instance_uid
        self.exception_class=exception_class
        self.exception_message=exception_message
        self.exception_stacktrace=exception_stacktrace
        self.row_guid=row_guid
        self.is_active=is_active
        self.created_date=created_date
        self.created_by=created_by
        self.last_updated_date=last_updated_date
        self.last_updated_by=last_updated_by
        self.removed_date=removed_date
        self.removed_by=removed_by
        self.custom_attributes=custom_attributes

    def get_model(self) -> ModelBase:
        return system_exception_model

    def get_key(self) -> str:
        return self.system_exception_uid


@dataclass(frozen=False)
class system_instance_dto(BaseDto):
    id: int
    system_instance_uid: str
    host_name: str
    host_ip: str
    local_path: str
    app_version: str
    mode_name: str
    row_guid: str
    is_active: int
    created_date: datetime
    created_by: str
    last_updated_date: datetime
    last_updated_by: str
    removed_date: datetime
    removed_by: str
    custom_attributes: str

    def __init__(self, id: int, system_instance_uid: str, host_name: str, host_ip: str, local_path: str, app_version: str, mode_name: str, row_guid: str, is_active: int, created_date: datetime, created_by: str, last_updated_date: datetime, last_updated_by: str, removed_date: datetime, removed_by: str, custom_attributes: str):
        self.id=id
        self.system_instance_uid=system_instance_uid
        self.host_name=host_name
        self.host_ip=host_ip
        self.local_path=local_path
        self.app_version=app_version
        self.mode_name=mode_name
        self.row_guid=row_guid
        self.is_active=is_active
        self.created_date=created_date
        self.created_by=created_by
        self.last_updated_date=last_updated_date
        self.last_updated_by=last_updated_by
        self.removed_date=removed_date
        self.removed_by=removed_by
        self.custom_attributes=custom_attributes

    def get_model(self) -> ModelBase:
        return system_instance_model

    def get_key(self) -> str:
        return self.system_instance_uid


@dataclass(frozen=False)
class system_object_dto(BaseDto):
    id: int
    system_object_uid: str
    object_name: str
    object_type: str
    table_name: str
    key_name: str
    parent_system_object_uid: str
    row_guid: str
    is_active: int
    created_date: datetime
    created_by: str
    last_updated_date: datetime
    last_updated_by: str
    removed_date: datetime
    removed_by: str
    custom_attributes: str

    def __init__(self, id: int, system_object_uid: str, object_name: str, object_type: str, table_name: str, key_name: str, parent_system_object_uid: str, row_guid: str, is_active: int, created_date: datetime, created_by: str, last_updated_date: datetime, last_updated_by: str, removed_date: datetime, removed_by: str, custom_attributes: str):
        self.id=id
        self.system_object_uid=system_object_uid
        self.object_name=object_name
        self.object_type=object_type
        self.table_name=table_name
        self.key_name=key_name
        self.parent_system_object_uid=parent_system_object_uid
        self.row_guid=row_guid
        self.is_active=is_active
        self.created_date=created_date
        self.created_by=created_by
        self.last_updated_date=last_updated_date
        self.last_updated_by=last_updated_by
        self.removed_date=removed_date
        self.removed_by=removed_by
        self.custom_attributes=custom_attributes

    def get_model(self) -> ModelBase:
        return system_object_model

    def get_key(self) -> str:
        return self.system_object_uid


@dataclass(frozen=False)
class system_setting_dto(BaseDto):
    id: int
    system_setting_uid: str
    account_instance_uid: str
    setting_name: str
    setting_value: str
    row_guid: str
    is_active: int
    created_date: datetime
    created_by: str
    last_updated_date: datetime
    last_updated_by: str
    removed_date: datetime
    removed_by: str
    custom_attributes: str

    def __init__(self, id: int, system_setting_uid: str, account_instance_uid: str, setting_name: str, setting_value: str, row_guid: str, is_active: int, created_date: datetime, created_by: str, last_updated_date: datetime, last_updated_by: str, removed_date: datetime, removed_by: str, custom_attributes: str):
        self.id=id
        self.system_setting_uid=system_setting_uid
        self.account_instance_uid=account_instance_uid
        self.setting_name=setting_name
        self.setting_value=setting_value
        self.row_guid=row_guid
        self.is_active=is_active
        self.created_date=created_date
        self.created_by=created_by
        self.last_updated_date=last_updated_date
        self.last_updated_by=last_updated_by
        self.removed_date=removed_date
        self.removed_by=removed_by
        self.custom_attributes=custom_attributes

    def get_model(self) -> ModelBase:
        return system_setting_model

    def get_key(self) -> str:
        return self.system_setting_uid


@dataclass(frozen=False)
class system_state_dto(BaseDto):
    id: int
    system_state_uid: str
    system_instance_uid: str
    host_name: str
    host_ip: str
    local_path: str
    app_version: str
    mode_name: str
    row_guid: str
    is_active: int
    created_date: datetime
    created_by: str
    last_updated_date: datetime
    last_updated_by: str
    removed_date: datetime
    removed_by: str
    custom_attributes: str

    def __init__(self, id: int, system_state_uid: str, system_instance_uid: str, host_name: str, host_ip: str, local_path: str, app_version: str, mode_name: str, row_guid: str, is_active: int, created_date: datetime, created_by: str, last_updated_date: datetime, last_updated_by: str, removed_date: datetime, removed_by: str, custom_attributes: str):
        self.id=id
        self.system_state_uid=system_state_uid
        self.system_instance_uid=system_instance_uid
        self.host_name=host_name
        self.host_ip=host_ip
        self.local_path=local_path
        self.app_version=app_version
        self.mode_name=mode_name
        self.row_guid=row_guid
        self.is_active=is_active
        self.created_date=created_date
        self.created_by=created_by
        self.last_updated_date=last_updated_date
        self.last_updated_by=last_updated_by
        self.removed_date=removed_date
        self.removed_by=removed_by
        self.custom_attributes=custom_attributes

    def get_model(self) -> ModelBase:
        return system_state_model

    def get_key(self) -> str:
        return self.system_state_uid

