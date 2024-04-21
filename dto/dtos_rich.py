# auto-generated - v_definition_python_dtos_rich - START at 2024-04-21 14:56:16.094161+02
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
    account_address: str | None
    is_verified: int | None
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
    tenant__tenant_name: str | None
    tenant__country_uid: str | None
    tenant__tenant_type_uid: str | None
    tenant__tenant_category_uid: str | None
    tenant__tenant_code: str | None
    tenant__tenant_description: str | None
    tenant__start_date: datetime.datetime | None
    tenant__end_date: datetime.datetime | None
    tenant__is_internal: int | None
    tenant__is_system: int | None
    tenant__is_test: int | None
    tenant__account_uid: str | None
    account_type__account_type_name: str | None
    account_type__class_name: str | None
    account_type__account_type_description: str | None
    account_title__account_title_name: str | None
    account_title__title_description: str | None
    account_division__account_division_name: str | None
    account_division__tenant_uid: str | None
    account_division__account_uid: str | None
    account_division__account_division_template_uid: str | None
    account_division__division_description: str | None
    account_group__account_group_name: str | None
    account_group__tenant_uid: str | None
    account_group__account_group_description: str | None
    auth_identity__auth_identity_name: str | None
    auth_identity__class_name: str | None
    auth_identity__default_parameters_json: str | None
    def __init__(self, account_uid: str | None, account_name: str | None, tenant_uid: str | None, account_type_uid: str | None, account_title_uid: str | None, account_division_uid: str | None, account_group_uid: str | None, auth_identity_uid: str | None, account_email: str | None, display_name: str | None, account_address: str | None, is_verified: int | None, is_system: int | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None, tenant__tenant_name: str | None, tenant__country_uid: str | None, tenant__tenant_type_uid: str | None, tenant__tenant_category_uid: str | None, tenant__tenant_code: str | None, tenant__tenant_description: str | None, tenant__start_date: datetime.datetime | None, tenant__end_date: datetime.datetime | None, tenant__is_internal: int | None, tenant__is_system: int | None, tenant__is_test: int | None, tenant__account_uid: str | None, account_type__account_type_name: str | None, account_type__class_name: str | None, account_type__account_type_description: str | None, account_title__account_title_name: str | None, account_title__title_description: str | None, account_division__account_division_name: str | None, account_division__tenant_uid: str | None, account_division__account_uid: str | None, account_division__account_division_template_uid: str | None, account_division__division_description: str | None, account_group__account_group_name: str | None, account_group__tenant_uid: str | None, account_group__account_group_description: str | None, auth_identity__auth_identity_name: str | None, auth_identity__class_name: str | None, auth_identity__default_parameters_json: str | None):
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
        self.account_address = account_address
        self.is_verified = is_verified
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
        self.tenant__tenant_name = tenant__tenant_name
        self.tenant__country_uid = tenant__country_uid
        self.tenant__tenant_type_uid = tenant__tenant_type_uid
        self.tenant__tenant_category_uid = tenant__tenant_category_uid
        self.tenant__tenant_code = tenant__tenant_code
        self.tenant__tenant_description = tenant__tenant_description
        self.tenant__start_date = tenant__start_date
        self.tenant__end_date = tenant__end_date
        self.tenant__is_internal = tenant__is_internal
        self.tenant__is_system = tenant__is_system
        self.tenant__is_test = tenant__is_test
        self.tenant__account_uid = tenant__account_uid
        self.account_type__account_type_name = account_type__account_type_name
        self.account_type__class_name = account_type__class_name
        self.account_type__account_type_description = account_type__account_type_description
        self.account_title__account_title_name = account_title__account_title_name
        self.account_title__title_description = account_title__title_description
        self.account_division__account_division_name = account_division__account_division_name
        self.account_division__tenant_uid = account_division__tenant_uid
        self.account_division__account_uid = account_division__account_uid
        self.account_division__account_division_template_uid = account_division__account_division_template_uid
        self.account_division__division_description = account_division__division_description
        self.account_group__account_group_name = account_group__account_group_name
        self.account_group__tenant_uid = account_group__tenant_uid
        self.account_group__account_group_description = account_group__account_group_description
        self.auth_identity__auth_identity_name = auth_identity__auth_identity_name
        self.auth_identity__class_name = auth_identity__class_name
        self.auth_identity__default_parameters_json = auth_identity__default_parameters_json
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.account_uid, self.account_name, self.tenant_uid, self.account_type_uid, self.account_title_uid, self.account_division_uid, self.account_group_uid, self.auth_identity_uid, self.account_email, self.display_name, self.account_address, self.is_verified, self.is_system, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes, self.tenant__tenant_name, self.tenant__country_uid, self.tenant__tenant_type_uid, self.tenant__tenant_category_uid, self.tenant__tenant_code, self.tenant__tenant_description, self.tenant__start_date, self.tenant__end_date, self.tenant__is_internal, self.tenant__is_system, self.tenant__is_test, self.tenant__account_uid, self.account_type__account_type_name, self.account_type__class_name, self.account_type__account_type_description, self.account_title__account_title_name, self.account_title__title_description, self.account_division__account_division_name, self.account_division__tenant_uid, self.account_division__account_uid, self.account_division__account_division_template_uid, self.account_division__division_description, self.account_group__account_group_name, self.account_group__tenant_uid, self.account_group__account_group_description, self.auth_identity__auth_identity_name, self.auth_identity__class_name, self.auth_identity__default_parameters_json]


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
    tenant__tenant_name: str | None
    tenant__country_uid: str | None
    tenant__tenant_type_uid: str | None
    tenant__tenant_category_uid: str | None
    tenant__tenant_code: str | None
    tenant__tenant_description: str | None
    tenant__start_date: datetime.datetime | None
    tenant__end_date: datetime.datetime | None
    tenant__is_internal: int | None
    tenant__is_system: int | None
    tenant__is_test: int | None
    tenant__account_uid: str | None
    account__account_name: str | None
    account__tenant_uid: str | None
    account__account_type_uid: str | None
    account__account_title_uid: str | None
    account__account_division_uid: str | None
    account__account_group_uid: str | None
    account__auth_identity_uid: str | None
    account__account_email: str | None
    account__display_name: str | None
    account__account_address: str | None
    account__is_verified: int | None
    account__is_system: int | None
    account_division_template__account_division_template_name: str | None
    account_division_template__division_description: str | None
    def __init__(self, account_division_uid: str | None, account_division_name: str | None, tenant_uid: str | None, account_uid: str | None, account_division_template_uid: str | None, division_description: str | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None, tenant__tenant_name: str | None, tenant__country_uid: str | None, tenant__tenant_type_uid: str | None, tenant__tenant_category_uid: str | None, tenant__tenant_code: str | None, tenant__tenant_description: str | None, tenant__start_date: datetime.datetime | None, tenant__end_date: datetime.datetime | None, tenant__is_internal: int | None, tenant__is_system: int | None, tenant__is_test: int | None, tenant__account_uid: str | None, account__account_name: str | None, account__tenant_uid: str | None, account__account_type_uid: str | None, account__account_title_uid: str | None, account__account_division_uid: str | None, account__account_group_uid: str | None, account__auth_identity_uid: str | None, account__account_email: str | None, account__display_name: str | None, account__account_address: str | None, account__is_verified: int | None, account__is_system: int | None, account_division_template__account_division_template_name: str | None, account_division_template__division_description: str | None):
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
        self.tenant__tenant_name = tenant__tenant_name
        self.tenant__country_uid = tenant__country_uid
        self.tenant__tenant_type_uid = tenant__tenant_type_uid
        self.tenant__tenant_category_uid = tenant__tenant_category_uid
        self.tenant__tenant_code = tenant__tenant_code
        self.tenant__tenant_description = tenant__tenant_description
        self.tenant__start_date = tenant__start_date
        self.tenant__end_date = tenant__end_date
        self.tenant__is_internal = tenant__is_internal
        self.tenant__is_system = tenant__is_system
        self.tenant__is_test = tenant__is_test
        self.tenant__account_uid = tenant__account_uid
        self.account__account_name = account__account_name
        self.account__tenant_uid = account__tenant_uid
        self.account__account_type_uid = account__account_type_uid
        self.account__account_title_uid = account__account_title_uid
        self.account__account_division_uid = account__account_division_uid
        self.account__account_group_uid = account__account_group_uid
        self.account__auth_identity_uid = account__auth_identity_uid
        self.account__account_email = account__account_email
        self.account__display_name = account__display_name
        self.account__account_address = account__account_address
        self.account__is_verified = account__is_verified
        self.account__is_system = account__is_system
        self.account_division_template__account_division_template_name = account_division_template__account_division_template_name
        self.account_division_template__division_description = account_division_template__division_description
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.account_division_uid, self.account_division_name, self.tenant_uid, self.account_uid, self.account_division_template_uid, self.division_description, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes, self.tenant__tenant_name, self.tenant__country_uid, self.tenant__tenant_type_uid, self.tenant__tenant_category_uid, self.tenant__tenant_code, self.tenant__tenant_description, self.tenant__start_date, self.tenant__end_date, self.tenant__is_internal, self.tenant__is_system, self.tenant__is_test, self.tenant__account_uid, self.account__account_name, self.account__tenant_uid, self.account__account_type_uid, self.account__account_title_uid, self.account__account_division_uid, self.account__account_group_uid, self.account__auth_identity_uid, self.account__account_email, self.account__display_name, self.account__account_address, self.account__is_verified, self.account__is_system, self.account_division_template__account_division_template_name, self.account_division_template__division_description]


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
    tenant__tenant_name: str | None
    tenant__country_uid: str | None
    tenant__tenant_type_uid: str | None
    tenant__tenant_category_uid: str | None
    tenant__tenant_code: str | None
    tenant__tenant_description: str | None
    tenant__start_date: datetime.datetime | None
    tenant__end_date: datetime.datetime | None
    tenant__is_internal: int | None
    tenant__is_system: int | None
    tenant__is_test: int | None
    tenant__account_uid: str | None
    def __init__(self, account_group_uid: str | None, account_group_name: str | None, tenant_uid: str | None, account_group_description: str | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None, tenant__tenant_name: str | None, tenant__country_uid: str | None, tenant__tenant_type_uid: str | None, tenant__tenant_category_uid: str | None, tenant__tenant_code: str | None, tenant__tenant_description: str | None, tenant__start_date: datetime.datetime | None, tenant__end_date: datetime.datetime | None, tenant__is_internal: int | None, tenant__is_system: int | None, tenant__is_test: int | None, tenant__account_uid: str | None):
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
        self.tenant__tenant_name = tenant__tenant_name
        self.tenant__country_uid = tenant__country_uid
        self.tenant__tenant_type_uid = tenant__tenant_type_uid
        self.tenant__tenant_category_uid = tenant__tenant_category_uid
        self.tenant__tenant_code = tenant__tenant_code
        self.tenant__tenant_description = tenant__tenant_description
        self.tenant__start_date = tenant__start_date
        self.tenant__end_date = tenant__end_date
        self.tenant__is_internal = tenant__is_internal
        self.tenant__is_system = tenant__is_system
        self.tenant__is_test = tenant__is_test
        self.tenant__account_uid = tenant__account_uid
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.account_group_uid, self.account_group_name, self.tenant_uid, self.account_group_description, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes, self.tenant__tenant_name, self.tenant__country_uid, self.tenant__tenant_type_uid, self.tenant__tenant_category_uid, self.tenant__tenant_code, self.tenant__tenant_description, self.tenant__start_date, self.tenant__end_date, self.tenant__is_internal, self.tenant__is_system, self.tenant__is_test, self.tenant__account_uid]


@dataclass(frozen=False)
class account_group_assignment_rich_dto(account_group_assignment_read_dto):
    account_group_assignment_uid: str | None
    account_group_assignment_name: str | None
    tenant_uid: str | None
    account_group_uid: str | None
    account_uid: str | None
    account_group_role_uid: str | None
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
    tenant__tenant_name: str | None
    tenant__country_uid: str | None
    tenant__tenant_type_uid: str | None
    tenant__tenant_category_uid: str | None
    tenant__tenant_code: str | None
    tenant__tenant_description: str | None
    tenant__start_date: datetime.datetime | None
    tenant__end_date: datetime.datetime | None
    tenant__is_internal: int | None
    tenant__is_system: int | None
    tenant__is_test: int | None
    tenant__account_uid: str | None
    account_group__account_group_name: str | None
    account_group__tenant_uid: str | None
    account_group__account_group_description: str | None
    account__account_name: str | None
    account__tenant_uid: str | None
    account__account_type_uid: str | None
    account__account_title_uid: str | None
    account__account_division_uid: str | None
    account__account_group_uid: str | None
    account__auth_identity_uid: str | None
    account__account_email: str | None
    account__display_name: str | None
    account__account_address: str | None
    account__is_verified: int | None
    account__is_system: int | None
    account_group_role__account_group_role_name: str | None
    def __init__(self, account_group_assignment_uid: str | None, account_group_assignment_name: str | None, tenant_uid: str | None, account_group_uid: str | None, account_uid: str | None, account_group_role_uid: str | None, start_date: datetime.datetime | None, end_date: datetime.datetime | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None, tenant__tenant_name: str | None, tenant__country_uid: str | None, tenant__tenant_type_uid: str | None, tenant__tenant_category_uid: str | None, tenant__tenant_code: str | None, tenant__tenant_description: str | None, tenant__start_date: datetime.datetime | None, tenant__end_date: datetime.datetime | None, tenant__is_internal: int | None, tenant__is_system: int | None, tenant__is_test: int | None, tenant__account_uid: str | None, account_group__account_group_name: str | None, account_group__tenant_uid: str | None, account_group__account_group_description: str | None, account__account_name: str | None, account__tenant_uid: str | None, account__account_type_uid: str | None, account__account_title_uid: str | None, account__account_division_uid: str | None, account__account_group_uid: str | None, account__auth_identity_uid: str | None, account__account_email: str | None, account__display_name: str | None, account__account_address: str | None, account__is_verified: int | None, account__is_system: int | None, account_group_role__account_group_role_name: str | None):
        self.account_group_assignment_uid = account_group_assignment_uid
        self.account_group_assignment_name = account_group_assignment_name
        self.tenant_uid = tenant_uid
        self.account_group_uid = account_group_uid
        self.account_uid = account_uid
        self.account_group_role_uid = account_group_role_uid
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
        self.tenant__tenant_name = tenant__tenant_name
        self.tenant__country_uid = tenant__country_uid
        self.tenant__tenant_type_uid = tenant__tenant_type_uid
        self.tenant__tenant_category_uid = tenant__tenant_category_uid
        self.tenant__tenant_code = tenant__tenant_code
        self.tenant__tenant_description = tenant__tenant_description
        self.tenant__start_date = tenant__start_date
        self.tenant__end_date = tenant__end_date
        self.tenant__is_internal = tenant__is_internal
        self.tenant__is_system = tenant__is_system
        self.tenant__is_test = tenant__is_test
        self.tenant__account_uid = tenant__account_uid
        self.account_group__account_group_name = account_group__account_group_name
        self.account_group__tenant_uid = account_group__tenant_uid
        self.account_group__account_group_description = account_group__account_group_description
        self.account__account_name = account__account_name
        self.account__tenant_uid = account__tenant_uid
        self.account__account_type_uid = account__account_type_uid
        self.account__account_title_uid = account__account_title_uid
        self.account__account_division_uid = account__account_division_uid
        self.account__account_group_uid = account__account_group_uid
        self.account__auth_identity_uid = account__auth_identity_uid
        self.account__account_email = account__account_email
        self.account__display_name = account__display_name
        self.account__account_address = account__account_address
        self.account__is_verified = account__is_verified
        self.account__is_system = account__is_system
        self.account_group_role__account_group_role_name = account_group_role__account_group_role_name
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.account_group_assignment_uid, self.account_group_assignment_name, self.tenant_uid, self.account_group_uid, self.account_uid, self.account_group_role_uid, self.start_date, self.end_date, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes, self.tenant__tenant_name, self.tenant__country_uid, self.tenant__tenant_type_uid, self.tenant__tenant_category_uid, self.tenant__tenant_code, self.tenant__tenant_description, self.tenant__start_date, self.tenant__end_date, self.tenant__is_internal, self.tenant__is_system, self.tenant__is_test, self.tenant__account_uid, self.account_group__account_group_name, self.account_group__tenant_uid, self.account_group__account_group_description, self.account__account_name, self.account__tenant_uid, self.account__account_type_uid, self.account__account_title_uid, self.account__account_division_uid, self.account__account_group_uid, self.account__auth_identity_uid, self.account__account_email, self.account__display_name, self.account__account_address, self.account__is_verified, self.account__is_system, self.account_group_role__account_group_role_name]


@dataclass(frozen=False)
class account_group_role_rich_dto(account_group_role_read_dto):
    account_group_role_uid: str | None
    account_group_role_name: str | None
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
    def __init__(self, account_group_role_uid: str | None, account_group_role_name: str | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None):
        self.account_group_role_uid = account_group_role_uid
        self.account_group_role_name = account_group_role_name
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
        return [self.account_group_role_uid, self.account_group_role_name, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]


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
    tenant__tenant_name: str | None
    tenant__country_uid: str | None
    tenant__tenant_type_uid: str | None
    tenant__tenant_category_uid: str | None
    tenant__tenant_code: str | None
    tenant__tenant_description: str | None
    tenant__start_date: datetime.datetime | None
    tenant__end_date: datetime.datetime | None
    tenant__is_internal: int | None
    tenant__is_system: int | None
    tenant__is_test: int | None
    tenant__account_uid: str | None
    parent_account__account_name: str | None
    parent_account__tenant_uid: str | None
    parent_account__account_type_uid: str | None
    parent_account__account_title_uid: str | None
    parent_account__account_division_uid: str | None
    parent_account__account_group_uid: str | None
    parent_account__auth_identity_uid: str | None
    parent_account__account_email: str | None
    parent_account__display_name: str | None
    parent_account__account_address: str | None
    parent_account__is_verified: int | None
    parent_account__is_system: int | None
    child_account__account_name: str | None
    child_account__tenant_uid: str | None
    child_account__account_type_uid: str | None
    child_account__account_title_uid: str | None
    child_account__account_division_uid: str | None
    child_account__account_group_uid: str | None
    child_account__auth_identity_uid: str | None
    child_account__account_email: str | None
    child_account__display_name: str | None
    child_account__account_address: str | None
    child_account__is_verified: int | None
    child_account__is_system: int | None
    def __init__(self, account_hierarchy_uid: str | None, account_hierarchy_name: str | None, tenant_uid: str | None, parent_account_uid: str | None, child_account_uid: str | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None, tenant__tenant_name: str | None, tenant__country_uid: str | None, tenant__tenant_type_uid: str | None, tenant__tenant_category_uid: str | None, tenant__tenant_code: str | None, tenant__tenant_description: str | None, tenant__start_date: datetime.datetime | None, tenant__end_date: datetime.datetime | None, tenant__is_internal: int | None, tenant__is_system: int | None, tenant__is_test: int | None, tenant__account_uid: str | None, parent_account__account_name: str | None, parent_account__tenant_uid: str | None, parent_account__account_type_uid: str | None, parent_account__account_title_uid: str | None, parent_account__account_division_uid: str | None, parent_account__account_group_uid: str | None, parent_account__auth_identity_uid: str | None, parent_account__account_email: str | None, parent_account__display_name: str | None, parent_account__account_address: str | None, parent_account__is_verified: int | None, parent_account__is_system: int | None, child_account__account_name: str | None, child_account__tenant_uid: str | None, child_account__account_type_uid: str | None, child_account__account_title_uid: str | None, child_account__account_division_uid: str | None, child_account__account_group_uid: str | None, child_account__auth_identity_uid: str | None, child_account__account_email: str | None, child_account__display_name: str | None, child_account__account_address: str | None, child_account__is_verified: int | None, child_account__is_system: int | None):
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
        self.tenant__tenant_name = tenant__tenant_name
        self.tenant__country_uid = tenant__country_uid
        self.tenant__tenant_type_uid = tenant__tenant_type_uid
        self.tenant__tenant_category_uid = tenant__tenant_category_uid
        self.tenant__tenant_code = tenant__tenant_code
        self.tenant__tenant_description = tenant__tenant_description
        self.tenant__start_date = tenant__start_date
        self.tenant__end_date = tenant__end_date
        self.tenant__is_internal = tenant__is_internal
        self.tenant__is_system = tenant__is_system
        self.tenant__is_test = tenant__is_test
        self.tenant__account_uid = tenant__account_uid
        self.parent_account__account_name = parent_account__account_name
        self.parent_account__tenant_uid = parent_account__tenant_uid
        self.parent_account__account_type_uid = parent_account__account_type_uid
        self.parent_account__account_title_uid = parent_account__account_title_uid
        self.parent_account__account_division_uid = parent_account__account_division_uid
        self.parent_account__account_group_uid = parent_account__account_group_uid
        self.parent_account__auth_identity_uid = parent_account__auth_identity_uid
        self.parent_account__account_email = parent_account__account_email
        self.parent_account__display_name = parent_account__display_name
        self.parent_account__account_address = parent_account__account_address
        self.parent_account__is_verified = parent_account__is_verified
        self.parent_account__is_system = parent_account__is_system
        self.child_account__account_name = child_account__account_name
        self.child_account__tenant_uid = child_account__tenant_uid
        self.child_account__account_type_uid = child_account__account_type_uid
        self.child_account__account_title_uid = child_account__account_title_uid
        self.child_account__account_division_uid = child_account__account_division_uid
        self.child_account__account_group_uid = child_account__account_group_uid
        self.child_account__auth_identity_uid = child_account__auth_identity_uid
        self.child_account__account_email = child_account__account_email
        self.child_account__display_name = child_account__display_name
        self.child_account__account_address = child_account__account_address
        self.child_account__is_verified = child_account__is_verified
        self.child_account__is_system = child_account__is_system
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.account_hierarchy_uid, self.account_hierarchy_name, self.tenant_uid, self.parent_account_uid, self.child_account_uid, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes, self.tenant__tenant_name, self.tenant__country_uid, self.tenant__tenant_type_uid, self.tenant__tenant_category_uid, self.tenant__tenant_code, self.tenant__tenant_description, self.tenant__start_date, self.tenant__end_date, self.tenant__is_internal, self.tenant__is_system, self.tenant__is_test, self.tenant__account_uid, self.parent_account__account_name, self.parent_account__tenant_uid, self.parent_account__account_type_uid, self.parent_account__account_title_uid, self.parent_account__account_division_uid, self.parent_account__account_group_uid, self.parent_account__auth_identity_uid, self.parent_account__account_email, self.parent_account__display_name, self.parent_account__account_address, self.parent_account__is_verified, self.parent_account__is_system, self.child_account__account_name, self.child_account__tenant_uid, self.child_account__account_type_uid, self.child_account__account_title_uid, self.child_account__account_division_uid, self.child_account__account_group_uid, self.child_account__auth_identity_uid, self.child_account__account_email, self.child_account__display_name, self.child_account__account_address, self.child_account__is_verified, self.child_account__is_system]


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
    tenant__tenant_name: str | None
    tenant__country_uid: str | None
    tenant__tenant_type_uid: str | None
    tenant__tenant_category_uid: str | None
    tenant__tenant_code: str | None
    tenant__tenant_description: str | None
    tenant__start_date: datetime.datetime | None
    tenant__end_date: datetime.datetime | None
    tenant__is_internal: int | None
    tenant__is_system: int | None
    tenant__is_test: int | None
    tenant__account_uid: str | None
    account__account_name: str | None
    account__tenant_uid: str | None
    account__account_type_uid: str | None
    account__account_title_uid: str | None
    account__account_division_uid: str | None
    account__account_group_uid: str | None
    account__auth_identity_uid: str | None
    account__account_email: str | None
    account__display_name: str | None
    account__account_address: str | None
    account__is_verified: int | None
    account__is_system: int | None
    currency__currency_name: str | None
    currency__is_focused: int | None
    currency__priority: int | None
    def __init__(self, account_rate_uid: str | None, account_rate_name: str | None, tenant_uid: str | None, account_uid: str | None, currency_uid: str | None, rate: str | None, start_date: datetime.datetime | None, end_date: datetime.datetime | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None, tenant__tenant_name: str | None, tenant__country_uid: str | None, tenant__tenant_type_uid: str | None, tenant__tenant_category_uid: str | None, tenant__tenant_code: str | None, tenant__tenant_description: str | None, tenant__start_date: datetime.datetime | None, tenant__end_date: datetime.datetime | None, tenant__is_internal: int | None, tenant__is_system: int | None, tenant__is_test: int | None, tenant__account_uid: str | None, account__account_name: str | None, account__tenant_uid: str | None, account__account_type_uid: str | None, account__account_title_uid: str | None, account__account_division_uid: str | None, account__account_group_uid: str | None, account__auth_identity_uid: str | None, account__account_email: str | None, account__display_name: str | None, account__account_address: str | None, account__is_verified: int | None, account__is_system: int | None, currency__currency_name: str | None, currency__is_focused: int | None, currency__priority: int | None):
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
        self.tenant__tenant_name = tenant__tenant_name
        self.tenant__country_uid = tenant__country_uid
        self.tenant__tenant_type_uid = tenant__tenant_type_uid
        self.tenant__tenant_category_uid = tenant__tenant_category_uid
        self.tenant__tenant_code = tenant__tenant_code
        self.tenant__tenant_description = tenant__tenant_description
        self.tenant__start_date = tenant__start_date
        self.tenant__end_date = tenant__end_date
        self.tenant__is_internal = tenant__is_internal
        self.tenant__is_system = tenant__is_system
        self.tenant__is_test = tenant__is_test
        self.tenant__account_uid = tenant__account_uid
        self.account__account_name = account__account_name
        self.account__tenant_uid = account__tenant_uid
        self.account__account_type_uid = account__account_type_uid
        self.account__account_title_uid = account__account_title_uid
        self.account__account_division_uid = account__account_division_uid
        self.account__account_group_uid = account__account_group_uid
        self.account__auth_identity_uid = account__auth_identity_uid
        self.account__account_email = account__account_email
        self.account__display_name = account__display_name
        self.account__account_address = account__account_address
        self.account__is_verified = account__is_verified
        self.account__is_system = account__is_system
        self.currency__currency_name = currency__currency_name
        self.currency__is_focused = currency__is_focused
        self.currency__priority = currency__priority
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.account_rate_uid, self.account_rate_name, self.tenant_uid, self.account_uid, self.currency_uid, self.rate, self.start_date, self.end_date, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes, self.tenant__tenant_name, self.tenant__country_uid, self.tenant__tenant_type_uid, self.tenant__tenant_category_uid, self.tenant__tenant_code, self.tenant__tenant_description, self.tenant__start_date, self.tenant__end_date, self.tenant__is_internal, self.tenant__is_system, self.tenant__is_test, self.tenant__account_uid, self.account__account_name, self.account__tenant_uid, self.account__account_type_uid, self.account__account_title_uid, self.account__account_division_uid, self.account__account_group_uid, self.account__auth_identity_uid, self.account__account_email, self.account__display_name, self.account__account_address, self.account__is_verified, self.account__is_system, self.currency__currency_name, self.currency__is_focused, self.currency__priority]


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
    tenant__tenant_name: str | None
    tenant__country_uid: str | None
    tenant__tenant_type_uid: str | None
    tenant__tenant_category_uid: str | None
    tenant__tenant_code: str | None
    tenant__tenant_description: str | None
    tenant__start_date: datetime.datetime | None
    tenant__end_date: datetime.datetime | None
    tenant__is_internal: int | None
    tenant__is_system: int | None
    tenant__is_test: int | None
    tenant__account_uid: str | None
    owner_account__account_name: str | None
    owner_account__tenant_uid: str | None
    owner_account__account_type_uid: str | None
    owner_account__account_title_uid: str | None
    owner_account__account_division_uid: str | None
    owner_account__account_group_uid: str | None
    owner_account__auth_identity_uid: str | None
    owner_account__account_email: str | None
    owner_account__display_name: str | None
    owner_account__account_address: str | None
    owner_account__is_verified: int | None
    owner_account__is_system: int | None
    def __init__(self, account_team_uid: str | None, account_team_name: str | None, tenant_uid: str | None, owner_account_uid: str | None, is_public: int | None, is_tenant: int | None, is_private: int | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None, tenant__tenant_name: str | None, tenant__country_uid: str | None, tenant__tenant_type_uid: str | None, tenant__tenant_category_uid: str | None, tenant__tenant_code: str | None, tenant__tenant_description: str | None, tenant__start_date: datetime.datetime | None, tenant__end_date: datetime.datetime | None, tenant__is_internal: int | None, tenant__is_system: int | None, tenant__is_test: int | None, tenant__account_uid: str | None, owner_account__account_name: str | None, owner_account__tenant_uid: str | None, owner_account__account_type_uid: str | None, owner_account__account_title_uid: str | None, owner_account__account_division_uid: str | None, owner_account__account_group_uid: str | None, owner_account__auth_identity_uid: str | None, owner_account__account_email: str | None, owner_account__display_name: str | None, owner_account__account_address: str | None, owner_account__is_verified: int | None, owner_account__is_system: int | None):
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
        self.tenant__tenant_name = tenant__tenant_name
        self.tenant__country_uid = tenant__country_uid
        self.tenant__tenant_type_uid = tenant__tenant_type_uid
        self.tenant__tenant_category_uid = tenant__tenant_category_uid
        self.tenant__tenant_code = tenant__tenant_code
        self.tenant__tenant_description = tenant__tenant_description
        self.tenant__start_date = tenant__start_date
        self.tenant__end_date = tenant__end_date
        self.tenant__is_internal = tenant__is_internal
        self.tenant__is_system = tenant__is_system
        self.tenant__is_test = tenant__is_test
        self.tenant__account_uid = tenant__account_uid
        self.owner_account__account_name = owner_account__account_name
        self.owner_account__tenant_uid = owner_account__tenant_uid
        self.owner_account__account_type_uid = owner_account__account_type_uid
        self.owner_account__account_title_uid = owner_account__account_title_uid
        self.owner_account__account_division_uid = owner_account__account_division_uid
        self.owner_account__account_group_uid = owner_account__account_group_uid
        self.owner_account__auth_identity_uid = owner_account__auth_identity_uid
        self.owner_account__account_email = owner_account__account_email
        self.owner_account__display_name = owner_account__display_name
        self.owner_account__account_address = owner_account__account_address
        self.owner_account__is_verified = owner_account__is_verified
        self.owner_account__is_system = owner_account__is_system
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.account_team_uid, self.account_team_name, self.tenant_uid, self.owner_account_uid, self.is_public, self.is_tenant, self.is_private, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes, self.tenant__tenant_name, self.tenant__country_uid, self.tenant__tenant_type_uid, self.tenant__tenant_category_uid, self.tenant__tenant_code, self.tenant__tenant_description, self.tenant__start_date, self.tenant__end_date, self.tenant__is_internal, self.tenant__is_system, self.tenant__is_test, self.tenant__account_uid, self.owner_account__account_name, self.owner_account__tenant_uid, self.owner_account__account_type_uid, self.owner_account__account_title_uid, self.owner_account__account_division_uid, self.owner_account__account_group_uid, self.owner_account__auth_identity_uid, self.owner_account__account_email, self.owner_account__display_name, self.owner_account__account_address, self.owner_account__is_verified, self.owner_account__is_system]


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
class account_title_assignment_rich_dto(account_title_assignment_read_dto):
    account_title_assignment_uid: str | None
    account_title_assignment_name: str | None
    tenant_uid: str | None
    account_title_uid: str | None
    account_title_responsibility_uid: str | None
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
    tenant__tenant_name: str | None
    tenant__country_uid: str | None
    tenant__tenant_type_uid: str | None
    tenant__tenant_category_uid: str | None
    tenant__tenant_code: str | None
    tenant__tenant_description: str | None
    tenant__start_date: datetime.datetime | None
    tenant__end_date: datetime.datetime | None
    tenant__is_internal: int | None
    tenant__is_system: int | None
    tenant__is_test: int | None
    tenant__account_uid: str | None
    account_title__account_title_name: str | None
    account_title__title_description: str | None
    account_title_responsibility__account_title_responsibility_name: str | None
    account_title_responsibility__tenant_uid: str | None
    account_title_responsibility__account_title_uid: str | None
    account_title_responsibility__responsibility_group: str | None
    account_title_responsibility__responsibility_description: str | None
    account_title_responsibility__responsibility_priority: int | None
    def __init__(self, account_title_assignment_uid: str | None, account_title_assignment_name: str | None, tenant_uid: str | None, account_title_uid: str | None, account_title_responsibility_uid: str | None, responsibility_description: str | None, responsibility_priority: int | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None, tenant__tenant_name: str | None, tenant__country_uid: str | None, tenant__tenant_type_uid: str | None, tenant__tenant_category_uid: str | None, tenant__tenant_code: str | None, tenant__tenant_description: str | None, tenant__start_date: datetime.datetime | None, tenant__end_date: datetime.datetime | None, tenant__is_internal: int | None, tenant__is_system: int | None, tenant__is_test: int | None, tenant__account_uid: str | None, account_title__account_title_name: str | None, account_title__title_description: str | None, account_title_responsibility__account_title_responsibility_name: str | None, account_title_responsibility__tenant_uid: str | None, account_title_responsibility__account_title_uid: str | None, account_title_responsibility__responsibility_group: str | None, account_title_responsibility__responsibility_description: str | None, account_title_responsibility__responsibility_priority: int | None):
        self.account_title_assignment_uid = account_title_assignment_uid
        self.account_title_assignment_name = account_title_assignment_name
        self.tenant_uid = tenant_uid
        self.account_title_uid = account_title_uid
        self.account_title_responsibility_uid = account_title_responsibility_uid
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
        self.tenant__tenant_name = tenant__tenant_name
        self.tenant__country_uid = tenant__country_uid
        self.tenant__tenant_type_uid = tenant__tenant_type_uid
        self.tenant__tenant_category_uid = tenant__tenant_category_uid
        self.tenant__tenant_code = tenant__tenant_code
        self.tenant__tenant_description = tenant__tenant_description
        self.tenant__start_date = tenant__start_date
        self.tenant__end_date = tenant__end_date
        self.tenant__is_internal = tenant__is_internal
        self.tenant__is_system = tenant__is_system
        self.tenant__is_test = tenant__is_test
        self.tenant__account_uid = tenant__account_uid
        self.account_title__account_title_name = account_title__account_title_name
        self.account_title__title_description = account_title__title_description
        self.account_title_responsibility__account_title_responsibility_name = account_title_responsibility__account_title_responsibility_name
        self.account_title_responsibility__tenant_uid = account_title_responsibility__tenant_uid
        self.account_title_responsibility__account_title_uid = account_title_responsibility__account_title_uid
        self.account_title_responsibility__responsibility_group = account_title_responsibility__responsibility_group
        self.account_title_responsibility__responsibility_description = account_title_responsibility__responsibility_description
        self.account_title_responsibility__responsibility_priority = account_title_responsibility__responsibility_priority
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.account_title_assignment_uid, self.account_title_assignment_name, self.tenant_uid, self.account_title_uid, self.account_title_responsibility_uid, self.responsibility_description, self.responsibility_priority, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes, self.tenant__tenant_name, self.tenant__country_uid, self.tenant__tenant_type_uid, self.tenant__tenant_category_uid, self.tenant__tenant_code, self.tenant__tenant_description, self.tenant__start_date, self.tenant__end_date, self.tenant__is_internal, self.tenant__is_system, self.tenant__is_test, self.tenant__account_uid, self.account_title__account_title_name, self.account_title__title_description, self.account_title_responsibility__account_title_responsibility_name, self.account_title_responsibility__tenant_uid, self.account_title_responsibility__account_title_uid, self.account_title_responsibility__responsibility_group, self.account_title_responsibility__responsibility_description, self.account_title_responsibility__responsibility_priority]


@dataclass(frozen=False)
class account_title_responsibility_rich_dto(account_title_responsibility_read_dto):
    account_title_responsibility_uid: str | None
    account_title_responsibility_name: str | None
    tenant_uid: str | None
    account_title_uid: str | None
    responsibility_group: str | None
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
    tenant__tenant_name: str | None
    tenant__country_uid: str | None
    tenant__tenant_type_uid: str | None
    tenant__tenant_category_uid: str | None
    tenant__tenant_code: str | None
    tenant__tenant_description: str | None
    tenant__start_date: datetime.datetime | None
    tenant__end_date: datetime.datetime | None
    tenant__is_internal: int | None
    tenant__is_system: int | None
    tenant__is_test: int | None
    tenant__account_uid: str | None
    account_title__account_title_name: str | None
    account_title__title_description: str | None
    def __init__(self, account_title_responsibility_uid: str | None, account_title_responsibility_name: str | None, tenant_uid: str | None, account_title_uid: str | None, responsibility_group: str | None, responsibility_description: str | None, responsibility_priority: int | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None, tenant__tenant_name: str | None, tenant__country_uid: str | None, tenant__tenant_type_uid: str | None, tenant__tenant_category_uid: str | None, tenant__tenant_code: str | None, tenant__tenant_description: str | None, tenant__start_date: datetime.datetime | None, tenant__end_date: datetime.datetime | None, tenant__is_internal: int | None, tenant__is_system: int | None, tenant__is_test: int | None, tenant__account_uid: str | None, account_title__account_title_name: str | None, account_title__title_description: str | None):
        self.account_title_responsibility_uid = account_title_responsibility_uid
        self.account_title_responsibility_name = account_title_responsibility_name
        self.tenant_uid = tenant_uid
        self.account_title_uid = account_title_uid
        self.responsibility_group = responsibility_group
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
        self.tenant__tenant_name = tenant__tenant_name
        self.tenant__country_uid = tenant__country_uid
        self.tenant__tenant_type_uid = tenant__tenant_type_uid
        self.tenant__tenant_category_uid = tenant__tenant_category_uid
        self.tenant__tenant_code = tenant__tenant_code
        self.tenant__tenant_description = tenant__tenant_description
        self.tenant__start_date = tenant__start_date
        self.tenant__end_date = tenant__end_date
        self.tenant__is_internal = tenant__is_internal
        self.tenant__is_system = tenant__is_system
        self.tenant__is_test = tenant__is_test
        self.tenant__account_uid = tenant__account_uid
        self.account_title__account_title_name = account_title__account_title_name
        self.account_title__title_description = account_title__title_description
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.account_title_responsibility_uid, self.account_title_responsibility_name, self.tenant_uid, self.account_title_uid, self.responsibility_group, self.responsibility_description, self.responsibility_priority, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes, self.tenant__tenant_name, self.tenant__country_uid, self.tenant__tenant_type_uid, self.tenant__tenant_category_uid, self.tenant__tenant_code, self.tenant__tenant_description, self.tenant__start_date, self.tenant__end_date, self.tenant__is_internal, self.tenant__is_system, self.tenant__is_test, self.tenant__account_uid, self.account_title__account_title_name, self.account_title__title_description]


@dataclass(frozen=False)
class account_type_rich_dto(account_type_read_dto):
    account_type_uid: str | None
    account_type_name: str | None
    class_name: str | None
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
    def __init__(self, account_type_uid: str | None, account_type_name: str | None, class_name: str | None, account_type_description: str | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None):
        self.account_type_uid = account_type_uid
        self.account_type_name = account_type_name
        self.class_name = class_name
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
        return [self.account_type_uid, self.account_type_name, self.class_name, self.account_type_description, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]


@dataclass(frozen=False)
class audit_change_rich_dto(audit_change_read_dto):
    audit_change_uid: str | None
    audit_change_name: str | None
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
    account__account_name: str | None
    account__tenant_uid: str | None
    account__account_type_uid: str | None
    account__account_title_uid: str | None
    account__account_division_uid: str | None
    account__account_group_uid: str | None
    account__auth_identity_uid: str | None
    account__account_email: str | None
    account__display_name: str | None
    account__account_address: str | None
    account__is_verified: int | None
    account__is_system: int | None
    audit_type__audit_type_name: str | None
    def __init__(self, audit_change_uid: str | None, audit_change_name: str | None, account_uid: str | None, audit_type_uid: str | None, change_type: str | None, change_json: str | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None, account__account_name: str | None, account__tenant_uid: str | None, account__account_type_uid: str | None, account__account_title_uid: str | None, account__account_division_uid: str | None, account__account_group_uid: str | None, account__auth_identity_uid: str | None, account__account_email: str | None, account__display_name: str | None, account__account_address: str | None, account__is_verified: int | None, account__is_system: int | None, audit_type__audit_type_name: str | None):
        self.audit_change_uid = audit_change_uid
        self.audit_change_name = audit_change_name
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
        self.account__account_name = account__account_name
        self.account__tenant_uid = account__tenant_uid
        self.account__account_type_uid = account__account_type_uid
        self.account__account_title_uid = account__account_title_uid
        self.account__account_division_uid = account__account_division_uid
        self.account__account_group_uid = account__account_group_uid
        self.account__auth_identity_uid = account__auth_identity_uid
        self.account__account_email = account__account_email
        self.account__display_name = account__display_name
        self.account__account_address = account__account_address
        self.account__is_verified = account__is_verified
        self.account__is_system = account__is_system
        self.audit_type__audit_type_name = audit_type__audit_type_name
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.audit_change_uid, self.audit_change_name, self.account_uid, self.audit_type_uid, self.change_type, self.change_json, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes, self.account__account_name, self.account__tenant_uid, self.account__account_type_uid, self.account__account_title_uid, self.account__account_division_uid, self.account__account_group_uid, self.account__auth_identity_uid, self.account__account_email, self.account__display_name, self.account__account_address, self.account__is_verified, self.account__is_system, self.audit_type__audit_type_name]


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
    tenant__tenant_name: str | None
    tenant__country_uid: str | None
    tenant__tenant_type_uid: str | None
    tenant__tenant_category_uid: str | None
    tenant__tenant_code: str | None
    tenant__tenant_description: str | None
    tenant__start_date: datetime.datetime | None
    tenant__end_date: datetime.datetime | None
    tenant__is_internal: int | None
    tenant__is_system: int | None
    tenant__is_test: int | None
    tenant__account_uid: str | None
    account__account_name: str | None
    account__tenant_uid: str | None
    account__account_type_uid: str | None
    account__account_title_uid: str | None
    account__account_division_uid: str | None
    account__account_group_uid: str | None
    account__auth_identity_uid: str | None
    account__account_email: str | None
    account__display_name: str | None
    account__account_address: str | None
    account__is_verified: int | None
    account__is_system: int | None
    def __init__(self, auth_attempt_uid: str | None, auth_attempt_name: str | None, tenant_uid: str | None, account_uid: str | None, account_login: str | None, identity_type: str | None, identity_parameters: str | None, last_status_name: str | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None, tenant__tenant_name: str | None, tenant__country_uid: str | None, tenant__tenant_type_uid: str | None, tenant__tenant_category_uid: str | None, tenant__tenant_code: str | None, tenant__tenant_description: str | None, tenant__start_date: datetime.datetime | None, tenant__end_date: datetime.datetime | None, tenant__is_internal: int | None, tenant__is_system: int | None, tenant__is_test: int | None, tenant__account_uid: str | None, account__account_name: str | None, account__tenant_uid: str | None, account__account_type_uid: str | None, account__account_title_uid: str | None, account__account_division_uid: str | None, account__account_group_uid: str | None, account__auth_identity_uid: str | None, account__account_email: str | None, account__display_name: str | None, account__account_address: str | None, account__is_verified: int | None, account__is_system: int | None):
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
        self.tenant__tenant_name = tenant__tenant_name
        self.tenant__country_uid = tenant__country_uid
        self.tenant__tenant_type_uid = tenant__tenant_type_uid
        self.tenant__tenant_category_uid = tenant__tenant_category_uid
        self.tenant__tenant_code = tenant__tenant_code
        self.tenant__tenant_description = tenant__tenant_description
        self.tenant__start_date = tenant__start_date
        self.tenant__end_date = tenant__end_date
        self.tenant__is_internal = tenant__is_internal
        self.tenant__is_system = tenant__is_system
        self.tenant__is_test = tenant__is_test
        self.tenant__account_uid = tenant__account_uid
        self.account__account_name = account__account_name
        self.account__tenant_uid = account__tenant_uid
        self.account__account_type_uid = account__account_type_uid
        self.account__account_title_uid = account__account_title_uid
        self.account__account_division_uid = account__account_division_uid
        self.account__account_group_uid = account__account_group_uid
        self.account__auth_identity_uid = account__auth_identity_uid
        self.account__account_email = account__account_email
        self.account__display_name = account__display_name
        self.account__account_address = account__account_address
        self.account__is_verified = account__is_verified
        self.account__is_system = account__is_system
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.auth_attempt_uid, self.auth_attempt_name, self.tenant_uid, self.account_uid, self.account_login, self.identity_type, self.identity_parameters, self.last_status_name, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes, self.tenant__tenant_name, self.tenant__country_uid, self.tenant__tenant_type_uid, self.tenant__tenant_category_uid, self.tenant__tenant_code, self.tenant__tenant_description, self.tenant__start_date, self.tenant__end_date, self.tenant__is_internal, self.tenant__is_system, self.tenant__is_test, self.tenant__account_uid, self.account__account_name, self.account__tenant_uid, self.account__account_type_uid, self.account__account_title_uid, self.account__account_division_uid, self.account__account_group_uid, self.account__auth_identity_uid, self.account__account_email, self.account__display_name, self.account__account_address, self.account__is_verified, self.account__is_system]


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
    auth_identity_tenant__tenant_name: str | None
    auth_identity_tenant__country_uid: str | None
    auth_identity_tenant__tenant_type_uid: str | None
    auth_identity_tenant__tenant_category_uid: str | None
    auth_identity_tenant__tenant_code: str | None
    auth_identity_tenant__tenant_description: str | None
    auth_identity_tenant__start_date: datetime.datetime | None
    auth_identity_tenant__end_date: datetime.datetime | None
    auth_identity_tenant__is_internal: int | None
    auth_identity_tenant__is_system: int | None
    auth_identity_tenant__is_test: int | None
    auth_identity_tenant__account_uid: str | None
    tenant__tenant_name: str | None
    tenant__country_uid: str | None
    tenant__tenant_type_uid: str | None
    tenant__tenant_category_uid: str | None
    tenant__tenant_code: str | None
    tenant__tenant_description: str | None
    tenant__start_date: datetime.datetime | None
    tenant__end_date: datetime.datetime | None
    tenant__is_internal: int | None
    tenant__is_system: int | None
    tenant__is_test: int | None
    tenant__account_uid: str | None
    auth_identity__auth_identity_name: str | None
    auth_identity__class_name: str | None
    auth_identity__default_parameters_json: str | None
    auth_sso__auth_sso_name: str | None
    auth_sso__tenant_uid: str | None
    auth_sso__owner_account_uid: str | None
    auth_sso__sso_name: str | None
    auth_sso__sso_url: str | None
    auth_sso__sso_key: str | None
    auth_sso__sso_secret: str | None
    auth_sso__sso_code: str | None
    auth_sso__clientid: str | None
    auth_sso__clientsecret: str | None
    auth_sso__callback_url: str | None
    def __init__(self, auth_identity_tenant_uid: str | None, auth_identity_tenant_name: str | None, tenant_uid: str | None, auth_identity_uid: str | None, auth_sso_uid: str | None, identity_parameters_json: str | None, last_status_name: str | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None, auth_identity_tenant__tenant_name: str | None, auth_identity_tenant__country_uid: str | None, auth_identity_tenant__tenant_type_uid: str | None, auth_identity_tenant__tenant_category_uid: str | None, auth_identity_tenant__tenant_code: str | None, auth_identity_tenant__tenant_description: str | None, auth_identity_tenant__start_date: datetime.datetime | None, auth_identity_tenant__end_date: datetime.datetime | None, auth_identity_tenant__is_internal: int | None, auth_identity_tenant__is_system: int | None, auth_identity_tenant__is_test: int | None, auth_identity_tenant__account_uid: str | None, tenant__tenant_name: str | None, tenant__country_uid: str | None, tenant__tenant_type_uid: str | None, tenant__tenant_category_uid: str | None, tenant__tenant_code: str | None, tenant__tenant_description: str | None, tenant__start_date: datetime.datetime | None, tenant__end_date: datetime.datetime | None, tenant__is_internal: int | None, tenant__is_system: int | None, tenant__is_test: int | None, tenant__account_uid: str | None, auth_identity__auth_identity_name: str | None, auth_identity__class_name: str | None, auth_identity__default_parameters_json: str | None, auth_sso__auth_sso_name: str | None, auth_sso__tenant_uid: str | None, auth_sso__owner_account_uid: str | None, auth_sso__sso_name: str | None, auth_sso__sso_url: str | None, auth_sso__sso_key: str | None, auth_sso__sso_secret: str | None, auth_sso__sso_code: str | None, auth_sso__clientid: str | None, auth_sso__clientsecret: str | None, auth_sso__callback_url: str | None):
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
        self.auth_identity_tenant__tenant_name = auth_identity_tenant__tenant_name
        self.auth_identity_tenant__country_uid = auth_identity_tenant__country_uid
        self.auth_identity_tenant__tenant_type_uid = auth_identity_tenant__tenant_type_uid
        self.auth_identity_tenant__tenant_category_uid = auth_identity_tenant__tenant_category_uid
        self.auth_identity_tenant__tenant_code = auth_identity_tenant__tenant_code
        self.auth_identity_tenant__tenant_description = auth_identity_tenant__tenant_description
        self.auth_identity_tenant__start_date = auth_identity_tenant__start_date
        self.auth_identity_tenant__end_date = auth_identity_tenant__end_date
        self.auth_identity_tenant__is_internal = auth_identity_tenant__is_internal
        self.auth_identity_tenant__is_system = auth_identity_tenant__is_system
        self.auth_identity_tenant__is_test = auth_identity_tenant__is_test
        self.auth_identity_tenant__account_uid = auth_identity_tenant__account_uid
        self.tenant__tenant_name = tenant__tenant_name
        self.tenant__country_uid = tenant__country_uid
        self.tenant__tenant_type_uid = tenant__tenant_type_uid
        self.tenant__tenant_category_uid = tenant__tenant_category_uid
        self.tenant__tenant_code = tenant__tenant_code
        self.tenant__tenant_description = tenant__tenant_description
        self.tenant__start_date = tenant__start_date
        self.tenant__end_date = tenant__end_date
        self.tenant__is_internal = tenant__is_internal
        self.tenant__is_system = tenant__is_system
        self.tenant__is_test = tenant__is_test
        self.tenant__account_uid = tenant__account_uid
        self.auth_identity__auth_identity_name = auth_identity__auth_identity_name
        self.auth_identity__class_name = auth_identity__class_name
        self.auth_identity__default_parameters_json = auth_identity__default_parameters_json
        self.auth_sso__auth_sso_name = auth_sso__auth_sso_name
        self.auth_sso__tenant_uid = auth_sso__tenant_uid
        self.auth_sso__owner_account_uid = auth_sso__owner_account_uid
        self.auth_sso__sso_name = auth_sso__sso_name
        self.auth_sso__sso_url = auth_sso__sso_url
        self.auth_sso__sso_key = auth_sso__sso_key
        self.auth_sso__sso_secret = auth_sso__sso_secret
        self.auth_sso__sso_code = auth_sso__sso_code
        self.auth_sso__clientid = auth_sso__clientid
        self.auth_sso__clientsecret = auth_sso__clientsecret
        self.auth_sso__callback_url = auth_sso__callback_url
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.auth_identity_tenant_uid, self.auth_identity_tenant_name, self.tenant_uid, self.auth_identity_uid, self.auth_sso_uid, self.identity_parameters_json, self.last_status_name, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes, self.auth_identity_tenant__tenant_name, self.auth_identity_tenant__country_uid, self.auth_identity_tenant__tenant_type_uid, self.auth_identity_tenant__tenant_category_uid, self.auth_identity_tenant__tenant_code, self.auth_identity_tenant__tenant_description, self.auth_identity_tenant__start_date, self.auth_identity_tenant__end_date, self.auth_identity_tenant__is_internal, self.auth_identity_tenant__is_system, self.auth_identity_tenant__is_test, self.auth_identity_tenant__account_uid, self.tenant__tenant_name, self.tenant__country_uid, self.tenant__tenant_type_uid, self.tenant__tenant_category_uid, self.tenant__tenant_code, self.tenant__tenant_description, self.tenant__start_date, self.tenant__end_date, self.tenant__is_internal, self.tenant__is_system, self.tenant__is_test, self.tenant__account_uid, self.auth_identity__auth_identity_name, self.auth_identity__class_name, self.auth_identity__default_parameters_json, self.auth_sso__auth_sso_name, self.auth_sso__tenant_uid, self.auth_sso__owner_account_uid, self.auth_sso__sso_name, self.auth_sso__sso_url, self.auth_sso__sso_key, self.auth_sso__sso_secret, self.auth_sso__sso_code, self.auth_sso__clientid, self.auth_sso__clientsecret, self.auth_sso__callback_url]


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
    tenant__tenant_name: str | None
    tenant__country_uid: str | None
    tenant__tenant_type_uid: str | None
    tenant__tenant_category_uid: str | None
    tenant__tenant_code: str | None
    tenant__tenant_description: str | None
    tenant__start_date: datetime.datetime | None
    tenant__end_date: datetime.datetime | None
    tenant__is_internal: int | None
    tenant__is_system: int | None
    tenant__is_test: int | None
    tenant__account_uid: str | None
    owner_account__account_name: str | None
    owner_account__tenant_uid: str | None
    owner_account__account_type_uid: str | None
    owner_account__account_title_uid: str | None
    owner_account__account_division_uid: str | None
    owner_account__account_group_uid: str | None
    owner_account__auth_identity_uid: str | None
    owner_account__account_email: str | None
    owner_account__display_name: str | None
    owner_account__account_address: str | None
    owner_account__is_verified: int | None
    owner_account__is_system: int | None
    auth_key_type__auth_key_type_name: str | None
    auth_key_type__class_name: str | None
    def __init__(self, auth_key_uid: str | None, auth_key_name: str | None, tenant_uid: str | None, owner_account_uid: str | None, auth_key_type_uid: str | None, key_private: str | None, key_public: str | None, key_length: int | None, key_exponent: str | None, key_modulus: str | None, key_parameters_json: str | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None, tenant__tenant_name: str | None, tenant__country_uid: str | None, tenant__tenant_type_uid: str | None, tenant__tenant_category_uid: str | None, tenant__tenant_code: str | None, tenant__tenant_description: str | None, tenant__start_date: datetime.datetime | None, tenant__end_date: datetime.datetime | None, tenant__is_internal: int | None, tenant__is_system: int | None, tenant__is_test: int | None, tenant__account_uid: str | None, owner_account__account_name: str | None, owner_account__tenant_uid: str | None, owner_account__account_type_uid: str | None, owner_account__account_title_uid: str | None, owner_account__account_division_uid: str | None, owner_account__account_group_uid: str | None, owner_account__auth_identity_uid: str | None, owner_account__account_email: str | None, owner_account__display_name: str | None, owner_account__account_address: str | None, owner_account__is_verified: int | None, owner_account__is_system: int | None, auth_key_type__auth_key_type_name: str | None, auth_key_type__class_name: str | None):
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
        self.tenant__tenant_name = tenant__tenant_name
        self.tenant__country_uid = tenant__country_uid
        self.tenant__tenant_type_uid = tenant__tenant_type_uid
        self.tenant__tenant_category_uid = tenant__tenant_category_uid
        self.tenant__tenant_code = tenant__tenant_code
        self.tenant__tenant_description = tenant__tenant_description
        self.tenant__start_date = tenant__start_date
        self.tenant__end_date = tenant__end_date
        self.tenant__is_internal = tenant__is_internal
        self.tenant__is_system = tenant__is_system
        self.tenant__is_test = tenant__is_test
        self.tenant__account_uid = tenant__account_uid
        self.owner_account__account_name = owner_account__account_name
        self.owner_account__tenant_uid = owner_account__tenant_uid
        self.owner_account__account_type_uid = owner_account__account_type_uid
        self.owner_account__account_title_uid = owner_account__account_title_uid
        self.owner_account__account_division_uid = owner_account__account_division_uid
        self.owner_account__account_group_uid = owner_account__account_group_uid
        self.owner_account__auth_identity_uid = owner_account__auth_identity_uid
        self.owner_account__account_email = owner_account__account_email
        self.owner_account__display_name = owner_account__display_name
        self.owner_account__account_address = owner_account__account_address
        self.owner_account__is_verified = owner_account__is_verified
        self.owner_account__is_system = owner_account__is_system
        self.auth_key_type__auth_key_type_name = auth_key_type__auth_key_type_name
        self.auth_key_type__class_name = auth_key_type__class_name
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.auth_key_uid, self.auth_key_name, self.tenant_uid, self.owner_account_uid, self.auth_key_type_uid, self.key_private, self.key_public, self.key_length, self.key_exponent, self.key_modulus, self.key_parameters_json, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes, self.tenant__tenant_name, self.tenant__country_uid, self.tenant__tenant_type_uid, self.tenant__tenant_category_uid, self.tenant__tenant_code, self.tenant__tenant_description, self.tenant__start_date, self.tenant__end_date, self.tenant__is_internal, self.tenant__is_system, self.tenant__is_test, self.tenant__account_uid, self.owner_account__account_name, self.owner_account__tenant_uid, self.owner_account__account_type_uid, self.owner_account__account_title_uid, self.owner_account__account_division_uid, self.owner_account__account_group_uid, self.owner_account__auth_identity_uid, self.owner_account__account_email, self.owner_account__display_name, self.owner_account__account_address, self.owner_account__is_verified, self.owner_account__is_system, self.auth_key_type__auth_key_type_name, self.auth_key_type__class_name]


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
    tenant__tenant_name: str | None
    tenant__country_uid: str | None
    tenant__tenant_type_uid: str | None
    tenant__tenant_category_uid: str | None
    tenant__tenant_code: str | None
    tenant__tenant_description: str | None
    tenant__start_date: datetime.datetime | None
    tenant__end_date: datetime.datetime | None
    tenant__is_internal: int | None
    tenant__is_system: int | None
    tenant__is_test: int | None
    tenant__account_uid: str | None
    account__account_name: str | None
    account__tenant_uid: str | None
    account__account_type_uid: str | None
    account__account_title_uid: str | None
    account__account_division_uid: str | None
    account__account_group_uid: str | None
    account__auth_identity_uid: str | None
    account__account_email: str | None
    account__display_name: str | None
    account__account_address: str | None
    account__is_verified: int | None
    account__is_system: int | None
    def __init__(self, auth_password_uid: str | None, auth_password_name: str | None, tenant_uid: str | None, account_uid: str | None, password_hash: str | None, password_salt: str | None, date_from: datetime.datetime | None, date_to: datetime.datetime | None, usage_count: int | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None, tenant__tenant_name: str | None, tenant__country_uid: str | None, tenant__tenant_type_uid: str | None, tenant__tenant_category_uid: str | None, tenant__tenant_code: str | None, tenant__tenant_description: str | None, tenant__start_date: datetime.datetime | None, tenant__end_date: datetime.datetime | None, tenant__is_internal: int | None, tenant__is_system: int | None, tenant__is_test: int | None, tenant__account_uid: str | None, account__account_name: str | None, account__tenant_uid: str | None, account__account_type_uid: str | None, account__account_title_uid: str | None, account__account_division_uid: str | None, account__account_group_uid: str | None, account__auth_identity_uid: str | None, account__account_email: str | None, account__display_name: str | None, account__account_address: str | None, account__is_verified: int | None, account__is_system: int | None):
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
        self.tenant__tenant_name = tenant__tenant_name
        self.tenant__country_uid = tenant__country_uid
        self.tenant__tenant_type_uid = tenant__tenant_type_uid
        self.tenant__tenant_category_uid = tenant__tenant_category_uid
        self.tenant__tenant_code = tenant__tenant_code
        self.tenant__tenant_description = tenant__tenant_description
        self.tenant__start_date = tenant__start_date
        self.tenant__end_date = tenant__end_date
        self.tenant__is_internal = tenant__is_internal
        self.tenant__is_system = tenant__is_system
        self.tenant__is_test = tenant__is_test
        self.tenant__account_uid = tenant__account_uid
        self.account__account_name = account__account_name
        self.account__tenant_uid = account__tenant_uid
        self.account__account_type_uid = account__account_type_uid
        self.account__account_title_uid = account__account_title_uid
        self.account__account_division_uid = account__account_division_uid
        self.account__account_group_uid = account__account_group_uid
        self.account__auth_identity_uid = account__auth_identity_uid
        self.account__account_email = account__account_email
        self.account__display_name = account__display_name
        self.account__account_address = account__account_address
        self.account__is_verified = account__is_verified
        self.account__is_system = account__is_system
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.auth_password_uid, self.auth_password_name, self.tenant_uid, self.account_uid, self.password_hash, self.password_salt, self.date_from, self.date_to, self.usage_count, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes, self.tenant__tenant_name, self.tenant__country_uid, self.tenant__tenant_type_uid, self.tenant__tenant_category_uid, self.tenant__tenant_code, self.tenant__tenant_description, self.tenant__start_date, self.tenant__end_date, self.tenant__is_internal, self.tenant__is_system, self.tenant__is_test, self.tenant__account_uid, self.account__account_name, self.account__tenant_uid, self.account__account_type_uid, self.account__account_title_uid, self.account__account_division_uid, self.account__account_group_uid, self.account__auth_identity_uid, self.account__account_email, self.account__display_name, self.account__account_address, self.account__is_verified, self.account__is_system]


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
    tenant__tenant_name: str | None
    tenant__country_uid: str | None
    tenant__tenant_type_uid: str | None
    tenant__tenant_category_uid: str | None
    tenant__tenant_code: str | None
    tenant__tenant_description: str | None
    tenant__start_date: datetime.datetime | None
    tenant__end_date: datetime.datetime | None
    tenant__is_internal: int | None
    tenant__is_system: int | None
    tenant__is_test: int | None
    tenant__account_uid: str | None
    account__account_name: str | None
    account__tenant_uid: str | None
    account__account_type_uid: str | None
    account__account_title_uid: str | None
    account__account_division_uid: str | None
    account__account_group_uid: str | None
    account__auth_identity_uid: str | None
    account__account_email: str | None
    account__display_name: str | None
    account__account_address: str | None
    account__is_verified: int | None
    account__is_system: int | None
    def __init__(self, auth_password_current_uid: str | None, auth_password_current_name: str | None, tenant_uid: str | None, account_uid: str | None, password_hash: str | None, password_salt: str | None, date_from: datetime.datetime | None, date_to: datetime.datetime | None, usage_count: int | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None, tenant__tenant_name: str | None, tenant__country_uid: str | None, tenant__tenant_type_uid: str | None, tenant__tenant_category_uid: str | None, tenant__tenant_code: str | None, tenant__tenant_description: str | None, tenant__start_date: datetime.datetime | None, tenant__end_date: datetime.datetime | None, tenant__is_internal: int | None, tenant__is_system: int | None, tenant__is_test: int | None, tenant__account_uid: str | None, account__account_name: str | None, account__tenant_uid: str | None, account__account_type_uid: str | None, account__account_title_uid: str | None, account__account_division_uid: str | None, account__account_group_uid: str | None, account__auth_identity_uid: str | None, account__account_email: str | None, account__display_name: str | None, account__account_address: str | None, account__is_verified: int | None, account__is_system: int | None):
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
        self.tenant__tenant_name = tenant__tenant_name
        self.tenant__country_uid = tenant__country_uid
        self.tenant__tenant_type_uid = tenant__tenant_type_uid
        self.tenant__tenant_category_uid = tenant__tenant_category_uid
        self.tenant__tenant_code = tenant__tenant_code
        self.tenant__tenant_description = tenant__tenant_description
        self.tenant__start_date = tenant__start_date
        self.tenant__end_date = tenant__end_date
        self.tenant__is_internal = tenant__is_internal
        self.tenant__is_system = tenant__is_system
        self.tenant__is_test = tenant__is_test
        self.tenant__account_uid = tenant__account_uid
        self.account__account_name = account__account_name
        self.account__tenant_uid = account__tenant_uid
        self.account__account_type_uid = account__account_type_uid
        self.account__account_title_uid = account__account_title_uid
        self.account__account_division_uid = account__account_division_uid
        self.account__account_group_uid = account__account_group_uid
        self.account__auth_identity_uid = account__auth_identity_uid
        self.account__account_email = account__account_email
        self.account__display_name = account__display_name
        self.account__account_address = account__account_address
        self.account__is_verified = account__is_verified
        self.account__is_system = account__is_system
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.auth_password_current_uid, self.auth_password_current_name, self.tenant_uid, self.account_uid, self.password_hash, self.password_salt, self.date_from, self.date_to, self.usage_count, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes, self.tenant__tenant_name, self.tenant__country_uid, self.tenant__tenant_type_uid, self.tenant__tenant_category_uid, self.tenant__tenant_code, self.tenant__tenant_description, self.tenant__start_date, self.tenant__end_date, self.tenant__is_internal, self.tenant__is_system, self.tenant__is_test, self.tenant__account_uid, self.account__account_name, self.account__tenant_uid, self.account__account_type_uid, self.account__account_title_uid, self.account__account_division_uid, self.account__account_group_uid, self.account__auth_identity_uid, self.account__account_email, self.account__display_name, self.account__account_address, self.account__is_verified, self.account__is_system]


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
    auth_password__auth_password_name: str | None
    auth_password__tenant_uid: str | None
    auth_password__account_uid: str | None
    auth_password__password_hash: str | None
    auth_password__password_salt: str | None
    auth_password__date_from: datetime.datetime | None
    auth_password__date_to: datetime.datetime | None
    auth_password__usage_count: int | None
    def __init__(self, auth_password_uid: str | None, auth_password_name: str | None, rule_type: int | None, rule_parameters: str | None, user_scope: str | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None, auth_password__auth_password_name: str | None, auth_password__tenant_uid: str | None, auth_password__account_uid: str | None, auth_password__password_hash: str | None, auth_password__password_salt: str | None, auth_password__date_from: datetime.datetime | None, auth_password__date_to: datetime.datetime | None, auth_password__usage_count: int | None):
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
        self.auth_password__auth_password_name = auth_password__auth_password_name
        self.auth_password__tenant_uid = auth_password__tenant_uid
        self.auth_password__account_uid = auth_password__account_uid
        self.auth_password__password_hash = auth_password__password_hash
        self.auth_password__password_salt = auth_password__password_salt
        self.auth_password__date_from = auth_password__date_from
        self.auth_password__date_to = auth_password__date_to
        self.auth_password__usage_count = auth_password__usage_count
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.auth_password_uid, self.auth_password_name, self.rule_type, self.rule_parameters, self.user_scope, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes, self.auth_password__auth_password_name, self.auth_password__tenant_uid, self.auth_password__account_uid, self.auth_password__password_hash, self.auth_password__password_salt, self.auth_password__date_from, self.auth_password__date_to, self.auth_password__usage_count]


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
    tenant__tenant_name: str | None
    tenant__country_uid: str | None
    tenant__tenant_type_uid: str | None
    tenant__tenant_category_uid: str | None
    tenant__tenant_code: str | None
    tenant__tenant_description: str | None
    tenant__start_date: datetime.datetime | None
    tenant__end_date: datetime.datetime | None
    tenant__is_internal: int | None
    tenant__is_system: int | None
    tenant__is_test: int | None
    tenant__account_uid: str | None
    account__account_name: str | None
    account__tenant_uid: str | None
    account__account_type_uid: str | None
    account__account_title_uid: str | None
    account__account_division_uid: str | None
    account__account_group_uid: str | None
    account__auth_identity_uid: str | None
    account__account_email: str | None
    account__display_name: str | None
    account__account_address: str | None
    account__is_verified: int | None
    account__is_system: int | None
    auth_role__auth_role_name: str | None
    auth_role__parent_auth_role_uid: str | None
    auth_role__tenant_uid: str | None
    auth_role__role_description: str | None
    auth_role__access_uris: str | None
    auth_role__is_project: int | None
    auth_role__is_tenant: int | None
    auth_role__is_client: int | None
    auth_role__is_custom: int | None
    client__client_name: str | None
    client__tenant_uid: str | None
    client__country_uid: str | None
    client__client_type_uid: str | None
    client__client_category_uid: str | None
    client__account_uid: str | None
    client__client_code: str | None
    client__client_description: str | None
    client__start_date: datetime.datetime | None
    client__end_date: datetime.datetime | None
    client__is_internal: int | None
    client__is_system: int | None
    client__is_test: int | None
    project_instance__project_instance_name: str | None
    project_instance__tenant_uid: str | None
    project_instance__client_uid: str | None
    project_instance__project_type_uid: str | None
    project_instance__manager_account_uid: str | None
    project_instance__project_group_uid: str | None
    project_instance__project_code: str | None
    project_instance__project_description: str | None
    project_instance__is_billable: int | None
    project_instance__start_date: datetime.datetime | None
    project_instance__end_date: datetime.datetime | None
    project_instance__current_billed: str | None
    project_instance__budget: str | None
    def __init__(self, auth_permission_uid: str | None, auth_permission_name: str | None, tenant_uid: str | None, account_uid: str | None, auth_role_uid: str | None, client_uid: str | None, project_instance_uid: str | None, valid_from_date: datetime.datetime | None, valid_till_date: datetime.datetime | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None, tenant__tenant_name: str | None, tenant__country_uid: str | None, tenant__tenant_type_uid: str | None, tenant__tenant_category_uid: str | None, tenant__tenant_code: str | None, tenant__tenant_description: str | None, tenant__start_date: datetime.datetime | None, tenant__end_date: datetime.datetime | None, tenant__is_internal: int | None, tenant__is_system: int | None, tenant__is_test: int | None, tenant__account_uid: str | None, account__account_name: str | None, account__tenant_uid: str | None, account__account_type_uid: str | None, account__account_title_uid: str | None, account__account_division_uid: str | None, account__account_group_uid: str | None, account__auth_identity_uid: str | None, account__account_email: str | None, account__display_name: str | None, account__account_address: str | None, account__is_verified: int | None, account__is_system: int | None, auth_role__auth_role_name: str | None, auth_role__parent_auth_role_uid: str | None, auth_role__tenant_uid: str | None, auth_role__role_description: str | None, auth_role__access_uris: str | None, auth_role__is_project: int | None, auth_role__is_tenant: int | None, auth_role__is_client: int | None, auth_role__is_custom: int | None, client__client_name: str | None, client__tenant_uid: str | None, client__country_uid: str | None, client__client_type_uid: str | None, client__client_category_uid: str | None, client__account_uid: str | None, client__client_code: str | None, client__client_description: str | None, client__start_date: datetime.datetime | None, client__end_date: datetime.datetime | None, client__is_internal: int | None, client__is_system: int | None, client__is_test: int | None, project_instance__project_instance_name: str | None, project_instance__tenant_uid: str | None, project_instance__client_uid: str | None, project_instance__project_type_uid: str | None, project_instance__manager_account_uid: str | None, project_instance__project_group_uid: str | None, project_instance__project_code: str | None, project_instance__project_description: str | None, project_instance__is_billable: int | None, project_instance__start_date: datetime.datetime | None, project_instance__end_date: datetime.datetime | None, project_instance__current_billed: str | None, project_instance__budget: str | None):
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
        self.tenant__tenant_name = tenant__tenant_name
        self.tenant__country_uid = tenant__country_uid
        self.tenant__tenant_type_uid = tenant__tenant_type_uid
        self.tenant__tenant_category_uid = tenant__tenant_category_uid
        self.tenant__tenant_code = tenant__tenant_code
        self.tenant__tenant_description = tenant__tenant_description
        self.tenant__start_date = tenant__start_date
        self.tenant__end_date = tenant__end_date
        self.tenant__is_internal = tenant__is_internal
        self.tenant__is_system = tenant__is_system
        self.tenant__is_test = tenant__is_test
        self.tenant__account_uid = tenant__account_uid
        self.account__account_name = account__account_name
        self.account__tenant_uid = account__tenant_uid
        self.account__account_type_uid = account__account_type_uid
        self.account__account_title_uid = account__account_title_uid
        self.account__account_division_uid = account__account_division_uid
        self.account__account_group_uid = account__account_group_uid
        self.account__auth_identity_uid = account__auth_identity_uid
        self.account__account_email = account__account_email
        self.account__display_name = account__display_name
        self.account__account_address = account__account_address
        self.account__is_verified = account__is_verified
        self.account__is_system = account__is_system
        self.auth_role__auth_role_name = auth_role__auth_role_name
        self.auth_role__parent_auth_role_uid = auth_role__parent_auth_role_uid
        self.auth_role__tenant_uid = auth_role__tenant_uid
        self.auth_role__role_description = auth_role__role_description
        self.auth_role__access_uris = auth_role__access_uris
        self.auth_role__is_project = auth_role__is_project
        self.auth_role__is_tenant = auth_role__is_tenant
        self.auth_role__is_client = auth_role__is_client
        self.auth_role__is_custom = auth_role__is_custom
        self.client__client_name = client__client_name
        self.client__tenant_uid = client__tenant_uid
        self.client__country_uid = client__country_uid
        self.client__client_type_uid = client__client_type_uid
        self.client__client_category_uid = client__client_category_uid
        self.client__account_uid = client__account_uid
        self.client__client_code = client__client_code
        self.client__client_description = client__client_description
        self.client__start_date = client__start_date
        self.client__end_date = client__end_date
        self.client__is_internal = client__is_internal
        self.client__is_system = client__is_system
        self.client__is_test = client__is_test
        self.project_instance__project_instance_name = project_instance__project_instance_name
        self.project_instance__tenant_uid = project_instance__tenant_uid
        self.project_instance__client_uid = project_instance__client_uid
        self.project_instance__project_type_uid = project_instance__project_type_uid
        self.project_instance__manager_account_uid = project_instance__manager_account_uid
        self.project_instance__project_group_uid = project_instance__project_group_uid
        self.project_instance__project_code = project_instance__project_code
        self.project_instance__project_description = project_instance__project_description
        self.project_instance__is_billable = project_instance__is_billable
        self.project_instance__start_date = project_instance__start_date
        self.project_instance__end_date = project_instance__end_date
        self.project_instance__current_billed = project_instance__current_billed
        self.project_instance__budget = project_instance__budget
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.auth_permission_uid, self.auth_permission_name, self.tenant_uid, self.account_uid, self.auth_role_uid, self.client_uid, self.project_instance_uid, self.valid_from_date, self.valid_till_date, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes, self.tenant__tenant_name, self.tenant__country_uid, self.tenant__tenant_type_uid, self.tenant__tenant_category_uid, self.tenant__tenant_code, self.tenant__tenant_description, self.tenant__start_date, self.tenant__end_date, self.tenant__is_internal, self.tenant__is_system, self.tenant__is_test, self.tenant__account_uid, self.account__account_name, self.account__tenant_uid, self.account__account_type_uid, self.account__account_title_uid, self.account__account_division_uid, self.account__account_group_uid, self.account__auth_identity_uid, self.account__account_email, self.account__display_name, self.account__account_address, self.account__is_verified, self.account__is_system, self.auth_role__auth_role_name, self.auth_role__parent_auth_role_uid, self.auth_role__tenant_uid, self.auth_role__role_description, self.auth_role__access_uris, self.auth_role__is_project, self.auth_role__is_tenant, self.auth_role__is_client, self.auth_role__is_custom, self.client__client_name, self.client__tenant_uid, self.client__country_uid, self.client__client_type_uid, self.client__client_category_uid, self.client__account_uid, self.client__client_code, self.client__client_description, self.client__start_date, self.client__end_date, self.client__is_internal, self.client__is_system, self.client__is_test, self.project_instance__project_instance_name, self.project_instance__tenant_uid, self.project_instance__client_uid, self.project_instance__project_type_uid, self.project_instance__manager_account_uid, self.project_instance__project_group_uid, self.project_instance__project_code, self.project_instance__project_description, self.project_instance__is_billable, self.project_instance__start_date, self.project_instance__end_date, self.project_instance__current_billed, self.project_instance__budget]


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
    tenant__tenant_name: str | None
    tenant__country_uid: str | None
    tenant__tenant_type_uid: str | None
    tenant__tenant_category_uid: str | None
    tenant__tenant_code: str | None
    tenant__tenant_description: str | None
    tenant__start_date: datetime.datetime | None
    tenant__end_date: datetime.datetime | None
    tenant__is_internal: int | None
    tenant__is_system: int | None
    tenant__is_test: int | None
    tenant__account_uid: str | None
    account__account_name: str | None
    account__tenant_uid: str | None
    account__account_type_uid: str | None
    account__account_title_uid: str | None
    account__account_division_uid: str | None
    account__account_group_uid: str | None
    account__auth_identity_uid: str | None
    account__account_email: str | None
    account__display_name: str | None
    account__account_address: str | None
    account__is_verified: int | None
    account__is_system: int | None
    event_notification__event_notification_name: str | None
    event_notification__tenant_uid: str | None
    event_notification__account_uid: str | None
    event_notification__notification_type: str | None
    event_notification__notification_topic: str | None
    event_notification__notification_format: str | None
    event_notification__notification_content: str | None
    event_notification__sending_status: str | None
    def __init__(self, auth_request_uid: str | None, auth_request_name: str | None, tenant_uid: str | None, account_uid: str | None, requestor_email: str | None, reset_guid: str | None, valid_till_date: datetime.datetime | None, lock_guid: str | None, lock_by: str | None, lock_date: datetime.datetime | None, is_checked: int | None, is_used: int | None, check_date: datetime.datetime | None, use_date: datetime.datetime | None, event_notification_uid: str | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None, tenant__tenant_name: str | None, tenant__country_uid: str | None, tenant__tenant_type_uid: str | None, tenant__tenant_category_uid: str | None, tenant__tenant_code: str | None, tenant__tenant_description: str | None, tenant__start_date: datetime.datetime | None, tenant__end_date: datetime.datetime | None, tenant__is_internal: int | None, tenant__is_system: int | None, tenant__is_test: int | None, tenant__account_uid: str | None, account__account_name: str | None, account__tenant_uid: str | None, account__account_type_uid: str | None, account__account_title_uid: str | None, account__account_division_uid: str | None, account__account_group_uid: str | None, account__auth_identity_uid: str | None, account__account_email: str | None, account__display_name: str | None, account__account_address: str | None, account__is_verified: int | None, account__is_system: int | None, event_notification__event_notification_name: str | None, event_notification__tenant_uid: str | None, event_notification__account_uid: str | None, event_notification__notification_type: str | None, event_notification__notification_topic: str | None, event_notification__notification_format: str | None, event_notification__notification_content: str | None, event_notification__sending_status: str | None):
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
        self.tenant__tenant_name = tenant__tenant_name
        self.tenant__country_uid = tenant__country_uid
        self.tenant__tenant_type_uid = tenant__tenant_type_uid
        self.tenant__tenant_category_uid = tenant__tenant_category_uid
        self.tenant__tenant_code = tenant__tenant_code
        self.tenant__tenant_description = tenant__tenant_description
        self.tenant__start_date = tenant__start_date
        self.tenant__end_date = tenant__end_date
        self.tenant__is_internal = tenant__is_internal
        self.tenant__is_system = tenant__is_system
        self.tenant__is_test = tenant__is_test
        self.tenant__account_uid = tenant__account_uid
        self.account__account_name = account__account_name
        self.account__tenant_uid = account__tenant_uid
        self.account__account_type_uid = account__account_type_uid
        self.account__account_title_uid = account__account_title_uid
        self.account__account_division_uid = account__account_division_uid
        self.account__account_group_uid = account__account_group_uid
        self.account__auth_identity_uid = account__auth_identity_uid
        self.account__account_email = account__account_email
        self.account__display_name = account__display_name
        self.account__account_address = account__account_address
        self.account__is_verified = account__is_verified
        self.account__is_system = account__is_system
        self.event_notification__event_notification_name = event_notification__event_notification_name
        self.event_notification__tenant_uid = event_notification__tenant_uid
        self.event_notification__account_uid = event_notification__account_uid
        self.event_notification__notification_type = event_notification__notification_type
        self.event_notification__notification_topic = event_notification__notification_topic
        self.event_notification__notification_format = event_notification__notification_format
        self.event_notification__notification_content = event_notification__notification_content
        self.event_notification__sending_status = event_notification__sending_status
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.auth_request_uid, self.auth_request_name, self.tenant_uid, self.account_uid, self.requestor_email, self.reset_guid, self.valid_till_date, self.lock_guid, self.lock_by, self.lock_date, self.is_checked, self.is_used, self.check_date, self.use_date, self.event_notification_uid, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes, self.tenant__tenant_name, self.tenant__country_uid, self.tenant__tenant_type_uid, self.tenant__tenant_category_uid, self.tenant__tenant_code, self.tenant__tenant_description, self.tenant__start_date, self.tenant__end_date, self.tenant__is_internal, self.tenant__is_system, self.tenant__is_test, self.tenant__account_uid, self.account__account_name, self.account__tenant_uid, self.account__account_type_uid, self.account__account_title_uid, self.account__account_division_uid, self.account__account_group_uid, self.account__auth_identity_uid, self.account__account_email, self.account__display_name, self.account__account_address, self.account__is_verified, self.account__is_system, self.event_notification__event_notification_name, self.event_notification__tenant_uid, self.event_notification__account_uid, self.event_notification__notification_type, self.event_notification__notification_topic, self.event_notification__notification_format, self.event_notification__notification_content, self.event_notification__sending_status]


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
    tenant__tenant_name: str | None
    tenant__country_uid: str | None
    tenant__tenant_type_uid: str | None
    tenant__tenant_category_uid: str | None
    tenant__tenant_code: str | None
    tenant__tenant_description: str | None
    tenant__start_date: datetime.datetime | None
    tenant__end_date: datetime.datetime | None
    tenant__is_internal: int | None
    tenant__is_system: int | None
    tenant__is_test: int | None
    tenant__account_uid: str | None
    def __init__(self, auth_role_uid: str | None, auth_role_name: str | None, parent_auth_role_uid: str | None, tenant_uid: str | None, role_description: str | None, access_uris: str | None, is_project: int | None, is_tenant: int | None, is_client: int | None, is_custom: int | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None, tenant__tenant_name: str | None, tenant__country_uid: str | None, tenant__tenant_type_uid: str | None, tenant__tenant_category_uid: str | None, tenant__tenant_code: str | None, tenant__tenant_description: str | None, tenant__start_date: datetime.datetime | None, tenant__end_date: datetime.datetime | None, tenant__is_internal: int | None, tenant__is_system: int | None, tenant__is_test: int | None, tenant__account_uid: str | None):
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
        self.tenant__tenant_name = tenant__tenant_name
        self.tenant__country_uid = tenant__country_uid
        self.tenant__tenant_type_uid = tenant__tenant_type_uid
        self.tenant__tenant_category_uid = tenant__tenant_category_uid
        self.tenant__tenant_code = tenant__tenant_code
        self.tenant__tenant_description = tenant__tenant_description
        self.tenant__start_date = tenant__start_date
        self.tenant__end_date = tenant__end_date
        self.tenant__is_internal = tenant__is_internal
        self.tenant__is_system = tenant__is_system
        self.tenant__is_test = tenant__is_test
        self.tenant__account_uid = tenant__account_uid
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.auth_role_uid, self.auth_role_name, self.parent_auth_role_uid, self.tenant_uid, self.role_description, self.access_uris, self.is_project, self.is_tenant, self.is_client, self.is_custom, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes, self.tenant__tenant_name, self.tenant__country_uid, self.tenant__tenant_type_uid, self.tenant__tenant_category_uid, self.tenant__tenant_code, self.tenant__tenant_description, self.tenant__start_date, self.tenant__end_date, self.tenant__is_internal, self.tenant__is_system, self.tenant__is_test, self.tenant__account_uid]


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
    auth_role__auth_role_name: str | None
    auth_role__parent_auth_role_uid: str | None
    auth_role__tenant_uid: str | None
    auth_role__role_description: str | None
    auth_role__access_uris: str | None
    auth_role__is_project: int | None
    auth_role__is_tenant: int | None
    auth_role__is_client: int | None
    auth_role__is_custom: int | None
    def __init__(self, auth_role_uri_uid: str | None, auth_role_uri_name: str | None, auth_role_uid: str | None, uri: str | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None, auth_role__auth_role_name: str | None, auth_role__parent_auth_role_uid: str | None, auth_role__tenant_uid: str | None, auth_role__role_description: str | None, auth_role__access_uris: str | None, auth_role__is_project: int | None, auth_role__is_tenant: int | None, auth_role__is_client: int | None, auth_role__is_custom: int | None):
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
        self.auth_role__auth_role_name = auth_role__auth_role_name
        self.auth_role__parent_auth_role_uid = auth_role__parent_auth_role_uid
        self.auth_role__tenant_uid = auth_role__tenant_uid
        self.auth_role__role_description = auth_role__role_description
        self.auth_role__access_uris = auth_role__access_uris
        self.auth_role__is_project = auth_role__is_project
        self.auth_role__is_tenant = auth_role__is_tenant
        self.auth_role__is_client = auth_role__is_client
        self.auth_role__is_custom = auth_role__is_custom
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.auth_role_uri_uid, self.auth_role_uri_name, self.auth_role_uid, self.uri, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes, self.auth_role__auth_role_name, self.auth_role__parent_auth_role_uid, self.auth_role__tenant_uid, self.auth_role__role_description, self.auth_role__access_uris, self.auth_role__is_project, self.auth_role__is_tenant, self.auth_role__is_client, self.auth_role__is_custom]


@dataclass(frozen=False)
class auth_session_rich_dto(auth_session_read_dto):
    auth_session_uid: str | None
    auth_session_name: str | None
    tenant_uid: str | None
    account_uid: str | None
    session_token: str | None
    browser_name: str | None
    browser_description: str | None
    host_name: str | None
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
    tenant__tenant_name: str | None
    tenant__country_uid: str | None
    tenant__tenant_type_uid: str | None
    tenant__tenant_category_uid: str | None
    tenant__tenant_code: str | None
    tenant__tenant_description: str | None
    tenant__start_date: datetime.datetime | None
    tenant__end_date: datetime.datetime | None
    tenant__is_internal: int | None
    tenant__is_system: int | None
    tenant__is_test: int | None
    tenant__account_uid: str | None
    account__account_name: str | None
    account__tenant_uid: str | None
    account__account_type_uid: str | None
    account__account_title_uid: str | None
    account__account_division_uid: str | None
    account__account_group_uid: str | None
    account__auth_identity_uid: str | None
    account__account_email: str | None
    account__display_name: str | None
    account__account_address: str | None
    account__is_verified: int | None
    account__is_system: int | None
    def __init__(self, auth_session_uid: str | None, auth_session_name: str | None, tenant_uid: str | None, account_uid: str | None, session_token: str | None, browser_name: str | None, browser_description: str | None, host_name: str | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None, tenant__tenant_name: str | None, tenant__country_uid: str | None, tenant__tenant_type_uid: str | None, tenant__tenant_category_uid: str | None, tenant__tenant_code: str | None, tenant__tenant_description: str | None, tenant__start_date: datetime.datetime | None, tenant__end_date: datetime.datetime | None, tenant__is_internal: int | None, tenant__is_system: int | None, tenant__is_test: int | None, tenant__account_uid: str | None, account__account_name: str | None, account__tenant_uid: str | None, account__account_type_uid: str | None, account__account_title_uid: str | None, account__account_division_uid: str | None, account__account_group_uid: str | None, account__auth_identity_uid: str | None, account__account_email: str | None, account__display_name: str | None, account__account_address: str | None, account__is_verified: int | None, account__is_system: int | None):
        self.auth_session_uid = auth_session_uid
        self.auth_session_name = auth_session_name
        self.tenant_uid = tenant_uid
        self.account_uid = account_uid
        self.session_token = session_token
        self.browser_name = browser_name
        self.browser_description = browser_description
        self.host_name = host_name
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
        self.tenant__tenant_name = tenant__tenant_name
        self.tenant__country_uid = tenant__country_uid
        self.tenant__tenant_type_uid = tenant__tenant_type_uid
        self.tenant__tenant_category_uid = tenant__tenant_category_uid
        self.tenant__tenant_code = tenant__tenant_code
        self.tenant__tenant_description = tenant__tenant_description
        self.tenant__start_date = tenant__start_date
        self.tenant__end_date = tenant__end_date
        self.tenant__is_internal = tenant__is_internal
        self.tenant__is_system = tenant__is_system
        self.tenant__is_test = tenant__is_test
        self.tenant__account_uid = tenant__account_uid
        self.account__account_name = account__account_name
        self.account__tenant_uid = account__tenant_uid
        self.account__account_type_uid = account__account_type_uid
        self.account__account_title_uid = account__account_title_uid
        self.account__account_division_uid = account__account_division_uid
        self.account__account_group_uid = account__account_group_uid
        self.account__auth_identity_uid = account__auth_identity_uid
        self.account__account_email = account__account_email
        self.account__display_name = account__display_name
        self.account__account_address = account__account_address
        self.account__is_verified = account__is_verified
        self.account__is_system = account__is_system
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.auth_session_uid, self.auth_session_name, self.tenant_uid, self.account_uid, self.session_token, self.browser_name, self.browser_description, self.host_name, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes, self.tenant__tenant_name, self.tenant__country_uid, self.tenant__tenant_type_uid, self.tenant__tenant_category_uid, self.tenant__tenant_code, self.tenant__tenant_description, self.tenant__start_date, self.tenant__end_date, self.tenant__is_internal, self.tenant__is_system, self.tenant__is_test, self.tenant__account_uid, self.account__account_name, self.account__tenant_uid, self.account__account_type_uid, self.account__account_title_uid, self.account__account_division_uid, self.account__account_group_uid, self.account__auth_identity_uid, self.account__account_email, self.account__display_name, self.account__account_address, self.account__is_verified, self.account__is_system]


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
    tenant__tenant_name: str | None
    tenant__country_uid: str | None
    tenant__tenant_type_uid: str | None
    tenant__tenant_category_uid: str | None
    tenant__tenant_code: str | None
    tenant__tenant_description: str | None
    tenant__start_date: datetime.datetime | None
    tenant__end_date: datetime.datetime | None
    tenant__is_internal: int | None
    tenant__is_system: int | None
    tenant__is_test: int | None
    tenant__account_uid: str | None
    owner_account__account_name: str | None
    owner_account__tenant_uid: str | None
    owner_account__account_type_uid: str | None
    owner_account__account_title_uid: str | None
    owner_account__account_division_uid: str | None
    owner_account__account_group_uid: str | None
    owner_account__auth_identity_uid: str | None
    owner_account__account_email: str | None
    owner_account__display_name: str | None
    owner_account__account_address: str | None
    owner_account__is_verified: int | None
    owner_account__is_system: int | None
    def __init__(self, auth_sso_uid: str | None, auth_sso_name: str | None, tenant_uid: str | None, owner_account_uid: str | None, sso_name: str | None, sso_url: str | None, sso_key: str | None, sso_secret: str | None, sso_code: str | None, clientid: str | None, clientsecret: str | None, callback_url: str | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None, tenant__tenant_name: str | None, tenant__country_uid: str | None, tenant__tenant_type_uid: str | None, tenant__tenant_category_uid: str | None, tenant__tenant_code: str | None, tenant__tenant_description: str | None, tenant__start_date: datetime.datetime | None, tenant__end_date: datetime.datetime | None, tenant__is_internal: int | None, tenant__is_system: int | None, tenant__is_test: int | None, tenant__account_uid: str | None, owner_account__account_name: str | None, owner_account__tenant_uid: str | None, owner_account__account_type_uid: str | None, owner_account__account_title_uid: str | None, owner_account__account_division_uid: str | None, owner_account__account_group_uid: str | None, owner_account__auth_identity_uid: str | None, owner_account__account_email: str | None, owner_account__display_name: str | None, owner_account__account_address: str | None, owner_account__is_verified: int | None, owner_account__is_system: int | None):
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
        self.tenant__tenant_name = tenant__tenant_name
        self.tenant__country_uid = tenant__country_uid
        self.tenant__tenant_type_uid = tenant__tenant_type_uid
        self.tenant__tenant_category_uid = tenant__tenant_category_uid
        self.tenant__tenant_code = tenant__tenant_code
        self.tenant__tenant_description = tenant__tenant_description
        self.tenant__start_date = tenant__start_date
        self.tenant__end_date = tenant__end_date
        self.tenant__is_internal = tenant__is_internal
        self.tenant__is_system = tenant__is_system
        self.tenant__is_test = tenant__is_test
        self.tenant__account_uid = tenant__account_uid
        self.owner_account__account_name = owner_account__account_name
        self.owner_account__tenant_uid = owner_account__tenant_uid
        self.owner_account__account_type_uid = owner_account__account_type_uid
        self.owner_account__account_title_uid = owner_account__account_title_uid
        self.owner_account__account_division_uid = owner_account__account_division_uid
        self.owner_account__account_group_uid = owner_account__account_group_uid
        self.owner_account__auth_identity_uid = owner_account__auth_identity_uid
        self.owner_account__account_email = owner_account__account_email
        self.owner_account__display_name = owner_account__display_name
        self.owner_account__account_address = owner_account__account_address
        self.owner_account__is_verified = owner_account__is_verified
        self.owner_account__is_system = owner_account__is_system
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.auth_sso_uid, self.auth_sso_name, self.tenant_uid, self.owner_account_uid, self.sso_name, self.sso_url, self.sso_key, self.sso_secret, self.sso_code, self.clientid, self.clientsecret, self.callback_url, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes, self.tenant__tenant_name, self.tenant__country_uid, self.tenant__tenant_type_uid, self.tenant__tenant_category_uid, self.tenant__tenant_code, self.tenant__tenant_description, self.tenant__start_date, self.tenant__end_date, self.tenant__is_internal, self.tenant__is_system, self.tenant__is_test, self.tenant__account_uid, self.owner_account__account_name, self.owner_account__tenant_uid, self.owner_account__account_type_uid, self.owner_account__account_title_uid, self.owner_account__account_division_uid, self.owner_account__account_group_uid, self.owner_account__auth_identity_uid, self.owner_account__account_email, self.owner_account__display_name, self.owner_account__account_address, self.owner_account__is_verified, self.owner_account__is_system]


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
    tenant__tenant_name: str | None
    tenant__country_uid: str | None
    tenant__tenant_type_uid: str | None
    tenant__tenant_category_uid: str | None
    tenant__tenant_code: str | None
    tenant__tenant_description: str | None
    tenant__start_date: datetime.datetime | None
    tenant__end_date: datetime.datetime | None
    tenant__is_internal: int | None
    tenant__is_system: int | None
    tenant__is_test: int | None
    tenant__account_uid: str | None
    account__account_name: str | None
    account__tenant_uid: str | None
    account__account_type_uid: str | None
    account__account_title_uid: str | None
    account__account_division_uid: str | None
    account__account_group_uid: str | None
    account__auth_identity_uid: str | None
    account__account_email: str | None
    account__display_name: str | None
    account__account_address: str | None
    account__is_verified: int | None
    account__is_system: int | None
    def __init__(self, auth_token_uid: str | None, auth_token_name: str | None, tenant_uid: str | None, account_uid: str | None, token_seq: int | None, token_hash: str | None, token_salt: str | None, valid_till_date: datetime.datetime | None, last_use_date: datetime.datetime | None, is_last: int | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None, tenant__tenant_name: str | None, tenant__country_uid: str | None, tenant__tenant_type_uid: str | None, tenant__tenant_category_uid: str | None, tenant__tenant_code: str | None, tenant__tenant_description: str | None, tenant__start_date: datetime.datetime | None, tenant__end_date: datetime.datetime | None, tenant__is_internal: int | None, tenant__is_system: int | None, tenant__is_test: int | None, tenant__account_uid: str | None, account__account_name: str | None, account__tenant_uid: str | None, account__account_type_uid: str | None, account__account_title_uid: str | None, account__account_division_uid: str | None, account__account_group_uid: str | None, account__auth_identity_uid: str | None, account__account_email: str | None, account__display_name: str | None, account__account_address: str | None, account__is_verified: int | None, account__is_system: int | None):
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
        self.tenant__tenant_name = tenant__tenant_name
        self.tenant__country_uid = tenant__country_uid
        self.tenant__tenant_type_uid = tenant__tenant_type_uid
        self.tenant__tenant_category_uid = tenant__tenant_category_uid
        self.tenant__tenant_code = tenant__tenant_code
        self.tenant__tenant_description = tenant__tenant_description
        self.tenant__start_date = tenant__start_date
        self.tenant__end_date = tenant__end_date
        self.tenant__is_internal = tenant__is_internal
        self.tenant__is_system = tenant__is_system
        self.tenant__is_test = tenant__is_test
        self.tenant__account_uid = tenant__account_uid
        self.account__account_name = account__account_name
        self.account__tenant_uid = account__tenant_uid
        self.account__account_type_uid = account__account_type_uid
        self.account__account_title_uid = account__account_title_uid
        self.account__account_division_uid = account__account_division_uid
        self.account__account_group_uid = account__account_group_uid
        self.account__auth_identity_uid = account__auth_identity_uid
        self.account__account_email = account__account_email
        self.account__display_name = account__display_name
        self.account__account_address = account__account_address
        self.account__is_verified = account__is_verified
        self.account__is_system = account__is_system
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.auth_token_uid, self.auth_token_name, self.tenant_uid, self.account_uid, self.token_seq, self.token_hash, self.token_salt, self.valid_till_date, self.last_use_date, self.is_last, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes, self.tenant__tenant_name, self.tenant__country_uid, self.tenant__tenant_type_uid, self.tenant__tenant_category_uid, self.tenant__tenant_code, self.tenant__tenant_description, self.tenant__start_date, self.tenant__end_date, self.tenant__is_internal, self.tenant__is_system, self.tenant__is_test, self.tenant__account_uid, self.account__account_name, self.account__tenant_uid, self.account__account_type_uid, self.account__account_title_uid, self.account__account_division_uid, self.account__account_group_uid, self.account__auth_identity_uid, self.account__account_email, self.account__display_name, self.account__account_address, self.account__is_verified, self.account__is_system]


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
    calendar_account__account_name: str | None
    calendar_account__tenant_uid: str | None
    calendar_account__account_type_uid: str | None
    calendar_account__account_title_uid: str | None
    calendar_account__account_division_uid: str | None
    calendar_account__account_group_uid: str | None
    calendar_account__auth_identity_uid: str | None
    calendar_account__account_email: str | None
    calendar_account__display_name: str | None
    calendar_account__account_address: str | None
    calendar_account__is_verified: int | None
    calendar_account__is_system: int | None
    tenant__tenant_name: str | None
    tenant__country_uid: str | None
    tenant__tenant_type_uid: str | None
    tenant__tenant_category_uid: str | None
    tenant__tenant_code: str | None
    tenant__tenant_description: str | None
    tenant__start_date: datetime.datetime | None
    tenant__end_date: datetime.datetime | None
    tenant__is_internal: int | None
    tenant__is_system: int | None
    tenant__is_test: int | None
    tenant__account_uid: str | None
    account__account_name: str | None
    account__tenant_uid: str | None
    account__account_type_uid: str | None
    account__account_title_uid: str | None
    account__account_division_uid: str | None
    account__account_group_uid: str | None
    account__auth_identity_uid: str | None
    account__account_email: str | None
    account__display_name: str | None
    account__account_address: str | None
    account__is_verified: int | None
    account__is_system: int | None
    calendar_type__calendar_type_name: str | None
    def __init__(self, calendar_account_uid: str | None, calendar_account_name: str | None, tenant_uid: str | None, account_uid: str | None, calendar_type_uid: str | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None, calendar_account__account_name: str | None, calendar_account__tenant_uid: str | None, calendar_account__account_type_uid: str | None, calendar_account__account_title_uid: str | None, calendar_account__account_division_uid: str | None, calendar_account__account_group_uid: str | None, calendar_account__auth_identity_uid: str | None, calendar_account__account_email: str | None, calendar_account__display_name: str | None, calendar_account__account_address: str | None, calendar_account__is_verified: int | None, calendar_account__is_system: int | None, tenant__tenant_name: str | None, tenant__country_uid: str | None, tenant__tenant_type_uid: str | None, tenant__tenant_category_uid: str | None, tenant__tenant_code: str | None, tenant__tenant_description: str | None, tenant__start_date: datetime.datetime | None, tenant__end_date: datetime.datetime | None, tenant__is_internal: int | None, tenant__is_system: int | None, tenant__is_test: int | None, tenant__account_uid: str | None, account__account_name: str | None, account__tenant_uid: str | None, account__account_type_uid: str | None, account__account_title_uid: str | None, account__account_division_uid: str | None, account__account_group_uid: str | None, account__auth_identity_uid: str | None, account__account_email: str | None, account__display_name: str | None, account__account_address: str | None, account__is_verified: int | None, account__is_system: int | None, calendar_type__calendar_type_name: str | None):
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
        self.calendar_account__account_name = calendar_account__account_name
        self.calendar_account__tenant_uid = calendar_account__tenant_uid
        self.calendar_account__account_type_uid = calendar_account__account_type_uid
        self.calendar_account__account_title_uid = calendar_account__account_title_uid
        self.calendar_account__account_division_uid = calendar_account__account_division_uid
        self.calendar_account__account_group_uid = calendar_account__account_group_uid
        self.calendar_account__auth_identity_uid = calendar_account__auth_identity_uid
        self.calendar_account__account_email = calendar_account__account_email
        self.calendar_account__display_name = calendar_account__display_name
        self.calendar_account__account_address = calendar_account__account_address
        self.calendar_account__is_verified = calendar_account__is_verified
        self.calendar_account__is_system = calendar_account__is_system
        self.tenant__tenant_name = tenant__tenant_name
        self.tenant__country_uid = tenant__country_uid
        self.tenant__tenant_type_uid = tenant__tenant_type_uid
        self.tenant__tenant_category_uid = tenant__tenant_category_uid
        self.tenant__tenant_code = tenant__tenant_code
        self.tenant__tenant_description = tenant__tenant_description
        self.tenant__start_date = tenant__start_date
        self.tenant__end_date = tenant__end_date
        self.tenant__is_internal = tenant__is_internal
        self.tenant__is_system = tenant__is_system
        self.tenant__is_test = tenant__is_test
        self.tenant__account_uid = tenant__account_uid
        self.account__account_name = account__account_name
        self.account__tenant_uid = account__tenant_uid
        self.account__account_type_uid = account__account_type_uid
        self.account__account_title_uid = account__account_title_uid
        self.account__account_division_uid = account__account_division_uid
        self.account__account_group_uid = account__account_group_uid
        self.account__auth_identity_uid = account__auth_identity_uid
        self.account__account_email = account__account_email
        self.account__display_name = account__display_name
        self.account__account_address = account__account_address
        self.account__is_verified = account__is_verified
        self.account__is_system = account__is_system
        self.calendar_type__calendar_type_name = calendar_type__calendar_type_name
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.calendar_account_uid, self.calendar_account_name, self.tenant_uid, self.account_uid, self.calendar_type_uid, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes, self.calendar_account__account_name, self.calendar_account__tenant_uid, self.calendar_account__account_type_uid, self.calendar_account__account_title_uid, self.calendar_account__account_division_uid, self.calendar_account__account_group_uid, self.calendar_account__auth_identity_uid, self.calendar_account__account_email, self.calendar_account__display_name, self.calendar_account__account_address, self.calendar_account__is_verified, self.calendar_account__is_system, self.tenant__tenant_name, self.tenant__country_uid, self.tenant__tenant_type_uid, self.tenant__tenant_category_uid, self.tenant__tenant_code, self.tenant__tenant_description, self.tenant__start_date, self.tenant__end_date, self.tenant__is_internal, self.tenant__is_system, self.tenant__is_test, self.tenant__account_uid, self.account__account_name, self.account__tenant_uid, self.account__account_type_uid, self.account__account_title_uid, self.account__account_division_uid, self.account__account_group_uid, self.account__auth_identity_uid, self.account__account_email, self.account__display_name, self.account__account_address, self.account__is_verified, self.account__is_system, self.calendar_type__calendar_type_name]


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
    client__client_name: str | None
    client__tenant_uid: str | None
    client__country_uid: str | None
    client__client_type_uid: str | None
    client__client_category_uid: str | None
    client__account_uid: str | None
    client__client_code: str | None
    client__client_description: str | None
    client__start_date: datetime.datetime | None
    client__end_date: datetime.datetime | None
    client__is_internal: int | None
    client__is_system: int | None
    client__is_test: int | None
    account__account_name: str | None
    account__tenant_uid: str | None
    account__account_type_uid: str | None
    account__account_title_uid: str | None
    account__account_division_uid: str | None
    account__account_group_uid: str | None
    account__auth_identity_uid: str | None
    account__account_email: str | None
    account__display_name: str | None
    account__account_address: str | None
    account__is_verified: int | None
    account__is_system: int | None
    calendar_approval_type__calendar_approval_type_name: str | None
    calendar_event_group__calendar_event_group_name: str | None
    calendar_event_group__client_uid: str | None
    calendar_event_group__account_uid: str | None
    calendar_event_group__calendar_account_uid: str | None
    calendar_event_group__calendar_event_type_uid: str | None
    calendar_event_group__group_comment: str | None
    calendar_event_group__event_start_date: datetime.datetime | None
    calendar_event_group__event_end_date: datetime.datetime | None
    calendar_event_group__is_approved: int | None
    calendar_type__calendar_type_name: str | None
    def __init__(self, calendar_approval_uid: str | None, calendar_approval_name: str | None, client_uid: str | None, account_uid: str | None, calendar_approval_type_uid: str | None, calendar_event_group_uid: str | None, calendar_type_uid: str | None, time_submit_type_name: str | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None, client__client_name: str | None, client__tenant_uid: str | None, client__country_uid: str | None, client__client_type_uid: str | None, client__client_category_uid: str | None, client__account_uid: str | None, client__client_code: str | None, client__client_description: str | None, client__start_date: datetime.datetime | None, client__end_date: datetime.datetime | None, client__is_internal: int | None, client__is_system: int | None, client__is_test: int | None, account__account_name: str | None, account__tenant_uid: str | None, account__account_type_uid: str | None, account__account_title_uid: str | None, account__account_division_uid: str | None, account__account_group_uid: str | None, account__auth_identity_uid: str | None, account__account_email: str | None, account__display_name: str | None, account__account_address: str | None, account__is_verified: int | None, account__is_system: int | None, calendar_approval_type__calendar_approval_type_name: str | None, calendar_event_group__calendar_event_group_name: str | None, calendar_event_group__client_uid: str | None, calendar_event_group__account_uid: str | None, calendar_event_group__calendar_account_uid: str | None, calendar_event_group__calendar_event_type_uid: str | None, calendar_event_group__group_comment: str | None, calendar_event_group__event_start_date: datetime.datetime | None, calendar_event_group__event_end_date: datetime.datetime | None, calendar_event_group__is_approved: int | None, calendar_type__calendar_type_name: str | None):
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
        self.client__client_name = client__client_name
        self.client__tenant_uid = client__tenant_uid
        self.client__country_uid = client__country_uid
        self.client__client_type_uid = client__client_type_uid
        self.client__client_category_uid = client__client_category_uid
        self.client__account_uid = client__account_uid
        self.client__client_code = client__client_code
        self.client__client_description = client__client_description
        self.client__start_date = client__start_date
        self.client__end_date = client__end_date
        self.client__is_internal = client__is_internal
        self.client__is_system = client__is_system
        self.client__is_test = client__is_test
        self.account__account_name = account__account_name
        self.account__tenant_uid = account__tenant_uid
        self.account__account_type_uid = account__account_type_uid
        self.account__account_title_uid = account__account_title_uid
        self.account__account_division_uid = account__account_division_uid
        self.account__account_group_uid = account__account_group_uid
        self.account__auth_identity_uid = account__auth_identity_uid
        self.account__account_email = account__account_email
        self.account__display_name = account__display_name
        self.account__account_address = account__account_address
        self.account__is_verified = account__is_verified
        self.account__is_system = account__is_system
        self.calendar_approval_type__calendar_approval_type_name = calendar_approval_type__calendar_approval_type_name
        self.calendar_event_group__calendar_event_group_name = calendar_event_group__calendar_event_group_name
        self.calendar_event_group__client_uid = calendar_event_group__client_uid
        self.calendar_event_group__account_uid = calendar_event_group__account_uid
        self.calendar_event_group__calendar_account_uid = calendar_event_group__calendar_account_uid
        self.calendar_event_group__calendar_event_type_uid = calendar_event_group__calendar_event_type_uid
        self.calendar_event_group__group_comment = calendar_event_group__group_comment
        self.calendar_event_group__event_start_date = calendar_event_group__event_start_date
        self.calendar_event_group__event_end_date = calendar_event_group__event_end_date
        self.calendar_event_group__is_approved = calendar_event_group__is_approved
        self.calendar_type__calendar_type_name = calendar_type__calendar_type_name
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.calendar_approval_uid, self.calendar_approval_name, self.client_uid, self.account_uid, self.calendar_approval_type_uid, self.calendar_event_group_uid, self.calendar_type_uid, self.time_submit_type_name, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes, self.client__client_name, self.client__tenant_uid, self.client__country_uid, self.client__client_type_uid, self.client__client_category_uid, self.client__account_uid, self.client__client_code, self.client__client_description, self.client__start_date, self.client__end_date, self.client__is_internal, self.client__is_system, self.client__is_test, self.account__account_name, self.account__tenant_uid, self.account__account_type_uid, self.account__account_title_uid, self.account__account_division_uid, self.account__account_group_uid, self.account__auth_identity_uid, self.account__account_email, self.account__display_name, self.account__account_address, self.account__is_verified, self.account__is_system, self.calendar_approval_type__calendar_approval_type_name, self.calendar_event_group__calendar_event_group_name, self.calendar_event_group__client_uid, self.calendar_event_group__account_uid, self.calendar_event_group__calendar_account_uid, self.calendar_event_group__calendar_event_type_uid, self.calendar_event_group__group_comment, self.calendar_event_group__event_start_date, self.calendar_event_group__event_end_date, self.calendar_event_group__is_approved, self.calendar_type__calendar_type_name]


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
    client__client_name: str | None
    client__tenant_uid: str | None
    client__country_uid: str | None
    client__client_type_uid: str | None
    client__client_category_uid: str | None
    client__account_uid: str | None
    client__client_code: str | None
    client__client_description: str | None
    client__start_date: datetime.datetime | None
    client__end_date: datetime.datetime | None
    client__is_internal: int | None
    client__is_system: int | None
    client__is_test: int | None
    account__account_name: str | None
    account__tenant_uid: str | None
    account__account_type_uid: str | None
    account__account_title_uid: str | None
    account__account_division_uid: str | None
    account__account_group_uid: str | None
    account__auth_identity_uid: str | None
    account__account_email: str | None
    account__display_name: str | None
    account__account_address: str | None
    account__is_verified: int | None
    account__is_system: int | None
    calendar_event_group__calendar_event_group_name: str | None
    calendar_event_group__client_uid: str | None
    calendar_event_group__account_uid: str | None
    calendar_event_group__calendar_account_uid: str | None
    calendar_event_group__calendar_event_type_uid: str | None
    calendar_event_group__group_comment: str | None
    calendar_event_group__event_start_date: datetime.datetime | None
    calendar_event_group__event_end_date: datetime.datetime | None
    calendar_event_group__is_approved: int | None
    calendar_type__calendar_type_name: str | None
    def __init__(self, calendar_event_uid: str | None, calendar_event_name: str | None, client_uid: str | None, account_uid: str | None, calendar_event_group_uid: str | None, calendar_type_uid: str | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None, client__client_name: str | None, client__tenant_uid: str | None, client__country_uid: str | None, client__client_type_uid: str | None, client__client_category_uid: str | None, client__account_uid: str | None, client__client_code: str | None, client__client_description: str | None, client__start_date: datetime.datetime | None, client__end_date: datetime.datetime | None, client__is_internal: int | None, client__is_system: int | None, client__is_test: int | None, account__account_name: str | None, account__tenant_uid: str | None, account__account_type_uid: str | None, account__account_title_uid: str | None, account__account_division_uid: str | None, account__account_group_uid: str | None, account__auth_identity_uid: str | None, account__account_email: str | None, account__display_name: str | None, account__account_address: str | None, account__is_verified: int | None, account__is_system: int | None, calendar_event_group__calendar_event_group_name: str | None, calendar_event_group__client_uid: str | None, calendar_event_group__account_uid: str | None, calendar_event_group__calendar_account_uid: str | None, calendar_event_group__calendar_event_type_uid: str | None, calendar_event_group__group_comment: str | None, calendar_event_group__event_start_date: datetime.datetime | None, calendar_event_group__event_end_date: datetime.datetime | None, calendar_event_group__is_approved: int | None, calendar_type__calendar_type_name: str | None):
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
        self.client__client_name = client__client_name
        self.client__tenant_uid = client__tenant_uid
        self.client__country_uid = client__country_uid
        self.client__client_type_uid = client__client_type_uid
        self.client__client_category_uid = client__client_category_uid
        self.client__account_uid = client__account_uid
        self.client__client_code = client__client_code
        self.client__client_description = client__client_description
        self.client__start_date = client__start_date
        self.client__end_date = client__end_date
        self.client__is_internal = client__is_internal
        self.client__is_system = client__is_system
        self.client__is_test = client__is_test
        self.account__account_name = account__account_name
        self.account__tenant_uid = account__tenant_uid
        self.account__account_type_uid = account__account_type_uid
        self.account__account_title_uid = account__account_title_uid
        self.account__account_division_uid = account__account_division_uid
        self.account__account_group_uid = account__account_group_uid
        self.account__auth_identity_uid = account__auth_identity_uid
        self.account__account_email = account__account_email
        self.account__display_name = account__display_name
        self.account__account_address = account__account_address
        self.account__is_verified = account__is_verified
        self.account__is_system = account__is_system
        self.calendar_event_group__calendar_event_group_name = calendar_event_group__calendar_event_group_name
        self.calendar_event_group__client_uid = calendar_event_group__client_uid
        self.calendar_event_group__account_uid = calendar_event_group__account_uid
        self.calendar_event_group__calendar_account_uid = calendar_event_group__calendar_account_uid
        self.calendar_event_group__calendar_event_type_uid = calendar_event_group__calendar_event_type_uid
        self.calendar_event_group__group_comment = calendar_event_group__group_comment
        self.calendar_event_group__event_start_date = calendar_event_group__event_start_date
        self.calendar_event_group__event_end_date = calendar_event_group__event_end_date
        self.calendar_event_group__is_approved = calendar_event_group__is_approved
        self.calendar_type__calendar_type_name = calendar_type__calendar_type_name
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.calendar_event_uid, self.calendar_event_name, self.client_uid, self.account_uid, self.calendar_event_group_uid, self.calendar_type_uid, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes, self.client__client_name, self.client__tenant_uid, self.client__country_uid, self.client__client_type_uid, self.client__client_category_uid, self.client__account_uid, self.client__client_code, self.client__client_description, self.client__start_date, self.client__end_date, self.client__is_internal, self.client__is_system, self.client__is_test, self.account__account_name, self.account__tenant_uid, self.account__account_type_uid, self.account__account_title_uid, self.account__account_division_uid, self.account__account_group_uid, self.account__auth_identity_uid, self.account__account_email, self.account__display_name, self.account__account_address, self.account__is_verified, self.account__is_system, self.calendar_event_group__calendar_event_group_name, self.calendar_event_group__client_uid, self.calendar_event_group__account_uid, self.calendar_event_group__calendar_account_uid, self.calendar_event_group__calendar_event_type_uid, self.calendar_event_group__group_comment, self.calendar_event_group__event_start_date, self.calendar_event_group__event_end_date, self.calendar_event_group__is_approved, self.calendar_type__calendar_type_name]


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
    client__client_name: str | None
    client__tenant_uid: str | None
    client__country_uid: str | None
    client__client_type_uid: str | None
    client__client_category_uid: str | None
    client__account_uid: str | None
    client__client_code: str | None
    client__client_description: str | None
    client__start_date: datetime.datetime | None
    client__end_date: datetime.datetime | None
    client__is_internal: int | None
    client__is_system: int | None
    client__is_test: int | None
    account__account_name: str | None
    account__tenant_uid: str | None
    account__account_type_uid: str | None
    account__account_title_uid: str | None
    account__account_division_uid: str | None
    account__account_group_uid: str | None
    account__auth_identity_uid: str | None
    account__account_email: str | None
    account__display_name: str | None
    account__account_address: str | None
    account__is_verified: int | None
    account__is_system: int | None
    calendar_account__account_name: str | None
    calendar_account__tenant_uid: str | None
    calendar_account__account_type_uid: str | None
    calendar_account__account_title_uid: str | None
    calendar_account__account_division_uid: str | None
    calendar_account__account_group_uid: str | None
    calendar_account__auth_identity_uid: str | None
    calendar_account__account_email: str | None
    calendar_account__display_name: str | None
    calendar_account__account_address: str | None
    calendar_account__is_verified: int | None
    calendar_account__is_system: int | None
    calendar_event_type__event_type_name: str | None
    calendar_event_type__event_type_description: str | None
    def __init__(self, calendar_event_group_uid: str | None, calendar_event_group_name: str | None, client_uid: str | None, account_uid: str | None, calendar_account_uid: str | None, calendar_event_type_uid: str | None, group_comment: str | None, event_start_date: datetime.datetime | None, event_end_date: datetime.datetime | None, is_approved: int | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None, client__client_name: str | None, client__tenant_uid: str | None, client__country_uid: str | None, client__client_type_uid: str | None, client__client_category_uid: str | None, client__account_uid: str | None, client__client_code: str | None, client__client_description: str | None, client__start_date: datetime.datetime | None, client__end_date: datetime.datetime | None, client__is_internal: int | None, client__is_system: int | None, client__is_test: int | None, account__account_name: str | None, account__tenant_uid: str | None, account__account_type_uid: str | None, account__account_title_uid: str | None, account__account_division_uid: str | None, account__account_group_uid: str | None, account__auth_identity_uid: str | None, account__account_email: str | None, account__display_name: str | None, account__account_address: str | None, account__is_verified: int | None, account__is_system: int | None, calendar_account__account_name: str | None, calendar_account__tenant_uid: str | None, calendar_account__account_type_uid: str | None, calendar_account__account_title_uid: str | None, calendar_account__account_division_uid: str | None, calendar_account__account_group_uid: str | None, calendar_account__auth_identity_uid: str | None, calendar_account__account_email: str | None, calendar_account__display_name: str | None, calendar_account__account_address: str | None, calendar_account__is_verified: int | None, calendar_account__is_system: int | None, calendar_event_type__event_type_name: str | None, calendar_event_type__event_type_description: str | None):
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
        self.client__client_name = client__client_name
        self.client__tenant_uid = client__tenant_uid
        self.client__country_uid = client__country_uid
        self.client__client_type_uid = client__client_type_uid
        self.client__client_category_uid = client__client_category_uid
        self.client__account_uid = client__account_uid
        self.client__client_code = client__client_code
        self.client__client_description = client__client_description
        self.client__start_date = client__start_date
        self.client__end_date = client__end_date
        self.client__is_internal = client__is_internal
        self.client__is_system = client__is_system
        self.client__is_test = client__is_test
        self.account__account_name = account__account_name
        self.account__tenant_uid = account__tenant_uid
        self.account__account_type_uid = account__account_type_uid
        self.account__account_title_uid = account__account_title_uid
        self.account__account_division_uid = account__account_division_uid
        self.account__account_group_uid = account__account_group_uid
        self.account__auth_identity_uid = account__auth_identity_uid
        self.account__account_email = account__account_email
        self.account__display_name = account__display_name
        self.account__account_address = account__account_address
        self.account__is_verified = account__is_verified
        self.account__is_system = account__is_system
        self.calendar_account__account_name = calendar_account__account_name
        self.calendar_account__tenant_uid = calendar_account__tenant_uid
        self.calendar_account__account_type_uid = calendar_account__account_type_uid
        self.calendar_account__account_title_uid = calendar_account__account_title_uid
        self.calendar_account__account_division_uid = calendar_account__account_division_uid
        self.calendar_account__account_group_uid = calendar_account__account_group_uid
        self.calendar_account__auth_identity_uid = calendar_account__auth_identity_uid
        self.calendar_account__account_email = calendar_account__account_email
        self.calendar_account__display_name = calendar_account__display_name
        self.calendar_account__account_address = calendar_account__account_address
        self.calendar_account__is_verified = calendar_account__is_verified
        self.calendar_account__is_system = calendar_account__is_system
        self.calendar_event_type__event_type_name = calendar_event_type__event_type_name
        self.calendar_event_type__event_type_description = calendar_event_type__event_type_description
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.calendar_event_group_uid, self.calendar_event_group_name, self.client_uid, self.account_uid, self.calendar_account_uid, self.calendar_event_type_uid, self.group_comment, self.event_start_date, self.event_end_date, self.is_approved, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes, self.client__client_name, self.client__tenant_uid, self.client__country_uid, self.client__client_type_uid, self.client__client_category_uid, self.client__account_uid, self.client__client_code, self.client__client_description, self.client__start_date, self.client__end_date, self.client__is_internal, self.client__is_system, self.client__is_test, self.account__account_name, self.account__tenant_uid, self.account__account_type_uid, self.account__account_title_uid, self.account__account_division_uid, self.account__account_group_uid, self.account__auth_identity_uid, self.account__account_email, self.account__display_name, self.account__account_address, self.account__is_verified, self.account__is_system, self.calendar_account__account_name, self.calendar_account__tenant_uid, self.calendar_account__account_type_uid, self.calendar_account__account_title_uid, self.calendar_account__account_division_uid, self.calendar_account__account_group_uid, self.calendar_account__auth_identity_uid, self.calendar_account__account_email, self.calendar_account__display_name, self.calendar_account__account_address, self.calendar_account__is_verified, self.calendar_account__is_system, self.calendar_event_type__event_type_name, self.calendar_event_type__event_type_description]


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
    calendar_event_type__event_type_name: str | None
    calendar_event_type__event_type_description: str | None
    client__client_name: str | None
    client__tenant_uid: str | None
    client__country_uid: str | None
    client__client_type_uid: str | None
    client__client_category_uid: str | None
    client__account_uid: str | None
    client__client_code: str | None
    client__client_description: str | None
    client__start_date: datetime.datetime | None
    client__end_date: datetime.datetime | None
    client__is_internal: int | None
    client__is_system: int | None
    client__is_test: int | None
    calendar_type__calendar_type_name: str | None
    def __init__(self, calendar_event_type_uid: str | None, calendar_event_type_name: str | None, client_uid: str | None, calendar_type_uid: str | None, auto_approved: int | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None, calendar_event_type__event_type_name: str | None, calendar_event_type__event_type_description: str | None, client__client_name: str | None, client__tenant_uid: str | None, client__country_uid: str | None, client__client_type_uid: str | None, client__client_category_uid: str | None, client__account_uid: str | None, client__client_code: str | None, client__client_description: str | None, client__start_date: datetime.datetime | None, client__end_date: datetime.datetime | None, client__is_internal: int | None, client__is_system: int | None, client__is_test: int | None, calendar_type__calendar_type_name: str | None):
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
        self.calendar_event_type__event_type_name = calendar_event_type__event_type_name
        self.calendar_event_type__event_type_description = calendar_event_type__event_type_description
        self.client__client_name = client__client_name
        self.client__tenant_uid = client__tenant_uid
        self.client__country_uid = client__country_uid
        self.client__client_type_uid = client__client_type_uid
        self.client__client_category_uid = client__client_category_uid
        self.client__account_uid = client__account_uid
        self.client__client_code = client__client_code
        self.client__client_description = client__client_description
        self.client__start_date = client__start_date
        self.client__end_date = client__end_date
        self.client__is_internal = client__is_internal
        self.client__is_system = client__is_system
        self.client__is_test = client__is_test
        self.calendar_type__calendar_type_name = calendar_type__calendar_type_name
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.calendar_event_type_uid, self.calendar_event_type_name, self.client_uid, self.calendar_type_uid, self.auto_approved, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes, self.calendar_event_type__event_type_name, self.calendar_event_type__event_type_description, self.client__client_name, self.client__tenant_uid, self.client__country_uid, self.client__client_type_uid, self.client__client_category_uid, self.client__account_uid, self.client__client_code, self.client__client_description, self.client__start_date, self.client__end_date, self.client__is_internal, self.client__is_system, self.client__is_test, self.calendar_type__calendar_type_name]


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
    tenant__tenant_name: str | None
    tenant__country_uid: str | None
    tenant__tenant_type_uid: str | None
    tenant__tenant_category_uid: str | None
    tenant__tenant_code: str | None
    tenant__tenant_description: str | None
    tenant__start_date: datetime.datetime | None
    tenant__end_date: datetime.datetime | None
    tenant__is_internal: int | None
    tenant__is_system: int | None
    tenant__is_test: int | None
    tenant__account_uid: str | None
    country__country_name: str | None
    country__continent_name: str | None
    country__continent_code: str | None
    country__country_iso3: str | None
    country__country_code: str | None
    country__phone_code: str | None
    country__currency_code: str | None
    country__capital_name: str | None
    country__region_name: str | None
    country__subregion_name: str | None
    country__region_code: str | None
    country__latitude: str | None
    country__longitude: str | None
    country__currency_name: str | None
    country__population: str | None
    country__languages: str | None
    country__area: str | None
    country__bar_code: str | None
    country__top_level_domain: str | None
    country__is_focused: int | None
    client_type__client_type_name: str | None
    client_type__client_type_description: str | None
    account__account_name: str | None
    account__tenant_uid: str | None
    account__account_type_uid: str | None
    account__account_title_uid: str | None
    account__account_division_uid: str | None
    account__account_group_uid: str | None
    account__auth_identity_uid: str | None
    account__account_email: str | None
    account__display_name: str | None
    account__account_address: str | None
    account__is_verified: int | None
    account__is_system: int | None
    def __init__(self, client_uid: str | None, client_name: str | None, tenant_uid: str | None, country_uid: str | None, client_type_uid: str | None, client_category_uid: str | None, account_uid: str | None, client_code: str | None, client_description: str | None, start_date: datetime.datetime | None, end_date: datetime.datetime | None, is_internal: int | None, is_system: int | None, is_test: int | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None, tenant__tenant_name: str | None, tenant__country_uid: str | None, tenant__tenant_type_uid: str | None, tenant__tenant_category_uid: str | None, tenant__tenant_code: str | None, tenant__tenant_description: str | None, tenant__start_date: datetime.datetime | None, tenant__end_date: datetime.datetime | None, tenant__is_internal: int | None, tenant__is_system: int | None, tenant__is_test: int | None, tenant__account_uid: str | None, country__country_name: str | None, country__continent_name: str | None, country__continent_code: str | None, country__country_iso3: str | None, country__country_code: str | None, country__phone_code: str | None, country__currency_code: str | None, country__capital_name: str | None, country__region_name: str | None, country__subregion_name: str | None, country__region_code: str | None, country__latitude: str | None, country__longitude: str | None, country__currency_name: str | None, country__population: str | None, country__languages: str | None, country__area: str | None, country__bar_code: str | None, country__top_level_domain: str | None, country__is_focused: int | None, client_type__client_type_name: str | None, client_type__client_type_description: str | None, account__account_name: str | None, account__tenant_uid: str | None, account__account_type_uid: str | None, account__account_title_uid: str | None, account__account_division_uid: str | None, account__account_group_uid: str | None, account__auth_identity_uid: str | None, account__account_email: str | None, account__display_name: str | None, account__account_address: str | None, account__is_verified: int | None, account__is_system: int | None):
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
        self.tenant__tenant_name = tenant__tenant_name
        self.tenant__country_uid = tenant__country_uid
        self.tenant__tenant_type_uid = tenant__tenant_type_uid
        self.tenant__tenant_category_uid = tenant__tenant_category_uid
        self.tenant__tenant_code = tenant__tenant_code
        self.tenant__tenant_description = tenant__tenant_description
        self.tenant__start_date = tenant__start_date
        self.tenant__end_date = tenant__end_date
        self.tenant__is_internal = tenant__is_internal
        self.tenant__is_system = tenant__is_system
        self.tenant__is_test = tenant__is_test
        self.tenant__account_uid = tenant__account_uid
        self.country__country_name = country__country_name
        self.country__continent_name = country__continent_name
        self.country__continent_code = country__continent_code
        self.country__country_iso3 = country__country_iso3
        self.country__country_code = country__country_code
        self.country__phone_code = country__phone_code
        self.country__currency_code = country__currency_code
        self.country__capital_name = country__capital_name
        self.country__region_name = country__region_name
        self.country__subregion_name = country__subregion_name
        self.country__region_code = country__region_code
        self.country__latitude = country__latitude
        self.country__longitude = country__longitude
        self.country__currency_name = country__currency_name
        self.country__population = country__population
        self.country__languages = country__languages
        self.country__area = country__area
        self.country__bar_code = country__bar_code
        self.country__top_level_domain = country__top_level_domain
        self.country__is_focused = country__is_focused
        self.client_type__client_type_name = client_type__client_type_name
        self.client_type__client_type_description = client_type__client_type_description
        self.account__account_name = account__account_name
        self.account__tenant_uid = account__tenant_uid
        self.account__account_type_uid = account__account_type_uid
        self.account__account_title_uid = account__account_title_uid
        self.account__account_division_uid = account__account_division_uid
        self.account__account_group_uid = account__account_group_uid
        self.account__auth_identity_uid = account__auth_identity_uid
        self.account__account_email = account__account_email
        self.account__display_name = account__display_name
        self.account__account_address = account__account_address
        self.account__is_verified = account__is_verified
        self.account__is_system = account__is_system
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.client_uid, self.client_name, self.tenant_uid, self.country_uid, self.client_type_uid, self.client_category_uid, self.account_uid, self.client_code, self.client_description, self.start_date, self.end_date, self.is_internal, self.is_system, self.is_test, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes, self.tenant__tenant_name, self.tenant__country_uid, self.tenant__tenant_type_uid, self.tenant__tenant_category_uid, self.tenant__tenant_code, self.tenant__tenant_description, self.tenant__start_date, self.tenant__end_date, self.tenant__is_internal, self.tenant__is_system, self.tenant__is_test, self.tenant__account_uid, self.country__country_name, self.country__continent_name, self.country__continent_code, self.country__country_iso3, self.country__country_code, self.country__phone_code, self.country__currency_code, self.country__capital_name, self.country__region_name, self.country__subregion_name, self.country__region_code, self.country__latitude, self.country__longitude, self.country__currency_name, self.country__population, self.country__languages, self.country__area, self.country__bar_code, self.country__top_level_domain, self.country__is_focused, self.client_type__client_type_name, self.client_type__client_type_description, self.account__account_name, self.account__tenant_uid, self.account__account_type_uid, self.account__account_title_uid, self.account__account_division_uid, self.account__account_group_uid, self.account__auth_identity_uid, self.account__account_email, self.account__display_name, self.account__account_address, self.account__is_verified, self.account__is_system]


@dataclass(frozen=False)
class client_account_rich_dto(client_account_read_dto):
    client_account_uid: str | None
    client_account_name: str | None
    tenant_uid: str | None
    client_uid: str | None
    account_uid: str | None
    client_role_uid: str | None
    role_comment: str | None
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
    client_account__account_name: str | None
    client_account__tenant_uid: str | None
    client_account__account_type_uid: str | None
    client_account__account_title_uid: str | None
    client_account__account_division_uid: str | None
    client_account__account_group_uid: str | None
    client_account__auth_identity_uid: str | None
    client_account__account_email: str | None
    client_account__display_name: str | None
    client_account__account_address: str | None
    client_account__is_verified: int | None
    client_account__is_system: int | None
    tenant__tenant_name: str | None
    tenant__country_uid: str | None
    tenant__tenant_type_uid: str | None
    tenant__tenant_category_uid: str | None
    tenant__tenant_code: str | None
    tenant__tenant_description: str | None
    tenant__start_date: datetime.datetime | None
    tenant__end_date: datetime.datetime | None
    tenant__is_internal: int | None
    tenant__is_system: int | None
    tenant__is_test: int | None
    tenant__account_uid: str | None
    client__client_name: str | None
    client__tenant_uid: str | None
    client__country_uid: str | None
    client__client_type_uid: str | None
    client__client_category_uid: str | None
    client__account_uid: str | None
    client__client_code: str | None
    client__client_description: str | None
    client__start_date: datetime.datetime | None
    client__end_date: datetime.datetime | None
    client__is_internal: int | None
    client__is_system: int | None
    client__is_test: int | None
    account__account_name: str | None
    account__tenant_uid: str | None
    account__account_type_uid: str | None
    account__account_title_uid: str | None
    account__account_division_uid: str | None
    account__account_group_uid: str | None
    account__auth_identity_uid: str | None
    account__account_email: str | None
    account__display_name: str | None
    account__account_address: str | None
    account__is_verified: int | None
    account__is_system: int | None
    client_role__client_role_name: str | None
    client_role__role_description: str | None
    def __init__(self, client_account_uid: str | None, client_account_name: str | None, tenant_uid: str | None, client_uid: str | None, account_uid: str | None, client_role_uid: str | None, role_comment: str | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None, client_account__account_name: str | None, client_account__tenant_uid: str | None, client_account__account_type_uid: str | None, client_account__account_title_uid: str | None, client_account__account_division_uid: str | None, client_account__account_group_uid: str | None, client_account__auth_identity_uid: str | None, client_account__account_email: str | None, client_account__display_name: str | None, client_account__account_address: str | None, client_account__is_verified: int | None, client_account__is_system: int | None, tenant__tenant_name: str | None, tenant__country_uid: str | None, tenant__tenant_type_uid: str | None, tenant__tenant_category_uid: str | None, tenant__tenant_code: str | None, tenant__tenant_description: str | None, tenant__start_date: datetime.datetime | None, tenant__end_date: datetime.datetime | None, tenant__is_internal: int | None, tenant__is_system: int | None, tenant__is_test: int | None, tenant__account_uid: str | None, client__client_name: str | None, client__tenant_uid: str | None, client__country_uid: str | None, client__client_type_uid: str | None, client__client_category_uid: str | None, client__account_uid: str | None, client__client_code: str | None, client__client_description: str | None, client__start_date: datetime.datetime | None, client__end_date: datetime.datetime | None, client__is_internal: int | None, client__is_system: int | None, client__is_test: int | None, account__account_name: str | None, account__tenant_uid: str | None, account__account_type_uid: str | None, account__account_title_uid: str | None, account__account_division_uid: str | None, account__account_group_uid: str | None, account__auth_identity_uid: str | None, account__account_email: str | None, account__display_name: str | None, account__account_address: str | None, account__is_verified: int | None, account__is_system: int | None, client_role__client_role_name: str | None, client_role__role_description: str | None):
        self.client_account_uid = client_account_uid
        self.client_account_name = client_account_name
        self.tenant_uid = tenant_uid
        self.client_uid = client_uid
        self.account_uid = account_uid
        self.client_role_uid = client_role_uid
        self.role_comment = role_comment
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
        self.client_account__account_name = client_account__account_name
        self.client_account__tenant_uid = client_account__tenant_uid
        self.client_account__account_type_uid = client_account__account_type_uid
        self.client_account__account_title_uid = client_account__account_title_uid
        self.client_account__account_division_uid = client_account__account_division_uid
        self.client_account__account_group_uid = client_account__account_group_uid
        self.client_account__auth_identity_uid = client_account__auth_identity_uid
        self.client_account__account_email = client_account__account_email
        self.client_account__display_name = client_account__display_name
        self.client_account__account_address = client_account__account_address
        self.client_account__is_verified = client_account__is_verified
        self.client_account__is_system = client_account__is_system
        self.tenant__tenant_name = tenant__tenant_name
        self.tenant__country_uid = tenant__country_uid
        self.tenant__tenant_type_uid = tenant__tenant_type_uid
        self.tenant__tenant_category_uid = tenant__tenant_category_uid
        self.tenant__tenant_code = tenant__tenant_code
        self.tenant__tenant_description = tenant__tenant_description
        self.tenant__start_date = tenant__start_date
        self.tenant__end_date = tenant__end_date
        self.tenant__is_internal = tenant__is_internal
        self.tenant__is_system = tenant__is_system
        self.tenant__is_test = tenant__is_test
        self.tenant__account_uid = tenant__account_uid
        self.client__client_name = client__client_name
        self.client__tenant_uid = client__tenant_uid
        self.client__country_uid = client__country_uid
        self.client__client_type_uid = client__client_type_uid
        self.client__client_category_uid = client__client_category_uid
        self.client__account_uid = client__account_uid
        self.client__client_code = client__client_code
        self.client__client_description = client__client_description
        self.client__start_date = client__start_date
        self.client__end_date = client__end_date
        self.client__is_internal = client__is_internal
        self.client__is_system = client__is_system
        self.client__is_test = client__is_test
        self.account__account_name = account__account_name
        self.account__tenant_uid = account__tenant_uid
        self.account__account_type_uid = account__account_type_uid
        self.account__account_title_uid = account__account_title_uid
        self.account__account_division_uid = account__account_division_uid
        self.account__account_group_uid = account__account_group_uid
        self.account__auth_identity_uid = account__auth_identity_uid
        self.account__account_email = account__account_email
        self.account__display_name = account__display_name
        self.account__account_address = account__account_address
        self.account__is_verified = account__is_verified
        self.account__is_system = account__is_system
        self.client_role__client_role_name = client_role__client_role_name
        self.client_role__role_description = client_role__role_description
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.client_account_uid, self.client_account_name, self.tenant_uid, self.client_uid, self.account_uid, self.client_role_uid, self.role_comment, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes, self.client_account__account_name, self.client_account__tenant_uid, self.client_account__account_type_uid, self.client_account__account_title_uid, self.client_account__account_division_uid, self.client_account__account_group_uid, self.client_account__auth_identity_uid, self.client_account__account_email, self.client_account__display_name, self.client_account__account_address, self.client_account__is_verified, self.client_account__is_system, self.tenant__tenant_name, self.tenant__country_uid, self.tenant__tenant_type_uid, self.tenant__tenant_category_uid, self.tenant__tenant_code, self.tenant__tenant_description, self.tenant__start_date, self.tenant__end_date, self.tenant__is_internal, self.tenant__is_system, self.tenant__is_test, self.tenant__account_uid, self.client__client_name, self.client__tenant_uid, self.client__country_uid, self.client__client_type_uid, self.client__client_category_uid, self.client__account_uid, self.client__client_code, self.client__client_description, self.client__start_date, self.client__end_date, self.client__is_internal, self.client__is_system, self.client__is_test, self.account__account_name, self.account__tenant_uid, self.account__account_type_uid, self.account__account_title_uid, self.account__account_division_uid, self.account__account_group_uid, self.account__auth_identity_uid, self.account__account_email, self.account__display_name, self.account__account_address, self.account__is_verified, self.account__is_system, self.client_role__client_role_name, self.client_role__role_description]


@dataclass(frozen=False)
class client_country_rich_dto(client_country_read_dto):
    client_country_uid: str | None
    client_country_name: str | None
    tenant_uid: str | None
    client_uid: str | None
    country_uid: str | None
    country_priority: int | None
    country_comment: str | None
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
    client_country__country_name: str | None
    client_country__continent_name: str | None
    client_country__continent_code: str | None
    client_country__country_iso3: str | None
    client_country__country_code: str | None
    client_country__phone_code: str | None
    client_country__currency_code: str | None
    client_country__capital_name: str | None
    client_country__region_name: str | None
    client_country__subregion_name: str | None
    client_country__region_code: str | None
    client_country__latitude: str | None
    client_country__longitude: str | None
    client_country__currency_name: str | None
    client_country__population: str | None
    client_country__languages: str | None
    client_country__area: str | None
    client_country__bar_code: str | None
    client_country__top_level_domain: str | None
    client_country__is_focused: int | None
    tenant__tenant_name: str | None
    tenant__country_uid: str | None
    tenant__tenant_type_uid: str | None
    tenant__tenant_category_uid: str | None
    tenant__tenant_code: str | None
    tenant__tenant_description: str | None
    tenant__start_date: datetime.datetime | None
    tenant__end_date: datetime.datetime | None
    tenant__is_internal: int | None
    tenant__is_system: int | None
    tenant__is_test: int | None
    tenant__account_uid: str | None
    client__client_name: str | None
    client__tenant_uid: str | None
    client__country_uid: str | None
    client__client_type_uid: str | None
    client__client_category_uid: str | None
    client__account_uid: str | None
    client__client_code: str | None
    client__client_description: str | None
    client__start_date: datetime.datetime | None
    client__end_date: datetime.datetime | None
    client__is_internal: int | None
    client__is_system: int | None
    client__is_test: int | None
    country__country_name: str | None
    country__continent_name: str | None
    country__continent_code: str | None
    country__country_iso3: str | None
    country__country_code: str | None
    country__phone_code: str | None
    country__currency_code: str | None
    country__capital_name: str | None
    country__region_name: str | None
    country__subregion_name: str | None
    country__region_code: str | None
    country__latitude: str | None
    country__longitude: str | None
    country__currency_name: str | None
    country__population: str | None
    country__languages: str | None
    country__area: str | None
    country__bar_code: str | None
    country__top_level_domain: str | None
    country__is_focused: int | None
    def __init__(self, client_country_uid: str | None, client_country_name: str | None, tenant_uid: str | None, client_uid: str | None, country_uid: str | None, country_priority: int | None, country_comment: str | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None, client_country__country_name: str | None, client_country__continent_name: str | None, client_country__continent_code: str | None, client_country__country_iso3: str | None, client_country__country_code: str | None, client_country__phone_code: str | None, client_country__currency_code: str | None, client_country__capital_name: str | None, client_country__region_name: str | None, client_country__subregion_name: str | None, client_country__region_code: str | None, client_country__latitude: str | None, client_country__longitude: str | None, client_country__currency_name: str | None, client_country__population: str | None, client_country__languages: str | None, client_country__area: str | None, client_country__bar_code: str | None, client_country__top_level_domain: str | None, client_country__is_focused: int | None, tenant__tenant_name: str | None, tenant__country_uid: str | None, tenant__tenant_type_uid: str | None, tenant__tenant_category_uid: str | None, tenant__tenant_code: str | None, tenant__tenant_description: str | None, tenant__start_date: datetime.datetime | None, tenant__end_date: datetime.datetime | None, tenant__is_internal: int | None, tenant__is_system: int | None, tenant__is_test: int | None, tenant__account_uid: str | None, client__client_name: str | None, client__tenant_uid: str | None, client__country_uid: str | None, client__client_type_uid: str | None, client__client_category_uid: str | None, client__account_uid: str | None, client__client_code: str | None, client__client_description: str | None, client__start_date: datetime.datetime | None, client__end_date: datetime.datetime | None, client__is_internal: int | None, client__is_system: int | None, client__is_test: int | None, country__country_name: str | None, country__continent_name: str | None, country__continent_code: str | None, country__country_iso3: str | None, country__country_code: str | None, country__phone_code: str | None, country__currency_code: str | None, country__capital_name: str | None, country__region_name: str | None, country__subregion_name: str | None, country__region_code: str | None, country__latitude: str | None, country__longitude: str | None, country__currency_name: str | None, country__population: str | None, country__languages: str | None, country__area: str | None, country__bar_code: str | None, country__top_level_domain: str | None, country__is_focused: int | None):
        self.client_country_uid = client_country_uid
        self.client_country_name = client_country_name
        self.tenant_uid = tenant_uid
        self.client_uid = client_uid
        self.country_uid = country_uid
        self.country_priority = country_priority
        self.country_comment = country_comment
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
        self.client_country__country_name = client_country__country_name
        self.client_country__continent_name = client_country__continent_name
        self.client_country__continent_code = client_country__continent_code
        self.client_country__country_iso3 = client_country__country_iso3
        self.client_country__country_code = client_country__country_code
        self.client_country__phone_code = client_country__phone_code
        self.client_country__currency_code = client_country__currency_code
        self.client_country__capital_name = client_country__capital_name
        self.client_country__region_name = client_country__region_name
        self.client_country__subregion_name = client_country__subregion_name
        self.client_country__region_code = client_country__region_code
        self.client_country__latitude = client_country__latitude
        self.client_country__longitude = client_country__longitude
        self.client_country__currency_name = client_country__currency_name
        self.client_country__population = client_country__population
        self.client_country__languages = client_country__languages
        self.client_country__area = client_country__area
        self.client_country__bar_code = client_country__bar_code
        self.client_country__top_level_domain = client_country__top_level_domain
        self.client_country__is_focused = client_country__is_focused
        self.tenant__tenant_name = tenant__tenant_name
        self.tenant__country_uid = tenant__country_uid
        self.tenant__tenant_type_uid = tenant__tenant_type_uid
        self.tenant__tenant_category_uid = tenant__tenant_category_uid
        self.tenant__tenant_code = tenant__tenant_code
        self.tenant__tenant_description = tenant__tenant_description
        self.tenant__start_date = tenant__start_date
        self.tenant__end_date = tenant__end_date
        self.tenant__is_internal = tenant__is_internal
        self.tenant__is_system = tenant__is_system
        self.tenant__is_test = tenant__is_test
        self.tenant__account_uid = tenant__account_uid
        self.client__client_name = client__client_name
        self.client__tenant_uid = client__tenant_uid
        self.client__country_uid = client__country_uid
        self.client__client_type_uid = client__client_type_uid
        self.client__client_category_uid = client__client_category_uid
        self.client__account_uid = client__account_uid
        self.client__client_code = client__client_code
        self.client__client_description = client__client_description
        self.client__start_date = client__start_date
        self.client__end_date = client__end_date
        self.client__is_internal = client__is_internal
        self.client__is_system = client__is_system
        self.client__is_test = client__is_test
        self.country__country_name = country__country_name
        self.country__continent_name = country__continent_name
        self.country__continent_code = country__continent_code
        self.country__country_iso3 = country__country_iso3
        self.country__country_code = country__country_code
        self.country__phone_code = country__phone_code
        self.country__currency_code = country__currency_code
        self.country__capital_name = country__capital_name
        self.country__region_name = country__region_name
        self.country__subregion_name = country__subregion_name
        self.country__region_code = country__region_code
        self.country__latitude = country__latitude
        self.country__longitude = country__longitude
        self.country__currency_name = country__currency_name
        self.country__population = country__population
        self.country__languages = country__languages
        self.country__area = country__area
        self.country__bar_code = country__bar_code
        self.country__top_level_domain = country__top_level_domain
        self.country__is_focused = country__is_focused
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.client_country_uid, self.client_country_name, self.tenant_uid, self.client_uid, self.country_uid, self.country_priority, self.country_comment, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes, self.client_country__country_name, self.client_country__continent_name, self.client_country__continent_code, self.client_country__country_iso3, self.client_country__country_code, self.client_country__phone_code, self.client_country__currency_code, self.client_country__capital_name, self.client_country__region_name, self.client_country__subregion_name, self.client_country__region_code, self.client_country__latitude, self.client_country__longitude, self.client_country__currency_name, self.client_country__population, self.client_country__languages, self.client_country__area, self.client_country__bar_code, self.client_country__top_level_domain, self.client_country__is_focused, self.tenant__tenant_name, self.tenant__country_uid, self.tenant__tenant_type_uid, self.tenant__tenant_category_uid, self.tenant__tenant_code, self.tenant__tenant_description, self.tenant__start_date, self.tenant__end_date, self.tenant__is_internal, self.tenant__is_system, self.tenant__is_test, self.tenant__account_uid, self.client__client_name, self.client__tenant_uid, self.client__country_uid, self.client__client_type_uid, self.client__client_category_uid, self.client__account_uid, self.client__client_code, self.client__client_description, self.client__start_date, self.client__end_date, self.client__is_internal, self.client__is_system, self.client__is_test, self.country__country_name, self.country__continent_name, self.country__continent_code, self.country__country_iso3, self.country__country_code, self.country__phone_code, self.country__currency_code, self.country__capital_name, self.country__region_name, self.country__subregion_name, self.country__region_code, self.country__latitude, self.country__longitude, self.country__currency_name, self.country__population, self.country__languages, self.country__area, self.country__bar_code, self.country__top_level_domain, self.country__is_focused]


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
    tenant__tenant_name: str | None
    tenant__country_uid: str | None
    tenant__tenant_type_uid: str | None
    tenant__tenant_category_uid: str | None
    tenant__tenant_code: str | None
    tenant__tenant_description: str | None
    tenant__start_date: datetime.datetime | None
    tenant__end_date: datetime.datetime | None
    tenant__is_internal: int | None
    tenant__is_system: int | None
    tenant__is_test: int | None
    tenant__account_uid: str | None
    client__client_name: str | None
    client__tenant_uid: str | None
    client__country_uid: str | None
    client__client_type_uid: str | None
    client__client_category_uid: str | None
    client__account_uid: str | None
    client__client_code: str | None
    client__client_description: str | None
    client__start_date: datetime.datetime | None
    client__end_date: datetime.datetime | None
    client__is_internal: int | None
    client__is_system: int | None
    client__is_test: int | None
    account__account_name: str | None
    account__tenant_uid: str | None
    account__account_type_uid: str | None
    account__account_title_uid: str | None
    account__account_division_uid: str | None
    account__account_group_uid: str | None
    account__auth_identity_uid: str | None
    account__account_email: str | None
    account__display_name: str | None
    account__account_address: str | None
    account__is_verified: int | None
    account__is_system: int | None
    currency__currency_name: str | None
    currency__is_focused: int | None
    currency__priority: int | None
    def __init__(self, client_payment_uid: str | None, client_payment_name: str | None, tenant_uid: str | None, client_uid: str | None, account_uid: str | None, currency_uid: str | None, start_date: datetime.datetime | None, end_date: datetime.datetime | None, payment_value: str | None, payment_type: str | None, source_number: str | None, source_reference: str | None, is_approved: int | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None, tenant__tenant_name: str | None, tenant__country_uid: str | None, tenant__tenant_type_uid: str | None, tenant__tenant_category_uid: str | None, tenant__tenant_code: str | None, tenant__tenant_description: str | None, tenant__start_date: datetime.datetime | None, tenant__end_date: datetime.datetime | None, tenant__is_internal: int | None, tenant__is_system: int | None, tenant__is_test: int | None, tenant__account_uid: str | None, client__client_name: str | None, client__tenant_uid: str | None, client__country_uid: str | None, client__client_type_uid: str | None, client__client_category_uid: str | None, client__account_uid: str | None, client__client_code: str | None, client__client_description: str | None, client__start_date: datetime.datetime | None, client__end_date: datetime.datetime | None, client__is_internal: int | None, client__is_system: int | None, client__is_test: int | None, account__account_name: str | None, account__tenant_uid: str | None, account__account_type_uid: str | None, account__account_title_uid: str | None, account__account_division_uid: str | None, account__account_group_uid: str | None, account__auth_identity_uid: str | None, account__account_email: str | None, account__display_name: str | None, account__account_address: str | None, account__is_verified: int | None, account__is_system: int | None, currency__currency_name: str | None, currency__is_focused: int | None, currency__priority: int | None):
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
        self.tenant__tenant_name = tenant__tenant_name
        self.tenant__country_uid = tenant__country_uid
        self.tenant__tenant_type_uid = tenant__tenant_type_uid
        self.tenant__tenant_category_uid = tenant__tenant_category_uid
        self.tenant__tenant_code = tenant__tenant_code
        self.tenant__tenant_description = tenant__tenant_description
        self.tenant__start_date = tenant__start_date
        self.tenant__end_date = tenant__end_date
        self.tenant__is_internal = tenant__is_internal
        self.tenant__is_system = tenant__is_system
        self.tenant__is_test = tenant__is_test
        self.tenant__account_uid = tenant__account_uid
        self.client__client_name = client__client_name
        self.client__tenant_uid = client__tenant_uid
        self.client__country_uid = client__country_uid
        self.client__client_type_uid = client__client_type_uid
        self.client__client_category_uid = client__client_category_uid
        self.client__account_uid = client__account_uid
        self.client__client_code = client__client_code
        self.client__client_description = client__client_description
        self.client__start_date = client__start_date
        self.client__end_date = client__end_date
        self.client__is_internal = client__is_internal
        self.client__is_system = client__is_system
        self.client__is_test = client__is_test
        self.account__account_name = account__account_name
        self.account__tenant_uid = account__tenant_uid
        self.account__account_type_uid = account__account_type_uid
        self.account__account_title_uid = account__account_title_uid
        self.account__account_division_uid = account__account_division_uid
        self.account__account_group_uid = account__account_group_uid
        self.account__auth_identity_uid = account__auth_identity_uid
        self.account__account_email = account__account_email
        self.account__display_name = account__display_name
        self.account__account_address = account__account_address
        self.account__is_verified = account__is_verified
        self.account__is_system = account__is_system
        self.currency__currency_name = currency__currency_name
        self.currency__is_focused = currency__is_focused
        self.currency__priority = currency__priority
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.client_payment_uid, self.client_payment_name, self.tenant_uid, self.client_uid, self.account_uid, self.currency_uid, self.start_date, self.end_date, self.payment_value, self.payment_type, self.source_number, self.source_reference, self.is_approved, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes, self.tenant__tenant_name, self.tenant__country_uid, self.tenant__tenant_type_uid, self.tenant__tenant_category_uid, self.tenant__tenant_code, self.tenant__tenant_description, self.tenant__start_date, self.tenant__end_date, self.tenant__is_internal, self.tenant__is_system, self.tenant__is_test, self.tenant__account_uid, self.client__client_name, self.client__tenant_uid, self.client__country_uid, self.client__client_type_uid, self.client__client_category_uid, self.client__account_uid, self.client__client_code, self.client__client_description, self.client__start_date, self.client__end_date, self.client__is_internal, self.client__is_system, self.client__is_test, self.account__account_name, self.account__tenant_uid, self.account__account_type_uid, self.account__account_title_uid, self.account__account_division_uid, self.account__account_group_uid, self.account__auth_identity_uid, self.account__account_email, self.account__display_name, self.account__account_address, self.account__is_verified, self.account__is_system, self.currency__currency_name, self.currency__is_focused, self.currency__priority]


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
    connection_engine__connection_engine_name: str | None
    connection_engine__start_date: datetime.datetime | None
    connection_engine__calls_count: int | None
    connection_engine__last_time: int | None
    connection_engine__host_count: int | None
    connection_engine__user_count: int | None
    connection_engine__token_count: int | None
    def __init__(self, connection_host_uid: str | None, connection_host_name: str | None, connection_engine_uid: str | None, host_ip: str | None, calls_count: int | None, start_time: int | None, last_call_time: int | None, user_count: int | None, token_count: int | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None, connection_engine__connection_engine_name: str | None, connection_engine__start_date: datetime.datetime | None, connection_engine__calls_count: int | None, connection_engine__last_time: int | None, connection_engine__host_count: int | None, connection_engine__user_count: int | None, connection_engine__token_count: int | None):
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
        self.connection_engine__connection_engine_name = connection_engine__connection_engine_name
        self.connection_engine__start_date = connection_engine__start_date
        self.connection_engine__calls_count = connection_engine__calls_count
        self.connection_engine__last_time = connection_engine__last_time
        self.connection_engine__host_count = connection_engine__host_count
        self.connection_engine__user_count = connection_engine__user_count
        self.connection_engine__token_count = connection_engine__token_count
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.connection_host_uid, self.connection_host_name, self.connection_engine_uid, self.host_ip, self.calls_count, self.start_time, self.last_call_time, self.user_count, self.token_count, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes, self.connection_engine__connection_engine_name, self.connection_engine__start_date, self.connection_engine__calls_count, self.connection_engine__last_time, self.connection_engine__host_count, self.connection_engine__user_count, self.connection_engine__token_count]


@dataclass(frozen=False)
class connection_tenant_rich_dto(connection_tenant_read_dto):
    connection_tenant_uid: str | None
    connection_tenant_name: str | None
    tenant_uid: str | None
    calls_count: int | None
    items_count: int | None
    request_size: int | None
    response_size: int | None
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
    connection_tenant__tenant_name: str | None
    connection_tenant__country_uid: str | None
    connection_tenant__tenant_type_uid: str | None
    connection_tenant__tenant_category_uid: str | None
    connection_tenant__tenant_code: str | None
    connection_tenant__tenant_description: str | None
    connection_tenant__start_date: datetime.datetime | None
    connection_tenant__end_date: datetime.datetime | None
    connection_tenant__is_internal: int | None
    connection_tenant__is_system: int | None
    connection_tenant__is_test: int | None
    connection_tenant__account_uid: str | None
    tenant__tenant_name: str | None
    tenant__country_uid: str | None
    tenant__tenant_type_uid: str | None
    tenant__tenant_category_uid: str | None
    tenant__tenant_code: str | None
    tenant__tenant_description: str | None
    tenant__start_date: datetime.datetime | None
    tenant__end_date: datetime.datetime | None
    tenant__is_internal: int | None
    tenant__is_system: int | None
    tenant__is_test: int | None
    tenant__account_uid: str | None
    def __init__(self, connection_tenant_uid: str | None, connection_tenant_name: str | None, tenant_uid: str | None, calls_count: int | None, items_count: int | None, request_size: int | None, response_size: int | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None, connection_tenant__tenant_name: str | None, connection_tenant__country_uid: str | None, connection_tenant__tenant_type_uid: str | None, connection_tenant__tenant_category_uid: str | None, connection_tenant__tenant_code: str | None, connection_tenant__tenant_description: str | None, connection_tenant__start_date: datetime.datetime | None, connection_tenant__end_date: datetime.datetime | None, connection_tenant__is_internal: int | None, connection_tenant__is_system: int | None, connection_tenant__is_test: int | None, connection_tenant__account_uid: str | None, tenant__tenant_name: str | None, tenant__country_uid: str | None, tenant__tenant_type_uid: str | None, tenant__tenant_category_uid: str | None, tenant__tenant_code: str | None, tenant__tenant_description: str | None, tenant__start_date: datetime.datetime | None, tenant__end_date: datetime.datetime | None, tenant__is_internal: int | None, tenant__is_system: int | None, tenant__is_test: int | None, tenant__account_uid: str | None):
        self.connection_tenant_uid = connection_tenant_uid
        self.connection_tenant_name = connection_tenant_name
        self.tenant_uid = tenant_uid
        self.calls_count = calls_count
        self.items_count = items_count
        self.request_size = request_size
        self.response_size = response_size
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
        self.connection_tenant__tenant_name = connection_tenant__tenant_name
        self.connection_tenant__country_uid = connection_tenant__country_uid
        self.connection_tenant__tenant_type_uid = connection_tenant__tenant_type_uid
        self.connection_tenant__tenant_category_uid = connection_tenant__tenant_category_uid
        self.connection_tenant__tenant_code = connection_tenant__tenant_code
        self.connection_tenant__tenant_description = connection_tenant__tenant_description
        self.connection_tenant__start_date = connection_tenant__start_date
        self.connection_tenant__end_date = connection_tenant__end_date
        self.connection_tenant__is_internal = connection_tenant__is_internal
        self.connection_tenant__is_system = connection_tenant__is_system
        self.connection_tenant__is_test = connection_tenant__is_test
        self.connection_tenant__account_uid = connection_tenant__account_uid
        self.tenant__tenant_name = tenant__tenant_name
        self.tenant__country_uid = tenant__country_uid
        self.tenant__tenant_type_uid = tenant__tenant_type_uid
        self.tenant__tenant_category_uid = tenant__tenant_category_uid
        self.tenant__tenant_code = tenant__tenant_code
        self.tenant__tenant_description = tenant__tenant_description
        self.tenant__start_date = tenant__start_date
        self.tenant__end_date = tenant__end_date
        self.tenant__is_internal = tenant__is_internal
        self.tenant__is_system = tenant__is_system
        self.tenant__is_test = tenant__is_test
        self.tenant__account_uid = tenant__account_uid
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.connection_tenant_uid, self.connection_tenant_name, self.tenant_uid, self.calls_count, self.items_count, self.request_size, self.response_size, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes, self.connection_tenant__tenant_name, self.connection_tenant__country_uid, self.connection_tenant__tenant_type_uid, self.connection_tenant__tenant_category_uid, self.connection_tenant__tenant_code, self.connection_tenant__tenant_description, self.connection_tenant__start_date, self.connection_tenant__end_date, self.connection_tenant__is_internal, self.connection_tenant__is_system, self.connection_tenant__is_test, self.connection_tenant__account_uid, self.tenant__tenant_name, self.tenant__country_uid, self.tenant__tenant_type_uid, self.tenant__tenant_category_uid, self.tenant__tenant_code, self.tenant__tenant_description, self.tenant__start_date, self.tenant__end_date, self.tenant__is_internal, self.tenant__is_system, self.tenant__is_test, self.tenant__account_uid]


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
    connection_engine__connection_engine_name: str | None
    connection_engine__start_date: datetime.datetime | None
    connection_engine__calls_count: int | None
    connection_engine__last_time: int | None
    connection_engine__host_count: int | None
    connection_engine__user_count: int | None
    connection_engine__token_count: int | None
    account__account_name: str | None
    account__tenant_uid: str | None
    account__account_type_uid: str | None
    account__account_title_uid: str | None
    account__account_division_uid: str | None
    account__account_group_uid: str | None
    account__auth_identity_uid: str | None
    account__account_email: str | None
    account__display_name: str | None
    account__account_address: str | None
    account__is_verified: int | None
    account__is_system: int | None
    def __init__(self, connection_user_uid: str | None, connection_user_name: str | None, connection_engine_uid: str | None, account_uid: str | None, call_count: int | None, host_count: int | None, token_count: int | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None, connection_engine__connection_engine_name: str | None, connection_engine__start_date: datetime.datetime | None, connection_engine__calls_count: int | None, connection_engine__last_time: int | None, connection_engine__host_count: int | None, connection_engine__user_count: int | None, connection_engine__token_count: int | None, account__account_name: str | None, account__tenant_uid: str | None, account__account_type_uid: str | None, account__account_title_uid: str | None, account__account_division_uid: str | None, account__account_group_uid: str | None, account__auth_identity_uid: str | None, account__account_email: str | None, account__display_name: str | None, account__account_address: str | None, account__is_verified: int | None, account__is_system: int | None):
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
        self.connection_engine__connection_engine_name = connection_engine__connection_engine_name
        self.connection_engine__start_date = connection_engine__start_date
        self.connection_engine__calls_count = connection_engine__calls_count
        self.connection_engine__last_time = connection_engine__last_time
        self.connection_engine__host_count = connection_engine__host_count
        self.connection_engine__user_count = connection_engine__user_count
        self.connection_engine__token_count = connection_engine__token_count
        self.account__account_name = account__account_name
        self.account__tenant_uid = account__tenant_uid
        self.account__account_type_uid = account__account_type_uid
        self.account__account_title_uid = account__account_title_uid
        self.account__account_division_uid = account__account_division_uid
        self.account__account_group_uid = account__account_group_uid
        self.account__auth_identity_uid = account__auth_identity_uid
        self.account__account_email = account__account_email
        self.account__display_name = account__display_name
        self.account__account_address = account__account_address
        self.account__is_verified = account__is_verified
        self.account__is_system = account__is_system
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.connection_user_uid, self.connection_user_name, self.connection_engine_uid, self.account_uid, self.call_count, self.host_count, self.token_count, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes, self.connection_engine__connection_engine_name, self.connection_engine__start_date, self.connection_engine__calls_count, self.connection_engine__last_time, self.connection_engine__host_count, self.connection_engine__user_count, self.connection_engine__token_count, self.account__account_name, self.account__tenant_uid, self.account__account_type_uid, self.account__account_title_uid, self.account__account_division_uid, self.account__account_group_uid, self.account__auth_identity_uid, self.account__account_email, self.account__display_name, self.account__account_address, self.account__is_verified, self.account__is_system]


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
    priority: int | None
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
    def __init__(self, currency_uid: str | None, currency_name: str | None, is_focused: int | None, priority: int | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None):
        self.currency_uid = currency_uid
        self.currency_name = currency_name
        self.is_focused = is_focused
        self.priority = priority
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
        return [self.currency_uid, self.currency_name, self.is_focused, self.priority, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]


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
    event_notification__event_notification_name: str | None
    event_notification__tenant_uid: str | None
    event_notification__account_uid: str | None
    event_notification__notification_type: str | None
    event_notification__notification_topic: str | None
    event_notification__notification_format: str | None
    event_notification__notification_content: str | None
    event_notification__sending_status: str | None
    tenant__tenant_name: str | None
    tenant__country_uid: str | None
    tenant__tenant_type_uid: str | None
    tenant__tenant_category_uid: str | None
    tenant__tenant_code: str | None
    tenant__tenant_description: str | None
    tenant__start_date: datetime.datetime | None
    tenant__end_date: datetime.datetime | None
    tenant__is_internal: int | None
    tenant__is_system: int | None
    tenant__is_test: int | None
    tenant__account_uid: str | None
    account__account_name: str | None
    account__tenant_uid: str | None
    account__account_type_uid: str | None
    account__account_title_uid: str | None
    account__account_division_uid: str | None
    account__account_group_uid: str | None
    account__auth_identity_uid: str | None
    account__account_email: str | None
    account__display_name: str | None
    account__account_address: str | None
    account__is_verified: int | None
    account__is_system: int | None
    def __init__(self, event_acknowledge_uid: str | None, event_acknowledge_name: str | None, event_notification_uid: str | None, tenant_uid: str | None, account_uid: str | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None, event_notification__event_notification_name: str | None, event_notification__tenant_uid: str | None, event_notification__account_uid: str | None, event_notification__notification_type: str | None, event_notification__notification_topic: str | None, event_notification__notification_format: str | None, event_notification__notification_content: str | None, event_notification__sending_status: str | None, tenant__tenant_name: str | None, tenant__country_uid: str | None, tenant__tenant_type_uid: str | None, tenant__tenant_category_uid: str | None, tenant__tenant_code: str | None, tenant__tenant_description: str | None, tenant__start_date: datetime.datetime | None, tenant__end_date: datetime.datetime | None, tenant__is_internal: int | None, tenant__is_system: int | None, tenant__is_test: int | None, tenant__account_uid: str | None, account__account_name: str | None, account__tenant_uid: str | None, account__account_type_uid: str | None, account__account_title_uid: str | None, account__account_division_uid: str | None, account__account_group_uid: str | None, account__auth_identity_uid: str | None, account__account_email: str | None, account__display_name: str | None, account__account_address: str | None, account__is_verified: int | None, account__is_system: int | None):
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
        self.event_notification__event_notification_name = event_notification__event_notification_name
        self.event_notification__tenant_uid = event_notification__tenant_uid
        self.event_notification__account_uid = event_notification__account_uid
        self.event_notification__notification_type = event_notification__notification_type
        self.event_notification__notification_topic = event_notification__notification_topic
        self.event_notification__notification_format = event_notification__notification_format
        self.event_notification__notification_content = event_notification__notification_content
        self.event_notification__sending_status = event_notification__sending_status
        self.tenant__tenant_name = tenant__tenant_name
        self.tenant__country_uid = tenant__country_uid
        self.tenant__tenant_type_uid = tenant__tenant_type_uid
        self.tenant__tenant_category_uid = tenant__tenant_category_uid
        self.tenant__tenant_code = tenant__tenant_code
        self.tenant__tenant_description = tenant__tenant_description
        self.tenant__start_date = tenant__start_date
        self.tenant__end_date = tenant__end_date
        self.tenant__is_internal = tenant__is_internal
        self.tenant__is_system = tenant__is_system
        self.tenant__is_test = tenant__is_test
        self.tenant__account_uid = tenant__account_uid
        self.account__account_name = account__account_name
        self.account__tenant_uid = account__tenant_uid
        self.account__account_type_uid = account__account_type_uid
        self.account__account_title_uid = account__account_title_uid
        self.account__account_division_uid = account__account_division_uid
        self.account__account_group_uid = account__account_group_uid
        self.account__auth_identity_uid = account__auth_identity_uid
        self.account__account_email = account__account_email
        self.account__display_name = account__display_name
        self.account__account_address = account__account_address
        self.account__is_verified = account__is_verified
        self.account__is_system = account__is_system
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.event_acknowledge_uid, self.event_acknowledge_name, self.event_notification_uid, self.tenant_uid, self.account_uid, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes, self.event_notification__event_notification_name, self.event_notification__tenant_uid, self.event_notification__account_uid, self.event_notification__notification_type, self.event_notification__notification_topic, self.event_notification__notification_format, self.event_notification__notification_content, self.event_notification__sending_status, self.tenant__tenant_name, self.tenant__country_uid, self.tenant__tenant_type_uid, self.tenant__tenant_category_uid, self.tenant__tenant_code, self.tenant__tenant_description, self.tenant__start_date, self.tenant__end_date, self.tenant__is_internal, self.tenant__is_system, self.tenant__is_test, self.tenant__account_uid, self.account__account_name, self.account__tenant_uid, self.account__account_type_uid, self.account__account_title_uid, self.account__account_division_uid, self.account__account_group_uid, self.account__auth_identity_uid, self.account__account_email, self.account__display_name, self.account__account_address, self.account__is_verified, self.account__is_system]


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
    event_channel_type__event_channel_type_name: str | None
    event_channel_type__channel_type_description: str | None
    tenant__tenant_name: str | None
    tenant__country_uid: str | None
    tenant__tenant_type_uid: str | None
    tenant__tenant_category_uid: str | None
    tenant__tenant_code: str | None
    tenant__tenant_description: str | None
    tenant__start_date: datetime.datetime | None
    tenant__end_date: datetime.datetime | None
    tenant__is_internal: int | None
    tenant__is_system: int | None
    tenant__is_test: int | None
    tenant__account_uid: str | None
    account__account_name: str | None
    account__tenant_uid: str | None
    account__account_type_uid: str | None
    account__account_title_uid: str | None
    account__account_division_uid: str | None
    account__account_group_uid: str | None
    account__auth_identity_uid: str | None
    account__account_email: str | None
    account__display_name: str | None
    account__account_address: str | None
    account__is_verified: int | None
    account__is_system: int | None
    def __init__(self, event_channel_uid: str | None, event_channel_name: str | None, event_channel_type_uid: str | None, channel_definition: str | None, last_status_name: str | None, tenant_uid: str | None, account_uid: str | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None, event_channel_type__event_channel_type_name: str | None, event_channel_type__channel_type_description: str | None, tenant__tenant_name: str | None, tenant__country_uid: str | None, tenant__tenant_type_uid: str | None, tenant__tenant_category_uid: str | None, tenant__tenant_code: str | None, tenant__tenant_description: str | None, tenant__start_date: datetime.datetime | None, tenant__end_date: datetime.datetime | None, tenant__is_internal: int | None, tenant__is_system: int | None, tenant__is_test: int | None, tenant__account_uid: str | None, account__account_name: str | None, account__tenant_uid: str | None, account__account_type_uid: str | None, account__account_title_uid: str | None, account__account_division_uid: str | None, account__account_group_uid: str | None, account__auth_identity_uid: str | None, account__account_email: str | None, account__display_name: str | None, account__account_address: str | None, account__is_verified: int | None, account__is_system: int | None):
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
        self.event_channel_type__event_channel_type_name = event_channel_type__event_channel_type_name
        self.event_channel_type__channel_type_description = event_channel_type__channel_type_description
        self.tenant__tenant_name = tenant__tenant_name
        self.tenant__country_uid = tenant__country_uid
        self.tenant__tenant_type_uid = tenant__tenant_type_uid
        self.tenant__tenant_category_uid = tenant__tenant_category_uid
        self.tenant__tenant_code = tenant__tenant_code
        self.tenant__tenant_description = tenant__tenant_description
        self.tenant__start_date = tenant__start_date
        self.tenant__end_date = tenant__end_date
        self.tenant__is_internal = tenant__is_internal
        self.tenant__is_system = tenant__is_system
        self.tenant__is_test = tenant__is_test
        self.tenant__account_uid = tenant__account_uid
        self.account__account_name = account__account_name
        self.account__tenant_uid = account__tenant_uid
        self.account__account_type_uid = account__account_type_uid
        self.account__account_title_uid = account__account_title_uid
        self.account__account_division_uid = account__account_division_uid
        self.account__account_group_uid = account__account_group_uid
        self.account__auth_identity_uid = account__auth_identity_uid
        self.account__account_email = account__account_email
        self.account__display_name = account__display_name
        self.account__account_address = account__account_address
        self.account__is_verified = account__is_verified
        self.account__is_system = account__is_system
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.event_channel_uid, self.event_channel_name, self.event_channel_type_uid, self.channel_definition, self.last_status_name, self.tenant_uid, self.account_uid, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes, self.event_channel_type__event_channel_type_name, self.event_channel_type__channel_type_description, self.tenant__tenant_name, self.tenant__country_uid, self.tenant__tenant_type_uid, self.tenant__tenant_category_uid, self.tenant__tenant_code, self.tenant__tenant_description, self.tenant__start_date, self.tenant__end_date, self.tenant__is_internal, self.tenant__is_system, self.tenant__is_test, self.tenant__account_uid, self.account__account_name, self.account__tenant_uid, self.account__account_type_uid, self.account__account_title_uid, self.account__account_division_uid, self.account__account_group_uid, self.account__auth_identity_uid, self.account__account_email, self.account__display_name, self.account__account_address, self.account__is_verified, self.account__is_system]


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
    tenant_uid: str | None
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
    tenant__tenant_name: str | None
    tenant__country_uid: str | None
    tenant__tenant_type_uid: str | None
    tenant__tenant_category_uid: str | None
    tenant__tenant_code: str | None
    tenant__tenant_description: str | None
    tenant__start_date: datetime.datetime | None
    tenant__end_date: datetime.datetime | None
    tenant__is_internal: int | None
    tenant__is_system: int | None
    tenant__is_test: int | None
    tenant__account_uid: str | None
    def __init__(self, event_instance_uid: str | None, event_instance_name: str | None, tenant_uid: str | None, event_type: str | None, event_object: str | None, event_method: str | None, event_parameters: str | None, event_signature: str | None, event_date: datetime.datetime | None, published_count: int | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None, tenant__tenant_name: str | None, tenant__country_uid: str | None, tenant__tenant_type_uid: str | None, tenant__tenant_category_uid: str | None, tenant__tenant_code: str | None, tenant__tenant_description: str | None, tenant__start_date: datetime.datetime | None, tenant__end_date: datetime.datetime | None, tenant__is_internal: int | None, tenant__is_system: int | None, tenant__is_test: int | None, tenant__account_uid: str | None):
        self.event_instance_uid = event_instance_uid
        self.event_instance_name = event_instance_name
        self.tenant_uid = tenant_uid
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
        self.tenant__tenant_name = tenant__tenant_name
        self.tenant__country_uid = tenant__country_uid
        self.tenant__tenant_type_uid = tenant__tenant_type_uid
        self.tenant__tenant_category_uid = tenant__tenant_category_uid
        self.tenant__tenant_code = tenant__tenant_code
        self.tenant__tenant_description = tenant__tenant_description
        self.tenant__start_date = tenant__start_date
        self.tenant__end_date = tenant__end_date
        self.tenant__is_internal = tenant__is_internal
        self.tenant__is_system = tenant__is_system
        self.tenant__is_test = tenant__is_test
        self.tenant__account_uid = tenant__account_uid
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.event_instance_uid, self.event_instance_name, self.tenant_uid, self.event_type, self.event_object, self.event_method, self.event_parameters, self.event_signature, self.event_date, self.published_count, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes, self.tenant__tenant_name, self.tenant__country_uid, self.tenant__tenant_type_uid, self.tenant__tenant_category_uid, self.tenant__tenant_code, self.tenant__tenant_description, self.tenant__start_date, self.tenant__end_date, self.tenant__is_internal, self.tenant__is_system, self.tenant__is_test, self.tenant__account_uid]


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
    tenant__tenant_name: str | None
    tenant__country_uid: str | None
    tenant__tenant_type_uid: str | None
    tenant__tenant_category_uid: str | None
    tenant__tenant_code: str | None
    tenant__tenant_description: str | None
    tenant__start_date: datetime.datetime | None
    tenant__end_date: datetime.datetime | None
    tenant__is_internal: int | None
    tenant__is_system: int | None
    tenant__is_test: int | None
    tenant__account_uid: str | None
    account__account_name: str | None
    account__tenant_uid: str | None
    account__account_type_uid: str | None
    account__account_title_uid: str | None
    account__account_division_uid: str | None
    account__account_group_uid: str | None
    account__auth_identity_uid: str | None
    account__account_email: str | None
    account__display_name: str | None
    account__account_address: str | None
    account__is_verified: int | None
    account__is_system: int | None
    def __init__(self, event_notification_uid: str | None, event_notification_name: str | None, tenant_uid: str | None, account_uid: str | None, notification_type: str | None, notification_topic: str | None, notification_format: str | None, notification_content: str | None, sending_status: str | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None, tenant__tenant_name: str | None, tenant__country_uid: str | None, tenant__tenant_type_uid: str | None, tenant__tenant_category_uid: str | None, tenant__tenant_code: str | None, tenant__tenant_description: str | None, tenant__start_date: datetime.datetime | None, tenant__end_date: datetime.datetime | None, tenant__is_internal: int | None, tenant__is_system: int | None, tenant__is_test: int | None, tenant__account_uid: str | None, account__account_name: str | None, account__tenant_uid: str | None, account__account_type_uid: str | None, account__account_title_uid: str | None, account__account_division_uid: str | None, account__account_group_uid: str | None, account__auth_identity_uid: str | None, account__account_email: str | None, account__display_name: str | None, account__account_address: str | None, account__is_verified: int | None, account__is_system: int | None):
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
        self.tenant__tenant_name = tenant__tenant_name
        self.tenant__country_uid = tenant__country_uid
        self.tenant__tenant_type_uid = tenant__tenant_type_uid
        self.tenant__tenant_category_uid = tenant__tenant_category_uid
        self.tenant__tenant_code = tenant__tenant_code
        self.tenant__tenant_description = tenant__tenant_description
        self.tenant__start_date = tenant__start_date
        self.tenant__end_date = tenant__end_date
        self.tenant__is_internal = tenant__is_internal
        self.tenant__is_system = tenant__is_system
        self.tenant__is_test = tenant__is_test
        self.tenant__account_uid = tenant__account_uid
        self.account__account_name = account__account_name
        self.account__tenant_uid = account__tenant_uid
        self.account__account_type_uid = account__account_type_uid
        self.account__account_title_uid = account__account_title_uid
        self.account__account_division_uid = account__account_division_uid
        self.account__account_group_uid = account__account_group_uid
        self.account__auth_identity_uid = account__auth_identity_uid
        self.account__account_email = account__account_email
        self.account__display_name = account__display_name
        self.account__account_address = account__account_address
        self.account__is_verified = account__is_verified
        self.account__is_system = account__is_system
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.event_notification_uid, self.event_notification_name, self.tenant_uid, self.account_uid, self.notification_type, self.notification_topic, self.notification_format, self.notification_content, self.sending_status, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes, self.tenant__tenant_name, self.tenant__country_uid, self.tenant__tenant_type_uid, self.tenant__tenant_category_uid, self.tenant__tenant_code, self.tenant__tenant_description, self.tenant__start_date, self.tenant__end_date, self.tenant__is_internal, self.tenant__is_system, self.tenant__is_test, self.tenant__account_uid, self.account__account_name, self.account__tenant_uid, self.account__account_type_uid, self.account__account_title_uid, self.account__account_division_uid, self.account__account_group_uid, self.account__auth_identity_uid, self.account__account_email, self.account__display_name, self.account__account_address, self.account__is_verified, self.account__is_system]


@dataclass(frozen=False)
class event_observer_rich_dto(event_observer_read_dto):
    event_observer_uid: str | None
    event_observer_name: str | None
    event_observer_definition: str | None
    action_definition: str | None
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
    def __init__(self, event_observer_uid: str | None, event_observer_name: str | None, event_observer_definition: str | None, action_definition: str | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None):
        self.event_observer_uid = event_observer_uid
        self.event_observer_name = event_observer_name
        self.event_observer_definition = event_observer_definition
        self.action_definition = action_definition
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
        return [self.event_observer_uid, self.event_observer_name, self.event_observer_definition, self.action_definition, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]


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
    event_channel__event_channel_name: str | None
    event_channel__event_channel_type_uid: str | None
    event_channel__channel_definition: str | None
    event_channel__last_status_name: str | None
    event_channel__tenant_uid: str | None
    event_channel__account_uid: str | None
    tenant__tenant_name: str | None
    tenant__country_uid: str | None
    tenant__tenant_type_uid: str | None
    tenant__tenant_category_uid: str | None
    tenant__tenant_code: str | None
    tenant__tenant_description: str | None
    tenant__start_date: datetime.datetime | None
    tenant__end_date: datetime.datetime | None
    tenant__is_internal: int | None
    tenant__is_system: int | None
    tenant__is_test: int | None
    tenant__account_uid: str | None
    account__account_name: str | None
    account__tenant_uid: str | None
    account__account_type_uid: str | None
    account__account_title_uid: str | None
    account__account_division_uid: str | None
    account__account_group_uid: str | None
    account__auth_identity_uid: str | None
    account__account_email: str | None
    account__display_name: str | None
    account__account_address: str | None
    account__is_verified: int | None
    account__is_system: int | None
    def __init__(self, event_subscription_uid: str | None, event_subscription_name: str | None, event_channel_uid: str | None, tenant_uid: str | None, account_uid: str | None, subscription_filter: str | None, subscription_topic: str | None, subscription_template: str | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None, event_channel__event_channel_name: str | None, event_channel__event_channel_type_uid: str | None, event_channel__channel_definition: str | None, event_channel__last_status_name: str | None, event_channel__tenant_uid: str | None, event_channel__account_uid: str | None, tenant__tenant_name: str | None, tenant__country_uid: str | None, tenant__tenant_type_uid: str | None, tenant__tenant_category_uid: str | None, tenant__tenant_code: str | None, tenant__tenant_description: str | None, tenant__start_date: datetime.datetime | None, tenant__end_date: datetime.datetime | None, tenant__is_internal: int | None, tenant__is_system: int | None, tenant__is_test: int | None, tenant__account_uid: str | None, account__account_name: str | None, account__tenant_uid: str | None, account__account_type_uid: str | None, account__account_title_uid: str | None, account__account_division_uid: str | None, account__account_group_uid: str | None, account__auth_identity_uid: str | None, account__account_email: str | None, account__display_name: str | None, account__account_address: str | None, account__is_verified: int | None, account__is_system: int | None):
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
        self.event_channel__event_channel_name = event_channel__event_channel_name
        self.event_channel__event_channel_type_uid = event_channel__event_channel_type_uid
        self.event_channel__channel_definition = event_channel__channel_definition
        self.event_channel__last_status_name = event_channel__last_status_name
        self.event_channel__tenant_uid = event_channel__tenant_uid
        self.event_channel__account_uid = event_channel__account_uid
        self.tenant__tenant_name = tenant__tenant_name
        self.tenant__country_uid = tenant__country_uid
        self.tenant__tenant_type_uid = tenant__tenant_type_uid
        self.tenant__tenant_category_uid = tenant__tenant_category_uid
        self.tenant__tenant_code = tenant__tenant_code
        self.tenant__tenant_description = tenant__tenant_description
        self.tenant__start_date = tenant__start_date
        self.tenant__end_date = tenant__end_date
        self.tenant__is_internal = tenant__is_internal
        self.tenant__is_system = tenant__is_system
        self.tenant__is_test = tenant__is_test
        self.tenant__account_uid = tenant__account_uid
        self.account__account_name = account__account_name
        self.account__tenant_uid = account__tenant_uid
        self.account__account_type_uid = account__account_type_uid
        self.account__account_title_uid = account__account_title_uid
        self.account__account_division_uid = account__account_division_uid
        self.account__account_group_uid = account__account_group_uid
        self.account__auth_identity_uid = account__auth_identity_uid
        self.account__account_email = account__account_email
        self.account__display_name = account__display_name
        self.account__account_address = account__account_address
        self.account__is_verified = account__is_verified
        self.account__is_system = account__is_system
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.event_subscription_uid, self.event_subscription_name, self.event_channel_uid, self.tenant_uid, self.account_uid, self.subscription_filter, self.subscription_topic, self.subscription_template, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes, self.event_channel__event_channel_name, self.event_channel__event_channel_type_uid, self.event_channel__channel_definition, self.event_channel__last_status_name, self.event_channel__tenant_uid, self.event_channel__account_uid, self.tenant__tenant_name, self.tenant__country_uid, self.tenant__tenant_type_uid, self.tenant__tenant_category_uid, self.tenant__tenant_code, self.tenant__tenant_description, self.tenant__start_date, self.tenant__end_date, self.tenant__is_internal, self.tenant__is_system, self.tenant__is_test, self.tenant__account_uid, self.account__account_name, self.account__tenant_uid, self.account__account_type_uid, self.account__account_title_uid, self.account__account_division_uid, self.account__account_group_uid, self.account__auth_identity_uid, self.account__account_email, self.account__display_name, self.account__account_address, self.account__is_verified, self.account__is_system]


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
    tenant__tenant_name: str | None
    tenant__country_uid: str | None
    tenant__tenant_type_uid: str | None
    tenant__tenant_category_uid: str | None
    tenant__tenant_code: str | None
    tenant__tenant_description: str | None
    tenant__start_date: datetime.datetime | None
    tenant__end_date: datetime.datetime | None
    tenant__is_internal: int | None
    tenant__is_system: int | None
    tenant__is_test: int | None
    tenant__account_uid: str | None
    def __init__(self, event_template_uid: str | None, event_template_name: str | None, tenant_uid: str | None, notification_type: str | None, notification_topic: str | None, notification_format: str | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None, tenant__tenant_name: str | None, tenant__country_uid: str | None, tenant__tenant_type_uid: str | None, tenant__tenant_category_uid: str | None, tenant__tenant_code: str | None, tenant__tenant_description: str | None, tenant__start_date: datetime.datetime | None, tenant__end_date: datetime.datetime | None, tenant__is_internal: int | None, tenant__is_system: int | None, tenant__is_test: int | None, tenant__account_uid: str | None):
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
        self.tenant__tenant_name = tenant__tenant_name
        self.tenant__country_uid = tenant__country_uid
        self.tenant__tenant_type_uid = tenant__tenant_type_uid
        self.tenant__tenant_category_uid = tenant__tenant_category_uid
        self.tenant__tenant_code = tenant__tenant_code
        self.tenant__tenant_description = tenant__tenant_description
        self.tenant__start_date = tenant__start_date
        self.tenant__end_date = tenant__end_date
        self.tenant__is_internal = tenant__is_internal
        self.tenant__is_system = tenant__is_system
        self.tenant__is_test = tenant__is_test
        self.tenant__account_uid = tenant__account_uid
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.event_template_uid, self.event_template_name, self.tenant_uid, self.notification_type, self.notification_topic, self.notification_format, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes, self.tenant__tenant_name, self.tenant__country_uid, self.tenant__tenant_type_uid, self.tenant__tenant_category_uid, self.tenant__tenant_code, self.tenant__tenant_description, self.tenant__start_date, self.tenant__end_date, self.tenant__is_internal, self.tenant__is_system, self.tenant__is_test, self.tenant__account_uid]


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
    tenant__tenant_name: str | None
    tenant__country_uid: str | None
    tenant__tenant_type_uid: str | None
    tenant__tenant_category_uid: str | None
    tenant__tenant_code: str | None
    tenant__tenant_description: str | None
    tenant__start_date: datetime.datetime | None
    tenant__end_date: datetime.datetime | None
    tenant__is_internal: int | None
    tenant__is_system: int | None
    tenant__is_test: int | None
    tenant__account_uid: str | None
    account__account_name: str | None
    account__tenant_uid: str | None
    account__account_type_uid: str | None
    account__account_title_uid: str | None
    account__account_division_uid: str | None
    account__account_group_uid: str | None
    account__auth_identity_uid: str | None
    account__account_email: str | None
    account__display_name: str | None
    account__account_address: str | None
    account__is_verified: int | None
    account__is_system: int | None
    invoice_instance__invoice_instance_name: str | None
    invoice_instance__tenant_uid: str | None
    invoice_instance__account_uid: str | None
    invoice_instance__invoice_flow_uid: str | None
    invoice_instance__invoice_status_uid: str | None
    invoice_instance__invoice_category_uid: str | None
    invoice_instance__invoice_type_uid: str | None
    invoice_instance__period_uid: str | None
    invoice_instance__currency_uid: str | None
    invoice_instance__invoice_number: str | None
    invoice_instance__invoice_details: str | None
    invoice_instance__invoice_amount_net: str | None
    invoice_instance__invoice_amount_tax: str | None
    invoice_instance__invoice_amount_gross: str | None
    invoice_action_type__invoice_action_type_name: str | None
    def __init__(self, invoice_action_uid: str | None, invoice_action_name: str | None, tenant_uid: str | None, account_uid: str | None, invoice_instance_uid: str | None, invoice_action_type_uid: str | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None, tenant__tenant_name: str | None, tenant__country_uid: str | None, tenant__tenant_type_uid: str | None, tenant__tenant_category_uid: str | None, tenant__tenant_code: str | None, tenant__tenant_description: str | None, tenant__start_date: datetime.datetime | None, tenant__end_date: datetime.datetime | None, tenant__is_internal: int | None, tenant__is_system: int | None, tenant__is_test: int | None, tenant__account_uid: str | None, account__account_name: str | None, account__tenant_uid: str | None, account__account_type_uid: str | None, account__account_title_uid: str | None, account__account_division_uid: str | None, account__account_group_uid: str | None, account__auth_identity_uid: str | None, account__account_email: str | None, account__display_name: str | None, account__account_address: str | None, account__is_verified: int | None, account__is_system: int | None, invoice_instance__invoice_instance_name: str | None, invoice_instance__tenant_uid: str | None, invoice_instance__account_uid: str | None, invoice_instance__invoice_flow_uid: str | None, invoice_instance__invoice_status_uid: str | None, invoice_instance__invoice_category_uid: str | None, invoice_instance__invoice_type_uid: str | None, invoice_instance__period_uid: str | None, invoice_instance__currency_uid: str | None, invoice_instance__invoice_number: str | None, invoice_instance__invoice_details: str | None, invoice_instance__invoice_amount_net: str | None, invoice_instance__invoice_amount_tax: str | None, invoice_instance__invoice_amount_gross: str | None, invoice_action_type__invoice_action_type_name: str | None):
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
        self.tenant__tenant_name = tenant__tenant_name
        self.tenant__country_uid = tenant__country_uid
        self.tenant__tenant_type_uid = tenant__tenant_type_uid
        self.tenant__tenant_category_uid = tenant__tenant_category_uid
        self.tenant__tenant_code = tenant__tenant_code
        self.tenant__tenant_description = tenant__tenant_description
        self.tenant__start_date = tenant__start_date
        self.tenant__end_date = tenant__end_date
        self.tenant__is_internal = tenant__is_internal
        self.tenant__is_system = tenant__is_system
        self.tenant__is_test = tenant__is_test
        self.tenant__account_uid = tenant__account_uid
        self.account__account_name = account__account_name
        self.account__tenant_uid = account__tenant_uid
        self.account__account_type_uid = account__account_type_uid
        self.account__account_title_uid = account__account_title_uid
        self.account__account_division_uid = account__account_division_uid
        self.account__account_group_uid = account__account_group_uid
        self.account__auth_identity_uid = account__auth_identity_uid
        self.account__account_email = account__account_email
        self.account__display_name = account__display_name
        self.account__account_address = account__account_address
        self.account__is_verified = account__is_verified
        self.account__is_system = account__is_system
        self.invoice_instance__invoice_instance_name = invoice_instance__invoice_instance_name
        self.invoice_instance__tenant_uid = invoice_instance__tenant_uid
        self.invoice_instance__account_uid = invoice_instance__account_uid
        self.invoice_instance__invoice_flow_uid = invoice_instance__invoice_flow_uid
        self.invoice_instance__invoice_status_uid = invoice_instance__invoice_status_uid
        self.invoice_instance__invoice_category_uid = invoice_instance__invoice_category_uid
        self.invoice_instance__invoice_type_uid = invoice_instance__invoice_type_uid
        self.invoice_instance__period_uid = invoice_instance__period_uid
        self.invoice_instance__currency_uid = invoice_instance__currency_uid
        self.invoice_instance__invoice_number = invoice_instance__invoice_number
        self.invoice_instance__invoice_details = invoice_instance__invoice_details
        self.invoice_instance__invoice_amount_net = invoice_instance__invoice_amount_net
        self.invoice_instance__invoice_amount_tax = invoice_instance__invoice_amount_tax
        self.invoice_instance__invoice_amount_gross = invoice_instance__invoice_amount_gross
        self.invoice_action_type__invoice_action_type_name = invoice_action_type__invoice_action_type_name
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.invoice_action_uid, self.invoice_action_name, self.tenant_uid, self.account_uid, self.invoice_instance_uid, self.invoice_action_type_uid, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes, self.tenant__tenant_name, self.tenant__country_uid, self.tenant__tenant_type_uid, self.tenant__tenant_category_uid, self.tenant__tenant_code, self.tenant__tenant_description, self.tenant__start_date, self.tenant__end_date, self.tenant__is_internal, self.tenant__is_system, self.tenant__is_test, self.tenant__account_uid, self.account__account_name, self.account__tenant_uid, self.account__account_type_uid, self.account__account_title_uid, self.account__account_division_uid, self.account__account_group_uid, self.account__auth_identity_uid, self.account__account_email, self.account__display_name, self.account__account_address, self.account__is_verified, self.account__is_system, self.invoice_instance__invoice_instance_name, self.invoice_instance__tenant_uid, self.invoice_instance__account_uid, self.invoice_instance__invoice_flow_uid, self.invoice_instance__invoice_status_uid, self.invoice_instance__invoice_category_uid, self.invoice_instance__invoice_type_uid, self.invoice_instance__period_uid, self.invoice_instance__currency_uid, self.invoice_instance__invoice_number, self.invoice_instance__invoice_details, self.invoice_instance__invoice_amount_net, self.invoice_instance__invoice_amount_tax, self.invoice_instance__invoice_amount_gross, self.invoice_action_type__invoice_action_type_name]


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
    tenant__tenant_name: str | None
    tenant__country_uid: str | None
    tenant__tenant_type_uid: str | None
    tenant__tenant_category_uid: str | None
    tenant__tenant_code: str | None
    tenant__tenant_description: str | None
    tenant__start_date: datetime.datetime | None
    tenant__end_date: datetime.datetime | None
    tenant__is_internal: int | None
    tenant__is_system: int | None
    tenant__is_test: int | None
    tenant__account_uid: str | None
    def __init__(self, invoice_category_uid: str | None, invoice_category_name: str | None, tenant_uid: str | None, invoice_category_description: str | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None, tenant__tenant_name: str | None, tenant__country_uid: str | None, tenant__tenant_type_uid: str | None, tenant__tenant_category_uid: str | None, tenant__tenant_code: str | None, tenant__tenant_description: str | None, tenant__start_date: datetime.datetime | None, tenant__end_date: datetime.datetime | None, tenant__is_internal: int | None, tenant__is_system: int | None, tenant__is_test: int | None, tenant__account_uid: str | None):
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
        self.tenant__tenant_name = tenant__tenant_name
        self.tenant__country_uid = tenant__country_uid
        self.tenant__tenant_type_uid = tenant__tenant_type_uid
        self.tenant__tenant_category_uid = tenant__tenant_category_uid
        self.tenant__tenant_code = tenant__tenant_code
        self.tenant__tenant_description = tenant__tenant_description
        self.tenant__start_date = tenant__start_date
        self.tenant__end_date = tenant__end_date
        self.tenant__is_internal = tenant__is_internal
        self.tenant__is_system = tenant__is_system
        self.tenant__is_test = tenant__is_test
        self.tenant__account_uid = tenant__account_uid
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.invoice_category_uid, self.invoice_category_name, self.tenant_uid, self.invoice_category_description, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes, self.tenant__tenant_name, self.tenant__country_uid, self.tenant__tenant_type_uid, self.tenant__tenant_category_uid, self.tenant__tenant_code, self.tenant__tenant_description, self.tenant__start_date, self.tenant__end_date, self.tenant__is_internal, self.tenant__is_system, self.tenant__is_test, self.tenant__account_uid]


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
    tenant__tenant_name: str | None
    tenant__country_uid: str | None
    tenant__tenant_type_uid: str | None
    tenant__tenant_category_uid: str | None
    tenant__tenant_code: str | None
    tenant__tenant_description: str | None
    tenant__start_date: datetime.datetime | None
    tenant__end_date: datetime.datetime | None
    tenant__is_internal: int | None
    tenant__is_system: int | None
    tenant__is_test: int | None
    tenant__account_uid: str | None
    account__account_name: str | None
    account__tenant_uid: str | None
    account__account_type_uid: str | None
    account__account_title_uid: str | None
    account__account_division_uid: str | None
    account__account_group_uid: str | None
    account__auth_identity_uid: str | None
    account__account_email: str | None
    account__display_name: str | None
    account__account_address: str | None
    account__is_verified: int | None
    account__is_system: int | None
    invoice_instance__invoice_instance_name: str | None
    invoice_instance__tenant_uid: str | None
    invoice_instance__account_uid: str | None
    invoice_instance__invoice_flow_uid: str | None
    invoice_instance__invoice_status_uid: str | None
    invoice_instance__invoice_category_uid: str | None
    invoice_instance__invoice_type_uid: str | None
    invoice_instance__period_uid: str | None
    invoice_instance__currency_uid: str | None
    invoice_instance__invoice_number: str | None
    invoice_instance__invoice_details: str | None
    invoice_instance__invoice_amount_net: str | None
    invoice_instance__invoice_amount_tax: str | None
    invoice_instance__invoice_amount_gross: str | None
    def __init__(self, invoice_entry_uid: str | None, invoice_entry_name: str | None, tenant_uid: str | None, account_uid: str | None, invoice_instance_uid: str | None, entry_details: str | None, entry_amount_net: str | None, entry_amount_tax: str | None, entry_amount_gross: str | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None, tenant__tenant_name: str | None, tenant__country_uid: str | None, tenant__tenant_type_uid: str | None, tenant__tenant_category_uid: str | None, tenant__tenant_code: str | None, tenant__tenant_description: str | None, tenant__start_date: datetime.datetime | None, tenant__end_date: datetime.datetime | None, tenant__is_internal: int | None, tenant__is_system: int | None, tenant__is_test: int | None, tenant__account_uid: str | None, account__account_name: str | None, account__tenant_uid: str | None, account__account_type_uid: str | None, account__account_title_uid: str | None, account__account_division_uid: str | None, account__account_group_uid: str | None, account__auth_identity_uid: str | None, account__account_email: str | None, account__display_name: str | None, account__account_address: str | None, account__is_verified: int | None, account__is_system: int | None, invoice_instance__invoice_instance_name: str | None, invoice_instance__tenant_uid: str | None, invoice_instance__account_uid: str | None, invoice_instance__invoice_flow_uid: str | None, invoice_instance__invoice_status_uid: str | None, invoice_instance__invoice_category_uid: str | None, invoice_instance__invoice_type_uid: str | None, invoice_instance__period_uid: str | None, invoice_instance__currency_uid: str | None, invoice_instance__invoice_number: str | None, invoice_instance__invoice_details: str | None, invoice_instance__invoice_amount_net: str | None, invoice_instance__invoice_amount_tax: str | None, invoice_instance__invoice_amount_gross: str | None):
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
        self.tenant__tenant_name = tenant__tenant_name
        self.tenant__country_uid = tenant__country_uid
        self.tenant__tenant_type_uid = tenant__tenant_type_uid
        self.tenant__tenant_category_uid = tenant__tenant_category_uid
        self.tenant__tenant_code = tenant__tenant_code
        self.tenant__tenant_description = tenant__tenant_description
        self.tenant__start_date = tenant__start_date
        self.tenant__end_date = tenant__end_date
        self.tenant__is_internal = tenant__is_internal
        self.tenant__is_system = tenant__is_system
        self.tenant__is_test = tenant__is_test
        self.tenant__account_uid = tenant__account_uid
        self.account__account_name = account__account_name
        self.account__tenant_uid = account__tenant_uid
        self.account__account_type_uid = account__account_type_uid
        self.account__account_title_uid = account__account_title_uid
        self.account__account_division_uid = account__account_division_uid
        self.account__account_group_uid = account__account_group_uid
        self.account__auth_identity_uid = account__auth_identity_uid
        self.account__account_email = account__account_email
        self.account__display_name = account__display_name
        self.account__account_address = account__account_address
        self.account__is_verified = account__is_verified
        self.account__is_system = account__is_system
        self.invoice_instance__invoice_instance_name = invoice_instance__invoice_instance_name
        self.invoice_instance__tenant_uid = invoice_instance__tenant_uid
        self.invoice_instance__account_uid = invoice_instance__account_uid
        self.invoice_instance__invoice_flow_uid = invoice_instance__invoice_flow_uid
        self.invoice_instance__invoice_status_uid = invoice_instance__invoice_status_uid
        self.invoice_instance__invoice_category_uid = invoice_instance__invoice_category_uid
        self.invoice_instance__invoice_type_uid = invoice_instance__invoice_type_uid
        self.invoice_instance__period_uid = invoice_instance__period_uid
        self.invoice_instance__currency_uid = invoice_instance__currency_uid
        self.invoice_instance__invoice_number = invoice_instance__invoice_number
        self.invoice_instance__invoice_details = invoice_instance__invoice_details
        self.invoice_instance__invoice_amount_net = invoice_instance__invoice_amount_net
        self.invoice_instance__invoice_amount_tax = invoice_instance__invoice_amount_tax
        self.invoice_instance__invoice_amount_gross = invoice_instance__invoice_amount_gross
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.invoice_entry_uid, self.invoice_entry_name, self.tenant_uid, self.account_uid, self.invoice_instance_uid, self.entry_details, self.entry_amount_net, self.entry_amount_tax, self.entry_amount_gross, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes, self.tenant__tenant_name, self.tenant__country_uid, self.tenant__tenant_type_uid, self.tenant__tenant_category_uid, self.tenant__tenant_code, self.tenant__tenant_description, self.tenant__start_date, self.tenant__end_date, self.tenant__is_internal, self.tenant__is_system, self.tenant__is_test, self.tenant__account_uid, self.account__account_name, self.account__tenant_uid, self.account__account_type_uid, self.account__account_title_uid, self.account__account_division_uid, self.account__account_group_uid, self.account__auth_identity_uid, self.account__account_email, self.account__display_name, self.account__account_address, self.account__is_verified, self.account__is_system, self.invoice_instance__invoice_instance_name, self.invoice_instance__tenant_uid, self.invoice_instance__account_uid, self.invoice_instance__invoice_flow_uid, self.invoice_instance__invoice_status_uid, self.invoice_instance__invoice_category_uid, self.invoice_instance__invoice_type_uid, self.invoice_instance__period_uid, self.invoice_instance__currency_uid, self.invoice_instance__invoice_number, self.invoice_instance__invoice_details, self.invoice_instance__invoice_amount_net, self.invoice_instance__invoice_amount_tax, self.invoice_instance__invoice_amount_gross]


@dataclass(frozen=False)
class invoice_flow_rich_dto(invoice_flow_read_dto):
    invoice_flow_uid: str | None
    invoice_flow_name: str | None
    class_name: str | None
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
    def __init__(self, invoice_flow_uid: str | None, invoice_flow_name: str | None, class_name: str | None, flow_description: str | None, flow_definition_json: str | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None):
        self.invoice_flow_uid = invoice_flow_uid
        self.invoice_flow_name = invoice_flow_name
        self.class_name = class_name
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
        return [self.invoice_flow_uid, self.invoice_flow_name, self.class_name, self.flow_description, self.flow_definition_json, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]


@dataclass(frozen=False)
class invoice_flow_state_rich_dto(invoice_flow_state_read_dto):
    invoice_flow_state_uid: str | None
    invoice_flow_state_name: str | None
    invoice_flow_uid: str | None
    state_definition_json: str | None
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
    invoice_flow__invoice_flow_name: str | None
    invoice_flow__class_name: str | None
    invoice_flow__flow_description: str | None
    invoice_flow__flow_definition_json: str | None
    def __init__(self, invoice_flow_state_uid: str | None, invoice_flow_state_name: str | None, invoice_flow_uid: str | None, state_definition_json: str | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None, invoice_flow__invoice_flow_name: str | None, invoice_flow__class_name: str | None, invoice_flow__flow_description: str | None, invoice_flow__flow_definition_json: str | None):
        self.invoice_flow_state_uid = invoice_flow_state_uid
        self.invoice_flow_state_name = invoice_flow_state_name
        self.invoice_flow_uid = invoice_flow_uid
        self.state_definition_json = state_definition_json
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
        self.invoice_flow__invoice_flow_name = invoice_flow__invoice_flow_name
        self.invoice_flow__class_name = invoice_flow__class_name
        self.invoice_flow__flow_description = invoice_flow__flow_description
        self.invoice_flow__flow_definition_json = invoice_flow__flow_definition_json
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.invoice_flow_state_uid, self.invoice_flow_state_name, self.invoice_flow_uid, self.state_definition_json, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes, self.invoice_flow__invoice_flow_name, self.invoice_flow__class_name, self.invoice_flow__flow_description, self.invoice_flow__flow_definition_json]


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
    tenant__tenant_name: str | None
    tenant__country_uid: str | None
    tenant__tenant_type_uid: str | None
    tenant__tenant_category_uid: str | None
    tenant__tenant_code: str | None
    tenant__tenant_description: str | None
    tenant__start_date: datetime.datetime | None
    tenant__end_date: datetime.datetime | None
    tenant__is_internal: int | None
    tenant__is_system: int | None
    tenant__is_test: int | None
    tenant__account_uid: str | None
    account__account_name: str | None
    account__tenant_uid: str | None
    account__account_type_uid: str | None
    account__account_title_uid: str | None
    account__account_division_uid: str | None
    account__account_group_uid: str | None
    account__auth_identity_uid: str | None
    account__account_email: str | None
    account__display_name: str | None
    account__account_address: str | None
    account__is_verified: int | None
    account__is_system: int | None
    invoice_flow__invoice_flow_name: str | None
    invoice_flow__class_name: str | None
    invoice_flow__flow_description: str | None
    invoice_flow__flow_definition_json: str | None
    invoice_status__invoice_status_name: str | None
    invoice_status__status_description: str | None
    invoice_category__invoice_category_name: str | None
    invoice_category__tenant_uid: str | None
    invoice_category__invoice_category_description: str | None
    invoice_type__invoice_type_name: str | None
    period__period_name: str | None
    period__period_number: int | None
    period__period_type: str | None
    period__period_start_time: datetime.datetime | None
    period__period_end_time: datetime.datetime | None
    period__period_year: int | None
    period__period_quarter: int | None
    period__period_month: int | None
    period__period_week: int | None
    period__period_day: int | None
    currency__currency_name: str | None
    currency__is_focused: int | None
    currency__priority: int | None
    def __init__(self, invoice_instance_uid: str | None, invoice_instance_name: str | None, tenant_uid: str | None, account_uid: str | None, invoice_flow_uid: str | None, invoice_status_uid: str | None, invoice_category_uid: str | None, invoice_type_uid: str | None, period_uid: str | None, currency_uid: str | None, invoice_number: str | None, invoice_details: str | None, invoice_amount_net: str | None, invoice_amount_tax: str | None, invoice_amount_gross: str | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None, tenant__tenant_name: str | None, tenant__country_uid: str | None, tenant__tenant_type_uid: str | None, tenant__tenant_category_uid: str | None, tenant__tenant_code: str | None, tenant__tenant_description: str | None, tenant__start_date: datetime.datetime | None, tenant__end_date: datetime.datetime | None, tenant__is_internal: int | None, tenant__is_system: int | None, tenant__is_test: int | None, tenant__account_uid: str | None, account__account_name: str | None, account__tenant_uid: str | None, account__account_type_uid: str | None, account__account_title_uid: str | None, account__account_division_uid: str | None, account__account_group_uid: str | None, account__auth_identity_uid: str | None, account__account_email: str | None, account__display_name: str | None, account__account_address: str | None, account__is_verified: int | None, account__is_system: int | None, invoice_flow__invoice_flow_name: str | None, invoice_flow__class_name: str | None, invoice_flow__flow_description: str | None, invoice_flow__flow_definition_json: str | None, invoice_status__invoice_status_name: str | None, invoice_status__status_description: str | None, invoice_category__invoice_category_name: str | None, invoice_category__tenant_uid: str | None, invoice_category__invoice_category_description: str | None, invoice_type__invoice_type_name: str | None, period__period_name: str | None, period__period_number: int | None, period__period_type: str | None, period__period_start_time: datetime.datetime | None, period__period_end_time: datetime.datetime | None, period__period_year: int | None, period__period_quarter: int | None, period__period_month: int | None, period__period_week: int | None, period__period_day: int | None, currency__currency_name: str | None, currency__is_focused: int | None, currency__priority: int | None):
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
        self.tenant__tenant_name = tenant__tenant_name
        self.tenant__country_uid = tenant__country_uid
        self.tenant__tenant_type_uid = tenant__tenant_type_uid
        self.tenant__tenant_category_uid = tenant__tenant_category_uid
        self.tenant__tenant_code = tenant__tenant_code
        self.tenant__tenant_description = tenant__tenant_description
        self.tenant__start_date = tenant__start_date
        self.tenant__end_date = tenant__end_date
        self.tenant__is_internal = tenant__is_internal
        self.tenant__is_system = tenant__is_system
        self.tenant__is_test = tenant__is_test
        self.tenant__account_uid = tenant__account_uid
        self.account__account_name = account__account_name
        self.account__tenant_uid = account__tenant_uid
        self.account__account_type_uid = account__account_type_uid
        self.account__account_title_uid = account__account_title_uid
        self.account__account_division_uid = account__account_division_uid
        self.account__account_group_uid = account__account_group_uid
        self.account__auth_identity_uid = account__auth_identity_uid
        self.account__account_email = account__account_email
        self.account__display_name = account__display_name
        self.account__account_address = account__account_address
        self.account__is_verified = account__is_verified
        self.account__is_system = account__is_system
        self.invoice_flow__invoice_flow_name = invoice_flow__invoice_flow_name
        self.invoice_flow__class_name = invoice_flow__class_name
        self.invoice_flow__flow_description = invoice_flow__flow_description
        self.invoice_flow__flow_definition_json = invoice_flow__flow_definition_json
        self.invoice_status__invoice_status_name = invoice_status__invoice_status_name
        self.invoice_status__status_description = invoice_status__status_description
        self.invoice_category__invoice_category_name = invoice_category__invoice_category_name
        self.invoice_category__tenant_uid = invoice_category__tenant_uid
        self.invoice_category__invoice_category_description = invoice_category__invoice_category_description
        self.invoice_type__invoice_type_name = invoice_type__invoice_type_name
        self.period__period_name = period__period_name
        self.period__period_number = period__period_number
        self.period__period_type = period__period_type
        self.period__period_start_time = period__period_start_time
        self.period__period_end_time = period__period_end_time
        self.period__period_year = period__period_year
        self.period__period_quarter = period__period_quarter
        self.period__period_month = period__period_month
        self.period__period_week = period__period_week
        self.period__period_day = period__period_day
        self.currency__currency_name = currency__currency_name
        self.currency__is_focused = currency__is_focused
        self.currency__priority = currency__priority
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.invoice_instance_uid, self.invoice_instance_name, self.tenant_uid, self.account_uid, self.invoice_flow_uid, self.invoice_status_uid, self.invoice_category_uid, self.invoice_type_uid, self.period_uid, self.currency_uid, self.invoice_number, self.invoice_details, self.invoice_amount_net, self.invoice_amount_tax, self.invoice_amount_gross, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes, self.tenant__tenant_name, self.tenant__country_uid, self.tenant__tenant_type_uid, self.tenant__tenant_category_uid, self.tenant__tenant_code, self.tenant__tenant_description, self.tenant__start_date, self.tenant__end_date, self.tenant__is_internal, self.tenant__is_system, self.tenant__is_test, self.tenant__account_uid, self.account__account_name, self.account__tenant_uid, self.account__account_type_uid, self.account__account_title_uid, self.account__account_division_uid, self.account__account_group_uid, self.account__auth_identity_uid, self.account__account_email, self.account__display_name, self.account__account_address, self.account__is_verified, self.account__is_system, self.invoice_flow__invoice_flow_name, self.invoice_flow__class_name, self.invoice_flow__flow_description, self.invoice_flow__flow_definition_json, self.invoice_status__invoice_status_name, self.invoice_status__status_description, self.invoice_category__invoice_category_name, self.invoice_category__tenant_uid, self.invoice_category__invoice_category_description, self.invoice_type__invoice_type_name, self.period__period_name, self.period__period_number, self.period__period_type, self.period__period_start_time, self.period__period_end_time, self.period__period_year, self.period__period_quarter, self.period__period_month, self.period__period_week, self.period__period_day, self.currency__currency_name, self.currency__is_focused, self.currency__priority]


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
class location_postal_code_rich_dto(location_postal_code_read_dto):
    location_postal_code_uid: str | None
    location_postal_code_name: str | None
    country_uid: str | None
    postal_code: str | None
    street_name: str | None
    city_name: str | None
    county_name: str | None
    state_name: str | None
    region_name: str | None
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
    country__country_name: str | None
    country__continent_name: str | None
    country__continent_code: str | None
    country__country_iso3: str | None
    country__country_code: str | None
    country__phone_code: str | None
    country__currency_code: str | None
    country__capital_name: str | None
    country__region_name: str | None
    country__subregion_name: str | None
    country__region_code: str | None
    country__latitude: str | None
    country__longitude: str | None
    country__currency_name: str | None
    country__population: str | None
    country__languages: str | None
    country__area: str | None
    country__bar_code: str | None
    country__top_level_domain: str | None
    country__is_focused: int | None
    def __init__(self, location_postal_code_uid: str | None, location_postal_code_name: str | None, country_uid: str | None, postal_code: str | None, street_name: str | None, city_name: str | None, county_name: str | None, state_name: str | None, region_name: str | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None, country__country_name: str | None, country__continent_name: str | None, country__continent_code: str | None, country__country_iso3: str | None, country__country_code: str | None, country__phone_code: str | None, country__currency_code: str | None, country__capital_name: str | None, country__region_name: str | None, country__subregion_name: str | None, country__region_code: str | None, country__latitude: str | None, country__longitude: str | None, country__currency_name: str | None, country__population: str | None, country__languages: str | None, country__area: str | None, country__bar_code: str | None, country__top_level_domain: str | None, country__is_focused: int | None):
        self.location_postal_code_uid = location_postal_code_uid
        self.location_postal_code_name = location_postal_code_name
        self.country_uid = country_uid
        self.postal_code = postal_code
        self.street_name = street_name
        self.city_name = city_name
        self.county_name = county_name
        self.state_name = state_name
        self.region_name = region_name
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
        self.country__country_name = country__country_name
        self.country__continent_name = country__continent_name
        self.country__continent_code = country__continent_code
        self.country__country_iso3 = country__country_iso3
        self.country__country_code = country__country_code
        self.country__phone_code = country__phone_code
        self.country__currency_code = country__currency_code
        self.country__capital_name = country__capital_name
        self.country__region_name = country__region_name
        self.country__subregion_name = country__subregion_name
        self.country__region_code = country__region_code
        self.country__latitude = country__latitude
        self.country__longitude = country__longitude
        self.country__currency_name = country__currency_name
        self.country__population = country__population
        self.country__languages = country__languages
        self.country__area = country__area
        self.country__bar_code = country__bar_code
        self.country__top_level_domain = country__top_level_domain
        self.country__is_focused = country__is_focused
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.location_postal_code_uid, self.location_postal_code_name, self.country_uid, self.postal_code, self.street_name, self.city_name, self.county_name, self.state_name, self.region_name, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes, self.country__country_name, self.country__continent_name, self.country__continent_code, self.country__country_iso3, self.country__country_code, self.country__phone_code, self.country__currency_code, self.country__capital_name, self.country__region_name, self.country__subregion_name, self.country__region_code, self.country__latitude, self.country__longitude, self.country__currency_name, self.country__population, self.country__languages, self.country__area, self.country__bar_code, self.country__top_level_domain, self.country__is_focused]


@dataclass(frozen=False)
class location_territory_rich_dto(location_territory_read_dto):
    location_territory_uid: str | None
    location_territory_name: str | None
    tenant_uid: str | None
    location_postal_code_uid: str | None
    territory_latitude: str | None
    territory_longitude: str | None
    territory_description: str | None
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
    tenant__tenant_name: str | None
    tenant__country_uid: str | None
    tenant__tenant_type_uid: str | None
    tenant__tenant_category_uid: str | None
    tenant__tenant_code: str | None
    tenant__tenant_description: str | None
    tenant__start_date: datetime.datetime | None
    tenant__end_date: datetime.datetime | None
    tenant__is_internal: int | None
    tenant__is_system: int | None
    tenant__is_test: int | None
    tenant__account_uid: str | None
    location_postal_code__location_postal_code_name: str | None
    location_postal_code__country_uid: str | None
    location_postal_code__postal_code: str | None
    location_postal_code__street_name: str | None
    location_postal_code__city_name: str | None
    location_postal_code__county_name: str | None
    location_postal_code__state_name: str | None
    location_postal_code__region_name: str | None
    def __init__(self, location_territory_uid: str | None, location_territory_name: str | None, tenant_uid: str | None, location_postal_code_uid: str | None, territory_latitude: str | None, territory_longitude: str | None, territory_description: str | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None, tenant__tenant_name: str | None, tenant__country_uid: str | None, tenant__tenant_type_uid: str | None, tenant__tenant_category_uid: str | None, tenant__tenant_code: str | None, tenant__tenant_description: str | None, tenant__start_date: datetime.datetime | None, tenant__end_date: datetime.datetime | None, tenant__is_internal: int | None, tenant__is_system: int | None, tenant__is_test: int | None, tenant__account_uid: str | None, location_postal_code__location_postal_code_name: str | None, location_postal_code__country_uid: str | None, location_postal_code__postal_code: str | None, location_postal_code__street_name: str | None, location_postal_code__city_name: str | None, location_postal_code__county_name: str | None, location_postal_code__state_name: str | None, location_postal_code__region_name: str | None):
        self.location_territory_uid = location_territory_uid
        self.location_territory_name = location_territory_name
        self.tenant_uid = tenant_uid
        self.location_postal_code_uid = location_postal_code_uid
        self.territory_latitude = territory_latitude
        self.territory_longitude = territory_longitude
        self.territory_description = territory_description
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
        self.tenant__tenant_name = tenant__tenant_name
        self.tenant__country_uid = tenant__country_uid
        self.tenant__tenant_type_uid = tenant__tenant_type_uid
        self.tenant__tenant_category_uid = tenant__tenant_category_uid
        self.tenant__tenant_code = tenant__tenant_code
        self.tenant__tenant_description = tenant__tenant_description
        self.tenant__start_date = tenant__start_date
        self.tenant__end_date = tenant__end_date
        self.tenant__is_internal = tenant__is_internal
        self.tenant__is_system = tenant__is_system
        self.tenant__is_test = tenant__is_test
        self.tenant__account_uid = tenant__account_uid
        self.location_postal_code__location_postal_code_name = location_postal_code__location_postal_code_name
        self.location_postal_code__country_uid = location_postal_code__country_uid
        self.location_postal_code__postal_code = location_postal_code__postal_code
        self.location_postal_code__street_name = location_postal_code__street_name
        self.location_postal_code__city_name = location_postal_code__city_name
        self.location_postal_code__county_name = location_postal_code__county_name
        self.location_postal_code__state_name = location_postal_code__state_name
        self.location_postal_code__region_name = location_postal_code__region_name
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.location_territory_uid, self.location_territory_name, self.tenant_uid, self.location_postal_code_uid, self.territory_latitude, self.territory_longitude, self.territory_description, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes, self.tenant__tenant_name, self.tenant__country_uid, self.tenant__tenant_type_uid, self.tenant__tenant_category_uid, self.tenant__tenant_code, self.tenant__tenant_description, self.tenant__start_date, self.tenant__end_date, self.tenant__is_internal, self.tenant__is_system, self.tenant__is_test, self.tenant__account_uid, self.location_postal_code__location_postal_code_name, self.location_postal_code__country_uid, self.location_postal_code__postal_code, self.location_postal_code__street_name, self.location_postal_code__city_name, self.location_postal_code__county_name, self.location_postal_code__state_name, self.location_postal_code__region_name]


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
    tenant__tenant_name: str | None
    tenant__country_uid: str | None
    tenant__tenant_type_uid: str | None
    tenant__tenant_category_uid: str | None
    tenant__tenant_code: str | None
    tenant__tenant_description: str | None
    tenant__start_date: datetime.datetime | None
    tenant__end_date: datetime.datetime | None
    tenant__is_internal: int | None
    tenant__is_system: int | None
    tenant__is_test: int | None
    tenant__account_uid: str | None
    account__account_name: str | None
    account__tenant_uid: str | None
    account__account_type_uid: str | None
    account__account_title_uid: str | None
    account__account_division_uid: str | None
    account__account_group_uid: str | None
    account__auth_identity_uid: str | None
    account__account_email: str | None
    account__display_name: str | None
    account__account_address: str | None
    account__is_verified: int | None
    account__is_system: int | None
    monitor_type__monitor_type_name: str | None
    monitor_type__class_name: str | None
    monitor_type__parameters_json: str | None
    def __init__(self, monitor_uid: str | None, monitor_name: str | None, tenant_uid: str | None, account_uid: str | None, monitor_type_uid: str | None, schedule_expression: str | None, monitor_protocol: str | None, monitor_url: str | None, monitor_user: str | None, monitor_priority: int | None, is_on_hold: int | None, last_status_name: str | None, last_run_time: str | None, last_exception_message: str | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None, tenant__tenant_name: str | None, tenant__country_uid: str | None, tenant__tenant_type_uid: str | None, tenant__tenant_category_uid: str | None, tenant__tenant_code: str | None, tenant__tenant_description: str | None, tenant__start_date: datetime.datetime | None, tenant__end_date: datetime.datetime | None, tenant__is_internal: int | None, tenant__is_system: int | None, tenant__is_test: int | None, tenant__account_uid: str | None, account__account_name: str | None, account__tenant_uid: str | None, account__account_type_uid: str | None, account__account_title_uid: str | None, account__account_division_uid: str | None, account__account_group_uid: str | None, account__auth_identity_uid: str | None, account__account_email: str | None, account__display_name: str | None, account__account_address: str | None, account__is_verified: int | None, account__is_system: int | None, monitor_type__monitor_type_name: str | None, monitor_type__class_name: str | None, monitor_type__parameters_json: str | None):
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
        self.tenant__tenant_name = tenant__tenant_name
        self.tenant__country_uid = tenant__country_uid
        self.tenant__tenant_type_uid = tenant__tenant_type_uid
        self.tenant__tenant_category_uid = tenant__tenant_category_uid
        self.tenant__tenant_code = tenant__tenant_code
        self.tenant__tenant_description = tenant__tenant_description
        self.tenant__start_date = tenant__start_date
        self.tenant__end_date = tenant__end_date
        self.tenant__is_internal = tenant__is_internal
        self.tenant__is_system = tenant__is_system
        self.tenant__is_test = tenant__is_test
        self.tenant__account_uid = tenant__account_uid
        self.account__account_name = account__account_name
        self.account__tenant_uid = account__tenant_uid
        self.account__account_type_uid = account__account_type_uid
        self.account__account_title_uid = account__account_title_uid
        self.account__account_division_uid = account__account_division_uid
        self.account__account_group_uid = account__account_group_uid
        self.account__auth_identity_uid = account__auth_identity_uid
        self.account__account_email = account__account_email
        self.account__display_name = account__display_name
        self.account__account_address = account__account_address
        self.account__is_verified = account__is_verified
        self.account__is_system = account__is_system
        self.monitor_type__monitor_type_name = monitor_type__monitor_type_name
        self.monitor_type__class_name = monitor_type__class_name
        self.monitor_type__parameters_json = monitor_type__parameters_json
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.monitor_uid, self.monitor_name, self.tenant_uid, self.account_uid, self.monitor_type_uid, self.schedule_expression, self.monitor_protocol, self.monitor_url, self.monitor_user, self.monitor_priority, self.is_on_hold, self.last_status_name, self.last_run_time, self.last_exception_message, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes, self.tenant__tenant_name, self.tenant__country_uid, self.tenant__tenant_type_uid, self.tenant__tenant_category_uid, self.tenant__tenant_code, self.tenant__tenant_description, self.tenant__start_date, self.tenant__end_date, self.tenant__is_internal, self.tenant__is_system, self.tenant__is_test, self.tenant__account_uid, self.account__account_name, self.account__tenant_uid, self.account__account_type_uid, self.account__account_title_uid, self.account__account_division_uid, self.account__account_group_uid, self.account__auth_identity_uid, self.account__account_email, self.account__display_name, self.account__account_address, self.account__is_verified, self.account__is_system, self.monitor_type__monitor_type_name, self.monitor_type__class_name, self.monitor_type__parameters_json]


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
    tenant__tenant_name: str | None
    tenant__country_uid: str | None
    tenant__tenant_type_uid: str | None
    tenant__tenant_category_uid: str | None
    tenant__tenant_code: str | None
    tenant__tenant_description: str | None
    tenant__start_date: datetime.datetime | None
    tenant__end_date: datetime.datetime | None
    tenant__is_internal: int | None
    tenant__is_system: int | None
    tenant__is_test: int | None
    tenant__account_uid: str | None
    account__account_name: str | None
    account__tenant_uid: str | None
    account__account_type_uid: str | None
    account__account_title_uid: str | None
    account__account_division_uid: str | None
    account__account_group_uid: str | None
    account__auth_identity_uid: str | None
    account__account_email: str | None
    account__display_name: str | None
    account__account_address: str | None
    account__is_verified: int | None
    account__is_system: int | None
    monitor__monitor_name: str | None
    monitor__tenant_uid: str | None
    monitor__account_uid: str | None
    monitor__monitor_type_uid: str | None
    monitor__schedule_expression: str | None
    monitor__monitor_protocol: str | None
    monitor__monitor_url: str | None
    monitor__monitor_user: str | None
    monitor__monitor_priority: int | None
    monitor__is_on_hold: int | None
    monitor__last_status_name: str | None
    monitor__last_run_time: str | None
    monitor__last_exception_message: str | None
    def __init__(self, monitor_run_uid: str | None, monitor_run_name: str | None, tenant_uid: str | None, account_uid: str | None, monitor_uid: str | None, status_name: str | None, run_time: str | None, exception_message: str | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None, tenant__tenant_name: str | None, tenant__country_uid: str | None, tenant__tenant_type_uid: str | None, tenant__tenant_category_uid: str | None, tenant__tenant_code: str | None, tenant__tenant_description: str | None, tenant__start_date: datetime.datetime | None, tenant__end_date: datetime.datetime | None, tenant__is_internal: int | None, tenant__is_system: int | None, tenant__is_test: int | None, tenant__account_uid: str | None, account__account_name: str | None, account__tenant_uid: str | None, account__account_type_uid: str | None, account__account_title_uid: str | None, account__account_division_uid: str | None, account__account_group_uid: str | None, account__auth_identity_uid: str | None, account__account_email: str | None, account__display_name: str | None, account__account_address: str | None, account__is_verified: int | None, account__is_system: int | None, monitor__monitor_name: str | None, monitor__tenant_uid: str | None, monitor__account_uid: str | None, monitor__monitor_type_uid: str | None, monitor__schedule_expression: str | None, monitor__monitor_protocol: str | None, monitor__monitor_url: str | None, monitor__monitor_user: str | None, monitor__monitor_priority: int | None, monitor__is_on_hold: int | None, monitor__last_status_name: str | None, monitor__last_run_time: str | None, monitor__last_exception_message: str | None):
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
        self.tenant__tenant_name = tenant__tenant_name
        self.tenant__country_uid = tenant__country_uid
        self.tenant__tenant_type_uid = tenant__tenant_type_uid
        self.tenant__tenant_category_uid = tenant__tenant_category_uid
        self.tenant__tenant_code = tenant__tenant_code
        self.tenant__tenant_description = tenant__tenant_description
        self.tenant__start_date = tenant__start_date
        self.tenant__end_date = tenant__end_date
        self.tenant__is_internal = tenant__is_internal
        self.tenant__is_system = tenant__is_system
        self.tenant__is_test = tenant__is_test
        self.tenant__account_uid = tenant__account_uid
        self.account__account_name = account__account_name
        self.account__tenant_uid = account__tenant_uid
        self.account__account_type_uid = account__account_type_uid
        self.account__account_title_uid = account__account_title_uid
        self.account__account_division_uid = account__account_division_uid
        self.account__account_group_uid = account__account_group_uid
        self.account__auth_identity_uid = account__auth_identity_uid
        self.account__account_email = account__account_email
        self.account__display_name = account__display_name
        self.account__account_address = account__account_address
        self.account__is_verified = account__is_verified
        self.account__is_system = account__is_system
        self.monitor__monitor_name = monitor__monitor_name
        self.monitor__tenant_uid = monitor__tenant_uid
        self.monitor__account_uid = monitor__account_uid
        self.monitor__monitor_type_uid = monitor__monitor_type_uid
        self.monitor__schedule_expression = monitor__schedule_expression
        self.monitor__monitor_protocol = monitor__monitor_protocol
        self.monitor__monitor_url = monitor__monitor_url
        self.monitor__monitor_user = monitor__monitor_user
        self.monitor__monitor_priority = monitor__monitor_priority
        self.monitor__is_on_hold = monitor__is_on_hold
        self.monitor__last_status_name = monitor__last_status_name
        self.monitor__last_run_time = monitor__last_run_time
        self.monitor__last_exception_message = monitor__last_exception_message
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.monitor_run_uid, self.monitor_run_name, self.tenant_uid, self.account_uid, self.monitor_uid, self.status_name, self.run_time, self.exception_message, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes, self.tenant__tenant_name, self.tenant__country_uid, self.tenant__tenant_type_uid, self.tenant__tenant_category_uid, self.tenant__tenant_code, self.tenant__tenant_description, self.tenant__start_date, self.tenant__end_date, self.tenant__is_internal, self.tenant__is_system, self.tenant__is_test, self.tenant__account_uid, self.account__account_name, self.account__tenant_uid, self.account__account_type_uid, self.account__account_title_uid, self.account__account_division_uid, self.account__account_group_uid, self.account__auth_identity_uid, self.account__account_email, self.account__display_name, self.account__account_address, self.account__is_verified, self.account__is_system, self.monitor__monitor_name, self.monitor__tenant_uid, self.monitor__account_uid, self.monitor__monitor_type_uid, self.monitor__schedule_expression, self.monitor__monitor_protocol, self.monitor__monitor_url, self.monitor__monitor_user, self.monitor__monitor_priority, self.monitor__is_on_hold, self.monitor__last_status_name, self.monitor__last_run_time, self.monitor__last_exception_message]


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
    tenant__tenant_name: str | None
    tenant__country_uid: str | None
    tenant__tenant_type_uid: str | None
    tenant__tenant_category_uid: str | None
    tenant__tenant_code: str | None
    tenant__tenant_description: str | None
    tenant__start_date: datetime.datetime | None
    tenant__end_date: datetime.datetime | None
    tenant__is_internal: int | None
    tenant__is_system: int | None
    tenant__is_test: int | None
    tenant__account_uid: str | None
    account__account_name: str | None
    account__tenant_uid: str | None
    account__account_type_uid: str | None
    account__account_title_uid: str | None
    account__account_division_uid: str | None
    account__account_group_uid: str | None
    account__auth_identity_uid: str | None
    account__account_email: str | None
    account__display_name: str | None
    account__account_address: str | None
    account__is_verified: int | None
    account__is_system: int | None
    process_type__process_type_name: str | None
    process_type__class_name: str | None
    def __init__(self, process_uid: str | None, process_name: str | None, tenant_uid: str | None, account_uid: str | None, process_type_uid: str | None, status_name: str | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None, tenant__tenant_name: str | None, tenant__country_uid: str | None, tenant__tenant_type_uid: str | None, tenant__tenant_category_uid: str | None, tenant__tenant_code: str | None, tenant__tenant_description: str | None, tenant__start_date: datetime.datetime | None, tenant__end_date: datetime.datetime | None, tenant__is_internal: int | None, tenant__is_system: int | None, tenant__is_test: int | None, tenant__account_uid: str | None, account__account_name: str | None, account__tenant_uid: str | None, account__account_type_uid: str | None, account__account_title_uid: str | None, account__account_division_uid: str | None, account__account_group_uid: str | None, account__auth_identity_uid: str | None, account__account_email: str | None, account__display_name: str | None, account__account_address: str | None, account__is_verified: int | None, account__is_system: int | None, process_type__process_type_name: str | None, process_type__class_name: str | None):
        self.process_uid = process_uid
        self.process_name = process_name
        self.tenant_uid = tenant_uid
        self.account_uid = account_uid
        self.process_type_uid = process_type_uid
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
        self.tenant__tenant_name = tenant__tenant_name
        self.tenant__country_uid = tenant__country_uid
        self.tenant__tenant_type_uid = tenant__tenant_type_uid
        self.tenant__tenant_category_uid = tenant__tenant_category_uid
        self.tenant__tenant_code = tenant__tenant_code
        self.tenant__tenant_description = tenant__tenant_description
        self.tenant__start_date = tenant__start_date
        self.tenant__end_date = tenant__end_date
        self.tenant__is_internal = tenant__is_internal
        self.tenant__is_system = tenant__is_system
        self.tenant__is_test = tenant__is_test
        self.tenant__account_uid = tenant__account_uid
        self.account__account_name = account__account_name
        self.account__tenant_uid = account__tenant_uid
        self.account__account_type_uid = account__account_type_uid
        self.account__account_title_uid = account__account_title_uid
        self.account__account_division_uid = account__account_division_uid
        self.account__account_group_uid = account__account_group_uid
        self.account__auth_identity_uid = account__auth_identity_uid
        self.account__account_email = account__account_email
        self.account__display_name = account__display_name
        self.account__account_address = account__account_address
        self.account__is_verified = account__is_verified
        self.account__is_system = account__is_system
        self.process_type__process_type_name = process_type__process_type_name
        self.process_type__class_name = process_type__class_name
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.process_uid, self.process_name, self.tenant_uid, self.account_uid, self.process_type_uid, self.status_name, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes, self.tenant__tenant_name, self.tenant__country_uid, self.tenant__tenant_type_uid, self.tenant__tenant_category_uid, self.tenant__tenant_code, self.tenant__tenant_description, self.tenant__start_date, self.tenant__end_date, self.tenant__is_internal, self.tenant__is_system, self.tenant__is_test, self.tenant__account_uid, self.account__account_name, self.account__tenant_uid, self.account__account_type_uid, self.account__account_title_uid, self.account__account_division_uid, self.account__account_group_uid, self.account__auth_identity_uid, self.account__account_email, self.account__display_name, self.account__account_address, self.account__is_verified, self.account__is_system, self.process_type__process_type_name, self.process_type__class_name]


@dataclass(frozen=False)
class process_run_rich_dto(process_run_read_dto):
    process_run_uid: str | None
    process_run_name: str | None
    tenant_uid: str | None
    account_uid: str | None
    process_uid: str | None
    status_name: str | None
    run_time: int | None
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
    tenant__tenant_name: str | None
    tenant__country_uid: str | None
    tenant__tenant_type_uid: str | None
    tenant__tenant_category_uid: str | None
    tenant__tenant_code: str | None
    tenant__tenant_description: str | None
    tenant__start_date: datetime.datetime | None
    tenant__end_date: datetime.datetime | None
    tenant__is_internal: int | None
    tenant__is_system: int | None
    tenant__is_test: int | None
    tenant__account_uid: str | None
    account__account_name: str | None
    account__tenant_uid: str | None
    account__account_type_uid: str | None
    account__account_title_uid: str | None
    account__account_division_uid: str | None
    account__account_group_uid: str | None
    account__auth_identity_uid: str | None
    account__account_email: str | None
    account__display_name: str | None
    account__account_address: str | None
    account__is_verified: int | None
    account__is_system: int | None
    process__process_name: str | None
    process__tenant_uid: str | None
    process__account_uid: str | None
    process__process_type_uid: str | None
    process__status_name: str | None
    def __init__(self, process_run_uid: str | None, process_run_name: str | None, tenant_uid: str | None, account_uid: str | None, process_uid: str | None, status_name: str | None, run_time: int | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None, tenant__tenant_name: str | None, tenant__country_uid: str | None, tenant__tenant_type_uid: str | None, tenant__tenant_category_uid: str | None, tenant__tenant_code: str | None, tenant__tenant_description: str | None, tenant__start_date: datetime.datetime | None, tenant__end_date: datetime.datetime | None, tenant__is_internal: int | None, tenant__is_system: int | None, tenant__is_test: int | None, tenant__account_uid: str | None, account__account_name: str | None, account__tenant_uid: str | None, account__account_type_uid: str | None, account__account_title_uid: str | None, account__account_division_uid: str | None, account__account_group_uid: str | None, account__auth_identity_uid: str | None, account__account_email: str | None, account__display_name: str | None, account__account_address: str | None, account__is_verified: int | None, account__is_system: int | None, process__process_name: str | None, process__tenant_uid: str | None, process__account_uid: str | None, process__process_type_uid: str | None, process__status_name: str | None):
        self.process_run_uid = process_run_uid
        self.process_run_name = process_run_name
        self.tenant_uid = tenant_uid
        self.account_uid = account_uid
        self.process_uid = process_uid
        self.status_name = status_name
        self.run_time = run_time
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
        self.tenant__tenant_name = tenant__tenant_name
        self.tenant__country_uid = tenant__country_uid
        self.tenant__tenant_type_uid = tenant__tenant_type_uid
        self.tenant__tenant_category_uid = tenant__tenant_category_uid
        self.tenant__tenant_code = tenant__tenant_code
        self.tenant__tenant_description = tenant__tenant_description
        self.tenant__start_date = tenant__start_date
        self.tenant__end_date = tenant__end_date
        self.tenant__is_internal = tenant__is_internal
        self.tenant__is_system = tenant__is_system
        self.tenant__is_test = tenant__is_test
        self.tenant__account_uid = tenant__account_uid
        self.account__account_name = account__account_name
        self.account__tenant_uid = account__tenant_uid
        self.account__account_type_uid = account__account_type_uid
        self.account__account_title_uid = account__account_title_uid
        self.account__account_division_uid = account__account_division_uid
        self.account__account_group_uid = account__account_group_uid
        self.account__auth_identity_uid = account__auth_identity_uid
        self.account__account_email = account__account_email
        self.account__display_name = account__display_name
        self.account__account_address = account__account_address
        self.account__is_verified = account__is_verified
        self.account__is_system = account__is_system
        self.process__process_name = process__process_name
        self.process__tenant_uid = process__tenant_uid
        self.process__account_uid = process__account_uid
        self.process__process_type_uid = process__process_type_uid
        self.process__status_name = process__status_name
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.process_run_uid, self.process_run_name, self.tenant_uid, self.account_uid, self.process_uid, self.status_name, self.run_time, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes, self.tenant__tenant_name, self.tenant__country_uid, self.tenant__tenant_type_uid, self.tenant__tenant_category_uid, self.tenant__tenant_code, self.tenant__tenant_description, self.tenant__start_date, self.tenant__end_date, self.tenant__is_internal, self.tenant__is_system, self.tenant__is_test, self.tenant__account_uid, self.account__account_name, self.account__tenant_uid, self.account__account_type_uid, self.account__account_title_uid, self.account__account_division_uid, self.account__account_group_uid, self.account__auth_identity_uid, self.account__account_email, self.account__display_name, self.account__account_address, self.account__is_verified, self.account__is_system, self.process__process_name, self.process__tenant_uid, self.process__account_uid, self.process__process_type_uid, self.process__status_name]


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
    project_account__account_name: str | None
    project_account__tenant_uid: str | None
    project_account__account_type_uid: str | None
    project_account__account_title_uid: str | None
    project_account__account_division_uid: str | None
    project_account__account_group_uid: str | None
    project_account__auth_identity_uid: str | None
    project_account__account_email: str | None
    project_account__display_name: str | None
    project_account__account_address: str | None
    project_account__is_verified: int | None
    project_account__is_system: int | None
    tenant__tenant_name: str | None
    tenant__country_uid: str | None
    tenant__tenant_type_uid: str | None
    tenant__tenant_category_uid: str | None
    tenant__tenant_code: str | None
    tenant__tenant_description: str | None
    tenant__start_date: datetime.datetime | None
    tenant__end_date: datetime.datetime | None
    tenant__is_internal: int | None
    tenant__is_system: int | None
    tenant__is_test: int | None
    tenant__account_uid: str | None
    client__client_name: str | None
    client__tenant_uid: str | None
    client__country_uid: str | None
    client__client_type_uid: str | None
    client__client_category_uid: str | None
    client__account_uid: str | None
    client__client_code: str | None
    client__client_description: str | None
    client__start_date: datetime.datetime | None
    client__end_date: datetime.datetime | None
    client__is_internal: int | None
    client__is_system: int | None
    client__is_test: int | None
    account__account_name: str | None
    account__tenant_uid: str | None
    account__account_type_uid: str | None
    account__account_title_uid: str | None
    account__account_division_uid: str | None
    account__account_group_uid: str | None
    account__auth_identity_uid: str | None
    account__account_email: str | None
    account__display_name: str | None
    account__account_address: str | None
    account__is_verified: int | None
    account__is_system: int | None
    project_instance__project_instance_name: str | None
    project_instance__tenant_uid: str | None
    project_instance__client_uid: str | None
    project_instance__project_type_uid: str | None
    project_instance__manager_account_uid: str | None
    project_instance__project_group_uid: str | None
    project_instance__project_code: str | None
    project_instance__project_description: str | None
    project_instance__is_billable: int | None
    project_instance__start_date: datetime.datetime | None
    project_instance__end_date: datetime.datetime | None
    project_instance__current_billed: str | None
    project_instance__budget: str | None
    def __init__(self, project_account_uid: str | None, project_account_name: str | None, tenant_uid: str | None, client_uid: str | None, account_uid: str | None, project_instance_uid: str | None, start_date: datetime.datetime | None, end_date: datetime.datetime | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None, project_account__account_name: str | None, project_account__tenant_uid: str | None, project_account__account_type_uid: str | None, project_account__account_title_uid: str | None, project_account__account_division_uid: str | None, project_account__account_group_uid: str | None, project_account__auth_identity_uid: str | None, project_account__account_email: str | None, project_account__display_name: str | None, project_account__account_address: str | None, project_account__is_verified: int | None, project_account__is_system: int | None, tenant__tenant_name: str | None, tenant__country_uid: str | None, tenant__tenant_type_uid: str | None, tenant__tenant_category_uid: str | None, tenant__tenant_code: str | None, tenant__tenant_description: str | None, tenant__start_date: datetime.datetime | None, tenant__end_date: datetime.datetime | None, tenant__is_internal: int | None, tenant__is_system: int | None, tenant__is_test: int | None, tenant__account_uid: str | None, client__client_name: str | None, client__tenant_uid: str | None, client__country_uid: str | None, client__client_type_uid: str | None, client__client_category_uid: str | None, client__account_uid: str | None, client__client_code: str | None, client__client_description: str | None, client__start_date: datetime.datetime | None, client__end_date: datetime.datetime | None, client__is_internal: int | None, client__is_system: int | None, client__is_test: int | None, account__account_name: str | None, account__tenant_uid: str | None, account__account_type_uid: str | None, account__account_title_uid: str | None, account__account_division_uid: str | None, account__account_group_uid: str | None, account__auth_identity_uid: str | None, account__account_email: str | None, account__display_name: str | None, account__account_address: str | None, account__is_verified: int | None, account__is_system: int | None, project_instance__project_instance_name: str | None, project_instance__tenant_uid: str | None, project_instance__client_uid: str | None, project_instance__project_type_uid: str | None, project_instance__manager_account_uid: str | None, project_instance__project_group_uid: str | None, project_instance__project_code: str | None, project_instance__project_description: str | None, project_instance__is_billable: int | None, project_instance__start_date: datetime.datetime | None, project_instance__end_date: datetime.datetime | None, project_instance__current_billed: str | None, project_instance__budget: str | None):
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
        self.project_account__account_name = project_account__account_name
        self.project_account__tenant_uid = project_account__tenant_uid
        self.project_account__account_type_uid = project_account__account_type_uid
        self.project_account__account_title_uid = project_account__account_title_uid
        self.project_account__account_division_uid = project_account__account_division_uid
        self.project_account__account_group_uid = project_account__account_group_uid
        self.project_account__auth_identity_uid = project_account__auth_identity_uid
        self.project_account__account_email = project_account__account_email
        self.project_account__display_name = project_account__display_name
        self.project_account__account_address = project_account__account_address
        self.project_account__is_verified = project_account__is_verified
        self.project_account__is_system = project_account__is_system
        self.tenant__tenant_name = tenant__tenant_name
        self.tenant__country_uid = tenant__country_uid
        self.tenant__tenant_type_uid = tenant__tenant_type_uid
        self.tenant__tenant_category_uid = tenant__tenant_category_uid
        self.tenant__tenant_code = tenant__tenant_code
        self.tenant__tenant_description = tenant__tenant_description
        self.tenant__start_date = tenant__start_date
        self.tenant__end_date = tenant__end_date
        self.tenant__is_internal = tenant__is_internal
        self.tenant__is_system = tenant__is_system
        self.tenant__is_test = tenant__is_test
        self.tenant__account_uid = tenant__account_uid
        self.client__client_name = client__client_name
        self.client__tenant_uid = client__tenant_uid
        self.client__country_uid = client__country_uid
        self.client__client_type_uid = client__client_type_uid
        self.client__client_category_uid = client__client_category_uid
        self.client__account_uid = client__account_uid
        self.client__client_code = client__client_code
        self.client__client_description = client__client_description
        self.client__start_date = client__start_date
        self.client__end_date = client__end_date
        self.client__is_internal = client__is_internal
        self.client__is_system = client__is_system
        self.client__is_test = client__is_test
        self.account__account_name = account__account_name
        self.account__tenant_uid = account__tenant_uid
        self.account__account_type_uid = account__account_type_uid
        self.account__account_title_uid = account__account_title_uid
        self.account__account_division_uid = account__account_division_uid
        self.account__account_group_uid = account__account_group_uid
        self.account__auth_identity_uid = account__auth_identity_uid
        self.account__account_email = account__account_email
        self.account__display_name = account__display_name
        self.account__account_address = account__account_address
        self.account__is_verified = account__is_verified
        self.account__is_system = account__is_system
        self.project_instance__project_instance_name = project_instance__project_instance_name
        self.project_instance__tenant_uid = project_instance__tenant_uid
        self.project_instance__client_uid = project_instance__client_uid
        self.project_instance__project_type_uid = project_instance__project_type_uid
        self.project_instance__manager_account_uid = project_instance__manager_account_uid
        self.project_instance__project_group_uid = project_instance__project_group_uid
        self.project_instance__project_code = project_instance__project_code
        self.project_instance__project_description = project_instance__project_description
        self.project_instance__is_billable = project_instance__is_billable
        self.project_instance__start_date = project_instance__start_date
        self.project_instance__end_date = project_instance__end_date
        self.project_instance__current_billed = project_instance__current_billed
        self.project_instance__budget = project_instance__budget
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.project_account_uid, self.project_account_name, self.tenant_uid, self.client_uid, self.account_uid, self.project_instance_uid, self.start_date, self.end_date, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes, self.project_account__account_name, self.project_account__tenant_uid, self.project_account__account_type_uid, self.project_account__account_title_uid, self.project_account__account_division_uid, self.project_account__account_group_uid, self.project_account__auth_identity_uid, self.project_account__account_email, self.project_account__display_name, self.project_account__account_address, self.project_account__is_verified, self.project_account__is_system, self.tenant__tenant_name, self.tenant__country_uid, self.tenant__tenant_type_uid, self.tenant__tenant_category_uid, self.tenant__tenant_code, self.tenant__tenant_description, self.tenant__start_date, self.tenant__end_date, self.tenant__is_internal, self.tenant__is_system, self.tenant__is_test, self.tenant__account_uid, self.client__client_name, self.client__tenant_uid, self.client__country_uid, self.client__client_type_uid, self.client__client_category_uid, self.client__account_uid, self.client__client_code, self.client__client_description, self.client__start_date, self.client__end_date, self.client__is_internal, self.client__is_system, self.client__is_test, self.account__account_name, self.account__tenant_uid, self.account__account_type_uid, self.account__account_title_uid, self.account__account_division_uid, self.account__account_group_uid, self.account__auth_identity_uid, self.account__account_email, self.account__display_name, self.account__account_address, self.account__is_verified, self.account__is_system, self.project_instance__project_instance_name, self.project_instance__tenant_uid, self.project_instance__client_uid, self.project_instance__project_type_uid, self.project_instance__manager_account_uid, self.project_instance__project_group_uid, self.project_instance__project_code, self.project_instance__project_description, self.project_instance__is_billable, self.project_instance__start_date, self.project_instance__end_date, self.project_instance__current_billed, self.project_instance__budget]


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
    tenant__tenant_name: str | None
    tenant__country_uid: str | None
    tenant__tenant_type_uid: str | None
    tenant__tenant_category_uid: str | None
    tenant__tenant_code: str | None
    tenant__tenant_description: str | None
    tenant__start_date: datetime.datetime | None
    tenant__end_date: datetime.datetime | None
    tenant__is_internal: int | None
    tenant__is_system: int | None
    tenant__is_test: int | None
    tenant__account_uid: str | None
    client__client_name: str | None
    client__tenant_uid: str | None
    client__country_uid: str | None
    client__client_type_uid: str | None
    client__client_category_uid: str | None
    client__account_uid: str | None
    client__client_code: str | None
    client__client_description: str | None
    client__start_date: datetime.datetime | None
    client__end_date: datetime.datetime | None
    client__is_internal: int | None
    client__is_system: int | None
    client__is_test: int | None
    project_instance__project_instance_name: str | None
    project_instance__tenant_uid: str | None
    project_instance__client_uid: str | None
    project_instance__project_type_uid: str | None
    project_instance__manager_account_uid: str | None
    project_instance__project_group_uid: str | None
    project_instance__project_code: str | None
    project_instance__project_description: str | None
    project_instance__is_billable: int | None
    project_instance__start_date: datetime.datetime | None
    project_instance__end_date: datetime.datetime | None
    project_instance__current_billed: str | None
    project_instance__budget: str | None
    currency__currency_name: str | None
    currency__is_focused: int | None
    currency__priority: int | None
    def __init__(self, project_budget_uid: str | None, project_budget_name: str | None, tenant_uid: str | None, client_uid: str | None, project_instance_uid: str | None, currency_uid: str | None, budget_value: str | None, is_approved: int | None, is_current: int | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None, tenant__tenant_name: str | None, tenant__country_uid: str | None, tenant__tenant_type_uid: str | None, tenant__tenant_category_uid: str | None, tenant__tenant_code: str | None, tenant__tenant_description: str | None, tenant__start_date: datetime.datetime | None, tenant__end_date: datetime.datetime | None, tenant__is_internal: int | None, tenant__is_system: int | None, tenant__is_test: int | None, tenant__account_uid: str | None, client__client_name: str | None, client__tenant_uid: str | None, client__country_uid: str | None, client__client_type_uid: str | None, client__client_category_uid: str | None, client__account_uid: str | None, client__client_code: str | None, client__client_description: str | None, client__start_date: datetime.datetime | None, client__end_date: datetime.datetime | None, client__is_internal: int | None, client__is_system: int | None, client__is_test: int | None, project_instance__project_instance_name: str | None, project_instance__tenant_uid: str | None, project_instance__client_uid: str | None, project_instance__project_type_uid: str | None, project_instance__manager_account_uid: str | None, project_instance__project_group_uid: str | None, project_instance__project_code: str | None, project_instance__project_description: str | None, project_instance__is_billable: int | None, project_instance__start_date: datetime.datetime | None, project_instance__end_date: datetime.datetime | None, project_instance__current_billed: str | None, project_instance__budget: str | None, currency__currency_name: str | None, currency__is_focused: int | None, currency__priority: int | None):
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
        self.tenant__tenant_name = tenant__tenant_name
        self.tenant__country_uid = tenant__country_uid
        self.tenant__tenant_type_uid = tenant__tenant_type_uid
        self.tenant__tenant_category_uid = tenant__tenant_category_uid
        self.tenant__tenant_code = tenant__tenant_code
        self.tenant__tenant_description = tenant__tenant_description
        self.tenant__start_date = tenant__start_date
        self.tenant__end_date = tenant__end_date
        self.tenant__is_internal = tenant__is_internal
        self.tenant__is_system = tenant__is_system
        self.tenant__is_test = tenant__is_test
        self.tenant__account_uid = tenant__account_uid
        self.client__client_name = client__client_name
        self.client__tenant_uid = client__tenant_uid
        self.client__country_uid = client__country_uid
        self.client__client_type_uid = client__client_type_uid
        self.client__client_category_uid = client__client_category_uid
        self.client__account_uid = client__account_uid
        self.client__client_code = client__client_code
        self.client__client_description = client__client_description
        self.client__start_date = client__start_date
        self.client__end_date = client__end_date
        self.client__is_internal = client__is_internal
        self.client__is_system = client__is_system
        self.client__is_test = client__is_test
        self.project_instance__project_instance_name = project_instance__project_instance_name
        self.project_instance__tenant_uid = project_instance__tenant_uid
        self.project_instance__client_uid = project_instance__client_uid
        self.project_instance__project_type_uid = project_instance__project_type_uid
        self.project_instance__manager_account_uid = project_instance__manager_account_uid
        self.project_instance__project_group_uid = project_instance__project_group_uid
        self.project_instance__project_code = project_instance__project_code
        self.project_instance__project_description = project_instance__project_description
        self.project_instance__is_billable = project_instance__is_billable
        self.project_instance__start_date = project_instance__start_date
        self.project_instance__end_date = project_instance__end_date
        self.project_instance__current_billed = project_instance__current_billed
        self.project_instance__budget = project_instance__budget
        self.currency__currency_name = currency__currency_name
        self.currency__is_focused = currency__is_focused
        self.currency__priority = currency__priority
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.project_budget_uid, self.project_budget_name, self.tenant_uid, self.client_uid, self.project_instance_uid, self.currency_uid, self.budget_value, self.is_approved, self.is_current, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes, self.tenant__tenant_name, self.tenant__country_uid, self.tenant__tenant_type_uid, self.tenant__tenant_category_uid, self.tenant__tenant_code, self.tenant__tenant_description, self.tenant__start_date, self.tenant__end_date, self.tenant__is_internal, self.tenant__is_system, self.tenant__is_test, self.tenant__account_uid, self.client__client_name, self.client__tenant_uid, self.client__country_uid, self.client__client_type_uid, self.client__client_category_uid, self.client__account_uid, self.client__client_code, self.client__client_description, self.client__start_date, self.client__end_date, self.client__is_internal, self.client__is_system, self.client__is_test, self.project_instance__project_instance_name, self.project_instance__tenant_uid, self.project_instance__client_uid, self.project_instance__project_type_uid, self.project_instance__manager_account_uid, self.project_instance__project_group_uid, self.project_instance__project_code, self.project_instance__project_description, self.project_instance__is_billable, self.project_instance__start_date, self.project_instance__end_date, self.project_instance__current_billed, self.project_instance__budget, self.currency__currency_name, self.currency__is_focused, self.currency__priority]


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
    tenant__tenant_name: str | None
    tenant__country_uid: str | None
    tenant__tenant_type_uid: str | None
    tenant__tenant_category_uid: str | None
    tenant__tenant_code: str | None
    tenant__tenant_description: str | None
    tenant__start_date: datetime.datetime | None
    tenant__end_date: datetime.datetime | None
    tenant__is_internal: int | None
    tenant__is_system: int | None
    tenant__is_test: int | None
    tenant__account_uid: str | None
    def __init__(self, project_group_uid: str | None, project_group_name: str | None, tenant_uid: str | None, project_group_description: str | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None, tenant__tenant_name: str | None, tenant__country_uid: str | None, tenant__tenant_type_uid: str | None, tenant__tenant_category_uid: str | None, tenant__tenant_code: str | None, tenant__tenant_description: str | None, tenant__start_date: datetime.datetime | None, tenant__end_date: datetime.datetime | None, tenant__is_internal: int | None, tenant__is_system: int | None, tenant__is_test: int | None, tenant__account_uid: str | None):
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
        self.tenant__tenant_name = tenant__tenant_name
        self.tenant__country_uid = tenant__country_uid
        self.tenant__tenant_type_uid = tenant__tenant_type_uid
        self.tenant__tenant_category_uid = tenant__tenant_category_uid
        self.tenant__tenant_code = tenant__tenant_code
        self.tenant__tenant_description = tenant__tenant_description
        self.tenant__start_date = tenant__start_date
        self.tenant__end_date = tenant__end_date
        self.tenant__is_internal = tenant__is_internal
        self.tenant__is_system = tenant__is_system
        self.tenant__is_test = tenant__is_test
        self.tenant__account_uid = tenant__account_uid
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.project_group_uid, self.project_group_name, self.tenant_uid, self.project_group_description, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes, self.tenant__tenant_name, self.tenant__country_uid, self.tenant__tenant_type_uid, self.tenant__tenant_category_uid, self.tenant__tenant_code, self.tenant__tenant_description, self.tenant__start_date, self.tenant__end_date, self.tenant__is_internal, self.tenant__is_system, self.tenant__is_test, self.tenant__account_uid]


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
    tenant__tenant_name: str | None
    tenant__country_uid: str | None
    tenant__tenant_type_uid: str | None
    tenant__tenant_category_uid: str | None
    tenant__tenant_code: str | None
    tenant__tenant_description: str | None
    tenant__start_date: datetime.datetime | None
    tenant__end_date: datetime.datetime | None
    tenant__is_internal: int | None
    tenant__is_system: int | None
    tenant__is_test: int | None
    tenant__account_uid: str | None
    client__client_name: str | None
    client__tenant_uid: str | None
    client__country_uid: str | None
    client__client_type_uid: str | None
    client__client_category_uid: str | None
    client__account_uid: str | None
    client__client_code: str | None
    client__client_description: str | None
    client__start_date: datetime.datetime | None
    client__end_date: datetime.datetime | None
    client__is_internal: int | None
    client__is_system: int | None
    client__is_test: int | None
    project_type__project_type_name: str | None
    project_type__project_type_description: str | None
    manager_account__account_name: str | None
    manager_account__tenant_uid: str | None
    manager_account__account_type_uid: str | None
    manager_account__account_title_uid: str | None
    manager_account__account_division_uid: str | None
    manager_account__account_group_uid: str | None
    manager_account__auth_identity_uid: str | None
    manager_account__account_email: str | None
    manager_account__display_name: str | None
    manager_account__account_address: str | None
    manager_account__is_verified: int | None
    manager_account__is_system: int | None
    project_group__project_group_name: str | None
    project_group__tenant_uid: str | None
    project_group__project_group_description: str | None
    def __init__(self, project_instance_uid: str | None, project_instance_name: str | None, tenant_uid: str | None, client_uid: str | None, project_type_uid: str | None, manager_account_uid: str | None, project_group_uid: str | None, project_code: str | None, project_description: str | None, is_billable: int | None, start_date: datetime.datetime | None, end_date: datetime.datetime | None, current_billed: str | None, budget: str | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None, tenant__tenant_name: str | None, tenant__country_uid: str | None, tenant__tenant_type_uid: str | None, tenant__tenant_category_uid: str | None, tenant__tenant_code: str | None, tenant__tenant_description: str | None, tenant__start_date: datetime.datetime | None, tenant__end_date: datetime.datetime | None, tenant__is_internal: int | None, tenant__is_system: int | None, tenant__is_test: int | None, tenant__account_uid: str | None, client__client_name: str | None, client__tenant_uid: str | None, client__country_uid: str | None, client__client_type_uid: str | None, client__client_category_uid: str | None, client__account_uid: str | None, client__client_code: str | None, client__client_description: str | None, client__start_date: datetime.datetime | None, client__end_date: datetime.datetime | None, client__is_internal: int | None, client__is_system: int | None, client__is_test: int | None, project_type__project_type_name: str | None, project_type__project_type_description: str | None, manager_account__account_name: str | None, manager_account__tenant_uid: str | None, manager_account__account_type_uid: str | None, manager_account__account_title_uid: str | None, manager_account__account_division_uid: str | None, manager_account__account_group_uid: str | None, manager_account__auth_identity_uid: str | None, manager_account__account_email: str | None, manager_account__display_name: str | None, manager_account__account_address: str | None, manager_account__is_verified: int | None, manager_account__is_system: int | None, project_group__project_group_name: str | None, project_group__tenant_uid: str | None, project_group__project_group_description: str | None):
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
        self.tenant__tenant_name = tenant__tenant_name
        self.tenant__country_uid = tenant__country_uid
        self.tenant__tenant_type_uid = tenant__tenant_type_uid
        self.tenant__tenant_category_uid = tenant__tenant_category_uid
        self.tenant__tenant_code = tenant__tenant_code
        self.tenant__tenant_description = tenant__tenant_description
        self.tenant__start_date = tenant__start_date
        self.tenant__end_date = tenant__end_date
        self.tenant__is_internal = tenant__is_internal
        self.tenant__is_system = tenant__is_system
        self.tenant__is_test = tenant__is_test
        self.tenant__account_uid = tenant__account_uid
        self.client__client_name = client__client_name
        self.client__tenant_uid = client__tenant_uid
        self.client__country_uid = client__country_uid
        self.client__client_type_uid = client__client_type_uid
        self.client__client_category_uid = client__client_category_uid
        self.client__account_uid = client__account_uid
        self.client__client_code = client__client_code
        self.client__client_description = client__client_description
        self.client__start_date = client__start_date
        self.client__end_date = client__end_date
        self.client__is_internal = client__is_internal
        self.client__is_system = client__is_system
        self.client__is_test = client__is_test
        self.project_type__project_type_name = project_type__project_type_name
        self.project_type__project_type_description = project_type__project_type_description
        self.manager_account__account_name = manager_account__account_name
        self.manager_account__tenant_uid = manager_account__tenant_uid
        self.manager_account__account_type_uid = manager_account__account_type_uid
        self.manager_account__account_title_uid = manager_account__account_title_uid
        self.manager_account__account_division_uid = manager_account__account_division_uid
        self.manager_account__account_group_uid = manager_account__account_group_uid
        self.manager_account__auth_identity_uid = manager_account__auth_identity_uid
        self.manager_account__account_email = manager_account__account_email
        self.manager_account__display_name = manager_account__display_name
        self.manager_account__account_address = manager_account__account_address
        self.manager_account__is_verified = manager_account__is_verified
        self.manager_account__is_system = manager_account__is_system
        self.project_group__project_group_name = project_group__project_group_name
        self.project_group__tenant_uid = project_group__tenant_uid
        self.project_group__project_group_description = project_group__project_group_description
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.project_instance_uid, self.project_instance_name, self.tenant_uid, self.client_uid, self.project_type_uid, self.manager_account_uid, self.project_group_uid, self.project_code, self.project_description, self.is_billable, self.start_date, self.end_date, self.current_billed, self.budget, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes, self.tenant__tenant_name, self.tenant__country_uid, self.tenant__tenant_type_uid, self.tenant__tenant_category_uid, self.tenant__tenant_code, self.tenant__tenant_description, self.tenant__start_date, self.tenant__end_date, self.tenant__is_internal, self.tenant__is_system, self.tenant__is_test, self.tenant__account_uid, self.client__client_name, self.client__tenant_uid, self.client__country_uid, self.client__client_type_uid, self.client__client_category_uid, self.client__account_uid, self.client__client_code, self.client__client_description, self.client__start_date, self.client__end_date, self.client__is_internal, self.client__is_system, self.client__is_test, self.project_type__project_type_name, self.project_type__project_type_description, self.manager_account__account_name, self.manager_account__tenant_uid, self.manager_account__account_type_uid, self.manager_account__account_title_uid, self.manager_account__account_division_uid, self.manager_account__account_group_uid, self.manager_account__auth_identity_uid, self.manager_account__account_email, self.manager_account__display_name, self.manager_account__account_address, self.manager_account__is_verified, self.manager_account__is_system, self.project_group__project_group_name, self.project_group__tenant_uid, self.project_group__project_group_description]


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
    tenant__tenant_name: str | None
    tenant__country_uid: str | None
    tenant__tenant_type_uid: str | None
    tenant__tenant_category_uid: str | None
    tenant__tenant_code: str | None
    tenant__tenant_description: str | None
    tenant__start_date: datetime.datetime | None
    tenant__end_date: datetime.datetime | None
    tenant__is_internal: int | None
    tenant__is_system: int | None
    tenant__is_test: int | None
    tenant__account_uid: str | None
    client__client_name: str | None
    client__tenant_uid: str | None
    client__country_uid: str | None
    client__client_type_uid: str | None
    client__client_category_uid: str | None
    client__account_uid: str | None
    client__client_code: str | None
    client__client_description: str | None
    client__start_date: datetime.datetime | None
    client__end_date: datetime.datetime | None
    client__is_internal: int | None
    client__is_system: int | None
    client__is_test: int | None
    project_instance__project_instance_name: str | None
    project_instance__tenant_uid: str | None
    project_instance__client_uid: str | None
    project_instance__project_type_uid: str | None
    project_instance__manager_account_uid: str | None
    project_instance__project_group_uid: str | None
    project_instance__project_code: str | None
    project_instance__project_description: str | None
    project_instance__is_billable: int | None
    project_instance__start_date: datetime.datetime | None
    project_instance__end_date: datetime.datetime | None
    project_instance__current_billed: str | None
    project_instance__budget: str | None
    project_budget__project_budget_name: str | None
    project_budget__tenant_uid: str | None
    project_budget__client_uid: str | None
    project_budget__project_instance_uid: str | None
    project_budget__currency_uid: str | None
    project_budget__budget_value: str | None
    project_budget__is_approved: int | None
    project_budget__is_current: int | None
    def __init__(self, project_milestone_uid: str | None, project_milestone_name: str | None, tenant_uid: str | None, client_uid: str | None, project_instance_uid: str | None, project_budget_uid: str | None, start_date: datetime.datetime | None, end_date: datetime.datetime | None, status_name: str | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None, tenant__tenant_name: str | None, tenant__country_uid: str | None, tenant__tenant_type_uid: str | None, tenant__tenant_category_uid: str | None, tenant__tenant_code: str | None, tenant__tenant_description: str | None, tenant__start_date: datetime.datetime | None, tenant__end_date: datetime.datetime | None, tenant__is_internal: int | None, tenant__is_system: int | None, tenant__is_test: int | None, tenant__account_uid: str | None, client__client_name: str | None, client__tenant_uid: str | None, client__country_uid: str | None, client__client_type_uid: str | None, client__client_category_uid: str | None, client__account_uid: str | None, client__client_code: str | None, client__client_description: str | None, client__start_date: datetime.datetime | None, client__end_date: datetime.datetime | None, client__is_internal: int | None, client__is_system: int | None, client__is_test: int | None, project_instance__project_instance_name: str | None, project_instance__tenant_uid: str | None, project_instance__client_uid: str | None, project_instance__project_type_uid: str | None, project_instance__manager_account_uid: str | None, project_instance__project_group_uid: str | None, project_instance__project_code: str | None, project_instance__project_description: str | None, project_instance__is_billable: int | None, project_instance__start_date: datetime.datetime | None, project_instance__end_date: datetime.datetime | None, project_instance__current_billed: str | None, project_instance__budget: str | None, project_budget__project_budget_name: str | None, project_budget__tenant_uid: str | None, project_budget__client_uid: str | None, project_budget__project_instance_uid: str | None, project_budget__currency_uid: str | None, project_budget__budget_value: str | None, project_budget__is_approved: int | None, project_budget__is_current: int | None):
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
        self.tenant__tenant_name = tenant__tenant_name
        self.tenant__country_uid = tenant__country_uid
        self.tenant__tenant_type_uid = tenant__tenant_type_uid
        self.tenant__tenant_category_uid = tenant__tenant_category_uid
        self.tenant__tenant_code = tenant__tenant_code
        self.tenant__tenant_description = tenant__tenant_description
        self.tenant__start_date = tenant__start_date
        self.tenant__end_date = tenant__end_date
        self.tenant__is_internal = tenant__is_internal
        self.tenant__is_system = tenant__is_system
        self.tenant__is_test = tenant__is_test
        self.tenant__account_uid = tenant__account_uid
        self.client__client_name = client__client_name
        self.client__tenant_uid = client__tenant_uid
        self.client__country_uid = client__country_uid
        self.client__client_type_uid = client__client_type_uid
        self.client__client_category_uid = client__client_category_uid
        self.client__account_uid = client__account_uid
        self.client__client_code = client__client_code
        self.client__client_description = client__client_description
        self.client__start_date = client__start_date
        self.client__end_date = client__end_date
        self.client__is_internal = client__is_internal
        self.client__is_system = client__is_system
        self.client__is_test = client__is_test
        self.project_instance__project_instance_name = project_instance__project_instance_name
        self.project_instance__tenant_uid = project_instance__tenant_uid
        self.project_instance__client_uid = project_instance__client_uid
        self.project_instance__project_type_uid = project_instance__project_type_uid
        self.project_instance__manager_account_uid = project_instance__manager_account_uid
        self.project_instance__project_group_uid = project_instance__project_group_uid
        self.project_instance__project_code = project_instance__project_code
        self.project_instance__project_description = project_instance__project_description
        self.project_instance__is_billable = project_instance__is_billable
        self.project_instance__start_date = project_instance__start_date
        self.project_instance__end_date = project_instance__end_date
        self.project_instance__current_billed = project_instance__current_billed
        self.project_instance__budget = project_instance__budget
        self.project_budget__project_budget_name = project_budget__project_budget_name
        self.project_budget__tenant_uid = project_budget__tenant_uid
        self.project_budget__client_uid = project_budget__client_uid
        self.project_budget__project_instance_uid = project_budget__project_instance_uid
        self.project_budget__currency_uid = project_budget__currency_uid
        self.project_budget__budget_value = project_budget__budget_value
        self.project_budget__is_approved = project_budget__is_approved
        self.project_budget__is_current = project_budget__is_current
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.project_milestone_uid, self.project_milestone_name, self.tenant_uid, self.client_uid, self.project_instance_uid, self.project_budget_uid, self.start_date, self.end_date, self.status_name, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes, self.tenant__tenant_name, self.tenant__country_uid, self.tenant__tenant_type_uid, self.tenant__tenant_category_uid, self.tenant__tenant_code, self.tenant__tenant_description, self.tenant__start_date, self.tenant__end_date, self.tenant__is_internal, self.tenant__is_system, self.tenant__is_test, self.tenant__account_uid, self.client__client_name, self.client__tenant_uid, self.client__country_uid, self.client__client_type_uid, self.client__client_category_uid, self.client__account_uid, self.client__client_code, self.client__client_description, self.client__start_date, self.client__end_date, self.client__is_internal, self.client__is_system, self.client__is_test, self.project_instance__project_instance_name, self.project_instance__tenant_uid, self.project_instance__client_uid, self.project_instance__project_type_uid, self.project_instance__manager_account_uid, self.project_instance__project_group_uid, self.project_instance__project_code, self.project_instance__project_description, self.project_instance__is_billable, self.project_instance__start_date, self.project_instance__end_date, self.project_instance__current_billed, self.project_instance__budget, self.project_budget__project_budget_name, self.project_budget__tenant_uid, self.project_budget__client_uid, self.project_budget__project_instance_uid, self.project_budget__currency_uid, self.project_budget__budget_value, self.project_budget__is_approved, self.project_budget__is_current]


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
    tenant__tenant_name: str | None
    tenant__country_uid: str | None
    tenant__tenant_type_uid: str | None
    tenant__tenant_category_uid: str | None
    tenant__tenant_code: str | None
    tenant__tenant_description: str | None
    tenant__start_date: datetime.datetime | None
    tenant__end_date: datetime.datetime | None
    tenant__is_internal: int | None
    tenant__is_system: int | None
    tenant__is_test: int | None
    tenant__account_uid: str | None
    account__account_name: str | None
    account__tenant_uid: str | None
    account__account_type_uid: str | None
    account__account_title_uid: str | None
    account__account_division_uid: str | None
    account__account_group_uid: str | None
    account__auth_identity_uid: str | None
    account__account_email: str | None
    account__display_name: str | None
    account__account_address: str | None
    account__is_verified: int | None
    account__is_system: int | None
    report_status__report_status_name: str | None
    def __init__(self, report_uid: str | None, report_name: str | None, tenant_uid: str | None, account_uid: str | None, report_status_uid: str | None, report_query: str | None, report_parameters: str | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None, tenant__tenant_name: str | None, tenant__country_uid: str | None, tenant__tenant_type_uid: str | None, tenant__tenant_category_uid: str | None, tenant__tenant_code: str | None, tenant__tenant_description: str | None, tenant__start_date: datetime.datetime | None, tenant__end_date: datetime.datetime | None, tenant__is_internal: int | None, tenant__is_system: int | None, tenant__is_test: int | None, tenant__account_uid: str | None, account__account_name: str | None, account__tenant_uid: str | None, account__account_type_uid: str | None, account__account_title_uid: str | None, account__account_division_uid: str | None, account__account_group_uid: str | None, account__auth_identity_uid: str | None, account__account_email: str | None, account__display_name: str | None, account__account_address: str | None, account__is_verified: int | None, account__is_system: int | None, report_status__report_status_name: str | None):
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
        self.tenant__tenant_name = tenant__tenant_name
        self.tenant__country_uid = tenant__country_uid
        self.tenant__tenant_type_uid = tenant__tenant_type_uid
        self.tenant__tenant_category_uid = tenant__tenant_category_uid
        self.tenant__tenant_code = tenant__tenant_code
        self.tenant__tenant_description = tenant__tenant_description
        self.tenant__start_date = tenant__start_date
        self.tenant__end_date = tenant__end_date
        self.tenant__is_internal = tenant__is_internal
        self.tenant__is_system = tenant__is_system
        self.tenant__is_test = tenant__is_test
        self.tenant__account_uid = tenant__account_uid
        self.account__account_name = account__account_name
        self.account__tenant_uid = account__tenant_uid
        self.account__account_type_uid = account__account_type_uid
        self.account__account_title_uid = account__account_title_uid
        self.account__account_division_uid = account__account_division_uid
        self.account__account_group_uid = account__account_group_uid
        self.account__auth_identity_uid = account__auth_identity_uid
        self.account__account_email = account__account_email
        self.account__display_name = account__display_name
        self.account__account_address = account__account_address
        self.account__is_verified = account__is_verified
        self.account__is_system = account__is_system
        self.report_status__report_status_name = report_status__report_status_name
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.report_uid, self.report_name, self.tenant_uid, self.account_uid, self.report_status_uid, self.report_query, self.report_parameters, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes, self.tenant__tenant_name, self.tenant__country_uid, self.tenant__tenant_type_uid, self.tenant__tenant_category_uid, self.tenant__tenant_code, self.tenant__tenant_description, self.tenant__start_date, self.tenant__end_date, self.tenant__is_internal, self.tenant__is_system, self.tenant__is_test, self.tenant__account_uid, self.account__account_name, self.account__tenant_uid, self.account__account_type_uid, self.account__account_title_uid, self.account__account_division_uid, self.account__account_group_uid, self.account__auth_identity_uid, self.account__account_email, self.account__display_name, self.account__account_address, self.account__is_verified, self.account__is_system, self.report_status__report_status_name]


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
    def __init__(self, report_format_uid: str | None, report_format_name: str | None, class_name: str | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None):
        self.report_format_uid = report_format_uid
        self.report_format_name = report_format_name
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
        return [self.report_format_uid, self.report_format_name, self.class_name, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]


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
    tenant__tenant_name: str | None
    tenant__country_uid: str | None
    tenant__tenant_type_uid: str | None
    tenant__tenant_category_uid: str | None
    tenant__tenant_code: str | None
    tenant__tenant_description: str | None
    tenant__start_date: datetime.datetime | None
    tenant__end_date: datetime.datetime | None
    tenant__is_internal: int | None
    tenant__is_system: int | None
    tenant__is_test: int | None
    tenant__account_uid: str | None
    account__account_name: str | None
    account__tenant_uid: str | None
    account__account_type_uid: str | None
    account__account_title_uid: str | None
    account__account_division_uid: str | None
    account__account_group_uid: str | None
    account__auth_identity_uid: str | None
    account__account_email: str | None
    account__display_name: str | None
    account__account_address: str | None
    account__is_verified: int | None
    account__is_system: int | None
    report__report_name: str | None
    report__tenant_uid: str | None
    report__account_uid: str | None
    report__report_status_uid: str | None
    report__report_query: str | None
    report__report_parameters: str | None
    report_format__report_format_name: str | None
    report_format__class_name: str | None
    report_status__report_status_name: str | None
    report_content_type__report_content_type_name: str | None
    def __init__(self, report_run_uid: str | None, report_run_name: str | None, tenant_uid: str | None, account_uid: str | None, report_uid: str | None, report_format_uid: str | None, report_status_uid: str | None, report_content_type_uid: str | None, input_parameters_json: str | None, run_time_ms: int | None, returned_rows: int | None, content_size: int | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None, tenant__tenant_name: str | None, tenant__country_uid: str | None, tenant__tenant_type_uid: str | None, tenant__tenant_category_uid: str | None, tenant__tenant_code: str | None, tenant__tenant_description: str | None, tenant__start_date: datetime.datetime | None, tenant__end_date: datetime.datetime | None, tenant__is_internal: int | None, tenant__is_system: int | None, tenant__is_test: int | None, tenant__account_uid: str | None, account__account_name: str | None, account__tenant_uid: str | None, account__account_type_uid: str | None, account__account_title_uid: str | None, account__account_division_uid: str | None, account__account_group_uid: str | None, account__auth_identity_uid: str | None, account__account_email: str | None, account__display_name: str | None, account__account_address: str | None, account__is_verified: int | None, account__is_system: int | None, report__report_name: str | None, report__tenant_uid: str | None, report__account_uid: str | None, report__report_status_uid: str | None, report__report_query: str | None, report__report_parameters: str | None, report_format__report_format_name: str | None, report_format__class_name: str | None, report_status__report_status_name: str | None, report_content_type__report_content_type_name: str | None):
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
        self.tenant__tenant_name = tenant__tenant_name
        self.tenant__country_uid = tenant__country_uid
        self.tenant__tenant_type_uid = tenant__tenant_type_uid
        self.tenant__tenant_category_uid = tenant__tenant_category_uid
        self.tenant__tenant_code = tenant__tenant_code
        self.tenant__tenant_description = tenant__tenant_description
        self.tenant__start_date = tenant__start_date
        self.tenant__end_date = tenant__end_date
        self.tenant__is_internal = tenant__is_internal
        self.tenant__is_system = tenant__is_system
        self.tenant__is_test = tenant__is_test
        self.tenant__account_uid = tenant__account_uid
        self.account__account_name = account__account_name
        self.account__tenant_uid = account__tenant_uid
        self.account__account_type_uid = account__account_type_uid
        self.account__account_title_uid = account__account_title_uid
        self.account__account_division_uid = account__account_division_uid
        self.account__account_group_uid = account__account_group_uid
        self.account__auth_identity_uid = account__auth_identity_uid
        self.account__account_email = account__account_email
        self.account__display_name = account__display_name
        self.account__account_address = account__account_address
        self.account__is_verified = account__is_verified
        self.account__is_system = account__is_system
        self.report__report_name = report__report_name
        self.report__tenant_uid = report__tenant_uid
        self.report__account_uid = report__account_uid
        self.report__report_status_uid = report__report_status_uid
        self.report__report_query = report__report_query
        self.report__report_parameters = report__report_parameters
        self.report_format__report_format_name = report_format__report_format_name
        self.report_format__class_name = report_format__class_name
        self.report_status__report_status_name = report_status__report_status_name
        self.report_content_type__report_content_type_name = report_content_type__report_content_type_name
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.report_run_uid, self.report_run_name, self.tenant_uid, self.account_uid, self.report_uid, self.report_format_uid, self.report_status_uid, self.report_content_type_uid, self.input_parameters_json, self.run_time_ms, self.returned_rows, self.content_size, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes, self.tenant__tenant_name, self.tenant__country_uid, self.tenant__tenant_type_uid, self.tenant__tenant_category_uid, self.tenant__tenant_code, self.tenant__tenant_description, self.tenant__start_date, self.tenant__end_date, self.tenant__is_internal, self.tenant__is_system, self.tenant__is_test, self.tenant__account_uid, self.account__account_name, self.account__tenant_uid, self.account__account_type_uid, self.account__account_title_uid, self.account__account_division_uid, self.account__account_group_uid, self.account__auth_identity_uid, self.account__account_email, self.account__display_name, self.account__account_address, self.account__is_verified, self.account__is_system, self.report__report_name, self.report__tenant_uid, self.report__account_uid, self.report__report_status_uid, self.report__report_query, self.report__report_parameters, self.report_format__report_format_name, self.report_format__class_name, self.report_status__report_status_name, self.report_content_type__report_content_type_name]


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
    tenant_uid: str | None
    account_uid: str | None
    storage_type_uid: str | None
    storage_category_uid: str | None
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
    tenant__tenant_name: str | None
    tenant__country_uid: str | None
    tenant__tenant_type_uid: str | None
    tenant__tenant_category_uid: str | None
    tenant__tenant_code: str | None
    tenant__tenant_description: str | None
    tenant__start_date: datetime.datetime | None
    tenant__end_date: datetime.datetime | None
    tenant__is_internal: int | None
    tenant__is_system: int | None
    tenant__is_test: int | None
    tenant__account_uid: str | None
    account__account_name: str | None
    account__tenant_uid: str | None
    account__account_type_uid: str | None
    account__account_title_uid: str | None
    account__account_division_uid: str | None
    account__account_group_uid: str | None
    account__auth_identity_uid: str | None
    account__account_email: str | None
    account__display_name: str | None
    account__account_address: str | None
    account__is_verified: int | None
    account__is_system: int | None
    storage_type__storage_type_name: str | None
    storage_type__storage_class: str | None
    storage_category__storage_category_name: str | None
    def __init__(self, storage_uid: str | None, storage_name: str | None, tenant_uid: str | None, account_uid: str | None, storage_type_uid: str | None, storage_category_uid: str | None, storage_parameters_json: str | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None, tenant__tenant_name: str | None, tenant__country_uid: str | None, tenant__tenant_type_uid: str | None, tenant__tenant_category_uid: str | None, tenant__tenant_code: str | None, tenant__tenant_description: str | None, tenant__start_date: datetime.datetime | None, tenant__end_date: datetime.datetime | None, tenant__is_internal: int | None, tenant__is_system: int | None, tenant__is_test: int | None, tenant__account_uid: str | None, account__account_name: str | None, account__tenant_uid: str | None, account__account_type_uid: str | None, account__account_title_uid: str | None, account__account_division_uid: str | None, account__account_group_uid: str | None, account__auth_identity_uid: str | None, account__account_email: str | None, account__display_name: str | None, account__account_address: str | None, account__is_verified: int | None, account__is_system: int | None, storage_type__storage_type_name: str | None, storage_type__storage_class: str | None, storage_category__storage_category_name: str | None):
        self.storage_uid = storage_uid
        self.storage_name = storage_name
        self.tenant_uid = tenant_uid
        self.account_uid = account_uid
        self.storage_type_uid = storage_type_uid
        self.storage_category_uid = storage_category_uid
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
        self.tenant__tenant_name = tenant__tenant_name
        self.tenant__country_uid = tenant__country_uid
        self.tenant__tenant_type_uid = tenant__tenant_type_uid
        self.tenant__tenant_category_uid = tenant__tenant_category_uid
        self.tenant__tenant_code = tenant__tenant_code
        self.tenant__tenant_description = tenant__tenant_description
        self.tenant__start_date = tenant__start_date
        self.tenant__end_date = tenant__end_date
        self.tenant__is_internal = tenant__is_internal
        self.tenant__is_system = tenant__is_system
        self.tenant__is_test = tenant__is_test
        self.tenant__account_uid = tenant__account_uid
        self.account__account_name = account__account_name
        self.account__tenant_uid = account__tenant_uid
        self.account__account_type_uid = account__account_type_uid
        self.account__account_title_uid = account__account_title_uid
        self.account__account_division_uid = account__account_division_uid
        self.account__account_group_uid = account__account_group_uid
        self.account__auth_identity_uid = account__auth_identity_uid
        self.account__account_email = account__account_email
        self.account__display_name = account__display_name
        self.account__account_address = account__account_address
        self.account__is_verified = account__is_verified
        self.account__is_system = account__is_system
        self.storage_type__storage_type_name = storage_type__storage_type_name
        self.storage_type__storage_class = storage_type__storage_class
        self.storage_category__storage_category_name = storage_category__storage_category_name
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.storage_uid, self.storage_name, self.tenant_uid, self.account_uid, self.storage_type_uid, self.storage_category_uid, self.storage_parameters_json, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes, self.tenant__tenant_name, self.tenant__country_uid, self.tenant__tenant_type_uid, self.tenant__tenant_category_uid, self.tenant__tenant_code, self.tenant__tenant_description, self.tenant__start_date, self.tenant__end_date, self.tenant__is_internal, self.tenant__is_system, self.tenant__is_test, self.tenant__account_uid, self.account__account_name, self.account__tenant_uid, self.account__account_type_uid, self.account__account_title_uid, self.account__account_division_uid, self.account__account_group_uid, self.account__auth_identity_uid, self.account__account_email, self.account__display_name, self.account__account_address, self.account__is_verified, self.account__is_system, self.storage_type__storage_type_name, self.storage_type__storage_class, self.storage_category__storage_category_name]


@dataclass(frozen=False)
class storage_category_rich_dto(storage_category_read_dto):
    storage_category_uid: str | None
    storage_category_name: str | None
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
    def __init__(self, storage_category_uid: str | None, storage_category_name: str | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None):
        self.storage_category_uid = storage_category_uid
        self.storage_category_name = storage_category_name
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
        return [self.storage_category_uid, self.storage_category_name, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]


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
    storage__storage_name: str | None
    storage__tenant_uid: str | None
    storage__account_uid: str | None
    storage__storage_type_uid: str | None
    storage__storage_category_uid: str | None
    storage__storage_parameters_json: str | None
    def __init__(self, storage_connection_uid: str | None, storage_connection_name: str | None, storage_uid: str | None, connection_type: str | None, storage_parameters_json: str | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None, storage__storage_name: str | None, storage__tenant_uid: str | None, storage__account_uid: str | None, storage__storage_type_uid: str | None, storage__storage_category_uid: str | None, storage__storage_parameters_json: str | None):
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
        self.storage__storage_name = storage__storage_name
        self.storage__tenant_uid = storage__tenant_uid
        self.storage__account_uid = storage__account_uid
        self.storage__storage_type_uid = storage__storage_type_uid
        self.storage__storage_category_uid = storage__storage_category_uid
        self.storage__storage_parameters_json = storage__storage_parameters_json
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.storage_connection_uid, self.storage_connection_name, self.storage_uid, self.connection_type, self.storage_parameters_json, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes, self.storage__storage_name, self.storage__tenant_uid, self.storage__account_uid, self.storage__storage_type_uid, self.storage__storage_category_uid, self.storage__storage_parameters_json]


@dataclass(frozen=False)
class storage_query_rich_dto(storage_query_read_dto):
    storage_query_uid: str | None
    storage_query_name: str | None
    storage_uid: str | None
    query_content: str | None
    query_parameters_json: str | None
    execution_status: str | None
    execution_time: int | None
    execution_rows: int | None
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
    storage__storage_name: str | None
    storage__tenant_uid: str | None
    storage__account_uid: str | None
    storage__storage_type_uid: str | None
    storage__storage_category_uid: str | None
    storage__storage_parameters_json: str | None
    def __init__(self, storage_query_uid: str | None, storage_query_name: str | None, storage_uid: str | None, query_content: str | None, query_parameters_json: str | None, execution_status: str | None, execution_time: int | None, execution_rows: int | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None, storage__storage_name: str | None, storage__tenant_uid: str | None, storage__account_uid: str | None, storage__storage_type_uid: str | None, storage__storage_category_uid: str | None, storage__storage_parameters_json: str | None):
        self.storage_query_uid = storage_query_uid
        self.storage_query_name = storage_query_name
        self.storage_uid = storage_uid
        self.query_content = query_content
        self.query_parameters_json = query_parameters_json
        self.execution_status = execution_status
        self.execution_time = execution_time
        self.execution_rows = execution_rows
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
        self.storage__storage_name = storage__storage_name
        self.storage__tenant_uid = storage__tenant_uid
        self.storage__account_uid = storage__account_uid
        self.storage__storage_type_uid = storage__storage_type_uid
        self.storage__storage_category_uid = storage__storage_category_uid
        self.storage__storage_parameters_json = storage__storage_parameters_json
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.storage_query_uid, self.storage_query_name, self.storage_uid, self.query_content, self.query_parameters_json, self.execution_status, self.execution_time, self.execution_rows, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes, self.storage__storage_name, self.storage__tenant_uid, self.storage__account_uid, self.storage__storage_type_uid, self.storage__storage_category_uid, self.storage__storage_parameters_json]


@dataclass(frozen=False)
class storage_type_rich_dto(storage_type_read_dto):
    storage_type_uid: str | None
    storage_type_name: str | None
    storage_class: str | None
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
    def __init__(self, storage_type_uid: str | None, storage_type_name: str | None, storage_class: str | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None):
        self.storage_type_uid = storage_type_uid
        self.storage_type_name = storage_type_name
        self.storage_class = storage_class
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
        return [self.storage_type_uid, self.storage_type_name, self.storage_class, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]


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
    tenant__tenant_name: str | None
    tenant__country_uid: str | None
    tenant__tenant_type_uid: str | None
    tenant__tenant_category_uid: str | None
    tenant__tenant_code: str | None
    tenant__tenant_description: str | None
    tenant__start_date: datetime.datetime | None
    tenant__end_date: datetime.datetime | None
    tenant__is_internal: int | None
    tenant__is_system: int | None
    tenant__is_test: int | None
    tenant__account_uid: str | None
    synchronization_type__synchronization_type_name: str | None
    synchronization_type__sync_type: str | None
    synchronization_type__sync_class_name: str | None
    storage__storage_name: str | None
    storage__tenant_uid: str | None
    storage__account_uid: str | None
    storage__storage_type_uid: str | None
    storage__storage_category_uid: str | None
    storage__storage_parameters_json: str | None
    def __init__(self, synchronization_uid: str | None, synchronization_name: str | None, tenant_uid: str | None, synchronization_type_uid: str | None, storage_uid: str | None, sync_expression: str | None, sync_query: str | None, sync_definition: str | None, sync_priority: int | None, last_run_date: datetime.datetime | None, last_run_seconds: str | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None, tenant__tenant_name: str | None, tenant__country_uid: str | None, tenant__tenant_type_uid: str | None, tenant__tenant_category_uid: str | None, tenant__tenant_code: str | None, tenant__tenant_description: str | None, tenant__start_date: datetime.datetime | None, tenant__end_date: datetime.datetime | None, tenant__is_internal: int | None, tenant__is_system: int | None, tenant__is_test: int | None, tenant__account_uid: str | None, synchronization_type__synchronization_type_name: str | None, synchronization_type__sync_type: str | None, synchronization_type__sync_class_name: str | None, storage__storage_name: str | None, storage__tenant_uid: str | None, storage__account_uid: str | None, storage__storage_type_uid: str | None, storage__storage_category_uid: str | None, storage__storage_parameters_json: str | None):
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
        self.tenant__tenant_name = tenant__tenant_name
        self.tenant__country_uid = tenant__country_uid
        self.tenant__tenant_type_uid = tenant__tenant_type_uid
        self.tenant__tenant_category_uid = tenant__tenant_category_uid
        self.tenant__tenant_code = tenant__tenant_code
        self.tenant__tenant_description = tenant__tenant_description
        self.tenant__start_date = tenant__start_date
        self.tenant__end_date = tenant__end_date
        self.tenant__is_internal = tenant__is_internal
        self.tenant__is_system = tenant__is_system
        self.tenant__is_test = tenant__is_test
        self.tenant__account_uid = tenant__account_uid
        self.synchronization_type__synchronization_type_name = synchronization_type__synchronization_type_name
        self.synchronization_type__sync_type = synchronization_type__sync_type
        self.synchronization_type__sync_class_name = synchronization_type__sync_class_name
        self.storage__storage_name = storage__storage_name
        self.storage__tenant_uid = storage__tenant_uid
        self.storage__account_uid = storage__account_uid
        self.storage__storage_type_uid = storage__storage_type_uid
        self.storage__storage_category_uid = storage__storage_category_uid
        self.storage__storage_parameters_json = storage__storage_parameters_json
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.synchronization_uid, self.synchronization_name, self.tenant_uid, self.synchronization_type_uid, self.storage_uid, self.sync_expression, self.sync_query, self.sync_definition, self.sync_priority, self.last_run_date, self.last_run_seconds, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes, self.tenant__tenant_name, self.tenant__country_uid, self.tenant__tenant_type_uid, self.tenant__tenant_category_uid, self.tenant__tenant_code, self.tenant__tenant_description, self.tenant__start_date, self.tenant__end_date, self.tenant__is_internal, self.tenant__is_system, self.tenant__is_test, self.tenant__account_uid, self.synchronization_type__synchronization_type_name, self.synchronization_type__sync_type, self.synchronization_type__sync_class_name, self.storage__storage_name, self.storage__tenant_uid, self.storage__account_uid, self.storage__storage_type_uid, self.storage__storage_category_uid, self.storage__storage_parameters_json]


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
    synchronization__synchronization_name: str | None
    synchronization__tenant_uid: str | None
    synchronization__synchronization_type_uid: str | None
    synchronization__storage_uid: str | None
    synchronization__sync_expression: str | None
    synchronization__sync_query: str | None
    synchronization__sync_definition: str | None
    synchronization__sync_priority: int | None
    synchronization__last_run_date: datetime.datetime | None
    synchronization__last_run_seconds: str | None
    def __init__(self, synchronization_run_uid: str | None, synchronization_run_name: str | None, synchronization_uid: str | None, run_status: str | None, run_time_seconds: str | None, copied_items: int | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None, synchronization__synchronization_name: str | None, synchronization__tenant_uid: str | None, synchronization__synchronization_type_uid: str | None, synchronization__storage_uid: str | None, synchronization__sync_expression: str | None, synchronization__sync_query: str | None, synchronization__sync_definition: str | None, synchronization__sync_priority: int | None, synchronization__last_run_date: datetime.datetime | None, synchronization__last_run_seconds: str | None):
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
        self.synchronization__synchronization_name = synchronization__synchronization_name
        self.synchronization__tenant_uid = synchronization__tenant_uid
        self.synchronization__synchronization_type_uid = synchronization__synchronization_type_uid
        self.synchronization__storage_uid = synchronization__storage_uid
        self.synchronization__sync_expression = synchronization__sync_expression
        self.synchronization__sync_query = synchronization__sync_query
        self.synchronization__sync_definition = synchronization__sync_definition
        self.synchronization__sync_priority = synchronization__sync_priority
        self.synchronization__last_run_date = synchronization__last_run_date
        self.synchronization__last_run_seconds = synchronization__last_run_seconds
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.synchronization_run_uid, self.synchronization_run_name, self.synchronization_uid, self.run_status, self.run_time_seconds, self.copied_items, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes, self.synchronization__synchronization_name, self.synchronization__tenant_uid, self.synchronization__synchronization_type_uid, self.synchronization__storage_uid, self.synchronization__sync_expression, self.synchronization__sync_query, self.synchronization__sync_definition, self.synchronization__sync_priority, self.synchronization__last_run_date, self.synchronization__last_run_seconds]


@dataclass(frozen=False)
class synchronization_type_rich_dto(synchronization_type_read_dto):
    synchronization_type_uid: str | None
    synchronization_type_name: str | None
    sync_type: str | None
    sync_class_name: str | None
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
    def __init__(self, synchronization_type_uid: str | None, synchronization_type_name: str | None, sync_type: str | None, sync_class_name: str | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None):
        self.synchronization_type_uid = synchronization_type_uid
        self.synchronization_type_name = synchronization_type_name
        self.sync_type = sync_type
        self.sync_class_name = sync_class_name
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
        return [self.synchronization_type_uid, self.synchronization_type_name, self.sync_type, self.sync_class_name, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]


@dataclass(frozen=False)
class system_attribute_rich_dto(system_attribute_read_dto):
    system_attribute_uid: str | None
    system_attribute_name: str | None
    system_table_uid: str | None
    column_name: str | None
    attribute_type: str | None
    attribute_category: str | None
    attribute_label: str | None
    attribute_description: str | None
    ordinal_position: int | None
    is_hidden: int | None
    is_meta: int | None
    is_secret: int | None
    is_full_search: int | None
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
    system_table__system_table_name: str | None
    system_table__parent_system_table_uid: str | None
    system_table__table_label: str | None
    system_table__uid_name: str | None
    system_table__table_group: str | None
    system_table__table_code: str | None
    system_table__table_type: str | None
    system_table__table_category: str | None
    system_table__cardinality: int | None
    system_table__is_object: int | None
    system_table__is_rich: int | None
    system_table__is_tenant: int | None
    system_table__is_local: int | None
    system_table__table_comment: str | None
    def __init__(self, system_attribute_uid: str | None, system_attribute_name: str | None, system_table_uid: str | None, column_name: str | None, attribute_type: str | None, attribute_category: str | None, attribute_label: str | None, attribute_description: str | None, ordinal_position: int | None, is_hidden: int | None, is_meta: int | None, is_secret: int | None, is_full_search: int | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None, system_table__system_table_name: str | None, system_table__parent_system_table_uid: str | None, system_table__table_label: str | None, system_table__uid_name: str | None, system_table__table_group: str | None, system_table__table_code: str | None, system_table__table_type: str | None, system_table__table_category: str | None, system_table__cardinality: int | None, system_table__is_object: int | None, system_table__is_rich: int | None, system_table__is_tenant: int | None, system_table__is_local: int | None, system_table__table_comment: str | None):
        self.system_attribute_uid = system_attribute_uid
        self.system_attribute_name = system_attribute_name
        self.system_table_uid = system_table_uid
        self.column_name = column_name
        self.attribute_type = attribute_type
        self.attribute_category = attribute_category
        self.attribute_label = attribute_label
        self.attribute_description = attribute_description
        self.ordinal_position = ordinal_position
        self.is_hidden = is_hidden
        self.is_meta = is_meta
        self.is_secret = is_secret
        self.is_full_search = is_full_search
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
        self.system_table__system_table_name = system_table__system_table_name
        self.system_table__parent_system_table_uid = system_table__parent_system_table_uid
        self.system_table__table_label = system_table__table_label
        self.system_table__uid_name = system_table__uid_name
        self.system_table__table_group = system_table__table_group
        self.system_table__table_code = system_table__table_code
        self.system_table__table_type = system_table__table_type
        self.system_table__table_category = system_table__table_category
        self.system_table__cardinality = system_table__cardinality
        self.system_table__is_object = system_table__is_object
        self.system_table__is_rich = system_table__is_rich
        self.system_table__is_tenant = system_table__is_tenant
        self.system_table__is_local = system_table__is_local
        self.system_table__table_comment = system_table__table_comment
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.system_attribute_uid, self.system_attribute_name, self.system_table_uid, self.column_name, self.attribute_type, self.attribute_category, self.attribute_label, self.attribute_description, self.ordinal_position, self.is_hidden, self.is_meta, self.is_secret, self.is_full_search, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes, self.system_table__system_table_name, self.system_table__parent_system_table_uid, self.system_table__table_label, self.system_table__uid_name, self.system_table__table_group, self.system_table__table_code, self.system_table__table_type, self.system_table__table_category, self.system_table__cardinality, self.system_table__is_object, self.system_table__is_rich, self.system_table__is_tenant, self.system_table__is_local, self.system_table__table_comment]


@dataclass(frozen=False)
class system_constraint_rich_dto(system_constraint_read_dto):
    system_constraint_uid: str | None
    system_constraint_name: str | None
    system_table_uid: str | None
    system_attribute_uid: str | None
    tenant_uid: str | None
    constraint_class: str | None
    constraint_params_json: str | None
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
    system_table__system_table_name: str | None
    system_table__parent_system_table_uid: str | None
    system_table__table_label: str | None
    system_table__uid_name: str | None
    system_table__table_group: str | None
    system_table__table_code: str | None
    system_table__table_type: str | None
    system_table__table_category: str | None
    system_table__cardinality: int | None
    system_table__is_object: int | None
    system_table__is_rich: int | None
    system_table__is_tenant: int | None
    system_table__is_local: int | None
    system_table__table_comment: str | None
    system_attribute__system_attribute_name: str | None
    system_attribute__system_table_uid: str | None
    system_attribute__column_name: str | None
    system_attribute__attribute_type: str | None
    system_attribute__attribute_category: str | None
    system_attribute__attribute_label: str | None
    system_attribute__attribute_description: str | None
    system_attribute__ordinal_position: int | None
    system_attribute__is_hidden: int | None
    system_attribute__is_meta: int | None
    system_attribute__is_secret: int | None
    system_attribute__is_full_search: int | None
    tenant__tenant_name: str | None
    tenant__country_uid: str | None
    tenant__tenant_type_uid: str | None
    tenant__tenant_category_uid: str | None
    tenant__tenant_code: str | None
    tenant__tenant_description: str | None
    tenant__start_date: datetime.datetime | None
    tenant__end_date: datetime.datetime | None
    tenant__is_internal: int | None
    tenant__is_system: int | None
    tenant__is_test: int | None
    tenant__account_uid: str | None
    def __init__(self, system_constraint_uid: str | None, system_constraint_name: str | None, system_table_uid: str | None, system_attribute_uid: str | None, tenant_uid: str | None, constraint_class: str | None, constraint_params_json: str | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None, system_table__system_table_name: str | None, system_table__parent_system_table_uid: str | None, system_table__table_label: str | None, system_table__uid_name: str | None, system_table__table_group: str | None, system_table__table_code: str | None, system_table__table_type: str | None, system_table__table_category: str | None, system_table__cardinality: int | None, system_table__is_object: int | None, system_table__is_rich: int | None, system_table__is_tenant: int | None, system_table__is_local: int | None, system_table__table_comment: str | None, system_attribute__system_attribute_name: str | None, system_attribute__system_table_uid: str | None, system_attribute__column_name: str | None, system_attribute__attribute_type: str | None, system_attribute__attribute_category: str | None, system_attribute__attribute_label: str | None, system_attribute__attribute_description: str | None, system_attribute__ordinal_position: int | None, system_attribute__is_hidden: int | None, system_attribute__is_meta: int | None, system_attribute__is_secret: int | None, system_attribute__is_full_search: int | None, tenant__tenant_name: str | None, tenant__country_uid: str | None, tenant__tenant_type_uid: str | None, tenant__tenant_category_uid: str | None, tenant__tenant_code: str | None, tenant__tenant_description: str | None, tenant__start_date: datetime.datetime | None, tenant__end_date: datetime.datetime | None, tenant__is_internal: int | None, tenant__is_system: int | None, tenant__is_test: int | None, tenant__account_uid: str | None):
        self.system_constraint_uid = system_constraint_uid
        self.system_constraint_name = system_constraint_name
        self.system_table_uid = system_table_uid
        self.system_attribute_uid = system_attribute_uid
        self.tenant_uid = tenant_uid
        self.constraint_class = constraint_class
        self.constraint_params_json = constraint_params_json
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
        self.system_table__system_table_name = system_table__system_table_name
        self.system_table__parent_system_table_uid = system_table__parent_system_table_uid
        self.system_table__table_label = system_table__table_label
        self.system_table__uid_name = system_table__uid_name
        self.system_table__table_group = system_table__table_group
        self.system_table__table_code = system_table__table_code
        self.system_table__table_type = system_table__table_type
        self.system_table__table_category = system_table__table_category
        self.system_table__cardinality = system_table__cardinality
        self.system_table__is_object = system_table__is_object
        self.system_table__is_rich = system_table__is_rich
        self.system_table__is_tenant = system_table__is_tenant
        self.system_table__is_local = system_table__is_local
        self.system_table__table_comment = system_table__table_comment
        self.system_attribute__system_attribute_name = system_attribute__system_attribute_name
        self.system_attribute__system_table_uid = system_attribute__system_table_uid
        self.system_attribute__column_name = system_attribute__column_name
        self.system_attribute__attribute_type = system_attribute__attribute_type
        self.system_attribute__attribute_category = system_attribute__attribute_category
        self.system_attribute__attribute_label = system_attribute__attribute_label
        self.system_attribute__attribute_description = system_attribute__attribute_description
        self.system_attribute__ordinal_position = system_attribute__ordinal_position
        self.system_attribute__is_hidden = system_attribute__is_hidden
        self.system_attribute__is_meta = system_attribute__is_meta
        self.system_attribute__is_secret = system_attribute__is_secret
        self.system_attribute__is_full_search = system_attribute__is_full_search
        self.tenant__tenant_name = tenant__tenant_name
        self.tenant__country_uid = tenant__country_uid
        self.tenant__tenant_type_uid = tenant__tenant_type_uid
        self.tenant__tenant_category_uid = tenant__tenant_category_uid
        self.tenant__tenant_code = tenant__tenant_code
        self.tenant__tenant_description = tenant__tenant_description
        self.tenant__start_date = tenant__start_date
        self.tenant__end_date = tenant__end_date
        self.tenant__is_internal = tenant__is_internal
        self.tenant__is_system = tenant__is_system
        self.tenant__is_test = tenant__is_test
        self.tenant__account_uid = tenant__account_uid
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.system_constraint_uid, self.system_constraint_name, self.system_table_uid, self.system_attribute_uid, self.tenant_uid, self.constraint_class, self.constraint_params_json, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes, self.system_table__system_table_name, self.system_table__parent_system_table_uid, self.system_table__table_label, self.system_table__uid_name, self.system_table__table_group, self.system_table__table_code, self.system_table__table_type, self.system_table__table_category, self.system_table__cardinality, self.system_table__is_object, self.system_table__is_rich, self.system_table__is_tenant, self.system_table__is_local, self.system_table__table_comment, self.system_attribute__system_attribute_name, self.system_attribute__system_table_uid, self.system_attribute__column_name, self.system_attribute__attribute_type, self.system_attribute__attribute_category, self.system_attribute__attribute_label, self.system_attribute__attribute_description, self.system_attribute__ordinal_position, self.system_attribute__is_hidden, self.system_attribute__is_meta, self.system_attribute__is_secret, self.system_attribute__is_full_search, self.tenant__tenant_name, self.tenant__country_uid, self.tenant__tenant_type_uid, self.tenant__tenant_category_uid, self.tenant__tenant_code, self.tenant__tenant_description, self.tenant__start_date, self.tenant__end_date, self.tenant__is_internal, self.tenant__is_system, self.tenant__is_test, self.tenant__account_uid]


@dataclass(frozen=False)
class system_database_rich_dto(system_database_read_dto):
    system_database_uid: str | None
    system_database_name: str | None
    db_url: str | None
    db_host: str | None
    db_name: str | None
    db_user: str | None
    last_status_name: str | None
    last_db_size: int | None
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
    def __init__(self, system_database_uid: str | None, system_database_name: str | None, db_url: str | None, db_host: str | None, db_name: str | None, db_user: str | None, last_status_name: str | None, last_db_size: int | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None):
        self.system_database_uid = system_database_uid
        self.system_database_name = system_database_name
        self.db_url = db_url
        self.db_host = db_host
        self.db_name = db_name
        self.db_user = db_user
        self.last_status_name = last_status_name
        self.last_db_size = last_db_size
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
        return [self.system_database_uid, self.system_database_name, self.db_url, self.db_host, self.db_name, self.db_user, self.last_status_name, self.last_db_size, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]


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
    system_version__system_version_name: str | None
    system_version__version_description: str | None
    def __init__(self, system_instance_uid: str | None, system_instance_name: str | None, system_version_uid: str | None, host_name: str | None, host_ip: str | None, local_path: str | None, mode_name: str | None, ticks_count: int | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None, system_version__system_version_name: str | None, system_version__version_description: str | None):
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
        self.system_version__system_version_name = system_version__system_version_name
        self.system_version__version_description = system_version__version_description
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.system_instance_uid, self.system_instance_name, self.system_version_uid, self.host_name, self.host_ip, self.local_path, self.mode_name, self.ticks_count, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes, self.system_version__system_version_name, self.system_version__version_description]


@dataclass(frozen=False)
class system_license_rich_dto(system_license_read_dto):
    system_license_uid: str | None
    system_license_name: str | None
    class_name: str | None
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
    def __init__(self, system_license_uid: str | None, system_license_name: str | None, class_name: str | None, license_description: str | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None):
        self.system_license_uid = system_license_uid
        self.system_license_name = system_license_name
        self.class_name = class_name
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
        return [self.system_license_uid, self.system_license_name, self.class_name, self.license_description, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]


@dataclass(frozen=False)
class system_lock_rich_dto(system_lock_read_dto):
    system_lock_uid: str | None
    system_lock_name: str | None
    lock_account_uid: str | None
    lock_comment: str | None
    lock_reason: str | None
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
    lock_account__account_name: str | None
    lock_account__tenant_uid: str | None
    lock_account__account_type_uid: str | None
    lock_account__account_title_uid: str | None
    lock_account__account_division_uid: str | None
    lock_account__account_group_uid: str | None
    lock_account__auth_identity_uid: str | None
    lock_account__account_email: str | None
    lock_account__display_name: str | None
    lock_account__account_address: str | None
    lock_account__is_verified: int | None
    lock_account__is_system: int | None
    def __init__(self, system_lock_uid: str | None, system_lock_name: str | None, lock_account_uid: str | None, lock_comment: str | None, lock_reason: str | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None, lock_account__account_name: str | None, lock_account__tenant_uid: str | None, lock_account__account_type_uid: str | None, lock_account__account_title_uid: str | None, lock_account__account_division_uid: str | None, lock_account__account_group_uid: str | None, lock_account__auth_identity_uid: str | None, lock_account__account_email: str | None, lock_account__display_name: str | None, lock_account__account_address: str | None, lock_account__is_verified: int | None, lock_account__is_system: int | None):
        self.system_lock_uid = system_lock_uid
        self.system_lock_name = system_lock_name
        self.lock_account_uid = lock_account_uid
        self.lock_comment = lock_comment
        self.lock_reason = lock_reason
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
        self.lock_account__account_name = lock_account__account_name
        self.lock_account__tenant_uid = lock_account__tenant_uid
        self.lock_account__account_type_uid = lock_account__account_type_uid
        self.lock_account__account_title_uid = lock_account__account_title_uid
        self.lock_account__account_division_uid = lock_account__account_division_uid
        self.lock_account__account_group_uid = lock_account__account_group_uid
        self.lock_account__auth_identity_uid = lock_account__auth_identity_uid
        self.lock_account__account_email = lock_account__account_email
        self.lock_account__display_name = lock_account__display_name
        self.lock_account__account_address = lock_account__account_address
        self.lock_account__is_verified = lock_account__is_verified
        self.lock_account__is_system = lock_account__is_system
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.system_lock_uid, self.system_lock_name, self.lock_account_uid, self.lock_comment, self.lock_reason, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes, self.lock_account__account_name, self.lock_account__tenant_uid, self.lock_account__account_type_uid, self.lock_account__account_title_uid, self.lock_account__account_division_uid, self.lock_account__account_group_uid, self.lock_account__auth_identity_uid, self.lock_account__account_email, self.lock_account__display_name, self.lock_account__account_address, self.lock_account__is_verified, self.lock_account__is_system]


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
    account__account_name: str | None
    account__tenant_uid: str | None
    account__account_type_uid: str | None
    account__account_title_uid: str | None
    account__account_division_uid: str | None
    account__account_group_uid: str | None
    account__auth_identity_uid: str | None
    account__account_email: str | None
    account__display_name: str | None
    account__account_address: str | None
    account__is_verified: int | None
    account__is_system: int | None
    def __init__(self, system_request_uid: str | None, system_request_name: str | None, account_uid: str | None, request_method: str | None, request_url: str | None, request_body_size: int | None, request_host: str | None, request_time: int | None, response_code: int | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None, account__account_name: str | None, account__tenant_uid: str | None, account__account_type_uid: str | None, account__account_title_uid: str | None, account__account_division_uid: str | None, account__account_group_uid: str | None, account__auth_identity_uid: str | None, account__account_email: str | None, account__display_name: str | None, account__account_address: str | None, account__is_verified: int | None, account__is_system: int | None):
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
        self.account__account_name = account__account_name
        self.account__tenant_uid = account__tenant_uid
        self.account__account_type_uid = account__account_type_uid
        self.account__account_title_uid = account__account_title_uid
        self.account__account_division_uid = account__account_division_uid
        self.account__account_group_uid = account__account_group_uid
        self.account__auth_identity_uid = account__auth_identity_uid
        self.account__account_email = account__account_email
        self.account__display_name = account__display_name
        self.account__account_address = account__account_address
        self.account__is_verified = account__is_verified
        self.account__is_system = account__is_system
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.system_request_uid, self.system_request_name, self.account_uid, self.request_method, self.request_url, self.request_body_size, self.request_host, self.request_time, self.response_code, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes, self.account__account_name, self.account__tenant_uid, self.account__account_type_uid, self.account__account_title_uid, self.account__account_division_uid, self.account__account_group_uid, self.account__auth_identity_uid, self.account__account_email, self.account__display_name, self.account__account_address, self.account__is_verified, self.account__is_system]


@dataclass(frozen=False)
class system_setting_rich_dto(system_setting_read_dto):
    system_setting_uid: str | None
    system_setting_name: str | None
    setting_value: str | None
    setting_type: str | None
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
    def __init__(self, system_setting_uid: str | None, system_setting_name: str | None, setting_value: str | None, setting_type: str | None, is_public: int | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None):
        self.system_setting_uid = system_setting_uid
        self.system_setting_name = system_setting_name
        self.setting_value = setting_value
        self.setting_type = setting_type
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
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.system_setting_uid, self.system_setting_name, self.setting_value, self.setting_type, self.is_public, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]


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
    system_setting_account__account_name: str | None
    system_setting_account__tenant_uid: str | None
    system_setting_account__account_type_uid: str | None
    system_setting_account__account_title_uid: str | None
    system_setting_account__account_division_uid: str | None
    system_setting_account__account_group_uid: str | None
    system_setting_account__auth_identity_uid: str | None
    system_setting_account__account_email: str | None
    system_setting_account__display_name: str | None
    system_setting_account__account_address: str | None
    system_setting_account__is_verified: int | None
    system_setting_account__is_system: int | None
    account__account_name: str | None
    account__tenant_uid: str | None
    account__account_type_uid: str | None
    account__account_title_uid: str | None
    account__account_division_uid: str | None
    account__account_group_uid: str | None
    account__auth_identity_uid: str | None
    account__account_email: str | None
    account__display_name: str | None
    account__account_address: str | None
    account__is_verified: int | None
    account__is_system: int | None
    def __init__(self, system_setting_account_uid: str | None, system_setting_account_name: str | None, account_uid: str | None, setting_value: str | None, is_public: int | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None, system_setting_account__account_name: str | None, system_setting_account__tenant_uid: str | None, system_setting_account__account_type_uid: str | None, system_setting_account__account_title_uid: str | None, system_setting_account__account_division_uid: str | None, system_setting_account__account_group_uid: str | None, system_setting_account__auth_identity_uid: str | None, system_setting_account__account_email: str | None, system_setting_account__display_name: str | None, system_setting_account__account_address: str | None, system_setting_account__is_verified: int | None, system_setting_account__is_system: int | None, account__account_name: str | None, account__tenant_uid: str | None, account__account_type_uid: str | None, account__account_title_uid: str | None, account__account_division_uid: str | None, account__account_group_uid: str | None, account__auth_identity_uid: str | None, account__account_email: str | None, account__display_name: str | None, account__account_address: str | None, account__is_verified: int | None, account__is_system: int | None):
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
        self.system_setting_account__account_name = system_setting_account__account_name
        self.system_setting_account__tenant_uid = system_setting_account__tenant_uid
        self.system_setting_account__account_type_uid = system_setting_account__account_type_uid
        self.system_setting_account__account_title_uid = system_setting_account__account_title_uid
        self.system_setting_account__account_division_uid = system_setting_account__account_division_uid
        self.system_setting_account__account_group_uid = system_setting_account__account_group_uid
        self.system_setting_account__auth_identity_uid = system_setting_account__auth_identity_uid
        self.system_setting_account__account_email = system_setting_account__account_email
        self.system_setting_account__display_name = system_setting_account__display_name
        self.system_setting_account__account_address = system_setting_account__account_address
        self.system_setting_account__is_verified = system_setting_account__is_verified
        self.system_setting_account__is_system = system_setting_account__is_system
        self.account__account_name = account__account_name
        self.account__tenant_uid = account__tenant_uid
        self.account__account_type_uid = account__account_type_uid
        self.account__account_title_uid = account__account_title_uid
        self.account__account_division_uid = account__account_division_uid
        self.account__account_group_uid = account__account_group_uid
        self.account__auth_identity_uid = account__auth_identity_uid
        self.account__account_email = account__account_email
        self.account__display_name = account__display_name
        self.account__account_address = account__account_address
        self.account__is_verified = account__is_verified
        self.account__is_system = account__is_system
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.system_setting_account_uid, self.system_setting_account_name, self.account_uid, self.setting_value, self.is_public, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes, self.system_setting_account__account_name, self.system_setting_account__tenant_uid, self.system_setting_account__account_type_uid, self.system_setting_account__account_title_uid, self.system_setting_account__account_division_uid, self.system_setting_account__account_group_uid, self.system_setting_account__auth_identity_uid, self.system_setting_account__account_email, self.system_setting_account__display_name, self.system_setting_account__account_address, self.system_setting_account__is_verified, self.system_setting_account__is_system, self.account__account_name, self.account__tenant_uid, self.account__account_type_uid, self.account__account_title_uid, self.account__account_division_uid, self.account__account_group_uid, self.account__auth_identity_uid, self.account__account_email, self.account__display_name, self.account__account_address, self.account__is_verified, self.account__is_system]


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
    table_label: str | None
    uid_name: str | None
    table_group: str | None
    table_code: str | None
    table_type: str | None
    table_category: str | None
    cardinality: int | None
    is_object: int | None
    is_rich: int | None
    is_tenant: int | None
    is_local: int | None
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
    def __init__(self, system_table_uid: str | None, system_table_name: str | None, parent_system_table_uid: str | None, table_label: str | None, uid_name: str | None, table_group: str | None, table_code: str | None, table_type: str | None, table_category: str | None, cardinality: int | None, is_object: int | None, is_rich: int | None, is_tenant: int | None, is_local: int | None, table_comment: str | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None):
        self.system_table_uid = system_table_uid
        self.system_table_name = system_table_name
        self.parent_system_table_uid = parent_system_table_uid
        self.table_label = table_label
        self.uid_name = uid_name
        self.table_group = table_group
        self.table_code = table_code
        self.table_type = table_type
        self.table_category = table_category
        self.cardinality = cardinality
        self.is_object = is_object
        self.is_rich = is_rich
        self.is_tenant = is_tenant
        self.is_local = is_local
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
        return [self.system_table_uid, self.system_table_name, self.parent_system_table_uid, self.table_label, self.uid_name, self.table_group, self.table_code, self.table_type, self.table_category, self.cardinality, self.is_object, self.is_rich, self.is_tenant, self.is_local, self.table_comment, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]


@dataclass(frozen=False)
class system_thread_rich_dto(system_thread_read_dto):
    system_thread_uid: str | None
    system_thread_name: str | None
    thread_name: str | None
    thread_id: int | None
    parent_object: str | None
    ticks_count: int | None
    is_alive: int | None
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
    def __init__(self, system_thread_uid: str | None, system_thread_name: str | None, thread_name: str | None, thread_id: int | None, parent_object: str | None, ticks_count: int | None, is_alive: int | None, sleep_time: int | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None):
        self.system_thread_uid = system_thread_uid
        self.system_thread_name = system_thread_name
        self.thread_name = thread_name
        self.thread_id = thread_id
        self.parent_object = parent_object
        self.ticks_count = ticks_count
        self.is_alive = is_alive
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
        return [self.system_thread_uid, self.system_thread_name, self.thread_name, self.thread_id, self.parent_object, self.ticks_count, self.is_alive, self.sleep_time, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]


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
    country__country_name: str | None
    country__continent_name: str | None
    country__continent_code: str | None
    country__country_iso3: str | None
    country__country_code: str | None
    country__phone_code: str | None
    country__currency_code: str | None
    country__capital_name: str | None
    country__region_name: str | None
    country__subregion_name: str | None
    country__region_code: str | None
    country__latitude: str | None
    country__longitude: str | None
    country__currency_name: str | None
    country__population: str | None
    country__languages: str | None
    country__area: str | None
    country__bar_code: str | None
    country__top_level_domain: str | None
    country__is_focused: int | None
    tenant_type__tenant_type_name: str | None
    tenant_type__tenant_type_description: str | None
    tenant_category__tenant_category_name: str | None
    tenant_category__tenant_category_description: str | None
    account__account_name: str | None
    account__tenant_uid: str | None
    account__account_type_uid: str | None
    account__account_title_uid: str | None
    account__account_division_uid: str | None
    account__account_group_uid: str | None
    account__auth_identity_uid: str | None
    account__account_email: str | None
    account__display_name: str | None
    account__account_address: str | None
    account__is_verified: int | None
    account__is_system: int | None
    def __init__(self, tenant_uid: str | None, tenant_name: str | None, country_uid: str | None, tenant_type_uid: str | None, tenant_category_uid: str | None, tenant_code: str | None, tenant_description: str | None, start_date: datetime.datetime | None, end_date: datetime.datetime | None, is_internal: int | None, is_system: int | None, is_test: int | None, account_uid: str | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None, country__country_name: str | None, country__continent_name: str | None, country__continent_code: str | None, country__country_iso3: str | None, country__country_code: str | None, country__phone_code: str | None, country__currency_code: str | None, country__capital_name: str | None, country__region_name: str | None, country__subregion_name: str | None, country__region_code: str | None, country__latitude: str | None, country__longitude: str | None, country__currency_name: str | None, country__population: str | None, country__languages: str | None, country__area: str | None, country__bar_code: str | None, country__top_level_domain: str | None, country__is_focused: int | None, tenant_type__tenant_type_name: str | None, tenant_type__tenant_type_description: str | None, tenant_category__tenant_category_name: str | None, tenant_category__tenant_category_description: str | None, account__account_name: str | None, account__tenant_uid: str | None, account__account_type_uid: str | None, account__account_title_uid: str | None, account__account_division_uid: str | None, account__account_group_uid: str | None, account__auth_identity_uid: str | None, account__account_email: str | None, account__display_name: str | None, account__account_address: str | None, account__is_verified: int | None, account__is_system: int | None):
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
        self.country__country_name = country__country_name
        self.country__continent_name = country__continent_name
        self.country__continent_code = country__continent_code
        self.country__country_iso3 = country__country_iso3
        self.country__country_code = country__country_code
        self.country__phone_code = country__phone_code
        self.country__currency_code = country__currency_code
        self.country__capital_name = country__capital_name
        self.country__region_name = country__region_name
        self.country__subregion_name = country__subregion_name
        self.country__region_code = country__region_code
        self.country__latitude = country__latitude
        self.country__longitude = country__longitude
        self.country__currency_name = country__currency_name
        self.country__population = country__population
        self.country__languages = country__languages
        self.country__area = country__area
        self.country__bar_code = country__bar_code
        self.country__top_level_domain = country__top_level_domain
        self.country__is_focused = country__is_focused
        self.tenant_type__tenant_type_name = tenant_type__tenant_type_name
        self.tenant_type__tenant_type_description = tenant_type__tenant_type_description
        self.tenant_category__tenant_category_name = tenant_category__tenant_category_name
        self.tenant_category__tenant_category_description = tenant_category__tenant_category_description
        self.account__account_name = account__account_name
        self.account__tenant_uid = account__tenant_uid
        self.account__account_type_uid = account__account_type_uid
        self.account__account_title_uid = account__account_title_uid
        self.account__account_division_uid = account__account_division_uid
        self.account__account_group_uid = account__account_group_uid
        self.account__auth_identity_uid = account__auth_identity_uid
        self.account__account_email = account__account_email
        self.account__display_name = account__display_name
        self.account__account_address = account__account_address
        self.account__is_verified = account__is_verified
        self.account__is_system = account__is_system
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.tenant_uid, self.tenant_name, self.country_uid, self.tenant_type_uid, self.tenant_category_uid, self.tenant_code, self.tenant_description, self.start_date, self.end_date, self.is_internal, self.is_system, self.is_test, self.account_uid, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes, self.country__country_name, self.country__continent_name, self.country__continent_code, self.country__country_iso3, self.country__country_code, self.country__phone_code, self.country__currency_code, self.country__capital_name, self.country__region_name, self.country__subregion_name, self.country__region_code, self.country__latitude, self.country__longitude, self.country__currency_name, self.country__population, self.country__languages, self.country__area, self.country__bar_code, self.country__top_level_domain, self.country__is_focused, self.tenant_type__tenant_type_name, self.tenant_type__tenant_type_description, self.tenant_category__tenant_category_name, self.tenant_category__tenant_category_description, self.account__account_name, self.account__tenant_uid, self.account__account_type_uid, self.account__account_title_uid, self.account__account_division_uid, self.account__account_group_uid, self.account__auth_identity_uid, self.account__account_email, self.account__display_name, self.account__account_address, self.account__is_verified, self.account__is_system]


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
    tenant_account__account_name: str | None
    tenant_account__tenant_uid: str | None
    tenant_account__account_type_uid: str | None
    tenant_account__account_title_uid: str | None
    tenant_account__account_division_uid: str | None
    tenant_account__account_group_uid: str | None
    tenant_account__auth_identity_uid: str | None
    tenant_account__account_email: str | None
    tenant_account__display_name: str | None
    tenant_account__account_address: str | None
    tenant_account__is_verified: int | None
    tenant_account__is_system: int | None
    tenant__tenant_name: str | None
    tenant__country_uid: str | None
    tenant__tenant_type_uid: str | None
    tenant__tenant_category_uid: str | None
    tenant__tenant_code: str | None
    tenant__tenant_description: str | None
    tenant__start_date: datetime.datetime | None
    tenant__end_date: datetime.datetime | None
    tenant__is_internal: int | None
    tenant__is_system: int | None
    tenant__is_test: int | None
    tenant__account_uid: str | None
    account__account_name: str | None
    account__tenant_uid: str | None
    account__account_type_uid: str | None
    account__account_title_uid: str | None
    account__account_division_uid: str | None
    account__account_group_uid: str | None
    account__auth_identity_uid: str | None
    account__account_email: str | None
    account__display_name: str | None
    account__account_address: str | None
    account__is_verified: int | None
    account__is_system: int | None
    tenant_role__tenant_role_name: str | None
    tenant_role__role_description: str | None
    def __init__(self, tenant_account_uid: str | None, tenant_account_name: str | None, tenant_uid: str | None, account_uid: str | None, tenant_role_uid: str | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None, tenant_account__account_name: str | None, tenant_account__tenant_uid: str | None, tenant_account__account_type_uid: str | None, tenant_account__account_title_uid: str | None, tenant_account__account_division_uid: str | None, tenant_account__account_group_uid: str | None, tenant_account__auth_identity_uid: str | None, tenant_account__account_email: str | None, tenant_account__display_name: str | None, tenant_account__account_address: str | None, tenant_account__is_verified: int | None, tenant_account__is_system: int | None, tenant__tenant_name: str | None, tenant__country_uid: str | None, tenant__tenant_type_uid: str | None, tenant__tenant_category_uid: str | None, tenant__tenant_code: str | None, tenant__tenant_description: str | None, tenant__start_date: datetime.datetime | None, tenant__end_date: datetime.datetime | None, tenant__is_internal: int | None, tenant__is_system: int | None, tenant__is_test: int | None, tenant__account_uid: str | None, account__account_name: str | None, account__tenant_uid: str | None, account__account_type_uid: str | None, account__account_title_uid: str | None, account__account_division_uid: str | None, account__account_group_uid: str | None, account__auth_identity_uid: str | None, account__account_email: str | None, account__display_name: str | None, account__account_address: str | None, account__is_verified: int | None, account__is_system: int | None, tenant_role__tenant_role_name: str | None, tenant_role__role_description: str | None):
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
        self.tenant_account__account_name = tenant_account__account_name
        self.tenant_account__tenant_uid = tenant_account__tenant_uid
        self.tenant_account__account_type_uid = tenant_account__account_type_uid
        self.tenant_account__account_title_uid = tenant_account__account_title_uid
        self.tenant_account__account_division_uid = tenant_account__account_division_uid
        self.tenant_account__account_group_uid = tenant_account__account_group_uid
        self.tenant_account__auth_identity_uid = tenant_account__auth_identity_uid
        self.tenant_account__account_email = tenant_account__account_email
        self.tenant_account__display_name = tenant_account__display_name
        self.tenant_account__account_address = tenant_account__account_address
        self.tenant_account__is_verified = tenant_account__is_verified
        self.tenant_account__is_system = tenant_account__is_system
        self.tenant__tenant_name = tenant__tenant_name
        self.tenant__country_uid = tenant__country_uid
        self.tenant__tenant_type_uid = tenant__tenant_type_uid
        self.tenant__tenant_category_uid = tenant__tenant_category_uid
        self.tenant__tenant_code = tenant__tenant_code
        self.tenant__tenant_description = tenant__tenant_description
        self.tenant__start_date = tenant__start_date
        self.tenant__end_date = tenant__end_date
        self.tenant__is_internal = tenant__is_internal
        self.tenant__is_system = tenant__is_system
        self.tenant__is_test = tenant__is_test
        self.tenant__account_uid = tenant__account_uid
        self.account__account_name = account__account_name
        self.account__tenant_uid = account__tenant_uid
        self.account__account_type_uid = account__account_type_uid
        self.account__account_title_uid = account__account_title_uid
        self.account__account_division_uid = account__account_division_uid
        self.account__account_group_uid = account__account_group_uid
        self.account__auth_identity_uid = account__auth_identity_uid
        self.account__account_email = account__account_email
        self.account__display_name = account__display_name
        self.account__account_address = account__account_address
        self.account__is_verified = account__is_verified
        self.account__is_system = account__is_system
        self.tenant_role__tenant_role_name = tenant_role__tenant_role_name
        self.tenant_role__role_description = tenant_role__role_description
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.tenant_account_uid, self.tenant_account_name, self.tenant_uid, self.account_uid, self.tenant_role_uid, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes, self.tenant_account__account_name, self.tenant_account__tenant_uid, self.tenant_account__account_type_uid, self.tenant_account__account_title_uid, self.tenant_account__account_division_uid, self.tenant_account__account_group_uid, self.tenant_account__auth_identity_uid, self.tenant_account__account_email, self.tenant_account__display_name, self.tenant_account__account_address, self.tenant_account__is_verified, self.tenant_account__is_system, self.tenant__tenant_name, self.tenant__country_uid, self.tenant__tenant_type_uid, self.tenant__tenant_category_uid, self.tenant__tenant_code, self.tenant__tenant_description, self.tenant__start_date, self.tenant__end_date, self.tenant__is_internal, self.tenant__is_system, self.tenant__is_test, self.tenant__account_uid, self.account__account_name, self.account__tenant_uid, self.account__account_type_uid, self.account__account_title_uid, self.account__account_division_uid, self.account__account_group_uid, self.account__auth_identity_uid, self.account__account_email, self.account__display_name, self.account__account_address, self.account__is_verified, self.account__is_system, self.tenant_role__tenant_role_name, self.tenant_role__role_description]


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
    tenant_country__country_name: str | None
    tenant_country__continent_name: str | None
    tenant_country__continent_code: str | None
    tenant_country__country_iso3: str | None
    tenant_country__country_code: str | None
    tenant_country__phone_code: str | None
    tenant_country__currency_code: str | None
    tenant_country__capital_name: str | None
    tenant_country__region_name: str | None
    tenant_country__subregion_name: str | None
    tenant_country__region_code: str | None
    tenant_country__latitude: str | None
    tenant_country__longitude: str | None
    tenant_country__currency_name: str | None
    tenant_country__population: str | None
    tenant_country__languages: str | None
    tenant_country__area: str | None
    tenant_country__bar_code: str | None
    tenant_country__top_level_domain: str | None
    tenant_country__is_focused: int | None
    country__country_name: str | None
    country__continent_name: str | None
    country__continent_code: str | None
    country__country_iso3: str | None
    country__country_code: str | None
    country__phone_code: str | None
    country__currency_code: str | None
    country__capital_name: str | None
    country__region_name: str | None
    country__subregion_name: str | None
    country__region_code: str | None
    country__latitude: str | None
    country__longitude: str | None
    country__currency_name: str | None
    country__population: str | None
    country__languages: str | None
    country__area: str | None
    country__bar_code: str | None
    country__top_level_domain: str | None
    country__is_focused: int | None
    tenant__tenant_name: str | None
    tenant__country_uid: str | None
    tenant__tenant_type_uid: str | None
    tenant__tenant_category_uid: str | None
    tenant__tenant_code: str | None
    tenant__tenant_description: str | None
    tenant__start_date: datetime.datetime | None
    tenant__end_date: datetime.datetime | None
    tenant__is_internal: int | None
    tenant__is_system: int | None
    tenant__is_test: int | None
    tenant__account_uid: str | None
    def __init__(self, tenant_country_uid: str | None, tenant_country_name: str | None, country_uid: str | None, tenant_uid: str | None, country_priority: int | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None, tenant_country__country_name: str | None, tenant_country__continent_name: str | None, tenant_country__continent_code: str | None, tenant_country__country_iso3: str | None, tenant_country__country_code: str | None, tenant_country__phone_code: str | None, tenant_country__currency_code: str | None, tenant_country__capital_name: str | None, tenant_country__region_name: str | None, tenant_country__subregion_name: str | None, tenant_country__region_code: str | None, tenant_country__latitude: str | None, tenant_country__longitude: str | None, tenant_country__currency_name: str | None, tenant_country__population: str | None, tenant_country__languages: str | None, tenant_country__area: str | None, tenant_country__bar_code: str | None, tenant_country__top_level_domain: str | None, tenant_country__is_focused: int | None, country__country_name: str | None, country__continent_name: str | None, country__continent_code: str | None, country__country_iso3: str | None, country__country_code: str | None, country__phone_code: str | None, country__currency_code: str | None, country__capital_name: str | None, country__region_name: str | None, country__subregion_name: str | None, country__region_code: str | None, country__latitude: str | None, country__longitude: str | None, country__currency_name: str | None, country__population: str | None, country__languages: str | None, country__area: str | None, country__bar_code: str | None, country__top_level_domain: str | None, country__is_focused: int | None, tenant__tenant_name: str | None, tenant__country_uid: str | None, tenant__tenant_type_uid: str | None, tenant__tenant_category_uid: str | None, tenant__tenant_code: str | None, tenant__tenant_description: str | None, tenant__start_date: datetime.datetime | None, tenant__end_date: datetime.datetime | None, tenant__is_internal: int | None, tenant__is_system: int | None, tenant__is_test: int | None, tenant__account_uid: str | None):
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
        self.tenant_country__country_name = tenant_country__country_name
        self.tenant_country__continent_name = tenant_country__continent_name
        self.tenant_country__continent_code = tenant_country__continent_code
        self.tenant_country__country_iso3 = tenant_country__country_iso3
        self.tenant_country__country_code = tenant_country__country_code
        self.tenant_country__phone_code = tenant_country__phone_code
        self.tenant_country__currency_code = tenant_country__currency_code
        self.tenant_country__capital_name = tenant_country__capital_name
        self.tenant_country__region_name = tenant_country__region_name
        self.tenant_country__subregion_name = tenant_country__subregion_name
        self.tenant_country__region_code = tenant_country__region_code
        self.tenant_country__latitude = tenant_country__latitude
        self.tenant_country__longitude = tenant_country__longitude
        self.tenant_country__currency_name = tenant_country__currency_name
        self.tenant_country__population = tenant_country__population
        self.tenant_country__languages = tenant_country__languages
        self.tenant_country__area = tenant_country__area
        self.tenant_country__bar_code = tenant_country__bar_code
        self.tenant_country__top_level_domain = tenant_country__top_level_domain
        self.tenant_country__is_focused = tenant_country__is_focused
        self.country__country_name = country__country_name
        self.country__continent_name = country__continent_name
        self.country__continent_code = country__continent_code
        self.country__country_iso3 = country__country_iso3
        self.country__country_code = country__country_code
        self.country__phone_code = country__phone_code
        self.country__currency_code = country__currency_code
        self.country__capital_name = country__capital_name
        self.country__region_name = country__region_name
        self.country__subregion_name = country__subregion_name
        self.country__region_code = country__region_code
        self.country__latitude = country__latitude
        self.country__longitude = country__longitude
        self.country__currency_name = country__currency_name
        self.country__population = country__population
        self.country__languages = country__languages
        self.country__area = country__area
        self.country__bar_code = country__bar_code
        self.country__top_level_domain = country__top_level_domain
        self.country__is_focused = country__is_focused
        self.tenant__tenant_name = tenant__tenant_name
        self.tenant__country_uid = tenant__country_uid
        self.tenant__tenant_type_uid = tenant__tenant_type_uid
        self.tenant__tenant_category_uid = tenant__tenant_category_uid
        self.tenant__tenant_code = tenant__tenant_code
        self.tenant__tenant_description = tenant__tenant_description
        self.tenant__start_date = tenant__start_date
        self.tenant__end_date = tenant__end_date
        self.tenant__is_internal = tenant__is_internal
        self.tenant__is_system = tenant__is_system
        self.tenant__is_test = tenant__is_test
        self.tenant__account_uid = tenant__account_uid
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.tenant_country_uid, self.tenant_country_name, self.country_uid, self.tenant_uid, self.country_priority, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes, self.tenant_country__country_name, self.tenant_country__continent_name, self.tenant_country__continent_code, self.tenant_country__country_iso3, self.tenant_country__country_code, self.tenant_country__phone_code, self.tenant_country__currency_code, self.tenant_country__capital_name, self.tenant_country__region_name, self.tenant_country__subregion_name, self.tenant_country__region_code, self.tenant_country__latitude, self.tenant_country__longitude, self.tenant_country__currency_name, self.tenant_country__population, self.tenant_country__languages, self.tenant_country__area, self.tenant_country__bar_code, self.tenant_country__top_level_domain, self.tenant_country__is_focused, self.country__country_name, self.country__continent_name, self.country__continent_code, self.country__country_iso3, self.country__country_code, self.country__phone_code, self.country__currency_code, self.country__capital_name, self.country__region_name, self.country__subregion_name, self.country__region_code, self.country__latitude, self.country__longitude, self.country__currency_name, self.country__population, self.country__languages, self.country__area, self.country__bar_code, self.country__top_level_domain, self.country__is_focused, self.tenant__tenant_name, self.tenant__country_uid, self.tenant__tenant_type_uid, self.tenant__tenant_category_uid, self.tenant__tenant_code, self.tenant__tenant_description, self.tenant__start_date, self.tenant__end_date, self.tenant__is_internal, self.tenant__is_system, self.tenant__is_test, self.tenant__account_uid]


@dataclass(frozen=False)
class tenant_license_rich_dto(tenant_license_read_dto):
    tenant_license_uid: str | None
    tenant_license_name: str | None
    tenant_uid: str | None
    system_license_uid: str | None
    start_date: datetime.datetime | None
    end_date: datetime.datetime | None
    accounts_count: int | None
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
    tenant__tenant_name: str | None
    tenant__country_uid: str | None
    tenant__tenant_type_uid: str | None
    tenant__tenant_category_uid: str | None
    tenant__tenant_code: str | None
    tenant__tenant_description: str | None
    tenant__start_date: datetime.datetime | None
    tenant__end_date: datetime.datetime | None
    tenant__is_internal: int | None
    tenant__is_system: int | None
    tenant__is_test: int | None
    tenant__account_uid: str | None
    system_license__system_license_name: str | None
    system_license__class_name: str | None
    system_license__license_description: str | None
    def __init__(self, tenant_license_uid: str | None, tenant_license_name: str | None, tenant_uid: str | None, system_license_uid: str | None, start_date: datetime.datetime | None, end_date: datetime.datetime | None, accounts_count: int | None, is_approved: int | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None, tenant__tenant_name: str | None, tenant__country_uid: str | None, tenant__tenant_type_uid: str | None, tenant__tenant_category_uid: str | None, tenant__tenant_code: str | None, tenant__tenant_description: str | None, tenant__start_date: datetime.datetime | None, tenant__end_date: datetime.datetime | None, tenant__is_internal: int | None, tenant__is_system: int | None, tenant__is_test: int | None, tenant__account_uid: str | None, system_license__system_license_name: str | None, system_license__class_name: str | None, system_license__license_description: str | None):
        self.tenant_license_uid = tenant_license_uid
        self.tenant_license_name = tenant_license_name
        self.tenant_uid = tenant_uid
        self.system_license_uid = system_license_uid
        self.start_date = start_date
        self.end_date = end_date
        self.accounts_count = accounts_count
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
        self.tenant__tenant_name = tenant__tenant_name
        self.tenant__country_uid = tenant__country_uid
        self.tenant__tenant_type_uid = tenant__tenant_type_uid
        self.tenant__tenant_category_uid = tenant__tenant_category_uid
        self.tenant__tenant_code = tenant__tenant_code
        self.tenant__tenant_description = tenant__tenant_description
        self.tenant__start_date = tenant__start_date
        self.tenant__end_date = tenant__end_date
        self.tenant__is_internal = tenant__is_internal
        self.tenant__is_system = tenant__is_system
        self.tenant__is_test = tenant__is_test
        self.tenant__account_uid = tenant__account_uid
        self.system_license__system_license_name = system_license__system_license_name
        self.system_license__class_name = system_license__class_name
        self.system_license__license_description = system_license__license_description
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.tenant_license_uid, self.tenant_license_name, self.tenant_uid, self.system_license_uid, self.start_date, self.end_date, self.accounts_count, self.is_approved, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes, self.tenant__tenant_name, self.tenant__country_uid, self.tenant__tenant_type_uid, self.tenant__tenant_category_uid, self.tenant__tenant_code, self.tenant__tenant_description, self.tenant__start_date, self.tenant__end_date, self.tenant__is_internal, self.tenant__is_system, self.tenant__is_test, self.tenant__account_uid, self.system_license__system_license_name, self.system_license__class_name, self.system_license__license_description]


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
    tenant__tenant_name: str | None
    tenant__country_uid: str | None
    tenant__tenant_type_uid: str | None
    tenant__tenant_category_uid: str | None
    tenant__tenant_code: str | None
    tenant__tenant_description: str | None
    tenant__start_date: datetime.datetime | None
    tenant__end_date: datetime.datetime | None
    tenant__is_internal: int | None
    tenant__is_system: int | None
    tenant__is_test: int | None
    tenant__account_uid: str | None
    account__account_name: str | None
    account__tenant_uid: str | None
    account__account_type_uid: str | None
    account__account_title_uid: str | None
    account__account_division_uid: str | None
    account__account_group_uid: str | None
    account__auth_identity_uid: str | None
    account__account_email: str | None
    account__display_name: str | None
    account__account_address: str | None
    account__is_verified: int | None
    account__is_system: int | None
    currency__currency_name: str | None
    currency__is_focused: int | None
    currency__priority: int | None
    tenant_payment_type__tenant_payment_type_name: str | None
    def __init__(self, tenant_payment_uid: str | None, tenant_payment_name: str | None, tenant_uid: str | None, account_uid: str | None, currency_uid: str | None, tenant_payment_type_uid: str | None, start_date: datetime.datetime | None, end_date: datetime.datetime | None, payment_value: str | None, source_number: str | None, source_reference: str | None, is_approved: int | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None, tenant__tenant_name: str | None, tenant__country_uid: str | None, tenant__tenant_type_uid: str | None, tenant__tenant_category_uid: str | None, tenant__tenant_code: str | None, tenant__tenant_description: str | None, tenant__start_date: datetime.datetime | None, tenant__end_date: datetime.datetime | None, tenant__is_internal: int | None, tenant__is_system: int | None, tenant__is_test: int | None, tenant__account_uid: str | None, account__account_name: str | None, account__tenant_uid: str | None, account__account_type_uid: str | None, account__account_title_uid: str | None, account__account_division_uid: str | None, account__account_group_uid: str | None, account__auth_identity_uid: str | None, account__account_email: str | None, account__display_name: str | None, account__account_address: str | None, account__is_verified: int | None, account__is_system: int | None, currency__currency_name: str | None, currency__is_focused: int | None, currency__priority: int | None, tenant_payment_type__tenant_payment_type_name: str | None):
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
        self.tenant__tenant_name = tenant__tenant_name
        self.tenant__country_uid = tenant__country_uid
        self.tenant__tenant_type_uid = tenant__tenant_type_uid
        self.tenant__tenant_category_uid = tenant__tenant_category_uid
        self.tenant__tenant_code = tenant__tenant_code
        self.tenant__tenant_description = tenant__tenant_description
        self.tenant__start_date = tenant__start_date
        self.tenant__end_date = tenant__end_date
        self.tenant__is_internal = tenant__is_internal
        self.tenant__is_system = tenant__is_system
        self.tenant__is_test = tenant__is_test
        self.tenant__account_uid = tenant__account_uid
        self.account__account_name = account__account_name
        self.account__tenant_uid = account__tenant_uid
        self.account__account_type_uid = account__account_type_uid
        self.account__account_title_uid = account__account_title_uid
        self.account__account_division_uid = account__account_division_uid
        self.account__account_group_uid = account__account_group_uid
        self.account__auth_identity_uid = account__auth_identity_uid
        self.account__account_email = account__account_email
        self.account__display_name = account__display_name
        self.account__account_address = account__account_address
        self.account__is_verified = account__is_verified
        self.account__is_system = account__is_system
        self.currency__currency_name = currency__currency_name
        self.currency__is_focused = currency__is_focused
        self.currency__priority = currency__priority
        self.tenant_payment_type__tenant_payment_type_name = tenant_payment_type__tenant_payment_type_name
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.tenant_payment_uid, self.tenant_payment_name, self.tenant_uid, self.account_uid, self.currency_uid, self.tenant_payment_type_uid, self.start_date, self.end_date, self.payment_value, self.source_number, self.source_reference, self.is_approved, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes, self.tenant__tenant_name, self.tenant__country_uid, self.tenant__tenant_type_uid, self.tenant__tenant_category_uid, self.tenant__tenant_code, self.tenant__tenant_description, self.tenant__start_date, self.tenant__end_date, self.tenant__is_internal, self.tenant__is_system, self.tenant__is_test, self.tenant__account_uid, self.account__account_name, self.account__tenant_uid, self.account__account_type_uid, self.account__account_title_uid, self.account__account_division_uid, self.account__account_group_uid, self.account__auth_identity_uid, self.account__account_email, self.account__display_name, self.account__account_address, self.account__is_verified, self.account__is_system, self.currency__currency_name, self.currency__is_focused, self.currency__priority, self.tenant_payment_type__tenant_payment_type_name]


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
    tenant__tenant_name: str | None
    tenant__country_uid: str | None
    tenant__tenant_type_uid: str | None
    tenant__tenant_category_uid: str | None
    tenant__tenant_code: str | None
    tenant__tenant_description: str | None
    tenant__start_date: datetime.datetime | None
    tenant__end_date: datetime.datetime | None
    tenant__is_internal: int | None
    tenant__is_system: int | None
    tenant__is_test: int | None
    tenant__account_uid: str | None
    account__account_name: str | None
    account__tenant_uid: str | None
    account__account_type_uid: str | None
    account__account_title_uid: str | None
    account__account_division_uid: str | None
    account__account_group_uid: str | None
    account__auth_identity_uid: str | None
    account__account_email: str | None
    account__display_name: str | None
    account__account_address: str | None
    account__is_verified: int | None
    account__is_system: int | None
    time_entry__time_entry_name: str | None
    time_entry__time_submit_uid: str | None
    time_entry__tenant_uid: str | None
    time_entry__account_uid: str | None
    time_entry__project_instance_uid: str | None
    time_entry__project_milestone_uid: str | None
    time_entry__period_uid: str | None
    time_entry__invoice_instance_uid: str | None
    time_entry__entry_period: str | None
    time_entry__entry_note: str | None
    time_entry__lock_row: str | None
    time_entry__start_date: datetime.datetime | None
    time_entry__end_date: datetime.datetime | None
    time_entry__entry_minutes: int | None
    time_entry__is_approved: int | None
    def __init__(self, time_approval_uid: str | None, time_approval_name: str | None, tenant_uid: str | None, account_uid: str | None, time_entry_uid: str | None, approval_comment: str | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None, tenant__tenant_name: str | None, tenant__country_uid: str | None, tenant__tenant_type_uid: str | None, tenant__tenant_category_uid: str | None, tenant__tenant_code: str | None, tenant__tenant_description: str | None, tenant__start_date: datetime.datetime | None, tenant__end_date: datetime.datetime | None, tenant__is_internal: int | None, tenant__is_system: int | None, tenant__is_test: int | None, tenant__account_uid: str | None, account__account_name: str | None, account__tenant_uid: str | None, account__account_type_uid: str | None, account__account_title_uid: str | None, account__account_division_uid: str | None, account__account_group_uid: str | None, account__auth_identity_uid: str | None, account__account_email: str | None, account__display_name: str | None, account__account_address: str | None, account__is_verified: int | None, account__is_system: int | None, time_entry__time_entry_name: str | None, time_entry__time_submit_uid: str | None, time_entry__tenant_uid: str | None, time_entry__account_uid: str | None, time_entry__project_instance_uid: str | None, time_entry__project_milestone_uid: str | None, time_entry__period_uid: str | None, time_entry__invoice_instance_uid: str | None, time_entry__entry_period: str | None, time_entry__entry_note: str | None, time_entry__lock_row: str | None, time_entry__start_date: datetime.datetime | None, time_entry__end_date: datetime.datetime | None, time_entry__entry_minutes: int | None, time_entry__is_approved: int | None):
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
        self.tenant__tenant_name = tenant__tenant_name
        self.tenant__country_uid = tenant__country_uid
        self.tenant__tenant_type_uid = tenant__tenant_type_uid
        self.tenant__tenant_category_uid = tenant__tenant_category_uid
        self.tenant__tenant_code = tenant__tenant_code
        self.tenant__tenant_description = tenant__tenant_description
        self.tenant__start_date = tenant__start_date
        self.tenant__end_date = tenant__end_date
        self.tenant__is_internal = tenant__is_internal
        self.tenant__is_system = tenant__is_system
        self.tenant__is_test = tenant__is_test
        self.tenant__account_uid = tenant__account_uid
        self.account__account_name = account__account_name
        self.account__tenant_uid = account__tenant_uid
        self.account__account_type_uid = account__account_type_uid
        self.account__account_title_uid = account__account_title_uid
        self.account__account_division_uid = account__account_division_uid
        self.account__account_group_uid = account__account_group_uid
        self.account__auth_identity_uid = account__auth_identity_uid
        self.account__account_email = account__account_email
        self.account__display_name = account__display_name
        self.account__account_address = account__account_address
        self.account__is_verified = account__is_verified
        self.account__is_system = account__is_system
        self.time_entry__time_entry_name = time_entry__time_entry_name
        self.time_entry__time_submit_uid = time_entry__time_submit_uid
        self.time_entry__tenant_uid = time_entry__tenant_uid
        self.time_entry__account_uid = time_entry__account_uid
        self.time_entry__project_instance_uid = time_entry__project_instance_uid
        self.time_entry__project_milestone_uid = time_entry__project_milestone_uid
        self.time_entry__period_uid = time_entry__period_uid
        self.time_entry__invoice_instance_uid = time_entry__invoice_instance_uid
        self.time_entry__entry_period = time_entry__entry_period
        self.time_entry__entry_note = time_entry__entry_note
        self.time_entry__lock_row = time_entry__lock_row
        self.time_entry__start_date = time_entry__start_date
        self.time_entry__end_date = time_entry__end_date
        self.time_entry__entry_minutes = time_entry__entry_minutes
        self.time_entry__is_approved = time_entry__is_approved
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.time_approval_uid, self.time_approval_name, self.tenant_uid, self.account_uid, self.time_entry_uid, self.approval_comment, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes, self.tenant__tenant_name, self.tenant__country_uid, self.tenant__tenant_type_uid, self.tenant__tenant_category_uid, self.tenant__tenant_code, self.tenant__tenant_description, self.tenant__start_date, self.tenant__end_date, self.tenant__is_internal, self.tenant__is_system, self.tenant__is_test, self.tenant__account_uid, self.account__account_name, self.account__tenant_uid, self.account__account_type_uid, self.account__account_title_uid, self.account__account_division_uid, self.account__account_group_uid, self.account__auth_identity_uid, self.account__account_email, self.account__display_name, self.account__account_address, self.account__is_verified, self.account__is_system, self.time_entry__time_entry_name, self.time_entry__time_submit_uid, self.time_entry__tenant_uid, self.time_entry__account_uid, self.time_entry__project_instance_uid, self.time_entry__project_milestone_uid, self.time_entry__period_uid, self.time_entry__invoice_instance_uid, self.time_entry__entry_period, self.time_entry__entry_note, self.time_entry__lock_row, self.time_entry__start_date, self.time_entry__end_date, self.time_entry__entry_minutes, self.time_entry__is_approved]


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
    time_submit__time_submit_name: str | None
    time_submit__tenant_uid: str | None
    time_submit__account_uid: str | None
    time_submit__period_uid: str | None
    time_submit__time_submit_description: str | None
    tenant__tenant_name: str | None
    tenant__country_uid: str | None
    tenant__tenant_type_uid: str | None
    tenant__tenant_category_uid: str | None
    tenant__tenant_code: str | None
    tenant__tenant_description: str | None
    tenant__start_date: datetime.datetime | None
    tenant__end_date: datetime.datetime | None
    tenant__is_internal: int | None
    tenant__is_system: int | None
    tenant__is_test: int | None
    tenant__account_uid: str | None
    account__account_name: str | None
    account__tenant_uid: str | None
    account__account_type_uid: str | None
    account__account_title_uid: str | None
    account__account_division_uid: str | None
    account__account_group_uid: str | None
    account__auth_identity_uid: str | None
    account__account_email: str | None
    account__display_name: str | None
    account__account_address: str | None
    account__is_verified: int | None
    account__is_system: int | None
    project_instance__project_instance_name: str | None
    project_instance__tenant_uid: str | None
    project_instance__client_uid: str | None
    project_instance__project_type_uid: str | None
    project_instance__manager_account_uid: str | None
    project_instance__project_group_uid: str | None
    project_instance__project_code: str | None
    project_instance__project_description: str | None
    project_instance__is_billable: int | None
    project_instance__start_date: datetime.datetime | None
    project_instance__end_date: datetime.datetime | None
    project_instance__current_billed: str | None
    project_instance__budget: str | None
    project_milestone__project_milestone_name: str | None
    project_milestone__tenant_uid: str | None
    project_milestone__client_uid: str | None
    project_milestone__project_instance_uid: str | None
    project_milestone__project_budget_uid: str | None
    project_milestone__start_date: datetime.datetime | None
    project_milestone__end_date: datetime.datetime | None
    project_milestone__status_name: str | None
    period__period_name: str | None
    period__period_number: int | None
    period__period_type: str | None
    period__period_start_time: datetime.datetime | None
    period__period_end_time: datetime.datetime | None
    period__period_year: int | None
    period__period_quarter: int | None
    period__period_month: int | None
    period__period_week: int | None
    period__period_day: int | None
    invoice_instance__invoice_instance_name: str | None
    invoice_instance__tenant_uid: str | None
    invoice_instance__account_uid: str | None
    invoice_instance__invoice_flow_uid: str | None
    invoice_instance__invoice_status_uid: str | None
    invoice_instance__invoice_category_uid: str | None
    invoice_instance__invoice_type_uid: str | None
    invoice_instance__period_uid: str | None
    invoice_instance__currency_uid: str | None
    invoice_instance__invoice_number: str | None
    invoice_instance__invoice_details: str | None
    invoice_instance__invoice_amount_net: str | None
    invoice_instance__invoice_amount_tax: str | None
    invoice_instance__invoice_amount_gross: str | None
    def __init__(self, time_entry_uid: str | None, time_entry_name: str | None, time_submit_uid: str | None, tenant_uid: str | None, account_uid: str | None, project_instance_uid: str | None, project_milestone_uid: str | None, period_uid: str | None, invoice_instance_uid: str | None, entry_period: str | None, entry_note: str | None, lock_row: str | None, start_date: datetime.datetime | None, end_date: datetime.datetime | None, entry_minutes: int | None, is_approved: int | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None, time_submit__time_submit_name: str | None, time_submit__tenant_uid: str | None, time_submit__account_uid: str | None, time_submit__period_uid: str | None, time_submit__time_submit_description: str | None, tenant__tenant_name: str | None, tenant__country_uid: str | None, tenant__tenant_type_uid: str | None, tenant__tenant_category_uid: str | None, tenant__tenant_code: str | None, tenant__tenant_description: str | None, tenant__start_date: datetime.datetime | None, tenant__end_date: datetime.datetime | None, tenant__is_internal: int | None, tenant__is_system: int | None, tenant__is_test: int | None, tenant__account_uid: str | None, account__account_name: str | None, account__tenant_uid: str | None, account__account_type_uid: str | None, account__account_title_uid: str | None, account__account_division_uid: str | None, account__account_group_uid: str | None, account__auth_identity_uid: str | None, account__account_email: str | None, account__display_name: str | None, account__account_address: str | None, account__is_verified: int | None, account__is_system: int | None, project_instance__project_instance_name: str | None, project_instance__tenant_uid: str | None, project_instance__client_uid: str | None, project_instance__project_type_uid: str | None, project_instance__manager_account_uid: str | None, project_instance__project_group_uid: str | None, project_instance__project_code: str | None, project_instance__project_description: str | None, project_instance__is_billable: int | None, project_instance__start_date: datetime.datetime | None, project_instance__end_date: datetime.datetime | None, project_instance__current_billed: str | None, project_instance__budget: str | None, project_milestone__project_milestone_name: str | None, project_milestone__tenant_uid: str | None, project_milestone__client_uid: str | None, project_milestone__project_instance_uid: str | None, project_milestone__project_budget_uid: str | None, project_milestone__start_date: datetime.datetime | None, project_milestone__end_date: datetime.datetime | None, project_milestone__status_name: str | None, period__period_name: str | None, period__period_number: int | None, period__period_type: str | None, period__period_start_time: datetime.datetime | None, period__period_end_time: datetime.datetime | None, period__period_year: int | None, period__period_quarter: int | None, period__period_month: int | None, period__period_week: int | None, period__period_day: int | None, invoice_instance__invoice_instance_name: str | None, invoice_instance__tenant_uid: str | None, invoice_instance__account_uid: str | None, invoice_instance__invoice_flow_uid: str | None, invoice_instance__invoice_status_uid: str | None, invoice_instance__invoice_category_uid: str | None, invoice_instance__invoice_type_uid: str | None, invoice_instance__period_uid: str | None, invoice_instance__currency_uid: str | None, invoice_instance__invoice_number: str | None, invoice_instance__invoice_details: str | None, invoice_instance__invoice_amount_net: str | None, invoice_instance__invoice_amount_tax: str | None, invoice_instance__invoice_amount_gross: str | None):
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
        self.time_submit__time_submit_name = time_submit__time_submit_name
        self.time_submit__tenant_uid = time_submit__tenant_uid
        self.time_submit__account_uid = time_submit__account_uid
        self.time_submit__period_uid = time_submit__period_uid
        self.time_submit__time_submit_description = time_submit__time_submit_description
        self.tenant__tenant_name = tenant__tenant_name
        self.tenant__country_uid = tenant__country_uid
        self.tenant__tenant_type_uid = tenant__tenant_type_uid
        self.tenant__tenant_category_uid = tenant__tenant_category_uid
        self.tenant__tenant_code = tenant__tenant_code
        self.tenant__tenant_description = tenant__tenant_description
        self.tenant__start_date = tenant__start_date
        self.tenant__end_date = tenant__end_date
        self.tenant__is_internal = tenant__is_internal
        self.tenant__is_system = tenant__is_system
        self.tenant__is_test = tenant__is_test
        self.tenant__account_uid = tenant__account_uid
        self.account__account_name = account__account_name
        self.account__tenant_uid = account__tenant_uid
        self.account__account_type_uid = account__account_type_uid
        self.account__account_title_uid = account__account_title_uid
        self.account__account_division_uid = account__account_division_uid
        self.account__account_group_uid = account__account_group_uid
        self.account__auth_identity_uid = account__auth_identity_uid
        self.account__account_email = account__account_email
        self.account__display_name = account__display_name
        self.account__account_address = account__account_address
        self.account__is_verified = account__is_verified
        self.account__is_system = account__is_system
        self.project_instance__project_instance_name = project_instance__project_instance_name
        self.project_instance__tenant_uid = project_instance__tenant_uid
        self.project_instance__client_uid = project_instance__client_uid
        self.project_instance__project_type_uid = project_instance__project_type_uid
        self.project_instance__manager_account_uid = project_instance__manager_account_uid
        self.project_instance__project_group_uid = project_instance__project_group_uid
        self.project_instance__project_code = project_instance__project_code
        self.project_instance__project_description = project_instance__project_description
        self.project_instance__is_billable = project_instance__is_billable
        self.project_instance__start_date = project_instance__start_date
        self.project_instance__end_date = project_instance__end_date
        self.project_instance__current_billed = project_instance__current_billed
        self.project_instance__budget = project_instance__budget
        self.project_milestone__project_milestone_name = project_milestone__project_milestone_name
        self.project_milestone__tenant_uid = project_milestone__tenant_uid
        self.project_milestone__client_uid = project_milestone__client_uid
        self.project_milestone__project_instance_uid = project_milestone__project_instance_uid
        self.project_milestone__project_budget_uid = project_milestone__project_budget_uid
        self.project_milestone__start_date = project_milestone__start_date
        self.project_milestone__end_date = project_milestone__end_date
        self.project_milestone__status_name = project_milestone__status_name
        self.period__period_name = period__period_name
        self.period__period_number = period__period_number
        self.period__period_type = period__period_type
        self.period__period_start_time = period__period_start_time
        self.period__period_end_time = period__period_end_time
        self.period__period_year = period__period_year
        self.period__period_quarter = period__period_quarter
        self.period__period_month = period__period_month
        self.period__period_week = period__period_week
        self.period__period_day = period__period_day
        self.invoice_instance__invoice_instance_name = invoice_instance__invoice_instance_name
        self.invoice_instance__tenant_uid = invoice_instance__tenant_uid
        self.invoice_instance__account_uid = invoice_instance__account_uid
        self.invoice_instance__invoice_flow_uid = invoice_instance__invoice_flow_uid
        self.invoice_instance__invoice_status_uid = invoice_instance__invoice_status_uid
        self.invoice_instance__invoice_category_uid = invoice_instance__invoice_category_uid
        self.invoice_instance__invoice_type_uid = invoice_instance__invoice_type_uid
        self.invoice_instance__period_uid = invoice_instance__period_uid
        self.invoice_instance__currency_uid = invoice_instance__currency_uid
        self.invoice_instance__invoice_number = invoice_instance__invoice_number
        self.invoice_instance__invoice_details = invoice_instance__invoice_details
        self.invoice_instance__invoice_amount_net = invoice_instance__invoice_amount_net
        self.invoice_instance__invoice_amount_tax = invoice_instance__invoice_amount_tax
        self.invoice_instance__invoice_amount_gross = invoice_instance__invoice_amount_gross
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.time_entry_uid, self.time_entry_name, self.time_submit_uid, self.tenant_uid, self.account_uid, self.project_instance_uid, self.project_milestone_uid, self.period_uid, self.invoice_instance_uid, self.entry_period, self.entry_note, self.lock_row, self.start_date, self.end_date, self.entry_minutes, self.is_approved, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes, self.time_submit__time_submit_name, self.time_submit__tenant_uid, self.time_submit__account_uid, self.time_submit__period_uid, self.time_submit__time_submit_description, self.tenant__tenant_name, self.tenant__country_uid, self.tenant__tenant_type_uid, self.tenant__tenant_category_uid, self.tenant__tenant_code, self.tenant__tenant_description, self.tenant__start_date, self.tenant__end_date, self.tenant__is_internal, self.tenant__is_system, self.tenant__is_test, self.tenant__account_uid, self.account__account_name, self.account__tenant_uid, self.account__account_type_uid, self.account__account_title_uid, self.account__account_division_uid, self.account__account_group_uid, self.account__auth_identity_uid, self.account__account_email, self.account__display_name, self.account__account_address, self.account__is_verified, self.account__is_system, self.project_instance__project_instance_name, self.project_instance__tenant_uid, self.project_instance__client_uid, self.project_instance__project_type_uid, self.project_instance__manager_account_uid, self.project_instance__project_group_uid, self.project_instance__project_code, self.project_instance__project_description, self.project_instance__is_billable, self.project_instance__start_date, self.project_instance__end_date, self.project_instance__current_billed, self.project_instance__budget, self.project_milestone__project_milestone_name, self.project_milestone__tenant_uid, self.project_milestone__client_uid, self.project_milestone__project_instance_uid, self.project_milestone__project_budget_uid, self.project_milestone__start_date, self.project_milestone__end_date, self.project_milestone__status_name, self.period__period_name, self.period__period_number, self.period__period_type, self.period__period_start_time, self.period__period_end_time, self.period__period_year, self.period__period_quarter, self.period__period_month, self.period__period_week, self.period__period_day, self.invoice_instance__invoice_instance_name, self.invoice_instance__tenant_uid, self.invoice_instance__account_uid, self.invoice_instance__invoice_flow_uid, self.invoice_instance__invoice_status_uid, self.invoice_instance__invoice_category_uid, self.invoice_instance__invoice_type_uid, self.invoice_instance__period_uid, self.invoice_instance__currency_uid, self.invoice_instance__invoice_number, self.invoice_instance__invoice_details, self.invoice_instance__invoice_amount_net, self.invoice_instance__invoice_amount_tax, self.invoice_instance__invoice_amount_gross]


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
    tenant__tenant_name: str | None
    tenant__country_uid: str | None
    tenant__tenant_type_uid: str | None
    tenant__tenant_category_uid: str | None
    tenant__tenant_code: str | None
    tenant__tenant_description: str | None
    tenant__start_date: datetime.datetime | None
    tenant__end_date: datetime.datetime | None
    tenant__is_internal: int | None
    tenant__is_system: int | None
    tenant__is_test: int | None
    tenant__account_uid: str | None
    account__account_name: str | None
    account__tenant_uid: str | None
    account__account_type_uid: str | None
    account__account_title_uid: str | None
    account__account_division_uid: str | None
    account__account_group_uid: str | None
    account__auth_identity_uid: str | None
    account__account_email: str | None
    account__display_name: str | None
    account__account_address: str | None
    account__is_verified: int | None
    account__is_system: int | None
    project_instance__project_instance_name: str | None
    project_instance__tenant_uid: str | None
    project_instance__client_uid: str | None
    project_instance__project_type_uid: str | None
    project_instance__manager_account_uid: str | None
    project_instance__project_group_uid: str | None
    project_instance__project_code: str | None
    project_instance__project_description: str | None
    project_instance__is_billable: int | None
    project_instance__start_date: datetime.datetime | None
    project_instance__end_date: datetime.datetime | None
    project_instance__current_billed: str | None
    project_instance__budget: str | None
    project_milestone__project_milestone_name: str | None
    project_milestone__tenant_uid: str | None
    project_milestone__client_uid: str | None
    project_milestone__project_instance_uid: str | None
    project_milestone__project_budget_uid: str | None
    project_milestone__start_date: datetime.datetime | None
    project_milestone__end_date: datetime.datetime | None
    project_milestone__status_name: str | None
    invoice_instance__invoice_instance_name: str | None
    invoice_instance__tenant_uid: str | None
    invoice_instance__account_uid: str | None
    invoice_instance__invoice_flow_uid: str | None
    invoice_instance__invoice_status_uid: str | None
    invoice_instance__invoice_category_uid: str | None
    invoice_instance__invoice_type_uid: str | None
    invoice_instance__period_uid: str | None
    invoice_instance__currency_uid: str | None
    invoice_instance__invoice_number: str | None
    invoice_instance__invoice_details: str | None
    invoice_instance__invoice_amount_net: str | None
    invoice_instance__invoice_amount_tax: str | None
    invoice_instance__invoice_amount_gross: str | None
    def __init__(self, time_entry_final_uid: str | None, time_entry_final_name: str | None, tenant_uid: str | None, account_uid: str | None, project_instance_uid: str | None, project_milestone_uid: str | None, invoice_instance_uid: str | None, entry_period: str | None, entry_note: str | None, lock_uid: str | None, start_date: datetime.datetime | None, end_date: datetime.datetime | None, entry_minutes: int | None, is_approved: int | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None, tenant__tenant_name: str | None, tenant__country_uid: str | None, tenant__tenant_type_uid: str | None, tenant__tenant_category_uid: str | None, tenant__tenant_code: str | None, tenant__tenant_description: str | None, tenant__start_date: datetime.datetime | None, tenant__end_date: datetime.datetime | None, tenant__is_internal: int | None, tenant__is_system: int | None, tenant__is_test: int | None, tenant__account_uid: str | None, account__account_name: str | None, account__tenant_uid: str | None, account__account_type_uid: str | None, account__account_title_uid: str | None, account__account_division_uid: str | None, account__account_group_uid: str | None, account__auth_identity_uid: str | None, account__account_email: str | None, account__display_name: str | None, account__account_address: str | None, account__is_verified: int | None, account__is_system: int | None, project_instance__project_instance_name: str | None, project_instance__tenant_uid: str | None, project_instance__client_uid: str | None, project_instance__project_type_uid: str | None, project_instance__manager_account_uid: str | None, project_instance__project_group_uid: str | None, project_instance__project_code: str | None, project_instance__project_description: str | None, project_instance__is_billable: int | None, project_instance__start_date: datetime.datetime | None, project_instance__end_date: datetime.datetime | None, project_instance__current_billed: str | None, project_instance__budget: str | None, project_milestone__project_milestone_name: str | None, project_milestone__tenant_uid: str | None, project_milestone__client_uid: str | None, project_milestone__project_instance_uid: str | None, project_milestone__project_budget_uid: str | None, project_milestone__start_date: datetime.datetime | None, project_milestone__end_date: datetime.datetime | None, project_milestone__status_name: str | None, invoice_instance__invoice_instance_name: str | None, invoice_instance__tenant_uid: str | None, invoice_instance__account_uid: str | None, invoice_instance__invoice_flow_uid: str | None, invoice_instance__invoice_status_uid: str | None, invoice_instance__invoice_category_uid: str | None, invoice_instance__invoice_type_uid: str | None, invoice_instance__period_uid: str | None, invoice_instance__currency_uid: str | None, invoice_instance__invoice_number: str | None, invoice_instance__invoice_details: str | None, invoice_instance__invoice_amount_net: str | None, invoice_instance__invoice_amount_tax: str | None, invoice_instance__invoice_amount_gross: str | None):
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
        self.tenant__tenant_name = tenant__tenant_name
        self.tenant__country_uid = tenant__country_uid
        self.tenant__tenant_type_uid = tenant__tenant_type_uid
        self.tenant__tenant_category_uid = tenant__tenant_category_uid
        self.tenant__tenant_code = tenant__tenant_code
        self.tenant__tenant_description = tenant__tenant_description
        self.tenant__start_date = tenant__start_date
        self.tenant__end_date = tenant__end_date
        self.tenant__is_internal = tenant__is_internal
        self.tenant__is_system = tenant__is_system
        self.tenant__is_test = tenant__is_test
        self.tenant__account_uid = tenant__account_uid
        self.account__account_name = account__account_name
        self.account__tenant_uid = account__tenant_uid
        self.account__account_type_uid = account__account_type_uid
        self.account__account_title_uid = account__account_title_uid
        self.account__account_division_uid = account__account_division_uid
        self.account__account_group_uid = account__account_group_uid
        self.account__auth_identity_uid = account__auth_identity_uid
        self.account__account_email = account__account_email
        self.account__display_name = account__display_name
        self.account__account_address = account__account_address
        self.account__is_verified = account__is_verified
        self.account__is_system = account__is_system
        self.project_instance__project_instance_name = project_instance__project_instance_name
        self.project_instance__tenant_uid = project_instance__tenant_uid
        self.project_instance__client_uid = project_instance__client_uid
        self.project_instance__project_type_uid = project_instance__project_type_uid
        self.project_instance__manager_account_uid = project_instance__manager_account_uid
        self.project_instance__project_group_uid = project_instance__project_group_uid
        self.project_instance__project_code = project_instance__project_code
        self.project_instance__project_description = project_instance__project_description
        self.project_instance__is_billable = project_instance__is_billable
        self.project_instance__start_date = project_instance__start_date
        self.project_instance__end_date = project_instance__end_date
        self.project_instance__current_billed = project_instance__current_billed
        self.project_instance__budget = project_instance__budget
        self.project_milestone__project_milestone_name = project_milestone__project_milestone_name
        self.project_milestone__tenant_uid = project_milestone__tenant_uid
        self.project_milestone__client_uid = project_milestone__client_uid
        self.project_milestone__project_instance_uid = project_milestone__project_instance_uid
        self.project_milestone__project_budget_uid = project_milestone__project_budget_uid
        self.project_milestone__start_date = project_milestone__start_date
        self.project_milestone__end_date = project_milestone__end_date
        self.project_milestone__status_name = project_milestone__status_name
        self.invoice_instance__invoice_instance_name = invoice_instance__invoice_instance_name
        self.invoice_instance__tenant_uid = invoice_instance__tenant_uid
        self.invoice_instance__account_uid = invoice_instance__account_uid
        self.invoice_instance__invoice_flow_uid = invoice_instance__invoice_flow_uid
        self.invoice_instance__invoice_status_uid = invoice_instance__invoice_status_uid
        self.invoice_instance__invoice_category_uid = invoice_instance__invoice_category_uid
        self.invoice_instance__invoice_type_uid = invoice_instance__invoice_type_uid
        self.invoice_instance__period_uid = invoice_instance__period_uid
        self.invoice_instance__currency_uid = invoice_instance__currency_uid
        self.invoice_instance__invoice_number = invoice_instance__invoice_number
        self.invoice_instance__invoice_details = invoice_instance__invoice_details
        self.invoice_instance__invoice_amount_net = invoice_instance__invoice_amount_net
        self.invoice_instance__invoice_amount_tax = invoice_instance__invoice_amount_tax
        self.invoice_instance__invoice_amount_gross = invoice_instance__invoice_amount_gross
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.time_entry_final_uid, self.time_entry_final_name, self.tenant_uid, self.account_uid, self.project_instance_uid, self.project_milestone_uid, self.invoice_instance_uid, self.entry_period, self.entry_note, self.lock_uid, self.start_date, self.end_date, self.entry_minutes, self.is_approved, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes, self.tenant__tenant_name, self.tenant__country_uid, self.tenant__tenant_type_uid, self.tenant__tenant_category_uid, self.tenant__tenant_code, self.tenant__tenant_description, self.tenant__start_date, self.tenant__end_date, self.tenant__is_internal, self.tenant__is_system, self.tenant__is_test, self.tenant__account_uid, self.account__account_name, self.account__tenant_uid, self.account__account_type_uid, self.account__account_title_uid, self.account__account_division_uid, self.account__account_group_uid, self.account__auth_identity_uid, self.account__account_email, self.account__display_name, self.account__account_address, self.account__is_verified, self.account__is_system, self.project_instance__project_instance_name, self.project_instance__tenant_uid, self.project_instance__client_uid, self.project_instance__project_type_uid, self.project_instance__manager_account_uid, self.project_instance__project_group_uid, self.project_instance__project_code, self.project_instance__project_description, self.project_instance__is_billable, self.project_instance__start_date, self.project_instance__end_date, self.project_instance__current_billed, self.project_instance__budget, self.project_milestone__project_milestone_name, self.project_milestone__tenant_uid, self.project_milestone__client_uid, self.project_milestone__project_instance_uid, self.project_milestone__project_budget_uid, self.project_milestone__start_date, self.project_milestone__end_date, self.project_milestone__status_name, self.invoice_instance__invoice_instance_name, self.invoice_instance__tenant_uid, self.invoice_instance__account_uid, self.invoice_instance__invoice_flow_uid, self.invoice_instance__invoice_status_uid, self.invoice_instance__invoice_category_uid, self.invoice_instance__invoice_type_uid, self.invoice_instance__period_uid, self.invoice_instance__currency_uid, self.invoice_instance__invoice_number, self.invoice_instance__invoice_details, self.invoice_instance__invoice_amount_net, self.invoice_instance__invoice_amount_tax, self.invoice_instance__invoice_amount_gross]


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
    tenant__tenant_name: str | None
    tenant__country_uid: str | None
    tenant__tenant_type_uid: str | None
    tenant__tenant_category_uid: str | None
    tenant__tenant_code: str | None
    tenant__tenant_description: str | None
    tenant__start_date: datetime.datetime | None
    tenant__end_date: datetime.datetime | None
    tenant__is_internal: int | None
    tenant__is_system: int | None
    tenant__is_test: int | None
    tenant__account_uid: str | None
    account__account_name: str | None
    account__tenant_uid: str | None
    account__account_type_uid: str | None
    account__account_title_uid: str | None
    account__account_division_uid: str | None
    account__account_group_uid: str | None
    account__auth_identity_uid: str | None
    account__account_email: str | None
    account__display_name: str | None
    account__account_address: str | None
    account__is_verified: int | None
    account__is_system: int | None
    time_submit__time_submit_name: str | None
    time_submit__tenant_uid: str | None
    time_submit__account_uid: str | None
    time_submit__period_uid: str | None
    time_submit__time_submit_description: str | None
    time_entry__time_entry_name: str | None
    time_entry__time_submit_uid: str | None
    time_entry__tenant_uid: str | None
    time_entry__account_uid: str | None
    time_entry__project_instance_uid: str | None
    time_entry__project_milestone_uid: str | None
    time_entry__period_uid: str | None
    time_entry__invoice_instance_uid: str | None
    time_entry__entry_period: str | None
    time_entry__entry_note: str | None
    time_entry__lock_row: str | None
    time_entry__start_date: datetime.datetime | None
    time_entry__end_date: datetime.datetime | None
    time_entry__entry_minutes: int | None
    time_entry__is_approved: int | None
    project_instance__project_instance_name: str | None
    project_instance__tenant_uid: str | None
    project_instance__client_uid: str | None
    project_instance__project_type_uid: str | None
    project_instance__manager_account_uid: str | None
    project_instance__project_group_uid: str | None
    project_instance__project_code: str | None
    project_instance__project_description: str | None
    project_instance__is_billable: int | None
    project_instance__start_date: datetime.datetime | None
    project_instance__end_date: datetime.datetime | None
    project_instance__current_billed: str | None
    project_instance__budget: str | None
    project_milestone__project_milestone_name: str | None
    project_milestone__tenant_uid: str | None
    project_milestone__client_uid: str | None
    project_milestone__project_instance_uid: str | None
    project_milestone__project_budget_uid: str | None
    project_milestone__start_date: datetime.datetime | None
    project_milestone__end_date: datetime.datetime | None
    project_milestone__status_name: str | None
    period__period_name: str | None
    period__period_number: int | None
    period__period_type: str | None
    period__period_start_time: datetime.datetime | None
    period__period_end_time: datetime.datetime | None
    period__period_year: int | None
    period__period_quarter: int | None
    period__period_month: int | None
    period__period_week: int | None
    period__period_day: int | None
    invoice_instance__invoice_instance_name: str | None
    invoice_instance__tenant_uid: str | None
    invoice_instance__account_uid: str | None
    invoice_instance__invoice_flow_uid: str | None
    invoice_instance__invoice_status_uid: str | None
    invoice_instance__invoice_category_uid: str | None
    invoice_instance__invoice_type_uid: str | None
    invoice_instance__period_uid: str | None
    invoice_instance__currency_uid: str | None
    invoice_instance__invoice_number: str | None
    invoice_instance__invoice_details: str | None
    invoice_instance__invoice_amount_net: str | None
    invoice_instance__invoice_amount_tax: str | None
    invoice_instance__invoice_amount_gross: str | None
    def __init__(self, time_entry_invoice_uid: str | None, time_entry_invoice_name: str | None, tenant_uid: str | None, account_uid: str | None, time_submit_uid: str | None, time_entry_uid: str | None, project_instance_uid: str | None, project_milestone_uid: str | None, period_uid: str | None, invoice_instance_uid: str | None, entry_period: str | None, entry_note: str | None, lock_row: str | None, start_date: datetime.datetime | None, end_date: datetime.datetime | None, entry_minutes: int | None, is_approved: int | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None, tenant__tenant_name: str | None, tenant__country_uid: str | None, tenant__tenant_type_uid: str | None, tenant__tenant_category_uid: str | None, tenant__tenant_code: str | None, tenant__tenant_description: str | None, tenant__start_date: datetime.datetime | None, tenant__end_date: datetime.datetime | None, tenant__is_internal: int | None, tenant__is_system: int | None, tenant__is_test: int | None, tenant__account_uid: str | None, account__account_name: str | None, account__tenant_uid: str | None, account__account_type_uid: str | None, account__account_title_uid: str | None, account__account_division_uid: str | None, account__account_group_uid: str | None, account__auth_identity_uid: str | None, account__account_email: str | None, account__display_name: str | None, account__account_address: str | None, account__is_verified: int | None, account__is_system: int | None, time_submit__time_submit_name: str | None, time_submit__tenant_uid: str | None, time_submit__account_uid: str | None, time_submit__period_uid: str | None, time_submit__time_submit_description: str | None, time_entry__time_entry_name: str | None, time_entry__time_submit_uid: str | None, time_entry__tenant_uid: str | None, time_entry__account_uid: str | None, time_entry__project_instance_uid: str | None, time_entry__project_milestone_uid: str | None, time_entry__period_uid: str | None, time_entry__invoice_instance_uid: str | None, time_entry__entry_period: str | None, time_entry__entry_note: str | None, time_entry__lock_row: str | None, time_entry__start_date: datetime.datetime | None, time_entry__end_date: datetime.datetime | None, time_entry__entry_minutes: int | None, time_entry__is_approved: int | None, project_instance__project_instance_name: str | None, project_instance__tenant_uid: str | None, project_instance__client_uid: str | None, project_instance__project_type_uid: str | None, project_instance__manager_account_uid: str | None, project_instance__project_group_uid: str | None, project_instance__project_code: str | None, project_instance__project_description: str | None, project_instance__is_billable: int | None, project_instance__start_date: datetime.datetime | None, project_instance__end_date: datetime.datetime | None, project_instance__current_billed: str | None, project_instance__budget: str | None, project_milestone__project_milestone_name: str | None, project_milestone__tenant_uid: str | None, project_milestone__client_uid: str | None, project_milestone__project_instance_uid: str | None, project_milestone__project_budget_uid: str | None, project_milestone__start_date: datetime.datetime | None, project_milestone__end_date: datetime.datetime | None, project_milestone__status_name: str | None, period__period_name: str | None, period__period_number: int | None, period__period_type: str | None, period__period_start_time: datetime.datetime | None, period__period_end_time: datetime.datetime | None, period__period_year: int | None, period__period_quarter: int | None, period__period_month: int | None, period__period_week: int | None, period__period_day: int | None, invoice_instance__invoice_instance_name: str | None, invoice_instance__tenant_uid: str | None, invoice_instance__account_uid: str | None, invoice_instance__invoice_flow_uid: str | None, invoice_instance__invoice_status_uid: str | None, invoice_instance__invoice_category_uid: str | None, invoice_instance__invoice_type_uid: str | None, invoice_instance__period_uid: str | None, invoice_instance__currency_uid: str | None, invoice_instance__invoice_number: str | None, invoice_instance__invoice_details: str | None, invoice_instance__invoice_amount_net: str | None, invoice_instance__invoice_amount_tax: str | None, invoice_instance__invoice_amount_gross: str | None):
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
        self.tenant__tenant_name = tenant__tenant_name
        self.tenant__country_uid = tenant__country_uid
        self.tenant__tenant_type_uid = tenant__tenant_type_uid
        self.tenant__tenant_category_uid = tenant__tenant_category_uid
        self.tenant__tenant_code = tenant__tenant_code
        self.tenant__tenant_description = tenant__tenant_description
        self.tenant__start_date = tenant__start_date
        self.tenant__end_date = tenant__end_date
        self.tenant__is_internal = tenant__is_internal
        self.tenant__is_system = tenant__is_system
        self.tenant__is_test = tenant__is_test
        self.tenant__account_uid = tenant__account_uid
        self.account__account_name = account__account_name
        self.account__tenant_uid = account__tenant_uid
        self.account__account_type_uid = account__account_type_uid
        self.account__account_title_uid = account__account_title_uid
        self.account__account_division_uid = account__account_division_uid
        self.account__account_group_uid = account__account_group_uid
        self.account__auth_identity_uid = account__auth_identity_uid
        self.account__account_email = account__account_email
        self.account__display_name = account__display_name
        self.account__account_address = account__account_address
        self.account__is_verified = account__is_verified
        self.account__is_system = account__is_system
        self.time_submit__time_submit_name = time_submit__time_submit_name
        self.time_submit__tenant_uid = time_submit__tenant_uid
        self.time_submit__account_uid = time_submit__account_uid
        self.time_submit__period_uid = time_submit__period_uid
        self.time_submit__time_submit_description = time_submit__time_submit_description
        self.time_entry__time_entry_name = time_entry__time_entry_name
        self.time_entry__time_submit_uid = time_entry__time_submit_uid
        self.time_entry__tenant_uid = time_entry__tenant_uid
        self.time_entry__account_uid = time_entry__account_uid
        self.time_entry__project_instance_uid = time_entry__project_instance_uid
        self.time_entry__project_milestone_uid = time_entry__project_milestone_uid
        self.time_entry__period_uid = time_entry__period_uid
        self.time_entry__invoice_instance_uid = time_entry__invoice_instance_uid
        self.time_entry__entry_period = time_entry__entry_period
        self.time_entry__entry_note = time_entry__entry_note
        self.time_entry__lock_row = time_entry__lock_row
        self.time_entry__start_date = time_entry__start_date
        self.time_entry__end_date = time_entry__end_date
        self.time_entry__entry_minutes = time_entry__entry_minutes
        self.time_entry__is_approved = time_entry__is_approved
        self.project_instance__project_instance_name = project_instance__project_instance_name
        self.project_instance__tenant_uid = project_instance__tenant_uid
        self.project_instance__client_uid = project_instance__client_uid
        self.project_instance__project_type_uid = project_instance__project_type_uid
        self.project_instance__manager_account_uid = project_instance__manager_account_uid
        self.project_instance__project_group_uid = project_instance__project_group_uid
        self.project_instance__project_code = project_instance__project_code
        self.project_instance__project_description = project_instance__project_description
        self.project_instance__is_billable = project_instance__is_billable
        self.project_instance__start_date = project_instance__start_date
        self.project_instance__end_date = project_instance__end_date
        self.project_instance__current_billed = project_instance__current_billed
        self.project_instance__budget = project_instance__budget
        self.project_milestone__project_milestone_name = project_milestone__project_milestone_name
        self.project_milestone__tenant_uid = project_milestone__tenant_uid
        self.project_milestone__client_uid = project_milestone__client_uid
        self.project_milestone__project_instance_uid = project_milestone__project_instance_uid
        self.project_milestone__project_budget_uid = project_milestone__project_budget_uid
        self.project_milestone__start_date = project_milestone__start_date
        self.project_milestone__end_date = project_milestone__end_date
        self.project_milestone__status_name = project_milestone__status_name
        self.period__period_name = period__period_name
        self.period__period_number = period__period_number
        self.period__period_type = period__period_type
        self.period__period_start_time = period__period_start_time
        self.period__period_end_time = period__period_end_time
        self.period__period_year = period__period_year
        self.period__period_quarter = period__period_quarter
        self.period__period_month = period__period_month
        self.period__period_week = period__period_week
        self.period__period_day = period__period_day
        self.invoice_instance__invoice_instance_name = invoice_instance__invoice_instance_name
        self.invoice_instance__tenant_uid = invoice_instance__tenant_uid
        self.invoice_instance__account_uid = invoice_instance__account_uid
        self.invoice_instance__invoice_flow_uid = invoice_instance__invoice_flow_uid
        self.invoice_instance__invoice_status_uid = invoice_instance__invoice_status_uid
        self.invoice_instance__invoice_category_uid = invoice_instance__invoice_category_uid
        self.invoice_instance__invoice_type_uid = invoice_instance__invoice_type_uid
        self.invoice_instance__period_uid = invoice_instance__period_uid
        self.invoice_instance__currency_uid = invoice_instance__currency_uid
        self.invoice_instance__invoice_number = invoice_instance__invoice_number
        self.invoice_instance__invoice_details = invoice_instance__invoice_details
        self.invoice_instance__invoice_amount_net = invoice_instance__invoice_amount_net
        self.invoice_instance__invoice_amount_tax = invoice_instance__invoice_amount_tax
        self.invoice_instance__invoice_amount_gross = invoice_instance__invoice_amount_gross
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.time_entry_invoice_uid, self.time_entry_invoice_name, self.tenant_uid, self.account_uid, self.time_submit_uid, self.time_entry_uid, self.project_instance_uid, self.project_milestone_uid, self.period_uid, self.invoice_instance_uid, self.entry_period, self.entry_note, self.lock_row, self.start_date, self.end_date, self.entry_minutes, self.is_approved, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes, self.tenant__tenant_name, self.tenant__country_uid, self.tenant__tenant_type_uid, self.tenant__tenant_category_uid, self.tenant__tenant_code, self.tenant__tenant_description, self.tenant__start_date, self.tenant__end_date, self.tenant__is_internal, self.tenant__is_system, self.tenant__is_test, self.tenant__account_uid, self.account__account_name, self.account__tenant_uid, self.account__account_type_uid, self.account__account_title_uid, self.account__account_division_uid, self.account__account_group_uid, self.account__auth_identity_uid, self.account__account_email, self.account__display_name, self.account__account_address, self.account__is_verified, self.account__is_system, self.time_submit__time_submit_name, self.time_submit__tenant_uid, self.time_submit__account_uid, self.time_submit__period_uid, self.time_submit__time_submit_description, self.time_entry__time_entry_name, self.time_entry__time_submit_uid, self.time_entry__tenant_uid, self.time_entry__account_uid, self.time_entry__project_instance_uid, self.time_entry__project_milestone_uid, self.time_entry__period_uid, self.time_entry__invoice_instance_uid, self.time_entry__entry_period, self.time_entry__entry_note, self.time_entry__lock_row, self.time_entry__start_date, self.time_entry__end_date, self.time_entry__entry_minutes, self.time_entry__is_approved, self.project_instance__project_instance_name, self.project_instance__tenant_uid, self.project_instance__client_uid, self.project_instance__project_type_uid, self.project_instance__manager_account_uid, self.project_instance__project_group_uid, self.project_instance__project_code, self.project_instance__project_description, self.project_instance__is_billable, self.project_instance__start_date, self.project_instance__end_date, self.project_instance__current_billed, self.project_instance__budget, self.project_milestone__project_milestone_name, self.project_milestone__tenant_uid, self.project_milestone__client_uid, self.project_milestone__project_instance_uid, self.project_milestone__project_budget_uid, self.project_milestone__start_date, self.project_milestone__end_date, self.project_milestone__status_name, self.period__period_name, self.period__period_number, self.period__period_type, self.period__period_start_time, self.period__period_end_time, self.period__period_year, self.period__period_quarter, self.period__period_month, self.period__period_week, self.period__period_day, self.invoice_instance__invoice_instance_name, self.invoice_instance__tenant_uid, self.invoice_instance__account_uid, self.invoice_instance__invoice_flow_uid, self.invoice_instance__invoice_status_uid, self.invoice_instance__invoice_category_uid, self.invoice_instance__invoice_type_uid, self.invoice_instance__period_uid, self.invoice_instance__currency_uid, self.invoice_instance__invoice_number, self.invoice_instance__invoice_details, self.invoice_instance__invoice_amount_net, self.invoice_instance__invoice_amount_tax, self.invoice_instance__invoice_amount_gross]


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
    time_rule_client__client_name: str | None
    time_rule_client__tenant_uid: str | None
    time_rule_client__country_uid: str | None
    time_rule_client__client_type_uid: str | None
    time_rule_client__client_category_uid: str | None
    time_rule_client__account_uid: str | None
    time_rule_client__client_code: str | None
    time_rule_client__client_description: str | None
    time_rule_client__start_date: datetime.datetime | None
    time_rule_client__end_date: datetime.datetime | None
    time_rule_client__is_internal: int | None
    time_rule_client__is_system: int | None
    time_rule_client__is_test: int | None
    def __init__(self, time_rule_client_uid: str | None, time_rule_client_name: str | None, time_rule_definition: str | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None, time_rule_client__client_name: str | None, time_rule_client__tenant_uid: str | None, time_rule_client__country_uid: str | None, time_rule_client__client_type_uid: str | None, time_rule_client__client_category_uid: str | None, time_rule_client__account_uid: str | None, time_rule_client__client_code: str | None, time_rule_client__client_description: str | None, time_rule_client__start_date: datetime.datetime | None, time_rule_client__end_date: datetime.datetime | None, time_rule_client__is_internal: int | None, time_rule_client__is_system: int | None, time_rule_client__is_test: int | None):
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
        self.time_rule_client__client_name = time_rule_client__client_name
        self.time_rule_client__tenant_uid = time_rule_client__tenant_uid
        self.time_rule_client__country_uid = time_rule_client__country_uid
        self.time_rule_client__client_type_uid = time_rule_client__client_type_uid
        self.time_rule_client__client_category_uid = time_rule_client__client_category_uid
        self.time_rule_client__account_uid = time_rule_client__account_uid
        self.time_rule_client__client_code = time_rule_client__client_code
        self.time_rule_client__client_description = time_rule_client__client_description
        self.time_rule_client__start_date = time_rule_client__start_date
        self.time_rule_client__end_date = time_rule_client__end_date
        self.time_rule_client__is_internal = time_rule_client__is_internal
        self.time_rule_client__is_system = time_rule_client__is_system
        self.time_rule_client__is_test = time_rule_client__is_test
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.time_rule_client_uid, self.time_rule_client_name, self.time_rule_definition, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes, self.time_rule_client__client_name, self.time_rule_client__tenant_uid, self.time_rule_client__country_uid, self.time_rule_client__client_type_uid, self.time_rule_client__client_category_uid, self.time_rule_client__account_uid, self.time_rule_client__client_code, self.time_rule_client__client_description, self.time_rule_client__start_date, self.time_rule_client__end_date, self.time_rule_client__is_internal, self.time_rule_client__is_system, self.time_rule_client__is_test]


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
    tenant__tenant_name: str | None
    tenant__country_uid: str | None
    tenant__tenant_type_uid: str | None
    tenant__tenant_category_uid: str | None
    tenant__tenant_code: str | None
    tenant__tenant_description: str | None
    tenant__start_date: datetime.datetime | None
    tenant__end_date: datetime.datetime | None
    tenant__is_internal: int | None
    tenant__is_system: int | None
    tenant__is_test: int | None
    tenant__account_uid: str | None
    account__account_name: str | None
    account__tenant_uid: str | None
    account__account_type_uid: str | None
    account__account_title_uid: str | None
    account__account_division_uid: str | None
    account__account_group_uid: str | None
    account__auth_identity_uid: str | None
    account__account_email: str | None
    account__display_name: str | None
    account__account_address: str | None
    account__is_verified: int | None
    account__is_system: int | None
    period__period_name: str | None
    period__period_number: int | None
    period__period_type: str | None
    period__period_start_time: datetime.datetime | None
    period__period_end_time: datetime.datetime | None
    period__period_year: int | None
    period__period_quarter: int | None
    period__period_month: int | None
    period__period_week: int | None
    period__period_day: int | None
    def __init__(self, time_submit_uid: str | None, time_submit_name: str | None, tenant_uid: str | None, account_uid: str | None, period_uid: str | None, time_submit_description: str | None, row_instance: str | None, row_lock: str | None, row_owner: str | None, row_seq: int | None, row_guid: str | None, row_version: int | None, is_active: int | None, created_date: datetime.datetime | None, created_by: str | None, last_updated_date: datetime.datetime | None, last_updated_by: str | None, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str | None, tenant__tenant_name: str | None, tenant__country_uid: str | None, tenant__tenant_type_uid: str | None, tenant__tenant_category_uid: str | None, tenant__tenant_code: str | None, tenant__tenant_description: str | None, tenant__start_date: datetime.datetime | None, tenant__end_date: datetime.datetime | None, tenant__is_internal: int | None, tenant__is_system: int | None, tenant__is_test: int | None, tenant__account_uid: str | None, account__account_name: str | None, account__tenant_uid: str | None, account__account_type_uid: str | None, account__account_title_uid: str | None, account__account_division_uid: str | None, account__account_group_uid: str | None, account__auth_identity_uid: str | None, account__account_email: str | None, account__display_name: str | None, account__account_address: str | None, account__is_verified: int | None, account__is_system: int | None, period__period_name: str | None, period__period_number: int | None, period__period_type: str | None, period__period_start_time: datetime.datetime | None, period__period_end_time: datetime.datetime | None, period__period_year: int | None, period__period_quarter: int | None, period__period_month: int | None, period__period_week: int | None, period__period_day: int | None):
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
        self.tenant__tenant_name = tenant__tenant_name
        self.tenant__country_uid = tenant__country_uid
        self.tenant__tenant_type_uid = tenant__tenant_type_uid
        self.tenant__tenant_category_uid = tenant__tenant_category_uid
        self.tenant__tenant_code = tenant__tenant_code
        self.tenant__tenant_description = tenant__tenant_description
        self.tenant__start_date = tenant__start_date
        self.tenant__end_date = tenant__end_date
        self.tenant__is_internal = tenant__is_internal
        self.tenant__is_system = tenant__is_system
        self.tenant__is_test = tenant__is_test
        self.tenant__account_uid = tenant__account_uid
        self.account__account_name = account__account_name
        self.account__tenant_uid = account__tenant_uid
        self.account__account_type_uid = account__account_type_uid
        self.account__account_title_uid = account__account_title_uid
        self.account__account_division_uid = account__account_division_uid
        self.account__account_group_uid = account__account_group_uid
        self.account__auth_identity_uid = account__auth_identity_uid
        self.account__account_email = account__account_email
        self.account__display_name = account__display_name
        self.account__account_address = account__account_address
        self.account__is_verified = account__is_verified
        self.account__is_system = account__is_system
        self.period__period_name = period__period_name
        self.period__period_number = period__period_number
        self.period__period_type = period__period_type
        self.period__period_start_time = period__period_start_time
        self.period__period_end_time = period__period_end_time
        self.period__period_year = period__period_year
        self.period__period_quarter = period__period_quarter
        self.period__period_month = period__period_month
        self.period__period_week = period__period_week
        self.period__period_day = period__period_day
    def to_rich_dict(self) -> dict:
        return asdict(self)
    def get_rich_all_values(self) -> list[any]:
        return [self.time_submit_uid, self.time_submit_name, self.tenant_uid, self.account_uid, self.period_uid, self.time_submit_description, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes, self.tenant__tenant_name, self.tenant__country_uid, self.tenant__tenant_type_uid, self.tenant__tenant_category_uid, self.tenant__tenant_code, self.tenant__tenant_description, self.tenant__start_date, self.tenant__end_date, self.tenant__is_internal, self.tenant__is_system, self.tenant__is_test, self.tenant__account_uid, self.account__account_name, self.account__tenant_uid, self.account__account_type_uid, self.account__account_title_uid, self.account__account_division_uid, self.account__account_group_uid, self.account__auth_identity_uid, self.account__account_email, self.account__display_name, self.account__account_address, self.account__is_verified, self.account__is_system, self.period__period_name, self.period__period_number, self.period__period_type, self.period__period_start_time, self.period__period_end_time, self.period__period_year, self.period__period_quarter, self.period__period_month, self.period__period_week, self.period__period_day]


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