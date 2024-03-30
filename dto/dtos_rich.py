# auto-generated - v_definition_python_dtos_rich - START at 2024-03-30 03:32:02.778089+01
import datetime
from datetime import datetime
from abc import abstractmethod
from dataclasses import dataclass
from dto.dtos import *
from dto.dtos_thin import *
from dto.dtos_write import *
from dto.dtos_read import *


@dataclass(frozen=False)
class account_rich_dto(account_read_dto):
    account_uid: str | None
    account_name: str | None
    tenant_uid: str | None
    account_type_uid: str | None
    account_title_uid: str | None
    account_division_uid: str | None
    account_group_uid: str | None
    auth_identity_uid: str | None
    account_email: str | None
    display_name: str | None
    is_system: int | None
    row_instance: str | None
    row_lock: str | None
    row_owner: str | None
    row_seq: int | None
    row_guid: str | None
    row_version: int | None
    is_active: int | None
    created_date: datetime.datetime | None
    created_by: str | None
    last_updated_date: datetime.datetime | None
    last_updated_by: str | None
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str | None
    tenant_uid_tenant_name: str | None
    tenant_uid_country_uid: str | None
    tenant_uid_tenant_type_uid: str | None
    tenant_uid_tenant_category_uid: str | None
    tenant_uid_tenant_code: str | None
    tenant_uid_tenant_description: str | None
    tenant_uid_start_date: datetime.datetime | None
    tenant_uid_end_date: datetime.datetime | None
    tenant_uid_is_internal: int | None
    tenant_uid_is_system: int | None
    tenant_uid_is_test: int | None
    tenant_uid_account_uid: str | None
    account_type_uid_account_type_name: str | None
    account_type_uid_account_type_description: str | None
    account_title_uid_account_title_name: str | None
    account_title_uid_title_description: str | None
    account_division_uid_account_division_name: str | None
    account_division_uid_tenant_uid: str | None
    account_division_uid_account_uid: str | None
    account_division_uid_account_division_template_uid: str | None
    account_division_uid_division_description: str | None
    account_group_uid_account_group_name: str | None
    account_group_uid_tenant_uid: str | None
    account_group_uid_account_group_description: str | None
    auth_identity_uid_auth_identity_name: str | None
    auth_identity_uid_class_name: str | None
    auth_identity_uid_default_parameters_json: str | None
    def __init__(self, account_uid: str | None, account_name: str | None, tenant_uid: str | None, account_type_uid: str | None, account_title_uid: str | None, account_division_uid: str | None, account_group_uid: str | None, auth_identity_uid: str | None, account_email: str | None, display_name: str | None, is_system: int | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None, tenant_uid_tenant_name: str | None, tenant_uid_country_uid: str | None, tenant_uid_tenant_type_uid: str | None, tenant_uid_tenant_category_uid: str | None, tenant_uid_tenant_code: str | None, tenant_uid_tenant_description: str | None, tenant_uid_start_date: datetime.datetime | None, tenant_uid_end_date: datetime.datetime | None, tenant_uid_is_internal: int | None, tenant_uid_is_system: int | None, tenant_uid_is_test: int | None, tenant_uid_account_uid: str | None, account_type_uid_account_type_name: str | None, account_type_uid_account_type_description: str | None, account_title_uid_account_title_name: str | None, account_title_uid_title_description: str | None, account_division_uid_account_division_name: str | None, account_division_uid_tenant_uid: str | None, account_division_uid_account_uid: str | None, account_division_uid_account_division_template_uid: str | None, account_division_uid_division_description: str | None, account_group_uid_account_group_name: str | None, account_group_uid_tenant_uid: str | None, account_group_uid_account_group_description: str | None, auth_identity_uid_auth_identity_name: str | None, auth_identity_uid_class_name: str | None, auth_identity_uid_default_parameters_json: str | None):
        self.account_uid = account_uid
        self.account_name = account_name
        self.tenant_uid = tenant_uid
        self.account_type_uid = account_type_uid
        self.account_title_uid = account_title_uid
        self.account_division_uid = account_division_uid
        self.account_group_uid = account_group_uid
        self.auth_identity_uid = auth_identity_uid
        self.account_email = account_email
        self.display_name = display_name
        self.is_system = is_system
        self.row_instance = row_instance
        self.row_lock = row_lock
        self.row_owner = row_owner
        self.row_seq = row_seq
        self.row_guid = row_guid
        self.row_version = row_version
        self.is_active = is_active
        self.created_date = created_date
        self.created_by = created_by
        self.last_updated_date = last_updated_date
        self.last_updated_by = last_updated_by
        self.removed_date = removed_date
        self.removed_by = removed_by
        self.custom_attributes = custom_attributes
        self.tenant_uid_tenant_name = tenant_uid_tenant_name
        self.tenant_uid_country_uid = tenant_uid_country_uid
        self.tenant_uid_tenant_type_uid = tenant_uid_tenant_type_uid
        self.tenant_uid_tenant_category_uid = tenant_uid_tenant_category_uid
        self.tenant_uid_tenant_code = tenant_uid_tenant_code
        self.tenant_uid_tenant_description = tenant_uid_tenant_description
        self.tenant_uid_start_date = tenant_uid_start_date
        self.tenant_uid_end_date = tenant_uid_end_date
        self.tenant_uid_is_internal = tenant_uid_is_internal
        self.tenant_uid_is_system = tenant_uid_is_system
        self.tenant_uid_is_test = tenant_uid_is_test
        self.tenant_uid_account_uid = tenant_uid_account_uid
        self.account_type_uid_account_type_name = account_type_uid_account_type_name
        self.account_type_uid_account_type_description = account_type_uid_account_type_description
        self.account_title_uid_account_title_name = account_title_uid_account_title_name
        self.account_title_uid_title_description = account_title_uid_title_description
        self.account_division_uid_account_division_name = account_division_uid_account_division_name
        self.account_division_uid_tenant_uid = account_division_uid_tenant_uid
        self.account_division_uid_account_uid = account_division_uid_account_uid
        self.account_division_uid_account_division_template_uid = account_division_uid_account_division_template_uid
        self.account_division_uid_division_description = account_division_uid_division_description
        self.account_group_uid_account_group_name = account_group_uid_account_group_name
        self.account_group_uid_tenant_uid = account_group_uid_tenant_uid
        self.account_group_uid_account_group_description = account_group_uid_account_group_description
        self.auth_identity_uid_auth_identity_name = auth_identity_uid_auth_identity_name
        self.auth_identity_uid_class_name = auth_identity_uid_class_name
        self.auth_identity_uid_default_parameters_json = auth_identity_uid_default_parameters_json
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.account_uid, self.account_name, self.tenant_uid, self.account_type_uid, self.account_title_uid, self.account_division_uid, self.account_group_uid, self.auth_identity_uid, self.account_email, self.display_name, self.is_system, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes, self.tenant_uid_tenant_name, self.tenant_uid_country_uid, self.tenant_uid_tenant_type_uid, self.tenant_uid_tenant_category_uid, self.tenant_uid_tenant_code, self.tenant_uid_tenant_description, self.tenant_uid_start_date, self.tenant_uid_end_date, self.tenant_uid_is_internal, self.tenant_uid_is_system, self.tenant_uid_is_test, self.tenant_uid_account_uid, self.account_type_uid_account_type_name, self.account_type_uid_account_type_description, self.account_title_uid_account_title_name, self.account_title_uid_title_description, self.account_division_uid_account_division_name, self.account_division_uid_tenant_uid, self.account_division_uid_account_uid, self.account_division_uid_account_division_template_uid, self.account_division_uid_division_description, self.account_group_uid_account_group_name, self.account_group_uid_tenant_uid, self.account_group_uid_account_group_description, self.auth_identity_uid_auth_identity_name, self.auth_identity_uid_class_name, self.auth_identity_uid_default_parameters_json]


@dataclass(frozen=False)
class account_division_rich_dto(account_division_read_dto):
    account_division_uid: str | None
    account_division_name: str | None
    tenant_uid: str | None
    account_uid: str | None
    account_division_template_uid: str | None
    division_description: str | None
    row_instance: str | None
    row_lock: str | None
    row_owner: str | None
    row_seq: int | None
    row_guid: str | None
    row_version: int | None
    is_active: int | None
    created_date: datetime.datetime | None
    created_by: str | None
    last_updated_date: datetime.datetime | None
    last_updated_by: str | None
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str | None
    tenant_uid_tenant_name: str | None
    tenant_uid_country_uid: str | None
    tenant_uid_tenant_type_uid: str | None
    tenant_uid_tenant_category_uid: str | None
    tenant_uid_tenant_code: str | None
    tenant_uid_tenant_description: str | None
    tenant_uid_start_date: datetime.datetime | None
    tenant_uid_end_date: datetime.datetime | None
    tenant_uid_is_internal: int | None
    tenant_uid_is_system: int | None
    tenant_uid_is_test: int | None
    tenant_uid_account_uid: str | None
    account_uid_account_name: str | None
    account_uid_tenant_uid: str | None
    account_uid_account_type_uid: str | None
    account_uid_account_title_uid: str | None
    account_uid_account_division_uid: str | None
    account_uid_account_group_uid: str | None
    account_uid_auth_identity_uid: str | None
    account_uid_account_email: str | None
    account_uid_display_name: str | None
    account_uid_is_system: int | None
    account_division_template_uid_account_division_template_name: str | None
    account_division_template_uid_division_description: str | None
    def __init__(self, account_division_uid: str | None, account_division_name: str | None, tenant_uid: str | None, account_uid: str | None, account_division_template_uid: str | None, division_description: str | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None, tenant_uid_tenant_name: str | None, tenant_uid_country_uid: str | None, tenant_uid_tenant_type_uid: str | None, tenant_uid_tenant_category_uid: str | None, tenant_uid_tenant_code: str | None, tenant_uid_tenant_description: str | None, tenant_uid_start_date: datetime.datetime | None, tenant_uid_end_date: datetime.datetime | None, tenant_uid_is_internal: int | None, tenant_uid_is_system: int | None, tenant_uid_is_test: int | None, tenant_uid_account_uid: str | None, account_uid_account_name: str | None, account_uid_tenant_uid: str | None, account_uid_account_type_uid: str | None, account_uid_account_title_uid: str | None, account_uid_account_division_uid: str | None, account_uid_account_group_uid: str | None, account_uid_auth_identity_uid: str | None, account_uid_account_email: str | None, account_uid_display_name: str | None, account_uid_is_system: int | None, account_division_template_uid_account_division_template_name: str | None, account_division_template_uid_division_description: str | None):
        self.account_division_uid = account_division_uid
        self.account_division_name = account_division_name
        self.tenant_uid = tenant_uid
        self.account_uid = account_uid
        self.account_division_template_uid = account_division_template_uid
        self.division_description = division_description
        self.row_instance = row_instance
        self.row_lock = row_lock
        self.row_owner = row_owner
        self.row_seq = row_seq
        self.row_guid = row_guid
        self.row_version = row_version
        self.is_active = is_active
        self.created_date = created_date
        self.created_by = created_by
        self.last_updated_date = last_updated_date
        self.last_updated_by = last_updated_by
        self.removed_date = removed_date
        self.removed_by = removed_by
        self.custom_attributes = custom_attributes
        self.tenant_uid_tenant_name = tenant_uid_tenant_name
        self.tenant_uid_country_uid = tenant_uid_country_uid
        self.tenant_uid_tenant_type_uid = tenant_uid_tenant_type_uid
        self.tenant_uid_tenant_category_uid = tenant_uid_tenant_category_uid
        self.tenant_uid_tenant_code = tenant_uid_tenant_code
        self.tenant_uid_tenant_description = tenant_uid_tenant_description
        self.tenant_uid_start_date = tenant_uid_start_date
        self.tenant_uid_end_date = tenant_uid_end_date
        self.tenant_uid_is_internal = tenant_uid_is_internal
        self.tenant_uid_is_system = tenant_uid_is_system
        self.tenant_uid_is_test = tenant_uid_is_test
        self.tenant_uid_account_uid = tenant_uid_account_uid
        self.account_uid_account_name = account_uid_account_name
        self.account_uid_tenant_uid = account_uid_tenant_uid
        self.account_uid_account_type_uid = account_uid_account_type_uid
        self.account_uid_account_title_uid = account_uid_account_title_uid
        self.account_uid_account_division_uid = account_uid_account_division_uid
        self.account_uid_account_group_uid = account_uid_account_group_uid
        self.account_uid_auth_identity_uid = account_uid_auth_identity_uid
        self.account_uid_account_email = account_uid_account_email
        self.account_uid_display_name = account_uid_display_name
        self.account_uid_is_system = account_uid_is_system
        self.account_division_template_uid_account_division_template_name = account_division_template_uid_account_division_template_name
        self.account_division_template_uid_division_description = account_division_template_uid_division_description
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.account_division_uid, self.account_division_name, self.tenant_uid, self.account_uid, self.account_division_template_uid, self.division_description, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes, self.tenant_uid_tenant_name, self.tenant_uid_country_uid, self.tenant_uid_tenant_type_uid, self.tenant_uid_tenant_category_uid, self.tenant_uid_tenant_code, self.tenant_uid_tenant_description, self.tenant_uid_start_date, self.tenant_uid_end_date, self.tenant_uid_is_internal, self.tenant_uid_is_system, self.tenant_uid_is_test, self.tenant_uid_account_uid, self.account_uid_account_name, self.account_uid_tenant_uid, self.account_uid_account_type_uid, self.account_uid_account_title_uid, self.account_uid_account_division_uid, self.account_uid_account_group_uid, self.account_uid_auth_identity_uid, self.account_uid_account_email, self.account_uid_display_name, self.account_uid_is_system, self.account_division_template_uid_account_division_template_name, self.account_division_template_uid_division_description]


@dataclass(frozen=False)
class account_division_template_rich_dto(account_division_template_read_dto):
    account_division_template_uid: str | None
    account_division_template_name: str | None
    division_description: str | None
    row_instance: str | None
    row_lock: str | None
    row_owner: str | None
    row_seq: int | None
    row_guid: str | None
    row_version: int | None
    is_active: int | None
    created_date: datetime.datetime | None
    created_by: str | None
    last_updated_date: datetime.datetime | None
    last_updated_by: str | None
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str | None
    def __init__(self, account_division_template_uid: str | None, account_division_template_name: str | None, division_description: str | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None):
        self.account_division_template_uid = account_division_template_uid
        self.account_division_template_name = account_division_template_name
        self.division_description = division_description
        self.row_instance = row_instance
        self.row_lock = row_lock
        self.row_owner = row_owner
        self.row_seq = row_seq
        self.row_guid = row_guid
        self.row_version = row_version
        self.is_active = is_active
        self.created_date = created_date
        self.created_by = created_by
        self.last_updated_date = last_updated_date
        self.last_updated_by = last_updated_by
        self.removed_date = removed_date
        self.removed_by = removed_by
        self.custom_attributes = custom_attributes
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.account_division_template_uid, self.account_division_template_name, self.division_description, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]


@dataclass(frozen=False)
class account_group_rich_dto(account_group_read_dto):
    account_group_uid: str | None
    account_group_name: str | None
    tenant_uid: str | None
    account_group_description: str | None
    row_instance: str | None
    row_lock: str | None
    row_owner: str | None
    row_seq: int | None
    row_guid: str | None
    row_version: int | None
    is_active: int | None
    created_date: datetime.datetime | None
    created_by: str | None
    last_updated_date: datetime.datetime | None
    last_updated_by: str | None
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str | None
    tenant_uid_tenant_name: str | None
    tenant_uid_country_uid: str | None
    tenant_uid_tenant_type_uid: str | None
    tenant_uid_tenant_category_uid: str | None
    tenant_uid_tenant_code: str | None
    tenant_uid_tenant_description: str | None
    tenant_uid_start_date: datetime.datetime | None
    tenant_uid_end_date: datetime.datetime | None
    tenant_uid_is_internal: int | None
    tenant_uid_is_system: int | None
    tenant_uid_is_test: int | None
    tenant_uid_account_uid: str | None
    def __init__(self, account_group_uid: str | None, account_group_name: str | None, tenant_uid: str | None, account_group_description: str | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None, tenant_uid_tenant_name: str | None, tenant_uid_country_uid: str | None, tenant_uid_tenant_type_uid: str | None, tenant_uid_tenant_category_uid: str | None, tenant_uid_tenant_code: str | None, tenant_uid_tenant_description: str | None, tenant_uid_start_date: datetime.datetime | None, tenant_uid_end_date: datetime.datetime | None, tenant_uid_is_internal: int | None, tenant_uid_is_system: int | None, tenant_uid_is_test: int | None, tenant_uid_account_uid: str | None):
        self.account_group_uid = account_group_uid
        self.account_group_name = account_group_name
        self.tenant_uid = tenant_uid
        self.account_group_description = account_group_description
        self.row_instance = row_instance
        self.row_lock = row_lock
        self.row_owner = row_owner
        self.row_seq = row_seq
        self.row_guid = row_guid
        self.row_version = row_version
        self.is_active = is_active
        self.created_date = created_date
        self.created_by = created_by
        self.last_updated_date = last_updated_date
        self.last_updated_by = last_updated_by
        self.removed_date = removed_date
        self.removed_by = removed_by
        self.custom_attributes = custom_attributes
        self.tenant_uid_tenant_name = tenant_uid_tenant_name
        self.tenant_uid_country_uid = tenant_uid_country_uid
        self.tenant_uid_tenant_type_uid = tenant_uid_tenant_type_uid
        self.tenant_uid_tenant_category_uid = tenant_uid_tenant_category_uid
        self.tenant_uid_tenant_code = tenant_uid_tenant_code
        self.tenant_uid_tenant_description = tenant_uid_tenant_description
        self.tenant_uid_start_date = tenant_uid_start_date
        self.tenant_uid_end_date = tenant_uid_end_date
        self.tenant_uid_is_internal = tenant_uid_is_internal
        self.tenant_uid_is_system = tenant_uid_is_system
        self.tenant_uid_is_test = tenant_uid_is_test
        self.tenant_uid_account_uid = tenant_uid_account_uid
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.account_group_uid, self.account_group_name, self.tenant_uid, self.account_group_description, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes, self.tenant_uid_tenant_name, self.tenant_uid_country_uid, self.tenant_uid_tenant_type_uid, self.tenant_uid_tenant_category_uid, self.tenant_uid_tenant_code, self.tenant_uid_tenant_description, self.tenant_uid_start_date, self.tenant_uid_end_date, self.tenant_uid_is_internal, self.tenant_uid_is_system, self.tenant_uid_is_test, self.tenant_uid_account_uid]


@dataclass(frozen=False)
class account_hierarchy_rich_dto(account_hierarchy_read_dto):
    account_hierarchy_uid: str | None
    account_hierarchy_name: str | None
    tenant_uid: str | None
    parent_account_uid: str | None
    child_account_uid: str | None
    row_instance: str | None
    row_lock: str | None
    row_owner: str | None
    row_seq: int | None
    row_guid: str | None
    row_version: int | None
    is_active: int | None
    created_date: datetime.datetime | None
    created_by: str | None
    last_updated_date: datetime.datetime | None
    last_updated_by: str | None
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str | None
    tenant_uid_tenant_name: str | None
    tenant_uid_country_uid: str | None
    tenant_uid_tenant_type_uid: str | None
    tenant_uid_tenant_category_uid: str | None
    tenant_uid_tenant_code: str | None
    tenant_uid_tenant_description: str | None
    tenant_uid_start_date: datetime.datetime | None
    tenant_uid_end_date: datetime.datetime | None
    tenant_uid_is_internal: int | None
    tenant_uid_is_system: int | None
    tenant_uid_is_test: int | None
    tenant_uid_account_uid: str | None
    parent_account_uid_account_name: str | None
    parent_account_uid_tenant_uid: str | None
    parent_account_uid_account_type_uid: str | None
    parent_account_uid_account_title_uid: str | None
    parent_account_uid_account_division_uid: str | None
    parent_account_uid_account_group_uid: str | None
    parent_account_uid_auth_identity_uid: str | None
    parent_account_uid_account_email: str | None
    parent_account_uid_display_name: str | None
    parent_account_uid_is_system: int | None
    child_account_uid_account_name: str | None
    child_account_uid_tenant_uid: str | None
    child_account_uid_account_type_uid: str | None
    child_account_uid_account_title_uid: str | None
    child_account_uid_account_division_uid: str | None
    child_account_uid_account_group_uid: str | None
    child_account_uid_auth_identity_uid: str | None
    child_account_uid_account_email: str | None
    child_account_uid_display_name: str | None
    child_account_uid_is_system: int | None
    def __init__(self, account_hierarchy_uid: str | None, account_hierarchy_name: str | None, tenant_uid: str | None, parent_account_uid: str | None, child_account_uid: str | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None, tenant_uid_tenant_name: str | None, tenant_uid_country_uid: str | None, tenant_uid_tenant_type_uid: str | None, tenant_uid_tenant_category_uid: str | None, tenant_uid_tenant_code: str | None, tenant_uid_tenant_description: str | None, tenant_uid_start_date: datetime.datetime | None, tenant_uid_end_date: datetime.datetime | None, tenant_uid_is_internal: int | None, tenant_uid_is_system: int | None, tenant_uid_is_test: int | None, tenant_uid_account_uid: str | None, parent_account_uid_account_name: str | None, parent_account_uid_tenant_uid: str | None, parent_account_uid_account_type_uid: str | None, parent_account_uid_account_title_uid: str | None, parent_account_uid_account_division_uid: str | None, parent_account_uid_account_group_uid: str | None, parent_account_uid_auth_identity_uid: str | None, parent_account_uid_account_email: str | None, parent_account_uid_display_name: str | None, parent_account_uid_is_system: int | None, child_account_uid_account_name: str | None, child_account_uid_tenant_uid: str | None, child_account_uid_account_type_uid: str | None, child_account_uid_account_title_uid: str | None, child_account_uid_account_division_uid: str | None, child_account_uid_account_group_uid: str | None, child_account_uid_auth_identity_uid: str | None, child_account_uid_account_email: str | None, child_account_uid_display_name: str | None, child_account_uid_is_system: int | None):
        self.account_hierarchy_uid = account_hierarchy_uid
        self.account_hierarchy_name = account_hierarchy_name
        self.tenant_uid = tenant_uid
        self.parent_account_uid = parent_account_uid
        self.child_account_uid = child_account_uid
        self.row_instance = row_instance
        self.row_lock = row_lock
        self.row_owner = row_owner
        self.row_seq = row_seq
        self.row_guid = row_guid
        self.row_version = row_version
        self.is_active = is_active
        self.created_date = created_date
        self.created_by = created_by
        self.last_updated_date = last_updated_date
        self.last_updated_by = last_updated_by
        self.removed_date = removed_date
        self.removed_by = removed_by
        self.custom_attributes = custom_attributes
        self.tenant_uid_tenant_name = tenant_uid_tenant_name
        self.tenant_uid_country_uid = tenant_uid_country_uid
        self.tenant_uid_tenant_type_uid = tenant_uid_tenant_type_uid
        self.tenant_uid_tenant_category_uid = tenant_uid_tenant_category_uid
        self.tenant_uid_tenant_code = tenant_uid_tenant_code
        self.tenant_uid_tenant_description = tenant_uid_tenant_description
        self.tenant_uid_start_date = tenant_uid_start_date
        self.tenant_uid_end_date = tenant_uid_end_date
        self.tenant_uid_is_internal = tenant_uid_is_internal
        self.tenant_uid_is_system = tenant_uid_is_system
        self.tenant_uid_is_test = tenant_uid_is_test
        self.tenant_uid_account_uid = tenant_uid_account_uid
        self.parent_account_uid_account_name = parent_account_uid_account_name
        self.parent_account_uid_tenant_uid = parent_account_uid_tenant_uid
        self.parent_account_uid_account_type_uid = parent_account_uid_account_type_uid
        self.parent_account_uid_account_title_uid = parent_account_uid_account_title_uid
        self.parent_account_uid_account_division_uid = parent_account_uid_account_division_uid
        self.parent_account_uid_account_group_uid = parent_account_uid_account_group_uid
        self.parent_account_uid_auth_identity_uid = parent_account_uid_auth_identity_uid
        self.parent_account_uid_account_email = parent_account_uid_account_email
        self.parent_account_uid_display_name = parent_account_uid_display_name
        self.parent_account_uid_is_system = parent_account_uid_is_system
        self.child_account_uid_account_name = child_account_uid_account_name
        self.child_account_uid_tenant_uid = child_account_uid_tenant_uid
        self.child_account_uid_account_type_uid = child_account_uid_account_type_uid
        self.child_account_uid_account_title_uid = child_account_uid_account_title_uid
        self.child_account_uid_account_division_uid = child_account_uid_account_division_uid
        self.child_account_uid_account_group_uid = child_account_uid_account_group_uid
        self.child_account_uid_auth_identity_uid = child_account_uid_auth_identity_uid
        self.child_account_uid_account_email = child_account_uid_account_email
        self.child_account_uid_display_name = child_account_uid_display_name
        self.child_account_uid_is_system = child_account_uid_is_system
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.account_hierarchy_uid, self.account_hierarchy_name, self.tenant_uid, self.parent_account_uid, self.child_account_uid, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes, self.tenant_uid_tenant_name, self.tenant_uid_country_uid, self.tenant_uid_tenant_type_uid, self.tenant_uid_tenant_category_uid, self.tenant_uid_tenant_code, self.tenant_uid_tenant_description, self.tenant_uid_start_date, self.tenant_uid_end_date, self.tenant_uid_is_internal, self.tenant_uid_is_system, self.tenant_uid_is_test, self.tenant_uid_account_uid, self.parent_account_uid_account_name, self.parent_account_uid_tenant_uid, self.parent_account_uid_account_type_uid, self.parent_account_uid_account_title_uid, self.parent_account_uid_account_division_uid, self.parent_account_uid_account_group_uid, self.parent_account_uid_auth_identity_uid, self.parent_account_uid_account_email, self.parent_account_uid_display_name, self.parent_account_uid_is_system, self.child_account_uid_account_name, self.child_account_uid_tenant_uid, self.child_account_uid_account_type_uid, self.child_account_uid_account_title_uid, self.child_account_uid_account_division_uid, self.child_account_uid_account_group_uid, self.child_account_uid_auth_identity_uid, self.child_account_uid_account_email, self.child_account_uid_display_name, self.child_account_uid_is_system]


@dataclass(frozen=False)
class account_rate_rich_dto(account_rate_read_dto):
    account_rate_uid: str | None
    account_rate_name: str | None
    tenant_uid: str | None
    account_uid: str | None
    currency_uid: str | None
    rate: str | None
    start_date: datetime.datetime | None
    end_date: datetime.datetime | None
    row_instance: str | None
    row_lock: str | None
    row_owner: str | None
    row_seq: int | None
    row_guid: str | None
    row_version: int | None
    is_active: int | None
    created_date: datetime.datetime | None
    created_by: str | None
    last_updated_date: datetime.datetime | None
    last_updated_by: str | None
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str | None
    tenant_uid_tenant_name: str | None
    tenant_uid_country_uid: str | None
    tenant_uid_tenant_type_uid: str | None
    tenant_uid_tenant_category_uid: str | None
    tenant_uid_tenant_code: str | None
    tenant_uid_tenant_description: str | None
    tenant_uid_start_date: datetime.datetime | None
    tenant_uid_end_date: datetime.datetime | None
    tenant_uid_is_internal: int | None
    tenant_uid_is_system: int | None
    tenant_uid_is_test: int | None
    tenant_uid_account_uid: str | None
    account_uid_account_name: str | None
    account_uid_tenant_uid: str | None
    account_uid_account_type_uid: str | None
    account_uid_account_title_uid: str | None
    account_uid_account_division_uid: str | None
    account_uid_account_group_uid: str | None
    account_uid_auth_identity_uid: str | None
    account_uid_account_email: str | None
    account_uid_display_name: str | None
    account_uid_is_system: int | None
    currency_uid_currency_name: str | None
    currency_uid_is_focused: int | None
    def __init__(self, account_rate_uid: str | None, account_rate_name: str | None, tenant_uid: str | None, account_uid: str | None, currency_uid: str | None, rate: str | None, start_date: datetime.datetime | None, end_date: datetime.datetime | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None, tenant_uid_tenant_name: str | None, tenant_uid_country_uid: str | None, tenant_uid_tenant_type_uid: str | None, tenant_uid_tenant_category_uid: str | None, tenant_uid_tenant_code: str | None, tenant_uid_tenant_description: str | None, tenant_uid_start_date: datetime.datetime | None, tenant_uid_end_date: datetime.datetime | None, tenant_uid_is_internal: int | None, tenant_uid_is_system: int | None, tenant_uid_is_test: int | None, tenant_uid_account_uid: str | None, account_uid_account_name: str | None, account_uid_tenant_uid: str | None, account_uid_account_type_uid: str | None, account_uid_account_title_uid: str | None, account_uid_account_division_uid: str | None, account_uid_account_group_uid: str | None, account_uid_auth_identity_uid: str | None, account_uid_account_email: str | None, account_uid_display_name: str | None, account_uid_is_system: int | None, currency_uid_currency_name: str | None, currency_uid_is_focused: int | None):
        self.account_rate_uid = account_rate_uid
        self.account_rate_name = account_rate_name
        self.tenant_uid = tenant_uid
        self.account_uid = account_uid
        self.currency_uid = currency_uid
        self.rate = rate
        self.start_date = start_date
        self.end_date = end_date
        self.row_instance = row_instance
        self.row_lock = row_lock
        self.row_owner = row_owner
        self.row_seq = row_seq
        self.row_guid = row_guid
        self.row_version = row_version
        self.is_active = is_active
        self.created_date = created_date
        self.created_by = created_by
        self.last_updated_date = last_updated_date
        self.last_updated_by = last_updated_by
        self.removed_date = removed_date
        self.removed_by = removed_by
        self.custom_attributes = custom_attributes
        self.tenant_uid_tenant_name = tenant_uid_tenant_name
        self.tenant_uid_country_uid = tenant_uid_country_uid
        self.tenant_uid_tenant_type_uid = tenant_uid_tenant_type_uid
        self.tenant_uid_tenant_category_uid = tenant_uid_tenant_category_uid
        self.tenant_uid_tenant_code = tenant_uid_tenant_code
        self.tenant_uid_tenant_description = tenant_uid_tenant_description
        self.tenant_uid_start_date = tenant_uid_start_date
        self.tenant_uid_end_date = tenant_uid_end_date
        self.tenant_uid_is_internal = tenant_uid_is_internal
        self.tenant_uid_is_system = tenant_uid_is_system
        self.tenant_uid_is_test = tenant_uid_is_test
        self.tenant_uid_account_uid = tenant_uid_account_uid
        self.account_uid_account_name = account_uid_account_name
        self.account_uid_tenant_uid = account_uid_tenant_uid
        self.account_uid_account_type_uid = account_uid_account_type_uid
        self.account_uid_account_title_uid = account_uid_account_title_uid
        self.account_uid_account_division_uid = account_uid_account_division_uid
        self.account_uid_account_group_uid = account_uid_account_group_uid
        self.account_uid_auth_identity_uid = account_uid_auth_identity_uid
        self.account_uid_account_email = account_uid_account_email
        self.account_uid_display_name = account_uid_display_name
        self.account_uid_is_system = account_uid_is_system
        self.currency_uid_currency_name = currency_uid_currency_name
        self.currency_uid_is_focused = currency_uid_is_focused
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.account_rate_uid, self.account_rate_name, self.tenant_uid, self.account_uid, self.currency_uid, self.rate, self.start_date, self.end_date, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes, self.tenant_uid_tenant_name, self.tenant_uid_country_uid, self.tenant_uid_tenant_type_uid, self.tenant_uid_tenant_category_uid, self.tenant_uid_tenant_code, self.tenant_uid_tenant_description, self.tenant_uid_start_date, self.tenant_uid_end_date, self.tenant_uid_is_internal, self.tenant_uid_is_system, self.tenant_uid_is_test, self.tenant_uid_account_uid, self.account_uid_account_name, self.account_uid_tenant_uid, self.account_uid_account_type_uid, self.account_uid_account_title_uid, self.account_uid_account_division_uid, self.account_uid_account_group_uid, self.account_uid_auth_identity_uid, self.account_uid_account_email, self.account_uid_display_name, self.account_uid_is_system, self.currency_uid_currency_name, self.currency_uid_is_focused]


@dataclass(frozen=False)
class account_skill_rich_dto(account_skill_read_dto):
    account_skill_uid: str | None
    account_skill_name: str | None
    account_skill_description: str | None
    row_instance: str | None
    row_lock: str | None
    row_owner: str | None
    row_seq: int | None
    row_guid: str | None
    row_version: int | None
    is_active: int | None
    created_date: datetime.datetime | None
    created_by: str | None
    last_updated_date: datetime.datetime | None
    last_updated_by: str | None
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str | None
    def __init__(self, account_skill_uid: str | None, account_skill_name: str | None, account_skill_description: str | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None):
        self.account_skill_uid = account_skill_uid
        self.account_skill_name = account_skill_name
        self.account_skill_description = account_skill_description
        self.row_instance = row_instance
        self.row_lock = row_lock
        self.row_owner = row_owner
        self.row_seq = row_seq
        self.row_guid = row_guid
        self.row_version = row_version
        self.is_active = is_active
        self.created_date = created_date
        self.created_by = created_by
        self.last_updated_date = last_updated_date
        self.last_updated_by = last_updated_by
        self.removed_date = removed_date
        self.removed_by = removed_by
        self.custom_attributes = custom_attributes
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.account_skill_uid, self.account_skill_name, self.account_skill_description, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]


@dataclass(frozen=False)
class account_team_rich_dto(account_team_read_dto):
    account_team_uid: str | None
    account_team_name: str | None
    tenant_uid: str | None
    owner_account_uid: str | None
    is_public: int | None
    is_tenant: int | None
    is_private: int | None
    row_instance: str | None
    row_lock: str | None
    row_owner: str | None
    row_seq: int | None
    row_guid: str | None
    row_version: int | None
    is_active: int | None
    created_date: datetime.datetime | None
    created_by: str | None
    last_updated_date: datetime.datetime | None
    last_updated_by: str | None
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str | None
    tenant_uid_tenant_name: str | None
    tenant_uid_country_uid: str | None
    tenant_uid_tenant_type_uid: str | None
    tenant_uid_tenant_category_uid: str | None
    tenant_uid_tenant_code: str | None
    tenant_uid_tenant_description: str | None
    tenant_uid_start_date: datetime.datetime | None
    tenant_uid_end_date: datetime.datetime | None
    tenant_uid_is_internal: int | None
    tenant_uid_is_system: int | None
    tenant_uid_is_test: int | None
    tenant_uid_account_uid: str | None
    owner_account_uid_account_name: str | None
    owner_account_uid_tenant_uid: str | None
    owner_account_uid_account_type_uid: str | None
    owner_account_uid_account_title_uid: str | None
    owner_account_uid_account_division_uid: str | None
    owner_account_uid_account_group_uid: str | None
    owner_account_uid_auth_identity_uid: str | None
    owner_account_uid_account_email: str | None
    owner_account_uid_display_name: str | None
    owner_account_uid_is_system: int | None
    def __init__(self, account_team_uid: str | None, account_team_name: str | None, tenant_uid: str | None, owner_account_uid: str | None, is_public: int | None, is_tenant: int | None, is_private: int | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None, tenant_uid_tenant_name: str | None, tenant_uid_country_uid: str | None, tenant_uid_tenant_type_uid: str | None, tenant_uid_tenant_category_uid: str | None, tenant_uid_tenant_code: str | None, tenant_uid_tenant_description: str | None, tenant_uid_start_date: datetime.datetime | None, tenant_uid_end_date: datetime.datetime | None, tenant_uid_is_internal: int | None, tenant_uid_is_system: int | None, tenant_uid_is_test: int | None, tenant_uid_account_uid: str | None, owner_account_uid_account_name: str | None, owner_account_uid_tenant_uid: str | None, owner_account_uid_account_type_uid: str | None, owner_account_uid_account_title_uid: str | None, owner_account_uid_account_division_uid: str | None, owner_account_uid_account_group_uid: str | None, owner_account_uid_auth_identity_uid: str | None, owner_account_uid_account_email: str | None, owner_account_uid_display_name: str | None, owner_account_uid_is_system: int | None):
        self.account_team_uid = account_team_uid
        self.account_team_name = account_team_name
        self.tenant_uid = tenant_uid
        self.owner_account_uid = owner_account_uid
        self.is_public = is_public
        self.is_tenant = is_tenant
        self.is_private = is_private
        self.row_instance = row_instance
        self.row_lock = row_lock
        self.row_owner = row_owner
        self.row_seq = row_seq
        self.row_guid = row_guid
        self.row_version = row_version
        self.is_active = is_active
        self.created_date = created_date
        self.created_by = created_by
        self.last_updated_date = last_updated_date
        self.last_updated_by = last_updated_by
        self.removed_date = removed_date
        self.removed_by = removed_by
        self.custom_attributes = custom_attributes
        self.tenant_uid_tenant_name = tenant_uid_tenant_name
        self.tenant_uid_country_uid = tenant_uid_country_uid
        self.tenant_uid_tenant_type_uid = tenant_uid_tenant_type_uid
        self.tenant_uid_tenant_category_uid = tenant_uid_tenant_category_uid
        self.tenant_uid_tenant_code = tenant_uid_tenant_code
        self.tenant_uid_tenant_description = tenant_uid_tenant_description
        self.tenant_uid_start_date = tenant_uid_start_date
        self.tenant_uid_end_date = tenant_uid_end_date
        self.tenant_uid_is_internal = tenant_uid_is_internal
        self.tenant_uid_is_system = tenant_uid_is_system
        self.tenant_uid_is_test = tenant_uid_is_test
        self.tenant_uid_account_uid = tenant_uid_account_uid
        self.owner_account_uid_account_name = owner_account_uid_account_name
        self.owner_account_uid_tenant_uid = owner_account_uid_tenant_uid
        self.owner_account_uid_account_type_uid = owner_account_uid_account_type_uid
        self.owner_account_uid_account_title_uid = owner_account_uid_account_title_uid
        self.owner_account_uid_account_division_uid = owner_account_uid_account_division_uid
        self.owner_account_uid_account_group_uid = owner_account_uid_account_group_uid
        self.owner_account_uid_auth_identity_uid = owner_account_uid_auth_identity_uid
        self.owner_account_uid_account_email = owner_account_uid_account_email
        self.owner_account_uid_display_name = owner_account_uid_display_name
        self.owner_account_uid_is_system = owner_account_uid_is_system
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.account_team_uid, self.account_team_name, self.tenant_uid, self.owner_account_uid, self.is_public, self.is_tenant, self.is_private, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes, self.tenant_uid_tenant_name, self.tenant_uid_country_uid, self.tenant_uid_tenant_type_uid, self.tenant_uid_tenant_category_uid, self.tenant_uid_tenant_code, self.tenant_uid_tenant_description, self.tenant_uid_start_date, self.tenant_uid_end_date, self.tenant_uid_is_internal, self.tenant_uid_is_system, self.tenant_uid_is_test, self.tenant_uid_account_uid, self.owner_account_uid_account_name, self.owner_account_uid_tenant_uid, self.owner_account_uid_account_type_uid, self.owner_account_uid_account_title_uid, self.owner_account_uid_account_division_uid, self.owner_account_uid_account_group_uid, self.owner_account_uid_auth_identity_uid, self.owner_account_uid_account_email, self.owner_account_uid_display_name, self.owner_account_uid_is_system]


@dataclass(frozen=False)
class account_title_rich_dto(account_title_read_dto):
    account_title_uid: str | None
    account_title_name: str | None
    title_description: str | None
    row_instance: str | None
    row_lock: str | None
    row_owner: str | None
    row_seq: int | None
    row_guid: str | None
    row_version: int | None
    is_active: int | None
    created_date: datetime.datetime | None
    created_by: str | None
    last_updated_date: datetime.datetime | None
    last_updated_by: str | None
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str | None
    def __init__(self, account_title_uid: str | None, account_title_name: str | None, title_description: str | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None):
        self.account_title_uid = account_title_uid
        self.account_title_name = account_title_name
        self.title_description = title_description
        self.row_instance = row_instance
        self.row_lock = row_lock
        self.row_owner = row_owner
        self.row_seq = row_seq
        self.row_guid = row_guid
        self.row_version = row_version
        self.is_active = is_active
        self.created_date = created_date
        self.created_by = created_by
        self.last_updated_date = last_updated_date
        self.last_updated_by = last_updated_by
        self.removed_date = removed_date
        self.removed_by = removed_by
        self.custom_attributes = custom_attributes
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.account_title_uid, self.account_title_name, self.title_description, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]


@dataclass(frozen=False)
class account_title_responsibility_rich_dto(account_title_responsibility_read_dto):
    account_title_responsibility_uid: str | None
    account_title_responsibility_name: str | None
    tenant_uid: str | None
    account_title_uid: str | None
    responsibility_description: str | None
    responsibility_priority: int | None
    row_instance: str | None
    row_lock: str | None
    row_owner: str | None
    row_seq: int | None
    row_guid: str | None
    row_version: int | None
    is_active: int | None
    created_date: datetime.datetime | None
    created_by: str | None
    last_updated_date: datetime.datetime | None
    last_updated_by: str | None
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str | None
    tenant_uid_tenant_name: str | None
    tenant_uid_country_uid: str | None
    tenant_uid_tenant_type_uid: str | None
    tenant_uid_tenant_category_uid: str | None
    tenant_uid_tenant_code: str | None
    tenant_uid_tenant_description: str | None
    tenant_uid_start_date: datetime.datetime | None
    tenant_uid_end_date: datetime.datetime | None
    tenant_uid_is_internal: int | None
    tenant_uid_is_system: int | None
    tenant_uid_is_test: int | None
    tenant_uid_account_uid: str | None
    account_title_uid_account_title_name: str | None
    account_title_uid_title_description: str | None
    def __init__(self, account_title_responsibility_uid: str | None, account_title_responsibility_name: str | None, tenant_uid: str | None, account_title_uid: str | None, responsibility_description: str | None, responsibility_priority: int | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None, tenant_uid_tenant_name: str | None, tenant_uid_country_uid: str | None, tenant_uid_tenant_type_uid: str | None, tenant_uid_tenant_category_uid: str | None, tenant_uid_tenant_code: str | None, tenant_uid_tenant_description: str | None, tenant_uid_start_date: datetime.datetime | None, tenant_uid_end_date: datetime.datetime | None, tenant_uid_is_internal: int | None, tenant_uid_is_system: int | None, tenant_uid_is_test: int | None, tenant_uid_account_uid: str | None, account_title_uid_account_title_name: str | None, account_title_uid_title_description: str | None):
        self.account_title_responsibility_uid = account_title_responsibility_uid
        self.account_title_responsibility_name = account_title_responsibility_name
        self.tenant_uid = tenant_uid
        self.account_title_uid = account_title_uid
        self.responsibility_description = responsibility_description
        self.responsibility_priority = responsibility_priority
        self.row_instance = row_instance
        self.row_lock = row_lock
        self.row_owner = row_owner
        self.row_seq = row_seq
        self.row_guid = row_guid
        self.row_version = row_version
        self.is_active = is_active
        self.created_date = created_date
        self.created_by = created_by
        self.last_updated_date = last_updated_date
        self.last_updated_by = last_updated_by
        self.removed_date = removed_date
        self.removed_by = removed_by
        self.custom_attributes = custom_attributes
        self.tenant_uid_tenant_name = tenant_uid_tenant_name
        self.tenant_uid_country_uid = tenant_uid_country_uid
        self.tenant_uid_tenant_type_uid = tenant_uid_tenant_type_uid
        self.tenant_uid_tenant_category_uid = tenant_uid_tenant_category_uid
        self.tenant_uid_tenant_code = tenant_uid_tenant_code
        self.tenant_uid_tenant_description = tenant_uid_tenant_description
        self.tenant_uid_start_date = tenant_uid_start_date
        self.tenant_uid_end_date = tenant_uid_end_date
        self.tenant_uid_is_internal = tenant_uid_is_internal
        self.tenant_uid_is_system = tenant_uid_is_system
        self.tenant_uid_is_test = tenant_uid_is_test
        self.tenant_uid_account_uid = tenant_uid_account_uid
        self.account_title_uid_account_title_name = account_title_uid_account_title_name
        self.account_title_uid_title_description = account_title_uid_title_description
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.account_title_responsibility_uid, self.account_title_responsibility_name, self.tenant_uid, self.account_title_uid, self.responsibility_description, self.responsibility_priority, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes, self.tenant_uid_tenant_name, self.tenant_uid_country_uid, self.tenant_uid_tenant_type_uid, self.tenant_uid_tenant_category_uid, self.tenant_uid_tenant_code, self.tenant_uid_tenant_description, self.tenant_uid_start_date, self.tenant_uid_end_date, self.tenant_uid_is_internal, self.tenant_uid_is_system, self.tenant_uid_is_test, self.tenant_uid_account_uid, self.account_title_uid_account_title_name, self.account_title_uid_title_description]


@dataclass(frozen=False)
class account_type_rich_dto(account_type_read_dto):
    account_type_uid: str | None
    account_type_name: str | None
    account_type_description: str | None
    row_instance: str | None
    row_lock: str | None
    row_owner: str | None
    row_seq: int | None
    row_guid: str | None
    row_version: int | None
    is_active: int | None
    created_date: datetime.datetime | None
    created_by: str | None
    last_updated_date: datetime.datetime | None
    last_updated_by: str | None
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str | None
    def __init__(self, account_type_uid: str | None, account_type_name: str | None, account_type_description: str | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None):
        self.account_type_uid = account_type_uid
        self.account_type_name = account_type_name
        self.account_type_description = account_type_description
        self.row_instance = row_instance
        self.row_lock = row_lock
        self.row_owner = row_owner
        self.row_seq = row_seq
        self.row_guid = row_guid
        self.row_version = row_version
        self.is_active = is_active
        self.created_date = created_date
        self.created_by = created_by
        self.last_updated_date = last_updated_date
        self.last_updated_by = last_updated_by
        self.removed_date = removed_date
        self.removed_by = removed_by
        self.custom_attributes = custom_attributes
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.account_type_uid, self.account_type_name, self.account_type_description, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]


@dataclass(frozen=False)
class audit_change_rich_dto(audit_change_read_dto):
    system_change_uid: str | None
    system_change_name: str | None
    account_uid: str | None
    audit_type_uid: str | None
    change_type: str | None
    change_json: str | None
    row_instance: str | None
    row_lock: str | None
    row_owner: str | None
    row_seq: int | None
    row_guid: str | None
    row_version: int | None
    is_active: int | None
    created_date: datetime.datetime | None
    created_by: str | None
    last_updated_date: datetime.datetime | None
    last_updated_by: str | None
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str | None
    account_uid_account_name: str | None
    account_uid_tenant_uid: str | None
    account_uid_account_type_uid: str | None
    account_uid_account_title_uid: str | None
    account_uid_account_division_uid: str | None
    account_uid_account_group_uid: str | None
    account_uid_auth_identity_uid: str | None
    account_uid_account_email: str | None
    account_uid_display_name: str | None
    account_uid_is_system: int | None
    audit_type_uid_audit_type_name: str | None
    def __init__(self, system_change_uid: str | None, system_change_name: str | None, account_uid: str | None, audit_type_uid: str | None, change_type: str | None, change_json: str | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None, account_uid_account_name: str | None, account_uid_tenant_uid: str | None, account_uid_account_type_uid: str | None, account_uid_account_title_uid: str | None, account_uid_account_division_uid: str | None, account_uid_account_group_uid: str | None, account_uid_auth_identity_uid: str | None, account_uid_account_email: str | None, account_uid_display_name: str | None, account_uid_is_system: int | None, audit_type_uid_audit_type_name: str | None):
        self.system_change_uid = system_change_uid
        self.system_change_name = system_change_name
        self.account_uid = account_uid
        self.audit_type_uid = audit_type_uid
        self.change_type = change_type
        self.change_json = change_json
        self.row_instance = row_instance
        self.row_lock = row_lock
        self.row_owner = row_owner
        self.row_seq = row_seq
        self.row_guid = row_guid
        self.row_version = row_version
        self.is_active = is_active
        self.created_date = created_date
        self.created_by = created_by
        self.last_updated_date = last_updated_date
        self.last_updated_by = last_updated_by
        self.removed_date = removed_date
        self.removed_by = removed_by
        self.custom_attributes = custom_attributes
        self.account_uid_account_name = account_uid_account_name
        self.account_uid_tenant_uid = account_uid_tenant_uid
        self.account_uid_account_type_uid = account_uid_account_type_uid
        self.account_uid_account_title_uid = account_uid_account_title_uid
        self.account_uid_account_division_uid = account_uid_account_division_uid
        self.account_uid_account_group_uid = account_uid_account_group_uid
        self.account_uid_auth_identity_uid = account_uid_auth_identity_uid
        self.account_uid_account_email = account_uid_account_email
        self.account_uid_display_name = account_uid_display_name
        self.account_uid_is_system = account_uid_is_system
        self.audit_type_uid_audit_type_name = audit_type_uid_audit_type_name
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.system_change_uid, self.system_change_name, self.account_uid, self.audit_type_uid, self.change_type, self.change_json, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes, self.account_uid_account_name, self.account_uid_tenant_uid, self.account_uid_account_type_uid, self.account_uid_account_title_uid, self.account_uid_account_division_uid, self.account_uid_account_group_uid, self.account_uid_auth_identity_uid, self.account_uid_account_email, self.account_uid_display_name, self.account_uid_is_system, self.audit_type_uid_audit_type_name]


@dataclass(frozen=False)
class audit_type_rich_dto(audit_type_read_dto):
    audit_type_uid: str | None
    audit_type_name: str | None
    row_instance: str | None
    row_lock: str | None
    row_owner: str | None
    row_seq: int | None
    row_guid: str | None
    row_version: int | None
    is_active: int | None
    created_date: datetime.datetime | None
    created_by: str | None
    last_updated_date: datetime.datetime | None
    last_updated_by: str | None
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str | None
    def __init__(self, audit_type_uid: str | None, audit_type_name: str | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None):
        self.audit_type_uid = audit_type_uid
        self.audit_type_name = audit_type_name
        self.row_instance = row_instance
        self.row_lock = row_lock
        self.row_owner = row_owner
        self.row_seq = row_seq
        self.row_guid = row_guid
        self.row_version = row_version
        self.is_active = is_active
        self.created_date = created_date
        self.created_by = created_by
        self.last_updated_date = last_updated_date
        self.last_updated_by = last_updated_by
        self.removed_date = removed_date
        self.removed_by = removed_by
        self.custom_attributes = custom_attributes
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.audit_type_uid, self.audit_type_name, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]


@dataclass(frozen=False)
class auth_attempt_rich_dto(auth_attempt_read_dto):
    auth_attempt_uid: str | None
    auth_attempt_name: str | None
    tenant_uid: str | None
    account_uid: str | None
    account_login: str | None
    identity_type: str | None
    identity_parameters: str | None
    last_status_name: str | None
    row_instance: str | None
    row_lock: str | None
    row_owner: str | None
    row_seq: int | None
    row_guid: str | None
    row_version: int | None
    is_active: int | None
    created_date: datetime.datetime | None
    created_by: str | None
    last_updated_date: datetime.datetime | None
    last_updated_by: str | None
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str | None
    tenant_uid_tenant_name: str | None
    tenant_uid_country_uid: str | None
    tenant_uid_tenant_type_uid: str | None
    tenant_uid_tenant_category_uid: str | None
    tenant_uid_tenant_code: str | None
    tenant_uid_tenant_description: str | None
    tenant_uid_start_date: datetime.datetime | None
    tenant_uid_end_date: datetime.datetime | None
    tenant_uid_is_internal: int | None
    tenant_uid_is_system: int | None
    tenant_uid_is_test: int | None
    tenant_uid_account_uid: str | None
    account_uid_account_name: str | None
    account_uid_tenant_uid: str | None
    account_uid_account_type_uid: str | None
    account_uid_account_title_uid: str | None
    account_uid_account_division_uid: str | None
    account_uid_account_group_uid: str | None
    account_uid_auth_identity_uid: str | None
    account_uid_account_email: str | None
    account_uid_display_name: str | None
    account_uid_is_system: int | None
    def __init__(self, auth_attempt_uid: str | None, auth_attempt_name: str | None, tenant_uid: str | None, account_uid: str | None, account_login: str | None, identity_type: str | None, identity_parameters: str | None, last_status_name: str | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None, tenant_uid_tenant_name: str | None, tenant_uid_country_uid: str | None, tenant_uid_tenant_type_uid: str | None, tenant_uid_tenant_category_uid: str | None, tenant_uid_tenant_code: str | None, tenant_uid_tenant_description: str | None, tenant_uid_start_date: datetime.datetime | None, tenant_uid_end_date: datetime.datetime | None, tenant_uid_is_internal: int | None, tenant_uid_is_system: int | None, tenant_uid_is_test: int | None, tenant_uid_account_uid: str | None, account_uid_account_name: str | None, account_uid_tenant_uid: str | None, account_uid_account_type_uid: str | None, account_uid_account_title_uid: str | None, account_uid_account_division_uid: str | None, account_uid_account_group_uid: str | None, account_uid_auth_identity_uid: str | None, account_uid_account_email: str | None, account_uid_display_name: str | None, account_uid_is_system: int | None):
        self.auth_attempt_uid = auth_attempt_uid
        self.auth_attempt_name = auth_attempt_name
        self.tenant_uid = tenant_uid
        self.account_uid = account_uid
        self.account_login = account_login
        self.identity_type = identity_type
        self.identity_parameters = identity_parameters
        self.last_status_name = last_status_name
        self.row_instance = row_instance
        self.row_lock = row_lock
        self.row_owner = row_owner
        self.row_seq = row_seq
        self.row_guid = row_guid
        self.row_version = row_version
        self.is_active = is_active
        self.created_date = created_date
        self.created_by = created_by
        self.last_updated_date = last_updated_date
        self.last_updated_by = last_updated_by
        self.removed_date = removed_date
        self.removed_by = removed_by
        self.custom_attributes = custom_attributes
        self.tenant_uid_tenant_name = tenant_uid_tenant_name
        self.tenant_uid_country_uid = tenant_uid_country_uid
        self.tenant_uid_tenant_type_uid = tenant_uid_tenant_type_uid
        self.tenant_uid_tenant_category_uid = tenant_uid_tenant_category_uid
        self.tenant_uid_tenant_code = tenant_uid_tenant_code
        self.tenant_uid_tenant_description = tenant_uid_tenant_description
        self.tenant_uid_start_date = tenant_uid_start_date
        self.tenant_uid_end_date = tenant_uid_end_date
        self.tenant_uid_is_internal = tenant_uid_is_internal
        self.tenant_uid_is_system = tenant_uid_is_system
        self.tenant_uid_is_test = tenant_uid_is_test
        self.tenant_uid_account_uid = tenant_uid_account_uid
        self.account_uid_account_name = account_uid_account_name
        self.account_uid_tenant_uid = account_uid_tenant_uid
        self.account_uid_account_type_uid = account_uid_account_type_uid
        self.account_uid_account_title_uid = account_uid_account_title_uid
        self.account_uid_account_division_uid = account_uid_account_division_uid
        self.account_uid_account_group_uid = account_uid_account_group_uid
        self.account_uid_auth_identity_uid = account_uid_auth_identity_uid
        self.account_uid_account_email = account_uid_account_email
        self.account_uid_display_name = account_uid_display_name
        self.account_uid_is_system = account_uid_is_system
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.auth_attempt_uid, self.auth_attempt_name, self.tenant_uid, self.account_uid, self.account_login, self.identity_type, self.identity_parameters, self.last_status_name, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes, self.tenant_uid_tenant_name, self.tenant_uid_country_uid, self.tenant_uid_tenant_type_uid, self.tenant_uid_tenant_category_uid, self.tenant_uid_tenant_code, self.tenant_uid_tenant_description, self.tenant_uid_start_date, self.tenant_uid_end_date, self.tenant_uid_is_internal, self.tenant_uid_is_system, self.tenant_uid_is_test, self.tenant_uid_account_uid, self.account_uid_account_name, self.account_uid_tenant_uid, self.account_uid_account_type_uid, self.account_uid_account_title_uid, self.account_uid_account_division_uid, self.account_uid_account_group_uid, self.account_uid_auth_identity_uid, self.account_uid_account_email, self.account_uid_display_name, self.account_uid_is_system]


@dataclass(frozen=False)
class auth_identity_rich_dto(auth_identity_read_dto):
    auth_identity_uid: str | None
    auth_identity_name: str | None
    class_name: str | None
    default_parameters_json: str | None
    row_instance: str | None
    row_lock: str | None
    row_owner: str | None
    row_seq: int | None
    row_guid: str | None
    row_version: int | None
    is_active: int | None
    created_date: datetime.datetime | None
    created_by: str | None
    last_updated_date: datetime.datetime | None
    last_updated_by: str | None
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str | None
    def __init__(self, auth_identity_uid: str | None, auth_identity_name: str | None, class_name: str | None, default_parameters_json: str | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None):
        self.auth_identity_uid = auth_identity_uid
        self.auth_identity_name = auth_identity_name
        self.class_name = class_name
        self.default_parameters_json = default_parameters_json
        self.row_instance = row_instance
        self.row_lock = row_lock
        self.row_owner = row_owner
        self.row_seq = row_seq
        self.row_guid = row_guid
        self.row_version = row_version
        self.is_active = is_active
        self.created_date = created_date
        self.created_by = created_by
        self.last_updated_date = last_updated_date
        self.last_updated_by = last_updated_by
        self.removed_date = removed_date
        self.removed_by = removed_by
        self.custom_attributes = custom_attributes
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.auth_identity_uid, self.auth_identity_name, self.class_name, self.default_parameters_json, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]


@dataclass(frozen=False)
class auth_identity_tenant_rich_dto(auth_identity_tenant_read_dto):
    auth_identity_tenant_uid: str | None
    auth_identity_tenant_name: str | None
    tenant_uid: str | None
    auth_identity_uid: str | None
    auth_sso_uid: str | None
    identity_parameters_json: str | None
    last_status_name: str | None
    row_instance: str | None
    row_lock: str | None
    row_owner: str | None
    row_seq: int | None
    row_guid: str | None
    row_version: int | None
    is_active: int | None
    created_date: datetime.datetime | None
    created_by: str | None
    last_updated_date: datetime.datetime | None
    last_updated_by: str | None
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str | None
    auth_identity_tenant_uid_tenant_name: str | None
    auth_identity_tenant_uid_country_uid: str | None
    auth_identity_tenant_uid_tenant_type_uid: str | None
    auth_identity_tenant_uid_tenant_category_uid: str | None
    auth_identity_tenant_uid_tenant_code: str | None
    auth_identity_tenant_uid_tenant_description: str | None
    auth_identity_tenant_uid_start_date: datetime.datetime | None
    auth_identity_tenant_uid_end_date: datetime.datetime | None
    auth_identity_tenant_uid_is_internal: int | None
    auth_identity_tenant_uid_is_system: int | None
    auth_identity_tenant_uid_is_test: int | None
    auth_identity_tenant_uid_account_uid: str | None
    tenant_uid_tenant_name: str | None
    tenant_uid_country_uid: str | None
    tenant_uid_tenant_type_uid: str | None
    tenant_uid_tenant_category_uid: str | None
    tenant_uid_tenant_code: str | None
    tenant_uid_tenant_description: str | None
    tenant_uid_start_date: datetime.datetime | None
    tenant_uid_end_date: datetime.datetime | None
    tenant_uid_is_internal: int | None
    tenant_uid_is_system: int | None
    tenant_uid_is_test: int | None
    tenant_uid_account_uid: str | None
    auth_identity_uid_auth_identity_name: str | None
    auth_identity_uid_class_name: str | None
    auth_identity_uid_default_parameters_json: str | None
    auth_sso_uid_auth_sso_name: str | None
    auth_sso_uid_tenant_uid: str | None
    auth_sso_uid_owner_account_uid: str | None
    auth_sso_uid_sso_name: str | None
    auth_sso_uid_sso_url: str | None
    auth_sso_uid_sso_key: str | None
    auth_sso_uid_sso_secret: str | None
    auth_sso_uid_sso_code: str | None
    auth_sso_uid_clientid: str | None
    auth_sso_uid_clientsecret: str | None
    auth_sso_uid_callback_url: str | None
    def __init__(self, auth_identity_tenant_uid: str | None, auth_identity_tenant_name: str | None, tenant_uid: str | None, auth_identity_uid: str | None, auth_sso_uid: str | None, identity_parameters_json: str | None, last_status_name: str | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None, auth_identity_tenant_uid_tenant_name: str | None, auth_identity_tenant_uid_country_uid: str | None, auth_identity_tenant_uid_tenant_type_uid: str | None, auth_identity_tenant_uid_tenant_category_uid: str | None, auth_identity_tenant_uid_tenant_code: str | None, auth_identity_tenant_uid_tenant_description: str | None, auth_identity_tenant_uid_start_date: datetime.datetime | None, auth_identity_tenant_uid_end_date: datetime.datetime | None, auth_identity_tenant_uid_is_internal: int | None, auth_identity_tenant_uid_is_system: int | None, auth_identity_tenant_uid_is_test: int | None, auth_identity_tenant_uid_account_uid: str | None, tenant_uid_tenant_name: str | None, tenant_uid_country_uid: str | None, tenant_uid_tenant_type_uid: str | None, tenant_uid_tenant_category_uid: str | None, tenant_uid_tenant_code: str | None, tenant_uid_tenant_description: str | None, tenant_uid_start_date: datetime.datetime | None, tenant_uid_end_date: datetime.datetime | None, tenant_uid_is_internal: int | None, tenant_uid_is_system: int | None, tenant_uid_is_test: int | None, tenant_uid_account_uid: str | None, auth_identity_uid_auth_identity_name: str | None, auth_identity_uid_class_name: str | None, auth_identity_uid_default_parameters_json: str | None, auth_sso_uid_auth_sso_name: str | None, auth_sso_uid_tenant_uid: str | None, auth_sso_uid_owner_account_uid: str | None, auth_sso_uid_sso_name: str | None, auth_sso_uid_sso_url: str | None, auth_sso_uid_sso_key: str | None, auth_sso_uid_sso_secret: str | None, auth_sso_uid_sso_code: str | None, auth_sso_uid_clientid: str | None, auth_sso_uid_clientsecret: str | None, auth_sso_uid_callback_url: str | None):
        self.auth_identity_tenant_uid = auth_identity_tenant_uid
        self.auth_identity_tenant_name = auth_identity_tenant_name
        self.tenant_uid = tenant_uid
        self.auth_identity_uid = auth_identity_uid
        self.auth_sso_uid = auth_sso_uid
        self.identity_parameters_json = identity_parameters_json
        self.last_status_name = last_status_name
        self.row_instance = row_instance
        self.row_lock = row_lock
        self.row_owner = row_owner
        self.row_seq = row_seq
        self.row_guid = row_guid
        self.row_version = row_version
        self.is_active = is_active
        self.created_date = created_date
        self.created_by = created_by
        self.last_updated_date = last_updated_date
        self.last_updated_by = last_updated_by
        self.removed_date = removed_date
        self.removed_by = removed_by
        self.custom_attributes = custom_attributes
        self.auth_identity_tenant_uid_tenant_name = auth_identity_tenant_uid_tenant_name
        self.auth_identity_tenant_uid_country_uid = auth_identity_tenant_uid_country_uid
        self.auth_identity_tenant_uid_tenant_type_uid = auth_identity_tenant_uid_tenant_type_uid
        self.auth_identity_tenant_uid_tenant_category_uid = auth_identity_tenant_uid_tenant_category_uid
        self.auth_identity_tenant_uid_tenant_code = auth_identity_tenant_uid_tenant_code
        self.auth_identity_tenant_uid_tenant_description = auth_identity_tenant_uid_tenant_description
        self.auth_identity_tenant_uid_start_date = auth_identity_tenant_uid_start_date
        self.auth_identity_tenant_uid_end_date = auth_identity_tenant_uid_end_date
        self.auth_identity_tenant_uid_is_internal = auth_identity_tenant_uid_is_internal
        self.auth_identity_tenant_uid_is_system = auth_identity_tenant_uid_is_system
        self.auth_identity_tenant_uid_is_test = auth_identity_tenant_uid_is_test
        self.auth_identity_tenant_uid_account_uid = auth_identity_tenant_uid_account_uid
        self.tenant_uid_tenant_name = tenant_uid_tenant_name
        self.tenant_uid_country_uid = tenant_uid_country_uid
        self.tenant_uid_tenant_type_uid = tenant_uid_tenant_type_uid
        self.tenant_uid_tenant_category_uid = tenant_uid_tenant_category_uid
        self.tenant_uid_tenant_code = tenant_uid_tenant_code
        self.tenant_uid_tenant_description = tenant_uid_tenant_description
        self.tenant_uid_start_date = tenant_uid_start_date
        self.tenant_uid_end_date = tenant_uid_end_date
        self.tenant_uid_is_internal = tenant_uid_is_internal
        self.tenant_uid_is_system = tenant_uid_is_system
        self.tenant_uid_is_test = tenant_uid_is_test
        self.tenant_uid_account_uid = tenant_uid_account_uid
        self.auth_identity_uid_auth_identity_name = auth_identity_uid_auth_identity_name
        self.auth_identity_uid_class_name = auth_identity_uid_class_name
        self.auth_identity_uid_default_parameters_json = auth_identity_uid_default_parameters_json
        self.auth_sso_uid_auth_sso_name = auth_sso_uid_auth_sso_name
        self.auth_sso_uid_tenant_uid = auth_sso_uid_tenant_uid
        self.auth_sso_uid_owner_account_uid = auth_sso_uid_owner_account_uid
        self.auth_sso_uid_sso_name = auth_sso_uid_sso_name
        self.auth_sso_uid_sso_url = auth_sso_uid_sso_url
        self.auth_sso_uid_sso_key = auth_sso_uid_sso_key
        self.auth_sso_uid_sso_secret = auth_sso_uid_sso_secret
        self.auth_sso_uid_sso_code = auth_sso_uid_sso_code
        self.auth_sso_uid_clientid = auth_sso_uid_clientid
        self.auth_sso_uid_clientsecret = auth_sso_uid_clientsecret
        self.auth_sso_uid_callback_url = auth_sso_uid_callback_url
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.auth_identity_tenant_uid, self.auth_identity_tenant_name, self.tenant_uid, self.auth_identity_uid, self.auth_sso_uid, self.identity_parameters_json, self.last_status_name, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes, self.auth_identity_tenant_uid_tenant_name, self.auth_identity_tenant_uid_country_uid, self.auth_identity_tenant_uid_tenant_type_uid, self.auth_identity_tenant_uid_tenant_category_uid, self.auth_identity_tenant_uid_tenant_code, self.auth_identity_tenant_uid_tenant_description, self.auth_identity_tenant_uid_start_date, self.auth_identity_tenant_uid_end_date, self.auth_identity_tenant_uid_is_internal, self.auth_identity_tenant_uid_is_system, self.auth_identity_tenant_uid_is_test, self.auth_identity_tenant_uid_account_uid, self.tenant_uid_tenant_name, self.tenant_uid_country_uid, self.tenant_uid_tenant_type_uid, self.tenant_uid_tenant_category_uid, self.tenant_uid_tenant_code, self.tenant_uid_tenant_description, self.tenant_uid_start_date, self.tenant_uid_end_date, self.tenant_uid_is_internal, self.tenant_uid_is_system, self.tenant_uid_is_test, self.tenant_uid_account_uid, self.auth_identity_uid_auth_identity_name, self.auth_identity_uid_class_name, self.auth_identity_uid_default_parameters_json, self.auth_sso_uid_auth_sso_name, self.auth_sso_uid_tenant_uid, self.auth_sso_uid_owner_account_uid, self.auth_sso_uid_sso_name, self.auth_sso_uid_sso_url, self.auth_sso_uid_sso_key, self.auth_sso_uid_sso_secret, self.auth_sso_uid_sso_code, self.auth_sso_uid_clientid, self.auth_sso_uid_clientsecret, self.auth_sso_uid_callback_url]


@dataclass(frozen=False)
class auth_key_rich_dto(auth_key_read_dto):
    auth_key_uid: str | None
    auth_key_name: str | None
    tenant_uid: str | None
    owner_account_uid: str | None
    auth_key_type_uid: str | None
    key_private: str | None
    key_public: str | None
    key_length: int | None
    key_exponent: str | None
    key_modulus: str | None
    key_parameters_json: str | None
    row_instance: str | None
    row_lock: str | None
    row_owner: str | None
    row_seq: int | None
    row_guid: str | None
    row_version: int | None
    is_active: int | None
    created_date: datetime.datetime | None
    created_by: str | None
    last_updated_date: datetime.datetime | None
    last_updated_by: str | None
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str | None
    tenant_uid_tenant_name: str | None
    tenant_uid_country_uid: str | None
    tenant_uid_tenant_type_uid: str | None
    tenant_uid_tenant_category_uid: str | None
    tenant_uid_tenant_code: str | None
    tenant_uid_tenant_description: str | None
    tenant_uid_start_date: datetime.datetime | None
    tenant_uid_end_date: datetime.datetime | None
    tenant_uid_is_internal: int | None
    tenant_uid_is_system: int | None
    tenant_uid_is_test: int | None
    tenant_uid_account_uid: str | None
    owner_account_uid_account_name: str | None
    owner_account_uid_tenant_uid: str | None
    owner_account_uid_account_type_uid: str | None
    owner_account_uid_account_title_uid: str | None
    owner_account_uid_account_division_uid: str | None
    owner_account_uid_account_group_uid: str | None
    owner_account_uid_auth_identity_uid: str | None
    owner_account_uid_account_email: str | None
    owner_account_uid_display_name: str | None
    owner_account_uid_is_system: int | None
    auth_key_type_uid_auth_key_type_name: str | None
    auth_key_type_uid_class_name: str | None
    def __init__(self, auth_key_uid: str | None, auth_key_name: str | None, tenant_uid: str | None, owner_account_uid: str | None, auth_key_type_uid: str | None, key_private: str | None, key_public: str | None, key_length: int | None, key_exponent: str | None, key_modulus: str | None, key_parameters_json: str | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None, tenant_uid_tenant_name: str | None, tenant_uid_country_uid: str | None, tenant_uid_tenant_type_uid: str | None, tenant_uid_tenant_category_uid: str | None, tenant_uid_tenant_code: str | None, tenant_uid_tenant_description: str | None, tenant_uid_start_date: datetime.datetime | None, tenant_uid_end_date: datetime.datetime | None, tenant_uid_is_internal: int | None, tenant_uid_is_system: int | None, tenant_uid_is_test: int | None, tenant_uid_account_uid: str | None, owner_account_uid_account_name: str | None, owner_account_uid_tenant_uid: str | None, owner_account_uid_account_type_uid: str | None, owner_account_uid_account_title_uid: str | None, owner_account_uid_account_division_uid: str | None, owner_account_uid_account_group_uid: str | None, owner_account_uid_auth_identity_uid: str | None, owner_account_uid_account_email: str | None, owner_account_uid_display_name: str | None, owner_account_uid_is_system: int | None, auth_key_type_uid_auth_key_type_name: str | None, auth_key_type_uid_class_name: str | None):
        self.auth_key_uid = auth_key_uid
        self.auth_key_name = auth_key_name
        self.tenant_uid = tenant_uid
        self.owner_account_uid = owner_account_uid
        self.auth_key_type_uid = auth_key_type_uid
        self.key_private = key_private
        self.key_public = key_public
        self.key_length = key_length
        self.key_exponent = key_exponent
        self.key_modulus = key_modulus
        self.key_parameters_json = key_parameters_json
        self.row_instance = row_instance
        self.row_lock = row_lock
        self.row_owner = row_owner
        self.row_seq = row_seq
        self.row_guid = row_guid
        self.row_version = row_version
        self.is_active = is_active
        self.created_date = created_date
        self.created_by = created_by
        self.last_updated_date = last_updated_date
        self.last_updated_by = last_updated_by
        self.removed_date = removed_date
        self.removed_by = removed_by
        self.custom_attributes = custom_attributes
        self.tenant_uid_tenant_name = tenant_uid_tenant_name
        self.tenant_uid_country_uid = tenant_uid_country_uid
        self.tenant_uid_tenant_type_uid = tenant_uid_tenant_type_uid
        self.tenant_uid_tenant_category_uid = tenant_uid_tenant_category_uid
        self.tenant_uid_tenant_code = tenant_uid_tenant_code
        self.tenant_uid_tenant_description = tenant_uid_tenant_description
        self.tenant_uid_start_date = tenant_uid_start_date
        self.tenant_uid_end_date = tenant_uid_end_date
        self.tenant_uid_is_internal = tenant_uid_is_internal
        self.tenant_uid_is_system = tenant_uid_is_system
        self.tenant_uid_is_test = tenant_uid_is_test
        self.tenant_uid_account_uid = tenant_uid_account_uid
        self.owner_account_uid_account_name = owner_account_uid_account_name
        self.owner_account_uid_tenant_uid = owner_account_uid_tenant_uid
        self.owner_account_uid_account_type_uid = owner_account_uid_account_type_uid
        self.owner_account_uid_account_title_uid = owner_account_uid_account_title_uid
        self.owner_account_uid_account_division_uid = owner_account_uid_account_division_uid
        self.owner_account_uid_account_group_uid = owner_account_uid_account_group_uid
        self.owner_account_uid_auth_identity_uid = owner_account_uid_auth_identity_uid
        self.owner_account_uid_account_email = owner_account_uid_account_email
        self.owner_account_uid_display_name = owner_account_uid_display_name
        self.owner_account_uid_is_system = owner_account_uid_is_system
        self.auth_key_type_uid_auth_key_type_name = auth_key_type_uid_auth_key_type_name
        self.auth_key_type_uid_class_name = auth_key_type_uid_class_name
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.auth_key_uid, self.auth_key_name, self.tenant_uid, self.owner_account_uid, self.auth_key_type_uid, self.key_private, self.key_public, self.key_length, self.key_exponent, self.key_modulus, self.key_parameters_json, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes, self.tenant_uid_tenant_name, self.tenant_uid_country_uid, self.tenant_uid_tenant_type_uid, self.tenant_uid_tenant_category_uid, self.tenant_uid_tenant_code, self.tenant_uid_tenant_description, self.tenant_uid_start_date, self.tenant_uid_end_date, self.tenant_uid_is_internal, self.tenant_uid_is_system, self.tenant_uid_is_test, self.tenant_uid_account_uid, self.owner_account_uid_account_name, self.owner_account_uid_tenant_uid, self.owner_account_uid_account_type_uid, self.owner_account_uid_account_title_uid, self.owner_account_uid_account_division_uid, self.owner_account_uid_account_group_uid, self.owner_account_uid_auth_identity_uid, self.owner_account_uid_account_email, self.owner_account_uid_display_name, self.owner_account_uid_is_system, self.auth_key_type_uid_auth_key_type_name, self.auth_key_type_uid_class_name]


@dataclass(frozen=False)
class auth_key_type_rich_dto(auth_key_type_read_dto):
    auth_key_type_uid: str | None
    auth_key_type_name: str | None
    class_name: str | None
    row_instance: str | None
    row_lock: str | None
    row_owner: str | None
    row_seq: int | None
    row_guid: str | None
    row_version: int | None
    is_active: int | None
    created_date: datetime.datetime | None
    created_by: str | None
    last_updated_date: datetime.datetime | None
    last_updated_by: str | None
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str | None
    def __init__(self, auth_key_type_uid: str | None, auth_key_type_name: str | None, class_name: str | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None):
        self.auth_key_type_uid = auth_key_type_uid
        self.auth_key_type_name = auth_key_type_name
        self.class_name = class_name
        self.row_instance = row_instance
        self.row_lock = row_lock
        self.row_owner = row_owner
        self.row_seq = row_seq
        self.row_guid = row_guid
        self.row_version = row_version
        self.is_active = is_active
        self.created_date = created_date
        self.created_by = created_by
        self.last_updated_date = last_updated_date
        self.last_updated_by = last_updated_by
        self.removed_date = removed_date
        self.removed_by = removed_by
        self.custom_attributes = custom_attributes
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.auth_key_type_uid, self.auth_key_type_name, self.class_name, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]


@dataclass(frozen=False)
class auth_password_rich_dto(auth_password_read_dto):
    auth_password_uid: str | None
    auth_password_name: str | None
    tenant_uid: str | None
    account_uid: str | None
    password_hash: str | None
    password_salt: str | None
    date_from: datetime.datetime | None
    date_to: datetime.datetime | None
    usage_count: int | None
    row_instance: str | None
    row_lock: str | None
    row_owner: str | None
    row_seq: int | None
    row_guid: str | None
    row_version: int | None
    is_active: int | None
    created_date: datetime.datetime | None
    created_by: str | None
    last_updated_date: datetime.datetime | None
    last_updated_by: str | None
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str | None
    tenant_uid_tenant_name: str | None
    tenant_uid_country_uid: str | None
    tenant_uid_tenant_type_uid: str | None
    tenant_uid_tenant_category_uid: str | None
    tenant_uid_tenant_code: str | None
    tenant_uid_tenant_description: str | None
    tenant_uid_start_date: datetime.datetime | None
    tenant_uid_end_date: datetime.datetime | None
    tenant_uid_is_internal: int | None
    tenant_uid_is_system: int | None
    tenant_uid_is_test: int | None
    tenant_uid_account_uid: str | None
    account_uid_account_name: str | None
    account_uid_tenant_uid: str | None
    account_uid_account_type_uid: str | None
    account_uid_account_title_uid: str | None
    account_uid_account_division_uid: str | None
    account_uid_account_group_uid: str | None
    account_uid_auth_identity_uid: str | None
    account_uid_account_email: str | None
    account_uid_display_name: str | None
    account_uid_is_system: int | None
    def __init__(self, auth_password_uid: str | None, auth_password_name: str | None, tenant_uid: str | None, account_uid: str | None, password_hash: str | None, password_salt: str | None, date_from: datetime.datetime | None, date_to: datetime.datetime | None, usage_count: int | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None, tenant_uid_tenant_name: str | None, tenant_uid_country_uid: str | None, tenant_uid_tenant_type_uid: str | None, tenant_uid_tenant_category_uid: str | None, tenant_uid_tenant_code: str | None, tenant_uid_tenant_description: str | None, tenant_uid_start_date: datetime.datetime | None, tenant_uid_end_date: datetime.datetime | None, tenant_uid_is_internal: int | None, tenant_uid_is_system: int | None, tenant_uid_is_test: int | None, tenant_uid_account_uid: str | None, account_uid_account_name: str | None, account_uid_tenant_uid: str | None, account_uid_account_type_uid: str | None, account_uid_account_title_uid: str | None, account_uid_account_division_uid: str | None, account_uid_account_group_uid: str | None, account_uid_auth_identity_uid: str | None, account_uid_account_email: str | None, account_uid_display_name: str | None, account_uid_is_system: int | None):
        self.auth_password_uid = auth_password_uid
        self.auth_password_name = auth_password_name
        self.tenant_uid = tenant_uid
        self.account_uid = account_uid
        self.password_hash = password_hash
        self.password_salt = password_salt
        self.date_from = date_from
        self.date_to = date_to
        self.usage_count = usage_count
        self.row_instance = row_instance
        self.row_lock = row_lock
        self.row_owner = row_owner
        self.row_seq = row_seq
        self.row_guid = row_guid
        self.row_version = row_version
        self.is_active = is_active
        self.created_date = created_date
        self.created_by = created_by
        self.last_updated_date = last_updated_date
        self.last_updated_by = last_updated_by
        self.removed_date = removed_date
        self.removed_by = removed_by
        self.custom_attributes = custom_attributes
        self.tenant_uid_tenant_name = tenant_uid_tenant_name
        self.tenant_uid_country_uid = tenant_uid_country_uid
        self.tenant_uid_tenant_type_uid = tenant_uid_tenant_type_uid
        self.tenant_uid_tenant_category_uid = tenant_uid_tenant_category_uid
        self.tenant_uid_tenant_code = tenant_uid_tenant_code
        self.tenant_uid_tenant_description = tenant_uid_tenant_description
        self.tenant_uid_start_date = tenant_uid_start_date
        self.tenant_uid_end_date = tenant_uid_end_date
        self.tenant_uid_is_internal = tenant_uid_is_internal
        self.tenant_uid_is_system = tenant_uid_is_system
        self.tenant_uid_is_test = tenant_uid_is_test
        self.tenant_uid_account_uid = tenant_uid_account_uid
        self.account_uid_account_name = account_uid_account_name
        self.account_uid_tenant_uid = account_uid_tenant_uid
        self.account_uid_account_type_uid = account_uid_account_type_uid
        self.account_uid_account_title_uid = account_uid_account_title_uid
        self.account_uid_account_division_uid = account_uid_account_division_uid
        self.account_uid_account_group_uid = account_uid_account_group_uid
        self.account_uid_auth_identity_uid = account_uid_auth_identity_uid
        self.account_uid_account_email = account_uid_account_email
        self.account_uid_display_name = account_uid_display_name
        self.account_uid_is_system = account_uid_is_system
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.auth_password_uid, self.auth_password_name, self.tenant_uid, self.account_uid, self.password_hash, self.password_salt, self.date_from, self.date_to, self.usage_count, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes, self.tenant_uid_tenant_name, self.tenant_uid_country_uid, self.tenant_uid_tenant_type_uid, self.tenant_uid_tenant_category_uid, self.tenant_uid_tenant_code, self.tenant_uid_tenant_description, self.tenant_uid_start_date, self.tenant_uid_end_date, self.tenant_uid_is_internal, self.tenant_uid_is_system, self.tenant_uid_is_test, self.tenant_uid_account_uid, self.account_uid_account_name, self.account_uid_tenant_uid, self.account_uid_account_type_uid, self.account_uid_account_title_uid, self.account_uid_account_division_uid, self.account_uid_account_group_uid, self.account_uid_auth_identity_uid, self.account_uid_account_email, self.account_uid_display_name, self.account_uid_is_system]


@dataclass(frozen=False)
class auth_password_current_rich_dto(auth_password_current_read_dto):
    auth_password_current_uid: str | None
    auth_password_current_name: str | None
    tenant_uid: str | None
    account_uid: str | None
    password_hash: str | None
    password_salt: str | None
    date_from: datetime.datetime | None
    date_to: datetime.datetime | None
    usage_count: int | None
    row_instance: str | None
    row_lock: str | None
    row_owner: str | None
    row_seq: int | None
    row_guid: str | None
    row_version: int | None
    is_active: int | None
    created_date: datetime.datetime | None
    created_by: str | None
    last_updated_date: datetime.datetime | None
    last_updated_by: str | None
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str | None
    tenant_uid_tenant_name: str | None
    tenant_uid_country_uid: str | None
    tenant_uid_tenant_type_uid: str | None
    tenant_uid_tenant_category_uid: str | None
    tenant_uid_tenant_code: str | None
    tenant_uid_tenant_description: str | None
    tenant_uid_start_date: datetime.datetime | None
    tenant_uid_end_date: datetime.datetime | None
    tenant_uid_is_internal: int | None
    tenant_uid_is_system: int | None
    tenant_uid_is_test: int | None
    tenant_uid_account_uid: str | None
    account_uid_account_name: str | None
    account_uid_tenant_uid: str | None
    account_uid_account_type_uid: str | None
    account_uid_account_title_uid: str | None
    account_uid_account_division_uid: str | None
    account_uid_account_group_uid: str | None
    account_uid_auth_identity_uid: str | None
    account_uid_account_email: str | None
    account_uid_display_name: str | None
    account_uid_is_system: int | None
    def __init__(self, auth_password_current_uid: str | None, auth_password_current_name: str | None, tenant_uid: str | None, account_uid: str | None, password_hash: str | None, password_salt: str | None, date_from: datetime.datetime | None, date_to: datetime.datetime | None, usage_count: int | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None, tenant_uid_tenant_name: str | None, tenant_uid_country_uid: str | None, tenant_uid_tenant_type_uid: str | None, tenant_uid_tenant_category_uid: str | None, tenant_uid_tenant_code: str | None, tenant_uid_tenant_description: str | None, tenant_uid_start_date: datetime.datetime | None, tenant_uid_end_date: datetime.datetime | None, tenant_uid_is_internal: int | None, tenant_uid_is_system: int | None, tenant_uid_is_test: int | None, tenant_uid_account_uid: str | None, account_uid_account_name: str | None, account_uid_tenant_uid: str | None, account_uid_account_type_uid: str | None, account_uid_account_title_uid: str | None, account_uid_account_division_uid: str | None, account_uid_account_group_uid: str | None, account_uid_auth_identity_uid: str | None, account_uid_account_email: str | None, account_uid_display_name: str | None, account_uid_is_system: int | None):
        self.auth_password_current_uid = auth_password_current_uid
        self.auth_password_current_name = auth_password_current_name
        self.tenant_uid = tenant_uid
        self.account_uid = account_uid
        self.password_hash = password_hash
        self.password_salt = password_salt
        self.date_from = date_from
        self.date_to = date_to
        self.usage_count = usage_count
        self.row_instance = row_instance
        self.row_lock = row_lock
        self.row_owner = row_owner
        self.row_seq = row_seq
        self.row_guid = row_guid
        self.row_version = row_version
        self.is_active = is_active
        self.created_date = created_date
        self.created_by = created_by
        self.last_updated_date = last_updated_date
        self.last_updated_by = last_updated_by
        self.removed_date = removed_date
        self.removed_by = removed_by
        self.custom_attributes = custom_attributes
        self.tenant_uid_tenant_name = tenant_uid_tenant_name
        self.tenant_uid_country_uid = tenant_uid_country_uid
        self.tenant_uid_tenant_type_uid = tenant_uid_tenant_type_uid
        self.tenant_uid_tenant_category_uid = tenant_uid_tenant_category_uid
        self.tenant_uid_tenant_code = tenant_uid_tenant_code
        self.tenant_uid_tenant_description = tenant_uid_tenant_description
        self.tenant_uid_start_date = tenant_uid_start_date
        self.tenant_uid_end_date = tenant_uid_end_date
        self.tenant_uid_is_internal = tenant_uid_is_internal
        self.tenant_uid_is_system = tenant_uid_is_system
        self.tenant_uid_is_test = tenant_uid_is_test
        self.tenant_uid_account_uid = tenant_uid_account_uid
        self.account_uid_account_name = account_uid_account_name
        self.account_uid_tenant_uid = account_uid_tenant_uid
        self.account_uid_account_type_uid = account_uid_account_type_uid
        self.account_uid_account_title_uid = account_uid_account_title_uid
        self.account_uid_account_division_uid = account_uid_account_division_uid
        self.account_uid_account_group_uid = account_uid_account_group_uid
        self.account_uid_auth_identity_uid = account_uid_auth_identity_uid
        self.account_uid_account_email = account_uid_account_email
        self.account_uid_display_name = account_uid_display_name
        self.account_uid_is_system = account_uid_is_system
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.auth_password_current_uid, self.auth_password_current_name, self.tenant_uid, self.account_uid, self.password_hash, self.password_salt, self.date_from, self.date_to, self.usage_count, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes, self.tenant_uid_tenant_name, self.tenant_uid_country_uid, self.tenant_uid_tenant_type_uid, self.tenant_uid_tenant_category_uid, self.tenant_uid_tenant_code, self.tenant_uid_tenant_description, self.tenant_uid_start_date, self.tenant_uid_end_date, self.tenant_uid_is_internal, self.tenant_uid_is_system, self.tenant_uid_is_test, self.tenant_uid_account_uid, self.account_uid_account_name, self.account_uid_tenant_uid, self.account_uid_account_type_uid, self.account_uid_account_title_uid, self.account_uid_account_division_uid, self.account_uid_account_group_uid, self.account_uid_auth_identity_uid, self.account_uid_account_email, self.account_uid_display_name, self.account_uid_is_system]


@dataclass(frozen=False)
class auth_password_rule_rich_dto(auth_password_rule_read_dto):
    auth_password_uid: str | None
    auth_password_name: str | None
    rule_type: int | None
    rule_parameters: str | None
    user_scope: str | None
    row_instance: str | None
    row_lock: str | None
    row_owner: str | None
    row_seq: int | None
    row_guid: str | None
    row_version: int | None
    is_active: int | None
    created_date: datetime.datetime | None
    created_by: str | None
    last_updated_date: datetime.datetime | None
    last_updated_by: str | None
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str | None
    auth_password_uid_auth_password_name: str | None
    auth_password_uid_tenant_uid: str | None
    auth_password_uid_account_uid: str | None
    auth_password_uid_password_hash: str | None
    auth_password_uid_password_salt: str | None
    auth_password_uid_date_from: datetime.datetime | None
    auth_password_uid_date_to: datetime.datetime | None
    auth_password_uid_usage_count: int | None
    def __init__(self, auth_password_uid: str | None, auth_password_name: str | None, rule_type: int | None, rule_parameters: str | None, user_scope: str | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None, auth_password_uid_auth_password_name: str | None, auth_password_uid_tenant_uid: str | None, auth_password_uid_account_uid: str | None, auth_password_uid_password_hash: str | None, auth_password_uid_password_salt: str | None, auth_password_uid_date_from: datetime.datetime | None, auth_password_uid_date_to: datetime.datetime | None, auth_password_uid_usage_count: int | None):
        self.auth_password_uid = auth_password_uid
        self.auth_password_name = auth_password_name
        self.rule_type = rule_type
        self.rule_parameters = rule_parameters
        self.user_scope = user_scope
        self.row_instance = row_instance
        self.row_lock = row_lock
        self.row_owner = row_owner
        self.row_seq = row_seq
        self.row_guid = row_guid
        self.row_version = row_version
        self.is_active = is_active
        self.created_date = created_date
        self.created_by = created_by
        self.last_updated_date = last_updated_date
        self.last_updated_by = last_updated_by
        self.removed_date = removed_date
        self.removed_by = removed_by
        self.custom_attributes = custom_attributes
        self.auth_password_uid_auth_password_name = auth_password_uid_auth_password_name
        self.auth_password_uid_tenant_uid = auth_password_uid_tenant_uid
        self.auth_password_uid_account_uid = auth_password_uid_account_uid
        self.auth_password_uid_password_hash = auth_password_uid_password_hash
        self.auth_password_uid_password_salt = auth_password_uid_password_salt
        self.auth_password_uid_date_from = auth_password_uid_date_from
        self.auth_password_uid_date_to = auth_password_uid_date_to
        self.auth_password_uid_usage_count = auth_password_uid_usage_count
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.auth_password_uid, self.auth_password_name, self.rule_type, self.rule_parameters, self.user_scope, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes, self.auth_password_uid_auth_password_name, self.auth_password_uid_tenant_uid, self.auth_password_uid_account_uid, self.auth_password_uid_password_hash, self.auth_password_uid_password_salt, self.auth_password_uid_date_from, self.auth_password_uid_date_to, self.auth_password_uid_usage_count]


@dataclass(frozen=False)
class auth_permission_rich_dto(auth_permission_read_dto):
    auth_permission_uid: str | None
    auth_permission_name: str | None
    tenant_uid: str | None
    account_uid: str | None
    auth_role_uid: str | None
    client_uid: str | None
    project_instance_uid: str | None
    valid_from_date: datetime.datetime | None
    valid_till_date: datetime.datetime | None
    row_instance: str | None
    row_lock: str | None
    row_owner: str | None
    row_seq: int | None
    row_guid: str | None
    row_version: int | None
    is_active: int | None
    created_date: datetime.datetime | None
    created_by: str | None
    last_updated_date: datetime.datetime | None
    last_updated_by: str | None
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str | None
    tenant_uid_tenant_name: str | None
    tenant_uid_country_uid: str | None
    tenant_uid_tenant_type_uid: str | None
    tenant_uid_tenant_category_uid: str | None
    tenant_uid_tenant_code: str | None
    tenant_uid_tenant_description: str | None
    tenant_uid_start_date: datetime.datetime | None
    tenant_uid_end_date: datetime.datetime | None
    tenant_uid_is_internal: int | None
    tenant_uid_is_system: int | None
    tenant_uid_is_test: int | None
    tenant_uid_account_uid: str | None
    account_uid_account_name: str | None
    account_uid_tenant_uid: str | None
    account_uid_account_type_uid: str | None
    account_uid_account_title_uid: str | None
    account_uid_account_division_uid: str | None
    account_uid_account_group_uid: str | None
    account_uid_auth_identity_uid: str | None
    account_uid_account_email: str | None
    account_uid_display_name: str | None
    account_uid_is_system: int | None
    auth_role_uid_auth_role_name: str | None
    auth_role_uid_parent_auth_role_uid: str | None
    auth_role_uid_tenant_uid: str | None
    auth_role_uid_role_description: str | None
    auth_role_uid_access_uris: str | None
    auth_role_uid_is_project: int | None
    auth_role_uid_is_tenant: int | None
    auth_role_uid_is_client: int | None
    auth_role_uid_is_custom: int | None
    client_uid_client_name: str | None
    client_uid_tenant_uid: str | None
    client_uid_country_uid: str | None
    client_uid_client_type_uid: str | None
    client_uid_client_category_uid: str | None
    client_uid_account_uid: str | None
    client_uid_client_code: str | None
    client_uid_client_description: str | None
    client_uid_start_date: datetime.datetime | None
    client_uid_end_date: datetime.datetime | None
    client_uid_is_internal: int | None
    client_uid_is_system: int | None
    client_uid_is_test: int | None
    project_instance_uid_project_instance_name: str | None
    project_instance_uid_tenant_uid: str | None
    project_instance_uid_client_uid: str | None
    project_instance_uid_project_type_uid: str | None
    project_instance_uid_manager_account_uid: str | None
    project_instance_uid_project_group_uid: str | None
    project_instance_uid_project_code: str | None
    project_instance_uid_project_description: str | None
    project_instance_uid_is_billable: int | None
    project_instance_uid_start_date: datetime.datetime | None
    project_instance_uid_end_date: datetime.datetime | None
    project_instance_uid_current_billed: str | None
    project_instance_uid_budget: str | None
    def __init__(self, auth_permission_uid: str | None, auth_permission_name: str | None, tenant_uid: str | None, account_uid: str | None, auth_role_uid: str | None, client_uid: str | None, project_instance_uid: str | None, valid_from_date: datetime.datetime | None, valid_till_date: datetime.datetime | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None, tenant_uid_tenant_name: str | None, tenant_uid_country_uid: str | None, tenant_uid_tenant_type_uid: str | None, tenant_uid_tenant_category_uid: str | None, tenant_uid_tenant_code: str | None, tenant_uid_tenant_description: str | None, tenant_uid_start_date: datetime.datetime | None, tenant_uid_end_date: datetime.datetime | None, tenant_uid_is_internal: int | None, tenant_uid_is_system: int | None, tenant_uid_is_test: int | None, tenant_uid_account_uid: str | None, account_uid_account_name: str | None, account_uid_tenant_uid: str | None, account_uid_account_type_uid: str | None, account_uid_account_title_uid: str | None, account_uid_account_division_uid: str | None, account_uid_account_group_uid: str | None, account_uid_auth_identity_uid: str | None, account_uid_account_email: str | None, account_uid_display_name: str | None, account_uid_is_system: int | None, auth_role_uid_auth_role_name: str | None, auth_role_uid_parent_auth_role_uid: str | None, auth_role_uid_tenant_uid: str | None, auth_role_uid_role_description: str | None, auth_role_uid_access_uris: str | None, auth_role_uid_is_project: int | None, auth_role_uid_is_tenant: int | None, auth_role_uid_is_client: int | None, auth_role_uid_is_custom: int | None, client_uid_client_name: str | None, client_uid_tenant_uid: str | None, client_uid_country_uid: str | None, client_uid_client_type_uid: str | None, client_uid_client_category_uid: str | None, client_uid_account_uid: str | None, client_uid_client_code: str | None, client_uid_client_description: str | None, client_uid_start_date: datetime.datetime | None, client_uid_end_date: datetime.datetime | None, client_uid_is_internal: int | None, client_uid_is_system: int | None, client_uid_is_test: int | None, project_instance_uid_project_instance_name: str | None, project_instance_uid_tenant_uid: str | None, project_instance_uid_client_uid: str | None, project_instance_uid_project_type_uid: str | None, project_instance_uid_manager_account_uid: str | None, project_instance_uid_project_group_uid: str | None, project_instance_uid_project_code: str | None, project_instance_uid_project_description: str | None, project_instance_uid_is_billable: int | None, project_instance_uid_start_date: datetime.datetime | None, project_instance_uid_end_date: datetime.datetime | None, project_instance_uid_current_billed: str | None, project_instance_uid_budget: str | None):
        self.auth_permission_uid = auth_permission_uid
        self.auth_permission_name = auth_permission_name
        self.tenant_uid = tenant_uid
        self.account_uid = account_uid
        self.auth_role_uid = auth_role_uid
        self.client_uid = client_uid
        self.project_instance_uid = project_instance_uid
        self.valid_from_date = valid_from_date
        self.valid_till_date = valid_till_date
        self.row_instance = row_instance
        self.row_lock = row_lock
        self.row_owner = row_owner
        self.row_seq = row_seq
        self.row_guid = row_guid
        self.row_version = row_version
        self.is_active = is_active
        self.created_date = created_date
        self.created_by = created_by
        self.last_updated_date = last_updated_date
        self.last_updated_by = last_updated_by
        self.removed_date = removed_date
        self.removed_by = removed_by
        self.custom_attributes = custom_attributes
        self.tenant_uid_tenant_name = tenant_uid_tenant_name
        self.tenant_uid_country_uid = tenant_uid_country_uid
        self.tenant_uid_tenant_type_uid = tenant_uid_tenant_type_uid
        self.tenant_uid_tenant_category_uid = tenant_uid_tenant_category_uid
        self.tenant_uid_tenant_code = tenant_uid_tenant_code
        self.tenant_uid_tenant_description = tenant_uid_tenant_description
        self.tenant_uid_start_date = tenant_uid_start_date
        self.tenant_uid_end_date = tenant_uid_end_date
        self.tenant_uid_is_internal = tenant_uid_is_internal
        self.tenant_uid_is_system = tenant_uid_is_system
        self.tenant_uid_is_test = tenant_uid_is_test
        self.tenant_uid_account_uid = tenant_uid_account_uid
        self.account_uid_account_name = account_uid_account_name
        self.account_uid_tenant_uid = account_uid_tenant_uid
        self.account_uid_account_type_uid = account_uid_account_type_uid
        self.account_uid_account_title_uid = account_uid_account_title_uid
        self.account_uid_account_division_uid = account_uid_account_division_uid
        self.account_uid_account_group_uid = account_uid_account_group_uid
        self.account_uid_auth_identity_uid = account_uid_auth_identity_uid
        self.account_uid_account_email = account_uid_account_email
        self.account_uid_display_name = account_uid_display_name
        self.account_uid_is_system = account_uid_is_system
        self.auth_role_uid_auth_role_name = auth_role_uid_auth_role_name
        self.auth_role_uid_parent_auth_role_uid = auth_role_uid_parent_auth_role_uid
        self.auth_role_uid_tenant_uid = auth_role_uid_tenant_uid
        self.auth_role_uid_role_description = auth_role_uid_role_description
        self.auth_role_uid_access_uris = auth_role_uid_access_uris
        self.auth_role_uid_is_project = auth_role_uid_is_project
        self.auth_role_uid_is_tenant = auth_role_uid_is_tenant
        self.auth_role_uid_is_client = auth_role_uid_is_client
        self.auth_role_uid_is_custom = auth_role_uid_is_custom
        self.client_uid_client_name = client_uid_client_name
        self.client_uid_tenant_uid = client_uid_tenant_uid
        self.client_uid_country_uid = client_uid_country_uid
        self.client_uid_client_type_uid = client_uid_client_type_uid
        self.client_uid_client_category_uid = client_uid_client_category_uid
        self.client_uid_account_uid = client_uid_account_uid
        self.client_uid_client_code = client_uid_client_code
        self.client_uid_client_description = client_uid_client_description
        self.client_uid_start_date = client_uid_start_date
        self.client_uid_end_date = client_uid_end_date
        self.client_uid_is_internal = client_uid_is_internal
        self.client_uid_is_system = client_uid_is_system
        self.client_uid_is_test = client_uid_is_test
        self.project_instance_uid_project_instance_name = project_instance_uid_project_instance_name
        self.project_instance_uid_tenant_uid = project_instance_uid_tenant_uid
        self.project_instance_uid_client_uid = project_instance_uid_client_uid
        self.project_instance_uid_project_type_uid = project_instance_uid_project_type_uid
        self.project_instance_uid_manager_account_uid = project_instance_uid_manager_account_uid
        self.project_instance_uid_project_group_uid = project_instance_uid_project_group_uid
        self.project_instance_uid_project_code = project_instance_uid_project_code
        self.project_instance_uid_project_description = project_instance_uid_project_description
        self.project_instance_uid_is_billable = project_instance_uid_is_billable
        self.project_instance_uid_start_date = project_instance_uid_start_date
        self.project_instance_uid_end_date = project_instance_uid_end_date
        self.project_instance_uid_current_billed = project_instance_uid_current_billed
        self.project_instance_uid_budget = project_instance_uid_budget
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.auth_permission_uid, self.auth_permission_name, self.tenant_uid, self.account_uid, self.auth_role_uid, self.client_uid, self.project_instance_uid, self.valid_from_date, self.valid_till_date, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes, self.tenant_uid_tenant_name, self.tenant_uid_country_uid, self.tenant_uid_tenant_type_uid, self.tenant_uid_tenant_category_uid, self.tenant_uid_tenant_code, self.tenant_uid_tenant_description, self.tenant_uid_start_date, self.tenant_uid_end_date, self.tenant_uid_is_internal, self.tenant_uid_is_system, self.tenant_uid_is_test, self.tenant_uid_account_uid, self.account_uid_account_name, self.account_uid_tenant_uid, self.account_uid_account_type_uid, self.account_uid_account_title_uid, self.account_uid_account_division_uid, self.account_uid_account_group_uid, self.account_uid_auth_identity_uid, self.account_uid_account_email, self.account_uid_display_name, self.account_uid_is_system, self.auth_role_uid_auth_role_name, self.auth_role_uid_parent_auth_role_uid, self.auth_role_uid_tenant_uid, self.auth_role_uid_role_description, self.auth_role_uid_access_uris, self.auth_role_uid_is_project, self.auth_role_uid_is_tenant, self.auth_role_uid_is_client, self.auth_role_uid_is_custom, self.client_uid_client_name, self.client_uid_tenant_uid, self.client_uid_country_uid, self.client_uid_client_type_uid, self.client_uid_client_category_uid, self.client_uid_account_uid, self.client_uid_client_code, self.client_uid_client_description, self.client_uid_start_date, self.client_uid_end_date, self.client_uid_is_internal, self.client_uid_is_system, self.client_uid_is_test, self.project_instance_uid_project_instance_name, self.project_instance_uid_tenant_uid, self.project_instance_uid_client_uid, self.project_instance_uid_project_type_uid, self.project_instance_uid_manager_account_uid, self.project_instance_uid_project_group_uid, self.project_instance_uid_project_code, self.project_instance_uid_project_description, self.project_instance_uid_is_billable, self.project_instance_uid_start_date, self.project_instance_uid_end_date, self.project_instance_uid_current_billed, self.project_instance_uid_budget]


@dataclass(frozen=False)
class auth_request_rich_dto(auth_request_read_dto):
    auth_request_uid: str | None
    auth_request_name: str | None
    tenant_uid: str | None
    account_uid: str | None
    requestor_email: str | None
    reset_guid: str | None
    valid_till_date: datetime.datetime | None
    lock_guid: str | None
    lock_by: str | None
    lock_date: datetime.datetime | None
    is_checked: int | None
    is_used: int | None
    check_date: datetime.datetime | None
    use_date: datetime.datetime | None
    event_notification_uid: str | None
    row_instance: str | None
    row_lock: str | None
    row_owner: str | None
    row_seq: int | None
    row_guid: str | None
    row_version: int | None
    is_active: int | None
    created_date: datetime.datetime | None
    created_by: str | None
    last_updated_date: datetime.datetime | None
    last_updated_by: str | None
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str | None
    tenant_uid_tenant_name: str | None
    tenant_uid_country_uid: str | None
    tenant_uid_tenant_type_uid: str | None
    tenant_uid_tenant_category_uid: str | None
    tenant_uid_tenant_code: str | None
    tenant_uid_tenant_description: str | None
    tenant_uid_start_date: datetime.datetime | None
    tenant_uid_end_date: datetime.datetime | None
    tenant_uid_is_internal: int | None
    tenant_uid_is_system: int | None
    tenant_uid_is_test: int | None
    tenant_uid_account_uid: str | None
    account_uid_account_name: str | None
    account_uid_tenant_uid: str | None
    account_uid_account_type_uid: str | None
    account_uid_account_title_uid: str | None
    account_uid_account_division_uid: str | None
    account_uid_account_group_uid: str | None
    account_uid_auth_identity_uid: str | None
    account_uid_account_email: str | None
    account_uid_display_name: str | None
    account_uid_is_system: int | None
    event_notification_uid_event_notification_name: str | None
    event_notification_uid_tenant_uid: str | None
    event_notification_uid_account_uid: str | None
    event_notification_uid_notification_type: str | None
    event_notification_uid_notification_topic: str | None
    event_notification_uid_notification_format: str | None
    event_notification_uid_notification_content: str | None
    event_notification_uid_sending_status: str | None
    def __init__(self, auth_request_uid: str | None, auth_request_name: str | None, tenant_uid: str | None, account_uid: str | None, requestor_email: str | None, reset_guid: str | None, valid_till_date: datetime.datetime | None, lock_guid: str | None, lock_by: str | None, lock_date: datetime.datetime | None, is_checked: int | None, is_used: int | None, check_date: datetime.datetime | None, use_date: datetime.datetime | None, event_notification_uid: str | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None, tenant_uid_tenant_name: str | None, tenant_uid_country_uid: str | None, tenant_uid_tenant_type_uid: str | None, tenant_uid_tenant_category_uid: str | None, tenant_uid_tenant_code: str | None, tenant_uid_tenant_description: str | None, tenant_uid_start_date: datetime.datetime | None, tenant_uid_end_date: datetime.datetime | None, tenant_uid_is_internal: int | None, tenant_uid_is_system: int | None, tenant_uid_is_test: int | None, tenant_uid_account_uid: str | None, account_uid_account_name: str | None, account_uid_tenant_uid: str | None, account_uid_account_type_uid: str | None, account_uid_account_title_uid: str | None, account_uid_account_division_uid: str | None, account_uid_account_group_uid: str | None, account_uid_auth_identity_uid: str | None, account_uid_account_email: str | None, account_uid_display_name: str | None, account_uid_is_system: int | None, event_notification_uid_event_notification_name: str | None, event_notification_uid_tenant_uid: str | None, event_notification_uid_account_uid: str | None, event_notification_uid_notification_type: str | None, event_notification_uid_notification_topic: str | None, event_notification_uid_notification_format: str | None, event_notification_uid_notification_content: str | None, event_notification_uid_sending_status: str | None):
        self.auth_request_uid = auth_request_uid
        self.auth_request_name = auth_request_name
        self.tenant_uid = tenant_uid
        self.account_uid = account_uid
        self.requestor_email = requestor_email
        self.reset_guid = reset_guid
        self.valid_till_date = valid_till_date
        self.lock_guid = lock_guid
        self.lock_by = lock_by
        self.lock_date = lock_date
        self.is_checked = is_checked
        self.is_used = is_used
        self.check_date = check_date
        self.use_date = use_date
        self.event_notification_uid = event_notification_uid
        self.row_instance = row_instance
        self.row_lock = row_lock
        self.row_owner = row_owner
        self.row_seq = row_seq
        self.row_guid = row_guid
        self.row_version = row_version
        self.is_active = is_active
        self.created_date = created_date
        self.created_by = created_by
        self.last_updated_date = last_updated_date
        self.last_updated_by = last_updated_by
        self.removed_date = removed_date
        self.removed_by = removed_by
        self.custom_attributes = custom_attributes
        self.tenant_uid_tenant_name = tenant_uid_tenant_name
        self.tenant_uid_country_uid = tenant_uid_country_uid
        self.tenant_uid_tenant_type_uid = tenant_uid_tenant_type_uid
        self.tenant_uid_tenant_category_uid = tenant_uid_tenant_category_uid
        self.tenant_uid_tenant_code = tenant_uid_tenant_code
        self.tenant_uid_tenant_description = tenant_uid_tenant_description
        self.tenant_uid_start_date = tenant_uid_start_date
        self.tenant_uid_end_date = tenant_uid_end_date
        self.tenant_uid_is_internal = tenant_uid_is_internal
        self.tenant_uid_is_system = tenant_uid_is_system
        self.tenant_uid_is_test = tenant_uid_is_test
        self.tenant_uid_account_uid = tenant_uid_account_uid
        self.account_uid_account_name = account_uid_account_name
        self.account_uid_tenant_uid = account_uid_tenant_uid
        self.account_uid_account_type_uid = account_uid_account_type_uid
        self.account_uid_account_title_uid = account_uid_account_title_uid
        self.account_uid_account_division_uid = account_uid_account_division_uid
        self.account_uid_account_group_uid = account_uid_account_group_uid
        self.account_uid_auth_identity_uid = account_uid_auth_identity_uid
        self.account_uid_account_email = account_uid_account_email
        self.account_uid_display_name = account_uid_display_name
        self.account_uid_is_system = account_uid_is_system
        self.event_notification_uid_event_notification_name = event_notification_uid_event_notification_name
        self.event_notification_uid_tenant_uid = event_notification_uid_tenant_uid
        self.event_notification_uid_account_uid = event_notification_uid_account_uid
        self.event_notification_uid_notification_type = event_notification_uid_notification_type
        self.event_notification_uid_notification_topic = event_notification_uid_notification_topic
        self.event_notification_uid_notification_format = event_notification_uid_notification_format
        self.event_notification_uid_notification_content = event_notification_uid_notification_content
        self.event_notification_uid_sending_status = event_notification_uid_sending_status
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.auth_request_uid, self.auth_request_name, self.tenant_uid, self.account_uid, self.requestor_email, self.reset_guid, self.valid_till_date, self.lock_guid, self.lock_by, self.lock_date, self.is_checked, self.is_used, self.check_date, self.use_date, self.event_notification_uid, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes, self.tenant_uid_tenant_name, self.tenant_uid_country_uid, self.tenant_uid_tenant_type_uid, self.tenant_uid_tenant_category_uid, self.tenant_uid_tenant_code, self.tenant_uid_tenant_description, self.tenant_uid_start_date, self.tenant_uid_end_date, self.tenant_uid_is_internal, self.tenant_uid_is_system, self.tenant_uid_is_test, self.tenant_uid_account_uid, self.account_uid_account_name, self.account_uid_tenant_uid, self.account_uid_account_type_uid, self.account_uid_account_title_uid, self.account_uid_account_division_uid, self.account_uid_account_group_uid, self.account_uid_auth_identity_uid, self.account_uid_account_email, self.account_uid_display_name, self.account_uid_is_system, self.event_notification_uid_event_notification_name, self.event_notification_uid_tenant_uid, self.event_notification_uid_account_uid, self.event_notification_uid_notification_type, self.event_notification_uid_notification_topic, self.event_notification_uid_notification_format, self.event_notification_uid_notification_content, self.event_notification_uid_sending_status]


@dataclass(frozen=False)
class auth_role_rich_dto(auth_role_read_dto):
    auth_role_uid: str | None
    auth_role_name: str | None
    parent_auth_role_uid: str | None
    tenant_uid: str | None
    role_description: str | None
    access_uris: str | None
    is_project: int | None
    is_tenant: int | None
    is_client: int | None
    is_custom: int | None
    row_instance: str | None
    row_lock: str | None
    row_owner: str | None
    row_seq: int | None
    row_guid: str | None
    row_version: int | None
    is_active: int | None
    created_date: datetime.datetime | None
    created_by: str | None
    last_updated_date: datetime.datetime | None
    last_updated_by: str | None
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str | None
    tenant_uid_tenant_name: str | None
    tenant_uid_country_uid: str | None
    tenant_uid_tenant_type_uid: str | None
    tenant_uid_tenant_category_uid: str | None
    tenant_uid_tenant_code: str | None
    tenant_uid_tenant_description: str | None
    tenant_uid_start_date: datetime.datetime | None
    tenant_uid_end_date: datetime.datetime | None
    tenant_uid_is_internal: int | None
    tenant_uid_is_system: int | None
    tenant_uid_is_test: int | None
    tenant_uid_account_uid: str | None
    def __init__(self, auth_role_uid: str | None, auth_role_name: str | None, parent_auth_role_uid: str | None, tenant_uid: str | None, role_description: str | None, access_uris: str | None, is_project: int | None, is_tenant: int | None, is_client: int | None, is_custom: int | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None, tenant_uid_tenant_name: str | None, tenant_uid_country_uid: str | None, tenant_uid_tenant_type_uid: str | None, tenant_uid_tenant_category_uid: str | None, tenant_uid_tenant_code: str | None, tenant_uid_tenant_description: str | None, tenant_uid_start_date: datetime.datetime | None, tenant_uid_end_date: datetime.datetime | None, tenant_uid_is_internal: int | None, tenant_uid_is_system: int | None, tenant_uid_is_test: int | None, tenant_uid_account_uid: str | None):
        self.auth_role_uid = auth_role_uid
        self.auth_role_name = auth_role_name
        self.parent_auth_role_uid = parent_auth_role_uid
        self.tenant_uid = tenant_uid
        self.role_description = role_description
        self.access_uris = access_uris
        self.is_project = is_project
        self.is_tenant = is_tenant
        self.is_client = is_client
        self.is_custom = is_custom
        self.row_instance = row_instance
        self.row_lock = row_lock
        self.row_owner = row_owner
        self.row_seq = row_seq
        self.row_guid = row_guid
        self.row_version = row_version
        self.is_active = is_active
        self.created_date = created_date
        self.created_by = created_by
        self.last_updated_date = last_updated_date
        self.last_updated_by = last_updated_by
        self.removed_date = removed_date
        self.removed_by = removed_by
        self.custom_attributes = custom_attributes
        self.tenant_uid_tenant_name = tenant_uid_tenant_name
        self.tenant_uid_country_uid = tenant_uid_country_uid
        self.tenant_uid_tenant_type_uid = tenant_uid_tenant_type_uid
        self.tenant_uid_tenant_category_uid = tenant_uid_tenant_category_uid
        self.tenant_uid_tenant_code = tenant_uid_tenant_code
        self.tenant_uid_tenant_description = tenant_uid_tenant_description
        self.tenant_uid_start_date = tenant_uid_start_date
        self.tenant_uid_end_date = tenant_uid_end_date
        self.tenant_uid_is_internal = tenant_uid_is_internal
        self.tenant_uid_is_system = tenant_uid_is_system
        self.tenant_uid_is_test = tenant_uid_is_test
        self.tenant_uid_account_uid = tenant_uid_account_uid
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.auth_role_uid, self.auth_role_name, self.parent_auth_role_uid, self.tenant_uid, self.role_description, self.access_uris, self.is_project, self.is_tenant, self.is_client, self.is_custom, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes, self.tenant_uid_tenant_name, self.tenant_uid_country_uid, self.tenant_uid_tenant_type_uid, self.tenant_uid_tenant_category_uid, self.tenant_uid_tenant_code, self.tenant_uid_tenant_description, self.tenant_uid_start_date, self.tenant_uid_end_date, self.tenant_uid_is_internal, self.tenant_uid_is_system, self.tenant_uid_is_test, self.tenant_uid_account_uid]


@dataclass(frozen=False)
class auth_role_uri_rich_dto(auth_role_uri_read_dto):
    auth_role_uri_uid: str | None
    auth_role_uri_name: str | None
    auth_role_uid: str | None
    uri: str | None
    row_instance: str | None
    row_lock: str | None
    row_owner: str | None
    row_seq: int | None
    row_guid: str | None
    row_version: int | None
    is_active: int | None
    created_date: datetime.datetime | None
    created_by: str | None
    last_updated_date: datetime.datetime | None
    last_updated_by: str | None
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str | None
    auth_role_uid_auth_role_name: str | None
    auth_role_uid_parent_auth_role_uid: str | None
    auth_role_uid_tenant_uid: str | None
    auth_role_uid_role_description: str | None
    auth_role_uid_access_uris: str | None
    auth_role_uid_is_project: int | None
    auth_role_uid_is_tenant: int | None
    auth_role_uid_is_client: int | None
    auth_role_uid_is_custom: int | None
    def __init__(self, auth_role_uri_uid: str | None, auth_role_uri_name: str | None, auth_role_uid: str | None, uri: str | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None, auth_role_uid_auth_role_name: str | None, auth_role_uid_parent_auth_role_uid: str | None, auth_role_uid_tenant_uid: str | None, auth_role_uid_role_description: str | None, auth_role_uid_access_uris: str | None, auth_role_uid_is_project: int | None, auth_role_uid_is_tenant: int | None, auth_role_uid_is_client: int | None, auth_role_uid_is_custom: int | None):
        self.auth_role_uri_uid = auth_role_uri_uid
        self.auth_role_uri_name = auth_role_uri_name
        self.auth_role_uid = auth_role_uid
        self.uri = uri
        self.row_instance = row_instance
        self.row_lock = row_lock
        self.row_owner = row_owner
        self.row_seq = row_seq
        self.row_guid = row_guid
        self.row_version = row_version
        self.is_active = is_active
        self.created_date = created_date
        self.created_by = created_by
        self.last_updated_date = last_updated_date
        self.last_updated_by = last_updated_by
        self.removed_date = removed_date
        self.removed_by = removed_by
        self.custom_attributes = custom_attributes
        self.auth_role_uid_auth_role_name = auth_role_uid_auth_role_name
        self.auth_role_uid_parent_auth_role_uid = auth_role_uid_parent_auth_role_uid
        self.auth_role_uid_tenant_uid = auth_role_uid_tenant_uid
        self.auth_role_uid_role_description = auth_role_uid_role_description
        self.auth_role_uid_access_uris = auth_role_uid_access_uris
        self.auth_role_uid_is_project = auth_role_uid_is_project
        self.auth_role_uid_is_tenant = auth_role_uid_is_tenant
        self.auth_role_uid_is_client = auth_role_uid_is_client
        self.auth_role_uid_is_custom = auth_role_uid_is_custom
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.auth_role_uri_uid, self.auth_role_uri_name, self.auth_role_uid, self.uri, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes, self.auth_role_uid_auth_role_name, self.auth_role_uid_parent_auth_role_uid, self.auth_role_uid_tenant_uid, self.auth_role_uid_role_description, self.auth_role_uid_access_uris, self.auth_role_uid_is_project, self.auth_role_uid_is_tenant, self.auth_role_uid_is_client, self.auth_role_uid_is_custom]


@dataclass(frozen=False)
class auth_session_rich_dto(auth_session_read_dto):
    auth_session_uid: str | None
    auth_session_name: str | None
    tenant_uid: str | None
    account_uid: str | None
    session_token: str | None
    browser_name: str | None
    browser_: str | None
    row_instance: str | None
    row_lock: str | None
    row_owner: str | None
    row_seq: int | None
    row_guid: str | None
    row_version: int | None
    is_active: int | None
    created_date: datetime.datetime | None
    created_by: str | None
    last_updated_date: datetime.datetime | None
    last_updated_by: str | None
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str | None
    tenant_uid_tenant_name: str | None
    tenant_uid_country_uid: str | None
    tenant_uid_tenant_type_uid: str | None
    tenant_uid_tenant_category_uid: str | None
    tenant_uid_tenant_code: str | None
    tenant_uid_tenant_description: str | None
    tenant_uid_start_date: datetime.datetime | None
    tenant_uid_end_date: datetime.datetime | None
    tenant_uid_is_internal: int | None
    tenant_uid_is_system: int | None
    tenant_uid_is_test: int | None
    tenant_uid_account_uid: str | None
    account_uid_account_name: str | None
    account_uid_tenant_uid: str | None
    account_uid_account_type_uid: str | None
    account_uid_account_title_uid: str | None
    account_uid_account_division_uid: str | None
    account_uid_account_group_uid: str | None
    account_uid_auth_identity_uid: str | None
    account_uid_account_email: str | None
    account_uid_display_name: str | None
    account_uid_is_system: int | None
    def __init__(self, auth_session_uid: str | None, auth_session_name: str | None, tenant_uid: str | None, account_uid: str | None, session_token: str | None, browser_name: str | None, browser_: str | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None, tenant_uid_tenant_name: str | None, tenant_uid_country_uid: str | None, tenant_uid_tenant_type_uid: str | None, tenant_uid_tenant_category_uid: str | None, tenant_uid_tenant_code: str | None, tenant_uid_tenant_description: str | None, tenant_uid_start_date: datetime.datetime | None, tenant_uid_end_date: datetime.datetime | None, tenant_uid_is_internal: int | None, tenant_uid_is_system: int | None, tenant_uid_is_test: int | None, tenant_uid_account_uid: str | None, account_uid_account_name: str | None, account_uid_tenant_uid: str | None, account_uid_account_type_uid: str | None, account_uid_account_title_uid: str | None, account_uid_account_division_uid: str | None, account_uid_account_group_uid: str | None, account_uid_auth_identity_uid: str | None, account_uid_account_email: str | None, account_uid_display_name: str | None, account_uid_is_system: int | None):
        self.auth_session_uid = auth_session_uid
        self.auth_session_name = auth_session_name
        self.tenant_uid = tenant_uid
        self.account_uid = account_uid
        self.session_token = session_token
        self.browser_name = browser_name
        self.browser_ = browser_
        self.row_instance = row_instance
        self.row_lock = row_lock
        self.row_owner = row_owner
        self.row_seq = row_seq
        self.row_guid = row_guid
        self.row_version = row_version
        self.is_active = is_active
        self.created_date = created_date
        self.created_by = created_by
        self.last_updated_date = last_updated_date
        self.last_updated_by = last_updated_by
        self.removed_date = removed_date
        self.removed_by = removed_by
        self.custom_attributes = custom_attributes
        self.tenant_uid_tenant_name = tenant_uid_tenant_name
        self.tenant_uid_country_uid = tenant_uid_country_uid
        self.tenant_uid_tenant_type_uid = tenant_uid_tenant_type_uid
        self.tenant_uid_tenant_category_uid = tenant_uid_tenant_category_uid
        self.tenant_uid_tenant_code = tenant_uid_tenant_code
        self.tenant_uid_tenant_description = tenant_uid_tenant_description
        self.tenant_uid_start_date = tenant_uid_start_date
        self.tenant_uid_end_date = tenant_uid_end_date
        self.tenant_uid_is_internal = tenant_uid_is_internal
        self.tenant_uid_is_system = tenant_uid_is_system
        self.tenant_uid_is_test = tenant_uid_is_test
        self.tenant_uid_account_uid = tenant_uid_account_uid
        self.account_uid_account_name = account_uid_account_name
        self.account_uid_tenant_uid = account_uid_tenant_uid
        self.account_uid_account_type_uid = account_uid_account_type_uid
        self.account_uid_account_title_uid = account_uid_account_title_uid
        self.account_uid_account_division_uid = account_uid_account_division_uid
        self.account_uid_account_group_uid = account_uid_account_group_uid
        self.account_uid_auth_identity_uid = account_uid_auth_identity_uid
        self.account_uid_account_email = account_uid_account_email
        self.account_uid_display_name = account_uid_display_name
        self.account_uid_is_system = account_uid_is_system
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.auth_session_uid, self.auth_session_name, self.tenant_uid, self.account_uid, self.session_token, self.browser_name, self.browser_, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes, self.tenant_uid_tenant_name, self.tenant_uid_country_uid, self.tenant_uid_tenant_type_uid, self.tenant_uid_tenant_category_uid, self.tenant_uid_tenant_code, self.tenant_uid_tenant_description, self.tenant_uid_start_date, self.tenant_uid_end_date, self.tenant_uid_is_internal, self.tenant_uid_is_system, self.tenant_uid_is_test, self.tenant_uid_account_uid, self.account_uid_account_name, self.account_uid_tenant_uid, self.account_uid_account_type_uid, self.account_uid_account_title_uid, self.account_uid_account_division_uid, self.account_uid_account_group_uid, self.account_uid_auth_identity_uid, self.account_uid_account_email, self.account_uid_display_name, self.account_uid_is_system]


@dataclass(frozen=False)
class auth_sso_rich_dto(auth_sso_read_dto):
    auth_sso_uid: str | None
    auth_sso_name: str | None
    tenant_uid: str | None
    owner_account_uid: str | None
    sso_name: str | None
    sso_url: str | None
    sso_key: str | None
    sso_secret: str | None
    sso_code: str | None
    clientid: str | None
    clientsecret: str | None
    callback_url: str | None
    row_instance: str | None
    row_lock: str | None
    row_owner: str | None
    row_seq: int | None
    row_guid: str | None
    row_version: int | None
    is_active: int | None
    created_date: datetime.datetime | None
    created_by: str | None
    last_updated_date: datetime.datetime | None
    last_updated_by: str | None
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str | None
    tenant_uid_tenant_name: str | None
    tenant_uid_country_uid: str | None
    tenant_uid_tenant_type_uid: str | None
    tenant_uid_tenant_category_uid: str | None
    tenant_uid_tenant_code: str | None
    tenant_uid_tenant_description: str | None
    tenant_uid_start_date: datetime.datetime | None
    tenant_uid_end_date: datetime.datetime | None
    tenant_uid_is_internal: int | None
    tenant_uid_is_system: int | None
    tenant_uid_is_test: int | None
    tenant_uid_account_uid: str | None
    owner_account_uid_account_name: str | None
    owner_account_uid_tenant_uid: str | None
    owner_account_uid_account_type_uid: str | None
    owner_account_uid_account_title_uid: str | None
    owner_account_uid_account_division_uid: str | None
    owner_account_uid_account_group_uid: str | None
    owner_account_uid_auth_identity_uid: str | None
    owner_account_uid_account_email: str | None
    owner_account_uid_display_name: str | None
    owner_account_uid_is_system: int | None
    def __init__(self, auth_sso_uid: str | None, auth_sso_name: str | None, tenant_uid: str | None, owner_account_uid: str | None, sso_name: str | None, sso_url: str | None, sso_key: str | None, sso_secret: str | None, sso_code: str | None, clientid: str | None, clientsecret: str | None, callback_url: str | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None, tenant_uid_tenant_name: str | None, tenant_uid_country_uid: str | None, tenant_uid_tenant_type_uid: str | None, tenant_uid_tenant_category_uid: str | None, tenant_uid_tenant_code: str | None, tenant_uid_tenant_description: str | None, tenant_uid_start_date: datetime.datetime | None, tenant_uid_end_date: datetime.datetime | None, tenant_uid_is_internal: int | None, tenant_uid_is_system: int | None, tenant_uid_is_test: int | None, tenant_uid_account_uid: str | None, owner_account_uid_account_name: str | None, owner_account_uid_tenant_uid: str | None, owner_account_uid_account_type_uid: str | None, owner_account_uid_account_title_uid: str | None, owner_account_uid_account_division_uid: str | None, owner_account_uid_account_group_uid: str | None, owner_account_uid_auth_identity_uid: str | None, owner_account_uid_account_email: str | None, owner_account_uid_display_name: str | None, owner_account_uid_is_system: int | None):
        self.auth_sso_uid = auth_sso_uid
        self.auth_sso_name = auth_sso_name
        self.tenant_uid = tenant_uid
        self.owner_account_uid = owner_account_uid
        self.sso_name = sso_name
        self.sso_url = sso_url
        self.sso_key = sso_key
        self.sso_secret = sso_secret
        self.sso_code = sso_code
        self.clientid = clientid
        self.clientsecret = clientsecret
        self.callback_url = callback_url
        self.row_instance = row_instance
        self.row_lock = row_lock
        self.row_owner = row_owner
        self.row_seq = row_seq
        self.row_guid = row_guid
        self.row_version = row_version
        self.is_active = is_active
        self.created_date = created_date
        self.created_by = created_by
        self.last_updated_date = last_updated_date
        self.last_updated_by = last_updated_by
        self.removed_date = removed_date
        self.removed_by = removed_by
        self.custom_attributes = custom_attributes
        self.tenant_uid_tenant_name = tenant_uid_tenant_name
        self.tenant_uid_country_uid = tenant_uid_country_uid
        self.tenant_uid_tenant_type_uid = tenant_uid_tenant_type_uid
        self.tenant_uid_tenant_category_uid = tenant_uid_tenant_category_uid
        self.tenant_uid_tenant_code = tenant_uid_tenant_code
        self.tenant_uid_tenant_description = tenant_uid_tenant_description
        self.tenant_uid_start_date = tenant_uid_start_date
        self.tenant_uid_end_date = tenant_uid_end_date
        self.tenant_uid_is_internal = tenant_uid_is_internal
        self.tenant_uid_is_system = tenant_uid_is_system
        self.tenant_uid_is_test = tenant_uid_is_test
        self.tenant_uid_account_uid = tenant_uid_account_uid
        self.owner_account_uid_account_name = owner_account_uid_account_name
        self.owner_account_uid_tenant_uid = owner_account_uid_tenant_uid
        self.owner_account_uid_account_type_uid = owner_account_uid_account_type_uid
        self.owner_account_uid_account_title_uid = owner_account_uid_account_title_uid
        self.owner_account_uid_account_division_uid = owner_account_uid_account_division_uid
        self.owner_account_uid_account_group_uid = owner_account_uid_account_group_uid
        self.owner_account_uid_auth_identity_uid = owner_account_uid_auth_identity_uid
        self.owner_account_uid_account_email = owner_account_uid_account_email
        self.owner_account_uid_display_name = owner_account_uid_display_name
        self.owner_account_uid_is_system = owner_account_uid_is_system
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.auth_sso_uid, self.auth_sso_name, self.tenant_uid, self.owner_account_uid, self.sso_name, self.sso_url, self.sso_key, self.sso_secret, self.sso_code, self.clientid, self.clientsecret, self.callback_url, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes, self.tenant_uid_tenant_name, self.tenant_uid_country_uid, self.tenant_uid_tenant_type_uid, self.tenant_uid_tenant_category_uid, self.tenant_uid_tenant_code, self.tenant_uid_tenant_description, self.tenant_uid_start_date, self.tenant_uid_end_date, self.tenant_uid_is_internal, self.tenant_uid_is_system, self.tenant_uid_is_test, self.tenant_uid_account_uid, self.owner_account_uid_account_name, self.owner_account_uid_tenant_uid, self.owner_account_uid_account_type_uid, self.owner_account_uid_account_title_uid, self.owner_account_uid_account_division_uid, self.owner_account_uid_account_group_uid, self.owner_account_uid_auth_identity_uid, self.owner_account_uid_account_email, self.owner_account_uid_display_name, self.owner_account_uid_is_system]


@dataclass(frozen=False)
class auth_token_rich_dto(auth_token_read_dto):
    auth_token_uid: str | None
    auth_token_name: str | None
    tenant_uid: str | None
    account_uid: str | None
    token_seq: int | None
    token_hash: str | None
    token_salt: str | None
    valid_till_date: datetime.datetime | None
    last_use_date: datetime.datetime | None
    is_last: int | None
    row_instance: str | None
    row_lock: str | None
    row_owner: str | None
    row_seq: int | None
    row_guid: str | None
    row_version: int | None
    is_active: int | None
    created_date: datetime.datetime | None
    created_by: str | None
    last_updated_date: datetime.datetime | None
    last_updated_by: str | None
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str | None
    tenant_uid_tenant_name: str | None
    tenant_uid_country_uid: str | None
    tenant_uid_tenant_type_uid: str | None
    tenant_uid_tenant_category_uid: str | None
    tenant_uid_tenant_code: str | None
    tenant_uid_tenant_description: str | None
    tenant_uid_start_date: datetime.datetime | None
    tenant_uid_end_date: datetime.datetime | None
    tenant_uid_is_internal: int | None
    tenant_uid_is_system: int | None
    tenant_uid_is_test: int | None
    tenant_uid_account_uid: str | None
    account_uid_account_name: str | None
    account_uid_tenant_uid: str | None
    account_uid_account_type_uid: str | None
    account_uid_account_title_uid: str | None
    account_uid_account_division_uid: str | None
    account_uid_account_group_uid: str | None
    account_uid_auth_identity_uid: str | None
    account_uid_account_email: str | None
    account_uid_display_name: str | None
    account_uid_is_system: int | None
    def __init__(self, auth_token_uid: str | None, auth_token_name: str | None, tenant_uid: str | None, account_uid: str | None, token_seq: int | None, token_hash: str | None, token_salt: str | None, valid_till_date: datetime.datetime | None, last_use_date: datetime.datetime | None, is_last: int | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None, tenant_uid_tenant_name: str | None, tenant_uid_country_uid: str | None, tenant_uid_tenant_type_uid: str | None, tenant_uid_tenant_category_uid: str | None, tenant_uid_tenant_code: str | None, tenant_uid_tenant_description: str | None, tenant_uid_start_date: datetime.datetime | None, tenant_uid_end_date: datetime.datetime | None, tenant_uid_is_internal: int | None, tenant_uid_is_system: int | None, tenant_uid_is_test: int | None, tenant_uid_account_uid: str | None, account_uid_account_name: str | None, account_uid_tenant_uid: str | None, account_uid_account_type_uid: str | None, account_uid_account_title_uid: str | None, account_uid_account_division_uid: str | None, account_uid_account_group_uid: str | None, account_uid_auth_identity_uid: str | None, account_uid_account_email: str | None, account_uid_display_name: str | None, account_uid_is_system: int | None):
        self.auth_token_uid = auth_token_uid
        self.auth_token_name = auth_token_name
        self.tenant_uid = tenant_uid
        self.account_uid = account_uid
        self.token_seq = token_seq
        self.token_hash = token_hash
        self.token_salt = token_salt
        self.valid_till_date = valid_till_date
        self.last_use_date = last_use_date
        self.is_last = is_last
        self.row_instance = row_instance
        self.row_lock = row_lock
        self.row_owner = row_owner
        self.row_seq = row_seq
        self.row_guid = row_guid
        self.row_version = row_version
        self.is_active = is_active
        self.created_date = created_date
        self.created_by = created_by
        self.last_updated_date = last_updated_date
        self.last_updated_by = last_updated_by
        self.removed_date = removed_date
        self.removed_by = removed_by
        self.custom_attributes = custom_attributes
        self.tenant_uid_tenant_name = tenant_uid_tenant_name
        self.tenant_uid_country_uid = tenant_uid_country_uid
        self.tenant_uid_tenant_type_uid = tenant_uid_tenant_type_uid
        self.tenant_uid_tenant_category_uid = tenant_uid_tenant_category_uid
        self.tenant_uid_tenant_code = tenant_uid_tenant_code
        self.tenant_uid_tenant_description = tenant_uid_tenant_description
        self.tenant_uid_start_date = tenant_uid_start_date
        self.tenant_uid_end_date = tenant_uid_end_date
        self.tenant_uid_is_internal = tenant_uid_is_internal
        self.tenant_uid_is_system = tenant_uid_is_system
        self.tenant_uid_is_test = tenant_uid_is_test
        self.tenant_uid_account_uid = tenant_uid_account_uid
        self.account_uid_account_name = account_uid_account_name
        self.account_uid_tenant_uid = account_uid_tenant_uid
        self.account_uid_account_type_uid = account_uid_account_type_uid
        self.account_uid_account_title_uid = account_uid_account_title_uid
        self.account_uid_account_division_uid = account_uid_account_division_uid
        self.account_uid_account_group_uid = account_uid_account_group_uid
        self.account_uid_auth_identity_uid = account_uid_auth_identity_uid
        self.account_uid_account_email = account_uid_account_email
        self.account_uid_display_name = account_uid_display_name
        self.account_uid_is_system = account_uid_is_system
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.auth_token_uid, self.auth_token_name, self.tenant_uid, self.account_uid, self.token_seq, self.token_hash, self.token_salt, self.valid_till_date, self.last_use_date, self.is_last, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes, self.tenant_uid_tenant_name, self.tenant_uid_country_uid, self.tenant_uid_tenant_type_uid, self.tenant_uid_tenant_category_uid, self.tenant_uid_tenant_code, self.tenant_uid_tenant_description, self.tenant_uid_start_date, self.tenant_uid_end_date, self.tenant_uid_is_internal, self.tenant_uid_is_system, self.tenant_uid_is_test, self.tenant_uid_account_uid, self.account_uid_account_name, self.account_uid_tenant_uid, self.account_uid_account_type_uid, self.account_uid_account_title_uid, self.account_uid_account_division_uid, self.account_uid_account_group_uid, self.account_uid_auth_identity_uid, self.account_uid_account_email, self.account_uid_display_name, self.account_uid_is_system]


@dataclass(frozen=False)
class calendar_account_rich_dto(calendar_account_read_dto):
    calendar_account_uid: str | None
    calendar_account_name: str | None
    tenant_uid: str | None
    account_uid: str | None
    calendar_type_uid: str | None
    row_instance: str | None
    row_lock: str | None
    row_owner: str | None
    row_seq: int | None
    row_guid: str | None
    row_version: int | None
    is_active: int | None
    created_date: datetime.datetime | None
    created_by: str | None
    last_updated_date: datetime.datetime | None
    last_updated_by: str | None
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str | None
    calendar_account_uid_account_name: str | None
    calendar_account_uid_tenant_uid: str | None
    calendar_account_uid_account_type_uid: str | None
    calendar_account_uid_account_title_uid: str | None
    calendar_account_uid_account_division_uid: str | None
    calendar_account_uid_account_group_uid: str | None
    calendar_account_uid_auth_identity_uid: str | None
    calendar_account_uid_account_email: str | None
    calendar_account_uid_display_name: str | None
    calendar_account_uid_is_system: int | None
    tenant_uid_tenant_name: str | None
    tenant_uid_country_uid: str | None
    tenant_uid_tenant_type_uid: str | None
    tenant_uid_tenant_category_uid: str | None
    tenant_uid_tenant_code: str | None
    tenant_uid_tenant_description: str | None
    tenant_uid_start_date: datetime.datetime | None
    tenant_uid_end_date: datetime.datetime | None
    tenant_uid_is_internal: int | None
    tenant_uid_is_system: int | None
    tenant_uid_is_test: int | None
    tenant_uid_account_uid: str | None
    account_uid_account_name: str | None
    account_uid_tenant_uid: str | None
    account_uid_account_type_uid: str | None
    account_uid_account_title_uid: str | None
    account_uid_account_division_uid: str | None
    account_uid_account_group_uid: str | None
    account_uid_auth_identity_uid: str | None
    account_uid_account_email: str | None
    account_uid_display_name: str | None
    account_uid_is_system: int | None
    calendar_type_uid_calendar_type_name: str | None
    def __init__(self, calendar_account_uid: str | None, calendar_account_name: str | None, tenant_uid: str | None, account_uid: str | None, calendar_type_uid: str | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None, calendar_account_uid_account_name: str | None, calendar_account_uid_tenant_uid: str | None, calendar_account_uid_account_type_uid: str | None, calendar_account_uid_account_title_uid: str | None, calendar_account_uid_account_division_uid: str | None, calendar_account_uid_account_group_uid: str | None, calendar_account_uid_auth_identity_uid: str | None, calendar_account_uid_account_email: str | None, calendar_account_uid_display_name: str | None, calendar_account_uid_is_system: int | None, tenant_uid_tenant_name: str | None, tenant_uid_country_uid: str | None, tenant_uid_tenant_type_uid: str | None, tenant_uid_tenant_category_uid: str | None, tenant_uid_tenant_code: str | None, tenant_uid_tenant_description: str | None, tenant_uid_start_date: datetime.datetime | None, tenant_uid_end_date: datetime.datetime | None, tenant_uid_is_internal: int | None, tenant_uid_is_system: int | None, tenant_uid_is_test: int | None, tenant_uid_account_uid: str | None, account_uid_account_name: str | None, account_uid_tenant_uid: str | None, account_uid_account_type_uid: str | None, account_uid_account_title_uid: str | None, account_uid_account_division_uid: str | None, account_uid_account_group_uid: str | None, account_uid_auth_identity_uid: str | None, account_uid_account_email: str | None, account_uid_display_name: str | None, account_uid_is_system: int | None, calendar_type_uid_calendar_type_name: str | None):
        self.calendar_account_uid = calendar_account_uid
        self.calendar_account_name = calendar_account_name
        self.tenant_uid = tenant_uid
        self.account_uid = account_uid
        self.calendar_type_uid = calendar_type_uid
        self.row_instance = row_instance
        self.row_lock = row_lock
        self.row_owner = row_owner
        self.row_seq = row_seq
        self.row_guid = row_guid
        self.row_version = row_version
        self.is_active = is_active
        self.created_date = created_date
        self.created_by = created_by
        self.last_updated_date = last_updated_date
        self.last_updated_by = last_updated_by
        self.removed_date = removed_date
        self.removed_by = removed_by
        self.custom_attributes = custom_attributes
        self.calendar_account_uid_account_name = calendar_account_uid_account_name
        self.calendar_account_uid_tenant_uid = calendar_account_uid_tenant_uid
        self.calendar_account_uid_account_type_uid = calendar_account_uid_account_type_uid
        self.calendar_account_uid_account_title_uid = calendar_account_uid_account_title_uid
        self.calendar_account_uid_account_division_uid = calendar_account_uid_account_division_uid
        self.calendar_account_uid_account_group_uid = calendar_account_uid_account_group_uid
        self.calendar_account_uid_auth_identity_uid = calendar_account_uid_auth_identity_uid
        self.calendar_account_uid_account_email = calendar_account_uid_account_email
        self.calendar_account_uid_display_name = calendar_account_uid_display_name
        self.calendar_account_uid_is_system = calendar_account_uid_is_system
        self.tenant_uid_tenant_name = tenant_uid_tenant_name
        self.tenant_uid_country_uid = tenant_uid_country_uid
        self.tenant_uid_tenant_type_uid = tenant_uid_tenant_type_uid
        self.tenant_uid_tenant_category_uid = tenant_uid_tenant_category_uid
        self.tenant_uid_tenant_code = tenant_uid_tenant_code
        self.tenant_uid_tenant_description = tenant_uid_tenant_description
        self.tenant_uid_start_date = tenant_uid_start_date
        self.tenant_uid_end_date = tenant_uid_end_date
        self.tenant_uid_is_internal = tenant_uid_is_internal
        self.tenant_uid_is_system = tenant_uid_is_system
        self.tenant_uid_is_test = tenant_uid_is_test
        self.tenant_uid_account_uid = tenant_uid_account_uid
        self.account_uid_account_name = account_uid_account_name
        self.account_uid_tenant_uid = account_uid_tenant_uid
        self.account_uid_account_type_uid = account_uid_account_type_uid
        self.account_uid_account_title_uid = account_uid_account_title_uid
        self.account_uid_account_division_uid = account_uid_account_division_uid
        self.account_uid_account_group_uid = account_uid_account_group_uid
        self.account_uid_auth_identity_uid = account_uid_auth_identity_uid
        self.account_uid_account_email = account_uid_account_email
        self.account_uid_display_name = account_uid_display_name
        self.account_uid_is_system = account_uid_is_system
        self.calendar_type_uid_calendar_type_name = calendar_type_uid_calendar_type_name
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.calendar_account_uid, self.calendar_account_name, self.tenant_uid, self.account_uid, self.calendar_type_uid, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes, self.calendar_account_uid_account_name, self.calendar_account_uid_tenant_uid, self.calendar_account_uid_account_type_uid, self.calendar_account_uid_account_title_uid, self.calendar_account_uid_account_division_uid, self.calendar_account_uid_account_group_uid, self.calendar_account_uid_auth_identity_uid, self.calendar_account_uid_account_email, self.calendar_account_uid_display_name, self.calendar_account_uid_is_system, self.tenant_uid_tenant_name, self.tenant_uid_country_uid, self.tenant_uid_tenant_type_uid, self.tenant_uid_tenant_category_uid, self.tenant_uid_tenant_code, self.tenant_uid_tenant_description, self.tenant_uid_start_date, self.tenant_uid_end_date, self.tenant_uid_is_internal, self.tenant_uid_is_system, self.tenant_uid_is_test, self.tenant_uid_account_uid, self.account_uid_account_name, self.account_uid_tenant_uid, self.account_uid_account_type_uid, self.account_uid_account_title_uid, self.account_uid_account_division_uid, self.account_uid_account_group_uid, self.account_uid_auth_identity_uid, self.account_uid_account_email, self.account_uid_display_name, self.account_uid_is_system, self.calendar_type_uid_calendar_type_name]


@dataclass(frozen=False)
class calendar_approval_rich_dto(calendar_approval_read_dto):
    calendar_approval_uid: str | None
    calendar_approval_name: str | None
    client_uid: str | None
    account_uid: str | None
    calendar_approval_type_uid: str | None
    calendar_event_group_uid: str | None
    calendar_type_uid: str | None
    time_submit_type_name: str | None
    row_instance: str | None
    row_lock: str | None
    row_owner: str | None
    row_seq: int | None
    row_guid: str | None
    row_version: int | None
    is_active: int | None
    created_date: datetime.datetime | None
    created_by: str | None
    last_updated_date: datetime.datetime | None
    last_updated_by: str | None
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str | None
    client_uid_client_name: str | None
    client_uid_tenant_uid: str | None
    client_uid_country_uid: str | None
    client_uid_client_type_uid: str | None
    client_uid_client_category_uid: str | None
    client_uid_account_uid: str | None
    client_uid_client_code: str | None
    client_uid_client_description: str | None
    client_uid_start_date: datetime.datetime | None
    client_uid_end_date: datetime.datetime | None
    client_uid_is_internal: int | None
    client_uid_is_system: int | None
    client_uid_is_test: int | None
    account_uid_account_name: str | None
    account_uid_tenant_uid: str | None
    account_uid_account_type_uid: str | None
    account_uid_account_title_uid: str | None
    account_uid_account_division_uid: str | None
    account_uid_account_group_uid: str | None
    account_uid_auth_identity_uid: str | None
    account_uid_account_email: str | None
    account_uid_display_name: str | None
    account_uid_is_system: int | None
    calendar_approval_type_uid_calendar_approval_type_name: str | None
    calendar_event_group_uid_calendar_event_group_name: str | None
    calendar_event_group_uid_client_uid: str | None
    calendar_event_group_uid_account_uid: str | None
    calendar_event_group_uid_calendar_account_uid: str | None
    calendar_event_group_uid_calendar_event_type_uid: str | None
    calendar_event_group_uid_group_comment: str | None
    calendar_event_group_uid_event_start_date: datetime.datetime | None
    calendar_event_group_uid_event_end_date: datetime.datetime | None
    calendar_event_group_uid_is_approved: int | None
    calendar_type_uid_calendar_type_name: str | None
    def __init__(self, calendar_approval_uid: str | None, calendar_approval_name: str | None, client_uid: str | None, account_uid: str | None, calendar_approval_type_uid: str | None, calendar_event_group_uid: str | None, calendar_type_uid: str | None, time_submit_type_name: str | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None, client_uid_client_name: str | None, client_uid_tenant_uid: str | None, client_uid_country_uid: str | None, client_uid_client_type_uid: str | None, client_uid_client_category_uid: str | None, client_uid_account_uid: str | None, client_uid_client_code: str | None, client_uid_client_description: str | None, client_uid_start_date: datetime.datetime | None, client_uid_end_date: datetime.datetime | None, client_uid_is_internal: int | None, client_uid_is_system: int | None, client_uid_is_test: int | None, account_uid_account_name: str | None, account_uid_tenant_uid: str | None, account_uid_account_type_uid: str | None, account_uid_account_title_uid: str | None, account_uid_account_division_uid: str | None, account_uid_account_group_uid: str | None, account_uid_auth_identity_uid: str | None, account_uid_account_email: str | None, account_uid_display_name: str | None, account_uid_is_system: int | None, calendar_approval_type_uid_calendar_approval_type_name: str | None, calendar_event_group_uid_calendar_event_group_name: str | None, calendar_event_group_uid_client_uid: str | None, calendar_event_group_uid_account_uid: str | None, calendar_event_group_uid_calendar_account_uid: str | None, calendar_event_group_uid_calendar_event_type_uid: str | None, calendar_event_group_uid_group_comment: str | None, calendar_event_group_uid_event_start_date: datetime.datetime | None, calendar_event_group_uid_event_end_date: datetime.datetime | None, calendar_event_group_uid_is_approved: int | None, calendar_type_uid_calendar_type_name: str | None):
        self.calendar_approval_uid = calendar_approval_uid
        self.calendar_approval_name = calendar_approval_name
        self.client_uid = client_uid
        self.account_uid = account_uid
        self.calendar_approval_type_uid = calendar_approval_type_uid
        self.calendar_event_group_uid = calendar_event_group_uid
        self.calendar_type_uid = calendar_type_uid
        self.time_submit_type_name = time_submit_type_name
        self.row_instance = row_instance
        self.row_lock = row_lock
        self.row_owner = row_owner
        self.row_seq = row_seq
        self.row_guid = row_guid
        self.row_version = row_version
        self.is_active = is_active
        self.created_date = created_date
        self.created_by = created_by
        self.last_updated_date = last_updated_date
        self.last_updated_by = last_updated_by
        self.removed_date = removed_date
        self.removed_by = removed_by
        self.custom_attributes = custom_attributes
        self.client_uid_client_name = client_uid_client_name
        self.client_uid_tenant_uid = client_uid_tenant_uid
        self.client_uid_country_uid = client_uid_country_uid
        self.client_uid_client_type_uid = client_uid_client_type_uid
        self.client_uid_client_category_uid = client_uid_client_category_uid
        self.client_uid_account_uid = client_uid_account_uid
        self.client_uid_client_code = client_uid_client_code
        self.client_uid_client_description = client_uid_client_description
        self.client_uid_start_date = client_uid_start_date
        self.client_uid_end_date = client_uid_end_date
        self.client_uid_is_internal = client_uid_is_internal
        self.client_uid_is_system = client_uid_is_system
        self.client_uid_is_test = client_uid_is_test
        self.account_uid_account_name = account_uid_account_name
        self.account_uid_tenant_uid = account_uid_tenant_uid
        self.account_uid_account_type_uid = account_uid_account_type_uid
        self.account_uid_account_title_uid = account_uid_account_title_uid
        self.account_uid_account_division_uid = account_uid_account_division_uid
        self.account_uid_account_group_uid = account_uid_account_group_uid
        self.account_uid_auth_identity_uid = account_uid_auth_identity_uid
        self.account_uid_account_email = account_uid_account_email
        self.account_uid_display_name = account_uid_display_name
        self.account_uid_is_system = account_uid_is_system
        self.calendar_approval_type_uid_calendar_approval_type_name = calendar_approval_type_uid_calendar_approval_type_name
        self.calendar_event_group_uid_calendar_event_group_name = calendar_event_group_uid_calendar_event_group_name
        self.calendar_event_group_uid_client_uid = calendar_event_group_uid_client_uid
        self.calendar_event_group_uid_account_uid = calendar_event_group_uid_account_uid
        self.calendar_event_group_uid_calendar_account_uid = calendar_event_group_uid_calendar_account_uid
        self.calendar_event_group_uid_calendar_event_type_uid = calendar_event_group_uid_calendar_event_type_uid
        self.calendar_event_group_uid_group_comment = calendar_event_group_uid_group_comment
        self.calendar_event_group_uid_event_start_date = calendar_event_group_uid_event_start_date
        self.calendar_event_group_uid_event_end_date = calendar_event_group_uid_event_end_date
        self.calendar_event_group_uid_is_approved = calendar_event_group_uid_is_approved
        self.calendar_type_uid_calendar_type_name = calendar_type_uid_calendar_type_name
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.calendar_approval_uid, self.calendar_approval_name, self.client_uid, self.account_uid, self.calendar_approval_type_uid, self.calendar_event_group_uid, self.calendar_type_uid, self.time_submit_type_name, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes, self.client_uid_client_name, self.client_uid_tenant_uid, self.client_uid_country_uid, self.client_uid_client_type_uid, self.client_uid_client_category_uid, self.client_uid_account_uid, self.client_uid_client_code, self.client_uid_client_description, self.client_uid_start_date, self.client_uid_end_date, self.client_uid_is_internal, self.client_uid_is_system, self.client_uid_is_test, self.account_uid_account_name, self.account_uid_tenant_uid, self.account_uid_account_type_uid, self.account_uid_account_title_uid, self.account_uid_account_division_uid, self.account_uid_account_group_uid, self.account_uid_auth_identity_uid, self.account_uid_account_email, self.account_uid_display_name, self.account_uid_is_system, self.calendar_approval_type_uid_calendar_approval_type_name, self.calendar_event_group_uid_calendar_event_group_name, self.calendar_event_group_uid_client_uid, self.calendar_event_group_uid_account_uid, self.calendar_event_group_uid_calendar_account_uid, self.calendar_event_group_uid_calendar_event_type_uid, self.calendar_event_group_uid_group_comment, self.calendar_event_group_uid_event_start_date, self.calendar_event_group_uid_event_end_date, self.calendar_event_group_uid_is_approved, self.calendar_type_uid_calendar_type_name]


@dataclass(frozen=False)
class calendar_approval_type_rich_dto(calendar_approval_type_read_dto):
    calendar_approval_type_uid: str | None
    calendar_approval_type_name: str | None
    row_instance: str | None
    row_lock: str | None
    row_owner: str | None
    row_seq: int | None
    row_guid: str | None
    row_version: int | None
    is_active: int | None
    created_date: datetime.datetime | None
    created_by: str | None
    last_updated_date: datetime.datetime | None
    last_updated_by: str | None
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str | None
    def __init__(self, calendar_approval_type_uid: str | None, calendar_approval_type_name: str | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None):
        self.calendar_approval_type_uid = calendar_approval_type_uid
        self.calendar_approval_type_name = calendar_approval_type_name
        self.row_instance = row_instance
        self.row_lock = row_lock
        self.row_owner = row_owner
        self.row_seq = row_seq
        self.row_guid = row_guid
        self.row_version = row_version
        self.is_active = is_active
        self.created_date = created_date
        self.created_by = created_by
        self.last_updated_date = last_updated_date
        self.last_updated_by = last_updated_by
        self.removed_date = removed_date
        self.removed_by = removed_by
        self.custom_attributes = custom_attributes
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.calendar_approval_type_uid, self.calendar_approval_type_name, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]


@dataclass(frozen=False)
class calendar_event_rich_dto(calendar_event_read_dto):
    calendar_event_uid: str | None
    calendar_event_name: str | None
    client_uid: str | None
    account_uid: str | None
    calendar_event_group_uid: str | None
    calendar_type_uid: str | None
    row_instance: str | None
    row_lock: str | None
    row_owner: str | None
    row_seq: int | None
    row_guid: str | None
    row_version: int | None
    is_active: int | None
    created_date: datetime.datetime | None
    created_by: str | None
    last_updated_date: datetime.datetime | None
    last_updated_by: str | None
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str | None
    client_uid_client_name: str | None
    client_uid_tenant_uid: str | None
    client_uid_country_uid: str | None
    client_uid_client_type_uid: str | None
    client_uid_client_category_uid: str | None
    client_uid_account_uid: str | None
    client_uid_client_code: str | None
    client_uid_client_description: str | None
    client_uid_start_date: datetime.datetime | None
    client_uid_end_date: datetime.datetime | None
    client_uid_is_internal: int | None
    client_uid_is_system: int | None
    client_uid_is_test: int | None
    account_uid_account_name: str | None
    account_uid_tenant_uid: str | None
    account_uid_account_type_uid: str | None
    account_uid_account_title_uid: str | None
    account_uid_account_division_uid: str | None
    account_uid_account_group_uid: str | None
    account_uid_auth_identity_uid: str | None
    account_uid_account_email: str | None
    account_uid_display_name: str | None
    account_uid_is_system: int | None
    calendar_event_group_uid_calendar_event_group_name: str | None
    calendar_event_group_uid_client_uid: str | None
    calendar_event_group_uid_account_uid: str | None
    calendar_event_group_uid_calendar_account_uid: str | None
    calendar_event_group_uid_calendar_event_type_uid: str | None
    calendar_event_group_uid_group_comment: str | None
    calendar_event_group_uid_event_start_date: datetime.datetime | None
    calendar_event_group_uid_event_end_date: datetime.datetime | None
    calendar_event_group_uid_is_approved: int | None
    calendar_type_uid_calendar_type_name: str | None
    def __init__(self, calendar_event_uid: str | None, calendar_event_name: str | None, client_uid: str | None, account_uid: str | None, calendar_event_group_uid: str | None, calendar_type_uid: str | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None, client_uid_client_name: str | None, client_uid_tenant_uid: str | None, client_uid_country_uid: str | None, client_uid_client_type_uid: str | None, client_uid_client_category_uid: str | None, client_uid_account_uid: str | None, client_uid_client_code: str | None, client_uid_client_description: str | None, client_uid_start_date: datetime.datetime | None, client_uid_end_date: datetime.datetime | None, client_uid_is_internal: int | None, client_uid_is_system: int | None, client_uid_is_test: int | None, account_uid_account_name: str | None, account_uid_tenant_uid: str | None, account_uid_account_type_uid: str | None, account_uid_account_title_uid: str | None, account_uid_account_division_uid: str | None, account_uid_account_group_uid: str | None, account_uid_auth_identity_uid: str | None, account_uid_account_email: str | None, account_uid_display_name: str | None, account_uid_is_system: int | None, calendar_event_group_uid_calendar_event_group_name: str | None, calendar_event_group_uid_client_uid: str | None, calendar_event_group_uid_account_uid: str | None, calendar_event_group_uid_calendar_account_uid: str | None, calendar_event_group_uid_calendar_event_type_uid: str | None, calendar_event_group_uid_group_comment: str | None, calendar_event_group_uid_event_start_date: datetime.datetime | None, calendar_event_group_uid_event_end_date: datetime.datetime | None, calendar_event_group_uid_is_approved: int | None, calendar_type_uid_calendar_type_name: str | None):
        self.calendar_event_uid = calendar_event_uid
        self.calendar_event_name = calendar_event_name
        self.client_uid = client_uid
        self.account_uid = account_uid
        self.calendar_event_group_uid = calendar_event_group_uid
        self.calendar_type_uid = calendar_type_uid
        self.row_instance = row_instance
        self.row_lock = row_lock
        self.row_owner = row_owner
        self.row_seq = row_seq
        self.row_guid = row_guid
        self.row_version = row_version
        self.is_active = is_active
        self.created_date = created_date
        self.created_by = created_by
        self.last_updated_date = last_updated_date
        self.last_updated_by = last_updated_by
        self.removed_date = removed_date
        self.removed_by = removed_by
        self.custom_attributes = custom_attributes
        self.client_uid_client_name = client_uid_client_name
        self.client_uid_tenant_uid = client_uid_tenant_uid
        self.client_uid_country_uid = client_uid_country_uid
        self.client_uid_client_type_uid = client_uid_client_type_uid
        self.client_uid_client_category_uid = client_uid_client_category_uid
        self.client_uid_account_uid = client_uid_account_uid
        self.client_uid_client_code = client_uid_client_code
        self.client_uid_client_description = client_uid_client_description
        self.client_uid_start_date = client_uid_start_date
        self.client_uid_end_date = client_uid_end_date
        self.client_uid_is_internal = client_uid_is_internal
        self.client_uid_is_system = client_uid_is_system
        self.client_uid_is_test = client_uid_is_test
        self.account_uid_account_name = account_uid_account_name
        self.account_uid_tenant_uid = account_uid_tenant_uid
        self.account_uid_account_type_uid = account_uid_account_type_uid
        self.account_uid_account_title_uid = account_uid_account_title_uid
        self.account_uid_account_division_uid = account_uid_account_division_uid
        self.account_uid_account_group_uid = account_uid_account_group_uid
        self.account_uid_auth_identity_uid = account_uid_auth_identity_uid
        self.account_uid_account_email = account_uid_account_email
        self.account_uid_display_name = account_uid_display_name
        self.account_uid_is_system = account_uid_is_system
        self.calendar_event_group_uid_calendar_event_group_name = calendar_event_group_uid_calendar_event_group_name
        self.calendar_event_group_uid_client_uid = calendar_event_group_uid_client_uid
        self.calendar_event_group_uid_account_uid = calendar_event_group_uid_account_uid
        self.calendar_event_group_uid_calendar_account_uid = calendar_event_group_uid_calendar_account_uid
        self.calendar_event_group_uid_calendar_event_type_uid = calendar_event_group_uid_calendar_event_type_uid
        self.calendar_event_group_uid_group_comment = calendar_event_group_uid_group_comment
        self.calendar_event_group_uid_event_start_date = calendar_event_group_uid_event_start_date
        self.calendar_event_group_uid_event_end_date = calendar_event_group_uid_event_end_date
        self.calendar_event_group_uid_is_approved = calendar_event_group_uid_is_approved
        self.calendar_type_uid_calendar_type_name = calendar_type_uid_calendar_type_name
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.calendar_event_uid, self.calendar_event_name, self.client_uid, self.account_uid, self.calendar_event_group_uid, self.calendar_type_uid, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes, self.client_uid_client_name, self.client_uid_tenant_uid, self.client_uid_country_uid, self.client_uid_client_type_uid, self.client_uid_client_category_uid, self.client_uid_account_uid, self.client_uid_client_code, self.client_uid_client_description, self.client_uid_start_date, self.client_uid_end_date, self.client_uid_is_internal, self.client_uid_is_system, self.client_uid_is_test, self.account_uid_account_name, self.account_uid_tenant_uid, self.account_uid_account_type_uid, self.account_uid_account_title_uid, self.account_uid_account_division_uid, self.account_uid_account_group_uid, self.account_uid_auth_identity_uid, self.account_uid_account_email, self.account_uid_display_name, self.account_uid_is_system, self.calendar_event_group_uid_calendar_event_group_name, self.calendar_event_group_uid_client_uid, self.calendar_event_group_uid_account_uid, self.calendar_event_group_uid_calendar_account_uid, self.calendar_event_group_uid_calendar_event_type_uid, self.calendar_event_group_uid_group_comment, self.calendar_event_group_uid_event_start_date, self.calendar_event_group_uid_event_end_date, self.calendar_event_group_uid_is_approved, self.calendar_type_uid_calendar_type_name]


@dataclass(frozen=False)
class calendar_event_group_rich_dto(calendar_event_group_read_dto):
    calendar_event_group_uid: str | None
    calendar_event_group_name: str | None
    client_uid: str | None
    account_uid: str | None
    calendar_account_uid: str | None
    calendar_event_type_uid: str | None
    group_comment: str | None
    event_start_date: datetime.datetime | None
    event_end_date: datetime.datetime | None
    is_approved: int | None
    row_instance: str | None
    row_lock: str | None
    row_owner: str | None
    row_seq: int | None
    row_guid: str | None
    row_version: int | None
    is_active: int | None
    created_date: datetime.datetime | None
    created_by: str | None
    last_updated_date: datetime.datetime | None
    last_updated_by: str | None
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str | None
    client_uid_client_name: str | None
    client_uid_tenant_uid: str | None
    client_uid_country_uid: str | None
    client_uid_client_type_uid: str | None
    client_uid_client_category_uid: str | None
    client_uid_account_uid: str | None
    client_uid_client_code: str | None
    client_uid_client_description: str | None
    client_uid_start_date: datetime.datetime | None
    client_uid_end_date: datetime.datetime | None
    client_uid_is_internal: int | None
    client_uid_is_system: int | None
    client_uid_is_test: int | None
    account_uid_account_name: str | None
    account_uid_tenant_uid: str | None
    account_uid_account_type_uid: str | None
    account_uid_account_title_uid: str | None
    account_uid_account_division_uid: str | None
    account_uid_account_group_uid: str | None
    account_uid_auth_identity_uid: str | None
    account_uid_account_email: str | None
    account_uid_display_name: str | None
    account_uid_is_system: int | None
    calendar_account_uid_account_name: str | None
    calendar_account_uid_tenant_uid: str | None
    calendar_account_uid_account_type_uid: str | None
    calendar_account_uid_account_title_uid: str | None
    calendar_account_uid_account_division_uid: str | None
    calendar_account_uid_account_group_uid: str | None
    calendar_account_uid_auth_identity_uid: str | None
    calendar_account_uid_account_email: str | None
    calendar_account_uid_display_name: str | None
    calendar_account_uid_is_system: int | None
    calendar_event_type_uid_calendar_event_type_name: str | None
    calendar_event_type_uid_client_uid: str | None
    calendar_event_type_uid_calendar_type_uid: str | None
    calendar_event_type_uid_auto_approved: int | None
    def __init__(self, calendar_event_group_uid: str | None, calendar_event_group_name: str | None, client_uid: str | None, account_uid: str | None, calendar_account_uid: str | None, calendar_event_type_uid: str | None, group_comment: str | None, event_start_date: datetime.datetime | None, event_end_date: datetime.datetime | None, is_approved: int | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None, client_uid_client_name: str | None, client_uid_tenant_uid: str | None, client_uid_country_uid: str | None, client_uid_client_type_uid: str | None, client_uid_client_category_uid: str | None, client_uid_account_uid: str | None, client_uid_client_code: str | None, client_uid_client_description: str | None, client_uid_start_date: datetime.datetime | None, client_uid_end_date: datetime.datetime | None, client_uid_is_internal: int | None, client_uid_is_system: int | None, client_uid_is_test: int | None, account_uid_account_name: str | None, account_uid_tenant_uid: str | None, account_uid_account_type_uid: str | None, account_uid_account_title_uid: str | None, account_uid_account_division_uid: str | None, account_uid_account_group_uid: str | None, account_uid_auth_identity_uid: str | None, account_uid_account_email: str | None, account_uid_display_name: str | None, account_uid_is_system: int | None, calendar_account_uid_account_name: str | None, calendar_account_uid_tenant_uid: str | None, calendar_account_uid_account_type_uid: str | None, calendar_account_uid_account_title_uid: str | None, calendar_account_uid_account_division_uid: str | None, calendar_account_uid_account_group_uid: str | None, calendar_account_uid_auth_identity_uid: str | None, calendar_account_uid_account_email: str | None, calendar_account_uid_display_name: str | None, calendar_account_uid_is_system: int | None, calendar_event_type_uid_calendar_event_type_name: str | None, calendar_event_type_uid_client_uid: str | None, calendar_event_type_uid_calendar_type_uid: str | None, calendar_event_type_uid_auto_approved: int | None):
        self.calendar_event_group_uid = calendar_event_group_uid
        self.calendar_event_group_name = calendar_event_group_name
        self.client_uid = client_uid
        self.account_uid = account_uid
        self.calendar_account_uid = calendar_account_uid
        self.calendar_event_type_uid = calendar_event_type_uid
        self.group_comment = group_comment
        self.event_start_date = event_start_date
        self.event_end_date = event_end_date
        self.is_approved = is_approved
        self.row_instance = row_instance
        self.row_lock = row_lock
        self.row_owner = row_owner
        self.row_seq = row_seq
        self.row_guid = row_guid
        self.row_version = row_version
        self.is_active = is_active
        self.created_date = created_date
        self.created_by = created_by
        self.last_updated_date = last_updated_date
        self.last_updated_by = last_updated_by
        self.removed_date = removed_date
        self.removed_by = removed_by
        self.custom_attributes = custom_attributes
        self.client_uid_client_name = client_uid_client_name
        self.client_uid_tenant_uid = client_uid_tenant_uid
        self.client_uid_country_uid = client_uid_country_uid
        self.client_uid_client_type_uid = client_uid_client_type_uid
        self.client_uid_client_category_uid = client_uid_client_category_uid
        self.client_uid_account_uid = client_uid_account_uid
        self.client_uid_client_code = client_uid_client_code
        self.client_uid_client_description = client_uid_client_description
        self.client_uid_start_date = client_uid_start_date
        self.client_uid_end_date = client_uid_end_date
        self.client_uid_is_internal = client_uid_is_internal
        self.client_uid_is_system = client_uid_is_system
        self.client_uid_is_test = client_uid_is_test
        self.account_uid_account_name = account_uid_account_name
        self.account_uid_tenant_uid = account_uid_tenant_uid
        self.account_uid_account_type_uid = account_uid_account_type_uid
        self.account_uid_account_title_uid = account_uid_account_title_uid
        self.account_uid_account_division_uid = account_uid_account_division_uid
        self.account_uid_account_group_uid = account_uid_account_group_uid
        self.account_uid_auth_identity_uid = account_uid_auth_identity_uid
        self.account_uid_account_email = account_uid_account_email
        self.account_uid_display_name = account_uid_display_name
        self.account_uid_is_system = account_uid_is_system
        self.calendar_account_uid_account_name = calendar_account_uid_account_name
        self.calendar_account_uid_tenant_uid = calendar_account_uid_tenant_uid
        self.calendar_account_uid_account_type_uid = calendar_account_uid_account_type_uid
        self.calendar_account_uid_account_title_uid = calendar_account_uid_account_title_uid
        self.calendar_account_uid_account_division_uid = calendar_account_uid_account_division_uid
        self.calendar_account_uid_account_group_uid = calendar_account_uid_account_group_uid
        self.calendar_account_uid_auth_identity_uid = calendar_account_uid_auth_identity_uid
        self.calendar_account_uid_account_email = calendar_account_uid_account_email
        self.calendar_account_uid_display_name = calendar_account_uid_display_name
        self.calendar_account_uid_is_system = calendar_account_uid_is_system
        self.calendar_event_type_uid_calendar_event_type_name = calendar_event_type_uid_calendar_event_type_name
        self.calendar_event_type_uid_client_uid = calendar_event_type_uid_client_uid
        self.calendar_event_type_uid_calendar_type_uid = calendar_event_type_uid_calendar_type_uid
        self.calendar_event_type_uid_auto_approved = calendar_event_type_uid_auto_approved
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.calendar_event_group_uid, self.calendar_event_group_name, self.client_uid, self.account_uid, self.calendar_account_uid, self.calendar_event_type_uid, self.group_comment, self.event_start_date, self.event_end_date, self.is_approved, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes, self.client_uid_client_name, self.client_uid_tenant_uid, self.client_uid_country_uid, self.client_uid_client_type_uid, self.client_uid_client_category_uid, self.client_uid_account_uid, self.client_uid_client_code, self.client_uid_client_description, self.client_uid_start_date, self.client_uid_end_date, self.client_uid_is_internal, self.client_uid_is_system, self.client_uid_is_test, self.account_uid_account_name, self.account_uid_tenant_uid, self.account_uid_account_type_uid, self.account_uid_account_title_uid, self.account_uid_account_division_uid, self.account_uid_account_group_uid, self.account_uid_auth_identity_uid, self.account_uid_account_email, self.account_uid_display_name, self.account_uid_is_system, self.calendar_account_uid_account_name, self.calendar_account_uid_tenant_uid, self.calendar_account_uid_account_type_uid, self.calendar_account_uid_account_title_uid, self.calendar_account_uid_account_division_uid, self.calendar_account_uid_account_group_uid, self.calendar_account_uid_auth_identity_uid, self.calendar_account_uid_account_email, self.calendar_account_uid_display_name, self.calendar_account_uid_is_system, self.calendar_event_type_uid_calendar_event_type_name, self.calendar_event_type_uid_client_uid, self.calendar_event_type_uid_calendar_type_uid, self.calendar_event_type_uid_auto_approved]


@dataclass(frozen=False)
class calendar_event_type_rich_dto(calendar_event_type_read_dto):
    calendar_event_type_uid: str | None
    calendar_event_type_name: str | None
    client_uid: str | None
    calendar_type_uid: str | None
    auto_approved: int | None
    row_instance: str | None
    row_lock: str | None
    row_owner: str | None
    row_seq: int | None
    row_guid: str | None
    row_version: int | None
    is_active: int | None
    created_date: datetime.datetime | None
    created_by: str | None
    last_updated_date: datetime.datetime | None
    last_updated_by: str | None
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str | None
    calendar_event_type_uid_event_type_name: str | None
    calendar_event_type_uid_event_type_description: str | None
    client_uid_client_name: str | None
    client_uid_tenant_uid: str | None
    client_uid_country_uid: str | None
    client_uid_client_type_uid: str | None
    client_uid_client_category_uid: str | None
    client_uid_account_uid: str | None
    client_uid_client_code: str | None
    client_uid_client_description: str | None
    client_uid_start_date: datetime.datetime | None
    client_uid_end_date: datetime.datetime | None
    client_uid_is_internal: int | None
    client_uid_is_system: int | None
    client_uid_is_test: int | None
    calendar_type_uid_calendar_type_name: str | None
    def __init__(self, calendar_event_type_uid: str | None, calendar_event_type_name: str | None, client_uid: str | None, calendar_type_uid: str | None, auto_approved: int | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None, calendar_event_type_uid_event_type_name: str | None, calendar_event_type_uid_event_type_description: str | None, client_uid_client_name: str | None, client_uid_tenant_uid: str | None, client_uid_country_uid: str | None, client_uid_client_type_uid: str | None, client_uid_client_category_uid: str | None, client_uid_account_uid: str | None, client_uid_client_code: str | None, client_uid_client_description: str | None, client_uid_start_date: datetime.datetime | None, client_uid_end_date: datetime.datetime | None, client_uid_is_internal: int | None, client_uid_is_system: int | None, client_uid_is_test: int | None, calendar_type_uid_calendar_type_name: str | None):
        self.calendar_event_type_uid = calendar_event_type_uid
        self.calendar_event_type_name = calendar_event_type_name
        self.client_uid = client_uid
        self.calendar_type_uid = calendar_type_uid
        self.auto_approved = auto_approved
        self.row_instance = row_instance
        self.row_lock = row_lock
        self.row_owner = row_owner
        self.row_seq = row_seq
        self.row_guid = row_guid
        self.row_version = row_version
        self.is_active = is_active
        self.created_date = created_date
        self.created_by = created_by
        self.last_updated_date = last_updated_date
        self.last_updated_by = last_updated_by
        self.removed_date = removed_date
        self.removed_by = removed_by
        self.custom_attributes = custom_attributes
        self.calendar_event_type_uid_event_type_name = calendar_event_type_uid_event_type_name
        self.calendar_event_type_uid_event_type_description = calendar_event_type_uid_event_type_description
        self.client_uid_client_name = client_uid_client_name
        self.client_uid_tenant_uid = client_uid_tenant_uid
        self.client_uid_country_uid = client_uid_country_uid
        self.client_uid_client_type_uid = client_uid_client_type_uid
        self.client_uid_client_category_uid = client_uid_client_category_uid
        self.client_uid_account_uid = client_uid_account_uid
        self.client_uid_client_code = client_uid_client_code
        self.client_uid_client_description = client_uid_client_description
        self.client_uid_start_date = client_uid_start_date
        self.client_uid_end_date = client_uid_end_date
        self.client_uid_is_internal = client_uid_is_internal
        self.client_uid_is_system = client_uid_is_system
        self.client_uid_is_test = client_uid_is_test
        self.calendar_type_uid_calendar_type_name = calendar_type_uid_calendar_type_name
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.calendar_event_type_uid, self.calendar_event_type_name, self.client_uid, self.calendar_type_uid, self.auto_approved, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes, self.calendar_event_type_uid_event_type_name, self.calendar_event_type_uid_event_type_description, self.client_uid_client_name, self.client_uid_tenant_uid, self.client_uid_country_uid, self.client_uid_client_type_uid, self.client_uid_client_category_uid, self.client_uid_account_uid, self.client_uid_client_code, self.client_uid_client_description, self.client_uid_start_date, self.client_uid_end_date, self.client_uid_is_internal, self.client_uid_is_system, self.client_uid_is_test, self.calendar_type_uid_calendar_type_name]


@dataclass(frozen=False)
class calendar_type_rich_dto(calendar_type_read_dto):
    calendar_type_uid: str | None
    calendar_type_name: str | None
    row_instance: str | None
    row_seq: int | None
    row_guid: str | None
    row_version: int | None
    is_active: int | None
    created_date: datetime.datetime | None
    created_by: str | None
    last_updated_date: datetime.datetime | None
    last_updated_by: str | None
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str | None
    def __init__(self, calendar_type_uid: str | None, calendar_type_name: str | None, row_instance: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None):
        self.calendar_type_uid = calendar_type_uid
        self.calendar_type_name = calendar_type_name
        self.row_instance = row_instance
        self.row_seq = row_seq
        self.row_guid = row_guid
        self.row_version = row_version
        self.is_active = is_active
        self.created_date = created_date
        self.created_by = created_by
        self.last_updated_date = last_updated_date
        self.last_updated_by = last_updated_by
        self.removed_date = removed_date
        self.removed_by = removed_by
        self.custom_attributes = custom_attributes
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.calendar_type_uid, self.calendar_type_name, self.row_instance, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]


@dataclass(frozen=False)
class client_rich_dto(client_read_dto):
    client_uid: str | None
    client_name: str | None
    tenant_uid: str | None
    country_uid: str | None
    client_type_uid: str | None
    client_category_uid: str | None
    account_uid: str | None
    client_code: str | None
    client_description: str | None
    start_date: datetime.datetime | None
    end_date: datetime.datetime | None
    is_internal: int | None
    is_system: int | None
    is_test: int | None
    row_instance: str | None
    row_lock: str | None
    row_owner: str | None
    row_seq: int | None
    row_guid: str | None
    row_version: int | None
    is_active: int | None
    created_date: datetime.datetime | None
    created_by: str | None
    last_updated_date: datetime.datetime | None
    last_updated_by: str | None
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str | None
    tenant_uid_tenant_name: str | None
    tenant_uid_country_uid: str | None
    tenant_uid_tenant_type_uid: str | None
    tenant_uid_tenant_category_uid: str | None
    tenant_uid_tenant_code: str | None
    tenant_uid_tenant_description: str | None
    tenant_uid_start_date: datetime.datetime | None
    tenant_uid_end_date: datetime.datetime | None
    tenant_uid_is_internal: int | None
    tenant_uid_is_system: int | None
    tenant_uid_is_test: int | None
    tenant_uid_account_uid: str | None
    country_uid_country_name: str | None
    country_uid_continent_name: str | None
    country_uid_continent_code: str | None
    country_uid_country_iso3: str | None
    country_uid_country_code: str | None
    country_uid_phone_code: str | None
    country_uid_currency_code: str | None
    country_uid_capital_name: str | None
    country_uid_region_name: str | None
    country_uid_subregion_name: str | None
    country_uid_region_code: str | None
    country_uid_latitude: str | None
    country_uid_longitude: str | None
    country_uid_currency_name: str | None
    country_uid_population: str | None
    country_uid_languages: str | None
    country_uid_area: str | None
    country_uid_bar_code: str | None
    country_uid_top_level_domain: str | None
    country_uid_is_focused: int | None
    client_type_uid_client_type_name: str | None
    client_type_uid_client_type_description: str | None
    account_uid_account_name: str | None
    account_uid_tenant_uid: str | None
    account_uid_account_type_uid: str | None
    account_uid_account_title_uid: str | None
    account_uid_account_division_uid: str | None
    account_uid_account_group_uid: str | None
    account_uid_auth_identity_uid: str | None
    account_uid_account_email: str | None
    account_uid_display_name: str | None
    account_uid_is_system: int | None
    def __init__(self, client_uid: str | None, client_name: str | None, tenant_uid: str | None, country_uid: str | None, client_type_uid: str | None, client_category_uid: str | None, account_uid: str | None, client_code: str | None, client_description: str | None, start_date: datetime.datetime | None, end_date: datetime.datetime | None, is_internal: int | None, is_system: int | None, is_test: int | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None, tenant_uid_tenant_name: str | None, tenant_uid_country_uid: str | None, tenant_uid_tenant_type_uid: str | None, tenant_uid_tenant_category_uid: str | None, tenant_uid_tenant_code: str | None, tenant_uid_tenant_description: str | None, tenant_uid_start_date: datetime.datetime | None, tenant_uid_end_date: datetime.datetime | None, tenant_uid_is_internal: int | None, tenant_uid_is_system: int | None, tenant_uid_is_test: int | None, tenant_uid_account_uid: str | None, country_uid_country_name: str | None, country_uid_continent_name: str | None, country_uid_continent_code: str | None, country_uid_country_iso3: str | None, country_uid_country_code: str | None, country_uid_phone_code: str | None, country_uid_currency_code: str | None, country_uid_capital_name: str | None, country_uid_region_name: str | None, country_uid_subregion_name: str | None, country_uid_region_code: str | None, country_uid_latitude: str | None, country_uid_longitude: str | None, country_uid_currency_name: str | None, country_uid_population: str | None, country_uid_languages: str | None, country_uid_area: str | None, country_uid_bar_code: str | None, country_uid_top_level_domain: str | None, country_uid_is_focused: int | None, client_type_uid_client_type_name: str | None, client_type_uid_client_type_description: str | None, account_uid_account_name: str | None, account_uid_tenant_uid: str | None, account_uid_account_type_uid: str | None, account_uid_account_title_uid: str | None, account_uid_account_division_uid: str | None, account_uid_account_group_uid: str | None, account_uid_auth_identity_uid: str | None, account_uid_account_email: str | None, account_uid_display_name: str | None, account_uid_is_system: int | None):
        self.client_uid = client_uid
        self.client_name = client_name
        self.tenant_uid = tenant_uid
        self.country_uid = country_uid
        self.client_type_uid = client_type_uid
        self.client_category_uid = client_category_uid
        self.account_uid = account_uid
        self.client_code = client_code
        self.client_description = client_description
        self.start_date = start_date
        self.end_date = end_date
        self.is_internal = is_internal
        self.is_system = is_system
        self.is_test = is_test
        self.row_instance = row_instance
        self.row_lock = row_lock
        self.row_owner = row_owner
        self.row_seq = row_seq
        self.row_guid = row_guid
        self.row_version = row_version
        self.is_active = is_active
        self.created_date = created_date
        self.created_by = created_by
        self.last_updated_date = last_updated_date
        self.last_updated_by = last_updated_by
        self.removed_date = removed_date
        self.removed_by = removed_by
        self.custom_attributes = custom_attributes
        self.tenant_uid_tenant_name = tenant_uid_tenant_name
        self.tenant_uid_country_uid = tenant_uid_country_uid
        self.tenant_uid_tenant_type_uid = tenant_uid_tenant_type_uid
        self.tenant_uid_tenant_category_uid = tenant_uid_tenant_category_uid
        self.tenant_uid_tenant_code = tenant_uid_tenant_code
        self.tenant_uid_tenant_description = tenant_uid_tenant_description
        self.tenant_uid_start_date = tenant_uid_start_date
        self.tenant_uid_end_date = tenant_uid_end_date
        self.tenant_uid_is_internal = tenant_uid_is_internal
        self.tenant_uid_is_system = tenant_uid_is_system
        self.tenant_uid_is_test = tenant_uid_is_test
        self.tenant_uid_account_uid = tenant_uid_account_uid
        self.country_uid_country_name = country_uid_country_name
        self.country_uid_continent_name = country_uid_continent_name
        self.country_uid_continent_code = country_uid_continent_code
        self.country_uid_country_iso3 = country_uid_country_iso3
        self.country_uid_country_code = country_uid_country_code
        self.country_uid_phone_code = country_uid_phone_code
        self.country_uid_currency_code = country_uid_currency_code
        self.country_uid_capital_name = country_uid_capital_name
        self.country_uid_region_name = country_uid_region_name
        self.country_uid_subregion_name = country_uid_subregion_name
        self.country_uid_region_code = country_uid_region_code
        self.country_uid_latitude = country_uid_latitude
        self.country_uid_longitude = country_uid_longitude
        self.country_uid_currency_name = country_uid_currency_name
        self.country_uid_population = country_uid_population
        self.country_uid_languages = country_uid_languages
        self.country_uid_area = country_uid_area
        self.country_uid_bar_code = country_uid_bar_code
        self.country_uid_top_level_domain = country_uid_top_level_domain
        self.country_uid_is_focused = country_uid_is_focused
        self.client_type_uid_client_type_name = client_type_uid_client_type_name
        self.client_type_uid_client_type_description = client_type_uid_client_type_description
        self.account_uid_account_name = account_uid_account_name
        self.account_uid_tenant_uid = account_uid_tenant_uid
        self.account_uid_account_type_uid = account_uid_account_type_uid
        self.account_uid_account_title_uid = account_uid_account_title_uid
        self.account_uid_account_division_uid = account_uid_account_division_uid
        self.account_uid_account_group_uid = account_uid_account_group_uid
        self.account_uid_auth_identity_uid = account_uid_auth_identity_uid
        self.account_uid_account_email = account_uid_account_email
        self.account_uid_display_name = account_uid_display_name
        self.account_uid_is_system = account_uid_is_system
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.client_uid, self.client_name, self.tenant_uid, self.country_uid, self.client_type_uid, self.client_category_uid, self.account_uid, self.client_code, self.client_description, self.start_date, self.end_date, self.is_internal, self.is_system, self.is_test, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes, self.tenant_uid_tenant_name, self.tenant_uid_country_uid, self.tenant_uid_tenant_type_uid, self.tenant_uid_tenant_category_uid, self.tenant_uid_tenant_code, self.tenant_uid_tenant_description, self.tenant_uid_start_date, self.tenant_uid_end_date, self.tenant_uid_is_internal, self.tenant_uid_is_system, self.tenant_uid_is_test, self.tenant_uid_account_uid, self.country_uid_country_name, self.country_uid_continent_name, self.country_uid_continent_code, self.country_uid_country_iso3, self.country_uid_country_code, self.country_uid_phone_code, self.country_uid_currency_code, self.country_uid_capital_name, self.country_uid_region_name, self.country_uid_subregion_name, self.country_uid_region_code, self.country_uid_latitude, self.country_uid_longitude, self.country_uid_currency_name, self.country_uid_population, self.country_uid_languages, self.country_uid_area, self.country_uid_bar_code, self.country_uid_top_level_domain, self.country_uid_is_focused, self.client_type_uid_client_type_name, self.client_type_uid_client_type_description, self.account_uid_account_name, self.account_uid_tenant_uid, self.account_uid_account_type_uid, self.account_uid_account_title_uid, self.account_uid_account_division_uid, self.account_uid_account_group_uid, self.account_uid_auth_identity_uid, self.account_uid_account_email, self.account_uid_display_name, self.account_uid_is_system]


@dataclass(frozen=False)
class client_account_rich_dto(client_account_read_dto):
    client_account_uid: str | None
    client_account_name: str | None
    tenant_uid: str | None
    client_uid: str | None
    account_uid: str | None
    client_role_uid: str | None
    row_instance: str | None
    row_lock: str | None
    row_owner: str | None
    row_seq: int | None
    row_guid: str | None
    row_version: int | None
    is_active: int | None
    created_date: datetime.datetime | None
    created_by: str | None
    last_updated_date: datetime.datetime | None
    last_updated_by: str | None
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str | None
    client_account_uid_account_name: str | None
    client_account_uid_tenant_uid: str | None
    client_account_uid_account_type_uid: str | None
    client_account_uid_account_title_uid: str | None
    client_account_uid_account_division_uid: str | None
    client_account_uid_account_group_uid: str | None
    client_account_uid_auth_identity_uid: str | None
    client_account_uid_account_email: str | None
    client_account_uid_display_name: str | None
    client_account_uid_is_system: int | None
    tenant_uid_tenant_name: str | None
    tenant_uid_country_uid: str | None
    tenant_uid_tenant_type_uid: str | None
    tenant_uid_tenant_category_uid: str | None
    tenant_uid_tenant_code: str | None
    tenant_uid_tenant_description: str | None
    tenant_uid_start_date: datetime.datetime | None
    tenant_uid_end_date: datetime.datetime | None
    tenant_uid_is_internal: int | None
    tenant_uid_is_system: int | None
    tenant_uid_is_test: int | None
    tenant_uid_account_uid: str | None
    client_uid_client_name: str | None
    client_uid_tenant_uid: str | None
    client_uid_country_uid: str | None
    client_uid_client_type_uid: str | None
    client_uid_client_category_uid: str | None
    client_uid_account_uid: str | None
    client_uid_client_code: str | None
    client_uid_client_description: str | None
    client_uid_start_date: datetime.datetime | None
    client_uid_end_date: datetime.datetime | None
    client_uid_is_internal: int | None
    client_uid_is_system: int | None
    client_uid_is_test: int | None
    account_uid_account_name: str | None
    account_uid_tenant_uid: str | None
    account_uid_account_type_uid: str | None
    account_uid_account_title_uid: str | None
    account_uid_account_division_uid: str | None
    account_uid_account_group_uid: str | None
    account_uid_auth_identity_uid: str | None
    account_uid_account_email: str | None
    account_uid_display_name: str | None
    account_uid_is_system: int | None
    client_role_uid_client_role_name: str | None
    client_role_uid_role_description: str | None
    def __init__(self, client_account_uid: str | None, client_account_name: str | None, tenant_uid: str | None, client_uid: str | None, account_uid: str | None, client_role_uid: str | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None, client_account_uid_account_name: str | None, client_account_uid_tenant_uid: str | None, client_account_uid_account_type_uid: str | None, client_account_uid_account_title_uid: str | None, client_account_uid_account_division_uid: str | None, client_account_uid_account_group_uid: str | None, client_account_uid_auth_identity_uid: str | None, client_account_uid_account_email: str | None, client_account_uid_display_name: str | None, client_account_uid_is_system: int | None, tenant_uid_tenant_name: str | None, tenant_uid_country_uid: str | None, tenant_uid_tenant_type_uid: str | None, tenant_uid_tenant_category_uid: str | None, tenant_uid_tenant_code: str | None, tenant_uid_tenant_description: str | None, tenant_uid_start_date: datetime.datetime | None, tenant_uid_end_date: datetime.datetime | None, tenant_uid_is_internal: int | None, tenant_uid_is_system: int | None, tenant_uid_is_test: int | None, tenant_uid_account_uid: str | None, client_uid_client_name: str | None, client_uid_tenant_uid: str | None, client_uid_country_uid: str | None, client_uid_client_type_uid: str | None, client_uid_client_category_uid: str | None, client_uid_account_uid: str | None, client_uid_client_code: str | None, client_uid_client_description: str | None, client_uid_start_date: datetime.datetime | None, client_uid_end_date: datetime.datetime | None, client_uid_is_internal: int | None, client_uid_is_system: int | None, client_uid_is_test: int | None, account_uid_account_name: str | None, account_uid_tenant_uid: str | None, account_uid_account_type_uid: str | None, account_uid_account_title_uid: str | None, account_uid_account_division_uid: str | None, account_uid_account_group_uid: str | None, account_uid_auth_identity_uid: str | None, account_uid_account_email: str | None, account_uid_display_name: str | None, account_uid_is_system: int | None, client_role_uid_client_role_name: str | None, client_role_uid_role_description: str | None):
        self.client_account_uid = client_account_uid
        self.client_account_name = client_account_name
        self.tenant_uid = tenant_uid
        self.client_uid = client_uid
        self.account_uid = account_uid
        self.client_role_uid = client_role_uid
        self.row_instance = row_instance
        self.row_lock = row_lock
        self.row_owner = row_owner
        self.row_seq = row_seq
        self.row_guid = row_guid
        self.row_version = row_version
        self.is_active = is_active
        self.created_date = created_date
        self.created_by = created_by
        self.last_updated_date = last_updated_date
        self.last_updated_by = last_updated_by
        self.removed_date = removed_date
        self.removed_by = removed_by
        self.custom_attributes = custom_attributes
        self.client_account_uid_account_name = client_account_uid_account_name
        self.client_account_uid_tenant_uid = client_account_uid_tenant_uid
        self.client_account_uid_account_type_uid = client_account_uid_account_type_uid
        self.client_account_uid_account_title_uid = client_account_uid_account_title_uid
        self.client_account_uid_account_division_uid = client_account_uid_account_division_uid
        self.client_account_uid_account_group_uid = client_account_uid_account_group_uid
        self.client_account_uid_auth_identity_uid = client_account_uid_auth_identity_uid
        self.client_account_uid_account_email = client_account_uid_account_email
        self.client_account_uid_display_name = client_account_uid_display_name
        self.client_account_uid_is_system = client_account_uid_is_system
        self.tenant_uid_tenant_name = tenant_uid_tenant_name
        self.tenant_uid_country_uid = tenant_uid_country_uid
        self.tenant_uid_tenant_type_uid = tenant_uid_tenant_type_uid
        self.tenant_uid_tenant_category_uid = tenant_uid_tenant_category_uid
        self.tenant_uid_tenant_code = tenant_uid_tenant_code
        self.tenant_uid_tenant_description = tenant_uid_tenant_description
        self.tenant_uid_start_date = tenant_uid_start_date
        self.tenant_uid_end_date = tenant_uid_end_date
        self.tenant_uid_is_internal = tenant_uid_is_internal
        self.tenant_uid_is_system = tenant_uid_is_system
        self.tenant_uid_is_test = tenant_uid_is_test
        self.tenant_uid_account_uid = tenant_uid_account_uid
        self.client_uid_client_name = client_uid_client_name
        self.client_uid_tenant_uid = client_uid_tenant_uid
        self.client_uid_country_uid = client_uid_country_uid
        self.client_uid_client_type_uid = client_uid_client_type_uid
        self.client_uid_client_category_uid = client_uid_client_category_uid
        self.client_uid_account_uid = client_uid_account_uid
        self.client_uid_client_code = client_uid_client_code
        self.client_uid_client_description = client_uid_client_description
        self.client_uid_start_date = client_uid_start_date
        self.client_uid_end_date = client_uid_end_date
        self.client_uid_is_internal = client_uid_is_internal
        self.client_uid_is_system = client_uid_is_system
        self.client_uid_is_test = client_uid_is_test
        self.account_uid_account_name = account_uid_account_name
        self.account_uid_tenant_uid = account_uid_tenant_uid
        self.account_uid_account_type_uid = account_uid_account_type_uid
        self.account_uid_account_title_uid = account_uid_account_title_uid
        self.account_uid_account_division_uid = account_uid_account_division_uid
        self.account_uid_account_group_uid = account_uid_account_group_uid
        self.account_uid_auth_identity_uid = account_uid_auth_identity_uid
        self.account_uid_account_email = account_uid_account_email
        self.account_uid_display_name = account_uid_display_name
        self.account_uid_is_system = account_uid_is_system
        self.client_role_uid_client_role_name = client_role_uid_client_role_name
        self.client_role_uid_role_description = client_role_uid_role_description
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.client_account_uid, self.client_account_name, self.tenant_uid, self.client_uid, self.account_uid, self.client_role_uid, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes, self.client_account_uid_account_name, self.client_account_uid_tenant_uid, self.client_account_uid_account_type_uid, self.client_account_uid_account_title_uid, self.client_account_uid_account_division_uid, self.client_account_uid_account_group_uid, self.client_account_uid_auth_identity_uid, self.client_account_uid_account_email, self.client_account_uid_display_name, self.client_account_uid_is_system, self.tenant_uid_tenant_name, self.tenant_uid_country_uid, self.tenant_uid_tenant_type_uid, self.tenant_uid_tenant_category_uid, self.tenant_uid_tenant_code, self.tenant_uid_tenant_description, self.tenant_uid_start_date, self.tenant_uid_end_date, self.tenant_uid_is_internal, self.tenant_uid_is_system, self.tenant_uid_is_test, self.tenant_uid_account_uid, self.client_uid_client_name, self.client_uid_tenant_uid, self.client_uid_country_uid, self.client_uid_client_type_uid, self.client_uid_client_category_uid, self.client_uid_account_uid, self.client_uid_client_code, self.client_uid_client_description, self.client_uid_start_date, self.client_uid_end_date, self.client_uid_is_internal, self.client_uid_is_system, self.client_uid_is_test, self.account_uid_account_name, self.account_uid_tenant_uid, self.account_uid_account_type_uid, self.account_uid_account_title_uid, self.account_uid_account_division_uid, self.account_uid_account_group_uid, self.account_uid_auth_identity_uid, self.account_uid_account_email, self.account_uid_display_name, self.account_uid_is_system, self.client_role_uid_client_role_name, self.client_role_uid_role_description]


@dataclass(frozen=False)
class client_country_rich_dto(client_country_read_dto):
    client_country_uid: str | None
    client_country_name: str | None
    tenant_uid: str | None
    client_uid: str | None
    country_uid: str | None
    row_instance: str | None
    row_lock: str | None
    row_owner: str | None
    row_seq: int | None
    row_guid: str | None
    row_version: int | None
    is_active: int | None
    created_date: datetime.datetime | None
    created_by: str | None
    last_updated_date: datetime.datetime | None
    last_updated_by: str | None
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str | None
    client_country_uid_country_name: str | None
    client_country_uid_continent_name: str | None
    client_country_uid_continent_code: str | None
    client_country_uid_country_iso3: str | None
    client_country_uid_country_code: str | None
    client_country_uid_phone_code: str | None
    client_country_uid_currency_code: str | None
    client_country_uid_capital_name: str | None
    client_country_uid_region_name: str | None
    client_country_uid_subregion_name: str | None
    client_country_uid_region_code: str | None
    client_country_uid_latitude: str | None
    client_country_uid_longitude: str | None
    client_country_uid_currency_name: str | None
    client_country_uid_population: str | None
    client_country_uid_languages: str | None
    client_country_uid_area: str | None
    client_country_uid_bar_code: str | None
    client_country_uid_top_level_domain: str | None
    client_country_uid_is_focused: int | None
    tenant_uid_tenant_name: str | None
    tenant_uid_country_uid: str | None
    tenant_uid_tenant_type_uid: str | None
    tenant_uid_tenant_category_uid: str | None
    tenant_uid_tenant_code: str | None
    tenant_uid_tenant_description: str | None
    tenant_uid_start_date: datetime.datetime | None
    tenant_uid_end_date: datetime.datetime | None
    tenant_uid_is_internal: int | None
    tenant_uid_is_system: int | None
    tenant_uid_is_test: int | None
    tenant_uid_account_uid: str | None
    client_uid_client_name: str | None
    client_uid_tenant_uid: str | None
    client_uid_country_uid: str | None
    client_uid_client_type_uid: str | None
    client_uid_client_category_uid: str | None
    client_uid_account_uid: str | None
    client_uid_client_code: str | None
    client_uid_client_description: str | None
    client_uid_start_date: datetime.datetime | None
    client_uid_end_date: datetime.datetime | None
    client_uid_is_internal: int | None
    client_uid_is_system: int | None
    client_uid_is_test: int | None
    country_uid_country_name: str | None
    country_uid_continent_name: str | None
    country_uid_continent_code: str | None
    country_uid_country_iso3: str | None
    country_uid_country_code: str | None
    country_uid_phone_code: str | None
    country_uid_currency_code: str | None
    country_uid_capital_name: str | None
    country_uid_region_name: str | None
    country_uid_subregion_name: str | None
    country_uid_region_code: str | None
    country_uid_latitude: str | None
    country_uid_longitude: str | None
    country_uid_currency_name: str | None
    country_uid_population: str | None
    country_uid_languages: str | None
    country_uid_area: str | None
    country_uid_bar_code: str | None
    country_uid_top_level_domain: str | None
    country_uid_is_focused: int | None
    def __init__(self, client_country_uid: str | None, client_country_name: str | None, tenant_uid: str | None, client_uid: str | None, country_uid: str | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None, client_country_uid_country_name: str | None, client_country_uid_continent_name: str | None, client_country_uid_continent_code: str | None, client_country_uid_country_iso3: str | None, client_country_uid_country_code: str | None, client_country_uid_phone_code: str | None, client_country_uid_currency_code: str | None, client_country_uid_capital_name: str | None, client_country_uid_region_name: str | None, client_country_uid_subregion_name: str | None, client_country_uid_region_code: str | None, client_country_uid_latitude: str | None, client_country_uid_longitude: str | None, client_country_uid_currency_name: str | None, client_country_uid_population: str | None, client_country_uid_languages: str | None, client_country_uid_area: str | None, client_country_uid_bar_code: str | None, client_country_uid_top_level_domain: str | None, client_country_uid_is_focused: int | None, tenant_uid_tenant_name: str | None, tenant_uid_country_uid: str | None, tenant_uid_tenant_type_uid: str | None, tenant_uid_tenant_category_uid: str | None, tenant_uid_tenant_code: str | None, tenant_uid_tenant_description: str | None, tenant_uid_start_date: datetime.datetime | None, tenant_uid_end_date: datetime.datetime | None, tenant_uid_is_internal: int | None, tenant_uid_is_system: int | None, tenant_uid_is_test: int | None, tenant_uid_account_uid: str | None, client_uid_client_name: str | None, client_uid_tenant_uid: str | None, client_uid_country_uid: str | None, client_uid_client_type_uid: str | None, client_uid_client_category_uid: str | None, client_uid_account_uid: str | None, client_uid_client_code: str | None, client_uid_client_description: str | None, client_uid_start_date: datetime.datetime | None, client_uid_end_date: datetime.datetime | None, client_uid_is_internal: int | None, client_uid_is_system: int | None, client_uid_is_test: int | None, country_uid_country_name: str | None, country_uid_continent_name: str | None, country_uid_continent_code: str | None, country_uid_country_iso3: str | None, country_uid_country_code: str | None, country_uid_phone_code: str | None, country_uid_currency_code: str | None, country_uid_capital_name: str | None, country_uid_region_name: str | None, country_uid_subregion_name: str | None, country_uid_region_code: str | None, country_uid_latitude: str | None, country_uid_longitude: str | None, country_uid_currency_name: str | None, country_uid_population: str | None, country_uid_languages: str | None, country_uid_area: str | None, country_uid_bar_code: str | None, country_uid_top_level_domain: str | None, country_uid_is_focused: int | None):
        self.client_country_uid = client_country_uid
        self.client_country_name = client_country_name
        self.tenant_uid = tenant_uid
        self.client_uid = client_uid
        self.country_uid = country_uid
        self.row_instance = row_instance
        self.row_lock = row_lock
        self.row_owner = row_owner
        self.row_seq = row_seq
        self.row_guid = row_guid
        self.row_version = row_version
        self.is_active = is_active
        self.created_date = created_date
        self.created_by = created_by
        self.last_updated_date = last_updated_date
        self.last_updated_by = last_updated_by
        self.removed_date = removed_date
        self.removed_by = removed_by
        self.custom_attributes = custom_attributes
        self.client_country_uid_country_name = client_country_uid_country_name
        self.client_country_uid_continent_name = client_country_uid_continent_name
        self.client_country_uid_continent_code = client_country_uid_continent_code
        self.client_country_uid_country_iso3 = client_country_uid_country_iso3
        self.client_country_uid_country_code = client_country_uid_country_code
        self.client_country_uid_phone_code = client_country_uid_phone_code
        self.client_country_uid_currency_code = client_country_uid_currency_code
        self.client_country_uid_capital_name = client_country_uid_capital_name
        self.client_country_uid_region_name = client_country_uid_region_name
        self.client_country_uid_subregion_name = client_country_uid_subregion_name
        self.client_country_uid_region_code = client_country_uid_region_code
        self.client_country_uid_latitude = client_country_uid_latitude
        self.client_country_uid_longitude = client_country_uid_longitude
        self.client_country_uid_currency_name = client_country_uid_currency_name
        self.client_country_uid_population = client_country_uid_population
        self.client_country_uid_languages = client_country_uid_languages
        self.client_country_uid_area = client_country_uid_area
        self.client_country_uid_bar_code = client_country_uid_bar_code
        self.client_country_uid_top_level_domain = client_country_uid_top_level_domain
        self.client_country_uid_is_focused = client_country_uid_is_focused
        self.tenant_uid_tenant_name = tenant_uid_tenant_name
        self.tenant_uid_country_uid = tenant_uid_country_uid
        self.tenant_uid_tenant_type_uid = tenant_uid_tenant_type_uid
        self.tenant_uid_tenant_category_uid = tenant_uid_tenant_category_uid
        self.tenant_uid_tenant_code = tenant_uid_tenant_code
        self.tenant_uid_tenant_description = tenant_uid_tenant_description
        self.tenant_uid_start_date = tenant_uid_start_date
        self.tenant_uid_end_date = tenant_uid_end_date
        self.tenant_uid_is_internal = tenant_uid_is_internal
        self.tenant_uid_is_system = tenant_uid_is_system
        self.tenant_uid_is_test = tenant_uid_is_test
        self.tenant_uid_account_uid = tenant_uid_account_uid
        self.client_uid_client_name = client_uid_client_name
        self.client_uid_tenant_uid = client_uid_tenant_uid
        self.client_uid_country_uid = client_uid_country_uid
        self.client_uid_client_type_uid = client_uid_client_type_uid
        self.client_uid_client_category_uid = client_uid_client_category_uid
        self.client_uid_account_uid = client_uid_account_uid
        self.client_uid_client_code = client_uid_client_code
        self.client_uid_client_description = client_uid_client_description
        self.client_uid_start_date = client_uid_start_date
        self.client_uid_end_date = client_uid_end_date
        self.client_uid_is_internal = client_uid_is_internal
        self.client_uid_is_system = client_uid_is_system
        self.client_uid_is_test = client_uid_is_test
        self.country_uid_country_name = country_uid_country_name
        self.country_uid_continent_name = country_uid_continent_name
        self.country_uid_continent_code = country_uid_continent_code
        self.country_uid_country_iso3 = country_uid_country_iso3
        self.country_uid_country_code = country_uid_country_code
        self.country_uid_phone_code = country_uid_phone_code
        self.country_uid_currency_code = country_uid_currency_code
        self.country_uid_capital_name = country_uid_capital_name
        self.country_uid_region_name = country_uid_region_name
        self.country_uid_subregion_name = country_uid_subregion_name
        self.country_uid_region_code = country_uid_region_code
        self.country_uid_latitude = country_uid_latitude
        self.country_uid_longitude = country_uid_longitude
        self.country_uid_currency_name = country_uid_currency_name
        self.country_uid_population = country_uid_population
        self.country_uid_languages = country_uid_languages
        self.country_uid_area = country_uid_area
        self.country_uid_bar_code = country_uid_bar_code
        self.country_uid_top_level_domain = country_uid_top_level_domain
        self.country_uid_is_focused = country_uid_is_focused
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.client_country_uid, self.client_country_name, self.tenant_uid, self.client_uid, self.country_uid, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes, self.client_country_uid_country_name, self.client_country_uid_continent_name, self.client_country_uid_continent_code, self.client_country_uid_country_iso3, self.client_country_uid_country_code, self.client_country_uid_phone_code, self.client_country_uid_currency_code, self.client_country_uid_capital_name, self.client_country_uid_region_name, self.client_country_uid_subregion_name, self.client_country_uid_region_code, self.client_country_uid_latitude, self.client_country_uid_longitude, self.client_country_uid_currency_name, self.client_country_uid_population, self.client_country_uid_languages, self.client_country_uid_area, self.client_country_uid_bar_code, self.client_country_uid_top_level_domain, self.client_country_uid_is_focused, self.tenant_uid_tenant_name, self.tenant_uid_country_uid, self.tenant_uid_tenant_type_uid, self.tenant_uid_tenant_category_uid, self.tenant_uid_tenant_code, self.tenant_uid_tenant_description, self.tenant_uid_start_date, self.tenant_uid_end_date, self.tenant_uid_is_internal, self.tenant_uid_is_system, self.tenant_uid_is_test, self.tenant_uid_account_uid, self.client_uid_client_name, self.client_uid_tenant_uid, self.client_uid_country_uid, self.client_uid_client_type_uid, self.client_uid_client_category_uid, self.client_uid_account_uid, self.client_uid_client_code, self.client_uid_client_description, self.client_uid_start_date, self.client_uid_end_date, self.client_uid_is_internal, self.client_uid_is_system, self.client_uid_is_test, self.country_uid_country_name, self.country_uid_continent_name, self.country_uid_continent_code, self.country_uid_country_iso3, self.country_uid_country_code, self.country_uid_phone_code, self.country_uid_currency_code, self.country_uid_capital_name, self.country_uid_region_name, self.country_uid_subregion_name, self.country_uid_region_code, self.country_uid_latitude, self.country_uid_longitude, self.country_uid_currency_name, self.country_uid_population, self.country_uid_languages, self.country_uid_area, self.country_uid_bar_code, self.country_uid_top_level_domain, self.country_uid_is_focused]


@dataclass(frozen=False)
class client_payment_rich_dto(client_payment_read_dto):
    client_payment_uid: str | None
    client_payment_name: str | None
    tenant_uid: str | None
    client_uid: str | None
    account_uid: str | None
    currency_uid: str | None
    start_date: datetime.datetime | None
    end_date: datetime.datetime | None
    payment_value: str | None
    payment_type: str | None
    source_number: str | None
    source_reference: str | None
    is_approved: int | None
    row_instance: str | None
    row_lock: str | None
    row_owner: str | None
    row_seq: int | None
    row_guid: str | None
    row_version: int | None
    is_active: int | None
    created_date: datetime.datetime | None
    created_by: str | None
    last_updated_date: datetime.datetime | None
    last_updated_by: str | None
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str | None
    tenant_uid_tenant_name: str | None
    tenant_uid_country_uid: str | None
    tenant_uid_tenant_type_uid: str | None
    tenant_uid_tenant_category_uid: str | None
    tenant_uid_tenant_code: str | None
    tenant_uid_tenant_description: str | None
    tenant_uid_start_date: datetime.datetime | None
    tenant_uid_end_date: datetime.datetime | None
    tenant_uid_is_internal: int | None
    tenant_uid_is_system: int | None
    tenant_uid_is_test: int | None
    tenant_uid_account_uid: str | None
    client_uid_client_name: str | None
    client_uid_tenant_uid: str | None
    client_uid_country_uid: str | None
    client_uid_client_type_uid: str | None
    client_uid_client_category_uid: str | None
    client_uid_account_uid: str | None
    client_uid_client_code: str | None
    client_uid_client_description: str | None
    client_uid_start_date: datetime.datetime | None
    client_uid_end_date: datetime.datetime | None
    client_uid_is_internal: int | None
    client_uid_is_system: int | None
    client_uid_is_test: int | None
    account_uid_account_name: str | None
    account_uid_tenant_uid: str | None
    account_uid_account_type_uid: str | None
    account_uid_account_title_uid: str | None
    account_uid_account_division_uid: str | None
    account_uid_account_group_uid: str | None
    account_uid_auth_identity_uid: str | None
    account_uid_account_email: str | None
    account_uid_display_name: str | None
    account_uid_is_system: int | None
    currency_uid_currency_name: str | None
    currency_uid_is_focused: int | None
    def __init__(self, client_payment_uid: str | None, client_payment_name: str | None, tenant_uid: str | None, client_uid: str | None, account_uid: str | None, currency_uid: str | None, start_date: datetime.datetime | None, end_date: datetime.datetime | None, payment_value: str | None, payment_type: str | None, source_number: str | None, source_reference: str | None, is_approved: int | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None, tenant_uid_tenant_name: str | None, tenant_uid_country_uid: str | None, tenant_uid_tenant_type_uid: str | None, tenant_uid_tenant_category_uid: str | None, tenant_uid_tenant_code: str | None, tenant_uid_tenant_description: str | None, tenant_uid_start_date: datetime.datetime | None, tenant_uid_end_date: datetime.datetime | None, tenant_uid_is_internal: int | None, tenant_uid_is_system: int | None, tenant_uid_is_test: int | None, tenant_uid_account_uid: str | None, client_uid_client_name: str | None, client_uid_tenant_uid: str | None, client_uid_country_uid: str | None, client_uid_client_type_uid: str | None, client_uid_client_category_uid: str | None, client_uid_account_uid: str | None, client_uid_client_code: str | None, client_uid_client_description: str | None, client_uid_start_date: datetime.datetime | None, client_uid_end_date: datetime.datetime | None, client_uid_is_internal: int | None, client_uid_is_system: int | None, client_uid_is_test: int | None, account_uid_account_name: str | None, account_uid_tenant_uid: str | None, account_uid_account_type_uid: str | None, account_uid_account_title_uid: str | None, account_uid_account_division_uid: str | None, account_uid_account_group_uid: str | None, account_uid_auth_identity_uid: str | None, account_uid_account_email: str | None, account_uid_display_name: str | None, account_uid_is_system: int | None, currency_uid_currency_name: str | None, currency_uid_is_focused: int | None):
        self.client_payment_uid = client_payment_uid
        self.client_payment_name = client_payment_name
        self.tenant_uid = tenant_uid
        self.client_uid = client_uid
        self.account_uid = account_uid
        self.currency_uid = currency_uid
        self.start_date = start_date
        self.end_date = end_date
        self.payment_value = payment_value
        self.payment_type = payment_type
        self.source_number = source_number
        self.source_reference = source_reference
        self.is_approved = is_approved
        self.row_instance = row_instance
        self.row_lock = row_lock
        self.row_owner = row_owner
        self.row_seq = row_seq
        self.row_guid = row_guid
        self.row_version = row_version
        self.is_active = is_active
        self.created_date = created_date
        self.created_by = created_by
        self.last_updated_date = last_updated_date
        self.last_updated_by = last_updated_by
        self.removed_date = removed_date
        self.removed_by = removed_by
        self.custom_attributes = custom_attributes
        self.tenant_uid_tenant_name = tenant_uid_tenant_name
        self.tenant_uid_country_uid = tenant_uid_country_uid
        self.tenant_uid_tenant_type_uid = tenant_uid_tenant_type_uid
        self.tenant_uid_tenant_category_uid = tenant_uid_tenant_category_uid
        self.tenant_uid_tenant_code = tenant_uid_tenant_code
        self.tenant_uid_tenant_description = tenant_uid_tenant_description
        self.tenant_uid_start_date = tenant_uid_start_date
        self.tenant_uid_end_date = tenant_uid_end_date
        self.tenant_uid_is_internal = tenant_uid_is_internal
        self.tenant_uid_is_system = tenant_uid_is_system
        self.tenant_uid_is_test = tenant_uid_is_test
        self.tenant_uid_account_uid = tenant_uid_account_uid
        self.client_uid_client_name = client_uid_client_name
        self.client_uid_tenant_uid = client_uid_tenant_uid
        self.client_uid_country_uid = client_uid_country_uid
        self.client_uid_client_type_uid = client_uid_client_type_uid
        self.client_uid_client_category_uid = client_uid_client_category_uid
        self.client_uid_account_uid = client_uid_account_uid
        self.client_uid_client_code = client_uid_client_code
        self.client_uid_client_description = client_uid_client_description
        self.client_uid_start_date = client_uid_start_date
        self.client_uid_end_date = client_uid_end_date
        self.client_uid_is_internal = client_uid_is_internal
        self.client_uid_is_system = client_uid_is_system
        self.client_uid_is_test = client_uid_is_test
        self.account_uid_account_name = account_uid_account_name
        self.account_uid_tenant_uid = account_uid_tenant_uid
        self.account_uid_account_type_uid = account_uid_account_type_uid
        self.account_uid_account_title_uid = account_uid_account_title_uid
        self.account_uid_account_division_uid = account_uid_account_division_uid
        self.account_uid_account_group_uid = account_uid_account_group_uid
        self.account_uid_auth_identity_uid = account_uid_auth_identity_uid
        self.account_uid_account_email = account_uid_account_email
        self.account_uid_display_name = account_uid_display_name
        self.account_uid_is_system = account_uid_is_system
        self.currency_uid_currency_name = currency_uid_currency_name
        self.currency_uid_is_focused = currency_uid_is_focused
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.client_payment_uid, self.client_payment_name, self.tenant_uid, self.client_uid, self.account_uid, self.currency_uid, self.start_date, self.end_date, self.payment_value, self.payment_type, self.source_number, self.source_reference, self.is_approved, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes, self.tenant_uid_tenant_name, self.tenant_uid_country_uid, self.tenant_uid_tenant_type_uid, self.tenant_uid_tenant_category_uid, self.tenant_uid_tenant_code, self.tenant_uid_tenant_description, self.tenant_uid_start_date, self.tenant_uid_end_date, self.tenant_uid_is_internal, self.tenant_uid_is_system, self.tenant_uid_is_test, self.tenant_uid_account_uid, self.client_uid_client_name, self.client_uid_tenant_uid, self.client_uid_country_uid, self.client_uid_client_type_uid, self.client_uid_client_category_uid, self.client_uid_account_uid, self.client_uid_client_code, self.client_uid_client_description, self.client_uid_start_date, self.client_uid_end_date, self.client_uid_is_internal, self.client_uid_is_system, self.client_uid_is_test, self.account_uid_account_name, self.account_uid_tenant_uid, self.account_uid_account_type_uid, self.account_uid_account_title_uid, self.account_uid_account_division_uid, self.account_uid_account_group_uid, self.account_uid_auth_identity_uid, self.account_uid_account_email, self.account_uid_display_name, self.account_uid_is_system, self.currency_uid_currency_name, self.currency_uid_is_focused]


@dataclass(frozen=False)
class client_role_rich_dto(client_role_read_dto):
    client_role_uid: str | None
    client_role_name: str | None
    role_description: str | None
    row_instance: str | None
    row_lock: str | None
    row_owner: str | None
    row_seq: int | None
    row_guid: str | None
    row_version: int | None
    is_active: int | None
    created_date: datetime.datetime | None
    created_by: str | None
    last_updated_date: datetime.datetime | None
    last_updated_by: str | None
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str | None
    def __init__(self, client_role_uid: str | None, client_role_name: str | None, role_description: str | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None):
        self.client_role_uid = client_role_uid
        self.client_role_name = client_role_name
        self.role_description = role_description
        self.row_instance = row_instance
        self.row_lock = row_lock
        self.row_owner = row_owner
        self.row_seq = row_seq
        self.row_guid = row_guid
        self.row_version = row_version
        self.is_active = is_active
        self.created_date = created_date
        self.created_by = created_by
        self.last_updated_date = last_updated_date
        self.last_updated_by = last_updated_by
        self.removed_date = removed_date
        self.removed_by = removed_by
        self.custom_attributes = custom_attributes
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.client_role_uid, self.client_role_name, self.role_description, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]


@dataclass(frozen=False)
class client_status_rich_dto(client_status_read_dto):
    client_status_uid: str | None
    client_status_name: str | None
    client_status_description: str | None
    row_instance: str | None
    row_lock: str | None
    row_owner: str | None
    row_seq: int | None
    row_guid: str | None
    row_version: int | None
    is_active: int | None
    created_date: datetime.datetime | None
    created_by: str | None
    last_updated_date: datetime.datetime | None
    last_updated_by: str | None
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str | None
    def __init__(self, client_status_uid: str | None, client_status_name: str | None, client_status_description: str | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None):
        self.client_status_uid = client_status_uid
        self.client_status_name = client_status_name
        self.client_status_description = client_status_description
        self.row_instance = row_instance
        self.row_lock = row_lock
        self.row_owner = row_owner
        self.row_seq = row_seq
        self.row_guid = row_guid
        self.row_version = row_version
        self.is_active = is_active
        self.created_date = created_date
        self.created_by = created_by
        self.last_updated_date = last_updated_date
        self.last_updated_by = last_updated_by
        self.removed_date = removed_date
        self.removed_by = removed_by
        self.custom_attributes = custom_attributes
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.client_status_uid, self.client_status_name, self.client_status_description, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]


@dataclass(frozen=False)
class client_type_rich_dto(client_type_read_dto):
    client_type_uid: str | None
    client_type_name: str | None
    client_type_description: str | None
    row_instance: str | None
    row_lock: str | None
    row_owner: str | None
    row_seq: int | None
    row_guid: str | None
    row_version: int | None
    is_active: int | None
    created_date: datetime.datetime | None
    created_by: str | None
    last_updated_date: datetime.datetime | None
    last_updated_by: str | None
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str | None
    def __init__(self, client_type_uid: str | None, client_type_name: str | None, client_type_description: str | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None):
        self.client_type_uid = client_type_uid
        self.client_type_name = client_type_name
        self.client_type_description = client_type_description
        self.row_instance = row_instance
        self.row_lock = row_lock
        self.row_owner = row_owner
        self.row_seq = row_seq
        self.row_guid = row_guid
        self.row_version = row_version
        self.is_active = is_active
        self.created_date = created_date
        self.created_by = created_by
        self.last_updated_date = last_updated_date
        self.last_updated_by = last_updated_by
        self.removed_date = removed_date
        self.removed_by = removed_by
        self.custom_attributes = custom_attributes
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.client_type_uid, self.client_type_name, self.client_type_description, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]


@dataclass(frozen=False)
class connection_engine_rich_dto(connection_engine_read_dto):
    connection_engine_uid: str | None
    connection_engine_name: str | None
    start_date: datetime.datetime | None
    calls_count: int | None
    last_time: int | None
    host_count: int | None
    user_count: int | None
    token_count: int | None
    row_instance: str | None
    row_lock: str | None
    row_owner: str | None
    row_seq: int | None
    row_guid: str | None
    row_version: int | None
    is_active: int | None
    created_date: datetime.datetime | None
    created_by: str | None
    last_updated_date: datetime.datetime | None
    last_updated_by: str | None
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str | None
    def __init__(self, connection_engine_uid: str | None, connection_engine_name: str | None, start_date: datetime.datetime | None, calls_count: int | None, last_time: int | None, host_count: int | None, user_count: int | None, token_count: int | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None):
        self.connection_engine_uid = connection_engine_uid
        self.connection_engine_name = connection_engine_name
        self.start_date = start_date
        self.calls_count = calls_count
        self.last_time = last_time
        self.host_count = host_count
        self.user_count = user_count
        self.token_count = token_count
        self.row_instance = row_instance
        self.row_lock = row_lock
        self.row_owner = row_owner
        self.row_seq = row_seq
        self.row_guid = row_guid
        self.row_version = row_version
        self.is_active = is_active
        self.created_date = created_date
        self.created_by = created_by
        self.last_updated_date = last_updated_date
        self.last_updated_by = last_updated_by
        self.removed_date = removed_date
        self.removed_by = removed_by
        self.custom_attributes = custom_attributes
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.connection_engine_uid, self.connection_engine_name, self.start_date, self.calls_count, self.last_time, self.host_count, self.user_count, self.token_count, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]


@dataclass(frozen=False)
class connection_host_rich_dto(connection_host_read_dto):
    connection_host_uid: str | None
    connection_host_name: str | None
    connection_engine_uid: str | None
    host_ip: str | None
    calls_count: int | None
    start_time: int | None
    last_call_time: int | None
    user_count: int | None
    token_count: int | None
    row_instance: str | None
    row_lock: str | None
    row_owner: str | None
    row_seq: int | None
    row_guid: str | None
    row_version: int | None
    is_active: int | None
    created_date: datetime.datetime | None
    created_by: str | None
    last_updated_date: datetime.datetime | None
    last_updated_by: str | None
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str | None
    connection_engine_uid_connection_engine_name: str | None
    connection_engine_uid_start_date: datetime.datetime | None
    connection_engine_uid_calls_count: int | None
    connection_engine_uid_last_time: int | None
    connection_engine_uid_host_count: int | None
    connection_engine_uid_user_count: int | None
    connection_engine_uid_token_count: int | None
    def __init__(self, connection_host_uid: str | None, connection_host_name: str | None, connection_engine_uid: str | None, host_ip: str | None, calls_count: int | None, start_time: int | None, last_call_time: int | None, user_count: int | None, token_count: int | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None, connection_engine_uid_connection_engine_name: str | None, connection_engine_uid_start_date: datetime.datetime | None, connection_engine_uid_calls_count: int | None, connection_engine_uid_last_time: int | None, connection_engine_uid_host_count: int | None, connection_engine_uid_user_count: int | None, connection_engine_uid_token_count: int | None):
        self.connection_host_uid = connection_host_uid
        self.connection_host_name = connection_host_name
        self.connection_engine_uid = connection_engine_uid
        self.host_ip = host_ip
        self.calls_count = calls_count
        self.start_time = start_time
        self.last_call_time = last_call_time
        self.user_count = user_count
        self.token_count = token_count
        self.row_instance = row_instance
        self.row_lock = row_lock
        self.row_owner = row_owner
        self.row_seq = row_seq
        self.row_guid = row_guid
        self.row_version = row_version
        self.is_active = is_active
        self.created_date = created_date
        self.created_by = created_by
        self.last_updated_date = last_updated_date
        self.last_updated_by = last_updated_by
        self.removed_date = removed_date
        self.removed_by = removed_by
        self.custom_attributes = custom_attributes
        self.connection_engine_uid_connection_engine_name = connection_engine_uid_connection_engine_name
        self.connection_engine_uid_start_date = connection_engine_uid_start_date
        self.connection_engine_uid_calls_count = connection_engine_uid_calls_count
        self.connection_engine_uid_last_time = connection_engine_uid_last_time
        self.connection_engine_uid_host_count = connection_engine_uid_host_count
        self.connection_engine_uid_user_count = connection_engine_uid_user_count
        self.connection_engine_uid_token_count = connection_engine_uid_token_count
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.connection_host_uid, self.connection_host_name, self.connection_engine_uid, self.host_ip, self.calls_count, self.start_time, self.last_call_time, self.user_count, self.token_count, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes, self.connection_engine_uid_connection_engine_name, self.connection_engine_uid_start_date, self.connection_engine_uid_calls_count, self.connection_engine_uid_last_time, self.connection_engine_uid_host_count, self.connection_engine_uid_user_count, self.connection_engine_uid_token_count]


@dataclass(frozen=False)
class connection_user_rich_dto(connection_user_read_dto):
    connection_user_uid: str | None
    connection_user_name: str | None
    connection_engine_uid: str | None
    account_uid: str | None
    call_count: int | None
    host_count: int | None
    token_count: int | None
    row_instance: str | None
    row_lock: str | None
    row_owner: str | None
    row_seq: int | None
    row_guid: str | None
    row_version: int | None
    is_active: int | None
    created_date: datetime.datetime | None
    created_by: str | None
    last_updated_date: datetime.datetime | None
    last_updated_by: str | None
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str | None
    connection_engine_uid_connection_engine_name: str | None
    connection_engine_uid_start_date: datetime.datetime | None
    connection_engine_uid_calls_count: int | None
    connection_engine_uid_last_time: int | None
    connection_engine_uid_host_count: int | None
    connection_engine_uid_user_count: int | None
    connection_engine_uid_token_count: int | None
    account_uid_account_name: str | None
    account_uid_tenant_uid: str | None
    account_uid_account_type_uid: str | None
    account_uid_account_title_uid: str | None
    account_uid_account_division_uid: str | None
    account_uid_account_group_uid: str | None
    account_uid_auth_identity_uid: str | None
    account_uid_account_email: str | None
    account_uid_display_name: str | None
    account_uid_is_system: int | None
    def __init__(self, connection_user_uid: str | None, connection_user_name: str | None, connection_engine_uid: str | None, account_uid: str | None, call_count: int | None, host_count: int | None, token_count: int | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None, connection_engine_uid_connection_engine_name: str | None, connection_engine_uid_start_date: datetime.datetime | None, connection_engine_uid_calls_count: int | None, connection_engine_uid_last_time: int | None, connection_engine_uid_host_count: int | None, connection_engine_uid_user_count: int | None, connection_engine_uid_token_count: int | None, account_uid_account_name: str | None, account_uid_tenant_uid: str | None, account_uid_account_type_uid: str | None, account_uid_account_title_uid: str | None, account_uid_account_division_uid: str | None, account_uid_account_group_uid: str | None, account_uid_auth_identity_uid: str | None, account_uid_account_email: str | None, account_uid_display_name: str | None, account_uid_is_system: int | None):
        self.connection_user_uid = connection_user_uid
        self.connection_user_name = connection_user_name
        self.connection_engine_uid = connection_engine_uid
        self.account_uid = account_uid
        self.call_count = call_count
        self.host_count = host_count
        self.token_count = token_count
        self.row_instance = row_instance
        self.row_lock = row_lock
        self.row_owner = row_owner
        self.row_seq = row_seq
        self.row_guid = row_guid
        self.row_version = row_version
        self.is_active = is_active
        self.created_date = created_date
        self.created_by = created_by
        self.last_updated_date = last_updated_date
        self.last_updated_by = last_updated_by
        self.removed_date = removed_date
        self.removed_by = removed_by
        self.custom_attributes = custom_attributes
        self.connection_engine_uid_connection_engine_name = connection_engine_uid_connection_engine_name
        self.connection_engine_uid_start_date = connection_engine_uid_start_date
        self.connection_engine_uid_calls_count = connection_engine_uid_calls_count
        self.connection_engine_uid_last_time = connection_engine_uid_last_time
        self.connection_engine_uid_host_count = connection_engine_uid_host_count
        self.connection_engine_uid_user_count = connection_engine_uid_user_count
        self.connection_engine_uid_token_count = connection_engine_uid_token_count
        self.account_uid_account_name = account_uid_account_name
        self.account_uid_tenant_uid = account_uid_tenant_uid
        self.account_uid_account_type_uid = account_uid_account_type_uid
        self.account_uid_account_title_uid = account_uid_account_title_uid
        self.account_uid_account_division_uid = account_uid_account_division_uid
        self.account_uid_account_group_uid = account_uid_account_group_uid
        self.account_uid_auth_identity_uid = account_uid_auth_identity_uid
        self.account_uid_account_email = account_uid_account_email
        self.account_uid_display_name = account_uid_display_name
        self.account_uid_is_system = account_uid_is_system
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.connection_user_uid, self.connection_user_name, self.connection_engine_uid, self.account_uid, self.call_count, self.host_count, self.token_count, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes, self.connection_engine_uid_connection_engine_name, self.connection_engine_uid_start_date, self.connection_engine_uid_calls_count, self.connection_engine_uid_last_time, self.connection_engine_uid_host_count, self.connection_engine_uid_user_count, self.connection_engine_uid_token_count, self.account_uid_account_name, self.account_uid_tenant_uid, self.account_uid_account_type_uid, self.account_uid_account_title_uid, self.account_uid_account_division_uid, self.account_uid_account_group_uid, self.account_uid_auth_identity_uid, self.account_uid_account_email, self.account_uid_display_name, self.account_uid_is_system]


@dataclass(frozen=False)
class country_rich_dto(country_read_dto):
    country_uid: str | None
    country_name: str | None
    continent_name: str | None
    continent_code: str | None
    country_iso3: str | None
    country_code: str | None
    phone_code: str | None
    currency_code: str | None
    capital_name: str | None
    region_name: str | None
    subregion_name: str | None
    region_code: str | None
    latitude: str | None
    longitude: str | None
    currency_name: str | None
    population: str | None
    languages: str | None
    area: str | None
    bar_code: str | None
    top_level_domain: str | None
    is_focused: int | None
    row_instance: str | None
    row_lock: str | None
    row_owner: str | None
    row_seq: int | None
    row_guid: str | None
    row_version: int | None
    is_active: int | None
    created_date: datetime.datetime | None
    created_by: str | None
    last_updated_date: datetime.datetime | None
    last_updated_by: str | None
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str | None
    def __init__(self, country_uid: str | None, country_name: str | None, continent_name: str | None, continent_code: str | None, country_iso3: str | None, country_code: str | None, phone_code: str | None, currency_code: str | None, capital_name: str | None, region_name: str | None, subregion_name: str | None, region_code: str | None, latitude: str | None, longitude: str | None, currency_name: str | None, population: str | None, languages: str | None, area: str | None, bar_code: str | None, top_level_domain: str | None, is_focused: int | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None):
        self.country_uid = country_uid
        self.country_name = country_name
        self.continent_name = continent_name
        self.continent_code = continent_code
        self.country_iso3 = country_iso3
        self.country_code = country_code
        self.phone_code = phone_code
        self.currency_code = currency_code
        self.capital_name = capital_name
        self.region_name = region_name
        self.subregion_name = subregion_name
        self.region_code = region_code
        self.latitude = latitude
        self.longitude = longitude
        self.currency_name = currency_name
        self.population = population
        self.languages = languages
        self.area = area
        self.bar_code = bar_code
        self.top_level_domain = top_level_domain
        self.is_focused = is_focused
        self.row_instance = row_instance
        self.row_lock = row_lock
        self.row_owner = row_owner
        self.row_seq = row_seq
        self.row_guid = row_guid
        self.row_version = row_version
        self.is_active = is_active
        self.created_date = created_date
        self.created_by = created_by
        self.last_updated_date = last_updated_date
        self.last_updated_by = last_updated_by
        self.removed_date = removed_date
        self.removed_by = removed_by
        self.custom_attributes = custom_attributes
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.country_uid, self.country_name, self.continent_name, self.continent_code, self.country_iso3, self.country_code, self.phone_code, self.currency_code, self.capital_name, self.region_name, self.subregion_name, self.region_code, self.latitude, self.longitude, self.currency_name, self.population, self.languages, self.area, self.bar_code, self.top_level_domain, self.is_focused, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]


@dataclass(frozen=False)
class currency_rich_dto(currency_read_dto):
    currency_uid: str | None
    currency_name: str | None
    is_focused: int | None
    row_instance: str | None
    row_lock: str | None
    row_owner: str | None
    row_seq: int | None
    row_guid: str | None
    row_version: int | None
    is_active: int | None
    created_date: datetime.datetime | None
    created_by: str | None
    last_updated_date: datetime.datetime | None
    last_updated_by: str | None
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str | None
    def __init__(self, currency_uid: str | None, currency_name: str | None, is_focused: int | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None):
        self.currency_uid = currency_uid
        self.currency_name = currency_name
        self.is_focused = is_focused
        self.row_instance = row_instance
        self.row_lock = row_lock
        self.row_owner = row_owner
        self.row_seq = row_seq
        self.row_guid = row_guid
        self.row_version = row_version
        self.is_active = is_active
        self.created_date = created_date
        self.created_by = created_by
        self.last_updated_date = last_updated_date
        self.last_updated_by = last_updated_by
        self.removed_date = removed_date
        self.removed_by = removed_by
        self.custom_attributes = custom_attributes
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.currency_uid, self.currency_name, self.is_focused, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]


@dataclass(frozen=False)
class event_acknowledge_rich_dto(event_acknowledge_read_dto):
    event_acknowledge_uid: str | None
    event_acknowledge_name: str | None
    event_notification_uid: str | None
    tenant_uid: str | None
    account_uid: str | None
    row_instance: str | None
    row_lock: str | None
    row_owner: str | None
    row_seq: int | None
    row_guid: str | None
    row_version: int | None
    is_active: int | None
    created_date: datetime.datetime | None
    created_by: str | None
    last_updated_date: datetime.datetime | None
    last_updated_by: str | None
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str | None
    event_notification_uid_event_notification_name: str | None
    event_notification_uid_tenant_uid: str | None
    event_notification_uid_account_uid: str | None
    event_notification_uid_notification_type: str | None
    event_notification_uid_notification_topic: str | None
    event_notification_uid_notification_format: str | None
    event_notification_uid_notification_content: str | None
    event_notification_uid_sending_status: str | None
    tenant_uid_tenant_name: str | None
    tenant_uid_country_uid: str | None
    tenant_uid_tenant_type_uid: str | None
    tenant_uid_tenant_category_uid: str | None
    tenant_uid_tenant_code: str | None
    tenant_uid_tenant_description: str | None
    tenant_uid_start_date: datetime.datetime | None
    tenant_uid_end_date: datetime.datetime | None
    tenant_uid_is_internal: int | None
    tenant_uid_is_system: int | None
    tenant_uid_is_test: int | None
    tenant_uid_account_uid: str | None
    account_uid_account_name: str | None
    account_uid_tenant_uid: str | None
    account_uid_account_type_uid: str | None
    account_uid_account_title_uid: str | None
    account_uid_account_division_uid: str | None
    account_uid_account_group_uid: str | None
    account_uid_auth_identity_uid: str | None
    account_uid_account_email: str | None
    account_uid_display_name: str | None
    account_uid_is_system: int | None
    def __init__(self, event_acknowledge_uid: str | None, event_acknowledge_name: str | None, event_notification_uid: str | None, tenant_uid: str | None, account_uid: str | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None, event_notification_uid_event_notification_name: str | None, event_notification_uid_tenant_uid: str | None, event_notification_uid_account_uid: str | None, event_notification_uid_notification_type: str | None, event_notification_uid_notification_topic: str | None, event_notification_uid_notification_format: str | None, event_notification_uid_notification_content: str | None, event_notification_uid_sending_status: str | None, tenant_uid_tenant_name: str | None, tenant_uid_country_uid: str | None, tenant_uid_tenant_type_uid: str | None, tenant_uid_tenant_category_uid: str | None, tenant_uid_tenant_code: str | None, tenant_uid_tenant_description: str | None, tenant_uid_start_date: datetime.datetime | None, tenant_uid_end_date: datetime.datetime | None, tenant_uid_is_internal: int | None, tenant_uid_is_system: int | None, tenant_uid_is_test: int | None, tenant_uid_account_uid: str | None, account_uid_account_name: str | None, account_uid_tenant_uid: str | None, account_uid_account_type_uid: str | None, account_uid_account_title_uid: str | None, account_uid_account_division_uid: str | None, account_uid_account_group_uid: str | None, account_uid_auth_identity_uid: str | None, account_uid_account_email: str | None, account_uid_display_name: str | None, account_uid_is_system: int | None):
        self.event_acknowledge_uid = event_acknowledge_uid
        self.event_acknowledge_name = event_acknowledge_name
        self.event_notification_uid = event_notification_uid
        self.tenant_uid = tenant_uid
        self.account_uid = account_uid
        self.row_instance = row_instance
        self.row_lock = row_lock
        self.row_owner = row_owner
        self.row_seq = row_seq
        self.row_guid = row_guid
        self.row_version = row_version
        self.is_active = is_active
        self.created_date = created_date
        self.created_by = created_by
        self.last_updated_date = last_updated_date
        self.last_updated_by = last_updated_by
        self.removed_date = removed_date
        self.removed_by = removed_by
        self.custom_attributes = custom_attributes
        self.event_notification_uid_event_notification_name = event_notification_uid_event_notification_name
        self.event_notification_uid_tenant_uid = event_notification_uid_tenant_uid
        self.event_notification_uid_account_uid = event_notification_uid_account_uid
        self.event_notification_uid_notification_type = event_notification_uid_notification_type
        self.event_notification_uid_notification_topic = event_notification_uid_notification_topic
        self.event_notification_uid_notification_format = event_notification_uid_notification_format
        self.event_notification_uid_notification_content = event_notification_uid_notification_content
        self.event_notification_uid_sending_status = event_notification_uid_sending_status
        self.tenant_uid_tenant_name = tenant_uid_tenant_name
        self.tenant_uid_country_uid = tenant_uid_country_uid
        self.tenant_uid_tenant_type_uid = tenant_uid_tenant_type_uid
        self.tenant_uid_tenant_category_uid = tenant_uid_tenant_category_uid
        self.tenant_uid_tenant_code = tenant_uid_tenant_code
        self.tenant_uid_tenant_description = tenant_uid_tenant_description
        self.tenant_uid_start_date = tenant_uid_start_date
        self.tenant_uid_end_date = tenant_uid_end_date
        self.tenant_uid_is_internal = tenant_uid_is_internal
        self.tenant_uid_is_system = tenant_uid_is_system
        self.tenant_uid_is_test = tenant_uid_is_test
        self.tenant_uid_account_uid = tenant_uid_account_uid
        self.account_uid_account_name = account_uid_account_name
        self.account_uid_tenant_uid = account_uid_tenant_uid
        self.account_uid_account_type_uid = account_uid_account_type_uid
        self.account_uid_account_title_uid = account_uid_account_title_uid
        self.account_uid_account_division_uid = account_uid_account_division_uid
        self.account_uid_account_group_uid = account_uid_account_group_uid
        self.account_uid_auth_identity_uid = account_uid_auth_identity_uid
        self.account_uid_account_email = account_uid_account_email
        self.account_uid_display_name = account_uid_display_name
        self.account_uid_is_system = account_uid_is_system
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.event_acknowledge_uid, self.event_acknowledge_name, self.event_notification_uid, self.tenant_uid, self.account_uid, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes, self.event_notification_uid_event_notification_name, self.event_notification_uid_tenant_uid, self.event_notification_uid_account_uid, self.event_notification_uid_notification_type, self.event_notification_uid_notification_topic, self.event_notification_uid_notification_format, self.event_notification_uid_notification_content, self.event_notification_uid_sending_status, self.tenant_uid_tenant_name, self.tenant_uid_country_uid, self.tenant_uid_tenant_type_uid, self.tenant_uid_tenant_category_uid, self.tenant_uid_tenant_code, self.tenant_uid_tenant_description, self.tenant_uid_start_date, self.tenant_uid_end_date, self.tenant_uid_is_internal, self.tenant_uid_is_system, self.tenant_uid_is_test, self.tenant_uid_account_uid, self.account_uid_account_name, self.account_uid_tenant_uid, self.account_uid_account_type_uid, self.account_uid_account_title_uid, self.account_uid_account_division_uid, self.account_uid_account_group_uid, self.account_uid_auth_identity_uid, self.account_uid_account_email, self.account_uid_display_name, self.account_uid_is_system]


@dataclass(frozen=False)
class event_channel_rich_dto(event_channel_read_dto):
    event_channel_uid: str | None
    event_channel_name: str | None
    event_channel_type_uid: str | None
    channel_definition: str | None
    last_status_name: str | None
    tenant_uid: str | None
    account_uid: str | None
    row_instance: str | None
    row_lock: str | None
    row_owner: str | None
    row_seq: int | None
    row_guid: str | None
    row_version: int | None
    is_active: int | None
    created_date: datetime.datetime | None
    created_by: str | None
    last_updated_date: datetime.datetime | None
    last_updated_by: str | None
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str | None
    event_channel_type_uid_event_channel_type_name: str | None
    event_channel_type_uid_channel_type_description: str | None
    tenant_uid_tenant_name: str | None
    tenant_uid_country_uid: str | None
    tenant_uid_tenant_type_uid: str | None
    tenant_uid_tenant_category_uid: str | None
    tenant_uid_tenant_code: str | None
    tenant_uid_tenant_description: str | None
    tenant_uid_start_date: datetime.datetime | None
    tenant_uid_end_date: datetime.datetime | None
    tenant_uid_is_internal: int | None
    tenant_uid_is_system: int | None
    tenant_uid_is_test: int | None
    tenant_uid_account_uid: str | None
    account_uid_account_name: str | None
    account_uid_tenant_uid: str | None
    account_uid_account_type_uid: str | None
    account_uid_account_title_uid: str | None
    account_uid_account_division_uid: str | None
    account_uid_account_group_uid: str | None
    account_uid_auth_identity_uid: str | None
    account_uid_account_email: str | None
    account_uid_display_name: str | None
    account_uid_is_system: int | None
    def __init__(self, event_channel_uid: str | None, event_channel_name: str | None, event_channel_type_uid: str | None, channel_definition: str | None, last_status_name: str | None, tenant_uid: str | None, account_uid: str | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None, event_channel_type_uid_event_channel_type_name: str | None, event_channel_type_uid_channel_type_description: str | None, tenant_uid_tenant_name: str | None, tenant_uid_country_uid: str | None, tenant_uid_tenant_type_uid: str | None, tenant_uid_tenant_category_uid: str | None, tenant_uid_tenant_code: str | None, tenant_uid_tenant_description: str | None, tenant_uid_start_date: datetime.datetime | None, tenant_uid_end_date: datetime.datetime | None, tenant_uid_is_internal: int | None, tenant_uid_is_system: int | None, tenant_uid_is_test: int | None, tenant_uid_account_uid: str | None, account_uid_account_name: str | None, account_uid_tenant_uid: str | None, account_uid_account_type_uid: str | None, account_uid_account_title_uid: str | None, account_uid_account_division_uid: str | None, account_uid_account_group_uid: str | None, account_uid_auth_identity_uid: str | None, account_uid_account_email: str | None, account_uid_display_name: str | None, account_uid_is_system: int | None):
        self.event_channel_uid = event_channel_uid
        self.event_channel_name = event_channel_name
        self.event_channel_type_uid = event_channel_type_uid
        self.channel_definition = channel_definition
        self.last_status_name = last_status_name
        self.tenant_uid = tenant_uid
        self.account_uid = account_uid
        self.row_instance = row_instance
        self.row_lock = row_lock
        self.row_owner = row_owner
        self.row_seq = row_seq
        self.row_guid = row_guid
        self.row_version = row_version
        self.is_active = is_active
        self.created_date = created_date
        self.created_by = created_by
        self.last_updated_date = last_updated_date
        self.last_updated_by = last_updated_by
        self.removed_date = removed_date
        self.removed_by = removed_by
        self.custom_attributes = custom_attributes
        self.event_channel_type_uid_event_channel_type_name = event_channel_type_uid_event_channel_type_name
        self.event_channel_type_uid_channel_type_description = event_channel_type_uid_channel_type_description
        self.tenant_uid_tenant_name = tenant_uid_tenant_name
        self.tenant_uid_country_uid = tenant_uid_country_uid
        self.tenant_uid_tenant_type_uid = tenant_uid_tenant_type_uid
        self.tenant_uid_tenant_category_uid = tenant_uid_tenant_category_uid
        self.tenant_uid_tenant_code = tenant_uid_tenant_code
        self.tenant_uid_tenant_description = tenant_uid_tenant_description
        self.tenant_uid_start_date = tenant_uid_start_date
        self.tenant_uid_end_date = tenant_uid_end_date
        self.tenant_uid_is_internal = tenant_uid_is_internal
        self.tenant_uid_is_system = tenant_uid_is_system
        self.tenant_uid_is_test = tenant_uid_is_test
        self.tenant_uid_account_uid = tenant_uid_account_uid
        self.account_uid_account_name = account_uid_account_name
        self.account_uid_tenant_uid = account_uid_tenant_uid
        self.account_uid_account_type_uid = account_uid_account_type_uid
        self.account_uid_account_title_uid = account_uid_account_title_uid
        self.account_uid_account_division_uid = account_uid_account_division_uid
        self.account_uid_account_group_uid = account_uid_account_group_uid
        self.account_uid_auth_identity_uid = account_uid_auth_identity_uid
        self.account_uid_account_email = account_uid_account_email
        self.account_uid_display_name = account_uid_display_name
        self.account_uid_is_system = account_uid_is_system
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.event_channel_uid, self.event_channel_name, self.event_channel_type_uid, self.channel_definition, self.last_status_name, self.tenant_uid, self.account_uid, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes, self.event_channel_type_uid_event_channel_type_name, self.event_channel_type_uid_channel_type_description, self.tenant_uid_tenant_name, self.tenant_uid_country_uid, self.tenant_uid_tenant_type_uid, self.tenant_uid_tenant_category_uid, self.tenant_uid_tenant_code, self.tenant_uid_tenant_description, self.tenant_uid_start_date, self.tenant_uid_end_date, self.tenant_uid_is_internal, self.tenant_uid_is_system, self.tenant_uid_is_test, self.tenant_uid_account_uid, self.account_uid_account_name, self.account_uid_tenant_uid, self.account_uid_account_type_uid, self.account_uid_account_title_uid, self.account_uid_account_division_uid, self.account_uid_account_group_uid, self.account_uid_auth_identity_uid, self.account_uid_account_email, self.account_uid_display_name, self.account_uid_is_system]


@dataclass(frozen=False)
class event_channel_type_rich_dto(event_channel_type_read_dto):
    event_channel_type_uid: str | None
    event_channel_type_name: str | None
    channel_type_description: str | None
    row_instance: str | None
    row_lock: str | None
    row_owner: str | None
    row_seq: int | None
    row_guid: str | None
    row_version: int | None
    is_active: int | None
    created_date: datetime.datetime | None
    created_by: str | None
    last_updated_date: datetime.datetime | None
    last_updated_by: str | None
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str | None
    def __init__(self, event_channel_type_uid: str | None, event_channel_type_name: str | None, channel_type_description: str | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None):
        self.event_channel_type_uid = event_channel_type_uid
        self.event_channel_type_name = event_channel_type_name
        self.channel_type_description = channel_type_description
        self.row_instance = row_instance
        self.row_lock = row_lock
        self.row_owner = row_owner
        self.row_seq = row_seq
        self.row_guid = row_guid
        self.row_version = row_version
        self.is_active = is_active
        self.created_date = created_date
        self.created_by = created_by
        self.last_updated_date = last_updated_date
        self.last_updated_by = last_updated_by
        self.removed_date = removed_date
        self.removed_by = removed_by
        self.custom_attributes = custom_attributes
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.event_channel_type_uid, self.event_channel_type_name, self.channel_type_description, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]


@dataclass(frozen=False)
class event_instance_rich_dto(event_instance_read_dto):
    event_instance_uid: str | None
    event_instance_name: str | None
    client_uid: str | None
    event_type: str | None
    event_object: str | None
    event_method: str | None
    event_parameters: str | None
    event_signature: str | None
    event_date: datetime.datetime | None
    published_count: int | None
    row_instance: str | None
    row_lock: str | None
    row_owner: str | None
    row_seq: int | None
    row_guid: str | None
    row_version: int | None
    is_active: int | None
    created_date: datetime.datetime | None
    created_by: str | None
    last_updated_date: datetime.datetime | None
    last_updated_by: str | None
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str | None
    client_uid_client_name: str | None
    client_uid_tenant_uid: str | None
    client_uid_country_uid: str | None
    client_uid_client_type_uid: str | None
    client_uid_client_category_uid: str | None
    client_uid_account_uid: str | None
    client_uid_client_code: str | None
    client_uid_client_description: str | None
    client_uid_start_date: datetime.datetime | None
    client_uid_end_date: datetime.datetime | None
    client_uid_is_internal: int | None
    client_uid_is_system: int | None
    client_uid_is_test: int | None
    def __init__(self, event_instance_uid: str | None, event_instance_name: str | None, client_uid: str | None, event_type: str | None, event_object: str | None, event_method: str | None, event_parameters: str | None, event_signature: str | None, event_date: datetime.datetime | None, published_count: int | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None, client_uid_client_name: str | None, client_uid_tenant_uid: str | None, client_uid_country_uid: str | None, client_uid_client_type_uid: str | None, client_uid_client_category_uid: str | None, client_uid_account_uid: str | None, client_uid_client_code: str | None, client_uid_client_description: str | None, client_uid_start_date: datetime.datetime | None, client_uid_end_date: datetime.datetime | None, client_uid_is_internal: int | None, client_uid_is_system: int | None, client_uid_is_test: int | None):
        self.event_instance_uid = event_instance_uid
        self.event_instance_name = event_instance_name
        self.client_uid = client_uid
        self.event_type = event_type
        self.event_object = event_object
        self.event_method = event_method
        self.event_parameters = event_parameters
        self.event_signature = event_signature
        self.event_date = event_date
        self.published_count = published_count
        self.row_instance = row_instance
        self.row_lock = row_lock
        self.row_owner = row_owner
        self.row_seq = row_seq
        self.row_guid = row_guid
        self.row_version = row_version
        self.is_active = is_active
        self.created_date = created_date
        self.created_by = created_by
        self.last_updated_date = last_updated_date
        self.last_updated_by = last_updated_by
        self.removed_date = removed_date
        self.removed_by = removed_by
        self.custom_attributes = custom_attributes
        self.client_uid_client_name = client_uid_client_name
        self.client_uid_tenant_uid = client_uid_tenant_uid
        self.client_uid_country_uid = client_uid_country_uid
        self.client_uid_client_type_uid = client_uid_client_type_uid
        self.client_uid_client_category_uid = client_uid_client_category_uid
        self.client_uid_account_uid = client_uid_account_uid
        self.client_uid_client_code = client_uid_client_code
        self.client_uid_client_description = client_uid_client_description
        self.client_uid_start_date = client_uid_start_date
        self.client_uid_end_date = client_uid_end_date
        self.client_uid_is_internal = client_uid_is_internal
        self.client_uid_is_system = client_uid_is_system
        self.client_uid_is_test = client_uid_is_test
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.event_instance_uid, self.event_instance_name, self.client_uid, self.event_type, self.event_object, self.event_method, self.event_parameters, self.event_signature, self.event_date, self.published_count, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes, self.client_uid_client_name, self.client_uid_tenant_uid, self.client_uid_country_uid, self.client_uid_client_type_uid, self.client_uid_client_category_uid, self.client_uid_account_uid, self.client_uid_client_code, self.client_uid_client_description, self.client_uid_start_date, self.client_uid_end_date, self.client_uid_is_internal, self.client_uid_is_system, self.client_uid_is_test]


@dataclass(frozen=False)
class event_notification_rich_dto(event_notification_read_dto):
    event_notification_uid: str | None
    event_notification_name: str | None
    tenant_uid: str | None
    account_uid: str | None
    notification_type: str | None
    notification_topic: str | None
    notification_format: str | None
    notification_content: str | None
    sending_status: str | None
    row_instance: str | None
    row_lock: str | None
    row_owner: str | None
    row_seq: int | None
    row_guid: str | None
    row_version: int | None
    is_active: int | None
    created_date: datetime.datetime | None
    created_by: str | None
    last_updated_date: datetime.datetime | None
    last_updated_by: str | None
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str | None
    tenant_uid_tenant_name: str | None
    tenant_uid_country_uid: str | None
    tenant_uid_tenant_type_uid: str | None
    tenant_uid_tenant_category_uid: str | None
    tenant_uid_tenant_code: str | None
    tenant_uid_tenant_description: str | None
    tenant_uid_start_date: datetime.datetime | None
    tenant_uid_end_date: datetime.datetime | None
    tenant_uid_is_internal: int | None
    tenant_uid_is_system: int | None
    tenant_uid_is_test: int | None
    tenant_uid_account_uid: str | None
    account_uid_account_name: str | None
    account_uid_tenant_uid: str | None
    account_uid_account_type_uid: str | None
    account_uid_account_title_uid: str | None
    account_uid_account_division_uid: str | None
    account_uid_account_group_uid: str | None
    account_uid_auth_identity_uid: str | None
    account_uid_account_email: str | None
    account_uid_display_name: str | None
    account_uid_is_system: int | None
    def __init__(self, event_notification_uid: str | None, event_notification_name: str | None, tenant_uid: str | None, account_uid: str | None, notification_type: str | None, notification_topic: str | None, notification_format: str | None, notification_content: str | None, sending_status: str | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None, tenant_uid_tenant_name: str | None, tenant_uid_country_uid: str | None, tenant_uid_tenant_type_uid: str | None, tenant_uid_tenant_category_uid: str | None, tenant_uid_tenant_code: str | None, tenant_uid_tenant_description: str | None, tenant_uid_start_date: datetime.datetime | None, tenant_uid_end_date: datetime.datetime | None, tenant_uid_is_internal: int | None, tenant_uid_is_system: int | None, tenant_uid_is_test: int | None, tenant_uid_account_uid: str | None, account_uid_account_name: str | None, account_uid_tenant_uid: str | None, account_uid_account_type_uid: str | None, account_uid_account_title_uid: str | None, account_uid_account_division_uid: str | None, account_uid_account_group_uid: str | None, account_uid_auth_identity_uid: str | None, account_uid_account_email: str | None, account_uid_display_name: str | None, account_uid_is_system: int | None):
        self.event_notification_uid = event_notification_uid
        self.event_notification_name = event_notification_name
        self.tenant_uid = tenant_uid
        self.account_uid = account_uid
        self.notification_type = notification_type
        self.notification_topic = notification_topic
        self.notification_format = notification_format
        self.notification_content = notification_content
        self.sending_status = sending_status
        self.row_instance = row_instance
        self.row_lock = row_lock
        self.row_owner = row_owner
        self.row_seq = row_seq
        self.row_guid = row_guid
        self.row_version = row_version
        self.is_active = is_active
        self.created_date = created_date
        self.created_by = created_by
        self.last_updated_date = last_updated_date
        self.last_updated_by = last_updated_by
        self.removed_date = removed_date
        self.removed_by = removed_by
        self.custom_attributes = custom_attributes
        self.tenant_uid_tenant_name = tenant_uid_tenant_name
        self.tenant_uid_country_uid = tenant_uid_country_uid
        self.tenant_uid_tenant_type_uid = tenant_uid_tenant_type_uid
        self.tenant_uid_tenant_category_uid = tenant_uid_tenant_category_uid
        self.tenant_uid_tenant_code = tenant_uid_tenant_code
        self.tenant_uid_tenant_description = tenant_uid_tenant_description
        self.tenant_uid_start_date = tenant_uid_start_date
        self.tenant_uid_end_date = tenant_uid_end_date
        self.tenant_uid_is_internal = tenant_uid_is_internal
        self.tenant_uid_is_system = tenant_uid_is_system
        self.tenant_uid_is_test = tenant_uid_is_test
        self.tenant_uid_account_uid = tenant_uid_account_uid
        self.account_uid_account_name = account_uid_account_name
        self.account_uid_tenant_uid = account_uid_tenant_uid
        self.account_uid_account_type_uid = account_uid_account_type_uid
        self.account_uid_account_title_uid = account_uid_account_title_uid
        self.account_uid_account_division_uid = account_uid_account_division_uid
        self.account_uid_account_group_uid = account_uid_account_group_uid
        self.account_uid_auth_identity_uid = account_uid_auth_identity_uid
        self.account_uid_account_email = account_uid_account_email
        self.account_uid_display_name = account_uid_display_name
        self.account_uid_is_system = account_uid_is_system
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.event_notification_uid, self.event_notification_name, self.tenant_uid, self.account_uid, self.notification_type, self.notification_topic, self.notification_format, self.notification_content, self.sending_status, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes, self.tenant_uid_tenant_name, self.tenant_uid_country_uid, self.tenant_uid_tenant_type_uid, self.tenant_uid_tenant_category_uid, self.tenant_uid_tenant_code, self.tenant_uid_tenant_description, self.tenant_uid_start_date, self.tenant_uid_end_date, self.tenant_uid_is_internal, self.tenant_uid_is_system, self.tenant_uid_is_test, self.tenant_uid_account_uid, self.account_uid_account_name, self.account_uid_tenant_uid, self.account_uid_account_type_uid, self.account_uid_account_title_uid, self.account_uid_account_division_uid, self.account_uid_account_group_uid, self.account_uid_auth_identity_uid, self.account_uid_account_email, self.account_uid_display_name, self.account_uid_is_system]


@dataclass(frozen=False)
class event_observer_rich_dto(event_observer_read_dto):
    event_observer_uid: str | None
    event_observer_name: str | None
    event_observer_definition: str | None
    row_instance: str | None
    row_lock: str | None
    row_owner: str | None
    row_seq: int | None
    row_guid: str | None
    row_version: int | None
    is_active: int | None
    created_date: datetime.datetime | None
    created_by: str | None
    last_updated_date: datetime.datetime | None
    last_updated_by: str | None
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str | None
    def __init__(self, event_observer_uid: str | None, event_observer_name: str | None, event_observer_definition: str | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None):
        self.event_observer_uid = event_observer_uid
        self.event_observer_name = event_observer_name
        self.event_observer_definition = event_observer_definition
        self.row_instance = row_instance
        self.row_lock = row_lock
        self.row_owner = row_owner
        self.row_seq = row_seq
        self.row_guid = row_guid
        self.row_version = row_version
        self.is_active = is_active
        self.created_date = created_date
        self.created_by = created_by
        self.last_updated_date = last_updated_date
        self.last_updated_by = last_updated_by
        self.removed_date = removed_date
        self.removed_by = removed_by
        self.custom_attributes = custom_attributes
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.event_observer_uid, self.event_observer_name, self.event_observer_definition, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]


@dataclass(frozen=False)
class event_subscription_rich_dto(event_subscription_read_dto):
    event_subscription_uid: str | None
    event_subscription_name: str | None
    event_channel_uid: str | None
    tenant_uid: str | None
    account_uid: str | None
    subscription_filter: str | None
    subscription_topic: str | None
    subscription_template: str | None
    row_instance: str | None
    row_lock: str | None
    row_owner: str | None
    row_seq: int | None
    row_guid: str | None
    row_version: int | None
    is_active: int | None
    created_date: datetime.datetime | None
    created_by: str | None
    last_updated_date: datetime.datetime | None
    last_updated_by: str | None
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str | None
    event_channel_uid_event_channel_name: str | None
    event_channel_uid_event_channel_type_uid: str | None
    event_channel_uid_channel_definition: str | None
    event_channel_uid_last_status_name: str | None
    event_channel_uid_tenant_uid: str | None
    event_channel_uid_account_uid: str | None
    tenant_uid_tenant_name: str | None
    tenant_uid_country_uid: str | None
    tenant_uid_tenant_type_uid: str | None
    tenant_uid_tenant_category_uid: str | None
    tenant_uid_tenant_code: str | None
    tenant_uid_tenant_description: str | None
    tenant_uid_start_date: datetime.datetime | None
    tenant_uid_end_date: datetime.datetime | None
    tenant_uid_is_internal: int | None
    tenant_uid_is_system: int | None
    tenant_uid_is_test: int | None
    tenant_uid_account_uid: str | None
    account_uid_account_name: str | None
    account_uid_tenant_uid: str | None
    account_uid_account_type_uid: str | None
    account_uid_account_title_uid: str | None
    account_uid_account_division_uid: str | None
    account_uid_account_group_uid: str | None
    account_uid_auth_identity_uid: str | None
    account_uid_account_email: str | None
    account_uid_display_name: str | None
    account_uid_is_system: int | None
    def __init__(self, event_subscription_uid: str | None, event_subscription_name: str | None, event_channel_uid: str | None, tenant_uid: str | None, account_uid: str | None, subscription_filter: str | None, subscription_topic: str | None, subscription_template: str | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None, event_channel_uid_event_channel_name: str | None, event_channel_uid_event_channel_type_uid: str | None, event_channel_uid_channel_definition: str | None, event_channel_uid_last_status_name: str | None, event_channel_uid_tenant_uid: str | None, event_channel_uid_account_uid: str | None, tenant_uid_tenant_name: str | None, tenant_uid_country_uid: str | None, tenant_uid_tenant_type_uid: str | None, tenant_uid_tenant_category_uid: str | None, tenant_uid_tenant_code: str | None, tenant_uid_tenant_description: str | None, tenant_uid_start_date: datetime.datetime | None, tenant_uid_end_date: datetime.datetime | None, tenant_uid_is_internal: int | None, tenant_uid_is_system: int | None, tenant_uid_is_test: int | None, tenant_uid_account_uid: str | None, account_uid_account_name: str | None, account_uid_tenant_uid: str | None, account_uid_account_type_uid: str | None, account_uid_account_title_uid: str | None, account_uid_account_division_uid: str | None, account_uid_account_group_uid: str | None, account_uid_auth_identity_uid: str | None, account_uid_account_email: str | None, account_uid_display_name: str | None, account_uid_is_system: int | None):
        self.event_subscription_uid = event_subscription_uid
        self.event_subscription_name = event_subscription_name
        self.event_channel_uid = event_channel_uid
        self.tenant_uid = tenant_uid
        self.account_uid = account_uid
        self.subscription_filter = subscription_filter
        self.subscription_topic = subscription_topic
        self.subscription_template = subscription_template
        self.row_instance = row_instance
        self.row_lock = row_lock
        self.row_owner = row_owner
        self.row_seq = row_seq
        self.row_guid = row_guid
        self.row_version = row_version
        self.is_active = is_active
        self.created_date = created_date
        self.created_by = created_by
        self.last_updated_date = last_updated_date
        self.last_updated_by = last_updated_by
        self.removed_date = removed_date
        self.removed_by = removed_by
        self.custom_attributes = custom_attributes
        self.event_channel_uid_event_channel_name = event_channel_uid_event_channel_name
        self.event_channel_uid_event_channel_type_uid = event_channel_uid_event_channel_type_uid
        self.event_channel_uid_channel_definition = event_channel_uid_channel_definition
        self.event_channel_uid_last_status_name = event_channel_uid_last_status_name
        self.event_channel_uid_tenant_uid = event_channel_uid_tenant_uid
        self.event_channel_uid_account_uid = event_channel_uid_account_uid
        self.tenant_uid_tenant_name = tenant_uid_tenant_name
        self.tenant_uid_country_uid = tenant_uid_country_uid
        self.tenant_uid_tenant_type_uid = tenant_uid_tenant_type_uid
        self.tenant_uid_tenant_category_uid = tenant_uid_tenant_category_uid
        self.tenant_uid_tenant_code = tenant_uid_tenant_code
        self.tenant_uid_tenant_description = tenant_uid_tenant_description
        self.tenant_uid_start_date = tenant_uid_start_date
        self.tenant_uid_end_date = tenant_uid_end_date
        self.tenant_uid_is_internal = tenant_uid_is_internal
        self.tenant_uid_is_system = tenant_uid_is_system
        self.tenant_uid_is_test = tenant_uid_is_test
        self.tenant_uid_account_uid = tenant_uid_account_uid
        self.account_uid_account_name = account_uid_account_name
        self.account_uid_tenant_uid = account_uid_tenant_uid
        self.account_uid_account_type_uid = account_uid_account_type_uid
        self.account_uid_account_title_uid = account_uid_account_title_uid
        self.account_uid_account_division_uid = account_uid_account_division_uid
        self.account_uid_account_group_uid = account_uid_account_group_uid
        self.account_uid_auth_identity_uid = account_uid_auth_identity_uid
        self.account_uid_account_email = account_uid_account_email
        self.account_uid_display_name = account_uid_display_name
        self.account_uid_is_system = account_uid_is_system
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.event_subscription_uid, self.event_subscription_name, self.event_channel_uid, self.tenant_uid, self.account_uid, self.subscription_filter, self.subscription_topic, self.subscription_template, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes, self.event_channel_uid_event_channel_name, self.event_channel_uid_event_channel_type_uid, self.event_channel_uid_channel_definition, self.event_channel_uid_last_status_name, self.event_channel_uid_tenant_uid, self.event_channel_uid_account_uid, self.tenant_uid_tenant_name, self.tenant_uid_country_uid, self.tenant_uid_tenant_type_uid, self.tenant_uid_tenant_category_uid, self.tenant_uid_tenant_code, self.tenant_uid_tenant_description, self.tenant_uid_start_date, self.tenant_uid_end_date, self.tenant_uid_is_internal, self.tenant_uid_is_system, self.tenant_uid_is_test, self.tenant_uid_account_uid, self.account_uid_account_name, self.account_uid_tenant_uid, self.account_uid_account_type_uid, self.account_uid_account_title_uid, self.account_uid_account_division_uid, self.account_uid_account_group_uid, self.account_uid_auth_identity_uid, self.account_uid_account_email, self.account_uid_display_name, self.account_uid_is_system]


@dataclass(frozen=False)
class event_template_rich_dto(event_template_read_dto):
    event_template_uid: str | None
    event_template_name: str | None
    tenant_uid: str | None
    notification_type: str | None
    notification_topic: str | None
    notification_format: str | None
    row_instance: str | None
    row_lock: str | None
    row_owner: str | None
    row_seq: int | None
    row_guid: str | None
    row_version: int | None
    is_active: int | None
    created_date: datetime.datetime | None
    created_by: str | None
    last_updated_date: datetime.datetime | None
    last_updated_by: str | None
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str | None
    tenant_uid_tenant_name: str | None
    tenant_uid_country_uid: str | None
    tenant_uid_tenant_type_uid: str | None
    tenant_uid_tenant_category_uid: str | None
    tenant_uid_tenant_code: str | None
    tenant_uid_tenant_description: str | None
    tenant_uid_start_date: datetime.datetime | None
    tenant_uid_end_date: datetime.datetime | None
    tenant_uid_is_internal: int | None
    tenant_uid_is_system: int | None
    tenant_uid_is_test: int | None
    tenant_uid_account_uid: str | None
    def __init__(self, event_template_uid: str | None, event_template_name: str | None, tenant_uid: str | None, notification_type: str | None, notification_topic: str | None, notification_format: str | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None, tenant_uid_tenant_name: str | None, tenant_uid_country_uid: str | None, tenant_uid_tenant_type_uid: str | None, tenant_uid_tenant_category_uid: str | None, tenant_uid_tenant_code: str | None, tenant_uid_tenant_description: str | None, tenant_uid_start_date: datetime.datetime | None, tenant_uid_end_date: datetime.datetime | None, tenant_uid_is_internal: int | None, tenant_uid_is_system: int | None, tenant_uid_is_test: int | None, tenant_uid_account_uid: str | None):
        self.event_template_uid = event_template_uid
        self.event_template_name = event_template_name
        self.tenant_uid = tenant_uid
        self.notification_type = notification_type
        self.notification_topic = notification_topic
        self.notification_format = notification_format
        self.row_instance = row_instance
        self.row_lock = row_lock
        self.row_owner = row_owner
        self.row_seq = row_seq
        self.row_guid = row_guid
        self.row_version = row_version
        self.is_active = is_active
        self.created_date = created_date
        self.created_by = created_by
        self.last_updated_date = last_updated_date
        self.last_updated_by = last_updated_by
        self.removed_date = removed_date
        self.removed_by = removed_by
        self.custom_attributes = custom_attributes
        self.tenant_uid_tenant_name = tenant_uid_tenant_name
        self.tenant_uid_country_uid = tenant_uid_country_uid
        self.tenant_uid_tenant_type_uid = tenant_uid_tenant_type_uid
        self.tenant_uid_tenant_category_uid = tenant_uid_tenant_category_uid
        self.tenant_uid_tenant_code = tenant_uid_tenant_code
        self.tenant_uid_tenant_description = tenant_uid_tenant_description
        self.tenant_uid_start_date = tenant_uid_start_date
        self.tenant_uid_end_date = tenant_uid_end_date
        self.tenant_uid_is_internal = tenant_uid_is_internal
        self.tenant_uid_is_system = tenant_uid_is_system
        self.tenant_uid_is_test = tenant_uid_is_test
        self.tenant_uid_account_uid = tenant_uid_account_uid
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.event_template_uid, self.event_template_name, self.tenant_uid, self.notification_type, self.notification_topic, self.notification_format, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes, self.tenant_uid_tenant_name, self.tenant_uid_country_uid, self.tenant_uid_tenant_type_uid, self.tenant_uid_tenant_category_uid, self.tenant_uid_tenant_code, self.tenant_uid_tenant_description, self.tenant_uid_start_date, self.tenant_uid_end_date, self.tenant_uid_is_internal, self.tenant_uid_is_system, self.tenant_uid_is_test, self.tenant_uid_account_uid]


@dataclass(frozen=False)
class event_type_rich_dto(event_type_read_dto):
    event_type_uid: str | None
    event_type_name: str | None
    event_type_description: str | None
    row_instance: str | None
    row_lock: str | None
    row_owner: str | None
    row_seq: int | None
    row_guid: str | None
    row_version: int | None
    is_active: int | None
    created_date: datetime.datetime | None
    created_by: str | None
    last_updated_date: datetime.datetime | None
    last_updated_by: str | None
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str | None
    def __init__(self, event_type_uid: str | None, event_type_name: str | None, event_type_description: str | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None):
        self.event_type_uid = event_type_uid
        self.event_type_name = event_type_name
        self.event_type_description = event_type_description
        self.row_instance = row_instance
        self.row_lock = row_lock
        self.row_owner = row_owner
        self.row_seq = row_seq
        self.row_guid = row_guid
        self.row_version = row_version
        self.is_active = is_active
        self.created_date = created_date
        self.created_by = created_by
        self.last_updated_date = last_updated_date
        self.last_updated_by = last_updated_by
        self.removed_date = removed_date
        self.removed_by = removed_by
        self.custom_attributes = custom_attributes
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.event_type_uid, self.event_type_name, self.event_type_description, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]


@dataclass(frozen=False)
class invoice_action_rich_dto(invoice_action_read_dto):
    invoice_action_uid: str | None
    invoice_action_name: str | None
    tenant_uid: str | None
    account_uid: str | None
    invoice_instance_uid: str | None
    invoice_action_type_uid: str | None
    row_instance: str | None
    row_lock: str | None
    row_owner: str | None
    row_seq: int | None
    row_guid: str | None
    row_version: int | None
    is_active: int | None
    created_date: datetime.datetime | None
    created_by: str | None
    last_updated_date: datetime.datetime | None
    last_updated_by: str | None
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str | None
    tenant_uid_tenant_name: str | None
    tenant_uid_country_uid: str | None
    tenant_uid_tenant_type_uid: str | None
    tenant_uid_tenant_category_uid: str | None
    tenant_uid_tenant_code: str | None
    tenant_uid_tenant_description: str | None
    tenant_uid_start_date: datetime.datetime | None
    tenant_uid_end_date: datetime.datetime | None
    tenant_uid_is_internal: int | None
    tenant_uid_is_system: int | None
    tenant_uid_is_test: int | None
    tenant_uid_account_uid: str | None
    account_uid_account_name: str | None
    account_uid_tenant_uid: str | None
    account_uid_account_type_uid: str | None
    account_uid_account_title_uid: str | None
    account_uid_account_division_uid: str | None
    account_uid_account_group_uid: str | None
    account_uid_auth_identity_uid: str | None
    account_uid_account_email: str | None
    account_uid_display_name: str | None
    account_uid_is_system: int | None
    invoice_instance_uid_invoice_instance_name: str | None
    invoice_instance_uid_tenant_uid: str | None
    invoice_instance_uid_account_uid: str | None
    invoice_instance_uid_invoice_flow_uid: str | None
    invoice_instance_uid_invoice_status_uid: str | None
    invoice_instance_uid_invoice_category_uid: str | None
    invoice_instance_uid_invoice_type_uid: str | None
    invoice_instance_uid_period_uid: str | None
    invoice_instance_uid_currency_uid: str | None
    invoice_instance_uid_invoice_number: str | None
    invoice_instance_uid_invoice_details: str | None
    invoice_instance_uid_invoice_amount_net: str | None
    invoice_instance_uid_invoice_amount_tax: str | None
    invoice_instance_uid_invoice_amount_gross: str | None
    invoice_action_type_uid_invoice_action_type_name: str | None
    def __init__(self, invoice_action_uid: str | None, invoice_action_name: str | None, tenant_uid: str | None, account_uid: str | None, invoice_instance_uid: str | None, invoice_action_type_uid: str | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None, tenant_uid_tenant_name: str | None, tenant_uid_country_uid: str | None, tenant_uid_tenant_type_uid: str | None, tenant_uid_tenant_category_uid: str | None, tenant_uid_tenant_code: str | None, tenant_uid_tenant_description: str | None, tenant_uid_start_date: datetime.datetime | None, tenant_uid_end_date: datetime.datetime | None, tenant_uid_is_internal: int | None, tenant_uid_is_system: int | None, tenant_uid_is_test: int | None, tenant_uid_account_uid: str | None, account_uid_account_name: str | None, account_uid_tenant_uid: str | None, account_uid_account_type_uid: str | None, account_uid_account_title_uid: str | None, account_uid_account_division_uid: str | None, account_uid_account_group_uid: str | None, account_uid_auth_identity_uid: str | None, account_uid_account_email: str | None, account_uid_display_name: str | None, account_uid_is_system: int | None, invoice_instance_uid_invoice_instance_name: str | None, invoice_instance_uid_tenant_uid: str | None, invoice_instance_uid_account_uid: str | None, invoice_instance_uid_invoice_flow_uid: str | None, invoice_instance_uid_invoice_status_uid: str | None, invoice_instance_uid_invoice_category_uid: str | None, invoice_instance_uid_invoice_type_uid: str | None, invoice_instance_uid_period_uid: str | None, invoice_instance_uid_currency_uid: str | None, invoice_instance_uid_invoice_number: str | None, invoice_instance_uid_invoice_details: str | None, invoice_instance_uid_invoice_amount_net: str | None, invoice_instance_uid_invoice_amount_tax: str | None, invoice_instance_uid_invoice_amount_gross: str | None, invoice_action_type_uid_invoice_action_type_name: str | None):
        self.invoice_action_uid = invoice_action_uid
        self.invoice_action_name = invoice_action_name
        self.tenant_uid = tenant_uid
        self.account_uid = account_uid
        self.invoice_instance_uid = invoice_instance_uid
        self.invoice_action_type_uid = invoice_action_type_uid
        self.row_instance = row_instance
        self.row_lock = row_lock
        self.row_owner = row_owner
        self.row_seq = row_seq
        self.row_guid = row_guid
        self.row_version = row_version
        self.is_active = is_active
        self.created_date = created_date
        self.created_by = created_by
        self.last_updated_date = last_updated_date
        self.last_updated_by = last_updated_by
        self.removed_date = removed_date
        self.removed_by = removed_by
        self.custom_attributes = custom_attributes
        self.tenant_uid_tenant_name = tenant_uid_tenant_name
        self.tenant_uid_country_uid = tenant_uid_country_uid
        self.tenant_uid_tenant_type_uid = tenant_uid_tenant_type_uid
        self.tenant_uid_tenant_category_uid = tenant_uid_tenant_category_uid
        self.tenant_uid_tenant_code = tenant_uid_tenant_code
        self.tenant_uid_tenant_description = tenant_uid_tenant_description
        self.tenant_uid_start_date = tenant_uid_start_date
        self.tenant_uid_end_date = tenant_uid_end_date
        self.tenant_uid_is_internal = tenant_uid_is_internal
        self.tenant_uid_is_system = tenant_uid_is_system
        self.tenant_uid_is_test = tenant_uid_is_test
        self.tenant_uid_account_uid = tenant_uid_account_uid
        self.account_uid_account_name = account_uid_account_name
        self.account_uid_tenant_uid = account_uid_tenant_uid
        self.account_uid_account_type_uid = account_uid_account_type_uid
        self.account_uid_account_title_uid = account_uid_account_title_uid
        self.account_uid_account_division_uid = account_uid_account_division_uid
        self.account_uid_account_group_uid = account_uid_account_group_uid
        self.account_uid_auth_identity_uid = account_uid_auth_identity_uid
        self.account_uid_account_email = account_uid_account_email
        self.account_uid_display_name = account_uid_display_name
        self.account_uid_is_system = account_uid_is_system
        self.invoice_instance_uid_invoice_instance_name = invoice_instance_uid_invoice_instance_name
        self.invoice_instance_uid_tenant_uid = invoice_instance_uid_tenant_uid
        self.invoice_instance_uid_account_uid = invoice_instance_uid_account_uid
        self.invoice_instance_uid_invoice_flow_uid = invoice_instance_uid_invoice_flow_uid
        self.invoice_instance_uid_invoice_status_uid = invoice_instance_uid_invoice_status_uid
        self.invoice_instance_uid_invoice_category_uid = invoice_instance_uid_invoice_category_uid
        self.invoice_instance_uid_invoice_type_uid = invoice_instance_uid_invoice_type_uid
        self.invoice_instance_uid_period_uid = invoice_instance_uid_period_uid
        self.invoice_instance_uid_currency_uid = invoice_instance_uid_currency_uid
        self.invoice_instance_uid_invoice_number = invoice_instance_uid_invoice_number
        self.invoice_instance_uid_invoice_details = invoice_instance_uid_invoice_details
        self.invoice_instance_uid_invoice_amount_net = invoice_instance_uid_invoice_amount_net
        self.invoice_instance_uid_invoice_amount_tax = invoice_instance_uid_invoice_amount_tax
        self.invoice_instance_uid_invoice_amount_gross = invoice_instance_uid_invoice_amount_gross
        self.invoice_action_type_uid_invoice_action_type_name = invoice_action_type_uid_invoice_action_type_name
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.invoice_action_uid, self.invoice_action_name, self.tenant_uid, self.account_uid, self.invoice_instance_uid, self.invoice_action_type_uid, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes, self.tenant_uid_tenant_name, self.tenant_uid_country_uid, self.tenant_uid_tenant_type_uid, self.tenant_uid_tenant_category_uid, self.tenant_uid_tenant_code, self.tenant_uid_tenant_description, self.tenant_uid_start_date, self.tenant_uid_end_date, self.tenant_uid_is_internal, self.tenant_uid_is_system, self.tenant_uid_is_test, self.tenant_uid_account_uid, self.account_uid_account_name, self.account_uid_tenant_uid, self.account_uid_account_type_uid, self.account_uid_account_title_uid, self.account_uid_account_division_uid, self.account_uid_account_group_uid, self.account_uid_auth_identity_uid, self.account_uid_account_email, self.account_uid_display_name, self.account_uid_is_system, self.invoice_instance_uid_invoice_instance_name, self.invoice_instance_uid_tenant_uid, self.invoice_instance_uid_account_uid, self.invoice_instance_uid_invoice_flow_uid, self.invoice_instance_uid_invoice_status_uid, self.invoice_instance_uid_invoice_category_uid, self.invoice_instance_uid_invoice_type_uid, self.invoice_instance_uid_period_uid, self.invoice_instance_uid_currency_uid, self.invoice_instance_uid_invoice_number, self.invoice_instance_uid_invoice_details, self.invoice_instance_uid_invoice_amount_net, self.invoice_instance_uid_invoice_amount_tax, self.invoice_instance_uid_invoice_amount_gross, self.invoice_action_type_uid_invoice_action_type_name]


@dataclass(frozen=False)
class invoice_action_type_rich_dto(invoice_action_type_read_dto):
    invoice_action_type_uid: str | None
    invoice_action_type_name: str | None
    row_instance: str | None
    row_lock: str | None
    row_owner: str | None
    row_seq: int | None
    row_guid: str | None
    row_version: int | None
    is_active: int | None
    created_date: datetime.datetime | None
    created_by: str | None
    last_updated_date: datetime.datetime | None
    last_updated_by: str | None
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str | None
    def __init__(self, invoice_action_type_uid: str | None, invoice_action_type_name: str | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None):
        self.invoice_action_type_uid = invoice_action_type_uid
        self.invoice_action_type_name = invoice_action_type_name
        self.row_instance = row_instance
        self.row_lock = row_lock
        self.row_owner = row_owner
        self.row_seq = row_seq
        self.row_guid = row_guid
        self.row_version = row_version
        self.is_active = is_active
        self.created_date = created_date
        self.created_by = created_by
        self.last_updated_date = last_updated_date
        self.last_updated_by = last_updated_by
        self.removed_date = removed_date
        self.removed_by = removed_by
        self.custom_attributes = custom_attributes
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.invoice_action_type_uid, self.invoice_action_type_name, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]


@dataclass(frozen=False)
class invoice_category_rich_dto(invoice_category_read_dto):
    invoice_category_uid: str | None
    invoice_category_name: str | None
    tenant_uid: str | None
    invoice_category_description: str | None
    row_instance: str | None
    row_lock: str | None
    row_owner: str | None
    row_seq: int | None
    row_guid: str | None
    row_version: int | None
    is_active: int | None
    created_date: datetime.datetime | None
    created_by: str | None
    last_updated_date: datetime.datetime | None
    last_updated_by: str | None
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str | None
    tenant_uid_tenant_name: str | None
    tenant_uid_country_uid: str | None
    tenant_uid_tenant_type_uid: str | None
    tenant_uid_tenant_category_uid: str | None
    tenant_uid_tenant_code: str | None
    tenant_uid_tenant_description: str | None
    tenant_uid_start_date: datetime.datetime | None
    tenant_uid_end_date: datetime.datetime | None
    tenant_uid_is_internal: int | None
    tenant_uid_is_system: int | None
    tenant_uid_is_test: int | None
    tenant_uid_account_uid: str | None
    def __init__(self, invoice_category_uid: str | None, invoice_category_name: str | None, tenant_uid: str | None, invoice_category_description: str | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None, tenant_uid_tenant_name: str | None, tenant_uid_country_uid: str | None, tenant_uid_tenant_type_uid: str | None, tenant_uid_tenant_category_uid: str | None, tenant_uid_tenant_code: str | None, tenant_uid_tenant_description: str | None, tenant_uid_start_date: datetime.datetime | None, tenant_uid_end_date: datetime.datetime | None, tenant_uid_is_internal: int | None, tenant_uid_is_system: int | None, tenant_uid_is_test: int | None, tenant_uid_account_uid: str | None):
        self.invoice_category_uid = invoice_category_uid
        self.invoice_category_name = invoice_category_name
        self.tenant_uid = tenant_uid
        self.invoice_category_description = invoice_category_description
        self.row_instance = row_instance
        self.row_lock = row_lock
        self.row_owner = row_owner
        self.row_seq = row_seq
        self.row_guid = row_guid
        self.row_version = row_version
        self.is_active = is_active
        self.created_date = created_date
        self.created_by = created_by
        self.last_updated_date = last_updated_date
        self.last_updated_by = last_updated_by
        self.removed_date = removed_date
        self.removed_by = removed_by
        self.custom_attributes = custom_attributes
        self.tenant_uid_tenant_name = tenant_uid_tenant_name
        self.tenant_uid_country_uid = tenant_uid_country_uid
        self.tenant_uid_tenant_type_uid = tenant_uid_tenant_type_uid
        self.tenant_uid_tenant_category_uid = tenant_uid_tenant_category_uid
        self.tenant_uid_tenant_code = tenant_uid_tenant_code
        self.tenant_uid_tenant_description = tenant_uid_tenant_description
        self.tenant_uid_start_date = tenant_uid_start_date
        self.tenant_uid_end_date = tenant_uid_end_date
        self.tenant_uid_is_internal = tenant_uid_is_internal
        self.tenant_uid_is_system = tenant_uid_is_system
        self.tenant_uid_is_test = tenant_uid_is_test
        self.tenant_uid_account_uid = tenant_uid_account_uid
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.invoice_category_uid, self.invoice_category_name, self.tenant_uid, self.invoice_category_description, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes, self.tenant_uid_tenant_name, self.tenant_uid_country_uid, self.tenant_uid_tenant_type_uid, self.tenant_uid_tenant_category_uid, self.tenant_uid_tenant_code, self.tenant_uid_tenant_description, self.tenant_uid_start_date, self.tenant_uid_end_date, self.tenant_uid_is_internal, self.tenant_uid_is_system, self.tenant_uid_is_test, self.tenant_uid_account_uid]


@dataclass(frozen=False)
class invoice_entry_rich_dto(invoice_entry_read_dto):
    invoice_entry_uid: str | None
    invoice_entry_name: str | None
    tenant_uid: str | None
    account_uid: str | None
    invoice_instance_uid: str | None
    entry_details: str | None
    entry_amount_net: str | None
    entry_amount_tax: str | None
    entry_amount_gross: str | None
    row_instance: str | None
    row_lock: str | None
    row_owner: str | None
    row_seq: int | None
    row_guid: str | None
    row_version: int | None
    is_active: int | None
    created_date: datetime.datetime | None
    created_by: str | None
    last_updated_date: datetime.datetime | None
    last_updated_by: str | None
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str | None
    tenant_uid_tenant_name: str | None
    tenant_uid_country_uid: str | None
    tenant_uid_tenant_type_uid: str | None
    tenant_uid_tenant_category_uid: str | None
    tenant_uid_tenant_code: str | None
    tenant_uid_tenant_description: str | None
    tenant_uid_start_date: datetime.datetime | None
    tenant_uid_end_date: datetime.datetime | None
    tenant_uid_is_internal: int | None
    tenant_uid_is_system: int | None
    tenant_uid_is_test: int | None
    tenant_uid_account_uid: str | None
    account_uid_account_name: str | None
    account_uid_tenant_uid: str | None
    account_uid_account_type_uid: str | None
    account_uid_account_title_uid: str | None
    account_uid_account_division_uid: str | None
    account_uid_account_group_uid: str | None
    account_uid_auth_identity_uid: str | None
    account_uid_account_email: str | None
    account_uid_display_name: str | None
    account_uid_is_system: int | None
    invoice_instance_uid_invoice_instance_name: str | None
    invoice_instance_uid_tenant_uid: str | None
    invoice_instance_uid_account_uid: str | None
    invoice_instance_uid_invoice_flow_uid: str | None
    invoice_instance_uid_invoice_status_uid: str | None
    invoice_instance_uid_invoice_category_uid: str | None
    invoice_instance_uid_invoice_type_uid: str | None
    invoice_instance_uid_period_uid: str | None
    invoice_instance_uid_currency_uid: str | None
    invoice_instance_uid_invoice_number: str | None
    invoice_instance_uid_invoice_details: str | None
    invoice_instance_uid_invoice_amount_net: str | None
    invoice_instance_uid_invoice_amount_tax: str | None
    invoice_instance_uid_invoice_amount_gross: str | None
    def __init__(self, invoice_entry_uid: str | None, invoice_entry_name: str | None, tenant_uid: str | None, account_uid: str | None, invoice_instance_uid: str | None, entry_details: str | None, entry_amount_net: str | None, entry_amount_tax: str | None, entry_amount_gross: str | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None, tenant_uid_tenant_name: str | None, tenant_uid_country_uid: str | None, tenant_uid_tenant_type_uid: str | None, tenant_uid_tenant_category_uid: str | None, tenant_uid_tenant_code: str | None, tenant_uid_tenant_description: str | None, tenant_uid_start_date: datetime.datetime | None, tenant_uid_end_date: datetime.datetime | None, tenant_uid_is_internal: int | None, tenant_uid_is_system: int | None, tenant_uid_is_test: int | None, tenant_uid_account_uid: str | None, account_uid_account_name: str | None, account_uid_tenant_uid: str | None, account_uid_account_type_uid: str | None, account_uid_account_title_uid: str | None, account_uid_account_division_uid: str | None, account_uid_account_group_uid: str | None, account_uid_auth_identity_uid: str | None, account_uid_account_email: str | None, account_uid_display_name: str | None, account_uid_is_system: int | None, invoice_instance_uid_invoice_instance_name: str | None, invoice_instance_uid_tenant_uid: str | None, invoice_instance_uid_account_uid: str | None, invoice_instance_uid_invoice_flow_uid: str | None, invoice_instance_uid_invoice_status_uid: str | None, invoice_instance_uid_invoice_category_uid: str | None, invoice_instance_uid_invoice_type_uid: str | None, invoice_instance_uid_period_uid: str | None, invoice_instance_uid_currency_uid: str | None, invoice_instance_uid_invoice_number: str | None, invoice_instance_uid_invoice_details: str | None, invoice_instance_uid_invoice_amount_net: str | None, invoice_instance_uid_invoice_amount_tax: str | None, invoice_instance_uid_invoice_amount_gross: str | None):
        self.invoice_entry_uid = invoice_entry_uid
        self.invoice_entry_name = invoice_entry_name
        self.tenant_uid = tenant_uid
        self.account_uid = account_uid
        self.invoice_instance_uid = invoice_instance_uid
        self.entry_details = entry_details
        self.entry_amount_net = entry_amount_net
        self.entry_amount_tax = entry_amount_tax
        self.entry_amount_gross = entry_amount_gross
        self.row_instance = row_instance
        self.row_lock = row_lock
        self.row_owner = row_owner
        self.row_seq = row_seq
        self.row_guid = row_guid
        self.row_version = row_version
        self.is_active = is_active
        self.created_date = created_date
        self.created_by = created_by
        self.last_updated_date = last_updated_date
        self.last_updated_by = last_updated_by
        self.removed_date = removed_date
        self.removed_by = removed_by
        self.custom_attributes = custom_attributes
        self.tenant_uid_tenant_name = tenant_uid_tenant_name
        self.tenant_uid_country_uid = tenant_uid_country_uid
        self.tenant_uid_tenant_type_uid = tenant_uid_tenant_type_uid
        self.tenant_uid_tenant_category_uid = tenant_uid_tenant_category_uid
        self.tenant_uid_tenant_code = tenant_uid_tenant_code
        self.tenant_uid_tenant_description = tenant_uid_tenant_description
        self.tenant_uid_start_date = tenant_uid_start_date
        self.tenant_uid_end_date = tenant_uid_end_date
        self.tenant_uid_is_internal = tenant_uid_is_internal
        self.tenant_uid_is_system = tenant_uid_is_system
        self.tenant_uid_is_test = tenant_uid_is_test
        self.tenant_uid_account_uid = tenant_uid_account_uid
        self.account_uid_account_name = account_uid_account_name
        self.account_uid_tenant_uid = account_uid_tenant_uid
        self.account_uid_account_type_uid = account_uid_account_type_uid
        self.account_uid_account_title_uid = account_uid_account_title_uid
        self.account_uid_account_division_uid = account_uid_account_division_uid
        self.account_uid_account_group_uid = account_uid_account_group_uid
        self.account_uid_auth_identity_uid = account_uid_auth_identity_uid
        self.account_uid_account_email = account_uid_account_email
        self.account_uid_display_name = account_uid_display_name
        self.account_uid_is_system = account_uid_is_system
        self.invoice_instance_uid_invoice_instance_name = invoice_instance_uid_invoice_instance_name
        self.invoice_instance_uid_tenant_uid = invoice_instance_uid_tenant_uid
        self.invoice_instance_uid_account_uid = invoice_instance_uid_account_uid
        self.invoice_instance_uid_invoice_flow_uid = invoice_instance_uid_invoice_flow_uid
        self.invoice_instance_uid_invoice_status_uid = invoice_instance_uid_invoice_status_uid
        self.invoice_instance_uid_invoice_category_uid = invoice_instance_uid_invoice_category_uid
        self.invoice_instance_uid_invoice_type_uid = invoice_instance_uid_invoice_type_uid
        self.invoice_instance_uid_period_uid = invoice_instance_uid_period_uid
        self.invoice_instance_uid_currency_uid = invoice_instance_uid_currency_uid
        self.invoice_instance_uid_invoice_number = invoice_instance_uid_invoice_number
        self.invoice_instance_uid_invoice_details = invoice_instance_uid_invoice_details
        self.invoice_instance_uid_invoice_amount_net = invoice_instance_uid_invoice_amount_net
        self.invoice_instance_uid_invoice_amount_tax = invoice_instance_uid_invoice_amount_tax
        self.invoice_instance_uid_invoice_amount_gross = invoice_instance_uid_invoice_amount_gross
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.invoice_entry_uid, self.invoice_entry_name, self.tenant_uid, self.account_uid, self.invoice_instance_uid, self.entry_details, self.entry_amount_net, self.entry_amount_tax, self.entry_amount_gross, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes, self.tenant_uid_tenant_name, self.tenant_uid_country_uid, self.tenant_uid_tenant_type_uid, self.tenant_uid_tenant_category_uid, self.tenant_uid_tenant_code, self.tenant_uid_tenant_description, self.tenant_uid_start_date, self.tenant_uid_end_date, self.tenant_uid_is_internal, self.tenant_uid_is_system, self.tenant_uid_is_test, self.tenant_uid_account_uid, self.account_uid_account_name, self.account_uid_tenant_uid, self.account_uid_account_type_uid, self.account_uid_account_title_uid, self.account_uid_account_division_uid, self.account_uid_account_group_uid, self.account_uid_auth_identity_uid, self.account_uid_account_email, self.account_uid_display_name, self.account_uid_is_system, self.invoice_instance_uid_invoice_instance_name, self.invoice_instance_uid_tenant_uid, self.invoice_instance_uid_account_uid, self.invoice_instance_uid_invoice_flow_uid, self.invoice_instance_uid_invoice_status_uid, self.invoice_instance_uid_invoice_category_uid, self.invoice_instance_uid_invoice_type_uid, self.invoice_instance_uid_period_uid, self.invoice_instance_uid_currency_uid, self.invoice_instance_uid_invoice_number, self.invoice_instance_uid_invoice_details, self.invoice_instance_uid_invoice_amount_net, self.invoice_instance_uid_invoice_amount_tax, self.invoice_instance_uid_invoice_amount_gross]


@dataclass(frozen=False)
class invoice_flow_rich_dto(invoice_flow_read_dto):
    invoice_flow_uid: str | None
    invoice_flow_name: str | None
    flow_description: str | None
    flow_definition_json: str | None
    row_instance: str | None
    row_lock: str | None
    row_owner: str | None
    row_seq: int | None
    row_guid: str | None
    row_version: int | None
    is_active: int | None
    created_date: datetime.datetime | None
    created_by: str | None
    last_updated_date: datetime.datetime | None
    last_updated_by: str | None
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str | None
    def __init__(self, invoice_flow_uid: str | None, invoice_flow_name: str | None, flow_description: str | None, flow_definition_json: str | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None):
        self.invoice_flow_uid = invoice_flow_uid
        self.invoice_flow_name = invoice_flow_name
        self.flow_description = flow_description
        self.flow_definition_json = flow_definition_json
        self.row_instance = row_instance
        self.row_lock = row_lock
        self.row_owner = row_owner
        self.row_seq = row_seq
        self.row_guid = row_guid
        self.row_version = row_version
        self.is_active = is_active
        self.created_date = created_date
        self.created_by = created_by
        self.last_updated_date = last_updated_date
        self.last_updated_by = last_updated_by
        self.removed_date = removed_date
        self.removed_by = removed_by
        self.custom_attributes = custom_attributes
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.invoice_flow_uid, self.invoice_flow_name, self.flow_description, self.flow_definition_json, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]


@dataclass(frozen=False)
class invoice_flow_state_rich_dto(invoice_flow_state_read_dto):
    invoice_flow_state_uid: str | None
    invoice_flow_state_name: str | None
    invoice_flow_uid: str | None
    row_instance: str | None
    row_lock: str | None
    row_owner: str | None
    row_seq: int | None
    row_guid: str | None
    row_version: int | None
    is_active: int | None
    created_date: datetime.datetime | None
    created_by: str | None
    last_updated_date: datetime.datetime | None
    last_updated_by: str | None
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str | None
    invoice_flow_uid_invoice_flow_name: str | None
    invoice_flow_uid_flow_description: str | None
    invoice_flow_uid_flow_definition_json: str | None
    def __init__(self, invoice_flow_state_uid: str | None, invoice_flow_state_name: str | None, invoice_flow_uid: str | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None, invoice_flow_uid_invoice_flow_name: str | None, invoice_flow_uid_flow_description: str | None, invoice_flow_uid_flow_definition_json: str | None):
        self.invoice_flow_state_uid = invoice_flow_state_uid
        self.invoice_flow_state_name = invoice_flow_state_name
        self.invoice_flow_uid = invoice_flow_uid
        self.row_instance = row_instance
        self.row_lock = row_lock
        self.row_owner = row_owner
        self.row_seq = row_seq
        self.row_guid = row_guid
        self.row_version = row_version
        self.is_active = is_active
        self.created_date = created_date
        self.created_by = created_by
        self.last_updated_date = last_updated_date
        self.last_updated_by = last_updated_by
        self.removed_date = removed_date
        self.removed_by = removed_by
        self.custom_attributes = custom_attributes
        self.invoice_flow_uid_invoice_flow_name = invoice_flow_uid_invoice_flow_name
        self.invoice_flow_uid_flow_description = invoice_flow_uid_flow_description
        self.invoice_flow_uid_flow_definition_json = invoice_flow_uid_flow_definition_json
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.invoice_flow_state_uid, self.invoice_flow_state_name, self.invoice_flow_uid, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes, self.invoice_flow_uid_invoice_flow_name, self.invoice_flow_uid_flow_description, self.invoice_flow_uid_flow_definition_json]


@dataclass(frozen=False)
class invoice_instance_rich_dto(invoice_instance_read_dto):
    invoice_instance_uid: str | None
    invoice_instance_name: str | None
    tenant_uid: str | None
    account_uid: str | None
    invoice_flow_uid: str | None
    invoice_status_uid: str | None
    invoice_category_uid: str | None
    invoice_type_uid: str | None
    period_uid: str | None
    currency_uid: str | None
    invoice_number: str | None
    invoice_details: str | None
    invoice_amount_net: str | None
    invoice_amount_tax: str | None
    invoice_amount_gross: str | None
    row_instance: str | None
    row_lock: str | None
    row_owner: str | None
    row_seq: int | None
    row_guid: str | None
    row_version: int | None
    is_active: int | None
    created_date: datetime.datetime | None
    created_by: str | None
    last_updated_date: datetime.datetime | None
    last_updated_by: str | None
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str | None
    tenant_uid_tenant_name: str | None
    tenant_uid_country_uid: str | None
    tenant_uid_tenant_type_uid: str | None
    tenant_uid_tenant_category_uid: str | None
    tenant_uid_tenant_code: str | None
    tenant_uid_tenant_description: str | None
    tenant_uid_start_date: datetime.datetime | None
    tenant_uid_end_date: datetime.datetime | None
    tenant_uid_is_internal: int | None
    tenant_uid_is_system: int | None
    tenant_uid_is_test: int | None
    tenant_uid_account_uid: str | None
    account_uid_account_name: str | None
    account_uid_tenant_uid: str | None
    account_uid_account_type_uid: str | None
    account_uid_account_title_uid: str | None
    account_uid_account_division_uid: str | None
    account_uid_account_group_uid: str | None
    account_uid_auth_identity_uid: str | None
    account_uid_account_email: str | None
    account_uid_display_name: str | None
    account_uid_is_system: int | None
    invoice_flow_uid_invoice_flow_name: str | None
    invoice_flow_uid_flow_description: str | None
    invoice_flow_uid_flow_definition_json: str | None
    invoice_status_uid_invoice_status_name: str | None
    invoice_status_uid_status_description: str | None
    invoice_category_uid_invoice_category_name: str | None
    invoice_category_uid_tenant_uid: str | None
    invoice_category_uid_invoice_category_description: str | None
    invoice_type_uid_invoice_type_name: str | None
    period_uid_period_name: str | None
    period_uid_period_number: int | None
    period_uid_period_type: str | None
    period_uid_period_start_time: datetime.datetime | None
    period_uid_period_end_time: datetime.datetime | None
    period_uid_period_year: int | None
    period_uid_period_quarter: int | None
    period_uid_period_month: int | None
    period_uid_period_week: int | None
    period_uid_period_day: int | None
    currency_uid_currency_name: str | None
    currency_uid_is_focused: int | None
    def __init__(self, invoice_instance_uid: str | None, invoice_instance_name: str | None, tenant_uid: str | None, account_uid: str | None, invoice_flow_uid: str | None, invoice_status_uid: str | None, invoice_category_uid: str | None, invoice_type_uid: str | None, period_uid: str | None, currency_uid: str | None, invoice_number: str | None, invoice_details: str | None, invoice_amount_net: str | None, invoice_amount_tax: str | None, invoice_amount_gross: str | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None, tenant_uid_tenant_name: str | None, tenant_uid_country_uid: str | None, tenant_uid_tenant_type_uid: str | None, tenant_uid_tenant_category_uid: str | None, tenant_uid_tenant_code: str | None, tenant_uid_tenant_description: str | None, tenant_uid_start_date: datetime.datetime | None, tenant_uid_end_date: datetime.datetime | None, tenant_uid_is_internal: int | None, tenant_uid_is_system: int | None, tenant_uid_is_test: int | None, tenant_uid_account_uid: str | None, account_uid_account_name: str | None, account_uid_tenant_uid: str | None, account_uid_account_type_uid: str | None, account_uid_account_title_uid: str | None, account_uid_account_division_uid: str | None, account_uid_account_group_uid: str | None, account_uid_auth_identity_uid: str | None, account_uid_account_email: str | None, account_uid_display_name: str | None, account_uid_is_system: int | None, invoice_flow_uid_invoice_flow_name: str | None, invoice_flow_uid_flow_description: str | None, invoice_flow_uid_flow_definition_json: str | None, invoice_status_uid_invoice_status_name: str | None, invoice_status_uid_status_description: str | None, invoice_category_uid_invoice_category_name: str | None, invoice_category_uid_tenant_uid: str | None, invoice_category_uid_invoice_category_description: str | None, invoice_type_uid_invoice_type_name: str | None, period_uid_period_name: str | None, period_uid_period_number: int | None, period_uid_period_type: str | None, period_uid_period_start_time: datetime.datetime | None, period_uid_period_end_time: datetime.datetime | None, period_uid_period_year: int | None, period_uid_period_quarter: int | None, period_uid_period_month: int | None, period_uid_period_week: int | None, period_uid_period_day: int | None, currency_uid_currency_name: str | None, currency_uid_is_focused: int | None):
        self.invoice_instance_uid = invoice_instance_uid
        self.invoice_instance_name = invoice_instance_name
        self.tenant_uid = tenant_uid
        self.account_uid = account_uid
        self.invoice_flow_uid = invoice_flow_uid
        self.invoice_status_uid = invoice_status_uid
        self.invoice_category_uid = invoice_category_uid
        self.invoice_type_uid = invoice_type_uid
        self.period_uid = period_uid
        self.currency_uid = currency_uid
        self.invoice_number = invoice_number
        self.invoice_details = invoice_details
        self.invoice_amount_net = invoice_amount_net
        self.invoice_amount_tax = invoice_amount_tax
        self.invoice_amount_gross = invoice_amount_gross
        self.row_instance = row_instance
        self.row_lock = row_lock
        self.row_owner = row_owner
        self.row_seq = row_seq
        self.row_guid = row_guid
        self.row_version = row_version
        self.is_active = is_active
        self.created_date = created_date
        self.created_by = created_by
        self.last_updated_date = last_updated_date
        self.last_updated_by = last_updated_by
        self.removed_date = removed_date
        self.removed_by = removed_by
        self.custom_attributes = custom_attributes
        self.tenant_uid_tenant_name = tenant_uid_tenant_name
        self.tenant_uid_country_uid = tenant_uid_country_uid
        self.tenant_uid_tenant_type_uid = tenant_uid_tenant_type_uid
        self.tenant_uid_tenant_category_uid = tenant_uid_tenant_category_uid
        self.tenant_uid_tenant_code = tenant_uid_tenant_code
        self.tenant_uid_tenant_description = tenant_uid_tenant_description
        self.tenant_uid_start_date = tenant_uid_start_date
        self.tenant_uid_end_date = tenant_uid_end_date
        self.tenant_uid_is_internal = tenant_uid_is_internal
        self.tenant_uid_is_system = tenant_uid_is_system
        self.tenant_uid_is_test = tenant_uid_is_test
        self.tenant_uid_account_uid = tenant_uid_account_uid
        self.account_uid_account_name = account_uid_account_name
        self.account_uid_tenant_uid = account_uid_tenant_uid
        self.account_uid_account_type_uid = account_uid_account_type_uid
        self.account_uid_account_title_uid = account_uid_account_title_uid
        self.account_uid_account_division_uid = account_uid_account_division_uid
        self.account_uid_account_group_uid = account_uid_account_group_uid
        self.account_uid_auth_identity_uid = account_uid_auth_identity_uid
        self.account_uid_account_email = account_uid_account_email
        self.account_uid_display_name = account_uid_display_name
        self.account_uid_is_system = account_uid_is_system
        self.invoice_flow_uid_invoice_flow_name = invoice_flow_uid_invoice_flow_name
        self.invoice_flow_uid_flow_description = invoice_flow_uid_flow_description
        self.invoice_flow_uid_flow_definition_json = invoice_flow_uid_flow_definition_json
        self.invoice_status_uid_invoice_status_name = invoice_status_uid_invoice_status_name
        self.invoice_status_uid_status_description = invoice_status_uid_status_description
        self.invoice_category_uid_invoice_category_name = invoice_category_uid_invoice_category_name
        self.invoice_category_uid_tenant_uid = invoice_category_uid_tenant_uid
        self.invoice_category_uid_invoice_category_description = invoice_category_uid_invoice_category_description
        self.invoice_type_uid_invoice_type_name = invoice_type_uid_invoice_type_name
        self.period_uid_period_name = period_uid_period_name
        self.period_uid_period_number = period_uid_period_number
        self.period_uid_period_type = period_uid_period_type
        self.period_uid_period_start_time = period_uid_period_start_time
        self.period_uid_period_end_time = period_uid_period_end_time
        self.period_uid_period_year = period_uid_period_year
        self.period_uid_period_quarter = period_uid_period_quarter
        self.period_uid_period_month = period_uid_period_month
        self.period_uid_period_week = period_uid_period_week
        self.period_uid_period_day = period_uid_period_day
        self.currency_uid_currency_name = currency_uid_currency_name
        self.currency_uid_is_focused = currency_uid_is_focused
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.invoice_instance_uid, self.invoice_instance_name, self.tenant_uid, self.account_uid, self.invoice_flow_uid, self.invoice_status_uid, self.invoice_category_uid, self.invoice_type_uid, self.period_uid, self.currency_uid, self.invoice_number, self.invoice_details, self.invoice_amount_net, self.invoice_amount_tax, self.invoice_amount_gross, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes, self.tenant_uid_tenant_name, self.tenant_uid_country_uid, self.tenant_uid_tenant_type_uid, self.tenant_uid_tenant_category_uid, self.tenant_uid_tenant_code, self.tenant_uid_tenant_description, self.tenant_uid_start_date, self.tenant_uid_end_date, self.tenant_uid_is_internal, self.tenant_uid_is_system, self.tenant_uid_is_test, self.tenant_uid_account_uid, self.account_uid_account_name, self.account_uid_tenant_uid, self.account_uid_account_type_uid, self.account_uid_account_title_uid, self.account_uid_account_division_uid, self.account_uid_account_group_uid, self.account_uid_auth_identity_uid, self.account_uid_account_email, self.account_uid_display_name, self.account_uid_is_system, self.invoice_flow_uid_invoice_flow_name, self.invoice_flow_uid_flow_description, self.invoice_flow_uid_flow_definition_json, self.invoice_status_uid_invoice_status_name, self.invoice_status_uid_status_description, self.invoice_category_uid_invoice_category_name, self.invoice_category_uid_tenant_uid, self.invoice_category_uid_invoice_category_description, self.invoice_type_uid_invoice_type_name, self.period_uid_period_name, self.period_uid_period_number, self.period_uid_period_type, self.period_uid_period_start_time, self.period_uid_period_end_time, self.period_uid_period_year, self.period_uid_period_quarter, self.period_uid_period_month, self.period_uid_period_week, self.period_uid_period_day, self.currency_uid_currency_name, self.currency_uid_is_focused]


@dataclass(frozen=False)
class invoice_status_rich_dto(invoice_status_read_dto):
    invoice_status_uid: str | None
    invoice_status_name: str | None
    status_description: str | None
    row_instance: str | None
    row_lock: str | None
    row_owner: str | None
    row_seq: int | None
    row_guid: str | None
    row_version: int | None
    is_active: int | None
    created_date: datetime.datetime | None
    created_by: str | None
    last_updated_date: datetime.datetime | None
    last_updated_by: str | None
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str | None
    def __init__(self, invoice_status_uid: str | None, invoice_status_name: str | None, status_description: str | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None):
        self.invoice_status_uid = invoice_status_uid
        self.invoice_status_name = invoice_status_name
        self.status_description = status_description
        self.row_instance = row_instance
        self.row_lock = row_lock
        self.row_owner = row_owner
        self.row_seq = row_seq
        self.row_guid = row_guid
        self.row_version = row_version
        self.is_active = is_active
        self.created_date = created_date
        self.created_by = created_by
        self.last_updated_date = last_updated_date
        self.last_updated_by = last_updated_by
        self.removed_date = removed_date
        self.removed_by = removed_by
        self.custom_attributes = custom_attributes
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.invoice_status_uid, self.invoice_status_name, self.status_description, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]


@dataclass(frozen=False)
class invoice_type_rich_dto(invoice_type_read_dto):
    invoice_type_uid: str | None
    invoice_type_name: str | None
    row_instance: str | None
    row_lock: str | None
    row_owner: str | None
    row_seq: int | None
    row_guid: str | None
    row_version: int | None
    is_active: int | None
    created_date: datetime.datetime | None
    created_by: str | None
    last_updated_date: datetime.datetime | None
    last_updated_by: str | None
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str | None
    def __init__(self, invoice_type_uid: str | None, invoice_type_name: str | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None):
        self.invoice_type_uid = invoice_type_uid
        self.invoice_type_name = invoice_type_name
        self.row_instance = row_instance
        self.row_lock = row_lock
        self.row_owner = row_owner
        self.row_seq = row_seq
        self.row_guid = row_guid
        self.row_version = row_version
        self.is_active = is_active
        self.created_date = created_date
        self.created_by = created_by
        self.last_updated_date = last_updated_date
        self.last_updated_by = last_updated_by
        self.removed_date = removed_date
        self.removed_by = removed_by
        self.custom_attributes = custom_attributes
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.invoice_type_uid, self.invoice_type_name, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]


@dataclass(frozen=False)
class monitor_rich_dto(monitor_read_dto):
    monitor_uid: str | None
    monitor_name: str | None
    tenant_uid: str | None
    account_uid: str | None
    monitor_type_uid: str | None
    schedule_expression: str | None
    monitor_protocol: str | None
    monitor_url: str | None
    monitor_user: str | None
    monitor_priority: int | None
    is_on_hold: int | None
    last_status_name: str | None
    last_run_time: str | None
    last_exception_message: str | None
    row_instance: str | None
    row_lock: str | None
    row_owner: str | None
    row_seq: int | None
    row_guid: str | None
    row_version: int | None
    is_active: int | None
    created_date: datetime.datetime | None
    created_by: str | None
    last_updated_date: datetime.datetime | None
    last_updated_by: str | None
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str | None
    tenant_uid_tenant_name: str | None
    tenant_uid_country_uid: str | None
    tenant_uid_tenant_type_uid: str | None
    tenant_uid_tenant_category_uid: str | None
    tenant_uid_tenant_code: str | None
    tenant_uid_tenant_description: str | None
    tenant_uid_start_date: datetime.datetime | None
    tenant_uid_end_date: datetime.datetime | None
    tenant_uid_is_internal: int | None
    tenant_uid_is_system: int | None
    tenant_uid_is_test: int | None
    tenant_uid_account_uid: str | None
    account_uid_account_name: str | None
    account_uid_tenant_uid: str | None
    account_uid_account_type_uid: str | None
    account_uid_account_title_uid: str | None
    account_uid_account_division_uid: str | None
    account_uid_account_group_uid: str | None
    account_uid_auth_identity_uid: str | None
    account_uid_account_email: str | None
    account_uid_display_name: str | None
    account_uid_is_system: int | None
    monitor_type_uid_monitor_type_name: str | None
    monitor_type_uid_class_name: str | None
    monitor_type_uid_parameters_json: str | None
    def __init__(self, monitor_uid: str | None, monitor_name: str | None, tenant_uid: str | None, account_uid: str | None, monitor_type_uid: str | None, schedule_expression: str | None, monitor_protocol: str | None, monitor_url: str | None, monitor_user: str | None, monitor_priority: int | None, is_on_hold: int | None, last_status_name: str | None, last_run_time: str | None, last_exception_message: str | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None, tenant_uid_tenant_name: str | None, tenant_uid_country_uid: str | None, tenant_uid_tenant_type_uid: str | None, tenant_uid_tenant_category_uid: str | None, tenant_uid_tenant_code: str | None, tenant_uid_tenant_description: str | None, tenant_uid_start_date: datetime.datetime | None, tenant_uid_end_date: datetime.datetime | None, tenant_uid_is_internal: int | None, tenant_uid_is_system: int | None, tenant_uid_is_test: int | None, tenant_uid_account_uid: str | None, account_uid_account_name: str | None, account_uid_tenant_uid: str | None, account_uid_account_type_uid: str | None, account_uid_account_title_uid: str | None, account_uid_account_division_uid: str | None, account_uid_account_group_uid: str | None, account_uid_auth_identity_uid: str | None, account_uid_account_email: str | None, account_uid_display_name: str | None, account_uid_is_system: int | None, monitor_type_uid_monitor_type_name: str | None, monitor_type_uid_class_name: str | None, monitor_type_uid_parameters_json: str | None):
        self.monitor_uid = monitor_uid
        self.monitor_name = monitor_name
        self.tenant_uid = tenant_uid
        self.account_uid = account_uid
        self.monitor_type_uid = monitor_type_uid
        self.schedule_expression = schedule_expression
        self.monitor_protocol = monitor_protocol
        self.monitor_url = monitor_url
        self.monitor_user = monitor_user
        self.monitor_priority = monitor_priority
        self.is_on_hold = is_on_hold
        self.last_status_name = last_status_name
        self.last_run_time = last_run_time
        self.last_exception_message = last_exception_message
        self.row_instance = row_instance
        self.row_lock = row_lock
        self.row_owner = row_owner
        self.row_seq = row_seq
        self.row_guid = row_guid
        self.row_version = row_version
        self.is_active = is_active
        self.created_date = created_date
        self.created_by = created_by
        self.last_updated_date = last_updated_date
        self.last_updated_by = last_updated_by
        self.removed_date = removed_date
        self.removed_by = removed_by
        self.custom_attributes = custom_attributes
        self.tenant_uid_tenant_name = tenant_uid_tenant_name
        self.tenant_uid_country_uid = tenant_uid_country_uid
        self.tenant_uid_tenant_type_uid = tenant_uid_tenant_type_uid
        self.tenant_uid_tenant_category_uid = tenant_uid_tenant_category_uid
        self.tenant_uid_tenant_code = tenant_uid_tenant_code
        self.tenant_uid_tenant_description = tenant_uid_tenant_description
        self.tenant_uid_start_date = tenant_uid_start_date
        self.tenant_uid_end_date = tenant_uid_end_date
        self.tenant_uid_is_internal = tenant_uid_is_internal
        self.tenant_uid_is_system = tenant_uid_is_system
        self.tenant_uid_is_test = tenant_uid_is_test
        self.tenant_uid_account_uid = tenant_uid_account_uid
        self.account_uid_account_name = account_uid_account_name
        self.account_uid_tenant_uid = account_uid_tenant_uid
        self.account_uid_account_type_uid = account_uid_account_type_uid
        self.account_uid_account_title_uid = account_uid_account_title_uid
        self.account_uid_account_division_uid = account_uid_account_division_uid
        self.account_uid_account_group_uid = account_uid_account_group_uid
        self.account_uid_auth_identity_uid = account_uid_auth_identity_uid
        self.account_uid_account_email = account_uid_account_email
        self.account_uid_display_name = account_uid_display_name
        self.account_uid_is_system = account_uid_is_system
        self.monitor_type_uid_monitor_type_name = monitor_type_uid_monitor_type_name
        self.monitor_type_uid_class_name = monitor_type_uid_class_name
        self.monitor_type_uid_parameters_json = monitor_type_uid_parameters_json
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.monitor_uid, self.monitor_name, self.tenant_uid, self.account_uid, self.monitor_type_uid, self.schedule_expression, self.monitor_protocol, self.monitor_url, self.monitor_user, self.monitor_priority, self.is_on_hold, self.last_status_name, self.last_run_time, self.last_exception_message, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes, self.tenant_uid_tenant_name, self.tenant_uid_country_uid, self.tenant_uid_tenant_type_uid, self.tenant_uid_tenant_category_uid, self.tenant_uid_tenant_code, self.tenant_uid_tenant_description, self.tenant_uid_start_date, self.tenant_uid_end_date, self.tenant_uid_is_internal, self.tenant_uid_is_system, self.tenant_uid_is_test, self.tenant_uid_account_uid, self.account_uid_account_name, self.account_uid_tenant_uid, self.account_uid_account_type_uid, self.account_uid_account_title_uid, self.account_uid_account_division_uid, self.account_uid_account_group_uid, self.account_uid_auth_identity_uid, self.account_uid_account_email, self.account_uid_display_name, self.account_uid_is_system, self.monitor_type_uid_monitor_type_name, self.monitor_type_uid_class_name, self.monitor_type_uid_parameters_json]


@dataclass(frozen=False)
class monitor_run_rich_dto(monitor_run_read_dto):
    monitor_run_uid: str | None
    monitor_run_name: str | None
    tenant_uid: str | None
    account_uid: str | None
    monitor_uid: str | None
    status_name: str | None
    run_time: str | None
    exception_message: str | None
    row_instance: str | None
    row_lock: str | None
    row_owner: str | None
    row_seq: int | None
    row_guid: str | None
    row_version: int | None
    is_active: int | None
    created_date: datetime.datetime | None
    created_by: str | None
    last_updated_date: datetime.datetime | None
    last_updated_by: str | None
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str | None
    tenant_uid_tenant_name: str | None
    tenant_uid_country_uid: str | None
    tenant_uid_tenant_type_uid: str | None
    tenant_uid_tenant_category_uid: str | None
    tenant_uid_tenant_code: str | None
    tenant_uid_tenant_description: str | None
    tenant_uid_start_date: datetime.datetime | None
    tenant_uid_end_date: datetime.datetime | None
    tenant_uid_is_internal: int | None
    tenant_uid_is_system: int | None
    tenant_uid_is_test: int | None
    tenant_uid_account_uid: str | None
    account_uid_account_name: str | None
    account_uid_tenant_uid: str | None
    account_uid_account_type_uid: str | None
    account_uid_account_title_uid: str | None
    account_uid_account_division_uid: str | None
    account_uid_account_group_uid: str | None
    account_uid_auth_identity_uid: str | None
    account_uid_account_email: str | None
    account_uid_display_name: str | None
    account_uid_is_system: int | None
    monitor_uid_monitor_name: str | None
    monitor_uid_tenant_uid: str | None
    monitor_uid_account_uid: str | None
    monitor_uid_monitor_type_uid: str | None
    monitor_uid_schedule_expression: str | None
    monitor_uid_monitor_protocol: str | None
    monitor_uid_monitor_url: str | None
    monitor_uid_monitor_user: str | None
    monitor_uid_monitor_priority: int | None
    monitor_uid_is_on_hold: int | None
    monitor_uid_last_status_name: str | None
    monitor_uid_last_run_time: str | None
    monitor_uid_last_exception_message: str | None
    def __init__(self, monitor_run_uid: str | None, monitor_run_name: str | None, tenant_uid: str | None, account_uid: str | None, monitor_uid: str | None, status_name: str | None, run_time: str | None, exception_message: str | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None, tenant_uid_tenant_name: str | None, tenant_uid_country_uid: str | None, tenant_uid_tenant_type_uid: str | None, tenant_uid_tenant_category_uid: str | None, tenant_uid_tenant_code: str | None, tenant_uid_tenant_description: str | None, tenant_uid_start_date: datetime.datetime | None, tenant_uid_end_date: datetime.datetime | None, tenant_uid_is_internal: int | None, tenant_uid_is_system: int | None, tenant_uid_is_test: int | None, tenant_uid_account_uid: str | None, account_uid_account_name: str | None, account_uid_tenant_uid: str | None, account_uid_account_type_uid: str | None, account_uid_account_title_uid: str | None, account_uid_account_division_uid: str | None, account_uid_account_group_uid: str | None, account_uid_auth_identity_uid: str | None, account_uid_account_email: str | None, account_uid_display_name: str | None, account_uid_is_system: int | None, monitor_uid_monitor_name: str | None, monitor_uid_tenant_uid: str | None, monitor_uid_account_uid: str | None, monitor_uid_monitor_type_uid: str | None, monitor_uid_schedule_expression: str | None, monitor_uid_monitor_protocol: str | None, monitor_uid_monitor_url: str | None, monitor_uid_monitor_user: str | None, monitor_uid_monitor_priority: int | None, monitor_uid_is_on_hold: int | None, monitor_uid_last_status_name: str | None, monitor_uid_last_run_time: str | None, monitor_uid_last_exception_message: str | None):
        self.monitor_run_uid = monitor_run_uid
        self.monitor_run_name = monitor_run_name
        self.tenant_uid = tenant_uid
        self.account_uid = account_uid
        self.monitor_uid = monitor_uid
        self.status_name = status_name
        self.run_time = run_time
        self.exception_message = exception_message
        self.row_instance = row_instance
        self.row_lock = row_lock
        self.row_owner = row_owner
        self.row_seq = row_seq
        self.row_guid = row_guid
        self.row_version = row_version
        self.is_active = is_active
        self.created_date = created_date
        self.created_by = created_by
        self.last_updated_date = last_updated_date
        self.last_updated_by = last_updated_by
        self.removed_date = removed_date
        self.removed_by = removed_by
        self.custom_attributes = custom_attributes
        self.tenant_uid_tenant_name = tenant_uid_tenant_name
        self.tenant_uid_country_uid = tenant_uid_country_uid
        self.tenant_uid_tenant_type_uid = tenant_uid_tenant_type_uid
        self.tenant_uid_tenant_category_uid = tenant_uid_tenant_category_uid
        self.tenant_uid_tenant_code = tenant_uid_tenant_code
        self.tenant_uid_tenant_description = tenant_uid_tenant_description
        self.tenant_uid_start_date = tenant_uid_start_date
        self.tenant_uid_end_date = tenant_uid_end_date
        self.tenant_uid_is_internal = tenant_uid_is_internal
        self.tenant_uid_is_system = tenant_uid_is_system
        self.tenant_uid_is_test = tenant_uid_is_test
        self.tenant_uid_account_uid = tenant_uid_account_uid
        self.account_uid_account_name = account_uid_account_name
        self.account_uid_tenant_uid = account_uid_tenant_uid
        self.account_uid_account_type_uid = account_uid_account_type_uid
        self.account_uid_account_title_uid = account_uid_account_title_uid
        self.account_uid_account_division_uid = account_uid_account_division_uid
        self.account_uid_account_group_uid = account_uid_account_group_uid
        self.account_uid_auth_identity_uid = account_uid_auth_identity_uid
        self.account_uid_account_email = account_uid_account_email
        self.account_uid_display_name = account_uid_display_name
        self.account_uid_is_system = account_uid_is_system
        self.monitor_uid_monitor_name = monitor_uid_monitor_name
        self.monitor_uid_tenant_uid = monitor_uid_tenant_uid
        self.monitor_uid_account_uid = monitor_uid_account_uid
        self.monitor_uid_monitor_type_uid = monitor_uid_monitor_type_uid
        self.monitor_uid_schedule_expression = monitor_uid_schedule_expression
        self.monitor_uid_monitor_protocol = monitor_uid_monitor_protocol
        self.monitor_uid_monitor_url = monitor_uid_monitor_url
        self.monitor_uid_monitor_user = monitor_uid_monitor_user
        self.monitor_uid_monitor_priority = monitor_uid_monitor_priority
        self.monitor_uid_is_on_hold = monitor_uid_is_on_hold
        self.monitor_uid_last_status_name = monitor_uid_last_status_name
        self.monitor_uid_last_run_time = monitor_uid_last_run_time
        self.monitor_uid_last_exception_message = monitor_uid_last_exception_message
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.monitor_run_uid, self.monitor_run_name, self.tenant_uid, self.account_uid, self.monitor_uid, self.status_name, self.run_time, self.exception_message, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes, self.tenant_uid_tenant_name, self.tenant_uid_country_uid, self.tenant_uid_tenant_type_uid, self.tenant_uid_tenant_category_uid, self.tenant_uid_tenant_code, self.tenant_uid_tenant_description, self.tenant_uid_start_date, self.tenant_uid_end_date, self.tenant_uid_is_internal, self.tenant_uid_is_system, self.tenant_uid_is_test, self.tenant_uid_account_uid, self.account_uid_account_name, self.account_uid_tenant_uid, self.account_uid_account_type_uid, self.account_uid_account_title_uid, self.account_uid_account_division_uid, self.account_uid_account_group_uid, self.account_uid_auth_identity_uid, self.account_uid_account_email, self.account_uid_display_name, self.account_uid_is_system, self.monitor_uid_monitor_name, self.monitor_uid_tenant_uid, self.monitor_uid_account_uid, self.monitor_uid_monitor_type_uid, self.monitor_uid_schedule_expression, self.monitor_uid_monitor_protocol, self.monitor_uid_monitor_url, self.monitor_uid_monitor_user, self.monitor_uid_monitor_priority, self.monitor_uid_is_on_hold, self.monitor_uid_last_status_name, self.monitor_uid_last_run_time, self.monitor_uid_last_exception_message]


@dataclass(frozen=False)
class monitor_type_rich_dto(monitor_type_read_dto):
    monitor_type_uid: str | None
    monitor_type_name: str | None
    class_name: str | None
    parameters_json: str | None
    row_instance: str | None
    row_lock: str | None
    row_owner: str | None
    row_seq: int | None
    row_guid: str | None
    row_version: int | None
    is_active: int | None
    created_date: datetime.datetime | None
    created_by: str | None
    last_updated_date: datetime.datetime | None
    last_updated_by: str | None
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str | None
    def __init__(self, monitor_type_uid: str | None, monitor_type_name: str | None, class_name: str | None, parameters_json: str | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None):
        self.monitor_type_uid = monitor_type_uid
        self.monitor_type_name = monitor_type_name
        self.class_name = class_name
        self.parameters_json = parameters_json
        self.row_instance = row_instance
        self.row_lock = row_lock
        self.row_owner = row_owner
        self.row_seq = row_seq
        self.row_guid = row_guid
        self.row_version = row_version
        self.is_active = is_active
        self.created_date = created_date
        self.created_by = created_by
        self.last_updated_date = last_updated_date
        self.last_updated_by = last_updated_by
        self.removed_date = removed_date
        self.removed_by = removed_by
        self.custom_attributes = custom_attributes
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.monitor_type_uid, self.monitor_type_name, self.class_name, self.parameters_json, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]


@dataclass(frozen=False)
class period_rich_dto(period_read_dto):
    period_uid: str | None
    period_name: str | None
    period_number: int | None
    period_type: str | None
    period_start_time: datetime.datetime | None
    period_end_time: datetime.datetime | None
    period_year: int | None
    period_quarter: int | None
    period_month: int | None
    period_week: int | None
    period_day: int | None
    row_instance: str | None
    row_lock: str | None
    row_owner: str | None
    row_seq: int | None
    row_guid: str | None
    row_version: int | None
    is_active: int | None
    created_date: datetime.datetime | None
    created_by: str | None
    last_updated_date: datetime.datetime | None
    last_updated_by: str | None
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str | None
    def __init__(self, period_uid: str | None, period_name: str | None, period_number: int | None, period_type: str | None, period_start_time: datetime.datetime | None, period_end_time: datetime.datetime | None, period_year: int | None, period_quarter: int | None, period_month: int | None, period_week: int | None, period_day: int | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None):
        self.period_uid = period_uid
        self.period_name = period_name
        self.period_number = period_number
        self.period_type = period_type
        self.period_start_time = period_start_time
        self.period_end_time = period_end_time
        self.period_year = period_year
        self.period_quarter = period_quarter
        self.period_month = period_month
        self.period_week = period_week
        self.period_day = period_day
        self.row_instance = row_instance
        self.row_lock = row_lock
        self.row_owner = row_owner
        self.row_seq = row_seq
        self.row_guid = row_guid
        self.row_version = row_version
        self.is_active = is_active
        self.created_date = created_date
        self.created_by = created_by
        self.last_updated_date = last_updated_date
        self.last_updated_by = last_updated_by
        self.removed_date = removed_date
        self.removed_by = removed_by
        self.custom_attributes = custom_attributes
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.period_uid, self.period_name, self.period_number, self.period_type, self.period_start_time, self.period_end_time, self.period_year, self.period_quarter, self.period_month, self.period_week, self.period_day, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]


@dataclass(frozen=False)
class process_rich_dto(process_read_dto):
    process_uid: str | None
    process_name: str | None
    tenant_uid: str | None
    account_uid: str | None
    process_type_uid: str | None
    row_instance: str | None
    row_lock: str | None
    row_owner: str | None
    row_seq: int | None
    row_guid: str | None
    row_version: int | None
    is_active: int | None
    created_date: datetime.datetime | None
    created_by: str | None
    last_updated_date: datetime.datetime | None
    last_updated_by: str | None
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str | None
    tenant_uid_tenant_name: str | None
    tenant_uid_country_uid: str | None
    tenant_uid_tenant_type_uid: str | None
    tenant_uid_tenant_category_uid: str | None
    tenant_uid_tenant_code: str | None
    tenant_uid_tenant_description: str | None
    tenant_uid_start_date: datetime.datetime | None
    tenant_uid_end_date: datetime.datetime | None
    tenant_uid_is_internal: int | None
    tenant_uid_is_system: int | None
    tenant_uid_is_test: int | None
    tenant_uid_account_uid: str | None
    account_uid_account_name: str | None
    account_uid_tenant_uid: str | None
    account_uid_account_type_uid: str | None
    account_uid_account_title_uid: str | None
    account_uid_account_division_uid: str | None
    account_uid_account_group_uid: str | None
    account_uid_auth_identity_uid: str | None
    account_uid_account_email: str | None
    account_uid_display_name: str | None
    account_uid_is_system: int | None
    process_type_uid_process_type_name: str | None
    process_type_uid_class_name: str | None
    def __init__(self, process_uid: str | None, process_name: str | None, tenant_uid: str | None, account_uid: str | None, process_type_uid: str | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None, tenant_uid_tenant_name: str | None, tenant_uid_country_uid: str | None, tenant_uid_tenant_type_uid: str | None, tenant_uid_tenant_category_uid: str | None, tenant_uid_tenant_code: str | None, tenant_uid_tenant_description: str | None, tenant_uid_start_date: datetime.datetime | None, tenant_uid_end_date: datetime.datetime | None, tenant_uid_is_internal: int | None, tenant_uid_is_system: int | None, tenant_uid_is_test: int | None, tenant_uid_account_uid: str | None, account_uid_account_name: str | None, account_uid_tenant_uid: str | None, account_uid_account_type_uid: str | None, account_uid_account_title_uid: str | None, account_uid_account_division_uid: str | None, account_uid_account_group_uid: str | None, account_uid_auth_identity_uid: str | None, account_uid_account_email: str | None, account_uid_display_name: str | None, account_uid_is_system: int | None, process_type_uid_process_type_name: str | None, process_type_uid_class_name: str | None):
        self.process_uid = process_uid
        self.process_name = process_name
        self.tenant_uid = tenant_uid
        self.account_uid = account_uid
        self.process_type_uid = process_type_uid
        self.row_instance = row_instance
        self.row_lock = row_lock
        self.row_owner = row_owner
        self.row_seq = row_seq
        self.row_guid = row_guid
        self.row_version = row_version
        self.is_active = is_active
        self.created_date = created_date
        self.created_by = created_by
        self.last_updated_date = last_updated_date
        self.last_updated_by = last_updated_by
        self.removed_date = removed_date
        self.removed_by = removed_by
        self.custom_attributes = custom_attributes
        self.tenant_uid_tenant_name = tenant_uid_tenant_name
        self.tenant_uid_country_uid = tenant_uid_country_uid
        self.tenant_uid_tenant_type_uid = tenant_uid_tenant_type_uid
        self.tenant_uid_tenant_category_uid = tenant_uid_tenant_category_uid
        self.tenant_uid_tenant_code = tenant_uid_tenant_code
        self.tenant_uid_tenant_description = tenant_uid_tenant_description
        self.tenant_uid_start_date = tenant_uid_start_date
        self.tenant_uid_end_date = tenant_uid_end_date
        self.tenant_uid_is_internal = tenant_uid_is_internal
        self.tenant_uid_is_system = tenant_uid_is_system
        self.tenant_uid_is_test = tenant_uid_is_test
        self.tenant_uid_account_uid = tenant_uid_account_uid
        self.account_uid_account_name = account_uid_account_name
        self.account_uid_tenant_uid = account_uid_tenant_uid
        self.account_uid_account_type_uid = account_uid_account_type_uid
        self.account_uid_account_title_uid = account_uid_account_title_uid
        self.account_uid_account_division_uid = account_uid_account_division_uid
        self.account_uid_account_group_uid = account_uid_account_group_uid
        self.account_uid_auth_identity_uid = account_uid_auth_identity_uid
        self.account_uid_account_email = account_uid_account_email
        self.account_uid_display_name = account_uid_display_name
        self.account_uid_is_system = account_uid_is_system
        self.process_type_uid_process_type_name = process_type_uid_process_type_name
        self.process_type_uid_class_name = process_type_uid_class_name
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.process_uid, self.process_name, self.tenant_uid, self.account_uid, self.process_type_uid, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes, self.tenant_uid_tenant_name, self.tenant_uid_country_uid, self.tenant_uid_tenant_type_uid, self.tenant_uid_tenant_category_uid, self.tenant_uid_tenant_code, self.tenant_uid_tenant_description, self.tenant_uid_start_date, self.tenant_uid_end_date, self.tenant_uid_is_internal, self.tenant_uid_is_system, self.tenant_uid_is_test, self.tenant_uid_account_uid, self.account_uid_account_name, self.account_uid_tenant_uid, self.account_uid_account_type_uid, self.account_uid_account_title_uid, self.account_uid_account_division_uid, self.account_uid_account_group_uid, self.account_uid_auth_identity_uid, self.account_uid_account_email, self.account_uid_display_name, self.account_uid_is_system, self.process_type_uid_process_type_name, self.process_type_uid_class_name]


@dataclass(frozen=False)
class process_run_rich_dto(process_run_read_dto):
    process_run_uid: str | None
    process_run_name: str | None
    tenant_uid: str | None
    account_uid: str | None
    process_uid: str | None
    row_instance: str | None
    row_lock: str | None
    row_owner: str | None
    row_seq: int | None
    row_guid: str | None
    row_version: int | None
    is_active: int | None
    created_date: datetime.datetime | None
    created_by: str | None
    last_updated_date: datetime.datetime | None
    last_updated_by: str | None
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str | None
    tenant_uid_tenant_name: str | None
    tenant_uid_country_uid: str | None
    tenant_uid_tenant_type_uid: str | None
    tenant_uid_tenant_category_uid: str | None
    tenant_uid_tenant_code: str | None
    tenant_uid_tenant_description: str | None
    tenant_uid_start_date: datetime.datetime | None
    tenant_uid_end_date: datetime.datetime | None
    tenant_uid_is_internal: int | None
    tenant_uid_is_system: int | None
    tenant_uid_is_test: int | None
    tenant_uid_account_uid: str | None
    account_uid_account_name: str | None
    account_uid_tenant_uid: str | None
    account_uid_account_type_uid: str | None
    account_uid_account_title_uid: str | None
    account_uid_account_division_uid: str | None
    account_uid_account_group_uid: str | None
    account_uid_auth_identity_uid: str | None
    account_uid_account_email: str | None
    account_uid_display_name: str | None
    account_uid_is_system: int | None
    process_uid_process_name: str | None
    process_uid_tenant_uid: str | None
    process_uid_account_uid: str | None
    process_uid_process_type_uid: str | None
    def __init__(self, process_run_uid: str | None, process_run_name: str | None, tenant_uid: str | None, account_uid: str | None, process_uid: str | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None, tenant_uid_tenant_name: str | None, tenant_uid_country_uid: str | None, tenant_uid_tenant_type_uid: str | None, tenant_uid_tenant_category_uid: str | None, tenant_uid_tenant_code: str | None, tenant_uid_tenant_description: str | None, tenant_uid_start_date: datetime.datetime | None, tenant_uid_end_date: datetime.datetime | None, tenant_uid_is_internal: int | None, tenant_uid_is_system: int | None, tenant_uid_is_test: int | None, tenant_uid_account_uid: str | None, account_uid_account_name: str | None, account_uid_tenant_uid: str | None, account_uid_account_type_uid: str | None, account_uid_account_title_uid: str | None, account_uid_account_division_uid: str | None, account_uid_account_group_uid: str | None, account_uid_auth_identity_uid: str | None, account_uid_account_email: str | None, account_uid_display_name: str | None, account_uid_is_system: int | None, process_uid_process_name: str | None, process_uid_tenant_uid: str | None, process_uid_account_uid: str | None, process_uid_process_type_uid: str | None):
        self.process_run_uid = process_run_uid
        self.process_run_name = process_run_name
        self.tenant_uid = tenant_uid
        self.account_uid = account_uid
        self.process_uid = process_uid
        self.row_instance = row_instance
        self.row_lock = row_lock
        self.row_owner = row_owner
        self.row_seq = row_seq
        self.row_guid = row_guid
        self.row_version = row_version
        self.is_active = is_active
        self.created_date = created_date
        self.created_by = created_by
        self.last_updated_date = last_updated_date
        self.last_updated_by = last_updated_by
        self.removed_date = removed_date
        self.removed_by = removed_by
        self.custom_attributes = custom_attributes
        self.tenant_uid_tenant_name = tenant_uid_tenant_name
        self.tenant_uid_country_uid = tenant_uid_country_uid
        self.tenant_uid_tenant_type_uid = tenant_uid_tenant_type_uid
        self.tenant_uid_tenant_category_uid = tenant_uid_tenant_category_uid
        self.tenant_uid_tenant_code = tenant_uid_tenant_code
        self.tenant_uid_tenant_description = tenant_uid_tenant_description
        self.tenant_uid_start_date = tenant_uid_start_date
        self.tenant_uid_end_date = tenant_uid_end_date
        self.tenant_uid_is_internal = tenant_uid_is_internal
        self.tenant_uid_is_system = tenant_uid_is_system
        self.tenant_uid_is_test = tenant_uid_is_test
        self.tenant_uid_account_uid = tenant_uid_account_uid
        self.account_uid_account_name = account_uid_account_name
        self.account_uid_tenant_uid = account_uid_tenant_uid
        self.account_uid_account_type_uid = account_uid_account_type_uid
        self.account_uid_account_title_uid = account_uid_account_title_uid
        self.account_uid_account_division_uid = account_uid_account_division_uid
        self.account_uid_account_group_uid = account_uid_account_group_uid
        self.account_uid_auth_identity_uid = account_uid_auth_identity_uid
        self.account_uid_account_email = account_uid_account_email
        self.account_uid_display_name = account_uid_display_name
        self.account_uid_is_system = account_uid_is_system
        self.process_uid_process_name = process_uid_process_name
        self.process_uid_tenant_uid = process_uid_tenant_uid
        self.process_uid_account_uid = process_uid_account_uid
        self.process_uid_process_type_uid = process_uid_process_type_uid
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.process_run_uid, self.process_run_name, self.tenant_uid, self.account_uid, self.process_uid, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes, self.tenant_uid_tenant_name, self.tenant_uid_country_uid, self.tenant_uid_tenant_type_uid, self.tenant_uid_tenant_category_uid, self.tenant_uid_tenant_code, self.tenant_uid_tenant_description, self.tenant_uid_start_date, self.tenant_uid_end_date, self.tenant_uid_is_internal, self.tenant_uid_is_system, self.tenant_uid_is_test, self.tenant_uid_account_uid, self.account_uid_account_name, self.account_uid_tenant_uid, self.account_uid_account_type_uid, self.account_uid_account_title_uid, self.account_uid_account_division_uid, self.account_uid_account_group_uid, self.account_uid_auth_identity_uid, self.account_uid_account_email, self.account_uid_display_name, self.account_uid_is_system, self.process_uid_process_name, self.process_uid_tenant_uid, self.process_uid_account_uid, self.process_uid_process_type_uid]


@dataclass(frozen=False)
class process_type_rich_dto(process_type_read_dto):
    process_type_uid: str | None
    process_type_name: str | None
    class_name: str | None
    row_instance: str | None
    row_lock: str | None
    row_owner: str | None
    row_seq: int | None
    row_guid: str | None
    row_version: int | None
    is_active: int | None
    created_date: datetime.datetime | None
    created_by: str | None
    last_updated_date: datetime.datetime | None
    last_updated_by: str | None
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str | None
    def __init__(self, process_type_uid: str | None, process_type_name: str | None, class_name: str | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None):
        self.process_type_uid = process_type_uid
        self.process_type_name = process_type_name
        self.class_name = class_name
        self.row_instance = row_instance
        self.row_lock = row_lock
        self.row_owner = row_owner
        self.row_seq = row_seq
        self.row_guid = row_guid
        self.row_version = row_version
        self.is_active = is_active
        self.created_date = created_date
        self.created_by = created_by
        self.last_updated_date = last_updated_date
        self.last_updated_by = last_updated_by
        self.removed_date = removed_date
        self.removed_by = removed_by
        self.custom_attributes = custom_attributes
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.process_type_uid, self.process_type_name, self.class_name, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]


@dataclass(frozen=False)
class project_account_rich_dto(project_account_read_dto):
    project_account_uid: str | None
    project_account_name: str | None
    tenant_uid: str | None
    client_uid: str | None
    account_uid: str | None
    project_instance_uid: str | None
    start_date: datetime.datetime | None
    end_date: datetime.datetime | None
    row_instance: str | None
    row_lock: str | None
    row_owner: str | None
    row_seq: int | None
    row_guid: str | None
    row_version: int | None
    is_active: int | None
    created_date: datetime.datetime | None
    created_by: str | None
    last_updated_date: datetime.datetime | None
    last_updated_by: str | None
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str | None
    project_account_uid_account_name: str | None
    project_account_uid_tenant_uid: str | None
    project_account_uid_account_type_uid: str | None
    project_account_uid_account_title_uid: str | None
    project_account_uid_account_division_uid: str | None
    project_account_uid_account_group_uid: str | None
    project_account_uid_auth_identity_uid: str | None
    project_account_uid_account_email: str | None
    project_account_uid_display_name: str | None
    project_account_uid_is_system: int | None
    tenant_uid_tenant_name: str | None
    tenant_uid_country_uid: str | None
    tenant_uid_tenant_type_uid: str | None
    tenant_uid_tenant_category_uid: str | None
    tenant_uid_tenant_code: str | None
    tenant_uid_tenant_description: str | None
    tenant_uid_start_date: datetime.datetime | None
    tenant_uid_end_date: datetime.datetime | None
    tenant_uid_is_internal: int | None
    tenant_uid_is_system: int | None
    tenant_uid_is_test: int | None
    tenant_uid_account_uid: str | None
    client_uid_client_name: str | None
    client_uid_tenant_uid: str | None
    client_uid_country_uid: str | None
    client_uid_client_type_uid: str | None
    client_uid_client_category_uid: str | None
    client_uid_account_uid: str | None
    client_uid_client_code: str | None
    client_uid_client_description: str | None
    client_uid_start_date: datetime.datetime | None
    client_uid_end_date: datetime.datetime | None
    client_uid_is_internal: int | None
    client_uid_is_system: int | None
    client_uid_is_test: int | None
    account_uid_account_name: str | None
    account_uid_tenant_uid: str | None
    account_uid_account_type_uid: str | None
    account_uid_account_title_uid: str | None
    account_uid_account_division_uid: str | None
    account_uid_account_group_uid: str | None
    account_uid_auth_identity_uid: str | None
    account_uid_account_email: str | None
    account_uid_display_name: str | None
    account_uid_is_system: int | None
    project_instance_uid_project_instance_name: str | None
    project_instance_uid_tenant_uid: str | None
    project_instance_uid_client_uid: str | None
    project_instance_uid_project_type_uid: str | None
    project_instance_uid_manager_account_uid: str | None
    project_instance_uid_project_group_uid: str | None
    project_instance_uid_project_code: str | None
    project_instance_uid_project_description: str | None
    project_instance_uid_is_billable: int | None
    project_instance_uid_start_date: datetime.datetime | None
    project_instance_uid_end_date: datetime.datetime | None
    project_instance_uid_current_billed: str | None
    project_instance_uid_budget: str | None
    def __init__(self, project_account_uid: str | None, project_account_name: str | None, tenant_uid: str | None, client_uid: str | None, account_uid: str | None, project_instance_uid: str | None, start_date: datetime.datetime | None, end_date: datetime.datetime | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None, project_account_uid_account_name: str | None, project_account_uid_tenant_uid: str | None, project_account_uid_account_type_uid: str | None, project_account_uid_account_title_uid: str | None, project_account_uid_account_division_uid: str | None, project_account_uid_account_group_uid: str | None, project_account_uid_auth_identity_uid: str | None, project_account_uid_account_email: str | None, project_account_uid_display_name: str | None, project_account_uid_is_system: int | None, tenant_uid_tenant_name: str | None, tenant_uid_country_uid: str | None, tenant_uid_tenant_type_uid: str | None, tenant_uid_tenant_category_uid: str | None, tenant_uid_tenant_code: str | None, tenant_uid_tenant_description: str | None, tenant_uid_start_date: datetime.datetime | None, tenant_uid_end_date: datetime.datetime | None, tenant_uid_is_internal: int | None, tenant_uid_is_system: int | None, tenant_uid_is_test: int | None, tenant_uid_account_uid: str | None, client_uid_client_name: str | None, client_uid_tenant_uid: str | None, client_uid_country_uid: str | None, client_uid_client_type_uid: str | None, client_uid_client_category_uid: str | None, client_uid_account_uid: str | None, client_uid_client_code: str | None, client_uid_client_description: str | None, client_uid_start_date: datetime.datetime | None, client_uid_end_date: datetime.datetime | None, client_uid_is_internal: int | None, client_uid_is_system: int | None, client_uid_is_test: int | None, account_uid_account_name: str | None, account_uid_tenant_uid: str | None, account_uid_account_type_uid: str | None, account_uid_account_title_uid: str | None, account_uid_account_division_uid: str | None, account_uid_account_group_uid: str | None, account_uid_auth_identity_uid: str | None, account_uid_account_email: str | None, account_uid_display_name: str | None, account_uid_is_system: int | None, project_instance_uid_project_instance_name: str | None, project_instance_uid_tenant_uid: str | None, project_instance_uid_client_uid: str | None, project_instance_uid_project_type_uid: str | None, project_instance_uid_manager_account_uid: str | None, project_instance_uid_project_group_uid: str | None, project_instance_uid_project_code: str | None, project_instance_uid_project_description: str | None, project_instance_uid_is_billable: int | None, project_instance_uid_start_date: datetime.datetime | None, project_instance_uid_end_date: datetime.datetime | None, project_instance_uid_current_billed: str | None, project_instance_uid_budget: str | None):
        self.project_account_uid = project_account_uid
        self.project_account_name = project_account_name
        self.tenant_uid = tenant_uid
        self.client_uid = client_uid
        self.account_uid = account_uid
        self.project_instance_uid = project_instance_uid
        self.start_date = start_date
        self.end_date = end_date
        self.row_instance = row_instance
        self.row_lock = row_lock
        self.row_owner = row_owner
        self.row_seq = row_seq
        self.row_guid = row_guid
        self.row_version = row_version
        self.is_active = is_active
        self.created_date = created_date
        self.created_by = created_by
        self.last_updated_date = last_updated_date
        self.last_updated_by = last_updated_by
        self.removed_date = removed_date
        self.removed_by = removed_by
        self.custom_attributes = custom_attributes
        self.project_account_uid_account_name = project_account_uid_account_name
        self.project_account_uid_tenant_uid = project_account_uid_tenant_uid
        self.project_account_uid_account_type_uid = project_account_uid_account_type_uid
        self.project_account_uid_account_title_uid = project_account_uid_account_title_uid
        self.project_account_uid_account_division_uid = project_account_uid_account_division_uid
        self.project_account_uid_account_group_uid = project_account_uid_account_group_uid
        self.project_account_uid_auth_identity_uid = project_account_uid_auth_identity_uid
        self.project_account_uid_account_email = project_account_uid_account_email
        self.project_account_uid_display_name = project_account_uid_display_name
        self.project_account_uid_is_system = project_account_uid_is_system
        self.tenant_uid_tenant_name = tenant_uid_tenant_name
        self.tenant_uid_country_uid = tenant_uid_country_uid
        self.tenant_uid_tenant_type_uid = tenant_uid_tenant_type_uid
        self.tenant_uid_tenant_category_uid = tenant_uid_tenant_category_uid
        self.tenant_uid_tenant_code = tenant_uid_tenant_code
        self.tenant_uid_tenant_description = tenant_uid_tenant_description
        self.tenant_uid_start_date = tenant_uid_start_date
        self.tenant_uid_end_date = tenant_uid_end_date
        self.tenant_uid_is_internal = tenant_uid_is_internal
        self.tenant_uid_is_system = tenant_uid_is_system
        self.tenant_uid_is_test = tenant_uid_is_test
        self.tenant_uid_account_uid = tenant_uid_account_uid
        self.client_uid_client_name = client_uid_client_name
        self.client_uid_tenant_uid = client_uid_tenant_uid
        self.client_uid_country_uid = client_uid_country_uid
        self.client_uid_client_type_uid = client_uid_client_type_uid
        self.client_uid_client_category_uid = client_uid_client_category_uid
        self.client_uid_account_uid = client_uid_account_uid
        self.client_uid_client_code = client_uid_client_code
        self.client_uid_client_description = client_uid_client_description
        self.client_uid_start_date = client_uid_start_date
        self.client_uid_end_date = client_uid_end_date
        self.client_uid_is_internal = client_uid_is_internal
        self.client_uid_is_system = client_uid_is_system
        self.client_uid_is_test = client_uid_is_test
        self.account_uid_account_name = account_uid_account_name
        self.account_uid_tenant_uid = account_uid_tenant_uid
        self.account_uid_account_type_uid = account_uid_account_type_uid
        self.account_uid_account_title_uid = account_uid_account_title_uid
        self.account_uid_account_division_uid = account_uid_account_division_uid
        self.account_uid_account_group_uid = account_uid_account_group_uid
        self.account_uid_auth_identity_uid = account_uid_auth_identity_uid
        self.account_uid_account_email = account_uid_account_email
        self.account_uid_display_name = account_uid_display_name
        self.account_uid_is_system = account_uid_is_system
        self.project_instance_uid_project_instance_name = project_instance_uid_project_instance_name
        self.project_instance_uid_tenant_uid = project_instance_uid_tenant_uid
        self.project_instance_uid_client_uid = project_instance_uid_client_uid
        self.project_instance_uid_project_type_uid = project_instance_uid_project_type_uid
        self.project_instance_uid_manager_account_uid = project_instance_uid_manager_account_uid
        self.project_instance_uid_project_group_uid = project_instance_uid_project_group_uid
        self.project_instance_uid_project_code = project_instance_uid_project_code
        self.project_instance_uid_project_description = project_instance_uid_project_description
        self.project_instance_uid_is_billable = project_instance_uid_is_billable
        self.project_instance_uid_start_date = project_instance_uid_start_date
        self.project_instance_uid_end_date = project_instance_uid_end_date
        self.project_instance_uid_current_billed = project_instance_uid_current_billed
        self.project_instance_uid_budget = project_instance_uid_budget
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.project_account_uid, self.project_account_name, self.tenant_uid, self.client_uid, self.account_uid, self.project_instance_uid, self.start_date, self.end_date, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes, self.project_account_uid_account_name, self.project_account_uid_tenant_uid, self.project_account_uid_account_type_uid, self.project_account_uid_account_title_uid, self.project_account_uid_account_division_uid, self.project_account_uid_account_group_uid, self.project_account_uid_auth_identity_uid, self.project_account_uid_account_email, self.project_account_uid_display_name, self.project_account_uid_is_system, self.tenant_uid_tenant_name, self.tenant_uid_country_uid, self.tenant_uid_tenant_type_uid, self.tenant_uid_tenant_category_uid, self.tenant_uid_tenant_code, self.tenant_uid_tenant_description, self.tenant_uid_start_date, self.tenant_uid_end_date, self.tenant_uid_is_internal, self.tenant_uid_is_system, self.tenant_uid_is_test, self.tenant_uid_account_uid, self.client_uid_client_name, self.client_uid_tenant_uid, self.client_uid_country_uid, self.client_uid_client_type_uid, self.client_uid_client_category_uid, self.client_uid_account_uid, self.client_uid_client_code, self.client_uid_client_description, self.client_uid_start_date, self.client_uid_end_date, self.client_uid_is_internal, self.client_uid_is_system, self.client_uid_is_test, self.account_uid_account_name, self.account_uid_tenant_uid, self.account_uid_account_type_uid, self.account_uid_account_title_uid, self.account_uid_account_division_uid, self.account_uid_account_group_uid, self.account_uid_auth_identity_uid, self.account_uid_account_email, self.account_uid_display_name, self.account_uid_is_system, self.project_instance_uid_project_instance_name, self.project_instance_uid_tenant_uid, self.project_instance_uid_client_uid, self.project_instance_uid_project_type_uid, self.project_instance_uid_manager_account_uid, self.project_instance_uid_project_group_uid, self.project_instance_uid_project_code, self.project_instance_uid_project_description, self.project_instance_uid_is_billable, self.project_instance_uid_start_date, self.project_instance_uid_end_date, self.project_instance_uid_current_billed, self.project_instance_uid_budget]


@dataclass(frozen=False)
class project_budget_rich_dto(project_budget_read_dto):
    project_budget_uid: str | None
    project_budget_name: str | None
    tenant_uid: str | None
    client_uid: str | None
    project_instance_uid: str | None
    currency_uid: str | None
    budget_value: str | None
    is_approved: int | None
    is_current: int | None
    row_instance: str | None
    row_lock: str | None
    row_owner: str | None
    row_seq: int | None
    row_guid: str | None
    row_version: int | None
    is_active: int | None
    created_date: datetime.datetime | None
    created_by: str | None
    last_updated_date: datetime.datetime | None
    last_updated_by: str | None
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str | None
    tenant_uid_tenant_name: str | None
    tenant_uid_country_uid: str | None
    tenant_uid_tenant_type_uid: str | None
    tenant_uid_tenant_category_uid: str | None
    tenant_uid_tenant_code: str | None
    tenant_uid_tenant_description: str | None
    tenant_uid_start_date: datetime.datetime | None
    tenant_uid_end_date: datetime.datetime | None
    tenant_uid_is_internal: int | None
    tenant_uid_is_system: int | None
    tenant_uid_is_test: int | None
    tenant_uid_account_uid: str | None
    client_uid_client_name: str | None
    client_uid_tenant_uid: str | None
    client_uid_country_uid: str | None
    client_uid_client_type_uid: str | None
    client_uid_client_category_uid: str | None
    client_uid_account_uid: str | None
    client_uid_client_code: str | None
    client_uid_client_description: str | None
    client_uid_start_date: datetime.datetime | None
    client_uid_end_date: datetime.datetime | None
    client_uid_is_internal: int | None
    client_uid_is_system: int | None
    client_uid_is_test: int | None
    project_instance_uid_project_instance_name: str | None
    project_instance_uid_tenant_uid: str | None
    project_instance_uid_client_uid: str | None
    project_instance_uid_project_type_uid: str | None
    project_instance_uid_manager_account_uid: str | None
    project_instance_uid_project_group_uid: str | None
    project_instance_uid_project_code: str | None
    project_instance_uid_project_description: str | None
    project_instance_uid_is_billable: int | None
    project_instance_uid_start_date: datetime.datetime | None
    project_instance_uid_end_date: datetime.datetime | None
    project_instance_uid_current_billed: str | None
    project_instance_uid_budget: str | None
    currency_uid_currency_name: str | None
    currency_uid_is_focused: int | None
    def __init__(self, project_budget_uid: str | None, project_budget_name: str | None, tenant_uid: str | None, client_uid: str | None, project_instance_uid: str | None, currency_uid: str | None, budget_value: str | None, is_approved: int | None, is_current: int | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None, tenant_uid_tenant_name: str | None, tenant_uid_country_uid: str | None, tenant_uid_tenant_type_uid: str | None, tenant_uid_tenant_category_uid: str | None, tenant_uid_tenant_code: str | None, tenant_uid_tenant_description: str | None, tenant_uid_start_date: datetime.datetime | None, tenant_uid_end_date: datetime.datetime | None, tenant_uid_is_internal: int | None, tenant_uid_is_system: int | None, tenant_uid_is_test: int | None, tenant_uid_account_uid: str | None, client_uid_client_name: str | None, client_uid_tenant_uid: str | None, client_uid_country_uid: str | None, client_uid_client_type_uid: str | None, client_uid_client_category_uid: str | None, client_uid_account_uid: str | None, client_uid_client_code: str | None, client_uid_client_description: str | None, client_uid_start_date: datetime.datetime | None, client_uid_end_date: datetime.datetime | None, client_uid_is_internal: int | None, client_uid_is_system: int | None, client_uid_is_test: int | None, project_instance_uid_project_instance_name: str | None, project_instance_uid_tenant_uid: str | None, project_instance_uid_client_uid: str | None, project_instance_uid_project_type_uid: str | None, project_instance_uid_manager_account_uid: str | None, project_instance_uid_project_group_uid: str | None, project_instance_uid_project_code: str | None, project_instance_uid_project_description: str | None, project_instance_uid_is_billable: int | None, project_instance_uid_start_date: datetime.datetime | None, project_instance_uid_end_date: datetime.datetime | None, project_instance_uid_current_billed: str | None, project_instance_uid_budget: str | None, currency_uid_currency_name: str | None, currency_uid_is_focused: int | None):
        self.project_budget_uid = project_budget_uid
        self.project_budget_name = project_budget_name
        self.tenant_uid = tenant_uid
        self.client_uid = client_uid
        self.project_instance_uid = project_instance_uid
        self.currency_uid = currency_uid
        self.budget_value = budget_value
        self.is_approved = is_approved
        self.is_current = is_current
        self.row_instance = row_instance
        self.row_lock = row_lock
        self.row_owner = row_owner
        self.row_seq = row_seq
        self.row_guid = row_guid
        self.row_version = row_version
        self.is_active = is_active
        self.created_date = created_date
        self.created_by = created_by
        self.last_updated_date = last_updated_date
        self.last_updated_by = last_updated_by
        self.removed_date = removed_date
        self.removed_by = removed_by
        self.custom_attributes = custom_attributes
        self.tenant_uid_tenant_name = tenant_uid_tenant_name
        self.tenant_uid_country_uid = tenant_uid_country_uid
        self.tenant_uid_tenant_type_uid = tenant_uid_tenant_type_uid
        self.tenant_uid_tenant_category_uid = tenant_uid_tenant_category_uid
        self.tenant_uid_tenant_code = tenant_uid_tenant_code
        self.tenant_uid_tenant_description = tenant_uid_tenant_description
        self.tenant_uid_start_date = tenant_uid_start_date
        self.tenant_uid_end_date = tenant_uid_end_date
        self.tenant_uid_is_internal = tenant_uid_is_internal
        self.tenant_uid_is_system = tenant_uid_is_system
        self.tenant_uid_is_test = tenant_uid_is_test
        self.tenant_uid_account_uid = tenant_uid_account_uid
        self.client_uid_client_name = client_uid_client_name
        self.client_uid_tenant_uid = client_uid_tenant_uid
        self.client_uid_country_uid = client_uid_country_uid
        self.client_uid_client_type_uid = client_uid_client_type_uid
        self.client_uid_client_category_uid = client_uid_client_category_uid
        self.client_uid_account_uid = client_uid_account_uid
        self.client_uid_client_code = client_uid_client_code
        self.client_uid_client_description = client_uid_client_description
        self.client_uid_start_date = client_uid_start_date
        self.client_uid_end_date = client_uid_end_date
        self.client_uid_is_internal = client_uid_is_internal
        self.client_uid_is_system = client_uid_is_system
        self.client_uid_is_test = client_uid_is_test
        self.project_instance_uid_project_instance_name = project_instance_uid_project_instance_name
        self.project_instance_uid_tenant_uid = project_instance_uid_tenant_uid
        self.project_instance_uid_client_uid = project_instance_uid_client_uid
        self.project_instance_uid_project_type_uid = project_instance_uid_project_type_uid
        self.project_instance_uid_manager_account_uid = project_instance_uid_manager_account_uid
        self.project_instance_uid_project_group_uid = project_instance_uid_project_group_uid
        self.project_instance_uid_project_code = project_instance_uid_project_code
        self.project_instance_uid_project_description = project_instance_uid_project_description
        self.project_instance_uid_is_billable = project_instance_uid_is_billable
        self.project_instance_uid_start_date = project_instance_uid_start_date
        self.project_instance_uid_end_date = project_instance_uid_end_date
        self.project_instance_uid_current_billed = project_instance_uid_current_billed
        self.project_instance_uid_budget = project_instance_uid_budget
        self.currency_uid_currency_name = currency_uid_currency_name
        self.currency_uid_is_focused = currency_uid_is_focused
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.project_budget_uid, self.project_budget_name, self.tenant_uid, self.client_uid, self.project_instance_uid, self.currency_uid, self.budget_value, self.is_approved, self.is_current, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes, self.tenant_uid_tenant_name, self.tenant_uid_country_uid, self.tenant_uid_tenant_type_uid, self.tenant_uid_tenant_category_uid, self.tenant_uid_tenant_code, self.tenant_uid_tenant_description, self.tenant_uid_start_date, self.tenant_uid_end_date, self.tenant_uid_is_internal, self.tenant_uid_is_system, self.tenant_uid_is_test, self.tenant_uid_account_uid, self.client_uid_client_name, self.client_uid_tenant_uid, self.client_uid_country_uid, self.client_uid_client_type_uid, self.client_uid_client_category_uid, self.client_uid_account_uid, self.client_uid_client_code, self.client_uid_client_description, self.client_uid_start_date, self.client_uid_end_date, self.client_uid_is_internal, self.client_uid_is_system, self.client_uid_is_test, self.project_instance_uid_project_instance_name, self.project_instance_uid_tenant_uid, self.project_instance_uid_client_uid, self.project_instance_uid_project_type_uid, self.project_instance_uid_manager_account_uid, self.project_instance_uid_project_group_uid, self.project_instance_uid_project_code, self.project_instance_uid_project_description, self.project_instance_uid_is_billable, self.project_instance_uid_start_date, self.project_instance_uid_end_date, self.project_instance_uid_current_billed, self.project_instance_uid_budget, self.currency_uid_currency_name, self.currency_uid_is_focused]


@dataclass(frozen=False)
class project_group_rich_dto(project_group_read_dto):
    project_group_uid: str | None
    project_group_name: str | None
    tenant_uid: str | None
    project_group_description: str | None
    row_instance: str | None
    row_lock: str | None
    row_owner: str | None
    row_seq: int | None
    row_guid: str | None
    row_version: int | None
    is_active: int | None
    created_date: datetime.datetime | None
    created_by: str | None
    last_updated_date: datetime.datetime | None
    last_updated_by: str | None
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str | None
    tenant_uid_tenant_name: str | None
    tenant_uid_country_uid: str | None
    tenant_uid_tenant_type_uid: str | None
    tenant_uid_tenant_category_uid: str | None
    tenant_uid_tenant_code: str | None
    tenant_uid_tenant_description: str | None
    tenant_uid_start_date: datetime.datetime | None
    tenant_uid_end_date: datetime.datetime | None
    tenant_uid_is_internal: int | None
    tenant_uid_is_system: int | None
    tenant_uid_is_test: int | None
    tenant_uid_account_uid: str | None
    def __init__(self, project_group_uid: str | None, project_group_name: str | None, tenant_uid: str | None, project_group_description: str | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None, tenant_uid_tenant_name: str | None, tenant_uid_country_uid: str | None, tenant_uid_tenant_type_uid: str | None, tenant_uid_tenant_category_uid: str | None, tenant_uid_tenant_code: str | None, tenant_uid_tenant_description: str | None, tenant_uid_start_date: datetime.datetime | None, tenant_uid_end_date: datetime.datetime | None, tenant_uid_is_internal: int | None, tenant_uid_is_system: int | None, tenant_uid_is_test: int | None, tenant_uid_account_uid: str | None):
        self.project_group_uid = project_group_uid
        self.project_group_name = project_group_name
        self.tenant_uid = tenant_uid
        self.project_group_description = project_group_description
        self.row_instance = row_instance
        self.row_lock = row_lock
        self.row_owner = row_owner
        self.row_seq = row_seq
        self.row_guid = row_guid
        self.row_version = row_version
        self.is_active = is_active
        self.created_date = created_date
        self.created_by = created_by
        self.last_updated_date = last_updated_date
        self.last_updated_by = last_updated_by
        self.removed_date = removed_date
        self.removed_by = removed_by
        self.custom_attributes = custom_attributes
        self.tenant_uid_tenant_name = tenant_uid_tenant_name
        self.tenant_uid_country_uid = tenant_uid_country_uid
        self.tenant_uid_tenant_type_uid = tenant_uid_tenant_type_uid
        self.tenant_uid_tenant_category_uid = tenant_uid_tenant_category_uid
        self.tenant_uid_tenant_code = tenant_uid_tenant_code
        self.tenant_uid_tenant_description = tenant_uid_tenant_description
        self.tenant_uid_start_date = tenant_uid_start_date
        self.tenant_uid_end_date = tenant_uid_end_date
        self.tenant_uid_is_internal = tenant_uid_is_internal
        self.tenant_uid_is_system = tenant_uid_is_system
        self.tenant_uid_is_test = tenant_uid_is_test
        self.tenant_uid_account_uid = tenant_uid_account_uid
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.project_group_uid, self.project_group_name, self.tenant_uid, self.project_group_description, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes, self.tenant_uid_tenant_name, self.tenant_uid_country_uid, self.tenant_uid_tenant_type_uid, self.tenant_uid_tenant_category_uid, self.tenant_uid_tenant_code, self.tenant_uid_tenant_description, self.tenant_uid_start_date, self.tenant_uid_end_date, self.tenant_uid_is_internal, self.tenant_uid_is_system, self.tenant_uid_is_test, self.tenant_uid_account_uid]


@dataclass(frozen=False)
class project_instance_rich_dto(project_instance_read_dto):
    project_instance_uid: str | None
    project_instance_name: str | None
    tenant_uid: str | None
    client_uid: str | None
    project_type_uid: str | None
    manager_account_uid: str | None
    project_group_uid: str | None
    project_code: str | None
    project_description: str | None
    is_billable: int | None
    start_date: datetime.datetime | None
    end_date: datetime.datetime | None
    current_billed: str | None
    budget: str | None
    row_instance: str | None
    row_lock: str | None
    row_owner: str | None
    row_seq: int | None
    row_guid: str | None
    row_version: int | None
    is_active: int | None
    created_date: datetime.datetime | None
    created_by: str | None
    last_updated_date: datetime.datetime | None
    last_updated_by: str | None
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str | None
    tenant_uid_tenant_name: str | None
    tenant_uid_country_uid: str | None
    tenant_uid_tenant_type_uid: str | None
    tenant_uid_tenant_category_uid: str | None
    tenant_uid_tenant_code: str | None
    tenant_uid_tenant_description: str | None
    tenant_uid_start_date: datetime.datetime | None
    tenant_uid_end_date: datetime.datetime | None
    tenant_uid_is_internal: int | None
    tenant_uid_is_system: int | None
    tenant_uid_is_test: int | None
    tenant_uid_account_uid: str | None
    client_uid_client_name: str | None
    client_uid_tenant_uid: str | None
    client_uid_country_uid: str | None
    client_uid_client_type_uid: str | None
    client_uid_client_category_uid: str | None
    client_uid_account_uid: str | None
    client_uid_client_code: str | None
    client_uid_client_description: str | None
    client_uid_start_date: datetime.datetime | None
    client_uid_end_date: datetime.datetime | None
    client_uid_is_internal: int | None
    client_uid_is_system: int | None
    client_uid_is_test: int | None
    project_type_uid_project_type_name: str | None
    project_type_uid_project_type_description: str | None
    manager_account_uid_account_name: str | None
    manager_account_uid_tenant_uid: str | None
    manager_account_uid_account_type_uid: str | None
    manager_account_uid_account_title_uid: str | None
    manager_account_uid_account_division_uid: str | None
    manager_account_uid_account_group_uid: str | None
    manager_account_uid_auth_identity_uid: str | None
    manager_account_uid_account_email: str | None
    manager_account_uid_display_name: str | None
    manager_account_uid_is_system: int | None
    project_group_uid_project_group_name: str | None
    project_group_uid_tenant_uid: str | None
    project_group_uid_project_group_description: str | None
    def __init__(self, project_instance_uid: str | None, project_instance_name: str | None, tenant_uid: str | None, client_uid: str | None, project_type_uid: str | None, manager_account_uid: str | None, project_group_uid: str | None, project_code: str | None, project_description: str | None, is_billable: int | None, start_date: datetime.datetime | None, end_date: datetime.datetime | None, current_billed: str | None, budget: str | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None, tenant_uid_tenant_name: str | None, tenant_uid_country_uid: str | None, tenant_uid_tenant_type_uid: str | None, tenant_uid_tenant_category_uid: str | None, tenant_uid_tenant_code: str | None, tenant_uid_tenant_description: str | None, tenant_uid_start_date: datetime.datetime | None, tenant_uid_end_date: datetime.datetime | None, tenant_uid_is_internal: int | None, tenant_uid_is_system: int | None, tenant_uid_is_test: int | None, tenant_uid_account_uid: str | None, client_uid_client_name: str | None, client_uid_tenant_uid: str | None, client_uid_country_uid: str | None, client_uid_client_type_uid: str | None, client_uid_client_category_uid: str | None, client_uid_account_uid: str | None, client_uid_client_code: str | None, client_uid_client_description: str | None, client_uid_start_date: datetime.datetime | None, client_uid_end_date: datetime.datetime | None, client_uid_is_internal: int | None, client_uid_is_system: int | None, client_uid_is_test: int | None, project_type_uid_project_type_name: str | None, project_type_uid_project_type_description: str | None, manager_account_uid_account_name: str | None, manager_account_uid_tenant_uid: str | None, manager_account_uid_account_type_uid: str | None, manager_account_uid_account_title_uid: str | None, manager_account_uid_account_division_uid: str | None, manager_account_uid_account_group_uid: str | None, manager_account_uid_auth_identity_uid: str | None, manager_account_uid_account_email: str | None, manager_account_uid_display_name: str | None, manager_account_uid_is_system: int | None, project_group_uid_project_group_name: str | None, project_group_uid_tenant_uid: str | None, project_group_uid_project_group_description: str | None):
        self.project_instance_uid = project_instance_uid
        self.project_instance_name = project_instance_name
        self.tenant_uid = tenant_uid
        self.client_uid = client_uid
        self.project_type_uid = project_type_uid
        self.manager_account_uid = manager_account_uid
        self.project_group_uid = project_group_uid
        self.project_code = project_code
        self.project_description = project_description
        self.is_billable = is_billable
        self.start_date = start_date
        self.end_date = end_date
        self.current_billed = current_billed
        self.budget = budget
        self.row_instance = row_instance
        self.row_lock = row_lock
        self.row_owner = row_owner
        self.row_seq = row_seq
        self.row_guid = row_guid
        self.row_version = row_version
        self.is_active = is_active
        self.created_date = created_date
        self.created_by = created_by
        self.last_updated_date = last_updated_date
        self.last_updated_by = last_updated_by
        self.removed_date = removed_date
        self.removed_by = removed_by
        self.custom_attributes = custom_attributes
        self.tenant_uid_tenant_name = tenant_uid_tenant_name
        self.tenant_uid_country_uid = tenant_uid_country_uid
        self.tenant_uid_tenant_type_uid = tenant_uid_tenant_type_uid
        self.tenant_uid_tenant_category_uid = tenant_uid_tenant_category_uid
        self.tenant_uid_tenant_code = tenant_uid_tenant_code
        self.tenant_uid_tenant_description = tenant_uid_tenant_description
        self.tenant_uid_start_date = tenant_uid_start_date
        self.tenant_uid_end_date = tenant_uid_end_date
        self.tenant_uid_is_internal = tenant_uid_is_internal
        self.tenant_uid_is_system = tenant_uid_is_system
        self.tenant_uid_is_test = tenant_uid_is_test
        self.tenant_uid_account_uid = tenant_uid_account_uid
        self.client_uid_client_name = client_uid_client_name
        self.client_uid_tenant_uid = client_uid_tenant_uid
        self.client_uid_country_uid = client_uid_country_uid
        self.client_uid_client_type_uid = client_uid_client_type_uid
        self.client_uid_client_category_uid = client_uid_client_category_uid
        self.client_uid_account_uid = client_uid_account_uid
        self.client_uid_client_code = client_uid_client_code
        self.client_uid_client_description = client_uid_client_description
        self.client_uid_start_date = client_uid_start_date
        self.client_uid_end_date = client_uid_end_date
        self.client_uid_is_internal = client_uid_is_internal
        self.client_uid_is_system = client_uid_is_system
        self.client_uid_is_test = client_uid_is_test
        self.project_type_uid_project_type_name = project_type_uid_project_type_name
        self.project_type_uid_project_type_description = project_type_uid_project_type_description
        self.manager_account_uid_account_name = manager_account_uid_account_name
        self.manager_account_uid_tenant_uid = manager_account_uid_tenant_uid
        self.manager_account_uid_account_type_uid = manager_account_uid_account_type_uid
        self.manager_account_uid_account_title_uid = manager_account_uid_account_title_uid
        self.manager_account_uid_account_division_uid = manager_account_uid_account_division_uid
        self.manager_account_uid_account_group_uid = manager_account_uid_account_group_uid
        self.manager_account_uid_auth_identity_uid = manager_account_uid_auth_identity_uid
        self.manager_account_uid_account_email = manager_account_uid_account_email
        self.manager_account_uid_display_name = manager_account_uid_display_name
        self.manager_account_uid_is_system = manager_account_uid_is_system
        self.project_group_uid_project_group_name = project_group_uid_project_group_name
        self.project_group_uid_tenant_uid = project_group_uid_tenant_uid
        self.project_group_uid_project_group_description = project_group_uid_project_group_description
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.project_instance_uid, self.project_instance_name, self.tenant_uid, self.client_uid, self.project_type_uid, self.manager_account_uid, self.project_group_uid, self.project_code, self.project_description, self.is_billable, self.start_date, self.end_date, self.current_billed, self.budget, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes, self.tenant_uid_tenant_name, self.tenant_uid_country_uid, self.tenant_uid_tenant_type_uid, self.tenant_uid_tenant_category_uid, self.tenant_uid_tenant_code, self.tenant_uid_tenant_description, self.tenant_uid_start_date, self.tenant_uid_end_date, self.tenant_uid_is_internal, self.tenant_uid_is_system, self.tenant_uid_is_test, self.tenant_uid_account_uid, self.client_uid_client_name, self.client_uid_tenant_uid, self.client_uid_country_uid, self.client_uid_client_type_uid, self.client_uid_client_category_uid, self.client_uid_account_uid, self.client_uid_client_code, self.client_uid_client_description, self.client_uid_start_date, self.client_uid_end_date, self.client_uid_is_internal, self.client_uid_is_system, self.client_uid_is_test, self.project_type_uid_project_type_name, self.project_type_uid_project_type_description, self.manager_account_uid_account_name, self.manager_account_uid_tenant_uid, self.manager_account_uid_account_type_uid, self.manager_account_uid_account_title_uid, self.manager_account_uid_account_division_uid, self.manager_account_uid_account_group_uid, self.manager_account_uid_auth_identity_uid, self.manager_account_uid_account_email, self.manager_account_uid_display_name, self.manager_account_uid_is_system, self.project_group_uid_project_group_name, self.project_group_uid_tenant_uid, self.project_group_uid_project_group_description]


@dataclass(frozen=False)
class project_milestone_rich_dto(project_milestone_read_dto):
    project_milestone_uid: str | None
    project_milestone_name: str | None
    tenant_uid: str | None
    client_uid: str | None
    project_instance_uid: str | None
    project_budget_uid: str | None
    start_date: datetime.datetime | None
    end_date: datetime.datetime | None
    status_name: str | None
    row_instance: str | None
    row_lock: str | None
    row_owner: str | None
    row_seq: int | None
    row_guid: str | None
    row_version: int | None
    is_active: int | None
    created_date: datetime.datetime | None
    created_by: str | None
    last_updated_date: datetime.datetime | None
    last_updated_by: str | None
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str | None
    tenant_uid_tenant_name: str | None
    tenant_uid_country_uid: str | None
    tenant_uid_tenant_type_uid: str | None
    tenant_uid_tenant_category_uid: str | None
    tenant_uid_tenant_code: str | None
    tenant_uid_tenant_description: str | None
    tenant_uid_start_date: datetime.datetime | None
    tenant_uid_end_date: datetime.datetime | None
    tenant_uid_is_internal: int | None
    tenant_uid_is_system: int | None
    tenant_uid_is_test: int | None
    tenant_uid_account_uid: str | None
    client_uid_client_name: str | None
    client_uid_tenant_uid: str | None
    client_uid_country_uid: str | None
    client_uid_client_type_uid: str | None
    client_uid_client_category_uid: str | None
    client_uid_account_uid: str | None
    client_uid_client_code: str | None
    client_uid_client_description: str | None
    client_uid_start_date: datetime.datetime | None
    client_uid_end_date: datetime.datetime | None
    client_uid_is_internal: int | None
    client_uid_is_system: int | None
    client_uid_is_test: int | None
    project_instance_uid_project_instance_name: str | None
    project_instance_uid_tenant_uid: str | None
    project_instance_uid_client_uid: str | None
    project_instance_uid_project_type_uid: str | None
    project_instance_uid_manager_account_uid: str | None
    project_instance_uid_project_group_uid: str | None
    project_instance_uid_project_code: str | None
    project_instance_uid_project_description: str | None
    project_instance_uid_is_billable: int | None
    project_instance_uid_start_date: datetime.datetime | None
    project_instance_uid_end_date: datetime.datetime | None
    project_instance_uid_current_billed: str | None
    project_instance_uid_budget: str | None
    project_budget_uid_project_budget_name: str | None
    project_budget_uid_tenant_uid: str | None
    project_budget_uid_client_uid: str | None
    project_budget_uid_project_instance_uid: str | None
    project_budget_uid_currency_uid: str | None
    project_budget_uid_budget_value: str | None
    project_budget_uid_is_approved: int | None
    project_budget_uid_is_current: int | None
    def __init__(self, project_milestone_uid: str | None, project_milestone_name: str | None, tenant_uid: str | None, client_uid: str | None, project_instance_uid: str | None, project_budget_uid: str | None, start_date: datetime.datetime | None, end_date: datetime.datetime | None, status_name: str | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None, tenant_uid_tenant_name: str | None, tenant_uid_country_uid: str | None, tenant_uid_tenant_type_uid: str | None, tenant_uid_tenant_category_uid: str | None, tenant_uid_tenant_code: str | None, tenant_uid_tenant_description: str | None, tenant_uid_start_date: datetime.datetime | None, tenant_uid_end_date: datetime.datetime | None, tenant_uid_is_internal: int | None, tenant_uid_is_system: int | None, tenant_uid_is_test: int | None, tenant_uid_account_uid: str | None, client_uid_client_name: str | None, client_uid_tenant_uid: str | None, client_uid_country_uid: str | None, client_uid_client_type_uid: str | None, client_uid_client_category_uid: str | None, client_uid_account_uid: str | None, client_uid_client_code: str | None, client_uid_client_description: str | None, client_uid_start_date: datetime.datetime | None, client_uid_end_date: datetime.datetime | None, client_uid_is_internal: int | None, client_uid_is_system: int | None, client_uid_is_test: int | None, project_instance_uid_project_instance_name: str | None, project_instance_uid_tenant_uid: str | None, project_instance_uid_client_uid: str | None, project_instance_uid_project_type_uid: str | None, project_instance_uid_manager_account_uid: str | None, project_instance_uid_project_group_uid: str | None, project_instance_uid_project_code: str | None, project_instance_uid_project_description: str | None, project_instance_uid_is_billable: int | None, project_instance_uid_start_date: datetime.datetime | None, project_instance_uid_end_date: datetime.datetime | None, project_instance_uid_current_billed: str | None, project_instance_uid_budget: str | None, project_budget_uid_project_budget_name: str | None, project_budget_uid_tenant_uid: str | None, project_budget_uid_client_uid: str | None, project_budget_uid_project_instance_uid: str | None, project_budget_uid_currency_uid: str | None, project_budget_uid_budget_value: str | None, project_budget_uid_is_approved: int | None, project_budget_uid_is_current: int | None):
        self.project_milestone_uid = project_milestone_uid
        self.project_milestone_name = project_milestone_name
        self.tenant_uid = tenant_uid
        self.client_uid = client_uid
        self.project_instance_uid = project_instance_uid
        self.project_budget_uid = project_budget_uid
        self.start_date = start_date
        self.end_date = end_date
        self.status_name = status_name
        self.row_instance = row_instance
        self.row_lock = row_lock
        self.row_owner = row_owner
        self.row_seq = row_seq
        self.row_guid = row_guid
        self.row_version = row_version
        self.is_active = is_active
        self.created_date = created_date
        self.created_by = created_by
        self.last_updated_date = last_updated_date
        self.last_updated_by = last_updated_by
        self.removed_date = removed_date
        self.removed_by = removed_by
        self.custom_attributes = custom_attributes
        self.tenant_uid_tenant_name = tenant_uid_tenant_name
        self.tenant_uid_country_uid = tenant_uid_country_uid
        self.tenant_uid_tenant_type_uid = tenant_uid_tenant_type_uid
        self.tenant_uid_tenant_category_uid = tenant_uid_tenant_category_uid
        self.tenant_uid_tenant_code = tenant_uid_tenant_code
        self.tenant_uid_tenant_description = tenant_uid_tenant_description
        self.tenant_uid_start_date = tenant_uid_start_date
        self.tenant_uid_end_date = tenant_uid_end_date
        self.tenant_uid_is_internal = tenant_uid_is_internal
        self.tenant_uid_is_system = tenant_uid_is_system
        self.tenant_uid_is_test = tenant_uid_is_test
        self.tenant_uid_account_uid = tenant_uid_account_uid
        self.client_uid_client_name = client_uid_client_name
        self.client_uid_tenant_uid = client_uid_tenant_uid
        self.client_uid_country_uid = client_uid_country_uid
        self.client_uid_client_type_uid = client_uid_client_type_uid
        self.client_uid_client_category_uid = client_uid_client_category_uid
        self.client_uid_account_uid = client_uid_account_uid
        self.client_uid_client_code = client_uid_client_code
        self.client_uid_client_description = client_uid_client_description
        self.client_uid_start_date = client_uid_start_date
        self.client_uid_end_date = client_uid_end_date
        self.client_uid_is_internal = client_uid_is_internal
        self.client_uid_is_system = client_uid_is_system
        self.client_uid_is_test = client_uid_is_test
        self.project_instance_uid_project_instance_name = project_instance_uid_project_instance_name
        self.project_instance_uid_tenant_uid = project_instance_uid_tenant_uid
        self.project_instance_uid_client_uid = project_instance_uid_client_uid
        self.project_instance_uid_project_type_uid = project_instance_uid_project_type_uid
        self.project_instance_uid_manager_account_uid = project_instance_uid_manager_account_uid
        self.project_instance_uid_project_group_uid = project_instance_uid_project_group_uid
        self.project_instance_uid_project_code = project_instance_uid_project_code
        self.project_instance_uid_project_description = project_instance_uid_project_description
        self.project_instance_uid_is_billable = project_instance_uid_is_billable
        self.project_instance_uid_start_date = project_instance_uid_start_date
        self.project_instance_uid_end_date = project_instance_uid_end_date
        self.project_instance_uid_current_billed = project_instance_uid_current_billed
        self.project_instance_uid_budget = project_instance_uid_budget
        self.project_budget_uid_project_budget_name = project_budget_uid_project_budget_name
        self.project_budget_uid_tenant_uid = project_budget_uid_tenant_uid
        self.project_budget_uid_client_uid = project_budget_uid_client_uid
        self.project_budget_uid_project_instance_uid = project_budget_uid_project_instance_uid
        self.project_budget_uid_currency_uid = project_budget_uid_currency_uid
        self.project_budget_uid_budget_value = project_budget_uid_budget_value
        self.project_budget_uid_is_approved = project_budget_uid_is_approved
        self.project_budget_uid_is_current = project_budget_uid_is_current
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.project_milestone_uid, self.project_milestone_name, self.tenant_uid, self.client_uid, self.project_instance_uid, self.project_budget_uid, self.start_date, self.end_date, self.status_name, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes, self.tenant_uid_tenant_name, self.tenant_uid_country_uid, self.tenant_uid_tenant_type_uid, self.tenant_uid_tenant_category_uid, self.tenant_uid_tenant_code, self.tenant_uid_tenant_description, self.tenant_uid_start_date, self.tenant_uid_end_date, self.tenant_uid_is_internal, self.tenant_uid_is_system, self.tenant_uid_is_test, self.tenant_uid_account_uid, self.client_uid_client_name, self.client_uid_tenant_uid, self.client_uid_country_uid, self.client_uid_client_type_uid, self.client_uid_client_category_uid, self.client_uid_account_uid, self.client_uid_client_code, self.client_uid_client_description, self.client_uid_start_date, self.client_uid_end_date, self.client_uid_is_internal, self.client_uid_is_system, self.client_uid_is_test, self.project_instance_uid_project_instance_name, self.project_instance_uid_tenant_uid, self.project_instance_uid_client_uid, self.project_instance_uid_project_type_uid, self.project_instance_uid_manager_account_uid, self.project_instance_uid_project_group_uid, self.project_instance_uid_project_code, self.project_instance_uid_project_description, self.project_instance_uid_is_billable, self.project_instance_uid_start_date, self.project_instance_uid_end_date, self.project_instance_uid_current_billed, self.project_instance_uid_budget, self.project_budget_uid_project_budget_name, self.project_budget_uid_tenant_uid, self.project_budget_uid_client_uid, self.project_budget_uid_project_instance_uid, self.project_budget_uid_currency_uid, self.project_budget_uid_budget_value, self.project_budget_uid_is_approved, self.project_budget_uid_is_current]


@dataclass(frozen=False)
class project_type_rich_dto(project_type_read_dto):
    project_type_uid: str | None
    project_type_name: str | None
    project_type_description: str | None
    row_instance: str | None
    row_lock: str | None
    row_owner: str | None
    row_seq: int | None
    row_guid: str | None
    row_version: int | None
    is_active: int | None
    created_date: datetime.datetime | None
    created_by: str | None
    last_updated_date: datetime.datetime | None
    last_updated_by: str | None
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str | None
    def __init__(self, project_type_uid: str | None, project_type_name: str | None, project_type_description: str | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None):
        self.project_type_uid = project_type_uid
        self.project_type_name = project_type_name
        self.project_type_description = project_type_description
        self.row_instance = row_instance
        self.row_lock = row_lock
        self.row_owner = row_owner
        self.row_seq = row_seq
        self.row_guid = row_guid
        self.row_version = row_version
        self.is_active = is_active
        self.created_date = created_date
        self.created_by = created_by
        self.last_updated_date = last_updated_date
        self.last_updated_by = last_updated_by
        self.removed_date = removed_date
        self.removed_by = removed_by
        self.custom_attributes = custom_attributes
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.project_type_uid, self.project_type_name, self.project_type_description, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]


@dataclass(frozen=False)
class report_rich_dto(report_read_dto):
    report_uid: str | None
    report_name: str | None
    tenant_uid: str | None
    account_uid: str | None
    report_status_uid: str | None
    report_query: str | None
    report_parameters: str | None
    row_instance: str | None
    row_lock: str | None
    row_owner: str | None
    row_seq: int | None
    row_guid: str | None
    row_version: int | None
    is_active: int | None
    created_date: datetime.datetime | None
    created_by: str | None
    last_updated_date: datetime.datetime | None
    last_updated_by: str | None
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str | None
    tenant_uid_tenant_name: str | None
    tenant_uid_country_uid: str | None
    tenant_uid_tenant_type_uid: str | None
    tenant_uid_tenant_category_uid: str | None
    tenant_uid_tenant_code: str | None
    tenant_uid_tenant_description: str | None
    tenant_uid_start_date: datetime.datetime | None
    tenant_uid_end_date: datetime.datetime | None
    tenant_uid_is_internal: int | None
    tenant_uid_is_system: int | None
    tenant_uid_is_test: int | None
    tenant_uid_account_uid: str | None
    account_uid_account_name: str | None
    account_uid_tenant_uid: str | None
    account_uid_account_type_uid: str | None
    account_uid_account_title_uid: str | None
    account_uid_account_division_uid: str | None
    account_uid_account_group_uid: str | None
    account_uid_auth_identity_uid: str | None
    account_uid_account_email: str | None
    account_uid_display_name: str | None
    account_uid_is_system: int | None
    report_status_uid_report_status_name: str | None
    def __init__(self, report_uid: str | None, report_name: str | None, tenant_uid: str | None, account_uid: str | None, report_status_uid: str | None, report_query: str | None, report_parameters: str | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None, tenant_uid_tenant_name: str | None, tenant_uid_country_uid: str | None, tenant_uid_tenant_type_uid: str | None, tenant_uid_tenant_category_uid: str | None, tenant_uid_tenant_code: str | None, tenant_uid_tenant_description: str | None, tenant_uid_start_date: datetime.datetime | None, tenant_uid_end_date: datetime.datetime | None, tenant_uid_is_internal: int | None, tenant_uid_is_system: int | None, tenant_uid_is_test: int | None, tenant_uid_account_uid: str | None, account_uid_account_name: str | None, account_uid_tenant_uid: str | None, account_uid_account_type_uid: str | None, account_uid_account_title_uid: str | None, account_uid_account_division_uid: str | None, account_uid_account_group_uid: str | None, account_uid_auth_identity_uid: str | None, account_uid_account_email: str | None, account_uid_display_name: str | None, account_uid_is_system: int | None, report_status_uid_report_status_name: str | None):
        self.report_uid = report_uid
        self.report_name = report_name
        self.tenant_uid = tenant_uid
        self.account_uid = account_uid
        self.report_status_uid = report_status_uid
        self.report_query = report_query
        self.report_parameters = report_parameters
        self.row_instance = row_instance
        self.row_lock = row_lock
        self.row_owner = row_owner
        self.row_seq = row_seq
        self.row_guid = row_guid
        self.row_version = row_version
        self.is_active = is_active
        self.created_date = created_date
        self.created_by = created_by
        self.last_updated_date = last_updated_date
        self.last_updated_by = last_updated_by
        self.removed_date = removed_date
        self.removed_by = removed_by
        self.custom_attributes = custom_attributes
        self.tenant_uid_tenant_name = tenant_uid_tenant_name
        self.tenant_uid_country_uid = tenant_uid_country_uid
        self.tenant_uid_tenant_type_uid = tenant_uid_tenant_type_uid
        self.tenant_uid_tenant_category_uid = tenant_uid_tenant_category_uid
        self.tenant_uid_tenant_code = tenant_uid_tenant_code
        self.tenant_uid_tenant_description = tenant_uid_tenant_description
        self.tenant_uid_start_date = tenant_uid_start_date
        self.tenant_uid_end_date = tenant_uid_end_date
        self.tenant_uid_is_internal = tenant_uid_is_internal
        self.tenant_uid_is_system = tenant_uid_is_system
        self.tenant_uid_is_test = tenant_uid_is_test
        self.tenant_uid_account_uid = tenant_uid_account_uid
        self.account_uid_account_name = account_uid_account_name
        self.account_uid_tenant_uid = account_uid_tenant_uid
        self.account_uid_account_type_uid = account_uid_account_type_uid
        self.account_uid_account_title_uid = account_uid_account_title_uid
        self.account_uid_account_division_uid = account_uid_account_division_uid
        self.account_uid_account_group_uid = account_uid_account_group_uid
        self.account_uid_auth_identity_uid = account_uid_auth_identity_uid
        self.account_uid_account_email = account_uid_account_email
        self.account_uid_display_name = account_uid_display_name
        self.account_uid_is_system = account_uid_is_system
        self.report_status_uid_report_status_name = report_status_uid_report_status_name
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.report_uid, self.report_name, self.tenant_uid, self.account_uid, self.report_status_uid, self.report_query, self.report_parameters, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes, self.tenant_uid_tenant_name, self.tenant_uid_country_uid, self.tenant_uid_tenant_type_uid, self.tenant_uid_tenant_category_uid, self.tenant_uid_tenant_code, self.tenant_uid_tenant_description, self.tenant_uid_start_date, self.tenant_uid_end_date, self.tenant_uid_is_internal, self.tenant_uid_is_system, self.tenant_uid_is_test, self.tenant_uid_account_uid, self.account_uid_account_name, self.account_uid_tenant_uid, self.account_uid_account_type_uid, self.account_uid_account_title_uid, self.account_uid_account_division_uid, self.account_uid_account_group_uid, self.account_uid_auth_identity_uid, self.account_uid_account_email, self.account_uid_display_name, self.account_uid_is_system, self.report_status_uid_report_status_name]


@dataclass(frozen=False)
class report_content_type_rich_dto(report_content_type_read_dto):
    report_content_type_uid: str | None
    report_content_type_name: str | None
    row_instance: str | None
    row_lock: str | None
    row_owner: str | None
    row_seq: int | None
    row_guid: str | None
    row_version: int | None
    is_active: int | None
    created_date: datetime.datetime | None
    created_by: str | None
    last_updated_date: datetime.datetime | None
    last_updated_by: str | None
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str | None
    def __init__(self, report_content_type_uid: str | None, report_content_type_name: str | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None):
        self.report_content_type_uid = report_content_type_uid
        self.report_content_type_name = report_content_type_name
        self.row_instance = row_instance
        self.row_lock = row_lock
        self.row_owner = row_owner
        self.row_seq = row_seq
        self.row_guid = row_guid
        self.row_version = row_version
        self.is_active = is_active
        self.created_date = created_date
        self.created_by = created_by
        self.last_updated_date = last_updated_date
        self.last_updated_by = last_updated_by
        self.removed_date = removed_date
        self.removed_by = removed_by
        self.custom_attributes = custom_attributes
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.report_content_type_uid, self.report_content_type_name, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]


@dataclass(frozen=False)
class report_format_rich_dto(report_format_read_dto):
    report_format_uid: str | None
    report_format_name: str | None
    row_instance: str | None
    row_lock: str | None
    row_owner: str | None
    row_seq: int | None
    row_guid: str | None
    row_version: int | None
    is_active: int | None
    created_date: datetime.datetime | None
    created_by: str | None
    last_updated_date: datetime.datetime | None
    last_updated_by: str | None
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str | None
    def __init__(self, report_format_uid: str | None, report_format_name: str | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None):
        self.report_format_uid = report_format_uid
        self.report_format_name = report_format_name
        self.row_instance = row_instance
        self.row_lock = row_lock
        self.row_owner = row_owner
        self.row_seq = row_seq
        self.row_guid = row_guid
        self.row_version = row_version
        self.is_active = is_active
        self.created_date = created_date
        self.created_by = created_by
        self.last_updated_date = last_updated_date
        self.last_updated_by = last_updated_by
        self.removed_date = removed_date
        self.removed_by = removed_by
        self.custom_attributes = custom_attributes
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.report_format_uid, self.report_format_name, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]


@dataclass(frozen=False)
class report_run_rich_dto(report_run_read_dto):
    report_run_uid: str | None
    report_run_name: str | None
    tenant_uid: str | None
    account_uid: str | None
    report_uid: str | None
    report_format_uid: str | None
    report_status_uid: str | None
    report_content_type_uid: str | None
    input_parameters_json: str | None
    run_time_ms: int | None
    returned_rows: int | None
    content_size: int | None
    row_instance: str | None
    row_lock: str | None
    row_owner: str | None
    row_seq: int | None
    row_guid: str | None
    row_version: int | None
    is_active: int | None
    created_date: datetime.datetime | None
    created_by: str | None
    last_updated_date: datetime.datetime | None
    last_updated_by: str | None
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str | None
    tenant_uid_tenant_name: str | None
    tenant_uid_country_uid: str | None
    tenant_uid_tenant_type_uid: str | None
    tenant_uid_tenant_category_uid: str | None
    tenant_uid_tenant_code: str | None
    tenant_uid_tenant_description: str | None
    tenant_uid_start_date: datetime.datetime | None
    tenant_uid_end_date: datetime.datetime | None
    tenant_uid_is_internal: int | None
    tenant_uid_is_system: int | None
    tenant_uid_is_test: int | None
    tenant_uid_account_uid: str | None
    account_uid_account_name: str | None
    account_uid_tenant_uid: str | None
    account_uid_account_type_uid: str | None
    account_uid_account_title_uid: str | None
    account_uid_account_division_uid: str | None
    account_uid_account_group_uid: str | None
    account_uid_auth_identity_uid: str | None
    account_uid_account_email: str | None
    account_uid_display_name: str | None
    account_uid_is_system: int | None
    report_uid_report_name: str | None
    report_uid_tenant_uid: str | None
    report_uid_account_uid: str | None
    report_uid_report_status_uid: str | None
    report_uid_report_query: str | None
    report_uid_report_parameters: str | None
    report_format_uid_report_format_name: str | None
    report_status_uid_report_status_name: str | None
    report_content_type_uid_report_content_type_name: str | None
    def __init__(self, report_run_uid: str | None, report_run_name: str | None, tenant_uid: str | None, account_uid: str | None, report_uid: str | None, report_format_uid: str | None, report_status_uid: str | None, report_content_type_uid: str | None, input_parameters_json: str | None, run_time_ms: int | None, returned_rows: int | None, content_size: int | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None, tenant_uid_tenant_name: str | None, tenant_uid_country_uid: str | None, tenant_uid_tenant_type_uid: str | None, tenant_uid_tenant_category_uid: str | None, tenant_uid_tenant_code: str | None, tenant_uid_tenant_description: str | None, tenant_uid_start_date: datetime.datetime | None, tenant_uid_end_date: datetime.datetime | None, tenant_uid_is_internal: int | None, tenant_uid_is_system: int | None, tenant_uid_is_test: int | None, tenant_uid_account_uid: str | None, account_uid_account_name: str | None, account_uid_tenant_uid: str | None, account_uid_account_type_uid: str | None, account_uid_account_title_uid: str | None, account_uid_account_division_uid: str | None, account_uid_account_group_uid: str | None, account_uid_auth_identity_uid: str | None, account_uid_account_email: str | None, account_uid_display_name: str | None, account_uid_is_system: int | None, report_uid_report_name: str | None, report_uid_tenant_uid: str | None, report_uid_account_uid: str | None, report_uid_report_status_uid: str | None, report_uid_report_query: str | None, report_uid_report_parameters: str | None, report_format_uid_report_format_name: str | None, report_status_uid_report_status_name: str | None, report_content_type_uid_report_content_type_name: str | None):
        self.report_run_uid = report_run_uid
        self.report_run_name = report_run_name
        self.tenant_uid = tenant_uid
        self.account_uid = account_uid
        self.report_uid = report_uid
        self.report_format_uid = report_format_uid
        self.report_status_uid = report_status_uid
        self.report_content_type_uid = report_content_type_uid
        self.input_parameters_json = input_parameters_json
        self.run_time_ms = run_time_ms
        self.returned_rows = returned_rows
        self.content_size = content_size
        self.row_instance = row_instance
        self.row_lock = row_lock
        self.row_owner = row_owner
        self.row_seq = row_seq
        self.row_guid = row_guid
        self.row_version = row_version
        self.is_active = is_active
        self.created_date = created_date
        self.created_by = created_by
        self.last_updated_date = last_updated_date
        self.last_updated_by = last_updated_by
        self.removed_date = removed_date
        self.removed_by = removed_by
        self.custom_attributes = custom_attributes
        self.tenant_uid_tenant_name = tenant_uid_tenant_name
        self.tenant_uid_country_uid = tenant_uid_country_uid
        self.tenant_uid_tenant_type_uid = tenant_uid_tenant_type_uid
        self.tenant_uid_tenant_category_uid = tenant_uid_tenant_category_uid
        self.tenant_uid_tenant_code = tenant_uid_tenant_code
        self.tenant_uid_tenant_description = tenant_uid_tenant_description
        self.tenant_uid_start_date = tenant_uid_start_date
        self.tenant_uid_end_date = tenant_uid_end_date
        self.tenant_uid_is_internal = tenant_uid_is_internal
        self.tenant_uid_is_system = tenant_uid_is_system
        self.tenant_uid_is_test = tenant_uid_is_test
        self.tenant_uid_account_uid = tenant_uid_account_uid
        self.account_uid_account_name = account_uid_account_name
        self.account_uid_tenant_uid = account_uid_tenant_uid
        self.account_uid_account_type_uid = account_uid_account_type_uid
        self.account_uid_account_title_uid = account_uid_account_title_uid
        self.account_uid_account_division_uid = account_uid_account_division_uid
        self.account_uid_account_group_uid = account_uid_account_group_uid
        self.account_uid_auth_identity_uid = account_uid_auth_identity_uid
        self.account_uid_account_email = account_uid_account_email
        self.account_uid_display_name = account_uid_display_name
        self.account_uid_is_system = account_uid_is_system
        self.report_uid_report_name = report_uid_report_name
        self.report_uid_tenant_uid = report_uid_tenant_uid
        self.report_uid_account_uid = report_uid_account_uid
        self.report_uid_report_status_uid = report_uid_report_status_uid
        self.report_uid_report_query = report_uid_report_query
        self.report_uid_report_parameters = report_uid_report_parameters
        self.report_format_uid_report_format_name = report_format_uid_report_format_name
        self.report_status_uid_report_status_name = report_status_uid_report_status_name
        self.report_content_type_uid_report_content_type_name = report_content_type_uid_report_content_type_name
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.report_run_uid, self.report_run_name, self.tenant_uid, self.account_uid, self.report_uid, self.report_format_uid, self.report_status_uid, self.report_content_type_uid, self.input_parameters_json, self.run_time_ms, self.returned_rows, self.content_size, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes, self.tenant_uid_tenant_name, self.tenant_uid_country_uid, self.tenant_uid_tenant_type_uid, self.tenant_uid_tenant_category_uid, self.tenant_uid_tenant_code, self.tenant_uid_tenant_description, self.tenant_uid_start_date, self.tenant_uid_end_date, self.tenant_uid_is_internal, self.tenant_uid_is_system, self.tenant_uid_is_test, self.tenant_uid_account_uid, self.account_uid_account_name, self.account_uid_tenant_uid, self.account_uid_account_type_uid, self.account_uid_account_title_uid, self.account_uid_account_division_uid, self.account_uid_account_group_uid, self.account_uid_auth_identity_uid, self.account_uid_account_email, self.account_uid_display_name, self.account_uid_is_system, self.report_uid_report_name, self.report_uid_tenant_uid, self.report_uid_account_uid, self.report_uid_report_status_uid, self.report_uid_report_query, self.report_uid_report_parameters, self.report_format_uid_report_format_name, self.report_status_uid_report_status_name, self.report_content_type_uid_report_content_type_name]


@dataclass(frozen=False)
class report_status_rich_dto(report_status_read_dto):
    report_status_uid: str | None
    report_status_name: str | None
    row_instance: str | None
    row_lock: str | None
    row_owner: str | None
    row_seq: int | None
    row_guid: str | None
    row_version: int | None
    is_active: int | None
    created_date: datetime.datetime | None
    created_by: str | None
    last_updated_date: datetime.datetime | None
    last_updated_by: str | None
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str | None
    def __init__(self, report_status_uid: str | None, report_status_name: str | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None):
        self.report_status_uid = report_status_uid
        self.report_status_name = report_status_name
        self.row_instance = row_instance
        self.row_lock = row_lock
        self.row_owner = row_owner
        self.row_seq = row_seq
        self.row_guid = row_guid
        self.row_version = row_version
        self.is_active = is_active
        self.created_date = created_date
        self.created_by = created_by
        self.last_updated_date = last_updated_date
        self.last_updated_by = last_updated_by
        self.removed_date = removed_date
        self.removed_by = removed_by
        self.custom_attributes = custom_attributes
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.report_status_uid, self.report_status_name, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]


@dataclass(frozen=False)
class report_type_rich_dto(report_type_read_dto):
    report_type_uid: str | None
    report_type_name: str | None
    row_instance: str | None
    row_lock: str | None
    row_owner: str | None
    row_seq: int | None
    row_guid: str | None
    row_version: int | None
    is_active: int | None
    created_date: datetime.datetime | None
    created_by: str | None
    last_updated_date: datetime.datetime | None
    last_updated_by: str | None
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str | None
    def __init__(self, report_type_uid: str | None, report_type_name: str | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None):
        self.report_type_uid = report_type_uid
        self.report_type_name = report_type_name
        self.row_instance = row_instance
        self.row_lock = row_lock
        self.row_owner = row_owner
        self.row_seq = row_seq
        self.row_guid = row_guid
        self.row_version = row_version
        self.is_active = is_active
        self.created_date = created_date
        self.created_by = created_by
        self.last_updated_date = last_updated_date
        self.last_updated_by = last_updated_by
        self.removed_date = removed_date
        self.removed_by = removed_by
        self.custom_attributes = custom_attributes
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.report_type_uid, self.report_type_name, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]


@dataclass(frozen=False)
class storage_rich_dto(storage_read_dto):
    storage_uid: str | None
    storage_name: str | None
    storage_class: str | None
    storage_parameters_json: str | None
    row_instance: str | None
    row_lock: str | None
    row_owner: str | None
    row_seq: int | None
    row_guid: str | None
    row_version: int | None
    is_active: int | None
    created_date: datetime.datetime | None
    created_by: str | None
    last_updated_date: datetime.datetime | None
    last_updated_by: str | None
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str | None
    def __init__(self, storage_uid: str | None, storage_name: str | None, storage_class: str | None, storage_parameters_json: str | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None):
        self.storage_uid = storage_uid
        self.storage_name = storage_name
        self.storage_class = storage_class
        self.storage_parameters_json = storage_parameters_json
        self.row_instance = row_instance
        self.row_lock = row_lock
        self.row_owner = row_owner
        self.row_seq = row_seq
        self.row_guid = row_guid
        self.row_version = row_version
        self.is_active = is_active
        self.created_date = created_date
        self.created_by = created_by
        self.last_updated_date = last_updated_date
        self.last_updated_by = last_updated_by
        self.removed_date = removed_date
        self.removed_by = removed_by
        self.custom_attributes = custom_attributes
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.storage_uid, self.storage_name, self.storage_class, self.storage_parameters_json, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]


@dataclass(frozen=False)
class storage_connection_rich_dto(storage_connection_read_dto):
    storage_connection_uid: str | None
    storage_connection_name: str | None
    storage_uid: str | None
    connection_type: str | None
    storage_parameters_json: str | None
    row_instance: str | None
    row_lock: str | None
    row_owner: str | None
    row_seq: int | None
    row_guid: str | None
    row_version: int | None
    is_active: int | None
    created_date: datetime.datetime | None
    created_by: str | None
    last_updated_date: datetime.datetime | None
    last_updated_by: str | None
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str | None
    storage_uid_storage_name: str | None
    storage_uid_storage_class: str | None
    storage_uid_storage_parameters_json: str | None
    def __init__(self, storage_connection_uid: str | None, storage_connection_name: str | None, storage_uid: str | None, connection_type: str | None, storage_parameters_json: str | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None, storage_uid_storage_name: str | None, storage_uid_storage_class: str | None, storage_uid_storage_parameters_json: str | None):
        self.storage_connection_uid = storage_connection_uid
        self.storage_connection_name = storage_connection_name
        self.storage_uid = storage_uid
        self.connection_type = connection_type
        self.storage_parameters_json = storage_parameters_json
        self.row_instance = row_instance
        self.row_lock = row_lock
        self.row_owner = row_owner
        self.row_seq = row_seq
        self.row_guid = row_guid
        self.row_version = row_version
        self.is_active = is_active
        self.created_date = created_date
        self.created_by = created_by
        self.last_updated_date = last_updated_date
        self.last_updated_by = last_updated_by
        self.removed_date = removed_date
        self.removed_by = removed_by
        self.custom_attributes = custom_attributes
        self.storage_uid_storage_name = storage_uid_storage_name
        self.storage_uid_storage_class = storage_uid_storage_class
        self.storage_uid_storage_parameters_json = storage_uid_storage_parameters_json
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.storage_connection_uid, self.storage_connection_name, self.storage_uid, self.connection_type, self.storage_parameters_json, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes, self.storage_uid_storage_name, self.storage_uid_storage_class, self.storage_uid_storage_parameters_json]


@dataclass(frozen=False)
class storage_query_rich_dto(storage_query_read_dto):
    storage_connection_uid: str | None
    storage_connection_name: str | None
    storage_uid: str | None
    storage_parameters_json: str | None
    row_instance: str | None
    row_lock: str | None
    row_owner: str | None
    row_seq: int | None
    row_guid: str | None
    row_version: int | None
    is_active: int | None
    created_date: datetime.datetime | None
    created_by: str | None
    last_updated_date: datetime.datetime | None
    last_updated_by: str | None
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str | None
    storage_connection_uid_storage_connection_name: str | None
    storage_connection_uid_storage_uid: str | None
    storage_connection_uid_connection_type: str | None
    storage_connection_uid_storage_parameters_json: str | None
    storage_uid_storage_name: str | None
    storage_uid_storage_class: str | None
    storage_uid_storage_parameters_json: str | None
    def __init__(self, storage_connection_uid: str | None, storage_connection_name: str | None, storage_uid: str | None, storage_parameters_json: str | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None, storage_connection_uid_storage_connection_name: str | None, storage_connection_uid_storage_uid: str | None, storage_connection_uid_connection_type: str | None, storage_connection_uid_storage_parameters_json: str | None, storage_uid_storage_name: str | None, storage_uid_storage_class: str | None, storage_uid_storage_parameters_json: str | None):
        self.storage_connection_uid = storage_connection_uid
        self.storage_connection_name = storage_connection_name
        self.storage_uid = storage_uid
        self.storage_parameters_json = storage_parameters_json
        self.row_instance = row_instance
        self.row_lock = row_lock
        self.row_owner = row_owner
        self.row_seq = row_seq
        self.row_guid = row_guid
        self.row_version = row_version
        self.is_active = is_active
        self.created_date = created_date
        self.created_by = created_by
        self.last_updated_date = last_updated_date
        self.last_updated_by = last_updated_by
        self.removed_date = removed_date
        self.removed_by = removed_by
        self.custom_attributes = custom_attributes
        self.storage_connection_uid_storage_connection_name = storage_connection_uid_storage_connection_name
        self.storage_connection_uid_storage_uid = storage_connection_uid_storage_uid
        self.storage_connection_uid_connection_type = storage_connection_uid_connection_type
        self.storage_connection_uid_storage_parameters_json = storage_connection_uid_storage_parameters_json
        self.storage_uid_storage_name = storage_uid_storage_name
        self.storage_uid_storage_class = storage_uid_storage_class
        self.storage_uid_storage_parameters_json = storage_uid_storage_parameters_json
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.storage_connection_uid, self.storage_connection_name, self.storage_uid, self.storage_parameters_json, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes, self.storage_connection_uid_storage_connection_name, self.storage_connection_uid_storage_uid, self.storage_connection_uid_connection_type, self.storage_connection_uid_storage_parameters_json, self.storage_uid_storage_name, self.storage_uid_storage_class, self.storage_uid_storage_parameters_json]


@dataclass(frozen=False)
class storage_type_rich_dto(storage_type_read_dto):
    storage_type_uid: str | None
    storage_type_name: str | None
    storage_class: str | None
    storage_parameters_json: str | None
    row_instance: str | None
    row_lock: str | None
    row_owner: str | None
    row_seq: int | None
    row_guid: str | None
    row_version: int | None
    is_active: int | None
    created_date: datetime.datetime | None
    created_by: str | None
    last_updated_date: datetime.datetime | None
    last_updated_by: str | None
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str | None
    def __init__(self, storage_type_uid: str | None, storage_type_name: str | None, storage_class: str | None, storage_parameters_json: str | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None):
        self.storage_type_uid = storage_type_uid
        self.storage_type_name = storage_type_name
        self.storage_class = storage_class
        self.storage_parameters_json = storage_parameters_json
        self.row_instance = row_instance
        self.row_lock = row_lock
        self.row_owner = row_owner
        self.row_seq = row_seq
        self.row_guid = row_guid
        self.row_version = row_version
        self.is_active = is_active
        self.created_date = created_date
        self.created_by = created_by
        self.last_updated_date = last_updated_date
        self.last_updated_by = last_updated_by
        self.removed_date = removed_date
        self.removed_by = removed_by
        self.custom_attributes = custom_attributes
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.storage_type_uid, self.storage_type_name, self.storage_class, self.storage_parameters_json, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]


@dataclass(frozen=False)
class synchronization_rich_dto(synchronization_read_dto):
    synchronization_uid: str | None
    synchronization_name: str | None
    tenant_uid: str | None
    synchronization_type_uid: str | None
    storage_uid: str | None
    sync_expression: str | None
    sync_query: str | None
    sync_definition: str | None
    sync_priority: int | None
    last_run_date: datetime.datetime | None
    last_run_seconds: str | None
    row_instance: str | None
    row_lock: str | None
    row_owner: str | None
    row_seq: int | None
    row_guid: str | None
    row_version: int | None
    is_active: int | None
    created_date: datetime.datetime | None
    created_by: str | None
    last_updated_date: datetime.datetime | None
    last_updated_by: str | None
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str | None
    tenant_uid_tenant_name: str | None
    tenant_uid_country_uid: str | None
    tenant_uid_tenant_type_uid: str | None
    tenant_uid_tenant_category_uid: str | None
    tenant_uid_tenant_code: str | None
    tenant_uid_tenant_description: str | None
    tenant_uid_start_date: datetime.datetime | None
    tenant_uid_end_date: datetime.datetime | None
    tenant_uid_is_internal: int | None
    tenant_uid_is_system: int | None
    tenant_uid_is_test: int | None
    tenant_uid_account_uid: str | None
    synchronization_type_uid_synchronization_type_name: str | None
    synchronization_type_uid_sync_type: str | None
    synchronization_type_uid_sync_class_came: str | None
    storage_uid_storage_name: str | None
    storage_uid_storage_class: str | None
    storage_uid_storage_parameters_json: str | None
    def __init__(self, synchronization_uid: str | None, synchronization_name: str | None, tenant_uid: str | None, synchronization_type_uid: str | None, storage_uid: str | None, sync_expression: str | None, sync_query: str | None, sync_definition: str | None, sync_priority: int | None, last_run_date: datetime.datetime | None, last_run_seconds: str | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None, tenant_uid_tenant_name: str | None, tenant_uid_country_uid: str | None, tenant_uid_tenant_type_uid: str | None, tenant_uid_tenant_category_uid: str | None, tenant_uid_tenant_code: str | None, tenant_uid_tenant_description: str | None, tenant_uid_start_date: datetime.datetime | None, tenant_uid_end_date: datetime.datetime | None, tenant_uid_is_internal: int | None, tenant_uid_is_system: int | None, tenant_uid_is_test: int | None, tenant_uid_account_uid: str | None, synchronization_type_uid_synchronization_type_name: str | None, synchronization_type_uid_sync_type: str | None, synchronization_type_uid_sync_class_came: str | None, storage_uid_storage_name: str | None, storage_uid_storage_class: str | None, storage_uid_storage_parameters_json: str | None):
        self.synchronization_uid = synchronization_uid
        self.synchronization_name = synchronization_name
        self.tenant_uid = tenant_uid
        self.synchronization_type_uid = synchronization_type_uid
        self.storage_uid = storage_uid
        self.sync_expression = sync_expression
        self.sync_query = sync_query
        self.sync_definition = sync_definition
        self.sync_priority = sync_priority
        self.last_run_date = last_run_date
        self.last_run_seconds = last_run_seconds
        self.row_instance = row_instance
        self.row_lock = row_lock
        self.row_owner = row_owner
        self.row_seq = row_seq
        self.row_guid = row_guid
        self.row_version = row_version
        self.is_active = is_active
        self.created_date = created_date
        self.created_by = created_by
        self.last_updated_date = last_updated_date
        self.last_updated_by = last_updated_by
        self.removed_date = removed_date
        self.removed_by = removed_by
        self.custom_attributes = custom_attributes
        self.tenant_uid_tenant_name = tenant_uid_tenant_name
        self.tenant_uid_country_uid = tenant_uid_country_uid
        self.tenant_uid_tenant_type_uid = tenant_uid_tenant_type_uid
        self.tenant_uid_tenant_category_uid = tenant_uid_tenant_category_uid
        self.tenant_uid_tenant_code = tenant_uid_tenant_code
        self.tenant_uid_tenant_description = tenant_uid_tenant_description
        self.tenant_uid_start_date = tenant_uid_start_date
        self.tenant_uid_end_date = tenant_uid_end_date
        self.tenant_uid_is_internal = tenant_uid_is_internal
        self.tenant_uid_is_system = tenant_uid_is_system
        self.tenant_uid_is_test = tenant_uid_is_test
        self.tenant_uid_account_uid = tenant_uid_account_uid
        self.synchronization_type_uid_synchronization_type_name = synchronization_type_uid_synchronization_type_name
        self.synchronization_type_uid_sync_type = synchronization_type_uid_sync_type
        self.synchronization_type_uid_sync_class_came = synchronization_type_uid_sync_class_came
        self.storage_uid_storage_name = storage_uid_storage_name
        self.storage_uid_storage_class = storage_uid_storage_class
        self.storage_uid_storage_parameters_json = storage_uid_storage_parameters_json
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.synchronization_uid, self.synchronization_name, self.tenant_uid, self.synchronization_type_uid, self.storage_uid, self.sync_expression, self.sync_query, self.sync_definition, self.sync_priority, self.last_run_date, self.last_run_seconds, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes, self.tenant_uid_tenant_name, self.tenant_uid_country_uid, self.tenant_uid_tenant_type_uid, self.tenant_uid_tenant_category_uid, self.tenant_uid_tenant_code, self.tenant_uid_tenant_description, self.tenant_uid_start_date, self.tenant_uid_end_date, self.tenant_uid_is_internal, self.tenant_uid_is_system, self.tenant_uid_is_test, self.tenant_uid_account_uid, self.synchronization_type_uid_synchronization_type_name, self.synchronization_type_uid_sync_type, self.synchronization_type_uid_sync_class_came, self.storage_uid_storage_name, self.storage_uid_storage_class, self.storage_uid_storage_parameters_json]


@dataclass(frozen=False)
class synchronization_run_rich_dto(synchronization_run_read_dto):
    synchronization_run_uid: str | None
    synchronization_run_name: str | None
    synchronization_uid: str | None
    run_status: str | None
    run_time_seconds: str | None
    copied_items: int | None
    row_instance: str | None
    row_lock: str | None
    row_owner: str | None
    row_seq: int | None
    row_guid: str | None
    row_version: int | None
    is_active: int | None
    created_date: datetime.datetime | None
    created_by: str | None
    last_updated_date: datetime.datetime | None
    last_updated_by: str | None
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str | None
    synchronization_uid_synchronization_name: str | None
    synchronization_uid_tenant_uid: str | None
    synchronization_uid_synchronization_type_uid: str | None
    synchronization_uid_storage_uid: str | None
    synchronization_uid_sync_expression: str | None
    synchronization_uid_sync_query: str | None
    synchronization_uid_sync_definition: str | None
    synchronization_uid_sync_priority: int | None
    synchronization_uid_last_run_date: datetime.datetime | None
    synchronization_uid_last_run_seconds: str | None
    def __init__(self, synchronization_run_uid: str | None, synchronization_run_name: str | None, synchronization_uid: str | None, run_status: str | None, run_time_seconds: str | None, copied_items: int | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None, synchronization_uid_synchronization_name: str | None, synchronization_uid_tenant_uid: str | None, synchronization_uid_synchronization_type_uid: str | None, synchronization_uid_storage_uid: str | None, synchronization_uid_sync_expression: str | None, synchronization_uid_sync_query: str | None, synchronization_uid_sync_definition: str | None, synchronization_uid_sync_priority: int | None, synchronization_uid_last_run_date: datetime.datetime | None, synchronization_uid_last_run_seconds: str | None):
        self.synchronization_run_uid = synchronization_run_uid
        self.synchronization_run_name = synchronization_run_name
        self.synchronization_uid = synchronization_uid
        self.run_status = run_status
        self.run_time_seconds = run_time_seconds
        self.copied_items = copied_items
        self.row_instance = row_instance
        self.row_lock = row_lock
        self.row_owner = row_owner
        self.row_seq = row_seq
        self.row_guid = row_guid
        self.row_version = row_version
        self.is_active = is_active
        self.created_date = created_date
        self.created_by = created_by
        self.last_updated_date = last_updated_date
        self.last_updated_by = last_updated_by
        self.removed_date = removed_date
        self.removed_by = removed_by
        self.custom_attributes = custom_attributes
        self.synchronization_uid_synchronization_name = synchronization_uid_synchronization_name
        self.synchronization_uid_tenant_uid = synchronization_uid_tenant_uid
        self.synchronization_uid_synchronization_type_uid = synchronization_uid_synchronization_type_uid
        self.synchronization_uid_storage_uid = synchronization_uid_storage_uid
        self.synchronization_uid_sync_expression = synchronization_uid_sync_expression
        self.synchronization_uid_sync_query = synchronization_uid_sync_query
        self.synchronization_uid_sync_definition = synchronization_uid_sync_definition
        self.synchronization_uid_sync_priority = synchronization_uid_sync_priority
        self.synchronization_uid_last_run_date = synchronization_uid_last_run_date
        self.synchronization_uid_last_run_seconds = synchronization_uid_last_run_seconds
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.synchronization_run_uid, self.synchronization_run_name, self.synchronization_uid, self.run_status, self.run_time_seconds, self.copied_items, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes, self.synchronization_uid_synchronization_name, self.synchronization_uid_tenant_uid, self.synchronization_uid_synchronization_type_uid, self.synchronization_uid_storage_uid, self.synchronization_uid_sync_expression, self.synchronization_uid_sync_query, self.synchronization_uid_sync_definition, self.synchronization_uid_sync_priority, self.synchronization_uid_last_run_date, self.synchronization_uid_last_run_seconds]


@dataclass(frozen=False)
class synchronization_type_rich_dto(synchronization_type_read_dto):
    synchronization_type_uid: str | None
    synchronization_type_name: str | None
    sync_type: str | None
    sync_class_came: str | None
    row_instance: str | None
    row_lock: str | None
    row_owner: str | None
    row_seq: int | None
    row_guid: str | None
    row_version: int | None
    is_active: int | None
    created_date: datetime.datetime | None
    created_by: str | None
    last_updated_date: datetime.datetime | None
    last_updated_by: str | None
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str | None
    def __init__(self, synchronization_type_uid: str | None, synchronization_type_name: str | None, sync_type: str | None, sync_class_came: str | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None):
        self.synchronization_type_uid = synchronization_type_uid
        self.synchronization_type_name = synchronization_type_name
        self.sync_type = sync_type
        self.sync_class_came = sync_class_came
        self.row_instance = row_instance
        self.row_lock = row_lock
        self.row_owner = row_owner
        self.row_seq = row_seq
        self.row_guid = row_guid
        self.row_version = row_version
        self.is_active = is_active
        self.created_date = created_date
        self.created_by = created_by
        self.last_updated_date = last_updated_date
        self.last_updated_by = last_updated_by
        self.removed_date = removed_date
        self.removed_by = removed_by
        self.custom_attributes = custom_attributes
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.synchronization_type_uid, self.synchronization_type_name, self.sync_type, self.sync_class_came, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]


@dataclass(frozen=False)
class system_attribute_rich_dto(system_attribute_read_dto):
    system_attribute_uid: str | None
    system_attribute_name: str | None
    system_object_uid: str | None
    column_name: str | None
    attribute_type: str | None
    attribute_label: str | None
    attribute_description: str | None
    row_instance: str | None
    row_lock: str | None
    row_owner: str | None
    row_seq: int | None
    row_guid: str | None
    row_version: int | None
    is_active: int | None
    created_date: datetime.datetime | None
    created_by: str | None
    last_updated_date: datetime.datetime | None
    last_updated_by: str | None
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str | None
    system_object_uid_system_object_name: str | None
    system_object_uid_system_version_uid: str | None
    system_object_uid_system_table_uid: str | None
    system_object_uid_system_object_type_uid: str | None
    system_object_uid_parent_system_object_uid: str | None
    system_object_uid_object_type: str | None
    def __init__(self, system_attribute_uid: str | None, system_attribute_name: str | None, system_object_uid: str | None, column_name: str | None, attribute_type: str | None, attribute_label: str | None, attribute_description: str | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None, system_object_uid_system_object_name: str | None, system_object_uid_system_version_uid: str | None, system_object_uid_system_table_uid: str | None, system_object_uid_system_object_type_uid: str | None, system_object_uid_parent_system_object_uid: str | None, system_object_uid_object_type: str | None):
        self.system_attribute_uid = system_attribute_uid
        self.system_attribute_name = system_attribute_name
        self.system_object_uid = system_object_uid
        self.column_name = column_name
        self.attribute_type = attribute_type
        self.attribute_label = attribute_label
        self.attribute_description = attribute_description
        self.row_instance = row_instance
        self.row_lock = row_lock
        self.row_owner = row_owner
        self.row_seq = row_seq
        self.row_guid = row_guid
        self.row_version = row_version
        self.is_active = is_active
        self.created_date = created_date
        self.created_by = created_by
        self.last_updated_date = last_updated_date
        self.last_updated_by = last_updated_by
        self.removed_date = removed_date
        self.removed_by = removed_by
        self.custom_attributes = custom_attributes
        self.system_object_uid_system_object_name = system_object_uid_system_object_name
        self.system_object_uid_system_version_uid = system_object_uid_system_version_uid
        self.system_object_uid_system_table_uid = system_object_uid_system_table_uid
        self.system_object_uid_system_object_type_uid = system_object_uid_system_object_type_uid
        self.system_object_uid_parent_system_object_uid = system_object_uid_parent_system_object_uid
        self.system_object_uid_object_type = system_object_uid_object_type
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.system_attribute_uid, self.system_attribute_name, self.system_object_uid, self.column_name, self.attribute_type, self.attribute_label, self.attribute_description, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes, self.system_object_uid_system_object_name, self.system_object_uid_system_version_uid, self.system_object_uid_system_table_uid, self.system_object_uid_system_object_type_uid, self.system_object_uid_parent_system_object_uid, self.system_object_uid_object_type]


@dataclass(frozen=False)
class system_database_rich_dto(system_database_read_dto):
    system_database_uid: str | None
    system_database_name: str | None
    db_url: str | None
    db_host: str | None
    db_name: str | None
    db_user: str | None
    row_instance: str | None
    row_lock: str | None
    row_owner: str | None
    row_seq: int | None
    row_guid: str | None
    row_version: int | None
    is_active: int | None
    created_date: datetime.datetime | None
    created_by: str | None
    last_updated_date: datetime.datetime | None
    last_updated_by: str | None
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str | None
    def __init__(self, system_database_uid: str | None, system_database_name: str | None, db_url: str | None, db_host: str | None, db_name: str | None, db_user: str | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None):
        self.system_database_uid = system_database_uid
        self.system_database_name = system_database_name
        self.db_url = db_url
        self.db_host = db_host
        self.db_name = db_name
        self.db_user = db_user
        self.row_instance = row_instance
        self.row_lock = row_lock
        self.row_owner = row_owner
        self.row_seq = row_seq
        self.row_guid = row_guid
        self.row_version = row_version
        self.is_active = is_active
        self.created_date = created_date
        self.created_by = created_by
        self.last_updated_date = last_updated_date
        self.last_updated_by = last_updated_by
        self.removed_date = removed_date
        self.removed_by = removed_by
        self.custom_attributes = custom_attributes
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.system_database_uid, self.system_database_name, self.db_url, self.db_host, self.db_name, self.db_user, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]


@dataclass(frozen=False)
class system_exception_rich_dto(system_exception_read_dto):
    system_exception_uid: str | None
    system_exception_name: str | None
    exception_class: str | None
    exception_message: str | None
    exception_stacktrace: str | None
    row_instance: str | None
    row_lock: str | None
    row_owner: str | None
    row_seq: int | None
    row_guid: str | None
    row_version: int | None
    is_active: int | None
    created_date: datetime.datetime | None
    created_by: str | None
    last_updated_date: datetime.datetime | None
    last_updated_by: str | None
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str | None
    def __init__(self, system_exception_uid: str | None, system_exception_name: str | None, exception_class: str | None, exception_message: str | None, exception_stacktrace: str | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None):
        self.system_exception_uid = system_exception_uid
        self.system_exception_name = system_exception_name
        self.exception_class = exception_class
        self.exception_message = exception_message
        self.exception_stacktrace = exception_stacktrace
        self.row_instance = row_instance
        self.row_lock = row_lock
        self.row_owner = row_owner
        self.row_seq = row_seq
        self.row_guid = row_guid
        self.row_version = row_version
        self.is_active = is_active
        self.created_date = created_date
        self.created_by = created_by
        self.last_updated_date = last_updated_date
        self.last_updated_by = last_updated_by
        self.removed_date = removed_date
        self.removed_by = removed_by
        self.custom_attributes = custom_attributes
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.system_exception_uid, self.system_exception_name, self.exception_class, self.exception_message, self.exception_stacktrace, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]


@dataclass(frozen=False)
class system_instance_rich_dto(system_instance_read_dto):
    system_instance_uid: str | None
    system_instance_name: str | None
    system_version_uid: str | None
    host_name: str | None
    host_ip: str | None
    local_path: str | None
    mode_name: str | None
    ticks_count: int | None
    row_instance: str | None
    row_lock: str | None
    row_owner: str | None
    row_seq: int | None
    row_guid: str | None
    row_version: int | None
    is_active: int | None
    created_date: datetime.datetime | None
    created_by: str | None
    last_updated_date: datetime.datetime | None
    last_updated_by: str | None
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str | None
    system_version_uid_system_version_name: str | None
    system_version_uid_version_description: str | None
    def __init__(self, system_instance_uid: str | None, system_instance_name: str | None, system_version_uid: str | None, host_name: str | None, host_ip: str | None, local_path: str | None, mode_name: str | None, ticks_count: int | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None, system_version_uid_system_version_name: str | None, system_version_uid_version_description: str | None):
        self.system_instance_uid = system_instance_uid
        self.system_instance_name = system_instance_name
        self.system_version_uid = system_version_uid
        self.host_name = host_name
        self.host_ip = host_ip
        self.local_path = local_path
        self.mode_name = mode_name
        self.ticks_count = ticks_count
        self.row_instance = row_instance
        self.row_lock = row_lock
        self.row_owner = row_owner
        self.row_seq = row_seq
        self.row_guid = row_guid
        self.row_version = row_version
        self.is_active = is_active
        self.created_date = created_date
        self.created_by = created_by
        self.last_updated_date = last_updated_date
        self.last_updated_by = last_updated_by
        self.removed_date = removed_date
        self.removed_by = removed_by
        self.custom_attributes = custom_attributes
        self.system_version_uid_system_version_name = system_version_uid_system_version_name
        self.system_version_uid_version_description = system_version_uid_version_description
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.system_instance_uid, self.system_instance_name, self.system_version_uid, self.host_name, self.host_ip, self.local_path, self.mode_name, self.ticks_count, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes, self.system_version_uid_system_version_name, self.system_version_uid_version_description]


@dataclass(frozen=False)
class system_license_rich_dto(system_license_read_dto):
    system_license_uid: str | None
    system_license_name: str | None
    license_description: str | None
    row_instance: str | None
    row_lock: str | None
    row_owner: str | None
    row_seq: int | None
    row_guid: str | None
    row_version: int | None
    is_active: int | None
    created_date: datetime.datetime | None
    created_by: str | None
    last_updated_date: datetime.datetime | None
    last_updated_by: str | None
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str | None
    def __init__(self, system_license_uid: str | None, system_license_name: str | None, license_description: str | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None):
        self.system_license_uid = system_license_uid
        self.system_license_name = system_license_name
        self.license_description = license_description
        self.row_instance = row_instance
        self.row_lock = row_lock
        self.row_owner = row_owner
        self.row_seq = row_seq
        self.row_guid = row_guid
        self.row_version = row_version
        self.is_active = is_active
        self.created_date = created_date
        self.created_by = created_by
        self.last_updated_date = last_updated_date
        self.last_updated_by = last_updated_by
        self.removed_date = removed_date
        self.removed_by = removed_by
        self.custom_attributes = custom_attributes
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.system_license_uid, self.system_license_name, self.license_description, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]


@dataclass(frozen=False)
class system_lock_rich_dto(system_lock_read_dto):
    system_lock_uid: str | None
    system_lock_name: str | None
    lock_account_uid: str | None
    lock_comment: str | None
    row_instance: str | None
    row_lock: str | None
    row_owner: str | None
    row_seq: int | None
    row_guid: str | None
    row_version: int | None
    is_active: int | None
    created_date: datetime.datetime | None
    created_by: str | None
    last_updated_date: datetime.datetime | None
    last_updated_by: str | None
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str | None
    lock_account_uid_account_name: str | None
    lock_account_uid_tenant_uid: str | None
    lock_account_uid_account_type_uid: str | None
    lock_account_uid_account_title_uid: str | None
    lock_account_uid_account_division_uid: str | None
    lock_account_uid_account_group_uid: str | None
    lock_account_uid_auth_identity_uid: str | None
    lock_account_uid_account_email: str | None
    lock_account_uid_display_name: str | None
    lock_account_uid_is_system: int | None
    def __init__(self, system_lock_uid: str | None, system_lock_name: str | None, lock_account_uid: str | None, lock_comment: str | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None, lock_account_uid_account_name: str | None, lock_account_uid_tenant_uid: str | None, lock_account_uid_account_type_uid: str | None, lock_account_uid_account_title_uid: str | None, lock_account_uid_account_division_uid: str | None, lock_account_uid_account_group_uid: str | None, lock_account_uid_auth_identity_uid: str | None, lock_account_uid_account_email: str | None, lock_account_uid_display_name: str | None, lock_account_uid_is_system: int | None):
        self.system_lock_uid = system_lock_uid
        self.system_lock_name = system_lock_name
        self.lock_account_uid = lock_account_uid
        self.lock_comment = lock_comment
        self.row_instance = row_instance
        self.row_lock = row_lock
        self.row_owner = row_owner
        self.row_seq = row_seq
        self.row_guid = row_guid
        self.row_version = row_version
        self.is_active = is_active
        self.created_date = created_date
        self.created_by = created_by
        self.last_updated_date = last_updated_date
        self.last_updated_by = last_updated_by
        self.removed_date = removed_date
        self.removed_by = removed_by
        self.custom_attributes = custom_attributes
        self.lock_account_uid_account_name = lock_account_uid_account_name
        self.lock_account_uid_tenant_uid = lock_account_uid_tenant_uid
        self.lock_account_uid_account_type_uid = lock_account_uid_account_type_uid
        self.lock_account_uid_account_title_uid = lock_account_uid_account_title_uid
        self.lock_account_uid_account_division_uid = lock_account_uid_account_division_uid
        self.lock_account_uid_account_group_uid = lock_account_uid_account_group_uid
        self.lock_account_uid_auth_identity_uid = lock_account_uid_auth_identity_uid
        self.lock_account_uid_account_email = lock_account_uid_account_email
        self.lock_account_uid_display_name = lock_account_uid_display_name
        self.lock_account_uid_is_system = lock_account_uid_is_system
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.system_lock_uid, self.system_lock_name, self.lock_account_uid, self.lock_comment, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes, self.lock_account_uid_account_name, self.lock_account_uid_tenant_uid, self.lock_account_uid_account_type_uid, self.lock_account_uid_account_title_uid, self.lock_account_uid_account_division_uid, self.lock_account_uid_account_group_uid, self.lock_account_uid_auth_identity_uid, self.lock_account_uid_account_email, self.lock_account_uid_display_name, self.lock_account_uid_is_system]


@dataclass(frozen=False)
class system_module_rich_dto(system_module_read_dto):
    system_module_uid: str | None
    system_module_name: str | None
    system_module_description: str | None
    row_instance: str | None
    row_lock: str | None
    row_owner: str | None
    row_seq: int | None
    row_guid: str | None
    row_version: int | None
    is_active: int | None
    created_date: datetime.datetime | None
    created_by: str | None
    last_updated_date: datetime.datetime | None
    last_updated_by: str | None
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str | None
    def __init__(self, system_module_uid: str | None, system_module_name: str | None, system_module_description: str | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None):
        self.system_module_uid = system_module_uid
        self.system_module_name = system_module_name
        self.system_module_description = system_module_description
        self.row_instance = row_instance
        self.row_lock = row_lock
        self.row_owner = row_owner
        self.row_seq = row_seq
        self.row_guid = row_guid
        self.row_version = row_version
        self.is_active = is_active
        self.created_date = created_date
        self.created_by = created_by
        self.last_updated_date = last_updated_date
        self.last_updated_by = last_updated_by
        self.removed_date = removed_date
        self.removed_by = removed_by
        self.custom_attributes = custom_attributes
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.system_module_uid, self.system_module_name, self.system_module_description, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]


@dataclass(frozen=False)
class system_object_rich_dto(system_object_read_dto):
    system_object_uid: str | None
    system_object_name: str | None
    system_version_uid: str | None
    system_table_uid: str | None
    system_object_type_uid: str | None
    parent_system_object_uid: str | None
    object_type: str | None
    row_instance: str | None
    row_lock: str | None
    row_owner: str | None
    row_seq: int | None
    row_guid: str | None
    row_version: int | None
    is_active: int | None
    created_date: datetime.datetime | None
    created_by: str | None
    last_updated_date: datetime.datetime | None
    last_updated_by: str | None
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str | None
    system_version_uid_system_version_name: str | None
    system_version_uid_version_description: str | None
    system_table_uid_system_table_name: str | None
    system_table_uid_parent_system_table_uid: str | None
    system_table_uid_key_name: str | None
    system_table_uid_table_code: str | None
    system_table_uid_table_comment: str | None
    system_object_type_uid_system_object_type_name: str | None
    system_object_type_uid_object_type_description: str | None
    def __init__(self, system_object_uid: str | None, system_object_name: str | None, system_version_uid: str | None, system_table_uid: str | None, system_object_type_uid: str | None, parent_system_object_uid: str | None, object_type: str | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None, system_version_uid_system_version_name: str | None, system_version_uid_version_description: str | None, system_table_uid_system_table_name: str | None, system_table_uid_parent_system_table_uid: str | None, system_table_uid_key_name: str | None, system_table_uid_table_code: str | None, system_table_uid_table_comment: str | None, system_object_type_uid_system_object_type_name: str | None, system_object_type_uid_object_type_description: str | None):
        self.system_object_uid = system_object_uid
        self.system_object_name = system_object_name
        self.system_version_uid = system_version_uid
        self.system_table_uid = system_table_uid
        self.system_object_type_uid = system_object_type_uid
        self.parent_system_object_uid = parent_system_object_uid
        self.object_type = object_type
        self.row_instance = row_instance
        self.row_lock = row_lock
        self.row_owner = row_owner
        self.row_seq = row_seq
        self.row_guid = row_guid
        self.row_version = row_version
        self.is_active = is_active
        self.created_date = created_date
        self.created_by = created_by
        self.last_updated_date = last_updated_date
        self.last_updated_by = last_updated_by
        self.removed_date = removed_date
        self.removed_by = removed_by
        self.custom_attributes = custom_attributes
        self.system_version_uid_system_version_name = system_version_uid_system_version_name
        self.system_version_uid_version_description = system_version_uid_version_description
        self.system_table_uid_system_table_name = system_table_uid_system_table_name
        self.system_table_uid_parent_system_table_uid = system_table_uid_parent_system_table_uid
        self.system_table_uid_key_name = system_table_uid_key_name
        self.system_table_uid_table_code = system_table_uid_table_code
        self.system_table_uid_table_comment = system_table_uid_table_comment
        self.system_object_type_uid_system_object_type_name = system_object_type_uid_system_object_type_name
        self.system_object_type_uid_object_type_description = system_object_type_uid_object_type_description
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.system_object_uid, self.system_object_name, self.system_version_uid, self.system_table_uid, self.system_object_type_uid, self.parent_system_object_uid, self.object_type, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes, self.system_version_uid_system_version_name, self.system_version_uid_version_description, self.system_table_uid_system_table_name, self.system_table_uid_parent_system_table_uid, self.system_table_uid_key_name, self.system_table_uid_table_code, self.system_table_uid_table_comment, self.system_object_type_uid_system_object_type_name, self.system_object_type_uid_object_type_description]


@dataclass(frozen=False)
class system_object_type_rich_dto(system_object_type_read_dto):
    system_object_type_uid: str | None
    system_object_type_name: str | None
    object_type_description: str | None
    row_instance: str | None
    row_lock: str | None
    row_owner: str | None
    row_seq: int | None
    row_guid: str | None
    row_version: int | None
    is_active: int | None
    created_date: datetime.datetime | None
    created_by: str | None
    last_updated_date: datetime.datetime | None
    last_updated_by: str | None
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str | None
    def __init__(self, system_object_type_uid: str | None, system_object_type_name: str | None, object_type_description: str | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None):
        self.system_object_type_uid = system_object_type_uid
        self.system_object_type_name = system_object_type_name
        self.object_type_description = object_type_description
        self.row_instance = row_instance
        self.row_lock = row_lock
        self.row_owner = row_owner
        self.row_seq = row_seq
        self.row_guid = row_guid
        self.row_version = row_version
        self.is_active = is_active
        self.created_date = created_date
        self.created_by = created_by
        self.last_updated_date = last_updated_date
        self.last_updated_by = last_updated_by
        self.removed_date = removed_date
        self.removed_by = removed_by
        self.custom_attributes = custom_attributes
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.system_object_type_uid, self.system_object_type_name, self.object_type_description, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]


@dataclass(frozen=False)
class system_query_rich_dto(system_query_read_dto):
    system_query_uid: str | None
    system_query_name: str | None
    time_start: int | None
    total_query_time: int | None
    query_seq: int | None
    execution_counter: int | None
    connection_counter: int | None
    release_counter: int | None
    current_active: int | None
    current_idle: int | None
    table_name: str | None
    rows_count: int | None
    sql: str | None
    row_instance: str | None
    row_lock: str | None
    row_owner: str | None
    row_seq: int | None
    row_guid: str | None
    row_version: int | None
    is_active: int | None
    created_date: datetime.datetime | None
    created_by: str | None
    last_updated_date: datetime.datetime | None
    last_updated_by: str | None
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str | None
    def __init__(self, system_query_uid: str | None, system_query_name: str | None, time_start: int | None, total_query_time: int | None, query_seq: int | None, execution_counter: int | None, connection_counter: int | None, release_counter: int | None, current_active: int | None, current_idle: int | None, table_name: str | None, rows_count: int | None, sql: str | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None):
        self.system_query_uid = system_query_uid
        self.system_query_name = system_query_name
        self.time_start = time_start
        self.total_query_time = total_query_time
        self.query_seq = query_seq
        self.execution_counter = execution_counter
        self.connection_counter = connection_counter
        self.release_counter = release_counter
        self.current_active = current_active
        self.current_idle = current_idle
        self.table_name = table_name
        self.rows_count = rows_count
        self.sql = sql
        self.row_instance = row_instance
        self.row_lock = row_lock
        self.row_owner = row_owner
        self.row_seq = row_seq
        self.row_guid = row_guid
        self.row_version = row_version
        self.is_active = is_active
        self.created_date = created_date
        self.created_by = created_by
        self.last_updated_date = last_updated_date
        self.last_updated_by = last_updated_by
        self.removed_date = removed_date
        self.removed_by = removed_by
        self.custom_attributes = custom_attributes
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.system_query_uid, self.system_query_name, self.time_start, self.total_query_time, self.query_seq, self.execution_counter, self.connection_counter, self.release_counter, self.current_active, self.current_idle, self.table_name, self.rows_count, self.sql, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]


@dataclass(frozen=False)
class system_request_rich_dto(system_request_read_dto):
    system_request_uid: str | None
    system_request_name: str | None
    account_uid: str | None
    request_method: str | None
    request_url: str | None
    request_body_size: int | None
    request_host: str | None
    request_time: int | None
    response_code: int | None
    row_instance: str | None
    row_lock: str | None
    row_owner: str | None
    row_seq: int | None
    row_guid: str | None
    row_version: int | None
    is_active: int | None
    created_date: datetime.datetime | None
    created_by: str | None
    last_updated_date: datetime.datetime | None
    last_updated_by: str | None
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str | None
    account_uid_account_name: str | None
    account_uid_tenant_uid: str | None
    account_uid_account_type_uid: str | None
    account_uid_account_title_uid: str | None
    account_uid_account_division_uid: str | None
    account_uid_account_group_uid: str | None
    account_uid_auth_identity_uid: str | None
    account_uid_account_email: str | None
    account_uid_display_name: str | None
    account_uid_is_system: int | None
    def __init__(self, system_request_uid: str | None, system_request_name: str | None, account_uid: str | None, request_method: str | None, request_url: str | None, request_body_size: int | None, request_host: str | None, request_time: int | None, response_code: int | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None, account_uid_account_name: str | None, account_uid_tenant_uid: str | None, account_uid_account_type_uid: str | None, account_uid_account_title_uid: str | None, account_uid_account_division_uid: str | None, account_uid_account_group_uid: str | None, account_uid_auth_identity_uid: str | None, account_uid_account_email: str | None, account_uid_display_name: str | None, account_uid_is_system: int | None):
        self.system_request_uid = system_request_uid
        self.system_request_name = system_request_name
        self.account_uid = account_uid
        self.request_method = request_method
        self.request_url = request_url
        self.request_body_size = request_body_size
        self.request_host = request_host
        self.request_time = request_time
        self.response_code = response_code
        self.row_instance = row_instance
        self.row_lock = row_lock
        self.row_owner = row_owner
        self.row_seq = row_seq
        self.row_guid = row_guid
        self.row_version = row_version
        self.is_active = is_active
        self.created_date = created_date
        self.created_by = created_by
        self.last_updated_date = last_updated_date
        self.last_updated_by = last_updated_by
        self.removed_date = removed_date
        self.removed_by = removed_by
        self.custom_attributes = custom_attributes
        self.account_uid_account_name = account_uid_account_name
        self.account_uid_tenant_uid = account_uid_tenant_uid
        self.account_uid_account_type_uid = account_uid_account_type_uid
        self.account_uid_account_title_uid = account_uid_account_title_uid
        self.account_uid_account_division_uid = account_uid_account_division_uid
        self.account_uid_account_group_uid = account_uid_account_group_uid
        self.account_uid_auth_identity_uid = account_uid_auth_identity_uid
        self.account_uid_account_email = account_uid_account_email
        self.account_uid_display_name = account_uid_display_name
        self.account_uid_is_system = account_uid_is_system
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.system_request_uid, self.system_request_name, self.account_uid, self.request_method, self.request_url, self.request_body_size, self.request_host, self.request_time, self.response_code, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes, self.account_uid_account_name, self.account_uid_tenant_uid, self.account_uid_account_type_uid, self.account_uid_account_title_uid, self.account_uid_account_division_uid, self.account_uid_account_group_uid, self.account_uid_auth_identity_uid, self.account_uid_account_email, self.account_uid_display_name, self.account_uid_is_system]


@dataclass(frozen=False)
class system_setting_rich_dto(system_setting_read_dto):
    system_setting_uid: str | None
    system_setting_name: str | None
    setting_value: str | None
    row_instance: str | None
    row_lock: str | None
    row_owner: str | None
    row_seq: int | None
    row_guid: str | None
    row_version: int | None
    is_active: int | None
    created_date: datetime.datetime | None
    created_by: str | None
    last_updated_date: datetime.datetime | None
    last_updated_by: str | None
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str | None
    def __init__(self, system_setting_uid: str | None, system_setting_name: str | None, setting_value: str | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None):
        self.system_setting_uid = system_setting_uid
        self.system_setting_name = system_setting_name
        self.setting_value = setting_value
        self.row_instance = row_instance
        self.row_lock = row_lock
        self.row_owner = row_owner
        self.row_seq = row_seq
        self.row_guid = row_guid
        self.row_version = row_version
        self.is_active = is_active
        self.created_date = created_date
        self.created_by = created_by
        self.last_updated_date = last_updated_date
        self.last_updated_by = last_updated_by
        self.removed_date = removed_date
        self.removed_by = removed_by
        self.custom_attributes = custom_attributes
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.system_setting_uid, self.system_setting_name, self.setting_value, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]


@dataclass(frozen=False)
class system_setting_account_rich_dto(system_setting_account_read_dto):
    system_setting_account_uid: str | None
    system_setting_account_name: str | None
    account_uid: str | None
    setting_value: str | None
    is_public: int | None
    row_instance: str | None
    row_lock: str | None
    row_owner: str | None
    row_seq: int | None
    row_guid: str | None
    row_version: int | None
    is_active: int | None
    created_date: datetime.datetime | None
    created_by: str | None
    last_updated_date: datetime.datetime | None
    last_updated_by: str | None
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str | None
    system_setting_account_uid_account_name: str | None
    system_setting_account_uid_tenant_uid: str | None
    system_setting_account_uid_account_type_uid: str | None
    system_setting_account_uid_account_title_uid: str | None
    system_setting_account_uid_account_division_uid: str | None
    system_setting_account_uid_account_group_uid: str | None
    system_setting_account_uid_auth_identity_uid: str | None
    system_setting_account_uid_account_email: str | None
    system_setting_account_uid_display_name: str | None
    system_setting_account_uid_is_system: int | None
    account_uid_account_name: str | None
    account_uid_tenant_uid: str | None
    account_uid_account_type_uid: str | None
    account_uid_account_title_uid: str | None
    account_uid_account_division_uid: str | None
    account_uid_account_group_uid: str | None
    account_uid_auth_identity_uid: str | None
    account_uid_account_email: str | None
    account_uid_display_name: str | None
    account_uid_is_system: int | None
    def __init__(self, system_setting_account_uid: str | None, system_setting_account_name: str | None, account_uid: str | None, setting_value: str | None, is_public: int | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None, system_setting_account_uid_account_name: str | None, system_setting_account_uid_tenant_uid: str | None, system_setting_account_uid_account_type_uid: str | None, system_setting_account_uid_account_title_uid: str | None, system_setting_account_uid_account_division_uid: str | None, system_setting_account_uid_account_group_uid: str | None, system_setting_account_uid_auth_identity_uid: str | None, system_setting_account_uid_account_email: str | None, system_setting_account_uid_display_name: str | None, system_setting_account_uid_is_system: int | None, account_uid_account_name: str | None, account_uid_tenant_uid: str | None, account_uid_account_type_uid: str | None, account_uid_account_title_uid: str | None, account_uid_account_division_uid: str | None, account_uid_account_group_uid: str | None, account_uid_auth_identity_uid: str | None, account_uid_account_email: str | None, account_uid_display_name: str | None, account_uid_is_system: int | None):
        self.system_setting_account_uid = system_setting_account_uid
        self.system_setting_account_name = system_setting_account_name
        self.account_uid = account_uid
        self.setting_value = setting_value
        self.is_public = is_public
        self.row_instance = row_instance
        self.row_lock = row_lock
        self.row_owner = row_owner
        self.row_seq = row_seq
        self.row_guid = row_guid
        self.row_version = row_version
        self.is_active = is_active
        self.created_date = created_date
        self.created_by = created_by
        self.last_updated_date = last_updated_date
        self.last_updated_by = last_updated_by
        self.removed_date = removed_date
        self.removed_by = removed_by
        self.custom_attributes = custom_attributes
        self.system_setting_account_uid_account_name = system_setting_account_uid_account_name
        self.system_setting_account_uid_tenant_uid = system_setting_account_uid_tenant_uid
        self.system_setting_account_uid_account_type_uid = system_setting_account_uid_account_type_uid
        self.system_setting_account_uid_account_title_uid = system_setting_account_uid_account_title_uid
        self.system_setting_account_uid_account_division_uid = system_setting_account_uid_account_division_uid
        self.system_setting_account_uid_account_group_uid = system_setting_account_uid_account_group_uid
        self.system_setting_account_uid_auth_identity_uid = system_setting_account_uid_auth_identity_uid
        self.system_setting_account_uid_account_email = system_setting_account_uid_account_email
        self.system_setting_account_uid_display_name = system_setting_account_uid_display_name
        self.system_setting_account_uid_is_system = system_setting_account_uid_is_system
        self.account_uid_account_name = account_uid_account_name
        self.account_uid_tenant_uid = account_uid_tenant_uid
        self.account_uid_account_type_uid = account_uid_account_type_uid
        self.account_uid_account_title_uid = account_uid_account_title_uid
        self.account_uid_account_division_uid = account_uid_account_division_uid
        self.account_uid_account_group_uid = account_uid_account_group_uid
        self.account_uid_auth_identity_uid = account_uid_auth_identity_uid
        self.account_uid_account_email = account_uid_account_email
        self.account_uid_display_name = account_uid_display_name
        self.account_uid_is_system = account_uid_is_system
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.system_setting_account_uid, self.system_setting_account_name, self.account_uid, self.setting_value, self.is_public, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes, self.system_setting_account_uid_account_name, self.system_setting_account_uid_tenant_uid, self.system_setting_account_uid_account_type_uid, self.system_setting_account_uid_account_title_uid, self.system_setting_account_uid_account_division_uid, self.system_setting_account_uid_account_group_uid, self.system_setting_account_uid_auth_identity_uid, self.system_setting_account_uid_account_email, self.system_setting_account_uid_display_name, self.system_setting_account_uid_is_system, self.account_uid_account_name, self.account_uid_tenant_uid, self.account_uid_account_type_uid, self.account_uid_account_title_uid, self.account_uid_account_division_uid, self.account_uid_account_group_uid, self.account_uid_auth_identity_uid, self.account_uid_account_email, self.account_uid_display_name, self.account_uid_is_system]


@dataclass(frozen=False)
class system_state_rich_dto(system_state_read_dto):
    system_state_uid: str | None
    system_state_name: str | None
    mem_free: int | None
    mem_max: int | None
    objects_count: int | None
    row_instance: str | None
    row_lock: str | None
    row_owner: str | None
    row_seq: int | None
    row_guid: str | None
    row_version: int | None
    is_active: int | None
    created_date: datetime.datetime | None
    created_by: str | None
    last_updated_date: datetime.datetime | None
    last_updated_by: str | None
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str | None
    def __init__(self, system_state_uid: str | None, system_state_name: str | None, mem_free: int | None, mem_max: int | None, objects_count: int | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None):
        self.system_state_uid = system_state_uid
        self.system_state_name = system_state_name
        self.mem_free = mem_free
        self.mem_max = mem_max
        self.objects_count = objects_count
        self.row_instance = row_instance
        self.row_lock = row_lock
        self.row_owner = row_owner
        self.row_seq = row_seq
        self.row_guid = row_guid
        self.row_version = row_version
        self.is_active = is_active
        self.created_date = created_date
        self.created_by = created_by
        self.last_updated_date = last_updated_date
        self.last_updated_by = last_updated_by
        self.removed_date = removed_date
        self.removed_by = removed_by
        self.custom_attributes = custom_attributes
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.system_state_uid, self.system_state_name, self.mem_free, self.mem_max, self.objects_count, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]


@dataclass(frozen=False)
class system_table_rich_dto(system_table_read_dto):
    system_table_uid: str | None
    system_table_name: str | None
    parent_system_table_uid: str | None
    key_name: str | None
    table_code: str | None
    table_comment: str | None
    row_instance: str | None
    row_lock: str | None
    row_owner: str | None
    row_seq: int | None
    row_guid: str | None
    row_version: int | None
    is_active: int | None
    created_date: datetime.datetime | None
    created_by: str | None
    last_updated_date: datetime.datetime | None
    last_updated_by: str | None
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str | None
    def __init__(self, system_table_uid: str | None, system_table_name: str | None, parent_system_table_uid: str | None, key_name: str | None, table_code: str | None, table_comment: str | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None):
        self.system_table_uid = system_table_uid
        self.system_table_name = system_table_name
        self.parent_system_table_uid = parent_system_table_uid
        self.key_name = key_name
        self.table_code = table_code
        self.table_comment = table_comment
        self.row_instance = row_instance
        self.row_lock = row_lock
        self.row_owner = row_owner
        self.row_seq = row_seq
        self.row_guid = row_guid
        self.row_version = row_version
        self.is_active = is_active
        self.created_date = created_date
        self.created_by = created_by
        self.last_updated_date = last_updated_date
        self.last_updated_by = last_updated_by
        self.removed_date = removed_date
        self.removed_by = removed_by
        self.custom_attributes = custom_attributes
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.system_table_uid, self.system_table_name, self.parent_system_table_uid, self.key_name, self.table_code, self.table_comment, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]


@dataclass(frozen=False)
class system_thread_rich_dto(system_thread_read_dto):
    system_thread_uid: str | None
    system_thread_name: str | None
    thread_name: str | None
    parent_object: str | None
    ticks_count: int | None
    sleep_time: int | None
    row_instance: str | None
    row_lock: str | None
    row_owner: str | None
    row_seq: int | None
    row_guid: str | None
    row_version: int | None
    is_active: int | None
    created_date: datetime.datetime | None
    created_by: str | None
    last_updated_date: datetime.datetime | None
    last_updated_by: str | None
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str | None
    def __init__(self, system_thread_uid: str | None, system_thread_name: str | None, thread_name: str | None, parent_object: str | None, ticks_count: int | None, sleep_time: int | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None):
        self.system_thread_uid = system_thread_uid
        self.system_thread_name = system_thread_name
        self.thread_name = thread_name
        self.parent_object = parent_object
        self.ticks_count = ticks_count
        self.sleep_time = sleep_time
        self.row_instance = row_instance
        self.row_lock = row_lock
        self.row_owner = row_owner
        self.row_seq = row_seq
        self.row_guid = row_guid
        self.row_version = row_version
        self.is_active = is_active
        self.created_date = created_date
        self.created_by = created_by
        self.last_updated_date = last_updated_date
        self.last_updated_by = last_updated_by
        self.removed_date = removed_date
        self.removed_by = removed_by
        self.custom_attributes = custom_attributes
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.system_thread_uid, self.system_thread_name, self.thread_name, self.parent_object, self.ticks_count, self.sleep_time, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]


@dataclass(frozen=False)
class system_version_rich_dto(system_version_read_dto):
    system_version_uid: str | None
    system_version_name: str | None
    version_description: str | None
    row_instance: str | None
    row_lock: str | None
    row_owner: str | None
    row_seq: int | None
    row_guid: str | None
    row_version: int | None
    is_active: int | None
    created_date: datetime.datetime | None
    created_by: str | None
    last_updated_date: datetime.datetime | None
    last_updated_by: str | None
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str | None
    def __init__(self, system_version_uid: str | None, system_version_name: str | None, version_description: str | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None):
        self.system_version_uid = system_version_uid
        self.system_version_name = system_version_name
        self.version_description = version_description
        self.row_instance = row_instance
        self.row_lock = row_lock
        self.row_owner = row_owner
        self.row_seq = row_seq
        self.row_guid = row_guid
        self.row_version = row_version
        self.is_active = is_active
        self.created_date = created_date
        self.created_by = created_by
        self.last_updated_date = last_updated_date
        self.last_updated_by = last_updated_by
        self.removed_date = removed_date
        self.removed_by = removed_by
        self.custom_attributes = custom_attributes
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.system_version_uid, self.system_version_name, self.version_description, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]


@dataclass(frozen=False)
class tenant_rich_dto(tenant_read_dto):
    tenant_uid: str | None
    tenant_name: str | None
    country_uid: str | None
    tenant_type_uid: str | None
    tenant_category_uid: str | None
    tenant_code: str | None
    tenant_description: str | None
    start_date: datetime.datetime | None
    end_date: datetime.datetime | None
    is_internal: int | None
    is_system: int | None
    is_test: int | None
    account_uid: str | None
    row_instance: str | None
    row_lock: str | None
    row_owner: str | None
    row_seq: int | None
    row_guid: str | None
    row_version: int | None
    is_active: int | None
    created_date: datetime.datetime | None
    created_by: str | None
    last_updated_date: datetime.datetime | None
    last_updated_by: str | None
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str | None
    country_uid_country_name: str | None
    country_uid_continent_name: str | None
    country_uid_continent_code: str | None
    country_uid_country_iso3: str | None
    country_uid_country_code: str | None
    country_uid_phone_code: str | None
    country_uid_currency_code: str | None
    country_uid_capital_name: str | None
    country_uid_region_name: str | None
    country_uid_subregion_name: str | None
    country_uid_region_code: str | None
    country_uid_latitude: str | None
    country_uid_longitude: str | None
    country_uid_currency_name: str | None
    country_uid_population: str | None
    country_uid_languages: str | None
    country_uid_area: str | None
    country_uid_bar_code: str | None
    country_uid_top_level_domain: str | None
    country_uid_is_focused: int | None
    tenant_type_uid_tenant_type_name: str | None
    tenant_type_uid_tenant_type_description: str | None
    tenant_category_uid_tenant_category_name: str | None
    tenant_category_uid_tenant_category_description: str | None
    account_uid_account_name: str | None
    account_uid_tenant_uid: str | None
    account_uid_account_type_uid: str | None
    account_uid_account_title_uid: str | None
    account_uid_account_division_uid: str | None
    account_uid_account_group_uid: str | None
    account_uid_auth_identity_uid: str | None
    account_uid_account_email: str | None
    account_uid_display_name: str | None
    account_uid_is_system: int | None
    def __init__(self, tenant_uid: str | None, tenant_name: str | None, country_uid: str | None, tenant_type_uid: str | None, tenant_category_uid: str | None, tenant_code: str | None, tenant_description: str | None, start_date: datetime.datetime | None, end_date: datetime.datetime | None, is_internal: int | None, is_system: int | None, is_test: int | None, account_uid: str | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None, country_uid_country_name: str | None, country_uid_continent_name: str | None, country_uid_continent_code: str | None, country_uid_country_iso3: str | None, country_uid_country_code: str | None, country_uid_phone_code: str | None, country_uid_currency_code: str | None, country_uid_capital_name: str | None, country_uid_region_name: str | None, country_uid_subregion_name: str | None, country_uid_region_code: str | None, country_uid_latitude: str | None, country_uid_longitude: str | None, country_uid_currency_name: str | None, country_uid_population: str | None, country_uid_languages: str | None, country_uid_area: str | None, country_uid_bar_code: str | None, country_uid_top_level_domain: str | None, country_uid_is_focused: int | None, tenant_type_uid_tenant_type_name: str | None, tenant_type_uid_tenant_type_description: str | None, tenant_category_uid_tenant_category_name: str | None, tenant_category_uid_tenant_category_description: str | None, account_uid_account_name: str | None, account_uid_tenant_uid: str | None, account_uid_account_type_uid: str | None, account_uid_account_title_uid: str | None, account_uid_account_division_uid: str | None, account_uid_account_group_uid: str | None, account_uid_auth_identity_uid: str | None, account_uid_account_email: str | None, account_uid_display_name: str | None, account_uid_is_system: int | None):
        self.tenant_uid = tenant_uid
        self.tenant_name = tenant_name
        self.country_uid = country_uid
        self.tenant_type_uid = tenant_type_uid
        self.tenant_category_uid = tenant_category_uid
        self.tenant_code = tenant_code
        self.tenant_description = tenant_description
        self.start_date = start_date
        self.end_date = end_date
        self.is_internal = is_internal
        self.is_system = is_system
        self.is_test = is_test
        self.account_uid = account_uid
        self.row_instance = row_instance
        self.row_lock = row_lock
        self.row_owner = row_owner
        self.row_seq = row_seq
        self.row_guid = row_guid
        self.row_version = row_version
        self.is_active = is_active
        self.created_date = created_date
        self.created_by = created_by
        self.last_updated_date = last_updated_date
        self.last_updated_by = last_updated_by
        self.removed_date = removed_date
        self.removed_by = removed_by
        self.custom_attributes = custom_attributes
        self.country_uid_country_name = country_uid_country_name
        self.country_uid_continent_name = country_uid_continent_name
        self.country_uid_continent_code = country_uid_continent_code
        self.country_uid_country_iso3 = country_uid_country_iso3
        self.country_uid_country_code = country_uid_country_code
        self.country_uid_phone_code = country_uid_phone_code
        self.country_uid_currency_code = country_uid_currency_code
        self.country_uid_capital_name = country_uid_capital_name
        self.country_uid_region_name = country_uid_region_name
        self.country_uid_subregion_name = country_uid_subregion_name
        self.country_uid_region_code = country_uid_region_code
        self.country_uid_latitude = country_uid_latitude
        self.country_uid_longitude = country_uid_longitude
        self.country_uid_currency_name = country_uid_currency_name
        self.country_uid_population = country_uid_population
        self.country_uid_languages = country_uid_languages
        self.country_uid_area = country_uid_area
        self.country_uid_bar_code = country_uid_bar_code
        self.country_uid_top_level_domain = country_uid_top_level_domain
        self.country_uid_is_focused = country_uid_is_focused
        self.tenant_type_uid_tenant_type_name = tenant_type_uid_tenant_type_name
        self.tenant_type_uid_tenant_type_description = tenant_type_uid_tenant_type_description
        self.tenant_category_uid_tenant_category_name = tenant_category_uid_tenant_category_name
        self.tenant_category_uid_tenant_category_description = tenant_category_uid_tenant_category_description
        self.account_uid_account_name = account_uid_account_name
        self.account_uid_tenant_uid = account_uid_tenant_uid
        self.account_uid_account_type_uid = account_uid_account_type_uid
        self.account_uid_account_title_uid = account_uid_account_title_uid
        self.account_uid_account_division_uid = account_uid_account_division_uid
        self.account_uid_account_group_uid = account_uid_account_group_uid
        self.account_uid_auth_identity_uid = account_uid_auth_identity_uid
        self.account_uid_account_email = account_uid_account_email
        self.account_uid_display_name = account_uid_display_name
        self.account_uid_is_system = account_uid_is_system
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.tenant_uid, self.tenant_name, self.country_uid, self.tenant_type_uid, self.tenant_category_uid, self.tenant_code, self.tenant_description, self.start_date, self.end_date, self.is_internal, self.is_system, self.is_test, self.account_uid, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes, self.country_uid_country_name, self.country_uid_continent_name, self.country_uid_continent_code, self.country_uid_country_iso3, self.country_uid_country_code, self.country_uid_phone_code, self.country_uid_currency_code, self.country_uid_capital_name, self.country_uid_region_name, self.country_uid_subregion_name, self.country_uid_region_code, self.country_uid_latitude, self.country_uid_longitude, self.country_uid_currency_name, self.country_uid_population, self.country_uid_languages, self.country_uid_area, self.country_uid_bar_code, self.country_uid_top_level_domain, self.country_uid_is_focused, self.tenant_type_uid_tenant_type_name, self.tenant_type_uid_tenant_type_description, self.tenant_category_uid_tenant_category_name, self.tenant_category_uid_tenant_category_description, self.account_uid_account_name, self.account_uid_tenant_uid, self.account_uid_account_type_uid, self.account_uid_account_title_uid, self.account_uid_account_division_uid, self.account_uid_account_group_uid, self.account_uid_auth_identity_uid, self.account_uid_account_email, self.account_uid_display_name, self.account_uid_is_system]


@dataclass(frozen=False)
class tenant_account_rich_dto(tenant_account_read_dto):
    tenant_account_uid: str | None
    tenant_account_name: str | None
    tenant_uid: str | None
    account_uid: str | None
    tenant_role_uid: str | None
    row_instance: str | None
    row_lock: str | None
    row_owner: str | None
    row_seq: int | None
    row_guid: str | None
    row_version: int | None
    is_active: int | None
    created_date: datetime.datetime | None
    created_by: str | None
    last_updated_date: datetime.datetime | None
    last_updated_by: str | None
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str | None
    tenant_account_uid_account_name: str | None
    tenant_account_uid_tenant_uid: str | None
    tenant_account_uid_account_type_uid: str | None
    tenant_account_uid_account_title_uid: str | None
    tenant_account_uid_account_division_uid: str | None
    tenant_account_uid_account_group_uid: str | None
    tenant_account_uid_auth_identity_uid: str | None
    tenant_account_uid_account_email: str | None
    tenant_account_uid_display_name: str | None
    tenant_account_uid_is_system: int | None
    tenant_uid_tenant_name: str | None
    tenant_uid_country_uid: str | None
    tenant_uid_tenant_type_uid: str | None
    tenant_uid_tenant_category_uid: str | None
    tenant_uid_tenant_code: str | None
    tenant_uid_tenant_description: str | None
    tenant_uid_start_date: datetime.datetime | None
    tenant_uid_end_date: datetime.datetime | None
    tenant_uid_is_internal: int | None
    tenant_uid_is_system: int | None
    tenant_uid_is_test: int | None
    tenant_uid_account_uid: str | None
    account_uid_account_name: str | None
    account_uid_tenant_uid: str | None
    account_uid_account_type_uid: str | None
    account_uid_account_title_uid: str | None
    account_uid_account_division_uid: str | None
    account_uid_account_group_uid: str | None
    account_uid_auth_identity_uid: str | None
    account_uid_account_email: str | None
    account_uid_display_name: str | None
    account_uid_is_system: int | None
    tenant_role_uid_tenant_role_name: str | None
    tenant_role_uid_role_description: str | None
    def __init__(self, tenant_account_uid: str | None, tenant_account_name: str | None, tenant_uid: str | None, account_uid: str | None, tenant_role_uid: str | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None, tenant_account_uid_account_name: str | None, tenant_account_uid_tenant_uid: str | None, tenant_account_uid_account_type_uid: str | None, tenant_account_uid_account_title_uid: str | None, tenant_account_uid_account_division_uid: str | None, tenant_account_uid_account_group_uid: str | None, tenant_account_uid_auth_identity_uid: str | None, tenant_account_uid_account_email: str | None, tenant_account_uid_display_name: str | None, tenant_account_uid_is_system: int | None, tenant_uid_tenant_name: str | None, tenant_uid_country_uid: str | None, tenant_uid_tenant_type_uid: str | None, tenant_uid_tenant_category_uid: str | None, tenant_uid_tenant_code: str | None, tenant_uid_tenant_description: str | None, tenant_uid_start_date: datetime.datetime | None, tenant_uid_end_date: datetime.datetime | None, tenant_uid_is_internal: int | None, tenant_uid_is_system: int | None, tenant_uid_is_test: int | None, tenant_uid_account_uid: str | None, account_uid_account_name: str | None, account_uid_tenant_uid: str | None, account_uid_account_type_uid: str | None, account_uid_account_title_uid: str | None, account_uid_account_division_uid: str | None, account_uid_account_group_uid: str | None, account_uid_auth_identity_uid: str | None, account_uid_account_email: str | None, account_uid_display_name: str | None, account_uid_is_system: int | None, tenant_role_uid_tenant_role_name: str | None, tenant_role_uid_role_description: str | None):
        self.tenant_account_uid = tenant_account_uid
        self.tenant_account_name = tenant_account_name
        self.tenant_uid = tenant_uid
        self.account_uid = account_uid
        self.tenant_role_uid = tenant_role_uid
        self.row_instance = row_instance
        self.row_lock = row_lock
        self.row_owner = row_owner
        self.row_seq = row_seq
        self.row_guid = row_guid
        self.row_version = row_version
        self.is_active = is_active
        self.created_date = created_date
        self.created_by = created_by
        self.last_updated_date = last_updated_date
        self.last_updated_by = last_updated_by
        self.removed_date = removed_date
        self.removed_by = removed_by
        self.custom_attributes = custom_attributes
        self.tenant_account_uid_account_name = tenant_account_uid_account_name
        self.tenant_account_uid_tenant_uid = tenant_account_uid_tenant_uid
        self.tenant_account_uid_account_type_uid = tenant_account_uid_account_type_uid
        self.tenant_account_uid_account_title_uid = tenant_account_uid_account_title_uid
        self.tenant_account_uid_account_division_uid = tenant_account_uid_account_division_uid
        self.tenant_account_uid_account_group_uid = tenant_account_uid_account_group_uid
        self.tenant_account_uid_auth_identity_uid = tenant_account_uid_auth_identity_uid
        self.tenant_account_uid_account_email = tenant_account_uid_account_email
        self.tenant_account_uid_display_name = tenant_account_uid_display_name
        self.tenant_account_uid_is_system = tenant_account_uid_is_system
        self.tenant_uid_tenant_name = tenant_uid_tenant_name
        self.tenant_uid_country_uid = tenant_uid_country_uid
        self.tenant_uid_tenant_type_uid = tenant_uid_tenant_type_uid
        self.tenant_uid_tenant_category_uid = tenant_uid_tenant_category_uid
        self.tenant_uid_tenant_code = tenant_uid_tenant_code
        self.tenant_uid_tenant_description = tenant_uid_tenant_description
        self.tenant_uid_start_date = tenant_uid_start_date
        self.tenant_uid_end_date = tenant_uid_end_date
        self.tenant_uid_is_internal = tenant_uid_is_internal
        self.tenant_uid_is_system = tenant_uid_is_system
        self.tenant_uid_is_test = tenant_uid_is_test
        self.tenant_uid_account_uid = tenant_uid_account_uid
        self.account_uid_account_name = account_uid_account_name
        self.account_uid_tenant_uid = account_uid_tenant_uid
        self.account_uid_account_type_uid = account_uid_account_type_uid
        self.account_uid_account_title_uid = account_uid_account_title_uid
        self.account_uid_account_division_uid = account_uid_account_division_uid
        self.account_uid_account_group_uid = account_uid_account_group_uid
        self.account_uid_auth_identity_uid = account_uid_auth_identity_uid
        self.account_uid_account_email = account_uid_account_email
        self.account_uid_display_name = account_uid_display_name
        self.account_uid_is_system = account_uid_is_system
        self.tenant_role_uid_tenant_role_name = tenant_role_uid_tenant_role_name
        self.tenant_role_uid_role_description = tenant_role_uid_role_description
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.tenant_account_uid, self.tenant_account_name, self.tenant_uid, self.account_uid, self.tenant_role_uid, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes, self.tenant_account_uid_account_name, self.tenant_account_uid_tenant_uid, self.tenant_account_uid_account_type_uid, self.tenant_account_uid_account_title_uid, self.tenant_account_uid_account_division_uid, self.tenant_account_uid_account_group_uid, self.tenant_account_uid_auth_identity_uid, self.tenant_account_uid_account_email, self.tenant_account_uid_display_name, self.tenant_account_uid_is_system, self.tenant_uid_tenant_name, self.tenant_uid_country_uid, self.tenant_uid_tenant_type_uid, self.tenant_uid_tenant_category_uid, self.tenant_uid_tenant_code, self.tenant_uid_tenant_description, self.tenant_uid_start_date, self.tenant_uid_end_date, self.tenant_uid_is_internal, self.tenant_uid_is_system, self.tenant_uid_is_test, self.tenant_uid_account_uid, self.account_uid_account_name, self.account_uid_tenant_uid, self.account_uid_account_type_uid, self.account_uid_account_title_uid, self.account_uid_account_division_uid, self.account_uid_account_group_uid, self.account_uid_auth_identity_uid, self.account_uid_account_email, self.account_uid_display_name, self.account_uid_is_system, self.tenant_role_uid_tenant_role_name, self.tenant_role_uid_role_description]


@dataclass(frozen=False)
class tenant_category_rich_dto(tenant_category_read_dto):
    tenant_category_uid: str | None
    tenant_category_name: str | None
    tenant_category_description: str | None
    row_instance: str | None
    row_lock: str | None
    row_owner: str | None
    row_seq: int | None
    row_guid: str | None
    row_version: int | None
    is_active: int | None
    created_date: datetime.datetime | None
    created_by: str | None
    last_updated_date: datetime.datetime | None
    last_updated_by: str | None
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str | None
    def __init__(self, tenant_category_uid: str | None, tenant_category_name: str | None, tenant_category_description: str | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None):
        self.tenant_category_uid = tenant_category_uid
        self.tenant_category_name = tenant_category_name
        self.tenant_category_description = tenant_category_description
        self.row_instance = row_instance
        self.row_lock = row_lock
        self.row_owner = row_owner
        self.row_seq = row_seq
        self.row_guid = row_guid
        self.row_version = row_version
        self.is_active = is_active
        self.created_date = created_date
        self.created_by = created_by
        self.last_updated_date = last_updated_date
        self.last_updated_by = last_updated_by
        self.removed_date = removed_date
        self.removed_by = removed_by
        self.custom_attributes = custom_attributes
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.tenant_category_uid, self.tenant_category_name, self.tenant_category_description, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]


@dataclass(frozen=False)
class tenant_country_rich_dto(tenant_country_read_dto):
    tenant_country_uid: str | None
    tenant_country_name: str | None
    country_uid: str | None
    tenant_uid: str | None
    country_priority: int | None
    row_instance: str | None
    row_lock: str | None
    row_owner: str | None
    row_seq: int | None
    row_guid: str | None
    row_version: int | None
    is_active: int | None
    created_date: datetime.datetime | None
    created_by: str | None
    last_updated_date: datetime.datetime | None
    last_updated_by: str | None
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str | None
    tenant_country_uid_country_name: str | None
    tenant_country_uid_continent_name: str | None
    tenant_country_uid_continent_code: str | None
    tenant_country_uid_country_iso3: str | None
    tenant_country_uid_country_code: str | None
    tenant_country_uid_phone_code: str | None
    tenant_country_uid_currency_code: str | None
    tenant_country_uid_capital_name: str | None
    tenant_country_uid_region_name: str | None
    tenant_country_uid_subregion_name: str | None
    tenant_country_uid_region_code: str | None
    tenant_country_uid_latitude: str | None
    tenant_country_uid_longitude: str | None
    tenant_country_uid_currency_name: str | None
    tenant_country_uid_population: str | None
    tenant_country_uid_languages: str | None
    tenant_country_uid_area: str | None
    tenant_country_uid_bar_code: str | None
    tenant_country_uid_top_level_domain: str | None
    tenant_country_uid_is_focused: int | None
    country_uid_country_name: str | None
    country_uid_continent_name: str | None
    country_uid_continent_code: str | None
    country_uid_country_iso3: str | None
    country_uid_country_code: str | None
    country_uid_phone_code: str | None
    country_uid_currency_code: str | None
    country_uid_capital_name: str | None
    country_uid_region_name: str | None
    country_uid_subregion_name: str | None
    country_uid_region_code: str | None
    country_uid_latitude: str | None
    country_uid_longitude: str | None
    country_uid_currency_name: str | None
    country_uid_population: str | None
    country_uid_languages: str | None
    country_uid_area: str | None
    country_uid_bar_code: str | None
    country_uid_top_level_domain: str | None
    country_uid_is_focused: int | None
    tenant_uid_tenant_name: str | None
    tenant_uid_country_uid: str | None
    tenant_uid_tenant_type_uid: str | None
    tenant_uid_tenant_category_uid: str | None
    tenant_uid_tenant_code: str | None
    tenant_uid_tenant_description: str | None
    tenant_uid_start_date: datetime.datetime | None
    tenant_uid_end_date: datetime.datetime | None
    tenant_uid_is_internal: int | None
    tenant_uid_is_system: int | None
    tenant_uid_is_test: int | None
    tenant_uid_account_uid: str | None
    def __init__(self, tenant_country_uid: str | None, tenant_country_name: str | None, country_uid: str | None, tenant_uid: str | None, country_priority: int | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None, tenant_country_uid_country_name: str | None, tenant_country_uid_continent_name: str | None, tenant_country_uid_continent_code: str | None, tenant_country_uid_country_iso3: str | None, tenant_country_uid_country_code: str | None, tenant_country_uid_phone_code: str | None, tenant_country_uid_currency_code: str | None, tenant_country_uid_capital_name: str | None, tenant_country_uid_region_name: str | None, tenant_country_uid_subregion_name: str | None, tenant_country_uid_region_code: str | None, tenant_country_uid_latitude: str | None, tenant_country_uid_longitude: str | None, tenant_country_uid_currency_name: str | None, tenant_country_uid_population: str | None, tenant_country_uid_languages: str | None, tenant_country_uid_area: str | None, tenant_country_uid_bar_code: str | None, tenant_country_uid_top_level_domain: str | None, tenant_country_uid_is_focused: int | None, country_uid_country_name: str | None, country_uid_continent_name: str | None, country_uid_continent_code: str | None, country_uid_country_iso3: str | None, country_uid_country_code: str | None, country_uid_phone_code: str | None, country_uid_currency_code: str | None, country_uid_capital_name: str | None, country_uid_region_name: str | None, country_uid_subregion_name: str | None, country_uid_region_code: str | None, country_uid_latitude: str | None, country_uid_longitude: str | None, country_uid_currency_name: str | None, country_uid_population: str | None, country_uid_languages: str | None, country_uid_area: str | None, country_uid_bar_code: str | None, country_uid_top_level_domain: str | None, country_uid_is_focused: int | None, tenant_uid_tenant_name: str | None, tenant_uid_country_uid: str | None, tenant_uid_tenant_type_uid: str | None, tenant_uid_tenant_category_uid: str | None, tenant_uid_tenant_code: str | None, tenant_uid_tenant_description: str | None, tenant_uid_start_date: datetime.datetime | None, tenant_uid_end_date: datetime.datetime | None, tenant_uid_is_internal: int | None, tenant_uid_is_system: int | None, tenant_uid_is_test: int | None, tenant_uid_account_uid: str | None):
        self.tenant_country_uid = tenant_country_uid
        self.tenant_country_name = tenant_country_name
        self.country_uid = country_uid
        self.tenant_uid = tenant_uid
        self.country_priority = country_priority
        self.row_instance = row_instance
        self.row_lock = row_lock
        self.row_owner = row_owner
        self.row_seq = row_seq
        self.row_guid = row_guid
        self.row_version = row_version
        self.is_active = is_active
        self.created_date = created_date
        self.created_by = created_by
        self.last_updated_date = last_updated_date
        self.last_updated_by = last_updated_by
        self.removed_date = removed_date
        self.removed_by = removed_by
        self.custom_attributes = custom_attributes
        self.tenant_country_uid_country_name = tenant_country_uid_country_name
        self.tenant_country_uid_continent_name = tenant_country_uid_continent_name
        self.tenant_country_uid_continent_code = tenant_country_uid_continent_code
        self.tenant_country_uid_country_iso3 = tenant_country_uid_country_iso3
        self.tenant_country_uid_country_code = tenant_country_uid_country_code
        self.tenant_country_uid_phone_code = tenant_country_uid_phone_code
        self.tenant_country_uid_currency_code = tenant_country_uid_currency_code
        self.tenant_country_uid_capital_name = tenant_country_uid_capital_name
        self.tenant_country_uid_region_name = tenant_country_uid_region_name
        self.tenant_country_uid_subregion_name = tenant_country_uid_subregion_name
        self.tenant_country_uid_region_code = tenant_country_uid_region_code
        self.tenant_country_uid_latitude = tenant_country_uid_latitude
        self.tenant_country_uid_longitude = tenant_country_uid_longitude
        self.tenant_country_uid_currency_name = tenant_country_uid_currency_name
        self.tenant_country_uid_population = tenant_country_uid_population
        self.tenant_country_uid_languages = tenant_country_uid_languages
        self.tenant_country_uid_area = tenant_country_uid_area
        self.tenant_country_uid_bar_code = tenant_country_uid_bar_code
        self.tenant_country_uid_top_level_domain = tenant_country_uid_top_level_domain
        self.tenant_country_uid_is_focused = tenant_country_uid_is_focused
        self.country_uid_country_name = country_uid_country_name
        self.country_uid_continent_name = country_uid_continent_name
        self.country_uid_continent_code = country_uid_continent_code
        self.country_uid_country_iso3 = country_uid_country_iso3
        self.country_uid_country_code = country_uid_country_code
        self.country_uid_phone_code = country_uid_phone_code
        self.country_uid_currency_code = country_uid_currency_code
        self.country_uid_capital_name = country_uid_capital_name
        self.country_uid_region_name = country_uid_region_name
        self.country_uid_subregion_name = country_uid_subregion_name
        self.country_uid_region_code = country_uid_region_code
        self.country_uid_latitude = country_uid_latitude
        self.country_uid_longitude = country_uid_longitude
        self.country_uid_currency_name = country_uid_currency_name
        self.country_uid_population = country_uid_population
        self.country_uid_languages = country_uid_languages
        self.country_uid_area = country_uid_area
        self.country_uid_bar_code = country_uid_bar_code
        self.country_uid_top_level_domain = country_uid_top_level_domain
        self.country_uid_is_focused = country_uid_is_focused
        self.tenant_uid_tenant_name = tenant_uid_tenant_name
        self.tenant_uid_country_uid = tenant_uid_country_uid
        self.tenant_uid_tenant_type_uid = tenant_uid_tenant_type_uid
        self.tenant_uid_tenant_category_uid = tenant_uid_tenant_category_uid
        self.tenant_uid_tenant_code = tenant_uid_tenant_code
        self.tenant_uid_tenant_description = tenant_uid_tenant_description
        self.tenant_uid_start_date = tenant_uid_start_date
        self.tenant_uid_end_date = tenant_uid_end_date
        self.tenant_uid_is_internal = tenant_uid_is_internal
        self.tenant_uid_is_system = tenant_uid_is_system
        self.tenant_uid_is_test = tenant_uid_is_test
        self.tenant_uid_account_uid = tenant_uid_account_uid
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.tenant_country_uid, self.tenant_country_name, self.country_uid, self.tenant_uid, self.country_priority, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes, self.tenant_country_uid_country_name, self.tenant_country_uid_continent_name, self.tenant_country_uid_continent_code, self.tenant_country_uid_country_iso3, self.tenant_country_uid_country_code, self.tenant_country_uid_phone_code, self.tenant_country_uid_currency_code, self.tenant_country_uid_capital_name, self.tenant_country_uid_region_name, self.tenant_country_uid_subregion_name, self.tenant_country_uid_region_code, self.tenant_country_uid_latitude, self.tenant_country_uid_longitude, self.tenant_country_uid_currency_name, self.tenant_country_uid_population, self.tenant_country_uid_languages, self.tenant_country_uid_area, self.tenant_country_uid_bar_code, self.tenant_country_uid_top_level_domain, self.tenant_country_uid_is_focused, self.country_uid_country_name, self.country_uid_continent_name, self.country_uid_continent_code, self.country_uid_country_iso3, self.country_uid_country_code, self.country_uid_phone_code, self.country_uid_currency_code, self.country_uid_capital_name, self.country_uid_region_name, self.country_uid_subregion_name, self.country_uid_region_code, self.country_uid_latitude, self.country_uid_longitude, self.country_uid_currency_name, self.country_uid_population, self.country_uid_languages, self.country_uid_area, self.country_uid_bar_code, self.country_uid_top_level_domain, self.country_uid_is_focused, self.tenant_uid_tenant_name, self.tenant_uid_country_uid, self.tenant_uid_tenant_type_uid, self.tenant_uid_tenant_category_uid, self.tenant_uid_tenant_code, self.tenant_uid_tenant_description, self.tenant_uid_start_date, self.tenant_uid_end_date, self.tenant_uid_is_internal, self.tenant_uid_is_system, self.tenant_uid_is_test, self.tenant_uid_account_uid]


@dataclass(frozen=False)
class tenant_license_rich_dto(tenant_license_read_dto):
    tenant_license_uid: str | None
    tenant_license_name: str | None
    tenant_uid: str | None
    system_license_uid: str | None
    start_date: datetime.datetime | None
    end_date: datetime.datetime | None
    is_approved: int | None
    row_instance: str | None
    row_lock: str | None
    row_owner: str | None
    row_seq: int | None
    row_guid: str | None
    row_version: int | None
    is_active: int | None
    created_date: datetime.datetime | None
    created_by: str | None
    last_updated_date: datetime.datetime | None
    last_updated_by: str | None
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str | None
    tenant_uid_tenant_name: str | None
    tenant_uid_country_uid: str | None
    tenant_uid_tenant_type_uid: str | None
    tenant_uid_tenant_category_uid: str | None
    tenant_uid_tenant_code: str | None
    tenant_uid_tenant_description: str | None
    tenant_uid_start_date: datetime.datetime | None
    tenant_uid_end_date: datetime.datetime | None
    tenant_uid_is_internal: int | None
    tenant_uid_is_system: int | None
    tenant_uid_is_test: int | None
    tenant_uid_account_uid: str | None
    system_license_uid_system_license_name: str | None
    system_license_uid_license_description: str | None
    def __init__(self, tenant_license_uid: str | None, tenant_license_name: str | None, tenant_uid: str | None, system_license_uid: str | None, start_date: datetime.datetime | None, end_date: datetime.datetime | None, is_approved: int | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None, tenant_uid_tenant_name: str | None, tenant_uid_country_uid: str | None, tenant_uid_tenant_type_uid: str | None, tenant_uid_tenant_category_uid: str | None, tenant_uid_tenant_code: str | None, tenant_uid_tenant_description: str | None, tenant_uid_start_date: datetime.datetime | None, tenant_uid_end_date: datetime.datetime | None, tenant_uid_is_internal: int | None, tenant_uid_is_system: int | None, tenant_uid_is_test: int | None, tenant_uid_account_uid: str | None, system_license_uid_system_license_name: str | None, system_license_uid_license_description: str | None):
        self.tenant_license_uid = tenant_license_uid
        self.tenant_license_name = tenant_license_name
        self.tenant_uid = tenant_uid
        self.system_license_uid = system_license_uid
        self.start_date = start_date
        self.end_date = end_date
        self.is_approved = is_approved
        self.row_instance = row_instance
        self.row_lock = row_lock
        self.row_owner = row_owner
        self.row_seq = row_seq
        self.row_guid = row_guid
        self.row_version = row_version
        self.is_active = is_active
        self.created_date = created_date
        self.created_by = created_by
        self.last_updated_date = last_updated_date
        self.last_updated_by = last_updated_by
        self.removed_date = removed_date
        self.removed_by = removed_by
        self.custom_attributes = custom_attributes
        self.tenant_uid_tenant_name = tenant_uid_tenant_name
        self.tenant_uid_country_uid = tenant_uid_country_uid
        self.tenant_uid_tenant_type_uid = tenant_uid_tenant_type_uid
        self.tenant_uid_tenant_category_uid = tenant_uid_tenant_category_uid
        self.tenant_uid_tenant_code = tenant_uid_tenant_code
        self.tenant_uid_tenant_description = tenant_uid_tenant_description
        self.tenant_uid_start_date = tenant_uid_start_date
        self.tenant_uid_end_date = tenant_uid_end_date
        self.tenant_uid_is_internal = tenant_uid_is_internal
        self.tenant_uid_is_system = tenant_uid_is_system
        self.tenant_uid_is_test = tenant_uid_is_test
        self.tenant_uid_account_uid = tenant_uid_account_uid
        self.system_license_uid_system_license_name = system_license_uid_system_license_name
        self.system_license_uid_license_description = system_license_uid_license_description
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.tenant_license_uid, self.tenant_license_name, self.tenant_uid, self.system_license_uid, self.start_date, self.end_date, self.is_approved, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes, self.tenant_uid_tenant_name, self.tenant_uid_country_uid, self.tenant_uid_tenant_type_uid, self.tenant_uid_tenant_category_uid, self.tenant_uid_tenant_code, self.tenant_uid_tenant_description, self.tenant_uid_start_date, self.tenant_uid_end_date, self.tenant_uid_is_internal, self.tenant_uid_is_system, self.tenant_uid_is_test, self.tenant_uid_account_uid, self.system_license_uid_system_license_name, self.system_license_uid_license_description]


@dataclass(frozen=False)
class tenant_payment_rich_dto(tenant_payment_read_dto):
    tenant_payment_uid: str | None
    tenant_payment_name: str | None
    tenant_uid: str | None
    account_uid: str | None
    currency_uid: str | None
    tenant_payment_type_uid: str | None
    start_date: datetime.datetime | None
    end_date: datetime.datetime | None
    payment_value: str | None
    source_number: str | None
    source_reference: str | None
    is_approved: int | None
    row_instance: str | None
    row_lock: str | None
    row_owner: str | None
    row_seq: int | None
    row_guid: str | None
    row_version: int | None
    is_active: int | None
    created_date: datetime.datetime | None
    created_by: str | None
    last_updated_date: datetime.datetime | None
    last_updated_by: str | None
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str | None
    tenant_uid_tenant_name: str | None
    tenant_uid_country_uid: str | None
    tenant_uid_tenant_type_uid: str | None
    tenant_uid_tenant_category_uid: str | None
    tenant_uid_tenant_code: str | None
    tenant_uid_tenant_description: str | None
    tenant_uid_start_date: datetime.datetime | None
    tenant_uid_end_date: datetime.datetime | None
    tenant_uid_is_internal: int | None
    tenant_uid_is_system: int | None
    tenant_uid_is_test: int | None
    tenant_uid_account_uid: str | None
    account_uid_account_name: str | None
    account_uid_tenant_uid: str | None
    account_uid_account_type_uid: str | None
    account_uid_account_title_uid: str | None
    account_uid_account_division_uid: str | None
    account_uid_account_group_uid: str | None
    account_uid_auth_identity_uid: str | None
    account_uid_account_email: str | None
    account_uid_display_name: str | None
    account_uid_is_system: int | None
    currency_uid_currency_name: str | None
    currency_uid_is_focused: int | None
    tenant_payment_type_uid_tenant_payment_type_name: str | None
    def __init__(self, tenant_payment_uid: str | None, tenant_payment_name: str | None, tenant_uid: str | None, account_uid: str | None, currency_uid: str | None, tenant_payment_type_uid: str | None, start_date: datetime.datetime | None, end_date: datetime.datetime | None, payment_value: str | None, source_number: str | None, source_reference: str | None, is_approved: int | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None, tenant_uid_tenant_name: str | None, tenant_uid_country_uid: str | None, tenant_uid_tenant_type_uid: str | None, tenant_uid_tenant_category_uid: str | None, tenant_uid_tenant_code: str | None, tenant_uid_tenant_description: str | None, tenant_uid_start_date: datetime.datetime | None, tenant_uid_end_date: datetime.datetime | None, tenant_uid_is_internal: int | None, tenant_uid_is_system: int | None, tenant_uid_is_test: int | None, tenant_uid_account_uid: str | None, account_uid_account_name: str | None, account_uid_tenant_uid: str | None, account_uid_account_type_uid: str | None, account_uid_account_title_uid: str | None, account_uid_account_division_uid: str | None, account_uid_account_group_uid: str | None, account_uid_auth_identity_uid: str | None, account_uid_account_email: str | None, account_uid_display_name: str | None, account_uid_is_system: int | None, currency_uid_currency_name: str | None, currency_uid_is_focused: int | None, tenant_payment_type_uid_tenant_payment_type_name: str | None):
        self.tenant_payment_uid = tenant_payment_uid
        self.tenant_payment_name = tenant_payment_name
        self.tenant_uid = tenant_uid
        self.account_uid = account_uid
        self.currency_uid = currency_uid
        self.tenant_payment_type_uid = tenant_payment_type_uid
        self.start_date = start_date
        self.end_date = end_date
        self.payment_value = payment_value
        self.source_number = source_number
        self.source_reference = source_reference
        self.is_approved = is_approved
        self.row_instance = row_instance
        self.row_lock = row_lock
        self.row_owner = row_owner
        self.row_seq = row_seq
        self.row_guid = row_guid
        self.row_version = row_version
        self.is_active = is_active
        self.created_date = created_date
        self.created_by = created_by
        self.last_updated_date = last_updated_date
        self.last_updated_by = last_updated_by
        self.removed_date = removed_date
        self.removed_by = removed_by
        self.custom_attributes = custom_attributes
        self.tenant_uid_tenant_name = tenant_uid_tenant_name
        self.tenant_uid_country_uid = tenant_uid_country_uid
        self.tenant_uid_tenant_type_uid = tenant_uid_tenant_type_uid
        self.tenant_uid_tenant_category_uid = tenant_uid_tenant_category_uid
        self.tenant_uid_tenant_code = tenant_uid_tenant_code
        self.tenant_uid_tenant_description = tenant_uid_tenant_description
        self.tenant_uid_start_date = tenant_uid_start_date
        self.tenant_uid_end_date = tenant_uid_end_date
        self.tenant_uid_is_internal = tenant_uid_is_internal
        self.tenant_uid_is_system = tenant_uid_is_system
        self.tenant_uid_is_test = tenant_uid_is_test
        self.tenant_uid_account_uid = tenant_uid_account_uid
        self.account_uid_account_name = account_uid_account_name
        self.account_uid_tenant_uid = account_uid_tenant_uid
        self.account_uid_account_type_uid = account_uid_account_type_uid
        self.account_uid_account_title_uid = account_uid_account_title_uid
        self.account_uid_account_division_uid = account_uid_account_division_uid
        self.account_uid_account_group_uid = account_uid_account_group_uid
        self.account_uid_auth_identity_uid = account_uid_auth_identity_uid
        self.account_uid_account_email = account_uid_account_email
        self.account_uid_display_name = account_uid_display_name
        self.account_uid_is_system = account_uid_is_system
        self.currency_uid_currency_name = currency_uid_currency_name
        self.currency_uid_is_focused = currency_uid_is_focused
        self.tenant_payment_type_uid_tenant_payment_type_name = tenant_payment_type_uid_tenant_payment_type_name
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.tenant_payment_uid, self.tenant_payment_name, self.tenant_uid, self.account_uid, self.currency_uid, self.tenant_payment_type_uid, self.start_date, self.end_date, self.payment_value, self.source_number, self.source_reference, self.is_approved, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes, self.tenant_uid_tenant_name, self.tenant_uid_country_uid, self.tenant_uid_tenant_type_uid, self.tenant_uid_tenant_category_uid, self.tenant_uid_tenant_code, self.tenant_uid_tenant_description, self.tenant_uid_start_date, self.tenant_uid_end_date, self.tenant_uid_is_internal, self.tenant_uid_is_system, self.tenant_uid_is_test, self.tenant_uid_account_uid, self.account_uid_account_name, self.account_uid_tenant_uid, self.account_uid_account_type_uid, self.account_uid_account_title_uid, self.account_uid_account_division_uid, self.account_uid_account_group_uid, self.account_uid_auth_identity_uid, self.account_uid_account_email, self.account_uid_display_name, self.account_uid_is_system, self.currency_uid_currency_name, self.currency_uid_is_focused, self.tenant_payment_type_uid_tenant_payment_type_name]


@dataclass(frozen=False)
class tenant_payment_type_rich_dto(tenant_payment_type_read_dto):
    tenant_payment_type_uid: str | None
    tenant_payment_type_name: str | None
    row_instance: str | None
    row_lock: str | None
    row_owner: str | None
    row_seq: int | None
    row_guid: str | None
    row_version: int | None
    is_active: int | None
    created_date: datetime.datetime | None
    created_by: str | None
    last_updated_date: datetime.datetime | None
    last_updated_by: str | None
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str | None
    def __init__(self, tenant_payment_type_uid: str | None, tenant_payment_type_name: str | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None):
        self.tenant_payment_type_uid = tenant_payment_type_uid
        self.tenant_payment_type_name = tenant_payment_type_name
        self.row_instance = row_instance
        self.row_lock = row_lock
        self.row_owner = row_owner
        self.row_seq = row_seq
        self.row_guid = row_guid
        self.row_version = row_version
        self.is_active = is_active
        self.created_date = created_date
        self.created_by = created_by
        self.last_updated_date = last_updated_date
        self.last_updated_by = last_updated_by
        self.removed_date = removed_date
        self.removed_by = removed_by
        self.custom_attributes = custom_attributes
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.tenant_payment_type_uid, self.tenant_payment_type_name, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]


@dataclass(frozen=False)
class tenant_role_rich_dto(tenant_role_read_dto):
    tenant_role_uid: str | None
    tenant_role_name: str | None
    role_description: str | None
    row_instance: str | None
    row_lock: str | None
    row_owner: str | None
    row_seq: int | None
    row_guid: str | None
    row_version: int | None
    is_active: int | None
    created_date: datetime.datetime | None
    created_by: str | None
    last_updated_date: datetime.datetime | None
    last_updated_by: str | None
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str | None
    def __init__(self, tenant_role_uid: str | None, tenant_role_name: str | None, role_description: str | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None):
        self.tenant_role_uid = tenant_role_uid
        self.tenant_role_name = tenant_role_name
        self.role_description = role_description
        self.row_instance = row_instance
        self.row_lock = row_lock
        self.row_owner = row_owner
        self.row_seq = row_seq
        self.row_guid = row_guid
        self.row_version = row_version
        self.is_active = is_active
        self.created_date = created_date
        self.created_by = created_by
        self.last_updated_date = last_updated_date
        self.last_updated_by = last_updated_by
        self.removed_date = removed_date
        self.removed_by = removed_by
        self.custom_attributes = custom_attributes
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.tenant_role_uid, self.tenant_role_name, self.role_description, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]


@dataclass(frozen=False)
class tenant_status_rich_dto(tenant_status_read_dto):
    tenant_status_uid: str | None
    tenant_status_name: str | None
    tenant_status_description: str | None
    row_instance: str | None
    row_lock: str | None
    row_owner: str | None
    row_seq: int | None
    row_guid: str | None
    row_version: int | None
    is_active: int | None
    created_date: datetime.datetime | None
    created_by: str | None
    last_updated_date: datetime.datetime | None
    last_updated_by: str | None
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str | None
    def __init__(self, tenant_status_uid: str | None, tenant_status_name: str | None, tenant_status_description: str | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None):
        self.tenant_status_uid = tenant_status_uid
        self.tenant_status_name = tenant_status_name
        self.tenant_status_description = tenant_status_description
        self.row_instance = row_instance
        self.row_lock = row_lock
        self.row_owner = row_owner
        self.row_seq = row_seq
        self.row_guid = row_guid
        self.row_version = row_version
        self.is_active = is_active
        self.created_date = created_date
        self.created_by = created_by
        self.last_updated_date = last_updated_date
        self.last_updated_by = last_updated_by
        self.removed_date = removed_date
        self.removed_by = removed_by
        self.custom_attributes = custom_attributes
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.tenant_status_uid, self.tenant_status_name, self.tenant_status_description, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]


@dataclass(frozen=False)
class tenant_type_rich_dto(tenant_type_read_dto):
    tenant_type_uid: str | None
    tenant_type_name: str | None
    tenant_type_description: str | None
    row_instance: str | None
    row_lock: str | None
    row_owner: str | None
    row_seq: int | None
    row_guid: str | None
    row_version: int | None
    is_active: int | None
    created_date: datetime.datetime | None
    created_by: str | None
    last_updated_date: datetime.datetime | None
    last_updated_by: str | None
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str | None
    def __init__(self, tenant_type_uid: str | None, tenant_type_name: str | None, tenant_type_description: str | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None):
        self.tenant_type_uid = tenant_type_uid
        self.tenant_type_name = tenant_type_name
        self.tenant_type_description = tenant_type_description
        self.row_instance = row_instance
        self.row_lock = row_lock
        self.row_owner = row_owner
        self.row_seq = row_seq
        self.row_guid = row_guid
        self.row_version = row_version
        self.is_active = is_active
        self.created_date = created_date
        self.created_by = created_by
        self.last_updated_date = last_updated_date
        self.last_updated_by = last_updated_by
        self.removed_date = removed_date
        self.removed_by = removed_by
        self.custom_attributes = custom_attributes
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.tenant_type_uid, self.tenant_type_name, self.tenant_type_description, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]


@dataclass(frozen=False)
class time_approval_rich_dto(time_approval_read_dto):
    time_approval_uid: str | None
    time_approval_name: str | None
    tenant_uid: str | None
    account_uid: str | None
    time_entry_uid: str | None
    approval_comment: str | None
    row_instance: str | None
    row_lock: str | None
    row_owner: str | None
    row_seq: int | None
    row_guid: str | None
    row_version: int | None
    is_active: int | None
    created_date: datetime.datetime | None
    created_by: str | None
    last_updated_date: datetime.datetime | None
    last_updated_by: str | None
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str | None
    tenant_uid_tenant_name: str | None
    tenant_uid_country_uid: str | None
    tenant_uid_tenant_type_uid: str | None
    tenant_uid_tenant_category_uid: str | None
    tenant_uid_tenant_code: str | None
    tenant_uid_tenant_description: str | None
    tenant_uid_start_date: datetime.datetime | None
    tenant_uid_end_date: datetime.datetime | None
    tenant_uid_is_internal: int | None
    tenant_uid_is_system: int | None
    tenant_uid_is_test: int | None
    tenant_uid_account_uid: str | None
    account_uid_account_name: str | None
    account_uid_tenant_uid: str | None
    account_uid_account_type_uid: str | None
    account_uid_account_title_uid: str | None
    account_uid_account_division_uid: str | None
    account_uid_account_group_uid: str | None
    account_uid_auth_identity_uid: str | None
    account_uid_account_email: str | None
    account_uid_display_name: str | None
    account_uid_is_system: int | None
    time_entry_uid_time_entry_name: str | None
    time_entry_uid_time_submit_uid: str | None
    time_entry_uid_tenant_uid: str | None
    time_entry_uid_account_uid: str | None
    time_entry_uid_project_instance_uid: str | None
    time_entry_uid_project_milestone_uid: str | None
    time_entry_uid_period_uid: str | None
    time_entry_uid_invoice_instance_uid: str | None
    time_entry_uid_entry_period: str | None
    time_entry_uid_entry_note: str | None
    time_entry_uid_lock_row: str | None
    time_entry_uid_start_date: datetime.datetime | None
    time_entry_uid_end_date: datetime.datetime | None
    time_entry_uid_entry_minutes: int | None
    time_entry_uid_is_approved: int | None
    def __init__(self, time_approval_uid: str | None, time_approval_name: str | None, tenant_uid: str | None, account_uid: str | None, time_entry_uid: str | None, approval_comment: str | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None, tenant_uid_tenant_name: str | None, tenant_uid_country_uid: str | None, tenant_uid_tenant_type_uid: str | None, tenant_uid_tenant_category_uid: str | None, tenant_uid_tenant_code: str | None, tenant_uid_tenant_description: str | None, tenant_uid_start_date: datetime.datetime | None, tenant_uid_end_date: datetime.datetime | None, tenant_uid_is_internal: int | None, tenant_uid_is_system: int | None, tenant_uid_is_test: int | None, tenant_uid_account_uid: str | None, account_uid_account_name: str | None, account_uid_tenant_uid: str | None, account_uid_account_type_uid: str | None, account_uid_account_title_uid: str | None, account_uid_account_division_uid: str | None, account_uid_account_group_uid: str | None, account_uid_auth_identity_uid: str | None, account_uid_account_email: str | None, account_uid_display_name: str | None, account_uid_is_system: int | None, time_entry_uid_time_entry_name: str | None, time_entry_uid_time_submit_uid: str | None, time_entry_uid_tenant_uid: str | None, time_entry_uid_account_uid: str | None, time_entry_uid_project_instance_uid: str | None, time_entry_uid_project_milestone_uid: str | None, time_entry_uid_period_uid: str | None, time_entry_uid_invoice_instance_uid: str | None, time_entry_uid_entry_period: str | None, time_entry_uid_entry_note: str | None, time_entry_uid_lock_row: str | None, time_entry_uid_start_date: datetime.datetime | None, time_entry_uid_end_date: datetime.datetime | None, time_entry_uid_entry_minutes: int | None, time_entry_uid_is_approved: int | None):
        self.time_approval_uid = time_approval_uid
        self.time_approval_name = time_approval_name
        self.tenant_uid = tenant_uid
        self.account_uid = account_uid
        self.time_entry_uid = time_entry_uid
        self.approval_comment = approval_comment
        self.row_instance = row_instance
        self.row_lock = row_lock
        self.row_owner = row_owner
        self.row_seq = row_seq
        self.row_guid = row_guid
        self.row_version = row_version
        self.is_active = is_active
        self.created_date = created_date
        self.created_by = created_by
        self.last_updated_date = last_updated_date
        self.last_updated_by = last_updated_by
        self.removed_date = removed_date
        self.removed_by = removed_by
        self.custom_attributes = custom_attributes
        self.tenant_uid_tenant_name = tenant_uid_tenant_name
        self.tenant_uid_country_uid = tenant_uid_country_uid
        self.tenant_uid_tenant_type_uid = tenant_uid_tenant_type_uid
        self.tenant_uid_tenant_category_uid = tenant_uid_tenant_category_uid
        self.tenant_uid_tenant_code = tenant_uid_tenant_code
        self.tenant_uid_tenant_description = tenant_uid_tenant_description
        self.tenant_uid_start_date = tenant_uid_start_date
        self.tenant_uid_end_date = tenant_uid_end_date
        self.tenant_uid_is_internal = tenant_uid_is_internal
        self.tenant_uid_is_system = tenant_uid_is_system
        self.tenant_uid_is_test = tenant_uid_is_test
        self.tenant_uid_account_uid = tenant_uid_account_uid
        self.account_uid_account_name = account_uid_account_name
        self.account_uid_tenant_uid = account_uid_tenant_uid
        self.account_uid_account_type_uid = account_uid_account_type_uid
        self.account_uid_account_title_uid = account_uid_account_title_uid
        self.account_uid_account_division_uid = account_uid_account_division_uid
        self.account_uid_account_group_uid = account_uid_account_group_uid
        self.account_uid_auth_identity_uid = account_uid_auth_identity_uid
        self.account_uid_account_email = account_uid_account_email
        self.account_uid_display_name = account_uid_display_name
        self.account_uid_is_system = account_uid_is_system
        self.time_entry_uid_time_entry_name = time_entry_uid_time_entry_name
        self.time_entry_uid_time_submit_uid = time_entry_uid_time_submit_uid
        self.time_entry_uid_tenant_uid = time_entry_uid_tenant_uid
        self.time_entry_uid_account_uid = time_entry_uid_account_uid
        self.time_entry_uid_project_instance_uid = time_entry_uid_project_instance_uid
        self.time_entry_uid_project_milestone_uid = time_entry_uid_project_milestone_uid
        self.time_entry_uid_period_uid = time_entry_uid_period_uid
        self.time_entry_uid_invoice_instance_uid = time_entry_uid_invoice_instance_uid
        self.time_entry_uid_entry_period = time_entry_uid_entry_period
        self.time_entry_uid_entry_note = time_entry_uid_entry_note
        self.time_entry_uid_lock_row = time_entry_uid_lock_row
        self.time_entry_uid_start_date = time_entry_uid_start_date
        self.time_entry_uid_end_date = time_entry_uid_end_date
        self.time_entry_uid_entry_minutes = time_entry_uid_entry_minutes
        self.time_entry_uid_is_approved = time_entry_uid_is_approved
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.time_approval_uid, self.time_approval_name, self.tenant_uid, self.account_uid, self.time_entry_uid, self.approval_comment, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes, self.tenant_uid_tenant_name, self.tenant_uid_country_uid, self.tenant_uid_tenant_type_uid, self.tenant_uid_tenant_category_uid, self.tenant_uid_tenant_code, self.tenant_uid_tenant_description, self.tenant_uid_start_date, self.tenant_uid_end_date, self.tenant_uid_is_internal, self.tenant_uid_is_system, self.tenant_uid_is_test, self.tenant_uid_account_uid, self.account_uid_account_name, self.account_uid_tenant_uid, self.account_uid_account_type_uid, self.account_uid_account_title_uid, self.account_uid_account_division_uid, self.account_uid_account_group_uid, self.account_uid_auth_identity_uid, self.account_uid_account_email, self.account_uid_display_name, self.account_uid_is_system, self.time_entry_uid_time_entry_name, self.time_entry_uid_time_submit_uid, self.time_entry_uid_tenant_uid, self.time_entry_uid_account_uid, self.time_entry_uid_project_instance_uid, self.time_entry_uid_project_milestone_uid, self.time_entry_uid_period_uid, self.time_entry_uid_invoice_instance_uid, self.time_entry_uid_entry_period, self.time_entry_uid_entry_note, self.time_entry_uid_lock_row, self.time_entry_uid_start_date, self.time_entry_uid_end_date, self.time_entry_uid_entry_minutes, self.time_entry_uid_is_approved]


@dataclass(frozen=False)
class time_entry_rich_dto(time_entry_read_dto):
    time_entry_uid: str | None
    time_entry_name: str | None
    time_submit_uid: str | None
    tenant_uid: str | None
    account_uid: str | None
    project_instance_uid: str | None
    project_milestone_uid: str | None
    period_uid: str | None
    invoice_instance_uid: str | None
    entry_period: str | None
    entry_note: str | None
    lock_row: str | None
    start_date: datetime.datetime | None
    end_date: datetime.datetime | None
    entry_minutes: int | None
    is_approved: int | None
    row_instance: str | None
    row_lock: str | None
    row_owner: str | None
    row_seq: int | None
    row_guid: str | None
    row_version: int | None
    is_active: int | None
    created_date: datetime.datetime | None
    created_by: str | None
    last_updated_date: datetime.datetime | None
    last_updated_by: str | None
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str | None
    time_submit_uid_time_submit_name: str | None
    time_submit_uid_tenant_uid: str | None
    time_submit_uid_account_uid: str | None
    time_submit_uid_period_uid: str | None
    time_submit_uid_time_submit_description: str | None
    tenant_uid_tenant_name: str | None
    tenant_uid_country_uid: str | None
    tenant_uid_tenant_type_uid: str | None
    tenant_uid_tenant_category_uid: str | None
    tenant_uid_tenant_code: str | None
    tenant_uid_tenant_description: str | None
    tenant_uid_start_date: datetime.datetime | None
    tenant_uid_end_date: datetime.datetime | None
    tenant_uid_is_internal: int | None
    tenant_uid_is_system: int | None
    tenant_uid_is_test: int | None
    tenant_uid_account_uid: str | None
    account_uid_account_name: str | None
    account_uid_tenant_uid: str | None
    account_uid_account_type_uid: str | None
    account_uid_account_title_uid: str | None
    account_uid_account_division_uid: str | None
    account_uid_account_group_uid: str | None
    account_uid_auth_identity_uid: str | None
    account_uid_account_email: str | None
    account_uid_display_name: str | None
    account_uid_is_system: int | None
    project_instance_uid_project_instance_name: str | None
    project_instance_uid_tenant_uid: str | None
    project_instance_uid_client_uid: str | None
    project_instance_uid_project_type_uid: str | None
    project_instance_uid_manager_account_uid: str | None
    project_instance_uid_project_group_uid: str | None
    project_instance_uid_project_code: str | None
    project_instance_uid_project_description: str | None
    project_instance_uid_is_billable: int | None
    project_instance_uid_start_date: datetime.datetime | None
    project_instance_uid_end_date: datetime.datetime | None
    project_instance_uid_current_billed: str | None
    project_instance_uid_budget: str | None
    project_milestone_uid_project_milestone_name: str | None
    project_milestone_uid_tenant_uid: str | None
    project_milestone_uid_client_uid: str | None
    project_milestone_uid_project_instance_uid: str | None
    project_milestone_uid_project_budget_uid: str | None
    project_milestone_uid_start_date: datetime.datetime | None
    project_milestone_uid_end_date: datetime.datetime | None
    project_milestone_uid_status_name: str | None
    period_uid_period_name: str | None
    period_uid_period_number: int | None
    period_uid_period_type: str | None
    period_uid_period_start_time: datetime.datetime | None
    period_uid_period_end_time: datetime.datetime | None
    period_uid_period_year: int | None
    period_uid_period_quarter: int | None
    period_uid_period_month: int | None
    period_uid_period_week: int | None
    period_uid_period_day: int | None
    invoice_instance_uid_invoice_instance_name: str | None
    invoice_instance_uid_tenant_uid: str | None
    invoice_instance_uid_account_uid: str | None
    invoice_instance_uid_invoice_flow_uid: str | None
    invoice_instance_uid_invoice_status_uid: str | None
    invoice_instance_uid_invoice_category_uid: str | None
    invoice_instance_uid_invoice_type_uid: str | None
    invoice_instance_uid_period_uid: str | None
    invoice_instance_uid_currency_uid: str | None
    invoice_instance_uid_invoice_number: str | None
    invoice_instance_uid_invoice_details: str | None
    invoice_instance_uid_invoice_amount_net: str | None
    invoice_instance_uid_invoice_amount_tax: str | None
    invoice_instance_uid_invoice_amount_gross: str | None
    def __init__(self, time_entry_uid: str | None, time_entry_name: str | None, time_submit_uid: str | None, tenant_uid: str | None, account_uid: str | None, project_instance_uid: str | None, project_milestone_uid: str | None, period_uid: str | None, invoice_instance_uid: str | None, entry_period: str | None, entry_note: str | None, lock_row: str | None, start_date: datetime.datetime | None, end_date: datetime.datetime | None, entry_minutes: int | None, is_approved: int | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None, time_submit_uid_time_submit_name: str | None, time_submit_uid_tenant_uid: str | None, time_submit_uid_account_uid: str | None, time_submit_uid_period_uid: str | None, time_submit_uid_time_submit_description: str | None, tenant_uid_tenant_name: str | None, tenant_uid_country_uid: str | None, tenant_uid_tenant_type_uid: str | None, tenant_uid_tenant_category_uid: str | None, tenant_uid_tenant_code: str | None, tenant_uid_tenant_description: str | None, tenant_uid_start_date: datetime.datetime | None, tenant_uid_end_date: datetime.datetime | None, tenant_uid_is_internal: int | None, tenant_uid_is_system: int | None, tenant_uid_is_test: int | None, tenant_uid_account_uid: str | None, account_uid_account_name: str | None, account_uid_tenant_uid: str | None, account_uid_account_type_uid: str | None, account_uid_account_title_uid: str | None, account_uid_account_division_uid: str | None, account_uid_account_group_uid: str | None, account_uid_auth_identity_uid: str | None, account_uid_account_email: str | None, account_uid_display_name: str | None, account_uid_is_system: int | None, project_instance_uid_project_instance_name: str | None, project_instance_uid_tenant_uid: str | None, project_instance_uid_client_uid: str | None, project_instance_uid_project_type_uid: str | None, project_instance_uid_manager_account_uid: str | None, project_instance_uid_project_group_uid: str | None, project_instance_uid_project_code: str | None, project_instance_uid_project_description: str | None, project_instance_uid_is_billable: int | None, project_instance_uid_start_date: datetime.datetime | None, project_instance_uid_end_date: datetime.datetime | None, project_instance_uid_current_billed: str | None, project_instance_uid_budget: str | None, project_milestone_uid_project_milestone_name: str | None, project_milestone_uid_tenant_uid: str | None, project_milestone_uid_client_uid: str | None, project_milestone_uid_project_instance_uid: str | None, project_milestone_uid_project_budget_uid: str | None, project_milestone_uid_start_date: datetime.datetime | None, project_milestone_uid_end_date: datetime.datetime | None, project_milestone_uid_status_name: str | None, period_uid_period_name: str | None, period_uid_period_number: int | None, period_uid_period_type: str | None, period_uid_period_start_time: datetime.datetime | None, period_uid_period_end_time: datetime.datetime | None, period_uid_period_year: int | None, period_uid_period_quarter: int | None, period_uid_period_month: int | None, period_uid_period_week: int | None, period_uid_period_day: int | None, invoice_instance_uid_invoice_instance_name: str | None, invoice_instance_uid_tenant_uid: str | None, invoice_instance_uid_account_uid: str | None, invoice_instance_uid_invoice_flow_uid: str | None, invoice_instance_uid_invoice_status_uid: str | None, invoice_instance_uid_invoice_category_uid: str | None, invoice_instance_uid_invoice_type_uid: str | None, invoice_instance_uid_period_uid: str | None, invoice_instance_uid_currency_uid: str | None, invoice_instance_uid_invoice_number: str | None, invoice_instance_uid_invoice_details: str | None, invoice_instance_uid_invoice_amount_net: str | None, invoice_instance_uid_invoice_amount_tax: str | None, invoice_instance_uid_invoice_amount_gross: str | None):
        self.time_entry_uid = time_entry_uid
        self.time_entry_name = time_entry_name
        self.time_submit_uid = time_submit_uid
        self.tenant_uid = tenant_uid
        self.account_uid = account_uid
        self.project_instance_uid = project_instance_uid
        self.project_milestone_uid = project_milestone_uid
        self.period_uid = period_uid
        self.invoice_instance_uid = invoice_instance_uid
        self.entry_period = entry_period
        self.entry_note = entry_note
        self.lock_row = lock_row
        self.start_date = start_date
        self.end_date = end_date
        self.entry_minutes = entry_minutes
        self.is_approved = is_approved
        self.row_instance = row_instance
        self.row_lock = row_lock
        self.row_owner = row_owner
        self.row_seq = row_seq
        self.row_guid = row_guid
        self.row_version = row_version
        self.is_active = is_active
        self.created_date = created_date
        self.created_by = created_by
        self.last_updated_date = last_updated_date
        self.last_updated_by = last_updated_by
        self.removed_date = removed_date
        self.removed_by = removed_by
        self.custom_attributes = custom_attributes
        self.time_submit_uid_time_submit_name = time_submit_uid_time_submit_name
        self.time_submit_uid_tenant_uid = time_submit_uid_tenant_uid
        self.time_submit_uid_account_uid = time_submit_uid_account_uid
        self.time_submit_uid_period_uid = time_submit_uid_period_uid
        self.time_submit_uid_time_submit_description = time_submit_uid_time_submit_description
        self.tenant_uid_tenant_name = tenant_uid_tenant_name
        self.tenant_uid_country_uid = tenant_uid_country_uid
        self.tenant_uid_tenant_type_uid = tenant_uid_tenant_type_uid
        self.tenant_uid_tenant_category_uid = tenant_uid_tenant_category_uid
        self.tenant_uid_tenant_code = tenant_uid_tenant_code
        self.tenant_uid_tenant_description = tenant_uid_tenant_description
        self.tenant_uid_start_date = tenant_uid_start_date
        self.tenant_uid_end_date = tenant_uid_end_date
        self.tenant_uid_is_internal = tenant_uid_is_internal
        self.tenant_uid_is_system = tenant_uid_is_system
        self.tenant_uid_is_test = tenant_uid_is_test
        self.tenant_uid_account_uid = tenant_uid_account_uid
        self.account_uid_account_name = account_uid_account_name
        self.account_uid_tenant_uid = account_uid_tenant_uid
        self.account_uid_account_type_uid = account_uid_account_type_uid
        self.account_uid_account_title_uid = account_uid_account_title_uid
        self.account_uid_account_division_uid = account_uid_account_division_uid
        self.account_uid_account_group_uid = account_uid_account_group_uid
        self.account_uid_auth_identity_uid = account_uid_auth_identity_uid
        self.account_uid_account_email = account_uid_account_email
        self.account_uid_display_name = account_uid_display_name
        self.account_uid_is_system = account_uid_is_system
        self.project_instance_uid_project_instance_name = project_instance_uid_project_instance_name
        self.project_instance_uid_tenant_uid = project_instance_uid_tenant_uid
        self.project_instance_uid_client_uid = project_instance_uid_client_uid
        self.project_instance_uid_project_type_uid = project_instance_uid_project_type_uid
        self.project_instance_uid_manager_account_uid = project_instance_uid_manager_account_uid
        self.project_instance_uid_project_group_uid = project_instance_uid_project_group_uid
        self.project_instance_uid_project_code = project_instance_uid_project_code
        self.project_instance_uid_project_description = project_instance_uid_project_description
        self.project_instance_uid_is_billable = project_instance_uid_is_billable
        self.project_instance_uid_start_date = project_instance_uid_start_date
        self.project_instance_uid_end_date = project_instance_uid_end_date
        self.project_instance_uid_current_billed = project_instance_uid_current_billed
        self.project_instance_uid_budget = project_instance_uid_budget
        self.project_milestone_uid_project_milestone_name = project_milestone_uid_project_milestone_name
        self.project_milestone_uid_tenant_uid = project_milestone_uid_tenant_uid
        self.project_milestone_uid_client_uid = project_milestone_uid_client_uid
        self.project_milestone_uid_project_instance_uid = project_milestone_uid_project_instance_uid
        self.project_milestone_uid_project_budget_uid = project_milestone_uid_project_budget_uid
        self.project_milestone_uid_start_date = project_milestone_uid_start_date
        self.project_milestone_uid_end_date = project_milestone_uid_end_date
        self.project_milestone_uid_status_name = project_milestone_uid_status_name
        self.period_uid_period_name = period_uid_period_name
        self.period_uid_period_number = period_uid_period_number
        self.period_uid_period_type = period_uid_period_type
        self.period_uid_period_start_time = period_uid_period_start_time
        self.period_uid_period_end_time = period_uid_period_end_time
        self.period_uid_period_year = period_uid_period_year
        self.period_uid_period_quarter = period_uid_period_quarter
        self.period_uid_period_month = period_uid_period_month
        self.period_uid_period_week = period_uid_period_week
        self.period_uid_period_day = period_uid_period_day
        self.invoice_instance_uid_invoice_instance_name = invoice_instance_uid_invoice_instance_name
        self.invoice_instance_uid_tenant_uid = invoice_instance_uid_tenant_uid
        self.invoice_instance_uid_account_uid = invoice_instance_uid_account_uid
        self.invoice_instance_uid_invoice_flow_uid = invoice_instance_uid_invoice_flow_uid
        self.invoice_instance_uid_invoice_status_uid = invoice_instance_uid_invoice_status_uid
        self.invoice_instance_uid_invoice_category_uid = invoice_instance_uid_invoice_category_uid
        self.invoice_instance_uid_invoice_type_uid = invoice_instance_uid_invoice_type_uid
        self.invoice_instance_uid_period_uid = invoice_instance_uid_period_uid
        self.invoice_instance_uid_currency_uid = invoice_instance_uid_currency_uid
        self.invoice_instance_uid_invoice_number = invoice_instance_uid_invoice_number
        self.invoice_instance_uid_invoice_details = invoice_instance_uid_invoice_details
        self.invoice_instance_uid_invoice_amount_net = invoice_instance_uid_invoice_amount_net
        self.invoice_instance_uid_invoice_amount_tax = invoice_instance_uid_invoice_amount_tax
        self.invoice_instance_uid_invoice_amount_gross = invoice_instance_uid_invoice_amount_gross
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.time_entry_uid, self.time_entry_name, self.time_submit_uid, self.tenant_uid, self.account_uid, self.project_instance_uid, self.project_milestone_uid, self.period_uid, self.invoice_instance_uid, self.entry_period, self.entry_note, self.lock_row, self.start_date, self.end_date, self.entry_minutes, self.is_approved, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes, self.time_submit_uid_time_submit_name, self.time_submit_uid_tenant_uid, self.time_submit_uid_account_uid, self.time_submit_uid_period_uid, self.time_submit_uid_time_submit_description, self.tenant_uid_tenant_name, self.tenant_uid_country_uid, self.tenant_uid_tenant_type_uid, self.tenant_uid_tenant_category_uid, self.tenant_uid_tenant_code, self.tenant_uid_tenant_description, self.tenant_uid_start_date, self.tenant_uid_end_date, self.tenant_uid_is_internal, self.tenant_uid_is_system, self.tenant_uid_is_test, self.tenant_uid_account_uid, self.account_uid_account_name, self.account_uid_tenant_uid, self.account_uid_account_type_uid, self.account_uid_account_title_uid, self.account_uid_account_division_uid, self.account_uid_account_group_uid, self.account_uid_auth_identity_uid, self.account_uid_account_email, self.account_uid_display_name, self.account_uid_is_system, self.project_instance_uid_project_instance_name, self.project_instance_uid_tenant_uid, self.project_instance_uid_client_uid, self.project_instance_uid_project_type_uid, self.project_instance_uid_manager_account_uid, self.project_instance_uid_project_group_uid, self.project_instance_uid_project_code, self.project_instance_uid_project_description, self.project_instance_uid_is_billable, self.project_instance_uid_start_date, self.project_instance_uid_end_date, self.project_instance_uid_current_billed, self.project_instance_uid_budget, self.project_milestone_uid_project_milestone_name, self.project_milestone_uid_tenant_uid, self.project_milestone_uid_client_uid, self.project_milestone_uid_project_instance_uid, self.project_milestone_uid_project_budget_uid, self.project_milestone_uid_start_date, self.project_milestone_uid_end_date, self.project_milestone_uid_status_name, self.period_uid_period_name, self.period_uid_period_number, self.period_uid_period_type, self.period_uid_period_start_time, self.period_uid_period_end_time, self.period_uid_period_year, self.period_uid_period_quarter, self.period_uid_period_month, self.period_uid_period_week, self.period_uid_period_day, self.invoice_instance_uid_invoice_instance_name, self.invoice_instance_uid_tenant_uid, self.invoice_instance_uid_account_uid, self.invoice_instance_uid_invoice_flow_uid, self.invoice_instance_uid_invoice_status_uid, self.invoice_instance_uid_invoice_category_uid, self.invoice_instance_uid_invoice_type_uid, self.invoice_instance_uid_period_uid, self.invoice_instance_uid_currency_uid, self.invoice_instance_uid_invoice_number, self.invoice_instance_uid_invoice_details, self.invoice_instance_uid_invoice_amount_net, self.invoice_instance_uid_invoice_amount_tax, self.invoice_instance_uid_invoice_amount_gross]


@dataclass(frozen=False)
class time_entry_final_rich_dto(time_entry_final_read_dto):
    time_entry_final_uid: str | None
    time_entry_final_name: str | None
    tenant_uid: str | None
    account_uid: str | None
    project_instance_uid: str | None
    project_milestone_uid: str | None
    invoice_instance_uid: str | None
    entry_period: str | None
    entry_note: str | None
    lock_uid: str | None
    start_date: datetime.datetime | None
    end_date: datetime.datetime | None
    entry_minutes: int | None
    is_approved: int | None
    row_instance: str | None
    row_lock: str | None
    row_owner: str | None
    row_seq: int | None
    row_guid: str | None
    row_version: int | None
    is_active: int | None
    created_date: datetime.datetime | None
    created_by: str | None
    last_updated_date: datetime.datetime | None
    last_updated_by: str | None
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str | None
    tenant_uid_tenant_name: str | None
    tenant_uid_country_uid: str | None
    tenant_uid_tenant_type_uid: str | None
    tenant_uid_tenant_category_uid: str | None
    tenant_uid_tenant_code: str | None
    tenant_uid_tenant_description: str | None
    tenant_uid_start_date: datetime.datetime | None
    tenant_uid_end_date: datetime.datetime | None
    tenant_uid_is_internal: int | None
    tenant_uid_is_system: int | None
    tenant_uid_is_test: int | None
    tenant_uid_account_uid: str | None
    account_uid_account_name: str | None
    account_uid_tenant_uid: str | None
    account_uid_account_type_uid: str | None
    account_uid_account_title_uid: str | None
    account_uid_account_division_uid: str | None
    account_uid_account_group_uid: str | None
    account_uid_auth_identity_uid: str | None
    account_uid_account_email: str | None
    account_uid_display_name: str | None
    account_uid_is_system: int | None
    project_instance_uid_project_instance_name: str | None
    project_instance_uid_tenant_uid: str | None
    project_instance_uid_client_uid: str | None
    project_instance_uid_project_type_uid: str | None
    project_instance_uid_manager_account_uid: str | None
    project_instance_uid_project_group_uid: str | None
    project_instance_uid_project_code: str | None
    project_instance_uid_project_description: str | None
    project_instance_uid_is_billable: int | None
    project_instance_uid_start_date: datetime.datetime | None
    project_instance_uid_end_date: datetime.datetime | None
    project_instance_uid_current_billed: str | None
    project_instance_uid_budget: str | None
    project_milestone_uid_project_milestone_name: str | None
    project_milestone_uid_tenant_uid: str | None
    project_milestone_uid_client_uid: str | None
    project_milestone_uid_project_instance_uid: str | None
    project_milestone_uid_project_budget_uid: str | None
    project_milestone_uid_start_date: datetime.datetime | None
    project_milestone_uid_end_date: datetime.datetime | None
    project_milestone_uid_status_name: str | None
    invoice_instance_uid_invoice_instance_name: str | None
    invoice_instance_uid_tenant_uid: str | None
    invoice_instance_uid_account_uid: str | None
    invoice_instance_uid_invoice_flow_uid: str | None
    invoice_instance_uid_invoice_status_uid: str | None
    invoice_instance_uid_invoice_category_uid: str | None
    invoice_instance_uid_invoice_type_uid: str | None
    invoice_instance_uid_period_uid: str | None
    invoice_instance_uid_currency_uid: str | None
    invoice_instance_uid_invoice_number: str | None
    invoice_instance_uid_invoice_details: str | None
    invoice_instance_uid_invoice_amount_net: str | None
    invoice_instance_uid_invoice_amount_tax: str | None
    invoice_instance_uid_invoice_amount_gross: str | None
    def __init__(self, time_entry_final_uid: str | None, time_entry_final_name: str | None, tenant_uid: str | None, account_uid: str | None, project_instance_uid: str | None, project_milestone_uid: str | None, invoice_instance_uid: str | None, entry_period: str | None, entry_note: str | None, lock_uid: str | None, start_date: datetime.datetime | None, end_date: datetime.datetime | None, entry_minutes: int | None, is_approved: int | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None, tenant_uid_tenant_name: str | None, tenant_uid_country_uid: str | None, tenant_uid_tenant_type_uid: str | None, tenant_uid_tenant_category_uid: str | None, tenant_uid_tenant_code: str | None, tenant_uid_tenant_description: str | None, tenant_uid_start_date: datetime.datetime | None, tenant_uid_end_date: datetime.datetime | None, tenant_uid_is_internal: int | None, tenant_uid_is_system: int | None, tenant_uid_is_test: int | None, tenant_uid_account_uid: str | None, account_uid_account_name: str | None, account_uid_tenant_uid: str | None, account_uid_account_type_uid: str | None, account_uid_account_title_uid: str | None, account_uid_account_division_uid: str | None, account_uid_account_group_uid: str | None, account_uid_auth_identity_uid: str | None, account_uid_account_email: str | None, account_uid_display_name: str | None, account_uid_is_system: int | None, project_instance_uid_project_instance_name: str | None, project_instance_uid_tenant_uid: str | None, project_instance_uid_client_uid: str | None, project_instance_uid_project_type_uid: str | None, project_instance_uid_manager_account_uid: str | None, project_instance_uid_project_group_uid: str | None, project_instance_uid_project_code: str | None, project_instance_uid_project_description: str | None, project_instance_uid_is_billable: int | None, project_instance_uid_start_date: datetime.datetime | None, project_instance_uid_end_date: datetime.datetime | None, project_instance_uid_current_billed: str | None, project_instance_uid_budget: str | None, project_milestone_uid_project_milestone_name: str | None, project_milestone_uid_tenant_uid: str | None, project_milestone_uid_client_uid: str | None, project_milestone_uid_project_instance_uid: str | None, project_milestone_uid_project_budget_uid: str | None, project_milestone_uid_start_date: datetime.datetime | None, project_milestone_uid_end_date: datetime.datetime | None, project_milestone_uid_status_name: str | None, invoice_instance_uid_invoice_instance_name: str | None, invoice_instance_uid_tenant_uid: str | None, invoice_instance_uid_account_uid: str | None, invoice_instance_uid_invoice_flow_uid: str | None, invoice_instance_uid_invoice_status_uid: str | None, invoice_instance_uid_invoice_category_uid: str | None, invoice_instance_uid_invoice_type_uid: str | None, invoice_instance_uid_period_uid: str | None, invoice_instance_uid_currency_uid: str | None, invoice_instance_uid_invoice_number: str | None, invoice_instance_uid_invoice_details: str | None, invoice_instance_uid_invoice_amount_net: str | None, invoice_instance_uid_invoice_amount_tax: str | None, invoice_instance_uid_invoice_amount_gross: str | None):
        self.time_entry_final_uid = time_entry_final_uid
        self.time_entry_final_name = time_entry_final_name
        self.tenant_uid = tenant_uid
        self.account_uid = account_uid
        self.project_instance_uid = project_instance_uid
        self.project_milestone_uid = project_milestone_uid
        self.invoice_instance_uid = invoice_instance_uid
        self.entry_period = entry_period
        self.entry_note = entry_note
        self.lock_uid = lock_uid
        self.start_date = start_date
        self.end_date = end_date
        self.entry_minutes = entry_minutes
        self.is_approved = is_approved
        self.row_instance = row_instance
        self.row_lock = row_lock
        self.row_owner = row_owner
        self.row_seq = row_seq
        self.row_guid = row_guid
        self.row_version = row_version
        self.is_active = is_active
        self.created_date = created_date
        self.created_by = created_by
        self.last_updated_date = last_updated_date
        self.last_updated_by = last_updated_by
        self.removed_date = removed_date
        self.removed_by = removed_by
        self.custom_attributes = custom_attributes
        self.tenant_uid_tenant_name = tenant_uid_tenant_name
        self.tenant_uid_country_uid = tenant_uid_country_uid
        self.tenant_uid_tenant_type_uid = tenant_uid_tenant_type_uid
        self.tenant_uid_tenant_category_uid = tenant_uid_tenant_category_uid
        self.tenant_uid_tenant_code = tenant_uid_tenant_code
        self.tenant_uid_tenant_description = tenant_uid_tenant_description
        self.tenant_uid_start_date = tenant_uid_start_date
        self.tenant_uid_end_date = tenant_uid_end_date
        self.tenant_uid_is_internal = tenant_uid_is_internal
        self.tenant_uid_is_system = tenant_uid_is_system
        self.tenant_uid_is_test = tenant_uid_is_test
        self.tenant_uid_account_uid = tenant_uid_account_uid
        self.account_uid_account_name = account_uid_account_name
        self.account_uid_tenant_uid = account_uid_tenant_uid
        self.account_uid_account_type_uid = account_uid_account_type_uid
        self.account_uid_account_title_uid = account_uid_account_title_uid
        self.account_uid_account_division_uid = account_uid_account_division_uid
        self.account_uid_account_group_uid = account_uid_account_group_uid
        self.account_uid_auth_identity_uid = account_uid_auth_identity_uid
        self.account_uid_account_email = account_uid_account_email
        self.account_uid_display_name = account_uid_display_name
        self.account_uid_is_system = account_uid_is_system
        self.project_instance_uid_project_instance_name = project_instance_uid_project_instance_name
        self.project_instance_uid_tenant_uid = project_instance_uid_tenant_uid
        self.project_instance_uid_client_uid = project_instance_uid_client_uid
        self.project_instance_uid_project_type_uid = project_instance_uid_project_type_uid
        self.project_instance_uid_manager_account_uid = project_instance_uid_manager_account_uid
        self.project_instance_uid_project_group_uid = project_instance_uid_project_group_uid
        self.project_instance_uid_project_code = project_instance_uid_project_code
        self.project_instance_uid_project_description = project_instance_uid_project_description
        self.project_instance_uid_is_billable = project_instance_uid_is_billable
        self.project_instance_uid_start_date = project_instance_uid_start_date
        self.project_instance_uid_end_date = project_instance_uid_end_date
        self.project_instance_uid_current_billed = project_instance_uid_current_billed
        self.project_instance_uid_budget = project_instance_uid_budget
        self.project_milestone_uid_project_milestone_name = project_milestone_uid_project_milestone_name
        self.project_milestone_uid_tenant_uid = project_milestone_uid_tenant_uid
        self.project_milestone_uid_client_uid = project_milestone_uid_client_uid
        self.project_milestone_uid_project_instance_uid = project_milestone_uid_project_instance_uid
        self.project_milestone_uid_project_budget_uid = project_milestone_uid_project_budget_uid
        self.project_milestone_uid_start_date = project_milestone_uid_start_date
        self.project_milestone_uid_end_date = project_milestone_uid_end_date
        self.project_milestone_uid_status_name = project_milestone_uid_status_name
        self.invoice_instance_uid_invoice_instance_name = invoice_instance_uid_invoice_instance_name
        self.invoice_instance_uid_tenant_uid = invoice_instance_uid_tenant_uid
        self.invoice_instance_uid_account_uid = invoice_instance_uid_account_uid
        self.invoice_instance_uid_invoice_flow_uid = invoice_instance_uid_invoice_flow_uid
        self.invoice_instance_uid_invoice_status_uid = invoice_instance_uid_invoice_status_uid
        self.invoice_instance_uid_invoice_category_uid = invoice_instance_uid_invoice_category_uid
        self.invoice_instance_uid_invoice_type_uid = invoice_instance_uid_invoice_type_uid
        self.invoice_instance_uid_period_uid = invoice_instance_uid_period_uid
        self.invoice_instance_uid_currency_uid = invoice_instance_uid_currency_uid
        self.invoice_instance_uid_invoice_number = invoice_instance_uid_invoice_number
        self.invoice_instance_uid_invoice_details = invoice_instance_uid_invoice_details
        self.invoice_instance_uid_invoice_amount_net = invoice_instance_uid_invoice_amount_net
        self.invoice_instance_uid_invoice_amount_tax = invoice_instance_uid_invoice_amount_tax
        self.invoice_instance_uid_invoice_amount_gross = invoice_instance_uid_invoice_amount_gross
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.time_entry_final_uid, self.time_entry_final_name, self.tenant_uid, self.account_uid, self.project_instance_uid, self.project_milestone_uid, self.invoice_instance_uid, self.entry_period, self.entry_note, self.lock_uid, self.start_date, self.end_date, self.entry_minutes, self.is_approved, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes, self.tenant_uid_tenant_name, self.tenant_uid_country_uid, self.tenant_uid_tenant_type_uid, self.tenant_uid_tenant_category_uid, self.tenant_uid_tenant_code, self.tenant_uid_tenant_description, self.tenant_uid_start_date, self.tenant_uid_end_date, self.tenant_uid_is_internal, self.tenant_uid_is_system, self.tenant_uid_is_test, self.tenant_uid_account_uid, self.account_uid_account_name, self.account_uid_tenant_uid, self.account_uid_account_type_uid, self.account_uid_account_title_uid, self.account_uid_account_division_uid, self.account_uid_account_group_uid, self.account_uid_auth_identity_uid, self.account_uid_account_email, self.account_uid_display_name, self.account_uid_is_system, self.project_instance_uid_project_instance_name, self.project_instance_uid_tenant_uid, self.project_instance_uid_client_uid, self.project_instance_uid_project_type_uid, self.project_instance_uid_manager_account_uid, self.project_instance_uid_project_group_uid, self.project_instance_uid_project_code, self.project_instance_uid_project_description, self.project_instance_uid_is_billable, self.project_instance_uid_start_date, self.project_instance_uid_end_date, self.project_instance_uid_current_billed, self.project_instance_uid_budget, self.project_milestone_uid_project_milestone_name, self.project_milestone_uid_tenant_uid, self.project_milestone_uid_client_uid, self.project_milestone_uid_project_instance_uid, self.project_milestone_uid_project_budget_uid, self.project_milestone_uid_start_date, self.project_milestone_uid_end_date, self.project_milestone_uid_status_name, self.invoice_instance_uid_invoice_instance_name, self.invoice_instance_uid_tenant_uid, self.invoice_instance_uid_account_uid, self.invoice_instance_uid_invoice_flow_uid, self.invoice_instance_uid_invoice_status_uid, self.invoice_instance_uid_invoice_category_uid, self.invoice_instance_uid_invoice_type_uid, self.invoice_instance_uid_period_uid, self.invoice_instance_uid_currency_uid, self.invoice_instance_uid_invoice_number, self.invoice_instance_uid_invoice_details, self.invoice_instance_uid_invoice_amount_net, self.invoice_instance_uid_invoice_amount_tax, self.invoice_instance_uid_invoice_amount_gross]


@dataclass(frozen=False)
class time_entry_invoice_rich_dto(time_entry_invoice_read_dto):
    time_entry_invoice_uid: str | None
    time_entry_invoice_name: str | None
    tenant_uid: str | None
    account_uid: str | None
    time_submit_uid: str | None
    time_entry_uid: str | None
    project_instance_uid: str | None
    project_milestone_uid: str | None
    period_uid: str | None
    invoice_instance_uid: str | None
    entry_period: str | None
    entry_note: str | None
    lock_row: str | None
    start_date: datetime.datetime | None
    end_date: datetime.datetime | None
    entry_minutes: int | None
    is_approved: int | None
    row_instance: str | None
    row_lock: str | None
    row_owner: str | None
    row_seq: int | None
    row_guid: str | None
    row_version: int | None
    is_active: int | None
    created_date: datetime.datetime | None
    created_by: str | None
    last_updated_date: datetime.datetime | None
    last_updated_by: str | None
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str | None
    tenant_uid_tenant_name: str | None
    tenant_uid_country_uid: str | None
    tenant_uid_tenant_type_uid: str | None
    tenant_uid_tenant_category_uid: str | None
    tenant_uid_tenant_code: str | None
    tenant_uid_tenant_description: str | None
    tenant_uid_start_date: datetime.datetime | None
    tenant_uid_end_date: datetime.datetime | None
    tenant_uid_is_internal: int | None
    tenant_uid_is_system: int | None
    tenant_uid_is_test: int | None
    tenant_uid_account_uid: str | None
    account_uid_account_name: str | None
    account_uid_tenant_uid: str | None
    account_uid_account_type_uid: str | None
    account_uid_account_title_uid: str | None
    account_uid_account_division_uid: str | None
    account_uid_account_group_uid: str | None
    account_uid_auth_identity_uid: str | None
    account_uid_account_email: str | None
    account_uid_display_name: str | None
    account_uid_is_system: int | None
    time_submit_uid_time_submit_name: str | None
    time_submit_uid_tenant_uid: str | None
    time_submit_uid_account_uid: str | None
    time_submit_uid_period_uid: str | None
    time_submit_uid_time_submit_description: str | None
    time_entry_uid_time_entry_name: str | None
    time_entry_uid_time_submit_uid: str | None
    time_entry_uid_tenant_uid: str | None
    time_entry_uid_account_uid: str | None
    time_entry_uid_project_instance_uid: str | None
    time_entry_uid_project_milestone_uid: str | None
    time_entry_uid_period_uid: str | None
    time_entry_uid_invoice_instance_uid: str | None
    time_entry_uid_entry_period: str | None
    time_entry_uid_entry_note: str | None
    time_entry_uid_lock_row: str | None
    time_entry_uid_start_date: datetime.datetime | None
    time_entry_uid_end_date: datetime.datetime | None
    time_entry_uid_entry_minutes: int | None
    time_entry_uid_is_approved: int | None
    project_instance_uid_project_instance_name: str | None
    project_instance_uid_tenant_uid: str | None
    project_instance_uid_client_uid: str | None
    project_instance_uid_project_type_uid: str | None
    project_instance_uid_manager_account_uid: str | None
    project_instance_uid_project_group_uid: str | None
    project_instance_uid_project_code: str | None
    project_instance_uid_project_description: str | None
    project_instance_uid_is_billable: int | None
    project_instance_uid_start_date: datetime.datetime | None
    project_instance_uid_end_date: datetime.datetime | None
    project_instance_uid_current_billed: str | None
    project_instance_uid_budget: str | None
    project_milestone_uid_project_milestone_name: str | None
    project_milestone_uid_tenant_uid: str | None
    project_milestone_uid_client_uid: str | None
    project_milestone_uid_project_instance_uid: str | None
    project_milestone_uid_project_budget_uid: str | None
    project_milestone_uid_start_date: datetime.datetime | None
    project_milestone_uid_end_date: datetime.datetime | None
    project_milestone_uid_status_name: str | None
    period_uid_period_name: str | None
    period_uid_period_number: int | None
    period_uid_period_type: str | None
    period_uid_period_start_time: datetime.datetime | None
    period_uid_period_end_time: datetime.datetime | None
    period_uid_period_year: int | None
    period_uid_period_quarter: int | None
    period_uid_period_month: int | None
    period_uid_period_week: int | None
    period_uid_period_day: int | None
    invoice_instance_uid_invoice_instance_name: str | None
    invoice_instance_uid_tenant_uid: str | None
    invoice_instance_uid_account_uid: str | None
    invoice_instance_uid_invoice_flow_uid: str | None
    invoice_instance_uid_invoice_status_uid: str | None
    invoice_instance_uid_invoice_category_uid: str | None
    invoice_instance_uid_invoice_type_uid: str | None
    invoice_instance_uid_period_uid: str | None
    invoice_instance_uid_currency_uid: str | None
    invoice_instance_uid_invoice_number: str | None
    invoice_instance_uid_invoice_details: str | None
    invoice_instance_uid_invoice_amount_net: str | None
    invoice_instance_uid_invoice_amount_tax: str | None
    invoice_instance_uid_invoice_amount_gross: str | None
    def __init__(self, time_entry_invoice_uid: str | None, time_entry_invoice_name: str | None, tenant_uid: str | None, account_uid: str | None, time_submit_uid: str | None, time_entry_uid: str | None, project_instance_uid: str | None, project_milestone_uid: str | None, period_uid: str | None, invoice_instance_uid: str | None, entry_period: str | None, entry_note: str | None, lock_row: str | None, start_date: datetime.datetime | None, end_date: datetime.datetime | None, entry_minutes: int | None, is_approved: int | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None, tenant_uid_tenant_name: str | None, tenant_uid_country_uid: str | None, tenant_uid_tenant_type_uid: str | None, tenant_uid_tenant_category_uid: str | None, tenant_uid_tenant_code: str | None, tenant_uid_tenant_description: str | None, tenant_uid_start_date: datetime.datetime | None, tenant_uid_end_date: datetime.datetime | None, tenant_uid_is_internal: int | None, tenant_uid_is_system: int | None, tenant_uid_is_test: int | None, tenant_uid_account_uid: str | None, account_uid_account_name: str | None, account_uid_tenant_uid: str | None, account_uid_account_type_uid: str | None, account_uid_account_title_uid: str | None, account_uid_account_division_uid: str | None, account_uid_account_group_uid: str | None, account_uid_auth_identity_uid: str | None, account_uid_account_email: str | None, account_uid_display_name: str | None, account_uid_is_system: int | None, time_submit_uid_time_submit_name: str | None, time_submit_uid_tenant_uid: str | None, time_submit_uid_account_uid: str | None, time_submit_uid_period_uid: str | None, time_submit_uid_time_submit_description: str | None, time_entry_uid_time_entry_name: str | None, time_entry_uid_time_submit_uid: str | None, time_entry_uid_tenant_uid: str | None, time_entry_uid_account_uid: str | None, time_entry_uid_project_instance_uid: str | None, time_entry_uid_project_milestone_uid: str | None, time_entry_uid_period_uid: str | None, time_entry_uid_invoice_instance_uid: str | None, time_entry_uid_entry_period: str | None, time_entry_uid_entry_note: str | None, time_entry_uid_lock_row: str | None, time_entry_uid_start_date: datetime.datetime | None, time_entry_uid_end_date: datetime.datetime | None, time_entry_uid_entry_minutes: int | None, time_entry_uid_is_approved: int | None, project_instance_uid_project_instance_name: str | None, project_instance_uid_tenant_uid: str | None, project_instance_uid_client_uid: str | None, project_instance_uid_project_type_uid: str | None, project_instance_uid_manager_account_uid: str | None, project_instance_uid_project_group_uid: str | None, project_instance_uid_project_code: str | None, project_instance_uid_project_description: str | None, project_instance_uid_is_billable: int | None, project_instance_uid_start_date: datetime.datetime | None, project_instance_uid_end_date: datetime.datetime | None, project_instance_uid_current_billed: str | None, project_instance_uid_budget: str | None, project_milestone_uid_project_milestone_name: str | None, project_milestone_uid_tenant_uid: str | None, project_milestone_uid_client_uid: str | None, project_milestone_uid_project_instance_uid: str | None, project_milestone_uid_project_budget_uid: str | None, project_milestone_uid_start_date: datetime.datetime | None, project_milestone_uid_end_date: datetime.datetime | None, project_milestone_uid_status_name: str | None, period_uid_period_name: str | None, period_uid_period_number: int | None, period_uid_period_type: str | None, period_uid_period_start_time: datetime.datetime | None, period_uid_period_end_time: datetime.datetime | None, period_uid_period_year: int | None, period_uid_period_quarter: int | None, period_uid_period_month: int | None, period_uid_period_week: int | None, period_uid_period_day: int | None, invoice_instance_uid_invoice_instance_name: str | None, invoice_instance_uid_tenant_uid: str | None, invoice_instance_uid_account_uid: str | None, invoice_instance_uid_invoice_flow_uid: str | None, invoice_instance_uid_invoice_status_uid: str | None, invoice_instance_uid_invoice_category_uid: str | None, invoice_instance_uid_invoice_type_uid: str | None, invoice_instance_uid_period_uid: str | None, invoice_instance_uid_currency_uid: str | None, invoice_instance_uid_invoice_number: str | None, invoice_instance_uid_invoice_details: str | None, invoice_instance_uid_invoice_amount_net: str | None, invoice_instance_uid_invoice_amount_tax: str | None, invoice_instance_uid_invoice_amount_gross: str | None):
        self.time_entry_invoice_uid = time_entry_invoice_uid
        self.time_entry_invoice_name = time_entry_invoice_name
        self.tenant_uid = tenant_uid
        self.account_uid = account_uid
        self.time_submit_uid = time_submit_uid
        self.time_entry_uid = time_entry_uid
        self.project_instance_uid = project_instance_uid
        self.project_milestone_uid = project_milestone_uid
        self.period_uid = period_uid
        self.invoice_instance_uid = invoice_instance_uid
        self.entry_period = entry_period
        self.entry_note = entry_note
        self.lock_row = lock_row
        self.start_date = start_date
        self.end_date = end_date
        self.entry_minutes = entry_minutes
        self.is_approved = is_approved
        self.row_instance = row_instance
        self.row_lock = row_lock
        self.row_owner = row_owner
        self.row_seq = row_seq
        self.row_guid = row_guid
        self.row_version = row_version
        self.is_active = is_active
        self.created_date = created_date
        self.created_by = created_by
        self.last_updated_date = last_updated_date
        self.last_updated_by = last_updated_by
        self.removed_date = removed_date
        self.removed_by = removed_by
        self.custom_attributes = custom_attributes
        self.tenant_uid_tenant_name = tenant_uid_tenant_name
        self.tenant_uid_country_uid = tenant_uid_country_uid
        self.tenant_uid_tenant_type_uid = tenant_uid_tenant_type_uid
        self.tenant_uid_tenant_category_uid = tenant_uid_tenant_category_uid
        self.tenant_uid_tenant_code = tenant_uid_tenant_code
        self.tenant_uid_tenant_description = tenant_uid_tenant_description
        self.tenant_uid_start_date = tenant_uid_start_date
        self.tenant_uid_end_date = tenant_uid_end_date
        self.tenant_uid_is_internal = tenant_uid_is_internal
        self.tenant_uid_is_system = tenant_uid_is_system
        self.tenant_uid_is_test = tenant_uid_is_test
        self.tenant_uid_account_uid = tenant_uid_account_uid
        self.account_uid_account_name = account_uid_account_name
        self.account_uid_tenant_uid = account_uid_tenant_uid
        self.account_uid_account_type_uid = account_uid_account_type_uid
        self.account_uid_account_title_uid = account_uid_account_title_uid
        self.account_uid_account_division_uid = account_uid_account_division_uid
        self.account_uid_account_group_uid = account_uid_account_group_uid
        self.account_uid_auth_identity_uid = account_uid_auth_identity_uid
        self.account_uid_account_email = account_uid_account_email
        self.account_uid_display_name = account_uid_display_name
        self.account_uid_is_system = account_uid_is_system
        self.time_submit_uid_time_submit_name = time_submit_uid_time_submit_name
        self.time_submit_uid_tenant_uid = time_submit_uid_tenant_uid
        self.time_submit_uid_account_uid = time_submit_uid_account_uid
        self.time_submit_uid_period_uid = time_submit_uid_period_uid
        self.time_submit_uid_time_submit_description = time_submit_uid_time_submit_description
        self.time_entry_uid_time_entry_name = time_entry_uid_time_entry_name
        self.time_entry_uid_time_submit_uid = time_entry_uid_time_submit_uid
        self.time_entry_uid_tenant_uid = time_entry_uid_tenant_uid
        self.time_entry_uid_account_uid = time_entry_uid_account_uid
        self.time_entry_uid_project_instance_uid = time_entry_uid_project_instance_uid
        self.time_entry_uid_project_milestone_uid = time_entry_uid_project_milestone_uid
        self.time_entry_uid_period_uid = time_entry_uid_period_uid
        self.time_entry_uid_invoice_instance_uid = time_entry_uid_invoice_instance_uid
        self.time_entry_uid_entry_period = time_entry_uid_entry_period
        self.time_entry_uid_entry_note = time_entry_uid_entry_note
        self.time_entry_uid_lock_row = time_entry_uid_lock_row
        self.time_entry_uid_start_date = time_entry_uid_start_date
        self.time_entry_uid_end_date = time_entry_uid_end_date
        self.time_entry_uid_entry_minutes = time_entry_uid_entry_minutes
        self.time_entry_uid_is_approved = time_entry_uid_is_approved
        self.project_instance_uid_project_instance_name = project_instance_uid_project_instance_name
        self.project_instance_uid_tenant_uid = project_instance_uid_tenant_uid
        self.project_instance_uid_client_uid = project_instance_uid_client_uid
        self.project_instance_uid_project_type_uid = project_instance_uid_project_type_uid
        self.project_instance_uid_manager_account_uid = project_instance_uid_manager_account_uid
        self.project_instance_uid_project_group_uid = project_instance_uid_project_group_uid
        self.project_instance_uid_project_code = project_instance_uid_project_code
        self.project_instance_uid_project_description = project_instance_uid_project_description
        self.project_instance_uid_is_billable = project_instance_uid_is_billable
        self.project_instance_uid_start_date = project_instance_uid_start_date
        self.project_instance_uid_end_date = project_instance_uid_end_date
        self.project_instance_uid_current_billed = project_instance_uid_current_billed
        self.project_instance_uid_budget = project_instance_uid_budget
        self.project_milestone_uid_project_milestone_name = project_milestone_uid_project_milestone_name
        self.project_milestone_uid_tenant_uid = project_milestone_uid_tenant_uid
        self.project_milestone_uid_client_uid = project_milestone_uid_client_uid
        self.project_milestone_uid_project_instance_uid = project_milestone_uid_project_instance_uid
        self.project_milestone_uid_project_budget_uid = project_milestone_uid_project_budget_uid
        self.project_milestone_uid_start_date = project_milestone_uid_start_date
        self.project_milestone_uid_end_date = project_milestone_uid_end_date
        self.project_milestone_uid_status_name = project_milestone_uid_status_name
        self.period_uid_period_name = period_uid_period_name
        self.period_uid_period_number = period_uid_period_number
        self.period_uid_period_type = period_uid_period_type
        self.period_uid_period_start_time = period_uid_period_start_time
        self.period_uid_period_end_time = period_uid_period_end_time
        self.period_uid_period_year = period_uid_period_year
        self.period_uid_period_quarter = period_uid_period_quarter
        self.period_uid_period_month = period_uid_period_month
        self.period_uid_period_week = period_uid_period_week
        self.period_uid_period_day = period_uid_period_day
        self.invoice_instance_uid_invoice_instance_name = invoice_instance_uid_invoice_instance_name
        self.invoice_instance_uid_tenant_uid = invoice_instance_uid_tenant_uid
        self.invoice_instance_uid_account_uid = invoice_instance_uid_account_uid
        self.invoice_instance_uid_invoice_flow_uid = invoice_instance_uid_invoice_flow_uid
        self.invoice_instance_uid_invoice_status_uid = invoice_instance_uid_invoice_status_uid
        self.invoice_instance_uid_invoice_category_uid = invoice_instance_uid_invoice_category_uid
        self.invoice_instance_uid_invoice_type_uid = invoice_instance_uid_invoice_type_uid
        self.invoice_instance_uid_period_uid = invoice_instance_uid_period_uid
        self.invoice_instance_uid_currency_uid = invoice_instance_uid_currency_uid
        self.invoice_instance_uid_invoice_number = invoice_instance_uid_invoice_number
        self.invoice_instance_uid_invoice_details = invoice_instance_uid_invoice_details
        self.invoice_instance_uid_invoice_amount_net = invoice_instance_uid_invoice_amount_net
        self.invoice_instance_uid_invoice_amount_tax = invoice_instance_uid_invoice_amount_tax
        self.invoice_instance_uid_invoice_amount_gross = invoice_instance_uid_invoice_amount_gross
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.time_entry_invoice_uid, self.time_entry_invoice_name, self.tenant_uid, self.account_uid, self.time_submit_uid, self.time_entry_uid, self.project_instance_uid, self.project_milestone_uid, self.period_uid, self.invoice_instance_uid, self.entry_period, self.entry_note, self.lock_row, self.start_date, self.end_date, self.entry_minutes, self.is_approved, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes, self.tenant_uid_tenant_name, self.tenant_uid_country_uid, self.tenant_uid_tenant_type_uid, self.tenant_uid_tenant_category_uid, self.tenant_uid_tenant_code, self.tenant_uid_tenant_description, self.tenant_uid_start_date, self.tenant_uid_end_date, self.tenant_uid_is_internal, self.tenant_uid_is_system, self.tenant_uid_is_test, self.tenant_uid_account_uid, self.account_uid_account_name, self.account_uid_tenant_uid, self.account_uid_account_type_uid, self.account_uid_account_title_uid, self.account_uid_account_division_uid, self.account_uid_account_group_uid, self.account_uid_auth_identity_uid, self.account_uid_account_email, self.account_uid_display_name, self.account_uid_is_system, self.time_submit_uid_time_submit_name, self.time_submit_uid_tenant_uid, self.time_submit_uid_account_uid, self.time_submit_uid_period_uid, self.time_submit_uid_time_submit_description, self.time_entry_uid_time_entry_name, self.time_entry_uid_time_submit_uid, self.time_entry_uid_tenant_uid, self.time_entry_uid_account_uid, self.time_entry_uid_project_instance_uid, self.time_entry_uid_project_milestone_uid, self.time_entry_uid_period_uid, self.time_entry_uid_invoice_instance_uid, self.time_entry_uid_entry_period, self.time_entry_uid_entry_note, self.time_entry_uid_lock_row, self.time_entry_uid_start_date, self.time_entry_uid_end_date, self.time_entry_uid_entry_minutes, self.time_entry_uid_is_approved, self.project_instance_uid_project_instance_name, self.project_instance_uid_tenant_uid, self.project_instance_uid_client_uid, self.project_instance_uid_project_type_uid, self.project_instance_uid_manager_account_uid, self.project_instance_uid_project_group_uid, self.project_instance_uid_project_code, self.project_instance_uid_project_description, self.project_instance_uid_is_billable, self.project_instance_uid_start_date, self.project_instance_uid_end_date, self.project_instance_uid_current_billed, self.project_instance_uid_budget, self.project_milestone_uid_project_milestone_name, self.project_milestone_uid_tenant_uid, self.project_milestone_uid_client_uid, self.project_milestone_uid_project_instance_uid, self.project_milestone_uid_project_budget_uid, self.project_milestone_uid_start_date, self.project_milestone_uid_end_date, self.project_milestone_uid_status_name, self.period_uid_period_name, self.period_uid_period_number, self.period_uid_period_type, self.period_uid_period_start_time, self.period_uid_period_end_time, self.period_uid_period_year, self.period_uid_period_quarter, self.period_uid_period_month, self.period_uid_period_week, self.period_uid_period_day, self.invoice_instance_uid_invoice_instance_name, self.invoice_instance_uid_tenant_uid, self.invoice_instance_uid_account_uid, self.invoice_instance_uid_invoice_flow_uid, self.invoice_instance_uid_invoice_status_uid, self.invoice_instance_uid_invoice_category_uid, self.invoice_instance_uid_invoice_type_uid, self.invoice_instance_uid_period_uid, self.invoice_instance_uid_currency_uid, self.invoice_instance_uid_invoice_number, self.invoice_instance_uid_invoice_details, self.invoice_instance_uid_invoice_amount_net, self.invoice_instance_uid_invoice_amount_tax, self.invoice_instance_uid_invoice_amount_gross]


@dataclass(frozen=False)
class time_rule_rich_dto(time_rule_read_dto):
    time_rule_uid: str | None
    time_rule_name: str | None
    row_instance: str | None
    row_lock: str | None
    row_owner: str | None
    row_seq: int | None
    row_guid: str | None
    row_version: int | None
    is_active: int | None
    created_date: datetime.datetime | None
    created_by: str | None
    last_updated_date: datetime.datetime | None
    last_updated_by: str | None
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str | None
    def __init__(self, time_rule_uid: str | None, time_rule_name: str | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None):
        self.time_rule_uid = time_rule_uid
        self.time_rule_name = time_rule_name
        self.row_instance = row_instance
        self.row_lock = row_lock
        self.row_owner = row_owner
        self.row_seq = row_seq
        self.row_guid = row_guid
        self.row_version = row_version
        self.is_active = is_active
        self.created_date = created_date
        self.created_by = created_by
        self.last_updated_date = last_updated_date
        self.last_updated_by = last_updated_by
        self.removed_date = removed_date
        self.removed_by = removed_by
        self.custom_attributes = custom_attributes
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.time_rule_uid, self.time_rule_name, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]


@dataclass(frozen=False)
class time_rule_client_rich_dto(time_rule_client_read_dto):
    time_rule_client_uid: str | None
    time_rule_client_name: str | None
    time_rule_definition: str | None
    row_instance: str | None
    row_lock: str | None
    row_owner: str | None
    row_seq: int | None
    row_guid: str | None
    row_version: int | None
    is_active: int | None
    created_date: datetime.datetime | None
    created_by: str | None
    last_updated_date: datetime.datetime | None
    last_updated_by: str | None
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str | None
    time_rule_client_uid_client_name: str | None
    time_rule_client_uid_tenant_uid: str | None
    time_rule_client_uid_country_uid: str | None
    time_rule_client_uid_client_type_uid: str | None
    time_rule_client_uid_client_category_uid: str | None
    time_rule_client_uid_account_uid: str | None
    time_rule_client_uid_client_code: str | None
    time_rule_client_uid_client_description: str | None
    time_rule_client_uid_start_date: datetime.datetime | None
    time_rule_client_uid_end_date: datetime.datetime | None
    time_rule_client_uid_is_internal: int | None
    time_rule_client_uid_is_system: int | None
    time_rule_client_uid_is_test: int | None
    def __init__(self, time_rule_client_uid: str | None, time_rule_client_name: str | None, time_rule_definition: str | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None, time_rule_client_uid_client_name: str | None, time_rule_client_uid_tenant_uid: str | None, time_rule_client_uid_country_uid: str | None, time_rule_client_uid_client_type_uid: str | None, time_rule_client_uid_client_category_uid: str | None, time_rule_client_uid_account_uid: str | None, time_rule_client_uid_client_code: str | None, time_rule_client_uid_client_description: str | None, time_rule_client_uid_start_date: datetime.datetime | None, time_rule_client_uid_end_date: datetime.datetime | None, time_rule_client_uid_is_internal: int | None, time_rule_client_uid_is_system: int | None, time_rule_client_uid_is_test: int | None):
        self.time_rule_client_uid = time_rule_client_uid
        self.time_rule_client_name = time_rule_client_name
        self.time_rule_definition = time_rule_definition
        self.row_instance = row_instance
        self.row_lock = row_lock
        self.row_owner = row_owner
        self.row_seq = row_seq
        self.row_guid = row_guid
        self.row_version = row_version
        self.is_active = is_active
        self.created_date = created_date
        self.created_by = created_by
        self.last_updated_date = last_updated_date
        self.last_updated_by = last_updated_by
        self.removed_date = removed_date
        self.removed_by = removed_by
        self.custom_attributes = custom_attributes
        self.time_rule_client_uid_client_name = time_rule_client_uid_client_name
        self.time_rule_client_uid_tenant_uid = time_rule_client_uid_tenant_uid
        self.time_rule_client_uid_country_uid = time_rule_client_uid_country_uid
        self.time_rule_client_uid_client_type_uid = time_rule_client_uid_client_type_uid
        self.time_rule_client_uid_client_category_uid = time_rule_client_uid_client_category_uid
        self.time_rule_client_uid_account_uid = time_rule_client_uid_account_uid
        self.time_rule_client_uid_client_code = time_rule_client_uid_client_code
        self.time_rule_client_uid_client_description = time_rule_client_uid_client_description
        self.time_rule_client_uid_start_date = time_rule_client_uid_start_date
        self.time_rule_client_uid_end_date = time_rule_client_uid_end_date
        self.time_rule_client_uid_is_internal = time_rule_client_uid_is_internal
        self.time_rule_client_uid_is_system = time_rule_client_uid_is_system
        self.time_rule_client_uid_is_test = time_rule_client_uid_is_test
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.time_rule_client_uid, self.time_rule_client_name, self.time_rule_definition, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes, self.time_rule_client_uid_client_name, self.time_rule_client_uid_tenant_uid, self.time_rule_client_uid_country_uid, self.time_rule_client_uid_client_type_uid, self.time_rule_client_uid_client_category_uid, self.time_rule_client_uid_account_uid, self.time_rule_client_uid_client_code, self.time_rule_client_uid_client_description, self.time_rule_client_uid_start_date, self.time_rule_client_uid_end_date, self.time_rule_client_uid_is_internal, self.time_rule_client_uid_is_system, self.time_rule_client_uid_is_test]


@dataclass(frozen=False)
class time_submit_rich_dto(time_submit_read_dto):
    time_submit_uid: str | None
    time_submit_name: str | None
    tenant_uid: str | None
    account_uid: str | None
    period_uid: str | None
    time_submit_description: str | None
    row_instance: str | None
    row_lock: str | None
    row_owner: str | None
    row_seq: int | None
    row_guid: str | None
    row_version: int | None
    is_active: int | None
    created_date: datetime.datetime | None
    created_by: str | None
    last_updated_date: datetime.datetime | None
    last_updated_by: str | None
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str | None
    tenant_uid_tenant_name: str | None
    tenant_uid_country_uid: str | None
    tenant_uid_tenant_type_uid: str | None
    tenant_uid_tenant_category_uid: str | None
    tenant_uid_tenant_code: str | None
    tenant_uid_tenant_description: str | None
    tenant_uid_start_date: datetime.datetime | None
    tenant_uid_end_date: datetime.datetime | None
    tenant_uid_is_internal: int | None
    tenant_uid_is_system: int | None
    tenant_uid_is_test: int | None
    tenant_uid_account_uid: str | None
    account_uid_account_name: str | None
    account_uid_tenant_uid: str | None
    account_uid_account_type_uid: str | None
    account_uid_account_title_uid: str | None
    account_uid_account_division_uid: str | None
    account_uid_account_group_uid: str | None
    account_uid_auth_identity_uid: str | None
    account_uid_account_email: str | None
    account_uid_display_name: str | None
    account_uid_is_system: int | None
    period_uid_period_name: str | None
    period_uid_period_number: int | None
    period_uid_period_type: str | None
    period_uid_period_start_time: datetime.datetime | None
    period_uid_period_end_time: datetime.datetime | None
    period_uid_period_year: int | None
    period_uid_period_quarter: int | None
    period_uid_period_month: int | None
    period_uid_period_week: int | None
    period_uid_period_day: int | None
    def __init__(self, time_submit_uid: str | None, time_submit_name: str | None, tenant_uid: str | None, account_uid: str | None, period_uid: str | None, time_submit_description: str | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None, tenant_uid_tenant_name: str | None, tenant_uid_country_uid: str | None, tenant_uid_tenant_type_uid: str | None, tenant_uid_tenant_category_uid: str | None, tenant_uid_tenant_code: str | None, tenant_uid_tenant_description: str | None, tenant_uid_start_date: datetime.datetime | None, tenant_uid_end_date: datetime.datetime | None, tenant_uid_is_internal: int | None, tenant_uid_is_system: int | None, tenant_uid_is_test: int | None, tenant_uid_account_uid: str | None, account_uid_account_name: str | None, account_uid_tenant_uid: str | None, account_uid_account_type_uid: str | None, account_uid_account_title_uid: str | None, account_uid_account_division_uid: str | None, account_uid_account_group_uid: str | None, account_uid_auth_identity_uid: str | None, account_uid_account_email: str | None, account_uid_display_name: str | None, account_uid_is_system: int | None, period_uid_period_name: str | None, period_uid_period_number: int | None, period_uid_period_type: str | None, period_uid_period_start_time: datetime.datetime | None, period_uid_period_end_time: datetime.datetime | None, period_uid_period_year: int | None, period_uid_period_quarter: int | None, period_uid_period_month: int | None, period_uid_period_week: int | None, period_uid_period_day: int | None):
        self.time_submit_uid = time_submit_uid
        self.time_submit_name = time_submit_name
        self.tenant_uid = tenant_uid
        self.account_uid = account_uid
        self.period_uid = period_uid
        self.time_submit_description = time_submit_description
        self.row_instance = row_instance
        self.row_lock = row_lock
        self.row_owner = row_owner
        self.row_seq = row_seq
        self.row_guid = row_guid
        self.row_version = row_version
        self.is_active = is_active
        self.created_date = created_date
        self.created_by = created_by
        self.last_updated_date = last_updated_date
        self.last_updated_by = last_updated_by
        self.removed_date = removed_date
        self.removed_by = removed_by
        self.custom_attributes = custom_attributes
        self.tenant_uid_tenant_name = tenant_uid_tenant_name
        self.tenant_uid_country_uid = tenant_uid_country_uid
        self.tenant_uid_tenant_type_uid = tenant_uid_tenant_type_uid
        self.tenant_uid_tenant_category_uid = tenant_uid_tenant_category_uid
        self.tenant_uid_tenant_code = tenant_uid_tenant_code
        self.tenant_uid_tenant_description = tenant_uid_tenant_description
        self.tenant_uid_start_date = tenant_uid_start_date
        self.tenant_uid_end_date = tenant_uid_end_date
        self.tenant_uid_is_internal = tenant_uid_is_internal
        self.tenant_uid_is_system = tenant_uid_is_system
        self.tenant_uid_is_test = tenant_uid_is_test
        self.tenant_uid_account_uid = tenant_uid_account_uid
        self.account_uid_account_name = account_uid_account_name
        self.account_uid_tenant_uid = account_uid_tenant_uid
        self.account_uid_account_type_uid = account_uid_account_type_uid
        self.account_uid_account_title_uid = account_uid_account_title_uid
        self.account_uid_account_division_uid = account_uid_account_division_uid
        self.account_uid_account_group_uid = account_uid_account_group_uid
        self.account_uid_auth_identity_uid = account_uid_auth_identity_uid
        self.account_uid_account_email = account_uid_account_email
        self.account_uid_display_name = account_uid_display_name
        self.account_uid_is_system = account_uid_is_system
        self.period_uid_period_name = period_uid_period_name
        self.period_uid_period_number = period_uid_period_number
        self.period_uid_period_type = period_uid_period_type
        self.period_uid_period_start_time = period_uid_period_start_time
        self.period_uid_period_end_time = period_uid_period_end_time
        self.period_uid_period_year = period_uid_period_year
        self.period_uid_period_quarter = period_uid_period_quarter
        self.period_uid_period_month = period_uid_period_month
        self.period_uid_period_week = period_uid_period_week
        self.period_uid_period_day = period_uid_period_day
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.time_submit_uid, self.time_submit_name, self.tenant_uid, self.account_uid, self.period_uid, self.time_submit_description, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes, self.tenant_uid_tenant_name, self.tenant_uid_country_uid, self.tenant_uid_tenant_type_uid, self.tenant_uid_tenant_category_uid, self.tenant_uid_tenant_code, self.tenant_uid_tenant_description, self.tenant_uid_start_date, self.tenant_uid_end_date, self.tenant_uid_is_internal, self.tenant_uid_is_system, self.tenant_uid_is_test, self.tenant_uid_account_uid, self.account_uid_account_name, self.account_uid_tenant_uid, self.account_uid_account_type_uid, self.account_uid_account_title_uid, self.account_uid_account_division_uid, self.account_uid_account_group_uid, self.account_uid_auth_identity_uid, self.account_uid_account_email, self.account_uid_display_name, self.account_uid_is_system, self.period_uid_period_name, self.period_uid_period_number, self.period_uid_period_type, self.period_uid_period_start_time, self.period_uid_period_end_time, self.period_uid_period_year, self.period_uid_period_quarter, self.period_uid_period_month, self.period_uid_period_week, self.period_uid_period_day]


@dataclass(frozen=False)
class time_submit_type_rich_dto(time_submit_type_read_dto):
    time_submit_type_uid: str | None
    time_submit_type_name: str | None
    time_submit_type_description: str | None
    row_instance: str | None
    row_lock: str | None
    row_owner: str | None
    row_seq: int | None
    row_guid: str | None
    row_version: int | None
    is_active: int | None
    created_date: datetime.datetime | None
    created_by: str | None
    last_updated_date: datetime.datetime | None
    last_updated_by: str | None
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str | None
    def __init__(self, time_submit_type_uid: str | None, time_submit_type_name: str | None, time_submit_type_description: str | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None):
        self.time_submit_type_uid = time_submit_type_uid
        self.time_submit_type_name = time_submit_type_name
        self.time_submit_type_description = time_submit_type_description
        self.row_instance = row_instance
        self.row_lock = row_lock
        self.row_owner = row_owner
        self.row_seq = row_seq
        self.row_guid = row_guid
        self.row_version = row_version
        self.is_active = is_active
        self.created_date = created_date
        self.created_by = created_by
        self.last_updated_date = last_updated_date
        self.last_updated_by = last_updated_by
        self.removed_date = removed_date
        self.removed_by = removed_by
        self.custom_attributes = custom_attributes
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.time_submit_type_uid, self.time_submit_type_name, self.time_submit_type_description, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]


# auto-generated - v_definition_python_dtos_rich - END