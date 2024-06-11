# auto-generated - v_definition_python_dtos_read - START at 2024-04-21 11:58:41.449427+00
import datetime
from datetime import datetime
from abc import abstractmethod
from dataclasses import dataclass

from base.base_interfaces import *
from dto.dtos import *
from dto.dtos_thin import *
from dto.dtos_write import *


@dataclass(frozen=False)
class account_read_dto(base_read_dto, account_write_dto, account_interface_dto):
    account_uid: str
    account_name: str
    tenant_uid: str
    account_type_uid: str
    account_title_uid: str
    account_division_uid: str
    account_group_uid: str
    auth_identity_uid: str
    account_email: str
    display_name: str
    account_address: str
    is_verified: int
    is_system: int
    row_instance: str
    row_lock: str | None
    row_owner: str
    row_seq: int
    row_guid: str
    row_version: int
    is_active: int
    created_date: datetime.datetime
    created_by: str
    last_updated_date: datetime.datetime
    last_updated_by: str
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str
    def __init__(self, account_uid: str, account_name: str, tenant_uid: str, account_type_uid: str, account_title_uid: str, account_division_uid: str, account_group_uid: str, auth_identity_uid: str, account_email: str, display_name: str, account_address: str, is_verified: int, is_system: int, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
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
    @classmethod
    def empty_read(cls):
        return cls(0, "", "", "", "", "", "", "", "", "", "", "", 0, 0, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def default_read(cls):
        return cls(0, base_dto.get_random_uid(), "", "", "", "", "", "", "", "", "", "", 0, 0, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def random_read(cls):
        return cls(0, base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), 0, 0, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_default(cls, account_uid: str, account_name: str, tenant_uid: str, account_type_uid: str, account_title_uid: str, account_division_uid: str, account_group_uid: str, auth_identity_uid: str, account_email: str, display_name: str, account_address: str, is_verified: int, is_system: int):
        return cls(0, account_uid, account_name, tenant_uid, account_type_uid, account_title_uid, account_division_uid, account_group_uid, auth_identity_uid, account_email, display_name, account_address, is_verified, is_system, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_full(cls, account_uid: str, account_name: str, tenant_uid: str, account_type_uid: str, account_title_uid: str, account_division_uid: str, account_group_uid: str, auth_identity_uid: str, account_email: str, display_name: str, account_address: str, is_verified: int, is_system: int, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
        return cls(account_uid, account_name, tenant_uid, account_type_uid, account_title_uid, account_division_uid, account_group_uid, auth_identity_uid, account_email, display_name, account_address, is_verified, is_system, row_instance, row_lock, row_owner, row_seq, row_guid, row_version, is_active, created_date, created_by, last_updated_date, last_updated_by, removed_date, removed_by, custom_attributes)
    @classmethod
    def from_write(cls, dto: account_write_dto):
        return cls(0, dto.account_uid, dto.account_name, dto.tenant_uid, dto.account_type_uid, dto.account_title_uid, dto.account_division_uid, dto.account_group_uid, dto.auth_identity_uid, dto.account_email, dto.display_name, dto.account_address, dto.is_verified, dto.is_system, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, dto.custom_attributes)
    def clone_read(self):
        return account_read_dto(self.account_uid, self.account_name, self.tenant_uid, self.account_type_uid, self.account_title_uid, self.account_division_uid, self.account_group_uid, self.auth_identity_uid, self.account_email, self.display_name, self.account_address, self.is_verified, self.is_system, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes)
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["account_uid"], d["account_name"], d["tenant_uid"], d["account_type_uid"], d["account_title_uid"], d["account_division_uid"], d["account_group_uid"], d["auth_identity_uid"], d["account_email"], d["display_name"], d["account_address"], d["is_verified"], d["is_system"], d["row_instance"], d["row_lock"], d["row_owner"], d["row_seq"], d["row_guid"], d["row_version"], d["is_active"], d["created_date"], d["created_by"], d["last_updated_date"], d["last_updated_by"], d["removed_date"], d["removed_by"], d["custom_attributes"])
    def to_read_dict(self) -> dict:
        return asdict(self)
    def to_write(self) -> account_write_dto:
        return account_write_dto(self.account_uid, self.account_name, self.tenant_uid, self.account_type_uid, self.account_title_uid, self.account_division_uid, self.account_group_uid, self.auth_identity_uid, self.account_email, self.display_name, self.account_address, self.is_verified, self.is_system, self.custom_attributes)
    def to_thin(self) -> account_thin_dto:
        return account_thin_dto(self.account_uid, self.account_name, self.created_date, self.is_active)
    def touch(self, updated_by: str = "system"):
        self.last_updated_date = datetime.datetime.now()
        self.last_updated_by = updated_by
        self.row_version = self.row_version+1
    def get_list_all_values(self) -> list[any]:
        return [self.account_uid, self.account_name, self.tenant_uid, self.account_type_uid, self.account_title_uid, self.account_division_uid, self.account_group_uid, self.auth_identity_uid, self.account_email, self.display_name, self.account_address, self.is_verified, self.is_system, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]
    def get_list_update_values(self, updated_by: str) -> list[any]:
        return [self.account_name, self.tenant_uid, self.account_type_uid, self.account_title_uid, self.account_division_uid, self.account_group_uid, self.auth_identity_uid, self.account_email, self.display_name, self.account_address, self.is_verified, self.is_system, self.custom_attributes, updated_by, self.account_uid]
    def is_older_than(self, dt: datetime.datetime) -> bool:
        return self.created_date < dt
    def is_newer_than(self, dt: datetime.datetime) -> bool:
        return self.created_date > dt
    def to_json_read(self) -> str:
        return json.dumps(self.to_read_dict())


@dataclass(frozen=False)
class account_division_read_dto(base_read_dto, account_division_write_dto):
    account_division_uid: str
    account_division_name: str
    tenant_uid: str
    account_uid: str
    account_division_template_uid: str
    division_description: str
    row_instance: str
    row_lock: str | None
    row_owner: str
    row_seq: int
    row_guid: str
    row_version: int
    is_active: int
    created_date: datetime.datetime
    created_by: str
    last_updated_date: datetime.datetime
    last_updated_by: str
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str
    def __init__(self, account_division_uid: str, account_division_name: str, tenant_uid: str, account_uid: str, account_division_template_uid: str, division_description: str, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
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
    @classmethod
    def empty_read(cls):
        return cls(0, "", "", "", "", "", "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def default_read(cls):
        return cls(0, base_dto.get_random_uid(), "", "", "", "", "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def random_read(cls):
        return cls(0, base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_default(cls, account_division_uid: str, account_division_name: str, tenant_uid: str, account_uid: str, account_division_template_uid: str, division_description: str):
        return cls(0, account_division_uid, account_division_name, tenant_uid, account_uid, account_division_template_uid, division_description, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_full(cls, account_division_uid: str, account_division_name: str, tenant_uid: str, account_uid: str, account_division_template_uid: str, division_description: str, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
        return cls(account_division_uid, account_division_name, tenant_uid, account_uid, account_division_template_uid, division_description, row_instance, row_lock, row_owner, row_seq, row_guid, row_version, is_active, created_date, created_by, last_updated_date, last_updated_by, removed_date, removed_by, custom_attributes)
    @classmethod
    def from_write(cls, dto: account_division_write_dto):
        return cls(0, dto.account_division_uid, dto.account_division_name, dto.tenant_uid, dto.account_uid, dto.account_division_template_uid, dto.division_description, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, dto.custom_attributes)
    def clone_read(self):
        return account_division_read_dto(self.account_division_uid, self.account_division_name, self.tenant_uid, self.account_uid, self.account_division_template_uid, self.division_description, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes)
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["account_division_uid"], d["account_division_name"], d["tenant_uid"], d["account_uid"], d["account_division_template_uid"], d["division_description"], d["row_instance"], d["row_lock"], d["row_owner"], d["row_seq"], d["row_guid"], d["row_version"], d["is_active"], d["created_date"], d["created_by"], d["last_updated_date"], d["last_updated_by"], d["removed_date"], d["removed_by"], d["custom_attributes"])
    def to_read_dict(self) -> dict:
        return asdict(self)
    def to_write(self) -> account_division_write_dto:
        return account_division_write_dto(self.account_division_uid, self.account_division_name, self.tenant_uid, self.account_uid, self.account_division_template_uid, self.division_description, self.custom_attributes)
    def to_thin(self) -> account_division_thin_dto:
        return account_division_thin_dto(self.account_division_uid, self.account_division_name, self.created_date, self.is_active)
    def touch(self, updated_by: str = "system"):
        self.last_updated_date = datetime.datetime.now()
        self.last_updated_by = updated_by
        self.row_version = self.row_version+1
    def get_list_all_values(self) -> list[any]:
        return [self.account_division_uid, self.account_division_name, self.tenant_uid, self.account_uid, self.account_division_template_uid, self.division_description, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]
    def get_list_update_values(self, updated_by: str) -> list[any]:
        return [self.account_division_name, self.tenant_uid, self.account_uid, self.account_division_template_uid, self.division_description, self.custom_attributes, updated_by, self.account_division_uid]
    def is_older_than(self, dt: datetime.datetime) -> bool:
        return self.created_date < dt
    def is_newer_than(self, dt: datetime.datetime) -> bool:
        return self.created_date > dt
    def to_json_read(self) -> str:
        return json.dumps(self.to_read_dict())


@dataclass(frozen=False)
class account_division_template_read_dto(base_read_dto, account_division_template_write_dto):
    account_division_template_uid: str
    account_division_template_name: str
    division_description: str
    row_instance: str
    row_lock: str | None
    row_owner: str
    row_seq: int
    row_guid: str
    row_version: int
    is_active: int
    created_date: datetime.datetime
    created_by: str
    last_updated_date: datetime.datetime
    last_updated_by: str
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str
    def __init__(self, account_division_template_uid: str, account_division_template_name: str, division_description: str, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
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
    @classmethod
    def empty_read(cls):
        return cls(0, "", "", "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def default_read(cls):
        return cls(0, base_dto.get_random_uid(), "", "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def random_read(cls):
        return cls(0, base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_default(cls, account_division_template_uid: str, account_division_template_name: str, division_description: str):
        return cls(0, account_division_template_uid, account_division_template_name, division_description, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_full(cls, account_division_template_uid: str, account_division_template_name: str, division_description: str, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
        return cls(account_division_template_uid, account_division_template_name, division_description, row_instance, row_lock, row_owner, row_seq, row_guid, row_version, is_active, created_date, created_by, last_updated_date, last_updated_by, removed_date, removed_by, custom_attributes)
    @classmethod
    def from_write(cls, dto: account_division_template_write_dto):
        return cls(0, dto.account_division_template_uid, dto.account_division_template_name, dto.division_description, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, dto.custom_attributes)
    def clone_read(self):
        return account_division_template_read_dto(self.account_division_template_uid, self.account_division_template_name, self.division_description, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes)
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["account_division_template_uid"], d["account_division_template_name"], d["division_description"], d["row_instance"], d["row_lock"], d["row_owner"], d["row_seq"], d["row_guid"], d["row_version"], d["is_active"], d["created_date"], d["created_by"], d["last_updated_date"], d["last_updated_by"], d["removed_date"], d["removed_by"], d["custom_attributes"])
    def to_read_dict(self) -> dict:
        return asdict(self)
    def to_write(self) -> account_division_template_write_dto:
        return account_division_template_write_dto(self.account_division_template_uid, self.account_division_template_name, self.division_description, self.custom_attributes)
    def to_thin(self) -> account_division_template_thin_dto:
        return account_division_template_thin_dto(self.account_division_template_uid, self.account_division_template_name, self.created_date, self.is_active)
    def touch(self, updated_by: str = "system"):
        self.last_updated_date = datetime.datetime.now()
        self.last_updated_by = updated_by
        self.row_version = self.row_version+1
    def get_list_all_values(self) -> list[any]:
        return [self.account_division_template_uid, self.account_division_template_name, self.division_description, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]
    def get_list_update_values(self, updated_by: str) -> list[any]:
        return [self.account_division_template_name, self.division_description, self.custom_attributes, updated_by, self.account_division_template_uid]
    def is_older_than(self, dt: datetime.datetime) -> bool:
        return self.created_date < dt
    def is_newer_than(self, dt: datetime.datetime) -> bool:
        return self.created_date > dt
    def to_json_read(self) -> str:
        return json.dumps(self.to_read_dict())


@dataclass(frozen=False)
class account_group_read_dto(base_read_dto, account_group_write_dto):
    account_group_uid: str
    account_group_name: str
    tenant_uid: str
    account_group_description: str
    row_instance: str
    row_lock: str | None
    row_owner: str
    row_seq: int
    row_guid: str
    row_version: int
    is_active: int
    created_date: datetime.datetime
    created_by: str
    last_updated_date: datetime.datetime
    last_updated_by: str
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str
    def __init__(self, account_group_uid: str, account_group_name: str, tenant_uid: str, account_group_description: str, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
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
    @classmethod
    def empty_read(cls):
        return cls(0, "", "", "", "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def default_read(cls):
        return cls(0, base_dto.get_random_uid(), "", "", "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def random_read(cls):
        return cls(0, base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_default(cls, account_group_uid: str, account_group_name: str, tenant_uid: str, account_group_description: str):
        return cls(0, account_group_uid, account_group_name, tenant_uid, account_group_description, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_full(cls, account_group_uid: str, account_group_name: str, tenant_uid: str, account_group_description: str, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
        return cls(account_group_uid, account_group_name, tenant_uid, account_group_description, row_instance, row_lock, row_owner, row_seq, row_guid, row_version, is_active, created_date, created_by, last_updated_date, last_updated_by, removed_date, removed_by, custom_attributes)
    @classmethod
    def from_write(cls, dto: account_group_write_dto):
        return cls(0, dto.account_group_uid, dto.account_group_name, dto.tenant_uid, dto.account_group_description, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, dto.custom_attributes)
    def clone_read(self):
        return account_group_read_dto(self.account_group_uid, self.account_group_name, self.tenant_uid, self.account_group_description, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes)
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["account_group_uid"], d["account_group_name"], d["tenant_uid"], d["account_group_description"], d["row_instance"], d["row_lock"], d["row_owner"], d["row_seq"], d["row_guid"], d["row_version"], d["is_active"], d["created_date"], d["created_by"], d["last_updated_date"], d["last_updated_by"], d["removed_date"], d["removed_by"], d["custom_attributes"])
    def to_read_dict(self) -> dict:
        return asdict(self)
    def to_write(self) -> account_group_write_dto:
        return account_group_write_dto(self.account_group_uid, self.account_group_name, self.tenant_uid, self.account_group_description, self.custom_attributes)
    def to_thin(self) -> account_group_thin_dto:
        return account_group_thin_dto(self.account_group_uid, self.account_group_name, self.created_date, self.is_active)
    def touch(self, updated_by: str = "system"):
        self.last_updated_date = datetime.datetime.now()
        self.last_updated_by = updated_by
        self.row_version = self.row_version+1
    def get_list_all_values(self) -> list[any]:
        return [self.account_group_uid, self.account_group_name, self.tenant_uid, self.account_group_description, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]
    def get_list_update_values(self, updated_by: str) -> list[any]:
        return [self.account_group_name, self.tenant_uid, self.account_group_description, self.custom_attributes, updated_by, self.account_group_uid]
    def is_older_than(self, dt: datetime.datetime) -> bool:
        return self.created_date < dt
    def is_newer_than(self, dt: datetime.datetime) -> bool:
        return self.created_date > dt
    def to_json_read(self) -> str:
        return json.dumps(self.to_read_dict())


@dataclass(frozen=False)
class account_group_assignment_read_dto(base_read_dto, account_group_assignment_write_dto):
    account_group_assignment_uid: str
    account_group_assignment_name: str
    tenant_uid: str
    account_group_uid: str
    account_uid: str
    account_group_role_uid: str
    start_date: datetime.datetime
    end_date: datetime.datetime
    row_instance: str
    row_lock: str | None
    row_owner: str
    row_seq: int
    row_guid: str
    row_version: int
    is_active: int
    created_date: datetime.datetime
    created_by: str
    last_updated_date: datetime.datetime
    last_updated_by: str
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str
    def __init__(self, account_group_assignment_uid: str, account_group_assignment_name: str, tenant_uid: str, account_group_uid: str, account_uid: str, account_group_role_uid: str, start_date: datetime.datetime, end_date: datetime.datetime, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
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
    @classmethod
    def empty_read(cls):
        return cls(0, "", "", "", "", "", "", datetime.datetime.now(), datetime.datetime.now(), "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def default_read(cls):
        return cls(0, base_dto.get_random_uid(), "", "", "", "", "", datetime.datetime.now(), datetime.datetime.now(), "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def random_read(cls):
        return cls(0, base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), datetime.datetime.now(), datetime.datetime.now(), "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_default(cls, account_group_assignment_uid: str, account_group_assignment_name: str, tenant_uid: str, account_group_uid: str, account_uid: str, account_group_role_uid: str, start_date: datetime.datetime, end_date: datetime.datetime):
        return cls(0, account_group_assignment_uid, account_group_assignment_name, tenant_uid, account_group_uid, account_uid, account_group_role_uid, start_date, end_date, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_full(cls, account_group_assignment_uid: str, account_group_assignment_name: str, tenant_uid: str, account_group_uid: str, account_uid: str, account_group_role_uid: str, start_date: datetime.datetime, end_date: datetime.datetime, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
        return cls(account_group_assignment_uid, account_group_assignment_name, tenant_uid, account_group_uid, account_uid, account_group_role_uid, start_date, end_date, row_instance, row_lock, row_owner, row_seq, row_guid, row_version, is_active, created_date, created_by, last_updated_date, last_updated_by, removed_date, removed_by, custom_attributes)
    @classmethod
    def from_write(cls, dto: account_group_assignment_write_dto):
        return cls(0, dto.account_group_assignment_uid, dto.account_group_assignment_name, dto.tenant_uid, dto.account_group_uid, dto.account_uid, dto.account_group_role_uid, dto.start_date, dto.end_date, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, dto.custom_attributes)
    def clone_read(self):
        return account_group_assignment_read_dto(self.account_group_assignment_uid, self.account_group_assignment_name, self.tenant_uid, self.account_group_uid, self.account_uid, self.account_group_role_uid, self.start_date, self.end_date, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes)
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["account_group_assignment_uid"], d["account_group_assignment_name"], d["tenant_uid"], d["account_group_uid"], d["account_uid"], d["account_group_role_uid"], d["start_date"], d["end_date"], d["row_instance"], d["row_lock"], d["row_owner"], d["row_seq"], d["row_guid"], d["row_version"], d["is_active"], d["created_date"], d["created_by"], d["last_updated_date"], d["last_updated_by"], d["removed_date"], d["removed_by"], d["custom_attributes"])
    def to_read_dict(self) -> dict:
        return asdict(self)
    def to_write(self) -> account_group_assignment_write_dto:
        return account_group_assignment_write_dto(self.account_group_assignment_uid, self.account_group_assignment_name, self.tenant_uid, self.account_group_uid, self.account_uid, self.account_group_role_uid, self.start_date, self.end_date, self.custom_attributes)
    def to_thin(self) -> account_group_assignment_thin_dto:
        return account_group_assignment_thin_dto(self.account_group_assignment_uid, self.account_group_assignment_name, self.created_date, self.is_active)
    def touch(self, updated_by: str = "system"):
        self.last_updated_date = datetime.datetime.now()
        self.last_updated_by = updated_by
        self.row_version = self.row_version+1
    def get_list_all_values(self) -> list[any]:
        return [self.account_group_assignment_uid, self.account_group_assignment_name, self.tenant_uid, self.account_group_uid, self.account_uid, self.account_group_role_uid, self.start_date, self.end_date, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]
    def get_list_update_values(self, updated_by: str) -> list[any]:
        return [self.account_group_assignment_name, self.tenant_uid, self.account_group_uid, self.account_uid, self.account_group_role_uid, self.start_date, self.end_date, self.custom_attributes, updated_by, self.account_group_assignment_uid]
    def is_older_than(self, dt: datetime.datetime) -> bool:
        return self.created_date < dt
    def is_newer_than(self, dt: datetime.datetime) -> bool:
        return self.created_date > dt
    def to_json_read(self) -> str:
        return json.dumps(self.to_read_dict())


@dataclass(frozen=False)
class account_group_role_read_dto(base_read_dto, account_group_role_write_dto):
    account_group_role_uid: str
    account_group_role_name: str
    row_instance: str
    row_lock: str | None
    row_owner: str
    row_seq: int
    row_guid: str
    row_version: int
    is_active: int
    created_date: datetime.datetime
    created_by: str
    last_updated_date: datetime.datetime
    last_updated_by: str
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str
    def __init__(self, account_group_role_uid: str, account_group_role_name: str, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
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
    @classmethod
    def empty_read(cls):
        return cls(0, "", "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def default_read(cls):
        return cls(0, base_dto.get_random_uid(), "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def random_read(cls):
        return cls(0, base_dto.get_random_uid(), base_dto.get_random_uid(), "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_default(cls, account_group_role_uid: str, account_group_role_name: str):
        return cls(0, account_group_role_uid, account_group_role_name, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_full(cls, account_group_role_uid: str, account_group_role_name: str, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
        return cls(account_group_role_uid, account_group_role_name, row_instance, row_lock, row_owner, row_seq, row_guid, row_version, is_active, created_date, created_by, last_updated_date, last_updated_by, removed_date, removed_by, custom_attributes)
    @classmethod
    def from_write(cls, dto: account_group_role_write_dto):
        return cls(0, dto.account_group_role_uid, dto.account_group_role_name, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, dto.custom_attributes)
    def clone_read(self):
        return account_group_role_read_dto(self.account_group_role_uid, self.account_group_role_name, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes)
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["account_group_role_uid"], d["account_group_role_name"], d["row_instance"], d["row_lock"], d["row_owner"], d["row_seq"], d["row_guid"], d["row_version"], d["is_active"], d["created_date"], d["created_by"], d["last_updated_date"], d["last_updated_by"], d["removed_date"], d["removed_by"], d["custom_attributes"])
    def to_read_dict(self) -> dict:
        return asdict(self)
    def to_write(self) -> account_group_role_write_dto:
        return account_group_role_write_dto(self.account_group_role_uid, self.account_group_role_name, self.custom_attributes)
    def to_thin(self) -> account_group_role_thin_dto:
        return account_group_role_thin_dto(self.account_group_role_uid, self.account_group_role_name, self.created_date, self.is_active)
    def touch(self, updated_by: str = "system"):
        self.last_updated_date = datetime.datetime.now()
        self.last_updated_by = updated_by
        self.row_version = self.row_version+1
    def get_list_all_values(self) -> list[any]:
        return [self.account_group_role_uid, self.account_group_role_name, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]
    def get_list_update_values(self, updated_by: str) -> list[any]:
        return [self.account_group_role_name, self.custom_attributes, updated_by, self.account_group_role_uid]
    def is_older_than(self, dt: datetime.datetime) -> bool:
        return self.created_date < dt
    def is_newer_than(self, dt: datetime.datetime) -> bool:
        return self.created_date > dt
    def to_json_read(self) -> str:
        return json.dumps(self.to_read_dict())


@dataclass(frozen=False)
class account_hierarchy_read_dto(base_read_dto, account_hierarchy_write_dto):
    account_hierarchy_uid: str
    account_hierarchy_name: str
    tenant_uid: str
    parent_account_uid: str
    child_account_uid: str
    row_instance: str
    row_lock: str | None
    row_owner: str
    row_seq: int
    row_guid: str
    row_version: int
    is_active: int
    created_date: datetime.datetime
    created_by: str
    last_updated_date: datetime.datetime
    last_updated_by: str
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str
    def __init__(self, account_hierarchy_uid: str, account_hierarchy_name: str, tenant_uid: str, parent_account_uid: str, child_account_uid: str, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
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
    @classmethod
    def empty_read(cls):
        return cls(0, "", "", "", "", "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def default_read(cls):
        return cls(0, base_dto.get_random_uid(), "", "", "", "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def random_read(cls):
        return cls(0, base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_default(cls, account_hierarchy_uid: str, account_hierarchy_name: str, tenant_uid: str, parent_account_uid: str, child_account_uid: str):
        return cls(0, account_hierarchy_uid, account_hierarchy_name, tenant_uid, parent_account_uid, child_account_uid, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_full(cls, account_hierarchy_uid: str, account_hierarchy_name: str, tenant_uid: str, parent_account_uid: str, child_account_uid: str, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
        return cls(account_hierarchy_uid, account_hierarchy_name, tenant_uid, parent_account_uid, child_account_uid, row_instance, row_lock, row_owner, row_seq, row_guid, row_version, is_active, created_date, created_by, last_updated_date, last_updated_by, removed_date, removed_by, custom_attributes)
    @classmethod
    def from_write(cls, dto: account_hierarchy_write_dto):
        return cls(0, dto.account_hierarchy_uid, dto.account_hierarchy_name, dto.tenant_uid, dto.parent_account_uid, dto.child_account_uid, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, dto.custom_attributes)
    def clone_read(self):
        return account_hierarchy_read_dto(self.account_hierarchy_uid, self.account_hierarchy_name, self.tenant_uid, self.parent_account_uid, self.child_account_uid, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes)
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["account_hierarchy_uid"], d["account_hierarchy_name"], d["tenant_uid"], d["parent_account_uid"], d["child_account_uid"], d["row_instance"], d["row_lock"], d["row_owner"], d["row_seq"], d["row_guid"], d["row_version"], d["is_active"], d["created_date"], d["created_by"], d["last_updated_date"], d["last_updated_by"], d["removed_date"], d["removed_by"], d["custom_attributes"])
    def to_read_dict(self) -> dict:
        return asdict(self)
    def to_write(self) -> account_hierarchy_write_dto:
        return account_hierarchy_write_dto(self.account_hierarchy_uid, self.account_hierarchy_name, self.tenant_uid, self.parent_account_uid, self.child_account_uid, self.custom_attributes)
    def to_thin(self) -> account_hierarchy_thin_dto:
        return account_hierarchy_thin_dto(self.account_hierarchy_uid, self.account_hierarchy_name, self.created_date, self.is_active)
    def touch(self, updated_by: str = "system"):
        self.last_updated_date = datetime.datetime.now()
        self.last_updated_by = updated_by
        self.row_version = self.row_version+1
    def get_list_all_values(self) -> list[any]:
        return [self.account_hierarchy_uid, self.account_hierarchy_name, self.tenant_uid, self.parent_account_uid, self.child_account_uid, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]
    def get_list_update_values(self, updated_by: str) -> list[any]:
        return [self.account_hierarchy_name, self.tenant_uid, self.parent_account_uid, self.child_account_uid, self.custom_attributes, updated_by, self.account_hierarchy_uid]
    def is_older_than(self, dt: datetime.datetime) -> bool:
        return self.created_date < dt
    def is_newer_than(self, dt: datetime.datetime) -> bool:
        return self.created_date > dt
    def to_json_read(self) -> str:
        return json.dumps(self.to_read_dict())


@dataclass(frozen=False)
class account_rate_read_dto(base_read_dto, account_rate_write_dto):
    account_rate_uid: str
    account_rate_name: str
    tenant_uid: str
    account_uid: str
    currency_uid: str
    rate: str
    start_date: datetime.datetime
    end_date: datetime.datetime
    row_instance: str
    row_lock: str | None
    row_owner: str
    row_seq: int
    row_guid: str
    row_version: int
    is_active: int
    created_date: datetime.datetime
    created_by: str
    last_updated_date: datetime.datetime
    last_updated_by: str
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str
    def __init__(self, account_rate_uid: str, account_rate_name: str, tenant_uid: str, account_uid: str, currency_uid: str, rate: str, start_date: datetime.datetime, end_date: datetime.datetime, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
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
    @classmethod
    def empty_read(cls):
        return cls(0, "", "", "", "", "", "", datetime.datetime.now(), datetime.datetime.now(), "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def default_read(cls):
        return cls(0, base_dto.get_random_uid(), "", "", "", "", "", datetime.datetime.now(), datetime.datetime.now(), "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def random_read(cls):
        return cls(0, base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), "", datetime.datetime.now(), datetime.datetime.now(), "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_default(cls, account_rate_uid: str, account_rate_name: str, tenant_uid: str, account_uid: str, currency_uid: str, rate: str, start_date: datetime.datetime, end_date: datetime.datetime):
        return cls(0, account_rate_uid, account_rate_name, tenant_uid, account_uid, currency_uid, rate, start_date, end_date, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_full(cls, account_rate_uid: str, account_rate_name: str, tenant_uid: str, account_uid: str, currency_uid: str, rate: str, start_date: datetime.datetime, end_date: datetime.datetime, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
        return cls(account_rate_uid, account_rate_name, tenant_uid, account_uid, currency_uid, rate, start_date, end_date, row_instance, row_lock, row_owner, row_seq, row_guid, row_version, is_active, created_date, created_by, last_updated_date, last_updated_by, removed_date, removed_by, custom_attributes)
    @classmethod
    def from_write(cls, dto: account_rate_write_dto):
        return cls(0, dto.account_rate_uid, dto.account_rate_name, dto.tenant_uid, dto.account_uid, dto.currency_uid, dto.rate, dto.start_date, dto.end_date, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, dto.custom_attributes)
    def clone_read(self):
        return account_rate_read_dto(self.account_rate_uid, self.account_rate_name, self.tenant_uid, self.account_uid, self.currency_uid, self.rate, self.start_date, self.end_date, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes)
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["account_rate_uid"], d["account_rate_name"], d["tenant_uid"], d["account_uid"], d["currency_uid"], d["rate"], d["start_date"], d["end_date"], d["row_instance"], d["row_lock"], d["row_owner"], d["row_seq"], d["row_guid"], d["row_version"], d["is_active"], d["created_date"], d["created_by"], d["last_updated_date"], d["last_updated_by"], d["removed_date"], d["removed_by"], d["custom_attributes"])
    def to_read_dict(self) -> dict:
        return asdict(self)
    def to_write(self) -> account_rate_write_dto:
        return account_rate_write_dto(self.account_rate_uid, self.account_rate_name, self.tenant_uid, self.account_uid, self.currency_uid, self.rate, self.start_date, self.end_date, self.custom_attributes)
    def to_thin(self) -> account_rate_thin_dto:
        return account_rate_thin_dto(self.account_rate_uid, self.account_rate_name, self.created_date, self.is_active)
    def touch(self, updated_by: str = "system"):
        self.last_updated_date = datetime.datetime.now()
        self.last_updated_by = updated_by
        self.row_version = self.row_version+1
    def get_list_all_values(self) -> list[any]:
        return [self.account_rate_uid, self.account_rate_name, self.tenant_uid, self.account_uid, self.currency_uid, self.rate, self.start_date, self.end_date, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]
    def get_list_update_values(self, updated_by: str) -> list[any]:
        return [self.account_rate_name, self.tenant_uid, self.account_uid, self.currency_uid, self.rate, self.start_date, self.end_date, self.custom_attributes, updated_by, self.account_rate_uid]
    def is_older_than(self, dt: datetime.datetime) -> bool:
        return self.created_date < dt
    def is_newer_than(self, dt: datetime.datetime) -> bool:
        return self.created_date > dt
    def to_json_read(self) -> str:
        return json.dumps(self.to_read_dict())


@dataclass(frozen=False)
class account_skill_read_dto(base_read_dto, account_skill_write_dto):
    account_skill_uid: str
    account_skill_name: str
    account_skill_description: str
    row_instance: str
    row_lock: str | None
    row_owner: str
    row_seq: int
    row_guid: str
    row_version: int
    is_active: int
    created_date: datetime.datetime
    created_by: str
    last_updated_date: datetime.datetime
    last_updated_by: str
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str
    def __init__(self, account_skill_uid: str, account_skill_name: str, account_skill_description: str, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
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
    @classmethod
    def empty_read(cls):
        return cls(0, "", "", "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def default_read(cls):
        return cls(0, base_dto.get_random_uid(), "", "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def random_read(cls):
        return cls(0, base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_default(cls, account_skill_uid: str, account_skill_name: str, account_skill_description: str):
        return cls(0, account_skill_uid, account_skill_name, account_skill_description, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_full(cls, account_skill_uid: str, account_skill_name: str, account_skill_description: str, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
        return cls(account_skill_uid, account_skill_name, account_skill_description, row_instance, row_lock, row_owner, row_seq, row_guid, row_version, is_active, created_date, created_by, last_updated_date, last_updated_by, removed_date, removed_by, custom_attributes)
    @classmethod
    def from_write(cls, dto: account_skill_write_dto):
        return cls(0, dto.account_skill_uid, dto.account_skill_name, dto.account_skill_description, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, dto.custom_attributes)
    def clone_read(self):
        return account_skill_read_dto(self.account_skill_uid, self.account_skill_name, self.account_skill_description, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes)
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["account_skill_uid"], d["account_skill_name"], d["account_skill_description"], d["row_instance"], d["row_lock"], d["row_owner"], d["row_seq"], d["row_guid"], d["row_version"], d["is_active"], d["created_date"], d["created_by"], d["last_updated_date"], d["last_updated_by"], d["removed_date"], d["removed_by"], d["custom_attributes"])
    def to_read_dict(self) -> dict:
        return asdict(self)
    def to_write(self) -> account_skill_write_dto:
        return account_skill_write_dto(self.account_skill_uid, self.account_skill_name, self.account_skill_description, self.custom_attributes)
    def to_thin(self) -> account_skill_thin_dto:
        return account_skill_thin_dto(self.account_skill_uid, self.account_skill_name, self.created_date, self.is_active)
    def touch(self, updated_by: str = "system"):
        self.last_updated_date = datetime.datetime.now()
        self.last_updated_by = updated_by
        self.row_version = self.row_version+1
    def get_list_all_values(self) -> list[any]:
        return [self.account_skill_uid, self.account_skill_name, self.account_skill_description, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]
    def get_list_update_values(self, updated_by: str) -> list[any]:
        return [self.account_skill_name, self.account_skill_description, self.custom_attributes, updated_by, self.account_skill_uid]
    def is_older_than(self, dt: datetime.datetime) -> bool:
        return self.created_date < dt
    def is_newer_than(self, dt: datetime.datetime) -> bool:
        return self.created_date > dt
    def to_json_read(self) -> str:
        return json.dumps(self.to_read_dict())


@dataclass(frozen=False)
class account_team_read_dto(base_read_dto, account_team_write_dto):
    account_team_uid: str
    account_team_name: str
    tenant_uid: str
    owner_account_uid: str
    is_public: int
    is_tenant: int
    is_private: int
    row_instance: str
    row_lock: str | None
    row_owner: str
    row_seq: int
    row_guid: str
    row_version: int
    is_active: int
    created_date: datetime.datetime
    created_by: str
    last_updated_date: datetime.datetime
    last_updated_by: str
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str
    def __init__(self, account_team_uid: str, account_team_name: str, tenant_uid: str, owner_account_uid: str, is_public: int, is_tenant: int, is_private: int, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
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
    @classmethod
    def empty_read(cls):
        return cls(0, "", "", "", "", 0, 0, 0, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def default_read(cls):
        return cls(0, base_dto.get_random_uid(), "", "", "", 0, 0, 0, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def random_read(cls):
        return cls(0, base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), 0, 0, 0, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_default(cls, account_team_uid: str, account_team_name: str, tenant_uid: str, owner_account_uid: str, is_public: int, is_tenant: int, is_private: int):
        return cls(0, account_team_uid, account_team_name, tenant_uid, owner_account_uid, is_public, is_tenant, is_private, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_full(cls, account_team_uid: str, account_team_name: str, tenant_uid: str, owner_account_uid: str, is_public: int, is_tenant: int, is_private: int, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
        return cls(account_team_uid, account_team_name, tenant_uid, owner_account_uid, is_public, is_tenant, is_private, row_instance, row_lock, row_owner, row_seq, row_guid, row_version, is_active, created_date, created_by, last_updated_date, last_updated_by, removed_date, removed_by, custom_attributes)
    @classmethod
    def from_write(cls, dto: account_team_write_dto):
        return cls(0, dto.account_team_uid, dto.account_team_name, dto.tenant_uid, dto.owner_account_uid, dto.is_public, dto.is_tenant, dto.is_private, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, dto.custom_attributes)
    def clone_read(self):
        return account_team_read_dto(self.account_team_uid, self.account_team_name, self.tenant_uid, self.owner_account_uid, self.is_public, self.is_tenant, self.is_private, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes)
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["account_team_uid"], d["account_team_name"], d["tenant_uid"], d["owner_account_uid"], d["is_public"], d["is_tenant"], d["is_private"], d["row_instance"], d["row_lock"], d["row_owner"], d["row_seq"], d["row_guid"], d["row_version"], d["is_active"], d["created_date"], d["created_by"], d["last_updated_date"], d["last_updated_by"], d["removed_date"], d["removed_by"], d["custom_attributes"])
    def to_read_dict(self) -> dict:
        return asdict(self)
    def to_write(self) -> account_team_write_dto:
        return account_team_write_dto(self.account_team_uid, self.account_team_name, self.tenant_uid, self.owner_account_uid, self.is_public, self.is_tenant, self.is_private, self.custom_attributes)
    def to_thin(self) -> account_team_thin_dto:
        return account_team_thin_dto(self.account_team_uid, self.account_team_name, self.created_date, self.is_active)
    def touch(self, updated_by: str = "system"):
        self.last_updated_date = datetime.datetime.now()
        self.last_updated_by = updated_by
        self.row_version = self.row_version+1
    def get_list_all_values(self) -> list[any]:
        return [self.account_team_uid, self.account_team_name, self.tenant_uid, self.owner_account_uid, self.is_public, self.is_tenant, self.is_private, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]
    def get_list_update_values(self, updated_by: str) -> list[any]:
        return [self.account_team_name, self.tenant_uid, self.owner_account_uid, self.is_public, self.is_tenant, self.is_private, self.custom_attributes, updated_by, self.account_team_uid]
    def is_older_than(self, dt: datetime.datetime) -> bool:
        return self.created_date < dt
    def is_newer_than(self, dt: datetime.datetime) -> bool:
        return self.created_date > dt
    def to_json_read(self) -> str:
        return json.dumps(self.to_read_dict())


@dataclass(frozen=False)
class account_title_read_dto(base_read_dto, account_title_write_dto):
    account_title_uid: str
    account_title_name: str
    title_description: str
    row_instance: str
    row_lock: str | None
    row_owner: str
    row_seq: int
    row_guid: str
    row_version: int
    is_active: int
    created_date: datetime.datetime
    created_by: str
    last_updated_date: datetime.datetime
    last_updated_by: str
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str
    def __init__(self, account_title_uid: str, account_title_name: str, title_description: str, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
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
    @classmethod
    def empty_read(cls):
        return cls(0, "", "", "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def default_read(cls):
        return cls(0, base_dto.get_random_uid(), "", "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def random_read(cls):
        return cls(0, base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_default(cls, account_title_uid: str, account_title_name: str, title_description: str):
        return cls(0, account_title_uid, account_title_name, title_description, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_full(cls, account_title_uid: str, account_title_name: str, title_description: str, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
        return cls(account_title_uid, account_title_name, title_description, row_instance, row_lock, row_owner, row_seq, row_guid, row_version, is_active, created_date, created_by, last_updated_date, last_updated_by, removed_date, removed_by, custom_attributes)
    @classmethod
    def from_write(cls, dto: account_title_write_dto):
        return cls(0, dto.account_title_uid, dto.account_title_name, dto.title_description, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, dto.custom_attributes)
    def clone_read(self):
        return account_title_read_dto(self.account_title_uid, self.account_title_name, self.title_description, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes)
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["account_title_uid"], d["account_title_name"], d["title_description"], d["row_instance"], d["row_lock"], d["row_owner"], d["row_seq"], d["row_guid"], d["row_version"], d["is_active"], d["created_date"], d["created_by"], d["last_updated_date"], d["last_updated_by"], d["removed_date"], d["removed_by"], d["custom_attributes"])
    def to_read_dict(self) -> dict:
        return asdict(self)
    def to_write(self) -> account_title_write_dto:
        return account_title_write_dto(self.account_title_uid, self.account_title_name, self.title_description, self.custom_attributes)
    def to_thin(self) -> account_title_thin_dto:
        return account_title_thin_dto(self.account_title_uid, self.account_title_name, self.created_date, self.is_active)
    def touch(self, updated_by: str = "system"):
        self.last_updated_date = datetime.datetime.now()
        self.last_updated_by = updated_by
        self.row_version = self.row_version+1
    def get_list_all_values(self) -> list[any]:
        return [self.account_title_uid, self.account_title_name, self.title_description, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]
    def get_list_update_values(self, updated_by: str) -> list[any]:
        return [self.account_title_name, self.title_description, self.custom_attributes, updated_by, self.account_title_uid]
    def is_older_than(self, dt: datetime.datetime) -> bool:
        return self.created_date < dt
    def is_newer_than(self, dt: datetime.datetime) -> bool:
        return self.created_date > dt
    def to_json_read(self) -> str:
        return json.dumps(self.to_read_dict())


@dataclass(frozen=False)
class account_title_assignment_read_dto(base_read_dto, account_title_assignment_write_dto):
    account_title_assignment_uid: str
    account_title_assignment_name: str
    tenant_uid: str
    account_title_uid: str
    account_title_responsibility_uid: str
    responsibility_description: str
    responsibility_priority: int
    row_instance: str
    row_lock: str | None
    row_owner: str
    row_seq: int
    row_guid: str
    row_version: int
    is_active: int
    created_date: datetime.datetime
    created_by: str
    last_updated_date: datetime.datetime
    last_updated_by: str
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str
    def __init__(self, account_title_assignment_uid: str, account_title_assignment_name: str, tenant_uid: str, account_title_uid: str, account_title_responsibility_uid: str, responsibility_description: str, responsibility_priority: int, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
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
    @classmethod
    def empty_read(cls):
        return cls(0, "", "", "", "", "", "", 0, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def default_read(cls):
        return cls(0, base_dto.get_random_uid(), "", "", "", "", "", 0, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def random_read(cls):
        return cls(0, base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), 0, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_default(cls, account_title_assignment_uid: str, account_title_assignment_name: str, tenant_uid: str, account_title_uid: str, account_title_responsibility_uid: str, responsibility_description: str, responsibility_priority: int):
        return cls(0, account_title_assignment_uid, account_title_assignment_name, tenant_uid, account_title_uid, account_title_responsibility_uid, responsibility_description, responsibility_priority, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_full(cls, account_title_assignment_uid: str, account_title_assignment_name: str, tenant_uid: str, account_title_uid: str, account_title_responsibility_uid: str, responsibility_description: str, responsibility_priority: int, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
        return cls(account_title_assignment_uid, account_title_assignment_name, tenant_uid, account_title_uid, account_title_responsibility_uid, responsibility_description, responsibility_priority, row_instance, row_lock, row_owner, row_seq, row_guid, row_version, is_active, created_date, created_by, last_updated_date, last_updated_by, removed_date, removed_by, custom_attributes)
    @classmethod
    def from_write(cls, dto: account_title_assignment_write_dto):
        return cls(0, dto.account_title_assignment_uid, dto.account_title_assignment_name, dto.tenant_uid, dto.account_title_uid, dto.account_title_responsibility_uid, dto.responsibility_description, dto.responsibility_priority, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, dto.custom_attributes)
    def clone_read(self):
        return account_title_assignment_read_dto(self.account_title_assignment_uid, self.account_title_assignment_name, self.tenant_uid, self.account_title_uid, self.account_title_responsibility_uid, self.responsibility_description, self.responsibility_priority, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes)
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["account_title_assignment_uid"], d["account_title_assignment_name"], d["tenant_uid"], d["account_title_uid"], d["account_title_responsibility_uid"], d["responsibility_description"], d["responsibility_priority"], d["row_instance"], d["row_lock"], d["row_owner"], d["row_seq"], d["row_guid"], d["row_version"], d["is_active"], d["created_date"], d["created_by"], d["last_updated_date"], d["last_updated_by"], d["removed_date"], d["removed_by"], d["custom_attributes"])
    def to_read_dict(self) -> dict:
        return asdict(self)
    def to_write(self) -> account_title_assignment_write_dto:
        return account_title_assignment_write_dto(self.account_title_assignment_uid, self.account_title_assignment_name, self.tenant_uid, self.account_title_uid, self.account_title_responsibility_uid, self.responsibility_description, self.responsibility_priority, self.custom_attributes)
    def to_thin(self) -> account_title_assignment_thin_dto:
        return account_title_assignment_thin_dto(self.account_title_assignment_uid, self.account_title_assignment_name, self.created_date, self.is_active)
    def touch(self, updated_by: str = "system"):
        self.last_updated_date = datetime.datetime.now()
        self.last_updated_by = updated_by
        self.row_version = self.row_version+1
    def get_list_all_values(self) -> list[any]:
        return [self.account_title_assignment_uid, self.account_title_assignment_name, self.tenant_uid, self.account_title_uid, self.account_title_responsibility_uid, self.responsibility_description, self.responsibility_priority, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]
    def get_list_update_values(self, updated_by: str) -> list[any]:
        return [self.account_title_assignment_name, self.tenant_uid, self.account_title_uid, self.account_title_responsibility_uid, self.responsibility_description, self.responsibility_priority, self.custom_attributes, updated_by, self.account_title_assignment_uid]
    def is_older_than(self, dt: datetime.datetime) -> bool:
        return self.created_date < dt
    def is_newer_than(self, dt: datetime.datetime) -> bool:
        return self.created_date > dt
    def to_json_read(self) -> str:
        return json.dumps(self.to_read_dict())


@dataclass(frozen=False)
class account_title_responsibility_read_dto(base_read_dto, account_title_responsibility_write_dto):
    account_title_responsibility_uid: str
    account_title_responsibility_name: str
    tenant_uid: str
    account_title_uid: str
    responsibility_group: str
    responsibility_description: str
    responsibility_priority: int
    row_instance: str
    row_lock: str | None
    row_owner: str
    row_seq: int
    row_guid: str
    row_version: int
    is_active: int
    created_date: datetime.datetime
    created_by: str
    last_updated_date: datetime.datetime
    last_updated_by: str
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str
    def __init__(self, account_title_responsibility_uid: str, account_title_responsibility_name: str, tenant_uid: str, account_title_uid: str, responsibility_group: str, responsibility_description: str, responsibility_priority: int, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
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
    @classmethod
    def empty_read(cls):
        return cls(0, "", "", "", "", "", "", 0, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def default_read(cls):
        return cls(0, base_dto.get_random_uid(), "", "", "", "", "", 0, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def random_read(cls):
        return cls(0, base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), 0, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_default(cls, account_title_responsibility_uid: str, account_title_responsibility_name: str, tenant_uid: str, account_title_uid: str, responsibility_group: str, responsibility_description: str, responsibility_priority: int):
        return cls(0, account_title_responsibility_uid, account_title_responsibility_name, tenant_uid, account_title_uid, responsibility_group, responsibility_description, responsibility_priority, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_full(cls, account_title_responsibility_uid: str, account_title_responsibility_name: str, tenant_uid: str, account_title_uid: str, responsibility_group: str, responsibility_description: str, responsibility_priority: int, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
        return cls(account_title_responsibility_uid, account_title_responsibility_name, tenant_uid, account_title_uid, responsibility_group, responsibility_description, responsibility_priority, row_instance, row_lock, row_owner, row_seq, row_guid, row_version, is_active, created_date, created_by, last_updated_date, last_updated_by, removed_date, removed_by, custom_attributes)
    @classmethod
    def from_write(cls, dto: account_title_responsibility_write_dto):
        return cls(0, dto.account_title_responsibility_uid, dto.account_title_responsibility_name, dto.tenant_uid, dto.account_title_uid, dto.responsibility_group, dto.responsibility_description, dto.responsibility_priority, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, dto.custom_attributes)
    def clone_read(self):
        return account_title_responsibility_read_dto(self.account_title_responsibility_uid, self.account_title_responsibility_name, self.tenant_uid, self.account_title_uid, self.responsibility_group, self.responsibility_description, self.responsibility_priority, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes)
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["account_title_responsibility_uid"], d["account_title_responsibility_name"], d["tenant_uid"], d["account_title_uid"], d["responsibility_group"], d["responsibility_description"], d["responsibility_priority"], d["row_instance"], d["row_lock"], d["row_owner"], d["row_seq"], d["row_guid"], d["row_version"], d["is_active"], d["created_date"], d["created_by"], d["last_updated_date"], d["last_updated_by"], d["removed_date"], d["removed_by"], d["custom_attributes"])
    def to_read_dict(self) -> dict:
        return asdict(self)
    def to_write(self) -> account_title_responsibility_write_dto:
        return account_title_responsibility_write_dto(self.account_title_responsibility_uid, self.account_title_responsibility_name, self.tenant_uid, self.account_title_uid, self.responsibility_group, self.responsibility_description, self.responsibility_priority, self.custom_attributes)
    def to_thin(self) -> account_title_responsibility_thin_dto:
        return account_title_responsibility_thin_dto(self.account_title_responsibility_uid, self.account_title_responsibility_name, self.created_date, self.is_active)
    def touch(self, updated_by: str = "system"):
        self.last_updated_date = datetime.datetime.now()
        self.last_updated_by = updated_by
        self.row_version = self.row_version+1
    def get_list_all_values(self) -> list[any]:
        return [self.account_title_responsibility_uid, self.account_title_responsibility_name, self.tenant_uid, self.account_title_uid, self.responsibility_group, self.responsibility_description, self.responsibility_priority, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]
    def get_list_update_values(self, updated_by: str) -> list[any]:
        return [self.account_title_responsibility_name, self.tenant_uid, self.account_title_uid, self.responsibility_group, self.responsibility_description, self.responsibility_priority, self.custom_attributes, updated_by, self.account_title_responsibility_uid]
    def is_older_than(self, dt: datetime.datetime) -> bool:
        return self.created_date < dt
    def is_newer_than(self, dt: datetime.datetime) -> bool:
        return self.created_date > dt
    def to_json_read(self) -> str:
        return json.dumps(self.to_read_dict())


@dataclass(frozen=False)
class account_type_read_dto(base_read_dto, account_type_write_dto):
    account_type_uid: str
    account_type_name: str
    class_name: str
    account_type_description: str
    row_instance: str
    row_lock: str | None
    row_owner: str
    row_seq: int
    row_guid: str
    row_version: int
    is_active: int
    created_date: datetime.datetime
    created_by: str
    last_updated_date: datetime.datetime
    last_updated_by: str
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str
    def __init__(self, account_type_uid: str, account_type_name: str, class_name: str, account_type_description: str, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
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
    @classmethod
    def empty_read(cls):
        return cls(0, "", "", "", "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def default_read(cls):
        return cls(0, base_dto.get_random_uid(), "", "", "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def random_read(cls):
        return cls(0, base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_default(cls, account_type_uid: str, account_type_name: str, class_name: str, account_type_description: str):
        return cls(0, account_type_uid, account_type_name, class_name, account_type_description, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_full(cls, account_type_uid: str, account_type_name: str, class_name: str, account_type_description: str, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
        return cls(account_type_uid, account_type_name, class_name, account_type_description, row_instance, row_lock, row_owner, row_seq, row_guid, row_version, is_active, created_date, created_by, last_updated_date, last_updated_by, removed_date, removed_by, custom_attributes)
    @classmethod
    def from_write(cls, dto: account_type_write_dto):
        return cls(0, dto.account_type_uid, dto.account_type_name, dto.class_name, dto.account_type_description, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, dto.custom_attributes)
    def clone_read(self):
        return account_type_read_dto(self.account_type_uid, self.account_type_name, self.class_name, self.account_type_description, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes)
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["account_type_uid"], d["account_type_name"], d["class_name"], d["account_type_description"], d["row_instance"], d["row_lock"], d["row_owner"], d["row_seq"], d["row_guid"], d["row_version"], d["is_active"], d["created_date"], d["created_by"], d["last_updated_date"], d["last_updated_by"], d["removed_date"], d["removed_by"], d["custom_attributes"])
    def to_read_dict(self) -> dict:
        return asdict(self)
    def to_write(self) -> account_type_write_dto:
        return account_type_write_dto(self.account_type_uid, self.account_type_name, self.class_name, self.account_type_description, self.custom_attributes)
    def to_thin(self) -> account_type_thin_dto:
        return account_type_thin_dto(self.account_type_uid, self.account_type_name, self.created_date, self.is_active)
    def touch(self, updated_by: str = "system"):
        self.last_updated_date = datetime.datetime.now()
        self.last_updated_by = updated_by
        self.row_version = self.row_version+1
    def get_list_all_values(self) -> list[any]:
        return [self.account_type_uid, self.account_type_name, self.class_name, self.account_type_description, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]
    def get_list_update_values(self, updated_by: str) -> list[any]:
        return [self.account_type_name, self.class_name, self.account_type_description, self.custom_attributes, updated_by, self.account_type_uid]
    def is_older_than(self, dt: datetime.datetime) -> bool:
        return self.created_date < dt
    def is_newer_than(self, dt: datetime.datetime) -> bool:
        return self.created_date > dt
    def to_json_read(self) -> str:
        return json.dumps(self.to_read_dict())


@dataclass(frozen=False)
class audit_change_read_dto(base_read_dto, audit_change_write_dto):
    audit_change_uid: str
    audit_change_name: str
    account_uid: str
    audit_type_uid: str
    change_type: str
    change_json: str
    row_instance: str
    row_lock: str | None
    row_owner: str
    row_seq: int
    row_guid: str
    row_version: int
    is_active: int
    created_date: datetime.datetime
    created_by: str
    last_updated_date: datetime.datetime
    last_updated_by: str
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str
    def __init__(self, audit_change_uid: str, audit_change_name: str, account_uid: str, audit_type_uid: str, change_type: str, change_json: str, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
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
    @classmethod
    def empty_read(cls):
        return cls(0, "", "", "", "", "", "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def default_read(cls):
        return cls(0, base_dto.get_random_uid(), "", "", "", "", "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def random_read(cls):
        return cls(0, base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_default(cls, audit_change_uid: str, audit_change_name: str, account_uid: str, audit_type_uid: str, change_type: str, change_json: str):
        return cls(0, audit_change_uid, audit_change_name, account_uid, audit_type_uid, change_type, change_json, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_full(cls, audit_change_uid: str, audit_change_name: str, account_uid: str, audit_type_uid: str, change_type: str, change_json: str, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
        return cls(audit_change_uid, audit_change_name, account_uid, audit_type_uid, change_type, change_json, row_instance, row_lock, row_owner, row_seq, row_guid, row_version, is_active, created_date, created_by, last_updated_date, last_updated_by, removed_date, removed_by, custom_attributes)
    @classmethod
    def from_write(cls, dto: audit_change_write_dto):
        return cls(0, dto.audit_change_uid, dto.audit_change_name, dto.account_uid, dto.audit_type_uid, dto.change_type, dto.change_json, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, dto.custom_attributes)
    def clone_read(self):
        return audit_change_read_dto(self.audit_change_uid, self.audit_change_name, self.account_uid, self.audit_type_uid, self.change_type, self.change_json, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes)
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["audit_change_uid"], d["audit_change_name"], d["account_uid"], d["audit_type_uid"], d["change_type"], d["change_json"], d["row_instance"], d["row_lock"], d["row_owner"], d["row_seq"], d["row_guid"], d["row_version"], d["is_active"], d["created_date"], d["created_by"], d["last_updated_date"], d["last_updated_by"], d["removed_date"], d["removed_by"], d["custom_attributes"])
    def to_read_dict(self) -> dict:
        return asdict(self)
    def to_write(self) -> audit_change_write_dto:
        return audit_change_write_dto(self.audit_change_uid, self.audit_change_name, self.account_uid, self.audit_type_uid, self.change_type, self.change_json, self.custom_attributes)
    def to_thin(self) -> audit_change_thin_dto:
        return audit_change_thin_dto(self.audit_change_uid, self.audit_change_name, self.created_date, self.is_active)
    def touch(self, updated_by: str = "system"):
        self.last_updated_date = datetime.datetime.now()
        self.last_updated_by = updated_by
        self.row_version = self.row_version+1
    def get_list_all_values(self) -> list[any]:
        return [self.audit_change_uid, self.audit_change_name, self.account_uid, self.audit_type_uid, self.change_type, self.change_json, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]
    def get_list_update_values(self, updated_by: str) -> list[any]:
        return [self.audit_change_name, self.account_uid, self.audit_type_uid, self.change_type, self.change_json, self.custom_attributes, updated_by, self.audit_change_uid]
    def is_older_than(self, dt: datetime.datetime) -> bool:
        return self.created_date < dt
    def is_newer_than(self, dt: datetime.datetime) -> bool:
        return self.created_date > dt
    def to_json_read(self) -> str:
        return json.dumps(self.to_read_dict())


@dataclass(frozen=False)
class audit_type_read_dto(base_read_dto, audit_type_write_dto):
    audit_type_uid: str
    audit_type_name: str
    row_instance: str
    row_lock: str | None
    row_owner: str
    row_seq: int
    row_guid: str
    row_version: int
    is_active: int
    created_date: datetime.datetime
    created_by: str
    last_updated_date: datetime.datetime
    last_updated_by: str
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str
    def __init__(self, audit_type_uid: str, audit_type_name: str, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
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
    @classmethod
    def empty_read(cls):
        return cls(0, "", "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def default_read(cls):
        return cls(0, base_dto.get_random_uid(), "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def random_read(cls):
        return cls(0, base_dto.get_random_uid(), base_dto.get_random_uid(), "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_default(cls, audit_type_uid: str, audit_type_name: str):
        return cls(0, audit_type_uid, audit_type_name, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_full(cls, audit_type_uid: str, audit_type_name: str, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
        return cls(audit_type_uid, audit_type_name, row_instance, row_lock, row_owner, row_seq, row_guid, row_version, is_active, created_date, created_by, last_updated_date, last_updated_by, removed_date, removed_by, custom_attributes)
    @classmethod
    def from_write(cls, dto: audit_type_write_dto):
        return cls(0, dto.audit_type_uid, dto.audit_type_name, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, dto.custom_attributes)
    def clone_read(self):
        return audit_type_read_dto(self.audit_type_uid, self.audit_type_name, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes)
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["audit_type_uid"], d["audit_type_name"], d["row_instance"], d["row_lock"], d["row_owner"], d["row_seq"], d["row_guid"], d["row_version"], d["is_active"], d["created_date"], d["created_by"], d["last_updated_date"], d["last_updated_by"], d["removed_date"], d["removed_by"], d["custom_attributes"])
    def to_read_dict(self) -> dict:
        return asdict(self)
    def to_write(self) -> audit_type_write_dto:
        return audit_type_write_dto(self.audit_type_uid, self.audit_type_name, self.custom_attributes)
    def to_thin(self) -> audit_type_thin_dto:
        return audit_type_thin_dto(self.audit_type_uid, self.audit_type_name, self.created_date, self.is_active)
    def touch(self, updated_by: str = "system"):
        self.last_updated_date = datetime.datetime.now()
        self.last_updated_by = updated_by
        self.row_version = self.row_version+1
    def get_list_all_values(self) -> list[any]:
        return [self.audit_type_uid, self.audit_type_name, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]
    def get_list_update_values(self, updated_by: str) -> list[any]:
        return [self.audit_type_name, self.custom_attributes, updated_by, self.audit_type_uid]
    def is_older_than(self, dt: datetime.datetime) -> bool:
        return self.created_date < dt
    def is_newer_than(self, dt: datetime.datetime) -> bool:
        return self.created_date > dt
    def to_json_read(self) -> str:
        return json.dumps(self.to_read_dict())


@dataclass(frozen=False)
class auth_attempt_read_dto(base_read_dto, auth_attempt_write_dto):
    auth_attempt_uid: str
    auth_attempt_name: str
    tenant_uid: str | None
    account_uid: str | None
    account_login: str
    identity_type: str
    identity_parameters: str
    last_status_name: str
    row_instance: str
    row_lock: str | None
    row_owner: str
    row_seq: int
    row_guid: str
    row_version: int
    is_active: int
    created_date: datetime.datetime
    created_by: str
    last_updated_date: datetime.datetime
    last_updated_by: str
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str
    def __init__(self, auth_attempt_uid: str, auth_attempt_name: str, tenant_uid: str | None, account_uid: str | None, account_login: str, identity_type: str, identity_parameters: str, last_status_name: str, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
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
    @classmethod
    def empty_read(cls):
        return cls(0, "", "", "", "", "", "", "", "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def default_read(cls):
        return cls(0, base_dto.get_random_uid(), "", "", "", "", "", "", "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def random_read(cls):
        return cls(0, base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_default(cls, auth_attempt_uid: str, auth_attempt_name: str, tenant_uid: str | None, account_uid: str | None, account_login: str, identity_type: str, identity_parameters: str, last_status_name: str):
        return cls(0, auth_attempt_uid, auth_attempt_name, tenant_uid, account_uid, account_login, identity_type, identity_parameters, last_status_name, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_full(cls, auth_attempt_uid: str, auth_attempt_name: str, tenant_uid: str | None, account_uid: str | None, account_login: str, identity_type: str, identity_parameters: str, last_status_name: str, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
        return cls(auth_attempt_uid, auth_attempt_name, tenant_uid, account_uid, account_login, identity_type, identity_parameters, last_status_name, row_instance, row_lock, row_owner, row_seq, row_guid, row_version, is_active, created_date, created_by, last_updated_date, last_updated_by, removed_date, removed_by, custom_attributes)
    @classmethod
    def from_write(cls, dto: auth_attempt_write_dto):
        return cls(0, dto.auth_attempt_uid, dto.auth_attempt_name, dto.tenant_uid, dto.account_uid, dto.account_login, dto.identity_type, dto.identity_parameters, dto.last_status_name, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, dto.custom_attributes)
    def clone_read(self):
        return auth_attempt_read_dto(self.auth_attempt_uid, self.auth_attempt_name, self.tenant_uid, self.account_uid, self.account_login, self.identity_type, self.identity_parameters, self.last_status_name, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes)
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["auth_attempt_uid"], d["auth_attempt_name"], d["tenant_uid"], d["account_uid"], d["account_login"], d["identity_type"], d["identity_parameters"], d["last_status_name"], d["row_instance"], d["row_lock"], d["row_owner"], d["row_seq"], d["row_guid"], d["row_version"], d["is_active"], d["created_date"], d["created_by"], d["last_updated_date"], d["last_updated_by"], d["removed_date"], d["removed_by"], d["custom_attributes"])
    def to_read_dict(self) -> dict:
        return asdict(self)
    def to_write(self) -> auth_attempt_write_dto:
        return auth_attempt_write_dto(self.auth_attempt_uid, self.auth_attempt_name, self.tenant_uid, self.account_uid, self.account_login, self.identity_type, self.identity_parameters, self.last_status_name, self.custom_attributes)
    def to_thin(self) -> auth_attempt_thin_dto:
        return auth_attempt_thin_dto(self.auth_attempt_uid, self.auth_attempt_name, self.created_date, self.is_active)
    def touch(self, updated_by: str = "system"):
        self.last_updated_date = datetime.datetime.now()
        self.last_updated_by = updated_by
        self.row_version = self.row_version+1
    def get_list_all_values(self) -> list[any]:
        return [self.auth_attempt_uid, self.auth_attempt_name, self.tenant_uid, self.account_uid, self.account_login, self.identity_type, self.identity_parameters, self.last_status_name, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]
    def get_list_update_values(self, updated_by: str) -> list[any]:
        return [self.auth_attempt_name, self.tenant_uid, self.account_uid, self.account_login, self.identity_type, self.identity_parameters, self.last_status_name, self.custom_attributes, updated_by, self.auth_attempt_uid]
    def is_older_than(self, dt: datetime.datetime) -> bool:
        return self.created_date < dt
    def is_newer_than(self, dt: datetime.datetime) -> bool:
        return self.created_date > dt
    def to_json_read(self) -> str:
        return json.dumps(self.to_read_dict())


@dataclass(frozen=False)
class auth_identity_read_dto(base_read_dto, auth_identity_write_dto):
    auth_identity_uid: str
    auth_identity_name: str
    class_name: str
    default_parameters_json: str
    row_instance: str
    row_lock: str | None
    row_owner: str
    row_seq: int
    row_guid: str
    row_version: int
    is_active: int
    created_date: datetime.datetime
    created_by: str
    last_updated_date: datetime.datetime
    last_updated_by: str
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str
    def __init__(self, auth_identity_uid: str, auth_identity_name: str, class_name: str, default_parameters_json: str, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
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
    @classmethod
    def empty_read(cls):
        return cls(0, "", "", "", "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def default_read(cls):
        return cls(0, base_dto.get_random_uid(), "", "", "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def random_read(cls):
        return cls(0, base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_default(cls, auth_identity_uid: str, auth_identity_name: str, class_name: str, default_parameters_json: str):
        return cls(0, auth_identity_uid, auth_identity_name, class_name, default_parameters_json, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_full(cls, auth_identity_uid: str, auth_identity_name: str, class_name: str, default_parameters_json: str, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
        return cls(auth_identity_uid, auth_identity_name, class_name, default_parameters_json, row_instance, row_lock, row_owner, row_seq, row_guid, row_version, is_active, created_date, created_by, last_updated_date, last_updated_by, removed_date, removed_by, custom_attributes)
    @classmethod
    def from_write(cls, dto: auth_identity_write_dto):
        return cls(0, dto.auth_identity_uid, dto.auth_identity_name, dto.class_name, dto.default_parameters_json, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, dto.custom_attributes)
    def clone_read(self):
        return auth_identity_read_dto(self.auth_identity_uid, self.auth_identity_name, self.class_name, self.default_parameters_json, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes)
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["auth_identity_uid"], d["auth_identity_name"], d["class_name"], d["default_parameters_json"], d["row_instance"], d["row_lock"], d["row_owner"], d["row_seq"], d["row_guid"], d["row_version"], d["is_active"], d["created_date"], d["created_by"], d["last_updated_date"], d["last_updated_by"], d["removed_date"], d["removed_by"], d["custom_attributes"])
    def to_read_dict(self) -> dict:
        return asdict(self)
    def to_write(self) -> auth_identity_write_dto:
        return auth_identity_write_dto(self.auth_identity_uid, self.auth_identity_name, self.class_name, self.default_parameters_json, self.custom_attributes)
    def to_thin(self) -> auth_identity_thin_dto:
        return auth_identity_thin_dto(self.auth_identity_uid, self.auth_identity_name, self.created_date, self.is_active)
    def touch(self, updated_by: str = "system"):
        self.last_updated_date = datetime.datetime.now()
        self.last_updated_by = updated_by
        self.row_version = self.row_version+1
    def get_list_all_values(self) -> list[any]:
        return [self.auth_identity_uid, self.auth_identity_name, self.class_name, self.default_parameters_json, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]
    def get_list_update_values(self, updated_by: str) -> list[any]:
        return [self.auth_identity_name, self.class_name, self.default_parameters_json, self.custom_attributes, updated_by, self.auth_identity_uid]
    def is_older_than(self, dt: datetime.datetime) -> bool:
        return self.created_date < dt
    def is_newer_than(self, dt: datetime.datetime) -> bool:
        return self.created_date > dt
    def to_json_read(self) -> str:
        return json.dumps(self.to_read_dict())


@dataclass(frozen=False)
class auth_identity_tenant_read_dto(base_read_dto, auth_identity_tenant_write_dto):
    auth_identity_tenant_uid: str
    auth_identity_tenant_name: str
    tenant_uid: str
    auth_identity_uid: str
    auth_sso_uid: str | None
    identity_parameters_json: str
    last_status_name: str
    row_instance: str
    row_lock: str | None
    row_owner: str
    row_seq: int
    row_guid: str
    row_version: int
    is_active: int
    created_date: datetime.datetime
    created_by: str
    last_updated_date: datetime.datetime
    last_updated_by: str
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str
    def __init__(self, auth_identity_tenant_uid: str, auth_identity_tenant_name: str, tenant_uid: str, auth_identity_uid: str, auth_sso_uid: str | None, identity_parameters_json: str, last_status_name: str, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
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
    @classmethod
    def empty_read(cls):
        return cls(0, "", "", "", "", "", "", "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def default_read(cls):
        return cls(0, base_dto.get_random_uid(), "", "", "", "", "", "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def random_read(cls):
        return cls(0, base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_default(cls, auth_identity_tenant_uid: str, auth_identity_tenant_name: str, tenant_uid: str, auth_identity_uid: str, auth_sso_uid: str | None, identity_parameters_json: str, last_status_name: str):
        return cls(0, auth_identity_tenant_uid, auth_identity_tenant_name, tenant_uid, auth_identity_uid, auth_sso_uid, identity_parameters_json, last_status_name, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_full(cls, auth_identity_tenant_uid: str, auth_identity_tenant_name: str, tenant_uid: str, auth_identity_uid: str, auth_sso_uid: str | None, identity_parameters_json: str, last_status_name: str, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
        return cls(auth_identity_tenant_uid, auth_identity_tenant_name, tenant_uid, auth_identity_uid, auth_sso_uid, identity_parameters_json, last_status_name, row_instance, row_lock, row_owner, row_seq, row_guid, row_version, is_active, created_date, created_by, last_updated_date, last_updated_by, removed_date, removed_by, custom_attributes)
    @classmethod
    def from_write(cls, dto: auth_identity_tenant_write_dto):
        return cls(0, dto.auth_identity_tenant_uid, dto.auth_identity_tenant_name, dto.tenant_uid, dto.auth_identity_uid, dto.auth_sso_uid, dto.identity_parameters_json, dto.last_status_name, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, dto.custom_attributes)
    def clone_read(self):
        return auth_identity_tenant_read_dto(self.auth_identity_tenant_uid, self.auth_identity_tenant_name, self.tenant_uid, self.auth_identity_uid, self.auth_sso_uid, self.identity_parameters_json, self.last_status_name, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes)
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["auth_identity_tenant_uid"], d["auth_identity_tenant_name"], d["tenant_uid"], d["auth_identity_uid"], d["auth_sso_uid"], d["identity_parameters_json"], d["last_status_name"], d["row_instance"], d["row_lock"], d["row_owner"], d["row_seq"], d["row_guid"], d["row_version"], d["is_active"], d["created_date"], d["created_by"], d["last_updated_date"], d["last_updated_by"], d["removed_date"], d["removed_by"], d["custom_attributes"])
    def to_read_dict(self) -> dict:
        return asdict(self)
    def to_write(self) -> auth_identity_tenant_write_dto:
        return auth_identity_tenant_write_dto(self.auth_identity_tenant_uid, self.auth_identity_tenant_name, self.tenant_uid, self.auth_identity_uid, self.auth_sso_uid, self.identity_parameters_json, self.last_status_name, self.custom_attributes)
    def to_thin(self) -> auth_identity_tenant_thin_dto:
        return auth_identity_tenant_thin_dto(self.auth_identity_tenant_uid, self.auth_identity_tenant_name, self.created_date, self.is_active)
    def touch(self, updated_by: str = "system"):
        self.last_updated_date = datetime.datetime.now()
        self.last_updated_by = updated_by
        self.row_version = self.row_version+1
    def get_list_all_values(self) -> list[any]:
        return [self.auth_identity_tenant_uid, self.auth_identity_tenant_name, self.tenant_uid, self.auth_identity_uid, self.auth_sso_uid, self.identity_parameters_json, self.last_status_name, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]
    def get_list_update_values(self, updated_by: str) -> list[any]:
        return [self.auth_identity_tenant_name, self.tenant_uid, self.auth_identity_uid, self.auth_sso_uid, self.identity_parameters_json, self.last_status_name, self.custom_attributes, updated_by, self.auth_identity_tenant_uid]
    def is_older_than(self, dt: datetime.datetime) -> bool:
        return self.created_date < dt
    def is_newer_than(self, dt: datetime.datetime) -> bool:
        return self.created_date > dt
    def to_json_read(self) -> str:
        return json.dumps(self.to_read_dict())


@dataclass(frozen=False)
class auth_key_read_dto(base_read_dto, auth_key_write_dto):
    auth_key_uid: str
    auth_key_name: str
    tenant_uid: str
    owner_account_uid: str | None
    auth_key_type_uid: str
    key_private: str
    key_public: str
    key_length: int
    key_exponent: str
    key_modulus: str
    key_parameters_json: str
    row_instance: str
    row_lock: str | None
    row_owner: str
    row_seq: int
    row_guid: str
    row_version: int
    is_active: int
    created_date: datetime.datetime
    created_by: str
    last_updated_date: datetime.datetime
    last_updated_by: str
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str
    def __init__(self, auth_key_uid: str, auth_key_name: str, tenant_uid: str, owner_account_uid: str | None, auth_key_type_uid: str, key_private: str, key_public: str, key_length: int, key_exponent: str, key_modulus: str, key_parameters_json: str, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
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
    @classmethod
    def empty_read(cls):
        return cls(0, "", "", "", "", "", "", "", 0, "", "", "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def default_read(cls):
        return cls(0, base_dto.get_random_uid(), "", "", "", "", "", "", 0, "", "", "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def random_read(cls):
        return cls(0, base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), 0, base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_default(cls, auth_key_uid: str, auth_key_name: str, tenant_uid: str, owner_account_uid: str | None, auth_key_type_uid: str, key_private: str, key_public: str, key_length: int, key_exponent: str, key_modulus: str, key_parameters_json: str):
        return cls(0, auth_key_uid, auth_key_name, tenant_uid, owner_account_uid, auth_key_type_uid, key_private, key_public, key_length, key_exponent, key_modulus, key_parameters_json, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_full(cls, auth_key_uid: str, auth_key_name: str, tenant_uid: str, owner_account_uid: str | None, auth_key_type_uid: str, key_private: str, key_public: str, key_length: int, key_exponent: str, key_modulus: str, key_parameters_json: str, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
        return cls(auth_key_uid, auth_key_name, tenant_uid, owner_account_uid, auth_key_type_uid, key_private, key_public, key_length, key_exponent, key_modulus, key_parameters_json, row_instance, row_lock, row_owner, row_seq, row_guid, row_version, is_active, created_date, created_by, last_updated_date, last_updated_by, removed_date, removed_by, custom_attributes)
    @classmethod
    def from_write(cls, dto: auth_key_write_dto):
        return cls(0, dto.auth_key_uid, dto.auth_key_name, dto.tenant_uid, dto.owner_account_uid, dto.auth_key_type_uid, dto.key_private, dto.key_public, dto.key_length, dto.key_exponent, dto.key_modulus, dto.key_parameters_json, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, dto.custom_attributes)
    def clone_read(self):
        return auth_key_read_dto(self.auth_key_uid, self.auth_key_name, self.tenant_uid, self.owner_account_uid, self.auth_key_type_uid, self.key_private, self.key_public, self.key_length, self.key_exponent, self.key_modulus, self.key_parameters_json, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes)
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["auth_key_uid"], d["auth_key_name"], d["tenant_uid"], d["owner_account_uid"], d["auth_key_type_uid"], d["key_private"], d["key_public"], d["key_length"], d["key_exponent"], d["key_modulus"], d["key_parameters_json"], d["row_instance"], d["row_lock"], d["row_owner"], d["row_seq"], d["row_guid"], d["row_version"], d["is_active"], d["created_date"], d["created_by"], d["last_updated_date"], d["last_updated_by"], d["removed_date"], d["removed_by"], d["custom_attributes"])
    def to_read_dict(self) -> dict:
        return asdict(self)
    def to_write(self) -> auth_key_write_dto:
        return auth_key_write_dto(self.auth_key_uid, self.auth_key_name, self.tenant_uid, self.owner_account_uid, self.auth_key_type_uid, self.key_private, self.key_public, self.key_length, self.key_exponent, self.key_modulus, self.key_parameters_json, self.custom_attributes)
    def to_thin(self) -> auth_key_thin_dto:
        return auth_key_thin_dto(self.auth_key_uid, self.auth_key_name, self.created_date, self.is_active)
    def touch(self, updated_by: str = "system"):
        self.last_updated_date = datetime.datetime.now()
        self.last_updated_by = updated_by
        self.row_version = self.row_version+1
    def get_list_all_values(self) -> list[any]:
        return [self.auth_key_uid, self.auth_key_name, self.tenant_uid, self.owner_account_uid, self.auth_key_type_uid, self.key_private, self.key_public, self.key_length, self.key_exponent, self.key_modulus, self.key_parameters_json, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]
    def get_list_update_values(self, updated_by: str) -> list[any]:
        return [self.auth_key_name, self.tenant_uid, self.owner_account_uid, self.auth_key_type_uid, self.key_private, self.key_public, self.key_length, self.key_exponent, self.key_modulus, self.key_parameters_json, self.custom_attributes, updated_by, self.auth_key_uid]
    def is_older_than(self, dt: datetime.datetime) -> bool:
        return self.created_date < dt
    def is_newer_than(self, dt: datetime.datetime) -> bool:
        return self.created_date > dt
    def to_json_read(self) -> str:
        return json.dumps(self.to_read_dict())


@dataclass(frozen=False)
class auth_key_type_read_dto(base_read_dto, auth_key_type_write_dto):
    auth_key_type_uid: str
    auth_key_type_name: str
    class_name: str
    row_instance: str
    row_lock: str | None
    row_owner: str
    row_seq: int
    row_guid: str
    row_version: int
    is_active: int
    created_date: datetime.datetime
    created_by: str
    last_updated_date: datetime.datetime
    last_updated_by: str
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str
    def __init__(self, auth_key_type_uid: str, auth_key_type_name: str, class_name: str, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
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
    @classmethod
    def empty_read(cls):
        return cls(0, "", "", "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def default_read(cls):
        return cls(0, base_dto.get_random_uid(), "", "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def random_read(cls):
        return cls(0, base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_default(cls, auth_key_type_uid: str, auth_key_type_name: str, class_name: str):
        return cls(0, auth_key_type_uid, auth_key_type_name, class_name, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_full(cls, auth_key_type_uid: str, auth_key_type_name: str, class_name: str, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
        return cls(auth_key_type_uid, auth_key_type_name, class_name, row_instance, row_lock, row_owner, row_seq, row_guid, row_version, is_active, created_date, created_by, last_updated_date, last_updated_by, removed_date, removed_by, custom_attributes)
    @classmethod
    def from_write(cls, dto: auth_key_type_write_dto):
        return cls(0, dto.auth_key_type_uid, dto.auth_key_type_name, dto.class_name, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, dto.custom_attributes)
    def clone_read(self):
        return auth_key_type_read_dto(self.auth_key_type_uid, self.auth_key_type_name, self.class_name, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes)
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["auth_key_type_uid"], d["auth_key_type_name"], d["class_name"], d["row_instance"], d["row_lock"], d["row_owner"], d["row_seq"], d["row_guid"], d["row_version"], d["is_active"], d["created_date"], d["created_by"], d["last_updated_date"], d["last_updated_by"], d["removed_date"], d["removed_by"], d["custom_attributes"])
    def to_read_dict(self) -> dict:
        return asdict(self)
    def to_write(self) -> auth_key_type_write_dto:
        return auth_key_type_write_dto(self.auth_key_type_uid, self.auth_key_type_name, self.class_name, self.custom_attributes)
    def to_thin(self) -> auth_key_type_thin_dto:
        return auth_key_type_thin_dto(self.auth_key_type_uid, self.auth_key_type_name, self.created_date, self.is_active)
    def touch(self, updated_by: str = "system"):
        self.last_updated_date = datetime.datetime.now()
        self.last_updated_by = updated_by
        self.row_version = self.row_version+1
    def get_list_all_values(self) -> list[any]:
        return [self.auth_key_type_uid, self.auth_key_type_name, self.class_name, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]
    def get_list_update_values(self, updated_by: str) -> list[any]:
        return [self.auth_key_type_name, self.class_name, self.custom_attributes, updated_by, self.auth_key_type_uid]
    def is_older_than(self, dt: datetime.datetime) -> bool:
        return self.created_date < dt
    def is_newer_than(self, dt: datetime.datetime) -> bool:
        return self.created_date > dt
    def to_json_read(self) -> str:
        return json.dumps(self.to_read_dict())


@dataclass(frozen=False)
class auth_password_read_dto(base_read_dto, auth_password_write_dto):
    auth_password_uid: str
    auth_password_name: str
    tenant_uid: str
    account_uid: str
    password_hash: str
    password_salt: str
    date_from: datetime.datetime
    date_to: datetime.datetime
    usage_count: int
    row_instance: str
    row_lock: str | None
    row_owner: str
    row_seq: int
    row_guid: str
    row_version: int
    is_active: int
    created_date: datetime.datetime
    created_by: str
    last_updated_date: datetime.datetime
    last_updated_by: str
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str
    def __init__(self, auth_password_uid: str, auth_password_name: str, tenant_uid: str, account_uid: str, password_hash: str, password_salt: str, date_from: datetime.datetime, date_to: datetime.datetime, usage_count: int, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
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
    @classmethod
    def empty_read(cls):
        return cls(0, "", "", "", "", "", "", datetime.datetime.now(), datetime.datetime.now(), 0, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def default_read(cls):
        return cls(0, base_dto.get_random_uid(), "", "", "", "", "", datetime.datetime.now(), datetime.datetime.now(), 0, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def random_read(cls):
        return cls(0, base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), datetime.datetime.now(), datetime.datetime.now(), 0, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_default(cls, auth_password_uid: str, auth_password_name: str, tenant_uid: str, account_uid: str, password_hash: str, password_salt: str, date_from: datetime.datetime, date_to: datetime.datetime, usage_count: int):
        return cls(0, auth_password_uid, auth_password_name, tenant_uid, account_uid, password_hash, password_salt, date_from, date_to, usage_count, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_full(cls, auth_password_uid: str, auth_password_name: str, tenant_uid: str, account_uid: str, password_hash: str, password_salt: str, date_from: datetime.datetime, date_to: datetime.datetime, usage_count: int, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
        return cls(auth_password_uid, auth_password_name, tenant_uid, account_uid, password_hash, password_salt, date_from, date_to, usage_count, row_instance, row_lock, row_owner, row_seq, row_guid, row_version, is_active, created_date, created_by, last_updated_date, last_updated_by, removed_date, removed_by, custom_attributes)
    @classmethod
    def from_write(cls, dto: auth_password_write_dto):
        return cls(0, dto.auth_password_uid, dto.auth_password_name, dto.tenant_uid, dto.account_uid, dto.password_hash, dto.password_salt, dto.date_from, dto.date_to, dto.usage_count, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, dto.custom_attributes)
    def clone_read(self):
        return auth_password_read_dto(self.auth_password_uid, self.auth_password_name, self.tenant_uid, self.account_uid, self.password_hash, self.password_salt, self.date_from, self.date_to, self.usage_count, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes)
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["auth_password_uid"], d["auth_password_name"], d["tenant_uid"], d["account_uid"], d["password_hash"], d["password_salt"], d["date_from"], d["date_to"], d["usage_count"], d["row_instance"], d["row_lock"], d["row_owner"], d["row_seq"], d["row_guid"], d["row_version"], d["is_active"], d["created_date"], d["created_by"], d["last_updated_date"], d["last_updated_by"], d["removed_date"], d["removed_by"], d["custom_attributes"])
    def to_read_dict(self) -> dict:
        return asdict(self)
    def to_write(self) -> auth_password_write_dto:
        return auth_password_write_dto(self.auth_password_uid, self.auth_password_name, self.tenant_uid, self.account_uid, self.password_hash, self.password_salt, self.date_from, self.date_to, self.usage_count, self.custom_attributes)
    def to_thin(self) -> auth_password_thin_dto:
        return auth_password_thin_dto(self.auth_password_uid, self.auth_password_name, self.created_date, self.is_active)
    def touch(self, updated_by: str = "system"):
        self.last_updated_date = datetime.datetime.now()
        self.last_updated_by = updated_by
        self.row_version = self.row_version+1
    def get_list_all_values(self) -> list[any]:
        return [self.auth_password_uid, self.auth_password_name, self.tenant_uid, self.account_uid, self.password_hash, self.password_salt, self.date_from, self.date_to, self.usage_count, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]
    def get_list_update_values(self, updated_by: str) -> list[any]:
        return [self.auth_password_name, self.tenant_uid, self.account_uid, self.password_hash, self.password_salt, self.date_from, self.date_to, self.usage_count, self.custom_attributes, updated_by, self.auth_password_uid]
    def is_older_than(self, dt: datetime.datetime) -> bool:
        return self.created_date < dt
    def is_newer_than(self, dt: datetime.datetime) -> bool:
        return self.created_date > dt
    def to_json_read(self) -> str:
        return json.dumps(self.to_read_dict())


@dataclass(frozen=False)
class auth_password_current_read_dto(base_read_dto, auth_password_current_write_dto):
    auth_password_current_uid: str
    auth_password_current_name: str
    tenant_uid: str
    account_uid: str
    password_hash: str
    password_salt: str
    date_from: datetime.datetime
    date_to: datetime.datetime
    usage_count: int
    row_instance: str
    row_lock: str | None
    row_owner: str
    row_seq: int
    row_guid: str
    row_version: int
    is_active: int
    created_date: datetime.datetime
    created_by: str
    last_updated_date: datetime.datetime
    last_updated_by: str
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str
    def __init__(self, auth_password_current_uid: str, auth_password_current_name: str, tenant_uid: str, account_uid: str, password_hash: str, password_salt: str, date_from: datetime.datetime, date_to: datetime.datetime, usage_count: int, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
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
    @classmethod
    def empty_read(cls):
        return cls(0, "", "", "", "", "", "", datetime.datetime.now(), datetime.datetime.now(), 0, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def default_read(cls):
        return cls(0, base_dto.get_random_uid(), "", "", "", "", "", datetime.datetime.now(), datetime.datetime.now(), 0, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def random_read(cls):
        return cls(0, base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), datetime.datetime.now(), datetime.datetime.now(), 0, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_default(cls, auth_password_current_uid: str, auth_password_current_name: str, tenant_uid: str, account_uid: str, password_hash: str, password_salt: str, date_from: datetime.datetime, date_to: datetime.datetime, usage_count: int):
        return cls(0, auth_password_current_uid, auth_password_current_name, tenant_uid, account_uid, password_hash, password_salt, date_from, date_to, usage_count, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_full(cls, auth_password_current_uid: str, auth_password_current_name: str, tenant_uid: str, account_uid: str, password_hash: str, password_salt: str, date_from: datetime.datetime, date_to: datetime.datetime, usage_count: int, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
        return cls(auth_password_current_uid, auth_password_current_name, tenant_uid, account_uid, password_hash, password_salt, date_from, date_to, usage_count, row_instance, row_lock, row_owner, row_seq, row_guid, row_version, is_active, created_date, created_by, last_updated_date, last_updated_by, removed_date, removed_by, custom_attributes)
    @classmethod
    def from_write(cls, dto: auth_password_current_write_dto):
        return cls(0, dto.auth_password_current_uid, dto.auth_password_current_name, dto.tenant_uid, dto.account_uid, dto.password_hash, dto.password_salt, dto.date_from, dto.date_to, dto.usage_count, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, dto.custom_attributes)
    def clone_read(self):
        return auth_password_current_read_dto(self.auth_password_current_uid, self.auth_password_current_name, self.tenant_uid, self.account_uid, self.password_hash, self.password_salt, self.date_from, self.date_to, self.usage_count, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes)
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["auth_password_current_uid"], d["auth_password_current_name"], d["tenant_uid"], d["account_uid"], d["password_hash"], d["password_salt"], d["date_from"], d["date_to"], d["usage_count"], d["row_instance"], d["row_lock"], d["row_owner"], d["row_seq"], d["row_guid"], d["row_version"], d["is_active"], d["created_date"], d["created_by"], d["last_updated_date"], d["last_updated_by"], d["removed_date"], d["removed_by"], d["custom_attributes"])
    def to_read_dict(self) -> dict:
        return asdict(self)
    def to_write(self) -> auth_password_current_write_dto:
        return auth_password_current_write_dto(self.auth_password_current_uid, self.auth_password_current_name, self.tenant_uid, self.account_uid, self.password_hash, self.password_salt, self.date_from, self.date_to, self.usage_count, self.custom_attributes)
    def to_thin(self) -> auth_password_current_thin_dto:
        return auth_password_current_thin_dto(self.auth_password_current_uid, self.auth_password_current_name, self.created_date, self.is_active)
    def touch(self, updated_by: str = "system"):
        self.last_updated_date = datetime.datetime.now()
        self.last_updated_by = updated_by
        self.row_version = self.row_version+1
    def get_list_all_values(self) -> list[any]:
        return [self.auth_password_current_uid, self.auth_password_current_name, self.tenant_uid, self.account_uid, self.password_hash, self.password_salt, self.date_from, self.date_to, self.usage_count, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]
    def get_list_update_values(self, updated_by: str) -> list[any]:
        return [self.auth_password_current_name, self.tenant_uid, self.account_uid, self.password_hash, self.password_salt, self.date_from, self.date_to, self.usage_count, self.custom_attributes, updated_by, self.auth_password_current_uid]
    def is_older_than(self, dt: datetime.datetime) -> bool:
        return self.created_date < dt
    def is_newer_than(self, dt: datetime.datetime) -> bool:
        return self.created_date > dt
    def to_json_read(self) -> str:
        return json.dumps(self.to_read_dict())


@dataclass(frozen=False)
class auth_password_rule_read_dto(base_read_dto, auth_password_rule_write_dto):
    auth_password_uid: str
    auth_password_name: str
    rule_type: int
    rule_parameters: str
    user_scope: str
    row_instance: str
    row_lock: str | None
    row_owner: str
    row_seq: int
    row_guid: str
    row_version: int
    is_active: int
    created_date: datetime.datetime
    created_by: str
    last_updated_date: datetime.datetime
    last_updated_by: str
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str
    def __init__(self, auth_password_uid: str, auth_password_name: str, rule_type: int, rule_parameters: str, user_scope: str, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
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
    @classmethod
    def empty_read(cls):
        return cls(0, "", "", 0, "", "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def default_read(cls):
        return cls(0, "", "", 0, "", "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def random_read(cls):
        return cls(0, base_dto.get_random_uid(), base_dto.get_random_uid(), 0, base_dto.get_random_uid(), base_dto.get_random_uid(), "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_default(cls, auth_password_uid: str, auth_password_name: str, rule_type: int, rule_parameters: str, user_scope: str):
        return cls(0, auth_password_uid, auth_password_name, rule_type, rule_parameters, user_scope, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_full(cls, auth_password_uid: str, auth_password_name: str, rule_type: int, rule_parameters: str, user_scope: str, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
        return cls(auth_password_uid, auth_password_name, rule_type, rule_parameters, user_scope, row_instance, row_lock, row_owner, row_seq, row_guid, row_version, is_active, created_date, created_by, last_updated_date, last_updated_by, removed_date, removed_by, custom_attributes)
    @classmethod
    def from_write(cls, dto: auth_password_rule_write_dto):
        return cls(0, dto.auth_password_uid, dto.auth_password_name, dto.rule_type, dto.rule_parameters, dto.user_scope, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, dto.custom_attributes)
    def clone_read(self):
        return auth_password_rule_read_dto(self.auth_password_uid, self.auth_password_name, self.rule_type, self.rule_parameters, self.user_scope, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes)
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["auth_password_uid"], d["auth_password_name"], d["rule_type"], d["rule_parameters"], d["user_scope"], d["row_instance"], d["row_lock"], d["row_owner"], d["row_seq"], d["row_guid"], d["row_version"], d["is_active"], d["created_date"], d["created_by"], d["last_updated_date"], d["last_updated_by"], d["removed_date"], d["removed_by"], d["custom_attributes"])
    def to_read_dict(self) -> dict:
        return asdict(self)
    def to_write(self) -> auth_password_rule_write_dto:
        return auth_password_rule_write_dto(self.auth_password_uid, self.auth_password_name, self.rule_type, self.rule_parameters, self.user_scope, self.custom_attributes)
    def to_thin(self) -> auth_password_rule_thin_dto:
        return auth_password_rule_thin_dto(self.auth_password_rule_uid, self.auth_password_rule_name, self.created_date, self.is_active)
    def touch(self, updated_by: str = "system"):
        self.last_updated_date = datetime.datetime.now()
        self.last_updated_by = updated_by
        self.row_version = self.row_version+1
    def get_list_all_values(self) -> list[any]:
        return [self.auth_password_uid, self.auth_password_name, self.rule_type, self.rule_parameters, self.user_scope, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]
    def get_list_update_values(self, updated_by: str) -> list[any]:
        return [self.auth_password_uid, self.auth_password_name, self.rule_type, self.rule_parameters, self.user_scope, self.custom_attributes, updated_by, self.auth_password_rule_uid]
    def is_older_than(self, dt: datetime.datetime) -> bool:
        return self.created_date < dt
    def is_newer_than(self, dt: datetime.datetime) -> bool:
        return self.created_date > dt
    def to_json_read(self) -> str:
        return json.dumps(self.to_read_dict())


@dataclass(frozen=False)
class auth_permission_read_dto(base_read_dto, auth_permission_write_dto):
    auth_permission_uid: str
    auth_permission_name: str
    tenant_uid: str
    account_uid: str
    auth_role_uid: str
    client_uid: str | None
    project_instance_uid: str | None
    valid_from_date: datetime.datetime
    valid_till_date: datetime.datetime
    row_instance: str
    row_lock: str | None
    row_owner: str
    row_seq: int
    row_guid: str
    row_version: int
    is_active: int
    created_date: datetime.datetime
    created_by: str
    last_updated_date: datetime.datetime
    last_updated_by: str
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str
    def __init__(self, auth_permission_uid: str, auth_permission_name: str, tenant_uid: str, account_uid: str, auth_role_uid: str, client_uid: str | None, project_instance_uid: str | None, valid_from_date: datetime.datetime, valid_till_date: datetime.datetime, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
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
    @classmethod
    def empty_read(cls):
        return cls(0, "", "", "", "", "", "", "", datetime.datetime.now(), datetime.datetime.now(), "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def default_read(cls):
        return cls(0, base_dto.get_random_uid(), "", "", "", "", "", "", datetime.datetime.now(), datetime.datetime.now(), "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def random_read(cls):
        return cls(0, base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), datetime.datetime.now(), datetime.datetime.now(), "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_default(cls, auth_permission_uid: str, auth_permission_name: str, tenant_uid: str, account_uid: str, auth_role_uid: str, client_uid: str | None, project_instance_uid: str | None, valid_from_date: datetime.datetime, valid_till_date: datetime.datetime):
        return cls(0, auth_permission_uid, auth_permission_name, tenant_uid, account_uid, auth_role_uid, client_uid, project_instance_uid, valid_from_date, valid_till_date, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_full(cls, auth_permission_uid: str, auth_permission_name: str, tenant_uid: str, account_uid: str, auth_role_uid: str, client_uid: str | None, project_instance_uid: str | None, valid_from_date: datetime.datetime, valid_till_date: datetime.datetime, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
        return cls(auth_permission_uid, auth_permission_name, tenant_uid, account_uid, auth_role_uid, client_uid, project_instance_uid, valid_from_date, valid_till_date, row_instance, row_lock, row_owner, row_seq, row_guid, row_version, is_active, created_date, created_by, last_updated_date, last_updated_by, removed_date, removed_by, custom_attributes)
    @classmethod
    def from_write(cls, dto: auth_permission_write_dto):
        return cls(0, dto.auth_permission_uid, dto.auth_permission_name, dto.tenant_uid, dto.account_uid, dto.auth_role_uid, dto.client_uid, dto.project_instance_uid, dto.valid_from_date, dto.valid_till_date, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, dto.custom_attributes)
    def clone_read(self):
        return auth_permission_read_dto(self.auth_permission_uid, self.auth_permission_name, self.tenant_uid, self.account_uid, self.auth_role_uid, self.client_uid, self.project_instance_uid, self.valid_from_date, self.valid_till_date, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes)
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["auth_permission_uid"], d["auth_permission_name"], d["tenant_uid"], d["account_uid"], d["auth_role_uid"], d["client_uid"], d["project_instance_uid"], d["valid_from_date"], d["valid_till_date"], d["row_instance"], d["row_lock"], d["row_owner"], d["row_seq"], d["row_guid"], d["row_version"], d["is_active"], d["created_date"], d["created_by"], d["last_updated_date"], d["last_updated_by"], d["removed_date"], d["removed_by"], d["custom_attributes"])
    def to_read_dict(self) -> dict:
        return asdict(self)
    def to_write(self) -> auth_permission_write_dto:
        return auth_permission_write_dto(self.auth_permission_uid, self.auth_permission_name, self.tenant_uid, self.account_uid, self.auth_role_uid, self.client_uid, self.project_instance_uid, self.valid_from_date, self.valid_till_date, self.custom_attributes)
    def to_thin(self) -> auth_permission_thin_dto:
        return auth_permission_thin_dto(self.auth_permission_uid, self.auth_permission_name, self.created_date, self.is_active)
    def touch(self, updated_by: str = "system"):
        self.last_updated_date = datetime.datetime.now()
        self.last_updated_by = updated_by
        self.row_version = self.row_version+1
    def get_list_all_values(self) -> list[any]:
        return [self.auth_permission_uid, self.auth_permission_name, self.tenant_uid, self.account_uid, self.auth_role_uid, self.client_uid, self.project_instance_uid, self.valid_from_date, self.valid_till_date, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]
    def get_list_update_values(self, updated_by: str) -> list[any]:
        return [self.auth_permission_name, self.tenant_uid, self.account_uid, self.auth_role_uid, self.client_uid, self.project_instance_uid, self.valid_from_date, self.valid_till_date, self.custom_attributes, updated_by, self.auth_permission_uid]
    def is_older_than(self, dt: datetime.datetime) -> bool:
        return self.created_date < dt
    def is_newer_than(self, dt: datetime.datetime) -> bool:
        return self.created_date > dt
    def to_json_read(self) -> str:
        return json.dumps(self.to_read_dict())


@dataclass(frozen=False)
class auth_request_read_dto(base_read_dto, auth_request_write_dto):
    auth_request_uid: str
    auth_request_name: str
    tenant_uid: str
    account_uid: str
    requestor_email: str
    reset_guid: str
    valid_till_date: datetime.datetime
    lock_guid: str | None
    lock_by: str | None
    lock_date: datetime.datetime | None
    is_checked: int
    is_used: int
    check_date: datetime.datetime | None
    use_date: datetime.datetime | None
    event_notification_uid: str | None
    row_instance: str
    row_lock: str | None
    row_owner: str
    row_seq: int
    row_guid: str
    row_version: int
    is_active: int
    created_date: datetime.datetime
    created_by: str
    last_updated_date: datetime.datetime
    last_updated_by: str
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str
    def __init__(self, auth_request_uid: str, auth_request_name: str, tenant_uid: str, account_uid: str, requestor_email: str, reset_guid: str, valid_till_date: datetime.datetime, lock_guid: str | None, lock_by: str | None, lock_date: datetime.datetime | None, is_checked: int, is_used: int, check_date: datetime.datetime | None, use_date: datetime.datetime | None, event_notification_uid: str | None, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
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
    @classmethod
    def empty_read(cls):
        return cls(0, "", "", "", "", "", "", datetime.datetime.now(), "", "", datetime.datetime.now(), 0, 0, datetime.datetime.now(), datetime.datetime.now(), "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def default_read(cls):
        return cls(0, base_dto.get_random_uid(), "", "", "", "", "", datetime.datetime.now(), "", "", datetime.datetime.now(), 0, 0, datetime.datetime.now(), datetime.datetime.now(), "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def random_read(cls):
        return cls(0, base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), datetime.datetime.now(), base_dto.get_random_uid(), base_dto.get_random_uid(), datetime.datetime.now(), 0, 0, datetime.datetime.now(), datetime.datetime.now(), base_dto.get_random_uid(), "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_default(cls, auth_request_uid: str, auth_request_name: str, tenant_uid: str, account_uid: str, requestor_email: str, reset_guid: str, valid_till_date: datetime.datetime, lock_guid: str | None, lock_by: str | None, lock_date: datetime.datetime | None, is_checked: int, is_used: int, check_date: datetime.datetime | None, use_date: datetime.datetime | None, event_notification_uid: str | None):
        return cls(0, auth_request_uid, auth_request_name, tenant_uid, account_uid, requestor_email, reset_guid, valid_till_date, lock_guid, lock_by, lock_date, is_checked, is_used, check_date, use_date, event_notification_uid, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_full(cls, auth_request_uid: str, auth_request_name: str, tenant_uid: str, account_uid: str, requestor_email: str, reset_guid: str, valid_till_date: datetime.datetime, lock_guid: str | None, lock_by: str | None, lock_date: datetime.datetime | None, is_checked: int, is_used: int, check_date: datetime.datetime | None, use_date: datetime.datetime | None, event_notification_uid: str | None, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
        return cls(auth_request_uid, auth_request_name, tenant_uid, account_uid, requestor_email, reset_guid, valid_till_date, lock_guid, lock_by, lock_date, is_checked, is_used, check_date, use_date, event_notification_uid, row_instance, row_lock, row_owner, row_seq, row_guid, row_version, is_active, created_date, created_by, last_updated_date, last_updated_by, removed_date, removed_by, custom_attributes)
    @classmethod
    def from_write(cls, dto: auth_request_write_dto):
        return cls(0, dto.auth_request_uid, dto.auth_request_name, dto.tenant_uid, dto.account_uid, dto.requestor_email, dto.reset_guid, dto.valid_till_date, dto.lock_guid, dto.lock_by, dto.lock_date, dto.is_checked, dto.is_used, dto.check_date, dto.use_date, dto.event_notification_uid, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, dto.custom_attributes)
    def clone_read(self):
        return auth_request_read_dto(self.auth_request_uid, self.auth_request_name, self.tenant_uid, self.account_uid, self.requestor_email, self.reset_guid, self.valid_till_date, self.lock_guid, self.lock_by, self.lock_date, self.is_checked, self.is_used, self.check_date, self.use_date, self.event_notification_uid, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes)
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["auth_request_uid"], d["auth_request_name"], d["tenant_uid"], d["account_uid"], d["requestor_email"], d["reset_guid"], d["valid_till_date"], d["lock_guid"], d["lock_by"], d["lock_date"], d["is_checked"], d["is_used"], d["check_date"], d["use_date"], d["event_notification_uid"], d["row_instance"], d["row_lock"], d["row_owner"], d["row_seq"], d["row_guid"], d["row_version"], d["is_active"], d["created_date"], d["created_by"], d["last_updated_date"], d["last_updated_by"], d["removed_date"], d["removed_by"], d["custom_attributes"])
    def to_read_dict(self) -> dict:
        return asdict(self)
    def to_write(self) -> auth_request_write_dto:
        return auth_request_write_dto(self.auth_request_uid, self.auth_request_name, self.tenant_uid, self.account_uid, self.requestor_email, self.reset_guid, self.valid_till_date, self.lock_guid, self.lock_by, self.lock_date, self.is_checked, self.is_used, self.check_date, self.use_date, self.event_notification_uid, self.custom_attributes)
    def to_thin(self) -> auth_request_thin_dto:
        return auth_request_thin_dto(self.auth_request_uid, self.auth_request_name, self.created_date, self.is_active)
    def touch(self, updated_by: str = "system"):
        self.last_updated_date = datetime.datetime.now()
        self.last_updated_by = updated_by
        self.row_version = self.row_version+1
    def get_list_all_values(self) -> list[any]:
        return [self.auth_request_uid, self.auth_request_name, self.tenant_uid, self.account_uid, self.requestor_email, self.reset_guid, self.valid_till_date, self.lock_guid, self.lock_by, self.lock_date, self.is_checked, self.is_used, self.check_date, self.use_date, self.event_notification_uid, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]
    def get_list_update_values(self, updated_by: str) -> list[any]:
        return [self.auth_request_name, self.tenant_uid, self.account_uid, self.requestor_email, self.reset_guid, self.valid_till_date, self.lock_guid, self.lock_by, self.lock_date, self.is_checked, self.is_used, self.check_date, self.use_date, self.event_notification_uid, self.custom_attributes, updated_by, self.auth_request_uid]
    def is_older_than(self, dt: datetime.datetime) -> bool:
        return self.created_date < dt
    def is_newer_than(self, dt: datetime.datetime) -> bool:
        return self.created_date > dt
    def to_json_read(self) -> str:
        return json.dumps(self.to_read_dict())


@dataclass(frozen=False)
class auth_role_read_dto(base_read_dto, auth_role_write_dto):
    auth_role_uid: str
    auth_role_name: str
    parent_auth_role_uid: str | None
    tenant_uid: str | None
    role_description: str
    access_uris: str
    is_project: int
    is_tenant: int
    is_client: int
    is_custom: int
    row_instance: str
    row_lock: str | None
    row_owner: str
    row_seq: int
    row_guid: str
    row_version: int
    is_active: int
    created_date: datetime.datetime
    created_by: str
    last_updated_date: datetime.datetime
    last_updated_by: str
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str
    def __init__(self, auth_role_uid: str, auth_role_name: str, parent_auth_role_uid: str | None, tenant_uid: str | None, role_description: str, access_uris: str, is_project: int, is_tenant: int, is_client: int, is_custom: int, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
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
    @classmethod
    def empty_read(cls):
        return cls(0, "", "", "", "", "", "", 0, 0, 0, 0, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def default_read(cls):
        return cls(0, base_dto.get_random_uid(), "", "", "", "", "", 0, 0, 0, 0, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def random_read(cls):
        return cls(0, base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), 0, 0, 0, 0, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_default(cls, auth_role_uid: str, auth_role_name: str, parent_auth_role_uid: str | None, tenant_uid: str | None, role_description: str, access_uris: str, is_project: int, is_tenant: int, is_client: int, is_custom: int):
        return cls(0, auth_role_uid, auth_role_name, parent_auth_role_uid, tenant_uid, role_description, access_uris, is_project, is_tenant, is_client, is_custom, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_full(cls, auth_role_uid: str, auth_role_name: str, parent_auth_role_uid: str | None, tenant_uid: str | None, role_description: str, access_uris: str, is_project: int, is_tenant: int, is_client: int, is_custom: int, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
        return cls(auth_role_uid, auth_role_name, parent_auth_role_uid, tenant_uid, role_description, access_uris, is_project, is_tenant, is_client, is_custom, row_instance, row_lock, row_owner, row_seq, row_guid, row_version, is_active, created_date, created_by, last_updated_date, last_updated_by, removed_date, removed_by, custom_attributes)
    @classmethod
    def from_write(cls, dto: auth_role_write_dto):
        return cls(0, dto.auth_role_uid, dto.auth_role_name, dto.parent_auth_role_uid, dto.tenant_uid, dto.role_description, dto.access_uris, dto.is_project, dto.is_tenant, dto.is_client, dto.is_custom, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, dto.custom_attributes)
    def clone_read(self):
        return auth_role_read_dto(self.auth_role_uid, self.auth_role_name, self.parent_auth_role_uid, self.tenant_uid, self.role_description, self.access_uris, self.is_project, self.is_tenant, self.is_client, self.is_custom, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes)
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["auth_role_uid"], d["auth_role_name"], d["parent_auth_role_uid"], d["tenant_uid"], d["role_description"], d["access_uris"], d["is_project"], d["is_tenant"], d["is_client"], d["is_custom"], d["row_instance"], d["row_lock"], d["row_owner"], d["row_seq"], d["row_guid"], d["row_version"], d["is_active"], d["created_date"], d["created_by"], d["last_updated_date"], d["last_updated_by"], d["removed_date"], d["removed_by"], d["custom_attributes"])
    def to_read_dict(self) -> dict:
        return asdict(self)
    def to_write(self) -> auth_role_write_dto:
        return auth_role_write_dto(self.auth_role_uid, self.auth_role_name, self.parent_auth_role_uid, self.tenant_uid, self.role_description, self.access_uris, self.is_project, self.is_tenant, self.is_client, self.is_custom, self.custom_attributes)
    def to_thin(self) -> auth_role_thin_dto:
        return auth_role_thin_dto(self.auth_role_uid, self.auth_role_name, self.created_date, self.is_active)
    def touch(self, updated_by: str = "system"):
        self.last_updated_date = datetime.datetime.now()
        self.last_updated_by = updated_by
        self.row_version = self.row_version+1
    def get_list_all_values(self) -> list[any]:
        return [self.auth_role_uid, self.auth_role_name, self.parent_auth_role_uid, self.tenant_uid, self.role_description, self.access_uris, self.is_project, self.is_tenant, self.is_client, self.is_custom, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]
    def get_list_update_values(self, updated_by: str) -> list[any]:
        return [self.auth_role_name, self.parent_auth_role_uid, self.tenant_uid, self.role_description, self.access_uris, self.is_project, self.is_tenant, self.is_client, self.is_custom, self.custom_attributes, updated_by, self.auth_role_uid]
    def is_older_than(self, dt: datetime.datetime) -> bool:
        return self.created_date < dt
    def is_newer_than(self, dt: datetime.datetime) -> bool:
        return self.created_date > dt
    def to_json_read(self) -> str:
        return json.dumps(self.to_read_dict())


@dataclass(frozen=False)
class auth_role_uri_read_dto(base_read_dto, auth_role_uri_write_dto):
    auth_role_uri_uid: str
    auth_role_uri_name: str
    auth_role_uid: str | None
    uri: str
    row_instance: str
    row_lock: str | None
    row_owner: str
    row_seq: int
    row_guid: str
    row_version: int
    is_active: int
    created_date: datetime.datetime
    created_by: str
    last_updated_date: datetime.datetime
    last_updated_by: str
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str
    def __init__(self, auth_role_uri_uid: str, auth_role_uri_name: str, auth_role_uid: str | None, uri: str, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
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
    @classmethod
    def empty_read(cls):
        return cls(0, "", "", "", "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def default_read(cls):
        return cls(0, base_dto.get_random_uid(), "", "", "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def random_read(cls):
        return cls(0, base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_default(cls, auth_role_uri_uid: str, auth_role_uri_name: str, auth_role_uid: str | None, uri: str):
        return cls(0, auth_role_uri_uid, auth_role_uri_name, auth_role_uid, uri, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_full(cls, auth_role_uri_uid: str, auth_role_uri_name: str, auth_role_uid: str | None, uri: str, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
        return cls(auth_role_uri_uid, auth_role_uri_name, auth_role_uid, uri, row_instance, row_lock, row_owner, row_seq, row_guid, row_version, is_active, created_date, created_by, last_updated_date, last_updated_by, removed_date, removed_by, custom_attributes)
    @classmethod
    def from_write(cls, dto: auth_role_uri_write_dto):
        return cls(0, dto.auth_role_uri_uid, dto.auth_role_uri_name, dto.auth_role_uid, dto.uri, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, dto.custom_attributes)
    def clone_read(self):
        return auth_role_uri_read_dto(self.auth_role_uri_uid, self.auth_role_uri_name, self.auth_role_uid, self.uri, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes)
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["auth_role_uri_uid"], d["auth_role_uri_name"], d["auth_role_uid"], d["uri"], d["row_instance"], d["row_lock"], d["row_owner"], d["row_seq"], d["row_guid"], d["row_version"], d["is_active"], d["created_date"], d["created_by"], d["last_updated_date"], d["last_updated_by"], d["removed_date"], d["removed_by"], d["custom_attributes"])
    def to_read_dict(self) -> dict:
        return asdict(self)
    def to_write(self) -> auth_role_uri_write_dto:
        return auth_role_uri_write_dto(self.auth_role_uri_uid, self.auth_role_uri_name, self.auth_role_uid, self.uri, self.custom_attributes)
    def to_thin(self) -> auth_role_uri_thin_dto:
        return auth_role_uri_thin_dto(self.auth_role_uri_uid, self.auth_role_uri_name, self.created_date, self.is_active)
    def touch(self, updated_by: str = "system"):
        self.last_updated_date = datetime.datetime.now()
        self.last_updated_by = updated_by
        self.row_version = self.row_version+1
    def get_list_all_values(self) -> list[any]:
        return [self.auth_role_uri_uid, self.auth_role_uri_name, self.auth_role_uid, self.uri, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]
    def get_list_update_values(self, updated_by: str) -> list[any]:
        return [self.auth_role_uri_name, self.auth_role_uid, self.uri, self.custom_attributes, updated_by, self.auth_role_uri_uid]
    def is_older_than(self, dt: datetime.datetime) -> bool:
        return self.created_date < dt
    def is_newer_than(self, dt: datetime.datetime) -> bool:
        return self.created_date > dt
    def to_json_read(self) -> str:
        return json.dumps(self.to_read_dict())


@dataclass(frozen=False)
class auth_session_read_dto(base_read_dto, auth_session_write_dto):
    auth_session_uid: str
    auth_session_name: str
    tenant_uid: str | None
    account_uid: str | None
    session_token: str
    browser_name: str
    browser_description: str
    host_name: str
    row_instance: str
    row_lock: str | None
    row_owner: str
    row_seq: int
    row_guid: str
    row_version: int
    is_active: int
    created_date: datetime.datetime
    created_by: str
    last_updated_date: datetime.datetime
    last_updated_by: str
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str
    def __init__(self, auth_session_uid: str, auth_session_name: str, tenant_uid: str | None, account_uid: str | None, session_token: str, browser_name: str, browser_description: str, host_name: str, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
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
    @classmethod
    def empty_read(cls):
        return cls(0, "", "", "", "", "", "", "", "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def default_read(cls):
        return cls(0, base_dto.get_random_uid(), "", "", "", "", "", "", "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def random_read(cls):
        return cls(0, base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_default(cls, auth_session_uid: str, auth_session_name: str, tenant_uid: str | None, account_uid: str | None, session_token: str, browser_name: str, browser_description: str, host_name: str):
        return cls(0, auth_session_uid, auth_session_name, tenant_uid, account_uid, session_token, browser_name, browser_description, host_name, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_full(cls, auth_session_uid: str, auth_session_name: str, tenant_uid: str | None, account_uid: str | None, session_token: str, browser_name: str, browser_description: str, host_name: str, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
        return cls(auth_session_uid, auth_session_name, tenant_uid, account_uid, session_token, browser_name, browser_description, host_name, row_instance, row_lock, row_owner, row_seq, row_guid, row_version, is_active, created_date, created_by, last_updated_date, last_updated_by, removed_date, removed_by, custom_attributes)
    @classmethod
    def from_write(cls, dto: auth_session_write_dto):
        return cls(0, dto.auth_session_uid, dto.auth_session_name, dto.tenant_uid, dto.account_uid, dto.session_token, dto.browser_name, dto.browser_description, dto.host_name, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, dto.custom_attributes)
    def clone_read(self):
        return auth_session_read_dto(self.auth_session_uid, self.auth_session_name, self.tenant_uid, self.account_uid, self.session_token, self.browser_name, self.browser_description, self.host_name, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes)
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["auth_session_uid"], d["auth_session_name"], d["tenant_uid"], d["account_uid"], d["session_token"], d["browser_name"], d["browser_description"], d["host_name"], d["row_instance"], d["row_lock"], d["row_owner"], d["row_seq"], d["row_guid"], d["row_version"], d["is_active"], d["created_date"], d["created_by"], d["last_updated_date"], d["last_updated_by"], d["removed_date"], d["removed_by"], d["custom_attributes"])
    def to_read_dict(self) -> dict:
        return asdict(self)
    def to_write(self) -> auth_session_write_dto:
        return auth_session_write_dto(self.auth_session_uid, self.auth_session_name, self.tenant_uid, self.account_uid, self.session_token, self.browser_name, self.browser_description, self.host_name, self.custom_attributes)
    def to_thin(self) -> auth_session_thin_dto:
        return auth_session_thin_dto(self.auth_session_uid, self.auth_session_name, self.created_date, self.is_active)
    def touch(self, updated_by: str = "system"):
        self.last_updated_date = datetime.datetime.now()
        self.last_updated_by = updated_by
        self.row_version = self.row_version+1
    def get_list_all_values(self) -> list[any]:
        return [self.auth_session_uid, self.auth_session_name, self.tenant_uid, self.account_uid, self.session_token, self.browser_name, self.browser_description, self.host_name, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]
    def get_list_update_values(self, updated_by: str) -> list[any]:
        return [self.auth_session_name, self.tenant_uid, self.account_uid, self.session_token, self.browser_name, self.browser_description, self.host_name, self.custom_attributes, updated_by, self.auth_session_uid]
    def is_older_than(self, dt: datetime.datetime) -> bool:
        return self.created_date < dt
    def is_newer_than(self, dt: datetime.datetime) -> bool:
        return self.created_date > dt
    def to_json_read(self) -> str:
        return json.dumps(self.to_read_dict())


@dataclass(frozen=False)
class auth_sso_read_dto(base_read_dto, auth_sso_write_dto):
    auth_sso_uid: str
    auth_sso_name: str
    tenant_uid: str
    owner_account_uid: str | None
    sso_name: str
    sso_url: str
    sso_key: str
    sso_secret: str
    sso_code: str | None
    clientid: str | None
    clientsecret: str | None
    callback_url: str | None
    row_instance: str
    row_lock: str | None
    row_owner: str
    row_seq: int
    row_guid: str
    row_version: int
    is_active: int
    created_date: datetime.datetime
    created_by: str
    last_updated_date: datetime.datetime
    last_updated_by: str
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str
    def __init__(self, auth_sso_uid: str, auth_sso_name: str, tenant_uid: str, owner_account_uid: str | None, sso_name: str, sso_url: str, sso_key: str, sso_secret: str, sso_code: str | None, clientid: str | None, clientsecret: str | None, callback_url: str | None, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
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
    @classmethod
    def empty_read(cls):
        return cls(0, "", "", "", "", "", "", "", "", "", "", "", "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def default_read(cls):
        return cls(0, base_dto.get_random_uid(), "", "", "", "", "", "", "", "", "", "", "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def random_read(cls):
        return cls(0, base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_default(cls, auth_sso_uid: str, auth_sso_name: str, tenant_uid: str, owner_account_uid: str | None, sso_name: str, sso_url: str, sso_key: str, sso_secret: str, sso_code: str | None, clientid: str | None, clientsecret: str | None, callback_url: str | None):
        return cls(0, auth_sso_uid, auth_sso_name, tenant_uid, owner_account_uid, sso_name, sso_url, sso_key, sso_secret, sso_code, clientid, clientsecret, callback_url, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_full(cls, auth_sso_uid: str, auth_sso_name: str, tenant_uid: str, owner_account_uid: str | None, sso_name: str, sso_url: str, sso_key: str, sso_secret: str, sso_code: str | None, clientid: str | None, clientsecret: str | None, callback_url: str | None, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
        return cls(auth_sso_uid, auth_sso_name, tenant_uid, owner_account_uid, sso_name, sso_url, sso_key, sso_secret, sso_code, clientid, clientsecret, callback_url, row_instance, row_lock, row_owner, row_seq, row_guid, row_version, is_active, created_date, created_by, last_updated_date, last_updated_by, removed_date, removed_by, custom_attributes)
    @classmethod
    def from_write(cls, dto: auth_sso_write_dto):
        return cls(0, dto.auth_sso_uid, dto.auth_sso_name, dto.tenant_uid, dto.owner_account_uid, dto.sso_name, dto.sso_url, dto.sso_key, dto.sso_secret, dto.sso_code, dto.clientid, dto.clientsecret, dto.callback_url, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, dto.custom_attributes)
    def clone_read(self):
        return auth_sso_read_dto(self.auth_sso_uid, self.auth_sso_name, self.tenant_uid, self.owner_account_uid, self.sso_name, self.sso_url, self.sso_key, self.sso_secret, self.sso_code, self.clientid, self.clientsecret, self.callback_url, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes)
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["auth_sso_uid"], d["auth_sso_name"], d["tenant_uid"], d["owner_account_uid"], d["sso_name"], d["sso_url"], d["sso_key"], d["sso_secret"], d["sso_code"], d["clientid"], d["clientsecret"], d["callback_url"], d["row_instance"], d["row_lock"], d["row_owner"], d["row_seq"], d["row_guid"], d["row_version"], d["is_active"], d["created_date"], d["created_by"], d["last_updated_date"], d["last_updated_by"], d["removed_date"], d["removed_by"], d["custom_attributes"])
    def to_read_dict(self) -> dict:
        return asdict(self)
    def to_write(self) -> auth_sso_write_dto:
        return auth_sso_write_dto(self.auth_sso_uid, self.auth_sso_name, self.tenant_uid, self.owner_account_uid, self.sso_name, self.sso_url, self.sso_key, self.sso_secret, self.sso_code, self.clientid, self.clientsecret, self.callback_url, self.custom_attributes)
    def to_thin(self) -> auth_sso_thin_dto:
        return auth_sso_thin_dto(self.auth_sso_uid, self.auth_sso_name, self.created_date, self.is_active)
    def touch(self, updated_by: str = "system"):
        self.last_updated_date = datetime.datetime.now()
        self.last_updated_by = updated_by
        self.row_version = self.row_version+1
    def get_list_all_values(self) -> list[any]:
        return [self.auth_sso_uid, self.auth_sso_name, self.tenant_uid, self.owner_account_uid, self.sso_name, self.sso_url, self.sso_key, self.sso_secret, self.sso_code, self.clientid, self.clientsecret, self.callback_url, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]
    def get_list_update_values(self, updated_by: str) -> list[any]:
        return [self.auth_sso_name, self.tenant_uid, self.owner_account_uid, self.sso_name, self.sso_url, self.sso_key, self.sso_secret, self.sso_code, self.clientid, self.clientsecret, self.callback_url, self.custom_attributes, updated_by, self.auth_sso_uid]
    def is_older_than(self, dt: datetime.datetime) -> bool:
        return self.created_date < dt
    def is_newer_than(self, dt: datetime.datetime) -> bool:
        return self.created_date > dt
    def to_json_read(self) -> str:
        return json.dumps(self.to_read_dict())


@dataclass(frozen=False)
class auth_token_read_dto(base_read_dto, auth_token_write_dto):
    auth_token_uid: str
    auth_token_name: str
    tenant_uid: str
    account_uid: str
    token_seq: int
    token_hash: str
    token_salt: str
    valid_till_date: datetime.datetime | None
    last_use_date: datetime.datetime | None
    is_last: int
    row_instance: str
    row_lock: str | None
    row_owner: str
    row_seq: int
    row_guid: str
    row_version: int
    is_active: int
    created_date: datetime.datetime
    created_by: str
    last_updated_date: datetime.datetime
    last_updated_by: str
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str
    def __init__(self, auth_token_uid: str, auth_token_name: str, tenant_uid: str, account_uid: str, token_seq: int, token_hash: str, token_salt: str, valid_till_date: datetime.datetime | None, last_use_date: datetime.datetime | None, is_last: int, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
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
    @classmethod
    def empty_read(cls):
        return cls(0, "", "", "", "", 0, "", "", datetime.datetime.now(), datetime.datetime.now(), 0, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def default_read(cls):
        return cls(0, base_dto.get_random_uid(), "", "", "", 0, "", "", datetime.datetime.now(), datetime.datetime.now(), 0, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def random_read(cls):
        return cls(0, base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), 0, base_dto.get_random_uid(), base_dto.get_random_uid(), datetime.datetime.now(), datetime.datetime.now(), 0, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_default(cls, auth_token_uid: str, auth_token_name: str, tenant_uid: str, account_uid: str, token_seq: int, token_hash: str, token_salt: str, valid_till_date: datetime.datetime | None, last_use_date: datetime.datetime | None, is_last: int):
        return cls(0, auth_token_uid, auth_token_name, tenant_uid, account_uid, token_seq, token_hash, token_salt, valid_till_date, last_use_date, is_last, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_full(cls, auth_token_uid: str, auth_token_name: str, tenant_uid: str, account_uid: str, token_seq: int, token_hash: str, token_salt: str, valid_till_date: datetime.datetime | None, last_use_date: datetime.datetime | None, is_last: int, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
        return cls(auth_token_uid, auth_token_name, tenant_uid, account_uid, token_seq, token_hash, token_salt, valid_till_date, last_use_date, is_last, row_instance, row_lock, row_owner, row_seq, row_guid, row_version, is_active, created_date, created_by, last_updated_date, last_updated_by, removed_date, removed_by, custom_attributes)
    @classmethod
    def from_write(cls, dto: auth_token_write_dto):
        return cls(0, dto.auth_token_uid, dto.auth_token_name, dto.tenant_uid, dto.account_uid, dto.token_seq, dto.token_hash, dto.token_salt, dto.valid_till_date, dto.last_use_date, dto.is_last, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, dto.custom_attributes)
    def clone_read(self):
        return auth_token_read_dto(self.auth_token_uid, self.auth_token_name, self.tenant_uid, self.account_uid, self.token_seq, self.token_hash, self.token_salt, self.valid_till_date, self.last_use_date, self.is_last, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes)
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["auth_token_uid"], d["auth_token_name"], d["tenant_uid"], d["account_uid"], d["token_seq"], d["token_hash"], d["token_salt"], d["valid_till_date"], d["last_use_date"], d["is_last"], d["row_instance"], d["row_lock"], d["row_owner"], d["row_seq"], d["row_guid"], d["row_version"], d["is_active"], d["created_date"], d["created_by"], d["last_updated_date"], d["last_updated_by"], d["removed_date"], d["removed_by"], d["custom_attributes"])
    def to_read_dict(self) -> dict:
        return asdict(self)
    def to_write(self) -> auth_token_write_dto:
        return auth_token_write_dto(self.auth_token_uid, self.auth_token_name, self.tenant_uid, self.account_uid, self.token_seq, self.token_hash, self.token_salt, self.valid_till_date, self.last_use_date, self.is_last, self.custom_attributes)
    def to_thin(self) -> auth_token_thin_dto:
        return auth_token_thin_dto(self.auth_token_uid, self.auth_token_name, self.created_date, self.is_active)
    def touch(self, updated_by: str = "system"):
        self.last_updated_date = datetime.datetime.now()
        self.last_updated_by = updated_by
        self.row_version = self.row_version+1
    def get_list_all_values(self) -> list[any]:
        return [self.auth_token_uid, self.auth_token_name, self.tenant_uid, self.account_uid, self.token_seq, self.token_hash, self.token_salt, self.valid_till_date, self.last_use_date, self.is_last, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]
    def get_list_update_values(self, updated_by: str) -> list[any]:
        return [self.auth_token_name, self.tenant_uid, self.account_uid, self.token_seq, self.token_hash, self.token_salt, self.valid_till_date, self.last_use_date, self.is_last, self.custom_attributes, updated_by, self.auth_token_uid]
    def is_older_than(self, dt: datetime.datetime) -> bool:
        return self.created_date < dt
    def is_newer_than(self, dt: datetime.datetime) -> bool:
        return self.created_date > dt
    def to_json_read(self) -> str:
        return json.dumps(self.to_read_dict())


@dataclass(frozen=False)
class calendar_account_read_dto(base_read_dto, calendar_account_write_dto):
    calendar_account_uid: str
    calendar_account_name: str
    tenant_uid: str
    account_uid: str
    calendar_type_uid: str
    row_instance: str
    row_lock: str | None
    row_owner: str
    row_seq: int
    row_guid: str
    row_version: int
    is_active: int
    created_date: datetime.datetime
    created_by: str
    last_updated_date: datetime.datetime
    last_updated_by: str
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str
    def __init__(self, calendar_account_uid: str, calendar_account_name: str, tenant_uid: str, account_uid: str, calendar_type_uid: str, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
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
    @classmethod
    def empty_read(cls):
        return cls(0, "", "", "", "", "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def default_read(cls):
        return cls(0, base_dto.get_random_uid(), "", "", "", "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def random_read(cls):
        return cls(0, base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_default(cls, calendar_account_uid: str, calendar_account_name: str, tenant_uid: str, account_uid: str, calendar_type_uid: str):
        return cls(0, calendar_account_uid, calendar_account_name, tenant_uid, account_uid, calendar_type_uid, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_full(cls, calendar_account_uid: str, calendar_account_name: str, tenant_uid: str, account_uid: str, calendar_type_uid: str, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
        return cls(calendar_account_uid, calendar_account_name, tenant_uid, account_uid, calendar_type_uid, row_instance, row_lock, row_owner, row_seq, row_guid, row_version, is_active, created_date, created_by, last_updated_date, last_updated_by, removed_date, removed_by, custom_attributes)
    @classmethod
    def from_write(cls, dto: calendar_account_write_dto):
        return cls(0, dto.calendar_account_uid, dto.calendar_account_name, dto.tenant_uid, dto.account_uid, dto.calendar_type_uid, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, dto.custom_attributes)
    def clone_read(self):
        return calendar_account_read_dto(self.calendar_account_uid, self.calendar_account_name, self.tenant_uid, self.account_uid, self.calendar_type_uid, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes)
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["calendar_account_uid"], d["calendar_account_name"], d["tenant_uid"], d["account_uid"], d["calendar_type_uid"], d["row_instance"], d["row_lock"], d["row_owner"], d["row_seq"], d["row_guid"], d["row_version"], d["is_active"], d["created_date"], d["created_by"], d["last_updated_date"], d["last_updated_by"], d["removed_date"], d["removed_by"], d["custom_attributes"])
    def to_read_dict(self) -> dict:
        return asdict(self)
    def to_write(self) -> calendar_account_write_dto:
        return calendar_account_write_dto(self.calendar_account_uid, self.calendar_account_name, self.tenant_uid, self.account_uid, self.calendar_type_uid, self.custom_attributes)
    def to_thin(self) -> calendar_account_thin_dto:
        return calendar_account_thin_dto(self.calendar_account_uid, self.calendar_account_name, self.created_date, self.is_active)
    def touch(self, updated_by: str = "system"):
        self.last_updated_date = datetime.datetime.now()
        self.last_updated_by = updated_by
        self.row_version = self.row_version+1
    def get_list_all_values(self) -> list[any]:
        return [self.calendar_account_uid, self.calendar_account_name, self.tenant_uid, self.account_uid, self.calendar_type_uid, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]
    def get_list_update_values(self, updated_by: str) -> list[any]:
        return [self.calendar_account_name, self.tenant_uid, self.account_uid, self.calendar_type_uid, self.custom_attributes, updated_by, self.calendar_account_uid]
    def is_older_than(self, dt: datetime.datetime) -> bool:
        return self.created_date < dt
    def is_newer_than(self, dt: datetime.datetime) -> bool:
        return self.created_date > dt
    def to_json_read(self) -> str:
        return json.dumps(self.to_read_dict())


@dataclass(frozen=False)
class calendar_approval_read_dto(base_read_dto, calendar_approval_write_dto):
    calendar_approval_uid: str
    calendar_approval_name: str
    client_uid: str
    account_uid: str
    calendar_approval_type_uid: str
    calendar_event_group_uid: str
    calendar_type_uid: str
    time_submit_type_name: str
    row_instance: str
    row_lock: str | None
    row_owner: str
    row_seq: int
    row_guid: str
    row_version: int
    is_active: int
    created_date: datetime.datetime
    created_by: str
    last_updated_date: datetime.datetime
    last_updated_by: str
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str
    def __init__(self, calendar_approval_uid: str, calendar_approval_name: str, client_uid: str, account_uid: str, calendar_approval_type_uid: str, calendar_event_group_uid: str, calendar_type_uid: str, time_submit_type_name: str, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
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
    @classmethod
    def empty_read(cls):
        return cls(0, "", "", "", "", "", "", "", "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def default_read(cls):
        return cls(0, base_dto.get_random_uid(), "", "", "", "", "", "", "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def random_read(cls):
        return cls(0, base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_default(cls, calendar_approval_uid: str, calendar_approval_name: str, client_uid: str, account_uid: str, calendar_approval_type_uid: str, calendar_event_group_uid: str, calendar_type_uid: str, time_submit_type_name: str):
        return cls(0, calendar_approval_uid, calendar_approval_name, client_uid, account_uid, calendar_approval_type_uid, calendar_event_group_uid, calendar_type_uid, time_submit_type_name, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_full(cls, calendar_approval_uid: str, calendar_approval_name: str, client_uid: str, account_uid: str, calendar_approval_type_uid: str, calendar_event_group_uid: str, calendar_type_uid: str, time_submit_type_name: str, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
        return cls(calendar_approval_uid, calendar_approval_name, client_uid, account_uid, calendar_approval_type_uid, calendar_event_group_uid, calendar_type_uid, time_submit_type_name, row_instance, row_lock, row_owner, row_seq, row_guid, row_version, is_active, created_date, created_by, last_updated_date, last_updated_by, removed_date, removed_by, custom_attributes)
    @classmethod
    def from_write(cls, dto: calendar_approval_write_dto):
        return cls(0, dto.calendar_approval_uid, dto.calendar_approval_name, dto.client_uid, dto.account_uid, dto.calendar_approval_type_uid, dto.calendar_event_group_uid, dto.calendar_type_uid, dto.time_submit_type_name, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, dto.custom_attributes)
    def clone_read(self):
        return calendar_approval_read_dto(self.calendar_approval_uid, self.calendar_approval_name, self.client_uid, self.account_uid, self.calendar_approval_type_uid, self.calendar_event_group_uid, self.calendar_type_uid, self.time_submit_type_name, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes)
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["calendar_approval_uid"], d["calendar_approval_name"], d["client_uid"], d["account_uid"], d["calendar_approval_type_uid"], d["calendar_event_group_uid"], d["calendar_type_uid"], d["time_submit_type_name"], d["row_instance"], d["row_lock"], d["row_owner"], d["row_seq"], d["row_guid"], d["row_version"], d["is_active"], d["created_date"], d["created_by"], d["last_updated_date"], d["last_updated_by"], d["removed_date"], d["removed_by"], d["custom_attributes"])
    def to_read_dict(self) -> dict:
        return asdict(self)
    def to_write(self) -> calendar_approval_write_dto:
        return calendar_approval_write_dto(self.calendar_approval_uid, self.calendar_approval_name, self.client_uid, self.account_uid, self.calendar_approval_type_uid, self.calendar_event_group_uid, self.calendar_type_uid, self.time_submit_type_name, self.custom_attributes)
    def to_thin(self) -> calendar_approval_thin_dto:
        return calendar_approval_thin_dto(self.calendar_approval_uid, self.calendar_approval_name, self.created_date, self.is_active)
    def touch(self, updated_by: str = "system"):
        self.last_updated_date = datetime.datetime.now()
        self.last_updated_by = updated_by
        self.row_version = self.row_version+1
    def get_list_all_values(self) -> list[any]:
        return [self.calendar_approval_uid, self.calendar_approval_name, self.client_uid, self.account_uid, self.calendar_approval_type_uid, self.calendar_event_group_uid, self.calendar_type_uid, self.time_submit_type_name, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]
    def get_list_update_values(self, updated_by: str) -> list[any]:
        return [self.calendar_approval_name, self.client_uid, self.account_uid, self.calendar_approval_type_uid, self.calendar_event_group_uid, self.calendar_type_uid, self.time_submit_type_name, self.custom_attributes, updated_by, self.calendar_approval_uid]
    def is_older_than(self, dt: datetime.datetime) -> bool:
        return self.created_date < dt
    def is_newer_than(self, dt: datetime.datetime) -> bool:
        return self.created_date > dt
    def to_json_read(self) -> str:
        return json.dumps(self.to_read_dict())


@dataclass(frozen=False)
class calendar_approval_type_read_dto(base_read_dto, calendar_approval_type_write_dto):
    calendar_approval_type_uid: str
    calendar_approval_type_name: str
    row_instance: str
    row_lock: str | None
    row_owner: str
    row_seq: int
    row_guid: str
    row_version: int
    is_active: int
    created_date: datetime.datetime
    created_by: str
    last_updated_date: datetime.datetime
    last_updated_by: str
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str
    def __init__(self, calendar_approval_type_uid: str, calendar_approval_type_name: str, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
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
    @classmethod
    def empty_read(cls):
        return cls(0, "", "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def default_read(cls):
        return cls(0, base_dto.get_random_uid(), "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def random_read(cls):
        return cls(0, base_dto.get_random_uid(), base_dto.get_random_uid(), "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_default(cls, calendar_approval_type_uid: str, calendar_approval_type_name: str):
        return cls(0, calendar_approval_type_uid, calendar_approval_type_name, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_full(cls, calendar_approval_type_uid: str, calendar_approval_type_name: str, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
        return cls(calendar_approval_type_uid, calendar_approval_type_name, row_instance, row_lock, row_owner, row_seq, row_guid, row_version, is_active, created_date, created_by, last_updated_date, last_updated_by, removed_date, removed_by, custom_attributes)
    @classmethod
    def from_write(cls, dto: calendar_approval_type_write_dto):
        return cls(0, dto.calendar_approval_type_uid, dto.calendar_approval_type_name, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, dto.custom_attributes)
    def clone_read(self):
        return calendar_approval_type_read_dto(self.calendar_approval_type_uid, self.calendar_approval_type_name, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes)
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["calendar_approval_type_uid"], d["calendar_approval_type_name"], d["row_instance"], d["row_lock"], d["row_owner"], d["row_seq"], d["row_guid"], d["row_version"], d["is_active"], d["created_date"], d["created_by"], d["last_updated_date"], d["last_updated_by"], d["removed_date"], d["removed_by"], d["custom_attributes"])
    def to_read_dict(self) -> dict:
        return asdict(self)
    def to_write(self) -> calendar_approval_type_write_dto:
        return calendar_approval_type_write_dto(self.calendar_approval_type_uid, self.calendar_approval_type_name, self.custom_attributes)
    def to_thin(self) -> calendar_approval_type_thin_dto:
        return calendar_approval_type_thin_dto(self.calendar_approval_type_uid, self.calendar_approval_type_name, self.created_date, self.is_active)
    def touch(self, updated_by: str = "system"):
        self.last_updated_date = datetime.datetime.now()
        self.last_updated_by = updated_by
        self.row_version = self.row_version+1
    def get_list_all_values(self) -> list[any]:
        return [self.calendar_approval_type_uid, self.calendar_approval_type_name, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]
    def get_list_update_values(self, updated_by: str) -> list[any]:
        return [self.calendar_approval_type_name, self.custom_attributes, updated_by, self.calendar_approval_type_uid]
    def is_older_than(self, dt: datetime.datetime) -> bool:
        return self.created_date < dt
    def is_newer_than(self, dt: datetime.datetime) -> bool:
        return self.created_date > dt
    def to_json_read(self) -> str:
        return json.dumps(self.to_read_dict())


@dataclass(frozen=False)
class calendar_event_read_dto(base_read_dto, calendar_event_write_dto):
    calendar_event_uid: str
    calendar_event_name: str
    client_uid: str
    account_uid: str
    calendar_event_group_uid: str
    calendar_type_uid: str
    row_instance: str
    row_lock: str | None
    row_owner: str
    row_seq: int
    row_guid: str
    row_version: int
    is_active: int
    created_date: datetime.datetime
    created_by: str
    last_updated_date: datetime.datetime
    last_updated_by: str
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str
    def __init__(self, calendar_event_uid: str, calendar_event_name: str, client_uid: str, account_uid: str, calendar_event_group_uid: str, calendar_type_uid: str, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
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
    @classmethod
    def empty_read(cls):
        return cls(0, "", "", "", "", "", "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def default_read(cls):
        return cls(0, base_dto.get_random_uid(), "", "", "", "", "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def random_read(cls):
        return cls(0, base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_default(cls, calendar_event_uid: str, calendar_event_name: str, client_uid: str, account_uid: str, calendar_event_group_uid: str, calendar_type_uid: str):
        return cls(0, calendar_event_uid, calendar_event_name, client_uid, account_uid, calendar_event_group_uid, calendar_type_uid, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_full(cls, calendar_event_uid: str, calendar_event_name: str, client_uid: str, account_uid: str, calendar_event_group_uid: str, calendar_type_uid: str, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
        return cls(calendar_event_uid, calendar_event_name, client_uid, account_uid, calendar_event_group_uid, calendar_type_uid, row_instance, row_lock, row_owner, row_seq, row_guid, row_version, is_active, created_date, created_by, last_updated_date, last_updated_by, removed_date, removed_by, custom_attributes)
    @classmethod
    def from_write(cls, dto: calendar_event_write_dto):
        return cls(0, dto.calendar_event_uid, dto.calendar_event_name, dto.client_uid, dto.account_uid, dto.calendar_event_group_uid, dto.calendar_type_uid, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, dto.custom_attributes)
    def clone_read(self):
        return calendar_event_read_dto(self.calendar_event_uid, self.calendar_event_name, self.client_uid, self.account_uid, self.calendar_event_group_uid, self.calendar_type_uid, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes)
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["calendar_event_uid"], d["calendar_event_name"], d["client_uid"], d["account_uid"], d["calendar_event_group_uid"], d["calendar_type_uid"], d["row_instance"], d["row_lock"], d["row_owner"], d["row_seq"], d["row_guid"], d["row_version"], d["is_active"], d["created_date"], d["created_by"], d["last_updated_date"], d["last_updated_by"], d["removed_date"], d["removed_by"], d["custom_attributes"])
    def to_read_dict(self) -> dict:
        return asdict(self)
    def to_write(self) -> calendar_event_write_dto:
        return calendar_event_write_dto(self.calendar_event_uid, self.calendar_event_name, self.client_uid, self.account_uid, self.calendar_event_group_uid, self.calendar_type_uid, self.custom_attributes)
    def to_thin(self) -> calendar_event_thin_dto:
        return calendar_event_thin_dto(self.calendar_event_uid, self.calendar_event_name, self.created_date, self.is_active)
    def touch(self, updated_by: str = "system"):
        self.last_updated_date = datetime.datetime.now()
        self.last_updated_by = updated_by
        self.row_version = self.row_version+1
    def get_list_all_values(self) -> list[any]:
        return [self.calendar_event_uid, self.calendar_event_name, self.client_uid, self.account_uid, self.calendar_event_group_uid, self.calendar_type_uid, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]
    def get_list_update_values(self, updated_by: str) -> list[any]:
        return [self.calendar_event_name, self.client_uid, self.account_uid, self.calendar_event_group_uid, self.calendar_type_uid, self.custom_attributes, updated_by, self.calendar_event_uid]
    def is_older_than(self, dt: datetime.datetime) -> bool:
        return self.created_date < dt
    def is_newer_than(self, dt: datetime.datetime) -> bool:
        return self.created_date > dt
    def to_json_read(self) -> str:
        return json.dumps(self.to_read_dict())


@dataclass(frozen=False)
class calendar_event_group_read_dto(base_read_dto, calendar_event_group_write_dto):
    calendar_event_group_uid: str
    calendar_event_group_name: str
    client_uid: str
    account_uid: str
    calendar_account_uid: str
    calendar_event_type_uid: str
    group_comment: str
    event_start_date: datetime.datetime
    event_end_date: datetime.datetime
    is_approved: int
    row_instance: str
    row_lock: str | None
    row_owner: str
    row_seq: int
    row_guid: str
    row_version: int
    is_active: int
    created_date: datetime.datetime
    created_by: str
    last_updated_date: datetime.datetime
    last_updated_by: str
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str
    def __init__(self, calendar_event_group_uid: str, calendar_event_group_name: str, client_uid: str, account_uid: str, calendar_account_uid: str, calendar_event_type_uid: str, group_comment: str, event_start_date: datetime.datetime, event_end_date: datetime.datetime, is_approved: int, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
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
    @classmethod
    def empty_read(cls):
        return cls(0, "", "", "", "", "", "", "", datetime.datetime.now(), datetime.datetime.now(), 0, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def default_read(cls):
        return cls(0, base_dto.get_random_uid(), "", "", "", "", "", "", datetime.datetime.now(), datetime.datetime.now(), 0, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def random_read(cls):
        return cls(0, base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), datetime.datetime.now(), datetime.datetime.now(), 0, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_default(cls, calendar_event_group_uid: str, calendar_event_group_name: str, client_uid: str, account_uid: str, calendar_account_uid: str, calendar_event_type_uid: str, group_comment: str, event_start_date: datetime.datetime, event_end_date: datetime.datetime, is_approved: int):
        return cls(0, calendar_event_group_uid, calendar_event_group_name, client_uid, account_uid, calendar_account_uid, calendar_event_type_uid, group_comment, event_start_date, event_end_date, is_approved, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_full(cls, calendar_event_group_uid: str, calendar_event_group_name: str, client_uid: str, account_uid: str, calendar_account_uid: str, calendar_event_type_uid: str, group_comment: str, event_start_date: datetime.datetime, event_end_date: datetime.datetime, is_approved: int, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
        return cls(calendar_event_group_uid, calendar_event_group_name, client_uid, account_uid, calendar_account_uid, calendar_event_type_uid, group_comment, event_start_date, event_end_date, is_approved, row_instance, row_lock, row_owner, row_seq, row_guid, row_version, is_active, created_date, created_by, last_updated_date, last_updated_by, removed_date, removed_by, custom_attributes)
    @classmethod
    def from_write(cls, dto: calendar_event_group_write_dto):
        return cls(0, dto.calendar_event_group_uid, dto.calendar_event_group_name, dto.client_uid, dto.account_uid, dto.calendar_account_uid, dto.calendar_event_type_uid, dto.group_comment, dto.event_start_date, dto.event_end_date, dto.is_approved, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, dto.custom_attributes)
    def clone_read(self):
        return calendar_event_group_read_dto(self.calendar_event_group_uid, self.calendar_event_group_name, self.client_uid, self.account_uid, self.calendar_account_uid, self.calendar_event_type_uid, self.group_comment, self.event_start_date, self.event_end_date, self.is_approved, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes)
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["calendar_event_group_uid"], d["calendar_event_group_name"], d["client_uid"], d["account_uid"], d["calendar_account_uid"], d["calendar_event_type_uid"], d["group_comment"], d["event_start_date"], d["event_end_date"], d["is_approved"], d["row_instance"], d["row_lock"], d["row_owner"], d["row_seq"], d["row_guid"], d["row_version"], d["is_active"], d["created_date"], d["created_by"], d["last_updated_date"], d["last_updated_by"], d["removed_date"], d["removed_by"], d["custom_attributes"])
    def to_read_dict(self) -> dict:
        return asdict(self)
    def to_write(self) -> calendar_event_group_write_dto:
        return calendar_event_group_write_dto(self.calendar_event_group_uid, self.calendar_event_group_name, self.client_uid, self.account_uid, self.calendar_account_uid, self.calendar_event_type_uid, self.group_comment, self.event_start_date, self.event_end_date, self.is_approved, self.custom_attributes)
    def to_thin(self) -> calendar_event_group_thin_dto:
        return calendar_event_group_thin_dto(self.calendar_event_group_uid, self.calendar_event_group_name, self.created_date, self.is_active)
    def touch(self, updated_by: str = "system"):
        self.last_updated_date = datetime.datetime.now()
        self.last_updated_by = updated_by
        self.row_version = self.row_version+1
    def get_list_all_values(self) -> list[any]:
        return [self.calendar_event_group_uid, self.calendar_event_group_name, self.client_uid, self.account_uid, self.calendar_account_uid, self.calendar_event_type_uid, self.group_comment, self.event_start_date, self.event_end_date, self.is_approved, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]
    def get_list_update_values(self, updated_by: str) -> list[any]:
        return [self.calendar_event_group_name, self.client_uid, self.account_uid, self.calendar_account_uid, self.calendar_event_type_uid, self.group_comment, self.event_start_date, self.event_end_date, self.is_approved, self.custom_attributes, updated_by, self.calendar_event_group_uid]
    def is_older_than(self, dt: datetime.datetime) -> bool:
        return self.created_date < dt
    def is_newer_than(self, dt: datetime.datetime) -> bool:
        return self.created_date > dt
    def to_json_read(self) -> str:
        return json.dumps(self.to_read_dict())


@dataclass(frozen=False)
class calendar_event_type_read_dto(base_read_dto, calendar_event_type_write_dto):
    calendar_event_type_uid: str
    calendar_event_type_name: str
    client_uid: str
    calendar_type_uid: str
    auto_approved: int
    row_instance: str
    row_lock: str | None
    row_owner: str
    row_seq: int
    row_guid: str
    row_version: int
    is_active: int
    created_date: datetime.datetime
    created_by: str
    last_updated_date: datetime.datetime
    last_updated_by: str
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str
    def __init__(self, calendar_event_type_uid: str, calendar_event_type_name: str, client_uid: str, calendar_type_uid: str, auto_approved: int, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
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
    @classmethod
    def empty_read(cls):
        return cls(0, "", "", "", "", 0, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def default_read(cls):
        return cls(0, base_dto.get_random_uid(), "", "", "", 0, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def random_read(cls):
        return cls(0, base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), 0, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_default(cls, calendar_event_type_uid: str, calendar_event_type_name: str, client_uid: str, calendar_type_uid: str, auto_approved: int):
        return cls(0, calendar_event_type_uid, calendar_event_type_name, client_uid, calendar_type_uid, auto_approved, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_full(cls, calendar_event_type_uid: str, calendar_event_type_name: str, client_uid: str, calendar_type_uid: str, auto_approved: int, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
        return cls(calendar_event_type_uid, calendar_event_type_name, client_uid, calendar_type_uid, auto_approved, row_instance, row_lock, row_owner, row_seq, row_guid, row_version, is_active, created_date, created_by, last_updated_date, last_updated_by, removed_date, removed_by, custom_attributes)
    @classmethod
    def from_write(cls, dto: calendar_event_type_write_dto):
        return cls(0, dto.calendar_event_type_uid, dto.calendar_event_type_name, dto.client_uid, dto.calendar_type_uid, dto.auto_approved, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, dto.custom_attributes)
    def clone_read(self):
        return calendar_event_type_read_dto(self.calendar_event_type_uid, self.calendar_event_type_name, self.client_uid, self.calendar_type_uid, self.auto_approved, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes)
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["calendar_event_type_uid"], d["calendar_event_type_name"], d["client_uid"], d["calendar_type_uid"], d["auto_approved"], d["row_instance"], d["row_lock"], d["row_owner"], d["row_seq"], d["row_guid"], d["row_version"], d["is_active"], d["created_date"], d["created_by"], d["last_updated_date"], d["last_updated_by"], d["removed_date"], d["removed_by"], d["custom_attributes"])
    def to_read_dict(self) -> dict:
        return asdict(self)
    def to_write(self) -> calendar_event_type_write_dto:
        return calendar_event_type_write_dto(self.calendar_event_type_uid, self.calendar_event_type_name, self.client_uid, self.calendar_type_uid, self.auto_approved, self.custom_attributes)
    def to_thin(self) -> calendar_event_type_thin_dto:
        return calendar_event_type_thin_dto(self.calendar_event_type_uid, self.calendar_event_type_name, self.created_date, self.is_active)
    def touch(self, updated_by: str = "system"):
        self.last_updated_date = datetime.datetime.now()
        self.last_updated_by = updated_by
        self.row_version = self.row_version+1
    def get_list_all_values(self) -> list[any]:
        return [self.calendar_event_type_uid, self.calendar_event_type_name, self.client_uid, self.calendar_type_uid, self.auto_approved, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]
    def get_list_update_values(self, updated_by: str) -> list[any]:
        return [self.calendar_event_type_name, self.client_uid, self.calendar_type_uid, self.auto_approved, self.custom_attributes, updated_by, self.calendar_event_type_uid]
    def is_older_than(self, dt: datetime.datetime) -> bool:
        return self.created_date < dt
    def is_newer_than(self, dt: datetime.datetime) -> bool:
        return self.created_date > dt
    def to_json_read(self) -> str:
        return json.dumps(self.to_read_dict())


@dataclass(frozen=False)
class calendar_type_read_dto(base_read_dto, calendar_type_write_dto):
    calendar_type_uid: str
    calendar_type_name: str
    row_instance: str
    row_seq: int
    row_guid: str
    row_version: int
    is_active: int
    created_date: datetime.datetime
    created_by: str
    last_updated_date: datetime.datetime
    last_updated_by: str
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str
    def __init__(self, calendar_type_uid: str, calendar_type_name: str, row_instance: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
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
    @classmethod
    def empty_read(cls):
        return cls(0, "", "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def default_read(cls):
        return cls(0, base_dto.get_random_uid(), "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def random_read(cls):
        return cls(0, base_dto.get_random_uid(), base_dto.get_random_uid(), "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_default(cls, calendar_type_uid: str, calendar_type_name: str):
        return cls(0, calendar_type_uid, calendar_type_name, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_full(cls, calendar_type_uid: str, calendar_type_name: str, row_instance: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
        return cls(calendar_type_uid, calendar_type_name, row_instance, row_seq, row_guid, row_version, is_active, created_date, created_by, last_updated_date, last_updated_by, removed_date, removed_by, custom_attributes)
    @classmethod
    def from_write(cls, dto: calendar_type_write_dto):
        return cls(0, dto.calendar_type_uid, dto.calendar_type_name, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, dto.custom_attributes)
    def clone_read(self):
        return calendar_type_read_dto(self.calendar_type_uid, self.calendar_type_name, self.row_instance, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes)
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["calendar_type_uid"], d["calendar_type_name"], d["row_instance"], d["row_seq"], d["row_guid"], d["row_version"], d["is_active"], d["created_date"], d["created_by"], d["last_updated_date"], d["last_updated_by"], d["removed_date"], d["removed_by"], d["custom_attributes"])
    def to_read_dict(self) -> dict:
        return asdict(self)
    def to_write(self) -> calendar_type_write_dto:
        return calendar_type_write_dto(self.calendar_type_uid, self.calendar_type_name, self.custom_attributes)
    def to_thin(self) -> calendar_type_thin_dto:
        return calendar_type_thin_dto(self.calendar_type_uid, self.calendar_type_name, self.created_date, self.is_active)
    def touch(self, updated_by: str = "system"):
        self.last_updated_date = datetime.datetime.now()
        self.last_updated_by = updated_by
        self.row_version = self.row_version+1
    def get_list_all_values(self) -> list[any]:
        return [self.calendar_type_uid, self.calendar_type_name, self.row_instance, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]
    def get_list_update_values(self, updated_by: str) -> list[any]:
        return [self.calendar_type_name, self.custom_attributes, updated_by, self.calendar_type_uid]
    def is_older_than(self, dt: datetime.datetime) -> bool:
        return self.created_date < dt
    def is_newer_than(self, dt: datetime.datetime) -> bool:
        return self.created_date > dt
    def to_json_read(self) -> str:
        return json.dumps(self.to_read_dict())


@dataclass(frozen=False)
class client_read_dto(base_read_dto, client_write_dto):
    client_uid: str
    client_name: str
    tenant_uid: str
    country_uid: str
    client_type_uid: str
    client_category_uid: str
    account_uid: str | None
    client_code: str
    client_description: str
    start_date: datetime.datetime
    end_date: datetime.datetime | None
    is_internal: int
    is_system: int
    is_test: int
    row_instance: str
    row_lock: str | None
    row_owner: str
    row_seq: int
    row_guid: str
    row_version: int
    is_active: int
    created_date: datetime.datetime
    created_by: str
    last_updated_date: datetime.datetime
    last_updated_by: str
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str
    def __init__(self, client_uid: str, client_name: str, tenant_uid: str, country_uid: str, client_type_uid: str, client_category_uid: str, account_uid: str | None, client_code: str, client_description: str, start_date: datetime.datetime, end_date: datetime.datetime | None, is_internal: int, is_system: int, is_test: int, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
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
    @classmethod
    def empty_read(cls):
        return cls(0, "", "", "", "", "", "", "", "", "", datetime.datetime.now(), datetime.datetime.now(), 0, 0, 0, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def default_read(cls):
        return cls(0, base_dto.get_random_uid(), "", "", "", "", "", "", "", "", datetime.datetime.now(), datetime.datetime.now(), 0, 0, 0, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def random_read(cls):
        return cls(0, base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), datetime.datetime.now(), datetime.datetime.now(), 0, 0, 0, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_default(cls, client_uid: str, client_name: str, tenant_uid: str, country_uid: str, client_type_uid: str, client_category_uid: str, account_uid: str | None, client_code: str, client_description: str, start_date: datetime.datetime, end_date: datetime.datetime | None, is_internal: int, is_system: int, is_test: int):
        return cls(0, client_uid, client_name, tenant_uid, country_uid, client_type_uid, client_category_uid, account_uid, client_code, client_description, start_date, end_date, is_internal, is_system, is_test, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_full(cls, client_uid: str, client_name: str, tenant_uid: str, country_uid: str, client_type_uid: str, client_category_uid: str, account_uid: str | None, client_code: str, client_description: str, start_date: datetime.datetime, end_date: datetime.datetime | None, is_internal: int, is_system: int, is_test: int, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
        return cls(client_uid, client_name, tenant_uid, country_uid, client_type_uid, client_category_uid, account_uid, client_code, client_description, start_date, end_date, is_internal, is_system, is_test, row_instance, row_lock, row_owner, row_seq, row_guid, row_version, is_active, created_date, created_by, last_updated_date, last_updated_by, removed_date, removed_by, custom_attributes)
    @classmethod
    def from_write(cls, dto: client_write_dto):
        return cls(0, dto.client_uid, dto.client_name, dto.tenant_uid, dto.country_uid, dto.client_type_uid, dto.client_category_uid, dto.account_uid, dto.client_code, dto.client_description, dto.start_date, dto.end_date, dto.is_internal, dto.is_system, dto.is_test, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, dto.custom_attributes)
    def clone_read(self):
        return client_read_dto(self.client_uid, self.client_name, self.tenant_uid, self.country_uid, self.client_type_uid, self.client_category_uid, self.account_uid, self.client_code, self.client_description, self.start_date, self.end_date, self.is_internal, self.is_system, self.is_test, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes)
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["client_uid"], d["client_name"], d["tenant_uid"], d["country_uid"], d["client_type_uid"], d["client_category_uid"], d["account_uid"], d["client_code"], d["client_description"], d["start_date"], d["end_date"], d["is_internal"], d["is_system"], d["is_test"], d["row_instance"], d["row_lock"], d["row_owner"], d["row_seq"], d["row_guid"], d["row_version"], d["is_active"], d["created_date"], d["created_by"], d["last_updated_date"], d["last_updated_by"], d["removed_date"], d["removed_by"], d["custom_attributes"])
    def to_read_dict(self) -> dict:
        return asdict(self)
    def to_write(self) -> client_write_dto:
        return client_write_dto(self.client_uid, self.client_name, self.tenant_uid, self.country_uid, self.client_type_uid, self.client_category_uid, self.account_uid, self.client_code, self.client_description, self.start_date, self.end_date, self.is_internal, self.is_system, self.is_test, self.custom_attributes)
    def to_thin(self) -> client_thin_dto:
        return client_thin_dto(self.client_uid, self.client_name, self.created_date, self.is_active)
    def touch(self, updated_by: str = "system"):
        self.last_updated_date = datetime.datetime.now()
        self.last_updated_by = updated_by
        self.row_version = self.row_version+1
    def get_list_all_values(self) -> list[any]:
        return [self.client_uid, self.client_name, self.tenant_uid, self.country_uid, self.client_type_uid, self.client_category_uid, self.account_uid, self.client_code, self.client_description, self.start_date, self.end_date, self.is_internal, self.is_system, self.is_test, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]
    def get_list_update_values(self, updated_by: str) -> list[any]:
        return [self.client_name, self.tenant_uid, self.country_uid, self.client_type_uid, self.client_category_uid, self.account_uid, self.client_code, self.client_description, self.start_date, self.end_date, self.is_internal, self.is_system, self.is_test, self.custom_attributes, updated_by, self.client_uid]
    def is_older_than(self, dt: datetime.datetime) -> bool:
        return self.created_date < dt
    def is_newer_than(self, dt: datetime.datetime) -> bool:
        return self.created_date > dt
    def to_json_read(self) -> str:
        return json.dumps(self.to_read_dict())


@dataclass(frozen=False)
class client_account_read_dto(base_read_dto, client_account_write_dto):
    client_account_uid: str
    client_account_name: str
    tenant_uid: str
    client_uid: str
    account_uid: str
    client_role_uid: str
    role_comment: str
    row_instance: str
    row_lock: str | None
    row_owner: str
    row_seq: int
    row_guid: str
    row_version: int
    is_active: int
    created_date: datetime.datetime
    created_by: str
    last_updated_date: datetime.datetime
    last_updated_by: str
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str
    def __init__(self, client_account_uid: str, client_account_name: str, tenant_uid: str, client_uid: str, account_uid: str, client_role_uid: str, role_comment: str, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
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
    @classmethod
    def empty_read(cls):
        return cls(0, "", "", "", "", "", "", "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def default_read(cls):
        return cls(0, base_dto.get_random_uid(), "", "", "", "", "", "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def random_read(cls):
        return cls(0, base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_default(cls, client_account_uid: str, client_account_name: str, tenant_uid: str, client_uid: str, account_uid: str, client_role_uid: str, role_comment: str):
        return cls(0, client_account_uid, client_account_name, tenant_uid, client_uid, account_uid, client_role_uid, role_comment, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_full(cls, client_account_uid: str, client_account_name: str, tenant_uid: str, client_uid: str, account_uid: str, client_role_uid: str, role_comment: str, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
        return cls(client_account_uid, client_account_name, tenant_uid, client_uid, account_uid, client_role_uid, role_comment, row_instance, row_lock, row_owner, row_seq, row_guid, row_version, is_active, created_date, created_by, last_updated_date, last_updated_by, removed_date, removed_by, custom_attributes)
    @classmethod
    def from_write(cls, dto: client_account_write_dto):
        return cls(0, dto.client_account_uid, dto.client_account_name, dto.tenant_uid, dto.client_uid, dto.account_uid, dto.client_role_uid, dto.role_comment, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, dto.custom_attributes)
    def clone_read(self):
        return client_account_read_dto(self.client_account_uid, self.client_account_name, self.tenant_uid, self.client_uid, self.account_uid, self.client_role_uid, self.role_comment, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes)
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["client_account_uid"], d["client_account_name"], d["tenant_uid"], d["client_uid"], d["account_uid"], d["client_role_uid"], d["role_comment"], d["row_instance"], d["row_lock"], d["row_owner"], d["row_seq"], d["row_guid"], d["row_version"], d["is_active"], d["created_date"], d["created_by"], d["last_updated_date"], d["last_updated_by"], d["removed_date"], d["removed_by"], d["custom_attributes"])
    def to_read_dict(self) -> dict:
        return asdict(self)
    def to_write(self) -> client_account_write_dto:
        return client_account_write_dto(self.client_account_uid, self.client_account_name, self.tenant_uid, self.client_uid, self.account_uid, self.client_role_uid, self.role_comment, self.custom_attributes)
    def to_thin(self) -> client_account_thin_dto:
        return client_account_thin_dto(self.client_account_uid, self.client_account_name, self.created_date, self.is_active)
    def touch(self, updated_by: str = "system"):
        self.last_updated_date = datetime.datetime.now()
        self.last_updated_by = updated_by
        self.row_version = self.row_version+1
    def get_list_all_values(self) -> list[any]:
        return [self.client_account_uid, self.client_account_name, self.tenant_uid, self.client_uid, self.account_uid, self.client_role_uid, self.role_comment, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]
    def get_list_update_values(self, updated_by: str) -> list[any]:
        return [self.client_account_name, self.tenant_uid, self.client_uid, self.account_uid, self.client_role_uid, self.role_comment, self.custom_attributes, updated_by, self.client_account_uid]
    def is_older_than(self, dt: datetime.datetime) -> bool:
        return self.created_date < dt
    def is_newer_than(self, dt: datetime.datetime) -> bool:
        return self.created_date > dt
    def to_json_read(self) -> str:
        return json.dumps(self.to_read_dict())


@dataclass(frozen=False)
class client_country_read_dto(base_read_dto, client_country_write_dto):
    client_country_uid: str
    client_country_name: str
    tenant_uid: str
    client_uid: str
    country_uid: str
    country_priority: int
    country_comment: str
    row_instance: str
    row_lock: str | None
    row_owner: str
    row_seq: int
    row_guid: str
    row_version: int
    is_active: int
    created_date: datetime.datetime
    created_by: str
    last_updated_date: datetime.datetime
    last_updated_by: str
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str
    def __init__(self, client_country_uid: str, client_country_name: str, tenant_uid: str, client_uid: str, country_uid: str, country_priority: int, country_comment: str, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
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
    @classmethod
    def empty_read(cls):
        return cls(0, "", "", "", "", "", 0, "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def default_read(cls):
        return cls(0, base_dto.get_random_uid(), "", "", "", "", 0, "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def random_read(cls):
        return cls(0, base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), 0, base_dto.get_random_uid(), "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_default(cls, client_country_uid: str, client_country_name: str, tenant_uid: str, client_uid: str, country_uid: str, country_priority: int, country_comment: str):
        return cls(0, client_country_uid, client_country_name, tenant_uid, client_uid, country_uid, country_priority, country_comment, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_full(cls, client_country_uid: str, client_country_name: str, tenant_uid: str, client_uid: str, country_uid: str, country_priority: int, country_comment: str, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
        return cls(client_country_uid, client_country_name, tenant_uid, client_uid, country_uid, country_priority, country_comment, row_instance, row_lock, row_owner, row_seq, row_guid, row_version, is_active, created_date, created_by, last_updated_date, last_updated_by, removed_date, removed_by, custom_attributes)
    @classmethod
    def from_write(cls, dto: client_country_write_dto):
        return cls(0, dto.client_country_uid, dto.client_country_name, dto.tenant_uid, dto.client_uid, dto.country_uid, dto.country_priority, dto.country_comment, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, dto.custom_attributes)
    def clone_read(self):
        return client_country_read_dto(self.client_country_uid, self.client_country_name, self.tenant_uid, self.client_uid, self.country_uid, self.country_priority, self.country_comment, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes)
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["client_country_uid"], d["client_country_name"], d["tenant_uid"], d["client_uid"], d["country_uid"], d["country_priority"], d["country_comment"], d["row_instance"], d["row_lock"], d["row_owner"], d["row_seq"], d["row_guid"], d["row_version"], d["is_active"], d["created_date"], d["created_by"], d["last_updated_date"], d["last_updated_by"], d["removed_date"], d["removed_by"], d["custom_attributes"])
    def to_read_dict(self) -> dict:
        return asdict(self)
    def to_write(self) -> client_country_write_dto:
        return client_country_write_dto(self.client_country_uid, self.client_country_name, self.tenant_uid, self.client_uid, self.country_uid, self.country_priority, self.country_comment, self.custom_attributes)
    def to_thin(self) -> client_country_thin_dto:
        return client_country_thin_dto(self.client_country_uid, self.client_country_name, self.created_date, self.is_active)
    def touch(self, updated_by: str = "system"):
        self.last_updated_date = datetime.datetime.now()
        self.last_updated_by = updated_by
        self.row_version = self.row_version+1
    def get_list_all_values(self) -> list[any]:
        return [self.client_country_uid, self.client_country_name, self.tenant_uid, self.client_uid, self.country_uid, self.country_priority, self.country_comment, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]
    def get_list_update_values(self, updated_by: str) -> list[any]:
        return [self.client_country_name, self.tenant_uid, self.client_uid, self.country_uid, self.country_priority, self.country_comment, self.custom_attributes, updated_by, self.client_country_uid]
    def is_older_than(self, dt: datetime.datetime) -> bool:
        return self.created_date < dt
    def is_newer_than(self, dt: datetime.datetime) -> bool:
        return self.created_date > dt
    def to_json_read(self) -> str:
        return json.dumps(self.to_read_dict())


@dataclass(frozen=False)
class client_payment_read_dto(base_read_dto, client_payment_write_dto):
    client_payment_uid: str
    client_payment_name: str
    tenant_uid: str
    client_uid: str
    account_uid: str
    currency_uid: str
    start_date: datetime.datetime
    end_date: datetime.datetime | None
    payment_value: str
    payment_type: str
    source_number: str
    source_reference: str
    is_approved: int
    row_instance: str
    row_lock: str | None
    row_owner: str
    row_seq: int
    row_guid: str
    row_version: int
    is_active: int
    created_date: datetime.datetime
    created_by: str
    last_updated_date: datetime.datetime
    last_updated_by: str
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str
    def __init__(self, client_payment_uid: str, client_payment_name: str, tenant_uid: str, client_uid: str, account_uid: str, currency_uid: str, start_date: datetime.datetime, end_date: datetime.datetime | None, payment_value: str, payment_type: str, source_number: str, source_reference: str, is_approved: int, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
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
    @classmethod
    def empty_read(cls):
        return cls(0, "", "", "", "", "", "", datetime.datetime.now(), datetime.datetime.now(), "", "", "", "", 0, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def default_read(cls):
        return cls(0, base_dto.get_random_uid(), "", "", "", "", "", datetime.datetime.now(), datetime.datetime.now(), "", "", "", "", 0, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def random_read(cls):
        return cls(0, base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), datetime.datetime.now(), datetime.datetime.now(), "", base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), 0, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_default(cls, client_payment_uid: str, client_payment_name: str, tenant_uid: str, client_uid: str, account_uid: str, currency_uid: str, start_date: datetime.datetime, end_date: datetime.datetime | None, payment_value: str, payment_type: str, source_number: str, source_reference: str, is_approved: int):
        return cls(0, client_payment_uid, client_payment_name, tenant_uid, client_uid, account_uid, currency_uid, start_date, end_date, payment_value, payment_type, source_number, source_reference, is_approved, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_full(cls, client_payment_uid: str, client_payment_name: str, tenant_uid: str, client_uid: str, account_uid: str, currency_uid: str, start_date: datetime.datetime, end_date: datetime.datetime | None, payment_value: str, payment_type: str, source_number: str, source_reference: str, is_approved: int, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
        return cls(client_payment_uid, client_payment_name, tenant_uid, client_uid, account_uid, currency_uid, start_date, end_date, payment_value, payment_type, source_number, source_reference, is_approved, row_instance, row_lock, row_owner, row_seq, row_guid, row_version, is_active, created_date, created_by, last_updated_date, last_updated_by, removed_date, removed_by, custom_attributes)
    @classmethod
    def from_write(cls, dto: client_payment_write_dto):
        return cls(0, dto.client_payment_uid, dto.client_payment_name, dto.tenant_uid, dto.client_uid, dto.account_uid, dto.currency_uid, dto.start_date, dto.end_date, dto.payment_value, dto.payment_type, dto.source_number, dto.source_reference, dto.is_approved, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, dto.custom_attributes)
    def clone_read(self):
        return client_payment_read_dto(self.client_payment_uid, self.client_payment_name, self.tenant_uid, self.client_uid, self.account_uid, self.currency_uid, self.start_date, self.end_date, self.payment_value, self.payment_type, self.source_number, self.source_reference, self.is_approved, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes)
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["client_payment_uid"], d["client_payment_name"], d["tenant_uid"], d["client_uid"], d["account_uid"], d["currency_uid"], d["start_date"], d["end_date"], d["payment_value"], d["payment_type"], d["source_number"], d["source_reference"], d["is_approved"], d["row_instance"], d["row_lock"], d["row_owner"], d["row_seq"], d["row_guid"], d["row_version"], d["is_active"], d["created_date"], d["created_by"], d["last_updated_date"], d["last_updated_by"], d["removed_date"], d["removed_by"], d["custom_attributes"])
    def to_read_dict(self) -> dict:
        return asdict(self)
    def to_write(self) -> client_payment_write_dto:
        return client_payment_write_dto(self.client_payment_uid, self.client_payment_name, self.tenant_uid, self.client_uid, self.account_uid, self.currency_uid, self.start_date, self.end_date, self.payment_value, self.payment_type, self.source_number, self.source_reference, self.is_approved, self.custom_attributes)
    def to_thin(self) -> client_payment_thin_dto:
        return client_payment_thin_dto(self.client_payment_uid, self.client_payment_name, self.created_date, self.is_active)
    def touch(self, updated_by: str = "system"):
        self.last_updated_date = datetime.datetime.now()
        self.last_updated_by = updated_by
        self.row_version = self.row_version+1
    def get_list_all_values(self) -> list[any]:
        return [self.client_payment_uid, self.client_payment_name, self.tenant_uid, self.client_uid, self.account_uid, self.currency_uid, self.start_date, self.end_date, self.payment_value, self.payment_type, self.source_number, self.source_reference, self.is_approved, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]
    def get_list_update_values(self, updated_by: str) -> list[any]:
        return [self.client_payment_name, self.tenant_uid, self.client_uid, self.account_uid, self.currency_uid, self.start_date, self.end_date, self.payment_value, self.payment_type, self.source_number, self.source_reference, self.is_approved, self.custom_attributes, updated_by, self.client_payment_uid]
    def is_older_than(self, dt: datetime.datetime) -> bool:
        return self.created_date < dt
    def is_newer_than(self, dt: datetime.datetime) -> bool:
        return self.created_date > dt
    def to_json_read(self) -> str:
        return json.dumps(self.to_read_dict())


@dataclass(frozen=False)
class client_role_read_dto(base_read_dto, client_role_write_dto):
    client_role_uid: str
    client_role_name: str
    role_description: str
    row_instance: str
    row_lock: str | None
    row_owner: str
    row_seq: int
    row_guid: str
    row_version: int
    is_active: int
    created_date: datetime.datetime
    created_by: str
    last_updated_date: datetime.datetime
    last_updated_by: str
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str
    def __init__(self, client_role_uid: str, client_role_name: str, role_description: str, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
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
    @classmethod
    def empty_read(cls):
        return cls(0, "", "", "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def default_read(cls):
        return cls(0, base_dto.get_random_uid(), "", "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def random_read(cls):
        return cls(0, base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_default(cls, client_role_uid: str, client_role_name: str, role_description: str):
        return cls(0, client_role_uid, client_role_name, role_description, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_full(cls, client_role_uid: str, client_role_name: str, role_description: str, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
        return cls(client_role_uid, client_role_name, role_description, row_instance, row_lock, row_owner, row_seq, row_guid, row_version, is_active, created_date, created_by, last_updated_date, last_updated_by, removed_date, removed_by, custom_attributes)
    @classmethod
    def from_write(cls, dto: client_role_write_dto):
        return cls(0, dto.client_role_uid, dto.client_role_name, dto.role_description, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, dto.custom_attributes)
    def clone_read(self):
        return client_role_read_dto(self.client_role_uid, self.client_role_name, self.role_description, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes)
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["client_role_uid"], d["client_role_name"], d["role_description"], d["row_instance"], d["row_lock"], d["row_owner"], d["row_seq"], d["row_guid"], d["row_version"], d["is_active"], d["created_date"], d["created_by"], d["last_updated_date"], d["last_updated_by"], d["removed_date"], d["removed_by"], d["custom_attributes"])
    def to_read_dict(self) -> dict:
        return asdict(self)
    def to_write(self) -> client_role_write_dto:
        return client_role_write_dto(self.client_role_uid, self.client_role_name, self.role_description, self.custom_attributes)
    def to_thin(self) -> client_role_thin_dto:
        return client_role_thin_dto(self.client_role_uid, self.client_role_name, self.created_date, self.is_active)
    def touch(self, updated_by: str = "system"):
        self.last_updated_date = datetime.datetime.now()
        self.last_updated_by = updated_by
        self.row_version = self.row_version+1
    def get_list_all_values(self) -> list[any]:
        return [self.client_role_uid, self.client_role_name, self.role_description, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]
    def get_list_update_values(self, updated_by: str) -> list[any]:
        return [self.client_role_name, self.role_description, self.custom_attributes, updated_by, self.client_role_uid]
    def is_older_than(self, dt: datetime.datetime) -> bool:
        return self.created_date < dt
    def is_newer_than(self, dt: datetime.datetime) -> bool:
        return self.created_date > dt
    def to_json_read(self) -> str:
        return json.dumps(self.to_read_dict())


@dataclass(frozen=False)
class client_status_read_dto(base_read_dto, client_status_write_dto):
    client_status_uid: str
    client_status_name: str
    client_status_description: str
    row_instance: str
    row_lock: str | None
    row_owner: str
    row_seq: int
    row_guid: str
    row_version: int
    is_active: int
    created_date: datetime.datetime
    created_by: str
    last_updated_date: datetime.datetime
    last_updated_by: str
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str
    def __init__(self, client_status_uid: str, client_status_name: str, client_status_description: str, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
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
    @classmethod
    def empty_read(cls):
        return cls(0, "", "", "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def default_read(cls):
        return cls(0, base_dto.get_random_uid(), "", "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def random_read(cls):
        return cls(0, base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_default(cls, client_status_uid: str, client_status_name: str, client_status_description: str):
        return cls(0, client_status_uid, client_status_name, client_status_description, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_full(cls, client_status_uid: str, client_status_name: str, client_status_description: str, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
        return cls(client_status_uid, client_status_name, client_status_description, row_instance, row_lock, row_owner, row_seq, row_guid, row_version, is_active, created_date, created_by, last_updated_date, last_updated_by, removed_date, removed_by, custom_attributes)
    @classmethod
    def from_write(cls, dto: client_status_write_dto):
        return cls(0, dto.client_status_uid, dto.client_status_name, dto.client_status_description, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, dto.custom_attributes)
    def clone_read(self):
        return client_status_read_dto(self.client_status_uid, self.client_status_name, self.client_status_description, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes)
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["client_status_uid"], d["client_status_name"], d["client_status_description"], d["row_instance"], d["row_lock"], d["row_owner"], d["row_seq"], d["row_guid"], d["row_version"], d["is_active"], d["created_date"], d["created_by"], d["last_updated_date"], d["last_updated_by"], d["removed_date"], d["removed_by"], d["custom_attributes"])
    def to_read_dict(self) -> dict:
        return asdict(self)
    def to_write(self) -> client_status_write_dto:
        return client_status_write_dto(self.client_status_uid, self.client_status_name, self.client_status_description, self.custom_attributes)
    def to_thin(self) -> client_status_thin_dto:
        return client_status_thin_dto(self.client_status_uid, self.client_status_name, self.created_date, self.is_active)
    def touch(self, updated_by: str = "system"):
        self.last_updated_date = datetime.datetime.now()
        self.last_updated_by = updated_by
        self.row_version = self.row_version+1
    def get_list_all_values(self) -> list[any]:
        return [self.client_status_uid, self.client_status_name, self.client_status_description, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]
    def get_list_update_values(self, updated_by: str) -> list[any]:
        return [self.client_status_name, self.client_status_description, self.custom_attributes, updated_by, self.client_status_uid]
    def is_older_than(self, dt: datetime.datetime) -> bool:
        return self.created_date < dt
    def is_newer_than(self, dt: datetime.datetime) -> bool:
        return self.created_date > dt
    def to_json_read(self) -> str:
        return json.dumps(self.to_read_dict())


@dataclass(frozen=False)
class client_type_read_dto(base_read_dto, client_type_write_dto):
    client_type_uid: str
    client_type_name: str
    client_type_description: str
    row_instance: str
    row_lock: str | None
    row_owner: str
    row_seq: int
    row_guid: str
    row_version: int
    is_active: int
    created_date: datetime.datetime
    created_by: str
    last_updated_date: datetime.datetime
    last_updated_by: str
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str
    def __init__(self, client_type_uid: str, client_type_name: str, client_type_description: str, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
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
    @classmethod
    def empty_read(cls):
        return cls(0, "", "", "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def default_read(cls):
        return cls(0, base_dto.get_random_uid(), "", "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def random_read(cls):
        return cls(0, base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_default(cls, client_type_uid: str, client_type_name: str, client_type_description: str):
        return cls(0, client_type_uid, client_type_name, client_type_description, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_full(cls, client_type_uid: str, client_type_name: str, client_type_description: str, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
        return cls(client_type_uid, client_type_name, client_type_description, row_instance, row_lock, row_owner, row_seq, row_guid, row_version, is_active, created_date, created_by, last_updated_date, last_updated_by, removed_date, removed_by, custom_attributes)
    @classmethod
    def from_write(cls, dto: client_type_write_dto):
        return cls(0, dto.client_type_uid, dto.client_type_name, dto.client_type_description, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, dto.custom_attributes)
    def clone_read(self):
        return client_type_read_dto(self.client_type_uid, self.client_type_name, self.client_type_description, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes)
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["client_type_uid"], d["client_type_name"], d["client_type_description"], d["row_instance"], d["row_lock"], d["row_owner"], d["row_seq"], d["row_guid"], d["row_version"], d["is_active"], d["created_date"], d["created_by"], d["last_updated_date"], d["last_updated_by"], d["removed_date"], d["removed_by"], d["custom_attributes"])
    def to_read_dict(self) -> dict:
        return asdict(self)
    def to_write(self) -> client_type_write_dto:
        return client_type_write_dto(self.client_type_uid, self.client_type_name, self.client_type_description, self.custom_attributes)
    def to_thin(self) -> client_type_thin_dto:
        return client_type_thin_dto(self.client_type_uid, self.client_type_name, self.created_date, self.is_active)
    def touch(self, updated_by: str = "system"):
        self.last_updated_date = datetime.datetime.now()
        self.last_updated_by = updated_by
        self.row_version = self.row_version+1
    def get_list_all_values(self) -> list[any]:
        return [self.client_type_uid, self.client_type_name, self.client_type_description, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]
    def get_list_update_values(self, updated_by: str) -> list[any]:
        return [self.client_type_name, self.client_type_description, self.custom_attributes, updated_by, self.client_type_uid]
    def is_older_than(self, dt: datetime.datetime) -> bool:
        return self.created_date < dt
    def is_newer_than(self, dt: datetime.datetime) -> bool:
        return self.created_date > dt
    def to_json_read(self) -> str:
        return json.dumps(self.to_read_dict())


@dataclass(frozen=False)
class connection_engine_read_dto(base_read_dto, connection_engine_write_dto):
    connection_engine_uid: str
    connection_engine_name: str
    start_date: datetime.datetime | None
    calls_count: int
    last_time: int
    host_count: int
    user_count: int
    token_count: int
    row_instance: str
    row_lock: str | None
    row_owner: str
    row_seq: int
    row_guid: str
    row_version: int
    is_active: int
    created_date: datetime.datetime
    created_by: str
    last_updated_date: datetime.datetime
    last_updated_by: str
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str
    def __init__(self, connection_engine_uid: str, connection_engine_name: str, start_date: datetime.datetime | None, calls_count: int, last_time: int, host_count: int, user_count: int, token_count: int, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
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
    @classmethod
    def empty_read(cls):
        return cls(0, "", "", datetime.datetime.now(), 0, 0, 0, 0, 0, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def default_read(cls):
        return cls(0, base_dto.get_random_uid(), "", datetime.datetime.now(), 0, 0, 0, 0, 0, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def random_read(cls):
        return cls(0, base_dto.get_random_uid(), base_dto.get_random_uid(), datetime.datetime.now(), 0, 0, 0, 0, 0, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_default(cls, connection_engine_uid: str, connection_engine_name: str, start_date: datetime.datetime | None, calls_count: int, last_time: int, host_count: int, user_count: int, token_count: int):
        return cls(0, connection_engine_uid, connection_engine_name, start_date, calls_count, last_time, host_count, user_count, token_count, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_full(cls, connection_engine_uid: str, connection_engine_name: str, start_date: datetime.datetime | None, calls_count: int, last_time: int, host_count: int, user_count: int, token_count: int, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
        return cls(connection_engine_uid, connection_engine_name, start_date, calls_count, last_time, host_count, user_count, token_count, row_instance, row_lock, row_owner, row_seq, row_guid, row_version, is_active, created_date, created_by, last_updated_date, last_updated_by, removed_date, removed_by, custom_attributes)
    @classmethod
    def from_write(cls, dto: connection_engine_write_dto):
        return cls(0, dto.connection_engine_uid, dto.connection_engine_name, dto.start_date, dto.calls_count, dto.last_time, dto.host_count, dto.user_count, dto.token_count, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, dto.custom_attributes)
    def clone_read(self):
        return connection_engine_read_dto(self.connection_engine_uid, self.connection_engine_name, self.start_date, self.calls_count, self.last_time, self.host_count, self.user_count, self.token_count, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes)
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["connection_engine_uid"], d["connection_engine_name"], d["start_date"], d["calls_count"], d["last_time"], d["host_count"], d["user_count"], d["token_count"], d["row_instance"], d["row_lock"], d["row_owner"], d["row_seq"], d["row_guid"], d["row_version"], d["is_active"], d["created_date"], d["created_by"], d["last_updated_date"], d["last_updated_by"], d["removed_date"], d["removed_by"], d["custom_attributes"])
    def to_read_dict(self) -> dict:
        return asdict(self)
    def to_write(self) -> connection_engine_write_dto:
        return connection_engine_write_dto(self.connection_engine_uid, self.connection_engine_name, self.start_date, self.calls_count, self.last_time, self.host_count, self.user_count, self.token_count, self.custom_attributes)
    def to_thin(self) -> connection_engine_thin_dto:
        return connection_engine_thin_dto(self.connection_engine_uid, self.connection_engine_name, self.created_date, self.is_active)
    def touch(self, updated_by: str = "system"):
        self.last_updated_date = datetime.datetime.now()
        self.last_updated_by = updated_by
        self.row_version = self.row_version+1
    def get_list_all_values(self) -> list[any]:
        return [self.connection_engine_uid, self.connection_engine_name, self.start_date, self.calls_count, self.last_time, self.host_count, self.user_count, self.token_count, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]
    def get_list_update_values(self, updated_by: str) -> list[any]:
        return [self.connection_engine_name, self.start_date, self.calls_count, self.last_time, self.host_count, self.user_count, self.token_count, self.custom_attributes, updated_by, self.connection_engine_uid]
    def is_older_than(self, dt: datetime.datetime) -> bool:
        return self.created_date < dt
    def is_newer_than(self, dt: datetime.datetime) -> bool:
        return self.created_date > dt
    def to_json_read(self) -> str:
        return json.dumps(self.to_read_dict())


@dataclass(frozen=False)
class connection_host_read_dto(base_read_dto, connection_host_write_dto):
    connection_host_uid: str
    connection_host_name: str
    connection_engine_uid: str
    host_ip: str
    calls_count: int | None
    start_time: int
    last_call_time: int
    user_count: int
    token_count: int
    row_instance: str
    row_lock: str | None
    row_owner: str
    row_seq: int
    row_guid: str
    row_version: int
    is_active: int
    created_date: datetime.datetime
    created_by: str
    last_updated_date: datetime.datetime
    last_updated_by: str
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str
    def __init__(self, connection_host_uid: str, connection_host_name: str, connection_engine_uid: str, host_ip: str, calls_count: int | None, start_time: int, last_call_time: int, user_count: int, token_count: int, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
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
    @classmethod
    def empty_read(cls):
        return cls(0, "", "", "", "", 0, 0, 0, 0, 0, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def default_read(cls):
        return cls(0, base_dto.get_random_uid(), "", "", "", 0, 0, 0, 0, 0, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def random_read(cls):
        return cls(0, base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), 0, 0, 0, 0, 0, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_default(cls, connection_host_uid: str, connection_host_name: str, connection_engine_uid: str, host_ip: str, calls_count: int | None, start_time: int, last_call_time: int, user_count: int, token_count: int):
        return cls(0, connection_host_uid, connection_host_name, connection_engine_uid, host_ip, calls_count, start_time, last_call_time, user_count, token_count, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_full(cls, connection_host_uid: str, connection_host_name: str, connection_engine_uid: str, host_ip: str, calls_count: int | None, start_time: int, last_call_time: int, user_count: int, token_count: int, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
        return cls(connection_host_uid, connection_host_name, connection_engine_uid, host_ip, calls_count, start_time, last_call_time, user_count, token_count, row_instance, row_lock, row_owner, row_seq, row_guid, row_version, is_active, created_date, created_by, last_updated_date, last_updated_by, removed_date, removed_by, custom_attributes)
    @classmethod
    def from_write(cls, dto: connection_host_write_dto):
        return cls(0, dto.connection_host_uid, dto.connection_host_name, dto.connection_engine_uid, dto.host_ip, dto.calls_count, dto.start_time, dto.last_call_time, dto.user_count, dto.token_count, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, dto.custom_attributes)
    def clone_read(self):
        return connection_host_read_dto(self.connection_host_uid, self.connection_host_name, self.connection_engine_uid, self.host_ip, self.calls_count, self.start_time, self.last_call_time, self.user_count, self.token_count, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes)
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["connection_host_uid"], d["connection_host_name"], d["connection_engine_uid"], d["host_ip"], d["calls_count"], d["start_time"], d["last_call_time"], d["user_count"], d["token_count"], d["row_instance"], d["row_lock"], d["row_owner"], d["row_seq"], d["row_guid"], d["row_version"], d["is_active"], d["created_date"], d["created_by"], d["last_updated_date"], d["last_updated_by"], d["removed_date"], d["removed_by"], d["custom_attributes"])
    def to_read_dict(self) -> dict:
        return asdict(self)
    def to_write(self) -> connection_host_write_dto:
        return connection_host_write_dto(self.connection_host_uid, self.connection_host_name, self.connection_engine_uid, self.host_ip, self.calls_count, self.start_time, self.last_call_time, self.user_count, self.token_count, self.custom_attributes)
    def to_thin(self) -> connection_host_thin_dto:
        return connection_host_thin_dto(self.connection_host_uid, self.connection_host_name, self.created_date, self.is_active)
    def touch(self, updated_by: str = "system"):
        self.last_updated_date = datetime.datetime.now()
        self.last_updated_by = updated_by
        self.row_version = self.row_version+1
    def get_list_all_values(self) -> list[any]:
        return [self.connection_host_uid, self.connection_host_name, self.connection_engine_uid, self.host_ip, self.calls_count, self.start_time, self.last_call_time, self.user_count, self.token_count, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]
    def get_list_update_values(self, updated_by: str) -> list[any]:
        return [self.connection_host_name, self.connection_engine_uid, self.host_ip, self.calls_count, self.start_time, self.last_call_time, self.user_count, self.token_count, self.custom_attributes, updated_by, self.connection_host_uid]
    def is_older_than(self, dt: datetime.datetime) -> bool:
        return self.created_date < dt
    def is_newer_than(self, dt: datetime.datetime) -> bool:
        return self.created_date > dt
    def to_json_read(self) -> str:
        return json.dumps(self.to_read_dict())


@dataclass(frozen=False)
class connection_tenant_read_dto(base_read_dto, connection_tenant_write_dto):
    connection_tenant_uid: str
    connection_tenant_name: str
    tenant_uid: str
    calls_count: int
    items_count: int
    request_size: int
    response_size: int
    row_instance: str
    row_lock: str | None
    row_owner: str
    row_seq: int
    row_guid: str
    row_version: int
    is_active: int
    created_date: datetime.datetime
    created_by: str
    last_updated_date: datetime.datetime
    last_updated_by: str
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str
    def __init__(self, connection_tenant_uid: str, connection_tenant_name: str, tenant_uid: str, calls_count: int, items_count: int, request_size: int, response_size: int, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
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
    @classmethod
    def empty_read(cls):
        return cls(0, "", "", "", 0, 0, 0, 0, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def default_read(cls):
        return cls(0, base_dto.get_random_uid(), "", "", 0, 0, 0, 0, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def random_read(cls):
        return cls(0, base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), 0, 0, 0, 0, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_default(cls, connection_tenant_uid: str, connection_tenant_name: str, tenant_uid: str, calls_count: int, items_count: int, request_size: int, response_size: int):
        return cls(0, connection_tenant_uid, connection_tenant_name, tenant_uid, calls_count, items_count, request_size, response_size, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_full(cls, connection_tenant_uid: str, connection_tenant_name: str, tenant_uid: str, calls_count: int, items_count: int, request_size: int, response_size: int, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
        return cls(connection_tenant_uid, connection_tenant_name, tenant_uid, calls_count, items_count, request_size, response_size, row_instance, row_lock, row_owner, row_seq, row_guid, row_version, is_active, created_date, created_by, last_updated_date, last_updated_by, removed_date, removed_by, custom_attributes)
    @classmethod
    def from_write(cls, dto: connection_tenant_write_dto):
        return cls(0, dto.connection_tenant_uid, dto.connection_tenant_name, dto.tenant_uid, dto.calls_count, dto.items_count, dto.request_size, dto.response_size, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, dto.custom_attributes)
    def clone_read(self):
        return connection_tenant_read_dto(self.connection_tenant_uid, self.connection_tenant_name, self.tenant_uid, self.calls_count, self.items_count, self.request_size, self.response_size, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes)
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["connection_tenant_uid"], d["connection_tenant_name"], d["tenant_uid"], d["calls_count"], d["items_count"], d["request_size"], d["response_size"], d["row_instance"], d["row_lock"], d["row_owner"], d["row_seq"], d["row_guid"], d["row_version"], d["is_active"], d["created_date"], d["created_by"], d["last_updated_date"], d["last_updated_by"], d["removed_date"], d["removed_by"], d["custom_attributes"])
    def to_read_dict(self) -> dict:
        return asdict(self)
    def to_write(self) -> connection_tenant_write_dto:
        return connection_tenant_write_dto(self.connection_tenant_uid, self.connection_tenant_name, self.tenant_uid, self.calls_count, self.items_count, self.request_size, self.response_size, self.custom_attributes)
    def to_thin(self) -> connection_tenant_thin_dto:
        return connection_tenant_thin_dto(self.connection_tenant_uid, self.connection_tenant_name, self.created_date, self.is_active)
    def touch(self, updated_by: str = "system"):
        self.last_updated_date = datetime.datetime.now()
        self.last_updated_by = updated_by
        self.row_version = self.row_version+1
    def get_list_all_values(self) -> list[any]:
        return [self.connection_tenant_uid, self.connection_tenant_name, self.tenant_uid, self.calls_count, self.items_count, self.request_size, self.response_size, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]
    def get_list_update_values(self, updated_by: str) -> list[any]:
        return [self.connection_tenant_name, self.tenant_uid, self.calls_count, self.items_count, self.request_size, self.response_size, self.custom_attributes, updated_by, self.connection_tenant_uid]
    def is_older_than(self, dt: datetime.datetime) -> bool:
        return self.created_date < dt
    def is_newer_than(self, dt: datetime.datetime) -> bool:
        return self.created_date > dt
    def to_json_read(self) -> str:
        return json.dumps(self.to_read_dict())


@dataclass(frozen=False)
class connection_user_read_dto(base_read_dto, connection_user_write_dto):
    connection_user_uid: str
    connection_user_name: str
    connection_engine_uid: str
    account_uid: str
    call_count: int
    host_count: int
    token_count: int
    row_instance: str
    row_lock: str | None
    row_owner: str
    row_seq: int
    row_guid: str
    row_version: int
    is_active: int
    created_date: datetime.datetime
    created_by: str
    last_updated_date: datetime.datetime
    last_updated_by: str
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str
    def __init__(self, connection_user_uid: str, connection_user_name: str, connection_engine_uid: str, account_uid: str, call_count: int, host_count: int, token_count: int, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
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
    @classmethod
    def empty_read(cls):
        return cls(0, "", "", "", "", 0, 0, 0, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def default_read(cls):
        return cls(0, base_dto.get_random_uid(), "", "", "", 0, 0, 0, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def random_read(cls):
        return cls(0, base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), 0, 0, 0, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_default(cls, connection_user_uid: str, connection_user_name: str, connection_engine_uid: str, account_uid: str, call_count: int, host_count: int, token_count: int):
        return cls(0, connection_user_uid, connection_user_name, connection_engine_uid, account_uid, call_count, host_count, token_count, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_full(cls, connection_user_uid: str, connection_user_name: str, connection_engine_uid: str, account_uid: str, call_count: int, host_count: int, token_count: int, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
        return cls(connection_user_uid, connection_user_name, connection_engine_uid, account_uid, call_count, host_count, token_count, row_instance, row_lock, row_owner, row_seq, row_guid, row_version, is_active, created_date, created_by, last_updated_date, last_updated_by, removed_date, removed_by, custom_attributes)
    @classmethod
    def from_write(cls, dto: connection_user_write_dto):
        return cls(0, dto.connection_user_uid, dto.connection_user_name, dto.connection_engine_uid, dto.account_uid, dto.call_count, dto.host_count, dto.token_count, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, dto.custom_attributes)
    def clone_read(self):
        return connection_user_read_dto(self.connection_user_uid, self.connection_user_name, self.connection_engine_uid, self.account_uid, self.call_count, self.host_count, self.token_count, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes)
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["connection_user_uid"], d["connection_user_name"], d["connection_engine_uid"], d["account_uid"], d["call_count"], d["host_count"], d["token_count"], d["row_instance"], d["row_lock"], d["row_owner"], d["row_seq"], d["row_guid"], d["row_version"], d["is_active"], d["created_date"], d["created_by"], d["last_updated_date"], d["last_updated_by"], d["removed_date"], d["removed_by"], d["custom_attributes"])
    def to_read_dict(self) -> dict:
        return asdict(self)
    def to_write(self) -> connection_user_write_dto:
        return connection_user_write_dto(self.connection_user_uid, self.connection_user_name, self.connection_engine_uid, self.account_uid, self.call_count, self.host_count, self.token_count, self.custom_attributes)
    def to_thin(self) -> connection_user_thin_dto:
        return connection_user_thin_dto(self.connection_user_uid, self.connection_user_name, self.created_date, self.is_active)
    def touch(self, updated_by: str = "system"):
        self.last_updated_date = datetime.datetime.now()
        self.last_updated_by = updated_by
        self.row_version = self.row_version+1
    def get_list_all_values(self) -> list[any]:
        return [self.connection_user_uid, self.connection_user_name, self.connection_engine_uid, self.account_uid, self.call_count, self.host_count, self.token_count, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]
    def get_list_update_values(self, updated_by: str) -> list[any]:
        return [self.connection_user_name, self.connection_engine_uid, self.account_uid, self.call_count, self.host_count, self.token_count, self.custom_attributes, updated_by, self.connection_user_uid]
    def is_older_than(self, dt: datetime.datetime) -> bool:
        return self.created_date < dt
    def is_newer_than(self, dt: datetime.datetime) -> bool:
        return self.created_date > dt
    def to_json_read(self) -> str:
        return json.dumps(self.to_read_dict())


@dataclass(frozen=False)
class country_read_dto(base_read_dto, country_write_dto):
    country_uid: str
    country_name: str
    continent_name: str
    continent_code: str
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
    row_instance: str
    row_lock: str | None
    row_owner: str
    row_seq: int
    row_guid: str
    row_version: int
    is_active: int
    created_date: datetime.datetime
    created_by: str
    last_updated_date: datetime.datetime
    last_updated_by: str
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str
    def __init__(self, country_uid: str, country_name: str, continent_name: str, continent_code: str, country_iso3: str, country_code: str, phone_code: str, currency_code: str, capital_name: str, region_name: str, subregion_name: str, region_code: str, latitude: str, longitude: str, currency_name: str, population: str, languages: str, area: str, bar_code: str, top_level_domain: str, is_focused: int, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
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
    @classmethod
    def empty_read(cls):
        return cls(0, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", 0, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def default_read(cls):
        return cls(0, base_dto.get_random_uid(), "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", 0, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def random_read(cls):
        return cls(0, base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), 0, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_default(cls, country_uid: str, country_name: str, continent_name: str, continent_code: str, country_iso3: str, country_code: str, phone_code: str, currency_code: str, capital_name: str, region_name: str, subregion_name: str, region_code: str, latitude: str, longitude: str, currency_name: str, population: str, languages: str, area: str, bar_code: str, top_level_domain: str, is_focused: int):
        return cls(0, country_uid, country_name, continent_name, continent_code, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain, is_focused, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_full(cls, country_uid: str, country_name: str, continent_name: str, continent_code: str, country_iso3: str, country_code: str, phone_code: str, currency_code: str, capital_name: str, region_name: str, subregion_name: str, region_code: str, latitude: str, longitude: str, currency_name: str, population: str, languages: str, area: str, bar_code: str, top_level_domain: str, is_focused: int, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
        return cls(country_uid, country_name, continent_name, continent_code, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain, is_focused, row_instance, row_lock, row_owner, row_seq, row_guid, row_version, is_active, created_date, created_by, last_updated_date, last_updated_by, removed_date, removed_by, custom_attributes)
    @classmethod
    def from_write(cls, dto: country_write_dto):
        return cls(0, dto.country_uid, dto.country_name, dto.continent_name, dto.continent_code, dto.country_iso3, dto.country_code, dto.phone_code, dto.currency_code, dto.capital_name, dto.region_name, dto.subregion_name, dto.region_code, dto.latitude, dto.longitude, dto.currency_name, dto.population, dto.languages, dto.area, dto.bar_code, dto.top_level_domain, dto.is_focused, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, dto.custom_attributes)
    def clone_read(self):
        return country_read_dto(self.country_uid, self.country_name, self.continent_name, self.continent_code, self.country_iso3, self.country_code, self.phone_code, self.currency_code, self.capital_name, self.region_name, self.subregion_name, self.region_code, self.latitude, self.longitude, self.currency_name, self.population, self.languages, self.area, self.bar_code, self.top_level_domain, self.is_focused, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes)
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["country_uid"], d["country_name"], d["continent_name"], d["continent_code"], d["country_iso3"], d["country_code"], d["phone_code"], d["currency_code"], d["capital_name"], d["region_name"], d["subregion_name"], d["region_code"], d["latitude"], d["longitude"], d["currency_name"], d["population"], d["languages"], d["area"], d["bar_code"], d["top_level_domain"], d["is_focused"], d["row_instance"], d["row_lock"], d["row_owner"], d["row_seq"], d["row_guid"], d["row_version"], d["is_active"], d["created_date"], d["created_by"], d["last_updated_date"], d["last_updated_by"], d["removed_date"], d["removed_by"], d["custom_attributes"])
    def to_read_dict(self) -> dict:
        return asdict(self)
    def to_write(self) -> country_write_dto:
        return country_write_dto(self.country_uid, self.country_name, self.continent_name, self.continent_code, self.country_iso3, self.country_code, self.phone_code, self.currency_code, self.capital_name, self.region_name, self.subregion_name, self.region_code, self.latitude, self.longitude, self.currency_name, self.population, self.languages, self.area, self.bar_code, self.top_level_domain, self.is_focused, self.custom_attributes)
    def to_thin(self) -> country_thin_dto:
        return country_thin_dto(self.country_uid, self.country_name, self.created_date, self.is_active)
    def touch(self, updated_by: str = "system"):
        self.last_updated_date = datetime.datetime.now()
        self.last_updated_by = updated_by
        self.row_version = self.row_version+1
    def get_list_all_values(self) -> list[any]:
        return [self.country_uid, self.country_name, self.continent_name, self.continent_code, self.country_iso3, self.country_code, self.phone_code, self.currency_code, self.capital_name, self.region_name, self.subregion_name, self.region_code, self.latitude, self.longitude, self.currency_name, self.population, self.languages, self.area, self.bar_code, self.top_level_domain, self.is_focused, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]
    def get_list_update_values(self, updated_by: str) -> list[any]:
        return [self.country_name, self.continent_name, self.continent_code, self.country_iso3, self.country_code, self.phone_code, self.currency_code, self.capital_name, self.region_name, self.subregion_name, self.region_code, self.latitude, self.longitude, self.currency_name, self.population, self.languages, self.area, self.bar_code, self.top_level_domain, self.is_focused, self.custom_attributes, updated_by, self.country_uid]
    def is_older_than(self, dt: datetime.datetime) -> bool:
        return self.created_date < dt
    def is_newer_than(self, dt: datetime.datetime) -> bool:
        return self.created_date > dt
    def to_json_read(self) -> str:
        return json.dumps(self.to_read_dict())


@dataclass(frozen=False)
class currency_read_dto(base_read_dto, currency_write_dto):
    currency_uid: str
    currency_name: str
    is_focused: int
    priority: int
    row_instance: str
    row_lock: str | None
    row_owner: str
    row_seq: int
    row_guid: str
    row_version: int
    is_active: int
    created_date: datetime.datetime
    created_by: str
    last_updated_date: datetime.datetime
    last_updated_by: str
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str
    def __init__(self, currency_uid: str, currency_name: str, is_focused: int, priority: int, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
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
    @classmethod
    def empty_read(cls):
        return cls(0, "", "", 0, 0, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def default_read(cls):
        return cls(0, base_dto.get_random_uid(), "", 0, 0, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def random_read(cls):
        return cls(0, base_dto.get_random_uid(), base_dto.get_random_uid(), 0, 0, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_default(cls, currency_uid: str, currency_name: str, is_focused: int, priority: int):
        return cls(0, currency_uid, currency_name, is_focused, priority, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_full(cls, currency_uid: str, currency_name: str, is_focused: int, priority: int, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
        return cls(currency_uid, currency_name, is_focused, priority, row_instance, row_lock, row_owner, row_seq, row_guid, row_version, is_active, created_date, created_by, last_updated_date, last_updated_by, removed_date, removed_by, custom_attributes)
    @classmethod
    def from_write(cls, dto: currency_write_dto):
        return cls(0, dto.currency_uid, dto.currency_name, dto.is_focused, dto.priority, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, dto.custom_attributes)
    def clone_read(self):
        return currency_read_dto(self.currency_uid, self.currency_name, self.is_focused, self.priority, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes)
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["currency_uid"], d["currency_name"], d["is_focused"], d["priority"], d["row_instance"], d["row_lock"], d["row_owner"], d["row_seq"], d["row_guid"], d["row_version"], d["is_active"], d["created_date"], d["created_by"], d["last_updated_date"], d["last_updated_by"], d["removed_date"], d["removed_by"], d["custom_attributes"])
    def to_read_dict(self) -> dict:
        return asdict(self)
    def to_write(self) -> currency_write_dto:
        return currency_write_dto(self.currency_uid, self.currency_name, self.is_focused, self.priority, self.custom_attributes)
    def to_thin(self) -> currency_thin_dto:
        return currency_thin_dto(self.currency_uid, self.currency_name, self.created_date, self.is_active)
    def touch(self, updated_by: str = "system"):
        self.last_updated_date = datetime.datetime.now()
        self.last_updated_by = updated_by
        self.row_version = self.row_version+1
    def get_list_all_values(self) -> list[any]:
        return [self.currency_uid, self.currency_name, self.is_focused, self.priority, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]
    def get_list_update_values(self, updated_by: str) -> list[any]:
        return [self.currency_name, self.is_focused, self.priority, self.custom_attributes, updated_by, self.currency_uid]
    def is_older_than(self, dt: datetime.datetime) -> bool:
        return self.created_date < dt
    def is_newer_than(self, dt: datetime.datetime) -> bool:
        return self.created_date > dt
    def to_json_read(self) -> str:
        return json.dumps(self.to_read_dict())


@dataclass(frozen=False)
class event_acknowledge_read_dto(base_read_dto, event_acknowledge_write_dto):
    event_acknowledge_uid: str
    event_acknowledge_name: str
    event_notification_uid: str
    tenant_uid: str
    account_uid: str
    row_instance: str
    row_lock: str | None
    row_owner: str
    row_seq: int
    row_guid: str
    row_version: int
    is_active: int
    created_date: datetime.datetime
    created_by: str
    last_updated_date: datetime.datetime
    last_updated_by: str
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str
    def __init__(self, event_acknowledge_uid: str, event_acknowledge_name: str, event_notification_uid: str, tenant_uid: str, account_uid: str, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
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
    @classmethod
    def empty_read(cls):
        return cls(0, "", "", "", "", "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def default_read(cls):
        return cls(0, base_dto.get_random_uid(), "", "", "", "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def random_read(cls):
        return cls(0, base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_default(cls, event_acknowledge_uid: str, event_acknowledge_name: str, event_notification_uid: str, tenant_uid: str, account_uid: str):
        return cls(0, event_acknowledge_uid, event_acknowledge_name, event_notification_uid, tenant_uid, account_uid, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_full(cls, event_acknowledge_uid: str, event_acknowledge_name: str, event_notification_uid: str, tenant_uid: str, account_uid: str, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
        return cls(event_acknowledge_uid, event_acknowledge_name, event_notification_uid, tenant_uid, account_uid, row_instance, row_lock, row_owner, row_seq, row_guid, row_version, is_active, created_date, created_by, last_updated_date, last_updated_by, removed_date, removed_by, custom_attributes)
    @classmethod
    def from_write(cls, dto: event_acknowledge_write_dto):
        return cls(0, dto.event_acknowledge_uid, dto.event_acknowledge_name, dto.event_notification_uid, dto.tenant_uid, dto.account_uid, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, dto.custom_attributes)
    def clone_read(self):
        return event_acknowledge_read_dto(self.event_acknowledge_uid, self.event_acknowledge_name, self.event_notification_uid, self.tenant_uid, self.account_uid, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes)
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["event_acknowledge_uid"], d["event_acknowledge_name"], d["event_notification_uid"], d["tenant_uid"], d["account_uid"], d["row_instance"], d["row_lock"], d["row_owner"], d["row_seq"], d["row_guid"], d["row_version"], d["is_active"], d["created_date"], d["created_by"], d["last_updated_date"], d["last_updated_by"], d["removed_date"], d["removed_by"], d["custom_attributes"])
    def to_read_dict(self) -> dict:
        return asdict(self)
    def to_write(self) -> event_acknowledge_write_dto:
        return event_acknowledge_write_dto(self.event_acknowledge_uid, self.event_acknowledge_name, self.event_notification_uid, self.tenant_uid, self.account_uid, self.custom_attributes)
    def to_thin(self) -> event_acknowledge_thin_dto:
        return event_acknowledge_thin_dto(self.event_acknowledge_uid, self.event_acknowledge_name, self.created_date, self.is_active)
    def touch(self, updated_by: str = "system"):
        self.last_updated_date = datetime.datetime.now()
        self.last_updated_by = updated_by
        self.row_version = self.row_version+1
    def get_list_all_values(self) -> list[any]:
        return [self.event_acknowledge_uid, self.event_acknowledge_name, self.event_notification_uid, self.tenant_uid, self.account_uid, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]
    def get_list_update_values(self, updated_by: str) -> list[any]:
        return [self.event_acknowledge_name, self.event_notification_uid, self.tenant_uid, self.account_uid, self.custom_attributes, updated_by, self.event_acknowledge_uid]
    def is_older_than(self, dt: datetime.datetime) -> bool:
        return self.created_date < dt
    def is_newer_than(self, dt: datetime.datetime) -> bool:
        return self.created_date > dt
    def to_json_read(self) -> str:
        return json.dumps(self.to_read_dict())


@dataclass(frozen=False)
class event_channel_read_dto(base_read_dto, event_channel_write_dto):
    event_channel_uid: str
    event_channel_name: str
    event_channel_type_uid: str
    channel_definition: str
    last_status_name: str
    tenant_uid: str
    account_uid: str
    row_instance: str
    row_lock: str | None
    row_owner: str
    row_seq: int
    row_guid: str
    row_version: int
    is_active: int
    created_date: datetime.datetime
    created_by: str
    last_updated_date: datetime.datetime
    last_updated_by: str
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str
    def __init__(self, event_channel_uid: str, event_channel_name: str, event_channel_type_uid: str, channel_definition: str, last_status_name: str, tenant_uid: str, account_uid: str, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
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
    @classmethod
    def empty_read(cls):
        return cls(0, "", "", "", "", "", "", "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def default_read(cls):
        return cls(0, base_dto.get_random_uid(), "", "", "", "", "", "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def random_read(cls):
        return cls(0, base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_default(cls, event_channel_uid: str, event_channel_name: str, event_channel_type_uid: str, channel_definition: str, last_status_name: str, tenant_uid: str, account_uid: str):
        return cls(0, event_channel_uid, event_channel_name, event_channel_type_uid, channel_definition, last_status_name, tenant_uid, account_uid, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_full(cls, event_channel_uid: str, event_channel_name: str, event_channel_type_uid: str, channel_definition: str, last_status_name: str, tenant_uid: str, account_uid: str, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
        return cls(event_channel_uid, event_channel_name, event_channel_type_uid, channel_definition, last_status_name, tenant_uid, account_uid, row_instance, row_lock, row_owner, row_seq, row_guid, row_version, is_active, created_date, created_by, last_updated_date, last_updated_by, removed_date, removed_by, custom_attributes)
    @classmethod
    def from_write(cls, dto: event_channel_write_dto):
        return cls(0, dto.event_channel_uid, dto.event_channel_name, dto.event_channel_type_uid, dto.channel_definition, dto.last_status_name, dto.tenant_uid, dto.account_uid, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, dto.custom_attributes)
    def clone_read(self):
        return event_channel_read_dto(self.event_channel_uid, self.event_channel_name, self.event_channel_type_uid, self.channel_definition, self.last_status_name, self.tenant_uid, self.account_uid, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes)
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["event_channel_uid"], d["event_channel_name"], d["event_channel_type_uid"], d["channel_definition"], d["last_status_name"], d["tenant_uid"], d["account_uid"], d["row_instance"], d["row_lock"], d["row_owner"], d["row_seq"], d["row_guid"], d["row_version"], d["is_active"], d["created_date"], d["created_by"], d["last_updated_date"], d["last_updated_by"], d["removed_date"], d["removed_by"], d["custom_attributes"])
    def to_read_dict(self) -> dict:
        return asdict(self)
    def to_write(self) -> event_channel_write_dto:
        return event_channel_write_dto(self.event_channel_uid, self.event_channel_name, self.event_channel_type_uid, self.channel_definition, self.last_status_name, self.tenant_uid, self.account_uid, self.custom_attributes)
    def to_thin(self) -> event_channel_thin_dto:
        return event_channel_thin_dto(self.event_channel_uid, self.event_channel_name, self.created_date, self.is_active)
    def touch(self, updated_by: str = "system"):
        self.last_updated_date = datetime.datetime.now()
        self.last_updated_by = updated_by
        self.row_version = self.row_version+1
    def get_list_all_values(self) -> list[any]:
        return [self.event_channel_uid, self.event_channel_name, self.event_channel_type_uid, self.channel_definition, self.last_status_name, self.tenant_uid, self.account_uid, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]
    def get_list_update_values(self, updated_by: str) -> list[any]:
        return [self.event_channel_name, self.event_channel_type_uid, self.channel_definition, self.last_status_name, self.tenant_uid, self.account_uid, self.custom_attributes, updated_by, self.event_channel_uid]
    def is_older_than(self, dt: datetime.datetime) -> bool:
        return self.created_date < dt
    def is_newer_than(self, dt: datetime.datetime) -> bool:
        return self.created_date > dt
    def to_json_read(self) -> str:
        return json.dumps(self.to_read_dict())


@dataclass(frozen=False)
class event_channel_type_read_dto(base_read_dto, event_channel_type_write_dto):
    event_channel_type_uid: str
    event_channel_type_name: str
    channel_type_description: str
    row_instance: str
    row_lock: str | None
    row_owner: str
    row_seq: int
    row_guid: str
    row_version: int
    is_active: int
    created_date: datetime.datetime
    created_by: str
    last_updated_date: datetime.datetime
    last_updated_by: str
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str
    def __init__(self, event_channel_type_uid: str, event_channel_type_name: str, channel_type_description: str, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
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
    @classmethod
    def empty_read(cls):
        return cls(0, "", "", "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def default_read(cls):
        return cls(0, base_dto.get_random_uid(), "", "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def random_read(cls):
        return cls(0, base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_default(cls, event_channel_type_uid: str, event_channel_type_name: str, channel_type_description: str):
        return cls(0, event_channel_type_uid, event_channel_type_name, channel_type_description, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_full(cls, event_channel_type_uid: str, event_channel_type_name: str, channel_type_description: str, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
        return cls(event_channel_type_uid, event_channel_type_name, channel_type_description, row_instance, row_lock, row_owner, row_seq, row_guid, row_version, is_active, created_date, created_by, last_updated_date, last_updated_by, removed_date, removed_by, custom_attributes)
    @classmethod
    def from_write(cls, dto: event_channel_type_write_dto):
        return cls(0, dto.event_channel_type_uid, dto.event_channel_type_name, dto.channel_type_description, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, dto.custom_attributes)
    def clone_read(self):
        return event_channel_type_read_dto(self.event_channel_type_uid, self.event_channel_type_name, self.channel_type_description, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes)
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["event_channel_type_uid"], d["event_channel_type_name"], d["channel_type_description"], d["row_instance"], d["row_lock"], d["row_owner"], d["row_seq"], d["row_guid"], d["row_version"], d["is_active"], d["created_date"], d["created_by"], d["last_updated_date"], d["last_updated_by"], d["removed_date"], d["removed_by"], d["custom_attributes"])
    def to_read_dict(self) -> dict:
        return asdict(self)
    def to_write(self) -> event_channel_type_write_dto:
        return event_channel_type_write_dto(self.event_channel_type_uid, self.event_channel_type_name, self.channel_type_description, self.custom_attributes)
    def to_thin(self) -> event_channel_type_thin_dto:
        return event_channel_type_thin_dto(self.event_channel_type_uid, self.event_channel_type_name, self.created_date, self.is_active)
    def touch(self, updated_by: str = "system"):
        self.last_updated_date = datetime.datetime.now()
        self.last_updated_by = updated_by
        self.row_version = self.row_version+1
    def get_list_all_values(self) -> list[any]:
        return [self.event_channel_type_uid, self.event_channel_type_name, self.channel_type_description, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]
    def get_list_update_values(self, updated_by: str) -> list[any]:
        return [self.event_channel_type_name, self.channel_type_description, self.custom_attributes, updated_by, self.event_channel_type_uid]
    def is_older_than(self, dt: datetime.datetime) -> bool:
        return self.created_date < dt
    def is_newer_than(self, dt: datetime.datetime) -> bool:
        return self.created_date > dt
    def to_json_read(self) -> str:
        return json.dumps(self.to_read_dict())


@dataclass(frozen=False)
class event_instance_read_dto(base_read_dto, event_instance_write_dto):
    event_instance_uid: str
    event_instance_name: str
    tenant_uid: str
    event_type: str
    event_object: str
    event_method: str
    event_parameters: str
    event_signature: str
    event_date: datetime.datetime
    published_count: int
    row_instance: str
    row_lock: str | None
    row_owner: str
    row_seq: int
    row_guid: str
    row_version: int
    is_active: int
    created_date: datetime.datetime
    created_by: str
    last_updated_date: datetime.datetime
    last_updated_by: str
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str
    def __init__(self, event_instance_uid: str, event_instance_name: str, tenant_uid: str, event_type: str, event_object: str, event_method: str, event_parameters: str, event_signature: str, event_date: datetime.datetime, published_count: int, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
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
    @classmethod
    def empty_read(cls):
        return cls(0, "", "", "", "", "", "", "", "", datetime.datetime.now(), 0, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def default_read(cls):
        return cls(0, base_dto.get_random_uid(), "", "", "", "", "", "", "", datetime.datetime.now(), 0, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def random_read(cls):
        return cls(0, base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), datetime.datetime.now(), 0, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_default(cls, event_instance_uid: str, event_instance_name: str, tenant_uid: str, event_type: str, event_object: str, event_method: str, event_parameters: str, event_signature: str, event_date: datetime.datetime, published_count: int):
        return cls(0, event_instance_uid, event_instance_name, tenant_uid, event_type, event_object, event_method, event_parameters, event_signature, event_date, published_count, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_full(cls, event_instance_uid: str, event_instance_name: str, tenant_uid: str, event_type: str, event_object: str, event_method: str, event_parameters: str, event_signature: str, event_date: datetime.datetime, published_count: int, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
        return cls(event_instance_uid, event_instance_name, tenant_uid, event_type, event_object, event_method, event_parameters, event_signature, event_date, published_count, row_instance, row_lock, row_owner, row_seq, row_guid, row_version, is_active, created_date, created_by, last_updated_date, last_updated_by, removed_date, removed_by, custom_attributes)
    @classmethod
    def from_write(cls, dto: event_instance_write_dto):
        return cls(0, dto.event_instance_uid, dto.event_instance_name, dto.tenant_uid, dto.event_type, dto.event_object, dto.event_method, dto.event_parameters, dto.event_signature, dto.event_date, dto.published_count, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, dto.custom_attributes)
    def clone_read(self):
        return event_instance_read_dto(self.event_instance_uid, self.event_instance_name, self.tenant_uid, self.event_type, self.event_object, self.event_method, self.event_parameters, self.event_signature, self.event_date, self.published_count, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes)
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["event_instance_uid"], d["event_instance_name"], d["tenant_uid"], d["event_type"], d["event_object"], d["event_method"], d["event_parameters"], d["event_signature"], d["event_date"], d["published_count"], d["row_instance"], d["row_lock"], d["row_owner"], d["row_seq"], d["row_guid"], d["row_version"], d["is_active"], d["created_date"], d["created_by"], d["last_updated_date"], d["last_updated_by"], d["removed_date"], d["removed_by"], d["custom_attributes"])
    def to_read_dict(self) -> dict:
        return asdict(self)
    def to_write(self) -> event_instance_write_dto:
        return event_instance_write_dto(self.event_instance_uid, self.event_instance_name, self.tenant_uid, self.event_type, self.event_object, self.event_method, self.event_parameters, self.event_signature, self.event_date, self.published_count, self.custom_attributes)
    def to_thin(self) -> event_instance_thin_dto:
        return event_instance_thin_dto(self.event_instance_uid, self.event_instance_name, self.created_date, self.is_active)
    def touch(self, updated_by: str = "system"):
        self.last_updated_date = datetime.datetime.now()
        self.last_updated_by = updated_by
        self.row_version = self.row_version+1
    def get_list_all_values(self) -> list[any]:
        return [self.event_instance_uid, self.event_instance_name, self.tenant_uid, self.event_type, self.event_object, self.event_method, self.event_parameters, self.event_signature, self.event_date, self.published_count, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]
    def get_list_update_values(self, updated_by: str) -> list[any]:
        return [self.event_instance_name, self.tenant_uid, self.event_type, self.event_object, self.event_method, self.event_parameters, self.event_signature, self.event_date, self.published_count, self.custom_attributes, updated_by, self.event_instance_uid]
    def is_older_than(self, dt: datetime.datetime) -> bool:
        return self.created_date < dt
    def is_newer_than(self, dt: datetime.datetime) -> bool:
        return self.created_date > dt
    def to_json_read(self) -> str:
        return json.dumps(self.to_read_dict())


@dataclass(frozen=False)
class event_notification_read_dto(base_read_dto, event_notification_write_dto):
    event_notification_uid: str
    event_notification_name: str
    tenant_uid: str
    account_uid: str
    notification_type: str
    notification_topic: str
    notification_format: str
    notification_content: str
    sending_status: str
    row_instance: str
    row_lock: str | None
    row_owner: str
    row_seq: int
    row_guid: str
    row_version: int
    is_active: int
    created_date: datetime.datetime
    created_by: str
    last_updated_date: datetime.datetime
    last_updated_by: str
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str
    def __init__(self, event_notification_uid: str, event_notification_name: str, tenant_uid: str, account_uid: str, notification_type: str, notification_topic: str, notification_format: str, notification_content: str, sending_status: str, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
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
    @classmethod
    def empty_read(cls):
        return cls(0, "", "", "", "", "", "", "", "", "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def default_read(cls):
        return cls(0, base_dto.get_random_uid(), "", "", "", "", "", "", "", "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def random_read(cls):
        return cls(0, base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_default(cls, event_notification_uid: str, event_notification_name: str, tenant_uid: str, account_uid: str, notification_type: str, notification_topic: str, notification_format: str, notification_content: str, sending_status: str):
        return cls(0, event_notification_uid, event_notification_name, tenant_uid, account_uid, notification_type, notification_topic, notification_format, notification_content, sending_status, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_full(cls, event_notification_uid: str, event_notification_name: str, tenant_uid: str, account_uid: str, notification_type: str, notification_topic: str, notification_format: str, notification_content: str, sending_status: str, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
        return cls(event_notification_uid, event_notification_name, tenant_uid, account_uid, notification_type, notification_topic, notification_format, notification_content, sending_status, row_instance, row_lock, row_owner, row_seq, row_guid, row_version, is_active, created_date, created_by, last_updated_date, last_updated_by, removed_date, removed_by, custom_attributes)
    @classmethod
    def from_write(cls, dto: event_notification_write_dto):
        return cls(0, dto.event_notification_uid, dto.event_notification_name, dto.tenant_uid, dto.account_uid, dto.notification_type, dto.notification_topic, dto.notification_format, dto.notification_content, dto.sending_status, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, dto.custom_attributes)
    def clone_read(self):
        return event_notification_read_dto(self.event_notification_uid, self.event_notification_name, self.tenant_uid, self.account_uid, self.notification_type, self.notification_topic, self.notification_format, self.notification_content, self.sending_status, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes)
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["event_notification_uid"], d["event_notification_name"], d["tenant_uid"], d["account_uid"], d["notification_type"], d["notification_topic"], d["notification_format"], d["notification_content"], d["sending_status"], d["row_instance"], d["row_lock"], d["row_owner"], d["row_seq"], d["row_guid"], d["row_version"], d["is_active"], d["created_date"], d["created_by"], d["last_updated_date"], d["last_updated_by"], d["removed_date"], d["removed_by"], d["custom_attributes"])
    def to_read_dict(self) -> dict:
        return asdict(self)
    def to_write(self) -> event_notification_write_dto:
        return event_notification_write_dto(self.event_notification_uid, self.event_notification_name, self.tenant_uid, self.account_uid, self.notification_type, self.notification_topic, self.notification_format, self.notification_content, self.sending_status, self.custom_attributes)
    def to_thin(self) -> event_notification_thin_dto:
        return event_notification_thin_dto(self.event_notification_uid, self.event_notification_name, self.created_date, self.is_active)
    def touch(self, updated_by: str = "system"):
        self.last_updated_date = datetime.datetime.now()
        self.last_updated_by = updated_by
        self.row_version = self.row_version+1
    def get_list_all_values(self) -> list[any]:
        return [self.event_notification_uid, self.event_notification_name, self.tenant_uid, self.account_uid, self.notification_type, self.notification_topic, self.notification_format, self.notification_content, self.sending_status, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]
    def get_list_update_values(self, updated_by: str) -> list[any]:
        return [self.event_notification_name, self.tenant_uid, self.account_uid, self.notification_type, self.notification_topic, self.notification_format, self.notification_content, self.sending_status, self.custom_attributes, updated_by, self.event_notification_uid]
    def is_older_than(self, dt: datetime.datetime) -> bool:
        return self.created_date < dt
    def is_newer_than(self, dt: datetime.datetime) -> bool:
        return self.created_date > dt
    def to_json_read(self) -> str:
        return json.dumps(self.to_read_dict())


@dataclass(frozen=False)
class event_observer_read_dto(base_read_dto, event_observer_write_dto):
    event_observer_uid: str
    event_observer_name: str
    event_observer_definition: str
    action_definition: str
    row_instance: str
    row_lock: str | None
    row_owner: str
    row_seq: int
    row_guid: str
    row_version: int
    is_active: int
    created_date: datetime.datetime
    created_by: str
    last_updated_date: datetime.datetime
    last_updated_by: str
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str
    def __init__(self, event_observer_uid: str, event_observer_name: str, event_observer_definition: str, action_definition: str, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
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
    @classmethod
    def empty_read(cls):
        return cls(0, "", "", "", "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def default_read(cls):
        return cls(0, base_dto.get_random_uid(), "", "", "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def random_read(cls):
        return cls(0, base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_default(cls, event_observer_uid: str, event_observer_name: str, event_observer_definition: str, action_definition: str):
        return cls(0, event_observer_uid, event_observer_name, event_observer_definition, action_definition, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_full(cls, event_observer_uid: str, event_observer_name: str, event_observer_definition: str, action_definition: str, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
        return cls(event_observer_uid, event_observer_name, event_observer_definition, action_definition, row_instance, row_lock, row_owner, row_seq, row_guid, row_version, is_active, created_date, created_by, last_updated_date, last_updated_by, removed_date, removed_by, custom_attributes)
    @classmethod
    def from_write(cls, dto: event_observer_write_dto):
        return cls(0, dto.event_observer_uid, dto.event_observer_name, dto.event_observer_definition, dto.action_definition, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, dto.custom_attributes)
    def clone_read(self):
        return event_observer_read_dto(self.event_observer_uid, self.event_observer_name, self.event_observer_definition, self.action_definition, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes)
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["event_observer_uid"], d["event_observer_name"], d["event_observer_definition"], d["action_definition"], d["row_instance"], d["row_lock"], d["row_owner"], d["row_seq"], d["row_guid"], d["row_version"], d["is_active"], d["created_date"], d["created_by"], d["last_updated_date"], d["last_updated_by"], d["removed_date"], d["removed_by"], d["custom_attributes"])
    def to_read_dict(self) -> dict:
        return asdict(self)
    def to_write(self) -> event_observer_write_dto:
        return event_observer_write_dto(self.event_observer_uid, self.event_observer_name, self.event_observer_definition, self.action_definition, self.custom_attributes)
    def to_thin(self) -> event_observer_thin_dto:
        return event_observer_thin_dto(self.event_observer_uid, self.event_observer_name, self.created_date, self.is_active)
    def touch(self, updated_by: str = "system"):
        self.last_updated_date = datetime.datetime.now()
        self.last_updated_by = updated_by
        self.row_version = self.row_version+1
    def get_list_all_values(self) -> list[any]:
        return [self.event_observer_uid, self.event_observer_name, self.event_observer_definition, self.action_definition, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]
    def get_list_update_values(self, updated_by: str) -> list[any]:
        return [self.event_observer_name, self.event_observer_definition, self.action_definition, self.custom_attributes, updated_by, self.event_observer_uid]
    def is_older_than(self, dt: datetime.datetime) -> bool:
        return self.created_date < dt
    def is_newer_than(self, dt: datetime.datetime) -> bool:
        return self.created_date > dt
    def to_json_read(self) -> str:
        return json.dumps(self.to_read_dict())


@dataclass(frozen=False)
class event_subscription_read_dto(base_read_dto, event_subscription_write_dto):
    event_subscription_uid: str
    event_subscription_name: str
    event_channel_uid: str
    tenant_uid: str
    account_uid: str
    subscription_filter: str
    subscription_topic: str
    subscription_template: str
    row_instance: str
    row_lock: str | None
    row_owner: str
    row_seq: int
    row_guid: str
    row_version: int
    is_active: int
    created_date: datetime.datetime
    created_by: str
    last_updated_date: datetime.datetime
    last_updated_by: str
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str
    def __init__(self, event_subscription_uid: str, event_subscription_name: str, event_channel_uid: str, tenant_uid: str, account_uid: str, subscription_filter: str, subscription_topic: str, subscription_template: str, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
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
    @classmethod
    def empty_read(cls):
        return cls(0, "", "", "", "", "", "", "", "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def default_read(cls):
        return cls(0, base_dto.get_random_uid(), "", "", "", "", "", "", "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def random_read(cls):
        return cls(0, base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_default(cls, event_subscription_uid: str, event_subscription_name: str, event_channel_uid: str, tenant_uid: str, account_uid: str, subscription_filter: str, subscription_topic: str, subscription_template: str):
        return cls(0, event_subscription_uid, event_subscription_name, event_channel_uid, tenant_uid, account_uid, subscription_filter, subscription_topic, subscription_template, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_full(cls, event_subscription_uid: str, event_subscription_name: str, event_channel_uid: str, tenant_uid: str, account_uid: str, subscription_filter: str, subscription_topic: str, subscription_template: str, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
        return cls(event_subscription_uid, event_subscription_name, event_channel_uid, tenant_uid, account_uid, subscription_filter, subscription_topic, subscription_template, row_instance, row_lock, row_owner, row_seq, row_guid, row_version, is_active, created_date, created_by, last_updated_date, last_updated_by, removed_date, removed_by, custom_attributes)
    @classmethod
    def from_write(cls, dto: event_subscription_write_dto):
        return cls(0, dto.event_subscription_uid, dto.event_subscription_name, dto.event_channel_uid, dto.tenant_uid, dto.account_uid, dto.subscription_filter, dto.subscription_topic, dto.subscription_template, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, dto.custom_attributes)
    def clone_read(self):
        return event_subscription_read_dto(self.event_subscription_uid, self.event_subscription_name, self.event_channel_uid, self.tenant_uid, self.account_uid, self.subscription_filter, self.subscription_topic, self.subscription_template, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes)
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["event_subscription_uid"], d["event_subscription_name"], d["event_channel_uid"], d["tenant_uid"], d["account_uid"], d["subscription_filter"], d["subscription_topic"], d["subscription_template"], d["row_instance"], d["row_lock"], d["row_owner"], d["row_seq"], d["row_guid"], d["row_version"], d["is_active"], d["created_date"], d["created_by"], d["last_updated_date"], d["last_updated_by"], d["removed_date"], d["removed_by"], d["custom_attributes"])
    def to_read_dict(self) -> dict:
        return asdict(self)
    def to_write(self) -> event_subscription_write_dto:
        return event_subscription_write_dto(self.event_subscription_uid, self.event_subscription_name, self.event_channel_uid, self.tenant_uid, self.account_uid, self.subscription_filter, self.subscription_topic, self.subscription_template, self.custom_attributes)
    def to_thin(self) -> event_subscription_thin_dto:
        return event_subscription_thin_dto(self.event_subscription_uid, self.event_subscription_name, self.created_date, self.is_active)
    def touch(self, updated_by: str = "system"):
        self.last_updated_date = datetime.datetime.now()
        self.last_updated_by = updated_by
        self.row_version = self.row_version+1
    def get_list_all_values(self) -> list[any]:
        return [self.event_subscription_uid, self.event_subscription_name, self.event_channel_uid, self.tenant_uid, self.account_uid, self.subscription_filter, self.subscription_topic, self.subscription_template, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]
    def get_list_update_values(self, updated_by: str) -> list[any]:
        return [self.event_subscription_name, self.event_channel_uid, self.tenant_uid, self.account_uid, self.subscription_filter, self.subscription_topic, self.subscription_template, self.custom_attributes, updated_by, self.event_subscription_uid]
    def is_older_than(self, dt: datetime.datetime) -> bool:
        return self.created_date < dt
    def is_newer_than(self, dt: datetime.datetime) -> bool:
        return self.created_date > dt
    def to_json_read(self) -> str:
        return json.dumps(self.to_read_dict())


@dataclass(frozen=False)
class event_template_read_dto(base_read_dto, event_template_write_dto):
    event_template_uid: str
    event_template_name: str
    tenant_uid: str
    notification_type: str
    notification_topic: str
    notification_format: str
    row_instance: str
    row_lock: str | None
    row_owner: str
    row_seq: int
    row_guid: str
    row_version: int
    is_active: int
    created_date: datetime.datetime
    created_by: str
    last_updated_date: datetime.datetime
    last_updated_by: str
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str
    def __init__(self, event_template_uid: str, event_template_name: str, tenant_uid: str, notification_type: str, notification_topic: str, notification_format: str, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
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
    @classmethod
    def empty_read(cls):
        return cls(0, "", "", "", "", "", "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def default_read(cls):
        return cls(0, base_dto.get_random_uid(), "", "", "", "", "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def random_read(cls):
        return cls(0, base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_default(cls, event_template_uid: str, event_template_name: str, tenant_uid: str, notification_type: str, notification_topic: str, notification_format: str):
        return cls(0, event_template_uid, event_template_name, tenant_uid, notification_type, notification_topic, notification_format, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_full(cls, event_template_uid: str, event_template_name: str, tenant_uid: str, notification_type: str, notification_topic: str, notification_format: str, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
        return cls(event_template_uid, event_template_name, tenant_uid, notification_type, notification_topic, notification_format, row_instance, row_lock, row_owner, row_seq, row_guid, row_version, is_active, created_date, created_by, last_updated_date, last_updated_by, removed_date, removed_by, custom_attributes)
    @classmethod
    def from_write(cls, dto: event_template_write_dto):
        return cls(0, dto.event_template_uid, dto.event_template_name, dto.tenant_uid, dto.notification_type, dto.notification_topic, dto.notification_format, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, dto.custom_attributes)
    def clone_read(self):
        return event_template_read_dto(self.event_template_uid, self.event_template_name, self.tenant_uid, self.notification_type, self.notification_topic, self.notification_format, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes)
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["event_template_uid"], d["event_template_name"], d["tenant_uid"], d["notification_type"], d["notification_topic"], d["notification_format"], d["row_instance"], d["row_lock"], d["row_owner"], d["row_seq"], d["row_guid"], d["row_version"], d["is_active"], d["created_date"], d["created_by"], d["last_updated_date"], d["last_updated_by"], d["removed_date"], d["removed_by"], d["custom_attributes"])
    def to_read_dict(self) -> dict:
        return asdict(self)
    def to_write(self) -> event_template_write_dto:
        return event_template_write_dto(self.event_template_uid, self.event_template_name, self.tenant_uid, self.notification_type, self.notification_topic, self.notification_format, self.custom_attributes)
    def to_thin(self) -> event_template_thin_dto:
        return event_template_thin_dto(self.event_template_uid, self.event_template_name, self.created_date, self.is_active)
    def touch(self, updated_by: str = "system"):
        self.last_updated_date = datetime.datetime.now()
        self.last_updated_by = updated_by
        self.row_version = self.row_version+1
    def get_list_all_values(self) -> list[any]:
        return [self.event_template_uid, self.event_template_name, self.tenant_uid, self.notification_type, self.notification_topic, self.notification_format, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]
    def get_list_update_values(self, updated_by: str) -> list[any]:
        return [self.event_template_name, self.tenant_uid, self.notification_type, self.notification_topic, self.notification_format, self.custom_attributes, updated_by, self.event_template_uid]
    def is_older_than(self, dt: datetime.datetime) -> bool:
        return self.created_date < dt
    def is_newer_than(self, dt: datetime.datetime) -> bool:
        return self.created_date > dt
    def to_json_read(self) -> str:
        return json.dumps(self.to_read_dict())


@dataclass(frozen=False)
class event_type_read_dto(base_read_dto, event_type_write_dto):
    event_type_uid: str
    event_type_name: str
    event_type_description: str
    row_instance: str
    row_lock: str | None
    row_owner: str
    row_seq: int
    row_guid: str
    row_version: int
    is_active: int
    created_date: datetime.datetime
    created_by: str
    last_updated_date: datetime.datetime
    last_updated_by: str
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str
    def __init__(self, event_type_uid: str, event_type_name: str, event_type_description: str, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
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
    @classmethod
    def empty_read(cls):
        return cls(0, "", "", "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def default_read(cls):
        return cls(0, base_dto.get_random_uid(), "", "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def random_read(cls):
        return cls(0, base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_default(cls, event_type_uid: str, event_type_name: str, event_type_description: str):
        return cls(0, event_type_uid, event_type_name, event_type_description, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_full(cls, event_type_uid: str, event_type_name: str, event_type_description: str, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
        return cls(event_type_uid, event_type_name, event_type_description, row_instance, row_lock, row_owner, row_seq, row_guid, row_version, is_active, created_date, created_by, last_updated_date, last_updated_by, removed_date, removed_by, custom_attributes)
    @classmethod
    def from_write(cls, dto: event_type_write_dto):
        return cls(0, dto.event_type_uid, dto.event_type_name, dto.event_type_description, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, dto.custom_attributes)
    def clone_read(self):
        return event_type_read_dto(self.event_type_uid, self.event_type_name, self.event_type_description, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes)
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["event_type_uid"], d["event_type_name"], d["event_type_description"], d["row_instance"], d["row_lock"], d["row_owner"], d["row_seq"], d["row_guid"], d["row_version"], d["is_active"], d["created_date"], d["created_by"], d["last_updated_date"], d["last_updated_by"], d["removed_date"], d["removed_by"], d["custom_attributes"])
    def to_read_dict(self) -> dict:
        return asdict(self)
    def to_write(self) -> event_type_write_dto:
        return event_type_write_dto(self.event_type_uid, self.event_type_name, self.event_type_description, self.custom_attributes)
    def to_thin(self) -> event_type_thin_dto:
        return event_type_thin_dto(self.event_type_uid, self.event_type_name, self.created_date, self.is_active)
    def touch(self, updated_by: str = "system"):
        self.last_updated_date = datetime.datetime.now()
        self.last_updated_by = updated_by
        self.row_version = self.row_version+1
    def get_list_all_values(self) -> list[any]:
        return [self.event_type_uid, self.event_type_name, self.event_type_description, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]
    def get_list_update_values(self, updated_by: str) -> list[any]:
        return [self.event_type_name, self.event_type_description, self.custom_attributes, updated_by, self.event_type_uid]
    def is_older_than(self, dt: datetime.datetime) -> bool:
        return self.created_date < dt
    def is_newer_than(self, dt: datetime.datetime) -> bool:
        return self.created_date > dt
    def to_json_read(self) -> str:
        return json.dumps(self.to_read_dict())


@dataclass(frozen=False)
class invoice_action_read_dto(base_read_dto, invoice_action_write_dto):
    invoice_action_uid: str
    invoice_action_name: str
    tenant_uid: str
    account_uid: str
    invoice_instance_uid: str
    invoice_action_type_uid: str
    row_instance: str
    row_lock: str | None
    row_owner: str
    row_seq: int
    row_guid: str
    row_version: int
    is_active: int
    created_date: datetime.datetime
    created_by: str
    last_updated_date: datetime.datetime
    last_updated_by: str
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str
    def __init__(self, invoice_action_uid: str, invoice_action_name: str, tenant_uid: str, account_uid: str, invoice_instance_uid: str, invoice_action_type_uid: str, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
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
    @classmethod
    def empty_read(cls):
        return cls(0, "", "", "", "", "", "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def default_read(cls):
        return cls(0, base_dto.get_random_uid(), "", "", "", "", "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def random_read(cls):
        return cls(0, base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_default(cls, invoice_action_uid: str, invoice_action_name: str, tenant_uid: str, account_uid: str, invoice_instance_uid: str, invoice_action_type_uid: str):
        return cls(0, invoice_action_uid, invoice_action_name, tenant_uid, account_uid, invoice_instance_uid, invoice_action_type_uid, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_full(cls, invoice_action_uid: str, invoice_action_name: str, tenant_uid: str, account_uid: str, invoice_instance_uid: str, invoice_action_type_uid: str, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
        return cls(invoice_action_uid, invoice_action_name, tenant_uid, account_uid, invoice_instance_uid, invoice_action_type_uid, row_instance, row_lock, row_owner, row_seq, row_guid, row_version, is_active, created_date, created_by, last_updated_date, last_updated_by, removed_date, removed_by, custom_attributes)
    @classmethod
    def from_write(cls, dto: invoice_action_write_dto):
        return cls(0, dto.invoice_action_uid, dto.invoice_action_name, dto.tenant_uid, dto.account_uid, dto.invoice_instance_uid, dto.invoice_action_type_uid, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, dto.custom_attributes)
    def clone_read(self):
        return invoice_action_read_dto(self.invoice_action_uid, self.invoice_action_name, self.tenant_uid, self.account_uid, self.invoice_instance_uid, self.invoice_action_type_uid, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes)
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["invoice_action_uid"], d["invoice_action_name"], d["tenant_uid"], d["account_uid"], d["invoice_instance_uid"], d["invoice_action_type_uid"], d["row_instance"], d["row_lock"], d["row_owner"], d["row_seq"], d["row_guid"], d["row_version"], d["is_active"], d["created_date"], d["created_by"], d["last_updated_date"], d["last_updated_by"], d["removed_date"], d["removed_by"], d["custom_attributes"])
    def to_read_dict(self) -> dict:
        return asdict(self)
    def to_write(self) -> invoice_action_write_dto:
        return invoice_action_write_dto(self.invoice_action_uid, self.invoice_action_name, self.tenant_uid, self.account_uid, self.invoice_instance_uid, self.invoice_action_type_uid, self.custom_attributes)
    def to_thin(self) -> invoice_action_thin_dto:
        return invoice_action_thin_dto(self.invoice_action_uid, self.invoice_action_name, self.created_date, self.is_active)
    def touch(self, updated_by: str = "system"):
        self.last_updated_date = datetime.datetime.now()
        self.last_updated_by = updated_by
        self.row_version = self.row_version+1
    def get_list_all_values(self) -> list[any]:
        return [self.invoice_action_uid, self.invoice_action_name, self.tenant_uid, self.account_uid, self.invoice_instance_uid, self.invoice_action_type_uid, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]
    def get_list_update_values(self, updated_by: str) -> list[any]:
        return [self.invoice_action_name, self.tenant_uid, self.account_uid, self.invoice_instance_uid, self.invoice_action_type_uid, self.custom_attributes, updated_by, self.invoice_action_uid]
    def is_older_than(self, dt: datetime.datetime) -> bool:
        return self.created_date < dt
    def is_newer_than(self, dt: datetime.datetime) -> bool:
        return self.created_date > dt
    def to_json_read(self) -> str:
        return json.dumps(self.to_read_dict())


@dataclass(frozen=False)
class invoice_action_type_read_dto(base_read_dto, invoice_action_type_write_dto):
    invoice_action_type_uid: str
    invoice_action_type_name: str
    row_instance: str
    row_lock: str | None
    row_owner: str
    row_seq: int
    row_guid: str
    row_version: int
    is_active: int
    created_date: datetime.datetime
    created_by: str
    last_updated_date: datetime.datetime
    last_updated_by: str
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str
    def __init__(self, invoice_action_type_uid: str, invoice_action_type_name: str, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
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
    @classmethod
    def empty_read(cls):
        return cls(0, "", "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def default_read(cls):
        return cls(0, base_dto.get_random_uid(), "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def random_read(cls):
        return cls(0, base_dto.get_random_uid(), base_dto.get_random_uid(), "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_default(cls, invoice_action_type_uid: str, invoice_action_type_name: str):
        return cls(0, invoice_action_type_uid, invoice_action_type_name, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_full(cls, invoice_action_type_uid: str, invoice_action_type_name: str, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
        return cls(invoice_action_type_uid, invoice_action_type_name, row_instance, row_lock, row_owner, row_seq, row_guid, row_version, is_active, created_date, created_by, last_updated_date, last_updated_by, removed_date, removed_by, custom_attributes)
    @classmethod
    def from_write(cls, dto: invoice_action_type_write_dto):
        return cls(0, dto.invoice_action_type_uid, dto.invoice_action_type_name, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, dto.custom_attributes)
    def clone_read(self):
        return invoice_action_type_read_dto(self.invoice_action_type_uid, self.invoice_action_type_name, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes)
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["invoice_action_type_uid"], d["invoice_action_type_name"], d["row_instance"], d["row_lock"], d["row_owner"], d["row_seq"], d["row_guid"], d["row_version"], d["is_active"], d["created_date"], d["created_by"], d["last_updated_date"], d["last_updated_by"], d["removed_date"], d["removed_by"], d["custom_attributes"])
    def to_read_dict(self) -> dict:
        return asdict(self)
    def to_write(self) -> invoice_action_type_write_dto:
        return invoice_action_type_write_dto(self.invoice_action_type_uid, self.invoice_action_type_name, self.custom_attributes)
    def to_thin(self) -> invoice_action_type_thin_dto:
        return invoice_action_type_thin_dto(self.invoice_action_type_uid, self.invoice_action_type_name, self.created_date, self.is_active)
    def touch(self, updated_by: str = "system"):
        self.last_updated_date = datetime.datetime.now()
        self.last_updated_by = updated_by
        self.row_version = self.row_version+1
    def get_list_all_values(self) -> list[any]:
        return [self.invoice_action_type_uid, self.invoice_action_type_name, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]
    def get_list_update_values(self, updated_by: str) -> list[any]:
        return [self.invoice_action_type_name, self.custom_attributes, updated_by, self.invoice_action_type_uid]
    def is_older_than(self, dt: datetime.datetime) -> bool:
        return self.created_date < dt
    def is_newer_than(self, dt: datetime.datetime) -> bool:
        return self.created_date > dt
    def to_json_read(self) -> str:
        return json.dumps(self.to_read_dict())


@dataclass(frozen=False)
class invoice_category_read_dto(base_read_dto, invoice_category_write_dto):
    invoice_category_uid: str
    invoice_category_name: str
    tenant_uid: str
    invoice_category_description: str
    row_instance: str
    row_lock: str | None
    row_owner: str
    row_seq: int
    row_guid: str
    row_version: int
    is_active: int
    created_date: datetime.datetime
    created_by: str
    last_updated_date: datetime.datetime
    last_updated_by: str
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str
    def __init__(self, invoice_category_uid: str, invoice_category_name: str, tenant_uid: str, invoice_category_description: str, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
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
    @classmethod
    def empty_read(cls):
        return cls(0, "", "", "", "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def default_read(cls):
        return cls(0, base_dto.get_random_uid(), "", "", "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def random_read(cls):
        return cls(0, base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_default(cls, invoice_category_uid: str, invoice_category_name: str, tenant_uid: str, invoice_category_description: str):
        return cls(0, invoice_category_uid, invoice_category_name, tenant_uid, invoice_category_description, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_full(cls, invoice_category_uid: str, invoice_category_name: str, tenant_uid: str, invoice_category_description: str, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
        return cls(invoice_category_uid, invoice_category_name, tenant_uid, invoice_category_description, row_instance, row_lock, row_owner, row_seq, row_guid, row_version, is_active, created_date, created_by, last_updated_date, last_updated_by, removed_date, removed_by, custom_attributes)
    @classmethod
    def from_write(cls, dto: invoice_category_write_dto):
        return cls(0, dto.invoice_category_uid, dto.invoice_category_name, dto.tenant_uid, dto.invoice_category_description, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, dto.custom_attributes)
    def clone_read(self):
        return invoice_category_read_dto(self.invoice_category_uid, self.invoice_category_name, self.tenant_uid, self.invoice_category_description, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes)
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["invoice_category_uid"], d["invoice_category_name"], d["tenant_uid"], d["invoice_category_description"], d["row_instance"], d["row_lock"], d["row_owner"], d["row_seq"], d["row_guid"], d["row_version"], d["is_active"], d["created_date"], d["created_by"], d["last_updated_date"], d["last_updated_by"], d["removed_date"], d["removed_by"], d["custom_attributes"])
    def to_read_dict(self) -> dict:
        return asdict(self)
    def to_write(self) -> invoice_category_write_dto:
        return invoice_category_write_dto(self.invoice_category_uid, self.invoice_category_name, self.tenant_uid, self.invoice_category_description, self.custom_attributes)
    def to_thin(self) -> invoice_category_thin_dto:
        return invoice_category_thin_dto(self.invoice_category_uid, self.invoice_category_name, self.created_date, self.is_active)
    def touch(self, updated_by: str = "system"):
        self.last_updated_date = datetime.datetime.now()
        self.last_updated_by = updated_by
        self.row_version = self.row_version+1
    def get_list_all_values(self) -> list[any]:
        return [self.invoice_category_uid, self.invoice_category_name, self.tenant_uid, self.invoice_category_description, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]
    def get_list_update_values(self, updated_by: str) -> list[any]:
        return [self.invoice_category_name, self.tenant_uid, self.invoice_category_description, self.custom_attributes, updated_by, self.invoice_category_uid]
    def is_older_than(self, dt: datetime.datetime) -> bool:
        return self.created_date < dt
    def is_newer_than(self, dt: datetime.datetime) -> bool:
        return self.created_date > dt
    def to_json_read(self) -> str:
        return json.dumps(self.to_read_dict())


@dataclass(frozen=False)
class invoice_entry_read_dto(base_read_dto, invoice_entry_write_dto):
    invoice_entry_uid: str
    invoice_entry_name: str
    tenant_uid: str
    account_uid: str
    invoice_instance_uid: str
    entry_details: str
    entry_amount_net: str
    entry_amount_tax: str
    entry_amount_gross: str
    row_instance: str
    row_lock: str | None
    row_owner: str
    row_seq: int
    row_guid: str
    row_version: int
    is_active: int
    created_date: datetime.datetime
    created_by: str
    last_updated_date: datetime.datetime
    last_updated_by: str
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str
    def __init__(self, invoice_entry_uid: str, invoice_entry_name: str, tenant_uid: str, account_uid: str, invoice_instance_uid: str, entry_details: str, entry_amount_net: str, entry_amount_tax: str, entry_amount_gross: str, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
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
    @classmethod
    def empty_read(cls):
        return cls(0, "", "", "", "", "", "", "", "", "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def default_read(cls):
        return cls(0, base_dto.get_random_uid(), "", "", "", "", "", "", "", "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def random_read(cls):
        return cls(0, base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), "", "", "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_default(cls, invoice_entry_uid: str, invoice_entry_name: str, tenant_uid: str, account_uid: str, invoice_instance_uid: str, entry_details: str, entry_amount_net: str, entry_amount_tax: str, entry_amount_gross: str):
        return cls(0, invoice_entry_uid, invoice_entry_name, tenant_uid, account_uid, invoice_instance_uid, entry_details, entry_amount_net, entry_amount_tax, entry_amount_gross, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_full(cls, invoice_entry_uid: str, invoice_entry_name: str, tenant_uid: str, account_uid: str, invoice_instance_uid: str, entry_details: str, entry_amount_net: str, entry_amount_tax: str, entry_amount_gross: str, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
        return cls(invoice_entry_uid, invoice_entry_name, tenant_uid, account_uid, invoice_instance_uid, entry_details, entry_amount_net, entry_amount_tax, entry_amount_gross, row_instance, row_lock, row_owner, row_seq, row_guid, row_version, is_active, created_date, created_by, last_updated_date, last_updated_by, removed_date, removed_by, custom_attributes)
    @classmethod
    def from_write(cls, dto: invoice_entry_write_dto):
        return cls(0, dto.invoice_entry_uid, dto.invoice_entry_name, dto.tenant_uid, dto.account_uid, dto.invoice_instance_uid, dto.entry_details, dto.entry_amount_net, dto.entry_amount_tax, dto.entry_amount_gross, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, dto.custom_attributes)
    def clone_read(self):
        return invoice_entry_read_dto(self.invoice_entry_uid, self.invoice_entry_name, self.tenant_uid, self.account_uid, self.invoice_instance_uid, self.entry_details, self.entry_amount_net, self.entry_amount_tax, self.entry_amount_gross, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes)
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["invoice_entry_uid"], d["invoice_entry_name"], d["tenant_uid"], d["account_uid"], d["invoice_instance_uid"], d["entry_details"], d["entry_amount_net"], d["entry_amount_tax"], d["entry_amount_gross"], d["row_instance"], d["row_lock"], d["row_owner"], d["row_seq"], d["row_guid"], d["row_version"], d["is_active"], d["created_date"], d["created_by"], d["last_updated_date"], d["last_updated_by"], d["removed_date"], d["removed_by"], d["custom_attributes"])
    def to_read_dict(self) -> dict:
        return asdict(self)
    def to_write(self) -> invoice_entry_write_dto:
        return invoice_entry_write_dto(self.invoice_entry_uid, self.invoice_entry_name, self.tenant_uid, self.account_uid, self.invoice_instance_uid, self.entry_details, self.entry_amount_net, self.entry_amount_tax, self.entry_amount_gross, self.custom_attributes)
    def to_thin(self) -> invoice_entry_thin_dto:
        return invoice_entry_thin_dto(self.invoice_entry_uid, self.invoice_entry_name, self.created_date, self.is_active)
    def touch(self, updated_by: str = "system"):
        self.last_updated_date = datetime.datetime.now()
        self.last_updated_by = updated_by
        self.row_version = self.row_version+1
    def get_list_all_values(self) -> list[any]:
        return [self.invoice_entry_uid, self.invoice_entry_name, self.tenant_uid, self.account_uid, self.invoice_instance_uid, self.entry_details, self.entry_amount_net, self.entry_amount_tax, self.entry_amount_gross, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]
    def get_list_update_values(self, updated_by: str) -> list[any]:
        return [self.invoice_entry_name, self.tenant_uid, self.account_uid, self.invoice_instance_uid, self.entry_details, self.entry_amount_net, self.entry_amount_tax, self.entry_amount_gross, self.custom_attributes, updated_by, self.invoice_entry_uid]
    def is_older_than(self, dt: datetime.datetime) -> bool:
        return self.created_date < dt
    def is_newer_than(self, dt: datetime.datetime) -> bool:
        return self.created_date > dt
    def to_json_read(self) -> str:
        return json.dumps(self.to_read_dict())


@dataclass(frozen=False)
class invoice_flow_read_dto(base_read_dto, invoice_flow_write_dto):
    invoice_flow_uid: str
    invoice_flow_name: str
    class_name: str
    flow_description: str
    flow_definition_json: str
    row_instance: str
    row_lock: str | None
    row_owner: str
    row_seq: int
    row_guid: str
    row_version: int
    is_active: int
    created_date: datetime.datetime
    created_by: str
    last_updated_date: datetime.datetime
    last_updated_by: str
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str
    def __init__(self, invoice_flow_uid: str, invoice_flow_name: str, class_name: str, flow_description: str, flow_definition_json: str, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
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
    @classmethod
    def empty_read(cls):
        return cls(0, "", "", "", "", "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def default_read(cls):
        return cls(0, base_dto.get_random_uid(), "", "", "", "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def random_read(cls):
        return cls(0, base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_default(cls, invoice_flow_uid: str, invoice_flow_name: str, class_name: str, flow_description: str, flow_definition_json: str):
        return cls(0, invoice_flow_uid, invoice_flow_name, class_name, flow_description, flow_definition_json, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_full(cls, invoice_flow_uid: str, invoice_flow_name: str, class_name: str, flow_description: str, flow_definition_json: str, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
        return cls(invoice_flow_uid, invoice_flow_name, class_name, flow_description, flow_definition_json, row_instance, row_lock, row_owner, row_seq, row_guid, row_version, is_active, created_date, created_by, last_updated_date, last_updated_by, removed_date, removed_by, custom_attributes)
    @classmethod
    def from_write(cls, dto: invoice_flow_write_dto):
        return cls(0, dto.invoice_flow_uid, dto.invoice_flow_name, dto.class_name, dto.flow_description, dto.flow_definition_json, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, dto.custom_attributes)
    def clone_read(self):
        return invoice_flow_read_dto(self.invoice_flow_uid, self.invoice_flow_name, self.class_name, self.flow_description, self.flow_definition_json, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes)
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["invoice_flow_uid"], d["invoice_flow_name"], d["class_name"], d["flow_description"], d["flow_definition_json"], d["row_instance"], d["row_lock"], d["row_owner"], d["row_seq"], d["row_guid"], d["row_version"], d["is_active"], d["created_date"], d["created_by"], d["last_updated_date"], d["last_updated_by"], d["removed_date"], d["removed_by"], d["custom_attributes"])
    def to_read_dict(self) -> dict:
        return asdict(self)
    def to_write(self) -> invoice_flow_write_dto:
        return invoice_flow_write_dto(self.invoice_flow_uid, self.invoice_flow_name, self.class_name, self.flow_description, self.flow_definition_json, self.custom_attributes)
    def to_thin(self) -> invoice_flow_thin_dto:
        return invoice_flow_thin_dto(self.invoice_flow_uid, self.invoice_flow_name, self.created_date, self.is_active)
    def touch(self, updated_by: str = "system"):
        self.last_updated_date = datetime.datetime.now()
        self.last_updated_by = updated_by
        self.row_version = self.row_version+1
    def get_list_all_values(self) -> list[any]:
        return [self.invoice_flow_uid, self.invoice_flow_name, self.class_name, self.flow_description, self.flow_definition_json, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]
    def get_list_update_values(self, updated_by: str) -> list[any]:
        return [self.invoice_flow_name, self.class_name, self.flow_description, self.flow_definition_json, self.custom_attributes, updated_by, self.invoice_flow_uid]
    def is_older_than(self, dt: datetime.datetime) -> bool:
        return self.created_date < dt
    def is_newer_than(self, dt: datetime.datetime) -> bool:
        return self.created_date > dt
    def to_json_read(self) -> str:
        return json.dumps(self.to_read_dict())


@dataclass(frozen=False)
class invoice_flow_state_read_dto(base_read_dto, invoice_flow_state_write_dto):
    invoice_flow_state_uid: str
    invoice_flow_state_name: str
    invoice_flow_uid: str
    state_definition_json: str
    row_instance: str
    row_lock: str | None
    row_owner: str
    row_seq: int
    row_guid: str
    row_version: int
    is_active: int
    created_date: datetime.datetime
    created_by: str
    last_updated_date: datetime.datetime
    last_updated_by: str
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str
    def __init__(self, invoice_flow_state_uid: str, invoice_flow_state_name: str, invoice_flow_uid: str, state_definition_json: str, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
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
    @classmethod
    def empty_read(cls):
        return cls(0, "", "", "", "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def default_read(cls):
        return cls(0, base_dto.get_random_uid(), "", "", "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def random_read(cls):
        return cls(0, base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_default(cls, invoice_flow_state_uid: str, invoice_flow_state_name: str, invoice_flow_uid: str, state_definition_json: str):
        return cls(0, invoice_flow_state_uid, invoice_flow_state_name, invoice_flow_uid, state_definition_json, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_full(cls, invoice_flow_state_uid: str, invoice_flow_state_name: str, invoice_flow_uid: str, state_definition_json: str, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
        return cls(invoice_flow_state_uid, invoice_flow_state_name, invoice_flow_uid, state_definition_json, row_instance, row_lock, row_owner, row_seq, row_guid, row_version, is_active, created_date, created_by, last_updated_date, last_updated_by, removed_date, removed_by, custom_attributes)
    @classmethod
    def from_write(cls, dto: invoice_flow_state_write_dto):
        return cls(0, dto.invoice_flow_state_uid, dto.invoice_flow_state_name, dto.invoice_flow_uid, dto.state_definition_json, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, dto.custom_attributes)
    def clone_read(self):
        return invoice_flow_state_read_dto(self.invoice_flow_state_uid, self.invoice_flow_state_name, self.invoice_flow_uid, self.state_definition_json, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes)
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["invoice_flow_state_uid"], d["invoice_flow_state_name"], d["invoice_flow_uid"], d["state_definition_json"], d["row_instance"], d["row_lock"], d["row_owner"], d["row_seq"], d["row_guid"], d["row_version"], d["is_active"], d["created_date"], d["created_by"], d["last_updated_date"], d["last_updated_by"], d["removed_date"], d["removed_by"], d["custom_attributes"])
    def to_read_dict(self) -> dict:
        return asdict(self)
    def to_write(self) -> invoice_flow_state_write_dto:
        return invoice_flow_state_write_dto(self.invoice_flow_state_uid, self.invoice_flow_state_name, self.invoice_flow_uid, self.state_definition_json, self.custom_attributes)
    def to_thin(self) -> invoice_flow_state_thin_dto:
        return invoice_flow_state_thin_dto(self.invoice_flow_state_uid, self.invoice_flow_state_name, self.created_date, self.is_active)
    def touch(self, updated_by: str = "system"):
        self.last_updated_date = datetime.datetime.now()
        self.last_updated_by = updated_by
        self.row_version = self.row_version+1
    def get_list_all_values(self) -> list[any]:
        return [self.invoice_flow_state_uid, self.invoice_flow_state_name, self.invoice_flow_uid, self.state_definition_json, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]
    def get_list_update_values(self, updated_by: str) -> list[any]:
        return [self.invoice_flow_state_name, self.invoice_flow_uid, self.state_definition_json, self.custom_attributes, updated_by, self.invoice_flow_state_uid]
    def is_older_than(self, dt: datetime.datetime) -> bool:
        return self.created_date < dt
    def is_newer_than(self, dt: datetime.datetime) -> bool:
        return self.created_date > dt
    def to_json_read(self) -> str:
        return json.dumps(self.to_read_dict())


@dataclass(frozen=False)
class invoice_instance_read_dto(base_read_dto, invoice_instance_write_dto):
    invoice_instance_uid: str
    invoice_instance_name: str
    tenant_uid: str
    account_uid: str
    invoice_flow_uid: str
    invoice_status_uid: str
    invoice_category_uid: str
    invoice_type_uid: str
    period_uid: str
    currency_uid: str
    invoice_number: str
    invoice_details: str
    invoice_amount_net: str
    invoice_amount_tax: str
    invoice_amount_gross: str
    row_instance: str
    row_lock: str | None
    row_owner: str
    row_seq: int
    row_guid: str
    row_version: int
    is_active: int
    created_date: datetime.datetime
    created_by: str
    last_updated_date: datetime.datetime
    last_updated_by: str
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str
    def __init__(self, invoice_instance_uid: str, invoice_instance_name: str, tenant_uid: str, account_uid: str, invoice_flow_uid: str, invoice_status_uid: str, invoice_category_uid: str, invoice_type_uid: str, period_uid: str, currency_uid: str, invoice_number: str, invoice_details: str, invoice_amount_net: str, invoice_amount_tax: str, invoice_amount_gross: str, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
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
    @classmethod
    def empty_read(cls):
        return cls(0, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def default_read(cls):
        return cls(0, base_dto.get_random_uid(), "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def random_read(cls):
        return cls(0, base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), "", "", "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_default(cls, invoice_instance_uid: str, invoice_instance_name: str, tenant_uid: str, account_uid: str, invoice_flow_uid: str, invoice_status_uid: str, invoice_category_uid: str, invoice_type_uid: str, period_uid: str, currency_uid: str, invoice_number: str, invoice_details: str, invoice_amount_net: str, invoice_amount_tax: str, invoice_amount_gross: str):
        return cls(0, invoice_instance_uid, invoice_instance_name, tenant_uid, account_uid, invoice_flow_uid, invoice_status_uid, invoice_category_uid, invoice_type_uid, period_uid, currency_uid, invoice_number, invoice_details, invoice_amount_net, invoice_amount_tax, invoice_amount_gross, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_full(cls, invoice_instance_uid: str, invoice_instance_name: str, tenant_uid: str, account_uid: str, invoice_flow_uid: str, invoice_status_uid: str, invoice_category_uid: str, invoice_type_uid: str, period_uid: str, currency_uid: str, invoice_number: str, invoice_details: str, invoice_amount_net: str, invoice_amount_tax: str, invoice_amount_gross: str, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
        return cls(invoice_instance_uid, invoice_instance_name, tenant_uid, account_uid, invoice_flow_uid, invoice_status_uid, invoice_category_uid, invoice_type_uid, period_uid, currency_uid, invoice_number, invoice_details, invoice_amount_net, invoice_amount_tax, invoice_amount_gross, row_instance, row_lock, row_owner, row_seq, row_guid, row_version, is_active, created_date, created_by, last_updated_date, last_updated_by, removed_date, removed_by, custom_attributes)
    @classmethod
    def from_write(cls, dto: invoice_instance_write_dto):
        return cls(0, dto.invoice_instance_uid, dto.invoice_instance_name, dto.tenant_uid, dto.account_uid, dto.invoice_flow_uid, dto.invoice_status_uid, dto.invoice_category_uid, dto.invoice_type_uid, dto.period_uid, dto.currency_uid, dto.invoice_number, dto.invoice_details, dto.invoice_amount_net, dto.invoice_amount_tax, dto.invoice_amount_gross, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, dto.custom_attributes)
    def clone_read(self):
        return invoice_instance_read_dto(self.invoice_instance_uid, self.invoice_instance_name, self.tenant_uid, self.account_uid, self.invoice_flow_uid, self.invoice_status_uid, self.invoice_category_uid, self.invoice_type_uid, self.period_uid, self.currency_uid, self.invoice_number, self.invoice_details, self.invoice_amount_net, self.invoice_amount_tax, self.invoice_amount_gross, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes)
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["invoice_instance_uid"], d["invoice_instance_name"], d["tenant_uid"], d["account_uid"], d["invoice_flow_uid"], d["invoice_status_uid"], d["invoice_category_uid"], d["invoice_type_uid"], d["period_uid"], d["currency_uid"], d["invoice_number"], d["invoice_details"], d["invoice_amount_net"], d["invoice_amount_tax"], d["invoice_amount_gross"], d["row_instance"], d["row_lock"], d["row_owner"], d["row_seq"], d["row_guid"], d["row_version"], d["is_active"], d["created_date"], d["created_by"], d["last_updated_date"], d["last_updated_by"], d["removed_date"], d["removed_by"], d["custom_attributes"])
    def to_read_dict(self) -> dict:
        return asdict(self)
    def to_write(self) -> invoice_instance_write_dto:
        return invoice_instance_write_dto(self.invoice_instance_uid, self.invoice_instance_name, self.tenant_uid, self.account_uid, self.invoice_flow_uid, self.invoice_status_uid, self.invoice_category_uid, self.invoice_type_uid, self.period_uid, self.currency_uid, self.invoice_number, self.invoice_details, self.invoice_amount_net, self.invoice_amount_tax, self.invoice_amount_gross, self.custom_attributes)
    def to_thin(self) -> invoice_instance_thin_dto:
        return invoice_instance_thin_dto(self.invoice_instance_uid, self.invoice_instance_name, self.created_date, self.is_active)
    def touch(self, updated_by: str = "system"):
        self.last_updated_date = datetime.datetime.now()
        self.last_updated_by = updated_by
        self.row_version = self.row_version+1
    def get_list_all_values(self) -> list[any]:
        return [self.invoice_instance_uid, self.invoice_instance_name, self.tenant_uid, self.account_uid, self.invoice_flow_uid, self.invoice_status_uid, self.invoice_category_uid, self.invoice_type_uid, self.period_uid, self.currency_uid, self.invoice_number, self.invoice_details, self.invoice_amount_net, self.invoice_amount_tax, self.invoice_amount_gross, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]
    def get_list_update_values(self, updated_by: str) -> list[any]:
        return [self.invoice_instance_name, self.tenant_uid, self.account_uid, self.invoice_flow_uid, self.invoice_status_uid, self.invoice_category_uid, self.invoice_type_uid, self.period_uid, self.currency_uid, self.invoice_number, self.invoice_details, self.invoice_amount_net, self.invoice_amount_tax, self.invoice_amount_gross, self.custom_attributes, updated_by, self.invoice_instance_uid]
    def is_older_than(self, dt: datetime.datetime) -> bool:
        return self.created_date < dt
    def is_newer_than(self, dt: datetime.datetime) -> bool:
        return self.created_date > dt
    def to_json_read(self) -> str:
        return json.dumps(self.to_read_dict())


@dataclass(frozen=False)
class invoice_status_read_dto(base_read_dto, invoice_status_write_dto):
    invoice_status_uid: str
    invoice_status_name: str
    status_description: str
    row_instance: str
    row_lock: str | None
    row_owner: str
    row_seq: int
    row_guid: str
    row_version: int
    is_active: int
    created_date: datetime.datetime
    created_by: str
    last_updated_date: datetime.datetime
    last_updated_by: str
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str
    def __init__(self, invoice_status_uid: str, invoice_status_name: str, status_description: str, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
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
    @classmethod
    def empty_read(cls):
        return cls(0, "", "", "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def default_read(cls):
        return cls(0, base_dto.get_random_uid(), "", "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def random_read(cls):
        return cls(0, base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_default(cls, invoice_status_uid: str, invoice_status_name: str, status_description: str):
        return cls(0, invoice_status_uid, invoice_status_name, status_description, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_full(cls, invoice_status_uid: str, invoice_status_name: str, status_description: str, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
        return cls(invoice_status_uid, invoice_status_name, status_description, row_instance, row_lock, row_owner, row_seq, row_guid, row_version, is_active, created_date, created_by, last_updated_date, last_updated_by, removed_date, removed_by, custom_attributes)
    @classmethod
    def from_write(cls, dto: invoice_status_write_dto):
        return cls(0, dto.invoice_status_uid, dto.invoice_status_name, dto.status_description, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, dto.custom_attributes)
    def clone_read(self):
        return invoice_status_read_dto(self.invoice_status_uid, self.invoice_status_name, self.status_description, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes)
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["invoice_status_uid"], d["invoice_status_name"], d["status_description"], d["row_instance"], d["row_lock"], d["row_owner"], d["row_seq"], d["row_guid"], d["row_version"], d["is_active"], d["created_date"], d["created_by"], d["last_updated_date"], d["last_updated_by"], d["removed_date"], d["removed_by"], d["custom_attributes"])
    def to_read_dict(self) -> dict:
        return asdict(self)
    def to_write(self) -> invoice_status_write_dto:
        return invoice_status_write_dto(self.invoice_status_uid, self.invoice_status_name, self.status_description, self.custom_attributes)
    def to_thin(self) -> invoice_status_thin_dto:
        return invoice_status_thin_dto(self.invoice_status_uid, self.invoice_status_name, self.created_date, self.is_active)
    def touch(self, updated_by: str = "system"):
        self.last_updated_date = datetime.datetime.now()
        self.last_updated_by = updated_by
        self.row_version = self.row_version+1
    def get_list_all_values(self) -> list[any]:
        return [self.invoice_status_uid, self.invoice_status_name, self.status_description, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]
    def get_list_update_values(self, updated_by: str) -> list[any]:
        return [self.invoice_status_name, self.status_description, self.custom_attributes, updated_by, self.invoice_status_uid]
    def is_older_than(self, dt: datetime.datetime) -> bool:
        return self.created_date < dt
    def is_newer_than(self, dt: datetime.datetime) -> bool:
        return self.created_date > dt
    def to_json_read(self) -> str:
        return json.dumps(self.to_read_dict())


@dataclass(frozen=False)
class invoice_type_read_dto(base_read_dto, invoice_type_write_dto):
    invoice_type_uid: str
    invoice_type_name: str
    row_instance: str
    row_lock: str | None
    row_owner: str
    row_seq: int
    row_guid: str
    row_version: int
    is_active: int
    created_date: datetime.datetime
    created_by: str
    last_updated_date: datetime.datetime
    last_updated_by: str
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str
    def __init__(self, invoice_type_uid: str, invoice_type_name: str, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
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
    @classmethod
    def empty_read(cls):
        return cls(0, "", "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def default_read(cls):
        return cls(0, base_dto.get_random_uid(), "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def random_read(cls):
        return cls(0, base_dto.get_random_uid(), base_dto.get_random_uid(), "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_default(cls, invoice_type_uid: str, invoice_type_name: str):
        return cls(0, invoice_type_uid, invoice_type_name, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_full(cls, invoice_type_uid: str, invoice_type_name: str, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
        return cls(invoice_type_uid, invoice_type_name, row_instance, row_lock, row_owner, row_seq, row_guid, row_version, is_active, created_date, created_by, last_updated_date, last_updated_by, removed_date, removed_by, custom_attributes)
    @classmethod
    def from_write(cls, dto: invoice_type_write_dto):
        return cls(0, dto.invoice_type_uid, dto.invoice_type_name, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, dto.custom_attributes)
    def clone_read(self):
        return invoice_type_read_dto(self.invoice_type_uid, self.invoice_type_name, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes)
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["invoice_type_uid"], d["invoice_type_name"], d["row_instance"], d["row_lock"], d["row_owner"], d["row_seq"], d["row_guid"], d["row_version"], d["is_active"], d["created_date"], d["created_by"], d["last_updated_date"], d["last_updated_by"], d["removed_date"], d["removed_by"], d["custom_attributes"])
    def to_read_dict(self) -> dict:
        return asdict(self)
    def to_write(self) -> invoice_type_write_dto:
        return invoice_type_write_dto(self.invoice_type_uid, self.invoice_type_name, self.custom_attributes)
    def to_thin(self) -> invoice_type_thin_dto:
        return invoice_type_thin_dto(self.invoice_type_uid, self.invoice_type_name, self.created_date, self.is_active)
    def touch(self, updated_by: str = "system"):
        self.last_updated_date = datetime.datetime.now()
        self.last_updated_by = updated_by
        self.row_version = self.row_version+1
    def get_list_all_values(self) -> list[any]:
        return [self.invoice_type_uid, self.invoice_type_name, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]
    def get_list_update_values(self, updated_by: str) -> list[any]:
        return [self.invoice_type_name, self.custom_attributes, updated_by, self.invoice_type_uid]
    def is_older_than(self, dt: datetime.datetime) -> bool:
        return self.created_date < dt
    def is_newer_than(self, dt: datetime.datetime) -> bool:
        return self.created_date > dt
    def to_json_read(self) -> str:
        return json.dumps(self.to_read_dict())


@dataclass(frozen=False)
class location_postal_code_read_dto(base_read_dto, location_postal_code_write_dto):
    location_postal_code_uid: str
    location_postal_code_name: str
    country_uid: str
    postal_code: str
    street_name: str
    city_name: str
    county_name: str
    state_name: str
    region_name: str
    row_instance: str
    row_lock: str | None
    row_owner: str
    row_seq: int
    row_guid: str
    row_version: int
    is_active: int
    created_date: datetime.datetime
    created_by: str
    last_updated_date: datetime.datetime
    last_updated_by: str
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str
    def __init__(self, location_postal_code_uid: str, location_postal_code_name: str, country_uid: str, postal_code: str, street_name: str, city_name: str, county_name: str, state_name: str, region_name: str, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
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
    @classmethod
    def empty_read(cls):
        return cls(0, "", "", "", "", "", "", "", "", "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def default_read(cls):
        return cls(0, base_dto.get_random_uid(), "", "", "", "", "", "", "", "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def random_read(cls):
        return cls(0, base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_default(cls, location_postal_code_uid: str, location_postal_code_name: str, country_uid: str, postal_code: str, street_name: str, city_name: str, county_name: str, state_name: str, region_name: str):
        return cls(0, location_postal_code_uid, location_postal_code_name, country_uid, postal_code, street_name, city_name, county_name, state_name, region_name, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_full(cls, location_postal_code_uid: str, location_postal_code_name: str, country_uid: str, postal_code: str, street_name: str, city_name: str, county_name: str, state_name: str, region_name: str, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
        return cls(location_postal_code_uid, location_postal_code_name, country_uid, postal_code, street_name, city_name, county_name, state_name, region_name, row_instance, row_lock, row_owner, row_seq, row_guid, row_version, is_active, created_date, created_by, last_updated_date, last_updated_by, removed_date, removed_by, custom_attributes)
    @classmethod
    def from_write(cls, dto: location_postal_code_write_dto):
        return cls(0, dto.location_postal_code_uid, dto.location_postal_code_name, dto.country_uid, dto.postal_code, dto.street_name, dto.city_name, dto.county_name, dto.state_name, dto.region_name, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, dto.custom_attributes)
    def clone_read(self):
        return location_postal_code_read_dto(self.location_postal_code_uid, self.location_postal_code_name, self.country_uid, self.postal_code, self.street_name, self.city_name, self.county_name, self.state_name, self.region_name, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes)
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["location_postal_code_uid"], d["location_postal_code_name"], d["country_uid"], d["postal_code"], d["street_name"], d["city_name"], d["county_name"], d["state_name"], d["region_name"], d["row_instance"], d["row_lock"], d["row_owner"], d["row_seq"], d["row_guid"], d["row_version"], d["is_active"], d["created_date"], d["created_by"], d["last_updated_date"], d["last_updated_by"], d["removed_date"], d["removed_by"], d["custom_attributes"])
    def to_read_dict(self) -> dict:
        return asdict(self)
    def to_write(self) -> location_postal_code_write_dto:
        return location_postal_code_write_dto(self.location_postal_code_uid, self.location_postal_code_name, self.country_uid, self.postal_code, self.street_name, self.city_name, self.county_name, self.state_name, self.region_name, self.custom_attributes)
    def to_thin(self) -> location_postal_code_thin_dto:
        return location_postal_code_thin_dto(self.location_postal_code_uid, self.location_postal_code_name, self.created_date, self.is_active)
    def touch(self, updated_by: str = "system"):
        self.last_updated_date = datetime.datetime.now()
        self.last_updated_by = updated_by
        self.row_version = self.row_version+1
    def get_list_all_values(self) -> list[any]:
        return [self.location_postal_code_uid, self.location_postal_code_name, self.country_uid, self.postal_code, self.street_name, self.city_name, self.county_name, self.state_name, self.region_name, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]
    def get_list_update_values(self, updated_by: str) -> list[any]:
        return [self.location_postal_code_name, self.country_uid, self.postal_code, self.street_name, self.city_name, self.county_name, self.state_name, self.region_name, self.custom_attributes, updated_by, self.location_postal_code_uid]
    def is_older_than(self, dt: datetime.datetime) -> bool:
        return self.created_date < dt
    def is_newer_than(self, dt: datetime.datetime) -> bool:
        return self.created_date > dt
    def to_json_read(self) -> str:
        return json.dumps(self.to_read_dict())


@dataclass(frozen=False)
class location_territory_read_dto(base_read_dto, location_territory_write_dto):
    location_territory_uid: str
    location_territory_name: str
    tenant_uid: str
    location_postal_code_uid: str
    territory_latitude: str
    territory_longitude: str
    territory_description: str
    row_instance: str
    row_lock: str | None
    row_owner: str
    row_seq: int
    row_guid: str
    row_version: int
    is_active: int
    created_date: datetime.datetime
    created_by: str
    last_updated_date: datetime.datetime
    last_updated_by: str
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str
    def __init__(self, location_territory_uid: str, location_territory_name: str, tenant_uid: str, location_postal_code_uid: str, territory_latitude: str, territory_longitude: str, territory_description: str, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
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
    @classmethod
    def empty_read(cls):
        return cls(0, "", "", "", "", "", "", "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def default_read(cls):
        return cls(0, base_dto.get_random_uid(), "", "", "", "", "", "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def random_read(cls):
        return cls(0, base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), "", "", base_dto.get_random_uid(), "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_default(cls, location_territory_uid: str, location_territory_name: str, tenant_uid: str, location_postal_code_uid: str, territory_latitude: str, territory_longitude: str, territory_description: str):
        return cls(0, location_territory_uid, location_territory_name, tenant_uid, location_postal_code_uid, territory_latitude, territory_longitude, territory_description, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_full(cls, location_territory_uid: str, location_territory_name: str, tenant_uid: str, location_postal_code_uid: str, territory_latitude: str, territory_longitude: str, territory_description: str, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
        return cls(location_territory_uid, location_territory_name, tenant_uid, location_postal_code_uid, territory_latitude, territory_longitude, territory_description, row_instance, row_lock, row_owner, row_seq, row_guid, row_version, is_active, created_date, created_by, last_updated_date, last_updated_by, removed_date, removed_by, custom_attributes)
    @classmethod
    def from_write(cls, dto: location_territory_write_dto):
        return cls(0, dto.location_territory_uid, dto.location_territory_name, dto.tenant_uid, dto.location_postal_code_uid, dto.territory_latitude, dto.territory_longitude, dto.territory_description, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, dto.custom_attributes)
    def clone_read(self):
        return location_territory_read_dto(self.location_territory_uid, self.location_territory_name, self.tenant_uid, self.location_postal_code_uid, self.territory_latitude, self.territory_longitude, self.territory_description, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes)
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["location_territory_uid"], d["location_territory_name"], d["tenant_uid"], d["location_postal_code_uid"], d["territory_latitude"], d["territory_longitude"], d["territory_description"], d["row_instance"], d["row_lock"], d["row_owner"], d["row_seq"], d["row_guid"], d["row_version"], d["is_active"], d["created_date"], d["created_by"], d["last_updated_date"], d["last_updated_by"], d["removed_date"], d["removed_by"], d["custom_attributes"])
    def to_read_dict(self) -> dict:
        return asdict(self)
    def to_write(self) -> location_territory_write_dto:
        return location_territory_write_dto(self.location_territory_uid, self.location_territory_name, self.tenant_uid, self.location_postal_code_uid, self.territory_latitude, self.territory_longitude, self.territory_description, self.custom_attributes)
    def to_thin(self) -> location_territory_thin_dto:
        return location_territory_thin_dto(self.location_territory_uid, self.location_territory_name, self.created_date, self.is_active)
    def touch(self, updated_by: str = "system"):
        self.last_updated_date = datetime.datetime.now()
        self.last_updated_by = updated_by
        self.row_version = self.row_version+1
    def get_list_all_values(self) -> list[any]:
        return [self.location_territory_uid, self.location_territory_name, self.tenant_uid, self.location_postal_code_uid, self.territory_latitude, self.territory_longitude, self.territory_description, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]
    def get_list_update_values(self, updated_by: str) -> list[any]:
        return [self.location_territory_name, self.tenant_uid, self.location_postal_code_uid, self.territory_latitude, self.territory_longitude, self.territory_description, self.custom_attributes, updated_by, self.location_territory_uid]
    def is_older_than(self, dt: datetime.datetime) -> bool:
        return self.created_date < dt
    def is_newer_than(self, dt: datetime.datetime) -> bool:
        return self.created_date > dt
    def to_json_read(self) -> str:
        return json.dumps(self.to_read_dict())


@dataclass(frozen=False)
class monitor_read_dto(base_read_dto, monitor_write_dto):
    monitor_uid: str
    monitor_name: str
    tenant_uid: str
    account_uid: str
    monitor_type_uid: str
    schedule_expression: str
    monitor_protocol: str
    monitor_url: str
    monitor_user: str
    monitor_priority: int
    is_on_hold: int
    last_status_name: str
    last_run_time: str
    last_exception_message: str
    row_instance: str
    row_lock: str | None
    row_owner: str
    row_seq: int
    row_guid: str
    row_version: int
    is_active: int
    created_date: datetime.datetime
    created_by: str
    last_updated_date: datetime.datetime
    last_updated_by: str
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str
    def __init__(self, monitor_uid: str, monitor_name: str, tenant_uid: str, account_uid: str, monitor_type_uid: str, schedule_expression: str, monitor_protocol: str, monitor_url: str, monitor_user: str, monitor_priority: int, is_on_hold: int, last_status_name: str, last_run_time: str, last_exception_message: str, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
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
    @classmethod
    def empty_read(cls):
        return cls(0, "", "", "", "", "", "", "", "", "", 0, 0, "", "", "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def default_read(cls):
        return cls(0, base_dto.get_random_uid(), "", "", "", "", "", "", "", "", 0, 0, "", "", "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def random_read(cls):
        return cls(0, base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), 0, 0, base_dto.get_random_uid(), "", base_dto.get_random_uid(), "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_default(cls, monitor_uid: str, monitor_name: str, tenant_uid: str, account_uid: str, monitor_type_uid: str, schedule_expression: str, monitor_protocol: str, monitor_url: str, monitor_user: str, monitor_priority: int, is_on_hold: int, last_status_name: str, last_run_time: str, last_exception_message: str):
        return cls(0, monitor_uid, monitor_name, tenant_uid, account_uid, monitor_type_uid, schedule_expression, monitor_protocol, monitor_url, monitor_user, monitor_priority, is_on_hold, last_status_name, last_run_time, last_exception_message, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_full(cls, monitor_uid: str, monitor_name: str, tenant_uid: str, account_uid: str, monitor_type_uid: str, schedule_expression: str, monitor_protocol: str, monitor_url: str, monitor_user: str, monitor_priority: int, is_on_hold: int, last_status_name: str, last_run_time: str, last_exception_message: str, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
        return cls(monitor_uid, monitor_name, tenant_uid, account_uid, monitor_type_uid, schedule_expression, monitor_protocol, monitor_url, monitor_user, monitor_priority, is_on_hold, last_status_name, last_run_time, last_exception_message, row_instance, row_lock, row_owner, row_seq, row_guid, row_version, is_active, created_date, created_by, last_updated_date, last_updated_by, removed_date, removed_by, custom_attributes)
    @classmethod
    def from_write(cls, dto: monitor_write_dto):
        return cls(0, dto.monitor_uid, dto.monitor_name, dto.tenant_uid, dto.account_uid, dto.monitor_type_uid, dto.schedule_expression, dto.monitor_protocol, dto.monitor_url, dto.monitor_user, dto.monitor_priority, dto.is_on_hold, dto.last_status_name, dto.last_run_time, dto.last_exception_message, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, dto.custom_attributes)
    def clone_read(self):
        return monitor_read_dto(self.monitor_uid, self.monitor_name, self.tenant_uid, self.account_uid, self.monitor_type_uid, self.schedule_expression, self.monitor_protocol, self.monitor_url, self.monitor_user, self.monitor_priority, self.is_on_hold, self.last_status_name, self.last_run_time, self.last_exception_message, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes)
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["monitor_uid"], d["monitor_name"], d["tenant_uid"], d["account_uid"], d["monitor_type_uid"], d["schedule_expression"], d["monitor_protocol"], d["monitor_url"], d["monitor_user"], d["monitor_priority"], d["is_on_hold"], d["last_status_name"], d["last_run_time"], d["last_exception_message"], d["row_instance"], d["row_lock"], d["row_owner"], d["row_seq"], d["row_guid"], d["row_version"], d["is_active"], d["created_date"], d["created_by"], d["last_updated_date"], d["last_updated_by"], d["removed_date"], d["removed_by"], d["custom_attributes"])
    def to_read_dict(self) -> dict:
        return asdict(self)
    def to_write(self) -> monitor_write_dto:
        return monitor_write_dto(self.monitor_uid, self.monitor_name, self.tenant_uid, self.account_uid, self.monitor_type_uid, self.schedule_expression, self.monitor_protocol, self.monitor_url, self.monitor_user, self.monitor_priority, self.is_on_hold, self.last_status_name, self.last_run_time, self.last_exception_message, self.custom_attributes)
    def to_thin(self) -> monitor_thin_dto:
        return monitor_thin_dto(self.monitor_uid, self.monitor_name, self.created_date, self.is_active)
    def touch(self, updated_by: str = "system"):
        self.last_updated_date = datetime.datetime.now()
        self.last_updated_by = updated_by
        self.row_version = self.row_version+1
    def get_list_all_values(self) -> list[any]:
        return [self.monitor_uid, self.monitor_name, self.tenant_uid, self.account_uid, self.monitor_type_uid, self.schedule_expression, self.monitor_protocol, self.monitor_url, self.monitor_user, self.monitor_priority, self.is_on_hold, self.last_status_name, self.last_run_time, self.last_exception_message, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]
    def get_list_update_values(self, updated_by: str) -> list[any]:
        return [self.monitor_name, self.tenant_uid, self.account_uid, self.monitor_type_uid, self.schedule_expression, self.monitor_protocol, self.monitor_url, self.monitor_user, self.monitor_priority, self.is_on_hold, self.last_status_name, self.last_run_time, self.last_exception_message, self.custom_attributes, updated_by, self.monitor_uid]
    def is_older_than(self, dt: datetime.datetime) -> bool:
        return self.created_date < dt
    def is_newer_than(self, dt: datetime.datetime) -> bool:
        return self.created_date > dt
    def to_json_read(self) -> str:
        return json.dumps(self.to_read_dict())


@dataclass(frozen=False)
class monitor_run_read_dto(base_read_dto, monitor_run_write_dto):
    monitor_run_uid: str
    monitor_run_name: str
    tenant_uid: str
    account_uid: str
    monitor_uid: str
    status_name: str
    run_time: str
    exception_message: str
    row_instance: str
    row_lock: str | None
    row_owner: str
    row_seq: int
    row_guid: str
    row_version: int
    is_active: int
    created_date: datetime.datetime
    created_by: str
    last_updated_date: datetime.datetime
    last_updated_by: str
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str
    def __init__(self, monitor_run_uid: str, monitor_run_name: str, tenant_uid: str, account_uid: str, monitor_uid: str, status_name: str, run_time: str, exception_message: str, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
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
    @classmethod
    def empty_read(cls):
        return cls(0, "", "", "", "", "", "", "", "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def default_read(cls):
        return cls(0, base_dto.get_random_uid(), "", "", "", "", "", "", "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def random_read(cls):
        return cls(0, base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), "", base_dto.get_random_uid(), "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_default(cls, monitor_run_uid: str, monitor_run_name: str, tenant_uid: str, account_uid: str, monitor_uid: str, status_name: str, run_time: str, exception_message: str):
        return cls(0, monitor_run_uid, monitor_run_name, tenant_uid, account_uid, monitor_uid, status_name, run_time, exception_message, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_full(cls, monitor_run_uid: str, monitor_run_name: str, tenant_uid: str, account_uid: str, monitor_uid: str, status_name: str, run_time: str, exception_message: str, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
        return cls(monitor_run_uid, monitor_run_name, tenant_uid, account_uid, monitor_uid, status_name, run_time, exception_message, row_instance, row_lock, row_owner, row_seq, row_guid, row_version, is_active, created_date, created_by, last_updated_date, last_updated_by, removed_date, removed_by, custom_attributes)
    @classmethod
    def from_write(cls, dto: monitor_run_write_dto):
        return cls(0, dto.monitor_run_uid, dto.monitor_run_name, dto.tenant_uid, dto.account_uid, dto.monitor_uid, dto.status_name, dto.run_time, dto.exception_message, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, dto.custom_attributes)
    def clone_read(self):
        return monitor_run_read_dto(self.monitor_run_uid, self.monitor_run_name, self.tenant_uid, self.account_uid, self.monitor_uid, self.status_name, self.run_time, self.exception_message, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes)
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["monitor_run_uid"], d["monitor_run_name"], d["tenant_uid"], d["account_uid"], d["monitor_uid"], d["status_name"], d["run_time"], d["exception_message"], d["row_instance"], d["row_lock"], d["row_owner"], d["row_seq"], d["row_guid"], d["row_version"], d["is_active"], d["created_date"], d["created_by"], d["last_updated_date"], d["last_updated_by"], d["removed_date"], d["removed_by"], d["custom_attributes"])
    def to_read_dict(self) -> dict:
        return asdict(self)
    def to_write(self) -> monitor_run_write_dto:
        return monitor_run_write_dto(self.monitor_run_uid, self.monitor_run_name, self.tenant_uid, self.account_uid, self.monitor_uid, self.status_name, self.run_time, self.exception_message, self.custom_attributes)
    def to_thin(self) -> monitor_run_thin_dto:
        return monitor_run_thin_dto(self.monitor_run_uid, self.monitor_run_name, self.created_date, self.is_active)
    def touch(self, updated_by: str = "system"):
        self.last_updated_date = datetime.datetime.now()
        self.last_updated_by = updated_by
        self.row_version = self.row_version+1
    def get_list_all_values(self) -> list[any]:
        return [self.monitor_run_uid, self.monitor_run_name, self.tenant_uid, self.account_uid, self.monitor_uid, self.status_name, self.run_time, self.exception_message, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]
    def get_list_update_values(self, updated_by: str) -> list[any]:
        return [self.monitor_run_name, self.tenant_uid, self.account_uid, self.monitor_uid, self.status_name, self.run_time, self.exception_message, self.custom_attributes, updated_by, self.monitor_run_uid]
    def is_older_than(self, dt: datetime.datetime) -> bool:
        return self.created_date < dt
    def is_newer_than(self, dt: datetime.datetime) -> bool:
        return self.created_date > dt
    def to_json_read(self) -> str:
        return json.dumps(self.to_read_dict())


@dataclass(frozen=False)
class monitor_type_read_dto(base_read_dto, monitor_type_write_dto):
    monitor_type_uid: str
    monitor_type_name: str
    class_name: str
    parameters_json: str
    row_instance: str
    row_lock: str | None
    row_owner: str
    row_seq: int
    row_guid: str
    row_version: int
    is_active: int
    created_date: datetime.datetime
    created_by: str
    last_updated_date: datetime.datetime
    last_updated_by: str
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str
    def __init__(self, monitor_type_uid: str, monitor_type_name: str, class_name: str, parameters_json: str, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
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
    @classmethod
    def empty_read(cls):
        return cls(0, "", "", "", "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def default_read(cls):
        return cls(0, base_dto.get_random_uid(), "", "", "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def random_read(cls):
        return cls(0, base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_default(cls, monitor_type_uid: str, monitor_type_name: str, class_name: str, parameters_json: str):
        return cls(0, monitor_type_uid, monitor_type_name, class_name, parameters_json, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_full(cls, monitor_type_uid: str, monitor_type_name: str, class_name: str, parameters_json: str, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
        return cls(monitor_type_uid, monitor_type_name, class_name, parameters_json, row_instance, row_lock, row_owner, row_seq, row_guid, row_version, is_active, created_date, created_by, last_updated_date, last_updated_by, removed_date, removed_by, custom_attributes)
    @classmethod
    def from_write(cls, dto: monitor_type_write_dto):
        return cls(0, dto.monitor_type_uid, dto.monitor_type_name, dto.class_name, dto.parameters_json, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, dto.custom_attributes)
    def clone_read(self):
        return monitor_type_read_dto(self.monitor_type_uid, self.monitor_type_name, self.class_name, self.parameters_json, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes)
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["monitor_type_uid"], d["monitor_type_name"], d["class_name"], d["parameters_json"], d["row_instance"], d["row_lock"], d["row_owner"], d["row_seq"], d["row_guid"], d["row_version"], d["is_active"], d["created_date"], d["created_by"], d["last_updated_date"], d["last_updated_by"], d["removed_date"], d["removed_by"], d["custom_attributes"])
    def to_read_dict(self) -> dict:
        return asdict(self)
    def to_write(self) -> monitor_type_write_dto:
        return monitor_type_write_dto(self.monitor_type_uid, self.monitor_type_name, self.class_name, self.parameters_json, self.custom_attributes)
    def to_thin(self) -> monitor_type_thin_dto:
        return monitor_type_thin_dto(self.monitor_type_uid, self.monitor_type_name, self.created_date, self.is_active)
    def touch(self, updated_by: str = "system"):
        self.last_updated_date = datetime.datetime.now()
        self.last_updated_by = updated_by
        self.row_version = self.row_version+1
    def get_list_all_values(self) -> list[any]:
        return [self.monitor_type_uid, self.monitor_type_name, self.class_name, self.parameters_json, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]
    def get_list_update_values(self, updated_by: str) -> list[any]:
        return [self.monitor_type_name, self.class_name, self.parameters_json, self.custom_attributes, updated_by, self.monitor_type_uid]
    def is_older_than(self, dt: datetime.datetime) -> bool:
        return self.created_date < dt
    def is_newer_than(self, dt: datetime.datetime) -> bool:
        return self.created_date > dt
    def to_json_read(self) -> str:
        return json.dumps(self.to_read_dict())


@dataclass(frozen=False)
class period_read_dto(base_read_dto, period_write_dto):
    period_uid: str
    period_name: str
    period_number: int
    period_type: str
    period_start_time: datetime.datetime
    period_end_time: datetime.datetime
    period_year: int | None
    period_quarter: int | None
    period_month: int | None
    period_week: int | None
    period_day: int | None
    row_instance: str
    row_lock: str | None
    row_owner: str
    row_seq: int
    row_guid: str
    row_version: int
    is_active: int
    created_date: datetime.datetime
    created_by: str
    last_updated_date: datetime.datetime
    last_updated_by: str
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str
    def __init__(self, period_uid: str, period_name: str, period_number: int, period_type: str, period_start_time: datetime.datetime, period_end_time: datetime.datetime, period_year: int | None, period_quarter: int | None, period_month: int | None, period_week: int | None, period_day: int | None, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
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
    @classmethod
    def empty_read(cls):
        return cls(0, "", "", 0, "", datetime.datetime.now(), datetime.datetime.now(), 0, 0, 0, 0, 0, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def default_read(cls):
        return cls(0, base_dto.get_random_uid(), "", 0, "", datetime.datetime.now(), datetime.datetime.now(), 0, 0, 0, 0, 0, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def random_read(cls):
        return cls(0, base_dto.get_random_uid(), base_dto.get_random_uid(), 0, base_dto.get_random_uid(), datetime.datetime.now(), datetime.datetime.now(), 0, 0, 0, 0, 0, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_default(cls, period_uid: str, period_name: str, period_number: int, period_type: str, period_start_time: datetime.datetime, period_end_time: datetime.datetime, period_year: int | None, period_quarter: int | None, period_month: int | None, period_week: int | None, period_day: int | None):
        return cls(0, period_uid, period_name, period_number, period_type, period_start_time, period_end_time, period_year, period_quarter, period_month, period_week, period_day, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_full(cls, period_uid: str, period_name: str, period_number: int, period_type: str, period_start_time: datetime.datetime, period_end_time: datetime.datetime, period_year: int | None, period_quarter: int | None, period_month: int | None, period_week: int | None, period_day: int | None, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
        return cls(period_uid, period_name, period_number, period_type, period_start_time, period_end_time, period_year, period_quarter, period_month, period_week, period_day, row_instance, row_lock, row_owner, row_seq, row_guid, row_version, is_active, created_date, created_by, last_updated_date, last_updated_by, removed_date, removed_by, custom_attributes)
    @classmethod
    def from_write(cls, dto: period_write_dto):
        return cls(0, dto.period_uid, dto.period_name, dto.period_number, dto.period_type, dto.period_start_time, dto.period_end_time, dto.period_year, dto.period_quarter, dto.period_month, dto.period_week, dto.period_day, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, dto.custom_attributes)
    def clone_read(self):
        return period_read_dto(self.period_uid, self.period_name, self.period_number, self.period_type, self.period_start_time, self.period_end_time, self.period_year, self.period_quarter, self.period_month, self.period_week, self.period_day, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes)
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["period_uid"], d["period_name"], d["period_number"], d["period_type"], d["period_start_time"], d["period_end_time"], d["period_year"], d["period_quarter"], d["period_month"], d["period_week"], d["period_day"], d["row_instance"], d["row_lock"], d["row_owner"], d["row_seq"], d["row_guid"], d["row_version"], d["is_active"], d["created_date"], d["created_by"], d["last_updated_date"], d["last_updated_by"], d["removed_date"], d["removed_by"], d["custom_attributes"])
    def to_read_dict(self) -> dict:
        return asdict(self)
    def to_write(self) -> period_write_dto:
        return period_write_dto(self.period_uid, self.period_name, self.period_number, self.period_type, self.period_start_time, self.period_end_time, self.period_year, self.period_quarter, self.period_month, self.period_week, self.period_day, self.custom_attributes)
    def to_thin(self) -> period_thin_dto:
        return period_thin_dto(self.period_uid, self.period_name, self.created_date, self.is_active)
    def touch(self, updated_by: str = "system"):
        self.last_updated_date = datetime.datetime.now()
        self.last_updated_by = updated_by
        self.row_version = self.row_version+1
    def get_list_all_values(self) -> list[any]:
        return [self.period_uid, self.period_name, self.period_number, self.period_type, self.period_start_time, self.period_end_time, self.period_year, self.period_quarter, self.period_month, self.period_week, self.period_day, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]
    def get_list_update_values(self, updated_by: str) -> list[any]:
        return [self.period_name, self.period_number, self.period_type, self.period_start_time, self.period_end_time, self.period_year, self.period_quarter, self.period_month, self.period_week, self.period_day, self.custom_attributes, updated_by, self.period_uid]
    def is_older_than(self, dt: datetime.datetime) -> bool:
        return self.created_date < dt
    def is_newer_than(self, dt: datetime.datetime) -> bool:
        return self.created_date > dt
    def to_json_read(self) -> str:
        return json.dumps(self.to_read_dict())


@dataclass(frozen=False)
class process_read_dto(base_read_dto, process_write_dto):
    process_uid: str
    process_name: str
    tenant_uid: str
    account_uid: str
    process_type_uid: str
    status_name: str
    row_instance: str
    row_lock: str | None
    row_owner: str
    row_seq: int
    row_guid: str
    row_version: int
    is_active: int
    created_date: datetime.datetime
    created_by: str
    last_updated_date: datetime.datetime
    last_updated_by: str
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str
    def __init__(self, process_uid: str, process_name: str, tenant_uid: str, account_uid: str, process_type_uid: str, status_name: str, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
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
    @classmethod
    def empty_read(cls):
        return cls(0, "", "", "", "", "", "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def default_read(cls):
        return cls(0, base_dto.get_random_uid(), "", "", "", "", "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def random_read(cls):
        return cls(0, base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_default(cls, process_uid: str, process_name: str, tenant_uid: str, account_uid: str, process_type_uid: str, status_name: str):
        return cls(0, process_uid, process_name, tenant_uid, account_uid, process_type_uid, status_name, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_full(cls, process_uid: str, process_name: str, tenant_uid: str, account_uid: str, process_type_uid: str, status_name: str, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
        return cls(process_uid, process_name, tenant_uid, account_uid, process_type_uid, status_name, row_instance, row_lock, row_owner, row_seq, row_guid, row_version, is_active, created_date, created_by, last_updated_date, last_updated_by, removed_date, removed_by, custom_attributes)
    @classmethod
    def from_write(cls, dto: process_write_dto):
        return cls(0, dto.process_uid, dto.process_name, dto.tenant_uid, dto.account_uid, dto.process_type_uid, dto.status_name, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, dto.custom_attributes)
    def clone_read(self):
        return process_read_dto(self.process_uid, self.process_name, self.tenant_uid, self.account_uid, self.process_type_uid, self.status_name, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes)
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["process_uid"], d["process_name"], d["tenant_uid"], d["account_uid"], d["process_type_uid"], d["status_name"], d["row_instance"], d["row_lock"], d["row_owner"], d["row_seq"], d["row_guid"], d["row_version"], d["is_active"], d["created_date"], d["created_by"], d["last_updated_date"], d["last_updated_by"], d["removed_date"], d["removed_by"], d["custom_attributes"])
    def to_read_dict(self) -> dict:
        return asdict(self)
    def to_write(self) -> process_write_dto:
        return process_write_dto(self.process_uid, self.process_name, self.tenant_uid, self.account_uid, self.process_type_uid, self.status_name, self.custom_attributes)
    def to_thin(self) -> process_thin_dto:
        return process_thin_dto(self.process_uid, self.process_name, self.created_date, self.is_active)
    def touch(self, updated_by: str = "system"):
        self.last_updated_date = datetime.datetime.now()
        self.last_updated_by = updated_by
        self.row_version = self.row_version+1
    def get_list_all_values(self) -> list[any]:
        return [self.process_uid, self.process_name, self.tenant_uid, self.account_uid, self.process_type_uid, self.status_name, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]
    def get_list_update_values(self, updated_by: str) -> list[any]:
        return [self.process_name, self.tenant_uid, self.account_uid, self.process_type_uid, self.status_name, self.custom_attributes, updated_by, self.process_uid]
    def is_older_than(self, dt: datetime.datetime) -> bool:
        return self.created_date < dt
    def is_newer_than(self, dt: datetime.datetime) -> bool:
        return self.created_date > dt
    def to_json_read(self) -> str:
        return json.dumps(self.to_read_dict())


@dataclass(frozen=False)
class process_run_read_dto(base_read_dto, process_run_write_dto):
    process_run_uid: str
    process_run_name: str
    tenant_uid: str
    account_uid: str
    process_uid: str
    status_name: str
    run_time: int
    row_instance: str
    row_lock: str | None
    row_owner: str
    row_seq: int
    row_guid: str
    row_version: int
    is_active: int
    created_date: datetime.datetime
    created_by: str
    last_updated_date: datetime.datetime
    last_updated_by: str
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str
    def __init__(self, process_run_uid: str, process_run_name: str, tenant_uid: str, account_uid: str, process_uid: str, status_name: str, run_time: int, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
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
    @classmethod
    def empty_read(cls):
        return cls(0, "", "", "", "", "", "", 0, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def default_read(cls):
        return cls(0, base_dto.get_random_uid(), "", "", "", "", "", 0, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def random_read(cls):
        return cls(0, base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), 0, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_default(cls, process_run_uid: str, process_run_name: str, tenant_uid: str, account_uid: str, process_uid: str, status_name: str, run_time: int):
        return cls(0, process_run_uid, process_run_name, tenant_uid, account_uid, process_uid, status_name, run_time, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_full(cls, process_run_uid: str, process_run_name: str, tenant_uid: str, account_uid: str, process_uid: str, status_name: str, run_time: int, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
        return cls(process_run_uid, process_run_name, tenant_uid, account_uid, process_uid, status_name, run_time, row_instance, row_lock, row_owner, row_seq, row_guid, row_version, is_active, created_date, created_by, last_updated_date, last_updated_by, removed_date, removed_by, custom_attributes)
    @classmethod
    def from_write(cls, dto: process_run_write_dto):
        return cls(0, dto.process_run_uid, dto.process_run_name, dto.tenant_uid, dto.account_uid, dto.process_uid, dto.status_name, dto.run_time, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, dto.custom_attributes)
    def clone_read(self):
        return process_run_read_dto(self.process_run_uid, self.process_run_name, self.tenant_uid, self.account_uid, self.process_uid, self.status_name, self.run_time, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes)
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["process_run_uid"], d["process_run_name"], d["tenant_uid"], d["account_uid"], d["process_uid"], d["status_name"], d["run_time"], d["row_instance"], d["row_lock"], d["row_owner"], d["row_seq"], d["row_guid"], d["row_version"], d["is_active"], d["created_date"], d["created_by"], d["last_updated_date"], d["last_updated_by"], d["removed_date"], d["removed_by"], d["custom_attributes"])
    def to_read_dict(self) -> dict:
        return asdict(self)
    def to_write(self) -> process_run_write_dto:
        return process_run_write_dto(self.process_run_uid, self.process_run_name, self.tenant_uid, self.account_uid, self.process_uid, self.status_name, self.run_time, self.custom_attributes)
    def to_thin(self) -> process_run_thin_dto:
        return process_run_thin_dto(self.process_run_uid, self.process_run_name, self.created_date, self.is_active)
    def touch(self, updated_by: str = "system"):
        self.last_updated_date = datetime.datetime.now()
        self.last_updated_by = updated_by
        self.row_version = self.row_version+1
    def get_list_all_values(self) -> list[any]:
        return [self.process_run_uid, self.process_run_name, self.tenant_uid, self.account_uid, self.process_uid, self.status_name, self.run_time, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]
    def get_list_update_values(self, updated_by: str) -> list[any]:
        return [self.process_run_name, self.tenant_uid, self.account_uid, self.process_uid, self.status_name, self.run_time, self.custom_attributes, updated_by, self.process_run_uid]
    def is_older_than(self, dt: datetime.datetime) -> bool:
        return self.created_date < dt
    def is_newer_than(self, dt: datetime.datetime) -> bool:
        return self.created_date > dt
    def to_json_read(self) -> str:
        return json.dumps(self.to_read_dict())


@dataclass(frozen=False)
class process_type_read_dto(base_read_dto, process_type_write_dto):
    process_type_uid: str
    process_type_name: str
    class_name: str
    row_instance: str
    row_lock: str | None
    row_owner: str
    row_seq: int
    row_guid: str
    row_version: int
    is_active: int
    created_date: datetime.datetime
    created_by: str
    last_updated_date: datetime.datetime
    last_updated_by: str
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str
    def __init__(self, process_type_uid: str, process_type_name: str, class_name: str, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
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
    @classmethod
    def empty_read(cls):
        return cls(0, "", "", "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def default_read(cls):
        return cls(0, base_dto.get_random_uid(), "", "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def random_read(cls):
        return cls(0, base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_default(cls, process_type_uid: str, process_type_name: str, class_name: str):
        return cls(0, process_type_uid, process_type_name, class_name, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_full(cls, process_type_uid: str, process_type_name: str, class_name: str, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
        return cls(process_type_uid, process_type_name, class_name, row_instance, row_lock, row_owner, row_seq, row_guid, row_version, is_active, created_date, created_by, last_updated_date, last_updated_by, removed_date, removed_by, custom_attributes)
    @classmethod
    def from_write(cls, dto: process_type_write_dto):
        return cls(0, dto.process_type_uid, dto.process_type_name, dto.class_name, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, dto.custom_attributes)
    def clone_read(self):
        return process_type_read_dto(self.process_type_uid, self.process_type_name, self.class_name, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes)
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["process_type_uid"], d["process_type_name"], d["class_name"], d["row_instance"], d["row_lock"], d["row_owner"], d["row_seq"], d["row_guid"], d["row_version"], d["is_active"], d["created_date"], d["created_by"], d["last_updated_date"], d["last_updated_by"], d["removed_date"], d["removed_by"], d["custom_attributes"])
    def to_read_dict(self) -> dict:
        return asdict(self)
    def to_write(self) -> process_type_write_dto:
        return process_type_write_dto(self.process_type_uid, self.process_type_name, self.class_name, self.custom_attributes)
    def to_thin(self) -> process_type_thin_dto:
        return process_type_thin_dto(self.process_type_uid, self.process_type_name, self.created_date, self.is_active)
    def touch(self, updated_by: str = "system"):
        self.last_updated_date = datetime.datetime.now()
        self.last_updated_by = updated_by
        self.row_version = self.row_version+1
    def get_list_all_values(self) -> list[any]:
        return [self.process_type_uid, self.process_type_name, self.class_name, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]
    def get_list_update_values(self, updated_by: str) -> list[any]:
        return [self.process_type_name, self.class_name, self.custom_attributes, updated_by, self.process_type_uid]
    def is_older_than(self, dt: datetime.datetime) -> bool:
        return self.created_date < dt
    def is_newer_than(self, dt: datetime.datetime) -> bool:
        return self.created_date > dt
    def to_json_read(self) -> str:
        return json.dumps(self.to_read_dict())


@dataclass(frozen=False)
class project_account_read_dto(base_read_dto, project_account_write_dto):
    project_account_uid: str
    project_account_name: str
    tenant_uid: str
    client_uid: str
    account_uid: str
    project_instance_uid: str
    start_date: datetime.datetime | None
    end_date: datetime.datetime | None
    row_instance: str
    row_lock: str | None
    row_owner: str
    row_seq: int
    row_guid: str
    row_version: int
    is_active: int
    created_date: datetime.datetime
    created_by: str
    last_updated_date: datetime.datetime
    last_updated_by: str
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str
    def __init__(self, project_account_uid: str, project_account_name: str, tenant_uid: str, client_uid: str, account_uid: str, project_instance_uid: str, start_date: datetime.datetime | None, end_date: datetime.datetime | None, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
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
    @classmethod
    def empty_read(cls):
        return cls(0, "", "", "", "", "", "", datetime.datetime.now(), datetime.datetime.now(), "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def default_read(cls):
        return cls(0, base_dto.get_random_uid(), "", "", "", "", "", datetime.datetime.now(), datetime.datetime.now(), "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def random_read(cls):
        return cls(0, base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), datetime.datetime.now(), datetime.datetime.now(), "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_default(cls, project_account_uid: str, project_account_name: str, tenant_uid: str, client_uid: str, account_uid: str, project_instance_uid: str, start_date: datetime.datetime | None, end_date: datetime.datetime | None):
        return cls(0, project_account_uid, project_account_name, tenant_uid, client_uid, account_uid, project_instance_uid, start_date, end_date, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_full(cls, project_account_uid: str, project_account_name: str, tenant_uid: str, client_uid: str, account_uid: str, project_instance_uid: str, start_date: datetime.datetime | None, end_date: datetime.datetime | None, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
        return cls(project_account_uid, project_account_name, tenant_uid, client_uid, account_uid, project_instance_uid, start_date, end_date, row_instance, row_lock, row_owner, row_seq, row_guid, row_version, is_active, created_date, created_by, last_updated_date, last_updated_by, removed_date, removed_by, custom_attributes)
    @classmethod
    def from_write(cls, dto: project_account_write_dto):
        return cls(0, dto.project_account_uid, dto.project_account_name, dto.tenant_uid, dto.client_uid, dto.account_uid, dto.project_instance_uid, dto.start_date, dto.end_date, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, dto.custom_attributes)
    def clone_read(self):
        return project_account_read_dto(self.project_account_uid, self.project_account_name, self.tenant_uid, self.client_uid, self.account_uid, self.project_instance_uid, self.start_date, self.end_date, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes)
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["project_account_uid"], d["project_account_name"], d["tenant_uid"], d["client_uid"], d["account_uid"], d["project_instance_uid"], d["start_date"], d["end_date"], d["row_instance"], d["row_lock"], d["row_owner"], d["row_seq"], d["row_guid"], d["row_version"], d["is_active"], d["created_date"], d["created_by"], d["last_updated_date"], d["last_updated_by"], d["removed_date"], d["removed_by"], d["custom_attributes"])
    def to_read_dict(self) -> dict:
        return asdict(self)
    def to_write(self) -> project_account_write_dto:
        return project_account_write_dto(self.project_account_uid, self.project_account_name, self.tenant_uid, self.client_uid, self.account_uid, self.project_instance_uid, self.start_date, self.end_date, self.custom_attributes)
    def to_thin(self) -> project_account_thin_dto:
        return project_account_thin_dto(self.project_account_uid, self.project_account_name, self.created_date, self.is_active)
    def touch(self, updated_by: str = "system"):
        self.last_updated_date = datetime.datetime.now()
        self.last_updated_by = updated_by
        self.row_version = self.row_version+1
    def get_list_all_values(self) -> list[any]:
        return [self.project_account_uid, self.project_account_name, self.tenant_uid, self.client_uid, self.account_uid, self.project_instance_uid, self.start_date, self.end_date, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]
    def get_list_update_values(self, updated_by: str) -> list[any]:
        return [self.project_account_name, self.tenant_uid, self.client_uid, self.account_uid, self.project_instance_uid, self.start_date, self.end_date, self.custom_attributes, updated_by, self.project_account_uid]
    def is_older_than(self, dt: datetime.datetime) -> bool:
        return self.created_date < dt
    def is_newer_than(self, dt: datetime.datetime) -> bool:
        return self.created_date > dt
    def to_json_read(self) -> str:
        return json.dumps(self.to_read_dict())


@dataclass(frozen=False)
class project_budget_read_dto(base_read_dto, project_budget_write_dto):
    project_budget_uid: str
    project_budget_name: str
    tenant_uid: str
    client_uid: str
    project_instance_uid: str
    currency_uid: str
    budget_value: str
    is_approved: int
    is_current: int
    row_instance: str
    row_lock: str | None
    row_owner: str
    row_seq: int
    row_guid: str
    row_version: int
    is_active: int
    created_date: datetime.datetime
    created_by: str
    last_updated_date: datetime.datetime
    last_updated_by: str
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str
    def __init__(self, project_budget_uid: str, project_budget_name: str, tenant_uid: str, client_uid: str, project_instance_uid: str, currency_uid: str, budget_value: str, is_approved: int, is_current: int, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
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
    @classmethod
    def empty_read(cls):
        return cls(0, "", "", "", "", "", "", "", 0, 0, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def default_read(cls):
        return cls(0, base_dto.get_random_uid(), "", "", "", "", "", "", 0, 0, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def random_read(cls):
        return cls(0, base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), "", 0, 0, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_default(cls, project_budget_uid: str, project_budget_name: str, tenant_uid: str, client_uid: str, project_instance_uid: str, currency_uid: str, budget_value: str, is_approved: int, is_current: int):
        return cls(0, project_budget_uid, project_budget_name, tenant_uid, client_uid, project_instance_uid, currency_uid, budget_value, is_approved, is_current, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_full(cls, project_budget_uid: str, project_budget_name: str, tenant_uid: str, client_uid: str, project_instance_uid: str, currency_uid: str, budget_value: str, is_approved: int, is_current: int, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
        return cls(project_budget_uid, project_budget_name, tenant_uid, client_uid, project_instance_uid, currency_uid, budget_value, is_approved, is_current, row_instance, row_lock, row_owner, row_seq, row_guid, row_version, is_active, created_date, created_by, last_updated_date, last_updated_by, removed_date, removed_by, custom_attributes)
    @classmethod
    def from_write(cls, dto: project_budget_write_dto):
        return cls(0, dto.project_budget_uid, dto.project_budget_name, dto.tenant_uid, dto.client_uid, dto.project_instance_uid, dto.currency_uid, dto.budget_value, dto.is_approved, dto.is_current, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, dto.custom_attributes)
    def clone_read(self):
        return project_budget_read_dto(self.project_budget_uid, self.project_budget_name, self.tenant_uid, self.client_uid, self.project_instance_uid, self.currency_uid, self.budget_value, self.is_approved, self.is_current, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes)
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["project_budget_uid"], d["project_budget_name"], d["tenant_uid"], d["client_uid"], d["project_instance_uid"], d["currency_uid"], d["budget_value"], d["is_approved"], d["is_current"], d["row_instance"], d["row_lock"], d["row_owner"], d["row_seq"], d["row_guid"], d["row_version"], d["is_active"], d["created_date"], d["created_by"], d["last_updated_date"], d["last_updated_by"], d["removed_date"], d["removed_by"], d["custom_attributes"])
    def to_read_dict(self) -> dict:
        return asdict(self)
    def to_write(self) -> project_budget_write_dto:
        return project_budget_write_dto(self.project_budget_uid, self.project_budget_name, self.tenant_uid, self.client_uid, self.project_instance_uid, self.currency_uid, self.budget_value, self.is_approved, self.is_current, self.custom_attributes)
    def to_thin(self) -> project_budget_thin_dto:
        return project_budget_thin_dto(self.project_budget_uid, self.project_budget_name, self.created_date, self.is_active)
    def touch(self, updated_by: str = "system"):
        self.last_updated_date = datetime.datetime.now()
        self.last_updated_by = updated_by
        self.row_version = self.row_version+1
    def get_list_all_values(self) -> list[any]:
        return [self.project_budget_uid, self.project_budget_name, self.tenant_uid, self.client_uid, self.project_instance_uid, self.currency_uid, self.budget_value, self.is_approved, self.is_current, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]
    def get_list_update_values(self, updated_by: str) -> list[any]:
        return [self.project_budget_name, self.tenant_uid, self.client_uid, self.project_instance_uid, self.currency_uid, self.budget_value, self.is_approved, self.is_current, self.custom_attributes, updated_by, self.project_budget_uid]
    def is_older_than(self, dt: datetime.datetime) -> bool:
        return self.created_date < dt
    def is_newer_than(self, dt: datetime.datetime) -> bool:
        return self.created_date > dt
    def to_json_read(self) -> str:
        return json.dumps(self.to_read_dict())


@dataclass(frozen=False)
class project_group_read_dto(base_read_dto, project_group_write_dto):
    project_group_uid: str
    project_group_name: str
    tenant_uid: str
    project_group_description: str
    row_instance: str
    row_lock: str | None
    row_owner: str
    row_seq: int
    row_guid: str
    row_version: int
    is_active: int
    created_date: datetime.datetime
    created_by: str
    last_updated_date: datetime.datetime
    last_updated_by: str
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str
    def __init__(self, project_group_uid: str, project_group_name: str, tenant_uid: str, project_group_description: str, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
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
    @classmethod
    def empty_read(cls):
        return cls(0, "", "", "", "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def default_read(cls):
        return cls(0, base_dto.get_random_uid(), "", "", "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def random_read(cls):
        return cls(0, base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_default(cls, project_group_uid: str, project_group_name: str, tenant_uid: str, project_group_description: str):
        return cls(0, project_group_uid, project_group_name, tenant_uid, project_group_description, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_full(cls, project_group_uid: str, project_group_name: str, tenant_uid: str, project_group_description: str, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
        return cls(project_group_uid, project_group_name, tenant_uid, project_group_description, row_instance, row_lock, row_owner, row_seq, row_guid, row_version, is_active, created_date, created_by, last_updated_date, last_updated_by, removed_date, removed_by, custom_attributes)
    @classmethod
    def from_write(cls, dto: project_group_write_dto):
        return cls(0, dto.project_group_uid, dto.project_group_name, dto.tenant_uid, dto.project_group_description, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, dto.custom_attributes)
    def clone_read(self):
        return project_group_read_dto(self.project_group_uid, self.project_group_name, self.tenant_uid, self.project_group_description, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes)
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["project_group_uid"], d["project_group_name"], d["tenant_uid"], d["project_group_description"], d["row_instance"], d["row_lock"], d["row_owner"], d["row_seq"], d["row_guid"], d["row_version"], d["is_active"], d["created_date"], d["created_by"], d["last_updated_date"], d["last_updated_by"], d["removed_date"], d["removed_by"], d["custom_attributes"])
    def to_read_dict(self) -> dict:
        return asdict(self)
    def to_write(self) -> project_group_write_dto:
        return project_group_write_dto(self.project_group_uid, self.project_group_name, self.tenant_uid, self.project_group_description, self.custom_attributes)
    def to_thin(self) -> project_group_thin_dto:
        return project_group_thin_dto(self.project_group_uid, self.project_group_name, self.created_date, self.is_active)
    def touch(self, updated_by: str = "system"):
        self.last_updated_date = datetime.datetime.now()
        self.last_updated_by = updated_by
        self.row_version = self.row_version+1
    def get_list_all_values(self) -> list[any]:
        return [self.project_group_uid, self.project_group_name, self.tenant_uid, self.project_group_description, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]
    def get_list_update_values(self, updated_by: str) -> list[any]:
        return [self.project_group_name, self.tenant_uid, self.project_group_description, self.custom_attributes, updated_by, self.project_group_uid]
    def is_older_than(self, dt: datetime.datetime) -> bool:
        return self.created_date < dt
    def is_newer_than(self, dt: datetime.datetime) -> bool:
        return self.created_date > dt
    def to_json_read(self) -> str:
        return json.dumps(self.to_read_dict())


@dataclass(frozen=False)
class project_instance_read_dto(base_read_dto, project_instance_write_dto):
    project_instance_uid: str
    project_instance_name: str
    tenant_uid: str
    client_uid: str
    project_type_uid: str
    manager_account_uid: str
    project_group_uid: str
    project_code: str
    project_description: str
    is_billable: int
    start_date: datetime.datetime | None
    end_date: datetime.datetime | None
    current_billed: str
    budget: str
    row_instance: str
    row_lock: str | None
    row_owner: str
    row_seq: int
    row_guid: str
    row_version: int
    is_active: int
    created_date: datetime.datetime
    created_by: str
    last_updated_date: datetime.datetime
    last_updated_by: str
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str
    def __init__(self, project_instance_uid: str, project_instance_name: str, tenant_uid: str, client_uid: str, project_type_uid: str, manager_account_uid: str, project_group_uid: str, project_code: str, project_description: str, is_billable: int, start_date: datetime.datetime | None, end_date: datetime.datetime | None, current_billed: str, budget: str, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
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
    @classmethod
    def empty_read(cls):
        return cls(0, "", "", "", "", "", "", "", "", "", 0, datetime.datetime.now(), datetime.datetime.now(), "", "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def default_read(cls):
        return cls(0, base_dto.get_random_uid(), "", "", "", "", "", "", "", "", 0, datetime.datetime.now(), datetime.datetime.now(), "", "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def random_read(cls):
        return cls(0, base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), 0, datetime.datetime.now(), datetime.datetime.now(), "", "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_default(cls, project_instance_uid: str, project_instance_name: str, tenant_uid: str, client_uid: str, project_type_uid: str, manager_account_uid: str, project_group_uid: str, project_code: str, project_description: str, is_billable: int, start_date: datetime.datetime | None, end_date: datetime.datetime | None, current_billed: str, budget: str):
        return cls(0, project_instance_uid, project_instance_name, tenant_uid, client_uid, project_type_uid, manager_account_uid, project_group_uid, project_code, project_description, is_billable, start_date, end_date, current_billed, budget, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_full(cls, project_instance_uid: str, project_instance_name: str, tenant_uid: str, client_uid: str, project_type_uid: str, manager_account_uid: str, project_group_uid: str, project_code: str, project_description: str, is_billable: int, start_date: datetime.datetime | None, end_date: datetime.datetime | None, current_billed: str, budget: str, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
        return cls(project_instance_uid, project_instance_name, tenant_uid, client_uid, project_type_uid, manager_account_uid, project_group_uid, project_code, project_description, is_billable, start_date, end_date, current_billed, budget, row_instance, row_lock, row_owner, row_seq, row_guid, row_version, is_active, created_date, created_by, last_updated_date, last_updated_by, removed_date, removed_by, custom_attributes)
    @classmethod
    def from_write(cls, dto: project_instance_write_dto):
        return cls(0, dto.project_instance_uid, dto.project_instance_name, dto.tenant_uid, dto.client_uid, dto.project_type_uid, dto.manager_account_uid, dto.project_group_uid, dto.project_code, dto.project_description, dto.is_billable, dto.start_date, dto.end_date, dto.current_billed, dto.budget, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, dto.custom_attributes)
    def clone_read(self):
        return project_instance_read_dto(self.project_instance_uid, self.project_instance_name, self.tenant_uid, self.client_uid, self.project_type_uid, self.manager_account_uid, self.project_group_uid, self.project_code, self.project_description, self.is_billable, self.start_date, self.end_date, self.current_billed, self.budget, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes)
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["project_instance_uid"], d["project_instance_name"], d["tenant_uid"], d["client_uid"], d["project_type_uid"], d["manager_account_uid"], d["project_group_uid"], d["project_code"], d["project_description"], d["is_billable"], d["start_date"], d["end_date"], d["current_billed"], d["budget"], d["row_instance"], d["row_lock"], d["row_owner"], d["row_seq"], d["row_guid"], d["row_version"], d["is_active"], d["created_date"], d["created_by"], d["last_updated_date"], d["last_updated_by"], d["removed_date"], d["removed_by"], d["custom_attributes"])
    def to_read_dict(self) -> dict:
        return asdict(self)
    def to_write(self) -> project_instance_write_dto:
        return project_instance_write_dto(self.project_instance_uid, self.project_instance_name, self.tenant_uid, self.client_uid, self.project_type_uid, self.manager_account_uid, self.project_group_uid, self.project_code, self.project_description, self.is_billable, self.start_date, self.end_date, self.current_billed, self.budget, self.custom_attributes)
    def to_thin(self) -> project_instance_thin_dto:
        return project_instance_thin_dto(self.project_instance_uid, self.project_instance_name, self.created_date, self.is_active)
    def touch(self, updated_by: str = "system"):
        self.last_updated_date = datetime.datetime.now()
        self.last_updated_by = updated_by
        self.row_version = self.row_version+1
    def get_list_all_values(self) -> list[any]:
        return [self.project_instance_uid, self.project_instance_name, self.tenant_uid, self.client_uid, self.project_type_uid, self.manager_account_uid, self.project_group_uid, self.project_code, self.project_description, self.is_billable, self.start_date, self.end_date, self.current_billed, self.budget, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]
    def get_list_update_values(self, updated_by: str) -> list[any]:
        return [self.project_instance_name, self.tenant_uid, self.client_uid, self.project_type_uid, self.manager_account_uid, self.project_group_uid, self.project_code, self.project_description, self.is_billable, self.start_date, self.end_date, self.current_billed, self.budget, self.custom_attributes, updated_by, self.project_instance_uid]
    def is_older_than(self, dt: datetime.datetime) -> bool:
        return self.created_date < dt
    def is_newer_than(self, dt: datetime.datetime) -> bool:
        return self.created_date > dt
    def to_json_read(self) -> str:
        return json.dumps(self.to_read_dict())


@dataclass(frozen=False)
class project_milestone_read_dto(base_read_dto, project_milestone_write_dto):
    project_milestone_uid: str
    project_milestone_name: str
    tenant_uid: str
    client_uid: str
    project_instance_uid: str
    project_budget_uid: str | None
    start_date: datetime.datetime
    end_date: datetime.datetime
    status_name: str
    row_instance: str
    row_lock: str | None
    row_owner: str
    row_seq: int
    row_guid: str
    row_version: int
    is_active: int
    created_date: datetime.datetime
    created_by: str
    last_updated_date: datetime.datetime
    last_updated_by: str
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str
    def __init__(self, project_milestone_uid: str, project_milestone_name: str, tenant_uid: str, client_uid: str, project_instance_uid: str, project_budget_uid: str | None, start_date: datetime.datetime, end_date: datetime.datetime, status_name: str, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
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
    @classmethod
    def empty_read(cls):
        return cls(0, "", "", "", "", "", "", datetime.datetime.now(), datetime.datetime.now(), "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def default_read(cls):
        return cls(0, base_dto.get_random_uid(), "", "", "", "", "", datetime.datetime.now(), datetime.datetime.now(), "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def random_read(cls):
        return cls(0, base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), datetime.datetime.now(), datetime.datetime.now(), base_dto.get_random_uid(), "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_default(cls, project_milestone_uid: str, project_milestone_name: str, tenant_uid: str, client_uid: str, project_instance_uid: str, project_budget_uid: str | None, start_date: datetime.datetime, end_date: datetime.datetime, status_name: str):
        return cls(0, project_milestone_uid, project_milestone_name, tenant_uid, client_uid, project_instance_uid, project_budget_uid, start_date, end_date, status_name, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_full(cls, project_milestone_uid: str, project_milestone_name: str, tenant_uid: str, client_uid: str, project_instance_uid: str, project_budget_uid: str | None, start_date: datetime.datetime, end_date: datetime.datetime, status_name: str, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
        return cls(project_milestone_uid, project_milestone_name, tenant_uid, client_uid, project_instance_uid, project_budget_uid, start_date, end_date, status_name, row_instance, row_lock, row_owner, row_seq, row_guid, row_version, is_active, created_date, created_by, last_updated_date, last_updated_by, removed_date, removed_by, custom_attributes)
    @classmethod
    def from_write(cls, dto: project_milestone_write_dto):
        return cls(0, dto.project_milestone_uid, dto.project_milestone_name, dto.tenant_uid, dto.client_uid, dto.project_instance_uid, dto.project_budget_uid, dto.start_date, dto.end_date, dto.status_name, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, dto.custom_attributes)
    def clone_read(self):
        return project_milestone_read_dto(self.project_milestone_uid, self.project_milestone_name, self.tenant_uid, self.client_uid, self.project_instance_uid, self.project_budget_uid, self.start_date, self.end_date, self.status_name, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes)
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["project_milestone_uid"], d["project_milestone_name"], d["tenant_uid"], d["client_uid"], d["project_instance_uid"], d["project_budget_uid"], d["start_date"], d["end_date"], d["status_name"], d["row_instance"], d["row_lock"], d["row_owner"], d["row_seq"], d["row_guid"], d["row_version"], d["is_active"], d["created_date"], d["created_by"], d["last_updated_date"], d["last_updated_by"], d["removed_date"], d["removed_by"], d["custom_attributes"])
    def to_read_dict(self) -> dict:
        return asdict(self)
    def to_write(self) -> project_milestone_write_dto:
        return project_milestone_write_dto(self.project_milestone_uid, self.project_milestone_name, self.tenant_uid, self.client_uid, self.project_instance_uid, self.project_budget_uid, self.start_date, self.end_date, self.status_name, self.custom_attributes)
    def to_thin(self) -> project_milestone_thin_dto:
        return project_milestone_thin_dto(self.project_milestone_uid, self.project_milestone_name, self.created_date, self.is_active)
    def touch(self, updated_by: str = "system"):
        self.last_updated_date = datetime.datetime.now()
        self.last_updated_by = updated_by
        self.row_version = self.row_version+1
    def get_list_all_values(self) -> list[any]:
        return [self.project_milestone_uid, self.project_milestone_name, self.tenant_uid, self.client_uid, self.project_instance_uid, self.project_budget_uid, self.start_date, self.end_date, self.status_name, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]
    def get_list_update_values(self, updated_by: str) -> list[any]:
        return [self.project_milestone_name, self.tenant_uid, self.client_uid, self.project_instance_uid, self.project_budget_uid, self.start_date, self.end_date, self.status_name, self.custom_attributes, updated_by, self.project_milestone_uid]
    def is_older_than(self, dt: datetime.datetime) -> bool:
        return self.created_date < dt
    def is_newer_than(self, dt: datetime.datetime) -> bool:
        return self.created_date > dt
    def to_json_read(self) -> str:
        return json.dumps(self.to_read_dict())


@dataclass(frozen=False)
class project_type_read_dto(base_read_dto, project_type_write_dto):
    project_type_uid: str
    project_type_name: str
    project_type_description: str
    row_instance: str
    row_lock: str | None
    row_owner: str
    row_seq: int
    row_guid: str
    row_version: int
    is_active: int
    created_date: datetime.datetime
    created_by: str
    last_updated_date: datetime.datetime
    last_updated_by: str
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str
    def __init__(self, project_type_uid: str, project_type_name: str, project_type_description: str, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
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
    @classmethod
    def empty_read(cls):
        return cls(0, "", "", "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def default_read(cls):
        return cls(0, base_dto.get_random_uid(), "", "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def random_read(cls):
        return cls(0, base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_default(cls, project_type_uid: str, project_type_name: str, project_type_description: str):
        return cls(0, project_type_uid, project_type_name, project_type_description, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_full(cls, project_type_uid: str, project_type_name: str, project_type_description: str, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
        return cls(project_type_uid, project_type_name, project_type_description, row_instance, row_lock, row_owner, row_seq, row_guid, row_version, is_active, created_date, created_by, last_updated_date, last_updated_by, removed_date, removed_by, custom_attributes)
    @classmethod
    def from_write(cls, dto: project_type_write_dto):
        return cls(0, dto.project_type_uid, dto.project_type_name, dto.project_type_description, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, dto.custom_attributes)
    def clone_read(self):
        return project_type_read_dto(self.project_type_uid, self.project_type_name, self.project_type_description, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes)
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["project_type_uid"], d["project_type_name"], d["project_type_description"], d["row_instance"], d["row_lock"], d["row_owner"], d["row_seq"], d["row_guid"], d["row_version"], d["is_active"], d["created_date"], d["created_by"], d["last_updated_date"], d["last_updated_by"], d["removed_date"], d["removed_by"], d["custom_attributes"])
    def to_read_dict(self) -> dict:
        return asdict(self)
    def to_write(self) -> project_type_write_dto:
        return project_type_write_dto(self.project_type_uid, self.project_type_name, self.project_type_description, self.custom_attributes)
    def to_thin(self) -> project_type_thin_dto:
        return project_type_thin_dto(self.project_type_uid, self.project_type_name, self.created_date, self.is_active)
    def touch(self, updated_by: str = "system"):
        self.last_updated_date = datetime.datetime.now()
        self.last_updated_by = updated_by
        self.row_version = self.row_version+1
    def get_list_all_values(self) -> list[any]:
        return [self.project_type_uid, self.project_type_name, self.project_type_description, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]
    def get_list_update_values(self, updated_by: str) -> list[any]:
        return [self.project_type_name, self.project_type_description, self.custom_attributes, updated_by, self.project_type_uid]
    def is_older_than(self, dt: datetime.datetime) -> bool:
        return self.created_date < dt
    def is_newer_than(self, dt: datetime.datetime) -> bool:
        return self.created_date > dt
    def to_json_read(self) -> str:
        return json.dumps(self.to_read_dict())


@dataclass(frozen=False)
class report_read_dto(base_read_dto, report_write_dto):
    report_uid: str
    report_name: str
    tenant_uid: str
    account_uid: str
    report_status_uid: str
    report_query: str
    report_parameters: str
    row_instance: str
    row_lock: str | None
    row_owner: str
    row_seq: int
    row_guid: str
    row_version: int
    is_active: int
    created_date: datetime.datetime
    created_by: str
    last_updated_date: datetime.datetime
    last_updated_by: str
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str
    def __init__(self, report_uid: str, report_name: str, tenant_uid: str, account_uid: str, report_status_uid: str, report_query: str, report_parameters: str, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
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
    @classmethod
    def empty_read(cls):
        return cls(0, "", "", "", "", "", "", "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def default_read(cls):
        return cls(0, base_dto.get_random_uid(), "", "", "", "", "", "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def random_read(cls):
        return cls(0, base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_default(cls, report_uid: str, report_name: str, tenant_uid: str, account_uid: str, report_status_uid: str, report_query: str, report_parameters: str):
        return cls(0, report_uid, report_name, tenant_uid, account_uid, report_status_uid, report_query, report_parameters, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_full(cls, report_uid: str, report_name: str, tenant_uid: str, account_uid: str, report_status_uid: str, report_query: str, report_parameters: str, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
        return cls(report_uid, report_name, tenant_uid, account_uid, report_status_uid, report_query, report_parameters, row_instance, row_lock, row_owner, row_seq, row_guid, row_version, is_active, created_date, created_by, last_updated_date, last_updated_by, removed_date, removed_by, custom_attributes)
    @classmethod
    def from_write(cls, dto: report_write_dto):
        return cls(0, dto.report_uid, dto.report_name, dto.tenant_uid, dto.account_uid, dto.report_status_uid, dto.report_query, dto.report_parameters, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, dto.custom_attributes)
    def clone_read(self):
        return report_read_dto(self.report_uid, self.report_name, self.tenant_uid, self.account_uid, self.report_status_uid, self.report_query, self.report_parameters, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes)
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["report_uid"], d["report_name"], d["tenant_uid"], d["account_uid"], d["report_status_uid"], d["report_query"], d["report_parameters"], d["row_instance"], d["row_lock"], d["row_owner"], d["row_seq"], d["row_guid"], d["row_version"], d["is_active"], d["created_date"], d["created_by"], d["last_updated_date"], d["last_updated_by"], d["removed_date"], d["removed_by"], d["custom_attributes"])
    def to_read_dict(self) -> dict:
        return asdict(self)
    def to_write(self) -> report_write_dto:
        return report_write_dto(self.report_uid, self.report_name, self.tenant_uid, self.account_uid, self.report_status_uid, self.report_query, self.report_parameters, self.custom_attributes)
    def to_thin(self) -> report_thin_dto:
        return report_thin_dto(self.report_uid, self.report_name, self.created_date, self.is_active)
    def touch(self, updated_by: str = "system"):
        self.last_updated_date = datetime.datetime.now()
        self.last_updated_by = updated_by
        self.row_version = self.row_version+1
    def get_list_all_values(self) -> list[any]:
        return [self.report_uid, self.report_name, self.tenant_uid, self.account_uid, self.report_status_uid, self.report_query, self.report_parameters, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]
    def get_list_update_values(self, updated_by: str) -> list[any]:
        return [self.report_name, self.tenant_uid, self.account_uid, self.report_status_uid, self.report_query, self.report_parameters, self.custom_attributes, updated_by, self.report_uid]
    def is_older_than(self, dt: datetime.datetime) -> bool:
        return self.created_date < dt
    def is_newer_than(self, dt: datetime.datetime) -> bool:
        return self.created_date > dt
    def to_json_read(self) -> str:
        return json.dumps(self.to_read_dict())


@dataclass(frozen=False)
class report_content_type_read_dto(base_read_dto, report_content_type_write_dto):
    report_content_type_uid: str
    report_content_type_name: str
    row_instance: str
    row_lock: str | None
    row_owner: str
    row_seq: int
    row_guid: str
    row_version: int
    is_active: int
    created_date: datetime.datetime
    created_by: str
    last_updated_date: datetime.datetime
    last_updated_by: str
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str
    def __init__(self, report_content_type_uid: str, report_content_type_name: str, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
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
    @classmethod
    def empty_read(cls):
        return cls(0, "", "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def default_read(cls):
        return cls(0, base_dto.get_random_uid(), "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def random_read(cls):
        return cls(0, base_dto.get_random_uid(), base_dto.get_random_uid(), "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_default(cls, report_content_type_uid: str, report_content_type_name: str):
        return cls(0, report_content_type_uid, report_content_type_name, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_full(cls, report_content_type_uid: str, report_content_type_name: str, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
        return cls(report_content_type_uid, report_content_type_name, row_instance, row_lock, row_owner, row_seq, row_guid, row_version, is_active, created_date, created_by, last_updated_date, last_updated_by, removed_date, removed_by, custom_attributes)
    @classmethod
    def from_write(cls, dto: report_content_type_write_dto):
        return cls(0, dto.report_content_type_uid, dto.report_content_type_name, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, dto.custom_attributes)
    def clone_read(self):
        return report_content_type_read_dto(self.report_content_type_uid, self.report_content_type_name, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes)
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["report_content_type_uid"], d["report_content_type_name"], d["row_instance"], d["row_lock"], d["row_owner"], d["row_seq"], d["row_guid"], d["row_version"], d["is_active"], d["created_date"], d["created_by"], d["last_updated_date"], d["last_updated_by"], d["removed_date"], d["removed_by"], d["custom_attributes"])
    def to_read_dict(self) -> dict:
        return asdict(self)
    def to_write(self) -> report_content_type_write_dto:
        return report_content_type_write_dto(self.report_content_type_uid, self.report_content_type_name, self.custom_attributes)
    def to_thin(self) -> report_content_type_thin_dto:
        return report_content_type_thin_dto(self.report_content_type_uid, self.report_content_type_name, self.created_date, self.is_active)
    def touch(self, updated_by: str = "system"):
        self.last_updated_date = datetime.datetime.now()
        self.last_updated_by = updated_by
        self.row_version = self.row_version+1
    def get_list_all_values(self) -> list[any]:
        return [self.report_content_type_uid, self.report_content_type_name, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]
    def get_list_update_values(self, updated_by: str) -> list[any]:
        return [self.report_content_type_name, self.custom_attributes, updated_by, self.report_content_type_uid]
    def is_older_than(self, dt: datetime.datetime) -> bool:
        return self.created_date < dt
    def is_newer_than(self, dt: datetime.datetime) -> bool:
        return self.created_date > dt
    def to_json_read(self) -> str:
        return json.dumps(self.to_read_dict())


@dataclass(frozen=False)
class report_format_read_dto(base_read_dto, report_format_write_dto):
    report_format_uid: str
    report_format_name: str
    class_name: str
    row_instance: str
    row_lock: str | None
    row_owner: str
    row_seq: int
    row_guid: str
    row_version: int
    is_active: int
    created_date: datetime.datetime
    created_by: str
    last_updated_date: datetime.datetime
    last_updated_by: str
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str
    def __init__(self, report_format_uid: str, report_format_name: str, class_name: str, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
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
    @classmethod
    def empty_read(cls):
        return cls(0, "", "", "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def default_read(cls):
        return cls(0, base_dto.get_random_uid(), "", "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def random_read(cls):
        return cls(0, base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_default(cls, report_format_uid: str, report_format_name: str, class_name: str):
        return cls(0, report_format_uid, report_format_name, class_name, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_full(cls, report_format_uid: str, report_format_name: str, class_name: str, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
        return cls(report_format_uid, report_format_name, class_name, row_instance, row_lock, row_owner, row_seq, row_guid, row_version, is_active, created_date, created_by, last_updated_date, last_updated_by, removed_date, removed_by, custom_attributes)
    @classmethod
    def from_write(cls, dto: report_format_write_dto):
        return cls(0, dto.report_format_uid, dto.report_format_name, dto.class_name, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, dto.custom_attributes)
    def clone_read(self):
        return report_format_read_dto(self.report_format_uid, self.report_format_name, self.class_name, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes)
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["report_format_uid"], d["report_format_name"], d["class_name"], d["row_instance"], d["row_lock"], d["row_owner"], d["row_seq"], d["row_guid"], d["row_version"], d["is_active"], d["created_date"], d["created_by"], d["last_updated_date"], d["last_updated_by"], d["removed_date"], d["removed_by"], d["custom_attributes"])
    def to_read_dict(self) -> dict:
        return asdict(self)
    def to_write(self) -> report_format_write_dto:
        return report_format_write_dto(self.report_format_uid, self.report_format_name, self.class_name, self.custom_attributes)
    def to_thin(self) -> report_format_thin_dto:
        return report_format_thin_dto(self.report_format_uid, self.report_format_name, self.created_date, self.is_active)
    def touch(self, updated_by: str = "system"):
        self.last_updated_date = datetime.datetime.now()
        self.last_updated_by = updated_by
        self.row_version = self.row_version+1
    def get_list_all_values(self) -> list[any]:
        return [self.report_format_uid, self.report_format_name, self.class_name, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]
    def get_list_update_values(self, updated_by: str) -> list[any]:
        return [self.report_format_name, self.class_name, self.custom_attributes, updated_by, self.report_format_uid]
    def is_older_than(self, dt: datetime.datetime) -> bool:
        return self.created_date < dt
    def is_newer_than(self, dt: datetime.datetime) -> bool:
        return self.created_date > dt
    def to_json_read(self) -> str:
        return json.dumps(self.to_read_dict())


@dataclass(frozen=False)
class report_run_read_dto(base_read_dto, report_run_write_dto):
    report_run_uid: str
    report_run_name: str
    tenant_uid: str
    account_uid: str
    report_uid: str
    report_format_uid: str
    report_status_uid: str
    report_content_type_uid: str
    input_parameters_json: str
    run_time_ms: int
    returned_rows: int
    content_size: int
    row_instance: str
    row_lock: str | None
    row_owner: str
    row_seq: int
    row_guid: str
    row_version: int
    is_active: int
    created_date: datetime.datetime
    created_by: str
    last_updated_date: datetime.datetime
    last_updated_by: str
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str
    def __init__(self, report_run_uid: str, report_run_name: str, tenant_uid: str, account_uid: str, report_uid: str, report_format_uid: str, report_status_uid: str, report_content_type_uid: str, input_parameters_json: str, run_time_ms: int, returned_rows: int, content_size: int, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
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
    @classmethod
    def empty_read(cls):
        return cls(0, "", "", "", "", "", "", "", "", "", 0, 0, 0, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def default_read(cls):
        return cls(0, base_dto.get_random_uid(), "", "", "", "", "", "", "", "", 0, 0, 0, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def random_read(cls):
        return cls(0, base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), 0, 0, 0, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_default(cls, report_run_uid: str, report_run_name: str, tenant_uid: str, account_uid: str, report_uid: str, report_format_uid: str, report_status_uid: str, report_content_type_uid: str, input_parameters_json: str, run_time_ms: int, returned_rows: int, content_size: int):
        return cls(0, report_run_uid, report_run_name, tenant_uid, account_uid, report_uid, report_format_uid, report_status_uid, report_content_type_uid, input_parameters_json, run_time_ms, returned_rows, content_size, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_full(cls, report_run_uid: str, report_run_name: str, tenant_uid: str, account_uid: str, report_uid: str, report_format_uid: str, report_status_uid: str, report_content_type_uid: str, input_parameters_json: str, run_time_ms: int, returned_rows: int, content_size: int, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
        return cls(report_run_uid, report_run_name, tenant_uid, account_uid, report_uid, report_format_uid, report_status_uid, report_content_type_uid, input_parameters_json, run_time_ms, returned_rows, content_size, row_instance, row_lock, row_owner, row_seq, row_guid, row_version, is_active, created_date, created_by, last_updated_date, last_updated_by, removed_date, removed_by, custom_attributes)
    @classmethod
    def from_write(cls, dto: report_run_write_dto):
        return cls(0, dto.report_run_uid, dto.report_run_name, dto.tenant_uid, dto.account_uid, dto.report_uid, dto.report_format_uid, dto.report_status_uid, dto.report_content_type_uid, dto.input_parameters_json, dto.run_time_ms, dto.returned_rows, dto.content_size, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, dto.custom_attributes)
    def clone_read(self):
        return report_run_read_dto(self.report_run_uid, self.report_run_name, self.tenant_uid, self.account_uid, self.report_uid, self.report_format_uid, self.report_status_uid, self.report_content_type_uid, self.input_parameters_json, self.run_time_ms, self.returned_rows, self.content_size, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes)
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["report_run_uid"], d["report_run_name"], d["tenant_uid"], d["account_uid"], d["report_uid"], d["report_format_uid"], d["report_status_uid"], d["report_content_type_uid"], d["input_parameters_json"], d["run_time_ms"], d["returned_rows"], d["content_size"], d["row_instance"], d["row_lock"], d["row_owner"], d["row_seq"], d["row_guid"], d["row_version"], d["is_active"], d["created_date"], d["created_by"], d["last_updated_date"], d["last_updated_by"], d["removed_date"], d["removed_by"], d["custom_attributes"])
    def to_read_dict(self) -> dict:
        return asdict(self)
    def to_write(self) -> report_run_write_dto:
        return report_run_write_dto(self.report_run_uid, self.report_run_name, self.tenant_uid, self.account_uid, self.report_uid, self.report_format_uid, self.report_status_uid, self.report_content_type_uid, self.input_parameters_json, self.run_time_ms, self.returned_rows, self.content_size, self.custom_attributes)
    def to_thin(self) -> report_run_thin_dto:
        return report_run_thin_dto(self.report_run_uid, self.report_run_name, self.created_date, self.is_active)
    def touch(self, updated_by: str = "system"):
        self.last_updated_date = datetime.datetime.now()
        self.last_updated_by = updated_by
        self.row_version = self.row_version+1
    def get_list_all_values(self) -> list[any]:
        return [self.report_run_uid, self.report_run_name, self.tenant_uid, self.account_uid, self.report_uid, self.report_format_uid, self.report_status_uid, self.report_content_type_uid, self.input_parameters_json, self.run_time_ms, self.returned_rows, self.content_size, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]
    def get_list_update_values(self, updated_by: str) -> list[any]:
        return [self.report_run_name, self.tenant_uid, self.account_uid, self.report_uid, self.report_format_uid, self.report_status_uid, self.report_content_type_uid, self.input_parameters_json, self.run_time_ms, self.returned_rows, self.content_size, self.custom_attributes, updated_by, self.report_run_uid]
    def is_older_than(self, dt: datetime.datetime) -> bool:
        return self.created_date < dt
    def is_newer_than(self, dt: datetime.datetime) -> bool:
        return self.created_date > dt
    def to_json_read(self) -> str:
        return json.dumps(self.to_read_dict())


@dataclass(frozen=False)
class report_status_read_dto(base_read_dto, report_status_write_dto):
    report_status_uid: str
    report_status_name: str
    row_instance: str
    row_lock: str | None
    row_owner: str
    row_seq: int
    row_guid: str
    row_version: int
    is_active: int
    created_date: datetime.datetime
    created_by: str
    last_updated_date: datetime.datetime
    last_updated_by: str
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str
    def __init__(self, report_status_uid: str, report_status_name: str, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
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
    @classmethod
    def empty_read(cls):
        return cls(0, "", "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def default_read(cls):
        return cls(0, base_dto.get_random_uid(), "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def random_read(cls):
        return cls(0, base_dto.get_random_uid(), base_dto.get_random_uid(), "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_default(cls, report_status_uid: str, report_status_name: str):
        return cls(0, report_status_uid, report_status_name, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_full(cls, report_status_uid: str, report_status_name: str, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
        return cls(report_status_uid, report_status_name, row_instance, row_lock, row_owner, row_seq, row_guid, row_version, is_active, created_date, created_by, last_updated_date, last_updated_by, removed_date, removed_by, custom_attributes)
    @classmethod
    def from_write(cls, dto: report_status_write_dto):
        return cls(0, dto.report_status_uid, dto.report_status_name, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, dto.custom_attributes)
    def clone_read(self):
        return report_status_read_dto(self.report_status_uid, self.report_status_name, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes)
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["report_status_uid"], d["report_status_name"], d["row_instance"], d["row_lock"], d["row_owner"], d["row_seq"], d["row_guid"], d["row_version"], d["is_active"], d["created_date"], d["created_by"], d["last_updated_date"], d["last_updated_by"], d["removed_date"], d["removed_by"], d["custom_attributes"])
    def to_read_dict(self) -> dict:
        return asdict(self)
    def to_write(self) -> report_status_write_dto:
        return report_status_write_dto(self.report_status_uid, self.report_status_name, self.custom_attributes)
    def to_thin(self) -> report_status_thin_dto:
        return report_status_thin_dto(self.report_status_uid, self.report_status_name, self.created_date, self.is_active)
    def touch(self, updated_by: str = "system"):
        self.last_updated_date = datetime.datetime.now()
        self.last_updated_by = updated_by
        self.row_version = self.row_version+1
    def get_list_all_values(self) -> list[any]:
        return [self.report_status_uid, self.report_status_name, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]
    def get_list_update_values(self, updated_by: str) -> list[any]:
        return [self.report_status_name, self.custom_attributes, updated_by, self.report_status_uid]
    def is_older_than(self, dt: datetime.datetime) -> bool:
        return self.created_date < dt
    def is_newer_than(self, dt: datetime.datetime) -> bool:
        return self.created_date > dt
    def to_json_read(self) -> str:
        return json.dumps(self.to_read_dict())


@dataclass(frozen=False)
class report_type_read_dto(base_read_dto, report_type_write_dto):
    report_type_uid: str
    report_type_name: str
    row_instance: str
    row_lock: str | None
    row_owner: str
    row_seq: int
    row_guid: str
    row_version: int
    is_active: int
    created_date: datetime.datetime
    created_by: str
    last_updated_date: datetime.datetime
    last_updated_by: str
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str
    def __init__(self, report_type_uid: str, report_type_name: str, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
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
    @classmethod
    def empty_read(cls):
        return cls(0, "", "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def default_read(cls):
        return cls(0, base_dto.get_random_uid(), "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def random_read(cls):
        return cls(0, base_dto.get_random_uid(), base_dto.get_random_uid(), "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_default(cls, report_type_uid: str, report_type_name: str):
        return cls(0, report_type_uid, report_type_name, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_full(cls, report_type_uid: str, report_type_name: str, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
        return cls(report_type_uid, report_type_name, row_instance, row_lock, row_owner, row_seq, row_guid, row_version, is_active, created_date, created_by, last_updated_date, last_updated_by, removed_date, removed_by, custom_attributes)
    @classmethod
    def from_write(cls, dto: report_type_write_dto):
        return cls(0, dto.report_type_uid, dto.report_type_name, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, dto.custom_attributes)
    def clone_read(self):
        return report_type_read_dto(self.report_type_uid, self.report_type_name, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes)
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["report_type_uid"], d["report_type_name"], d["row_instance"], d["row_lock"], d["row_owner"], d["row_seq"], d["row_guid"], d["row_version"], d["is_active"], d["created_date"], d["created_by"], d["last_updated_date"], d["last_updated_by"], d["removed_date"], d["removed_by"], d["custom_attributes"])
    def to_read_dict(self) -> dict:
        return asdict(self)
    def to_write(self) -> report_type_write_dto:
        return report_type_write_dto(self.report_type_uid, self.report_type_name, self.custom_attributes)
    def to_thin(self) -> report_type_thin_dto:
        return report_type_thin_dto(self.report_type_uid, self.report_type_name, self.created_date, self.is_active)
    def touch(self, updated_by: str = "system"):
        self.last_updated_date = datetime.datetime.now()
        self.last_updated_by = updated_by
        self.row_version = self.row_version+1
    def get_list_all_values(self) -> list[any]:
        return [self.report_type_uid, self.report_type_name, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]
    def get_list_update_values(self, updated_by: str) -> list[any]:
        return [self.report_type_name, self.custom_attributes, updated_by, self.report_type_uid]
    def is_older_than(self, dt: datetime.datetime) -> bool:
        return self.created_date < dt
    def is_newer_than(self, dt: datetime.datetime) -> bool:
        return self.created_date > dt
    def to_json_read(self) -> str:
        return json.dumps(self.to_read_dict())


@dataclass(frozen=False)
class storage_read_dto(base_read_dto, storage_write_dto):
    storage_uid: str
    storage_name: str
    tenant_uid: str
    account_uid: str
    storage_type_uid: str
    storage_category_uid: str
    storage_parameters_json: str
    row_instance: str
    row_lock: str | None
    row_owner: str
    row_seq: int
    row_guid: str
    row_version: int
    is_active: int
    created_date: datetime.datetime
    created_by: str
    last_updated_date: datetime.datetime
    last_updated_by: str
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str
    def __init__(self, storage_uid: str, storage_name: str, tenant_uid: str, account_uid: str, storage_type_uid: str, storage_category_uid: str, storage_parameters_json: str, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
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
    @classmethod
    def empty_read(cls):
        return cls(0, "", "", "", "", "", "", "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def default_read(cls):
        return cls(0, base_dto.get_random_uid(), "", "", "", "", "", "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def random_read(cls):
        return cls(0, base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_default(cls, storage_uid: str, storage_name: str, tenant_uid: str, account_uid: str, storage_type_uid: str, storage_category_uid: str, storage_parameters_json: str):
        return cls(0, storage_uid, storage_name, tenant_uid, account_uid, storage_type_uid, storage_category_uid, storage_parameters_json, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_full(cls, storage_uid: str, storage_name: str, tenant_uid: str, account_uid: str, storage_type_uid: str, storage_category_uid: str, storage_parameters_json: str, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
        return cls(storage_uid, storage_name, tenant_uid, account_uid, storage_type_uid, storage_category_uid, storage_parameters_json, row_instance, row_lock, row_owner, row_seq, row_guid, row_version, is_active, created_date, created_by, last_updated_date, last_updated_by, removed_date, removed_by, custom_attributes)
    @classmethod
    def from_write(cls, dto: storage_write_dto):
        return cls(0, dto.storage_uid, dto.storage_name, dto.tenant_uid, dto.account_uid, dto.storage_type_uid, dto.storage_category_uid, dto.storage_parameters_json, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, dto.custom_attributes)
    def clone_read(self):
        return storage_read_dto(self.storage_uid, self.storage_name, self.tenant_uid, self.account_uid, self.storage_type_uid, self.storage_category_uid, self.storage_parameters_json, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes)
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["storage_uid"], d["storage_name"], d["tenant_uid"], d["account_uid"], d["storage_type_uid"], d["storage_category_uid"], d["storage_parameters_json"], d["row_instance"], d["row_lock"], d["row_owner"], d["row_seq"], d["row_guid"], d["row_version"], d["is_active"], d["created_date"], d["created_by"], d["last_updated_date"], d["last_updated_by"], d["removed_date"], d["removed_by"], d["custom_attributes"])
    def to_read_dict(self) -> dict:
        return asdict(self)
    def to_write(self) -> storage_write_dto:
        return storage_write_dto(self.storage_uid, self.storage_name, self.tenant_uid, self.account_uid, self.storage_type_uid, self.storage_category_uid, self.storage_parameters_json, self.custom_attributes)
    def to_thin(self) -> storage_thin_dto:
        return storage_thin_dto(self.storage_uid, self.storage_name, self.created_date, self.is_active)
    def touch(self, updated_by: str = "system"):
        self.last_updated_date = datetime.datetime.now()
        self.last_updated_by = updated_by
        self.row_version = self.row_version+1
    def get_list_all_values(self) -> list[any]:
        return [self.storage_uid, self.storage_name, self.tenant_uid, self.account_uid, self.storage_type_uid, self.storage_category_uid, self.storage_parameters_json, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]
    def get_list_update_values(self, updated_by: str) -> list[any]:
        return [self.storage_name, self.tenant_uid, self.account_uid, self.storage_type_uid, self.storage_category_uid, self.storage_parameters_json, self.custom_attributes, updated_by, self.storage_uid]
    def is_older_than(self, dt: datetime.datetime) -> bool:
        return self.created_date < dt
    def is_newer_than(self, dt: datetime.datetime) -> bool:
        return self.created_date > dt
    def to_json_read(self) -> str:
        return json.dumps(self.to_read_dict())


@dataclass(frozen=False)
class storage_category_read_dto(base_read_dto, storage_category_write_dto):
    storage_category_uid: str
    storage_category_name: str
    row_instance: str
    row_lock: str | None
    row_owner: str
    row_seq: int
    row_guid: str
    row_version: int
    is_active: int
    created_date: datetime.datetime
    created_by: str
    last_updated_date: datetime.datetime
    last_updated_by: str
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str
    def __init__(self, storage_category_uid: str, storage_category_name: str, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
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
    @classmethod
    def empty_read(cls):
        return cls(0, "", "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def default_read(cls):
        return cls(0, base_dto.get_random_uid(), "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def random_read(cls):
        return cls(0, base_dto.get_random_uid(), base_dto.get_random_uid(), "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_default(cls, storage_category_uid: str, storage_category_name: str):
        return cls(0, storage_category_uid, storage_category_name, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_full(cls, storage_category_uid: str, storage_category_name: str, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
        return cls(storage_category_uid, storage_category_name, row_instance, row_lock, row_owner, row_seq, row_guid, row_version, is_active, created_date, created_by, last_updated_date, last_updated_by, removed_date, removed_by, custom_attributes)
    @classmethod
    def from_write(cls, dto: storage_category_write_dto):
        return cls(0, dto.storage_category_uid, dto.storage_category_name, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, dto.custom_attributes)
    def clone_read(self):
        return storage_category_read_dto(self.storage_category_uid, self.storage_category_name, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes)
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["storage_category_uid"], d["storage_category_name"], d["row_instance"], d["row_lock"], d["row_owner"], d["row_seq"], d["row_guid"], d["row_version"], d["is_active"], d["created_date"], d["created_by"], d["last_updated_date"], d["last_updated_by"], d["removed_date"], d["removed_by"], d["custom_attributes"])
    def to_read_dict(self) -> dict:
        return asdict(self)
    def to_write(self) -> storage_category_write_dto:
        return storage_category_write_dto(self.storage_category_uid, self.storage_category_name, self.custom_attributes)
    def to_thin(self) -> storage_category_thin_dto:
        return storage_category_thin_dto(self.storage_category_uid, self.storage_category_name, self.created_date, self.is_active)
    def touch(self, updated_by: str = "system"):
        self.last_updated_date = datetime.datetime.now()
        self.last_updated_by = updated_by
        self.row_version = self.row_version+1
    def get_list_all_values(self) -> list[any]:
        return [self.storage_category_uid, self.storage_category_name, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]
    def get_list_update_values(self, updated_by: str) -> list[any]:
        return [self.storage_category_name, self.custom_attributes, updated_by, self.storage_category_uid]
    def is_older_than(self, dt: datetime.datetime) -> bool:
        return self.created_date < dt
    def is_newer_than(self, dt: datetime.datetime) -> bool:
        return self.created_date > dt
    def to_json_read(self) -> str:
        return json.dumps(self.to_read_dict())


@dataclass(frozen=False)
class storage_connection_read_dto(base_read_dto, storage_connection_write_dto):
    storage_connection_uid: str
    storage_connection_name: str
    storage_uid: str
    connection_type: str
    storage_parameters_json: str
    row_instance: str
    row_lock: str | None
    row_owner: str
    row_seq: int
    row_guid: str
    row_version: int
    is_active: int
    created_date: datetime.datetime
    created_by: str
    last_updated_date: datetime.datetime
    last_updated_by: str
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str
    def __init__(self, storage_connection_uid: str, storage_connection_name: str, storage_uid: str, connection_type: str, storage_parameters_json: str, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
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
    @classmethod
    def empty_read(cls):
        return cls(0, "", "", "", "", "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def default_read(cls):
        return cls(0, base_dto.get_random_uid(), "", "", "", "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def random_read(cls):
        return cls(0, base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_default(cls, storage_connection_uid: str, storage_connection_name: str, storage_uid: str, connection_type: str, storage_parameters_json: str):
        return cls(0, storage_connection_uid, storage_connection_name, storage_uid, connection_type, storage_parameters_json, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_full(cls, storage_connection_uid: str, storage_connection_name: str, storage_uid: str, connection_type: str, storage_parameters_json: str, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
        return cls(storage_connection_uid, storage_connection_name, storage_uid, connection_type, storage_parameters_json, row_instance, row_lock, row_owner, row_seq, row_guid, row_version, is_active, created_date, created_by, last_updated_date, last_updated_by, removed_date, removed_by, custom_attributes)
    @classmethod
    def from_write(cls, dto: storage_connection_write_dto):
        return cls(0, dto.storage_connection_uid, dto.storage_connection_name, dto.storage_uid, dto.connection_type, dto.storage_parameters_json, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, dto.custom_attributes)
    def clone_read(self):
        return storage_connection_read_dto(self.storage_connection_uid, self.storage_connection_name, self.storage_uid, self.connection_type, self.storage_parameters_json, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes)
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["storage_connection_uid"], d["storage_connection_name"], d["storage_uid"], d["connection_type"], d["storage_parameters_json"], d["row_instance"], d["row_lock"], d["row_owner"], d["row_seq"], d["row_guid"], d["row_version"], d["is_active"], d["created_date"], d["created_by"], d["last_updated_date"], d["last_updated_by"], d["removed_date"], d["removed_by"], d["custom_attributes"])
    def to_read_dict(self) -> dict:
        return asdict(self)
    def to_write(self) -> storage_connection_write_dto:
        return storage_connection_write_dto(self.storage_connection_uid, self.storage_connection_name, self.storage_uid, self.connection_type, self.storage_parameters_json, self.custom_attributes)
    def to_thin(self) -> storage_connection_thin_dto:
        return storage_connection_thin_dto(self.storage_connection_uid, self.storage_connection_name, self.created_date, self.is_active)
    def touch(self, updated_by: str = "system"):
        self.last_updated_date = datetime.datetime.now()
        self.last_updated_by = updated_by
        self.row_version = self.row_version+1
    def get_list_all_values(self) -> list[any]:
        return [self.storage_connection_uid, self.storage_connection_name, self.storage_uid, self.connection_type, self.storage_parameters_json, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]
    def get_list_update_values(self, updated_by: str) -> list[any]:
        return [self.storage_connection_name, self.storage_uid, self.connection_type, self.storage_parameters_json, self.custom_attributes, updated_by, self.storage_connection_uid]
    def is_older_than(self, dt: datetime.datetime) -> bool:
        return self.created_date < dt
    def is_newer_than(self, dt: datetime.datetime) -> bool:
        return self.created_date > dt
    def to_json_read(self) -> str:
        return json.dumps(self.to_read_dict())


@dataclass(frozen=False)
class storage_query_read_dto(base_read_dto, storage_query_write_dto):
    storage_query_uid: str
    storage_query_name: str
    storage_uid: str
    query_content: str
    query_parameters_json: str
    execution_status: str
    execution_time: int | None
    execution_rows: int | None
    row_instance: str
    row_lock: str | None
    row_owner: str
    row_seq: int
    row_guid: str
    row_version: int
    is_active: int
    created_date: datetime.datetime
    created_by: str
    last_updated_date: datetime.datetime
    last_updated_by: str
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str
    def __init__(self, storage_query_uid: str, storage_query_name: str, storage_uid: str, query_content: str, query_parameters_json: str, execution_status: str, execution_time: int | None, execution_rows: int | None, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
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
    @classmethod
    def empty_read(cls):
        return cls(0, "", "", "", "", "", "", 0, 0, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def default_read(cls):
        return cls(0, base_dto.get_random_uid(), "", "", "", "", "", 0, 0, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def random_read(cls):
        return cls(0, base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), 0, 0, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_default(cls, storage_query_uid: str, storage_query_name: str, storage_uid: str, query_content: str, query_parameters_json: str, execution_status: str, execution_time: int | None, execution_rows: int | None):
        return cls(0, storage_query_uid, storage_query_name, storage_uid, query_content, query_parameters_json, execution_status, execution_time, execution_rows, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_full(cls, storage_query_uid: str, storage_query_name: str, storage_uid: str, query_content: str, query_parameters_json: str, execution_status: str, execution_time: int | None, execution_rows: int | None, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
        return cls(storage_query_uid, storage_query_name, storage_uid, query_content, query_parameters_json, execution_status, execution_time, execution_rows, row_instance, row_lock, row_owner, row_seq, row_guid, row_version, is_active, created_date, created_by, last_updated_date, last_updated_by, removed_date, removed_by, custom_attributes)
    @classmethod
    def from_write(cls, dto: storage_query_write_dto):
        return cls(0, dto.storage_query_uid, dto.storage_query_name, dto.storage_uid, dto.query_content, dto.query_parameters_json, dto.execution_status, dto.execution_time, dto.execution_rows, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, dto.custom_attributes)
    def clone_read(self):
        return storage_query_read_dto(self.storage_query_uid, self.storage_query_name, self.storage_uid, self.query_content, self.query_parameters_json, self.execution_status, self.execution_time, self.execution_rows, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes)
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["storage_query_uid"], d["storage_query_name"], d["storage_uid"], d["query_content"], d["query_parameters_json"], d["execution_status"], d["execution_time"], d["execution_rows"], d["row_instance"], d["row_lock"], d["row_owner"], d["row_seq"], d["row_guid"], d["row_version"], d["is_active"], d["created_date"], d["created_by"], d["last_updated_date"], d["last_updated_by"], d["removed_date"], d["removed_by"], d["custom_attributes"])
    def to_read_dict(self) -> dict:
        return asdict(self)
    def to_write(self) -> storage_query_write_dto:
        return storage_query_write_dto(self.storage_query_uid, self.storage_query_name, self.storage_uid, self.query_content, self.query_parameters_json, self.execution_status, self.execution_time, self.execution_rows, self.custom_attributes)
    def to_thin(self) -> storage_query_thin_dto:
        return storage_query_thin_dto(self.storage_query_uid, self.storage_query_name, self.created_date, self.is_active)
    def touch(self, updated_by: str = "system"):
        self.last_updated_date = datetime.datetime.now()
        self.last_updated_by = updated_by
        self.row_version = self.row_version+1
    def get_list_all_values(self) -> list[any]:
        return [self.storage_query_uid, self.storage_query_name, self.storage_uid, self.query_content, self.query_parameters_json, self.execution_status, self.execution_time, self.execution_rows, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]
    def get_list_update_values(self, updated_by: str) -> list[any]:
        return [self.storage_query_name, self.storage_uid, self.query_content, self.query_parameters_json, self.execution_status, self.execution_time, self.execution_rows, self.custom_attributes, updated_by, self.storage_query_uid]
    def is_older_than(self, dt: datetime.datetime) -> bool:
        return self.created_date < dt
    def is_newer_than(self, dt: datetime.datetime) -> bool:
        return self.created_date > dt
    def to_json_read(self) -> str:
        return json.dumps(self.to_read_dict())


@dataclass(frozen=False)
class storage_type_read_dto(base_read_dto, storage_type_write_dto):
    storage_type_uid: str
    storage_type_name: str
    storage_class: str
    row_instance: str
    row_lock: str | None
    row_owner: str
    row_seq: int
    row_guid: str
    row_version: int
    is_active: int
    created_date: datetime.datetime
    created_by: str
    last_updated_date: datetime.datetime
    last_updated_by: str
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str
    def __init__(self, storage_type_uid: str, storage_type_name: str, storage_class: str, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
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
    @classmethod
    def empty_read(cls):
        return cls(0, "", "", "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def default_read(cls):
        return cls(0, base_dto.get_random_uid(), "", "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def random_read(cls):
        return cls(0, base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_default(cls, storage_type_uid: str, storage_type_name: str, storage_class: str):
        return cls(0, storage_type_uid, storage_type_name, storage_class, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_full(cls, storage_type_uid: str, storage_type_name: str, storage_class: str, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
        return cls(storage_type_uid, storage_type_name, storage_class, row_instance, row_lock, row_owner, row_seq, row_guid, row_version, is_active, created_date, created_by, last_updated_date, last_updated_by, removed_date, removed_by, custom_attributes)
    @classmethod
    def from_write(cls, dto: storage_type_write_dto):
        return cls(0, dto.storage_type_uid, dto.storage_type_name, dto.storage_class, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, dto.custom_attributes)
    def clone_read(self):
        return storage_type_read_dto(self.storage_type_uid, self.storage_type_name, self.storage_class, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes)
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["storage_type_uid"], d["storage_type_name"], d["storage_class"], d["row_instance"], d["row_lock"], d["row_owner"], d["row_seq"], d["row_guid"], d["row_version"], d["is_active"], d["created_date"], d["created_by"], d["last_updated_date"], d["last_updated_by"], d["removed_date"], d["removed_by"], d["custom_attributes"])
    def to_read_dict(self) -> dict:
        return asdict(self)
    def to_write(self) -> storage_type_write_dto:
        return storage_type_write_dto(self.storage_type_uid, self.storage_type_name, self.storage_class, self.custom_attributes)
    def to_thin(self) -> storage_type_thin_dto:
        return storage_type_thin_dto(self.storage_type_uid, self.storage_type_name, self.created_date, self.is_active)
    def touch(self, updated_by: str = "system"):
        self.last_updated_date = datetime.datetime.now()
        self.last_updated_by = updated_by
        self.row_version = self.row_version+1
    def get_list_all_values(self) -> list[any]:
        return [self.storage_type_uid, self.storage_type_name, self.storage_class, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]
    def get_list_update_values(self, updated_by: str) -> list[any]:
        return [self.storage_type_name, self.storage_class, self.custom_attributes, updated_by, self.storage_type_uid]
    def is_older_than(self, dt: datetime.datetime) -> bool:
        return self.created_date < dt
    def is_newer_than(self, dt: datetime.datetime) -> bool:
        return self.created_date > dt
    def to_json_read(self) -> str:
        return json.dumps(self.to_read_dict())


@dataclass(frozen=False)
class synchronization_read_dto(base_read_dto, synchronization_write_dto):
    synchronization_uid: str
    synchronization_name: str
    tenant_uid: str
    synchronization_type_uid: str
    storage_uid: str
    sync_expression: str
    sync_query: str
    sync_definition: str
    sync_priority: int
    last_run_date: datetime.datetime | None
    last_run_seconds: str | None
    row_instance: str
    row_lock: str | None
    row_owner: str
    row_seq: int
    row_guid: str
    row_version: int
    is_active: int
    created_date: datetime.datetime
    created_by: str
    last_updated_date: datetime.datetime
    last_updated_by: str
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str
    def __init__(self, synchronization_uid: str, synchronization_name: str, tenant_uid: str, synchronization_type_uid: str, storage_uid: str, sync_expression: str, sync_query: str, sync_definition: str, sync_priority: int, last_run_date: datetime.datetime | None, last_run_seconds: str | None, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
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
    @classmethod
    def empty_read(cls):
        return cls(0, "", "", "", "", "", "", "", "", 0, datetime.datetime.now(), "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def default_read(cls):
        return cls(0, base_dto.get_random_uid(), "", "", "", "", "", "", "", 0, datetime.datetime.now(), "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def random_read(cls):
        return cls(0, base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), 0, datetime.datetime.now(), "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_default(cls, synchronization_uid: str, synchronization_name: str, tenant_uid: str, synchronization_type_uid: str, storage_uid: str, sync_expression: str, sync_query: str, sync_definition: str, sync_priority: int, last_run_date: datetime.datetime | None, last_run_seconds: str | None):
        return cls(0, synchronization_uid, synchronization_name, tenant_uid, synchronization_type_uid, storage_uid, sync_expression, sync_query, sync_definition, sync_priority, last_run_date, last_run_seconds, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_full(cls, synchronization_uid: str, synchronization_name: str, tenant_uid: str, synchronization_type_uid: str, storage_uid: str, sync_expression: str, sync_query: str, sync_definition: str, sync_priority: int, last_run_date: datetime.datetime | None, last_run_seconds: str | None, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
        return cls(synchronization_uid, synchronization_name, tenant_uid, synchronization_type_uid, storage_uid, sync_expression, sync_query, sync_definition, sync_priority, last_run_date, last_run_seconds, row_instance, row_lock, row_owner, row_seq, row_guid, row_version, is_active, created_date, created_by, last_updated_date, last_updated_by, removed_date, removed_by, custom_attributes)
    @classmethod
    def from_write(cls, dto: synchronization_write_dto):
        return cls(0, dto.synchronization_uid, dto.synchronization_name, dto.tenant_uid, dto.synchronization_type_uid, dto.storage_uid, dto.sync_expression, dto.sync_query, dto.sync_definition, dto.sync_priority, dto.last_run_date, dto.last_run_seconds, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, dto.custom_attributes)
    def clone_read(self):
        return synchronization_read_dto(self.synchronization_uid, self.synchronization_name, self.tenant_uid, self.synchronization_type_uid, self.storage_uid, self.sync_expression, self.sync_query, self.sync_definition, self.sync_priority, self.last_run_date, self.last_run_seconds, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes)
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["synchronization_uid"], d["synchronization_name"], d["tenant_uid"], d["synchronization_type_uid"], d["storage_uid"], d["sync_expression"], d["sync_query"], d["sync_definition"], d["sync_priority"], d["last_run_date"], d["last_run_seconds"], d["row_instance"], d["row_lock"], d["row_owner"], d["row_seq"], d["row_guid"], d["row_version"], d["is_active"], d["created_date"], d["created_by"], d["last_updated_date"], d["last_updated_by"], d["removed_date"], d["removed_by"], d["custom_attributes"])
    def to_read_dict(self) -> dict:
        return asdict(self)
    def to_write(self) -> synchronization_write_dto:
        return synchronization_write_dto(self.synchronization_uid, self.synchronization_name, self.tenant_uid, self.synchronization_type_uid, self.storage_uid, self.sync_expression, self.sync_query, self.sync_definition, self.sync_priority, self.last_run_date, self.last_run_seconds, self.custom_attributes)
    def to_thin(self) -> synchronization_thin_dto:
        return synchronization_thin_dto(self.synchronization_uid, self.synchronization_name, self.created_date, self.is_active)
    def touch(self, updated_by: str = "system"):
        self.last_updated_date = datetime.datetime.now()
        self.last_updated_by = updated_by
        self.row_version = self.row_version+1
    def get_list_all_values(self) -> list[any]:
        return [self.synchronization_uid, self.synchronization_name, self.tenant_uid, self.synchronization_type_uid, self.storage_uid, self.sync_expression, self.sync_query, self.sync_definition, self.sync_priority, self.last_run_date, self.last_run_seconds, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]
    def get_list_update_values(self, updated_by: str) -> list[any]:
        return [self.synchronization_name, self.tenant_uid, self.synchronization_type_uid, self.storage_uid, self.sync_expression, self.sync_query, self.sync_definition, self.sync_priority, self.last_run_date, self.last_run_seconds, self.custom_attributes, updated_by, self.synchronization_uid]
    def is_older_than(self, dt: datetime.datetime) -> bool:
        return self.created_date < dt
    def is_newer_than(self, dt: datetime.datetime) -> bool:
        return self.created_date > dt
    def to_json_read(self) -> str:
        return json.dumps(self.to_read_dict())


@dataclass(frozen=False)
class synchronization_run_read_dto(base_read_dto, synchronization_run_write_dto):
    synchronization_run_uid: str
    synchronization_run_name: str
    synchronization_uid: str
    run_status: str
    run_time_seconds: str
    copied_items: int
    row_instance: str
    row_lock: str | None
    row_owner: str
    row_seq: int
    row_guid: str
    row_version: int
    is_active: int
    created_date: datetime.datetime
    created_by: str
    last_updated_date: datetime.datetime
    last_updated_by: str
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str
    def __init__(self, synchronization_run_uid: str, synchronization_run_name: str, synchronization_uid: str, run_status: str, run_time_seconds: str, copied_items: int, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
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
    @classmethod
    def empty_read(cls):
        return cls(0, "", "", "", "", "", 0, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def default_read(cls):
        return cls(0, base_dto.get_random_uid(), "", "", "", "", 0, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def random_read(cls):
        return cls(0, base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), "", 0, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_default(cls, synchronization_run_uid: str, synchronization_run_name: str, synchronization_uid: str, run_status: str, run_time_seconds: str, copied_items: int):
        return cls(0, synchronization_run_uid, synchronization_run_name, synchronization_uid, run_status, run_time_seconds, copied_items, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_full(cls, synchronization_run_uid: str, synchronization_run_name: str, synchronization_uid: str, run_status: str, run_time_seconds: str, copied_items: int, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
        return cls(synchronization_run_uid, synchronization_run_name, synchronization_uid, run_status, run_time_seconds, copied_items, row_instance, row_lock, row_owner, row_seq, row_guid, row_version, is_active, created_date, created_by, last_updated_date, last_updated_by, removed_date, removed_by, custom_attributes)
    @classmethod
    def from_write(cls, dto: synchronization_run_write_dto):
        return cls(0, dto.synchronization_run_uid, dto.synchronization_run_name, dto.synchronization_uid, dto.run_status, dto.run_time_seconds, dto.copied_items, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, dto.custom_attributes)
    def clone_read(self):
        return synchronization_run_read_dto(self.synchronization_run_uid, self.synchronization_run_name, self.synchronization_uid, self.run_status, self.run_time_seconds, self.copied_items, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes)
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["synchronization_run_uid"], d["synchronization_run_name"], d["synchronization_uid"], d["run_status"], d["run_time_seconds"], d["copied_items"], d["row_instance"], d["row_lock"], d["row_owner"], d["row_seq"], d["row_guid"], d["row_version"], d["is_active"], d["created_date"], d["created_by"], d["last_updated_date"], d["last_updated_by"], d["removed_date"], d["removed_by"], d["custom_attributes"])
    def to_read_dict(self) -> dict:
        return asdict(self)
    def to_write(self) -> synchronization_run_write_dto:
        return synchronization_run_write_dto(self.synchronization_run_uid, self.synchronization_run_name, self.synchronization_uid, self.run_status, self.run_time_seconds, self.copied_items, self.custom_attributes)
    def to_thin(self) -> synchronization_run_thin_dto:
        return synchronization_run_thin_dto(self.synchronization_run_uid, self.synchronization_run_name, self.created_date, self.is_active)
    def touch(self, updated_by: str = "system"):
        self.last_updated_date = datetime.datetime.now()
        self.last_updated_by = updated_by
        self.row_version = self.row_version+1
    def get_list_all_values(self) -> list[any]:
        return [self.synchronization_run_uid, self.synchronization_run_name, self.synchronization_uid, self.run_status, self.run_time_seconds, self.copied_items, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]
    def get_list_update_values(self, updated_by: str) -> list[any]:
        return [self.synchronization_run_name, self.synchronization_uid, self.run_status, self.run_time_seconds, self.copied_items, self.custom_attributes, updated_by, self.synchronization_run_uid]
    def is_older_than(self, dt: datetime.datetime) -> bool:
        return self.created_date < dt
    def is_newer_than(self, dt: datetime.datetime) -> bool:
        return self.created_date > dt
    def to_json_read(self) -> str:
        return json.dumps(self.to_read_dict())


@dataclass(frozen=False)
class synchronization_type_read_dto(base_read_dto, synchronization_type_write_dto):
    synchronization_type_uid: str
    synchronization_type_name: str
    sync_type: str
    sync_class_name: str
    row_instance: str
    row_lock: str | None
    row_owner: str
    row_seq: int
    row_guid: str
    row_version: int
    is_active: int
    created_date: datetime.datetime
    created_by: str
    last_updated_date: datetime.datetime
    last_updated_by: str
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str
    def __init__(self, synchronization_type_uid: str, synchronization_type_name: str, sync_type: str, sync_class_name: str, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
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
    @classmethod
    def empty_read(cls):
        return cls(0, "", "", "", "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def default_read(cls):
        return cls(0, base_dto.get_random_uid(), "", "", "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def random_read(cls):
        return cls(0, base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_default(cls, synchronization_type_uid: str, synchronization_type_name: str, sync_type: str, sync_class_name: str):
        return cls(0, synchronization_type_uid, synchronization_type_name, sync_type, sync_class_name, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_full(cls, synchronization_type_uid: str, synchronization_type_name: str, sync_type: str, sync_class_name: str, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
        return cls(synchronization_type_uid, synchronization_type_name, sync_type, sync_class_name, row_instance, row_lock, row_owner, row_seq, row_guid, row_version, is_active, created_date, created_by, last_updated_date, last_updated_by, removed_date, removed_by, custom_attributes)
    @classmethod
    def from_write(cls, dto: synchronization_type_write_dto):
        return cls(0, dto.synchronization_type_uid, dto.synchronization_type_name, dto.sync_type, dto.sync_class_name, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, dto.custom_attributes)
    def clone_read(self):
        return synchronization_type_read_dto(self.synchronization_type_uid, self.synchronization_type_name, self.sync_type, self.sync_class_name, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes)
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["synchronization_type_uid"], d["synchronization_type_name"], d["sync_type"], d["sync_class_name"], d["row_instance"], d["row_lock"], d["row_owner"], d["row_seq"], d["row_guid"], d["row_version"], d["is_active"], d["created_date"], d["created_by"], d["last_updated_date"], d["last_updated_by"], d["removed_date"], d["removed_by"], d["custom_attributes"])
    def to_read_dict(self) -> dict:
        return asdict(self)
    def to_write(self) -> synchronization_type_write_dto:
        return synchronization_type_write_dto(self.synchronization_type_uid, self.synchronization_type_name, self.sync_type, self.sync_class_name, self.custom_attributes)
    def to_thin(self) -> synchronization_type_thin_dto:
        return synchronization_type_thin_dto(self.synchronization_type_uid, self.synchronization_type_name, self.created_date, self.is_active)
    def touch(self, updated_by: str = "system"):
        self.last_updated_date = datetime.datetime.now()
        self.last_updated_by = updated_by
        self.row_version = self.row_version+1
    def get_list_all_values(self) -> list[any]:
        return [self.synchronization_type_uid, self.synchronization_type_name, self.sync_type, self.sync_class_name, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]
    def get_list_update_values(self, updated_by: str) -> list[any]:
        return [self.synchronization_type_name, self.sync_type, self.sync_class_name, self.custom_attributes, updated_by, self.synchronization_type_uid]
    def is_older_than(self, dt: datetime.datetime) -> bool:
        return self.created_date < dt
    def is_newer_than(self, dt: datetime.datetime) -> bool:
        return self.created_date > dt
    def to_json_read(self) -> str:
        return json.dumps(self.to_read_dict())


@dataclass(frozen=False)
class system_attribute_read_dto(base_read_dto, system_attribute_write_dto):
    system_attribute_uid: str
    system_attribute_name: str
    system_table_uid: str
    column_name: str
    attribute_type: str
    attribute_category: str
    attribute_label: str
    attribute_description: str
    ordinal_position: int
    is_hidden: int
    is_meta: int
    is_secret: int
    is_full_search: int
    row_instance: str
    row_lock: str | None
    row_owner: str
    row_seq: int
    row_guid: str
    row_version: int
    is_active: int
    created_date: datetime.datetime
    created_by: str
    last_updated_date: datetime.datetime
    last_updated_by: str
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str
    def __init__(self, system_attribute_uid: str, system_attribute_name: str, system_table_uid: str, column_name: str, attribute_type: str, attribute_category: str, attribute_label: str, attribute_description: str, ordinal_position: int, is_hidden: int, is_meta: int, is_secret: int, is_full_search: int, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
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
    @classmethod
    def empty_read(cls):
        return cls(0, "", "", "", "", "", "", "", "", 0, 0, 0, 0, 0, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def default_read(cls):
        return cls(0, base_dto.get_random_uid(), "", "", "", "", "", "", "", 0, 0, 0, 0, 0, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def random_read(cls):
        return cls(0, base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), 0, 0, 0, 0, 0, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_default(cls, system_attribute_uid: str, system_attribute_name: str, system_table_uid: str, column_name: str, attribute_type: str, attribute_category: str, attribute_label: str, attribute_description: str, ordinal_position: int, is_hidden: int, is_meta: int, is_secret: int, is_full_search: int):
        return cls(0, system_attribute_uid, system_attribute_name, system_table_uid, column_name, attribute_type, attribute_category, attribute_label, attribute_description, ordinal_position, is_hidden, is_meta, is_secret, is_full_search, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_full(cls, system_attribute_uid: str, system_attribute_name: str, system_table_uid: str, column_name: str, attribute_type: str, attribute_category: str, attribute_label: str, attribute_description: str, ordinal_position: int, is_hidden: int, is_meta: int, is_secret: int, is_full_search: int, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
        return cls(system_attribute_uid, system_attribute_name, system_table_uid, column_name, attribute_type, attribute_category, attribute_label, attribute_description, ordinal_position, is_hidden, is_meta, is_secret, is_full_search, row_instance, row_lock, row_owner, row_seq, row_guid, row_version, is_active, created_date, created_by, last_updated_date, last_updated_by, removed_date, removed_by, custom_attributes)
    @classmethod
    def from_write(cls, dto: system_attribute_write_dto):
        return cls(0, dto.system_attribute_uid, dto.system_attribute_name, dto.system_table_uid, dto.column_name, dto.attribute_type, dto.attribute_category, dto.attribute_label, dto.attribute_description, dto.ordinal_position, dto.is_hidden, dto.is_meta, dto.is_secret, dto.is_full_search, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, dto.custom_attributes)
    def clone_read(self):
        return system_attribute_read_dto(self.system_attribute_uid, self.system_attribute_name, self.system_table_uid, self.column_name, self.attribute_type, self.attribute_category, self.attribute_label, self.attribute_description, self.ordinal_position, self.is_hidden, self.is_meta, self.is_secret, self.is_full_search, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes)
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["system_attribute_uid"], d["system_attribute_name"], d["system_table_uid"], d["column_name"], d["attribute_type"], d["attribute_category"], d["attribute_label"], d["attribute_description"], d["ordinal_position"], d["is_hidden"], d["is_meta"], d["is_secret"], d["is_full_search"], d["row_instance"], d["row_lock"], d["row_owner"], d["row_seq"], d["row_guid"], d["row_version"], d["is_active"], d["created_date"], d["created_by"], d["last_updated_date"], d["last_updated_by"], d["removed_date"], d["removed_by"], d["custom_attributes"])
    def to_read_dict(self) -> dict:
        return asdict(self)
    def to_write(self) -> system_attribute_write_dto:
        return system_attribute_write_dto(self.system_attribute_uid, self.system_attribute_name, self.system_table_uid, self.column_name, self.attribute_type, self.attribute_category, self.attribute_label, self.attribute_description, self.ordinal_position, self.is_hidden, self.is_meta, self.is_secret, self.is_full_search, self.custom_attributes)
    def to_thin(self) -> system_attribute_thin_dto:
        return system_attribute_thin_dto(self.system_attribute_uid, self.system_attribute_name, self.created_date, self.is_active)
    def touch(self, updated_by: str = "system"):
        self.last_updated_date = datetime.datetime.now()
        self.last_updated_by = updated_by
        self.row_version = self.row_version+1
    def get_list_all_values(self) -> list[any]:
        return [self.system_attribute_uid, self.system_attribute_name, self.system_table_uid, self.column_name, self.attribute_type, self.attribute_category, self.attribute_label, self.attribute_description, self.ordinal_position, self.is_hidden, self.is_meta, self.is_secret, self.is_full_search, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]
    def get_list_update_values(self, updated_by: str) -> list[any]:
        return [self.system_attribute_name, self.system_table_uid, self.column_name, self.attribute_type, self.attribute_category, self.attribute_label, self.attribute_description, self.ordinal_position, self.is_hidden, self.is_meta, self.is_secret, self.is_full_search, self.custom_attributes, updated_by, self.system_attribute_uid]
    def is_older_than(self, dt: datetime.datetime) -> bool:
        return self.created_date < dt
    def is_newer_than(self, dt: datetime.datetime) -> bool:
        return self.created_date > dt
    def to_json_read(self) -> str:
        return json.dumps(self.to_read_dict())


@dataclass(frozen=False)
class system_constraint_read_dto(base_read_dto, system_constraint_write_dto):
    system_constraint_uid: str
    system_constraint_name: str
    system_table_uid: str
    system_attribute_uid: str
    tenant_uid: str
    constraint_class: str
    constraint_params_json: str
    row_instance: str
    row_lock: str | None
    row_owner: str
    row_seq: int
    row_guid: str
    row_version: int
    is_active: int
    created_date: datetime.datetime
    created_by: str
    last_updated_date: datetime.datetime
    last_updated_by: str
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str
    def __init__(self, system_constraint_uid: str, system_constraint_name: str, system_table_uid: str, system_attribute_uid: str, tenant_uid: str, constraint_class: str, constraint_params_json: str, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
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
    @classmethod
    def empty_read(cls):
        return cls(0, "", "", "", "", "", "", "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def default_read(cls):
        return cls(0, base_dto.get_random_uid(), "", "", "", "", "", "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def random_read(cls):
        return cls(0, base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_default(cls, system_constraint_uid: str, system_constraint_name: str, system_table_uid: str, system_attribute_uid: str, tenant_uid: str, constraint_class: str, constraint_params_json: str):
        return cls(0, system_constraint_uid, system_constraint_name, system_table_uid, system_attribute_uid, tenant_uid, constraint_class, constraint_params_json, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_full(cls, system_constraint_uid: str, system_constraint_name: str, system_table_uid: str, system_attribute_uid: str, tenant_uid: str, constraint_class: str, constraint_params_json: str, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
        return cls(system_constraint_uid, system_constraint_name, system_table_uid, system_attribute_uid, tenant_uid, constraint_class, constraint_params_json, row_instance, row_lock, row_owner, row_seq, row_guid, row_version, is_active, created_date, created_by, last_updated_date, last_updated_by, removed_date, removed_by, custom_attributes)
    @classmethod
    def from_write(cls, dto: system_constraint_write_dto):
        return cls(0, dto.system_constraint_uid, dto.system_constraint_name, dto.system_table_uid, dto.system_attribute_uid, dto.tenant_uid, dto.constraint_class, dto.constraint_params_json, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, dto.custom_attributes)
    def clone_read(self):
        return system_constraint_read_dto(self.system_constraint_uid, self.system_constraint_name, self.system_table_uid, self.system_attribute_uid, self.tenant_uid, self.constraint_class, self.constraint_params_json, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes)
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["system_constraint_uid"], d["system_constraint_name"], d["system_table_uid"], d["system_attribute_uid"], d["tenant_uid"], d["constraint_class"], d["constraint_params_json"], d["row_instance"], d["row_lock"], d["row_owner"], d["row_seq"], d["row_guid"], d["row_version"], d["is_active"], d["created_date"], d["created_by"], d["last_updated_date"], d["last_updated_by"], d["removed_date"], d["removed_by"], d["custom_attributes"])
    def to_read_dict(self) -> dict:
        return asdict(self)
    def to_write(self) -> system_constraint_write_dto:
        return system_constraint_write_dto(self.system_constraint_uid, self.system_constraint_name, self.system_table_uid, self.system_attribute_uid, self.tenant_uid, self.constraint_class, self.constraint_params_json, self.custom_attributes)
    def to_thin(self) -> system_constraint_thin_dto:
        return system_constraint_thin_dto(self.system_constraint_uid, self.system_constraint_name, self.created_date, self.is_active)
    def touch(self, updated_by: str = "system"):
        self.last_updated_date = datetime.datetime.now()
        self.last_updated_by = updated_by
        self.row_version = self.row_version+1
    def get_list_all_values(self) -> list[any]:
        return [self.system_constraint_uid, self.system_constraint_name, self.system_table_uid, self.system_attribute_uid, self.tenant_uid, self.constraint_class, self.constraint_params_json, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]
    def get_list_update_values(self, updated_by: str) -> list[any]:
        return [self.system_constraint_name, self.system_table_uid, self.system_attribute_uid, self.tenant_uid, self.constraint_class, self.constraint_params_json, self.custom_attributes, updated_by, self.system_constraint_uid]
    def is_older_than(self, dt: datetime.datetime) -> bool:
        return self.created_date < dt
    def is_newer_than(self, dt: datetime.datetime) -> bool:
        return self.created_date > dt
    def to_json_read(self) -> str:
        return json.dumps(self.to_read_dict())


@dataclass(frozen=False)
class system_database_read_dto(base_read_dto, system_database_write_dto):
    system_database_uid: str
    system_database_name: str
    db_url: str
    db_host: str
    db_name: str
    db_user: str
    last_status_name: str
    last_db_size: int
    row_instance: str
    row_lock: str | None
    row_owner: str
    row_seq: int
    row_guid: str
    row_version: int
    is_active: int
    created_date: datetime.datetime
    created_by: str
    last_updated_date: datetime.datetime
    last_updated_by: str
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str
    def __init__(self, system_database_uid: str, system_database_name: str, db_url: str, db_host: str, db_name: str, db_user: str, last_status_name: str, last_db_size: int, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
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
    @classmethod
    def empty_read(cls):
        return cls(0, "", "", "", "", "", "", "", 0, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def default_read(cls):
        return cls(0, base_dto.get_random_uid(), "", "", "", "", "", "", 0, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def random_read(cls):
        return cls(0, base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), 0, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_default(cls, system_database_uid: str, system_database_name: str, db_url: str, db_host: str, db_name: str, db_user: str, last_status_name: str, last_db_size: int):
        return cls(0, system_database_uid, system_database_name, db_url, db_host, db_name, db_user, last_status_name, last_db_size, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_full(cls, system_database_uid: str, system_database_name: str, db_url: str, db_host: str, db_name: str, db_user: str, last_status_name: str, last_db_size: int, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
        return cls(system_database_uid, system_database_name, db_url, db_host, db_name, db_user, last_status_name, last_db_size, row_instance, row_lock, row_owner, row_seq, row_guid, row_version, is_active, created_date, created_by, last_updated_date, last_updated_by, removed_date, removed_by, custom_attributes)
    @classmethod
    def from_write(cls, dto: system_database_write_dto):
        return cls(0, dto.system_database_uid, dto.system_database_name, dto.db_url, dto.db_host, dto.db_name, dto.db_user, dto.last_status_name, dto.last_db_size, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, dto.custom_attributes)
    def clone_read(self):
        return system_database_read_dto(self.system_database_uid, self.system_database_name, self.db_url, self.db_host, self.db_name, self.db_user, self.last_status_name, self.last_db_size, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes)
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["system_database_uid"], d["system_database_name"], d["db_url"], d["db_host"], d["db_name"], d["db_user"], d["last_status_name"], d["last_db_size"], d["row_instance"], d["row_lock"], d["row_owner"], d["row_seq"], d["row_guid"], d["row_version"], d["is_active"], d["created_date"], d["created_by"], d["last_updated_date"], d["last_updated_by"], d["removed_date"], d["removed_by"], d["custom_attributes"])
    def to_read_dict(self) -> dict:
        return asdict(self)
    def to_write(self) -> system_database_write_dto:
        return system_database_write_dto(self.system_database_uid, self.system_database_name, self.db_url, self.db_host, self.db_name, self.db_user, self.last_status_name, self.last_db_size, self.custom_attributes)
    def to_thin(self) -> system_database_thin_dto:
        return system_database_thin_dto(self.system_database_uid, self.system_database_name, self.created_date, self.is_active)
    def touch(self, updated_by: str = "system"):
        self.last_updated_date = datetime.datetime.now()
        self.last_updated_by = updated_by
        self.row_version = self.row_version+1
    def get_list_all_values(self) -> list[any]:
        return [self.system_database_uid, self.system_database_name, self.db_url, self.db_host, self.db_name, self.db_user, self.last_status_name, self.last_db_size, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]
    def get_list_update_values(self, updated_by: str) -> list[any]:
        return [self.system_database_name, self.db_url, self.db_host, self.db_name, self.db_user, self.last_status_name, self.last_db_size, self.custom_attributes, updated_by, self.system_database_uid]
    def is_older_than(self, dt: datetime.datetime) -> bool:
        return self.created_date < dt
    def is_newer_than(self, dt: datetime.datetime) -> bool:
        return self.created_date > dt
    def to_json_read(self) -> str:
        return json.dumps(self.to_read_dict())


@dataclass(frozen=False)
class system_exception_read_dto(base_read_dto, system_exception_write_dto):
    system_exception_uid: str
    system_exception_name: str
    exception_class: str
    exception_message: str
    exception_stacktrace: str
    row_instance: str
    row_lock: str | None
    row_owner: str
    row_seq: int
    row_guid: str
    row_version: int
    is_active: int
    created_date: datetime.datetime
    created_by: str
    last_updated_date: datetime.datetime
    last_updated_by: str
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str
    def __init__(self, system_exception_uid: str, system_exception_name: str, exception_class: str, exception_message: str, exception_stacktrace: str, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
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
    @classmethod
    def empty_read(cls):
        return cls(0, "", "", "", "", "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def default_read(cls):
        return cls(0, base_dto.get_random_uid(), "", "", "", "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def random_read(cls):
        return cls(0, base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_default(cls, system_exception_uid: str, system_exception_name: str, exception_class: str, exception_message: str, exception_stacktrace: str):
        return cls(0, system_exception_uid, system_exception_name, exception_class, exception_message, exception_stacktrace, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_full(cls, system_exception_uid: str, system_exception_name: str, exception_class: str, exception_message: str, exception_stacktrace: str, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
        return cls(system_exception_uid, system_exception_name, exception_class, exception_message, exception_stacktrace, row_instance, row_lock, row_owner, row_seq, row_guid, row_version, is_active, created_date, created_by, last_updated_date, last_updated_by, removed_date, removed_by, custom_attributes)
    @classmethod
    def from_write(cls, dto: system_exception_write_dto):
        return cls(0, dto.system_exception_uid, dto.system_exception_name, dto.exception_class, dto.exception_message, dto.exception_stacktrace, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, dto.custom_attributes)
    def clone_read(self):
        return system_exception_read_dto(self.system_exception_uid, self.system_exception_name, self.exception_class, self.exception_message, self.exception_stacktrace, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes)
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["system_exception_uid"], d["system_exception_name"], d["exception_class"], d["exception_message"], d["exception_stacktrace"], d["row_instance"], d["row_lock"], d["row_owner"], d["row_seq"], d["row_guid"], d["row_version"], d["is_active"], d["created_date"], d["created_by"], d["last_updated_date"], d["last_updated_by"], d["removed_date"], d["removed_by"], d["custom_attributes"])
    def to_read_dict(self) -> dict:
        return asdict(self)
    def to_write(self) -> system_exception_write_dto:
        return system_exception_write_dto(self.system_exception_uid, self.system_exception_name, self.exception_class, self.exception_message, self.exception_stacktrace, self.custom_attributes)
    def to_thin(self) -> system_exception_thin_dto:
        return system_exception_thin_dto(self.system_exception_uid, self.system_exception_name, self.created_date, self.is_active)
    def touch(self, updated_by: str = "system"):
        self.last_updated_date = datetime.datetime.now()
        self.last_updated_by = updated_by
        self.row_version = self.row_version+1
    def get_list_all_values(self) -> list[any]:
        return [self.system_exception_uid, self.system_exception_name, self.exception_class, self.exception_message, self.exception_stacktrace, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]
    def get_list_update_values(self, updated_by: str) -> list[any]:
        return [self.system_exception_name, self.exception_class, self.exception_message, self.exception_stacktrace, self.custom_attributes, updated_by, self.system_exception_uid]
    def is_older_than(self, dt: datetime.datetime) -> bool:
        return self.created_date < dt
    def is_newer_than(self, dt: datetime.datetime) -> bool:
        return self.created_date > dt
    def to_json_read(self) -> str:
        return json.dumps(self.to_read_dict())


@dataclass(frozen=False)
class system_instance_read_dto(base_read_dto, system_instance_write_dto):
    system_instance_uid: str
    system_instance_name: str
    system_version_uid: str
    host_name: str
    host_ip: str
    local_path: str
    mode_name: str
    ticks_count: int
    row_instance: str
    row_lock: str | None
    row_owner: str
    row_seq: int
    row_guid: str
    row_version: int
    is_active: int
    created_date: datetime.datetime
    created_by: str
    last_updated_date: datetime.datetime
    last_updated_by: str
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str
    def __init__(self, system_instance_uid: str, system_instance_name: str, system_version_uid: str, host_name: str, host_ip: str, local_path: str, mode_name: str, ticks_count: int, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
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
    @classmethod
    def empty_read(cls):
        return cls(0, "", "", "", "", "", "", "", 0, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def default_read(cls):
        return cls(0, base_dto.get_random_uid(), "", "", "", "", "", "", 0, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def random_read(cls):
        return cls(0, base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), 0, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_default(cls, system_instance_uid: str, system_instance_name: str, system_version_uid: str, host_name: str, host_ip: str, local_path: str, mode_name: str, ticks_count: int):
        return cls(0, system_instance_uid, system_instance_name, system_version_uid, host_name, host_ip, local_path, mode_name, ticks_count, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_full(cls, system_instance_uid: str, system_instance_name: str, system_version_uid: str, host_name: str, host_ip: str, local_path: str, mode_name: str, ticks_count: int, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
        return cls(system_instance_uid, system_instance_name, system_version_uid, host_name, host_ip, local_path, mode_name, ticks_count, row_instance, row_lock, row_owner, row_seq, row_guid, row_version, is_active, created_date, created_by, last_updated_date, last_updated_by, removed_date, removed_by, custom_attributes)
    @classmethod
    def from_write(cls, dto: system_instance_write_dto):
        return cls(0, dto.system_instance_uid, dto.system_instance_name, dto.system_version_uid, dto.host_name, dto.host_ip, dto.local_path, dto.mode_name, dto.ticks_count, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, dto.custom_attributes)
    def clone_read(self):
        return system_instance_read_dto(self.system_instance_uid, self.system_instance_name, self.system_version_uid, self.host_name, self.host_ip, self.local_path, self.mode_name, self.ticks_count, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes)
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["system_instance_uid"], d["system_instance_name"], d["system_version_uid"], d["host_name"], d["host_ip"], d["local_path"], d["mode_name"], d["ticks_count"], d["row_instance"], d["row_lock"], d["row_owner"], d["row_seq"], d["row_guid"], d["row_version"], d["is_active"], d["created_date"], d["created_by"], d["last_updated_date"], d["last_updated_by"], d["removed_date"], d["removed_by"], d["custom_attributes"])
    def to_read_dict(self) -> dict:
        return asdict(self)
    def to_write(self) -> system_instance_write_dto:
        return system_instance_write_dto(self.system_instance_uid, self.system_instance_name, self.system_version_uid, self.host_name, self.host_ip, self.local_path, self.mode_name, self.ticks_count, self.custom_attributes)
    def to_thin(self) -> system_instance_thin_dto:
        return system_instance_thin_dto(self.system_instance_uid, self.system_instance_name, self.created_date, self.is_active)
    def touch(self, updated_by: str = "system"):
        self.last_updated_date = datetime.datetime.now()
        self.last_updated_by = updated_by
        self.row_version = self.row_version+1
    def get_list_all_values(self) -> list[any]:
        return [self.system_instance_uid, self.system_instance_name, self.system_version_uid, self.host_name, self.host_ip, self.local_path, self.mode_name, self.ticks_count, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]
    def get_list_update_values(self, updated_by: str) -> list[any]:
        return [self.system_instance_name, self.system_version_uid, self.host_name, self.host_ip, self.local_path, self.mode_name, self.ticks_count, self.custom_attributes, updated_by, self.system_instance_uid]
    def is_older_than(self, dt: datetime.datetime) -> bool:
        return self.created_date < dt
    def is_newer_than(self, dt: datetime.datetime) -> bool:
        return self.created_date > dt
    def to_json_read(self) -> str:
        return json.dumps(self.to_read_dict())


@dataclass(frozen=False)
class system_license_read_dto(base_read_dto, system_license_write_dto):
    system_license_uid: str
    system_license_name: str
    class_name: str
    license_description: str
    row_instance: str
    row_lock: str | None
    row_owner: str
    row_seq: int
    row_guid: str
    row_version: int
    is_active: int
    created_date: datetime.datetime
    created_by: str
    last_updated_date: datetime.datetime
    last_updated_by: str
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str
    def __init__(self, system_license_uid: str, system_license_name: str, class_name: str, license_description: str, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
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
    @classmethod
    def empty_read(cls):
        return cls(0, "", "", "", "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def default_read(cls):
        return cls(0, base_dto.get_random_uid(), "", "", "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def random_read(cls):
        return cls(0, base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_default(cls, system_license_uid: str, system_license_name: str, class_name: str, license_description: str):
        return cls(0, system_license_uid, system_license_name, class_name, license_description, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_full(cls, system_license_uid: str, system_license_name: str, class_name: str, license_description: str, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
        return cls(system_license_uid, system_license_name, class_name, license_description, row_instance, row_lock, row_owner, row_seq, row_guid, row_version, is_active, created_date, created_by, last_updated_date, last_updated_by, removed_date, removed_by, custom_attributes)
    @classmethod
    def from_write(cls, dto: system_license_write_dto):
        return cls(0, dto.system_license_uid, dto.system_license_name, dto.class_name, dto.license_description, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, dto.custom_attributes)
    def clone_read(self):
        return system_license_read_dto(self.system_license_uid, self.system_license_name, self.class_name, self.license_description, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes)
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["system_license_uid"], d["system_license_name"], d["class_name"], d["license_description"], d["row_instance"], d["row_lock"], d["row_owner"], d["row_seq"], d["row_guid"], d["row_version"], d["is_active"], d["created_date"], d["created_by"], d["last_updated_date"], d["last_updated_by"], d["removed_date"], d["removed_by"], d["custom_attributes"])
    def to_read_dict(self) -> dict:
        return asdict(self)
    def to_write(self) -> system_license_write_dto:
        return system_license_write_dto(self.system_license_uid, self.system_license_name, self.class_name, self.license_description, self.custom_attributes)
    def to_thin(self) -> system_license_thin_dto:
        return system_license_thin_dto(self.system_license_uid, self.system_license_name, self.created_date, self.is_active)
    def touch(self, updated_by: str = "system"):
        self.last_updated_date = datetime.datetime.now()
        self.last_updated_by = updated_by
        self.row_version = self.row_version+1
    def get_list_all_values(self) -> list[any]:
        return [self.system_license_uid, self.system_license_name, self.class_name, self.license_description, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]
    def get_list_update_values(self, updated_by: str) -> list[any]:
        return [self.system_license_name, self.class_name, self.license_description, self.custom_attributes, updated_by, self.system_license_uid]
    def is_older_than(self, dt: datetime.datetime) -> bool:
        return self.created_date < dt
    def is_newer_than(self, dt: datetime.datetime) -> bool:
        return self.created_date > dt
    def to_json_read(self) -> str:
        return json.dumps(self.to_read_dict())


@dataclass(frozen=False)
class system_lock_read_dto(base_read_dto, system_lock_write_dto):
    system_lock_uid: str
    system_lock_name: str
    lock_account_uid: str
    lock_comment: str
    lock_reason: str
    row_instance: str
    row_lock: str | None
    row_owner: str
    row_seq: int
    row_guid: str
    row_version: int
    is_active: int
    created_date: datetime.datetime
    created_by: str
    last_updated_date: datetime.datetime
    last_updated_by: str
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str
    def __init__(self, system_lock_uid: str, system_lock_name: str, lock_account_uid: str, lock_comment: str, lock_reason: str, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
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
    @classmethod
    def empty_read(cls):
        return cls(0, "", "", "", "", "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def default_read(cls):
        return cls(0, base_dto.get_random_uid(), "", "", "", "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def random_read(cls):
        return cls(0, base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_default(cls, system_lock_uid: str, system_lock_name: str, lock_account_uid: str, lock_comment: str, lock_reason: str):
        return cls(0, system_lock_uid, system_lock_name, lock_account_uid, lock_comment, lock_reason, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_full(cls, system_lock_uid: str, system_lock_name: str, lock_account_uid: str, lock_comment: str, lock_reason: str, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
        return cls(system_lock_uid, system_lock_name, lock_account_uid, lock_comment, lock_reason, row_instance, row_lock, row_owner, row_seq, row_guid, row_version, is_active, created_date, created_by, last_updated_date, last_updated_by, removed_date, removed_by, custom_attributes)
    @classmethod
    def from_write(cls, dto: system_lock_write_dto):
        return cls(0, dto.system_lock_uid, dto.system_lock_name, dto.lock_account_uid, dto.lock_comment, dto.lock_reason, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, dto.custom_attributes)
    def clone_read(self):
        return system_lock_read_dto(self.system_lock_uid, self.system_lock_name, self.lock_account_uid, self.lock_comment, self.lock_reason, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes)
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["system_lock_uid"], d["system_lock_name"], d["lock_account_uid"], d["lock_comment"], d["lock_reason"], d["row_instance"], d["row_lock"], d["row_owner"], d["row_seq"], d["row_guid"], d["row_version"], d["is_active"], d["created_date"], d["created_by"], d["last_updated_date"], d["last_updated_by"], d["removed_date"], d["removed_by"], d["custom_attributes"])
    def to_read_dict(self) -> dict:
        return asdict(self)
    def to_write(self) -> system_lock_write_dto:
        return system_lock_write_dto(self.system_lock_uid, self.system_lock_name, self.lock_account_uid, self.lock_comment, self.lock_reason, self.custom_attributes)
    def to_thin(self) -> system_lock_thin_dto:
        return system_lock_thin_dto(self.system_lock_uid, self.system_lock_name, self.created_date, self.is_active)
    def touch(self, updated_by: str = "system"):
        self.last_updated_date = datetime.datetime.now()
        self.last_updated_by = updated_by
        self.row_version = self.row_version+1
    def get_list_all_values(self) -> list[any]:
        return [self.system_lock_uid, self.system_lock_name, self.lock_account_uid, self.lock_comment, self.lock_reason, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]
    def get_list_update_values(self, updated_by: str) -> list[any]:
        return [self.system_lock_name, self.lock_account_uid, self.lock_comment, self.lock_reason, self.custom_attributes, updated_by, self.system_lock_uid]
    def is_older_than(self, dt: datetime.datetime) -> bool:
        return self.created_date < dt
    def is_newer_than(self, dt: datetime.datetime) -> bool:
        return self.created_date > dt
    def to_json_read(self) -> str:
        return json.dumps(self.to_read_dict())


@dataclass(frozen=False)
class system_module_read_dto(base_read_dto, system_module_write_dto):
    system_module_uid: str
    system_module_name: str
    system_module_description: str
    row_instance: str
    row_lock: str | None
    row_owner: str
    row_seq: int
    row_guid: str
    row_version: int
    is_active: int
    created_date: datetime.datetime
    created_by: str
    last_updated_date: datetime.datetime
    last_updated_by: str
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str
    def __init__(self, system_module_uid: str, system_module_name: str, system_module_description: str, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
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
    @classmethod
    def empty_read(cls):
        return cls(0, "", "", "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def default_read(cls):
        return cls(0, base_dto.get_random_uid(), "", "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def random_read(cls):
        return cls(0, base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_default(cls, system_module_uid: str, system_module_name: str, system_module_description: str):
        return cls(0, system_module_uid, system_module_name, system_module_description, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_full(cls, system_module_uid: str, system_module_name: str, system_module_description: str, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
        return cls(system_module_uid, system_module_name, system_module_description, row_instance, row_lock, row_owner, row_seq, row_guid, row_version, is_active, created_date, created_by, last_updated_date, last_updated_by, removed_date, removed_by, custom_attributes)
    @classmethod
    def from_write(cls, dto: system_module_write_dto):
        return cls(0, dto.system_module_uid, dto.system_module_name, dto.system_module_description, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, dto.custom_attributes)
    def clone_read(self):
        return system_module_read_dto(self.system_module_uid, self.system_module_name, self.system_module_description, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes)
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["system_module_uid"], d["system_module_name"], d["system_module_description"], d["row_instance"], d["row_lock"], d["row_owner"], d["row_seq"], d["row_guid"], d["row_version"], d["is_active"], d["created_date"], d["created_by"], d["last_updated_date"], d["last_updated_by"], d["removed_date"], d["removed_by"], d["custom_attributes"])
    def to_read_dict(self) -> dict:
        return asdict(self)
    def to_write(self) -> system_module_write_dto:
        return system_module_write_dto(self.system_module_uid, self.system_module_name, self.system_module_description, self.custom_attributes)
    def to_thin(self) -> system_module_thin_dto:
        return system_module_thin_dto(self.system_module_uid, self.system_module_name, self.created_date, self.is_active)
    def touch(self, updated_by: str = "system"):
        self.last_updated_date = datetime.datetime.now()
        self.last_updated_by = updated_by
        self.row_version = self.row_version+1
    def get_list_all_values(self) -> list[any]:
        return [self.system_module_uid, self.system_module_name, self.system_module_description, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]
    def get_list_update_values(self, updated_by: str) -> list[any]:
        return [self.system_module_name, self.system_module_description, self.custom_attributes, updated_by, self.system_module_uid]
    def is_older_than(self, dt: datetime.datetime) -> bool:
        return self.created_date < dt
    def is_newer_than(self, dt: datetime.datetime) -> bool:
        return self.created_date > dt
    def to_json_read(self) -> str:
        return json.dumps(self.to_read_dict())


@dataclass(frozen=False)
class system_query_read_dto(base_read_dto, system_query_write_dto):
    system_query_uid: str
    system_query_name: str
    time_start: int
    total_query_time: int
    query_seq: int
    execution_counter: int
    connection_counter: int
    release_counter: int
    current_active: int
    current_idle: int
    table_name: str
    rows_count: int
    sql: str
    row_instance: str
    row_lock: str | None
    row_owner: str
    row_seq: int
    row_guid: str
    row_version: int
    is_active: int
    created_date: datetime.datetime
    created_by: str
    last_updated_date: datetime.datetime
    last_updated_by: str
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str
    def __init__(self, system_query_uid: str, system_query_name: str, time_start: int, total_query_time: int, query_seq: int, execution_counter: int, connection_counter: int, release_counter: int, current_active: int, current_idle: int, table_name: str, rows_count: int, sql: str, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
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
    @classmethod
    def empty_read(cls):
        return cls(0, "", "", 0, 0, 0, 0, 0, 0, 0, 0, "", 0, "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def default_read(cls):
        return cls(0, base_dto.get_random_uid(), "", 0, 0, 0, 0, 0, 0, 0, 0, "", 0, "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def random_read(cls):
        return cls(0, base_dto.get_random_uid(), base_dto.get_random_uid(), 0, 0, 0, 0, 0, 0, 0, 0, base_dto.get_random_uid(), 0, base_dto.get_random_uid(), "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_default(cls, system_query_uid: str, system_query_name: str, time_start: int, total_query_time: int, query_seq: int, execution_counter: int, connection_counter: int, release_counter: int, current_active: int, current_idle: int, table_name: str, rows_count: int, sql: str):
        return cls(0, system_query_uid, system_query_name, time_start, total_query_time, query_seq, execution_counter, connection_counter, release_counter, current_active, current_idle, table_name, rows_count, sql, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_full(cls, system_query_uid: str, system_query_name: str, time_start: int, total_query_time: int, query_seq: int, execution_counter: int, connection_counter: int, release_counter: int, current_active: int, current_idle: int, table_name: str, rows_count: int, sql: str, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
        return cls(system_query_uid, system_query_name, time_start, total_query_time, query_seq, execution_counter, connection_counter, release_counter, current_active, current_idle, table_name, rows_count, sql, row_instance, row_lock, row_owner, row_seq, row_guid, row_version, is_active, created_date, created_by, last_updated_date, last_updated_by, removed_date, removed_by, custom_attributes)
    @classmethod
    def from_write(cls, dto: system_query_write_dto):
        return cls(0, dto.system_query_uid, dto.system_query_name, dto.time_start, dto.total_query_time, dto.query_seq, dto.execution_counter, dto.connection_counter, dto.release_counter, dto.current_active, dto.current_idle, dto.table_name, dto.rows_count, dto.sql, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, dto.custom_attributes)
    def clone_read(self):
        return system_query_read_dto(self.system_query_uid, self.system_query_name, self.time_start, self.total_query_time, self.query_seq, self.execution_counter, self.connection_counter, self.release_counter, self.current_active, self.current_idle, self.table_name, self.rows_count, self.sql, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes)
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["system_query_uid"], d["system_query_name"], d["time_start"], d["total_query_time"], d["query_seq"], d["execution_counter"], d["connection_counter"], d["release_counter"], d["current_active"], d["current_idle"], d["table_name"], d["rows_count"], d["sql"], d["row_instance"], d["row_lock"], d["row_owner"], d["row_seq"], d["row_guid"], d["row_version"], d["is_active"], d["created_date"], d["created_by"], d["last_updated_date"], d["last_updated_by"], d["removed_date"], d["removed_by"], d["custom_attributes"])
    def to_read_dict(self) -> dict:
        return asdict(self)
    def to_write(self) -> system_query_write_dto:
        return system_query_write_dto(self.system_query_uid, self.system_query_name, self.time_start, self.total_query_time, self.query_seq, self.execution_counter, self.connection_counter, self.release_counter, self.current_active, self.current_idle, self.table_name, self.rows_count, self.sql, self.custom_attributes)
    def to_thin(self) -> system_query_thin_dto:
        return system_query_thin_dto(self.system_query_uid, self.system_query_name, self.created_date, self.is_active)
    def touch(self, updated_by: str = "system"):
        self.last_updated_date = datetime.datetime.now()
        self.last_updated_by = updated_by
        self.row_version = self.row_version+1
    def get_list_all_values(self) -> list[any]:
        return [self.system_query_uid, self.system_query_name, self.time_start, self.total_query_time, self.query_seq, self.execution_counter, self.connection_counter, self.release_counter, self.current_active, self.current_idle, self.table_name, self.rows_count, self.sql, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]
    def get_list_update_values(self, updated_by: str) -> list[any]:
        return [self.system_query_name, self.time_start, self.total_query_time, self.query_seq, self.execution_counter, self.connection_counter, self.release_counter, self.current_active, self.current_idle, self.table_name, self.rows_count, self.sql, self.custom_attributes, updated_by, self.system_query_uid]
    def is_older_than(self, dt: datetime.datetime) -> bool:
        return self.created_date < dt
    def is_newer_than(self, dt: datetime.datetime) -> bool:
        return self.created_date > dt
    def to_json_read(self) -> str:
        return json.dumps(self.to_read_dict())


@dataclass(frozen=False)
class system_request_read_dto(base_read_dto, system_request_write_dto):
    system_request_uid: str
    system_request_name: str
    account_uid: str | None
    request_method: str
    request_url: str
    request_body_size: int
    request_host: str
    request_time: int
    response_code: int
    row_instance: str
    row_lock: str | None
    row_owner: str
    row_seq: int
    row_guid: str
    row_version: int
    is_active: int
    created_date: datetime.datetime
    created_by: str
    last_updated_date: datetime.datetime
    last_updated_by: str
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str
    def __init__(self, system_request_uid: str, system_request_name: str, account_uid: str | None, request_method: str, request_url: str, request_body_size: int, request_host: str, request_time: int, response_code: int, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
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
    @classmethod
    def empty_read(cls):
        return cls(0, "", "", "", "", "", 0, "", 0, 0, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def default_read(cls):
        return cls(0, base_dto.get_random_uid(), "", "", "", "", 0, "", 0, 0, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def random_read(cls):
        return cls(0, base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), 0, base_dto.get_random_uid(), 0, 0, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_default(cls, system_request_uid: str, system_request_name: str, account_uid: str | None, request_method: str, request_url: str, request_body_size: int, request_host: str, request_time: int, response_code: int):
        return cls(0, system_request_uid, system_request_name, account_uid, request_method, request_url, request_body_size, request_host, request_time, response_code, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_full(cls, system_request_uid: str, system_request_name: str, account_uid: str | None, request_method: str, request_url: str, request_body_size: int, request_host: str, request_time: int, response_code: int, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
        return cls(system_request_uid, system_request_name, account_uid, request_method, request_url, request_body_size, request_host, request_time, response_code, row_instance, row_lock, row_owner, row_seq, row_guid, row_version, is_active, created_date, created_by, last_updated_date, last_updated_by, removed_date, removed_by, custom_attributes)
    @classmethod
    def from_write(cls, dto: system_request_write_dto):
        return cls(0, dto.system_request_uid, dto.system_request_name, dto.account_uid, dto.request_method, dto.request_url, dto.request_body_size, dto.request_host, dto.request_time, dto.response_code, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, dto.custom_attributes)
    def clone_read(self):
        return system_request_read_dto(self.system_request_uid, self.system_request_name, self.account_uid, self.request_method, self.request_url, self.request_body_size, self.request_host, self.request_time, self.response_code, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes)
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["system_request_uid"], d["system_request_name"], d["account_uid"], d["request_method"], d["request_url"], d["request_body_size"], d["request_host"], d["request_time"], d["response_code"], d["row_instance"], d["row_lock"], d["row_owner"], d["row_seq"], d["row_guid"], d["row_version"], d["is_active"], d["created_date"], d["created_by"], d["last_updated_date"], d["last_updated_by"], d["removed_date"], d["removed_by"], d["custom_attributes"])
    def to_read_dict(self) -> dict:
        return asdict(self)
    def to_write(self) -> system_request_write_dto:
        return system_request_write_dto(self.system_request_uid, self.system_request_name, self.account_uid, self.request_method, self.request_url, self.request_body_size, self.request_host, self.request_time, self.response_code, self.custom_attributes)
    def to_thin(self) -> system_request_thin_dto:
        return system_request_thin_dto(self.system_request_uid, self.system_request_name, self.created_date, self.is_active)
    def touch(self, updated_by: str = "system"):
        self.last_updated_date = datetime.datetime.now()
        self.last_updated_by = updated_by
        self.row_version = self.row_version+1
    def get_list_all_values(self) -> list[any]:
        return [self.system_request_uid, self.system_request_name, self.account_uid, self.request_method, self.request_url, self.request_body_size, self.request_host, self.request_time, self.response_code, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]
    def get_list_update_values(self, updated_by: str) -> list[any]:
        return [self.system_request_name, self.account_uid, self.request_method, self.request_url, self.request_body_size, self.request_host, self.request_time, self.response_code, self.custom_attributes, updated_by, self.system_request_uid]
    def is_older_than(self, dt: datetime.datetime) -> bool:
        return self.created_date < dt
    def is_newer_than(self, dt: datetime.datetime) -> bool:
        return self.created_date > dt
    def to_json_read(self) -> str:
        return json.dumps(self.to_read_dict())


@dataclass(frozen=False)
class system_setting_read_dto(base_read_dto, system_setting_write_dto):
    system_setting_uid: str
    system_setting_name: str
    setting_value: str
    setting_type: str
    is_public: int
    row_instance: str
    row_lock: str | None
    row_owner: str
    row_seq: int
    row_guid: str
    row_version: int
    is_active: int
    created_date: datetime.datetime
    created_by: str
    last_updated_date: datetime.datetime
    last_updated_by: str
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str
    def __init__(self, system_setting_uid: str, system_setting_name: str, setting_value: str, setting_type: str, is_public: int, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
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
    @classmethod
    def empty_read(cls):
        return cls(0, "", "", "", "", 0, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def default_read(cls):
        return cls(0, base_dto.get_random_uid(), "", "", "", 0, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def random_read(cls):
        return cls(0, base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), 0, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_default(cls, system_setting_uid: str, system_setting_name: str, setting_value: str, setting_type: str, is_public: int):
        return cls(0, system_setting_uid, system_setting_name, setting_value, setting_type, is_public, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_full(cls, system_setting_uid: str, system_setting_name: str, setting_value: str, setting_type: str, is_public: int, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
        return cls(system_setting_uid, system_setting_name, setting_value, setting_type, is_public, row_instance, row_lock, row_owner, row_seq, row_guid, row_version, is_active, created_date, created_by, last_updated_date, last_updated_by, removed_date, removed_by, custom_attributes)
    @classmethod
    def from_write(cls, dto: system_setting_write_dto):
        return cls(0, dto.system_setting_uid, dto.system_setting_name, dto.setting_value, dto.setting_type, dto.is_public, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, dto.custom_attributes)
    def clone_read(self):
        return system_setting_read_dto(self.system_setting_uid, self.system_setting_name, self.setting_value, self.setting_type, self.is_public, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes)
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["system_setting_uid"], d["system_setting_name"], d["setting_value"], d["setting_type"], d["is_public"], d["row_instance"], d["row_lock"], d["row_owner"], d["row_seq"], d["row_guid"], d["row_version"], d["is_active"], d["created_date"], d["created_by"], d["last_updated_date"], d["last_updated_by"], d["removed_date"], d["removed_by"], d["custom_attributes"])
    def to_read_dict(self) -> dict:
        return asdict(self)
    def to_write(self) -> system_setting_write_dto:
        return system_setting_write_dto(self.system_setting_uid, self.system_setting_name, self.setting_value, self.setting_type, self.is_public, self.custom_attributes)
    def to_thin(self) -> system_setting_thin_dto:
        return system_setting_thin_dto(self.system_setting_uid, self.system_setting_name, self.created_date, self.is_active)
    def touch(self, updated_by: str = "system"):
        self.last_updated_date = datetime.datetime.now()
        self.last_updated_by = updated_by
        self.row_version = self.row_version+1
    def get_list_all_values(self) -> list[any]:
        return [self.system_setting_uid, self.system_setting_name, self.setting_value, self.setting_type, self.is_public, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]
    def get_list_update_values(self, updated_by: str) -> list[any]:
        return [self.system_setting_name, self.setting_value, self.setting_type, self.is_public, self.custom_attributes, updated_by, self.system_setting_uid]
    def is_older_than(self, dt: datetime.datetime) -> bool:
        return self.created_date < dt
    def is_newer_than(self, dt: datetime.datetime) -> bool:
        return self.created_date > dt
    def to_json_read(self) -> str:
        return json.dumps(self.to_read_dict())


@dataclass(frozen=False)
class system_setting_account_read_dto(base_read_dto, system_setting_account_write_dto):
    system_setting_account_uid: str
    system_setting_account_name: str
    account_uid: str
    setting_value: str
    is_public: int
    row_instance: str
    row_lock: str | None
    row_owner: str
    row_seq: int
    row_guid: str
    row_version: int
    is_active: int
    created_date: datetime.datetime
    created_by: str
    last_updated_date: datetime.datetime
    last_updated_by: str
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str
    def __init__(self, system_setting_account_uid: str, system_setting_account_name: str, account_uid: str, setting_value: str, is_public: int, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
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
    @classmethod
    def empty_read(cls):
        return cls(0, "", "", "", "", 0, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def default_read(cls):
        return cls(0, base_dto.get_random_uid(), "", "", "", 0, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def random_read(cls):
        return cls(0, base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), 0, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_default(cls, system_setting_account_uid: str, system_setting_account_name: str, account_uid: str, setting_value: str, is_public: int):
        return cls(0, system_setting_account_uid, system_setting_account_name, account_uid, setting_value, is_public, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_full(cls, system_setting_account_uid: str, system_setting_account_name: str, account_uid: str, setting_value: str, is_public: int, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
        return cls(system_setting_account_uid, system_setting_account_name, account_uid, setting_value, is_public, row_instance, row_lock, row_owner, row_seq, row_guid, row_version, is_active, created_date, created_by, last_updated_date, last_updated_by, removed_date, removed_by, custom_attributes)
    @classmethod
    def from_write(cls, dto: system_setting_account_write_dto):
        return cls(0, dto.system_setting_account_uid, dto.system_setting_account_name, dto.account_uid, dto.setting_value, dto.is_public, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, dto.custom_attributes)
    def clone_read(self):
        return system_setting_account_read_dto(self.system_setting_account_uid, self.system_setting_account_name, self.account_uid, self.setting_value, self.is_public, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes)
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["system_setting_account_uid"], d["system_setting_account_name"], d["account_uid"], d["setting_value"], d["is_public"], d["row_instance"], d["row_lock"], d["row_owner"], d["row_seq"], d["row_guid"], d["row_version"], d["is_active"], d["created_date"], d["created_by"], d["last_updated_date"], d["last_updated_by"], d["removed_date"], d["removed_by"], d["custom_attributes"])
    def to_read_dict(self) -> dict:
        return asdict(self)
    def to_write(self) -> system_setting_account_write_dto:
        return system_setting_account_write_dto(self.system_setting_account_uid, self.system_setting_account_name, self.account_uid, self.setting_value, self.is_public, self.custom_attributes)
    def to_thin(self) -> system_setting_account_thin_dto:
        return system_setting_account_thin_dto(self.system_setting_account_uid, self.system_setting_account_name, self.created_date, self.is_active)
    def touch(self, updated_by: str = "system"):
        self.last_updated_date = datetime.datetime.now()
        self.last_updated_by = updated_by
        self.row_version = self.row_version+1
    def get_list_all_values(self) -> list[any]:
        return [self.system_setting_account_uid, self.system_setting_account_name, self.account_uid, self.setting_value, self.is_public, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]
    def get_list_update_values(self, updated_by: str) -> list[any]:
        return [self.system_setting_account_name, self.account_uid, self.setting_value, self.is_public, self.custom_attributes, updated_by, self.system_setting_account_uid]
    def is_older_than(self, dt: datetime.datetime) -> bool:
        return self.created_date < dt
    def is_newer_than(self, dt: datetime.datetime) -> bool:
        return self.created_date > dt
    def to_json_read(self) -> str:
        return json.dumps(self.to_read_dict())


@dataclass(frozen=False)
class system_state_read_dto(base_read_dto, system_state_write_dto):
    system_state_uid: str
    system_state_name: str
    mem_free: int
    mem_max: int
    objects_count: int
    row_instance: str
    row_lock: str | None
    row_owner: str
    row_seq: int
    row_guid: str
    row_version: int
    is_active: int
    created_date: datetime.datetime
    created_by: str
    last_updated_date: datetime.datetime
    last_updated_by: str
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str
    def __init__(self, system_state_uid: str, system_state_name: str, mem_free: int, mem_max: int, objects_count: int, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
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
    @classmethod
    def empty_read(cls):
        return cls(0, "", "", 0, 0, 0, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def default_read(cls):
        return cls(0, base_dto.get_random_uid(), "", 0, 0, 0, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def random_read(cls):
        return cls(0, base_dto.get_random_uid(), base_dto.get_random_uid(), 0, 0, 0, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_default(cls, system_state_uid: str, system_state_name: str, mem_free: int, mem_max: int, objects_count: int):
        return cls(0, system_state_uid, system_state_name, mem_free, mem_max, objects_count, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_full(cls, system_state_uid: str, system_state_name: str, mem_free: int, mem_max: int, objects_count: int, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
        return cls(system_state_uid, system_state_name, mem_free, mem_max, objects_count, row_instance, row_lock, row_owner, row_seq, row_guid, row_version, is_active, created_date, created_by, last_updated_date, last_updated_by, removed_date, removed_by, custom_attributes)
    @classmethod
    def from_write(cls, dto: system_state_write_dto):
        return cls(0, dto.system_state_uid, dto.system_state_name, dto.mem_free, dto.mem_max, dto.objects_count, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, dto.custom_attributes)
    def clone_read(self):
        return system_state_read_dto(self.system_state_uid, self.system_state_name, self.mem_free, self.mem_max, self.objects_count, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes)
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["system_state_uid"], d["system_state_name"], d["mem_free"], d["mem_max"], d["objects_count"], d["row_instance"], d["row_lock"], d["row_owner"], d["row_seq"], d["row_guid"], d["row_version"], d["is_active"], d["created_date"], d["created_by"], d["last_updated_date"], d["last_updated_by"], d["removed_date"], d["removed_by"], d["custom_attributes"])
    def to_read_dict(self) -> dict:
        return asdict(self)
    def to_write(self) -> system_state_write_dto:
        return system_state_write_dto(self.system_state_uid, self.system_state_name, self.mem_free, self.mem_max, self.objects_count, self.custom_attributes)
    def to_thin(self) -> system_state_thin_dto:
        return system_state_thin_dto(self.system_state_uid, self.system_state_name, self.created_date, self.is_active)
    def touch(self, updated_by: str = "system"):
        self.last_updated_date = datetime.datetime.now()
        self.last_updated_by = updated_by
        self.row_version = self.row_version+1
    def get_list_all_values(self) -> list[any]:
        return [self.system_state_uid, self.system_state_name, self.mem_free, self.mem_max, self.objects_count, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]
    def get_list_update_values(self, updated_by: str) -> list[any]:
        return [self.system_state_name, self.mem_free, self.mem_max, self.objects_count, self.custom_attributes, updated_by, self.system_state_uid]
    def is_older_than(self, dt: datetime.datetime) -> bool:
        return self.created_date < dt
    def is_newer_than(self, dt: datetime.datetime) -> bool:
        return self.created_date > dt
    def to_json_read(self) -> str:
        return json.dumps(self.to_read_dict())


@dataclass(frozen=False)
class system_table_read_dto(base_read_dto, system_table_write_dto):
    system_table_uid: str
    system_table_name: str
    parent_system_table_uid: str | None
    table_label: str
    uid_name: str
    table_group: str
    table_code: str
    table_type: str
    table_category: str
    cardinality: int
    is_object: int
    is_rich: int
    is_tenant: int
    is_local: int
    table_comment: str
    row_instance: str
    row_lock: str | None
    row_owner: str
    row_seq: int
    row_guid: str
    row_version: int
    is_active: int
    created_date: datetime.datetime
    created_by: str
    last_updated_date: datetime.datetime
    last_updated_by: str
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str
    def __init__(self, system_table_uid: str, system_table_name: str, parent_system_table_uid: str | None, table_label: str, uid_name: str, table_group: str, table_code: str, table_type: str, table_category: str, cardinality: int, is_object: int, is_rich: int, is_tenant: int, is_local: int, table_comment: str, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
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
    @classmethod
    def empty_read(cls):
        return cls(0, "", "", "", "", "", "", "", "", "", 0, 0, 0, 0, 0, "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def default_read(cls):
        return cls(0, base_dto.get_random_uid(), "", "", "", "", "", "", "", "", 0, 0, 0, 0, 0, "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def random_read(cls):
        return cls(0, base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), 0, 0, 0, 0, 0, base_dto.get_random_uid(), "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_default(cls, system_table_uid: str, system_table_name: str, parent_system_table_uid: str | None, table_label: str, uid_name: str, table_group: str, table_code: str, table_type: str, table_category: str, cardinality: int, is_object: int, is_rich: int, is_tenant: int, is_local: int, table_comment: str):
        return cls(0, system_table_uid, system_table_name, parent_system_table_uid, table_label, uid_name, table_group, table_code, table_type, table_category, cardinality, is_object, is_rich, is_tenant, is_local, table_comment, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_full(cls, system_table_uid: str, system_table_name: str, parent_system_table_uid: str | None, table_label: str, uid_name: str, table_group: str, table_code: str, table_type: str, table_category: str, cardinality: int, is_object: int, is_rich: int, is_tenant: int, is_local: int, table_comment: str, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
        return cls(system_table_uid, system_table_name, parent_system_table_uid, table_label, uid_name, table_group, table_code, table_type, table_category, cardinality, is_object, is_rich, is_tenant, is_local, table_comment, row_instance, row_lock, row_owner, row_seq, row_guid, row_version, is_active, created_date, created_by, last_updated_date, last_updated_by, removed_date, removed_by, custom_attributes)
    @classmethod
    def from_write(cls, dto: system_table_write_dto):
        return cls(0, dto.system_table_uid, dto.system_table_name, dto.parent_system_table_uid, dto.table_label, dto.uid_name, dto.table_group, dto.table_code, dto.table_type, dto.table_category, dto.cardinality, dto.is_object, dto.is_rich, dto.is_tenant, dto.is_local, dto.table_comment, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, dto.custom_attributes)
    def clone_read(self):
        return system_table_read_dto(self.system_table_uid, self.system_table_name, self.parent_system_table_uid, self.table_label, self.uid_name, self.table_group, self.table_code, self.table_type, self.table_category, self.cardinality, self.is_object, self.is_rich, self.is_tenant, self.is_local, self.table_comment, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes)
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["system_table_uid"], d["system_table_name"], d["parent_system_table_uid"], d["table_label"], d["uid_name"], d["table_group"], d["table_code"], d["table_type"], d["table_category"], d["cardinality"], d["is_object"], d["is_rich"], d["is_tenant"], d["is_local"], d["table_comment"], d["row_instance"], d["row_lock"], d["row_owner"], d["row_seq"], d["row_guid"], d["row_version"], d["is_active"], d["created_date"], d["created_by"], d["last_updated_date"], d["last_updated_by"], d["removed_date"], d["removed_by"], d["custom_attributes"])
    def to_read_dict(self) -> dict:
        return asdict(self)
    def to_write(self) -> system_table_write_dto:
        return system_table_write_dto(self.system_table_uid, self.system_table_name, self.parent_system_table_uid, self.table_label, self.uid_name, self.table_group, self.table_code, self.table_type, self.table_category, self.cardinality, self.is_object, self.is_rich, self.is_tenant, self.is_local, self.table_comment, self.custom_attributes)
    def to_thin(self) -> system_table_thin_dto:
        return system_table_thin_dto(self.system_table_uid, self.system_table_name, self.created_date, self.is_active)
    def touch(self, updated_by: str = "system"):
        self.last_updated_date = datetime.datetime.now()
        self.last_updated_by = updated_by
        self.row_version = self.row_version+1
    def get_list_all_values(self) -> list[any]:
        return [self.system_table_uid, self.system_table_name, self.parent_system_table_uid, self.table_label, self.uid_name, self.table_group, self.table_code, self.table_type, self.table_category, self.cardinality, self.is_object, self.is_rich, self.is_tenant, self.is_local, self.table_comment, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]
    def get_list_update_values(self, updated_by: str) -> list[any]:
        return [self.system_table_name, self.parent_system_table_uid, self.table_label, self.uid_name, self.table_group, self.table_code, self.table_type, self.table_category, self.cardinality, self.is_object, self.is_rich, self.is_tenant, self.is_local, self.table_comment, self.custom_attributes, updated_by, self.system_table_uid]
    def is_older_than(self, dt: datetime.datetime) -> bool:
        return self.created_date < dt
    def is_newer_than(self, dt: datetime.datetime) -> bool:
        return self.created_date > dt
    def to_json_read(self) -> str:
        return json.dumps(self.to_read_dict())


@dataclass(frozen=False)
class system_thread_read_dto(base_read_dto, system_thread_write_dto):
    system_thread_uid: str
    system_thread_name: str
    thread_name: str
    thread_id: int
    parent_object: str
    ticks_count: int
    is_alive: int
    sleep_time: int
    row_instance: str
    row_lock: str | None
    row_owner: str
    row_seq: int
    row_guid: str
    row_version: int
    is_active: int
    created_date: datetime.datetime
    created_by: str
    last_updated_date: datetime.datetime
    last_updated_by: str
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str
    def __init__(self, system_thread_uid: str, system_thread_name: str, thread_name: str, thread_id: int, parent_object: str, ticks_count: int, is_alive: int, sleep_time: int, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
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
    @classmethod
    def empty_read(cls):
        return cls(0, "", "", "", 0, "", 0, 0, 0, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def default_read(cls):
        return cls(0, base_dto.get_random_uid(), "", "", 0, "", 0, 0, 0, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def random_read(cls):
        return cls(0, base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), 0, base_dto.get_random_uid(), 0, 0, 0, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_default(cls, system_thread_uid: str, system_thread_name: str, thread_name: str, thread_id: int, parent_object: str, ticks_count: int, is_alive: int, sleep_time: int):
        return cls(0, system_thread_uid, system_thread_name, thread_name, thread_id, parent_object, ticks_count, is_alive, sleep_time, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_full(cls, system_thread_uid: str, system_thread_name: str, thread_name: str, thread_id: int, parent_object: str, ticks_count: int, is_alive: int, sleep_time: int, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
        return cls(system_thread_uid, system_thread_name, thread_name, thread_id, parent_object, ticks_count, is_alive, sleep_time, row_instance, row_lock, row_owner, row_seq, row_guid, row_version, is_active, created_date, created_by, last_updated_date, last_updated_by, removed_date, removed_by, custom_attributes)
    @classmethod
    def from_write(cls, dto: system_thread_write_dto):
        return cls(0, dto.system_thread_uid, dto.system_thread_name, dto.thread_name, dto.thread_id, dto.parent_object, dto.ticks_count, dto.is_alive, dto.sleep_time, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, dto.custom_attributes)
    def clone_read(self):
        return system_thread_read_dto(self.system_thread_uid, self.system_thread_name, self.thread_name, self.thread_id, self.parent_object, self.ticks_count, self.is_alive, self.sleep_time, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes)
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["system_thread_uid"], d["system_thread_name"], d["thread_name"], d["thread_id"], d["parent_object"], d["ticks_count"], d["is_alive"], d["sleep_time"], d["row_instance"], d["row_lock"], d["row_owner"], d["row_seq"], d["row_guid"], d["row_version"], d["is_active"], d["created_date"], d["created_by"], d["last_updated_date"], d["last_updated_by"], d["removed_date"], d["removed_by"], d["custom_attributes"])
    def to_read_dict(self) -> dict:
        return asdict(self)
    def to_write(self) -> system_thread_write_dto:
        return system_thread_write_dto(self.system_thread_uid, self.system_thread_name, self.thread_name, self.thread_id, self.parent_object, self.ticks_count, self.is_alive, self.sleep_time, self.custom_attributes)
    def to_thin(self) -> system_thread_thin_dto:
        return system_thread_thin_dto(self.system_thread_uid, self.system_thread_name, self.created_date, self.is_active)
    def touch(self, updated_by: str = "system"):
        self.last_updated_date = datetime.datetime.now()
        self.last_updated_by = updated_by
        self.row_version = self.row_version+1
    def get_list_all_values(self) -> list[any]:
        return [self.system_thread_uid, self.system_thread_name, self.thread_name, self.thread_id, self.parent_object, self.ticks_count, self.is_alive, self.sleep_time, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]
    def get_list_update_values(self, updated_by: str) -> list[any]:
        return [self.system_thread_name, self.thread_name, self.thread_id, self.parent_object, self.ticks_count, self.is_alive, self.sleep_time, self.custom_attributes, updated_by, self.system_thread_uid]
    def is_older_than(self, dt: datetime.datetime) -> bool:
        return self.created_date < dt
    def is_newer_than(self, dt: datetime.datetime) -> bool:
        return self.created_date > dt
    def to_json_read(self) -> str:
        return json.dumps(self.to_read_dict())


@dataclass(frozen=False)
class system_version_read_dto(base_read_dto, system_version_write_dto):
    system_version_uid: str
    system_version_name: str
    version_description: str
    row_instance: str
    row_lock: str | None
    row_owner: str
    row_seq: int
    row_guid: str
    row_version: int
    is_active: int
    created_date: datetime.datetime
    created_by: str
    last_updated_date: datetime.datetime
    last_updated_by: str
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str
    def __init__(self, system_version_uid: str, system_version_name: str, version_description: str, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
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
    @classmethod
    def empty_read(cls):
        return cls(0, "", "", "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def default_read(cls):
        return cls(0, base_dto.get_random_uid(), "", "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def random_read(cls):
        return cls(0, base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_default(cls, system_version_uid: str, system_version_name: str, version_description: str):
        return cls(0, system_version_uid, system_version_name, version_description, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_full(cls, system_version_uid: str, system_version_name: str, version_description: str, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
        return cls(system_version_uid, system_version_name, version_description, row_instance, row_lock, row_owner, row_seq, row_guid, row_version, is_active, created_date, created_by, last_updated_date, last_updated_by, removed_date, removed_by, custom_attributes)
    @classmethod
    def from_write(cls, dto: system_version_write_dto):
        return cls(0, dto.system_version_uid, dto.system_version_name, dto.version_description, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, dto.custom_attributes)
    def clone_read(self):
        return system_version_read_dto(self.system_version_uid, self.system_version_name, self.version_description, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes)
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["system_version_uid"], d["system_version_name"], d["version_description"], d["row_instance"], d["row_lock"], d["row_owner"], d["row_seq"], d["row_guid"], d["row_version"], d["is_active"], d["created_date"], d["created_by"], d["last_updated_date"], d["last_updated_by"], d["removed_date"], d["removed_by"], d["custom_attributes"])
    def to_read_dict(self) -> dict:
        return asdict(self)
    def to_write(self) -> system_version_write_dto:
        return system_version_write_dto(self.system_version_uid, self.system_version_name, self.version_description, self.custom_attributes)
    def to_thin(self) -> system_version_thin_dto:
        return system_version_thin_dto(self.system_version_uid, self.system_version_name, self.created_date, self.is_active)
    def touch(self, updated_by: str = "system"):
        self.last_updated_date = datetime.datetime.now()
        self.last_updated_by = updated_by
        self.row_version = self.row_version+1
    def get_list_all_values(self) -> list[any]:
        return [self.system_version_uid, self.system_version_name, self.version_description, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]
    def get_list_update_values(self, updated_by: str) -> list[any]:
        return [self.system_version_name, self.version_description, self.custom_attributes, updated_by, self.system_version_uid]
    def is_older_than(self, dt: datetime.datetime) -> bool:
        return self.created_date < dt
    def is_newer_than(self, dt: datetime.datetime) -> bool:
        return self.created_date > dt
    def to_json_read(self) -> str:
        return json.dumps(self.to_read_dict())


@dataclass(frozen=False)
class tenant_read_dto(base_read_dto, tenant_write_dto):
    tenant_uid: str
    tenant_name: str
    country_uid: str
    tenant_type_uid: str
    tenant_category_uid: str
    tenant_code: str
    tenant_description: str
    start_date: datetime.datetime
    end_date: datetime.datetime | None
    is_internal: int
    is_system: int
    is_test: int
    account_uid: str | None
    row_instance: str
    row_lock: str | None
    row_owner: str
    row_seq: int
    row_guid: str
    row_version: int
    is_active: int
    created_date: datetime.datetime
    created_by: str
    last_updated_date: datetime.datetime
    last_updated_by: str
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str
    def __init__(self, tenant_uid: str, tenant_name: str, country_uid: str, tenant_type_uid: str, tenant_category_uid: str, tenant_code: str, tenant_description: str, start_date: datetime.datetime, end_date: datetime.datetime | None, is_internal: int, is_system: int, is_test: int, account_uid: str | None, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
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
    @classmethod
    def empty_read(cls):
        return cls(0, "", "", "", "", "", "", "", datetime.datetime.now(), datetime.datetime.now(), 0, 0, 0, "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def default_read(cls):
        return cls(0, base_dto.get_random_uid(), "", "", "", "", "", "", datetime.datetime.now(), datetime.datetime.now(), 0, 0, 0, "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def random_read(cls):
        return cls(0, base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), datetime.datetime.now(), datetime.datetime.now(), 0, 0, 0, base_dto.get_random_uid(), "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_default(cls, tenant_uid: str, tenant_name: str, country_uid: str, tenant_type_uid: str, tenant_category_uid: str, tenant_code: str, tenant_description: str, start_date: datetime.datetime, end_date: datetime.datetime | None, is_internal: int, is_system: int, is_test: int, account_uid: str | None):
        return cls(0, tenant_uid, tenant_name, country_uid, tenant_type_uid, tenant_category_uid, tenant_code, tenant_description, start_date, end_date, is_internal, is_system, is_test, account_uid, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_full(cls, tenant_uid: str, tenant_name: str, country_uid: str, tenant_type_uid: str, tenant_category_uid: str, tenant_code: str, tenant_description: str, start_date: datetime.datetime, end_date: datetime.datetime | None, is_internal: int, is_system: int, is_test: int, account_uid: str | None, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
        return cls(tenant_uid, tenant_name, country_uid, tenant_type_uid, tenant_category_uid, tenant_code, tenant_description, start_date, end_date, is_internal, is_system, is_test, account_uid, row_instance, row_lock, row_owner, row_seq, row_guid, row_version, is_active, created_date, created_by, last_updated_date, last_updated_by, removed_date, removed_by, custom_attributes)
    @classmethod
    def from_write(cls, dto: tenant_write_dto):
        return cls(0, dto.tenant_uid, dto.tenant_name, dto.country_uid, dto.tenant_type_uid, dto.tenant_category_uid, dto.tenant_code, dto.tenant_description, dto.start_date, dto.end_date, dto.is_internal, dto.is_system, dto.is_test, dto.account_uid, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, dto.custom_attributes)
    def clone_read(self):
        return tenant_read_dto(self.tenant_uid, self.tenant_name, self.country_uid, self.tenant_type_uid, self.tenant_category_uid, self.tenant_code, self.tenant_description, self.start_date, self.end_date, self.is_internal, self.is_system, self.is_test, self.account_uid, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes)
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["tenant_uid"], d["tenant_name"], d["country_uid"], d["tenant_type_uid"], d["tenant_category_uid"], d["tenant_code"], d["tenant_description"], d["start_date"], d["end_date"], d["is_internal"], d["is_system"], d["is_test"], d["account_uid"], d["row_instance"], d["row_lock"], d["row_owner"], d["row_seq"], d["row_guid"], d["row_version"], d["is_active"], d["created_date"], d["created_by"], d["last_updated_date"], d["last_updated_by"], d["removed_date"], d["removed_by"], d["custom_attributes"])
    def to_read_dict(self) -> dict:
        return asdict(self)
    def to_write(self) -> tenant_write_dto:
        return tenant_write_dto(self.tenant_uid, self.tenant_name, self.country_uid, self.tenant_type_uid, self.tenant_category_uid, self.tenant_code, self.tenant_description, self.start_date, self.end_date, self.is_internal, self.is_system, self.is_test, self.account_uid, self.custom_attributes)
    def to_thin(self) -> tenant_thin_dto:
        return tenant_thin_dto(self.tenant_uid, self.tenant_name, self.created_date, self.is_active)
    def touch(self, updated_by: str = "system"):
        self.last_updated_date = datetime.datetime.now()
        self.last_updated_by = updated_by
        self.row_version = self.row_version+1
    def get_list_all_values(self) -> list[any]:
        return [self.tenant_uid, self.tenant_name, self.country_uid, self.tenant_type_uid, self.tenant_category_uid, self.tenant_code, self.tenant_description, self.start_date, self.end_date, self.is_internal, self.is_system, self.is_test, self.account_uid, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]
    def get_list_update_values(self, updated_by: str) -> list[any]:
        return [self.tenant_name, self.country_uid, self.tenant_type_uid, self.tenant_category_uid, self.tenant_code, self.tenant_description, self.start_date, self.end_date, self.is_internal, self.is_system, self.is_test, self.account_uid, self.custom_attributes, updated_by, self.tenant_uid]
    def is_older_than(self, dt: datetime.datetime) -> bool:
        return self.created_date < dt
    def is_newer_than(self, dt: datetime.datetime) -> bool:
        return self.created_date > dt
    def to_json_read(self) -> str:
        return json.dumps(self.to_read_dict())


@dataclass(frozen=False)
class tenant_account_read_dto(base_read_dto, tenant_account_write_dto):
    tenant_account_uid: str
    tenant_account_name: str
    tenant_uid: str
    account_uid: str
    tenant_role_uid: str
    row_instance: str
    row_lock: str | None
    row_owner: str
    row_seq: int
    row_guid: str
    row_version: int
    is_active: int
    created_date: datetime.datetime
    created_by: str
    last_updated_date: datetime.datetime
    last_updated_by: str
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str
    def __init__(self, tenant_account_uid: str, tenant_account_name: str, tenant_uid: str, account_uid: str, tenant_role_uid: str, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
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
    @classmethod
    def empty_read(cls):
        return cls(0, "", "", "", "", "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def default_read(cls):
        return cls(0, base_dto.get_random_uid(), "", "", "", "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def random_read(cls):
        return cls(0, base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_default(cls, tenant_account_uid: str, tenant_account_name: str, tenant_uid: str, account_uid: str, tenant_role_uid: str):
        return cls(0, tenant_account_uid, tenant_account_name, tenant_uid, account_uid, tenant_role_uid, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_full(cls, tenant_account_uid: str, tenant_account_name: str, tenant_uid: str, account_uid: str, tenant_role_uid: str, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
        return cls(tenant_account_uid, tenant_account_name, tenant_uid, account_uid, tenant_role_uid, row_instance, row_lock, row_owner, row_seq, row_guid, row_version, is_active, created_date, created_by, last_updated_date, last_updated_by, removed_date, removed_by, custom_attributes)
    @classmethod
    def from_write(cls, dto: tenant_account_write_dto):
        return cls(0, dto.tenant_account_uid, dto.tenant_account_name, dto.tenant_uid, dto.account_uid, dto.tenant_role_uid, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, dto.custom_attributes)
    def clone_read(self):
        return tenant_account_read_dto(self.tenant_account_uid, self.tenant_account_name, self.tenant_uid, self.account_uid, self.tenant_role_uid, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes)
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["tenant_account_uid"], d["tenant_account_name"], d["tenant_uid"], d["account_uid"], d["tenant_role_uid"], d["row_instance"], d["row_lock"], d["row_owner"], d["row_seq"], d["row_guid"], d["row_version"], d["is_active"], d["created_date"], d["created_by"], d["last_updated_date"], d["last_updated_by"], d["removed_date"], d["removed_by"], d["custom_attributes"])
    def to_read_dict(self) -> dict:
        return asdict(self)
    def to_write(self) -> tenant_account_write_dto:
        return tenant_account_write_dto(self.tenant_account_uid, self.tenant_account_name, self.tenant_uid, self.account_uid, self.tenant_role_uid, self.custom_attributes)
    def to_thin(self) -> tenant_account_thin_dto:
        return tenant_account_thin_dto(self.tenant_account_uid, self.tenant_account_name, self.created_date, self.is_active)
    def touch(self, updated_by: str = "system"):
        self.last_updated_date = datetime.datetime.now()
        self.last_updated_by = updated_by
        self.row_version = self.row_version+1
    def get_list_all_values(self) -> list[any]:
        return [self.tenant_account_uid, self.tenant_account_name, self.tenant_uid, self.account_uid, self.tenant_role_uid, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]
    def get_list_update_values(self, updated_by: str) -> list[any]:
        return [self.tenant_account_name, self.tenant_uid, self.account_uid, self.tenant_role_uid, self.custom_attributes, updated_by, self.tenant_account_uid]
    def is_older_than(self, dt: datetime.datetime) -> bool:
        return self.created_date < dt
    def is_newer_than(self, dt: datetime.datetime) -> bool:
        return self.created_date > dt
    def to_json_read(self) -> str:
        return json.dumps(self.to_read_dict())


@dataclass(frozen=False)
class tenant_category_read_dto(base_read_dto, tenant_category_write_dto):
    tenant_category_uid: str
    tenant_category_name: str
    tenant_category_description: str
    row_instance: str
    row_lock: str | None
    row_owner: str
    row_seq: int
    row_guid: str
    row_version: int
    is_active: int
    created_date: datetime.datetime
    created_by: str
    last_updated_date: datetime.datetime
    last_updated_by: str
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str
    def __init__(self, tenant_category_uid: str, tenant_category_name: str, tenant_category_description: str, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
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
    @classmethod
    def empty_read(cls):
        return cls(0, "", "", "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def default_read(cls):
        return cls(0, base_dto.get_random_uid(), "", "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def random_read(cls):
        return cls(0, base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_default(cls, tenant_category_uid: str, tenant_category_name: str, tenant_category_description: str):
        return cls(0, tenant_category_uid, tenant_category_name, tenant_category_description, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_full(cls, tenant_category_uid: str, tenant_category_name: str, tenant_category_description: str, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
        return cls(tenant_category_uid, tenant_category_name, tenant_category_description, row_instance, row_lock, row_owner, row_seq, row_guid, row_version, is_active, created_date, created_by, last_updated_date, last_updated_by, removed_date, removed_by, custom_attributes)
    @classmethod
    def from_write(cls, dto: tenant_category_write_dto):
        return cls(0, dto.tenant_category_uid, dto.tenant_category_name, dto.tenant_category_description, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, dto.custom_attributes)
    def clone_read(self):
        return tenant_category_read_dto(self.tenant_category_uid, self.tenant_category_name, self.tenant_category_description, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes)
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["tenant_category_uid"], d["tenant_category_name"], d["tenant_category_description"], d["row_instance"], d["row_lock"], d["row_owner"], d["row_seq"], d["row_guid"], d["row_version"], d["is_active"], d["created_date"], d["created_by"], d["last_updated_date"], d["last_updated_by"], d["removed_date"], d["removed_by"], d["custom_attributes"])
    def to_read_dict(self) -> dict:
        return asdict(self)
    def to_write(self) -> tenant_category_write_dto:
        return tenant_category_write_dto(self.tenant_category_uid, self.tenant_category_name, self.tenant_category_description, self.custom_attributes)
    def to_thin(self) -> tenant_category_thin_dto:
        return tenant_category_thin_dto(self.tenant_category_uid, self.tenant_category_name, self.created_date, self.is_active)
    def touch(self, updated_by: str = "system"):
        self.last_updated_date = datetime.datetime.now()
        self.last_updated_by = updated_by
        self.row_version = self.row_version+1
    def get_list_all_values(self) -> list[any]:
        return [self.tenant_category_uid, self.tenant_category_name, self.tenant_category_description, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]
    def get_list_update_values(self, updated_by: str) -> list[any]:
        return [self.tenant_category_name, self.tenant_category_description, self.custom_attributes, updated_by, self.tenant_category_uid]
    def is_older_than(self, dt: datetime.datetime) -> bool:
        return self.created_date < dt
    def is_newer_than(self, dt: datetime.datetime) -> bool:
        return self.created_date > dt
    def to_json_read(self) -> str:
        return json.dumps(self.to_read_dict())


@dataclass(frozen=False)
class tenant_country_read_dto(base_read_dto, tenant_country_write_dto):
    tenant_country_uid: str
    tenant_country_name: str
    country_uid: str
    tenant_uid: str
    country_priority: int
    row_instance: str
    row_lock: str | None
    row_owner: str
    row_seq: int
    row_guid: str
    row_version: int
    is_active: int
    created_date: datetime.datetime
    created_by: str
    last_updated_date: datetime.datetime
    last_updated_by: str
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str
    def __init__(self, tenant_country_uid: str, tenant_country_name: str, country_uid: str, tenant_uid: str, country_priority: int, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
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
    @classmethod
    def empty_read(cls):
        return cls(0, "", "", "", "", 0, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def default_read(cls):
        return cls(0, base_dto.get_random_uid(), "", "", "", 0, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def random_read(cls):
        return cls(0, base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), 0, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_default(cls, tenant_country_uid: str, tenant_country_name: str, country_uid: str, tenant_uid: str, country_priority: int):
        return cls(0, tenant_country_uid, tenant_country_name, country_uid, tenant_uid, country_priority, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_full(cls, tenant_country_uid: str, tenant_country_name: str, country_uid: str, tenant_uid: str, country_priority: int, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
        return cls(tenant_country_uid, tenant_country_name, country_uid, tenant_uid, country_priority, row_instance, row_lock, row_owner, row_seq, row_guid, row_version, is_active, created_date, created_by, last_updated_date, last_updated_by, removed_date, removed_by, custom_attributes)
    @classmethod
    def from_write(cls, dto: tenant_country_write_dto):
        return cls(0, dto.tenant_country_uid, dto.tenant_country_name, dto.country_uid, dto.tenant_uid, dto.country_priority, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, dto.custom_attributes)
    def clone_read(self):
        return tenant_country_read_dto(self.tenant_country_uid, self.tenant_country_name, self.country_uid, self.tenant_uid, self.country_priority, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes)
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["tenant_country_uid"], d["tenant_country_name"], d["country_uid"], d["tenant_uid"], d["country_priority"], d["row_instance"], d["row_lock"], d["row_owner"], d["row_seq"], d["row_guid"], d["row_version"], d["is_active"], d["created_date"], d["created_by"], d["last_updated_date"], d["last_updated_by"], d["removed_date"], d["removed_by"], d["custom_attributes"])
    def to_read_dict(self) -> dict:
        return asdict(self)
    def to_write(self) -> tenant_country_write_dto:
        return tenant_country_write_dto(self.tenant_country_uid, self.tenant_country_name, self.country_uid, self.tenant_uid, self.country_priority, self.custom_attributes)
    def to_thin(self) -> tenant_country_thin_dto:
        return tenant_country_thin_dto(self.tenant_country_uid, self.tenant_country_name, self.created_date, self.is_active)
    def touch(self, updated_by: str = "system"):
        self.last_updated_date = datetime.datetime.now()
        self.last_updated_by = updated_by
        self.row_version = self.row_version+1
    def get_list_all_values(self) -> list[any]:
        return [self.tenant_country_uid, self.tenant_country_name, self.country_uid, self.tenant_uid, self.country_priority, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]
    def get_list_update_values(self, updated_by: str) -> list[any]:
        return [self.tenant_country_name, self.country_uid, self.tenant_uid, self.country_priority, self.custom_attributes, updated_by, self.tenant_country_uid]
    def is_older_than(self, dt: datetime.datetime) -> bool:
        return self.created_date < dt
    def is_newer_than(self, dt: datetime.datetime) -> bool:
        return self.created_date > dt
    def to_json_read(self) -> str:
        return json.dumps(self.to_read_dict())


@dataclass(frozen=False)
class tenant_license_read_dto(base_read_dto, tenant_license_write_dto):
    tenant_license_uid: str
    tenant_license_name: str
    tenant_uid: str
    system_license_uid: str
    start_date: datetime.datetime
    end_date: datetime.datetime
    accounts_count: int
    is_approved: int
    row_instance: str
    row_lock: str | None
    row_owner: str
    row_seq: int
    row_guid: str
    row_version: int
    is_active: int
    created_date: datetime.datetime
    created_by: str
    last_updated_date: datetime.datetime
    last_updated_by: str
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str
    def __init__(self, tenant_license_uid: str, tenant_license_name: str, tenant_uid: str, system_license_uid: str, start_date: datetime.datetime, end_date: datetime.datetime, accounts_count: int, is_approved: int, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
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
    @classmethod
    def empty_read(cls):
        return cls(0, "", "", "", "", datetime.datetime.now(), datetime.datetime.now(), 0, 0, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def default_read(cls):
        return cls(0, base_dto.get_random_uid(), "", "", "", datetime.datetime.now(), datetime.datetime.now(), 0, 0, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def random_read(cls):
        return cls(0, base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), datetime.datetime.now(), datetime.datetime.now(), 0, 0, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_default(cls, tenant_license_uid: str, tenant_license_name: str, tenant_uid: str, system_license_uid: str, start_date: datetime.datetime, end_date: datetime.datetime, accounts_count: int, is_approved: int):
        return cls(0, tenant_license_uid, tenant_license_name, tenant_uid, system_license_uid, start_date, end_date, accounts_count, is_approved, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_full(cls, tenant_license_uid: str, tenant_license_name: str, tenant_uid: str, system_license_uid: str, start_date: datetime.datetime, end_date: datetime.datetime, accounts_count: int, is_approved: int, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
        return cls(tenant_license_uid, tenant_license_name, tenant_uid, system_license_uid, start_date, end_date, accounts_count, is_approved, row_instance, row_lock, row_owner, row_seq, row_guid, row_version, is_active, created_date, created_by, last_updated_date, last_updated_by, removed_date, removed_by, custom_attributes)
    @classmethod
    def from_write(cls, dto: tenant_license_write_dto):
        return cls(0, dto.tenant_license_uid, dto.tenant_license_name, dto.tenant_uid, dto.system_license_uid, dto.start_date, dto.end_date, dto.accounts_count, dto.is_approved, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, dto.custom_attributes)
    def clone_read(self):
        return tenant_license_read_dto(self.tenant_license_uid, self.tenant_license_name, self.tenant_uid, self.system_license_uid, self.start_date, self.end_date, self.accounts_count, self.is_approved, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes)
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["tenant_license_uid"], d["tenant_license_name"], d["tenant_uid"], d["system_license_uid"], d["start_date"], d["end_date"], d["accounts_count"], d["is_approved"], d["row_instance"], d["row_lock"], d["row_owner"], d["row_seq"], d["row_guid"], d["row_version"], d["is_active"], d["created_date"], d["created_by"], d["last_updated_date"], d["last_updated_by"], d["removed_date"], d["removed_by"], d["custom_attributes"])
    def to_read_dict(self) -> dict:
        return asdict(self)
    def to_write(self) -> tenant_license_write_dto:
        return tenant_license_write_dto(self.tenant_license_uid, self.tenant_license_name, self.tenant_uid, self.system_license_uid, self.start_date, self.end_date, self.accounts_count, self.is_approved, self.custom_attributes)
    def to_thin(self) -> tenant_license_thin_dto:
        return tenant_license_thin_dto(self.tenant_license_uid, self.tenant_license_name, self.created_date, self.is_active)
    def touch(self, updated_by: str = "system"):
        self.last_updated_date = datetime.datetime.now()
        self.last_updated_by = updated_by
        self.row_version = self.row_version+1
    def get_list_all_values(self) -> list[any]:
        return [self.tenant_license_uid, self.tenant_license_name, self.tenant_uid, self.system_license_uid, self.start_date, self.end_date, self.accounts_count, self.is_approved, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]
    def get_list_update_values(self, updated_by: str) -> list[any]:
        return [self.tenant_license_name, self.tenant_uid, self.system_license_uid, self.start_date, self.end_date, self.accounts_count, self.is_approved, self.custom_attributes, updated_by, self.tenant_license_uid]
    def is_older_than(self, dt: datetime.datetime) -> bool:
        return self.created_date < dt
    def is_newer_than(self, dt: datetime.datetime) -> bool:
        return self.created_date > dt
    def to_json_read(self) -> str:
        return json.dumps(self.to_read_dict())


@dataclass(frozen=False)
class tenant_payment_read_dto(base_read_dto, tenant_payment_write_dto):
    tenant_payment_uid: str
    tenant_payment_name: str
    tenant_uid: str
    account_uid: str
    currency_uid: str
    tenant_payment_type_uid: str
    start_date: datetime.datetime
    end_date: datetime.datetime | None
    payment_value: str
    source_number: str
    source_reference: str
    is_approved: int
    row_instance: str
    row_lock: str | None
    row_owner: str
    row_seq: int
    row_guid: str
    row_version: int
    is_active: int
    created_date: datetime.datetime
    created_by: str
    last_updated_date: datetime.datetime
    last_updated_by: str
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str
    def __init__(self, tenant_payment_uid: str, tenant_payment_name: str, tenant_uid: str, account_uid: str, currency_uid: str, tenant_payment_type_uid: str, start_date: datetime.datetime, end_date: datetime.datetime | None, payment_value: str, source_number: str, source_reference: str, is_approved: int, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
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
    @classmethod
    def empty_read(cls):
        return cls(0, "", "", "", "", "", "", datetime.datetime.now(), datetime.datetime.now(), "", "", "", 0, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def default_read(cls):
        return cls(0, base_dto.get_random_uid(), "", "", "", "", "", datetime.datetime.now(), datetime.datetime.now(), "", "", "", 0, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def random_read(cls):
        return cls(0, base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), datetime.datetime.now(), datetime.datetime.now(), "", base_dto.get_random_uid(), base_dto.get_random_uid(), 0, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_default(cls, tenant_payment_uid: str, tenant_payment_name: str, tenant_uid: str, account_uid: str, currency_uid: str, tenant_payment_type_uid: str, start_date: datetime.datetime, end_date: datetime.datetime | None, payment_value: str, source_number: str, source_reference: str, is_approved: int):
        return cls(0, tenant_payment_uid, tenant_payment_name, tenant_uid, account_uid, currency_uid, tenant_payment_type_uid, start_date, end_date, payment_value, source_number, source_reference, is_approved, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_full(cls, tenant_payment_uid: str, tenant_payment_name: str, tenant_uid: str, account_uid: str, currency_uid: str, tenant_payment_type_uid: str, start_date: datetime.datetime, end_date: datetime.datetime | None, payment_value: str, source_number: str, source_reference: str, is_approved: int, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
        return cls(tenant_payment_uid, tenant_payment_name, tenant_uid, account_uid, currency_uid, tenant_payment_type_uid, start_date, end_date, payment_value, source_number, source_reference, is_approved, row_instance, row_lock, row_owner, row_seq, row_guid, row_version, is_active, created_date, created_by, last_updated_date, last_updated_by, removed_date, removed_by, custom_attributes)
    @classmethod
    def from_write(cls, dto: tenant_payment_write_dto):
        return cls(0, dto.tenant_payment_uid, dto.tenant_payment_name, dto.tenant_uid, dto.account_uid, dto.currency_uid, dto.tenant_payment_type_uid, dto.start_date, dto.end_date, dto.payment_value, dto.source_number, dto.source_reference, dto.is_approved, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, dto.custom_attributes)
    def clone_read(self):
        return tenant_payment_read_dto(self.tenant_payment_uid, self.tenant_payment_name, self.tenant_uid, self.account_uid, self.currency_uid, self.tenant_payment_type_uid, self.start_date, self.end_date, self.payment_value, self.source_number, self.source_reference, self.is_approved, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes)
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["tenant_payment_uid"], d["tenant_payment_name"], d["tenant_uid"], d["account_uid"], d["currency_uid"], d["tenant_payment_type_uid"], d["start_date"], d["end_date"], d["payment_value"], d["source_number"], d["source_reference"], d["is_approved"], d["row_instance"], d["row_lock"], d["row_owner"], d["row_seq"], d["row_guid"], d["row_version"], d["is_active"], d["created_date"], d["created_by"], d["last_updated_date"], d["last_updated_by"], d["removed_date"], d["removed_by"], d["custom_attributes"])
    def to_read_dict(self) -> dict:
        return asdict(self)
    def to_write(self) -> tenant_payment_write_dto:
        return tenant_payment_write_dto(self.tenant_payment_uid, self.tenant_payment_name, self.tenant_uid, self.account_uid, self.currency_uid, self.tenant_payment_type_uid, self.start_date, self.end_date, self.payment_value, self.source_number, self.source_reference, self.is_approved, self.custom_attributes)
    def to_thin(self) -> tenant_payment_thin_dto:
        return tenant_payment_thin_dto(self.tenant_payment_uid, self.tenant_payment_name, self.created_date, self.is_active)
    def touch(self, updated_by: str = "system"):
        self.last_updated_date = datetime.datetime.now()
        self.last_updated_by = updated_by
        self.row_version = self.row_version+1
    def get_list_all_values(self) -> list[any]:
        return [self.tenant_payment_uid, self.tenant_payment_name, self.tenant_uid, self.account_uid, self.currency_uid, self.tenant_payment_type_uid, self.start_date, self.end_date, self.payment_value, self.source_number, self.source_reference, self.is_approved, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]
    def get_list_update_values(self, updated_by: str) -> list[any]:
        return [self.tenant_payment_name, self.tenant_uid, self.account_uid, self.currency_uid, self.tenant_payment_type_uid, self.start_date, self.end_date, self.payment_value, self.source_number, self.source_reference, self.is_approved, self.custom_attributes, updated_by, self.tenant_payment_uid]
    def is_older_than(self, dt: datetime.datetime) -> bool:
        return self.created_date < dt
    def is_newer_than(self, dt: datetime.datetime) -> bool:
        return self.created_date > dt
    def to_json_read(self) -> str:
        return json.dumps(self.to_read_dict())


@dataclass(frozen=False)
class tenant_payment_type_read_dto(base_read_dto, tenant_payment_type_write_dto):
    tenant_payment_type_uid: str
    tenant_payment_type_name: str
    row_instance: str
    row_lock: str | None
    row_owner: str
    row_seq: int
    row_guid: str
    row_version: int
    is_active: int
    created_date: datetime.datetime
    created_by: str
    last_updated_date: datetime.datetime
    last_updated_by: str
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str
    def __init__(self, tenant_payment_type_uid: str, tenant_payment_type_name: str, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
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
    @classmethod
    def empty_read(cls):
        return cls(0, "", "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def default_read(cls):
        return cls(0, base_dto.get_random_uid(), "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def random_read(cls):
        return cls(0, base_dto.get_random_uid(), base_dto.get_random_uid(), "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_default(cls, tenant_payment_type_uid: str, tenant_payment_type_name: str):
        return cls(0, tenant_payment_type_uid, tenant_payment_type_name, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_full(cls, tenant_payment_type_uid: str, tenant_payment_type_name: str, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
        return cls(tenant_payment_type_uid, tenant_payment_type_name, row_instance, row_lock, row_owner, row_seq, row_guid, row_version, is_active, created_date, created_by, last_updated_date, last_updated_by, removed_date, removed_by, custom_attributes)
    @classmethod
    def from_write(cls, dto: tenant_payment_type_write_dto):
        return cls(0, dto.tenant_payment_type_uid, dto.tenant_payment_type_name, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, dto.custom_attributes)
    def clone_read(self):
        return tenant_payment_type_read_dto(self.tenant_payment_type_uid, self.tenant_payment_type_name, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes)
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["tenant_payment_type_uid"], d["tenant_payment_type_name"], d["row_instance"], d["row_lock"], d["row_owner"], d["row_seq"], d["row_guid"], d["row_version"], d["is_active"], d["created_date"], d["created_by"], d["last_updated_date"], d["last_updated_by"], d["removed_date"], d["removed_by"], d["custom_attributes"])
    def to_read_dict(self) -> dict:
        return asdict(self)
    def to_write(self) -> tenant_payment_type_write_dto:
        return tenant_payment_type_write_dto(self.tenant_payment_type_uid, self.tenant_payment_type_name, self.custom_attributes)
    def to_thin(self) -> tenant_payment_type_thin_dto:
        return tenant_payment_type_thin_dto(self.tenant_payment_type_uid, self.tenant_payment_type_name, self.created_date, self.is_active)
    def touch(self, updated_by: str = "system"):
        self.last_updated_date = datetime.datetime.now()
        self.last_updated_by = updated_by
        self.row_version = self.row_version+1
    def get_list_all_values(self) -> list[any]:
        return [self.tenant_payment_type_uid, self.tenant_payment_type_name, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]
    def get_list_update_values(self, updated_by: str) -> list[any]:
        return [self.tenant_payment_type_name, self.custom_attributes, updated_by, self.tenant_payment_type_uid]
    def is_older_than(self, dt: datetime.datetime) -> bool:
        return self.created_date < dt
    def is_newer_than(self, dt: datetime.datetime) -> bool:
        return self.created_date > dt
    def to_json_read(self) -> str:
        return json.dumps(self.to_read_dict())


@dataclass(frozen=False)
class tenant_role_read_dto(base_read_dto, tenant_role_write_dto):
    tenant_role_uid: str
    tenant_role_name: str
    role_description: str
    row_instance: str
    row_lock: str | None
    row_owner: str
    row_seq: int
    row_guid: str
    row_version: int
    is_active: int
    created_date: datetime.datetime
    created_by: str
    last_updated_date: datetime.datetime
    last_updated_by: str
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str
    def __init__(self, tenant_role_uid: str, tenant_role_name: str, role_description: str, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
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
    @classmethod
    def empty_read(cls):
        return cls(0, "", "", "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def default_read(cls):
        return cls(0, base_dto.get_random_uid(), "", "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def random_read(cls):
        return cls(0, base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_default(cls, tenant_role_uid: str, tenant_role_name: str, role_description: str):
        return cls(0, tenant_role_uid, tenant_role_name, role_description, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_full(cls, tenant_role_uid: str, tenant_role_name: str, role_description: str, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
        return cls(tenant_role_uid, tenant_role_name, role_description, row_instance, row_lock, row_owner, row_seq, row_guid, row_version, is_active, created_date, created_by, last_updated_date, last_updated_by, removed_date, removed_by, custom_attributes)
    @classmethod
    def from_write(cls, dto: tenant_role_write_dto):
        return cls(0, dto.tenant_role_uid, dto.tenant_role_name, dto.role_description, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, dto.custom_attributes)
    def clone_read(self):
        return tenant_role_read_dto(self.tenant_role_uid, self.tenant_role_name, self.role_description, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes)
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["tenant_role_uid"], d["tenant_role_name"], d["role_description"], d["row_instance"], d["row_lock"], d["row_owner"], d["row_seq"], d["row_guid"], d["row_version"], d["is_active"], d["created_date"], d["created_by"], d["last_updated_date"], d["last_updated_by"], d["removed_date"], d["removed_by"], d["custom_attributes"])
    def to_read_dict(self) -> dict:
        return asdict(self)
    def to_write(self) -> tenant_role_write_dto:
        return tenant_role_write_dto(self.tenant_role_uid, self.tenant_role_name, self.role_description, self.custom_attributes)
    def to_thin(self) -> tenant_role_thin_dto:
        return tenant_role_thin_dto(self.tenant_role_uid, self.tenant_role_name, self.created_date, self.is_active)
    def touch(self, updated_by: str = "system"):
        self.last_updated_date = datetime.datetime.now()
        self.last_updated_by = updated_by
        self.row_version = self.row_version+1
    def get_list_all_values(self) -> list[any]:
        return [self.tenant_role_uid, self.tenant_role_name, self.role_description, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]
    def get_list_update_values(self, updated_by: str) -> list[any]:
        return [self.tenant_role_name, self.role_description, self.custom_attributes, updated_by, self.tenant_role_uid]
    def is_older_than(self, dt: datetime.datetime) -> bool:
        return self.created_date < dt
    def is_newer_than(self, dt: datetime.datetime) -> bool:
        return self.created_date > dt
    def to_json_read(self) -> str:
        return json.dumps(self.to_read_dict())


@dataclass(frozen=False)
class tenant_status_read_dto(base_read_dto, tenant_status_write_dto):
    tenant_status_uid: str
    tenant_status_name: str
    tenant_status_description: str
    row_instance: str
    row_lock: str | None
    row_owner: str
    row_seq: int
    row_guid: str
    row_version: int
    is_active: int
    created_date: datetime.datetime
    created_by: str
    last_updated_date: datetime.datetime
    last_updated_by: str
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str
    def __init__(self, tenant_status_uid: str, tenant_status_name: str, tenant_status_description: str, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
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
    @classmethod
    def empty_read(cls):
        return cls(0, "", "", "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def default_read(cls):
        return cls(0, base_dto.get_random_uid(), "", "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def random_read(cls):
        return cls(0, base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_default(cls, tenant_status_uid: str, tenant_status_name: str, tenant_status_description: str):
        return cls(0, tenant_status_uid, tenant_status_name, tenant_status_description, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_full(cls, tenant_status_uid: str, tenant_status_name: str, tenant_status_description: str, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
        return cls(tenant_status_uid, tenant_status_name, tenant_status_description, row_instance, row_lock, row_owner, row_seq, row_guid, row_version, is_active, created_date, created_by, last_updated_date, last_updated_by, removed_date, removed_by, custom_attributes)
    @classmethod
    def from_write(cls, dto: tenant_status_write_dto):
        return cls(0, dto.tenant_status_uid, dto.tenant_status_name, dto.tenant_status_description, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, dto.custom_attributes)
    def clone_read(self):
        return tenant_status_read_dto(self.tenant_status_uid, self.tenant_status_name, self.tenant_status_description, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes)
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["tenant_status_uid"], d["tenant_status_name"], d["tenant_status_description"], d["row_instance"], d["row_lock"], d["row_owner"], d["row_seq"], d["row_guid"], d["row_version"], d["is_active"], d["created_date"], d["created_by"], d["last_updated_date"], d["last_updated_by"], d["removed_date"], d["removed_by"], d["custom_attributes"])
    def to_read_dict(self) -> dict:
        return asdict(self)
    def to_write(self) -> tenant_status_write_dto:
        return tenant_status_write_dto(self.tenant_status_uid, self.tenant_status_name, self.tenant_status_description, self.custom_attributes)
    def to_thin(self) -> tenant_status_thin_dto:
        return tenant_status_thin_dto(self.tenant_status_uid, self.tenant_status_name, self.created_date, self.is_active)
    def touch(self, updated_by: str = "system"):
        self.last_updated_date = datetime.datetime.now()
        self.last_updated_by = updated_by
        self.row_version = self.row_version+1
    def get_list_all_values(self) -> list[any]:
        return [self.tenant_status_uid, self.tenant_status_name, self.tenant_status_description, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]
    def get_list_update_values(self, updated_by: str) -> list[any]:
        return [self.tenant_status_name, self.tenant_status_description, self.custom_attributes, updated_by, self.tenant_status_uid]
    def is_older_than(self, dt: datetime.datetime) -> bool:
        return self.created_date < dt
    def is_newer_than(self, dt: datetime.datetime) -> bool:
        return self.created_date > dt
    def to_json_read(self) -> str:
        return json.dumps(self.to_read_dict())


@dataclass(frozen=False)
class tenant_type_read_dto(base_read_dto, tenant_type_write_dto):
    tenant_type_uid: str
    tenant_type_name: str
    tenant_type_description: str
    row_instance: str
    row_lock: str | None
    row_owner: str
    row_seq: int
    row_guid: str
    row_version: int
    is_active: int
    created_date: datetime.datetime
    created_by: str
    last_updated_date: datetime.datetime
    last_updated_by: str
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str
    def __init__(self, tenant_type_uid: str, tenant_type_name: str, tenant_type_description: str, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
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
    @classmethod
    def empty_read(cls):
        return cls(0, "", "", "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def default_read(cls):
        return cls(0, base_dto.get_random_uid(), "", "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def random_read(cls):
        return cls(0, base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_default(cls, tenant_type_uid: str, tenant_type_name: str, tenant_type_description: str):
        return cls(0, tenant_type_uid, tenant_type_name, tenant_type_description, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_full(cls, tenant_type_uid: str, tenant_type_name: str, tenant_type_description: str, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
        return cls(tenant_type_uid, tenant_type_name, tenant_type_description, row_instance, row_lock, row_owner, row_seq, row_guid, row_version, is_active, created_date, created_by, last_updated_date, last_updated_by, removed_date, removed_by, custom_attributes)
    @classmethod
    def from_write(cls, dto: tenant_type_write_dto):
        return cls(0, dto.tenant_type_uid, dto.tenant_type_name, dto.tenant_type_description, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, dto.custom_attributes)
    def clone_read(self):
        return tenant_type_read_dto(self.tenant_type_uid, self.tenant_type_name, self.tenant_type_description, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes)
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["tenant_type_uid"], d["tenant_type_name"], d["tenant_type_description"], d["row_instance"], d["row_lock"], d["row_owner"], d["row_seq"], d["row_guid"], d["row_version"], d["is_active"], d["created_date"], d["created_by"], d["last_updated_date"], d["last_updated_by"], d["removed_date"], d["removed_by"], d["custom_attributes"])
    def to_read_dict(self) -> dict:
        return asdict(self)
    def to_write(self) -> tenant_type_write_dto:
        return tenant_type_write_dto(self.tenant_type_uid, self.tenant_type_name, self.tenant_type_description, self.custom_attributes)
    def to_thin(self) -> tenant_type_thin_dto:
        return tenant_type_thin_dto(self.tenant_type_uid, self.tenant_type_name, self.created_date, self.is_active)
    def touch(self, updated_by: str = "system"):
        self.last_updated_date = datetime.datetime.now()
        self.last_updated_by = updated_by
        self.row_version = self.row_version+1
    def get_list_all_values(self) -> list[any]:
        return [self.tenant_type_uid, self.tenant_type_name, self.tenant_type_description, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]
    def get_list_update_values(self, updated_by: str) -> list[any]:
        return [self.tenant_type_name, self.tenant_type_description, self.custom_attributes, updated_by, self.tenant_type_uid]
    def is_older_than(self, dt: datetime.datetime) -> bool:
        return self.created_date < dt
    def is_newer_than(self, dt: datetime.datetime) -> bool:
        return self.created_date > dt
    def to_json_read(self) -> str:
        return json.dumps(self.to_read_dict())


@dataclass(frozen=False)
class time_approval_read_dto(base_read_dto, time_approval_write_dto):
    time_approval_uid: str
    time_approval_name: str
    tenant_uid: str
    account_uid: str
    time_entry_uid: str
    approval_comment: str
    row_instance: str
    row_lock: str | None
    row_owner: str
    row_seq: int
    row_guid: str
    row_version: int
    is_active: int
    created_date: datetime.datetime
    created_by: str
    last_updated_date: datetime.datetime
    last_updated_by: str
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str
    def __init__(self, time_approval_uid: str, time_approval_name: str, tenant_uid: str, account_uid: str, time_entry_uid: str, approval_comment: str, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
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
    @classmethod
    def empty_read(cls):
        return cls(0, "", "", "", "", "", "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def default_read(cls):
        return cls(0, base_dto.get_random_uid(), "", "", "", "", "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def random_read(cls):
        return cls(0, base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_default(cls, time_approval_uid: str, time_approval_name: str, tenant_uid: str, account_uid: str, time_entry_uid: str, approval_comment: str):
        return cls(0, time_approval_uid, time_approval_name, tenant_uid, account_uid, time_entry_uid, approval_comment, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_full(cls, time_approval_uid: str, time_approval_name: str, tenant_uid: str, account_uid: str, time_entry_uid: str, approval_comment: str, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
        return cls(time_approval_uid, time_approval_name, tenant_uid, account_uid, time_entry_uid, approval_comment, row_instance, row_lock, row_owner, row_seq, row_guid, row_version, is_active, created_date, created_by, last_updated_date, last_updated_by, removed_date, removed_by, custom_attributes)
    @classmethod
    def from_write(cls, dto: time_approval_write_dto):
        return cls(0, dto.time_approval_uid, dto.time_approval_name, dto.tenant_uid, dto.account_uid, dto.time_entry_uid, dto.approval_comment, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, dto.custom_attributes)
    def clone_read(self):
        return time_approval_read_dto(self.time_approval_uid, self.time_approval_name, self.tenant_uid, self.account_uid, self.time_entry_uid, self.approval_comment, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes)
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["time_approval_uid"], d["time_approval_name"], d["tenant_uid"], d["account_uid"], d["time_entry_uid"], d["approval_comment"], d["row_instance"], d["row_lock"], d["row_owner"], d["row_seq"], d["row_guid"], d["row_version"], d["is_active"], d["created_date"], d["created_by"], d["last_updated_date"], d["last_updated_by"], d["removed_date"], d["removed_by"], d["custom_attributes"])
    def to_read_dict(self) -> dict:
        return asdict(self)
    def to_write(self) -> time_approval_write_dto:
        return time_approval_write_dto(self.time_approval_uid, self.time_approval_name, self.tenant_uid, self.account_uid, self.time_entry_uid, self.approval_comment, self.custom_attributes)
    def to_thin(self) -> time_approval_thin_dto:
        return time_approval_thin_dto(self.time_approval_uid, self.time_approval_name, self.created_date, self.is_active)
    def touch(self, updated_by: str = "system"):
        self.last_updated_date = datetime.datetime.now()
        self.last_updated_by = updated_by
        self.row_version = self.row_version+1
    def get_list_all_values(self) -> list[any]:
        return [self.time_approval_uid, self.time_approval_name, self.tenant_uid, self.account_uid, self.time_entry_uid, self.approval_comment, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]
    def get_list_update_values(self, updated_by: str) -> list[any]:
        return [self.time_approval_name, self.tenant_uid, self.account_uid, self.time_entry_uid, self.approval_comment, self.custom_attributes, updated_by, self.time_approval_uid]
    def is_older_than(self, dt: datetime.datetime) -> bool:
        return self.created_date < dt
    def is_newer_than(self, dt: datetime.datetime) -> bool:
        return self.created_date > dt
    def to_json_read(self) -> str:
        return json.dumps(self.to_read_dict())


@dataclass(frozen=False)
class time_entry_read_dto(base_read_dto, time_entry_write_dto):
    time_entry_uid: str
    time_entry_name: str
    time_submit_uid: str
    tenant_uid: str
    account_uid: str
    project_instance_uid: str
    project_milestone_uid: str
    period_uid: str
    invoice_instance_uid: str | None
    entry_period: str
    entry_note: str
    lock_row: str | None
    start_date: datetime.datetime | None
    end_date: datetime.datetime | None
    entry_minutes: int
    is_approved: int
    row_instance: str
    row_lock: str | None
    row_owner: str
    row_seq: int
    row_guid: str
    row_version: int
    is_active: int
    created_date: datetime.datetime
    created_by: str
    last_updated_date: datetime.datetime
    last_updated_by: str
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str
    def __init__(self, time_entry_uid: str, time_entry_name: str, time_submit_uid: str, tenant_uid: str, account_uid: str, project_instance_uid: str, project_milestone_uid: str, period_uid: str, invoice_instance_uid: str | None, entry_period: str, entry_note: str, lock_row: str | None, start_date: datetime.datetime | None, end_date: datetime.datetime | None, entry_minutes: int, is_approved: int, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
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
    @classmethod
    def empty_read(cls):
        return cls(0, "", "", "", "", "", "", "", "", "", "", "", "", datetime.datetime.now(), datetime.datetime.now(), 0, 0, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def default_read(cls):
        return cls(0, base_dto.get_random_uid(), "", "", "", "", "", "", "", "", "", "", "", datetime.datetime.now(), datetime.datetime.now(), 0, 0, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def random_read(cls):
        return cls(0, base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), datetime.datetime.now(), datetime.datetime.now(), 0, 0, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_default(cls, time_entry_uid: str, time_entry_name: str, time_submit_uid: str, tenant_uid: str, account_uid: str, project_instance_uid: str, project_milestone_uid: str, period_uid: str, invoice_instance_uid: str | None, entry_period: str, entry_note: str, lock_row: str | None, start_date: datetime.datetime | None, end_date: datetime.datetime | None, entry_minutes: int, is_approved: int):
        return cls(0, time_entry_uid, time_entry_name, time_submit_uid, tenant_uid, account_uid, project_instance_uid, project_milestone_uid, period_uid, invoice_instance_uid, entry_period, entry_note, lock_row, start_date, end_date, entry_minutes, is_approved, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_full(cls, time_entry_uid: str, time_entry_name: str, time_submit_uid: str, tenant_uid: str, account_uid: str, project_instance_uid: str, project_milestone_uid: str, period_uid: str, invoice_instance_uid: str | None, entry_period: str, entry_note: str, lock_row: str | None, start_date: datetime.datetime | None, end_date: datetime.datetime | None, entry_minutes: int, is_approved: int, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
        return cls(time_entry_uid, time_entry_name, time_submit_uid, tenant_uid, account_uid, project_instance_uid, project_milestone_uid, period_uid, invoice_instance_uid, entry_period, entry_note, lock_row, start_date, end_date, entry_minutes, is_approved, row_instance, row_lock, row_owner, row_seq, row_guid, row_version, is_active, created_date, created_by, last_updated_date, last_updated_by, removed_date, removed_by, custom_attributes)
    @classmethod
    def from_write(cls, dto: time_entry_write_dto):
        return cls(0, dto.time_entry_uid, dto.time_entry_name, dto.time_submit_uid, dto.tenant_uid, dto.account_uid, dto.project_instance_uid, dto.project_milestone_uid, dto.period_uid, dto.invoice_instance_uid, dto.entry_period, dto.entry_note, dto.lock_row, dto.start_date, dto.end_date, dto.entry_minutes, dto.is_approved, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, dto.custom_attributes)
    def clone_read(self):
        return time_entry_read_dto(self.time_entry_uid, self.time_entry_name, self.time_submit_uid, self.tenant_uid, self.account_uid, self.project_instance_uid, self.project_milestone_uid, self.period_uid, self.invoice_instance_uid, self.entry_period, self.entry_note, self.lock_row, self.start_date, self.end_date, self.entry_minutes, self.is_approved, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes)
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["time_entry_uid"], d["time_entry_name"], d["time_submit_uid"], d["tenant_uid"], d["account_uid"], d["project_instance_uid"], d["project_milestone_uid"], d["period_uid"], d["invoice_instance_uid"], d["entry_period"], d["entry_note"], d["lock_row"], d["start_date"], d["end_date"], d["entry_minutes"], d["is_approved"], d["row_instance"], d["row_lock"], d["row_owner"], d["row_seq"], d["row_guid"], d["row_version"], d["is_active"], d["created_date"], d["created_by"], d["last_updated_date"], d["last_updated_by"], d["removed_date"], d["removed_by"], d["custom_attributes"])
    def to_read_dict(self) -> dict:
        return asdict(self)
    def to_write(self) -> time_entry_write_dto:
        return time_entry_write_dto(self.time_entry_uid, self.time_entry_name, self.time_submit_uid, self.tenant_uid, self.account_uid, self.project_instance_uid, self.project_milestone_uid, self.period_uid, self.invoice_instance_uid, self.entry_period, self.entry_note, self.lock_row, self.start_date, self.end_date, self.entry_minutes, self.is_approved, self.custom_attributes)
    def to_thin(self) -> time_entry_thin_dto:
        return time_entry_thin_dto(self.time_entry_uid, self.time_entry_name, self.created_date, self.is_active)
    def touch(self, updated_by: str = "system"):
        self.last_updated_date = datetime.datetime.now()
        self.last_updated_by = updated_by
        self.row_version = self.row_version+1
    def get_list_all_values(self) -> list[any]:
        return [self.time_entry_uid, self.time_entry_name, self.time_submit_uid, self.tenant_uid, self.account_uid, self.project_instance_uid, self.project_milestone_uid, self.period_uid, self.invoice_instance_uid, self.entry_period, self.entry_note, self.lock_row, self.start_date, self.end_date, self.entry_minutes, self.is_approved, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]
    def get_list_update_values(self, updated_by: str) -> list[any]:
        return [self.time_entry_name, self.time_submit_uid, self.tenant_uid, self.account_uid, self.project_instance_uid, self.project_milestone_uid, self.period_uid, self.invoice_instance_uid, self.entry_period, self.entry_note, self.lock_row, self.start_date, self.end_date, self.entry_minutes, self.is_approved, self.custom_attributes, updated_by, self.time_entry_uid]
    def is_older_than(self, dt: datetime.datetime) -> bool:
        return self.created_date < dt
    def is_newer_than(self, dt: datetime.datetime) -> bool:
        return self.created_date > dt
    def to_json_read(self) -> str:
        return json.dumps(self.to_read_dict())


@dataclass(frozen=False)
class time_entry_final_read_dto(base_read_dto, time_entry_final_write_dto):
    time_entry_final_uid: str
    time_entry_final_name: str
    tenant_uid: str
    account_uid: str
    project_instance_uid: str
    project_milestone_uid: str
    invoice_instance_uid: str | None
    entry_period: str
    entry_note: str
    lock_uid: str | None
    start_date: datetime.datetime | None
    end_date: datetime.datetime | None
    entry_minutes: int
    is_approved: int
    row_instance: str
    row_lock: str | None
    row_owner: str
    row_seq: int
    row_guid: str
    row_version: int
    is_active: int
    created_date: datetime.datetime
    created_by: str
    last_updated_date: datetime.datetime
    last_updated_by: str
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str
    def __init__(self, time_entry_final_uid: str, time_entry_final_name: str, tenant_uid: str, account_uid: str, project_instance_uid: str, project_milestone_uid: str, invoice_instance_uid: str | None, entry_period: str, entry_note: str, lock_uid: str | None, start_date: datetime.datetime | None, end_date: datetime.datetime | None, entry_minutes: int, is_approved: int, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
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
    @classmethod
    def empty_read(cls):
        return cls(0, "", "", "", "", "", "", "", "", "", "", datetime.datetime.now(), datetime.datetime.now(), 0, 0, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def default_read(cls):
        return cls(0, base_dto.get_random_uid(), "", "", "", "", "", "", "", "", "", datetime.datetime.now(), datetime.datetime.now(), 0, 0, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def random_read(cls):
        return cls(0, base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), datetime.datetime.now(), datetime.datetime.now(), 0, 0, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_default(cls, time_entry_final_uid: str, time_entry_final_name: str, tenant_uid: str, account_uid: str, project_instance_uid: str, project_milestone_uid: str, invoice_instance_uid: str | None, entry_period: str, entry_note: str, lock_uid: str | None, start_date: datetime.datetime | None, end_date: datetime.datetime | None, entry_minutes: int, is_approved: int):
        return cls(0, time_entry_final_uid, time_entry_final_name, tenant_uid, account_uid, project_instance_uid, project_milestone_uid, invoice_instance_uid, entry_period, entry_note, lock_uid, start_date, end_date, entry_minutes, is_approved, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_full(cls, time_entry_final_uid: str, time_entry_final_name: str, tenant_uid: str, account_uid: str, project_instance_uid: str, project_milestone_uid: str, invoice_instance_uid: str | None, entry_period: str, entry_note: str, lock_uid: str | None, start_date: datetime.datetime | None, end_date: datetime.datetime | None, entry_minutes: int, is_approved: int, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
        return cls(time_entry_final_uid, time_entry_final_name, tenant_uid, account_uid, project_instance_uid, project_milestone_uid, invoice_instance_uid, entry_period, entry_note, lock_uid, start_date, end_date, entry_minutes, is_approved, row_instance, row_lock, row_owner, row_seq, row_guid, row_version, is_active, created_date, created_by, last_updated_date, last_updated_by, removed_date, removed_by, custom_attributes)
    @classmethod
    def from_write(cls, dto: time_entry_final_write_dto):
        return cls(0, dto.time_entry_final_uid, dto.time_entry_final_name, dto.tenant_uid, dto.account_uid, dto.project_instance_uid, dto.project_milestone_uid, dto.invoice_instance_uid, dto.entry_period, dto.entry_note, dto.lock_uid, dto.start_date, dto.end_date, dto.entry_minutes, dto.is_approved, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, dto.custom_attributes)
    def clone_read(self):
        return time_entry_final_read_dto(self.time_entry_final_uid, self.time_entry_final_name, self.tenant_uid, self.account_uid, self.project_instance_uid, self.project_milestone_uid, self.invoice_instance_uid, self.entry_period, self.entry_note, self.lock_uid, self.start_date, self.end_date, self.entry_minutes, self.is_approved, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes)
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["time_entry_final_uid"], d["time_entry_final_name"], d["tenant_uid"], d["account_uid"], d["project_instance_uid"], d["project_milestone_uid"], d["invoice_instance_uid"], d["entry_period"], d["entry_note"], d["lock_uid"], d["start_date"], d["end_date"], d["entry_minutes"], d["is_approved"], d["row_instance"], d["row_lock"], d["row_owner"], d["row_seq"], d["row_guid"], d["row_version"], d["is_active"], d["created_date"], d["created_by"], d["last_updated_date"], d["last_updated_by"], d["removed_date"], d["removed_by"], d["custom_attributes"])
    def to_read_dict(self) -> dict:
        return asdict(self)
    def to_write(self) -> time_entry_final_write_dto:
        return time_entry_final_write_dto(self.time_entry_final_uid, self.time_entry_final_name, self.tenant_uid, self.account_uid, self.project_instance_uid, self.project_milestone_uid, self.invoice_instance_uid, self.entry_period, self.entry_note, self.lock_uid, self.start_date, self.end_date, self.entry_minutes, self.is_approved, self.custom_attributes)
    def to_thin(self) -> time_entry_final_thin_dto:
        return time_entry_final_thin_dto(self.time_entry_final_uid, self.time_entry_final_name, self.created_date, self.is_active)
    def touch(self, updated_by: str = "system"):
        self.last_updated_date = datetime.datetime.now()
        self.last_updated_by = updated_by
        self.row_version = self.row_version+1
    def get_list_all_values(self) -> list[any]:
        return [self.time_entry_final_uid, self.time_entry_final_name, self.tenant_uid, self.account_uid, self.project_instance_uid, self.project_milestone_uid, self.invoice_instance_uid, self.entry_period, self.entry_note, self.lock_uid, self.start_date, self.end_date, self.entry_minutes, self.is_approved, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]
    def get_list_update_values(self, updated_by: str) -> list[any]:
        return [self.time_entry_final_name, self.tenant_uid, self.account_uid, self.project_instance_uid, self.project_milestone_uid, self.invoice_instance_uid, self.entry_period, self.entry_note, self.lock_uid, self.start_date, self.end_date, self.entry_minutes, self.is_approved, self.custom_attributes, updated_by, self.time_entry_final_uid]
    def is_older_than(self, dt: datetime.datetime) -> bool:
        return self.created_date < dt
    def is_newer_than(self, dt: datetime.datetime) -> bool:
        return self.created_date > dt
    def to_json_read(self) -> str:
        return json.dumps(self.to_read_dict())


@dataclass(frozen=False)
class time_entry_invoice_read_dto(base_read_dto, time_entry_invoice_write_dto):
    time_entry_invoice_uid: str
    time_entry_invoice_name: str
    tenant_uid: str
    account_uid: str
    time_submit_uid: str
    time_entry_uid: str
    project_instance_uid: str
    project_milestone_uid: str
    period_uid: str
    invoice_instance_uid: str
    entry_period: str
    entry_note: str
    lock_row: str | None
    start_date: datetime.datetime | None
    end_date: datetime.datetime | None
    entry_minutes: int
    is_approved: int
    row_instance: str
    row_lock: str | None
    row_owner: str
    row_seq: int
    row_guid: str
    row_version: int
    is_active: int
    created_date: datetime.datetime
    created_by: str
    last_updated_date: datetime.datetime
    last_updated_by: str
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str
    def __init__(self, time_entry_invoice_uid: str, time_entry_invoice_name: str, tenant_uid: str, account_uid: str, time_submit_uid: str, time_entry_uid: str, project_instance_uid: str, project_milestone_uid: str, period_uid: str, invoice_instance_uid: str, entry_period: str, entry_note: str, lock_row: str | None, start_date: datetime.datetime | None, end_date: datetime.datetime | None, entry_minutes: int, is_approved: int, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
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
    @classmethod
    def empty_read(cls):
        return cls(0, "", "", "", "", "", "", "", "", "", "", "", "", "", datetime.datetime.now(), datetime.datetime.now(), 0, 0, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def default_read(cls):
        return cls(0, base_dto.get_random_uid(), "", "", "", "", "", "", "", "", "", "", "", "", datetime.datetime.now(), datetime.datetime.now(), 0, 0, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def random_read(cls):
        return cls(0, base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), datetime.datetime.now(), datetime.datetime.now(), 0, 0, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_default(cls, time_entry_invoice_uid: str, time_entry_invoice_name: str, tenant_uid: str, account_uid: str, time_submit_uid: str, time_entry_uid: str, project_instance_uid: str, project_milestone_uid: str, period_uid: str, invoice_instance_uid: str, entry_period: str, entry_note: str, lock_row: str | None, start_date: datetime.datetime | None, end_date: datetime.datetime | None, entry_minutes: int, is_approved: int):
        return cls(0, time_entry_invoice_uid, time_entry_invoice_name, tenant_uid, account_uid, time_submit_uid, time_entry_uid, project_instance_uid, project_milestone_uid, period_uid, invoice_instance_uid, entry_period, entry_note, lock_row, start_date, end_date, entry_minutes, is_approved, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_full(cls, time_entry_invoice_uid: str, time_entry_invoice_name: str, tenant_uid: str, account_uid: str, time_submit_uid: str, time_entry_uid: str, project_instance_uid: str, project_milestone_uid: str, period_uid: str, invoice_instance_uid: str, entry_period: str, entry_note: str, lock_row: str | None, start_date: datetime.datetime | None, end_date: datetime.datetime | None, entry_minutes: int, is_approved: int, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
        return cls(time_entry_invoice_uid, time_entry_invoice_name, tenant_uid, account_uid, time_submit_uid, time_entry_uid, project_instance_uid, project_milestone_uid, period_uid, invoice_instance_uid, entry_period, entry_note, lock_row, start_date, end_date, entry_minutes, is_approved, row_instance, row_lock, row_owner, row_seq, row_guid, row_version, is_active, created_date, created_by, last_updated_date, last_updated_by, removed_date, removed_by, custom_attributes)
    @classmethod
    def from_write(cls, dto: time_entry_invoice_write_dto):
        return cls(0, dto.time_entry_invoice_uid, dto.time_entry_invoice_name, dto.tenant_uid, dto.account_uid, dto.time_submit_uid, dto.time_entry_uid, dto.project_instance_uid, dto.project_milestone_uid, dto.period_uid, dto.invoice_instance_uid, dto.entry_period, dto.entry_note, dto.lock_row, dto.start_date, dto.end_date, dto.entry_minutes, dto.is_approved, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, dto.custom_attributes)
    def clone_read(self):
        return time_entry_invoice_read_dto(self.time_entry_invoice_uid, self.time_entry_invoice_name, self.tenant_uid, self.account_uid, self.time_submit_uid, self.time_entry_uid, self.project_instance_uid, self.project_milestone_uid, self.period_uid, self.invoice_instance_uid, self.entry_period, self.entry_note, self.lock_row, self.start_date, self.end_date, self.entry_minutes, self.is_approved, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes)
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["time_entry_invoice_uid"], d["time_entry_invoice_name"], d["tenant_uid"], d["account_uid"], d["time_submit_uid"], d["time_entry_uid"], d["project_instance_uid"], d["project_milestone_uid"], d["period_uid"], d["invoice_instance_uid"], d["entry_period"], d["entry_note"], d["lock_row"], d["start_date"], d["end_date"], d["entry_minutes"], d["is_approved"], d["row_instance"], d["row_lock"], d["row_owner"], d["row_seq"], d["row_guid"], d["row_version"], d["is_active"], d["created_date"], d["created_by"], d["last_updated_date"], d["last_updated_by"], d["removed_date"], d["removed_by"], d["custom_attributes"])
    def to_read_dict(self) -> dict:
        return asdict(self)
    def to_write(self) -> time_entry_invoice_write_dto:
        return time_entry_invoice_write_dto(self.time_entry_invoice_uid, self.time_entry_invoice_name, self.tenant_uid, self.account_uid, self.time_submit_uid, self.time_entry_uid, self.project_instance_uid, self.project_milestone_uid, self.period_uid, self.invoice_instance_uid, self.entry_period, self.entry_note, self.lock_row, self.start_date, self.end_date, self.entry_minutes, self.is_approved, self.custom_attributes)
    def to_thin(self) -> time_entry_invoice_thin_dto:
        return time_entry_invoice_thin_dto(self.time_entry_invoice_uid, self.time_entry_invoice_name, self.created_date, self.is_active)
    def touch(self, updated_by: str = "system"):
        self.last_updated_date = datetime.datetime.now()
        self.last_updated_by = updated_by
        self.row_version = self.row_version+1
    def get_list_all_values(self) -> list[any]:
        return [self.time_entry_invoice_uid, self.time_entry_invoice_name, self.tenant_uid, self.account_uid, self.time_submit_uid, self.time_entry_uid, self.project_instance_uid, self.project_milestone_uid, self.period_uid, self.invoice_instance_uid, self.entry_period, self.entry_note, self.lock_row, self.start_date, self.end_date, self.entry_minutes, self.is_approved, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]
    def get_list_update_values(self, updated_by: str) -> list[any]:
        return [self.time_entry_invoice_name, self.tenant_uid, self.account_uid, self.time_submit_uid, self.time_entry_uid, self.project_instance_uid, self.project_milestone_uid, self.period_uid, self.invoice_instance_uid, self.entry_period, self.entry_note, self.lock_row, self.start_date, self.end_date, self.entry_minutes, self.is_approved, self.custom_attributes, updated_by, self.time_entry_invoice_uid]
    def is_older_than(self, dt: datetime.datetime) -> bool:
        return self.created_date < dt
    def is_newer_than(self, dt: datetime.datetime) -> bool:
        return self.created_date > dt
    def to_json_read(self) -> str:
        return json.dumps(self.to_read_dict())


@dataclass(frozen=False)
class time_rule_read_dto(base_read_dto, time_rule_write_dto):
    time_rule_uid: str
    time_rule_name: str
    row_instance: str
    row_lock: str | None
    row_owner: str
    row_seq: int
    row_guid: str
    row_version: int
    is_active: int
    created_date: datetime.datetime
    created_by: str
    last_updated_date: datetime.datetime
    last_updated_by: str
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str
    def __init__(self, time_rule_uid: str, time_rule_name: str, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
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
    @classmethod
    def empty_read(cls):
        return cls(0, "", "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def default_read(cls):
        return cls(0, base_dto.get_random_uid(), "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def random_read(cls):
        return cls(0, base_dto.get_random_uid(), base_dto.get_random_uid(), "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_default(cls, time_rule_uid: str, time_rule_name: str):
        return cls(0, time_rule_uid, time_rule_name, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_full(cls, time_rule_uid: str, time_rule_name: str, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
        return cls(time_rule_uid, time_rule_name, row_instance, row_lock, row_owner, row_seq, row_guid, row_version, is_active, created_date, created_by, last_updated_date, last_updated_by, removed_date, removed_by, custom_attributes)
    @classmethod
    def from_write(cls, dto: time_rule_write_dto):
        return cls(0, dto.time_rule_uid, dto.time_rule_name, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, dto.custom_attributes)
    def clone_read(self):
        return time_rule_read_dto(self.time_rule_uid, self.time_rule_name, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes)
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["time_rule_uid"], d["time_rule_name"], d["row_instance"], d["row_lock"], d["row_owner"], d["row_seq"], d["row_guid"], d["row_version"], d["is_active"], d["created_date"], d["created_by"], d["last_updated_date"], d["last_updated_by"], d["removed_date"], d["removed_by"], d["custom_attributes"])
    def to_read_dict(self) -> dict:
        return asdict(self)
    def to_write(self) -> time_rule_write_dto:
        return time_rule_write_dto(self.time_rule_uid, self.time_rule_name, self.custom_attributes)
    def to_thin(self) -> time_rule_thin_dto:
        return time_rule_thin_dto(self.time_rule_uid, self.time_rule_name, self.created_date, self.is_active)
    def touch(self, updated_by: str = "system"):
        self.last_updated_date = datetime.datetime.now()
        self.last_updated_by = updated_by
        self.row_version = self.row_version+1
    def get_list_all_values(self) -> list[any]:
        return [self.time_rule_uid, self.time_rule_name, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]
    def get_list_update_values(self, updated_by: str) -> list[any]:
        return [self.time_rule_name, self.custom_attributes, updated_by, self.time_rule_uid]
    def is_older_than(self, dt: datetime.datetime) -> bool:
        return self.created_date < dt
    def is_newer_than(self, dt: datetime.datetime) -> bool:
        return self.created_date > dt
    def to_json_read(self) -> str:
        return json.dumps(self.to_read_dict())


@dataclass(frozen=False)
class time_rule_client_read_dto(base_read_dto, time_rule_client_write_dto):
    time_rule_client_uid: str
    time_rule_client_name: str
    time_rule_definition: str
    row_instance: str
    row_lock: str | None
    row_owner: str
    row_seq: int
    row_guid: str
    row_version: int
    is_active: int
    created_date: datetime.datetime
    created_by: str
    last_updated_date: datetime.datetime
    last_updated_by: str
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str
    def __init__(self, time_rule_client_uid: str, time_rule_client_name: str, time_rule_definition: str, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
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
    @classmethod
    def empty_read(cls):
        return cls(0, "", "", "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def default_read(cls):
        return cls(0, base_dto.get_random_uid(), "", "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def random_read(cls):
        return cls(0, base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_default(cls, time_rule_client_uid: str, time_rule_client_name: str, time_rule_definition: str):
        return cls(0, time_rule_client_uid, time_rule_client_name, time_rule_definition, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_full(cls, time_rule_client_uid: str, time_rule_client_name: str, time_rule_definition: str, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
        return cls(time_rule_client_uid, time_rule_client_name, time_rule_definition, row_instance, row_lock, row_owner, row_seq, row_guid, row_version, is_active, created_date, created_by, last_updated_date, last_updated_by, removed_date, removed_by, custom_attributes)
    @classmethod
    def from_write(cls, dto: time_rule_client_write_dto):
        return cls(0, dto.time_rule_client_uid, dto.time_rule_client_name, dto.time_rule_definition, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, dto.custom_attributes)
    def clone_read(self):
        return time_rule_client_read_dto(self.time_rule_client_uid, self.time_rule_client_name, self.time_rule_definition, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes)
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["time_rule_client_uid"], d["time_rule_client_name"], d["time_rule_definition"], d["row_instance"], d["row_lock"], d["row_owner"], d["row_seq"], d["row_guid"], d["row_version"], d["is_active"], d["created_date"], d["created_by"], d["last_updated_date"], d["last_updated_by"], d["removed_date"], d["removed_by"], d["custom_attributes"])
    def to_read_dict(self) -> dict:
        return asdict(self)
    def to_write(self) -> time_rule_client_write_dto:
        return time_rule_client_write_dto(self.time_rule_client_uid, self.time_rule_client_name, self.time_rule_definition, self.custom_attributes)
    def to_thin(self) -> time_rule_client_thin_dto:
        return time_rule_client_thin_dto(self.time_rule_client_uid, self.time_rule_client_name, self.created_date, self.is_active)
    def touch(self, updated_by: str = "system"):
        self.last_updated_date = datetime.datetime.now()
        self.last_updated_by = updated_by
        self.row_version = self.row_version+1
    def get_list_all_values(self) -> list[any]:
        return [self.time_rule_client_uid, self.time_rule_client_name, self.time_rule_definition, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]
    def get_list_update_values(self, updated_by: str) -> list[any]:
        return [self.time_rule_client_name, self.time_rule_definition, self.custom_attributes, updated_by, self.time_rule_client_uid]
    def is_older_than(self, dt: datetime.datetime) -> bool:
        return self.created_date < dt
    def is_newer_than(self, dt: datetime.datetime) -> bool:
        return self.created_date > dt
    def to_json_read(self) -> str:
        return json.dumps(self.to_read_dict())


@dataclass(frozen=False)
class time_submit_read_dto(base_read_dto, time_submit_write_dto):
    time_submit_uid: str
    time_submit_name: str
    tenant_uid: str
    account_uid: str
    period_uid: str
    time_submit_description: str
    row_instance: str
    row_lock: str | None
    row_owner: str
    row_seq: int
    row_guid: str
    row_version: int
    is_active: int
    created_date: datetime.datetime
    created_by: str
    last_updated_date: datetime.datetime
    last_updated_by: str
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str
    def __init__(self, time_submit_uid: str, time_submit_name: str, tenant_uid: str, account_uid: str, period_uid: str, time_submit_description: str, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
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
    @classmethod
    def empty_read(cls):
        return cls(0, "", "", "", "", "", "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def default_read(cls):
        return cls(0, base_dto.get_random_uid(), "", "", "", "", "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def random_read(cls):
        return cls(0, base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_default(cls, time_submit_uid: str, time_submit_name: str, tenant_uid: str, account_uid: str, period_uid: str, time_submit_description: str):
        return cls(0, time_submit_uid, time_submit_name, tenant_uid, account_uid, period_uid, time_submit_description, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_full(cls, time_submit_uid: str, time_submit_name: str, tenant_uid: str, account_uid: str, period_uid: str, time_submit_description: str, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
        return cls(time_submit_uid, time_submit_name, tenant_uid, account_uid, period_uid, time_submit_description, row_instance, row_lock, row_owner, row_seq, row_guid, row_version, is_active, created_date, created_by, last_updated_date, last_updated_by, removed_date, removed_by, custom_attributes)
    @classmethod
    def from_write(cls, dto: time_submit_write_dto):
        return cls(0, dto.time_submit_uid, dto.time_submit_name, dto.tenant_uid, dto.account_uid, dto.period_uid, dto.time_submit_description, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, dto.custom_attributes)
    def clone_read(self):
        return time_submit_read_dto(self.time_submit_uid, self.time_submit_name, self.tenant_uid, self.account_uid, self.period_uid, self.time_submit_description, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes)
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["time_submit_uid"], d["time_submit_name"], d["tenant_uid"], d["account_uid"], d["period_uid"], d["time_submit_description"], d["row_instance"], d["row_lock"], d["row_owner"], d["row_seq"], d["row_guid"], d["row_version"], d["is_active"], d["created_date"], d["created_by"], d["last_updated_date"], d["last_updated_by"], d["removed_date"], d["removed_by"], d["custom_attributes"])
    def to_read_dict(self) -> dict:
        return asdict(self)
    def to_write(self) -> time_submit_write_dto:
        return time_submit_write_dto(self.time_submit_uid, self.time_submit_name, self.tenant_uid, self.account_uid, self.period_uid, self.time_submit_description, self.custom_attributes)
    def to_thin(self) -> time_submit_thin_dto:
        return time_submit_thin_dto(self.time_submit_uid, self.time_submit_name, self.created_date, self.is_active)
    def touch(self, updated_by: str = "system"):
        self.last_updated_date = datetime.datetime.now()
        self.last_updated_by = updated_by
        self.row_version = self.row_version+1
    def get_list_all_values(self) -> list[any]:
        return [self.time_submit_uid, self.time_submit_name, self.tenant_uid, self.account_uid, self.period_uid, self.time_submit_description, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]
    def get_list_update_values(self, updated_by: str) -> list[any]:
        return [self.time_submit_name, self.tenant_uid, self.account_uid, self.period_uid, self.time_submit_description, self.custom_attributes, updated_by, self.time_submit_uid]
    def is_older_than(self, dt: datetime.datetime) -> bool:
        return self.created_date < dt
    def is_newer_than(self, dt: datetime.datetime) -> bool:
        return self.created_date > dt
    def to_json_read(self) -> str:
        return json.dumps(self.to_read_dict())


@dataclass(frozen=False)
class time_submit_type_read_dto(base_read_dto, time_submit_type_write_dto):
    time_submit_type_uid: str
    time_submit_type_name: str
    time_submit_type_description: str
    row_instance: str
    row_lock: str | None
    row_owner: str
    row_seq: int
    row_guid: str
    row_version: int
    is_active: int
    created_date: datetime.datetime
    created_by: str
    last_updated_date: datetime.datetime
    last_updated_by: str
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str
    def __init__(self, time_submit_type_uid: str, time_submit_type_name: str, time_submit_type_description: str, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
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
    @classmethod
    def empty_read(cls):
        return cls(0, "", "", "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def default_read(cls):
        return cls(0, base_dto.get_random_uid(), "", "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def random_read(cls):
        return cls(0, base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_default(cls, time_submit_type_uid: str, time_submit_type_name: str, time_submit_type_description: str):
        return cls(0, time_submit_type_uid, time_submit_type_name, time_submit_type_description, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_full(cls, time_submit_type_uid: str, time_submit_type_name: str, time_submit_type_description: str, row_instance: str, row_lock: str | None, row_owner: str, row_seq: int, row_guid: str, row_version: int, is_active: int, created_date: datetime.datetime, created_by: str, last_updated_date: datetime.datetime, last_updated_by: str, removed_date: datetime.datetime | None, removed_by: str | None, custom_attributes: str):
        return cls(time_submit_type_uid, time_submit_type_name, time_submit_type_description, row_instance, row_lock, row_owner, row_seq, row_guid, row_version, is_active, created_date, created_by, last_updated_date, last_updated_by, removed_date, removed_by, custom_attributes)
    @classmethod
    def from_write(cls, dto: time_submit_type_write_dto):
        return cls(0, dto.time_submit_type_uid, dto.time_submit_type_name, dto.time_submit_type_description, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, dto.custom_attributes)
    def clone_read(self):
        return time_submit_type_read_dto(self.time_submit_type_uid, self.time_submit_type_name, self.time_submit_type_description, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes)
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["time_submit_type_uid"], d["time_submit_type_name"], d["time_submit_type_description"], d["row_instance"], d["row_lock"], d["row_owner"], d["row_seq"], d["row_guid"], d["row_version"], d["is_active"], d["created_date"], d["created_by"], d["last_updated_date"], d["last_updated_by"], d["removed_date"], d["removed_by"], d["custom_attributes"])
    def to_read_dict(self) -> dict:
        return asdict(self)
    def to_write(self) -> time_submit_type_write_dto:
        return time_submit_type_write_dto(self.time_submit_type_uid, self.time_submit_type_name, self.time_submit_type_description, self.custom_attributes)
    def to_thin(self) -> time_submit_type_thin_dto:
        return time_submit_type_thin_dto(self.time_submit_type_uid, self.time_submit_type_name, self.created_date, self.is_active)
    def touch(self, updated_by: str = "system"):
        self.last_updated_date = datetime.datetime.now()
        self.last_updated_by = updated_by
        self.row_version = self.row_version+1
    def get_list_all_values(self) -> list[any]:
        return [self.time_submit_type_uid, self.time_submit_type_name, self.time_submit_type_description, self.row_instance, self.row_lock, self.row_owner, self.row_seq, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]
    def get_list_update_values(self, updated_by: str) -> list[any]:
        return [self.time_submit_type_name, self.time_submit_type_description, self.custom_attributes, updated_by, self.time_submit_type_uid]
    def is_older_than(self, dt: datetime.datetime) -> bool:
        return self.created_date < dt
    def is_newer_than(self, dt: datetime.datetime) -> bool:
        return self.created_date > dt
    def to_json_read(self) -> str:
        return json.dumps(self.to_read_dict())


# auto-generated - v_definition_python_dtos_read - END
