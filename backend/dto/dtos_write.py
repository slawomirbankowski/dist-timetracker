# auto-generated - v_definition_python_dtos_write - START at 2024-08-04 09:35:51.351118+00
import datetime
from abc import abstractmethod
from dataclasses import dataclass, asdict
import json
from base.base_objects import objects
from dto.dtos import *
from dto.dtos_models import *


@dataclass(frozen=False)
class account_write_dto(base_write_dto):
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
    def __init__(self, account_uid: str, account_name: str, tenant_uid: str, account_type_uid: str, account_title_uid: str, account_division_uid: str, account_group_uid: str, auth_identity_uid: str, account_email: str, display_name: str, account_address: str, is_verified: int, is_system: int, custom_attributes: str = "{}"):
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
        self.custom_attributes = custom_attributes
    @classmethod
    def empty_write(cls):
        return cls("", "", "", "", "", "", "", "", "", "", "", 0, 0)
    @classmethod
    def default_write(cls):
        return cls(base_dto.get_random_uid(), "", "", "", "", "", "", "", "", "", "", 0, 0)
    @classmethod
    def random_write(cls):
        return cls(base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), 0, 0)
    @classmethod
    def new_write(cls, account_uid: str, account_name: str, tenant_uid: str, account_type_uid: str, account_title_uid: str, account_division_uid: str, account_group_uid: str, auth_identity_uid: str, account_email: str, display_name: str, account_address: str, is_verified: int, is_system: int):
        return cls(account_uid, account_name, tenant_uid, account_type_uid, account_title_uid, account_division_uid, account_group_uid, auth_identity_uid, account_email, display_name, account_address, is_verified, is_system)
    @classmethod
    def new_write_with_defaults(cls, account_uid: str = "", account_name: str = "", tenant_uid: str = "", account_type_uid: str = "", account_title_uid: str = "", account_division_uid: str = "", account_group_uid: str = "", auth_identity_uid: str = "", account_email: str = "", display_name: str = "", account_address: str = "", is_verified: int = 0, is_system: int = 0):
        return cls(account_uid, account_name, tenant_uid, account_type_uid, account_title_uid, account_division_uid, account_group_uid, auth_identity_uid, account_email, display_name, account_address, is_verified, is_system)
    @classmethod
    def new_write_random_uid(cls, account_name: str, tenant_uid: str, account_type_uid: str, account_title_uid: str, account_division_uid: str, account_group_uid: str, auth_identity_uid: str, account_email: str, display_name: str, account_address: str, is_verified: int, is_system: int):
        return cls(base_dto.get_random_uid(), account_name, tenant_uid, account_type_uid, account_title_uid, account_division_uid, account_group_uid, auth_identity_uid, account_email, display_name, account_address, is_verified, is_system)
    @classmethod
    def get_class_model(cls) -> base_model:
        return db_models.account_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["account_uid"], d["account_name"], d["tenant_uid"], d["account_type_uid"], d["account_title_uid"], d["account_division_uid"], d["account_group_uid"], d["auth_identity_uid"], d["account_email"], d["display_name"], d["account_address"], d["is_verified"], d["is_system"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return account_write_dto(self.account_uid, self.account_name, self.tenant_uid, self.account_type_uid, self.account_title_uid, self.account_division_uid, self.account_group_uid, self.auth_identity_uid, self.account_email, self.display_name, self.account_address, self.is_verified, self.is_system, self.custom_attributes)
    def clone_write_new_uid(self):
        return account_write_dto(base_dto.get_random_uid(), self.account_name, self.tenant_uid, self.account_type_uid, self.account_title_uid, self.account_division_uid, self.account_group_uid, self.auth_identity_uid, self.account_email, self.display_name, self.account_address, self.is_verified, self.is_system, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return account_write_dto(uid, self.account_name, self.tenant_uid, self.account_type_uid, self.account_title_uid, self.account_division_uid, self.account_group_uid, self.auth_identity_uid, self.account_email, self.display_name, self.account_address, self.is_verified, self.is_system, self.custom_attributes)
    def get_model(self) -> base_model:
        return db_models.account_model
    def get_uid(self) -> str:
        return self.account_uid
    def get_name(self) -> str:
        return self.account_name
    def get_list_values(self) -> list[any]:
        return [self.account_uid, self.account_name, self.tenant_uid, self.account_type_uid, self.account_title_uid, self.account_division_uid, self.account_group_uid, self.auth_identity_uid, self.account_email, self.display_name, self.account_address, self.is_verified, self.is_system, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.account_uid, self.account_name, self.tenant_uid, self.account_type_uid, self.account_title_uid, self.account_division_uid, self.account_group_uid, self.auth_identity_uid, self.account_email, self.display_name, self.account_address, self.is_verified, self.is_system]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.account_name, self.tenant_uid, self.account_type_uid, self.account_title_uid, self.account_division_uid, self.account_group_uid, self.auth_identity_uid, self.account_email, self.display_name, self.account_address, self.is_verified, self.is_system, self.custom_attributes, updated_by, self.account_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.account_uid, self.account_name, self.tenant_uid, self.account_type_uid, self.account_title_uid, self.account_division_uid, self.account_group_uid, self.auth_identity_uid, self.account_email, self.display_name, self.account_address, self.is_verified, self.is_system, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.account_name, self.tenant_uid, self.account_type_uid, self.account_title_uid, self.account_division_uid, self.account_group_uid, self.auth_identity_uid, self.account_email, self.display_name, self.account_address, self.is_verified, self.is_system]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.account_name, self.tenant_uid, self.account_type_uid, self.account_title_uid, self.account_division_uid, self.account_group_uid, self.auth_identity_uid, self.account_email, self.display_name, self.account_address, self.is_verified, self.is_system, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_uid() == obj.get_uid()
    def update_uid(self, uid: str):
        self.account_uid = uid
    def update_uid_attributes(self, account_uid: str, account_name: str, tenant_uid: str, account_type_uid: str, account_title_uid: str, account_division_uid: str, account_group_uid: str, auth_identity_uid: str, account_email: str, display_name: str, account_address: str, is_verified: int, is_system: int):
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
    def update_attributes(self, account_name: str, tenant_uid: str, account_type_uid: str, account_title_uid: str, account_division_uid: str, account_group_uid: str, auth_identity_uid: str, account_email: str, display_name: str, account_address: str, is_verified: int, is_system: int):
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


@dataclass(frozen=False)
class account_division_write_dto(base_write_dto):
    account_division_uid: str
    account_division_name: str
    tenant_uid: str
    account_uid: str
    account_division_template_uid: str
    division_description: str
    def __init__(self, account_division_uid: str, account_division_name: str, tenant_uid: str, account_uid: str, account_division_template_uid: str, division_description: str, custom_attributes: str = "{}"):
        self.account_division_uid = account_division_uid
        self.account_division_name = account_division_name
        self.tenant_uid = tenant_uid
        self.account_uid = account_uid
        self.account_division_template_uid = account_division_template_uid
        self.division_description = division_description
        self.custom_attributes = custom_attributes
    @classmethod
    def empty_write(cls):
        return cls("", "", "", "", "", "")
    @classmethod
    def default_write(cls):
        return cls(base_dto.get_random_uid(), "", "", "", "", "")
    @classmethod
    def random_write(cls):
        return cls(base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid())
    @classmethod
    def new_write(cls, account_division_uid: str, account_division_name: str, tenant_uid: str, account_uid: str, account_division_template_uid: str, division_description: str):
        return cls(account_division_uid, account_division_name, tenant_uid, account_uid, account_division_template_uid, division_description)
    @classmethod
    def new_write_with_defaults(cls, account_division_uid: str = "", account_division_name: str = "", tenant_uid: str = "", account_uid: str = "", account_division_template_uid: str = "", division_description: str = ""):
        return cls(account_division_uid, account_division_name, tenant_uid, account_uid, account_division_template_uid, division_description)
    @classmethod
    def new_write_random_uid(cls, account_division_name: str, tenant_uid: str, account_uid: str, account_division_template_uid: str, division_description: str):
        return cls(base_dto.get_random_uid(), account_division_name, tenant_uid, account_uid, account_division_template_uid, division_description)
    @classmethod
    def get_class_model(cls) -> base_model:
        return db_models.account_division_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["account_division_uid"], d["account_division_name"], d["tenant_uid"], d["account_uid"], d["account_division_template_uid"], d["division_description"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return account_division_write_dto(self.account_division_uid, self.account_division_name, self.tenant_uid, self.account_uid, self.account_division_template_uid, self.division_description, self.custom_attributes)
    def clone_write_new_uid(self):
        return account_division_write_dto(base_dto.get_random_uid(), self.account_division_name, self.tenant_uid, self.account_uid, self.account_division_template_uid, self.division_description, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return account_division_write_dto(uid, self.account_division_name, self.tenant_uid, self.account_uid, self.account_division_template_uid, self.division_description, self.custom_attributes)
    def get_model(self) -> base_model:
        return db_models.account_division_model
    def get_uid(self) -> str:
        return self.account_division_uid
    def get_name(self) -> str:
        return self.account_division_name
    def get_list_values(self) -> list[any]:
        return [self.account_division_uid, self.account_division_name, self.tenant_uid, self.account_uid, self.account_division_template_uid, self.division_description, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.account_division_uid, self.account_division_name, self.tenant_uid, self.account_uid, self.account_division_template_uid, self.division_description]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.account_division_name, self.tenant_uid, self.account_uid, self.account_division_template_uid, self.division_description, self.custom_attributes, updated_by, self.account_division_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.account_division_uid, self.account_division_name, self.tenant_uid, self.account_uid, self.account_division_template_uid, self.division_description, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.account_division_name, self.tenant_uid, self.account_uid, self.account_division_template_uid, self.division_description]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.account_division_name, self.tenant_uid, self.account_uid, self.account_division_template_uid, self.division_description, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_uid() == obj.get_uid()
    def update_uid(self, uid: str):
        self.account_division_uid = uid
    def update_uid_attributes(self, account_division_uid: str, account_division_name: str, tenant_uid: str, account_uid: str, account_division_template_uid: str, division_description: str):
        self.account_division_uid = account_division_uid
        self.account_division_name = account_division_name
        self.tenant_uid = tenant_uid
        self.account_uid = account_uid
        self.account_division_template_uid = account_division_template_uid
        self.division_description = division_description
    def update_attributes(self, account_division_name: str, tenant_uid: str, account_uid: str, account_division_template_uid: str, division_description: str):
        self.account_division_name = account_division_name
        self.tenant_uid = tenant_uid
        self.account_uid = account_uid
        self.account_division_template_uid = account_division_template_uid
        self.division_description = division_description


@dataclass(frozen=False)
class account_division_template_write_dto(base_write_dto):
    account_division_template_uid: str
    account_division_template_name: str
    division_description: str
    def __init__(self, account_division_template_uid: str, account_division_template_name: str, division_description: str, custom_attributes: str = "{}"):
        self.account_division_template_uid = account_division_template_uid
        self.account_division_template_name = account_division_template_name
        self.division_description = division_description
        self.custom_attributes = custom_attributes
    @classmethod
    def empty_write(cls):
        return cls("", "", "")
    @classmethod
    def default_write(cls):
        return cls(base_dto.get_random_uid(), "", "")
    @classmethod
    def random_write(cls):
        return cls(base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid())
    @classmethod
    def new_write(cls, account_division_template_uid: str, account_division_template_name: str, division_description: str):
        return cls(account_division_template_uid, account_division_template_name, division_description)
    @classmethod
    def new_write_with_defaults(cls, account_division_template_uid: str = "", account_division_template_name: str = "", division_description: str = ""):
        return cls(account_division_template_uid, account_division_template_name, division_description)
    @classmethod
    def new_write_random_uid(cls, account_division_template_name: str, division_description: str):
        return cls(base_dto.get_random_uid(), account_division_template_name, division_description)
    @classmethod
    def get_class_model(cls) -> base_model:
        return db_models.account_division_template_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["account_division_template_uid"], d["account_division_template_name"], d["division_description"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return account_division_template_write_dto(self.account_division_template_uid, self.account_division_template_name, self.division_description, self.custom_attributes)
    def clone_write_new_uid(self):
        return account_division_template_write_dto(base_dto.get_random_uid(), self.account_division_template_name, self.division_description, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return account_division_template_write_dto(uid, self.account_division_template_name, self.division_description, self.custom_attributes)
    def get_model(self) -> base_model:
        return db_models.account_division_template_model
    def get_uid(self) -> str:
        return self.account_division_template_uid
    def get_name(self) -> str:
        return self.account_division_template_name
    def get_list_values(self) -> list[any]:
        return [self.account_division_template_uid, self.account_division_template_name, self.division_description, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.account_division_template_uid, self.account_division_template_name, self.division_description]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.account_division_template_name, self.division_description, self.custom_attributes, updated_by, self.account_division_template_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.account_division_template_uid, self.account_division_template_name, self.division_description, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.account_division_template_name, self.division_description]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.account_division_template_name, self.division_description, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_uid() == obj.get_uid()
    def update_uid(self, uid: str):
        self.account_division_template_uid = uid
    def update_uid_attributes(self, account_division_template_uid: str, account_division_template_name: str, division_description: str):
        self.account_division_template_uid = account_division_template_uid
        self.account_division_template_name = account_division_template_name
        self.division_description = division_description
    def update_attributes(self, account_division_template_name: str, division_description: str):
        self.account_division_template_name = account_division_template_name
        self.division_description = division_description


@dataclass(frozen=False)
class account_group_write_dto(base_write_dto):
    account_group_uid: str
    account_group_name: str
    tenant_uid: str
    account_group_description: str
    def __init__(self, account_group_uid: str, account_group_name: str, tenant_uid: str, account_group_description: str, custom_attributes: str = "{}"):
        self.account_group_uid = account_group_uid
        self.account_group_name = account_group_name
        self.tenant_uid = tenant_uid
        self.account_group_description = account_group_description
        self.custom_attributes = custom_attributes
    @classmethod
    def empty_write(cls):
        return cls("", "", "", "")
    @classmethod
    def default_write(cls):
        return cls(base_dto.get_random_uid(), "", "", "")
    @classmethod
    def random_write(cls):
        return cls(base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid())
    @classmethod
    def new_write(cls, account_group_uid: str, account_group_name: str, tenant_uid: str, account_group_description: str):
        return cls(account_group_uid, account_group_name, tenant_uid, account_group_description)
    @classmethod
    def new_write_with_defaults(cls, account_group_uid: str = "", account_group_name: str = "", tenant_uid: str = "", account_group_description: str = ""):
        return cls(account_group_uid, account_group_name, tenant_uid, account_group_description)
    @classmethod
    def new_write_random_uid(cls, account_group_name: str, tenant_uid: str, account_group_description: str):
        return cls(base_dto.get_random_uid(), account_group_name, tenant_uid, account_group_description)
    @classmethod
    def get_class_model(cls) -> base_model:
        return db_models.account_group_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["account_group_uid"], d["account_group_name"], d["tenant_uid"], d["account_group_description"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return account_group_write_dto(self.account_group_uid, self.account_group_name, self.tenant_uid, self.account_group_description, self.custom_attributes)
    def clone_write_new_uid(self):
        return account_group_write_dto(base_dto.get_random_uid(), self.account_group_name, self.tenant_uid, self.account_group_description, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return account_group_write_dto(uid, self.account_group_name, self.tenant_uid, self.account_group_description, self.custom_attributes)
    def get_model(self) -> base_model:
        return db_models.account_group_model
    def get_uid(self) -> str:
        return self.account_group_uid
    def get_name(self) -> str:
        return self.account_group_name
    def get_list_values(self) -> list[any]:
        return [self.account_group_uid, self.account_group_name, self.tenant_uid, self.account_group_description, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.account_group_uid, self.account_group_name, self.tenant_uid, self.account_group_description]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.account_group_name, self.tenant_uid, self.account_group_description, self.custom_attributes, updated_by, self.account_group_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.account_group_uid, self.account_group_name, self.tenant_uid, self.account_group_description, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.account_group_name, self.tenant_uid, self.account_group_description]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.account_group_name, self.tenant_uid, self.account_group_description, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_uid() == obj.get_uid()
    def update_uid(self, uid: str):
        self.account_group_uid = uid
    def update_uid_attributes(self, account_group_uid: str, account_group_name: str, tenant_uid: str, account_group_description: str):
        self.account_group_uid = account_group_uid
        self.account_group_name = account_group_name
        self.tenant_uid = tenant_uid
        self.account_group_description = account_group_description
    def update_attributes(self, account_group_name: str, tenant_uid: str, account_group_description: str):
        self.account_group_name = account_group_name
        self.tenant_uid = tenant_uid
        self.account_group_description = account_group_description


@dataclass(frozen=False)
class account_group_assignment_write_dto(base_write_dto):
    account_group_assignment_uid: str
    account_group_assignment_name: str
    tenant_uid: str
    account_group_uid: str
    account_uid: str
    account_group_role_uid: str
    start_date: datetime.datetime
    end_date: datetime.datetime
    def __init__(self, account_group_assignment_uid: str, account_group_assignment_name: str, tenant_uid: str, account_group_uid: str, account_uid: str, account_group_role_uid: str, start_date: datetime.datetime, end_date: datetime.datetime, custom_attributes: str = "{}"):
        self.account_group_assignment_uid = account_group_assignment_uid
        self.account_group_assignment_name = account_group_assignment_name
        self.tenant_uid = tenant_uid
        self.account_group_uid = account_group_uid
        self.account_uid = account_uid
        self.account_group_role_uid = account_group_role_uid
        self.start_date = start_date
        self.end_date = end_date
        self.custom_attributes = custom_attributes
    @classmethod
    def empty_write(cls):
        return cls("", "", "", "", "", "", datetime.datetime.now(), datetime.datetime.now())
    @classmethod
    def default_write(cls):
        return cls(base_dto.get_random_uid(), "", "", "", "", "", datetime.datetime.now(), datetime.datetime.now())
    @classmethod
    def random_write(cls):
        return cls(base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), datetime.datetime.now(), datetime.datetime.now())
    @classmethod
    def new_write(cls, account_group_assignment_uid: str, account_group_assignment_name: str, tenant_uid: str, account_group_uid: str, account_uid: str, account_group_role_uid: str, start_date: datetime.datetime, end_date: datetime.datetime):
        return cls(account_group_assignment_uid, account_group_assignment_name, tenant_uid, account_group_uid, account_uid, account_group_role_uid, start_date, end_date)
    @classmethod
    def new_write_with_defaults(cls, account_group_assignment_uid: str = "", account_group_assignment_name: str = "", tenant_uid: str = "", account_group_uid: str = "", account_uid: str = "", account_group_role_uid: str = "", start_date: datetime.datetime = datetime.datetime.now(), end_date: datetime.datetime = datetime.datetime.now()):
        return cls(account_group_assignment_uid, account_group_assignment_name, tenant_uid, account_group_uid, account_uid, account_group_role_uid, start_date, end_date)
    @classmethod
    def new_write_random_uid(cls, account_group_assignment_name: str, tenant_uid: str, account_group_uid: str, account_uid: str, account_group_role_uid: str, start_date: datetime.datetime, end_date: datetime.datetime):
        return cls(base_dto.get_random_uid(), account_group_assignment_name, tenant_uid, account_group_uid, account_uid, account_group_role_uid, start_date, end_date)
    @classmethod
    def get_class_model(cls) -> base_model:
        return db_models.account_group_assignment_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["account_group_assignment_uid"], d["account_group_assignment_name"], d["tenant_uid"], d["account_group_uid"], d["account_uid"], d["account_group_role_uid"], d["start_date"], d["end_date"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return account_group_assignment_write_dto(self.account_group_assignment_uid, self.account_group_assignment_name, self.tenant_uid, self.account_group_uid, self.account_uid, self.account_group_role_uid, self.start_date, self.end_date, self.custom_attributes)
    def clone_write_new_uid(self):
        return account_group_assignment_write_dto(base_dto.get_random_uid(), self.account_group_assignment_name, self.tenant_uid, self.account_group_uid, self.account_uid, self.account_group_role_uid, self.start_date, self.end_date, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return account_group_assignment_write_dto(uid, self.account_group_assignment_name, self.tenant_uid, self.account_group_uid, self.account_uid, self.account_group_role_uid, self.start_date, self.end_date, self.custom_attributes)
    def get_model(self) -> base_model:
        return db_models.account_group_assignment_model
    def get_uid(self) -> str:
        return self.account_group_assignment_uid
    def get_name(self) -> str:
        return self.account_group_assignment_name
    def get_list_values(self) -> list[any]:
        return [self.account_group_assignment_uid, self.account_group_assignment_name, self.tenant_uid, self.account_group_uid, self.account_uid, self.account_group_role_uid, self.start_date, self.end_date, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.account_group_assignment_uid, self.account_group_assignment_name, self.tenant_uid, self.account_group_uid, self.account_uid, self.account_group_role_uid, self.start_date, self.end_date]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.account_group_assignment_name, self.tenant_uid, self.account_group_uid, self.account_uid, self.account_group_role_uid, self.start_date, self.end_date, self.custom_attributes, updated_by, self.account_group_assignment_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.account_group_assignment_uid, self.account_group_assignment_name, self.tenant_uid, self.account_group_uid, self.account_uid, self.account_group_role_uid, self.start_date, self.end_date, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.account_group_assignment_name, self.tenant_uid, self.account_group_uid, self.account_uid, self.account_group_role_uid, self.start_date, self.end_date]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.account_group_assignment_name, self.tenant_uid, self.account_group_uid, self.account_uid, self.account_group_role_uid, self.start_date, self.end_date, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_uid() == obj.get_uid()
    def update_uid(self, uid: str):
        self.account_group_assignment_uid = uid
    def update_uid_attributes(self, account_group_assignment_uid: str, account_group_assignment_name: str, tenant_uid: str, account_group_uid: str, account_uid: str, account_group_role_uid: str, start_date: datetime.datetime, end_date: datetime.datetime):
        self.account_group_assignment_uid = account_group_assignment_uid
        self.account_group_assignment_name = account_group_assignment_name
        self.tenant_uid = tenant_uid
        self.account_group_uid = account_group_uid
        self.account_uid = account_uid
        self.account_group_role_uid = account_group_role_uid
        self.start_date = start_date
        self.end_date = end_date
    def update_attributes(self, account_group_assignment_name: str, tenant_uid: str, account_group_uid: str, account_uid: str, account_group_role_uid: str, start_date: datetime.datetime, end_date: datetime.datetime):
        self.account_group_assignment_name = account_group_assignment_name
        self.tenant_uid = tenant_uid
        self.account_group_uid = account_group_uid
        self.account_uid = account_uid
        self.account_group_role_uid = account_group_role_uid
        self.start_date = start_date
        self.end_date = end_date


@dataclass(frozen=False)
class account_group_role_write_dto(base_write_dto):
    account_group_role_uid: str
    account_group_role_name: str
    def __init__(self, account_group_role_uid: str, account_group_role_name: str, custom_attributes: str = "{}"):
        self.account_group_role_uid = account_group_role_uid
        self.account_group_role_name = account_group_role_name
        self.custom_attributes = custom_attributes
    @classmethod
    def empty_write(cls):
        return cls("", "")
    @classmethod
    def default_write(cls):
        return cls(base_dto.get_random_uid(), "")
    @classmethod
    def random_write(cls):
        return cls(base_dto.get_random_uid(), base_dto.get_random_uid())
    @classmethod
    def new_write(cls, account_group_role_uid: str, account_group_role_name: str):
        return cls(account_group_role_uid, account_group_role_name)
    @classmethod
    def new_write_with_defaults(cls, account_group_role_uid: str = "", account_group_role_name: str = ""):
        return cls(account_group_role_uid, account_group_role_name)
    @classmethod
    def new_write_random_uid(cls, account_group_role_name: str):
        return cls(base_dto.get_random_uid(), account_group_role_name)
    @classmethod
    def get_class_model(cls) -> base_model:
        return db_models.account_group_role_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["account_group_role_uid"], d["account_group_role_name"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return account_group_role_write_dto(self.account_group_role_uid, self.account_group_role_name, self.custom_attributes)
    def clone_write_new_uid(self):
        return account_group_role_write_dto(base_dto.get_random_uid(), self.account_group_role_name, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return account_group_role_write_dto(uid, self.account_group_role_name, self.custom_attributes)
    def get_model(self) -> base_model:
        return db_models.account_group_role_model
    def get_uid(self) -> str:
        return self.account_group_role_uid
    def get_name(self) -> str:
        return self.account_group_role_name
    def get_list_values(self) -> list[any]:
        return [self.account_group_role_uid, self.account_group_role_name, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.account_group_role_uid, self.account_group_role_name]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.account_group_role_name, self.custom_attributes, updated_by, self.account_group_role_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.account_group_role_uid, self.account_group_role_name, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.account_group_role_name]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.account_group_role_name, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_uid() == obj.get_uid()
    def update_uid(self, uid: str):
        self.account_group_role_uid = uid
    def update_uid_attributes(self, account_group_role_uid: str, account_group_role_name: str):
        self.account_group_role_uid = account_group_role_uid
        self.account_group_role_name = account_group_role_name
    def update_attributes(self, account_group_role_name: str):
        self.account_group_role_name = account_group_role_name


@dataclass(frozen=False)
class account_hierarchy_write_dto(base_write_dto):
    account_hierarchy_uid: str
    account_hierarchy_name: str
    tenant_uid: str
    parent_account_uid: str
    child_account_uid: str
    def __init__(self, account_hierarchy_uid: str, account_hierarchy_name: str, tenant_uid: str, parent_account_uid: str, child_account_uid: str, custom_attributes: str = "{}"):
        self.account_hierarchy_uid = account_hierarchy_uid
        self.account_hierarchy_name = account_hierarchy_name
        self.tenant_uid = tenant_uid
        self.parent_account_uid = parent_account_uid
        self.child_account_uid = child_account_uid
        self.custom_attributes = custom_attributes
    @classmethod
    def empty_write(cls):
        return cls("", "", "", "", "")
    @classmethod
    def default_write(cls):
        return cls(base_dto.get_random_uid(), "", "", "", "")
    @classmethod
    def random_write(cls):
        return cls(base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid())
    @classmethod
    def new_write(cls, account_hierarchy_uid: str, account_hierarchy_name: str, tenant_uid: str, parent_account_uid: str, child_account_uid: str):
        return cls(account_hierarchy_uid, account_hierarchy_name, tenant_uid, parent_account_uid, child_account_uid)
    @classmethod
    def new_write_with_defaults(cls, account_hierarchy_uid: str = "", account_hierarchy_name: str = "", tenant_uid: str = "", parent_account_uid: str = "", child_account_uid: str = ""):
        return cls(account_hierarchy_uid, account_hierarchy_name, tenant_uid, parent_account_uid, child_account_uid)
    @classmethod
    def new_write_random_uid(cls, account_hierarchy_name: str, tenant_uid: str, parent_account_uid: str, child_account_uid: str):
        return cls(base_dto.get_random_uid(), account_hierarchy_name, tenant_uid, parent_account_uid, child_account_uid)
    @classmethod
    def get_class_model(cls) -> base_model:
        return db_models.account_hierarchy_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["account_hierarchy_uid"], d["account_hierarchy_name"], d["tenant_uid"], d["parent_account_uid"], d["child_account_uid"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return account_hierarchy_write_dto(self.account_hierarchy_uid, self.account_hierarchy_name, self.tenant_uid, self.parent_account_uid, self.child_account_uid, self.custom_attributes)
    def clone_write_new_uid(self):
        return account_hierarchy_write_dto(base_dto.get_random_uid(), self.account_hierarchy_name, self.tenant_uid, self.parent_account_uid, self.child_account_uid, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return account_hierarchy_write_dto(uid, self.account_hierarchy_name, self.tenant_uid, self.parent_account_uid, self.child_account_uid, self.custom_attributes)
    def get_model(self) -> base_model:
        return db_models.account_hierarchy_model
    def get_uid(self) -> str:
        return self.account_hierarchy_uid
    def get_name(self) -> str:
        return self.account_hierarchy_name
    def get_list_values(self) -> list[any]:
        return [self.account_hierarchy_uid, self.account_hierarchy_name, self.tenant_uid, self.parent_account_uid, self.child_account_uid, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.account_hierarchy_uid, self.account_hierarchy_name, self.tenant_uid, self.parent_account_uid, self.child_account_uid]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.account_hierarchy_name, self.tenant_uid, self.parent_account_uid, self.child_account_uid, self.custom_attributes, updated_by, self.account_hierarchy_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.account_hierarchy_uid, self.account_hierarchy_name, self.tenant_uid, self.parent_account_uid, self.child_account_uid, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.account_hierarchy_name, self.tenant_uid, self.parent_account_uid, self.child_account_uid]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.account_hierarchy_name, self.tenant_uid, self.parent_account_uid, self.child_account_uid, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_uid() == obj.get_uid()
    def update_uid(self, uid: str):
        self.account_hierarchy_uid = uid
    def update_uid_attributes(self, account_hierarchy_uid: str, account_hierarchy_name: str, tenant_uid: str, parent_account_uid: str, child_account_uid: str):
        self.account_hierarchy_uid = account_hierarchy_uid
        self.account_hierarchy_name = account_hierarchy_name
        self.tenant_uid = tenant_uid
        self.parent_account_uid = parent_account_uid
        self.child_account_uid = child_account_uid
    def update_attributes(self, account_hierarchy_name: str, tenant_uid: str, parent_account_uid: str, child_account_uid: str):
        self.account_hierarchy_name = account_hierarchy_name
        self.tenant_uid = tenant_uid
        self.parent_account_uid = parent_account_uid
        self.child_account_uid = child_account_uid


@dataclass(frozen=False)
class account_rate_write_dto(base_write_dto):
    account_rate_uid: str
    account_rate_name: str
    tenant_uid: str
    account_uid: str
    currency_uid: str
    rate: str
    start_date: datetime.datetime
    end_date: datetime.datetime
    rate_note: str
    is_default: str
    def __init__(self, account_rate_uid: str, account_rate_name: str, tenant_uid: str, account_uid: str, currency_uid: str, rate: str, start_date: datetime.datetime, end_date: datetime.datetime, rate_note: str, is_default: str, custom_attributes: str = "{}"):
        self.account_rate_uid = account_rate_uid
        self.account_rate_name = account_rate_name
        self.tenant_uid = tenant_uid
        self.account_uid = account_uid
        self.currency_uid = currency_uid
        self.rate = rate
        self.start_date = start_date
        self.end_date = end_date
        self.rate_note = rate_note
        self.is_default = is_default
        self.custom_attributes = custom_attributes
    @classmethod
    def empty_write(cls):
        return cls("", "", "", "", "", "", datetime.datetime.now(), datetime.datetime.now(), "", "")
    @classmethod
    def default_write(cls):
        return cls(base_dto.get_random_uid(), "", "", "", "", "", datetime.datetime.now(), datetime.datetime.now(), "", "")
    @classmethod
    def random_write(cls):
        return cls(base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), "", datetime.datetime.now(), datetime.datetime.now(), base_dto.get_random_uid(), "")
    @classmethod
    def new_write(cls, account_rate_uid: str, account_rate_name: str, tenant_uid: str, account_uid: str, currency_uid: str, rate: str, start_date: datetime.datetime, end_date: datetime.datetime, rate_note: str, is_default: str):
        return cls(account_rate_uid, account_rate_name, tenant_uid, account_uid, currency_uid, rate, start_date, end_date, rate_note, is_default)
    @classmethod
    def new_write_with_defaults(cls, account_rate_uid: str = "", account_rate_name: str = "", tenant_uid: str = "", account_uid: str = "", currency_uid: str = "", rate: str = "", start_date: datetime.datetime = datetime.datetime.now(), end_date: datetime.datetime = datetime.datetime.now(), rate_note: str = "", is_default: str = ""):
        return cls(account_rate_uid, account_rate_name, tenant_uid, account_uid, currency_uid, rate, start_date, end_date, rate_note, is_default)
    @classmethod
    def new_write_random_uid(cls, account_rate_name: str, tenant_uid: str, account_uid: str, currency_uid: str, rate: str, start_date: datetime.datetime, end_date: datetime.datetime, rate_note: str, is_default: str):
        return cls(base_dto.get_random_uid(), account_rate_name, tenant_uid, account_uid, currency_uid, rate, start_date, end_date, rate_note, is_default)
    @classmethod
    def get_class_model(cls) -> base_model:
        return db_models.account_rate_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["account_rate_uid"], d["account_rate_name"], d["tenant_uid"], d["account_uid"], d["currency_uid"], d["rate"], d["start_date"], d["end_date"], d["rate_note"], d["is_default"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return account_rate_write_dto(self.account_rate_uid, self.account_rate_name, self.tenant_uid, self.account_uid, self.currency_uid, self.rate, self.start_date, self.end_date, self.rate_note, self.is_default, self.custom_attributes)
    def clone_write_new_uid(self):
        return account_rate_write_dto(base_dto.get_random_uid(), self.account_rate_name, self.tenant_uid, self.account_uid, self.currency_uid, self.rate, self.start_date, self.end_date, self.rate_note, self.is_default, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return account_rate_write_dto(uid, self.account_rate_name, self.tenant_uid, self.account_uid, self.currency_uid, self.rate, self.start_date, self.end_date, self.rate_note, self.is_default, self.custom_attributes)
    def get_model(self) -> base_model:
        return db_models.account_rate_model
    def get_uid(self) -> str:
        return self.account_rate_uid
    def get_name(self) -> str:
        return self.account_rate_name
    def get_list_values(self) -> list[any]:
        return [self.account_rate_uid, self.account_rate_name, self.tenant_uid, self.account_uid, self.currency_uid, self.rate, self.start_date, self.end_date, self.rate_note, self.is_default, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.account_rate_uid, self.account_rate_name, self.tenant_uid, self.account_uid, self.currency_uid, self.rate, self.start_date, self.end_date, self.rate_note, self.is_default]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.account_rate_name, self.tenant_uid, self.account_uid, self.currency_uid, self.rate, self.start_date, self.end_date, self.rate_note, self.is_default, self.custom_attributes, updated_by, self.account_rate_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.account_rate_uid, self.account_rate_name, self.tenant_uid, self.account_uid, self.currency_uid, self.rate, self.start_date, self.end_date, self.rate_note, self.is_default, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.account_rate_name, self.tenant_uid, self.account_uid, self.currency_uid, self.rate, self.start_date, self.end_date, self.rate_note, self.is_default]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.account_rate_name, self.tenant_uid, self.account_uid, self.currency_uid, self.rate, self.start_date, self.end_date, self.rate_note, self.is_default, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_uid() == obj.get_uid()
    def update_uid(self, uid: str):
        self.account_rate_uid = uid
    def update_uid_attributes(self, account_rate_uid: str, account_rate_name: str, tenant_uid: str, account_uid: str, currency_uid: str, rate: str, start_date: datetime.datetime, end_date: datetime.datetime, rate_note: str, is_default: str):
        self.account_rate_uid = account_rate_uid
        self.account_rate_name = account_rate_name
        self.tenant_uid = tenant_uid
        self.account_uid = account_uid
        self.currency_uid = currency_uid
        self.rate = rate
        self.start_date = start_date
        self.end_date = end_date
        self.rate_note = rate_note
        self.is_default = is_default
    def update_attributes(self, account_rate_name: str, tenant_uid: str, account_uid: str, currency_uid: str, rate: str, start_date: datetime.datetime, end_date: datetime.datetime, rate_note: str, is_default: str):
        self.account_rate_name = account_rate_name
        self.tenant_uid = tenant_uid
        self.account_uid = account_uid
        self.currency_uid = currency_uid
        self.rate = rate
        self.start_date = start_date
        self.end_date = end_date
        self.rate_note = rate_note
        self.is_default = is_default


@dataclass(frozen=False)
class account_skill_write_dto(base_write_dto):
    account_skill_uid: str
    account_skill_name: str
    account_skill_group_uid: str
    skill_title: str
    skill_code: str
    skill_description: str
    def __init__(self, account_skill_uid: str, account_skill_name: str, account_skill_group_uid: str, skill_title: str, skill_code: str, skill_description: str, custom_attributes: str = "{}"):
        self.account_skill_uid = account_skill_uid
        self.account_skill_name = account_skill_name
        self.account_skill_group_uid = account_skill_group_uid
        self.skill_title = skill_title
        self.skill_code = skill_code
        self.skill_description = skill_description
        self.custom_attributes = custom_attributes
    @classmethod
    def empty_write(cls):
        return cls("", "", "", "", "", "")
    @classmethod
    def default_write(cls):
        return cls(base_dto.get_random_uid(), "", "", "", "", "")
    @classmethod
    def random_write(cls):
        return cls(base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid())
    @classmethod
    def new_write(cls, account_skill_uid: str, account_skill_name: str, account_skill_group_uid: str, skill_title: str, skill_code: str, skill_description: str):
        return cls(account_skill_uid, account_skill_name, account_skill_group_uid, skill_title, skill_code, skill_description)
    @classmethod
    def new_write_with_defaults(cls, account_skill_uid: str = "", account_skill_name: str = "", account_skill_group_uid: str = "", skill_title: str = "", skill_code: str = "", skill_description: str = ""):
        return cls(account_skill_uid, account_skill_name, account_skill_group_uid, skill_title, skill_code, skill_description)
    @classmethod
    def new_write_random_uid(cls, account_skill_name: str, account_skill_group_uid: str, skill_title: str, skill_code: str, skill_description: str):
        return cls(base_dto.get_random_uid(), account_skill_name, account_skill_group_uid, skill_title, skill_code, skill_description)
    @classmethod
    def get_class_model(cls) -> base_model:
        return db_models.account_skill_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["account_skill_uid"], d["account_skill_name"], d["account_skill_group_uid"], d["skill_title"], d["skill_code"], d["skill_description"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return account_skill_write_dto(self.account_skill_uid, self.account_skill_name, self.account_skill_group_uid, self.skill_title, self.skill_code, self.skill_description, self.custom_attributes)
    def clone_write_new_uid(self):
        return account_skill_write_dto(base_dto.get_random_uid(), self.account_skill_name, self.account_skill_group_uid, self.skill_title, self.skill_code, self.skill_description, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return account_skill_write_dto(uid, self.account_skill_name, self.account_skill_group_uid, self.skill_title, self.skill_code, self.skill_description, self.custom_attributes)
    def get_model(self) -> base_model:
        return db_models.account_skill_model
    def get_uid(self) -> str:
        return self.account_skill_uid
    def get_name(self) -> str:
        return self.account_skill_name
    def get_list_values(self) -> list[any]:
        return [self.account_skill_uid, self.account_skill_name, self.account_skill_group_uid, self.skill_title, self.skill_code, self.skill_description, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.account_skill_uid, self.account_skill_name, self.account_skill_group_uid, self.skill_title, self.skill_code, self.skill_description]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.account_skill_name, self.account_skill_group_uid, self.skill_title, self.skill_code, self.skill_description, self.custom_attributes, updated_by, self.account_skill_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.account_skill_uid, self.account_skill_name, self.account_skill_group_uid, self.skill_title, self.skill_code, self.skill_description, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.account_skill_name, self.account_skill_group_uid, self.skill_title, self.skill_code, self.skill_description]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.account_skill_name, self.account_skill_group_uid, self.skill_title, self.skill_code, self.skill_description, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_uid() == obj.get_uid()
    def update_uid(self, uid: str):
        self.account_skill_uid = uid
    def update_uid_attributes(self, account_skill_uid: str, account_skill_name: str, account_skill_group_uid: str, skill_title: str, skill_code: str, skill_description: str):
        self.account_skill_uid = account_skill_uid
        self.account_skill_name = account_skill_name
        self.account_skill_group_uid = account_skill_group_uid
        self.skill_title = skill_title
        self.skill_code = skill_code
        self.skill_description = skill_description
    def update_attributes(self, account_skill_name: str, account_skill_group_uid: str, skill_title: str, skill_code: str, skill_description: str):
        self.account_skill_name = account_skill_name
        self.account_skill_group_uid = account_skill_group_uid
        self.skill_title = skill_title
        self.skill_code = skill_code
        self.skill_description = skill_description


@dataclass(frozen=False)
class account_skill_assignment_write_dto(base_write_dto):
    account_skill_assignment_uid: str
    account_skill_assignment_name: str
    tenant_uid: str
    account_uid: str
    account_skill_uid: str
    skill_rate: str
    account_skill_description: str
    def __init__(self, account_skill_assignment_uid: str, account_skill_assignment_name: str, tenant_uid: str, account_uid: str, account_skill_uid: str, skill_rate: str, account_skill_description: str, custom_attributes: str = "{}"):
        self.account_skill_assignment_uid = account_skill_assignment_uid
        self.account_skill_assignment_name = account_skill_assignment_name
        self.tenant_uid = tenant_uid
        self.account_uid = account_uid
        self.account_skill_uid = account_skill_uid
        self.skill_rate = skill_rate
        self.account_skill_description = account_skill_description
        self.custom_attributes = custom_attributes
    @classmethod
    def empty_write(cls):
        return cls("", "", "", "", "", "", "")
    @classmethod
    def default_write(cls):
        return cls(base_dto.get_random_uid(), "", "", "", "", "", "")
    @classmethod
    def random_write(cls):
        return cls(base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), "", base_dto.get_random_uid())
    @classmethod
    def new_write(cls, account_skill_assignment_uid: str, account_skill_assignment_name: str, tenant_uid: str, account_uid: str, account_skill_uid: str, skill_rate: str, account_skill_description: str):
        return cls(account_skill_assignment_uid, account_skill_assignment_name, tenant_uid, account_uid, account_skill_uid, skill_rate, account_skill_description)
    @classmethod
    def new_write_with_defaults(cls, account_skill_assignment_uid: str = "", account_skill_assignment_name: str = "", tenant_uid: str = "", account_uid: str = "", account_skill_uid: str = "", skill_rate: str = "", account_skill_description: str = ""):
        return cls(account_skill_assignment_uid, account_skill_assignment_name, tenant_uid, account_uid, account_skill_uid, skill_rate, account_skill_description)
    @classmethod
    def new_write_random_uid(cls, account_skill_assignment_name: str, tenant_uid: str, account_uid: str, account_skill_uid: str, skill_rate: str, account_skill_description: str):
        return cls(base_dto.get_random_uid(), account_skill_assignment_name, tenant_uid, account_uid, account_skill_uid, skill_rate, account_skill_description)
    @classmethod
    def get_class_model(cls) -> base_model:
        return db_models.account_skill_assignment_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["account_skill_assignment_uid"], d["account_skill_assignment_name"], d["tenant_uid"], d["account_uid"], d["account_skill_uid"], d["skill_rate"], d["account_skill_description"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return account_skill_assignment_write_dto(self.account_skill_assignment_uid, self.account_skill_assignment_name, self.tenant_uid, self.account_uid, self.account_skill_uid, self.skill_rate, self.account_skill_description, self.custom_attributes)
    def clone_write_new_uid(self):
        return account_skill_assignment_write_dto(base_dto.get_random_uid(), self.account_skill_assignment_name, self.tenant_uid, self.account_uid, self.account_skill_uid, self.skill_rate, self.account_skill_description, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return account_skill_assignment_write_dto(uid, self.account_skill_assignment_name, self.tenant_uid, self.account_uid, self.account_skill_uid, self.skill_rate, self.account_skill_description, self.custom_attributes)
    def get_model(self) -> base_model:
        return db_models.account_skill_assignment_model
    def get_uid(self) -> str:
        return self.account_skill_assignment_uid
    def get_name(self) -> str:
        return self.account_skill_assignment_name
    def get_list_values(self) -> list[any]:
        return [self.account_skill_assignment_uid, self.account_skill_assignment_name, self.tenant_uid, self.account_uid, self.account_skill_uid, self.skill_rate, self.account_skill_description, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.account_skill_assignment_uid, self.account_skill_assignment_name, self.tenant_uid, self.account_uid, self.account_skill_uid, self.skill_rate, self.account_skill_description]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.account_skill_assignment_name, self.tenant_uid, self.account_uid, self.account_skill_uid, self.skill_rate, self.account_skill_description, self.custom_attributes, updated_by, self.account_skill_assignment_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.account_skill_assignment_uid, self.account_skill_assignment_name, self.tenant_uid, self.account_uid, self.account_skill_uid, self.skill_rate, self.account_skill_description, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.account_skill_assignment_name, self.tenant_uid, self.account_uid, self.account_skill_uid, self.skill_rate, self.account_skill_description]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.account_skill_assignment_name, self.tenant_uid, self.account_uid, self.account_skill_uid, self.skill_rate, self.account_skill_description, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_uid() == obj.get_uid()
    def update_uid(self, uid: str):
        self.account_skill_assignment_uid = uid
    def update_uid_attributes(self, account_skill_assignment_uid: str, account_skill_assignment_name: str, tenant_uid: str, account_uid: str, account_skill_uid: str, skill_rate: str, account_skill_description: str):
        self.account_skill_assignment_uid = account_skill_assignment_uid
        self.account_skill_assignment_name = account_skill_assignment_name
        self.tenant_uid = tenant_uid
        self.account_uid = account_uid
        self.account_skill_uid = account_skill_uid
        self.skill_rate = skill_rate
        self.account_skill_description = account_skill_description
    def update_attributes(self, account_skill_assignment_name: str, tenant_uid: str, account_uid: str, account_skill_uid: str, skill_rate: str, account_skill_description: str):
        self.account_skill_assignment_name = account_skill_assignment_name
        self.tenant_uid = tenant_uid
        self.account_uid = account_uid
        self.account_skill_uid = account_skill_uid
        self.skill_rate = skill_rate
        self.account_skill_description = account_skill_description


@dataclass(frozen=False)
class account_skill_group_write_dto(base_write_dto):
    account_skill_group_uid: str
    account_skill_group_name: str
    def __init__(self, account_skill_group_uid: str, account_skill_group_name: str, custom_attributes: str = "{}"):
        self.account_skill_group_uid = account_skill_group_uid
        self.account_skill_group_name = account_skill_group_name
        self.custom_attributes = custom_attributes
    @classmethod
    def empty_write(cls):
        return cls("", "")
    @classmethod
    def default_write(cls):
        return cls(base_dto.get_random_uid(), "")
    @classmethod
    def random_write(cls):
        return cls(base_dto.get_random_uid(), base_dto.get_random_uid())
    @classmethod
    def new_write(cls, account_skill_group_uid: str, account_skill_group_name: str):
        return cls(account_skill_group_uid, account_skill_group_name)
    @classmethod
    def new_write_with_defaults(cls, account_skill_group_uid: str = "", account_skill_group_name: str = ""):
        return cls(account_skill_group_uid, account_skill_group_name)
    @classmethod
    def new_write_random_uid(cls, account_skill_group_name: str):
        return cls(base_dto.get_random_uid(), account_skill_group_name)
    @classmethod
    def get_class_model(cls) -> base_model:
        return db_models.account_skill_group_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["account_skill_group_uid"], d["account_skill_group_name"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return account_skill_group_write_dto(self.account_skill_group_uid, self.account_skill_group_name, self.custom_attributes)
    def clone_write_new_uid(self):
        return account_skill_group_write_dto(base_dto.get_random_uid(), self.account_skill_group_name, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return account_skill_group_write_dto(uid, self.account_skill_group_name, self.custom_attributes)
    def get_model(self) -> base_model:
        return db_models.account_skill_group_model
    def get_uid(self) -> str:
        return self.account_skill_group_uid
    def get_name(self) -> str:
        return self.account_skill_group_name
    def get_list_values(self) -> list[any]:
        return [self.account_skill_group_uid, self.account_skill_group_name, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.account_skill_group_uid, self.account_skill_group_name]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.account_skill_group_name, self.custom_attributes, updated_by, self.account_skill_group_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.account_skill_group_uid, self.account_skill_group_name, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.account_skill_group_name]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.account_skill_group_name, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_uid() == obj.get_uid()
    def update_uid(self, uid: str):
        self.account_skill_group_uid = uid
    def update_uid_attributes(self, account_skill_group_uid: str, account_skill_group_name: str):
        self.account_skill_group_uid = account_skill_group_uid
        self.account_skill_group_name = account_skill_group_name
    def update_attributes(self, account_skill_group_name: str):
        self.account_skill_group_name = account_skill_group_name


@dataclass(frozen=False)
class account_team_write_dto(base_write_dto):
    account_team_uid: str
    account_team_name: str
    tenant_uid: str
    owner_account_uid: str
    is_public: int
    is_tenant: int
    is_private: int
    def __init__(self, account_team_uid: str, account_team_name: str, tenant_uid: str, owner_account_uid: str, is_public: int, is_tenant: int, is_private: int, custom_attributes: str = "{}"):
        self.account_team_uid = account_team_uid
        self.account_team_name = account_team_name
        self.tenant_uid = tenant_uid
        self.owner_account_uid = owner_account_uid
        self.is_public = is_public
        self.is_tenant = is_tenant
        self.is_private = is_private
        self.custom_attributes = custom_attributes
    @classmethod
    def empty_write(cls):
        return cls("", "", "", "", 0, 0, 0)
    @classmethod
    def default_write(cls):
        return cls(base_dto.get_random_uid(), "", "", "", 0, 0, 0)
    @classmethod
    def random_write(cls):
        return cls(base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), 0, 0, 0)
    @classmethod
    def new_write(cls, account_team_uid: str, account_team_name: str, tenant_uid: str, owner_account_uid: str, is_public: int, is_tenant: int, is_private: int):
        return cls(account_team_uid, account_team_name, tenant_uid, owner_account_uid, is_public, is_tenant, is_private)
    @classmethod
    def new_write_with_defaults(cls, account_team_uid: str = "", account_team_name: str = "", tenant_uid: str = "", owner_account_uid: str = "", is_public: int = 0, is_tenant: int = 0, is_private: int = 0):
        return cls(account_team_uid, account_team_name, tenant_uid, owner_account_uid, is_public, is_tenant, is_private)
    @classmethod
    def new_write_random_uid(cls, account_team_name: str, tenant_uid: str, owner_account_uid: str, is_public: int, is_tenant: int, is_private: int):
        return cls(base_dto.get_random_uid(), account_team_name, tenant_uid, owner_account_uid, is_public, is_tenant, is_private)
    @classmethod
    def get_class_model(cls) -> base_model:
        return db_models.account_team_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["account_team_uid"], d["account_team_name"], d["tenant_uid"], d["owner_account_uid"], d["is_public"], d["is_tenant"], d["is_private"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return account_team_write_dto(self.account_team_uid, self.account_team_name, self.tenant_uid, self.owner_account_uid, self.is_public, self.is_tenant, self.is_private, self.custom_attributes)
    def clone_write_new_uid(self):
        return account_team_write_dto(base_dto.get_random_uid(), self.account_team_name, self.tenant_uid, self.owner_account_uid, self.is_public, self.is_tenant, self.is_private, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return account_team_write_dto(uid, self.account_team_name, self.tenant_uid, self.owner_account_uid, self.is_public, self.is_tenant, self.is_private, self.custom_attributes)
    def get_model(self) -> base_model:
        return db_models.account_team_model
    def get_uid(self) -> str:
        return self.account_team_uid
    def get_name(self) -> str:
        return self.account_team_name
    def get_list_values(self) -> list[any]:
        return [self.account_team_uid, self.account_team_name, self.tenant_uid, self.owner_account_uid, self.is_public, self.is_tenant, self.is_private, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.account_team_uid, self.account_team_name, self.tenant_uid, self.owner_account_uid, self.is_public, self.is_tenant, self.is_private]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.account_team_name, self.tenant_uid, self.owner_account_uid, self.is_public, self.is_tenant, self.is_private, self.custom_attributes, updated_by, self.account_team_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.account_team_uid, self.account_team_name, self.tenant_uid, self.owner_account_uid, self.is_public, self.is_tenant, self.is_private, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.account_team_name, self.tenant_uid, self.owner_account_uid, self.is_public, self.is_tenant, self.is_private]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.account_team_name, self.tenant_uid, self.owner_account_uid, self.is_public, self.is_tenant, self.is_private, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_uid() == obj.get_uid()
    def update_uid(self, uid: str):
        self.account_team_uid = uid
    def update_uid_attributes(self, account_team_uid: str, account_team_name: str, tenant_uid: str, owner_account_uid: str, is_public: int, is_tenant: int, is_private: int):
        self.account_team_uid = account_team_uid
        self.account_team_name = account_team_name
        self.tenant_uid = tenant_uid
        self.owner_account_uid = owner_account_uid
        self.is_public = is_public
        self.is_tenant = is_tenant
        self.is_private = is_private
    def update_attributes(self, account_team_name: str, tenant_uid: str, owner_account_uid: str, is_public: int, is_tenant: int, is_private: int):
        self.account_team_name = account_team_name
        self.tenant_uid = tenant_uid
        self.owner_account_uid = owner_account_uid
        self.is_public = is_public
        self.is_tenant = is_tenant
        self.is_private = is_private


@dataclass(frozen=False)
class account_title_write_dto(base_write_dto):
    account_title_uid: str
    account_title_name: str
    title_description: str
    def __init__(self, account_title_uid: str, account_title_name: str, title_description: str, custom_attributes: str = "{}"):
        self.account_title_uid = account_title_uid
        self.account_title_name = account_title_name
        self.title_description = title_description
        self.custom_attributes = custom_attributes
    @classmethod
    def empty_write(cls):
        return cls("", "", "")
    @classmethod
    def default_write(cls):
        return cls(base_dto.get_random_uid(), "", "")
    @classmethod
    def random_write(cls):
        return cls(base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid())
    @classmethod
    def new_write(cls, account_title_uid: str, account_title_name: str, title_description: str):
        return cls(account_title_uid, account_title_name, title_description)
    @classmethod
    def new_write_with_defaults(cls, account_title_uid: str = "", account_title_name: str = "", title_description: str = ""):
        return cls(account_title_uid, account_title_name, title_description)
    @classmethod
    def new_write_random_uid(cls, account_title_name: str, title_description: str):
        return cls(base_dto.get_random_uid(), account_title_name, title_description)
    @classmethod
    def get_class_model(cls) -> base_model:
        return db_models.account_title_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["account_title_uid"], d["account_title_name"], d["title_description"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return account_title_write_dto(self.account_title_uid, self.account_title_name, self.title_description, self.custom_attributes)
    def clone_write_new_uid(self):
        return account_title_write_dto(base_dto.get_random_uid(), self.account_title_name, self.title_description, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return account_title_write_dto(uid, self.account_title_name, self.title_description, self.custom_attributes)
    def get_model(self) -> base_model:
        return db_models.account_title_model
    def get_uid(self) -> str:
        return self.account_title_uid
    def get_name(self) -> str:
        return self.account_title_name
    def get_list_values(self) -> list[any]:
        return [self.account_title_uid, self.account_title_name, self.title_description, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.account_title_uid, self.account_title_name, self.title_description]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.account_title_name, self.title_description, self.custom_attributes, updated_by, self.account_title_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.account_title_uid, self.account_title_name, self.title_description, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.account_title_name, self.title_description]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.account_title_name, self.title_description, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_uid() == obj.get_uid()
    def update_uid(self, uid: str):
        self.account_title_uid = uid
    def update_uid_attributes(self, account_title_uid: str, account_title_name: str, title_description: str):
        self.account_title_uid = account_title_uid
        self.account_title_name = account_title_name
        self.title_description = title_description
    def update_attributes(self, account_title_name: str, title_description: str):
        self.account_title_name = account_title_name
        self.title_description = title_description


@dataclass(frozen=False)
class account_title_assignment_write_dto(base_write_dto):
    account_title_assignment_uid: str
    account_title_assignment_name: str
    tenant_uid: str
    account_title_uid: str
    account_title_responsibility_uid: str
    responsibility_description: str
    responsibility_priority: int
    def __init__(self, account_title_assignment_uid: str, account_title_assignment_name: str, tenant_uid: str, account_title_uid: str, account_title_responsibility_uid: str, responsibility_description: str, responsibility_priority: int, custom_attributes: str = "{}"):
        self.account_title_assignment_uid = account_title_assignment_uid
        self.account_title_assignment_name = account_title_assignment_name
        self.tenant_uid = tenant_uid
        self.account_title_uid = account_title_uid
        self.account_title_responsibility_uid = account_title_responsibility_uid
        self.responsibility_description = responsibility_description
        self.responsibility_priority = responsibility_priority
        self.custom_attributes = custom_attributes
    @classmethod
    def empty_write(cls):
        return cls("", "", "", "", "", "", 0)
    @classmethod
    def default_write(cls):
        return cls(base_dto.get_random_uid(), "", "", "", "", "", 0)
    @classmethod
    def random_write(cls):
        return cls(base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), 0)
    @classmethod
    def new_write(cls, account_title_assignment_uid: str, account_title_assignment_name: str, tenant_uid: str, account_title_uid: str, account_title_responsibility_uid: str, responsibility_description: str, responsibility_priority: int):
        return cls(account_title_assignment_uid, account_title_assignment_name, tenant_uid, account_title_uid, account_title_responsibility_uid, responsibility_description, responsibility_priority)
    @classmethod
    def new_write_with_defaults(cls, account_title_assignment_uid: str = "", account_title_assignment_name: str = "", tenant_uid: str = "", account_title_uid: str = "", account_title_responsibility_uid: str = "", responsibility_description: str = "", responsibility_priority: int = 0):
        return cls(account_title_assignment_uid, account_title_assignment_name, tenant_uid, account_title_uid, account_title_responsibility_uid, responsibility_description, responsibility_priority)
    @classmethod
    def new_write_random_uid(cls, account_title_assignment_name: str, tenant_uid: str, account_title_uid: str, account_title_responsibility_uid: str, responsibility_description: str, responsibility_priority: int):
        return cls(base_dto.get_random_uid(), account_title_assignment_name, tenant_uid, account_title_uid, account_title_responsibility_uid, responsibility_description, responsibility_priority)
    @classmethod
    def get_class_model(cls) -> base_model:
        return db_models.account_title_assignment_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["account_title_assignment_uid"], d["account_title_assignment_name"], d["tenant_uid"], d["account_title_uid"], d["account_title_responsibility_uid"], d["responsibility_description"], d["responsibility_priority"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return account_title_assignment_write_dto(self.account_title_assignment_uid, self.account_title_assignment_name, self.tenant_uid, self.account_title_uid, self.account_title_responsibility_uid, self.responsibility_description, self.responsibility_priority, self.custom_attributes)
    def clone_write_new_uid(self):
        return account_title_assignment_write_dto(base_dto.get_random_uid(), self.account_title_assignment_name, self.tenant_uid, self.account_title_uid, self.account_title_responsibility_uid, self.responsibility_description, self.responsibility_priority, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return account_title_assignment_write_dto(uid, self.account_title_assignment_name, self.tenant_uid, self.account_title_uid, self.account_title_responsibility_uid, self.responsibility_description, self.responsibility_priority, self.custom_attributes)
    def get_model(self) -> base_model:
        return db_models.account_title_assignment_model
    def get_uid(self) -> str:
        return self.account_title_assignment_uid
    def get_name(self) -> str:
        return self.account_title_assignment_name
    def get_list_values(self) -> list[any]:
        return [self.account_title_assignment_uid, self.account_title_assignment_name, self.tenant_uid, self.account_title_uid, self.account_title_responsibility_uid, self.responsibility_description, self.responsibility_priority, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.account_title_assignment_uid, self.account_title_assignment_name, self.tenant_uid, self.account_title_uid, self.account_title_responsibility_uid, self.responsibility_description, self.responsibility_priority]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.account_title_assignment_name, self.tenant_uid, self.account_title_uid, self.account_title_responsibility_uid, self.responsibility_description, self.responsibility_priority, self.custom_attributes, updated_by, self.account_title_assignment_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.account_title_assignment_uid, self.account_title_assignment_name, self.tenant_uid, self.account_title_uid, self.account_title_responsibility_uid, self.responsibility_description, self.responsibility_priority, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.account_title_assignment_name, self.tenant_uid, self.account_title_uid, self.account_title_responsibility_uid, self.responsibility_description, self.responsibility_priority]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.account_title_assignment_name, self.tenant_uid, self.account_title_uid, self.account_title_responsibility_uid, self.responsibility_description, self.responsibility_priority, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_uid() == obj.get_uid()
    def update_uid(self, uid: str):
        self.account_title_assignment_uid = uid
    def update_uid_attributes(self, account_title_assignment_uid: str, account_title_assignment_name: str, tenant_uid: str, account_title_uid: str, account_title_responsibility_uid: str, responsibility_description: str, responsibility_priority: int):
        self.account_title_assignment_uid = account_title_assignment_uid
        self.account_title_assignment_name = account_title_assignment_name
        self.tenant_uid = tenant_uid
        self.account_title_uid = account_title_uid
        self.account_title_responsibility_uid = account_title_responsibility_uid
        self.responsibility_description = responsibility_description
        self.responsibility_priority = responsibility_priority
    def update_attributes(self, account_title_assignment_name: str, tenant_uid: str, account_title_uid: str, account_title_responsibility_uid: str, responsibility_description: str, responsibility_priority: int):
        self.account_title_assignment_name = account_title_assignment_name
        self.tenant_uid = tenant_uid
        self.account_title_uid = account_title_uid
        self.account_title_responsibility_uid = account_title_responsibility_uid
        self.responsibility_description = responsibility_description
        self.responsibility_priority = responsibility_priority


@dataclass(frozen=False)
class account_title_responsibility_write_dto(base_write_dto):
    account_title_responsibility_uid: str
    account_title_responsibility_name: str
    tenant_uid: str
    account_title_uid: str
    responsibility_group: str
    responsibility_description: str
    responsibility_priority: int
    def __init__(self, account_title_responsibility_uid: str, account_title_responsibility_name: str, tenant_uid: str, account_title_uid: str, responsibility_group: str, responsibility_description: str, responsibility_priority: int, custom_attributes: str = "{}"):
        self.account_title_responsibility_uid = account_title_responsibility_uid
        self.account_title_responsibility_name = account_title_responsibility_name
        self.tenant_uid = tenant_uid
        self.account_title_uid = account_title_uid
        self.responsibility_group = responsibility_group
        self.responsibility_description = responsibility_description
        self.responsibility_priority = responsibility_priority
        self.custom_attributes = custom_attributes
    @classmethod
    def empty_write(cls):
        return cls("", "", "", "", "", "", 0)
    @classmethod
    def default_write(cls):
        return cls(base_dto.get_random_uid(), "", "", "", "", "", 0)
    @classmethod
    def random_write(cls):
        return cls(base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), 0)
    @classmethod
    def new_write(cls, account_title_responsibility_uid: str, account_title_responsibility_name: str, tenant_uid: str, account_title_uid: str, responsibility_group: str, responsibility_description: str, responsibility_priority: int):
        return cls(account_title_responsibility_uid, account_title_responsibility_name, tenant_uid, account_title_uid, responsibility_group, responsibility_description, responsibility_priority)
    @classmethod
    def new_write_with_defaults(cls, account_title_responsibility_uid: str = "", account_title_responsibility_name: str = "", tenant_uid: str = "", account_title_uid: str = "", responsibility_group: str = "", responsibility_description: str = "", responsibility_priority: int = 0):
        return cls(account_title_responsibility_uid, account_title_responsibility_name, tenant_uid, account_title_uid, responsibility_group, responsibility_description, responsibility_priority)
    @classmethod
    def new_write_random_uid(cls, account_title_responsibility_name: str, tenant_uid: str, account_title_uid: str, responsibility_group: str, responsibility_description: str, responsibility_priority: int):
        return cls(base_dto.get_random_uid(), account_title_responsibility_name, tenant_uid, account_title_uid, responsibility_group, responsibility_description, responsibility_priority)
    @classmethod
    def get_class_model(cls) -> base_model:
        return db_models.account_title_responsibility_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["account_title_responsibility_uid"], d["account_title_responsibility_name"], d["tenant_uid"], d["account_title_uid"], d["responsibility_group"], d["responsibility_description"], d["responsibility_priority"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return account_title_responsibility_write_dto(self.account_title_responsibility_uid, self.account_title_responsibility_name, self.tenant_uid, self.account_title_uid, self.responsibility_group, self.responsibility_description, self.responsibility_priority, self.custom_attributes)
    def clone_write_new_uid(self):
        return account_title_responsibility_write_dto(base_dto.get_random_uid(), self.account_title_responsibility_name, self.tenant_uid, self.account_title_uid, self.responsibility_group, self.responsibility_description, self.responsibility_priority, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return account_title_responsibility_write_dto(uid, self.account_title_responsibility_name, self.tenant_uid, self.account_title_uid, self.responsibility_group, self.responsibility_description, self.responsibility_priority, self.custom_attributes)
    def get_model(self) -> base_model:
        return db_models.account_title_responsibility_model
    def get_uid(self) -> str:
        return self.account_title_responsibility_uid
    def get_name(self) -> str:
        return self.account_title_responsibility_name
    def get_list_values(self) -> list[any]:
        return [self.account_title_responsibility_uid, self.account_title_responsibility_name, self.tenant_uid, self.account_title_uid, self.responsibility_group, self.responsibility_description, self.responsibility_priority, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.account_title_responsibility_uid, self.account_title_responsibility_name, self.tenant_uid, self.account_title_uid, self.responsibility_group, self.responsibility_description, self.responsibility_priority]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.account_title_responsibility_name, self.tenant_uid, self.account_title_uid, self.responsibility_group, self.responsibility_description, self.responsibility_priority, self.custom_attributes, updated_by, self.account_title_responsibility_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.account_title_responsibility_uid, self.account_title_responsibility_name, self.tenant_uid, self.account_title_uid, self.responsibility_group, self.responsibility_description, self.responsibility_priority, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.account_title_responsibility_name, self.tenant_uid, self.account_title_uid, self.responsibility_group, self.responsibility_description, self.responsibility_priority]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.account_title_responsibility_name, self.tenant_uid, self.account_title_uid, self.responsibility_group, self.responsibility_description, self.responsibility_priority, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_uid() == obj.get_uid()
    def update_uid(self, uid: str):
        self.account_title_responsibility_uid = uid
    def update_uid_attributes(self, account_title_responsibility_uid: str, account_title_responsibility_name: str, tenant_uid: str, account_title_uid: str, responsibility_group: str, responsibility_description: str, responsibility_priority: int):
        self.account_title_responsibility_uid = account_title_responsibility_uid
        self.account_title_responsibility_name = account_title_responsibility_name
        self.tenant_uid = tenant_uid
        self.account_title_uid = account_title_uid
        self.responsibility_group = responsibility_group
        self.responsibility_description = responsibility_description
        self.responsibility_priority = responsibility_priority
    def update_attributes(self, account_title_responsibility_name: str, tenant_uid: str, account_title_uid: str, responsibility_group: str, responsibility_description: str, responsibility_priority: int):
        self.account_title_responsibility_name = account_title_responsibility_name
        self.tenant_uid = tenant_uid
        self.account_title_uid = account_title_uid
        self.responsibility_group = responsibility_group
        self.responsibility_description = responsibility_description
        self.responsibility_priority = responsibility_priority


@dataclass(frozen=False)
class account_type_write_dto(base_write_dto):
    account_type_uid: str
    account_type_name: str
    class_name: str
    account_type_description: str
    def __init__(self, account_type_uid: str, account_type_name: str, class_name: str, account_type_description: str, custom_attributes: str = "{}"):
        self.account_type_uid = account_type_uid
        self.account_type_name = account_type_name
        self.class_name = class_name
        self.account_type_description = account_type_description
        self.custom_attributes = custom_attributes
    @classmethod
    def empty_write(cls):
        return cls("", "", "", "")
    @classmethod
    def default_write(cls):
        return cls(base_dto.get_random_uid(), "", "", "")
    @classmethod
    def random_write(cls):
        return cls(base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid())
    @classmethod
    def new_write(cls, account_type_uid: str, account_type_name: str, class_name: str, account_type_description: str):
        return cls(account_type_uid, account_type_name, class_name, account_type_description)
    @classmethod
    def new_write_with_defaults(cls, account_type_uid: str = "", account_type_name: str = "", class_name: str = "", account_type_description: str = ""):
        return cls(account_type_uid, account_type_name, class_name, account_type_description)
    @classmethod
    def new_write_random_uid(cls, account_type_name: str, class_name: str, account_type_description: str):
        return cls(base_dto.get_random_uid(), account_type_name, class_name, account_type_description)
    @classmethod
    def get_class_model(cls) -> base_model:
        return db_models.account_type_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["account_type_uid"], d["account_type_name"], d["class_name"], d["account_type_description"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return account_type_write_dto(self.account_type_uid, self.account_type_name, self.class_name, self.account_type_description, self.custom_attributes)
    def clone_write_new_uid(self):
        return account_type_write_dto(base_dto.get_random_uid(), self.account_type_name, self.class_name, self.account_type_description, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return account_type_write_dto(uid, self.account_type_name, self.class_name, self.account_type_description, self.custom_attributes)
    def get_model(self) -> base_model:
        return db_models.account_type_model
    def get_uid(self) -> str:
        return self.account_type_uid
    def get_name(self) -> str:
        return self.account_type_name
    def get_list_values(self) -> list[any]:
        return [self.account_type_uid, self.account_type_name, self.class_name, self.account_type_description, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.account_type_uid, self.account_type_name, self.class_name, self.account_type_description]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.account_type_name, self.class_name, self.account_type_description, self.custom_attributes, updated_by, self.account_type_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.account_type_uid, self.account_type_name, self.class_name, self.account_type_description, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.account_type_name, self.class_name, self.account_type_description]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.account_type_name, self.class_name, self.account_type_description, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_uid() == obj.get_uid()
    def update_uid(self, uid: str):
        self.account_type_uid = uid
    def update_uid_attributes(self, account_type_uid: str, account_type_name: str, class_name: str, account_type_description: str):
        self.account_type_uid = account_type_uid
        self.account_type_name = account_type_name
        self.class_name = class_name
        self.account_type_description = account_type_description
    def update_attributes(self, account_type_name: str, class_name: str, account_type_description: str):
        self.account_type_name = account_type_name
        self.class_name = class_name
        self.account_type_description = account_type_description


@dataclass(frozen=False)
class audit_change_write_dto(base_write_dto):
    audit_change_uid: str
    audit_change_name: str
    account_uid: str
    audit_type_uid: str
    change_type: str
    change_json: str
    def __init__(self, audit_change_uid: str, audit_change_name: str, account_uid: str, audit_type_uid: str, change_type: str, change_json: str, custom_attributes: str = "{}"):
        self.audit_change_uid = audit_change_uid
        self.audit_change_name = audit_change_name
        self.account_uid = account_uid
        self.audit_type_uid = audit_type_uid
        self.change_type = change_type
        self.change_json = change_json
        self.custom_attributes = custom_attributes
    @classmethod
    def empty_write(cls):
        return cls("", "", "", "", "", "")
    @classmethod
    def default_write(cls):
        return cls(base_dto.get_random_uid(), "", "", "", "", "")
    @classmethod
    def random_write(cls):
        return cls(base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid())
    @classmethod
    def new_write(cls, audit_change_uid: str, audit_change_name: str, account_uid: str, audit_type_uid: str, change_type: str, change_json: str):
        return cls(audit_change_uid, audit_change_name, account_uid, audit_type_uid, change_type, change_json)
    @classmethod
    def new_write_with_defaults(cls, audit_change_uid: str = "", audit_change_name: str = "", account_uid: str = "", audit_type_uid: str = "", change_type: str = "", change_json: str = ""):
        return cls(audit_change_uid, audit_change_name, account_uid, audit_type_uid, change_type, change_json)
    @classmethod
    def new_write_random_uid(cls, audit_change_name: str, account_uid: str, audit_type_uid: str, change_type: str, change_json: str):
        return cls(base_dto.get_random_uid(), audit_change_name, account_uid, audit_type_uid, change_type, change_json)
    @classmethod
    def get_class_model(cls) -> base_model:
        return db_models.audit_change_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["audit_change_uid"], d["audit_change_name"], d["account_uid"], d["audit_type_uid"], d["change_type"], d["change_json"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return audit_change_write_dto(self.audit_change_uid, self.audit_change_name, self.account_uid, self.audit_type_uid, self.change_type, self.change_json, self.custom_attributes)
    def clone_write_new_uid(self):
        return audit_change_write_dto(base_dto.get_random_uid(), self.audit_change_name, self.account_uid, self.audit_type_uid, self.change_type, self.change_json, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return audit_change_write_dto(uid, self.audit_change_name, self.account_uid, self.audit_type_uid, self.change_type, self.change_json, self.custom_attributes)
    def get_model(self) -> base_model:
        return db_models.audit_change_model
    def get_uid(self) -> str:
        return self.audit_change_uid
    def get_name(self) -> str:
        return self.audit_change_name
    def get_list_values(self) -> list[any]:
        return [self.audit_change_uid, self.audit_change_name, self.account_uid, self.audit_type_uid, self.change_type, self.change_json, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.audit_change_uid, self.audit_change_name, self.account_uid, self.audit_type_uid, self.change_type, self.change_json]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.audit_change_name, self.account_uid, self.audit_type_uid, self.change_type, self.change_json, self.custom_attributes, updated_by, self.audit_change_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.audit_change_uid, self.audit_change_name, self.account_uid, self.audit_type_uid, self.change_type, self.change_json, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.audit_change_name, self.account_uid, self.audit_type_uid, self.change_type, self.change_json]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.audit_change_name, self.account_uid, self.audit_type_uid, self.change_type, self.change_json, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_uid() == obj.get_uid()
    def update_uid(self, uid: str):
        self.audit_change_uid = uid
    def update_uid_attributes(self, audit_change_uid: str, audit_change_name: str, account_uid: str, audit_type_uid: str, change_type: str, change_json: str):
        self.audit_change_uid = audit_change_uid
        self.audit_change_name = audit_change_name
        self.account_uid = account_uid
        self.audit_type_uid = audit_type_uid
        self.change_type = change_type
        self.change_json = change_json
    def update_attributes(self, audit_change_name: str, account_uid: str, audit_type_uid: str, change_type: str, change_json: str):
        self.audit_change_name = audit_change_name
        self.account_uid = account_uid
        self.audit_type_uid = audit_type_uid
        self.change_type = change_type
        self.change_json = change_json


@dataclass(frozen=False)
class audit_type_write_dto(base_write_dto):
    audit_type_uid: str
    audit_type_name: str
    def __init__(self, audit_type_uid: str, audit_type_name: str, custom_attributes: str = "{}"):
        self.audit_type_uid = audit_type_uid
        self.audit_type_name = audit_type_name
        self.custom_attributes = custom_attributes
    @classmethod
    def empty_write(cls):
        return cls("", "")
    @classmethod
    def default_write(cls):
        return cls(base_dto.get_random_uid(), "")
    @classmethod
    def random_write(cls):
        return cls(base_dto.get_random_uid(), base_dto.get_random_uid())
    @classmethod
    def new_write(cls, audit_type_uid: str, audit_type_name: str):
        return cls(audit_type_uid, audit_type_name)
    @classmethod
    def new_write_with_defaults(cls, audit_type_uid: str = "", audit_type_name: str = ""):
        return cls(audit_type_uid, audit_type_name)
    @classmethod
    def new_write_random_uid(cls, audit_type_name: str):
        return cls(base_dto.get_random_uid(), audit_type_name)
    @classmethod
    def get_class_model(cls) -> base_model:
        return db_models.audit_type_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["audit_type_uid"], d["audit_type_name"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return audit_type_write_dto(self.audit_type_uid, self.audit_type_name, self.custom_attributes)
    def clone_write_new_uid(self):
        return audit_type_write_dto(base_dto.get_random_uid(), self.audit_type_name, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return audit_type_write_dto(uid, self.audit_type_name, self.custom_attributes)
    def get_model(self) -> base_model:
        return db_models.audit_type_model
    def get_uid(self) -> str:
        return self.audit_type_uid
    def get_name(self) -> str:
        return self.audit_type_name
    def get_list_values(self) -> list[any]:
        return [self.audit_type_uid, self.audit_type_name, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.audit_type_uid, self.audit_type_name]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.audit_type_name, self.custom_attributes, updated_by, self.audit_type_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.audit_type_uid, self.audit_type_name, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.audit_type_name]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.audit_type_name, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_uid() == obj.get_uid()
    def update_uid(self, uid: str):
        self.audit_type_uid = uid
    def update_uid_attributes(self, audit_type_uid: str, audit_type_name: str):
        self.audit_type_uid = audit_type_uid
        self.audit_type_name = audit_type_name
    def update_attributes(self, audit_type_name: str):
        self.audit_type_name = audit_type_name


@dataclass(frozen=False)
class auth_attempt_write_dto(base_write_dto):
    auth_attempt_uid: str
    auth_attempt_name: str
    tenant_uid: str | None
    account_uid: str | None
    account_login: str
    identity_type: str
    identity_parameters: str
    last_status_name: str
    def __init__(self, auth_attempt_uid: str, auth_attempt_name: str, tenant_uid: str | None, account_uid: str | None, account_login: str, identity_type: str, identity_parameters: str, last_status_name: str, custom_attributes: str = "{}"):
        self.auth_attempt_uid = auth_attempt_uid
        self.auth_attempt_name = auth_attempt_name
        self.tenant_uid = tenant_uid
        self.account_uid = account_uid
        self.account_login = account_login
        self.identity_type = identity_type
        self.identity_parameters = identity_parameters
        self.last_status_name = last_status_name
        self.custom_attributes = custom_attributes
    @classmethod
    def empty_write(cls):
        return cls("", "", "", "", "", "", "", "")
    @classmethod
    def default_write(cls):
        return cls(base_dto.get_random_uid(), "", "", "", "", "", "", "")
    @classmethod
    def random_write(cls):
        return cls(base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid())
    @classmethod
    def new_write(cls, auth_attempt_uid: str, auth_attempt_name: str, tenant_uid: str | None, account_uid: str | None, account_login: str, identity_type: str, identity_parameters: str, last_status_name: str):
        return cls(auth_attempt_uid, auth_attempt_name, tenant_uid, account_uid, account_login, identity_type, identity_parameters, last_status_name)
    @classmethod
    def new_write_with_defaults(cls, auth_attempt_uid: str = "", auth_attempt_name: str = "", tenant_uid: str | None = "", account_uid: str | None = "", account_login: str = "", identity_type: str = "", identity_parameters: str = "", last_status_name: str = ""):
        return cls(auth_attempt_uid, auth_attempt_name, tenant_uid, account_uid, account_login, identity_type, identity_parameters, last_status_name)
    @classmethod
    def new_write_random_uid(cls, auth_attempt_name: str, tenant_uid: str | None, account_uid: str | None, account_login: str, identity_type: str, identity_parameters: str, last_status_name: str):
        return cls(base_dto.get_random_uid(), auth_attempt_name, tenant_uid, account_uid, account_login, identity_type, identity_parameters, last_status_name)
    @classmethod
    def get_class_model(cls) -> base_model:
        return db_models.auth_attempt_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["auth_attempt_uid"], d["auth_attempt_name"], d["tenant_uid"], d["account_uid"], d["account_login"], d["identity_type"], d["identity_parameters"], d["last_status_name"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return auth_attempt_write_dto(self.auth_attempt_uid, self.auth_attempt_name, self.tenant_uid, self.account_uid, self.account_login, self.identity_type, self.identity_parameters, self.last_status_name, self.custom_attributes)
    def clone_write_new_uid(self):
        return auth_attempt_write_dto(base_dto.get_random_uid(), self.auth_attempt_name, self.tenant_uid, self.account_uid, self.account_login, self.identity_type, self.identity_parameters, self.last_status_name, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return auth_attempt_write_dto(uid, self.auth_attempt_name, self.tenant_uid, self.account_uid, self.account_login, self.identity_type, self.identity_parameters, self.last_status_name, self.custom_attributes)
    def get_model(self) -> base_model:
        return db_models.auth_attempt_model
    def get_uid(self) -> str:
        return self.auth_attempt_uid
    def get_name(self) -> str:
        return self.auth_attempt_name
    def get_list_values(self) -> list[any]:
        return [self.auth_attempt_uid, self.auth_attempt_name, self.tenant_uid, self.account_uid, self.account_login, self.identity_type, self.identity_parameters, self.last_status_name, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.auth_attempt_uid, self.auth_attempt_name, self.tenant_uid, self.account_uid, self.account_login, self.identity_type, self.identity_parameters, self.last_status_name]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.auth_attempt_name, self.tenant_uid, self.account_uid, self.account_login, self.identity_type, self.identity_parameters, self.last_status_name, self.custom_attributes, updated_by, self.auth_attempt_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.auth_attempt_uid, self.auth_attempt_name, self.tenant_uid, self.account_uid, self.account_login, self.identity_type, self.identity_parameters, self.last_status_name, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.auth_attempt_name, self.tenant_uid, self.account_uid, self.account_login, self.identity_type, self.identity_parameters, self.last_status_name]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.auth_attempt_name, self.tenant_uid, self.account_uid, self.account_login, self.identity_type, self.identity_parameters, self.last_status_name, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_uid() == obj.get_uid()
    def update_uid(self, uid: str):
        self.auth_attempt_uid = uid
    def update_uid_attributes(self, auth_attempt_uid: str, auth_attempt_name: str, tenant_uid: str | None, account_uid: str | None, account_login: str, identity_type: str, identity_parameters: str, last_status_name: str):
        self.auth_attempt_uid = auth_attempt_uid
        self.auth_attempt_name = auth_attempt_name
        self.tenant_uid = tenant_uid
        self.account_uid = account_uid
        self.account_login = account_login
        self.identity_type = identity_type
        self.identity_parameters = identity_parameters
        self.last_status_name = last_status_name
    def update_attributes(self, auth_attempt_name: str, tenant_uid: str | None, account_uid: str | None, account_login: str, identity_type: str, identity_parameters: str, last_status_name: str):
        self.auth_attempt_name = auth_attempt_name
        self.tenant_uid = tenant_uid
        self.account_uid = account_uid
        self.account_login = account_login
        self.identity_type = identity_type
        self.identity_parameters = identity_parameters
        self.last_status_name = last_status_name


@dataclass(frozen=False)
class auth_identity_write_dto(base_write_dto):
    auth_identity_uid: str
    auth_identity_name: str
    class_name: str
    auth_url: str
    default_parameters_json: str
    def __init__(self, auth_identity_uid: str, auth_identity_name: str, class_name: str, auth_url: str, default_parameters_json: str, custom_attributes: str = "{}"):
        self.auth_identity_uid = auth_identity_uid
        self.auth_identity_name = auth_identity_name
        self.class_name = class_name
        self.auth_url = auth_url
        self.default_parameters_json = default_parameters_json
        self.custom_attributes = custom_attributes
    @classmethod
    def empty_write(cls):
        return cls("", "", "", "", "")
    @classmethod
    def default_write(cls):
        return cls(base_dto.get_random_uid(), "", "", "", "")
    @classmethod
    def random_write(cls):
        return cls(base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid())
    @classmethod
    def new_write(cls, auth_identity_uid: str, auth_identity_name: str, class_name: str, auth_url: str, default_parameters_json: str):
        return cls(auth_identity_uid, auth_identity_name, class_name, auth_url, default_parameters_json)
    @classmethod
    def new_write_with_defaults(cls, auth_identity_uid: str = "", auth_identity_name: str = "", class_name: str = "", auth_url: str = "", default_parameters_json: str = ""):
        return cls(auth_identity_uid, auth_identity_name, class_name, auth_url, default_parameters_json)
    @classmethod
    def new_write_random_uid(cls, auth_identity_name: str, class_name: str, auth_url: str, default_parameters_json: str):
        return cls(base_dto.get_random_uid(), auth_identity_name, class_name, auth_url, default_parameters_json)
    @classmethod
    def get_class_model(cls) -> base_model:
        return db_models.auth_identity_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["auth_identity_uid"], d["auth_identity_name"], d["class_name"], d["auth_url"], d["default_parameters_json"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return auth_identity_write_dto(self.auth_identity_uid, self.auth_identity_name, self.class_name, self.auth_url, self.default_parameters_json, self.custom_attributes)
    def clone_write_new_uid(self):
        return auth_identity_write_dto(base_dto.get_random_uid(), self.auth_identity_name, self.class_name, self.auth_url, self.default_parameters_json, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return auth_identity_write_dto(uid, self.auth_identity_name, self.class_name, self.auth_url, self.default_parameters_json, self.custom_attributes)
    def get_model(self) -> base_model:
        return db_models.auth_identity_model
    def get_uid(self) -> str:
        return self.auth_identity_uid
    def get_name(self) -> str:
        return self.auth_identity_name
    def get_list_values(self) -> list[any]:
        return [self.auth_identity_uid, self.auth_identity_name, self.class_name, self.auth_url, self.default_parameters_json, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.auth_identity_uid, self.auth_identity_name, self.class_name, self.auth_url, self.default_parameters_json]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.auth_identity_name, self.class_name, self.auth_url, self.default_parameters_json, self.custom_attributes, updated_by, self.auth_identity_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.auth_identity_uid, self.auth_identity_name, self.class_name, self.auth_url, self.default_parameters_json, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.auth_identity_name, self.class_name, self.auth_url, self.default_parameters_json]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.auth_identity_name, self.class_name, self.auth_url, self.default_parameters_json, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_uid() == obj.get_uid()
    def update_uid(self, uid: str):
        self.auth_identity_uid = uid
    def update_uid_attributes(self, auth_identity_uid: str, auth_identity_name: str, class_name: str, auth_url: str, default_parameters_json: str):
        self.auth_identity_uid = auth_identity_uid
        self.auth_identity_name = auth_identity_name
        self.class_name = class_name
        self.auth_url = auth_url
        self.default_parameters_json = default_parameters_json
    def update_attributes(self, auth_identity_name: str, class_name: str, auth_url: str, default_parameters_json: str):
        self.auth_identity_name = auth_identity_name
        self.class_name = class_name
        self.auth_url = auth_url
        self.default_parameters_json = default_parameters_json


@dataclass(frozen=False)
class auth_identity_tenant_write_dto(base_write_dto):
    auth_identity_tenant_uid: str
    auth_identity_tenant_name: str
    tenant_uid: str
    auth_identity_uid: str
    auth_sso_uid: str | None
    identity_parameters_json: str
    last_status_name: str
    def __init__(self, auth_identity_tenant_uid: str, auth_identity_tenant_name: str, tenant_uid: str, auth_identity_uid: str, auth_sso_uid: str | None, identity_parameters_json: str, last_status_name: str, custom_attributes: str = "{}"):
        self.auth_identity_tenant_uid = auth_identity_tenant_uid
        self.auth_identity_tenant_name = auth_identity_tenant_name
        self.tenant_uid = tenant_uid
        self.auth_identity_uid = auth_identity_uid
        self.auth_sso_uid = auth_sso_uid
        self.identity_parameters_json = identity_parameters_json
        self.last_status_name = last_status_name
        self.custom_attributes = custom_attributes
    @classmethod
    def empty_write(cls):
        return cls("", "", "", "", "", "", "")
    @classmethod
    def default_write(cls):
        return cls(base_dto.get_random_uid(), "", "", "", "", "", "")
    @classmethod
    def random_write(cls):
        return cls(base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid())
    @classmethod
    def new_write(cls, auth_identity_tenant_uid: str, auth_identity_tenant_name: str, tenant_uid: str, auth_identity_uid: str, auth_sso_uid: str | None, identity_parameters_json: str, last_status_name: str):
        return cls(auth_identity_tenant_uid, auth_identity_tenant_name, tenant_uid, auth_identity_uid, auth_sso_uid, identity_parameters_json, last_status_name)
    @classmethod
    def new_write_with_defaults(cls, auth_identity_tenant_uid: str = "", auth_identity_tenant_name: str = "", tenant_uid: str = "", auth_identity_uid: str = "", auth_sso_uid: str | None = "", identity_parameters_json: str = "", last_status_name: str = ""):
        return cls(auth_identity_tenant_uid, auth_identity_tenant_name, tenant_uid, auth_identity_uid, auth_sso_uid, identity_parameters_json, last_status_name)
    @classmethod
    def new_write_random_uid(cls, auth_identity_tenant_name: str, tenant_uid: str, auth_identity_uid: str, auth_sso_uid: str | None, identity_parameters_json: str, last_status_name: str):
        return cls(base_dto.get_random_uid(), auth_identity_tenant_name, tenant_uid, auth_identity_uid, auth_sso_uid, identity_parameters_json, last_status_name)
    @classmethod
    def get_class_model(cls) -> base_model:
        return db_models.auth_identity_tenant_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["auth_identity_tenant_uid"], d["auth_identity_tenant_name"], d["tenant_uid"], d["auth_identity_uid"], d["auth_sso_uid"], d["identity_parameters_json"], d["last_status_name"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return auth_identity_tenant_write_dto(self.auth_identity_tenant_uid, self.auth_identity_tenant_name, self.tenant_uid, self.auth_identity_uid, self.auth_sso_uid, self.identity_parameters_json, self.last_status_name, self.custom_attributes)
    def clone_write_new_uid(self):
        return auth_identity_tenant_write_dto(base_dto.get_random_uid(), self.auth_identity_tenant_name, self.tenant_uid, self.auth_identity_uid, self.auth_sso_uid, self.identity_parameters_json, self.last_status_name, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return auth_identity_tenant_write_dto(uid, self.auth_identity_tenant_name, self.tenant_uid, self.auth_identity_uid, self.auth_sso_uid, self.identity_parameters_json, self.last_status_name, self.custom_attributes)
    def get_model(self) -> base_model:
        return db_models.auth_identity_tenant_model
    def get_uid(self) -> str:
        return self.auth_identity_tenant_uid
    def get_name(self) -> str:
        return self.auth_identity_tenant_name
    def get_list_values(self) -> list[any]:
        return [self.auth_identity_tenant_uid, self.auth_identity_tenant_name, self.tenant_uid, self.auth_identity_uid, self.auth_sso_uid, self.identity_parameters_json, self.last_status_name, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.auth_identity_tenant_uid, self.auth_identity_tenant_name, self.tenant_uid, self.auth_identity_uid, self.auth_sso_uid, self.identity_parameters_json, self.last_status_name]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.auth_identity_tenant_name, self.tenant_uid, self.auth_identity_uid, self.auth_sso_uid, self.identity_parameters_json, self.last_status_name, self.custom_attributes, updated_by, self.auth_identity_tenant_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.auth_identity_tenant_uid, self.auth_identity_tenant_name, self.tenant_uid, self.auth_identity_uid, self.auth_sso_uid, self.identity_parameters_json, self.last_status_name, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.auth_identity_tenant_name, self.tenant_uid, self.auth_identity_uid, self.auth_sso_uid, self.identity_parameters_json, self.last_status_name]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.auth_identity_tenant_name, self.tenant_uid, self.auth_identity_uid, self.auth_sso_uid, self.identity_parameters_json, self.last_status_name, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_uid() == obj.get_uid()
    def update_uid(self, uid: str):
        self.auth_identity_tenant_uid = uid
    def update_uid_attributes(self, auth_identity_tenant_uid: str, auth_identity_tenant_name: str, tenant_uid: str, auth_identity_uid: str, auth_sso_uid: str | None, identity_parameters_json: str, last_status_name: str):
        self.auth_identity_tenant_uid = auth_identity_tenant_uid
        self.auth_identity_tenant_name = auth_identity_tenant_name
        self.tenant_uid = tenant_uid
        self.auth_identity_uid = auth_identity_uid
        self.auth_sso_uid = auth_sso_uid
        self.identity_parameters_json = identity_parameters_json
        self.last_status_name = last_status_name
    def update_attributes(self, auth_identity_tenant_name: str, tenant_uid: str, auth_identity_uid: str, auth_sso_uid: str | None, identity_parameters_json: str, last_status_name: str):
        self.auth_identity_tenant_name = auth_identity_tenant_name
        self.tenant_uid = tenant_uid
        self.auth_identity_uid = auth_identity_uid
        self.auth_sso_uid = auth_sso_uid
        self.identity_parameters_json = identity_parameters_json
        self.last_status_name = last_status_name


@dataclass(frozen=False)
class auth_key_write_dto(base_write_dto):
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
    def __init__(self, auth_key_uid: str, auth_key_name: str, tenant_uid: str, owner_account_uid: str | None, auth_key_type_uid: str, key_private: str, key_public: str, key_length: int, key_exponent: str, key_modulus: str, key_parameters_json: str, custom_attributes: str = "{}"):
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
        self.custom_attributes = custom_attributes
    @classmethod
    def empty_write(cls):
        return cls("", "", "", "", "", "", "", 0, "", "", "")
    @classmethod
    def default_write(cls):
        return cls(base_dto.get_random_uid(), "", "", "", "", "", "", 0, "", "", "")
    @classmethod
    def random_write(cls):
        return cls(base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), 0, base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid())
    @classmethod
    def new_write(cls, auth_key_uid: str, auth_key_name: str, tenant_uid: str, owner_account_uid: str | None, auth_key_type_uid: str, key_private: str, key_public: str, key_length: int, key_exponent: str, key_modulus: str, key_parameters_json: str):
        return cls(auth_key_uid, auth_key_name, tenant_uid, owner_account_uid, auth_key_type_uid, key_private, key_public, key_length, key_exponent, key_modulus, key_parameters_json)
    @classmethod
    def new_write_with_defaults(cls, auth_key_uid: str = "", auth_key_name: str = "", tenant_uid: str = "", owner_account_uid: str | None = "", auth_key_type_uid: str = "", key_private: str = "", key_public: str = "", key_length: int = 0, key_exponent: str = "", key_modulus: str = "", key_parameters_json: str = ""):
        return cls(auth_key_uid, auth_key_name, tenant_uid, owner_account_uid, auth_key_type_uid, key_private, key_public, key_length, key_exponent, key_modulus, key_parameters_json)
    @classmethod
    def new_write_random_uid(cls, auth_key_name: str, tenant_uid: str, owner_account_uid: str | None, auth_key_type_uid: str, key_private: str, key_public: str, key_length: int, key_exponent: str, key_modulus: str, key_parameters_json: str):
        return cls(base_dto.get_random_uid(), auth_key_name, tenant_uid, owner_account_uid, auth_key_type_uid, key_private, key_public, key_length, key_exponent, key_modulus, key_parameters_json)
    @classmethod
    def get_class_model(cls) -> base_model:
        return db_models.auth_key_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["auth_key_uid"], d["auth_key_name"], d["tenant_uid"], d["owner_account_uid"], d["auth_key_type_uid"], d["key_private"], d["key_public"], d["key_length"], d["key_exponent"], d["key_modulus"], d["key_parameters_json"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return auth_key_write_dto(self.auth_key_uid, self.auth_key_name, self.tenant_uid, self.owner_account_uid, self.auth_key_type_uid, self.key_private, self.key_public, self.key_length, self.key_exponent, self.key_modulus, self.key_parameters_json, self.custom_attributes)
    def clone_write_new_uid(self):
        return auth_key_write_dto(base_dto.get_random_uid(), self.auth_key_name, self.tenant_uid, self.owner_account_uid, self.auth_key_type_uid, self.key_private, self.key_public, self.key_length, self.key_exponent, self.key_modulus, self.key_parameters_json, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return auth_key_write_dto(uid, self.auth_key_name, self.tenant_uid, self.owner_account_uid, self.auth_key_type_uid, self.key_private, self.key_public, self.key_length, self.key_exponent, self.key_modulus, self.key_parameters_json, self.custom_attributes)
    def get_model(self) -> base_model:
        return db_models.auth_key_model
    def get_uid(self) -> str:
        return self.auth_key_uid
    def get_name(self) -> str:
        return self.auth_key_name
    def get_list_values(self) -> list[any]:
        return [self.auth_key_uid, self.auth_key_name, self.tenant_uid, self.owner_account_uid, self.auth_key_type_uid, self.key_private, self.key_public, self.key_length, self.key_exponent, self.key_modulus, self.key_parameters_json, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.auth_key_uid, self.auth_key_name, self.tenant_uid, self.owner_account_uid, self.auth_key_type_uid, self.key_private, self.key_public, self.key_length, self.key_exponent, self.key_modulus, self.key_parameters_json]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.auth_key_name, self.tenant_uid, self.owner_account_uid, self.auth_key_type_uid, self.key_private, self.key_public, self.key_length, self.key_exponent, self.key_modulus, self.key_parameters_json, self.custom_attributes, updated_by, self.auth_key_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.auth_key_uid, self.auth_key_name, self.tenant_uid, self.owner_account_uid, self.auth_key_type_uid, self.key_private, self.key_public, self.key_length, self.key_exponent, self.key_modulus, self.key_parameters_json, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.auth_key_name, self.tenant_uid, self.owner_account_uid, self.auth_key_type_uid, self.key_private, self.key_public, self.key_length, self.key_exponent, self.key_modulus, self.key_parameters_json]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.auth_key_name, self.tenant_uid, self.owner_account_uid, self.auth_key_type_uid, self.key_private, self.key_public, self.key_length, self.key_exponent, self.key_modulus, self.key_parameters_json, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_uid() == obj.get_uid()
    def update_uid(self, uid: str):
        self.auth_key_uid = uid
    def update_uid_attributes(self, auth_key_uid: str, auth_key_name: str, tenant_uid: str, owner_account_uid: str | None, auth_key_type_uid: str, key_private: str, key_public: str, key_length: int, key_exponent: str, key_modulus: str, key_parameters_json: str):
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
    def update_attributes(self, auth_key_name: str, tenant_uid: str, owner_account_uid: str | None, auth_key_type_uid: str, key_private: str, key_public: str, key_length: int, key_exponent: str, key_modulus: str, key_parameters_json: str):
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


@dataclass(frozen=False)
class auth_key_type_write_dto(base_write_dto):
    auth_key_type_uid: str
    auth_key_type_name: str
    class_name: str
    def __init__(self, auth_key_type_uid: str, auth_key_type_name: str, class_name: str, custom_attributes: str = "{}"):
        self.auth_key_type_uid = auth_key_type_uid
        self.auth_key_type_name = auth_key_type_name
        self.class_name = class_name
        self.custom_attributes = custom_attributes
    @classmethod
    def empty_write(cls):
        return cls("", "", "")
    @classmethod
    def default_write(cls):
        return cls(base_dto.get_random_uid(), "", "")
    @classmethod
    def random_write(cls):
        return cls(base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid())
    @classmethod
    def new_write(cls, auth_key_type_uid: str, auth_key_type_name: str, class_name: str):
        return cls(auth_key_type_uid, auth_key_type_name, class_name)
    @classmethod
    def new_write_with_defaults(cls, auth_key_type_uid: str = "", auth_key_type_name: str = "", class_name: str = ""):
        return cls(auth_key_type_uid, auth_key_type_name, class_name)
    @classmethod
    def new_write_random_uid(cls, auth_key_type_name: str, class_name: str):
        return cls(base_dto.get_random_uid(), auth_key_type_name, class_name)
    @classmethod
    def get_class_model(cls) -> base_model:
        return db_models.auth_key_type_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["auth_key_type_uid"], d["auth_key_type_name"], d["class_name"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return auth_key_type_write_dto(self.auth_key_type_uid, self.auth_key_type_name, self.class_name, self.custom_attributes)
    def clone_write_new_uid(self):
        return auth_key_type_write_dto(base_dto.get_random_uid(), self.auth_key_type_name, self.class_name, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return auth_key_type_write_dto(uid, self.auth_key_type_name, self.class_name, self.custom_attributes)
    def get_model(self) -> base_model:
        return db_models.auth_key_type_model
    def get_uid(self) -> str:
        return self.auth_key_type_uid
    def get_name(self) -> str:
        return self.auth_key_type_name
    def get_list_values(self) -> list[any]:
        return [self.auth_key_type_uid, self.auth_key_type_name, self.class_name, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.auth_key_type_uid, self.auth_key_type_name, self.class_name]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.auth_key_type_name, self.class_name, self.custom_attributes, updated_by, self.auth_key_type_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.auth_key_type_uid, self.auth_key_type_name, self.class_name, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.auth_key_type_name, self.class_name]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.auth_key_type_name, self.class_name, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_uid() == obj.get_uid()
    def update_uid(self, uid: str):
        self.auth_key_type_uid = uid
    def update_uid_attributes(self, auth_key_type_uid: str, auth_key_type_name: str, class_name: str):
        self.auth_key_type_uid = auth_key_type_uid
        self.auth_key_type_name = auth_key_type_name
        self.class_name = class_name
    def update_attributes(self, auth_key_type_name: str, class_name: str):
        self.auth_key_type_name = auth_key_type_name
        self.class_name = class_name


@dataclass(frozen=False)
class auth_password_write_dto(base_write_dto):
    auth_password_uid: str
    auth_password_name: str
    tenant_uid: str
    account_uid: str
    password_hash: str
    password_salt: str
    date_from: datetime.datetime
    date_to: datetime.datetime
    usage_count: int
    def __init__(self, auth_password_uid: str, auth_password_name: str, tenant_uid: str, account_uid: str, password_hash: str, password_salt: str, date_from: datetime.datetime, date_to: datetime.datetime, usage_count: int, custom_attributes: str = "{}"):
        self.auth_password_uid = auth_password_uid
        self.auth_password_name = auth_password_name
        self.tenant_uid = tenant_uid
        self.account_uid = account_uid
        self.password_hash = password_hash
        self.password_salt = password_salt
        self.date_from = date_from
        self.date_to = date_to
        self.usage_count = usage_count
        self.custom_attributes = custom_attributes
    @classmethod
    def empty_write(cls):
        return cls("", "", "", "", "", "", datetime.datetime.now(), datetime.datetime.now(), 0)
    @classmethod
    def default_write(cls):
        return cls(base_dto.get_random_uid(), "", "", "", "", "", datetime.datetime.now(), datetime.datetime.now(), 0)
    @classmethod
    def random_write(cls):
        return cls(base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), datetime.datetime.now(), datetime.datetime.now(), 0)
    @classmethod
    def new_write(cls, auth_password_uid: str, auth_password_name: str, tenant_uid: str, account_uid: str, password_hash: str, password_salt: str, date_from: datetime.datetime, date_to: datetime.datetime, usage_count: int):
        return cls(auth_password_uid, auth_password_name, tenant_uid, account_uid, password_hash, password_salt, date_from, date_to, usage_count)
    @classmethod
    def new_write_with_defaults(cls, auth_password_uid: str = "", auth_password_name: str = "", tenant_uid: str = "", account_uid: str = "", password_hash: str = "", password_salt: str = "", date_from: datetime.datetime = datetime.datetime.now(), date_to: datetime.datetime = datetime.datetime.now(), usage_count: int = 0):
        return cls(auth_password_uid, auth_password_name, tenant_uid, account_uid, password_hash, password_salt, date_from, date_to, usage_count)
    @classmethod
    def new_write_random_uid(cls, auth_password_name: str, tenant_uid: str, account_uid: str, password_hash: str, password_salt: str, date_from: datetime.datetime, date_to: datetime.datetime, usage_count: int):
        return cls(base_dto.get_random_uid(), auth_password_name, tenant_uid, account_uid, password_hash, password_salt, date_from, date_to, usage_count)
    @classmethod
    def get_class_model(cls) -> base_model:
        return db_models.auth_password_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["auth_password_uid"], d["auth_password_name"], d["tenant_uid"], d["account_uid"], d["password_hash"], d["password_salt"], d["date_from"], d["date_to"], d["usage_count"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return auth_password_write_dto(self.auth_password_uid, self.auth_password_name, self.tenant_uid, self.account_uid, self.password_hash, self.password_salt, self.date_from, self.date_to, self.usage_count, self.custom_attributes)
    def clone_write_new_uid(self):
        return auth_password_write_dto(base_dto.get_random_uid(), self.auth_password_name, self.tenant_uid, self.account_uid, self.password_hash, self.password_salt, self.date_from, self.date_to, self.usage_count, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return auth_password_write_dto(uid, self.auth_password_name, self.tenant_uid, self.account_uid, self.password_hash, self.password_salt, self.date_from, self.date_to, self.usage_count, self.custom_attributes)
    def get_model(self) -> base_model:
        return db_models.auth_password_model
    def get_uid(self) -> str:
        return self.auth_password_uid
    def get_name(self) -> str:
        return self.auth_password_name
    def get_list_values(self) -> list[any]:
        return [self.auth_password_uid, self.auth_password_name, self.tenant_uid, self.account_uid, self.password_hash, self.password_salt, self.date_from, self.date_to, self.usage_count, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.auth_password_uid, self.auth_password_name, self.tenant_uid, self.account_uid, self.password_hash, self.password_salt, self.date_from, self.date_to, self.usage_count]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.auth_password_name, self.tenant_uid, self.account_uid, self.password_hash, self.password_salt, self.date_from, self.date_to, self.usage_count, self.custom_attributes, updated_by, self.auth_password_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.auth_password_uid, self.auth_password_name, self.tenant_uid, self.account_uid, self.password_hash, self.password_salt, self.date_from, self.date_to, self.usage_count, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.auth_password_name, self.tenant_uid, self.account_uid, self.password_hash, self.password_salt, self.date_from, self.date_to, self.usage_count]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.auth_password_name, self.tenant_uid, self.account_uid, self.password_hash, self.password_salt, self.date_from, self.date_to, self.usage_count, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_uid() == obj.get_uid()
    def update_uid(self, uid: str):
        self.auth_password_uid = uid
    def update_uid_attributes(self, auth_password_uid: str, auth_password_name: str, tenant_uid: str, account_uid: str, password_hash: str, password_salt: str, date_from: datetime.datetime, date_to: datetime.datetime, usage_count: int):
        self.auth_password_uid = auth_password_uid
        self.auth_password_name = auth_password_name
        self.tenant_uid = tenant_uid
        self.account_uid = account_uid
        self.password_hash = password_hash
        self.password_salt = password_salt
        self.date_from = date_from
        self.date_to = date_to
        self.usage_count = usage_count
    def update_attributes(self, auth_password_name: str, tenant_uid: str, account_uid: str, password_hash: str, password_salt: str, date_from: datetime.datetime, date_to: datetime.datetime, usage_count: int):
        self.auth_password_name = auth_password_name
        self.tenant_uid = tenant_uid
        self.account_uid = account_uid
        self.password_hash = password_hash
        self.password_salt = password_salt
        self.date_from = date_from
        self.date_to = date_to
        self.usage_count = usage_count


@dataclass(frozen=False)
class auth_password_current_write_dto(base_write_dto):
    auth_password_current_uid: str
    auth_password_current_name: str
    tenant_uid: str
    account_uid: str
    password_hash: str
    password_salt: str
    date_from: datetime.datetime
    date_to: datetime.datetime
    usage_count: int
    def __init__(self, auth_password_current_uid: str, auth_password_current_name: str, tenant_uid: str, account_uid: str, password_hash: str, password_salt: str, date_from: datetime.datetime, date_to: datetime.datetime, usage_count: int, custom_attributes: str = "{}"):
        self.auth_password_current_uid = auth_password_current_uid
        self.auth_password_current_name = auth_password_current_name
        self.tenant_uid = tenant_uid
        self.account_uid = account_uid
        self.password_hash = password_hash
        self.password_salt = password_salt
        self.date_from = date_from
        self.date_to = date_to
        self.usage_count = usage_count
        self.custom_attributes = custom_attributes
    @classmethod
    def empty_write(cls):
        return cls("", "", "", "", "", "", datetime.datetime.now(), datetime.datetime.now(), 0)
    @classmethod
    def default_write(cls):
        return cls(base_dto.get_random_uid(), "", "", "", "", "", datetime.datetime.now(), datetime.datetime.now(), 0)
    @classmethod
    def random_write(cls):
        return cls(base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), datetime.datetime.now(), datetime.datetime.now(), 0)
    @classmethod
    def new_write(cls, auth_password_current_uid: str, auth_password_current_name: str, tenant_uid: str, account_uid: str, password_hash: str, password_salt: str, date_from: datetime.datetime, date_to: datetime.datetime, usage_count: int):
        return cls(auth_password_current_uid, auth_password_current_name, tenant_uid, account_uid, password_hash, password_salt, date_from, date_to, usage_count)
    @classmethod
    def new_write_with_defaults(cls, auth_password_current_uid: str = "", auth_password_current_name: str = "", tenant_uid: str = "", account_uid: str = "", password_hash: str = "", password_salt: str = "", date_from: datetime.datetime = datetime.datetime.now(), date_to: datetime.datetime = datetime.datetime.now(), usage_count: int = 0):
        return cls(auth_password_current_uid, auth_password_current_name, tenant_uid, account_uid, password_hash, password_salt, date_from, date_to, usage_count)
    @classmethod
    def new_write_random_uid(cls, auth_password_current_name: str, tenant_uid: str, account_uid: str, password_hash: str, password_salt: str, date_from: datetime.datetime, date_to: datetime.datetime, usage_count: int):
        return cls(base_dto.get_random_uid(), auth_password_current_name, tenant_uid, account_uid, password_hash, password_salt, date_from, date_to, usage_count)
    @classmethod
    def get_class_model(cls) -> base_model:
        return db_models.auth_password_current_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["auth_password_current_uid"], d["auth_password_current_name"], d["tenant_uid"], d["account_uid"], d["password_hash"], d["password_salt"], d["date_from"], d["date_to"], d["usage_count"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return auth_password_current_write_dto(self.auth_password_current_uid, self.auth_password_current_name, self.tenant_uid, self.account_uid, self.password_hash, self.password_salt, self.date_from, self.date_to, self.usage_count, self.custom_attributes)
    def clone_write_new_uid(self):
        return auth_password_current_write_dto(base_dto.get_random_uid(), self.auth_password_current_name, self.tenant_uid, self.account_uid, self.password_hash, self.password_salt, self.date_from, self.date_to, self.usage_count, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return auth_password_current_write_dto(uid, self.auth_password_current_name, self.tenant_uid, self.account_uid, self.password_hash, self.password_salt, self.date_from, self.date_to, self.usage_count, self.custom_attributes)
    def get_model(self) -> base_model:
        return db_models.auth_password_current_model
    def get_uid(self) -> str:
        return self.auth_password_current_uid
    def get_name(self) -> str:
        return self.auth_password_current_name
    def get_list_values(self) -> list[any]:
        return [self.auth_password_current_uid, self.auth_password_current_name, self.tenant_uid, self.account_uid, self.password_hash, self.password_salt, self.date_from, self.date_to, self.usage_count, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.auth_password_current_uid, self.auth_password_current_name, self.tenant_uid, self.account_uid, self.password_hash, self.password_salt, self.date_from, self.date_to, self.usage_count]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.auth_password_current_name, self.tenant_uid, self.account_uid, self.password_hash, self.password_salt, self.date_from, self.date_to, self.usage_count, self.custom_attributes, updated_by, self.auth_password_current_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.auth_password_current_uid, self.auth_password_current_name, self.tenant_uid, self.account_uid, self.password_hash, self.password_salt, self.date_from, self.date_to, self.usage_count, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.auth_password_current_name, self.tenant_uid, self.account_uid, self.password_hash, self.password_salt, self.date_from, self.date_to, self.usage_count]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.auth_password_current_name, self.tenant_uid, self.account_uid, self.password_hash, self.password_salt, self.date_from, self.date_to, self.usage_count, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_uid() == obj.get_uid()
    def update_uid(self, uid: str):
        self.auth_password_current_uid = uid
    def update_uid_attributes(self, auth_password_current_uid: str, auth_password_current_name: str, tenant_uid: str, account_uid: str, password_hash: str, password_salt: str, date_from: datetime.datetime, date_to: datetime.datetime, usage_count: int):
        self.auth_password_current_uid = auth_password_current_uid
        self.auth_password_current_name = auth_password_current_name
        self.tenant_uid = tenant_uid
        self.account_uid = account_uid
        self.password_hash = password_hash
        self.password_salt = password_salt
        self.date_from = date_from
        self.date_to = date_to
        self.usage_count = usage_count
    def update_attributes(self, auth_password_current_name: str, tenant_uid: str, account_uid: str, password_hash: str, password_salt: str, date_from: datetime.datetime, date_to: datetime.datetime, usage_count: int):
        self.auth_password_current_name = auth_password_current_name
        self.tenant_uid = tenant_uid
        self.account_uid = account_uid
        self.password_hash = password_hash
        self.password_salt = password_salt
        self.date_from = date_from
        self.date_to = date_to
        self.usage_count = usage_count


@dataclass(frozen=False)
class auth_password_rule_write_dto(base_write_dto):
    auth_password_uid: str
    auth_password_name: str
    rule_type: int
    rule_parameters: str
    user_scope: str
    def __init__(self, auth_password_uid: str, auth_password_name: str, rule_type: int, rule_parameters: str, user_scope: str, custom_attributes: str = "{}"):
        self.auth_password_uid = auth_password_uid
        self.auth_password_name = auth_password_name
        self.rule_type = rule_type
        self.rule_parameters = rule_parameters
        self.user_scope = user_scope
        self.custom_attributes = custom_attributes
    @classmethod
    def empty_write(cls):
        return cls("", "", 0, "", "")
    @classmethod
    def default_write(cls):
        return cls("", "", 0, "", "")
    @classmethod
    def random_write(cls):
        return cls(base_dto.get_random_uid(), base_dto.get_random_uid(), 0, base_dto.get_random_uid(), base_dto.get_random_uid())
    @classmethod
    def new_write(cls, auth_password_uid: str, auth_password_name: str, rule_type: int, rule_parameters: str, user_scope: str):
        return cls(auth_password_uid, auth_password_name, rule_type, rule_parameters, user_scope)
    @classmethod
    def new_write_with_defaults(cls, auth_password_uid: str = "", auth_password_name: str = "", rule_type: int = 0, rule_parameters: str = "", user_scope: str = ""):
        return cls(auth_password_uid, auth_password_name, rule_type, rule_parameters, user_scope)
    @classmethod
    def new_write_random_uid(cls, auth_password_uid: str, auth_password_name: str, rule_type: int, rule_parameters: str, user_scope: str):
        return cls(base_dto.get_random_uid(), auth_password_uid, auth_password_name, rule_type, rule_parameters, user_scope)
    @classmethod
    def get_class_model(cls) -> base_model:
        return db_models.auth_password_rule_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["auth_password_uid"], d["auth_password_name"], d["rule_type"], d["rule_parameters"], d["user_scope"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return auth_password_rule_write_dto(self.auth_password_uid, self.auth_password_name, self.rule_type, self.rule_parameters, self.user_scope, self.custom_attributes)
    def clone_write_new_uid(self):
        return auth_password_rule_write_dto(base_dto.get_random_uid(), self.auth_password_uid, self.auth_password_name, self.rule_type, self.rule_parameters, self.user_scope, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return auth_password_rule_write_dto(uid, self.auth_password_uid, self.auth_password_name, self.rule_type, self.rule_parameters, self.user_scope, self.custom_attributes)
    def get_model(self) -> base_model:
        return db_models.auth_password_rule_model
    def get_uid(self) -> str:
        return self.auth_password_rule_uid
    def get_name(self) -> str:
        return self.auth_password_rule_name
    def get_list_values(self) -> list[any]:
        return [self.auth_password_uid, self.auth_password_name, self.rule_type, self.rule_parameters, self.user_scope, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.auth_password_uid, self.auth_password_name, self.rule_type, self.rule_parameters, self.user_scope]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.auth_password_uid, self.auth_password_name, self.rule_type, self.rule_parameters, self.user_scope, self.custom_attributes, updated_by, self.auth_password_rule_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.auth_password_rule_uid, self.auth_password_uid, self.auth_password_name, self.rule_type, self.rule_parameters, self.user_scope, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.auth_password_uid, self.auth_password_name, self.rule_type, self.rule_parameters, self.user_scope]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.auth_password_uid, self.auth_password_name, self.rule_type, self.rule_parameters, self.user_scope, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_uid() == obj.get_uid()
    def update_uid(self, uid: str):
        self.auth_password_rule_uid = uid
    def update_uid_attributes(self, auth_password_uid: str, auth_password_name: str, rule_type: int, rule_parameters: str, user_scope: str):
        self.auth_password_uid = auth_password_uid
        self.auth_password_name = auth_password_name
        self.rule_type = rule_type
        self.rule_parameters = rule_parameters
        self.user_scope = user_scope
    def update_attributes(self, auth_password_uid: str, auth_password_name: str, rule_type: int, rule_parameters: str, user_scope: str):
        self.auth_password_uid = auth_password_uid
        self.auth_password_name = auth_password_name
        self.rule_type = rule_type
        self.rule_parameters = rule_parameters
        self.user_scope = user_scope


@dataclass(frozen=False)
class auth_permission_write_dto(base_write_dto):
    auth_permission_uid: str
    auth_permission_name: str
    tenant_uid: str
    account_uid: str
    auth_role_uid: str
    client_uid: str | None
    project_instance_uid: str | None
    auth_permission_type_uid: str | None
    valid_from_date: datetime.datetime
    valid_till_date: datetime.datetime
    def __init__(self, auth_permission_uid: str, auth_permission_name: str, tenant_uid: str, account_uid: str, auth_role_uid: str, client_uid: str | None, project_instance_uid: str | None, auth_permission_type_uid: str | None, valid_from_date: datetime.datetime, valid_till_date: datetime.datetime, custom_attributes: str = "{}"):
        self.auth_permission_uid = auth_permission_uid
        self.auth_permission_name = auth_permission_name
        self.tenant_uid = tenant_uid
        self.account_uid = account_uid
        self.auth_role_uid = auth_role_uid
        self.client_uid = client_uid
        self.project_instance_uid = project_instance_uid
        self.auth_permission_type_uid = auth_permission_type_uid
        self.valid_from_date = valid_from_date
        self.valid_till_date = valid_till_date
        self.custom_attributes = custom_attributes
    @classmethod
    def empty_write(cls):
        return cls("", "", "", "", "", "", "", "", datetime.datetime.now(), datetime.datetime.now())
    @classmethod
    def default_write(cls):
        return cls(base_dto.get_random_uid(), "", "", "", "", "", "", "", datetime.datetime.now(), datetime.datetime.now())
    @classmethod
    def random_write(cls):
        return cls(base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), datetime.datetime.now(), datetime.datetime.now())
    @classmethod
    def new_write(cls, auth_permission_uid: str, auth_permission_name: str, tenant_uid: str, account_uid: str, auth_role_uid: str, client_uid: str | None, project_instance_uid: str | None, auth_permission_type_uid: str | None, valid_from_date: datetime.datetime, valid_till_date: datetime.datetime):
        return cls(auth_permission_uid, auth_permission_name, tenant_uid, account_uid, auth_role_uid, client_uid, project_instance_uid, auth_permission_type_uid, valid_from_date, valid_till_date)
    @classmethod
    def new_write_with_defaults(cls, auth_permission_uid: str = "", auth_permission_name: str = "", tenant_uid: str = "", account_uid: str = "", auth_role_uid: str = "", client_uid: str | None = "", project_instance_uid: str | None = "", auth_permission_type_uid: str | None = "", valid_from_date: datetime.datetime = datetime.datetime.now(), valid_till_date: datetime.datetime = datetime.datetime.now()):
        return cls(auth_permission_uid, auth_permission_name, tenant_uid, account_uid, auth_role_uid, client_uid, project_instance_uid, auth_permission_type_uid, valid_from_date, valid_till_date)
    @classmethod
    def new_write_random_uid(cls, auth_permission_name: str, tenant_uid: str, account_uid: str, auth_role_uid: str, client_uid: str | None, project_instance_uid: str | None, auth_permission_type_uid: str | None, valid_from_date: datetime.datetime, valid_till_date: datetime.datetime):
        return cls(base_dto.get_random_uid(), auth_permission_name, tenant_uid, account_uid, auth_role_uid, client_uid, project_instance_uid, auth_permission_type_uid, valid_from_date, valid_till_date)
    @classmethod
    def get_class_model(cls) -> base_model:
        return db_models.auth_permission_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["auth_permission_uid"], d["auth_permission_name"], d["tenant_uid"], d["account_uid"], d["auth_role_uid"], d["client_uid"], d["project_instance_uid"], d["auth_permission_type_uid"], d["valid_from_date"], d["valid_till_date"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return auth_permission_write_dto(self.auth_permission_uid, self.auth_permission_name, self.tenant_uid, self.account_uid, self.auth_role_uid, self.client_uid, self.project_instance_uid, self.auth_permission_type_uid, self.valid_from_date, self.valid_till_date, self.custom_attributes)
    def clone_write_new_uid(self):
        return auth_permission_write_dto(base_dto.get_random_uid(), self.auth_permission_name, self.tenant_uid, self.account_uid, self.auth_role_uid, self.client_uid, self.project_instance_uid, self.auth_permission_type_uid, self.valid_from_date, self.valid_till_date, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return auth_permission_write_dto(uid, self.auth_permission_name, self.tenant_uid, self.account_uid, self.auth_role_uid, self.client_uid, self.project_instance_uid, self.auth_permission_type_uid, self.valid_from_date, self.valid_till_date, self.custom_attributes)
    def get_model(self) -> base_model:
        return db_models.auth_permission_model
    def get_uid(self) -> str:
        return self.auth_permission_uid
    def get_name(self) -> str:
        return self.auth_permission_name
    def get_list_values(self) -> list[any]:
        return [self.auth_permission_uid, self.auth_permission_name, self.tenant_uid, self.account_uid, self.auth_role_uid, self.client_uid, self.project_instance_uid, self.auth_permission_type_uid, self.valid_from_date, self.valid_till_date, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.auth_permission_uid, self.auth_permission_name, self.tenant_uid, self.account_uid, self.auth_role_uid, self.client_uid, self.project_instance_uid, self.auth_permission_type_uid, self.valid_from_date, self.valid_till_date]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.auth_permission_name, self.tenant_uid, self.account_uid, self.auth_role_uid, self.client_uid, self.project_instance_uid, self.auth_permission_type_uid, self.valid_from_date, self.valid_till_date, self.custom_attributes, updated_by, self.auth_permission_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.auth_permission_uid, self.auth_permission_name, self.tenant_uid, self.account_uid, self.auth_role_uid, self.client_uid, self.project_instance_uid, self.auth_permission_type_uid, self.valid_from_date, self.valid_till_date, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.auth_permission_name, self.tenant_uid, self.account_uid, self.auth_role_uid, self.client_uid, self.project_instance_uid, self.auth_permission_type_uid, self.valid_from_date, self.valid_till_date]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.auth_permission_name, self.tenant_uid, self.account_uid, self.auth_role_uid, self.client_uid, self.project_instance_uid, self.auth_permission_type_uid, self.valid_from_date, self.valid_till_date, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_uid() == obj.get_uid()
    def update_uid(self, uid: str):
        self.auth_permission_uid = uid
    def update_uid_attributes(self, auth_permission_uid: str, auth_permission_name: str, tenant_uid: str, account_uid: str, auth_role_uid: str, client_uid: str | None, project_instance_uid: str | None, auth_permission_type_uid: str | None, valid_from_date: datetime.datetime, valid_till_date: datetime.datetime):
        self.auth_permission_uid = auth_permission_uid
        self.auth_permission_name = auth_permission_name
        self.tenant_uid = tenant_uid
        self.account_uid = account_uid
        self.auth_role_uid = auth_role_uid
        self.client_uid = client_uid
        self.project_instance_uid = project_instance_uid
        self.auth_permission_type_uid = auth_permission_type_uid
        self.valid_from_date = valid_from_date
        self.valid_till_date = valid_till_date
    def update_attributes(self, auth_permission_name: str, tenant_uid: str, account_uid: str, auth_role_uid: str, client_uid: str | None, project_instance_uid: str | None, auth_permission_type_uid: str | None, valid_from_date: datetime.datetime, valid_till_date: datetime.datetime):
        self.auth_permission_name = auth_permission_name
        self.tenant_uid = tenant_uid
        self.account_uid = account_uid
        self.auth_role_uid = auth_role_uid
        self.client_uid = client_uid
        self.project_instance_uid = project_instance_uid
        self.auth_permission_type_uid = auth_permission_type_uid
        self.valid_from_date = valid_from_date
        self.valid_till_date = valid_till_date


@dataclass(frozen=False)
class auth_permission_type_write_dto(base_write_dto):
    auth_permission_type_uid: str
    auth_permission_type_name: str
    def __init__(self, auth_permission_type_uid: str, auth_permission_type_name: str, custom_attributes: str = "{}"):
        self.auth_permission_type_uid = auth_permission_type_uid
        self.auth_permission_type_name = auth_permission_type_name
        self.custom_attributes = custom_attributes
    @classmethod
    def empty_write(cls):
        return cls("", "")
    @classmethod
    def default_write(cls):
        return cls(base_dto.get_random_uid(), "")
    @classmethod
    def random_write(cls):
        return cls(base_dto.get_random_uid(), base_dto.get_random_uid())
    @classmethod
    def new_write(cls, auth_permission_type_uid: str, auth_permission_type_name: str):
        return cls(auth_permission_type_uid, auth_permission_type_name)
    @classmethod
    def new_write_with_defaults(cls, auth_permission_type_uid: str = "", auth_permission_type_name: str = ""):
        return cls(auth_permission_type_uid, auth_permission_type_name)
    @classmethod
    def new_write_random_uid(cls, auth_permission_type_name: str):
        return cls(base_dto.get_random_uid(), auth_permission_type_name)
    @classmethod
    def get_class_model(cls) -> base_model:
        return db_models.auth_permission_type_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["auth_permission_type_uid"], d["auth_permission_type_name"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return auth_permission_type_write_dto(self.auth_permission_type_uid, self.auth_permission_type_name, self.custom_attributes)
    def clone_write_new_uid(self):
        return auth_permission_type_write_dto(base_dto.get_random_uid(), self.auth_permission_type_name, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return auth_permission_type_write_dto(uid, self.auth_permission_type_name, self.custom_attributes)
    def get_model(self) -> base_model:
        return db_models.auth_permission_type_model
    def get_uid(self) -> str:
        return self.auth_permission_type_uid
    def get_name(self) -> str:
        return self.auth_permission_type_name
    def get_list_values(self) -> list[any]:
        return [self.auth_permission_type_uid, self.auth_permission_type_name, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.auth_permission_type_uid, self.auth_permission_type_name]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.auth_permission_type_name, self.custom_attributes, updated_by, self.auth_permission_type_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.auth_permission_type_uid, self.auth_permission_type_name, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.auth_permission_type_name]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.auth_permission_type_name, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_uid() == obj.get_uid()
    def update_uid(self, uid: str):
        self.auth_permission_type_uid = uid
    def update_uid_attributes(self, auth_permission_type_uid: str, auth_permission_type_name: str):
        self.auth_permission_type_uid = auth_permission_type_uid
        self.auth_permission_type_name = auth_permission_type_name
    def update_attributes(self, auth_permission_type_name: str):
        self.auth_permission_type_name = auth_permission_type_name


@dataclass(frozen=False)
class auth_pin_write_dto(base_write_dto):
    auth_pin_uid: str
    auth_pin_name: str
    tenant_uid: str
    account_uid: str
    pin_hash: str
    pin_salt: str
    def __init__(self, auth_pin_uid: str, auth_pin_name: str, tenant_uid: str, account_uid: str, pin_hash: str, pin_salt: str, custom_attributes: str = "{}"):
        self.auth_pin_uid = auth_pin_uid
        self.auth_pin_name = auth_pin_name
        self.tenant_uid = tenant_uid
        self.account_uid = account_uid
        self.pin_hash = pin_hash
        self.pin_salt = pin_salt
        self.custom_attributes = custom_attributes
    @classmethod
    def empty_write(cls):
        return cls("", "", "", "", "", "")
    @classmethod
    def default_write(cls):
        return cls(base_dto.get_random_uid(), "", "", "", "", "")
    @classmethod
    def random_write(cls):
        return cls(base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid())
    @classmethod
    def new_write(cls, auth_pin_uid: str, auth_pin_name: str, tenant_uid: str, account_uid: str, pin_hash: str, pin_salt: str):
        return cls(auth_pin_uid, auth_pin_name, tenant_uid, account_uid, pin_hash, pin_salt)
    @classmethod
    def new_write_with_defaults(cls, auth_pin_uid: str = "", auth_pin_name: str = "", tenant_uid: str = "", account_uid: str = "", pin_hash: str = "", pin_salt: str = ""):
        return cls(auth_pin_uid, auth_pin_name, tenant_uid, account_uid, pin_hash, pin_salt)
    @classmethod
    def new_write_random_uid(cls, auth_pin_name: str, tenant_uid: str, account_uid: str, pin_hash: str, pin_salt: str):
        return cls(base_dto.get_random_uid(), auth_pin_name, tenant_uid, account_uid, pin_hash, pin_salt)
    @classmethod
    def get_class_model(cls) -> base_model:
        return db_models.auth_pin_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["auth_pin_uid"], d["auth_pin_name"], d["tenant_uid"], d["account_uid"], d["pin_hash"], d["pin_salt"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return auth_pin_write_dto(self.auth_pin_uid, self.auth_pin_name, self.tenant_uid, self.account_uid, self.pin_hash, self.pin_salt, self.custom_attributes)
    def clone_write_new_uid(self):
        return auth_pin_write_dto(base_dto.get_random_uid(), self.auth_pin_name, self.tenant_uid, self.account_uid, self.pin_hash, self.pin_salt, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return auth_pin_write_dto(uid, self.auth_pin_name, self.tenant_uid, self.account_uid, self.pin_hash, self.pin_salt, self.custom_attributes)
    def get_model(self) -> base_model:
        return db_models.auth_pin_model
    def get_uid(self) -> str:
        return self.auth_pin_uid
    def get_name(self) -> str:
        return self.auth_pin_name
    def get_list_values(self) -> list[any]:
        return [self.auth_pin_uid, self.auth_pin_name, self.tenant_uid, self.account_uid, self.pin_hash, self.pin_salt, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.auth_pin_uid, self.auth_pin_name, self.tenant_uid, self.account_uid, self.pin_hash, self.pin_salt]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.auth_pin_name, self.tenant_uid, self.account_uid, self.pin_hash, self.pin_salt, self.custom_attributes, updated_by, self.auth_pin_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.auth_pin_uid, self.auth_pin_name, self.tenant_uid, self.account_uid, self.pin_hash, self.pin_salt, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.auth_pin_name, self.tenant_uid, self.account_uid, self.pin_hash, self.pin_salt]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.auth_pin_name, self.tenant_uid, self.account_uid, self.pin_hash, self.pin_salt, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_uid() == obj.get_uid()
    def update_uid(self, uid: str):
        self.auth_pin_uid = uid
    def update_uid_attributes(self, auth_pin_uid: str, auth_pin_name: str, tenant_uid: str, account_uid: str, pin_hash: str, pin_salt: str):
        self.auth_pin_uid = auth_pin_uid
        self.auth_pin_name = auth_pin_name
        self.tenant_uid = tenant_uid
        self.account_uid = account_uid
        self.pin_hash = pin_hash
        self.pin_salt = pin_salt
    def update_attributes(self, auth_pin_name: str, tenant_uid: str, account_uid: str, pin_hash: str, pin_salt: str):
        self.auth_pin_name = auth_pin_name
        self.tenant_uid = tenant_uid
        self.account_uid = account_uid
        self.pin_hash = pin_hash
        self.pin_salt = pin_salt


@dataclass(frozen=False)
class auth_request_write_dto(base_write_dto):
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
    def __init__(self, auth_request_uid: str, auth_request_name: str, tenant_uid: str, account_uid: str, requestor_email: str, reset_guid: str, valid_till_date: datetime.datetime, lock_guid: str | None, lock_by: str | None, lock_date: datetime.datetime | None, is_checked: int, is_used: int, check_date: datetime.datetime | None, use_date: datetime.datetime | None, event_notification_uid: str | None, custom_attributes: str = "{}"):
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
        self.custom_attributes = custom_attributes
    @classmethod
    def empty_write(cls):
        return cls("", "", "", "", "", "", datetime.datetime.now(), "", "", datetime.datetime.now(), 0, 0, datetime.datetime.now(), datetime.datetime.now(), "")
    @classmethod
    def default_write(cls):
        return cls(base_dto.get_random_uid(), "", "", "", "", "", datetime.datetime.now(), "", "", datetime.datetime.now(), 0, 0, datetime.datetime.now(), datetime.datetime.now(), "")
    @classmethod
    def random_write(cls):
        return cls(base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), datetime.datetime.now(), base_dto.get_random_uid(), base_dto.get_random_uid(), datetime.datetime.now(), 0, 0, datetime.datetime.now(), datetime.datetime.now(), base_dto.get_random_uid())
    @classmethod
    def new_write(cls, auth_request_uid: str, auth_request_name: str, tenant_uid: str, account_uid: str, requestor_email: str, reset_guid: str, valid_till_date: datetime.datetime, lock_guid: str | None, lock_by: str | None, lock_date: datetime.datetime | None, is_checked: int, is_used: int, check_date: datetime.datetime | None, use_date: datetime.datetime | None, event_notification_uid: str | None):
        return cls(auth_request_uid, auth_request_name, tenant_uid, account_uid, requestor_email, reset_guid, valid_till_date, lock_guid, lock_by, lock_date, is_checked, is_used, check_date, use_date, event_notification_uid)
    @classmethod
    def new_write_with_defaults(cls, auth_request_uid: str = "", auth_request_name: str = "", tenant_uid: str = "", account_uid: str = "", requestor_email: str = "", reset_guid: str = "", valid_till_date: datetime.datetime = datetime.datetime.now(), lock_guid: str | None = "", lock_by: str | None = "", lock_date: datetime.datetime | None = datetime.datetime.now(), is_checked: int = 0, is_used: int = 0, check_date: datetime.datetime | None = datetime.datetime.now(), use_date: datetime.datetime | None = datetime.datetime.now(), event_notification_uid: str | None = ""):
        return cls(auth_request_uid, auth_request_name, tenant_uid, account_uid, requestor_email, reset_guid, valid_till_date, lock_guid, lock_by, lock_date, is_checked, is_used, check_date, use_date, event_notification_uid)
    @classmethod
    def new_write_random_uid(cls, auth_request_name: str, tenant_uid: str, account_uid: str, requestor_email: str, reset_guid: str, valid_till_date: datetime.datetime, lock_guid: str | None, lock_by: str | None, lock_date: datetime.datetime | None, is_checked: int, is_used: int, check_date: datetime.datetime | None, use_date: datetime.datetime | None, event_notification_uid: str | None):
        return cls(base_dto.get_random_uid(), auth_request_name, tenant_uid, account_uid, requestor_email, reset_guid, valid_till_date, lock_guid, lock_by, lock_date, is_checked, is_used, check_date, use_date, event_notification_uid)
    @classmethod
    def get_class_model(cls) -> base_model:
        return db_models.auth_request_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["auth_request_uid"], d["auth_request_name"], d["tenant_uid"], d["account_uid"], d["requestor_email"], d["reset_guid"], d["valid_till_date"], d["lock_guid"], d["lock_by"], d["lock_date"], d["is_checked"], d["is_used"], d["check_date"], d["use_date"], d["event_notification_uid"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return auth_request_write_dto(self.auth_request_uid, self.auth_request_name, self.tenant_uid, self.account_uid, self.requestor_email, self.reset_guid, self.valid_till_date, self.lock_guid, self.lock_by, self.lock_date, self.is_checked, self.is_used, self.check_date, self.use_date, self.event_notification_uid, self.custom_attributes)
    def clone_write_new_uid(self):
        return auth_request_write_dto(base_dto.get_random_uid(), self.auth_request_name, self.tenant_uid, self.account_uid, self.requestor_email, self.reset_guid, self.valid_till_date, self.lock_guid, self.lock_by, self.lock_date, self.is_checked, self.is_used, self.check_date, self.use_date, self.event_notification_uid, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return auth_request_write_dto(uid, self.auth_request_name, self.tenant_uid, self.account_uid, self.requestor_email, self.reset_guid, self.valid_till_date, self.lock_guid, self.lock_by, self.lock_date, self.is_checked, self.is_used, self.check_date, self.use_date, self.event_notification_uid, self.custom_attributes)
    def get_model(self) -> base_model:
        return db_models.auth_request_model
    def get_uid(self) -> str:
        return self.auth_request_uid
    def get_name(self) -> str:
        return self.auth_request_name
    def get_list_values(self) -> list[any]:
        return [self.auth_request_uid, self.auth_request_name, self.tenant_uid, self.account_uid, self.requestor_email, self.reset_guid, self.valid_till_date, self.lock_guid, self.lock_by, self.lock_date, self.is_checked, self.is_used, self.check_date, self.use_date, self.event_notification_uid, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.auth_request_uid, self.auth_request_name, self.tenant_uid, self.account_uid, self.requestor_email, self.reset_guid, self.valid_till_date, self.lock_guid, self.lock_by, self.lock_date, self.is_checked, self.is_used, self.check_date, self.use_date, self.event_notification_uid]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.auth_request_name, self.tenant_uid, self.account_uid, self.requestor_email, self.reset_guid, self.valid_till_date, self.lock_guid, self.lock_by, self.lock_date, self.is_checked, self.is_used, self.check_date, self.use_date, self.event_notification_uid, self.custom_attributes, updated_by, self.auth_request_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.auth_request_uid, self.auth_request_name, self.tenant_uid, self.account_uid, self.requestor_email, self.reset_guid, self.valid_till_date, self.lock_guid, self.lock_by, self.lock_date, self.is_checked, self.is_used, self.check_date, self.use_date, self.event_notification_uid, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.auth_request_name, self.tenant_uid, self.account_uid, self.requestor_email, self.reset_guid, self.valid_till_date, self.lock_guid, self.lock_by, self.lock_date, self.is_checked, self.is_used, self.check_date, self.use_date, self.event_notification_uid]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.auth_request_name, self.tenant_uid, self.account_uid, self.requestor_email, self.reset_guid, self.valid_till_date, self.lock_guid, self.lock_by, self.lock_date, self.is_checked, self.is_used, self.check_date, self.use_date, self.event_notification_uid, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_uid() == obj.get_uid()
    def update_uid(self, uid: str):
        self.auth_request_uid = uid
    def update_uid_attributes(self, auth_request_uid: str, auth_request_name: str, tenant_uid: str, account_uid: str, requestor_email: str, reset_guid: str, valid_till_date: datetime.datetime, lock_guid: str | None, lock_by: str | None, lock_date: datetime.datetime | None, is_checked: int, is_used: int, check_date: datetime.datetime | None, use_date: datetime.datetime | None, event_notification_uid: str | None):
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
    def update_attributes(self, auth_request_name: str, tenant_uid: str, account_uid: str, requestor_email: str, reset_guid: str, valid_till_date: datetime.datetime, lock_guid: str | None, lock_by: str | None, lock_date: datetime.datetime | None, is_checked: int, is_used: int, check_date: datetime.datetime | None, use_date: datetime.datetime | None, event_notification_uid: str | None):
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


@dataclass(frozen=False)
class auth_role_write_dto(base_write_dto):
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
    def __init__(self, auth_role_uid: str, auth_role_name: str, parent_auth_role_uid: str | None, tenant_uid: str | None, role_description: str, access_uris: str, is_project: int, is_tenant: int, is_client: int, is_custom: int, custom_attributes: str = "{}"):
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
        self.custom_attributes = custom_attributes
    @classmethod
    def empty_write(cls):
        return cls("", "", "", "", "", "", 0, 0, 0, 0)
    @classmethod
    def default_write(cls):
        return cls(base_dto.get_random_uid(), "", "", "", "", "", 0, 0, 0, 0)
    @classmethod
    def random_write(cls):
        return cls(base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), 0, 0, 0, 0)
    @classmethod
    def new_write(cls, auth_role_uid: str, auth_role_name: str, parent_auth_role_uid: str | None, tenant_uid: str | None, role_description: str, access_uris: str, is_project: int, is_tenant: int, is_client: int, is_custom: int):
        return cls(auth_role_uid, auth_role_name, parent_auth_role_uid, tenant_uid, role_description, access_uris, is_project, is_tenant, is_client, is_custom)
    @classmethod
    def new_write_with_defaults(cls, auth_role_uid: str = "", auth_role_name: str = "", parent_auth_role_uid: str | None = "", tenant_uid: str | None = "", role_description: str = "", access_uris: str = "", is_project: int = 0, is_tenant: int = 0, is_client: int = 0, is_custom: int = 0):
        return cls(auth_role_uid, auth_role_name, parent_auth_role_uid, tenant_uid, role_description, access_uris, is_project, is_tenant, is_client, is_custom)
    @classmethod
    def new_write_random_uid(cls, auth_role_name: str, parent_auth_role_uid: str | None, tenant_uid: str | None, role_description: str, access_uris: str, is_project: int, is_tenant: int, is_client: int, is_custom: int):
        return cls(base_dto.get_random_uid(), auth_role_name, parent_auth_role_uid, tenant_uid, role_description, access_uris, is_project, is_tenant, is_client, is_custom)
    @classmethod
    def get_class_model(cls) -> base_model:
        return db_models.auth_role_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["auth_role_uid"], d["auth_role_name"], d["parent_auth_role_uid"], d["tenant_uid"], d["role_description"], d["access_uris"], d["is_project"], d["is_tenant"], d["is_client"], d["is_custom"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return auth_role_write_dto(self.auth_role_uid, self.auth_role_name, self.parent_auth_role_uid, self.tenant_uid, self.role_description, self.access_uris, self.is_project, self.is_tenant, self.is_client, self.is_custom, self.custom_attributes)
    def clone_write_new_uid(self):
        return auth_role_write_dto(base_dto.get_random_uid(), self.auth_role_name, self.parent_auth_role_uid, self.tenant_uid, self.role_description, self.access_uris, self.is_project, self.is_tenant, self.is_client, self.is_custom, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return auth_role_write_dto(uid, self.auth_role_name, self.parent_auth_role_uid, self.tenant_uid, self.role_description, self.access_uris, self.is_project, self.is_tenant, self.is_client, self.is_custom, self.custom_attributes)
    def get_model(self) -> base_model:
        return db_models.auth_role_model
    def get_uid(self) -> str:
        return self.auth_role_uid
    def get_name(self) -> str:
        return self.auth_role_name
    def get_list_values(self) -> list[any]:
        return [self.auth_role_uid, self.auth_role_name, self.parent_auth_role_uid, self.tenant_uid, self.role_description, self.access_uris, self.is_project, self.is_tenant, self.is_client, self.is_custom, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.auth_role_uid, self.auth_role_name, self.parent_auth_role_uid, self.tenant_uid, self.role_description, self.access_uris, self.is_project, self.is_tenant, self.is_client, self.is_custom]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.auth_role_name, self.parent_auth_role_uid, self.tenant_uid, self.role_description, self.access_uris, self.is_project, self.is_tenant, self.is_client, self.is_custom, self.custom_attributes, updated_by, self.auth_role_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.auth_role_uid, self.auth_role_name, self.parent_auth_role_uid, self.tenant_uid, self.role_description, self.access_uris, self.is_project, self.is_tenant, self.is_client, self.is_custom, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.auth_role_name, self.parent_auth_role_uid, self.tenant_uid, self.role_description, self.access_uris, self.is_project, self.is_tenant, self.is_client, self.is_custom]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.auth_role_name, self.parent_auth_role_uid, self.tenant_uid, self.role_description, self.access_uris, self.is_project, self.is_tenant, self.is_client, self.is_custom, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_uid() == obj.get_uid()
    def update_uid(self, uid: str):
        self.auth_role_uid = uid
    def update_uid_attributes(self, auth_role_uid: str, auth_role_name: str, parent_auth_role_uid: str | None, tenant_uid: str | None, role_description: str, access_uris: str, is_project: int, is_tenant: int, is_client: int, is_custom: int):
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
    def update_attributes(self, auth_role_name: str, parent_auth_role_uid: str | None, tenant_uid: str | None, role_description: str, access_uris: str, is_project: int, is_tenant: int, is_client: int, is_custom: int):
        self.auth_role_name = auth_role_name
        self.parent_auth_role_uid = parent_auth_role_uid
        self.tenant_uid = tenant_uid
        self.role_description = role_description
        self.access_uris = access_uris
        self.is_project = is_project
        self.is_tenant = is_tenant
        self.is_client = is_client
        self.is_custom = is_custom


@dataclass(frozen=False)
class auth_role_uri_write_dto(base_write_dto):
    auth_role_uri_uid: str
    auth_role_uri_name: str
    auth_role_uid: str | None
    uri: str
    def __init__(self, auth_role_uri_uid: str, auth_role_uri_name: str, auth_role_uid: str | None, uri: str, custom_attributes: str = "{}"):
        self.auth_role_uri_uid = auth_role_uri_uid
        self.auth_role_uri_name = auth_role_uri_name
        self.auth_role_uid = auth_role_uid
        self.uri = uri
        self.custom_attributes = custom_attributes
    @classmethod
    def empty_write(cls):
        return cls("", "", "", "")
    @classmethod
    def default_write(cls):
        return cls(base_dto.get_random_uid(), "", "", "")
    @classmethod
    def random_write(cls):
        return cls(base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid())
    @classmethod
    def new_write(cls, auth_role_uri_uid: str, auth_role_uri_name: str, auth_role_uid: str | None, uri: str):
        return cls(auth_role_uri_uid, auth_role_uri_name, auth_role_uid, uri)
    @classmethod
    def new_write_with_defaults(cls, auth_role_uri_uid: str = "", auth_role_uri_name: str = "", auth_role_uid: str | None = "", uri: str = ""):
        return cls(auth_role_uri_uid, auth_role_uri_name, auth_role_uid, uri)
    @classmethod
    def new_write_random_uid(cls, auth_role_uri_name: str, auth_role_uid: str | None, uri: str):
        return cls(base_dto.get_random_uid(), auth_role_uri_name, auth_role_uid, uri)
    @classmethod
    def get_class_model(cls) -> base_model:
        return db_models.auth_role_uri_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["auth_role_uri_uid"], d["auth_role_uri_name"], d["auth_role_uid"], d["uri"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return auth_role_uri_write_dto(self.auth_role_uri_uid, self.auth_role_uri_name, self.auth_role_uid, self.uri, self.custom_attributes)
    def clone_write_new_uid(self):
        return auth_role_uri_write_dto(base_dto.get_random_uid(), self.auth_role_uri_name, self.auth_role_uid, self.uri, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return auth_role_uri_write_dto(uid, self.auth_role_uri_name, self.auth_role_uid, self.uri, self.custom_attributes)
    def get_model(self) -> base_model:
        return db_models.auth_role_uri_model
    def get_uid(self) -> str:
        return self.auth_role_uri_uid
    def get_name(self) -> str:
        return self.auth_role_uri_name
    def get_list_values(self) -> list[any]:
        return [self.auth_role_uri_uid, self.auth_role_uri_name, self.auth_role_uid, self.uri, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.auth_role_uri_uid, self.auth_role_uri_name, self.auth_role_uid, self.uri]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.auth_role_uri_name, self.auth_role_uid, self.uri, self.custom_attributes, updated_by, self.auth_role_uri_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.auth_role_uri_uid, self.auth_role_uri_name, self.auth_role_uid, self.uri, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.auth_role_uri_name, self.auth_role_uid, self.uri]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.auth_role_uri_name, self.auth_role_uid, self.uri, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_uid() == obj.get_uid()
    def update_uid(self, uid: str):
        self.auth_role_uri_uid = uid
    def update_uid_attributes(self, auth_role_uri_uid: str, auth_role_uri_name: str, auth_role_uid: str | None, uri: str):
        self.auth_role_uri_uid = auth_role_uri_uid
        self.auth_role_uri_name = auth_role_uri_name
        self.auth_role_uid = auth_role_uid
        self.uri = uri
    def update_attributes(self, auth_role_uri_name: str, auth_role_uid: str | None, uri: str):
        self.auth_role_uri_name = auth_role_uri_name
        self.auth_role_uid = auth_role_uid
        self.uri = uri


@dataclass(frozen=False)
class auth_session_write_dto(base_write_dto):
    auth_session_uid: str
    auth_session_name: str
    tenant_uid: str | None
    account_uid: str | None
    session_token: str
    browser_name: str
    browser_description: str
    host_name: str
    def __init__(self, auth_session_uid: str, auth_session_name: str, tenant_uid: str | None, account_uid: str | None, session_token: str, browser_name: str, browser_description: str, host_name: str, custom_attributes: str = "{}"):
        self.auth_session_uid = auth_session_uid
        self.auth_session_name = auth_session_name
        self.tenant_uid = tenant_uid
        self.account_uid = account_uid
        self.session_token = session_token
        self.browser_name = browser_name
        self.browser_description = browser_description
        self.host_name = host_name
        self.custom_attributes = custom_attributes
    @classmethod
    def empty_write(cls):
        return cls("", "", "", "", "", "", "", "")
    @classmethod
    def default_write(cls):
        return cls(base_dto.get_random_uid(), "", "", "", "", "", "", "")
    @classmethod
    def random_write(cls):
        return cls(base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid())
    @classmethod
    def new_write(cls, auth_session_uid: str, auth_session_name: str, tenant_uid: str | None, account_uid: str | None, session_token: str, browser_name: str, browser_description: str, host_name: str):
        return cls(auth_session_uid, auth_session_name, tenant_uid, account_uid, session_token, browser_name, browser_description, host_name)
    @classmethod
    def new_write_with_defaults(cls, auth_session_uid: str = "", auth_session_name: str = "", tenant_uid: str | None = "", account_uid: str | None = "", session_token: str = "", browser_name: str = "", browser_description: str = "", host_name: str = ""):
        return cls(auth_session_uid, auth_session_name, tenant_uid, account_uid, session_token, browser_name, browser_description, host_name)
    @classmethod
    def new_write_random_uid(cls, auth_session_name: str, tenant_uid: str | None, account_uid: str | None, session_token: str, browser_name: str, browser_description: str, host_name: str):
        return cls(base_dto.get_random_uid(), auth_session_name, tenant_uid, account_uid, session_token, browser_name, browser_description, host_name)
    @classmethod
    def get_class_model(cls) -> base_model:
        return db_models.auth_session_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["auth_session_uid"], d["auth_session_name"], d["tenant_uid"], d["account_uid"], d["session_token"], d["browser_name"], d["browser_description"], d["host_name"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return auth_session_write_dto(self.auth_session_uid, self.auth_session_name, self.tenant_uid, self.account_uid, self.session_token, self.browser_name, self.browser_description, self.host_name, self.custom_attributes)
    def clone_write_new_uid(self):
        return auth_session_write_dto(base_dto.get_random_uid(), self.auth_session_name, self.tenant_uid, self.account_uid, self.session_token, self.browser_name, self.browser_description, self.host_name, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return auth_session_write_dto(uid, self.auth_session_name, self.tenant_uid, self.account_uid, self.session_token, self.browser_name, self.browser_description, self.host_name, self.custom_attributes)
    def get_model(self) -> base_model:
        return db_models.auth_session_model
    def get_uid(self) -> str:
        return self.auth_session_uid
    def get_name(self) -> str:
        return self.auth_session_name
    def get_list_values(self) -> list[any]:
        return [self.auth_session_uid, self.auth_session_name, self.tenant_uid, self.account_uid, self.session_token, self.browser_name, self.browser_description, self.host_name, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.auth_session_uid, self.auth_session_name, self.tenant_uid, self.account_uid, self.session_token, self.browser_name, self.browser_description, self.host_name]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.auth_session_name, self.tenant_uid, self.account_uid, self.session_token, self.browser_name, self.browser_description, self.host_name, self.custom_attributes, updated_by, self.auth_session_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.auth_session_uid, self.auth_session_name, self.tenant_uid, self.account_uid, self.session_token, self.browser_name, self.browser_description, self.host_name, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.auth_session_name, self.tenant_uid, self.account_uid, self.session_token, self.browser_name, self.browser_description, self.host_name]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.auth_session_name, self.tenant_uid, self.account_uid, self.session_token, self.browser_name, self.browser_description, self.host_name, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_uid() == obj.get_uid()
    def update_uid(self, uid: str):
        self.auth_session_uid = uid
    def update_uid_attributes(self, auth_session_uid: str, auth_session_name: str, tenant_uid: str | None, account_uid: str | None, session_token: str, browser_name: str, browser_description: str, host_name: str):
        self.auth_session_uid = auth_session_uid
        self.auth_session_name = auth_session_name
        self.tenant_uid = tenant_uid
        self.account_uid = account_uid
        self.session_token = session_token
        self.browser_name = browser_name
        self.browser_description = browser_description
        self.host_name = host_name
    def update_attributes(self, auth_session_name: str, tenant_uid: str | None, account_uid: str | None, session_token: str, browser_name: str, browser_description: str, host_name: str):
        self.auth_session_name = auth_session_name
        self.tenant_uid = tenant_uid
        self.account_uid = account_uid
        self.session_token = session_token
        self.browser_name = browser_name
        self.browser_description = browser_description
        self.host_name = host_name


@dataclass(frozen=False)
class auth_sso_write_dto(base_write_dto):
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
    def __init__(self, auth_sso_uid: str, auth_sso_name: str, tenant_uid: str, owner_account_uid: str | None, sso_name: str, sso_url: str, sso_key: str, sso_secret: str, sso_code: str | None, clientid: str | None, clientsecret: str | None, callback_url: str | None, custom_attributes: str = "{}"):
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
        self.custom_attributes = custom_attributes
    @classmethod
    def empty_write(cls):
        return cls("", "", "", "", "", "", "", "", "", "", "", "")
    @classmethod
    def default_write(cls):
        return cls(base_dto.get_random_uid(), "", "", "", "", "", "", "", "", "", "", "")
    @classmethod
    def random_write(cls):
        return cls(base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid())
    @classmethod
    def new_write(cls, auth_sso_uid: str, auth_sso_name: str, tenant_uid: str, owner_account_uid: str | None, sso_name: str, sso_url: str, sso_key: str, sso_secret: str, sso_code: str | None, clientid: str | None, clientsecret: str | None, callback_url: str | None):
        return cls(auth_sso_uid, auth_sso_name, tenant_uid, owner_account_uid, sso_name, sso_url, sso_key, sso_secret, sso_code, clientid, clientsecret, callback_url)
    @classmethod
    def new_write_with_defaults(cls, auth_sso_uid: str = "", auth_sso_name: str = "", tenant_uid: str = "", owner_account_uid: str | None = "", sso_name: str = "", sso_url: str = "", sso_key: str = "", sso_secret: str = "", sso_code: str | None = "", clientid: str | None = "", clientsecret: str | None = "", callback_url: str | None = ""):
        return cls(auth_sso_uid, auth_sso_name, tenant_uid, owner_account_uid, sso_name, sso_url, sso_key, sso_secret, sso_code, clientid, clientsecret, callback_url)
    @classmethod
    def new_write_random_uid(cls, auth_sso_name: str, tenant_uid: str, owner_account_uid: str | None, sso_name: str, sso_url: str, sso_key: str, sso_secret: str, sso_code: str | None, clientid: str | None, clientsecret: str | None, callback_url: str | None):
        return cls(base_dto.get_random_uid(), auth_sso_name, tenant_uid, owner_account_uid, sso_name, sso_url, sso_key, sso_secret, sso_code, clientid, clientsecret, callback_url)
    @classmethod
    def get_class_model(cls) -> base_model:
        return db_models.auth_sso_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["auth_sso_uid"], d["auth_sso_name"], d["tenant_uid"], d["owner_account_uid"], d["sso_name"], d["sso_url"], d["sso_key"], d["sso_secret"], d["sso_code"], d["clientid"], d["clientsecret"], d["callback_url"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return auth_sso_write_dto(self.auth_sso_uid, self.auth_sso_name, self.tenant_uid, self.owner_account_uid, self.sso_name, self.sso_url, self.sso_key, self.sso_secret, self.sso_code, self.clientid, self.clientsecret, self.callback_url, self.custom_attributes)
    def clone_write_new_uid(self):
        return auth_sso_write_dto(base_dto.get_random_uid(), self.auth_sso_name, self.tenant_uid, self.owner_account_uid, self.sso_name, self.sso_url, self.sso_key, self.sso_secret, self.sso_code, self.clientid, self.clientsecret, self.callback_url, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return auth_sso_write_dto(uid, self.auth_sso_name, self.tenant_uid, self.owner_account_uid, self.sso_name, self.sso_url, self.sso_key, self.sso_secret, self.sso_code, self.clientid, self.clientsecret, self.callback_url, self.custom_attributes)
    def get_model(self) -> base_model:
        return db_models.auth_sso_model
    def get_uid(self) -> str:
        return self.auth_sso_uid
    def get_name(self) -> str:
        return self.auth_sso_name
    def get_list_values(self) -> list[any]:
        return [self.auth_sso_uid, self.auth_sso_name, self.tenant_uid, self.owner_account_uid, self.sso_name, self.sso_url, self.sso_key, self.sso_secret, self.sso_code, self.clientid, self.clientsecret, self.callback_url, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.auth_sso_uid, self.auth_sso_name, self.tenant_uid, self.owner_account_uid, self.sso_name, self.sso_url, self.sso_key, self.sso_secret, self.sso_code, self.clientid, self.clientsecret, self.callback_url]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.auth_sso_name, self.tenant_uid, self.owner_account_uid, self.sso_name, self.sso_url, self.sso_key, self.sso_secret, self.sso_code, self.clientid, self.clientsecret, self.callback_url, self.custom_attributes, updated_by, self.auth_sso_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.auth_sso_uid, self.auth_sso_name, self.tenant_uid, self.owner_account_uid, self.sso_name, self.sso_url, self.sso_key, self.sso_secret, self.sso_code, self.clientid, self.clientsecret, self.callback_url, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.auth_sso_name, self.tenant_uid, self.owner_account_uid, self.sso_name, self.sso_url, self.sso_key, self.sso_secret, self.sso_code, self.clientid, self.clientsecret, self.callback_url]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.auth_sso_name, self.tenant_uid, self.owner_account_uid, self.sso_name, self.sso_url, self.sso_key, self.sso_secret, self.sso_code, self.clientid, self.clientsecret, self.callback_url, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_uid() == obj.get_uid()
    def update_uid(self, uid: str):
        self.auth_sso_uid = uid
    def update_uid_attributes(self, auth_sso_uid: str, auth_sso_name: str, tenant_uid: str, owner_account_uid: str | None, sso_name: str, sso_url: str, sso_key: str, sso_secret: str, sso_code: str | None, clientid: str | None, clientsecret: str | None, callback_url: str | None):
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
    def update_attributes(self, auth_sso_name: str, tenant_uid: str, owner_account_uid: str | None, sso_name: str, sso_url: str, sso_key: str, sso_secret: str, sso_code: str | None, clientid: str | None, clientsecret: str | None, callback_url: str | None):
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


@dataclass(frozen=False)
class auth_token_write_dto(base_write_dto):
    auth_token_uid: str
    auth_token_name: str
    auth_attempt_uid: str
    auth_token_type_uid: str
    tenant_uid: str
    account_uid: str
    token_seq: int
    token_hash: str
    token_salt: str
    valid_till_date: datetime.datetime | None
    last_use_date: datetime.datetime | None
    is_last: int
    token_scope: str
    def __init__(self, auth_token_uid: str, auth_token_name: str, auth_attempt_uid: str, auth_token_type_uid: str, tenant_uid: str, account_uid: str, token_seq: int, token_hash: str, token_salt: str, valid_till_date: datetime.datetime | None, last_use_date: datetime.datetime | None, is_last: int, token_scope: str, custom_attributes: str = "{}"):
        self.auth_token_uid = auth_token_uid
        self.auth_token_name = auth_token_name
        self.auth_attempt_uid = auth_attempt_uid
        self.auth_token_type_uid = auth_token_type_uid
        self.tenant_uid = tenant_uid
        self.account_uid = account_uid
        self.token_seq = token_seq
        self.token_hash = token_hash
        self.token_salt = token_salt
        self.valid_till_date = valid_till_date
        self.last_use_date = last_use_date
        self.is_last = is_last
        self.token_scope = token_scope
        self.custom_attributes = custom_attributes
    @classmethod
    def empty_write(cls):
        return cls("", "", "", "", "", "", 0, "", "", datetime.datetime.now(), datetime.datetime.now(), 0, "")
    @classmethod
    def default_write(cls):
        return cls(base_dto.get_random_uid(), "", "", "", "", "", 0, "", "", datetime.datetime.now(), datetime.datetime.now(), 0, "")
    @classmethod
    def random_write(cls):
        return cls(base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), 0, base_dto.get_random_uid(), base_dto.get_random_uid(), datetime.datetime.now(), datetime.datetime.now(), 0, base_dto.get_random_uid())
    @classmethod
    def new_write(cls, auth_token_uid: str, auth_token_name: str, auth_attempt_uid: str, auth_token_type_uid: str, tenant_uid: str, account_uid: str, token_seq: int, token_hash: str, token_salt: str, valid_till_date: datetime.datetime | None, last_use_date: datetime.datetime | None, is_last: int, token_scope: str):
        return cls(auth_token_uid, auth_token_name, auth_attempt_uid, auth_token_type_uid, tenant_uid, account_uid, token_seq, token_hash, token_salt, valid_till_date, last_use_date, is_last, token_scope)
    @classmethod
    def new_write_with_defaults(cls, auth_token_uid: str = "", auth_token_name: str = "", auth_attempt_uid: str = "", auth_token_type_uid: str = "", tenant_uid: str = "", account_uid: str = "", token_seq: int = 0, token_hash: str = "", token_salt: str = "", valid_till_date: datetime.datetime | None = datetime.datetime.now(), last_use_date: datetime.datetime | None = datetime.datetime.now(), is_last: int = 0, token_scope: str = ""):
        return cls(auth_token_uid, auth_token_name, auth_attempt_uid, auth_token_type_uid, tenant_uid, account_uid, token_seq, token_hash, token_salt, valid_till_date, last_use_date, is_last, token_scope)
    @classmethod
    def new_write_random_uid(cls, auth_token_name: str, auth_attempt_uid: str, auth_token_type_uid: str, tenant_uid: str, account_uid: str, token_seq: int, token_hash: str, token_salt: str, valid_till_date: datetime.datetime | None, last_use_date: datetime.datetime | None, is_last: int, token_scope: str):
        return cls(base_dto.get_random_uid(), auth_token_name, auth_attempt_uid, auth_token_type_uid, tenant_uid, account_uid, token_seq, token_hash, token_salt, valid_till_date, last_use_date, is_last, token_scope)
    @classmethod
    def get_class_model(cls) -> base_model:
        return db_models.auth_token_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["auth_token_uid"], d["auth_token_name"], d["auth_attempt_uid"], d["auth_token_type_uid"], d["tenant_uid"], d["account_uid"], d["token_seq"], d["token_hash"], d["token_salt"], d["valid_till_date"], d["last_use_date"], d["is_last"], d["token_scope"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return auth_token_write_dto(self.auth_token_uid, self.auth_token_name, self.auth_attempt_uid, self.auth_token_type_uid, self.tenant_uid, self.account_uid, self.token_seq, self.token_hash, self.token_salt, self.valid_till_date, self.last_use_date, self.is_last, self.token_scope, self.custom_attributes)
    def clone_write_new_uid(self):
        return auth_token_write_dto(base_dto.get_random_uid(), self.auth_token_name, self.auth_attempt_uid, self.auth_token_type_uid, self.tenant_uid, self.account_uid, self.token_seq, self.token_hash, self.token_salt, self.valid_till_date, self.last_use_date, self.is_last, self.token_scope, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return auth_token_write_dto(uid, self.auth_token_name, self.auth_attempt_uid, self.auth_token_type_uid, self.tenant_uid, self.account_uid, self.token_seq, self.token_hash, self.token_salt, self.valid_till_date, self.last_use_date, self.is_last, self.token_scope, self.custom_attributes)
    def get_model(self) -> base_model:
        return db_models.auth_token_model
    def get_uid(self) -> str:
        return self.auth_token_uid
    def get_name(self) -> str:
        return self.auth_token_name
    def get_list_values(self) -> list[any]:
        return [self.auth_token_uid, self.auth_token_name, self.auth_attempt_uid, self.auth_token_type_uid, self.tenant_uid, self.account_uid, self.token_seq, self.token_hash, self.token_salt, self.valid_till_date, self.last_use_date, self.is_last, self.token_scope, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.auth_token_uid, self.auth_token_name, self.auth_attempt_uid, self.auth_token_type_uid, self.tenant_uid, self.account_uid, self.token_seq, self.token_hash, self.token_salt, self.valid_till_date, self.last_use_date, self.is_last, self.token_scope]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.auth_token_name, self.auth_attempt_uid, self.auth_token_type_uid, self.tenant_uid, self.account_uid, self.token_seq, self.token_hash, self.token_salt, self.valid_till_date, self.last_use_date, self.is_last, self.token_scope, self.custom_attributes, updated_by, self.auth_token_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.auth_token_uid, self.auth_token_name, self.auth_attempt_uid, self.auth_token_type_uid, self.tenant_uid, self.account_uid, self.token_seq, self.token_hash, self.token_salt, self.valid_till_date, self.last_use_date, self.is_last, self.token_scope, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.auth_token_name, self.auth_attempt_uid, self.auth_token_type_uid, self.tenant_uid, self.account_uid, self.token_seq, self.token_hash, self.token_salt, self.valid_till_date, self.last_use_date, self.is_last, self.token_scope]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.auth_token_name, self.auth_attempt_uid, self.auth_token_type_uid, self.tenant_uid, self.account_uid, self.token_seq, self.token_hash, self.token_salt, self.valid_till_date, self.last_use_date, self.is_last, self.token_scope, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_uid() == obj.get_uid()
    def update_uid(self, uid: str):
        self.auth_token_uid = uid
    def update_uid_attributes(self, auth_token_uid: str, auth_token_name: str, auth_attempt_uid: str, auth_token_type_uid: str, tenant_uid: str, account_uid: str, token_seq: int, token_hash: str, token_salt: str, valid_till_date: datetime.datetime | None, last_use_date: datetime.datetime | None, is_last: int, token_scope: str):
        self.auth_token_uid = auth_token_uid
        self.auth_token_name = auth_token_name
        self.auth_attempt_uid = auth_attempt_uid
        self.auth_token_type_uid = auth_token_type_uid
        self.tenant_uid = tenant_uid
        self.account_uid = account_uid
        self.token_seq = token_seq
        self.token_hash = token_hash
        self.token_salt = token_salt
        self.valid_till_date = valid_till_date
        self.last_use_date = last_use_date
        self.is_last = is_last
        self.token_scope = token_scope
    def update_attributes(self, auth_token_name: str, auth_attempt_uid: str, auth_token_type_uid: str, tenant_uid: str, account_uid: str, token_seq: int, token_hash: str, token_salt: str, valid_till_date: datetime.datetime | None, last_use_date: datetime.datetime | None, is_last: int, token_scope: str):
        self.auth_token_name = auth_token_name
        self.auth_attempt_uid = auth_attempt_uid
        self.auth_token_type_uid = auth_token_type_uid
        self.tenant_uid = tenant_uid
        self.account_uid = account_uid
        self.token_seq = token_seq
        self.token_hash = token_hash
        self.token_salt = token_salt
        self.valid_till_date = valid_till_date
        self.last_use_date = last_use_date
        self.is_last = is_last
        self.token_scope = token_scope


@dataclass(frozen=False)
class auth_token_type_write_dto(base_write_dto):
    auth_token_type_uid: str
    auth_token_type_name: str
    def __init__(self, auth_token_type_uid: str, auth_token_type_name: str, custom_attributes: str = "{}"):
        self.auth_token_type_uid = auth_token_type_uid
        self.auth_token_type_name = auth_token_type_name
        self.custom_attributes = custom_attributes
    @classmethod
    def empty_write(cls):
        return cls("", "")
    @classmethod
    def default_write(cls):
        return cls(base_dto.get_random_uid(), "")
    @classmethod
    def random_write(cls):
        return cls(base_dto.get_random_uid(), base_dto.get_random_uid())
    @classmethod
    def new_write(cls, auth_token_type_uid: str, auth_token_type_name: str):
        return cls(auth_token_type_uid, auth_token_type_name)
    @classmethod
    def new_write_with_defaults(cls, auth_token_type_uid: str = "", auth_token_type_name: str = ""):
        return cls(auth_token_type_uid, auth_token_type_name)
    @classmethod
    def new_write_random_uid(cls, auth_token_type_name: str):
        return cls(base_dto.get_random_uid(), auth_token_type_name)
    @classmethod
    def get_class_model(cls) -> base_model:
        return db_models.auth_token_type_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["auth_token_type_uid"], d["auth_token_type_name"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return auth_token_type_write_dto(self.auth_token_type_uid, self.auth_token_type_name, self.custom_attributes)
    def clone_write_new_uid(self):
        return auth_token_type_write_dto(base_dto.get_random_uid(), self.auth_token_type_name, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return auth_token_type_write_dto(uid, self.auth_token_type_name, self.custom_attributes)
    def get_model(self) -> base_model:
        return db_models.auth_token_type_model
    def get_uid(self) -> str:
        return self.auth_token_type_uid
    def get_name(self) -> str:
        return self.auth_token_type_name
    def get_list_values(self) -> list[any]:
        return [self.auth_token_type_uid, self.auth_token_type_name, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.auth_token_type_uid, self.auth_token_type_name]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.auth_token_type_name, self.custom_attributes, updated_by, self.auth_token_type_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.auth_token_type_uid, self.auth_token_type_name, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.auth_token_type_name]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.auth_token_type_name, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_uid() == obj.get_uid()
    def update_uid(self, uid: str):
        self.auth_token_type_uid = uid
    def update_uid_attributes(self, auth_token_type_uid: str, auth_token_type_name: str):
        self.auth_token_type_uid = auth_token_type_uid
        self.auth_token_type_name = auth_token_type_name
    def update_attributes(self, auth_token_type_name: str):
        self.auth_token_type_name = auth_token_type_name


@dataclass(frozen=False)
class calendar_account_write_dto(base_write_dto):
    calendar_account_uid: str
    calendar_account_name: str
    tenant_uid: str
    account_uid: str
    calendar_type_uid: str
    def __init__(self, calendar_account_uid: str, calendar_account_name: str, tenant_uid: str, account_uid: str, calendar_type_uid: str, custom_attributes: str = "{}"):
        self.calendar_account_uid = calendar_account_uid
        self.calendar_account_name = calendar_account_name
        self.tenant_uid = tenant_uid
        self.account_uid = account_uid
        self.calendar_type_uid = calendar_type_uid
        self.custom_attributes = custom_attributes
    @classmethod
    def empty_write(cls):
        return cls("", "", "", "", "")
    @classmethod
    def default_write(cls):
        return cls(base_dto.get_random_uid(), "", "", "", "")
    @classmethod
    def random_write(cls):
        return cls(base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid())
    @classmethod
    def new_write(cls, calendar_account_uid: str, calendar_account_name: str, tenant_uid: str, account_uid: str, calendar_type_uid: str):
        return cls(calendar_account_uid, calendar_account_name, tenant_uid, account_uid, calendar_type_uid)
    @classmethod
    def new_write_with_defaults(cls, calendar_account_uid: str = "", calendar_account_name: str = "", tenant_uid: str = "", account_uid: str = "", calendar_type_uid: str = ""):
        return cls(calendar_account_uid, calendar_account_name, tenant_uid, account_uid, calendar_type_uid)
    @classmethod
    def new_write_random_uid(cls, calendar_account_name: str, tenant_uid: str, account_uid: str, calendar_type_uid: str):
        return cls(base_dto.get_random_uid(), calendar_account_name, tenant_uid, account_uid, calendar_type_uid)
    @classmethod
    def get_class_model(cls) -> base_model:
        return db_models.calendar_account_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["calendar_account_uid"], d["calendar_account_name"], d["tenant_uid"], d["account_uid"], d["calendar_type_uid"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return calendar_account_write_dto(self.calendar_account_uid, self.calendar_account_name, self.tenant_uid, self.account_uid, self.calendar_type_uid, self.custom_attributes)
    def clone_write_new_uid(self):
        return calendar_account_write_dto(base_dto.get_random_uid(), self.calendar_account_name, self.tenant_uid, self.account_uid, self.calendar_type_uid, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return calendar_account_write_dto(uid, self.calendar_account_name, self.tenant_uid, self.account_uid, self.calendar_type_uid, self.custom_attributes)
    def get_model(self) -> base_model:
        return db_models.calendar_account_model
    def get_uid(self) -> str:
        return self.calendar_account_uid
    def get_name(self) -> str:
        return self.calendar_account_name
    def get_list_values(self) -> list[any]:
        return [self.calendar_account_uid, self.calendar_account_name, self.tenant_uid, self.account_uid, self.calendar_type_uid, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.calendar_account_uid, self.calendar_account_name, self.tenant_uid, self.account_uid, self.calendar_type_uid]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.calendar_account_name, self.tenant_uid, self.account_uid, self.calendar_type_uid, self.custom_attributes, updated_by, self.calendar_account_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.calendar_account_uid, self.calendar_account_name, self.tenant_uid, self.account_uid, self.calendar_type_uid, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.calendar_account_name, self.tenant_uid, self.account_uid, self.calendar_type_uid]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.calendar_account_name, self.tenant_uid, self.account_uid, self.calendar_type_uid, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_uid() == obj.get_uid()
    def update_uid(self, uid: str):
        self.calendar_account_uid = uid
    def update_uid_attributes(self, calendar_account_uid: str, calendar_account_name: str, tenant_uid: str, account_uid: str, calendar_type_uid: str):
        self.calendar_account_uid = calendar_account_uid
        self.calendar_account_name = calendar_account_name
        self.tenant_uid = tenant_uid
        self.account_uid = account_uid
        self.calendar_type_uid = calendar_type_uid
    def update_attributes(self, calendar_account_name: str, tenant_uid: str, account_uid: str, calendar_type_uid: str):
        self.calendar_account_name = calendar_account_name
        self.tenant_uid = tenant_uid
        self.account_uid = account_uid
        self.calendar_type_uid = calendar_type_uid


@dataclass(frozen=False)
class calendar_approval_write_dto(base_write_dto):
    calendar_approval_uid: str
    calendar_approval_name: str
    client_uid: str
    account_uid: str
    calendar_approval_type_uid: str
    calendar_event_group_uid: str
    calendar_type_uid: str
    time_submit_type_name: str
    def __init__(self, calendar_approval_uid: str, calendar_approval_name: str, client_uid: str, account_uid: str, calendar_approval_type_uid: str, calendar_event_group_uid: str, calendar_type_uid: str, time_submit_type_name: str, custom_attributes: str = "{}"):
        self.calendar_approval_uid = calendar_approval_uid
        self.calendar_approval_name = calendar_approval_name
        self.client_uid = client_uid
        self.account_uid = account_uid
        self.calendar_approval_type_uid = calendar_approval_type_uid
        self.calendar_event_group_uid = calendar_event_group_uid
        self.calendar_type_uid = calendar_type_uid
        self.time_submit_type_name = time_submit_type_name
        self.custom_attributes = custom_attributes
    @classmethod
    def empty_write(cls):
        return cls("", "", "", "", "", "", "", "")
    @classmethod
    def default_write(cls):
        return cls(base_dto.get_random_uid(), "", "", "", "", "", "", "")
    @classmethod
    def random_write(cls):
        return cls(base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid())
    @classmethod
    def new_write(cls, calendar_approval_uid: str, calendar_approval_name: str, client_uid: str, account_uid: str, calendar_approval_type_uid: str, calendar_event_group_uid: str, calendar_type_uid: str, time_submit_type_name: str):
        return cls(calendar_approval_uid, calendar_approval_name, client_uid, account_uid, calendar_approval_type_uid, calendar_event_group_uid, calendar_type_uid, time_submit_type_name)
    @classmethod
    def new_write_with_defaults(cls, calendar_approval_uid: str = "", calendar_approval_name: str = "", client_uid: str = "", account_uid: str = "", calendar_approval_type_uid: str = "", calendar_event_group_uid: str = "", calendar_type_uid: str = "", time_submit_type_name: str = ""):
        return cls(calendar_approval_uid, calendar_approval_name, client_uid, account_uid, calendar_approval_type_uid, calendar_event_group_uid, calendar_type_uid, time_submit_type_name)
    @classmethod
    def new_write_random_uid(cls, calendar_approval_name: str, client_uid: str, account_uid: str, calendar_approval_type_uid: str, calendar_event_group_uid: str, calendar_type_uid: str, time_submit_type_name: str):
        return cls(base_dto.get_random_uid(), calendar_approval_name, client_uid, account_uid, calendar_approval_type_uid, calendar_event_group_uid, calendar_type_uid, time_submit_type_name)
    @classmethod
    def get_class_model(cls) -> base_model:
        return db_models.calendar_approval_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["calendar_approval_uid"], d["calendar_approval_name"], d["client_uid"], d["account_uid"], d["calendar_approval_type_uid"], d["calendar_event_group_uid"], d["calendar_type_uid"], d["time_submit_type_name"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return calendar_approval_write_dto(self.calendar_approval_uid, self.calendar_approval_name, self.client_uid, self.account_uid, self.calendar_approval_type_uid, self.calendar_event_group_uid, self.calendar_type_uid, self.time_submit_type_name, self.custom_attributes)
    def clone_write_new_uid(self):
        return calendar_approval_write_dto(base_dto.get_random_uid(), self.calendar_approval_name, self.client_uid, self.account_uid, self.calendar_approval_type_uid, self.calendar_event_group_uid, self.calendar_type_uid, self.time_submit_type_name, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return calendar_approval_write_dto(uid, self.calendar_approval_name, self.client_uid, self.account_uid, self.calendar_approval_type_uid, self.calendar_event_group_uid, self.calendar_type_uid, self.time_submit_type_name, self.custom_attributes)
    def get_model(self) -> base_model:
        return db_models.calendar_approval_model
    def get_uid(self) -> str:
        return self.calendar_approval_uid
    def get_name(self) -> str:
        return self.calendar_approval_name
    def get_list_values(self) -> list[any]:
        return [self.calendar_approval_uid, self.calendar_approval_name, self.client_uid, self.account_uid, self.calendar_approval_type_uid, self.calendar_event_group_uid, self.calendar_type_uid, self.time_submit_type_name, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.calendar_approval_uid, self.calendar_approval_name, self.client_uid, self.account_uid, self.calendar_approval_type_uid, self.calendar_event_group_uid, self.calendar_type_uid, self.time_submit_type_name]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.calendar_approval_name, self.client_uid, self.account_uid, self.calendar_approval_type_uid, self.calendar_event_group_uid, self.calendar_type_uid, self.time_submit_type_name, self.custom_attributes, updated_by, self.calendar_approval_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.calendar_approval_uid, self.calendar_approval_name, self.client_uid, self.account_uid, self.calendar_approval_type_uid, self.calendar_event_group_uid, self.calendar_type_uid, self.time_submit_type_name, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.calendar_approval_name, self.client_uid, self.account_uid, self.calendar_approval_type_uid, self.calendar_event_group_uid, self.calendar_type_uid, self.time_submit_type_name]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.calendar_approval_name, self.client_uid, self.account_uid, self.calendar_approval_type_uid, self.calendar_event_group_uid, self.calendar_type_uid, self.time_submit_type_name, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_uid() == obj.get_uid()
    def update_uid(self, uid: str):
        self.calendar_approval_uid = uid
    def update_uid_attributes(self, calendar_approval_uid: str, calendar_approval_name: str, client_uid: str, account_uid: str, calendar_approval_type_uid: str, calendar_event_group_uid: str, calendar_type_uid: str, time_submit_type_name: str):
        self.calendar_approval_uid = calendar_approval_uid
        self.calendar_approval_name = calendar_approval_name
        self.client_uid = client_uid
        self.account_uid = account_uid
        self.calendar_approval_type_uid = calendar_approval_type_uid
        self.calendar_event_group_uid = calendar_event_group_uid
        self.calendar_type_uid = calendar_type_uid
        self.time_submit_type_name = time_submit_type_name
    def update_attributes(self, calendar_approval_name: str, client_uid: str, account_uid: str, calendar_approval_type_uid: str, calendar_event_group_uid: str, calendar_type_uid: str, time_submit_type_name: str):
        self.calendar_approval_name = calendar_approval_name
        self.client_uid = client_uid
        self.account_uid = account_uid
        self.calendar_approval_type_uid = calendar_approval_type_uid
        self.calendar_event_group_uid = calendar_event_group_uid
        self.calendar_type_uid = calendar_type_uid
        self.time_submit_type_name = time_submit_type_name


@dataclass(frozen=False)
class calendar_approval_type_write_dto(base_write_dto):
    calendar_approval_type_uid: str
    calendar_approval_type_name: str
    def __init__(self, calendar_approval_type_uid: str, calendar_approval_type_name: str, custom_attributes: str = "{}"):
        self.calendar_approval_type_uid = calendar_approval_type_uid
        self.calendar_approval_type_name = calendar_approval_type_name
        self.custom_attributes = custom_attributes
    @classmethod
    def empty_write(cls):
        return cls("", "")
    @classmethod
    def default_write(cls):
        return cls(base_dto.get_random_uid(), "")
    @classmethod
    def random_write(cls):
        return cls(base_dto.get_random_uid(), base_dto.get_random_uid())
    @classmethod
    def new_write(cls, calendar_approval_type_uid: str, calendar_approval_type_name: str):
        return cls(calendar_approval_type_uid, calendar_approval_type_name)
    @classmethod
    def new_write_with_defaults(cls, calendar_approval_type_uid: str = "", calendar_approval_type_name: str = ""):
        return cls(calendar_approval_type_uid, calendar_approval_type_name)
    @classmethod
    def new_write_random_uid(cls, calendar_approval_type_name: str):
        return cls(base_dto.get_random_uid(), calendar_approval_type_name)
    @classmethod
    def get_class_model(cls) -> base_model:
        return db_models.calendar_approval_type_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["calendar_approval_type_uid"], d["calendar_approval_type_name"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return calendar_approval_type_write_dto(self.calendar_approval_type_uid, self.calendar_approval_type_name, self.custom_attributes)
    def clone_write_new_uid(self):
        return calendar_approval_type_write_dto(base_dto.get_random_uid(), self.calendar_approval_type_name, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return calendar_approval_type_write_dto(uid, self.calendar_approval_type_name, self.custom_attributes)
    def get_model(self) -> base_model:
        return db_models.calendar_approval_type_model
    def get_uid(self) -> str:
        return self.calendar_approval_type_uid
    def get_name(self) -> str:
        return self.calendar_approval_type_name
    def get_list_values(self) -> list[any]:
        return [self.calendar_approval_type_uid, self.calendar_approval_type_name, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.calendar_approval_type_uid, self.calendar_approval_type_name]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.calendar_approval_type_name, self.custom_attributes, updated_by, self.calendar_approval_type_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.calendar_approval_type_uid, self.calendar_approval_type_name, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.calendar_approval_type_name]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.calendar_approval_type_name, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_uid() == obj.get_uid()
    def update_uid(self, uid: str):
        self.calendar_approval_type_uid = uid
    def update_uid_attributes(self, calendar_approval_type_uid: str, calendar_approval_type_name: str):
        self.calendar_approval_type_uid = calendar_approval_type_uid
        self.calendar_approval_type_name = calendar_approval_type_name
    def update_attributes(self, calendar_approval_type_name: str):
        self.calendar_approval_type_name = calendar_approval_type_name


@dataclass(frozen=False)
class calendar_event_write_dto(base_write_dto):
    calendar_event_uid: str
    calendar_event_name: str
    client_uid: str
    account_uid: str
    calendar_event_group_uid: str
    calendar_type_uid: str
    def __init__(self, calendar_event_uid: str, calendar_event_name: str, client_uid: str, account_uid: str, calendar_event_group_uid: str, calendar_type_uid: str, custom_attributes: str = "{}"):
        self.calendar_event_uid = calendar_event_uid
        self.calendar_event_name = calendar_event_name
        self.client_uid = client_uid
        self.account_uid = account_uid
        self.calendar_event_group_uid = calendar_event_group_uid
        self.calendar_type_uid = calendar_type_uid
        self.custom_attributes = custom_attributes
    @classmethod
    def empty_write(cls):
        return cls("", "", "", "", "", "")
    @classmethod
    def default_write(cls):
        return cls(base_dto.get_random_uid(), "", "", "", "", "")
    @classmethod
    def random_write(cls):
        return cls(base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid())
    @classmethod
    def new_write(cls, calendar_event_uid: str, calendar_event_name: str, client_uid: str, account_uid: str, calendar_event_group_uid: str, calendar_type_uid: str):
        return cls(calendar_event_uid, calendar_event_name, client_uid, account_uid, calendar_event_group_uid, calendar_type_uid)
    @classmethod
    def new_write_with_defaults(cls, calendar_event_uid: str = "", calendar_event_name: str = "", client_uid: str = "", account_uid: str = "", calendar_event_group_uid: str = "", calendar_type_uid: str = ""):
        return cls(calendar_event_uid, calendar_event_name, client_uid, account_uid, calendar_event_group_uid, calendar_type_uid)
    @classmethod
    def new_write_random_uid(cls, calendar_event_name: str, client_uid: str, account_uid: str, calendar_event_group_uid: str, calendar_type_uid: str):
        return cls(base_dto.get_random_uid(), calendar_event_name, client_uid, account_uid, calendar_event_group_uid, calendar_type_uid)
    @classmethod
    def get_class_model(cls) -> base_model:
        return db_models.calendar_event_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["calendar_event_uid"], d["calendar_event_name"], d["client_uid"], d["account_uid"], d["calendar_event_group_uid"], d["calendar_type_uid"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return calendar_event_write_dto(self.calendar_event_uid, self.calendar_event_name, self.client_uid, self.account_uid, self.calendar_event_group_uid, self.calendar_type_uid, self.custom_attributes)
    def clone_write_new_uid(self):
        return calendar_event_write_dto(base_dto.get_random_uid(), self.calendar_event_name, self.client_uid, self.account_uid, self.calendar_event_group_uid, self.calendar_type_uid, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return calendar_event_write_dto(uid, self.calendar_event_name, self.client_uid, self.account_uid, self.calendar_event_group_uid, self.calendar_type_uid, self.custom_attributes)
    def get_model(self) -> base_model:
        return db_models.calendar_event_model
    def get_uid(self) -> str:
        return self.calendar_event_uid
    def get_name(self) -> str:
        return self.calendar_event_name
    def get_list_values(self) -> list[any]:
        return [self.calendar_event_uid, self.calendar_event_name, self.client_uid, self.account_uid, self.calendar_event_group_uid, self.calendar_type_uid, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.calendar_event_uid, self.calendar_event_name, self.client_uid, self.account_uid, self.calendar_event_group_uid, self.calendar_type_uid]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.calendar_event_name, self.client_uid, self.account_uid, self.calendar_event_group_uid, self.calendar_type_uid, self.custom_attributes, updated_by, self.calendar_event_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.calendar_event_uid, self.calendar_event_name, self.client_uid, self.account_uid, self.calendar_event_group_uid, self.calendar_type_uid, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.calendar_event_name, self.client_uid, self.account_uid, self.calendar_event_group_uid, self.calendar_type_uid]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.calendar_event_name, self.client_uid, self.account_uid, self.calendar_event_group_uid, self.calendar_type_uid, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_uid() == obj.get_uid()
    def update_uid(self, uid: str):
        self.calendar_event_uid = uid
    def update_uid_attributes(self, calendar_event_uid: str, calendar_event_name: str, client_uid: str, account_uid: str, calendar_event_group_uid: str, calendar_type_uid: str):
        self.calendar_event_uid = calendar_event_uid
        self.calendar_event_name = calendar_event_name
        self.client_uid = client_uid
        self.account_uid = account_uid
        self.calendar_event_group_uid = calendar_event_group_uid
        self.calendar_type_uid = calendar_type_uid
    def update_attributes(self, calendar_event_name: str, client_uid: str, account_uid: str, calendar_event_group_uid: str, calendar_type_uid: str):
        self.calendar_event_name = calendar_event_name
        self.client_uid = client_uid
        self.account_uid = account_uid
        self.calendar_event_group_uid = calendar_event_group_uid
        self.calendar_type_uid = calendar_type_uid


@dataclass(frozen=False)
class calendar_event_group_write_dto(base_write_dto):
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
    def __init__(self, calendar_event_group_uid: str, calendar_event_group_name: str, client_uid: str, account_uid: str, calendar_account_uid: str, calendar_event_type_uid: str, group_comment: str, event_start_date: datetime.datetime, event_end_date: datetime.datetime, is_approved: int, custom_attributes: str = "{}"):
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
        self.custom_attributes = custom_attributes
    @classmethod
    def empty_write(cls):
        return cls("", "", "", "", "", "", "", datetime.datetime.now(), datetime.datetime.now(), 0)
    @classmethod
    def default_write(cls):
        return cls(base_dto.get_random_uid(), "", "", "", "", "", "", datetime.datetime.now(), datetime.datetime.now(), 0)
    @classmethod
    def random_write(cls):
        return cls(base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), datetime.datetime.now(), datetime.datetime.now(), 0)
    @classmethod
    def new_write(cls, calendar_event_group_uid: str, calendar_event_group_name: str, client_uid: str, account_uid: str, calendar_account_uid: str, calendar_event_type_uid: str, group_comment: str, event_start_date: datetime.datetime, event_end_date: datetime.datetime, is_approved: int):
        return cls(calendar_event_group_uid, calendar_event_group_name, client_uid, account_uid, calendar_account_uid, calendar_event_type_uid, group_comment, event_start_date, event_end_date, is_approved)
    @classmethod
    def new_write_with_defaults(cls, calendar_event_group_uid: str = "", calendar_event_group_name: str = "", client_uid: str = "", account_uid: str = "", calendar_account_uid: str = "", calendar_event_type_uid: str = "", group_comment: str = "", event_start_date: datetime.datetime = datetime.datetime.now(), event_end_date: datetime.datetime = datetime.datetime.now(), is_approved: int = 0):
        return cls(calendar_event_group_uid, calendar_event_group_name, client_uid, account_uid, calendar_account_uid, calendar_event_type_uid, group_comment, event_start_date, event_end_date, is_approved)
    @classmethod
    def new_write_random_uid(cls, calendar_event_group_name: str, client_uid: str, account_uid: str, calendar_account_uid: str, calendar_event_type_uid: str, group_comment: str, event_start_date: datetime.datetime, event_end_date: datetime.datetime, is_approved: int):
        return cls(base_dto.get_random_uid(), calendar_event_group_name, client_uid, account_uid, calendar_account_uid, calendar_event_type_uid, group_comment, event_start_date, event_end_date, is_approved)
    @classmethod
    def get_class_model(cls) -> base_model:
        return db_models.calendar_event_group_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["calendar_event_group_uid"], d["calendar_event_group_name"], d["client_uid"], d["account_uid"], d["calendar_account_uid"], d["calendar_event_type_uid"], d["group_comment"], d["event_start_date"], d["event_end_date"], d["is_approved"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return calendar_event_group_write_dto(self.calendar_event_group_uid, self.calendar_event_group_name, self.client_uid, self.account_uid, self.calendar_account_uid, self.calendar_event_type_uid, self.group_comment, self.event_start_date, self.event_end_date, self.is_approved, self.custom_attributes)
    def clone_write_new_uid(self):
        return calendar_event_group_write_dto(base_dto.get_random_uid(), self.calendar_event_group_name, self.client_uid, self.account_uid, self.calendar_account_uid, self.calendar_event_type_uid, self.group_comment, self.event_start_date, self.event_end_date, self.is_approved, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return calendar_event_group_write_dto(uid, self.calendar_event_group_name, self.client_uid, self.account_uid, self.calendar_account_uid, self.calendar_event_type_uid, self.group_comment, self.event_start_date, self.event_end_date, self.is_approved, self.custom_attributes)
    def get_model(self) -> base_model:
        return db_models.calendar_event_group_model
    def get_uid(self) -> str:
        return self.calendar_event_group_uid
    def get_name(self) -> str:
        return self.calendar_event_group_name
    def get_list_values(self) -> list[any]:
        return [self.calendar_event_group_uid, self.calendar_event_group_name, self.client_uid, self.account_uid, self.calendar_account_uid, self.calendar_event_type_uid, self.group_comment, self.event_start_date, self.event_end_date, self.is_approved, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.calendar_event_group_uid, self.calendar_event_group_name, self.client_uid, self.account_uid, self.calendar_account_uid, self.calendar_event_type_uid, self.group_comment, self.event_start_date, self.event_end_date, self.is_approved]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.calendar_event_group_name, self.client_uid, self.account_uid, self.calendar_account_uid, self.calendar_event_type_uid, self.group_comment, self.event_start_date, self.event_end_date, self.is_approved, self.custom_attributes, updated_by, self.calendar_event_group_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.calendar_event_group_uid, self.calendar_event_group_name, self.client_uid, self.account_uid, self.calendar_account_uid, self.calendar_event_type_uid, self.group_comment, self.event_start_date, self.event_end_date, self.is_approved, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.calendar_event_group_name, self.client_uid, self.account_uid, self.calendar_account_uid, self.calendar_event_type_uid, self.group_comment, self.event_start_date, self.event_end_date, self.is_approved]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.calendar_event_group_name, self.client_uid, self.account_uid, self.calendar_account_uid, self.calendar_event_type_uid, self.group_comment, self.event_start_date, self.event_end_date, self.is_approved, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_uid() == obj.get_uid()
    def update_uid(self, uid: str):
        self.calendar_event_group_uid = uid
    def update_uid_attributes(self, calendar_event_group_uid: str, calendar_event_group_name: str, client_uid: str, account_uid: str, calendar_account_uid: str, calendar_event_type_uid: str, group_comment: str, event_start_date: datetime.datetime, event_end_date: datetime.datetime, is_approved: int):
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
    def update_attributes(self, calendar_event_group_name: str, client_uid: str, account_uid: str, calendar_account_uid: str, calendar_event_type_uid: str, group_comment: str, event_start_date: datetime.datetime, event_end_date: datetime.datetime, is_approved: int):
        self.calendar_event_group_name = calendar_event_group_name
        self.client_uid = client_uid
        self.account_uid = account_uid
        self.calendar_account_uid = calendar_account_uid
        self.calendar_event_type_uid = calendar_event_type_uid
        self.group_comment = group_comment
        self.event_start_date = event_start_date
        self.event_end_date = event_end_date
        self.is_approved = is_approved


@dataclass(frozen=False)
class calendar_event_type_write_dto(base_write_dto):
    calendar_event_type_uid: str
    calendar_event_type_name: str
    client_uid: str
    calendar_type_uid: str
    auto_approved: int
    def __init__(self, calendar_event_type_uid: str, calendar_event_type_name: str, client_uid: str, calendar_type_uid: str, auto_approved: int, custom_attributes: str = "{}"):
        self.calendar_event_type_uid = calendar_event_type_uid
        self.calendar_event_type_name = calendar_event_type_name
        self.client_uid = client_uid
        self.calendar_type_uid = calendar_type_uid
        self.auto_approved = auto_approved
        self.custom_attributes = custom_attributes
    @classmethod
    def empty_write(cls):
        return cls("", "", "", "", 0)
    @classmethod
    def default_write(cls):
        return cls(base_dto.get_random_uid(), "", "", "", 0)
    @classmethod
    def random_write(cls):
        return cls(base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), 0)
    @classmethod
    def new_write(cls, calendar_event_type_uid: str, calendar_event_type_name: str, client_uid: str, calendar_type_uid: str, auto_approved: int):
        return cls(calendar_event_type_uid, calendar_event_type_name, client_uid, calendar_type_uid, auto_approved)
    @classmethod
    def new_write_with_defaults(cls, calendar_event_type_uid: str = "", calendar_event_type_name: str = "", client_uid: str = "", calendar_type_uid: str = "", auto_approved: int = 0):
        return cls(calendar_event_type_uid, calendar_event_type_name, client_uid, calendar_type_uid, auto_approved)
    @classmethod
    def new_write_random_uid(cls, calendar_event_type_name: str, client_uid: str, calendar_type_uid: str, auto_approved: int):
        return cls(base_dto.get_random_uid(), calendar_event_type_name, client_uid, calendar_type_uid, auto_approved)
    @classmethod
    def get_class_model(cls) -> base_model:
        return db_models.calendar_event_type_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["calendar_event_type_uid"], d["calendar_event_type_name"], d["client_uid"], d["calendar_type_uid"], d["auto_approved"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return calendar_event_type_write_dto(self.calendar_event_type_uid, self.calendar_event_type_name, self.client_uid, self.calendar_type_uid, self.auto_approved, self.custom_attributes)
    def clone_write_new_uid(self):
        return calendar_event_type_write_dto(base_dto.get_random_uid(), self.calendar_event_type_name, self.client_uid, self.calendar_type_uid, self.auto_approved, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return calendar_event_type_write_dto(uid, self.calendar_event_type_name, self.client_uid, self.calendar_type_uid, self.auto_approved, self.custom_attributes)
    def get_model(self) -> base_model:
        return db_models.calendar_event_type_model
    def get_uid(self) -> str:
        return self.calendar_event_type_uid
    def get_name(self) -> str:
        return self.calendar_event_type_name
    def get_list_values(self) -> list[any]:
        return [self.calendar_event_type_uid, self.calendar_event_type_name, self.client_uid, self.calendar_type_uid, self.auto_approved, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.calendar_event_type_uid, self.calendar_event_type_name, self.client_uid, self.calendar_type_uid, self.auto_approved]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.calendar_event_type_name, self.client_uid, self.calendar_type_uid, self.auto_approved, self.custom_attributes, updated_by, self.calendar_event_type_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.calendar_event_type_uid, self.calendar_event_type_name, self.client_uid, self.calendar_type_uid, self.auto_approved, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.calendar_event_type_name, self.client_uid, self.calendar_type_uid, self.auto_approved]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.calendar_event_type_name, self.client_uid, self.calendar_type_uid, self.auto_approved, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_uid() == obj.get_uid()
    def update_uid(self, uid: str):
        self.calendar_event_type_uid = uid
    def update_uid_attributes(self, calendar_event_type_uid: str, calendar_event_type_name: str, client_uid: str, calendar_type_uid: str, auto_approved: int):
        self.calendar_event_type_uid = calendar_event_type_uid
        self.calendar_event_type_name = calendar_event_type_name
        self.client_uid = client_uid
        self.calendar_type_uid = calendar_type_uid
        self.auto_approved = auto_approved
    def update_attributes(self, calendar_event_type_name: str, client_uid: str, calendar_type_uid: str, auto_approved: int):
        self.calendar_event_type_name = calendar_event_type_name
        self.client_uid = client_uid
        self.calendar_type_uid = calendar_type_uid
        self.auto_approved = auto_approved


@dataclass(frozen=False)
class calendar_type_write_dto(base_write_dto):
    calendar_type_uid: str
    calendar_type_name: str
    def __init__(self, calendar_type_uid: str, calendar_type_name: str, custom_attributes: str = "{}"):
        self.calendar_type_uid = calendar_type_uid
        self.calendar_type_name = calendar_type_name
        self.custom_attributes = custom_attributes
    @classmethod
    def empty_write(cls):
        return cls("", "")
    @classmethod
    def default_write(cls):
        return cls(base_dto.get_random_uid(), "")
    @classmethod
    def random_write(cls):
        return cls(base_dto.get_random_uid(), base_dto.get_random_uid())
    @classmethod
    def new_write(cls, calendar_type_uid: str, calendar_type_name: str):
        return cls(calendar_type_uid, calendar_type_name)
    @classmethod
    def new_write_with_defaults(cls, calendar_type_uid: str = "", calendar_type_name: str = ""):
        return cls(calendar_type_uid, calendar_type_name)
    @classmethod
    def new_write_random_uid(cls, calendar_type_name: str):
        return cls(base_dto.get_random_uid(), calendar_type_name)
    @classmethod
    def get_class_model(cls) -> base_model:
        return db_models.calendar_type_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["calendar_type_uid"], d["calendar_type_name"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return calendar_type_write_dto(self.calendar_type_uid, self.calendar_type_name, self.custom_attributes)
    def clone_write_new_uid(self):
        return calendar_type_write_dto(base_dto.get_random_uid(), self.calendar_type_name, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return calendar_type_write_dto(uid, self.calendar_type_name, self.custom_attributes)
    def get_model(self) -> base_model:
        return db_models.calendar_type_model
    def get_uid(self) -> str:
        return self.calendar_type_uid
    def get_name(self) -> str:
        return self.calendar_type_name
    def get_list_values(self) -> list[any]:
        return [self.calendar_type_uid, self.calendar_type_name, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.calendar_type_uid, self.calendar_type_name]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.calendar_type_name, self.custom_attributes, updated_by, self.calendar_type_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.calendar_type_uid, self.calendar_type_name, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.calendar_type_name]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.calendar_type_name, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_uid() == obj.get_uid()
    def update_uid(self, uid: str):
        self.calendar_type_uid = uid
    def update_uid_attributes(self, calendar_type_uid: str, calendar_type_name: str):
        self.calendar_type_uid = calendar_type_uid
        self.calendar_type_name = calendar_type_name
    def update_attributes(self, calendar_type_name: str):
        self.calendar_type_name = calendar_type_name


@dataclass(frozen=False)
class client_write_dto(base_write_dto):
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
    def __init__(self, client_uid: str, client_name: str, tenant_uid: str, country_uid: str, client_type_uid: str, client_category_uid: str, account_uid: str | None, client_code: str, client_description: str, start_date: datetime.datetime, end_date: datetime.datetime | None, is_internal: int, is_system: int, is_test: int, custom_attributes: str = "{}"):
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
        self.custom_attributes = custom_attributes
    @classmethod
    def empty_write(cls):
        return cls("", "", "", "", "", "", "", "", "", datetime.datetime.now(), datetime.datetime.now(), 0, 0, 0)
    @classmethod
    def default_write(cls):
        return cls(base_dto.get_random_uid(), "", "", "", "", "", "", "", "", datetime.datetime.now(), datetime.datetime.now(), 0, 0, 0)
    @classmethod
    def random_write(cls):
        return cls(base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), datetime.datetime.now(), datetime.datetime.now(), 0, 0, 0)
    @classmethod
    def new_write(cls, client_uid: str, client_name: str, tenant_uid: str, country_uid: str, client_type_uid: str, client_category_uid: str, account_uid: str | None, client_code: str, client_description: str, start_date: datetime.datetime, end_date: datetime.datetime | None, is_internal: int, is_system: int, is_test: int):
        return cls(client_uid, client_name, tenant_uid, country_uid, client_type_uid, client_category_uid, account_uid, client_code, client_description, start_date, end_date, is_internal, is_system, is_test)
    @classmethod
    def new_write_with_defaults(cls, client_uid: str = "", client_name: str = "", tenant_uid: str = "", country_uid: str = "", client_type_uid: str = "", client_category_uid: str = "", account_uid: str | None = "", client_code: str = "", client_description: str = "", start_date: datetime.datetime = datetime.datetime.now(), end_date: datetime.datetime | None = datetime.datetime.now(), is_internal: int = 0, is_system: int = 0, is_test: int = 0):
        return cls(client_uid, client_name, tenant_uid, country_uid, client_type_uid, client_category_uid, account_uid, client_code, client_description, start_date, end_date, is_internal, is_system, is_test)
    @classmethod
    def new_write_random_uid(cls, client_name: str, tenant_uid: str, country_uid: str, client_type_uid: str, client_category_uid: str, account_uid: str | None, client_code: str, client_description: str, start_date: datetime.datetime, end_date: datetime.datetime | None, is_internal: int, is_system: int, is_test: int):
        return cls(base_dto.get_random_uid(), client_name, tenant_uid, country_uid, client_type_uid, client_category_uid, account_uid, client_code, client_description, start_date, end_date, is_internal, is_system, is_test)
    @classmethod
    def get_class_model(cls) -> base_model:
        return db_models.client_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["client_uid"], d["client_name"], d["tenant_uid"], d["country_uid"], d["client_type_uid"], d["client_category_uid"], d["account_uid"], d["client_code"], d["client_description"], d["start_date"], d["end_date"], d["is_internal"], d["is_system"], d["is_test"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return client_write_dto(self.client_uid, self.client_name, self.tenant_uid, self.country_uid, self.client_type_uid, self.client_category_uid, self.account_uid, self.client_code, self.client_description, self.start_date, self.end_date, self.is_internal, self.is_system, self.is_test, self.custom_attributes)
    def clone_write_new_uid(self):
        return client_write_dto(base_dto.get_random_uid(), self.client_name, self.tenant_uid, self.country_uid, self.client_type_uid, self.client_category_uid, self.account_uid, self.client_code, self.client_description, self.start_date, self.end_date, self.is_internal, self.is_system, self.is_test, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return client_write_dto(uid, self.client_name, self.tenant_uid, self.country_uid, self.client_type_uid, self.client_category_uid, self.account_uid, self.client_code, self.client_description, self.start_date, self.end_date, self.is_internal, self.is_system, self.is_test, self.custom_attributes)
    def get_model(self) -> base_model:
        return db_models.client_model
    def get_uid(self) -> str:
        return self.client_uid
    def get_name(self) -> str:
        return self.client_name
    def get_list_values(self) -> list[any]:
        return [self.client_uid, self.client_name, self.tenant_uid, self.country_uid, self.client_type_uid, self.client_category_uid, self.account_uid, self.client_code, self.client_description, self.start_date, self.end_date, self.is_internal, self.is_system, self.is_test, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.client_uid, self.client_name, self.tenant_uid, self.country_uid, self.client_type_uid, self.client_category_uid, self.account_uid, self.client_code, self.client_description, self.start_date, self.end_date, self.is_internal, self.is_system, self.is_test]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.client_name, self.tenant_uid, self.country_uid, self.client_type_uid, self.client_category_uid, self.account_uid, self.client_code, self.client_description, self.start_date, self.end_date, self.is_internal, self.is_system, self.is_test, self.custom_attributes, updated_by, self.client_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.client_uid, self.client_name, self.tenant_uid, self.country_uid, self.client_type_uid, self.client_category_uid, self.account_uid, self.client_code, self.client_description, self.start_date, self.end_date, self.is_internal, self.is_system, self.is_test, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.client_name, self.tenant_uid, self.country_uid, self.client_type_uid, self.client_category_uid, self.account_uid, self.client_code, self.client_description, self.start_date, self.end_date, self.is_internal, self.is_system, self.is_test]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.client_name, self.tenant_uid, self.country_uid, self.client_type_uid, self.client_category_uid, self.account_uid, self.client_code, self.client_description, self.start_date, self.end_date, self.is_internal, self.is_system, self.is_test, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_uid() == obj.get_uid()
    def update_uid(self, uid: str):
        self.client_uid = uid
    def update_uid_attributes(self, client_uid: str, client_name: str, tenant_uid: str, country_uid: str, client_type_uid: str, client_category_uid: str, account_uid: str | None, client_code: str, client_description: str, start_date: datetime.datetime, end_date: datetime.datetime | None, is_internal: int, is_system: int, is_test: int):
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
    def update_attributes(self, client_name: str, tenant_uid: str, country_uid: str, client_type_uid: str, client_category_uid: str, account_uid: str | None, client_code: str, client_description: str, start_date: datetime.datetime, end_date: datetime.datetime | None, is_internal: int, is_system: int, is_test: int):
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


@dataclass(frozen=False)
class client_account_write_dto(base_write_dto):
    client_account_uid: str
    client_account_name: str
    tenant_uid: str
    client_uid: str
    account_uid: str
    client_role_uid: str
    role_comment: str
    def __init__(self, client_account_uid: str, client_account_name: str, tenant_uid: str, client_uid: str, account_uid: str, client_role_uid: str, role_comment: str, custom_attributes: str = "{}"):
        self.client_account_uid = client_account_uid
        self.client_account_name = client_account_name
        self.tenant_uid = tenant_uid
        self.client_uid = client_uid
        self.account_uid = account_uid
        self.client_role_uid = client_role_uid
        self.role_comment = role_comment
        self.custom_attributes = custom_attributes
    @classmethod
    def empty_write(cls):
        return cls("", "", "", "", "", "", "")
    @classmethod
    def default_write(cls):
        return cls(base_dto.get_random_uid(), "", "", "", "", "", "")
    @classmethod
    def random_write(cls):
        return cls(base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid())
    @classmethod
    def new_write(cls, client_account_uid: str, client_account_name: str, tenant_uid: str, client_uid: str, account_uid: str, client_role_uid: str, role_comment: str):
        return cls(client_account_uid, client_account_name, tenant_uid, client_uid, account_uid, client_role_uid, role_comment)
    @classmethod
    def new_write_with_defaults(cls, client_account_uid: str = "", client_account_name: str = "", tenant_uid: str = "", client_uid: str = "", account_uid: str = "", client_role_uid: str = "", role_comment: str = ""):
        return cls(client_account_uid, client_account_name, tenant_uid, client_uid, account_uid, client_role_uid, role_comment)
    @classmethod
    def new_write_random_uid(cls, client_account_name: str, tenant_uid: str, client_uid: str, account_uid: str, client_role_uid: str, role_comment: str):
        return cls(base_dto.get_random_uid(), client_account_name, tenant_uid, client_uid, account_uid, client_role_uid, role_comment)
    @classmethod
    def get_class_model(cls) -> base_model:
        return db_models.client_account_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["client_account_uid"], d["client_account_name"], d["tenant_uid"], d["client_uid"], d["account_uid"], d["client_role_uid"], d["role_comment"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return client_account_write_dto(self.client_account_uid, self.client_account_name, self.tenant_uid, self.client_uid, self.account_uid, self.client_role_uid, self.role_comment, self.custom_attributes)
    def clone_write_new_uid(self):
        return client_account_write_dto(base_dto.get_random_uid(), self.client_account_name, self.tenant_uid, self.client_uid, self.account_uid, self.client_role_uid, self.role_comment, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return client_account_write_dto(uid, self.client_account_name, self.tenant_uid, self.client_uid, self.account_uid, self.client_role_uid, self.role_comment, self.custom_attributes)
    def get_model(self) -> base_model:
        return db_models.client_account_model
    def get_uid(self) -> str:
        return self.client_account_uid
    def get_name(self) -> str:
        return self.client_account_name
    def get_list_values(self) -> list[any]:
        return [self.client_account_uid, self.client_account_name, self.tenant_uid, self.client_uid, self.account_uid, self.client_role_uid, self.role_comment, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.client_account_uid, self.client_account_name, self.tenant_uid, self.client_uid, self.account_uid, self.client_role_uid, self.role_comment]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.client_account_name, self.tenant_uid, self.client_uid, self.account_uid, self.client_role_uid, self.role_comment, self.custom_attributes, updated_by, self.client_account_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.client_account_uid, self.client_account_name, self.tenant_uid, self.client_uid, self.account_uid, self.client_role_uid, self.role_comment, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.client_account_name, self.tenant_uid, self.client_uid, self.account_uid, self.client_role_uid, self.role_comment]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.client_account_name, self.tenant_uid, self.client_uid, self.account_uid, self.client_role_uid, self.role_comment, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_uid() == obj.get_uid()
    def update_uid(self, uid: str):
        self.client_account_uid = uid
    def update_uid_attributes(self, client_account_uid: str, client_account_name: str, tenant_uid: str, client_uid: str, account_uid: str, client_role_uid: str, role_comment: str):
        self.client_account_uid = client_account_uid
        self.client_account_name = client_account_name
        self.tenant_uid = tenant_uid
        self.client_uid = client_uid
        self.account_uid = account_uid
        self.client_role_uid = client_role_uid
        self.role_comment = role_comment
    def update_attributes(self, client_account_name: str, tenant_uid: str, client_uid: str, account_uid: str, client_role_uid: str, role_comment: str):
        self.client_account_name = client_account_name
        self.tenant_uid = tenant_uid
        self.client_uid = client_uid
        self.account_uid = account_uid
        self.client_role_uid = client_role_uid
        self.role_comment = role_comment


@dataclass(frozen=False)
class client_contract_write_dto(base_write_dto):
    client_contract_uid: str
    client_contract_name: str
    tenant_uid: str
    client_uid: str
    parent_client_contract_uid: str | None
    contract_text: str
    contract_value: str
    currency_uid: str
    def __init__(self, client_contract_uid: str, client_contract_name: str, tenant_uid: str, client_uid: str, parent_client_contract_uid: str | None, contract_text: str, contract_value: str, currency_uid: str, custom_attributes: str = "{}"):
        self.client_contract_uid = client_contract_uid
        self.client_contract_name = client_contract_name
        self.tenant_uid = tenant_uid
        self.client_uid = client_uid
        self.parent_client_contract_uid = parent_client_contract_uid
        self.contract_text = contract_text
        self.contract_value = contract_value
        self.currency_uid = currency_uid
        self.custom_attributes = custom_attributes
    @classmethod
    def empty_write(cls):
        return cls("", "", "", "", "", "", "", "")
    @classmethod
    def default_write(cls):
        return cls(base_dto.get_random_uid(), "", "", "", "", "", "", "")
    @classmethod
    def random_write(cls):
        return cls(base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), "", base_dto.get_random_uid())
    @classmethod
    def new_write(cls, client_contract_uid: str, client_contract_name: str, tenant_uid: str, client_uid: str, parent_client_contract_uid: str | None, contract_text: str, contract_value: str, currency_uid: str):
        return cls(client_contract_uid, client_contract_name, tenant_uid, client_uid, parent_client_contract_uid, contract_text, contract_value, currency_uid)
    @classmethod
    def new_write_with_defaults(cls, client_contract_uid: str = "", client_contract_name: str = "", tenant_uid: str = "", client_uid: str = "", parent_client_contract_uid: str | None = "", contract_text: str = "", contract_value: str = "", currency_uid: str = ""):
        return cls(client_contract_uid, client_contract_name, tenant_uid, client_uid, parent_client_contract_uid, contract_text, contract_value, currency_uid)
    @classmethod
    def new_write_random_uid(cls, client_contract_name: str, tenant_uid: str, client_uid: str, parent_client_contract_uid: str | None, contract_text: str, contract_value: str, currency_uid: str):
        return cls(base_dto.get_random_uid(), client_contract_name, tenant_uid, client_uid, parent_client_contract_uid, contract_text, contract_value, currency_uid)
    @classmethod
    def get_class_model(cls) -> base_model:
        return db_models.client_contract_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["client_contract_uid"], d["client_contract_name"], d["tenant_uid"], d["client_uid"], d["parent_client_contract_uid"], d["contract_text"], d["contract_value"], d["currency_uid"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return client_contract_write_dto(self.client_contract_uid, self.client_contract_name, self.tenant_uid, self.client_uid, self.parent_client_contract_uid, self.contract_text, self.contract_value, self.currency_uid, self.custom_attributes)
    def clone_write_new_uid(self):
        return client_contract_write_dto(base_dto.get_random_uid(), self.client_contract_name, self.tenant_uid, self.client_uid, self.parent_client_contract_uid, self.contract_text, self.contract_value, self.currency_uid, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return client_contract_write_dto(uid, self.client_contract_name, self.tenant_uid, self.client_uid, self.parent_client_contract_uid, self.contract_text, self.contract_value, self.currency_uid, self.custom_attributes)
    def get_model(self) -> base_model:
        return db_models.client_contract_model
    def get_uid(self) -> str:
        return self.client_contract_uid
    def get_name(self) -> str:
        return self.client_contract_name
    def get_list_values(self) -> list[any]:
        return [self.client_contract_uid, self.client_contract_name, self.tenant_uid, self.client_uid, self.parent_client_contract_uid, self.contract_text, self.contract_value, self.currency_uid, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.client_contract_uid, self.client_contract_name, self.tenant_uid, self.client_uid, self.parent_client_contract_uid, self.contract_text, self.contract_value, self.currency_uid]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.client_contract_name, self.tenant_uid, self.client_uid, self.parent_client_contract_uid, self.contract_text, self.contract_value, self.currency_uid, self.custom_attributes, updated_by, self.client_contract_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.client_contract_uid, self.client_contract_name, self.tenant_uid, self.client_uid, self.parent_client_contract_uid, self.contract_text, self.contract_value, self.currency_uid, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.client_contract_name, self.tenant_uid, self.client_uid, self.parent_client_contract_uid, self.contract_text, self.contract_value, self.currency_uid]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.client_contract_name, self.tenant_uid, self.client_uid, self.parent_client_contract_uid, self.contract_text, self.contract_value, self.currency_uid, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_uid() == obj.get_uid()
    def update_uid(self, uid: str):
        self.client_contract_uid = uid
    def update_uid_attributes(self, client_contract_uid: str, client_contract_name: str, tenant_uid: str, client_uid: str, parent_client_contract_uid: str | None, contract_text: str, contract_value: str, currency_uid: str):
        self.client_contract_uid = client_contract_uid
        self.client_contract_name = client_contract_name
        self.tenant_uid = tenant_uid
        self.client_uid = client_uid
        self.parent_client_contract_uid = parent_client_contract_uid
        self.contract_text = contract_text
        self.contract_value = contract_value
        self.currency_uid = currency_uid
    def update_attributes(self, client_contract_name: str, tenant_uid: str, client_uid: str, parent_client_contract_uid: str | None, contract_text: str, contract_value: str, currency_uid: str):
        self.client_contract_name = client_contract_name
        self.tenant_uid = tenant_uid
        self.client_uid = client_uid
        self.parent_client_contract_uid = parent_client_contract_uid
        self.contract_text = contract_text
        self.contract_value = contract_value
        self.currency_uid = currency_uid


@dataclass(frozen=False)
class client_country_write_dto(base_write_dto):
    client_country_uid: str
    client_country_name: str
    tenant_uid: str
    client_uid: str
    country_uid: str
    country_priority: int
    country_comment: str
    def __init__(self, client_country_uid: str, client_country_name: str, tenant_uid: str, client_uid: str, country_uid: str, country_priority: int, country_comment: str, custom_attributes: str = "{}"):
        self.client_country_uid = client_country_uid
        self.client_country_name = client_country_name
        self.tenant_uid = tenant_uid
        self.client_uid = client_uid
        self.country_uid = country_uid
        self.country_priority = country_priority
        self.country_comment = country_comment
        self.custom_attributes = custom_attributes
    @classmethod
    def empty_write(cls):
        return cls("", "", "", "", "", 0, "")
    @classmethod
    def default_write(cls):
        return cls(base_dto.get_random_uid(), "", "", "", "", 0, "")
    @classmethod
    def random_write(cls):
        return cls(base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), 0, base_dto.get_random_uid())
    @classmethod
    def new_write(cls, client_country_uid: str, client_country_name: str, tenant_uid: str, client_uid: str, country_uid: str, country_priority: int, country_comment: str):
        return cls(client_country_uid, client_country_name, tenant_uid, client_uid, country_uid, country_priority, country_comment)
    @classmethod
    def new_write_with_defaults(cls, client_country_uid: str = "", client_country_name: str = "", tenant_uid: str = "", client_uid: str = "", country_uid: str = "", country_priority: int = 0, country_comment: str = ""):
        return cls(client_country_uid, client_country_name, tenant_uid, client_uid, country_uid, country_priority, country_comment)
    @classmethod
    def new_write_random_uid(cls, client_country_name: str, tenant_uid: str, client_uid: str, country_uid: str, country_priority: int, country_comment: str):
        return cls(base_dto.get_random_uid(), client_country_name, tenant_uid, client_uid, country_uid, country_priority, country_comment)
    @classmethod
    def get_class_model(cls) -> base_model:
        return db_models.client_country_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["client_country_uid"], d["client_country_name"], d["tenant_uid"], d["client_uid"], d["country_uid"], d["country_priority"], d["country_comment"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return client_country_write_dto(self.client_country_uid, self.client_country_name, self.tenant_uid, self.client_uid, self.country_uid, self.country_priority, self.country_comment, self.custom_attributes)
    def clone_write_new_uid(self):
        return client_country_write_dto(base_dto.get_random_uid(), self.client_country_name, self.tenant_uid, self.client_uid, self.country_uid, self.country_priority, self.country_comment, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return client_country_write_dto(uid, self.client_country_name, self.tenant_uid, self.client_uid, self.country_uid, self.country_priority, self.country_comment, self.custom_attributes)
    def get_model(self) -> base_model:
        return db_models.client_country_model
    def get_uid(self) -> str:
        return self.client_country_uid
    def get_name(self) -> str:
        return self.client_country_name
    def get_list_values(self) -> list[any]:
        return [self.client_country_uid, self.client_country_name, self.tenant_uid, self.client_uid, self.country_uid, self.country_priority, self.country_comment, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.client_country_uid, self.client_country_name, self.tenant_uid, self.client_uid, self.country_uid, self.country_priority, self.country_comment]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.client_country_name, self.tenant_uid, self.client_uid, self.country_uid, self.country_priority, self.country_comment, self.custom_attributes, updated_by, self.client_country_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.client_country_uid, self.client_country_name, self.tenant_uid, self.client_uid, self.country_uid, self.country_priority, self.country_comment, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.client_country_name, self.tenant_uid, self.client_uid, self.country_uid, self.country_priority, self.country_comment]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.client_country_name, self.tenant_uid, self.client_uid, self.country_uid, self.country_priority, self.country_comment, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_uid() == obj.get_uid()
    def update_uid(self, uid: str):
        self.client_country_uid = uid
    def update_uid_attributes(self, client_country_uid: str, client_country_name: str, tenant_uid: str, client_uid: str, country_uid: str, country_priority: int, country_comment: str):
        self.client_country_uid = client_country_uid
        self.client_country_name = client_country_name
        self.tenant_uid = tenant_uid
        self.client_uid = client_uid
        self.country_uid = country_uid
        self.country_priority = country_priority
        self.country_comment = country_comment
    def update_attributes(self, client_country_name: str, tenant_uid: str, client_uid: str, country_uid: str, country_priority: int, country_comment: str):
        self.client_country_name = client_country_name
        self.tenant_uid = tenant_uid
        self.client_uid = client_uid
        self.country_uid = country_uid
        self.country_priority = country_priority
        self.country_comment = country_comment


@dataclass(frozen=False)
class client_payment_write_dto(base_write_dto):
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
    def __init__(self, client_payment_uid: str, client_payment_name: str, tenant_uid: str, client_uid: str, account_uid: str, currency_uid: str, start_date: datetime.datetime, end_date: datetime.datetime | None, payment_value: str, payment_type: str, source_number: str, source_reference: str, is_approved: int, custom_attributes: str = "{}"):
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
        self.custom_attributes = custom_attributes
    @classmethod
    def empty_write(cls):
        return cls("", "", "", "", "", "", datetime.datetime.now(), datetime.datetime.now(), "", "", "", "", 0)
    @classmethod
    def default_write(cls):
        return cls(base_dto.get_random_uid(), "", "", "", "", "", datetime.datetime.now(), datetime.datetime.now(), "", "", "", "", 0)
    @classmethod
    def random_write(cls):
        return cls(base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), datetime.datetime.now(), datetime.datetime.now(), "", base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), 0)
    @classmethod
    def new_write(cls, client_payment_uid: str, client_payment_name: str, tenant_uid: str, client_uid: str, account_uid: str, currency_uid: str, start_date: datetime.datetime, end_date: datetime.datetime | None, payment_value: str, payment_type: str, source_number: str, source_reference: str, is_approved: int):
        return cls(client_payment_uid, client_payment_name, tenant_uid, client_uid, account_uid, currency_uid, start_date, end_date, payment_value, payment_type, source_number, source_reference, is_approved)
    @classmethod
    def new_write_with_defaults(cls, client_payment_uid: str = "", client_payment_name: str = "", tenant_uid: str = "", client_uid: str = "", account_uid: str = "", currency_uid: str = "", start_date: datetime.datetime = datetime.datetime.now(), end_date: datetime.datetime | None = datetime.datetime.now(), payment_value: str = "", payment_type: str = "", source_number: str = "", source_reference: str = "", is_approved: int = 0):
        return cls(client_payment_uid, client_payment_name, tenant_uid, client_uid, account_uid, currency_uid, start_date, end_date, payment_value, payment_type, source_number, source_reference, is_approved)
    @classmethod
    def new_write_random_uid(cls, client_payment_name: str, tenant_uid: str, client_uid: str, account_uid: str, currency_uid: str, start_date: datetime.datetime, end_date: datetime.datetime | None, payment_value: str, payment_type: str, source_number: str, source_reference: str, is_approved: int):
        return cls(base_dto.get_random_uid(), client_payment_name, tenant_uid, client_uid, account_uid, currency_uid, start_date, end_date, payment_value, payment_type, source_number, source_reference, is_approved)
    @classmethod
    def get_class_model(cls) -> base_model:
        return db_models.client_payment_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["client_payment_uid"], d["client_payment_name"], d["tenant_uid"], d["client_uid"], d["account_uid"], d["currency_uid"], d["start_date"], d["end_date"], d["payment_value"], d["payment_type"], d["source_number"], d["source_reference"], d["is_approved"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return client_payment_write_dto(self.client_payment_uid, self.client_payment_name, self.tenant_uid, self.client_uid, self.account_uid, self.currency_uid, self.start_date, self.end_date, self.payment_value, self.payment_type, self.source_number, self.source_reference, self.is_approved, self.custom_attributes)
    def clone_write_new_uid(self):
        return client_payment_write_dto(base_dto.get_random_uid(), self.client_payment_name, self.tenant_uid, self.client_uid, self.account_uid, self.currency_uid, self.start_date, self.end_date, self.payment_value, self.payment_type, self.source_number, self.source_reference, self.is_approved, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return client_payment_write_dto(uid, self.client_payment_name, self.tenant_uid, self.client_uid, self.account_uid, self.currency_uid, self.start_date, self.end_date, self.payment_value, self.payment_type, self.source_number, self.source_reference, self.is_approved, self.custom_attributes)
    def get_model(self) -> base_model:
        return db_models.client_payment_model
    def get_uid(self) -> str:
        return self.client_payment_uid
    def get_name(self) -> str:
        return self.client_payment_name
    def get_list_values(self) -> list[any]:
        return [self.client_payment_uid, self.client_payment_name, self.tenant_uid, self.client_uid, self.account_uid, self.currency_uid, self.start_date, self.end_date, self.payment_value, self.payment_type, self.source_number, self.source_reference, self.is_approved, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.client_payment_uid, self.client_payment_name, self.tenant_uid, self.client_uid, self.account_uid, self.currency_uid, self.start_date, self.end_date, self.payment_value, self.payment_type, self.source_number, self.source_reference, self.is_approved]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.client_payment_name, self.tenant_uid, self.client_uid, self.account_uid, self.currency_uid, self.start_date, self.end_date, self.payment_value, self.payment_type, self.source_number, self.source_reference, self.is_approved, self.custom_attributes, updated_by, self.client_payment_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.client_payment_uid, self.client_payment_name, self.tenant_uid, self.client_uid, self.account_uid, self.currency_uid, self.start_date, self.end_date, self.payment_value, self.payment_type, self.source_number, self.source_reference, self.is_approved, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.client_payment_name, self.tenant_uid, self.client_uid, self.account_uid, self.currency_uid, self.start_date, self.end_date, self.payment_value, self.payment_type, self.source_number, self.source_reference, self.is_approved]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.client_payment_name, self.tenant_uid, self.client_uid, self.account_uid, self.currency_uid, self.start_date, self.end_date, self.payment_value, self.payment_type, self.source_number, self.source_reference, self.is_approved, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_uid() == obj.get_uid()
    def update_uid(self, uid: str):
        self.client_payment_uid = uid
    def update_uid_attributes(self, client_payment_uid: str, client_payment_name: str, tenant_uid: str, client_uid: str, account_uid: str, currency_uid: str, start_date: datetime.datetime, end_date: datetime.datetime | None, payment_value: str, payment_type: str, source_number: str, source_reference: str, is_approved: int):
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
    def update_attributes(self, client_payment_name: str, tenant_uid: str, client_uid: str, account_uid: str, currency_uid: str, start_date: datetime.datetime, end_date: datetime.datetime | None, payment_value: str, payment_type: str, source_number: str, source_reference: str, is_approved: int):
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


@dataclass(frozen=False)
class client_role_write_dto(base_write_dto):
    client_role_uid: str
    client_role_name: str
    role_description: str
    def __init__(self, client_role_uid: str, client_role_name: str, role_description: str, custom_attributes: str = "{}"):
        self.client_role_uid = client_role_uid
        self.client_role_name = client_role_name
        self.role_description = role_description
        self.custom_attributes = custom_attributes
    @classmethod
    def empty_write(cls):
        return cls("", "", "")
    @classmethod
    def default_write(cls):
        return cls(base_dto.get_random_uid(), "", "")
    @classmethod
    def random_write(cls):
        return cls(base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid())
    @classmethod
    def new_write(cls, client_role_uid: str, client_role_name: str, role_description: str):
        return cls(client_role_uid, client_role_name, role_description)
    @classmethod
    def new_write_with_defaults(cls, client_role_uid: str = "", client_role_name: str = "", role_description: str = ""):
        return cls(client_role_uid, client_role_name, role_description)
    @classmethod
    def new_write_random_uid(cls, client_role_name: str, role_description: str):
        return cls(base_dto.get_random_uid(), client_role_name, role_description)
    @classmethod
    def get_class_model(cls) -> base_model:
        return db_models.client_role_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["client_role_uid"], d["client_role_name"], d["role_description"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return client_role_write_dto(self.client_role_uid, self.client_role_name, self.role_description, self.custom_attributes)
    def clone_write_new_uid(self):
        return client_role_write_dto(base_dto.get_random_uid(), self.client_role_name, self.role_description, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return client_role_write_dto(uid, self.client_role_name, self.role_description, self.custom_attributes)
    def get_model(self) -> base_model:
        return db_models.client_role_model
    def get_uid(self) -> str:
        return self.client_role_uid
    def get_name(self) -> str:
        return self.client_role_name
    def get_list_values(self) -> list[any]:
        return [self.client_role_uid, self.client_role_name, self.role_description, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.client_role_uid, self.client_role_name, self.role_description]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.client_role_name, self.role_description, self.custom_attributes, updated_by, self.client_role_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.client_role_uid, self.client_role_name, self.role_description, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.client_role_name, self.role_description]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.client_role_name, self.role_description, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_uid() == obj.get_uid()
    def update_uid(self, uid: str):
        self.client_role_uid = uid
    def update_uid_attributes(self, client_role_uid: str, client_role_name: str, role_description: str):
        self.client_role_uid = client_role_uid
        self.client_role_name = client_role_name
        self.role_description = role_description
    def update_attributes(self, client_role_name: str, role_description: str):
        self.client_role_name = client_role_name
        self.role_description = role_description


@dataclass(frozen=False)
class client_status_write_dto(base_write_dto):
    client_status_uid: str
    client_status_name: str
    client_status_description: str
    def __init__(self, client_status_uid: str, client_status_name: str, client_status_description: str, custom_attributes: str = "{}"):
        self.client_status_uid = client_status_uid
        self.client_status_name = client_status_name
        self.client_status_description = client_status_description
        self.custom_attributes = custom_attributes
    @classmethod
    def empty_write(cls):
        return cls("", "", "")
    @classmethod
    def default_write(cls):
        return cls(base_dto.get_random_uid(), "", "")
    @classmethod
    def random_write(cls):
        return cls(base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid())
    @classmethod
    def new_write(cls, client_status_uid: str, client_status_name: str, client_status_description: str):
        return cls(client_status_uid, client_status_name, client_status_description)
    @classmethod
    def new_write_with_defaults(cls, client_status_uid: str = "", client_status_name: str = "", client_status_description: str = ""):
        return cls(client_status_uid, client_status_name, client_status_description)
    @classmethod
    def new_write_random_uid(cls, client_status_name: str, client_status_description: str):
        return cls(base_dto.get_random_uid(), client_status_name, client_status_description)
    @classmethod
    def get_class_model(cls) -> base_model:
        return db_models.client_status_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["client_status_uid"], d["client_status_name"], d["client_status_description"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return client_status_write_dto(self.client_status_uid, self.client_status_name, self.client_status_description, self.custom_attributes)
    def clone_write_new_uid(self):
        return client_status_write_dto(base_dto.get_random_uid(), self.client_status_name, self.client_status_description, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return client_status_write_dto(uid, self.client_status_name, self.client_status_description, self.custom_attributes)
    def get_model(self) -> base_model:
        return db_models.client_status_model
    def get_uid(self) -> str:
        return self.client_status_uid
    def get_name(self) -> str:
        return self.client_status_name
    def get_list_values(self) -> list[any]:
        return [self.client_status_uid, self.client_status_name, self.client_status_description, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.client_status_uid, self.client_status_name, self.client_status_description]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.client_status_name, self.client_status_description, self.custom_attributes, updated_by, self.client_status_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.client_status_uid, self.client_status_name, self.client_status_description, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.client_status_name, self.client_status_description]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.client_status_name, self.client_status_description, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_uid() == obj.get_uid()
    def update_uid(self, uid: str):
        self.client_status_uid = uid
    def update_uid_attributes(self, client_status_uid: str, client_status_name: str, client_status_description: str):
        self.client_status_uid = client_status_uid
        self.client_status_name = client_status_name
        self.client_status_description = client_status_description
    def update_attributes(self, client_status_name: str, client_status_description: str):
        self.client_status_name = client_status_name
        self.client_status_description = client_status_description


@dataclass(frozen=False)
class client_type_write_dto(base_write_dto):
    client_type_uid: str
    client_type_name: str
    client_type_description: str
    def __init__(self, client_type_uid: str, client_type_name: str, client_type_description: str, custom_attributes: str = "{}"):
        self.client_type_uid = client_type_uid
        self.client_type_name = client_type_name
        self.client_type_description = client_type_description
        self.custom_attributes = custom_attributes
    @classmethod
    def empty_write(cls):
        return cls("", "", "")
    @classmethod
    def default_write(cls):
        return cls(base_dto.get_random_uid(), "", "")
    @classmethod
    def random_write(cls):
        return cls(base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid())
    @classmethod
    def new_write(cls, client_type_uid: str, client_type_name: str, client_type_description: str):
        return cls(client_type_uid, client_type_name, client_type_description)
    @classmethod
    def new_write_with_defaults(cls, client_type_uid: str = "", client_type_name: str = "", client_type_description: str = ""):
        return cls(client_type_uid, client_type_name, client_type_description)
    @classmethod
    def new_write_random_uid(cls, client_type_name: str, client_type_description: str):
        return cls(base_dto.get_random_uid(), client_type_name, client_type_description)
    @classmethod
    def get_class_model(cls) -> base_model:
        return db_models.client_type_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["client_type_uid"], d["client_type_name"], d["client_type_description"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return client_type_write_dto(self.client_type_uid, self.client_type_name, self.client_type_description, self.custom_attributes)
    def clone_write_new_uid(self):
        return client_type_write_dto(base_dto.get_random_uid(), self.client_type_name, self.client_type_description, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return client_type_write_dto(uid, self.client_type_name, self.client_type_description, self.custom_attributes)
    def get_model(self) -> base_model:
        return db_models.client_type_model
    def get_uid(self) -> str:
        return self.client_type_uid
    def get_name(self) -> str:
        return self.client_type_name
    def get_list_values(self) -> list[any]:
        return [self.client_type_uid, self.client_type_name, self.client_type_description, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.client_type_uid, self.client_type_name, self.client_type_description]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.client_type_name, self.client_type_description, self.custom_attributes, updated_by, self.client_type_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.client_type_uid, self.client_type_name, self.client_type_description, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.client_type_name, self.client_type_description]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.client_type_name, self.client_type_description, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_uid() == obj.get_uid()
    def update_uid(self, uid: str):
        self.client_type_uid = uid
    def update_uid_attributes(self, client_type_uid: str, client_type_name: str, client_type_description: str):
        self.client_type_uid = client_type_uid
        self.client_type_name = client_type_name
        self.client_type_description = client_type_description
    def update_attributes(self, client_type_name: str, client_type_description: str):
        self.client_type_name = client_type_name
        self.client_type_description = client_type_description


@dataclass(frozen=False)
class competency_entry_write_dto(base_write_dto):
    competency_entry_uid: str
    competency_entry_name: str
    tenant_uid: str
    competency_item_uid: str
    account_uid: str
    entry_template: str
    def __init__(self, competency_entry_uid: str, competency_entry_name: str, tenant_uid: str, competency_item_uid: str, account_uid: str, entry_template: str, custom_attributes: str = "{}"):
        self.competency_entry_uid = competency_entry_uid
        self.competency_entry_name = competency_entry_name
        self.tenant_uid = tenant_uid
        self.competency_item_uid = competency_item_uid
        self.account_uid = account_uid
        self.entry_template = entry_template
        self.custom_attributes = custom_attributes
    @classmethod
    def empty_write(cls):
        return cls("", "", "", "", "", "")
    @classmethod
    def default_write(cls):
        return cls(base_dto.get_random_uid(), "", "", "", "", "")
    @classmethod
    def random_write(cls):
        return cls(base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid())
    @classmethod
    def new_write(cls, competency_entry_uid: str, competency_entry_name: str, tenant_uid: str, competency_item_uid: str, account_uid: str, entry_template: str):
        return cls(competency_entry_uid, competency_entry_name, tenant_uid, competency_item_uid, account_uid, entry_template)
    @classmethod
    def new_write_with_defaults(cls, competency_entry_uid: str = "", competency_entry_name: str = "", tenant_uid: str = "", competency_item_uid: str = "", account_uid: str = "", entry_template: str = ""):
        return cls(competency_entry_uid, competency_entry_name, tenant_uid, competency_item_uid, account_uid, entry_template)
    @classmethod
    def new_write_random_uid(cls, competency_entry_name: str, tenant_uid: str, competency_item_uid: str, account_uid: str, entry_template: str):
        return cls(base_dto.get_random_uid(), competency_entry_name, tenant_uid, competency_item_uid, account_uid, entry_template)
    @classmethod
    def get_class_model(cls) -> base_model:
        return db_models.competency_entry_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["competency_entry_uid"], d["competency_entry_name"], d["tenant_uid"], d["competency_item_uid"], d["account_uid"], d["entry_template"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return competency_entry_write_dto(self.competency_entry_uid, self.competency_entry_name, self.tenant_uid, self.competency_item_uid, self.account_uid, self.entry_template, self.custom_attributes)
    def clone_write_new_uid(self):
        return competency_entry_write_dto(base_dto.get_random_uid(), self.competency_entry_name, self.tenant_uid, self.competency_item_uid, self.account_uid, self.entry_template, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return competency_entry_write_dto(uid, self.competency_entry_name, self.tenant_uid, self.competency_item_uid, self.account_uid, self.entry_template, self.custom_attributes)
    def get_model(self) -> base_model:
        return db_models.competency_entry_model
    def get_uid(self) -> str:
        return self.competency_entry_uid
    def get_name(self) -> str:
        return self.competency_entry_name
    def get_list_values(self) -> list[any]:
        return [self.competency_entry_uid, self.competency_entry_name, self.tenant_uid, self.competency_item_uid, self.account_uid, self.entry_template, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.competency_entry_uid, self.competency_entry_name, self.tenant_uid, self.competency_item_uid, self.account_uid, self.entry_template]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.competency_entry_name, self.tenant_uid, self.competency_item_uid, self.account_uid, self.entry_template, self.custom_attributes, updated_by, self.competency_entry_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.competency_entry_uid, self.competency_entry_name, self.tenant_uid, self.competency_item_uid, self.account_uid, self.entry_template, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.competency_entry_name, self.tenant_uid, self.competency_item_uid, self.account_uid, self.entry_template]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.competency_entry_name, self.tenant_uid, self.competency_item_uid, self.account_uid, self.entry_template, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_uid() == obj.get_uid()
    def update_uid(self, uid: str):
        self.competency_entry_uid = uid
    def update_uid_attributes(self, competency_entry_uid: str, competency_entry_name: str, tenant_uid: str, competency_item_uid: str, account_uid: str, entry_template: str):
        self.competency_entry_uid = competency_entry_uid
        self.competency_entry_name = competency_entry_name
        self.tenant_uid = tenant_uid
        self.competency_item_uid = competency_item_uid
        self.account_uid = account_uid
        self.entry_template = entry_template
    def update_attributes(self, competency_entry_name: str, tenant_uid: str, competency_item_uid: str, account_uid: str, entry_template: str):
        self.competency_entry_name = competency_entry_name
        self.tenant_uid = tenant_uid
        self.competency_item_uid = competency_item_uid
        self.account_uid = account_uid
        self.entry_template = entry_template


@dataclass(frozen=False)
class competency_entry_account_write_dto(base_write_dto):
    competency_entry_account_uid: str
    competency_entry_account_name: str
    tenant_uid: str
    account_uid: str
    competency_process_account_uid: str
    competency_group_account_uid: str
    competency_entry_uid: str
    competency_item_account_uid: str
    entry_title: str | None
    entry_content: str | None
    entry_value: str | None
    competency_ranking_uid: str
    def __init__(self, competency_entry_account_uid: str, competency_entry_account_name: str, tenant_uid: str, account_uid: str, competency_process_account_uid: str, competency_group_account_uid: str, competency_entry_uid: str, competency_item_account_uid: str, entry_title: str | None, entry_content: str | None, entry_value: str | None, competency_ranking_uid: str, custom_attributes: str = "{}"):
        self.competency_entry_account_uid = competency_entry_account_uid
        self.competency_entry_account_name = competency_entry_account_name
        self.tenant_uid = tenant_uid
        self.account_uid = account_uid
        self.competency_process_account_uid = competency_process_account_uid
        self.competency_group_account_uid = competency_group_account_uid
        self.competency_entry_uid = competency_entry_uid
        self.competency_item_account_uid = competency_item_account_uid
        self.entry_title = entry_title
        self.entry_content = entry_content
        self.entry_value = entry_value
        self.competency_ranking_uid = competency_ranking_uid
        self.custom_attributes = custom_attributes
    @classmethod
    def empty_write(cls):
        return cls("", "", "", "", "", "", "", "", "", "", "", "")
    @classmethod
    def default_write(cls):
        return cls(base_dto.get_random_uid(), "", "", "", "", "", "", "", "", "", "", "")
    @classmethod
    def random_write(cls):
        return cls(base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), "", base_dto.get_random_uid())
    @classmethod
    def new_write(cls, competency_entry_account_uid: str, competency_entry_account_name: str, tenant_uid: str, account_uid: str, competency_process_account_uid: str, competency_group_account_uid: str, competency_entry_uid: str, competency_item_account_uid: str, entry_title: str | None, entry_content: str | None, entry_value: str | None, competency_ranking_uid: str):
        return cls(competency_entry_account_uid, competency_entry_account_name, tenant_uid, account_uid, competency_process_account_uid, competency_group_account_uid, competency_entry_uid, competency_item_account_uid, entry_title, entry_content, entry_value, competency_ranking_uid)
    @classmethod
    def new_write_with_defaults(cls, competency_entry_account_uid: str = "", competency_entry_account_name: str = "", tenant_uid: str = "", account_uid: str = "", competency_process_account_uid: str = "", competency_group_account_uid: str = "", competency_entry_uid: str = "", competency_item_account_uid: str = "", entry_title: str | None = "", entry_content: str | None = "", entry_value: str | None = "", competency_ranking_uid: str = ""):
        return cls(competency_entry_account_uid, competency_entry_account_name, tenant_uid, account_uid, competency_process_account_uid, competency_group_account_uid, competency_entry_uid, competency_item_account_uid, entry_title, entry_content, entry_value, competency_ranking_uid)
    @classmethod
    def new_write_random_uid(cls, competency_entry_account_name: str, tenant_uid: str, account_uid: str, competency_process_account_uid: str, competency_group_account_uid: str, competency_entry_uid: str, competency_item_account_uid: str, entry_title: str | None, entry_content: str | None, entry_value: str | None, competency_ranking_uid: str):
        return cls(base_dto.get_random_uid(), competency_entry_account_name, tenant_uid, account_uid, competency_process_account_uid, competency_group_account_uid, competency_entry_uid, competency_item_account_uid, entry_title, entry_content, entry_value, competency_ranking_uid)
    @classmethod
    def get_class_model(cls) -> base_model:
        return db_models.competency_entry_account_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["competency_entry_account_uid"], d["competency_entry_account_name"], d["tenant_uid"], d["account_uid"], d["competency_process_account_uid"], d["competency_group_account_uid"], d["competency_entry_uid"], d["competency_item_account_uid"], d["entry_title"], d["entry_content"], d["entry_value"], d["competency_ranking_uid"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return competency_entry_account_write_dto(self.competency_entry_account_uid, self.competency_entry_account_name, self.tenant_uid, self.account_uid, self.competency_process_account_uid, self.competency_group_account_uid, self.competency_entry_uid, self.competency_item_account_uid, self.entry_title, self.entry_content, self.entry_value, self.competency_ranking_uid, self.custom_attributes)
    def clone_write_new_uid(self):
        return competency_entry_account_write_dto(base_dto.get_random_uid(), self.competency_entry_account_name, self.tenant_uid, self.account_uid, self.competency_process_account_uid, self.competency_group_account_uid, self.competency_entry_uid, self.competency_item_account_uid, self.entry_title, self.entry_content, self.entry_value, self.competency_ranking_uid, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return competency_entry_account_write_dto(uid, self.competency_entry_account_name, self.tenant_uid, self.account_uid, self.competency_process_account_uid, self.competency_group_account_uid, self.competency_entry_uid, self.competency_item_account_uid, self.entry_title, self.entry_content, self.entry_value, self.competency_ranking_uid, self.custom_attributes)
    def get_model(self) -> base_model:
        return db_models.competency_entry_account_model
    def get_uid(self) -> str:
        return self.competency_entry_account_uid
    def get_name(self) -> str:
        return self.competency_entry_account_name
    def get_list_values(self) -> list[any]:
        return [self.competency_entry_account_uid, self.competency_entry_account_name, self.tenant_uid, self.account_uid, self.competency_process_account_uid, self.competency_group_account_uid, self.competency_entry_uid, self.competency_item_account_uid, self.entry_title, self.entry_content, self.entry_value, self.competency_ranking_uid, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.competency_entry_account_uid, self.competency_entry_account_name, self.tenant_uid, self.account_uid, self.competency_process_account_uid, self.competency_group_account_uid, self.competency_entry_uid, self.competency_item_account_uid, self.entry_title, self.entry_content, self.entry_value, self.competency_ranking_uid]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.competency_entry_account_name, self.tenant_uid, self.account_uid, self.competency_process_account_uid, self.competency_group_account_uid, self.competency_entry_uid, self.competency_item_account_uid, self.entry_title, self.entry_content, self.entry_value, self.competency_ranking_uid, self.custom_attributes, updated_by, self.competency_entry_account_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.competency_entry_account_uid, self.competency_entry_account_name, self.tenant_uid, self.account_uid, self.competency_process_account_uid, self.competency_group_account_uid, self.competency_entry_uid, self.competency_item_account_uid, self.entry_title, self.entry_content, self.entry_value, self.competency_ranking_uid, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.competency_entry_account_name, self.tenant_uid, self.account_uid, self.competency_process_account_uid, self.competency_group_account_uid, self.competency_entry_uid, self.competency_item_account_uid, self.entry_title, self.entry_content, self.entry_value, self.competency_ranking_uid]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.competency_entry_account_name, self.tenant_uid, self.account_uid, self.competency_process_account_uid, self.competency_group_account_uid, self.competency_entry_uid, self.competency_item_account_uid, self.entry_title, self.entry_content, self.entry_value, self.competency_ranking_uid, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_uid() == obj.get_uid()
    def update_uid(self, uid: str):
        self.competency_entry_account_uid = uid
    def update_uid_attributes(self, competency_entry_account_uid: str, competency_entry_account_name: str, tenant_uid: str, account_uid: str, competency_process_account_uid: str, competency_group_account_uid: str, competency_entry_uid: str, competency_item_account_uid: str, entry_title: str | None, entry_content: str | None, entry_value: str | None, competency_ranking_uid: str):
        self.competency_entry_account_uid = competency_entry_account_uid
        self.competency_entry_account_name = competency_entry_account_name
        self.tenant_uid = tenant_uid
        self.account_uid = account_uid
        self.competency_process_account_uid = competency_process_account_uid
        self.competency_group_account_uid = competency_group_account_uid
        self.competency_entry_uid = competency_entry_uid
        self.competency_item_account_uid = competency_item_account_uid
        self.entry_title = entry_title
        self.entry_content = entry_content
        self.entry_value = entry_value
        self.competency_ranking_uid = competency_ranking_uid
    def update_attributes(self, competency_entry_account_name: str, tenant_uid: str, account_uid: str, competency_process_account_uid: str, competency_group_account_uid: str, competency_entry_uid: str, competency_item_account_uid: str, entry_title: str | None, entry_content: str | None, entry_value: str | None, competency_ranking_uid: str):
        self.competency_entry_account_name = competency_entry_account_name
        self.tenant_uid = tenant_uid
        self.account_uid = account_uid
        self.competency_process_account_uid = competency_process_account_uid
        self.competency_group_account_uid = competency_group_account_uid
        self.competency_entry_uid = competency_entry_uid
        self.competency_item_account_uid = competency_item_account_uid
        self.entry_title = entry_title
        self.entry_content = entry_content
        self.entry_value = entry_value
        self.competency_ranking_uid = competency_ranking_uid


@dataclass(frozen=False)
class competency_group_write_dto(base_write_dto):
    competency_group_uid: str
    competency_group_name: str
    competency_process_uid: str
    tenant_uid: str
    account_uid: str
    def __init__(self, competency_group_uid: str, competency_group_name: str, competency_process_uid: str, tenant_uid: str, account_uid: str, custom_attributes: str = "{}"):
        self.competency_group_uid = competency_group_uid
        self.competency_group_name = competency_group_name
        self.competency_process_uid = competency_process_uid
        self.tenant_uid = tenant_uid
        self.account_uid = account_uid
        self.custom_attributes = custom_attributes
    @classmethod
    def empty_write(cls):
        return cls("", "", "", "", "")
    @classmethod
    def default_write(cls):
        return cls(base_dto.get_random_uid(), "", "", "", "")
    @classmethod
    def random_write(cls):
        return cls(base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid())
    @classmethod
    def new_write(cls, competency_group_uid: str, competency_group_name: str, competency_process_uid: str, tenant_uid: str, account_uid: str):
        return cls(competency_group_uid, competency_group_name, competency_process_uid, tenant_uid, account_uid)
    @classmethod
    def new_write_with_defaults(cls, competency_group_uid: str = "", competency_group_name: str = "", competency_process_uid: str = "", tenant_uid: str = "", account_uid: str = ""):
        return cls(competency_group_uid, competency_group_name, competency_process_uid, tenant_uid, account_uid)
    @classmethod
    def new_write_random_uid(cls, competency_group_name: str, competency_process_uid: str, tenant_uid: str, account_uid: str):
        return cls(base_dto.get_random_uid(), competency_group_name, competency_process_uid, tenant_uid, account_uid)
    @classmethod
    def get_class_model(cls) -> base_model:
        return db_models.competency_group_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["competency_group_uid"], d["competency_group_name"], d["competency_process_uid"], d["tenant_uid"], d["account_uid"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return competency_group_write_dto(self.competency_group_uid, self.competency_group_name, self.competency_process_uid, self.tenant_uid, self.account_uid, self.custom_attributes)
    def clone_write_new_uid(self):
        return competency_group_write_dto(base_dto.get_random_uid(), self.competency_group_name, self.competency_process_uid, self.tenant_uid, self.account_uid, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return competency_group_write_dto(uid, self.competency_group_name, self.competency_process_uid, self.tenant_uid, self.account_uid, self.custom_attributes)
    def get_model(self) -> base_model:
        return db_models.competency_group_model
    def get_uid(self) -> str:
        return self.competency_group_uid
    def get_name(self) -> str:
        return self.competency_group_name
    def get_list_values(self) -> list[any]:
        return [self.competency_group_uid, self.competency_group_name, self.competency_process_uid, self.tenant_uid, self.account_uid, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.competency_group_uid, self.competency_group_name, self.competency_process_uid, self.tenant_uid, self.account_uid]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.competency_group_name, self.competency_process_uid, self.tenant_uid, self.account_uid, self.custom_attributes, updated_by, self.competency_group_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.competency_group_uid, self.competency_group_name, self.competency_process_uid, self.tenant_uid, self.account_uid, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.competency_group_name, self.competency_process_uid, self.tenant_uid, self.account_uid]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.competency_group_name, self.competency_process_uid, self.tenant_uid, self.account_uid, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_uid() == obj.get_uid()
    def update_uid(self, uid: str):
        self.competency_group_uid = uid
    def update_uid_attributes(self, competency_group_uid: str, competency_group_name: str, competency_process_uid: str, tenant_uid: str, account_uid: str):
        self.competency_group_uid = competency_group_uid
        self.competency_group_name = competency_group_name
        self.competency_process_uid = competency_process_uid
        self.tenant_uid = tenant_uid
        self.account_uid = account_uid
    def update_attributes(self, competency_group_name: str, competency_process_uid: str, tenant_uid: str, account_uid: str):
        self.competency_group_name = competency_group_name
        self.competency_process_uid = competency_process_uid
        self.tenant_uid = tenant_uid
        self.account_uid = account_uid


@dataclass(frozen=False)
class competency_group_account_write_dto(base_write_dto):
    competency_group_account_uid: str
    competency_group_account_name: str
    tenant_uid: str
    competency_process_uid: str
    competency_process_account_uid: str
    competency_group_uid: str
    account_uid: str
    start_date: datetime.datetime
    end_date: datetime.datetime | None
    final_group_result: str | None
    def __init__(self, competency_group_account_uid: str, competency_group_account_name: str, tenant_uid: str, competency_process_uid: str, competency_process_account_uid: str, competency_group_uid: str, account_uid: str, start_date: datetime.datetime, end_date: datetime.datetime | None, final_group_result: str | None, custom_attributes: str = "{}"):
        self.competency_group_account_uid = competency_group_account_uid
        self.competency_group_account_name = competency_group_account_name
        self.tenant_uid = tenant_uid
        self.competency_process_uid = competency_process_uid
        self.competency_process_account_uid = competency_process_account_uid
        self.competency_group_uid = competency_group_uid
        self.account_uid = account_uid
        self.start_date = start_date
        self.end_date = end_date
        self.final_group_result = final_group_result
        self.custom_attributes = custom_attributes
    @classmethod
    def empty_write(cls):
        return cls("", "", "", "", "", "", "", datetime.datetime.now(), datetime.datetime.now(), "")
    @classmethod
    def default_write(cls):
        return cls(base_dto.get_random_uid(), "", "", "", "", "", "", datetime.datetime.now(), datetime.datetime.now(), "")
    @classmethod
    def random_write(cls):
        return cls(base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), datetime.datetime.now(), datetime.datetime.now(), base_dto.get_random_uid())
    @classmethod
    def new_write(cls, competency_group_account_uid: str, competency_group_account_name: str, tenant_uid: str, competency_process_uid: str, competency_process_account_uid: str, competency_group_uid: str, account_uid: str, start_date: datetime.datetime, end_date: datetime.datetime | None, final_group_result: str | None):
        return cls(competency_group_account_uid, competency_group_account_name, tenant_uid, competency_process_uid, competency_process_account_uid, competency_group_uid, account_uid, start_date, end_date, final_group_result)
    @classmethod
    def new_write_with_defaults(cls, competency_group_account_uid: str = "", competency_group_account_name: str = "", tenant_uid: str = "", competency_process_uid: str = "", competency_process_account_uid: str = "", competency_group_uid: str = "", account_uid: str = "", start_date: datetime.datetime = datetime.datetime.now(), end_date: datetime.datetime | None = datetime.datetime.now(), final_group_result: str | None = ""):
        return cls(competency_group_account_uid, competency_group_account_name, tenant_uid, competency_process_uid, competency_process_account_uid, competency_group_uid, account_uid, start_date, end_date, final_group_result)
    @classmethod
    def new_write_random_uid(cls, competency_group_account_name: str, tenant_uid: str, competency_process_uid: str, competency_process_account_uid: str, competency_group_uid: str, account_uid: str, start_date: datetime.datetime, end_date: datetime.datetime | None, final_group_result: str | None):
        return cls(base_dto.get_random_uid(), competency_group_account_name, tenant_uid, competency_process_uid, competency_process_account_uid, competency_group_uid, account_uid, start_date, end_date, final_group_result)
    @classmethod
    def get_class_model(cls) -> base_model:
        return db_models.competency_group_account_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["competency_group_account_uid"], d["competency_group_account_name"], d["tenant_uid"], d["competency_process_uid"], d["competency_process_account_uid"], d["competency_group_uid"], d["account_uid"], d["start_date"], d["end_date"], d["final_group_result"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return competency_group_account_write_dto(self.competency_group_account_uid, self.competency_group_account_name, self.tenant_uid, self.competency_process_uid, self.competency_process_account_uid, self.competency_group_uid, self.account_uid, self.start_date, self.end_date, self.final_group_result, self.custom_attributes)
    def clone_write_new_uid(self):
        return competency_group_account_write_dto(base_dto.get_random_uid(), self.competency_group_account_name, self.tenant_uid, self.competency_process_uid, self.competency_process_account_uid, self.competency_group_uid, self.account_uid, self.start_date, self.end_date, self.final_group_result, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return competency_group_account_write_dto(uid, self.competency_group_account_name, self.tenant_uid, self.competency_process_uid, self.competency_process_account_uid, self.competency_group_uid, self.account_uid, self.start_date, self.end_date, self.final_group_result, self.custom_attributes)
    def get_model(self) -> base_model:
        return db_models.competency_group_account_model
    def get_uid(self) -> str:
        return self.competency_group_account_uid
    def get_name(self) -> str:
        return self.competency_group_account_name
    def get_list_values(self) -> list[any]:
        return [self.competency_group_account_uid, self.competency_group_account_name, self.tenant_uid, self.competency_process_uid, self.competency_process_account_uid, self.competency_group_uid, self.account_uid, self.start_date, self.end_date, self.final_group_result, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.competency_group_account_uid, self.competency_group_account_name, self.tenant_uid, self.competency_process_uid, self.competency_process_account_uid, self.competency_group_uid, self.account_uid, self.start_date, self.end_date, self.final_group_result]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.competency_group_account_name, self.tenant_uid, self.competency_process_uid, self.competency_process_account_uid, self.competency_group_uid, self.account_uid, self.start_date, self.end_date, self.final_group_result, self.custom_attributes, updated_by, self.competency_group_account_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.competency_group_account_uid, self.competency_group_account_name, self.tenant_uid, self.competency_process_uid, self.competency_process_account_uid, self.competency_group_uid, self.account_uid, self.start_date, self.end_date, self.final_group_result, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.competency_group_account_name, self.tenant_uid, self.competency_process_uid, self.competency_process_account_uid, self.competency_group_uid, self.account_uid, self.start_date, self.end_date, self.final_group_result]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.competency_group_account_name, self.tenant_uid, self.competency_process_uid, self.competency_process_account_uid, self.competency_group_uid, self.account_uid, self.start_date, self.end_date, self.final_group_result, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_uid() == obj.get_uid()
    def update_uid(self, uid: str):
        self.competency_group_account_uid = uid
    def update_uid_attributes(self, competency_group_account_uid: str, competency_group_account_name: str, tenant_uid: str, competency_process_uid: str, competency_process_account_uid: str, competency_group_uid: str, account_uid: str, start_date: datetime.datetime, end_date: datetime.datetime | None, final_group_result: str | None):
        self.competency_group_account_uid = competency_group_account_uid
        self.competency_group_account_name = competency_group_account_name
        self.tenant_uid = tenant_uid
        self.competency_process_uid = competency_process_uid
        self.competency_process_account_uid = competency_process_account_uid
        self.competency_group_uid = competency_group_uid
        self.account_uid = account_uid
        self.start_date = start_date
        self.end_date = end_date
        self.final_group_result = final_group_result
    def update_attributes(self, competency_group_account_name: str, tenant_uid: str, competency_process_uid: str, competency_process_account_uid: str, competency_group_uid: str, account_uid: str, start_date: datetime.datetime, end_date: datetime.datetime | None, final_group_result: str | None):
        self.competency_group_account_name = competency_group_account_name
        self.tenant_uid = tenant_uid
        self.competency_process_uid = competency_process_uid
        self.competency_process_account_uid = competency_process_account_uid
        self.competency_group_uid = competency_group_uid
        self.account_uid = account_uid
        self.start_date = start_date
        self.end_date = end_date
        self.final_group_result = final_group_result


@dataclass(frozen=False)
class competency_group_type_write_dto(base_write_dto):
    competency_group_type_uid: str
    competency_group_type_name: str
    tenant_uid: str
    def __init__(self, competency_group_type_uid: str, competency_group_type_name: str, tenant_uid: str, custom_attributes: str = "{}"):
        self.competency_group_type_uid = competency_group_type_uid
        self.competency_group_type_name = competency_group_type_name
        self.tenant_uid = tenant_uid
        self.custom_attributes = custom_attributes
    @classmethod
    def empty_write(cls):
        return cls("", "", "")
    @classmethod
    def default_write(cls):
        return cls(base_dto.get_random_uid(), "", "")
    @classmethod
    def random_write(cls):
        return cls(base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid())
    @classmethod
    def new_write(cls, competency_group_type_uid: str, competency_group_type_name: str, tenant_uid: str):
        return cls(competency_group_type_uid, competency_group_type_name, tenant_uid)
    @classmethod
    def new_write_with_defaults(cls, competency_group_type_uid: str = "", competency_group_type_name: str = "", tenant_uid: str = ""):
        return cls(competency_group_type_uid, competency_group_type_name, tenant_uid)
    @classmethod
    def new_write_random_uid(cls, competency_group_type_name: str, tenant_uid: str):
        return cls(base_dto.get_random_uid(), competency_group_type_name, tenant_uid)
    @classmethod
    def get_class_model(cls) -> base_model:
        return db_models.competency_group_type_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["competency_group_type_uid"], d["competency_group_type_name"], d["tenant_uid"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return competency_group_type_write_dto(self.competency_group_type_uid, self.competency_group_type_name, self.tenant_uid, self.custom_attributes)
    def clone_write_new_uid(self):
        return competency_group_type_write_dto(base_dto.get_random_uid(), self.competency_group_type_name, self.tenant_uid, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return competency_group_type_write_dto(uid, self.competency_group_type_name, self.tenant_uid, self.custom_attributes)
    def get_model(self) -> base_model:
        return db_models.competency_group_type_model
    def get_uid(self) -> str:
        return self.competency_group_type_uid
    def get_name(self) -> str:
        return self.competency_group_type_name
    def get_list_values(self) -> list[any]:
        return [self.competency_group_type_uid, self.competency_group_type_name, self.tenant_uid, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.competency_group_type_uid, self.competency_group_type_name, self.tenant_uid]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.competency_group_type_name, self.tenant_uid, self.custom_attributes, updated_by, self.competency_group_type_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.competency_group_type_uid, self.competency_group_type_name, self.tenant_uid, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.competency_group_type_name, self.tenant_uid]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.competency_group_type_name, self.tenant_uid, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_uid() == obj.get_uid()
    def update_uid(self, uid: str):
        self.competency_group_type_uid = uid
    def update_uid_attributes(self, competency_group_type_uid: str, competency_group_type_name: str, tenant_uid: str):
        self.competency_group_type_uid = competency_group_type_uid
        self.competency_group_type_name = competency_group_type_name
        self.tenant_uid = tenant_uid
    def update_attributes(self, competency_group_type_name: str, tenant_uid: str):
        self.competency_group_type_name = competency_group_type_name
        self.tenant_uid = tenant_uid


@dataclass(frozen=False)
class competency_item_write_dto(base_write_dto):
    competency_item_uid: str
    competency_item_name: str
    tenant_uid: str
    competency_process_uid: str
    competency_item_type_uid: str
    competency_group_uid: str
    account_uid: str
    item_template: str
    def __init__(self, competency_item_uid: str, competency_item_name: str, tenant_uid: str, competency_process_uid: str, competency_item_type_uid: str, competency_group_uid: str, account_uid: str, item_template: str, custom_attributes: str = "{}"):
        self.competency_item_uid = competency_item_uid
        self.competency_item_name = competency_item_name
        self.tenant_uid = tenant_uid
        self.competency_process_uid = competency_process_uid
        self.competency_item_type_uid = competency_item_type_uid
        self.competency_group_uid = competency_group_uid
        self.account_uid = account_uid
        self.item_template = item_template
        self.custom_attributes = custom_attributes
    @classmethod
    def empty_write(cls):
        return cls("", "", "", "", "", "", "", "")
    @classmethod
    def default_write(cls):
        return cls(base_dto.get_random_uid(), "", "", "", "", "", "", "")
    @classmethod
    def random_write(cls):
        return cls(base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid())
    @classmethod
    def new_write(cls, competency_item_uid: str, competency_item_name: str, tenant_uid: str, competency_process_uid: str, competency_item_type_uid: str, competency_group_uid: str, account_uid: str, item_template: str):
        return cls(competency_item_uid, competency_item_name, tenant_uid, competency_process_uid, competency_item_type_uid, competency_group_uid, account_uid, item_template)
    @classmethod
    def new_write_with_defaults(cls, competency_item_uid: str = "", competency_item_name: str = "", tenant_uid: str = "", competency_process_uid: str = "", competency_item_type_uid: str = "", competency_group_uid: str = "", account_uid: str = "", item_template: str = ""):
        return cls(competency_item_uid, competency_item_name, tenant_uid, competency_process_uid, competency_item_type_uid, competency_group_uid, account_uid, item_template)
    @classmethod
    def new_write_random_uid(cls, competency_item_name: str, tenant_uid: str, competency_process_uid: str, competency_item_type_uid: str, competency_group_uid: str, account_uid: str, item_template: str):
        return cls(base_dto.get_random_uid(), competency_item_name, tenant_uid, competency_process_uid, competency_item_type_uid, competency_group_uid, account_uid, item_template)
    @classmethod
    def get_class_model(cls) -> base_model:
        return db_models.competency_item_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["competency_item_uid"], d["competency_item_name"], d["tenant_uid"], d["competency_process_uid"], d["competency_item_type_uid"], d["competency_group_uid"], d["account_uid"], d["item_template"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return competency_item_write_dto(self.competency_item_uid, self.competency_item_name, self.tenant_uid, self.competency_process_uid, self.competency_item_type_uid, self.competency_group_uid, self.account_uid, self.item_template, self.custom_attributes)
    def clone_write_new_uid(self):
        return competency_item_write_dto(base_dto.get_random_uid(), self.competency_item_name, self.tenant_uid, self.competency_process_uid, self.competency_item_type_uid, self.competency_group_uid, self.account_uid, self.item_template, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return competency_item_write_dto(uid, self.competency_item_name, self.tenant_uid, self.competency_process_uid, self.competency_item_type_uid, self.competency_group_uid, self.account_uid, self.item_template, self.custom_attributes)
    def get_model(self) -> base_model:
        return db_models.competency_item_model
    def get_uid(self) -> str:
        return self.competency_item_uid
    def get_name(self) -> str:
        return self.competency_item_name
    def get_list_values(self) -> list[any]:
        return [self.competency_item_uid, self.competency_item_name, self.tenant_uid, self.competency_process_uid, self.competency_item_type_uid, self.competency_group_uid, self.account_uid, self.item_template, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.competency_item_uid, self.competency_item_name, self.tenant_uid, self.competency_process_uid, self.competency_item_type_uid, self.competency_group_uid, self.account_uid, self.item_template]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.competency_item_name, self.tenant_uid, self.competency_process_uid, self.competency_item_type_uid, self.competency_group_uid, self.account_uid, self.item_template, self.custom_attributes, updated_by, self.competency_item_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.competency_item_uid, self.competency_item_name, self.tenant_uid, self.competency_process_uid, self.competency_item_type_uid, self.competency_group_uid, self.account_uid, self.item_template, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.competency_item_name, self.tenant_uid, self.competency_process_uid, self.competency_item_type_uid, self.competency_group_uid, self.account_uid, self.item_template]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.competency_item_name, self.tenant_uid, self.competency_process_uid, self.competency_item_type_uid, self.competency_group_uid, self.account_uid, self.item_template, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_uid() == obj.get_uid()
    def update_uid(self, uid: str):
        self.competency_item_uid = uid
    def update_uid_attributes(self, competency_item_uid: str, competency_item_name: str, tenant_uid: str, competency_process_uid: str, competency_item_type_uid: str, competency_group_uid: str, account_uid: str, item_template: str):
        self.competency_item_uid = competency_item_uid
        self.competency_item_name = competency_item_name
        self.tenant_uid = tenant_uid
        self.competency_process_uid = competency_process_uid
        self.competency_item_type_uid = competency_item_type_uid
        self.competency_group_uid = competency_group_uid
        self.account_uid = account_uid
        self.item_template = item_template
    def update_attributes(self, competency_item_name: str, tenant_uid: str, competency_process_uid: str, competency_item_type_uid: str, competency_group_uid: str, account_uid: str, item_template: str):
        self.competency_item_name = competency_item_name
        self.tenant_uid = tenant_uid
        self.competency_process_uid = competency_process_uid
        self.competency_item_type_uid = competency_item_type_uid
        self.competency_group_uid = competency_group_uid
        self.account_uid = account_uid
        self.item_template = item_template


@dataclass(frozen=False)
class competency_item_account_write_dto(base_write_dto):
    competency_item_account_uid: str
    competency_item_account_name: str
    tenant_uid: str
    competency_process_account_uid: str
    competency_group_account_uid: str
    competency_item_uid: str
    account_uid: str
    start_date: datetime.datetime
    end_date: datetime.datetime | None
    item_title: str | None
    item_content: str | None
    item_value: str | None
    competency_ranking_uid: str
    def __init__(self, competency_item_account_uid: str, competency_item_account_name: str, tenant_uid: str, competency_process_account_uid: str, competency_group_account_uid: str, competency_item_uid: str, account_uid: str, start_date: datetime.datetime, end_date: datetime.datetime | None, item_title: str | None, item_content: str | None, item_value: str | None, competency_ranking_uid: str, custom_attributes: str = "{}"):
        self.competency_item_account_uid = competency_item_account_uid
        self.competency_item_account_name = competency_item_account_name
        self.tenant_uid = tenant_uid
        self.competency_process_account_uid = competency_process_account_uid
        self.competency_group_account_uid = competency_group_account_uid
        self.competency_item_uid = competency_item_uid
        self.account_uid = account_uid
        self.start_date = start_date
        self.end_date = end_date
        self.item_title = item_title
        self.item_content = item_content
        self.item_value = item_value
        self.competency_ranking_uid = competency_ranking_uid
        self.custom_attributes = custom_attributes
    @classmethod
    def empty_write(cls):
        return cls("", "", "", "", "", "", "", datetime.datetime.now(), datetime.datetime.now(), "", "", "", "")
    @classmethod
    def default_write(cls):
        return cls(base_dto.get_random_uid(), "", "", "", "", "", "", datetime.datetime.now(), datetime.datetime.now(), "", "", "", "")
    @classmethod
    def random_write(cls):
        return cls(base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), datetime.datetime.now(), datetime.datetime.now(), base_dto.get_random_uid(), base_dto.get_random_uid(), "", base_dto.get_random_uid())
    @classmethod
    def new_write(cls, competency_item_account_uid: str, competency_item_account_name: str, tenant_uid: str, competency_process_account_uid: str, competency_group_account_uid: str, competency_item_uid: str, account_uid: str, start_date: datetime.datetime, end_date: datetime.datetime | None, item_title: str | None, item_content: str | None, item_value: str | None, competency_ranking_uid: str):
        return cls(competency_item_account_uid, competency_item_account_name, tenant_uid, competency_process_account_uid, competency_group_account_uid, competency_item_uid, account_uid, start_date, end_date, item_title, item_content, item_value, competency_ranking_uid)
    @classmethod
    def new_write_with_defaults(cls, competency_item_account_uid: str = "", competency_item_account_name: str = "", tenant_uid: str = "", competency_process_account_uid: str = "", competency_group_account_uid: str = "", competency_item_uid: str = "", account_uid: str = "", start_date: datetime.datetime = datetime.datetime.now(), end_date: datetime.datetime | None = datetime.datetime.now(), item_title: str | None = "", item_content: str | None = "", item_value: str | None = "", competency_ranking_uid: str = ""):
        return cls(competency_item_account_uid, competency_item_account_name, tenant_uid, competency_process_account_uid, competency_group_account_uid, competency_item_uid, account_uid, start_date, end_date, item_title, item_content, item_value, competency_ranking_uid)
    @classmethod
    def new_write_random_uid(cls, competency_item_account_name: str, tenant_uid: str, competency_process_account_uid: str, competency_group_account_uid: str, competency_item_uid: str, account_uid: str, start_date: datetime.datetime, end_date: datetime.datetime | None, item_title: str | None, item_content: str | None, item_value: str | None, competency_ranking_uid: str):
        return cls(base_dto.get_random_uid(), competency_item_account_name, tenant_uid, competency_process_account_uid, competency_group_account_uid, competency_item_uid, account_uid, start_date, end_date, item_title, item_content, item_value, competency_ranking_uid)
    @classmethod
    def get_class_model(cls) -> base_model:
        return db_models.competency_item_account_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["competency_item_account_uid"], d["competency_item_account_name"], d["tenant_uid"], d["competency_process_account_uid"], d["competency_group_account_uid"], d["competency_item_uid"], d["account_uid"], d["start_date"], d["end_date"], d["item_title"], d["item_content"], d["item_value"], d["competency_ranking_uid"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return competency_item_account_write_dto(self.competency_item_account_uid, self.competency_item_account_name, self.tenant_uid, self.competency_process_account_uid, self.competency_group_account_uid, self.competency_item_uid, self.account_uid, self.start_date, self.end_date, self.item_title, self.item_content, self.item_value, self.competency_ranking_uid, self.custom_attributes)
    def clone_write_new_uid(self):
        return competency_item_account_write_dto(base_dto.get_random_uid(), self.competency_item_account_name, self.tenant_uid, self.competency_process_account_uid, self.competency_group_account_uid, self.competency_item_uid, self.account_uid, self.start_date, self.end_date, self.item_title, self.item_content, self.item_value, self.competency_ranking_uid, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return competency_item_account_write_dto(uid, self.competency_item_account_name, self.tenant_uid, self.competency_process_account_uid, self.competency_group_account_uid, self.competency_item_uid, self.account_uid, self.start_date, self.end_date, self.item_title, self.item_content, self.item_value, self.competency_ranking_uid, self.custom_attributes)
    def get_model(self) -> base_model:
        return db_models.competency_item_account_model
    def get_uid(self) -> str:
        return self.competency_item_account_uid
    def get_name(self) -> str:
        return self.competency_item_account_name
    def get_list_values(self) -> list[any]:
        return [self.competency_item_account_uid, self.competency_item_account_name, self.tenant_uid, self.competency_process_account_uid, self.competency_group_account_uid, self.competency_item_uid, self.account_uid, self.start_date, self.end_date, self.item_title, self.item_content, self.item_value, self.competency_ranking_uid, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.competency_item_account_uid, self.competency_item_account_name, self.tenant_uid, self.competency_process_account_uid, self.competency_group_account_uid, self.competency_item_uid, self.account_uid, self.start_date, self.end_date, self.item_title, self.item_content, self.item_value, self.competency_ranking_uid]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.competency_item_account_name, self.tenant_uid, self.competency_process_account_uid, self.competency_group_account_uid, self.competency_item_uid, self.account_uid, self.start_date, self.end_date, self.item_title, self.item_content, self.item_value, self.competency_ranking_uid, self.custom_attributes, updated_by, self.competency_item_account_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.competency_item_account_uid, self.competency_item_account_name, self.tenant_uid, self.competency_process_account_uid, self.competency_group_account_uid, self.competency_item_uid, self.account_uid, self.start_date, self.end_date, self.item_title, self.item_content, self.item_value, self.competency_ranking_uid, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.competency_item_account_name, self.tenant_uid, self.competency_process_account_uid, self.competency_group_account_uid, self.competency_item_uid, self.account_uid, self.start_date, self.end_date, self.item_title, self.item_content, self.item_value, self.competency_ranking_uid]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.competency_item_account_name, self.tenant_uid, self.competency_process_account_uid, self.competency_group_account_uid, self.competency_item_uid, self.account_uid, self.start_date, self.end_date, self.item_title, self.item_content, self.item_value, self.competency_ranking_uid, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_uid() == obj.get_uid()
    def update_uid(self, uid: str):
        self.competency_item_account_uid = uid
    def update_uid_attributes(self, competency_item_account_uid: str, competency_item_account_name: str, tenant_uid: str, competency_process_account_uid: str, competency_group_account_uid: str, competency_item_uid: str, account_uid: str, start_date: datetime.datetime, end_date: datetime.datetime | None, item_title: str | None, item_content: str | None, item_value: str | None, competency_ranking_uid: str):
        self.competency_item_account_uid = competency_item_account_uid
        self.competency_item_account_name = competency_item_account_name
        self.tenant_uid = tenant_uid
        self.competency_process_account_uid = competency_process_account_uid
        self.competency_group_account_uid = competency_group_account_uid
        self.competency_item_uid = competency_item_uid
        self.account_uid = account_uid
        self.start_date = start_date
        self.end_date = end_date
        self.item_title = item_title
        self.item_content = item_content
        self.item_value = item_value
        self.competency_ranking_uid = competency_ranking_uid
    def update_attributes(self, competency_item_account_name: str, tenant_uid: str, competency_process_account_uid: str, competency_group_account_uid: str, competency_item_uid: str, account_uid: str, start_date: datetime.datetime, end_date: datetime.datetime | None, item_title: str | None, item_content: str | None, item_value: str | None, competency_ranking_uid: str):
        self.competency_item_account_name = competency_item_account_name
        self.tenant_uid = tenant_uid
        self.competency_process_account_uid = competency_process_account_uid
        self.competency_group_account_uid = competency_group_account_uid
        self.competency_item_uid = competency_item_uid
        self.account_uid = account_uid
        self.start_date = start_date
        self.end_date = end_date
        self.item_title = item_title
        self.item_content = item_content
        self.item_value = item_value
        self.competency_ranking_uid = competency_ranking_uid


@dataclass(frozen=False)
class competency_item_type_write_dto(base_write_dto):
    competency_item_type_uid: str
    competency_item_type_name: str
    tenant_uid: str
    def __init__(self, competency_item_type_uid: str, competency_item_type_name: str, tenant_uid: str, custom_attributes: str = "{}"):
        self.competency_item_type_uid = competency_item_type_uid
        self.competency_item_type_name = competency_item_type_name
        self.tenant_uid = tenant_uid
        self.custom_attributes = custom_attributes
    @classmethod
    def empty_write(cls):
        return cls("", "", "")
    @classmethod
    def default_write(cls):
        return cls(base_dto.get_random_uid(), "", "")
    @classmethod
    def random_write(cls):
        return cls(base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid())
    @classmethod
    def new_write(cls, competency_item_type_uid: str, competency_item_type_name: str, tenant_uid: str):
        return cls(competency_item_type_uid, competency_item_type_name, tenant_uid)
    @classmethod
    def new_write_with_defaults(cls, competency_item_type_uid: str = "", competency_item_type_name: str = "", tenant_uid: str = ""):
        return cls(competency_item_type_uid, competency_item_type_name, tenant_uid)
    @classmethod
    def new_write_random_uid(cls, competency_item_type_name: str, tenant_uid: str):
        return cls(base_dto.get_random_uid(), competency_item_type_name, tenant_uid)
    @classmethod
    def get_class_model(cls) -> base_model:
        return db_models.competency_item_type_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["competency_item_type_uid"], d["competency_item_type_name"], d["tenant_uid"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return competency_item_type_write_dto(self.competency_item_type_uid, self.competency_item_type_name, self.tenant_uid, self.custom_attributes)
    def clone_write_new_uid(self):
        return competency_item_type_write_dto(base_dto.get_random_uid(), self.competency_item_type_name, self.tenant_uid, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return competency_item_type_write_dto(uid, self.competency_item_type_name, self.tenant_uid, self.custom_attributes)
    def get_model(self) -> base_model:
        return db_models.competency_item_type_model
    def get_uid(self) -> str:
        return self.competency_item_type_uid
    def get_name(self) -> str:
        return self.competency_item_type_name
    def get_list_values(self) -> list[any]:
        return [self.competency_item_type_uid, self.competency_item_type_name, self.tenant_uid, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.competency_item_type_uid, self.competency_item_type_name, self.tenant_uid]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.competency_item_type_name, self.tenant_uid, self.custom_attributes, updated_by, self.competency_item_type_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.competency_item_type_uid, self.competency_item_type_name, self.tenant_uid, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.competency_item_type_name, self.tenant_uid]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.competency_item_type_name, self.tenant_uid, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_uid() == obj.get_uid()
    def update_uid(self, uid: str):
        self.competency_item_type_uid = uid
    def update_uid_attributes(self, competency_item_type_uid: str, competency_item_type_name: str, tenant_uid: str):
        self.competency_item_type_uid = competency_item_type_uid
        self.competency_item_type_name = competency_item_type_name
        self.tenant_uid = tenant_uid
    def update_attributes(self, competency_item_type_name: str, tenant_uid: str):
        self.competency_item_type_name = competency_item_type_name
        self.tenant_uid = tenant_uid


@dataclass(frozen=False)
class competency_process_write_dto(base_write_dto):
    competency_process_uid: str
    competency_process_name: str
    competency_process_type_uid: str
    tenant_uid: str
    account_group_uid: str
    is_required: int
    process_description: str
    due_date: datetime.datetime
    def __init__(self, competency_process_uid: str, competency_process_name: str, competency_process_type_uid: str, tenant_uid: str, account_group_uid: str, is_required: int, process_description: str, due_date: datetime.datetime, custom_attributes: str = "{}"):
        self.competency_process_uid = competency_process_uid
        self.competency_process_name = competency_process_name
        self.competency_process_type_uid = competency_process_type_uid
        self.tenant_uid = tenant_uid
        self.account_group_uid = account_group_uid
        self.is_required = is_required
        self.process_description = process_description
        self.due_date = due_date
        self.custom_attributes = custom_attributes
    @classmethod
    def empty_write(cls):
        return cls("", "", "", "", "", 0, "", datetime.datetime.now())
    @classmethod
    def default_write(cls):
        return cls(base_dto.get_random_uid(), "", "", "", "", 0, "", datetime.datetime.now())
    @classmethod
    def random_write(cls):
        return cls(base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), 0, base_dto.get_random_uid(), datetime.datetime.now())
    @classmethod
    def new_write(cls, competency_process_uid: str, competency_process_name: str, competency_process_type_uid: str, tenant_uid: str, account_group_uid: str, is_required: int, process_description: str, due_date: datetime.datetime):
        return cls(competency_process_uid, competency_process_name, competency_process_type_uid, tenant_uid, account_group_uid, is_required, process_description, due_date)
    @classmethod
    def new_write_with_defaults(cls, competency_process_uid: str = "", competency_process_name: str = "", competency_process_type_uid: str = "", tenant_uid: str = "", account_group_uid: str = "", is_required: int = 0, process_description: str = "", due_date: datetime.datetime = datetime.datetime.now()):
        return cls(competency_process_uid, competency_process_name, competency_process_type_uid, tenant_uid, account_group_uid, is_required, process_description, due_date)
    @classmethod
    def new_write_random_uid(cls, competency_process_name: str, competency_process_type_uid: str, tenant_uid: str, account_group_uid: str, is_required: int, process_description: str, due_date: datetime.datetime):
        return cls(base_dto.get_random_uid(), competency_process_name, competency_process_type_uid, tenant_uid, account_group_uid, is_required, process_description, due_date)
    @classmethod
    def get_class_model(cls) -> base_model:
        return db_models.competency_process_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["competency_process_uid"], d["competency_process_name"], d["competency_process_type_uid"], d["tenant_uid"], d["account_group_uid"], d["is_required"], d["process_description"], d["due_date"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return competency_process_write_dto(self.competency_process_uid, self.competency_process_name, self.competency_process_type_uid, self.tenant_uid, self.account_group_uid, self.is_required, self.process_description, self.due_date, self.custom_attributes)
    def clone_write_new_uid(self):
        return competency_process_write_dto(base_dto.get_random_uid(), self.competency_process_name, self.competency_process_type_uid, self.tenant_uid, self.account_group_uid, self.is_required, self.process_description, self.due_date, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return competency_process_write_dto(uid, self.competency_process_name, self.competency_process_type_uid, self.tenant_uid, self.account_group_uid, self.is_required, self.process_description, self.due_date, self.custom_attributes)
    def get_model(self) -> base_model:
        return db_models.competency_process_model
    def get_uid(self) -> str:
        return self.competency_process_uid
    def get_name(self) -> str:
        return self.competency_process_name
    def get_list_values(self) -> list[any]:
        return [self.competency_process_uid, self.competency_process_name, self.competency_process_type_uid, self.tenant_uid, self.account_group_uid, self.is_required, self.process_description, self.due_date, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.competency_process_uid, self.competency_process_name, self.competency_process_type_uid, self.tenant_uid, self.account_group_uid, self.is_required, self.process_description, self.due_date]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.competency_process_name, self.competency_process_type_uid, self.tenant_uid, self.account_group_uid, self.is_required, self.process_description, self.due_date, self.custom_attributes, updated_by, self.competency_process_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.competency_process_uid, self.competency_process_name, self.competency_process_type_uid, self.tenant_uid, self.account_group_uid, self.is_required, self.process_description, self.due_date, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.competency_process_name, self.competency_process_type_uid, self.tenant_uid, self.account_group_uid, self.is_required, self.process_description, self.due_date]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.competency_process_name, self.competency_process_type_uid, self.tenant_uid, self.account_group_uid, self.is_required, self.process_description, self.due_date, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_uid() == obj.get_uid()
    def update_uid(self, uid: str):
        self.competency_process_uid = uid
    def update_uid_attributes(self, competency_process_uid: str, competency_process_name: str, competency_process_type_uid: str, tenant_uid: str, account_group_uid: str, is_required: int, process_description: str, due_date: datetime.datetime):
        self.competency_process_uid = competency_process_uid
        self.competency_process_name = competency_process_name
        self.competency_process_type_uid = competency_process_type_uid
        self.tenant_uid = tenant_uid
        self.account_group_uid = account_group_uid
        self.is_required = is_required
        self.process_description = process_description
        self.due_date = due_date
    def update_attributes(self, competency_process_name: str, competency_process_type_uid: str, tenant_uid: str, account_group_uid: str, is_required: int, process_description: str, due_date: datetime.datetime):
        self.competency_process_name = competency_process_name
        self.competency_process_type_uid = competency_process_type_uid
        self.tenant_uid = tenant_uid
        self.account_group_uid = account_group_uid
        self.is_required = is_required
        self.process_description = process_description
        self.due_date = due_date


@dataclass(frozen=False)
class competency_process_account_write_dto(base_write_dto):
    competency_process_account_uid: str
    competency_process_account_name: str
    tenant_uid: str
    competency_process_uid: str
    account_uid: str
    start_date: datetime.datetime
    due_date: datetime.datetime
    end_date: datetime.datetime | None
    is_closed: int
    final_result: str | None
    def __init__(self, competency_process_account_uid: str, competency_process_account_name: str, tenant_uid: str, competency_process_uid: str, account_uid: str, start_date: datetime.datetime, due_date: datetime.datetime, end_date: datetime.datetime | None, is_closed: int, final_result: str | None, custom_attributes: str = "{}"):
        self.competency_process_account_uid = competency_process_account_uid
        self.competency_process_account_name = competency_process_account_name
        self.tenant_uid = tenant_uid
        self.competency_process_uid = competency_process_uid
        self.account_uid = account_uid
        self.start_date = start_date
        self.due_date = due_date
        self.end_date = end_date
        self.is_closed = is_closed
        self.final_result = final_result
        self.custom_attributes = custom_attributes
    @classmethod
    def empty_write(cls):
        return cls("", "", "", "", "", datetime.datetime.now(), datetime.datetime.now(), datetime.datetime.now(), 0, "")
    @classmethod
    def default_write(cls):
        return cls(base_dto.get_random_uid(), "", "", "", "", datetime.datetime.now(), datetime.datetime.now(), datetime.datetime.now(), 0, "")
    @classmethod
    def random_write(cls):
        return cls(base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), datetime.datetime.now(), datetime.datetime.now(), datetime.datetime.now(), 0, base_dto.get_random_uid())
    @classmethod
    def new_write(cls, competency_process_account_uid: str, competency_process_account_name: str, tenant_uid: str, competency_process_uid: str, account_uid: str, start_date: datetime.datetime, due_date: datetime.datetime, end_date: datetime.datetime | None, is_closed: int, final_result: str | None):
        return cls(competency_process_account_uid, competency_process_account_name, tenant_uid, competency_process_uid, account_uid, start_date, due_date, end_date, is_closed, final_result)
    @classmethod
    def new_write_with_defaults(cls, competency_process_account_uid: str = "", competency_process_account_name: str = "", tenant_uid: str = "", competency_process_uid: str = "", account_uid: str = "", start_date: datetime.datetime = datetime.datetime.now(), due_date: datetime.datetime = datetime.datetime.now(), end_date: datetime.datetime | None = datetime.datetime.now(), is_closed: int = 0, final_result: str | None = ""):
        return cls(competency_process_account_uid, competency_process_account_name, tenant_uid, competency_process_uid, account_uid, start_date, due_date, end_date, is_closed, final_result)
    @classmethod
    def new_write_random_uid(cls, competency_process_account_name: str, tenant_uid: str, competency_process_uid: str, account_uid: str, start_date: datetime.datetime, due_date: datetime.datetime, end_date: datetime.datetime | None, is_closed: int, final_result: str | None):
        return cls(base_dto.get_random_uid(), competency_process_account_name, tenant_uid, competency_process_uid, account_uid, start_date, due_date, end_date, is_closed, final_result)
    @classmethod
    def get_class_model(cls) -> base_model:
        return db_models.competency_process_account_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["competency_process_account_uid"], d["competency_process_account_name"], d["tenant_uid"], d["competency_process_uid"], d["account_uid"], d["start_date"], d["due_date"], d["end_date"], d["is_closed"], d["final_result"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return competency_process_account_write_dto(self.competency_process_account_uid, self.competency_process_account_name, self.tenant_uid, self.competency_process_uid, self.account_uid, self.start_date, self.due_date, self.end_date, self.is_closed, self.final_result, self.custom_attributes)
    def clone_write_new_uid(self):
        return competency_process_account_write_dto(base_dto.get_random_uid(), self.competency_process_account_name, self.tenant_uid, self.competency_process_uid, self.account_uid, self.start_date, self.due_date, self.end_date, self.is_closed, self.final_result, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return competency_process_account_write_dto(uid, self.competency_process_account_name, self.tenant_uid, self.competency_process_uid, self.account_uid, self.start_date, self.due_date, self.end_date, self.is_closed, self.final_result, self.custom_attributes)
    def get_model(self) -> base_model:
        return db_models.competency_process_account_model
    def get_uid(self) -> str:
        return self.competency_process_account_uid
    def get_name(self) -> str:
        return self.competency_process_account_name
    def get_list_values(self) -> list[any]:
        return [self.competency_process_account_uid, self.competency_process_account_name, self.tenant_uid, self.competency_process_uid, self.account_uid, self.start_date, self.due_date, self.end_date, self.is_closed, self.final_result, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.competency_process_account_uid, self.competency_process_account_name, self.tenant_uid, self.competency_process_uid, self.account_uid, self.start_date, self.due_date, self.end_date, self.is_closed, self.final_result]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.competency_process_account_name, self.tenant_uid, self.competency_process_uid, self.account_uid, self.start_date, self.due_date, self.end_date, self.is_closed, self.final_result, self.custom_attributes, updated_by, self.competency_process_account_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.competency_process_account_uid, self.competency_process_account_name, self.tenant_uid, self.competency_process_uid, self.account_uid, self.start_date, self.due_date, self.end_date, self.is_closed, self.final_result, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.competency_process_account_name, self.tenant_uid, self.competency_process_uid, self.account_uid, self.start_date, self.due_date, self.end_date, self.is_closed, self.final_result]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.competency_process_account_name, self.tenant_uid, self.competency_process_uid, self.account_uid, self.start_date, self.due_date, self.end_date, self.is_closed, self.final_result, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_uid() == obj.get_uid()
    def update_uid(self, uid: str):
        self.competency_process_account_uid = uid
    def update_uid_attributes(self, competency_process_account_uid: str, competency_process_account_name: str, tenant_uid: str, competency_process_uid: str, account_uid: str, start_date: datetime.datetime, due_date: datetime.datetime, end_date: datetime.datetime | None, is_closed: int, final_result: str | None):
        self.competency_process_account_uid = competency_process_account_uid
        self.competency_process_account_name = competency_process_account_name
        self.tenant_uid = tenant_uid
        self.competency_process_uid = competency_process_uid
        self.account_uid = account_uid
        self.start_date = start_date
        self.due_date = due_date
        self.end_date = end_date
        self.is_closed = is_closed
        self.final_result = final_result
    def update_attributes(self, competency_process_account_name: str, tenant_uid: str, competency_process_uid: str, account_uid: str, start_date: datetime.datetime, due_date: datetime.datetime, end_date: datetime.datetime | None, is_closed: int, final_result: str | None):
        self.competency_process_account_name = competency_process_account_name
        self.tenant_uid = tenant_uid
        self.competency_process_uid = competency_process_uid
        self.account_uid = account_uid
        self.start_date = start_date
        self.due_date = due_date
        self.end_date = end_date
        self.is_closed = is_closed
        self.final_result = final_result


@dataclass(frozen=False)
class competency_process_type_write_dto(base_write_dto):
    competency_process_type_uid: str
    competency_process_type_name: str
    competency_class_name: str
    def __init__(self, competency_process_type_uid: str, competency_process_type_name: str, competency_class_name: str, custom_attributes: str = "{}"):
        self.competency_process_type_uid = competency_process_type_uid
        self.competency_process_type_name = competency_process_type_name
        self.competency_class_name = competency_class_name
        self.custom_attributes = custom_attributes
    @classmethod
    def empty_write(cls):
        return cls("", "", "")
    @classmethod
    def default_write(cls):
        return cls(base_dto.get_random_uid(), "", "")
    @classmethod
    def random_write(cls):
        return cls(base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid())
    @classmethod
    def new_write(cls, competency_process_type_uid: str, competency_process_type_name: str, competency_class_name: str):
        return cls(competency_process_type_uid, competency_process_type_name, competency_class_name)
    @classmethod
    def new_write_with_defaults(cls, competency_process_type_uid: str = "", competency_process_type_name: str = "", competency_class_name: str = ""):
        return cls(competency_process_type_uid, competency_process_type_name, competency_class_name)
    @classmethod
    def new_write_random_uid(cls, competency_process_type_name: str, competency_class_name: str):
        return cls(base_dto.get_random_uid(), competency_process_type_name, competency_class_name)
    @classmethod
    def get_class_model(cls) -> base_model:
        return db_models.competency_process_type_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["competency_process_type_uid"], d["competency_process_type_name"], d["competency_class_name"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return competency_process_type_write_dto(self.competency_process_type_uid, self.competency_process_type_name, self.competency_class_name, self.custom_attributes)
    def clone_write_new_uid(self):
        return competency_process_type_write_dto(base_dto.get_random_uid(), self.competency_process_type_name, self.competency_class_name, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return competency_process_type_write_dto(uid, self.competency_process_type_name, self.competency_class_name, self.custom_attributes)
    def get_model(self) -> base_model:
        return db_models.competency_process_type_model
    def get_uid(self) -> str:
        return self.competency_process_type_uid
    def get_name(self) -> str:
        return self.competency_process_type_name
    def get_list_values(self) -> list[any]:
        return [self.competency_process_type_uid, self.competency_process_type_name, self.competency_class_name, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.competency_process_type_uid, self.competency_process_type_name, self.competency_class_name]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.competency_process_type_name, self.competency_class_name, self.custom_attributes, updated_by, self.competency_process_type_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.competency_process_type_uid, self.competency_process_type_name, self.competency_class_name, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.competency_process_type_name, self.competency_class_name]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.competency_process_type_name, self.competency_class_name, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_uid() == obj.get_uid()
    def update_uid(self, uid: str):
        self.competency_process_type_uid = uid
    def update_uid_attributes(self, competency_process_type_uid: str, competency_process_type_name: str, competency_class_name: str):
        self.competency_process_type_uid = competency_process_type_uid
        self.competency_process_type_name = competency_process_type_name
        self.competency_class_name = competency_class_name
    def update_attributes(self, competency_process_type_name: str, competency_class_name: str):
        self.competency_process_type_name = competency_process_type_name
        self.competency_class_name = competency_class_name


@dataclass(frozen=False)
class competency_ranking_write_dto(base_write_dto):
    competency_ranking_uid: str
    competency_ranking_name: str
    tenant_uid: str
    competency_group_uid: str
    def __init__(self, competency_ranking_uid: str, competency_ranking_name: str, tenant_uid: str, competency_group_uid: str, custom_attributes: str = "{}"):
        self.competency_ranking_uid = competency_ranking_uid
        self.competency_ranking_name = competency_ranking_name
        self.tenant_uid = tenant_uid
        self.competency_group_uid = competency_group_uid
        self.custom_attributes = custom_attributes
    @classmethod
    def empty_write(cls):
        return cls("", "", "", "")
    @classmethod
    def default_write(cls):
        return cls(base_dto.get_random_uid(), "", "", "")
    @classmethod
    def random_write(cls):
        return cls(base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid())
    @classmethod
    def new_write(cls, competency_ranking_uid: str, competency_ranking_name: str, tenant_uid: str, competency_group_uid: str):
        return cls(competency_ranking_uid, competency_ranking_name, tenant_uid, competency_group_uid)
    @classmethod
    def new_write_with_defaults(cls, competency_ranking_uid: str = "", competency_ranking_name: str = "", tenant_uid: str = "", competency_group_uid: str = ""):
        return cls(competency_ranking_uid, competency_ranking_name, tenant_uid, competency_group_uid)
    @classmethod
    def new_write_random_uid(cls, competency_ranking_name: str, tenant_uid: str, competency_group_uid: str):
        return cls(base_dto.get_random_uid(), competency_ranking_name, tenant_uid, competency_group_uid)
    @classmethod
    def get_class_model(cls) -> base_model:
        return db_models.competency_ranking_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["competency_ranking_uid"], d["competency_ranking_name"], d["tenant_uid"], d["competency_group_uid"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return competency_ranking_write_dto(self.competency_ranking_uid, self.competency_ranking_name, self.tenant_uid, self.competency_group_uid, self.custom_attributes)
    def clone_write_new_uid(self):
        return competency_ranking_write_dto(base_dto.get_random_uid(), self.competency_ranking_name, self.tenant_uid, self.competency_group_uid, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return competency_ranking_write_dto(uid, self.competency_ranking_name, self.tenant_uid, self.competency_group_uid, self.custom_attributes)
    def get_model(self) -> base_model:
        return db_models.competency_ranking_model
    def get_uid(self) -> str:
        return self.competency_ranking_uid
    def get_name(self) -> str:
        return self.competency_ranking_name
    def get_list_values(self) -> list[any]:
        return [self.competency_ranking_uid, self.competency_ranking_name, self.tenant_uid, self.competency_group_uid, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.competency_ranking_uid, self.competency_ranking_name, self.tenant_uid, self.competency_group_uid]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.competency_ranking_name, self.tenant_uid, self.competency_group_uid, self.custom_attributes, updated_by, self.competency_ranking_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.competency_ranking_uid, self.competency_ranking_name, self.tenant_uid, self.competency_group_uid, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.competency_ranking_name, self.tenant_uid, self.competency_group_uid]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.competency_ranking_name, self.tenant_uid, self.competency_group_uid, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_uid() == obj.get_uid()
    def update_uid(self, uid: str):
        self.competency_ranking_uid = uid
    def update_uid_attributes(self, competency_ranking_uid: str, competency_ranking_name: str, tenant_uid: str, competency_group_uid: str):
        self.competency_ranking_uid = competency_ranking_uid
        self.competency_ranking_name = competency_ranking_name
        self.tenant_uid = tenant_uid
        self.competency_group_uid = competency_group_uid
    def update_attributes(self, competency_ranking_name: str, tenant_uid: str, competency_group_uid: str):
        self.competency_ranking_name = competency_ranking_name
        self.tenant_uid = tenant_uid
        self.competency_group_uid = competency_group_uid


@dataclass(frozen=False)
class connection_engine_write_dto(base_write_dto):
    connection_engine_uid: str
    connection_engine_name: str
    start_date: datetime.datetime | None
    calls_count: int
    last_time: int
    host_count: int
    user_count: int
    token_count: int
    def __init__(self, connection_engine_uid: str, connection_engine_name: str, start_date: datetime.datetime | None, calls_count: int, last_time: int, host_count: int, user_count: int, token_count: int, custom_attributes: str = "{}"):
        self.connection_engine_uid = connection_engine_uid
        self.connection_engine_name = connection_engine_name
        self.start_date = start_date
        self.calls_count = calls_count
        self.last_time = last_time
        self.host_count = host_count
        self.user_count = user_count
        self.token_count = token_count
        self.custom_attributes = custom_attributes
    @classmethod
    def empty_write(cls):
        return cls("", "", datetime.datetime.now(), 0, 0, 0, 0, 0)
    @classmethod
    def default_write(cls):
        return cls(base_dto.get_random_uid(), "", datetime.datetime.now(), 0, 0, 0, 0, 0)
    @classmethod
    def random_write(cls):
        return cls(base_dto.get_random_uid(), base_dto.get_random_uid(), datetime.datetime.now(), 0, 0, 0, 0, 0)
    @classmethod
    def new_write(cls, connection_engine_uid: str, connection_engine_name: str, start_date: datetime.datetime | None, calls_count: int, last_time: int, host_count: int, user_count: int, token_count: int):
        return cls(connection_engine_uid, connection_engine_name, start_date, calls_count, last_time, host_count, user_count, token_count)
    @classmethod
    def new_write_with_defaults(cls, connection_engine_uid: str = "", connection_engine_name: str = "", start_date: datetime.datetime | None = datetime.datetime.now(), calls_count: int = 0, last_time: int = 0, host_count: int = 0, user_count: int = 0, token_count: int = 0):
        return cls(connection_engine_uid, connection_engine_name, start_date, calls_count, last_time, host_count, user_count, token_count)
    @classmethod
    def new_write_random_uid(cls, connection_engine_name: str, start_date: datetime.datetime | None, calls_count: int, last_time: int, host_count: int, user_count: int, token_count: int):
        return cls(base_dto.get_random_uid(), connection_engine_name, start_date, calls_count, last_time, host_count, user_count, token_count)
    @classmethod
    def get_class_model(cls) -> base_model:
        return db_models.connection_engine_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["connection_engine_uid"], d["connection_engine_name"], d["start_date"], d["calls_count"], d["last_time"], d["host_count"], d["user_count"], d["token_count"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return connection_engine_write_dto(self.connection_engine_uid, self.connection_engine_name, self.start_date, self.calls_count, self.last_time, self.host_count, self.user_count, self.token_count, self.custom_attributes)
    def clone_write_new_uid(self):
        return connection_engine_write_dto(base_dto.get_random_uid(), self.connection_engine_name, self.start_date, self.calls_count, self.last_time, self.host_count, self.user_count, self.token_count, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return connection_engine_write_dto(uid, self.connection_engine_name, self.start_date, self.calls_count, self.last_time, self.host_count, self.user_count, self.token_count, self.custom_attributes)
    def get_model(self) -> base_model:
        return db_models.connection_engine_model
    def get_uid(self) -> str:
        return self.connection_engine_uid
    def get_name(self) -> str:
        return self.connection_engine_name
    def get_list_values(self) -> list[any]:
        return [self.connection_engine_uid, self.connection_engine_name, self.start_date, self.calls_count, self.last_time, self.host_count, self.user_count, self.token_count, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.connection_engine_uid, self.connection_engine_name, self.start_date, self.calls_count, self.last_time, self.host_count, self.user_count, self.token_count]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.connection_engine_name, self.start_date, self.calls_count, self.last_time, self.host_count, self.user_count, self.token_count, self.custom_attributes, updated_by, self.connection_engine_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.connection_engine_uid, self.connection_engine_name, self.start_date, self.calls_count, self.last_time, self.host_count, self.user_count, self.token_count, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.connection_engine_name, self.start_date, self.calls_count, self.last_time, self.host_count, self.user_count, self.token_count]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.connection_engine_name, self.start_date, self.calls_count, self.last_time, self.host_count, self.user_count, self.token_count, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_uid() == obj.get_uid()
    def update_uid(self, uid: str):
        self.connection_engine_uid = uid
    def update_uid_attributes(self, connection_engine_uid: str, connection_engine_name: str, start_date: datetime.datetime | None, calls_count: int, last_time: int, host_count: int, user_count: int, token_count: int):
        self.connection_engine_uid = connection_engine_uid
        self.connection_engine_name = connection_engine_name
        self.start_date = start_date
        self.calls_count = calls_count
        self.last_time = last_time
        self.host_count = host_count
        self.user_count = user_count
        self.token_count = token_count
    def update_attributes(self, connection_engine_name: str, start_date: datetime.datetime | None, calls_count: int, last_time: int, host_count: int, user_count: int, token_count: int):
        self.connection_engine_name = connection_engine_name
        self.start_date = start_date
        self.calls_count = calls_count
        self.last_time = last_time
        self.host_count = host_count
        self.user_count = user_count
        self.token_count = token_count


@dataclass(frozen=False)
class connection_host_write_dto(base_write_dto):
    connection_host_uid: str
    connection_host_name: str
    connection_engine_uid: str
    host_ip: str
    calls_count: int | None
    start_time: int
    last_call_time: int
    user_count: int
    token_count: int
    def __init__(self, connection_host_uid: str, connection_host_name: str, connection_engine_uid: str, host_ip: str, calls_count: int | None, start_time: int, last_call_time: int, user_count: int, token_count: int, custom_attributes: str = "{}"):
        self.connection_host_uid = connection_host_uid
        self.connection_host_name = connection_host_name
        self.connection_engine_uid = connection_engine_uid
        self.host_ip = host_ip
        self.calls_count = calls_count
        self.start_time = start_time
        self.last_call_time = last_call_time
        self.user_count = user_count
        self.token_count = token_count
        self.custom_attributes = custom_attributes
    @classmethod
    def empty_write(cls):
        return cls("", "", "", "", 0, 0, 0, 0, 0)
    @classmethod
    def default_write(cls):
        return cls(base_dto.get_random_uid(), "", "", "", 0, 0, 0, 0, 0)
    @classmethod
    def random_write(cls):
        return cls(base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), 0, 0, 0, 0, 0)
    @classmethod
    def new_write(cls, connection_host_uid: str, connection_host_name: str, connection_engine_uid: str, host_ip: str, calls_count: int | None, start_time: int, last_call_time: int, user_count: int, token_count: int):
        return cls(connection_host_uid, connection_host_name, connection_engine_uid, host_ip, calls_count, start_time, last_call_time, user_count, token_count)
    @classmethod
    def new_write_with_defaults(cls, connection_host_uid: str = "", connection_host_name: str = "", connection_engine_uid: str = "", host_ip: str = "", calls_count: int | None = 0, start_time: int = 0, last_call_time: int = 0, user_count: int = 0, token_count: int = 0):
        return cls(connection_host_uid, connection_host_name, connection_engine_uid, host_ip, calls_count, start_time, last_call_time, user_count, token_count)
    @classmethod
    def new_write_random_uid(cls, connection_host_name: str, connection_engine_uid: str, host_ip: str, calls_count: int | None, start_time: int, last_call_time: int, user_count: int, token_count: int):
        return cls(base_dto.get_random_uid(), connection_host_name, connection_engine_uid, host_ip, calls_count, start_time, last_call_time, user_count, token_count)
    @classmethod
    def get_class_model(cls) -> base_model:
        return db_models.connection_host_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["connection_host_uid"], d["connection_host_name"], d["connection_engine_uid"], d["host_ip"], d["calls_count"], d["start_time"], d["last_call_time"], d["user_count"], d["token_count"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return connection_host_write_dto(self.connection_host_uid, self.connection_host_name, self.connection_engine_uid, self.host_ip, self.calls_count, self.start_time, self.last_call_time, self.user_count, self.token_count, self.custom_attributes)
    def clone_write_new_uid(self):
        return connection_host_write_dto(base_dto.get_random_uid(), self.connection_host_name, self.connection_engine_uid, self.host_ip, self.calls_count, self.start_time, self.last_call_time, self.user_count, self.token_count, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return connection_host_write_dto(uid, self.connection_host_name, self.connection_engine_uid, self.host_ip, self.calls_count, self.start_time, self.last_call_time, self.user_count, self.token_count, self.custom_attributes)
    def get_model(self) -> base_model:
        return db_models.connection_host_model
    def get_uid(self) -> str:
        return self.connection_host_uid
    def get_name(self) -> str:
        return self.connection_host_name
    def get_list_values(self) -> list[any]:
        return [self.connection_host_uid, self.connection_host_name, self.connection_engine_uid, self.host_ip, self.calls_count, self.start_time, self.last_call_time, self.user_count, self.token_count, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.connection_host_uid, self.connection_host_name, self.connection_engine_uid, self.host_ip, self.calls_count, self.start_time, self.last_call_time, self.user_count, self.token_count]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.connection_host_name, self.connection_engine_uid, self.host_ip, self.calls_count, self.start_time, self.last_call_time, self.user_count, self.token_count, self.custom_attributes, updated_by, self.connection_host_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.connection_host_uid, self.connection_host_name, self.connection_engine_uid, self.host_ip, self.calls_count, self.start_time, self.last_call_time, self.user_count, self.token_count, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.connection_host_name, self.connection_engine_uid, self.host_ip, self.calls_count, self.start_time, self.last_call_time, self.user_count, self.token_count]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.connection_host_name, self.connection_engine_uid, self.host_ip, self.calls_count, self.start_time, self.last_call_time, self.user_count, self.token_count, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_uid() == obj.get_uid()
    def update_uid(self, uid: str):
        self.connection_host_uid = uid
    def update_uid_attributes(self, connection_host_uid: str, connection_host_name: str, connection_engine_uid: str, host_ip: str, calls_count: int | None, start_time: int, last_call_time: int, user_count: int, token_count: int):
        self.connection_host_uid = connection_host_uid
        self.connection_host_name = connection_host_name
        self.connection_engine_uid = connection_engine_uid
        self.host_ip = host_ip
        self.calls_count = calls_count
        self.start_time = start_time
        self.last_call_time = last_call_time
        self.user_count = user_count
        self.token_count = token_count
    def update_attributes(self, connection_host_name: str, connection_engine_uid: str, host_ip: str, calls_count: int | None, start_time: int, last_call_time: int, user_count: int, token_count: int):
        self.connection_host_name = connection_host_name
        self.connection_engine_uid = connection_engine_uid
        self.host_ip = host_ip
        self.calls_count = calls_count
        self.start_time = start_time
        self.last_call_time = last_call_time
        self.user_count = user_count
        self.token_count = token_count


@dataclass(frozen=False)
class connection_tenant_write_dto(base_write_dto):
    connection_tenant_uid: str
    connection_tenant_name: str
    tenant_uid: str
    calls_count: int
    items_count: int
    request_size: int
    response_size: int
    def __init__(self, connection_tenant_uid: str, connection_tenant_name: str, tenant_uid: str, calls_count: int, items_count: int, request_size: int, response_size: int, custom_attributes: str = "{}"):
        self.connection_tenant_uid = connection_tenant_uid
        self.connection_tenant_name = connection_tenant_name
        self.tenant_uid = tenant_uid
        self.calls_count = calls_count
        self.items_count = items_count
        self.request_size = request_size
        self.response_size = response_size
        self.custom_attributes = custom_attributes
    @classmethod
    def empty_write(cls):
        return cls("", "", "", 0, 0, 0, 0)
    @classmethod
    def default_write(cls):
        return cls(base_dto.get_random_uid(), "", "", 0, 0, 0, 0)
    @classmethod
    def random_write(cls):
        return cls(base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), 0, 0, 0, 0)
    @classmethod
    def new_write(cls, connection_tenant_uid: str, connection_tenant_name: str, tenant_uid: str, calls_count: int, items_count: int, request_size: int, response_size: int):
        return cls(connection_tenant_uid, connection_tenant_name, tenant_uid, calls_count, items_count, request_size, response_size)
    @classmethod
    def new_write_with_defaults(cls, connection_tenant_uid: str = "", connection_tenant_name: str = "", tenant_uid: str = "", calls_count: int = 0, items_count: int = 0, request_size: int = 0, response_size: int = 0):
        return cls(connection_tenant_uid, connection_tenant_name, tenant_uid, calls_count, items_count, request_size, response_size)
    @classmethod
    def new_write_random_uid(cls, connection_tenant_name: str, tenant_uid: str, calls_count: int, items_count: int, request_size: int, response_size: int):
        return cls(base_dto.get_random_uid(), connection_tenant_name, tenant_uid, calls_count, items_count, request_size, response_size)
    @classmethod
    def get_class_model(cls) -> base_model:
        return db_models.connection_tenant_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["connection_tenant_uid"], d["connection_tenant_name"], d["tenant_uid"], d["calls_count"], d["items_count"], d["request_size"], d["response_size"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return connection_tenant_write_dto(self.connection_tenant_uid, self.connection_tenant_name, self.tenant_uid, self.calls_count, self.items_count, self.request_size, self.response_size, self.custom_attributes)
    def clone_write_new_uid(self):
        return connection_tenant_write_dto(base_dto.get_random_uid(), self.connection_tenant_name, self.tenant_uid, self.calls_count, self.items_count, self.request_size, self.response_size, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return connection_tenant_write_dto(uid, self.connection_tenant_name, self.tenant_uid, self.calls_count, self.items_count, self.request_size, self.response_size, self.custom_attributes)
    def get_model(self) -> base_model:
        return db_models.connection_tenant_model
    def get_uid(self) -> str:
        return self.connection_tenant_uid
    def get_name(self) -> str:
        return self.connection_tenant_name
    def get_list_values(self) -> list[any]:
        return [self.connection_tenant_uid, self.connection_tenant_name, self.tenant_uid, self.calls_count, self.items_count, self.request_size, self.response_size, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.connection_tenant_uid, self.connection_tenant_name, self.tenant_uid, self.calls_count, self.items_count, self.request_size, self.response_size]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.connection_tenant_name, self.tenant_uid, self.calls_count, self.items_count, self.request_size, self.response_size, self.custom_attributes, updated_by, self.connection_tenant_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.connection_tenant_uid, self.connection_tenant_name, self.tenant_uid, self.calls_count, self.items_count, self.request_size, self.response_size, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.connection_tenant_name, self.tenant_uid, self.calls_count, self.items_count, self.request_size, self.response_size]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.connection_tenant_name, self.tenant_uid, self.calls_count, self.items_count, self.request_size, self.response_size, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_uid() == obj.get_uid()
    def update_uid(self, uid: str):
        self.connection_tenant_uid = uid
    def update_uid_attributes(self, connection_tenant_uid: str, connection_tenant_name: str, tenant_uid: str, calls_count: int, items_count: int, request_size: int, response_size: int):
        self.connection_tenant_uid = connection_tenant_uid
        self.connection_tenant_name = connection_tenant_name
        self.tenant_uid = tenant_uid
        self.calls_count = calls_count
        self.items_count = items_count
        self.request_size = request_size
        self.response_size = response_size
    def update_attributes(self, connection_tenant_name: str, tenant_uid: str, calls_count: int, items_count: int, request_size: int, response_size: int):
        self.connection_tenant_name = connection_tenant_name
        self.tenant_uid = tenant_uid
        self.calls_count = calls_count
        self.items_count = items_count
        self.request_size = request_size
        self.response_size = response_size


@dataclass(frozen=False)
class connection_user_write_dto(base_write_dto):
    connection_user_uid: str
    connection_user_name: str
    connection_engine_uid: str
    account_uid: str
    call_count: int
    host_count: int
    token_count: int
    def __init__(self, connection_user_uid: str, connection_user_name: str, connection_engine_uid: str, account_uid: str, call_count: int, host_count: int, token_count: int, custom_attributes: str = "{}"):
        self.connection_user_uid = connection_user_uid
        self.connection_user_name = connection_user_name
        self.connection_engine_uid = connection_engine_uid
        self.account_uid = account_uid
        self.call_count = call_count
        self.host_count = host_count
        self.token_count = token_count
        self.custom_attributes = custom_attributes
    @classmethod
    def empty_write(cls):
        return cls("", "", "", "", 0, 0, 0)
    @classmethod
    def default_write(cls):
        return cls(base_dto.get_random_uid(), "", "", "", 0, 0, 0)
    @classmethod
    def random_write(cls):
        return cls(base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), 0, 0, 0)
    @classmethod
    def new_write(cls, connection_user_uid: str, connection_user_name: str, connection_engine_uid: str, account_uid: str, call_count: int, host_count: int, token_count: int):
        return cls(connection_user_uid, connection_user_name, connection_engine_uid, account_uid, call_count, host_count, token_count)
    @classmethod
    def new_write_with_defaults(cls, connection_user_uid: str = "", connection_user_name: str = "", connection_engine_uid: str = "", account_uid: str = "", call_count: int = 0, host_count: int = 0, token_count: int = 0):
        return cls(connection_user_uid, connection_user_name, connection_engine_uid, account_uid, call_count, host_count, token_count)
    @classmethod
    def new_write_random_uid(cls, connection_user_name: str, connection_engine_uid: str, account_uid: str, call_count: int, host_count: int, token_count: int):
        return cls(base_dto.get_random_uid(), connection_user_name, connection_engine_uid, account_uid, call_count, host_count, token_count)
    @classmethod
    def get_class_model(cls) -> base_model:
        return db_models.connection_user_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["connection_user_uid"], d["connection_user_name"], d["connection_engine_uid"], d["account_uid"], d["call_count"], d["host_count"], d["token_count"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return connection_user_write_dto(self.connection_user_uid, self.connection_user_name, self.connection_engine_uid, self.account_uid, self.call_count, self.host_count, self.token_count, self.custom_attributes)
    def clone_write_new_uid(self):
        return connection_user_write_dto(base_dto.get_random_uid(), self.connection_user_name, self.connection_engine_uid, self.account_uid, self.call_count, self.host_count, self.token_count, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return connection_user_write_dto(uid, self.connection_user_name, self.connection_engine_uid, self.account_uid, self.call_count, self.host_count, self.token_count, self.custom_attributes)
    def get_model(self) -> base_model:
        return db_models.connection_user_model
    def get_uid(self) -> str:
        return self.connection_user_uid
    def get_name(self) -> str:
        return self.connection_user_name
    def get_list_values(self) -> list[any]:
        return [self.connection_user_uid, self.connection_user_name, self.connection_engine_uid, self.account_uid, self.call_count, self.host_count, self.token_count, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.connection_user_uid, self.connection_user_name, self.connection_engine_uid, self.account_uid, self.call_count, self.host_count, self.token_count]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.connection_user_name, self.connection_engine_uid, self.account_uid, self.call_count, self.host_count, self.token_count, self.custom_attributes, updated_by, self.connection_user_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.connection_user_uid, self.connection_user_name, self.connection_engine_uid, self.account_uid, self.call_count, self.host_count, self.token_count, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.connection_user_name, self.connection_engine_uid, self.account_uid, self.call_count, self.host_count, self.token_count]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.connection_user_name, self.connection_engine_uid, self.account_uid, self.call_count, self.host_count, self.token_count, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_uid() == obj.get_uid()
    def update_uid(self, uid: str):
        self.connection_user_uid = uid
    def update_uid_attributes(self, connection_user_uid: str, connection_user_name: str, connection_engine_uid: str, account_uid: str, call_count: int, host_count: int, token_count: int):
        self.connection_user_uid = connection_user_uid
        self.connection_user_name = connection_user_name
        self.connection_engine_uid = connection_engine_uid
        self.account_uid = account_uid
        self.call_count = call_count
        self.host_count = host_count
        self.token_count = token_count
    def update_attributes(self, connection_user_name: str, connection_engine_uid: str, account_uid: str, call_count: int, host_count: int, token_count: int):
        self.connection_user_name = connection_user_name
        self.connection_engine_uid = connection_engine_uid
        self.account_uid = account_uid
        self.call_count = call_count
        self.host_count = host_count
        self.token_count = token_count


@dataclass(frozen=False)
class country_write_dto(base_write_dto):
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
    def __init__(self, country_uid: str, country_name: str, continent_name: str, continent_code: str, country_iso3: str, country_code: str, phone_code: str, currency_code: str, capital_name: str, region_name: str, subregion_name: str, region_code: str, latitude: str, longitude: str, currency_name: str, population: str, languages: str, area: str, bar_code: str, top_level_domain: str, is_focused: int, custom_attributes: str = "{}"):
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
        self.custom_attributes = custom_attributes
    @classmethod
    def empty_write(cls):
        return cls("", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", 0)
    @classmethod
    def default_write(cls):
        return cls(base_dto.get_random_uid(), "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", 0)
    @classmethod
    def random_write(cls):
        return cls(base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), 0)
    @classmethod
    def new_write(cls, country_uid: str, country_name: str, continent_name: str, continent_code: str, country_iso3: str, country_code: str, phone_code: str, currency_code: str, capital_name: str, region_name: str, subregion_name: str, region_code: str, latitude: str, longitude: str, currency_name: str, population: str, languages: str, area: str, bar_code: str, top_level_domain: str, is_focused: int):
        return cls(country_uid, country_name, continent_name, continent_code, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain, is_focused)
    @classmethod
    def new_write_with_defaults(cls, country_uid: str = "", country_name: str = "", continent_name: str = "", continent_code: str = "", country_iso3: str = "", country_code: str = "", phone_code: str = "", currency_code: str = "", capital_name: str = "", region_name: str = "", subregion_name: str = "", region_code: str = "", latitude: str = "", longitude: str = "", currency_name: str = "", population: str = "", languages: str = "", area: str = "", bar_code: str = "", top_level_domain: str = "", is_focused: int = 0):
        return cls(country_uid, country_name, continent_name, continent_code, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain, is_focused)
    @classmethod
    def new_write_random_uid(cls, country_name: str, continent_name: str, continent_code: str, country_iso3: str, country_code: str, phone_code: str, currency_code: str, capital_name: str, region_name: str, subregion_name: str, region_code: str, latitude: str, longitude: str, currency_name: str, population: str, languages: str, area: str, bar_code: str, top_level_domain: str, is_focused: int):
        return cls(base_dto.get_random_uid(), country_name, continent_name, continent_code, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain, is_focused)
    @classmethod
    def get_class_model(cls) -> base_model:
        return db_models.country_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["country_uid"], d["country_name"], d["continent_name"], d["continent_code"], d["country_iso3"], d["country_code"], d["phone_code"], d["currency_code"], d["capital_name"], d["region_name"], d["subregion_name"], d["region_code"], d["latitude"], d["longitude"], d["currency_name"], d["population"], d["languages"], d["area"], d["bar_code"], d["top_level_domain"], d["is_focused"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return country_write_dto(self.country_uid, self.country_name, self.continent_name, self.continent_code, self.country_iso3, self.country_code, self.phone_code, self.currency_code, self.capital_name, self.region_name, self.subregion_name, self.region_code, self.latitude, self.longitude, self.currency_name, self.population, self.languages, self.area, self.bar_code, self.top_level_domain, self.is_focused, self.custom_attributes)
    def clone_write_new_uid(self):
        return country_write_dto(base_dto.get_random_uid(), self.country_name, self.continent_name, self.continent_code, self.country_iso3, self.country_code, self.phone_code, self.currency_code, self.capital_name, self.region_name, self.subregion_name, self.region_code, self.latitude, self.longitude, self.currency_name, self.population, self.languages, self.area, self.bar_code, self.top_level_domain, self.is_focused, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return country_write_dto(uid, self.country_name, self.continent_name, self.continent_code, self.country_iso3, self.country_code, self.phone_code, self.currency_code, self.capital_name, self.region_name, self.subregion_name, self.region_code, self.latitude, self.longitude, self.currency_name, self.population, self.languages, self.area, self.bar_code, self.top_level_domain, self.is_focused, self.custom_attributes)
    def get_model(self) -> base_model:
        return db_models.country_model
    def get_uid(self) -> str:
        return self.country_uid
    def get_name(self) -> str:
        return self.country_name
    def get_list_values(self) -> list[any]:
        return [self.country_uid, self.country_name, self.continent_name, self.continent_code, self.country_iso3, self.country_code, self.phone_code, self.currency_code, self.capital_name, self.region_name, self.subregion_name, self.region_code, self.latitude, self.longitude, self.currency_name, self.population, self.languages, self.area, self.bar_code, self.top_level_domain, self.is_focused, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.country_uid, self.country_name, self.continent_name, self.continent_code, self.country_iso3, self.country_code, self.phone_code, self.currency_code, self.capital_name, self.region_name, self.subregion_name, self.region_code, self.latitude, self.longitude, self.currency_name, self.population, self.languages, self.area, self.bar_code, self.top_level_domain, self.is_focused]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.country_name, self.continent_name, self.continent_code, self.country_iso3, self.country_code, self.phone_code, self.currency_code, self.capital_name, self.region_name, self.subregion_name, self.region_code, self.latitude, self.longitude, self.currency_name, self.population, self.languages, self.area, self.bar_code, self.top_level_domain, self.is_focused, self.custom_attributes, updated_by, self.country_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.country_uid, self.country_name, self.continent_name, self.continent_code, self.country_iso3, self.country_code, self.phone_code, self.currency_code, self.capital_name, self.region_name, self.subregion_name, self.region_code, self.latitude, self.longitude, self.currency_name, self.population, self.languages, self.area, self.bar_code, self.top_level_domain, self.is_focused, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.country_name, self.continent_name, self.continent_code, self.country_iso3, self.country_code, self.phone_code, self.currency_code, self.capital_name, self.region_name, self.subregion_name, self.region_code, self.latitude, self.longitude, self.currency_name, self.population, self.languages, self.area, self.bar_code, self.top_level_domain, self.is_focused]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.country_name, self.continent_name, self.continent_code, self.country_iso3, self.country_code, self.phone_code, self.currency_code, self.capital_name, self.region_name, self.subregion_name, self.region_code, self.latitude, self.longitude, self.currency_name, self.population, self.languages, self.area, self.bar_code, self.top_level_domain, self.is_focused, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_uid() == obj.get_uid()
    def update_uid(self, uid: str):
        self.country_uid = uid
    def update_uid_attributes(self, country_uid: str, country_name: str, continent_name: str, continent_code: str, country_iso3: str, country_code: str, phone_code: str, currency_code: str, capital_name: str, region_name: str, subregion_name: str, region_code: str, latitude: str, longitude: str, currency_name: str, population: str, languages: str, area: str, bar_code: str, top_level_domain: str, is_focused: int):
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
    def update_attributes(self, country_name: str, continent_name: str, continent_code: str, country_iso3: str, country_code: str, phone_code: str, currency_code: str, capital_name: str, region_name: str, subregion_name: str, region_code: str, latitude: str, longitude: str, currency_name: str, population: str, languages: str, area: str, bar_code: str, top_level_domain: str, is_focused: int):
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


@dataclass(frozen=False)
class currency_write_dto(base_write_dto):
    currency_uid: str
    currency_name: str
    is_focused: int
    priority: int
    def __init__(self, currency_uid: str, currency_name: str, is_focused: int, priority: int, custom_attributes: str = "{}"):
        self.currency_uid = currency_uid
        self.currency_name = currency_name
        self.is_focused = is_focused
        self.priority = priority
        self.custom_attributes = custom_attributes
    @classmethod
    def empty_write(cls):
        return cls("", "", 0, 0)
    @classmethod
    def default_write(cls):
        return cls(base_dto.get_random_uid(), "", 0, 0)
    @classmethod
    def random_write(cls):
        return cls(base_dto.get_random_uid(), base_dto.get_random_uid(), 0, 0)
    @classmethod
    def new_write(cls, currency_uid: str, currency_name: str, is_focused: int, priority: int):
        return cls(currency_uid, currency_name, is_focused, priority)
    @classmethod
    def new_write_with_defaults(cls, currency_uid: str = "", currency_name: str = "", is_focused: int = 0, priority: int = 0):
        return cls(currency_uid, currency_name, is_focused, priority)
    @classmethod
    def new_write_random_uid(cls, currency_name: str, is_focused: int, priority: int):
        return cls(base_dto.get_random_uid(), currency_name, is_focused, priority)
    @classmethod
    def get_class_model(cls) -> base_model:
        return db_models.currency_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["currency_uid"], d["currency_name"], d["is_focused"], d["priority"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return currency_write_dto(self.currency_uid, self.currency_name, self.is_focused, self.priority, self.custom_attributes)
    def clone_write_new_uid(self):
        return currency_write_dto(base_dto.get_random_uid(), self.currency_name, self.is_focused, self.priority, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return currency_write_dto(uid, self.currency_name, self.is_focused, self.priority, self.custom_attributes)
    def get_model(self) -> base_model:
        return db_models.currency_model
    def get_uid(self) -> str:
        return self.currency_uid
    def get_name(self) -> str:
        return self.currency_name
    def get_list_values(self) -> list[any]:
        return [self.currency_uid, self.currency_name, self.is_focused, self.priority, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.currency_uid, self.currency_name, self.is_focused, self.priority]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.currency_name, self.is_focused, self.priority, self.custom_attributes, updated_by, self.currency_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.currency_uid, self.currency_name, self.is_focused, self.priority, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.currency_name, self.is_focused, self.priority]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.currency_name, self.is_focused, self.priority, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_uid() == obj.get_uid()
    def update_uid(self, uid: str):
        self.currency_uid = uid
    def update_uid_attributes(self, currency_uid: str, currency_name: str, is_focused: int, priority: int):
        self.currency_uid = currency_uid
        self.currency_name = currency_name
        self.is_focused = is_focused
        self.priority = priority
    def update_attributes(self, currency_name: str, is_focused: int, priority: int):
        self.currency_name = currency_name
        self.is_focused = is_focused
        self.priority = priority


@dataclass(frozen=False)
class currency_rate_write_dto(base_write_dto):
    currency_rate_uid: str
    currency_rate_name: str
    tenant_uid: str
    currency_source_uid: str
    from_currency_uid: str
    to_currency_uid: str
    start_date: datetime.datetime | None
    end_date: datetime.datetime | None
    def __init__(self, currency_rate_uid: str, currency_rate_name: str, tenant_uid: str, currency_source_uid: str, from_currency_uid: str, to_currency_uid: str, start_date: datetime.datetime | None, end_date: datetime.datetime | None, custom_attributes: str = "{}"):
        self.currency_rate_uid = currency_rate_uid
        self.currency_rate_name = currency_rate_name
        self.tenant_uid = tenant_uid
        self.currency_source_uid = currency_source_uid
        self.from_currency_uid = from_currency_uid
        self.to_currency_uid = to_currency_uid
        self.start_date = start_date
        self.end_date = end_date
        self.custom_attributes = custom_attributes
    @classmethod
    def empty_write(cls):
        return cls("", "", "", "", "", "", datetime.datetime.now(), datetime.datetime.now())
    @classmethod
    def default_write(cls):
        return cls(base_dto.get_random_uid(), "", "", "", "", "", datetime.datetime.now(), datetime.datetime.now())
    @classmethod
    def random_write(cls):
        return cls(base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), datetime.datetime.now(), datetime.datetime.now())
    @classmethod
    def new_write(cls, currency_rate_uid: str, currency_rate_name: str, tenant_uid: str, currency_source_uid: str, from_currency_uid: str, to_currency_uid: str, start_date: datetime.datetime | None, end_date: datetime.datetime | None):
        return cls(currency_rate_uid, currency_rate_name, tenant_uid, currency_source_uid, from_currency_uid, to_currency_uid, start_date, end_date)
    @classmethod
    def new_write_with_defaults(cls, currency_rate_uid: str = "", currency_rate_name: str = "", tenant_uid: str = "", currency_source_uid: str = "", from_currency_uid: str = "", to_currency_uid: str = "", start_date: datetime.datetime | None = datetime.datetime.now(), end_date: datetime.datetime | None = datetime.datetime.now()):
        return cls(currency_rate_uid, currency_rate_name, tenant_uid, currency_source_uid, from_currency_uid, to_currency_uid, start_date, end_date)
    @classmethod
    def new_write_random_uid(cls, currency_rate_name: str, tenant_uid: str, currency_source_uid: str, from_currency_uid: str, to_currency_uid: str, start_date: datetime.datetime | None, end_date: datetime.datetime | None):
        return cls(base_dto.get_random_uid(), currency_rate_name, tenant_uid, currency_source_uid, from_currency_uid, to_currency_uid, start_date, end_date)
    @classmethod
    def get_class_model(cls) -> base_model:
        return db_models.currency_rate_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["currency_rate_uid"], d["currency_rate_name"], d["tenant_uid"], d["currency_source_uid"], d["from_currency_uid"], d["to_currency_uid"], d["start_date"], d["end_date"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return currency_rate_write_dto(self.currency_rate_uid, self.currency_rate_name, self.tenant_uid, self.currency_source_uid, self.from_currency_uid, self.to_currency_uid, self.start_date, self.end_date, self.custom_attributes)
    def clone_write_new_uid(self):
        return currency_rate_write_dto(base_dto.get_random_uid(), self.currency_rate_name, self.tenant_uid, self.currency_source_uid, self.from_currency_uid, self.to_currency_uid, self.start_date, self.end_date, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return currency_rate_write_dto(uid, self.currency_rate_name, self.tenant_uid, self.currency_source_uid, self.from_currency_uid, self.to_currency_uid, self.start_date, self.end_date, self.custom_attributes)
    def get_model(self) -> base_model:
        return db_models.currency_rate_model
    def get_uid(self) -> str:
        return self.currency_rate_uid
    def get_name(self) -> str:
        return self.currency_rate_name
    def get_list_values(self) -> list[any]:
        return [self.currency_rate_uid, self.currency_rate_name, self.tenant_uid, self.currency_source_uid, self.from_currency_uid, self.to_currency_uid, self.start_date, self.end_date, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.currency_rate_uid, self.currency_rate_name, self.tenant_uid, self.currency_source_uid, self.from_currency_uid, self.to_currency_uid, self.start_date, self.end_date]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.currency_rate_name, self.tenant_uid, self.currency_source_uid, self.from_currency_uid, self.to_currency_uid, self.start_date, self.end_date, self.custom_attributes, updated_by, self.currency_rate_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.currency_rate_uid, self.currency_rate_name, self.tenant_uid, self.currency_source_uid, self.from_currency_uid, self.to_currency_uid, self.start_date, self.end_date, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.currency_rate_name, self.tenant_uid, self.currency_source_uid, self.from_currency_uid, self.to_currency_uid, self.start_date, self.end_date]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.currency_rate_name, self.tenant_uid, self.currency_source_uid, self.from_currency_uid, self.to_currency_uid, self.start_date, self.end_date, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_uid() == obj.get_uid()
    def update_uid(self, uid: str):
        self.currency_rate_uid = uid
    def update_uid_attributes(self, currency_rate_uid: str, currency_rate_name: str, tenant_uid: str, currency_source_uid: str, from_currency_uid: str, to_currency_uid: str, start_date: datetime.datetime | None, end_date: datetime.datetime | None):
        self.currency_rate_uid = currency_rate_uid
        self.currency_rate_name = currency_rate_name
        self.tenant_uid = tenant_uid
        self.currency_source_uid = currency_source_uid
        self.from_currency_uid = from_currency_uid
        self.to_currency_uid = to_currency_uid
        self.start_date = start_date
        self.end_date = end_date
    def update_attributes(self, currency_rate_name: str, tenant_uid: str, currency_source_uid: str, from_currency_uid: str, to_currency_uid: str, start_date: datetime.datetime | None, end_date: datetime.datetime | None):
        self.currency_rate_name = currency_rate_name
        self.tenant_uid = tenant_uid
        self.currency_source_uid = currency_source_uid
        self.from_currency_uid = from_currency_uid
        self.to_currency_uid = to_currency_uid
        self.start_date = start_date
        self.end_date = end_date


@dataclass(frozen=False)
class currency_source_write_dto(base_write_dto):
    currency_source_uid: str
    currency_source_name: str
    tenant_uid: str
    source_url: str
    def __init__(self, currency_source_uid: str, currency_source_name: str, tenant_uid: str, source_url: str, custom_attributes: str = "{}"):
        self.currency_source_uid = currency_source_uid
        self.currency_source_name = currency_source_name
        self.tenant_uid = tenant_uid
        self.source_url = source_url
        self.custom_attributes = custom_attributes
    @classmethod
    def empty_write(cls):
        return cls("", "", "", "")
    @classmethod
    def default_write(cls):
        return cls(base_dto.get_random_uid(), "", "", "")
    @classmethod
    def random_write(cls):
        return cls(base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid())
    @classmethod
    def new_write(cls, currency_source_uid: str, currency_source_name: str, tenant_uid: str, source_url: str):
        return cls(currency_source_uid, currency_source_name, tenant_uid, source_url)
    @classmethod
    def new_write_with_defaults(cls, currency_source_uid: str = "", currency_source_name: str = "", tenant_uid: str = "", source_url: str = ""):
        return cls(currency_source_uid, currency_source_name, tenant_uid, source_url)
    @classmethod
    def new_write_random_uid(cls, currency_source_name: str, tenant_uid: str, source_url: str):
        return cls(base_dto.get_random_uid(), currency_source_name, tenant_uid, source_url)
    @classmethod
    def get_class_model(cls) -> base_model:
        return db_models.currency_source_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["currency_source_uid"], d["currency_source_name"], d["tenant_uid"], d["source_url"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return currency_source_write_dto(self.currency_source_uid, self.currency_source_name, self.tenant_uid, self.source_url, self.custom_attributes)
    def clone_write_new_uid(self):
        return currency_source_write_dto(base_dto.get_random_uid(), self.currency_source_name, self.tenant_uid, self.source_url, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return currency_source_write_dto(uid, self.currency_source_name, self.tenant_uid, self.source_url, self.custom_attributes)
    def get_model(self) -> base_model:
        return db_models.currency_source_model
    def get_uid(self) -> str:
        return self.currency_source_uid
    def get_name(self) -> str:
        return self.currency_source_name
    def get_list_values(self) -> list[any]:
        return [self.currency_source_uid, self.currency_source_name, self.tenant_uid, self.source_url, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.currency_source_uid, self.currency_source_name, self.tenant_uid, self.source_url]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.currency_source_name, self.tenant_uid, self.source_url, self.custom_attributes, updated_by, self.currency_source_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.currency_source_uid, self.currency_source_name, self.tenant_uid, self.source_url, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.currency_source_name, self.tenant_uid, self.source_url]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.currency_source_name, self.tenant_uid, self.source_url, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_uid() == obj.get_uid()
    def update_uid(self, uid: str):
        self.currency_source_uid = uid
    def update_uid_attributes(self, currency_source_uid: str, currency_source_name: str, tenant_uid: str, source_url: str):
        self.currency_source_uid = currency_source_uid
        self.currency_source_name = currency_source_name
        self.tenant_uid = tenant_uid
        self.source_url = source_url
    def update_attributes(self, currency_source_name: str, tenant_uid: str, source_url: str):
        self.currency_source_name = currency_source_name
        self.tenant_uid = tenant_uid
        self.source_url = source_url


@dataclass(frozen=False)
class event_acknowledge_write_dto(base_write_dto):
    event_acknowledge_uid: str
    event_acknowledge_name: str
    event_notification_uid: str
    tenant_uid: str
    account_uid: str
    def __init__(self, event_acknowledge_uid: str, event_acknowledge_name: str, event_notification_uid: str, tenant_uid: str, account_uid: str, custom_attributes: str = "{}"):
        self.event_acknowledge_uid = event_acknowledge_uid
        self.event_acknowledge_name = event_acknowledge_name
        self.event_notification_uid = event_notification_uid
        self.tenant_uid = tenant_uid
        self.account_uid = account_uid
        self.custom_attributes = custom_attributes
    @classmethod
    def empty_write(cls):
        return cls("", "", "", "", "")
    @classmethod
    def default_write(cls):
        return cls(base_dto.get_random_uid(), "", "", "", "")
    @classmethod
    def random_write(cls):
        return cls(base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid())
    @classmethod
    def new_write(cls, event_acknowledge_uid: str, event_acknowledge_name: str, event_notification_uid: str, tenant_uid: str, account_uid: str):
        return cls(event_acknowledge_uid, event_acknowledge_name, event_notification_uid, tenant_uid, account_uid)
    @classmethod
    def new_write_with_defaults(cls, event_acknowledge_uid: str = "", event_acknowledge_name: str = "", event_notification_uid: str = "", tenant_uid: str = "", account_uid: str = ""):
        return cls(event_acknowledge_uid, event_acknowledge_name, event_notification_uid, tenant_uid, account_uid)
    @classmethod
    def new_write_random_uid(cls, event_acknowledge_name: str, event_notification_uid: str, tenant_uid: str, account_uid: str):
        return cls(base_dto.get_random_uid(), event_acknowledge_name, event_notification_uid, tenant_uid, account_uid)
    @classmethod
    def get_class_model(cls) -> base_model:
        return db_models.event_acknowledge_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["event_acknowledge_uid"], d["event_acknowledge_name"], d["event_notification_uid"], d["tenant_uid"], d["account_uid"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return event_acknowledge_write_dto(self.event_acknowledge_uid, self.event_acknowledge_name, self.event_notification_uid, self.tenant_uid, self.account_uid, self.custom_attributes)
    def clone_write_new_uid(self):
        return event_acknowledge_write_dto(base_dto.get_random_uid(), self.event_acknowledge_name, self.event_notification_uid, self.tenant_uid, self.account_uid, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return event_acknowledge_write_dto(uid, self.event_acknowledge_name, self.event_notification_uid, self.tenant_uid, self.account_uid, self.custom_attributes)
    def get_model(self) -> base_model:
        return db_models.event_acknowledge_model
    def get_uid(self) -> str:
        return self.event_acknowledge_uid
    def get_name(self) -> str:
        return self.event_acknowledge_name
    def get_list_values(self) -> list[any]:
        return [self.event_acknowledge_uid, self.event_acknowledge_name, self.event_notification_uid, self.tenant_uid, self.account_uid, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.event_acknowledge_uid, self.event_acknowledge_name, self.event_notification_uid, self.tenant_uid, self.account_uid]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.event_acknowledge_name, self.event_notification_uid, self.tenant_uid, self.account_uid, self.custom_attributes, updated_by, self.event_acknowledge_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.event_acknowledge_uid, self.event_acknowledge_name, self.event_notification_uid, self.tenant_uid, self.account_uid, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.event_acknowledge_name, self.event_notification_uid, self.tenant_uid, self.account_uid]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.event_acknowledge_name, self.event_notification_uid, self.tenant_uid, self.account_uid, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_uid() == obj.get_uid()
    def update_uid(self, uid: str):
        self.event_acknowledge_uid = uid
    def update_uid_attributes(self, event_acknowledge_uid: str, event_acknowledge_name: str, event_notification_uid: str, tenant_uid: str, account_uid: str):
        self.event_acknowledge_uid = event_acknowledge_uid
        self.event_acknowledge_name = event_acknowledge_name
        self.event_notification_uid = event_notification_uid
        self.tenant_uid = tenant_uid
        self.account_uid = account_uid
    def update_attributes(self, event_acknowledge_name: str, event_notification_uid: str, tenant_uid: str, account_uid: str):
        self.event_acknowledge_name = event_acknowledge_name
        self.event_notification_uid = event_notification_uid
        self.tenant_uid = tenant_uid
        self.account_uid = account_uid


@dataclass(frozen=False)
class event_channel_write_dto(base_write_dto):
    event_channel_uid: str
    event_channel_name: str
    event_channel_type_uid: str
    channel_definition: str
    last_status_name: str
    tenant_uid: str
    account_uid: str
    def __init__(self, event_channel_uid: str, event_channel_name: str, event_channel_type_uid: str, channel_definition: str, last_status_name: str, tenant_uid: str, account_uid: str, custom_attributes: str = "{}"):
        self.event_channel_uid = event_channel_uid
        self.event_channel_name = event_channel_name
        self.event_channel_type_uid = event_channel_type_uid
        self.channel_definition = channel_definition
        self.last_status_name = last_status_name
        self.tenant_uid = tenant_uid
        self.account_uid = account_uid
        self.custom_attributes = custom_attributes
    @classmethod
    def empty_write(cls):
        return cls("", "", "", "", "", "", "")
    @classmethod
    def default_write(cls):
        return cls(base_dto.get_random_uid(), "", "", "", "", "", "")
    @classmethod
    def random_write(cls):
        return cls(base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid())
    @classmethod
    def new_write(cls, event_channel_uid: str, event_channel_name: str, event_channel_type_uid: str, channel_definition: str, last_status_name: str, tenant_uid: str, account_uid: str):
        return cls(event_channel_uid, event_channel_name, event_channel_type_uid, channel_definition, last_status_name, tenant_uid, account_uid)
    @classmethod
    def new_write_with_defaults(cls, event_channel_uid: str = "", event_channel_name: str = "", event_channel_type_uid: str = "", channel_definition: str = "", last_status_name: str = "", tenant_uid: str = "", account_uid: str = ""):
        return cls(event_channel_uid, event_channel_name, event_channel_type_uid, channel_definition, last_status_name, tenant_uid, account_uid)
    @classmethod
    def new_write_random_uid(cls, event_channel_name: str, event_channel_type_uid: str, channel_definition: str, last_status_name: str, tenant_uid: str, account_uid: str):
        return cls(base_dto.get_random_uid(), event_channel_name, event_channel_type_uid, channel_definition, last_status_name, tenant_uid, account_uid)
    @classmethod
    def get_class_model(cls) -> base_model:
        return db_models.event_channel_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["event_channel_uid"], d["event_channel_name"], d["event_channel_type_uid"], d["channel_definition"], d["last_status_name"], d["tenant_uid"], d["account_uid"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return event_channel_write_dto(self.event_channel_uid, self.event_channel_name, self.event_channel_type_uid, self.channel_definition, self.last_status_name, self.tenant_uid, self.account_uid, self.custom_attributes)
    def clone_write_new_uid(self):
        return event_channel_write_dto(base_dto.get_random_uid(), self.event_channel_name, self.event_channel_type_uid, self.channel_definition, self.last_status_name, self.tenant_uid, self.account_uid, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return event_channel_write_dto(uid, self.event_channel_name, self.event_channel_type_uid, self.channel_definition, self.last_status_name, self.tenant_uid, self.account_uid, self.custom_attributes)
    def get_model(self) -> base_model:
        return db_models.event_channel_model
    def get_uid(self) -> str:
        return self.event_channel_uid
    def get_name(self) -> str:
        return self.event_channel_name
    def get_list_values(self) -> list[any]:
        return [self.event_channel_uid, self.event_channel_name, self.event_channel_type_uid, self.channel_definition, self.last_status_name, self.tenant_uid, self.account_uid, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.event_channel_uid, self.event_channel_name, self.event_channel_type_uid, self.channel_definition, self.last_status_name, self.tenant_uid, self.account_uid]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.event_channel_name, self.event_channel_type_uid, self.channel_definition, self.last_status_name, self.tenant_uid, self.account_uid, self.custom_attributes, updated_by, self.event_channel_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.event_channel_uid, self.event_channel_name, self.event_channel_type_uid, self.channel_definition, self.last_status_name, self.tenant_uid, self.account_uid, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.event_channel_name, self.event_channel_type_uid, self.channel_definition, self.last_status_name, self.tenant_uid, self.account_uid]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.event_channel_name, self.event_channel_type_uid, self.channel_definition, self.last_status_name, self.tenant_uid, self.account_uid, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_uid() == obj.get_uid()
    def update_uid(self, uid: str):
        self.event_channel_uid = uid
    def update_uid_attributes(self, event_channel_uid: str, event_channel_name: str, event_channel_type_uid: str, channel_definition: str, last_status_name: str, tenant_uid: str, account_uid: str):
        self.event_channel_uid = event_channel_uid
        self.event_channel_name = event_channel_name
        self.event_channel_type_uid = event_channel_type_uid
        self.channel_definition = channel_definition
        self.last_status_name = last_status_name
        self.tenant_uid = tenant_uid
        self.account_uid = account_uid
    def update_attributes(self, event_channel_name: str, event_channel_type_uid: str, channel_definition: str, last_status_name: str, tenant_uid: str, account_uid: str):
        self.event_channel_name = event_channel_name
        self.event_channel_type_uid = event_channel_type_uid
        self.channel_definition = channel_definition
        self.last_status_name = last_status_name
        self.tenant_uid = tenant_uid
        self.account_uid = account_uid


@dataclass(frozen=False)
class event_channel_type_write_dto(base_write_dto):
    event_channel_type_uid: str
    event_channel_type_name: str
    channel_type_description: str
    def __init__(self, event_channel_type_uid: str, event_channel_type_name: str, channel_type_description: str, custom_attributes: str = "{}"):
        self.event_channel_type_uid = event_channel_type_uid
        self.event_channel_type_name = event_channel_type_name
        self.channel_type_description = channel_type_description
        self.custom_attributes = custom_attributes
    @classmethod
    def empty_write(cls):
        return cls("", "", "")
    @classmethod
    def default_write(cls):
        return cls(base_dto.get_random_uid(), "", "")
    @classmethod
    def random_write(cls):
        return cls(base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid())
    @classmethod
    def new_write(cls, event_channel_type_uid: str, event_channel_type_name: str, channel_type_description: str):
        return cls(event_channel_type_uid, event_channel_type_name, channel_type_description)
    @classmethod
    def new_write_with_defaults(cls, event_channel_type_uid: str = "", event_channel_type_name: str = "", channel_type_description: str = ""):
        return cls(event_channel_type_uid, event_channel_type_name, channel_type_description)
    @classmethod
    def new_write_random_uid(cls, event_channel_type_name: str, channel_type_description: str):
        return cls(base_dto.get_random_uid(), event_channel_type_name, channel_type_description)
    @classmethod
    def get_class_model(cls) -> base_model:
        return db_models.event_channel_type_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["event_channel_type_uid"], d["event_channel_type_name"], d["channel_type_description"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return event_channel_type_write_dto(self.event_channel_type_uid, self.event_channel_type_name, self.channel_type_description, self.custom_attributes)
    def clone_write_new_uid(self):
        return event_channel_type_write_dto(base_dto.get_random_uid(), self.event_channel_type_name, self.channel_type_description, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return event_channel_type_write_dto(uid, self.event_channel_type_name, self.channel_type_description, self.custom_attributes)
    def get_model(self) -> base_model:
        return db_models.event_channel_type_model
    def get_uid(self) -> str:
        return self.event_channel_type_uid
    def get_name(self) -> str:
        return self.event_channel_type_name
    def get_list_values(self) -> list[any]:
        return [self.event_channel_type_uid, self.event_channel_type_name, self.channel_type_description, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.event_channel_type_uid, self.event_channel_type_name, self.channel_type_description]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.event_channel_type_name, self.channel_type_description, self.custom_attributes, updated_by, self.event_channel_type_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.event_channel_type_uid, self.event_channel_type_name, self.channel_type_description, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.event_channel_type_name, self.channel_type_description]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.event_channel_type_name, self.channel_type_description, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_uid() == obj.get_uid()
    def update_uid(self, uid: str):
        self.event_channel_type_uid = uid
    def update_uid_attributes(self, event_channel_type_uid: str, event_channel_type_name: str, channel_type_description: str):
        self.event_channel_type_uid = event_channel_type_uid
        self.event_channel_type_name = event_channel_type_name
        self.channel_type_description = channel_type_description
    def update_attributes(self, event_channel_type_name: str, channel_type_description: str):
        self.event_channel_type_name = event_channel_type_name
        self.channel_type_description = channel_type_description


@dataclass(frozen=False)
class event_instance_write_dto(base_write_dto):
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
    def __init__(self, event_instance_uid: str, event_instance_name: str, tenant_uid: str, event_type: str, event_object: str, event_method: str, event_parameters: str, event_signature: str, event_date: datetime.datetime, published_count: int, custom_attributes: str = "{}"):
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
        self.custom_attributes = custom_attributes
    @classmethod
    def empty_write(cls):
        return cls("", "", "", "", "", "", "", "", datetime.datetime.now(), 0)
    @classmethod
    def default_write(cls):
        return cls(base_dto.get_random_uid(), "", "", "", "", "", "", "", datetime.datetime.now(), 0)
    @classmethod
    def random_write(cls):
        return cls(base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), datetime.datetime.now(), 0)
    @classmethod
    def new_write(cls, event_instance_uid: str, event_instance_name: str, tenant_uid: str, event_type: str, event_object: str, event_method: str, event_parameters: str, event_signature: str, event_date: datetime.datetime, published_count: int):
        return cls(event_instance_uid, event_instance_name, tenant_uid, event_type, event_object, event_method, event_parameters, event_signature, event_date, published_count)
    @classmethod
    def new_write_with_defaults(cls, event_instance_uid: str = "", event_instance_name: str = "", tenant_uid: str = "", event_type: str = "", event_object: str = "", event_method: str = "", event_parameters: str = "", event_signature: str = "", event_date: datetime.datetime = datetime.datetime.now(), published_count: int = 0):
        return cls(event_instance_uid, event_instance_name, tenant_uid, event_type, event_object, event_method, event_parameters, event_signature, event_date, published_count)
    @classmethod
    def new_write_random_uid(cls, event_instance_name: str, tenant_uid: str, event_type: str, event_object: str, event_method: str, event_parameters: str, event_signature: str, event_date: datetime.datetime, published_count: int):
        return cls(base_dto.get_random_uid(), event_instance_name, tenant_uid, event_type, event_object, event_method, event_parameters, event_signature, event_date, published_count)
    @classmethod
    def get_class_model(cls) -> base_model:
        return db_models.event_instance_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["event_instance_uid"], d["event_instance_name"], d["tenant_uid"], d["event_type"], d["event_object"], d["event_method"], d["event_parameters"], d["event_signature"], d["event_date"], d["published_count"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return event_instance_write_dto(self.event_instance_uid, self.event_instance_name, self.tenant_uid, self.event_type, self.event_object, self.event_method, self.event_parameters, self.event_signature, self.event_date, self.published_count, self.custom_attributes)
    def clone_write_new_uid(self):
        return event_instance_write_dto(base_dto.get_random_uid(), self.event_instance_name, self.tenant_uid, self.event_type, self.event_object, self.event_method, self.event_parameters, self.event_signature, self.event_date, self.published_count, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return event_instance_write_dto(uid, self.event_instance_name, self.tenant_uid, self.event_type, self.event_object, self.event_method, self.event_parameters, self.event_signature, self.event_date, self.published_count, self.custom_attributes)
    def get_model(self) -> base_model:
        return db_models.event_instance_model
    def get_uid(self) -> str:
        return self.event_instance_uid
    def get_name(self) -> str:
        return self.event_instance_name
    def get_list_values(self) -> list[any]:
        return [self.event_instance_uid, self.event_instance_name, self.tenant_uid, self.event_type, self.event_object, self.event_method, self.event_parameters, self.event_signature, self.event_date, self.published_count, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.event_instance_uid, self.event_instance_name, self.tenant_uid, self.event_type, self.event_object, self.event_method, self.event_parameters, self.event_signature, self.event_date, self.published_count]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.event_instance_name, self.tenant_uid, self.event_type, self.event_object, self.event_method, self.event_parameters, self.event_signature, self.event_date, self.published_count, self.custom_attributes, updated_by, self.event_instance_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.event_instance_uid, self.event_instance_name, self.tenant_uid, self.event_type, self.event_object, self.event_method, self.event_parameters, self.event_signature, self.event_date, self.published_count, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.event_instance_name, self.tenant_uid, self.event_type, self.event_object, self.event_method, self.event_parameters, self.event_signature, self.event_date, self.published_count]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.event_instance_name, self.tenant_uid, self.event_type, self.event_object, self.event_method, self.event_parameters, self.event_signature, self.event_date, self.published_count, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_uid() == obj.get_uid()
    def update_uid(self, uid: str):
        self.event_instance_uid = uid
    def update_uid_attributes(self, event_instance_uid: str, event_instance_name: str, tenant_uid: str, event_type: str, event_object: str, event_method: str, event_parameters: str, event_signature: str, event_date: datetime.datetime, published_count: int):
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
    def update_attributes(self, event_instance_name: str, tenant_uid: str, event_type: str, event_object: str, event_method: str, event_parameters: str, event_signature: str, event_date: datetime.datetime, published_count: int):
        self.event_instance_name = event_instance_name
        self.tenant_uid = tenant_uid
        self.event_type = event_type
        self.event_object = event_object
        self.event_method = event_method
        self.event_parameters = event_parameters
        self.event_signature = event_signature
        self.event_date = event_date
        self.published_count = published_count


@dataclass(frozen=False)
class event_notification_write_dto(base_write_dto):
    event_notification_uid: str
    event_notification_name: str
    tenant_uid: str
    account_uid: str
    notification_type: str
    notification_topic: str
    notification_format: str
    notification_content: str
    sending_status: str
    def __init__(self, event_notification_uid: str, event_notification_name: str, tenant_uid: str, account_uid: str, notification_type: str, notification_topic: str, notification_format: str, notification_content: str, sending_status: str, custom_attributes: str = "{}"):
        self.event_notification_uid = event_notification_uid
        self.event_notification_name = event_notification_name
        self.tenant_uid = tenant_uid
        self.account_uid = account_uid
        self.notification_type = notification_type
        self.notification_topic = notification_topic
        self.notification_format = notification_format
        self.notification_content = notification_content
        self.sending_status = sending_status
        self.custom_attributes = custom_attributes
    @classmethod
    def empty_write(cls):
        return cls("", "", "", "", "", "", "", "", "")
    @classmethod
    def default_write(cls):
        return cls(base_dto.get_random_uid(), "", "", "", "", "", "", "", "")
    @classmethod
    def random_write(cls):
        return cls(base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid())
    @classmethod
    def new_write(cls, event_notification_uid: str, event_notification_name: str, tenant_uid: str, account_uid: str, notification_type: str, notification_topic: str, notification_format: str, notification_content: str, sending_status: str):
        return cls(event_notification_uid, event_notification_name, tenant_uid, account_uid, notification_type, notification_topic, notification_format, notification_content, sending_status)
    @classmethod
    def new_write_with_defaults(cls, event_notification_uid: str = "", event_notification_name: str = "", tenant_uid: str = "", account_uid: str = "", notification_type: str = "", notification_topic: str = "", notification_format: str = "", notification_content: str = "", sending_status: str = ""):
        return cls(event_notification_uid, event_notification_name, tenant_uid, account_uid, notification_type, notification_topic, notification_format, notification_content, sending_status)
    @classmethod
    def new_write_random_uid(cls, event_notification_name: str, tenant_uid: str, account_uid: str, notification_type: str, notification_topic: str, notification_format: str, notification_content: str, sending_status: str):
        return cls(base_dto.get_random_uid(), event_notification_name, tenant_uid, account_uid, notification_type, notification_topic, notification_format, notification_content, sending_status)
    @classmethod
    def get_class_model(cls) -> base_model:
        return db_models.event_notification_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["event_notification_uid"], d["event_notification_name"], d["tenant_uid"], d["account_uid"], d["notification_type"], d["notification_topic"], d["notification_format"], d["notification_content"], d["sending_status"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return event_notification_write_dto(self.event_notification_uid, self.event_notification_name, self.tenant_uid, self.account_uid, self.notification_type, self.notification_topic, self.notification_format, self.notification_content, self.sending_status, self.custom_attributes)
    def clone_write_new_uid(self):
        return event_notification_write_dto(base_dto.get_random_uid(), self.event_notification_name, self.tenant_uid, self.account_uid, self.notification_type, self.notification_topic, self.notification_format, self.notification_content, self.sending_status, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return event_notification_write_dto(uid, self.event_notification_name, self.tenant_uid, self.account_uid, self.notification_type, self.notification_topic, self.notification_format, self.notification_content, self.sending_status, self.custom_attributes)
    def get_model(self) -> base_model:
        return db_models.event_notification_model
    def get_uid(self) -> str:
        return self.event_notification_uid
    def get_name(self) -> str:
        return self.event_notification_name
    def get_list_values(self) -> list[any]:
        return [self.event_notification_uid, self.event_notification_name, self.tenant_uid, self.account_uid, self.notification_type, self.notification_topic, self.notification_format, self.notification_content, self.sending_status, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.event_notification_uid, self.event_notification_name, self.tenant_uid, self.account_uid, self.notification_type, self.notification_topic, self.notification_format, self.notification_content, self.sending_status]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.event_notification_name, self.tenant_uid, self.account_uid, self.notification_type, self.notification_topic, self.notification_format, self.notification_content, self.sending_status, self.custom_attributes, updated_by, self.event_notification_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.event_notification_uid, self.event_notification_name, self.tenant_uid, self.account_uid, self.notification_type, self.notification_topic, self.notification_format, self.notification_content, self.sending_status, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.event_notification_name, self.tenant_uid, self.account_uid, self.notification_type, self.notification_topic, self.notification_format, self.notification_content, self.sending_status]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.event_notification_name, self.tenant_uid, self.account_uid, self.notification_type, self.notification_topic, self.notification_format, self.notification_content, self.sending_status, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_uid() == obj.get_uid()
    def update_uid(self, uid: str):
        self.event_notification_uid = uid
    def update_uid_attributes(self, event_notification_uid: str, event_notification_name: str, tenant_uid: str, account_uid: str, notification_type: str, notification_topic: str, notification_format: str, notification_content: str, sending_status: str):
        self.event_notification_uid = event_notification_uid
        self.event_notification_name = event_notification_name
        self.tenant_uid = tenant_uid
        self.account_uid = account_uid
        self.notification_type = notification_type
        self.notification_topic = notification_topic
        self.notification_format = notification_format
        self.notification_content = notification_content
        self.sending_status = sending_status
    def update_attributes(self, event_notification_name: str, tenant_uid: str, account_uid: str, notification_type: str, notification_topic: str, notification_format: str, notification_content: str, sending_status: str):
        self.event_notification_name = event_notification_name
        self.tenant_uid = tenant_uid
        self.account_uid = account_uid
        self.notification_type = notification_type
        self.notification_topic = notification_topic
        self.notification_format = notification_format
        self.notification_content = notification_content
        self.sending_status = sending_status


@dataclass(frozen=False)
class event_observer_write_dto(base_write_dto):
    event_observer_uid: str
    event_observer_name: str
    event_observer_definition: str
    action_definition: str
    def __init__(self, event_observer_uid: str, event_observer_name: str, event_observer_definition: str, action_definition: str, custom_attributes: str = "{}"):
        self.event_observer_uid = event_observer_uid
        self.event_observer_name = event_observer_name
        self.event_observer_definition = event_observer_definition
        self.action_definition = action_definition
        self.custom_attributes = custom_attributes
    @classmethod
    def empty_write(cls):
        return cls("", "", "", "")
    @classmethod
    def default_write(cls):
        return cls(base_dto.get_random_uid(), "", "", "")
    @classmethod
    def random_write(cls):
        return cls(base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid())
    @classmethod
    def new_write(cls, event_observer_uid: str, event_observer_name: str, event_observer_definition: str, action_definition: str):
        return cls(event_observer_uid, event_observer_name, event_observer_definition, action_definition)
    @classmethod
    def new_write_with_defaults(cls, event_observer_uid: str = "", event_observer_name: str = "", event_observer_definition: str = "", action_definition: str = ""):
        return cls(event_observer_uid, event_observer_name, event_observer_definition, action_definition)
    @classmethod
    def new_write_random_uid(cls, event_observer_name: str, event_observer_definition: str, action_definition: str):
        return cls(base_dto.get_random_uid(), event_observer_name, event_observer_definition, action_definition)
    @classmethod
    def get_class_model(cls) -> base_model:
        return db_models.event_observer_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["event_observer_uid"], d["event_observer_name"], d["event_observer_definition"], d["action_definition"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return event_observer_write_dto(self.event_observer_uid, self.event_observer_name, self.event_observer_definition, self.action_definition, self.custom_attributes)
    def clone_write_new_uid(self):
        return event_observer_write_dto(base_dto.get_random_uid(), self.event_observer_name, self.event_observer_definition, self.action_definition, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return event_observer_write_dto(uid, self.event_observer_name, self.event_observer_definition, self.action_definition, self.custom_attributes)
    def get_model(self) -> base_model:
        return db_models.event_observer_model
    def get_uid(self) -> str:
        return self.event_observer_uid
    def get_name(self) -> str:
        return self.event_observer_name
    def get_list_values(self) -> list[any]:
        return [self.event_observer_uid, self.event_observer_name, self.event_observer_definition, self.action_definition, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.event_observer_uid, self.event_observer_name, self.event_observer_definition, self.action_definition]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.event_observer_name, self.event_observer_definition, self.action_definition, self.custom_attributes, updated_by, self.event_observer_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.event_observer_uid, self.event_observer_name, self.event_observer_definition, self.action_definition, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.event_observer_name, self.event_observer_definition, self.action_definition]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.event_observer_name, self.event_observer_definition, self.action_definition, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_uid() == obj.get_uid()
    def update_uid(self, uid: str):
        self.event_observer_uid = uid
    def update_uid_attributes(self, event_observer_uid: str, event_observer_name: str, event_observer_definition: str, action_definition: str):
        self.event_observer_uid = event_observer_uid
        self.event_observer_name = event_observer_name
        self.event_observer_definition = event_observer_definition
        self.action_definition = action_definition
    def update_attributes(self, event_observer_name: str, event_observer_definition: str, action_definition: str):
        self.event_observer_name = event_observer_name
        self.event_observer_definition = event_observer_definition
        self.action_definition = action_definition


@dataclass(frozen=False)
class event_subscription_write_dto(base_write_dto):
    event_subscription_uid: str
    event_subscription_name: str
    event_channel_uid: str
    tenant_uid: str
    account_uid: str
    subscription_filter: str
    subscription_topic: str
    subscription_template: str
    def __init__(self, event_subscription_uid: str, event_subscription_name: str, event_channel_uid: str, tenant_uid: str, account_uid: str, subscription_filter: str, subscription_topic: str, subscription_template: str, custom_attributes: str = "{}"):
        self.event_subscription_uid = event_subscription_uid
        self.event_subscription_name = event_subscription_name
        self.event_channel_uid = event_channel_uid
        self.tenant_uid = tenant_uid
        self.account_uid = account_uid
        self.subscription_filter = subscription_filter
        self.subscription_topic = subscription_topic
        self.subscription_template = subscription_template
        self.custom_attributes = custom_attributes
    @classmethod
    def empty_write(cls):
        return cls("", "", "", "", "", "", "", "")
    @classmethod
    def default_write(cls):
        return cls(base_dto.get_random_uid(), "", "", "", "", "", "", "")
    @classmethod
    def random_write(cls):
        return cls(base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid())
    @classmethod
    def new_write(cls, event_subscription_uid: str, event_subscription_name: str, event_channel_uid: str, tenant_uid: str, account_uid: str, subscription_filter: str, subscription_topic: str, subscription_template: str):
        return cls(event_subscription_uid, event_subscription_name, event_channel_uid, tenant_uid, account_uid, subscription_filter, subscription_topic, subscription_template)
    @classmethod
    def new_write_with_defaults(cls, event_subscription_uid: str = "", event_subscription_name: str = "", event_channel_uid: str = "", tenant_uid: str = "", account_uid: str = "", subscription_filter: str = "", subscription_topic: str = "", subscription_template: str = ""):
        return cls(event_subscription_uid, event_subscription_name, event_channel_uid, tenant_uid, account_uid, subscription_filter, subscription_topic, subscription_template)
    @classmethod
    def new_write_random_uid(cls, event_subscription_name: str, event_channel_uid: str, tenant_uid: str, account_uid: str, subscription_filter: str, subscription_topic: str, subscription_template: str):
        return cls(base_dto.get_random_uid(), event_subscription_name, event_channel_uid, tenant_uid, account_uid, subscription_filter, subscription_topic, subscription_template)
    @classmethod
    def get_class_model(cls) -> base_model:
        return db_models.event_subscription_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["event_subscription_uid"], d["event_subscription_name"], d["event_channel_uid"], d["tenant_uid"], d["account_uid"], d["subscription_filter"], d["subscription_topic"], d["subscription_template"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return event_subscription_write_dto(self.event_subscription_uid, self.event_subscription_name, self.event_channel_uid, self.tenant_uid, self.account_uid, self.subscription_filter, self.subscription_topic, self.subscription_template, self.custom_attributes)
    def clone_write_new_uid(self):
        return event_subscription_write_dto(base_dto.get_random_uid(), self.event_subscription_name, self.event_channel_uid, self.tenant_uid, self.account_uid, self.subscription_filter, self.subscription_topic, self.subscription_template, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return event_subscription_write_dto(uid, self.event_subscription_name, self.event_channel_uid, self.tenant_uid, self.account_uid, self.subscription_filter, self.subscription_topic, self.subscription_template, self.custom_attributes)
    def get_model(self) -> base_model:
        return db_models.event_subscription_model
    def get_uid(self) -> str:
        return self.event_subscription_uid
    def get_name(self) -> str:
        return self.event_subscription_name
    def get_list_values(self) -> list[any]:
        return [self.event_subscription_uid, self.event_subscription_name, self.event_channel_uid, self.tenant_uid, self.account_uid, self.subscription_filter, self.subscription_topic, self.subscription_template, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.event_subscription_uid, self.event_subscription_name, self.event_channel_uid, self.tenant_uid, self.account_uid, self.subscription_filter, self.subscription_topic, self.subscription_template]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.event_subscription_name, self.event_channel_uid, self.tenant_uid, self.account_uid, self.subscription_filter, self.subscription_topic, self.subscription_template, self.custom_attributes, updated_by, self.event_subscription_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.event_subscription_uid, self.event_subscription_name, self.event_channel_uid, self.tenant_uid, self.account_uid, self.subscription_filter, self.subscription_topic, self.subscription_template, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.event_subscription_name, self.event_channel_uid, self.tenant_uid, self.account_uid, self.subscription_filter, self.subscription_topic, self.subscription_template]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.event_subscription_name, self.event_channel_uid, self.tenant_uid, self.account_uid, self.subscription_filter, self.subscription_topic, self.subscription_template, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_uid() == obj.get_uid()
    def update_uid(self, uid: str):
        self.event_subscription_uid = uid
    def update_uid_attributes(self, event_subscription_uid: str, event_subscription_name: str, event_channel_uid: str, tenant_uid: str, account_uid: str, subscription_filter: str, subscription_topic: str, subscription_template: str):
        self.event_subscription_uid = event_subscription_uid
        self.event_subscription_name = event_subscription_name
        self.event_channel_uid = event_channel_uid
        self.tenant_uid = tenant_uid
        self.account_uid = account_uid
        self.subscription_filter = subscription_filter
        self.subscription_topic = subscription_topic
        self.subscription_template = subscription_template
    def update_attributes(self, event_subscription_name: str, event_channel_uid: str, tenant_uid: str, account_uid: str, subscription_filter: str, subscription_topic: str, subscription_template: str):
        self.event_subscription_name = event_subscription_name
        self.event_channel_uid = event_channel_uid
        self.tenant_uid = tenant_uid
        self.account_uid = account_uid
        self.subscription_filter = subscription_filter
        self.subscription_topic = subscription_topic
        self.subscription_template = subscription_template


@dataclass(frozen=False)
class event_template_write_dto(base_write_dto):
    event_template_uid: str
    event_template_name: str
    tenant_uid: str
    notification_type: str
    notification_topic: str
    notification_format: str
    def __init__(self, event_template_uid: str, event_template_name: str, tenant_uid: str, notification_type: str, notification_topic: str, notification_format: str, custom_attributes: str = "{}"):
        self.event_template_uid = event_template_uid
        self.event_template_name = event_template_name
        self.tenant_uid = tenant_uid
        self.notification_type = notification_type
        self.notification_topic = notification_topic
        self.notification_format = notification_format
        self.custom_attributes = custom_attributes
    @classmethod
    def empty_write(cls):
        return cls("", "", "", "", "", "")
    @classmethod
    def default_write(cls):
        return cls(base_dto.get_random_uid(), "", "", "", "", "")
    @classmethod
    def random_write(cls):
        return cls(base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid())
    @classmethod
    def new_write(cls, event_template_uid: str, event_template_name: str, tenant_uid: str, notification_type: str, notification_topic: str, notification_format: str):
        return cls(event_template_uid, event_template_name, tenant_uid, notification_type, notification_topic, notification_format)
    @classmethod
    def new_write_with_defaults(cls, event_template_uid: str = "", event_template_name: str = "", tenant_uid: str = "", notification_type: str = "", notification_topic: str = "", notification_format: str = ""):
        return cls(event_template_uid, event_template_name, tenant_uid, notification_type, notification_topic, notification_format)
    @classmethod
    def new_write_random_uid(cls, event_template_name: str, tenant_uid: str, notification_type: str, notification_topic: str, notification_format: str):
        return cls(base_dto.get_random_uid(), event_template_name, tenant_uid, notification_type, notification_topic, notification_format)
    @classmethod
    def get_class_model(cls) -> base_model:
        return db_models.event_template_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["event_template_uid"], d["event_template_name"], d["tenant_uid"], d["notification_type"], d["notification_topic"], d["notification_format"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return event_template_write_dto(self.event_template_uid, self.event_template_name, self.tenant_uid, self.notification_type, self.notification_topic, self.notification_format, self.custom_attributes)
    def clone_write_new_uid(self):
        return event_template_write_dto(base_dto.get_random_uid(), self.event_template_name, self.tenant_uid, self.notification_type, self.notification_topic, self.notification_format, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return event_template_write_dto(uid, self.event_template_name, self.tenant_uid, self.notification_type, self.notification_topic, self.notification_format, self.custom_attributes)
    def get_model(self) -> base_model:
        return db_models.event_template_model
    def get_uid(self) -> str:
        return self.event_template_uid
    def get_name(self) -> str:
        return self.event_template_name
    def get_list_values(self) -> list[any]:
        return [self.event_template_uid, self.event_template_name, self.tenant_uid, self.notification_type, self.notification_topic, self.notification_format, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.event_template_uid, self.event_template_name, self.tenant_uid, self.notification_type, self.notification_topic, self.notification_format]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.event_template_name, self.tenant_uid, self.notification_type, self.notification_topic, self.notification_format, self.custom_attributes, updated_by, self.event_template_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.event_template_uid, self.event_template_name, self.tenant_uid, self.notification_type, self.notification_topic, self.notification_format, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.event_template_name, self.tenant_uid, self.notification_type, self.notification_topic, self.notification_format]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.event_template_name, self.tenant_uid, self.notification_type, self.notification_topic, self.notification_format, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_uid() == obj.get_uid()
    def update_uid(self, uid: str):
        self.event_template_uid = uid
    def update_uid_attributes(self, event_template_uid: str, event_template_name: str, tenant_uid: str, notification_type: str, notification_topic: str, notification_format: str):
        self.event_template_uid = event_template_uid
        self.event_template_name = event_template_name
        self.tenant_uid = tenant_uid
        self.notification_type = notification_type
        self.notification_topic = notification_topic
        self.notification_format = notification_format
    def update_attributes(self, event_template_name: str, tenant_uid: str, notification_type: str, notification_topic: str, notification_format: str):
        self.event_template_name = event_template_name
        self.tenant_uid = tenant_uid
        self.notification_type = notification_type
        self.notification_topic = notification_topic
        self.notification_format = notification_format


@dataclass(frozen=False)
class event_type_write_dto(base_write_dto):
    event_type_uid: str
    event_type_name: str
    event_type_description: str
    def __init__(self, event_type_uid: str, event_type_name: str, event_type_description: str, custom_attributes: str = "{}"):
        self.event_type_uid = event_type_uid
        self.event_type_name = event_type_name
        self.event_type_description = event_type_description
        self.custom_attributes = custom_attributes
    @classmethod
    def empty_write(cls):
        return cls("", "", "")
    @classmethod
    def default_write(cls):
        return cls(base_dto.get_random_uid(), "", "")
    @classmethod
    def random_write(cls):
        return cls(base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid())
    @classmethod
    def new_write(cls, event_type_uid: str, event_type_name: str, event_type_description: str):
        return cls(event_type_uid, event_type_name, event_type_description)
    @classmethod
    def new_write_with_defaults(cls, event_type_uid: str = "", event_type_name: str = "", event_type_description: str = ""):
        return cls(event_type_uid, event_type_name, event_type_description)
    @classmethod
    def new_write_random_uid(cls, event_type_name: str, event_type_description: str):
        return cls(base_dto.get_random_uid(), event_type_name, event_type_description)
    @classmethod
    def get_class_model(cls) -> base_model:
        return db_models.event_type_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["event_type_uid"], d["event_type_name"], d["event_type_description"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return event_type_write_dto(self.event_type_uid, self.event_type_name, self.event_type_description, self.custom_attributes)
    def clone_write_new_uid(self):
        return event_type_write_dto(base_dto.get_random_uid(), self.event_type_name, self.event_type_description, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return event_type_write_dto(uid, self.event_type_name, self.event_type_description, self.custom_attributes)
    def get_model(self) -> base_model:
        return db_models.event_type_model
    def get_uid(self) -> str:
        return self.event_type_uid
    def get_name(self) -> str:
        return self.event_type_name
    def get_list_values(self) -> list[any]:
        return [self.event_type_uid, self.event_type_name, self.event_type_description, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.event_type_uid, self.event_type_name, self.event_type_description]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.event_type_name, self.event_type_description, self.custom_attributes, updated_by, self.event_type_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.event_type_uid, self.event_type_name, self.event_type_description, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.event_type_name, self.event_type_description]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.event_type_name, self.event_type_description, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_uid() == obj.get_uid()
    def update_uid(self, uid: str):
        self.event_type_uid = uid
    def update_uid_attributes(self, event_type_uid: str, event_type_name: str, event_type_description: str):
        self.event_type_uid = event_type_uid
        self.event_type_name = event_type_name
        self.event_type_description = event_type_description
    def update_attributes(self, event_type_name: str, event_type_description: str):
        self.event_type_name = event_type_name
        self.event_type_description = event_type_description


@dataclass(frozen=False)
class invoice_action_write_dto(base_write_dto):
    invoice_action_uid: str
    invoice_action_name: str
    tenant_uid: str
    account_uid: str
    invoice_instance_uid: str
    invoice_action_type_uid: str
    def __init__(self, invoice_action_uid: str, invoice_action_name: str, tenant_uid: str, account_uid: str, invoice_instance_uid: str, invoice_action_type_uid: str, custom_attributes: str = "{}"):
        self.invoice_action_uid = invoice_action_uid
        self.invoice_action_name = invoice_action_name
        self.tenant_uid = tenant_uid
        self.account_uid = account_uid
        self.invoice_instance_uid = invoice_instance_uid
        self.invoice_action_type_uid = invoice_action_type_uid
        self.custom_attributes = custom_attributes
    @classmethod
    def empty_write(cls):
        return cls("", "", "", "", "", "")
    @classmethod
    def default_write(cls):
        return cls(base_dto.get_random_uid(), "", "", "", "", "")
    @classmethod
    def random_write(cls):
        return cls(base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid())
    @classmethod
    def new_write(cls, invoice_action_uid: str, invoice_action_name: str, tenant_uid: str, account_uid: str, invoice_instance_uid: str, invoice_action_type_uid: str):
        return cls(invoice_action_uid, invoice_action_name, tenant_uid, account_uid, invoice_instance_uid, invoice_action_type_uid)
    @classmethod
    def new_write_with_defaults(cls, invoice_action_uid: str = "", invoice_action_name: str = "", tenant_uid: str = "", account_uid: str = "", invoice_instance_uid: str = "", invoice_action_type_uid: str = ""):
        return cls(invoice_action_uid, invoice_action_name, tenant_uid, account_uid, invoice_instance_uid, invoice_action_type_uid)
    @classmethod
    def new_write_random_uid(cls, invoice_action_name: str, tenant_uid: str, account_uid: str, invoice_instance_uid: str, invoice_action_type_uid: str):
        return cls(base_dto.get_random_uid(), invoice_action_name, tenant_uid, account_uid, invoice_instance_uid, invoice_action_type_uid)
    @classmethod
    def get_class_model(cls) -> base_model:
        return db_models.invoice_action_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["invoice_action_uid"], d["invoice_action_name"], d["tenant_uid"], d["account_uid"], d["invoice_instance_uid"], d["invoice_action_type_uid"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return invoice_action_write_dto(self.invoice_action_uid, self.invoice_action_name, self.tenant_uid, self.account_uid, self.invoice_instance_uid, self.invoice_action_type_uid, self.custom_attributes)
    def clone_write_new_uid(self):
        return invoice_action_write_dto(base_dto.get_random_uid(), self.invoice_action_name, self.tenant_uid, self.account_uid, self.invoice_instance_uid, self.invoice_action_type_uid, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return invoice_action_write_dto(uid, self.invoice_action_name, self.tenant_uid, self.account_uid, self.invoice_instance_uid, self.invoice_action_type_uid, self.custom_attributes)
    def get_model(self) -> base_model:
        return db_models.invoice_action_model
    def get_uid(self) -> str:
        return self.invoice_action_uid
    def get_name(self) -> str:
        return self.invoice_action_name
    def get_list_values(self) -> list[any]:
        return [self.invoice_action_uid, self.invoice_action_name, self.tenant_uid, self.account_uid, self.invoice_instance_uid, self.invoice_action_type_uid, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.invoice_action_uid, self.invoice_action_name, self.tenant_uid, self.account_uid, self.invoice_instance_uid, self.invoice_action_type_uid]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.invoice_action_name, self.tenant_uid, self.account_uid, self.invoice_instance_uid, self.invoice_action_type_uid, self.custom_attributes, updated_by, self.invoice_action_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.invoice_action_uid, self.invoice_action_name, self.tenant_uid, self.account_uid, self.invoice_instance_uid, self.invoice_action_type_uid, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.invoice_action_name, self.tenant_uid, self.account_uid, self.invoice_instance_uid, self.invoice_action_type_uid]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.invoice_action_name, self.tenant_uid, self.account_uid, self.invoice_instance_uid, self.invoice_action_type_uid, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_uid() == obj.get_uid()
    def update_uid(self, uid: str):
        self.invoice_action_uid = uid
    def update_uid_attributes(self, invoice_action_uid: str, invoice_action_name: str, tenant_uid: str, account_uid: str, invoice_instance_uid: str, invoice_action_type_uid: str):
        self.invoice_action_uid = invoice_action_uid
        self.invoice_action_name = invoice_action_name
        self.tenant_uid = tenant_uid
        self.account_uid = account_uid
        self.invoice_instance_uid = invoice_instance_uid
        self.invoice_action_type_uid = invoice_action_type_uid
    def update_attributes(self, invoice_action_name: str, tenant_uid: str, account_uid: str, invoice_instance_uid: str, invoice_action_type_uid: str):
        self.invoice_action_name = invoice_action_name
        self.tenant_uid = tenant_uid
        self.account_uid = account_uid
        self.invoice_instance_uid = invoice_instance_uid
        self.invoice_action_type_uid = invoice_action_type_uid


@dataclass(frozen=False)
class invoice_action_type_write_dto(base_write_dto):
    invoice_action_type_uid: str
    invoice_action_type_name: str
    def __init__(self, invoice_action_type_uid: str, invoice_action_type_name: str, custom_attributes: str = "{}"):
        self.invoice_action_type_uid = invoice_action_type_uid
        self.invoice_action_type_name = invoice_action_type_name
        self.custom_attributes = custom_attributes
    @classmethod
    def empty_write(cls):
        return cls("", "")
    @classmethod
    def default_write(cls):
        return cls(base_dto.get_random_uid(), "")
    @classmethod
    def random_write(cls):
        return cls(base_dto.get_random_uid(), base_dto.get_random_uid())
    @classmethod
    def new_write(cls, invoice_action_type_uid: str, invoice_action_type_name: str):
        return cls(invoice_action_type_uid, invoice_action_type_name)
    @classmethod
    def new_write_with_defaults(cls, invoice_action_type_uid: str = "", invoice_action_type_name: str = ""):
        return cls(invoice_action_type_uid, invoice_action_type_name)
    @classmethod
    def new_write_random_uid(cls, invoice_action_type_name: str):
        return cls(base_dto.get_random_uid(), invoice_action_type_name)
    @classmethod
    def get_class_model(cls) -> base_model:
        return db_models.invoice_action_type_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["invoice_action_type_uid"], d["invoice_action_type_name"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return invoice_action_type_write_dto(self.invoice_action_type_uid, self.invoice_action_type_name, self.custom_attributes)
    def clone_write_new_uid(self):
        return invoice_action_type_write_dto(base_dto.get_random_uid(), self.invoice_action_type_name, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return invoice_action_type_write_dto(uid, self.invoice_action_type_name, self.custom_attributes)
    def get_model(self) -> base_model:
        return db_models.invoice_action_type_model
    def get_uid(self) -> str:
        return self.invoice_action_type_uid
    def get_name(self) -> str:
        return self.invoice_action_type_name
    def get_list_values(self) -> list[any]:
        return [self.invoice_action_type_uid, self.invoice_action_type_name, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.invoice_action_type_uid, self.invoice_action_type_name]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.invoice_action_type_name, self.custom_attributes, updated_by, self.invoice_action_type_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.invoice_action_type_uid, self.invoice_action_type_name, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.invoice_action_type_name]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.invoice_action_type_name, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_uid() == obj.get_uid()
    def update_uid(self, uid: str):
        self.invoice_action_type_uid = uid
    def update_uid_attributes(self, invoice_action_type_uid: str, invoice_action_type_name: str):
        self.invoice_action_type_uid = invoice_action_type_uid
        self.invoice_action_type_name = invoice_action_type_name
    def update_attributes(self, invoice_action_type_name: str):
        self.invoice_action_type_name = invoice_action_type_name


@dataclass(frozen=False)
class invoice_category_write_dto(base_write_dto):
    invoice_category_uid: str
    invoice_category_name: str
    tenant_uid: str
    invoice_category_description: str
    def __init__(self, invoice_category_uid: str, invoice_category_name: str, tenant_uid: str, invoice_category_description: str, custom_attributes: str = "{}"):
        self.invoice_category_uid = invoice_category_uid
        self.invoice_category_name = invoice_category_name
        self.tenant_uid = tenant_uid
        self.invoice_category_description = invoice_category_description
        self.custom_attributes = custom_attributes
    @classmethod
    def empty_write(cls):
        return cls("", "", "", "")
    @classmethod
    def default_write(cls):
        return cls(base_dto.get_random_uid(), "", "", "")
    @classmethod
    def random_write(cls):
        return cls(base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid())
    @classmethod
    def new_write(cls, invoice_category_uid: str, invoice_category_name: str, tenant_uid: str, invoice_category_description: str):
        return cls(invoice_category_uid, invoice_category_name, tenant_uid, invoice_category_description)
    @classmethod
    def new_write_with_defaults(cls, invoice_category_uid: str = "", invoice_category_name: str = "", tenant_uid: str = "", invoice_category_description: str = ""):
        return cls(invoice_category_uid, invoice_category_name, tenant_uid, invoice_category_description)
    @classmethod
    def new_write_random_uid(cls, invoice_category_name: str, tenant_uid: str, invoice_category_description: str):
        return cls(base_dto.get_random_uid(), invoice_category_name, tenant_uid, invoice_category_description)
    @classmethod
    def get_class_model(cls) -> base_model:
        return db_models.invoice_category_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["invoice_category_uid"], d["invoice_category_name"], d["tenant_uid"], d["invoice_category_description"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return invoice_category_write_dto(self.invoice_category_uid, self.invoice_category_name, self.tenant_uid, self.invoice_category_description, self.custom_attributes)
    def clone_write_new_uid(self):
        return invoice_category_write_dto(base_dto.get_random_uid(), self.invoice_category_name, self.tenant_uid, self.invoice_category_description, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return invoice_category_write_dto(uid, self.invoice_category_name, self.tenant_uid, self.invoice_category_description, self.custom_attributes)
    def get_model(self) -> base_model:
        return db_models.invoice_category_model
    def get_uid(self) -> str:
        return self.invoice_category_uid
    def get_name(self) -> str:
        return self.invoice_category_name
    def get_list_values(self) -> list[any]:
        return [self.invoice_category_uid, self.invoice_category_name, self.tenant_uid, self.invoice_category_description, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.invoice_category_uid, self.invoice_category_name, self.tenant_uid, self.invoice_category_description]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.invoice_category_name, self.tenant_uid, self.invoice_category_description, self.custom_attributes, updated_by, self.invoice_category_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.invoice_category_uid, self.invoice_category_name, self.tenant_uid, self.invoice_category_description, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.invoice_category_name, self.tenant_uid, self.invoice_category_description]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.invoice_category_name, self.tenant_uid, self.invoice_category_description, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_uid() == obj.get_uid()
    def update_uid(self, uid: str):
        self.invoice_category_uid = uid
    def update_uid_attributes(self, invoice_category_uid: str, invoice_category_name: str, tenant_uid: str, invoice_category_description: str):
        self.invoice_category_uid = invoice_category_uid
        self.invoice_category_name = invoice_category_name
        self.tenant_uid = tenant_uid
        self.invoice_category_description = invoice_category_description
    def update_attributes(self, invoice_category_name: str, tenant_uid: str, invoice_category_description: str):
        self.invoice_category_name = invoice_category_name
        self.tenant_uid = tenant_uid
        self.invoice_category_description = invoice_category_description


@dataclass(frozen=False)
class invoice_entry_write_dto(base_write_dto):
    invoice_entry_uid: str
    invoice_entry_name: str
    tenant_uid: str
    account_uid: str
    invoice_instance_uid: str
    entry_details: str
    entry_amount_net: str
    entry_amount_tax: str
    entry_amount_gross: str
    def __init__(self, invoice_entry_uid: str, invoice_entry_name: str, tenant_uid: str, account_uid: str, invoice_instance_uid: str, entry_details: str, entry_amount_net: str, entry_amount_tax: str, entry_amount_gross: str, custom_attributes: str = "{}"):
        self.invoice_entry_uid = invoice_entry_uid
        self.invoice_entry_name = invoice_entry_name
        self.tenant_uid = tenant_uid
        self.account_uid = account_uid
        self.invoice_instance_uid = invoice_instance_uid
        self.entry_details = entry_details
        self.entry_amount_net = entry_amount_net
        self.entry_amount_tax = entry_amount_tax
        self.entry_amount_gross = entry_amount_gross
        self.custom_attributes = custom_attributes
    @classmethod
    def empty_write(cls):
        return cls("", "", "", "", "", "", "", "", "")
    @classmethod
    def default_write(cls):
        return cls(base_dto.get_random_uid(), "", "", "", "", "", "", "", "")
    @classmethod
    def random_write(cls):
        return cls(base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), "", "", "")
    @classmethod
    def new_write(cls, invoice_entry_uid: str, invoice_entry_name: str, tenant_uid: str, account_uid: str, invoice_instance_uid: str, entry_details: str, entry_amount_net: str, entry_amount_tax: str, entry_amount_gross: str):
        return cls(invoice_entry_uid, invoice_entry_name, tenant_uid, account_uid, invoice_instance_uid, entry_details, entry_amount_net, entry_amount_tax, entry_amount_gross)
    @classmethod
    def new_write_with_defaults(cls, invoice_entry_uid: str = "", invoice_entry_name: str = "", tenant_uid: str = "", account_uid: str = "", invoice_instance_uid: str = "", entry_details: str = "", entry_amount_net: str = "", entry_amount_tax: str = "", entry_amount_gross: str = ""):
        return cls(invoice_entry_uid, invoice_entry_name, tenant_uid, account_uid, invoice_instance_uid, entry_details, entry_amount_net, entry_amount_tax, entry_amount_gross)
    @classmethod
    def new_write_random_uid(cls, invoice_entry_name: str, tenant_uid: str, account_uid: str, invoice_instance_uid: str, entry_details: str, entry_amount_net: str, entry_amount_tax: str, entry_amount_gross: str):
        return cls(base_dto.get_random_uid(), invoice_entry_name, tenant_uid, account_uid, invoice_instance_uid, entry_details, entry_amount_net, entry_amount_tax, entry_amount_gross)
    @classmethod
    def get_class_model(cls) -> base_model:
        return db_models.invoice_entry_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["invoice_entry_uid"], d["invoice_entry_name"], d["tenant_uid"], d["account_uid"], d["invoice_instance_uid"], d["entry_details"], d["entry_amount_net"], d["entry_amount_tax"], d["entry_amount_gross"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return invoice_entry_write_dto(self.invoice_entry_uid, self.invoice_entry_name, self.tenant_uid, self.account_uid, self.invoice_instance_uid, self.entry_details, self.entry_amount_net, self.entry_amount_tax, self.entry_amount_gross, self.custom_attributes)
    def clone_write_new_uid(self):
        return invoice_entry_write_dto(base_dto.get_random_uid(), self.invoice_entry_name, self.tenant_uid, self.account_uid, self.invoice_instance_uid, self.entry_details, self.entry_amount_net, self.entry_amount_tax, self.entry_amount_gross, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return invoice_entry_write_dto(uid, self.invoice_entry_name, self.tenant_uid, self.account_uid, self.invoice_instance_uid, self.entry_details, self.entry_amount_net, self.entry_amount_tax, self.entry_amount_gross, self.custom_attributes)
    def get_model(self) -> base_model:
        return db_models.invoice_entry_model
    def get_uid(self) -> str:
        return self.invoice_entry_uid
    def get_name(self) -> str:
        return self.invoice_entry_name
    def get_list_values(self) -> list[any]:
        return [self.invoice_entry_uid, self.invoice_entry_name, self.tenant_uid, self.account_uid, self.invoice_instance_uid, self.entry_details, self.entry_amount_net, self.entry_amount_tax, self.entry_amount_gross, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.invoice_entry_uid, self.invoice_entry_name, self.tenant_uid, self.account_uid, self.invoice_instance_uid, self.entry_details, self.entry_amount_net, self.entry_amount_tax, self.entry_amount_gross]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.invoice_entry_name, self.tenant_uid, self.account_uid, self.invoice_instance_uid, self.entry_details, self.entry_amount_net, self.entry_amount_tax, self.entry_amount_gross, self.custom_attributes, updated_by, self.invoice_entry_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.invoice_entry_uid, self.invoice_entry_name, self.tenant_uid, self.account_uid, self.invoice_instance_uid, self.entry_details, self.entry_amount_net, self.entry_amount_tax, self.entry_amount_gross, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.invoice_entry_name, self.tenant_uid, self.account_uid, self.invoice_instance_uid, self.entry_details, self.entry_amount_net, self.entry_amount_tax, self.entry_amount_gross]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.invoice_entry_name, self.tenant_uid, self.account_uid, self.invoice_instance_uid, self.entry_details, self.entry_amount_net, self.entry_amount_tax, self.entry_amount_gross, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_uid() == obj.get_uid()
    def update_uid(self, uid: str):
        self.invoice_entry_uid = uid
    def update_uid_attributes(self, invoice_entry_uid: str, invoice_entry_name: str, tenant_uid: str, account_uid: str, invoice_instance_uid: str, entry_details: str, entry_amount_net: str, entry_amount_tax: str, entry_amount_gross: str):
        self.invoice_entry_uid = invoice_entry_uid
        self.invoice_entry_name = invoice_entry_name
        self.tenant_uid = tenant_uid
        self.account_uid = account_uid
        self.invoice_instance_uid = invoice_instance_uid
        self.entry_details = entry_details
        self.entry_amount_net = entry_amount_net
        self.entry_amount_tax = entry_amount_tax
        self.entry_amount_gross = entry_amount_gross
    def update_attributes(self, invoice_entry_name: str, tenant_uid: str, account_uid: str, invoice_instance_uid: str, entry_details: str, entry_amount_net: str, entry_amount_tax: str, entry_amount_gross: str):
        self.invoice_entry_name = invoice_entry_name
        self.tenant_uid = tenant_uid
        self.account_uid = account_uid
        self.invoice_instance_uid = invoice_instance_uid
        self.entry_details = entry_details
        self.entry_amount_net = entry_amount_net
        self.entry_amount_tax = entry_amount_tax
        self.entry_amount_gross = entry_amount_gross


@dataclass(frozen=False)
class invoice_flow_write_dto(base_write_dto):
    invoice_flow_uid: str
    invoice_flow_name: str
    class_name: str
    flow_description: str
    flow_definition_json: str
    def __init__(self, invoice_flow_uid: str, invoice_flow_name: str, class_name: str, flow_description: str, flow_definition_json: str, custom_attributes: str = "{}"):
        self.invoice_flow_uid = invoice_flow_uid
        self.invoice_flow_name = invoice_flow_name
        self.class_name = class_name
        self.flow_description = flow_description
        self.flow_definition_json = flow_definition_json
        self.custom_attributes = custom_attributes
    @classmethod
    def empty_write(cls):
        return cls("", "", "", "", "")
    @classmethod
    def default_write(cls):
        return cls(base_dto.get_random_uid(), "", "", "", "")
    @classmethod
    def random_write(cls):
        return cls(base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid())
    @classmethod
    def new_write(cls, invoice_flow_uid: str, invoice_flow_name: str, class_name: str, flow_description: str, flow_definition_json: str):
        return cls(invoice_flow_uid, invoice_flow_name, class_name, flow_description, flow_definition_json)
    @classmethod
    def new_write_with_defaults(cls, invoice_flow_uid: str = "", invoice_flow_name: str = "", class_name: str = "", flow_description: str = "", flow_definition_json: str = ""):
        return cls(invoice_flow_uid, invoice_flow_name, class_name, flow_description, flow_definition_json)
    @classmethod
    def new_write_random_uid(cls, invoice_flow_name: str, class_name: str, flow_description: str, flow_definition_json: str):
        return cls(base_dto.get_random_uid(), invoice_flow_name, class_name, flow_description, flow_definition_json)
    @classmethod
    def get_class_model(cls) -> base_model:
        return db_models.invoice_flow_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["invoice_flow_uid"], d["invoice_flow_name"], d["class_name"], d["flow_description"], d["flow_definition_json"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return invoice_flow_write_dto(self.invoice_flow_uid, self.invoice_flow_name, self.class_name, self.flow_description, self.flow_definition_json, self.custom_attributes)
    def clone_write_new_uid(self):
        return invoice_flow_write_dto(base_dto.get_random_uid(), self.invoice_flow_name, self.class_name, self.flow_description, self.flow_definition_json, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return invoice_flow_write_dto(uid, self.invoice_flow_name, self.class_name, self.flow_description, self.flow_definition_json, self.custom_attributes)
    def get_model(self) -> base_model:
        return db_models.invoice_flow_model
    def get_uid(self) -> str:
        return self.invoice_flow_uid
    def get_name(self) -> str:
        return self.invoice_flow_name
    def get_list_values(self) -> list[any]:
        return [self.invoice_flow_uid, self.invoice_flow_name, self.class_name, self.flow_description, self.flow_definition_json, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.invoice_flow_uid, self.invoice_flow_name, self.class_name, self.flow_description, self.flow_definition_json]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.invoice_flow_name, self.class_name, self.flow_description, self.flow_definition_json, self.custom_attributes, updated_by, self.invoice_flow_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.invoice_flow_uid, self.invoice_flow_name, self.class_name, self.flow_description, self.flow_definition_json, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.invoice_flow_name, self.class_name, self.flow_description, self.flow_definition_json]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.invoice_flow_name, self.class_name, self.flow_description, self.flow_definition_json, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_uid() == obj.get_uid()
    def update_uid(self, uid: str):
        self.invoice_flow_uid = uid
    def update_uid_attributes(self, invoice_flow_uid: str, invoice_flow_name: str, class_name: str, flow_description: str, flow_definition_json: str):
        self.invoice_flow_uid = invoice_flow_uid
        self.invoice_flow_name = invoice_flow_name
        self.class_name = class_name
        self.flow_description = flow_description
        self.flow_definition_json = flow_definition_json
    def update_attributes(self, invoice_flow_name: str, class_name: str, flow_description: str, flow_definition_json: str):
        self.invoice_flow_name = invoice_flow_name
        self.class_name = class_name
        self.flow_description = flow_description
        self.flow_definition_json = flow_definition_json


@dataclass(frozen=False)
class invoice_flow_state_write_dto(base_write_dto):
    invoice_flow_state_uid: str
    invoice_flow_state_name: str
    invoice_flow_uid: str
    state_definition_json: str
    def __init__(self, invoice_flow_state_uid: str, invoice_flow_state_name: str, invoice_flow_uid: str, state_definition_json: str, custom_attributes: str = "{}"):
        self.invoice_flow_state_uid = invoice_flow_state_uid
        self.invoice_flow_state_name = invoice_flow_state_name
        self.invoice_flow_uid = invoice_flow_uid
        self.state_definition_json = state_definition_json
        self.custom_attributes = custom_attributes
    @classmethod
    def empty_write(cls):
        return cls("", "", "", "")
    @classmethod
    def default_write(cls):
        return cls(base_dto.get_random_uid(), "", "", "")
    @classmethod
    def random_write(cls):
        return cls(base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid())
    @classmethod
    def new_write(cls, invoice_flow_state_uid: str, invoice_flow_state_name: str, invoice_flow_uid: str, state_definition_json: str):
        return cls(invoice_flow_state_uid, invoice_flow_state_name, invoice_flow_uid, state_definition_json)
    @classmethod
    def new_write_with_defaults(cls, invoice_flow_state_uid: str = "", invoice_flow_state_name: str = "", invoice_flow_uid: str = "", state_definition_json: str = ""):
        return cls(invoice_flow_state_uid, invoice_flow_state_name, invoice_flow_uid, state_definition_json)
    @classmethod
    def new_write_random_uid(cls, invoice_flow_state_name: str, invoice_flow_uid: str, state_definition_json: str):
        return cls(base_dto.get_random_uid(), invoice_flow_state_name, invoice_flow_uid, state_definition_json)
    @classmethod
    def get_class_model(cls) -> base_model:
        return db_models.invoice_flow_state_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["invoice_flow_state_uid"], d["invoice_flow_state_name"], d["invoice_flow_uid"], d["state_definition_json"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return invoice_flow_state_write_dto(self.invoice_flow_state_uid, self.invoice_flow_state_name, self.invoice_flow_uid, self.state_definition_json, self.custom_attributes)
    def clone_write_new_uid(self):
        return invoice_flow_state_write_dto(base_dto.get_random_uid(), self.invoice_flow_state_name, self.invoice_flow_uid, self.state_definition_json, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return invoice_flow_state_write_dto(uid, self.invoice_flow_state_name, self.invoice_flow_uid, self.state_definition_json, self.custom_attributes)
    def get_model(self) -> base_model:
        return db_models.invoice_flow_state_model
    def get_uid(self) -> str:
        return self.invoice_flow_state_uid
    def get_name(self) -> str:
        return self.invoice_flow_state_name
    def get_list_values(self) -> list[any]:
        return [self.invoice_flow_state_uid, self.invoice_flow_state_name, self.invoice_flow_uid, self.state_definition_json, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.invoice_flow_state_uid, self.invoice_flow_state_name, self.invoice_flow_uid, self.state_definition_json]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.invoice_flow_state_name, self.invoice_flow_uid, self.state_definition_json, self.custom_attributes, updated_by, self.invoice_flow_state_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.invoice_flow_state_uid, self.invoice_flow_state_name, self.invoice_flow_uid, self.state_definition_json, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.invoice_flow_state_name, self.invoice_flow_uid, self.state_definition_json]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.invoice_flow_state_name, self.invoice_flow_uid, self.state_definition_json, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_uid() == obj.get_uid()
    def update_uid(self, uid: str):
        self.invoice_flow_state_uid = uid
    def update_uid_attributes(self, invoice_flow_state_uid: str, invoice_flow_state_name: str, invoice_flow_uid: str, state_definition_json: str):
        self.invoice_flow_state_uid = invoice_flow_state_uid
        self.invoice_flow_state_name = invoice_flow_state_name
        self.invoice_flow_uid = invoice_flow_uid
        self.state_definition_json = state_definition_json
    def update_attributes(self, invoice_flow_state_name: str, invoice_flow_uid: str, state_definition_json: str):
        self.invoice_flow_state_name = invoice_flow_state_name
        self.invoice_flow_uid = invoice_flow_uid
        self.state_definition_json = state_definition_json


@dataclass(frozen=False)
class invoice_instance_write_dto(base_write_dto):
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
    def __init__(self, invoice_instance_uid: str, invoice_instance_name: str, tenant_uid: str, account_uid: str, invoice_flow_uid: str, invoice_status_uid: str, invoice_category_uid: str, invoice_type_uid: str, period_uid: str, currency_uid: str, invoice_number: str, invoice_details: str, invoice_amount_net: str, invoice_amount_tax: str, invoice_amount_gross: str, custom_attributes: str = "{}"):
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
        self.custom_attributes = custom_attributes
    @classmethod
    def empty_write(cls):
        return cls("", "", "", "", "", "", "", "", "", "", "", "", "", "", "")
    @classmethod
    def default_write(cls):
        return cls(base_dto.get_random_uid(), "", "", "", "", "", "", "", "", "", "", "", "", "", "")
    @classmethod
    def random_write(cls):
        return cls(base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), "", "", "")
    @classmethod
    def new_write(cls, invoice_instance_uid: str, invoice_instance_name: str, tenant_uid: str, account_uid: str, invoice_flow_uid: str, invoice_status_uid: str, invoice_category_uid: str, invoice_type_uid: str, period_uid: str, currency_uid: str, invoice_number: str, invoice_details: str, invoice_amount_net: str, invoice_amount_tax: str, invoice_amount_gross: str):
        return cls(invoice_instance_uid, invoice_instance_name, tenant_uid, account_uid, invoice_flow_uid, invoice_status_uid, invoice_category_uid, invoice_type_uid, period_uid, currency_uid, invoice_number, invoice_details, invoice_amount_net, invoice_amount_tax, invoice_amount_gross)
    @classmethod
    def new_write_with_defaults(cls, invoice_instance_uid: str = "", invoice_instance_name: str = "", tenant_uid: str = "", account_uid: str = "", invoice_flow_uid: str = "", invoice_status_uid: str = "", invoice_category_uid: str = "", invoice_type_uid: str = "", period_uid: str = "", currency_uid: str = "", invoice_number: str = "", invoice_details: str = "", invoice_amount_net: str = "", invoice_amount_tax: str = "", invoice_amount_gross: str = ""):
        return cls(invoice_instance_uid, invoice_instance_name, tenant_uid, account_uid, invoice_flow_uid, invoice_status_uid, invoice_category_uid, invoice_type_uid, period_uid, currency_uid, invoice_number, invoice_details, invoice_amount_net, invoice_amount_tax, invoice_amount_gross)
    @classmethod
    def new_write_random_uid(cls, invoice_instance_name: str, tenant_uid: str, account_uid: str, invoice_flow_uid: str, invoice_status_uid: str, invoice_category_uid: str, invoice_type_uid: str, period_uid: str, currency_uid: str, invoice_number: str, invoice_details: str, invoice_amount_net: str, invoice_amount_tax: str, invoice_amount_gross: str):
        return cls(base_dto.get_random_uid(), invoice_instance_name, tenant_uid, account_uid, invoice_flow_uid, invoice_status_uid, invoice_category_uid, invoice_type_uid, period_uid, currency_uid, invoice_number, invoice_details, invoice_amount_net, invoice_amount_tax, invoice_amount_gross)
    @classmethod
    def get_class_model(cls) -> base_model:
        return db_models.invoice_instance_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["invoice_instance_uid"], d["invoice_instance_name"], d["tenant_uid"], d["account_uid"], d["invoice_flow_uid"], d["invoice_status_uid"], d["invoice_category_uid"], d["invoice_type_uid"], d["period_uid"], d["currency_uid"], d["invoice_number"], d["invoice_details"], d["invoice_amount_net"], d["invoice_amount_tax"], d["invoice_amount_gross"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return invoice_instance_write_dto(self.invoice_instance_uid, self.invoice_instance_name, self.tenant_uid, self.account_uid, self.invoice_flow_uid, self.invoice_status_uid, self.invoice_category_uid, self.invoice_type_uid, self.period_uid, self.currency_uid, self.invoice_number, self.invoice_details, self.invoice_amount_net, self.invoice_amount_tax, self.invoice_amount_gross, self.custom_attributes)
    def clone_write_new_uid(self):
        return invoice_instance_write_dto(base_dto.get_random_uid(), self.invoice_instance_name, self.tenant_uid, self.account_uid, self.invoice_flow_uid, self.invoice_status_uid, self.invoice_category_uid, self.invoice_type_uid, self.period_uid, self.currency_uid, self.invoice_number, self.invoice_details, self.invoice_amount_net, self.invoice_amount_tax, self.invoice_amount_gross, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return invoice_instance_write_dto(uid, self.invoice_instance_name, self.tenant_uid, self.account_uid, self.invoice_flow_uid, self.invoice_status_uid, self.invoice_category_uid, self.invoice_type_uid, self.period_uid, self.currency_uid, self.invoice_number, self.invoice_details, self.invoice_amount_net, self.invoice_amount_tax, self.invoice_amount_gross, self.custom_attributes)
    def get_model(self) -> base_model:
        return db_models.invoice_instance_model
    def get_uid(self) -> str:
        return self.invoice_instance_uid
    def get_name(self) -> str:
        return self.invoice_instance_name
    def get_list_values(self) -> list[any]:
        return [self.invoice_instance_uid, self.invoice_instance_name, self.tenant_uid, self.account_uid, self.invoice_flow_uid, self.invoice_status_uid, self.invoice_category_uid, self.invoice_type_uid, self.period_uid, self.currency_uid, self.invoice_number, self.invoice_details, self.invoice_amount_net, self.invoice_amount_tax, self.invoice_amount_gross, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.invoice_instance_uid, self.invoice_instance_name, self.tenant_uid, self.account_uid, self.invoice_flow_uid, self.invoice_status_uid, self.invoice_category_uid, self.invoice_type_uid, self.period_uid, self.currency_uid, self.invoice_number, self.invoice_details, self.invoice_amount_net, self.invoice_amount_tax, self.invoice_amount_gross]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.invoice_instance_name, self.tenant_uid, self.account_uid, self.invoice_flow_uid, self.invoice_status_uid, self.invoice_category_uid, self.invoice_type_uid, self.period_uid, self.currency_uid, self.invoice_number, self.invoice_details, self.invoice_amount_net, self.invoice_amount_tax, self.invoice_amount_gross, self.custom_attributes, updated_by, self.invoice_instance_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.invoice_instance_uid, self.invoice_instance_name, self.tenant_uid, self.account_uid, self.invoice_flow_uid, self.invoice_status_uid, self.invoice_category_uid, self.invoice_type_uid, self.period_uid, self.currency_uid, self.invoice_number, self.invoice_details, self.invoice_amount_net, self.invoice_amount_tax, self.invoice_amount_gross, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.invoice_instance_name, self.tenant_uid, self.account_uid, self.invoice_flow_uid, self.invoice_status_uid, self.invoice_category_uid, self.invoice_type_uid, self.period_uid, self.currency_uid, self.invoice_number, self.invoice_details, self.invoice_amount_net, self.invoice_amount_tax, self.invoice_amount_gross]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.invoice_instance_name, self.tenant_uid, self.account_uid, self.invoice_flow_uid, self.invoice_status_uid, self.invoice_category_uid, self.invoice_type_uid, self.period_uid, self.currency_uid, self.invoice_number, self.invoice_details, self.invoice_amount_net, self.invoice_amount_tax, self.invoice_amount_gross, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_uid() == obj.get_uid()
    def update_uid(self, uid: str):
        self.invoice_instance_uid = uid
    def update_uid_attributes(self, invoice_instance_uid: str, invoice_instance_name: str, tenant_uid: str, account_uid: str, invoice_flow_uid: str, invoice_status_uid: str, invoice_category_uid: str, invoice_type_uid: str, period_uid: str, currency_uid: str, invoice_number: str, invoice_details: str, invoice_amount_net: str, invoice_amount_tax: str, invoice_amount_gross: str):
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
    def update_attributes(self, invoice_instance_name: str, tenant_uid: str, account_uid: str, invoice_flow_uid: str, invoice_status_uid: str, invoice_category_uid: str, invoice_type_uid: str, period_uid: str, currency_uid: str, invoice_number: str, invoice_details: str, invoice_amount_net: str, invoice_amount_tax: str, invoice_amount_gross: str):
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


@dataclass(frozen=False)
class invoice_status_write_dto(base_write_dto):
    invoice_status_uid: str
    invoice_status_name: str
    status_description: str
    def __init__(self, invoice_status_uid: str, invoice_status_name: str, status_description: str, custom_attributes: str = "{}"):
        self.invoice_status_uid = invoice_status_uid
        self.invoice_status_name = invoice_status_name
        self.status_description = status_description
        self.custom_attributes = custom_attributes
    @classmethod
    def empty_write(cls):
        return cls("", "", "")
    @classmethod
    def default_write(cls):
        return cls(base_dto.get_random_uid(), "", "")
    @classmethod
    def random_write(cls):
        return cls(base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid())
    @classmethod
    def new_write(cls, invoice_status_uid: str, invoice_status_name: str, status_description: str):
        return cls(invoice_status_uid, invoice_status_name, status_description)
    @classmethod
    def new_write_with_defaults(cls, invoice_status_uid: str = "", invoice_status_name: str = "", status_description: str = ""):
        return cls(invoice_status_uid, invoice_status_name, status_description)
    @classmethod
    def new_write_random_uid(cls, invoice_status_name: str, status_description: str):
        return cls(base_dto.get_random_uid(), invoice_status_name, status_description)
    @classmethod
    def get_class_model(cls) -> base_model:
        return db_models.invoice_status_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["invoice_status_uid"], d["invoice_status_name"], d["status_description"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return invoice_status_write_dto(self.invoice_status_uid, self.invoice_status_name, self.status_description, self.custom_attributes)
    def clone_write_new_uid(self):
        return invoice_status_write_dto(base_dto.get_random_uid(), self.invoice_status_name, self.status_description, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return invoice_status_write_dto(uid, self.invoice_status_name, self.status_description, self.custom_attributes)
    def get_model(self) -> base_model:
        return db_models.invoice_status_model
    def get_uid(self) -> str:
        return self.invoice_status_uid
    def get_name(self) -> str:
        return self.invoice_status_name
    def get_list_values(self) -> list[any]:
        return [self.invoice_status_uid, self.invoice_status_name, self.status_description, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.invoice_status_uid, self.invoice_status_name, self.status_description]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.invoice_status_name, self.status_description, self.custom_attributes, updated_by, self.invoice_status_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.invoice_status_uid, self.invoice_status_name, self.status_description, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.invoice_status_name, self.status_description]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.invoice_status_name, self.status_description, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_uid() == obj.get_uid()
    def update_uid(self, uid: str):
        self.invoice_status_uid = uid
    def update_uid_attributes(self, invoice_status_uid: str, invoice_status_name: str, status_description: str):
        self.invoice_status_uid = invoice_status_uid
        self.invoice_status_name = invoice_status_name
        self.status_description = status_description
    def update_attributes(self, invoice_status_name: str, status_description: str):
        self.invoice_status_name = invoice_status_name
        self.status_description = status_description


@dataclass(frozen=False)
class invoice_type_write_dto(base_write_dto):
    invoice_type_uid: str
    invoice_type_name: str
    def __init__(self, invoice_type_uid: str, invoice_type_name: str, custom_attributes: str = "{}"):
        self.invoice_type_uid = invoice_type_uid
        self.invoice_type_name = invoice_type_name
        self.custom_attributes = custom_attributes
    @classmethod
    def empty_write(cls):
        return cls("", "")
    @classmethod
    def default_write(cls):
        return cls(base_dto.get_random_uid(), "")
    @classmethod
    def random_write(cls):
        return cls(base_dto.get_random_uid(), base_dto.get_random_uid())
    @classmethod
    def new_write(cls, invoice_type_uid: str, invoice_type_name: str):
        return cls(invoice_type_uid, invoice_type_name)
    @classmethod
    def new_write_with_defaults(cls, invoice_type_uid: str = "", invoice_type_name: str = ""):
        return cls(invoice_type_uid, invoice_type_name)
    @classmethod
    def new_write_random_uid(cls, invoice_type_name: str):
        return cls(base_dto.get_random_uid(), invoice_type_name)
    @classmethod
    def get_class_model(cls) -> base_model:
        return db_models.invoice_type_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["invoice_type_uid"], d["invoice_type_name"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return invoice_type_write_dto(self.invoice_type_uid, self.invoice_type_name, self.custom_attributes)
    def clone_write_new_uid(self):
        return invoice_type_write_dto(base_dto.get_random_uid(), self.invoice_type_name, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return invoice_type_write_dto(uid, self.invoice_type_name, self.custom_attributes)
    def get_model(self) -> base_model:
        return db_models.invoice_type_model
    def get_uid(self) -> str:
        return self.invoice_type_uid
    def get_name(self) -> str:
        return self.invoice_type_name
    def get_list_values(self) -> list[any]:
        return [self.invoice_type_uid, self.invoice_type_name, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.invoice_type_uid, self.invoice_type_name]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.invoice_type_name, self.custom_attributes, updated_by, self.invoice_type_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.invoice_type_uid, self.invoice_type_name, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.invoice_type_name]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.invoice_type_name, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_uid() == obj.get_uid()
    def update_uid(self, uid: str):
        self.invoice_type_uid = uid
    def update_uid_attributes(self, invoice_type_uid: str, invoice_type_name: str):
        self.invoice_type_uid = invoice_type_uid
        self.invoice_type_name = invoice_type_name
    def update_attributes(self, invoice_type_name: str):
        self.invoice_type_name = invoice_type_name


@dataclass(frozen=False)
class location_hierarchy_write_dto(base_write_dto):
    location_hierarchy_uid: str
    location_hierarchy_name: str
    tenant_uid: str
    country_uid: str | None
    hierarchy_description: str
    def __init__(self, location_hierarchy_uid: str, location_hierarchy_name: str, tenant_uid: str, country_uid: str | None, hierarchy_description: str, custom_attributes: str = "{}"):
        self.location_hierarchy_uid = location_hierarchy_uid
        self.location_hierarchy_name = location_hierarchy_name
        self.tenant_uid = tenant_uid
        self.country_uid = country_uid
        self.hierarchy_description = hierarchy_description
        self.custom_attributes = custom_attributes
    @classmethod
    def empty_write(cls):
        return cls("", "", "", "", "")
    @classmethod
    def default_write(cls):
        return cls(base_dto.get_random_uid(), "", "", "", "")
    @classmethod
    def random_write(cls):
        return cls(base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid())
    @classmethod
    def new_write(cls, location_hierarchy_uid: str, location_hierarchy_name: str, tenant_uid: str, country_uid: str | None, hierarchy_description: str):
        return cls(location_hierarchy_uid, location_hierarchy_name, tenant_uid, country_uid, hierarchy_description)
    @classmethod
    def new_write_with_defaults(cls, location_hierarchy_uid: str = "", location_hierarchy_name: str = "", tenant_uid: str = "", country_uid: str | None = "", hierarchy_description: str = ""):
        return cls(location_hierarchy_uid, location_hierarchy_name, tenant_uid, country_uid, hierarchy_description)
    @classmethod
    def new_write_random_uid(cls, location_hierarchy_name: str, tenant_uid: str, country_uid: str | None, hierarchy_description: str):
        return cls(base_dto.get_random_uid(), location_hierarchy_name, tenant_uid, country_uid, hierarchy_description)
    @classmethod
    def get_class_model(cls) -> base_model:
        return db_models.location_hierarchy_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["location_hierarchy_uid"], d["location_hierarchy_name"], d["tenant_uid"], d["country_uid"], d["hierarchy_description"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return location_hierarchy_write_dto(self.location_hierarchy_uid, self.location_hierarchy_name, self.tenant_uid, self.country_uid, self.hierarchy_description, self.custom_attributes)
    def clone_write_new_uid(self):
        return location_hierarchy_write_dto(base_dto.get_random_uid(), self.location_hierarchy_name, self.tenant_uid, self.country_uid, self.hierarchy_description, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return location_hierarchy_write_dto(uid, self.location_hierarchy_name, self.tenant_uid, self.country_uid, self.hierarchy_description, self.custom_attributes)
    def get_model(self) -> base_model:
        return db_models.location_hierarchy_model
    def get_uid(self) -> str:
        return self.location_hierarchy_uid
    def get_name(self) -> str:
        return self.location_hierarchy_name
    def get_list_values(self) -> list[any]:
        return [self.location_hierarchy_uid, self.location_hierarchy_name, self.tenant_uid, self.country_uid, self.hierarchy_description, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.location_hierarchy_uid, self.location_hierarchy_name, self.tenant_uid, self.country_uid, self.hierarchy_description]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.location_hierarchy_name, self.tenant_uid, self.country_uid, self.hierarchy_description, self.custom_attributes, updated_by, self.location_hierarchy_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.location_hierarchy_uid, self.location_hierarchy_name, self.tenant_uid, self.country_uid, self.hierarchy_description, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.location_hierarchy_name, self.tenant_uid, self.country_uid, self.hierarchy_description]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.location_hierarchy_name, self.tenant_uid, self.country_uid, self.hierarchy_description, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_uid() == obj.get_uid()
    def update_uid(self, uid: str):
        self.location_hierarchy_uid = uid
    def update_uid_attributes(self, location_hierarchy_uid: str, location_hierarchy_name: str, tenant_uid: str, country_uid: str | None, hierarchy_description: str):
        self.location_hierarchy_uid = location_hierarchy_uid
        self.location_hierarchy_name = location_hierarchy_name
        self.tenant_uid = tenant_uid
        self.country_uid = country_uid
        self.hierarchy_description = hierarchy_description
    def update_attributes(self, location_hierarchy_name: str, tenant_uid: str, country_uid: str | None, hierarchy_description: str):
        self.location_hierarchy_name = location_hierarchy_name
        self.tenant_uid = tenant_uid
        self.country_uid = country_uid
        self.hierarchy_description = hierarchy_description


@dataclass(frozen=False)
class location_postal_code_write_dto(base_write_dto):
    location_postal_code_uid: str
    location_postal_code_name: str
    country_uid: str
    postal_code: str
    street_name: str
    city_name: str
    county_name: str
    state_name: str
    region_name: str
    def __init__(self, location_postal_code_uid: str, location_postal_code_name: str, country_uid: str, postal_code: str, street_name: str, city_name: str, county_name: str, state_name: str, region_name: str, custom_attributes: str = "{}"):
        self.location_postal_code_uid = location_postal_code_uid
        self.location_postal_code_name = location_postal_code_name
        self.country_uid = country_uid
        self.postal_code = postal_code
        self.street_name = street_name
        self.city_name = city_name
        self.county_name = county_name
        self.state_name = state_name
        self.region_name = region_name
        self.custom_attributes = custom_attributes
    @classmethod
    def empty_write(cls):
        return cls("", "", "", "", "", "", "", "", "")
    @classmethod
    def default_write(cls):
        return cls(base_dto.get_random_uid(), "", "", "", "", "", "", "", "")
    @classmethod
    def random_write(cls):
        return cls(base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid())
    @classmethod
    def new_write(cls, location_postal_code_uid: str, location_postal_code_name: str, country_uid: str, postal_code: str, street_name: str, city_name: str, county_name: str, state_name: str, region_name: str):
        return cls(location_postal_code_uid, location_postal_code_name, country_uid, postal_code, street_name, city_name, county_name, state_name, region_name)
    @classmethod
    def new_write_with_defaults(cls, location_postal_code_uid: str = "", location_postal_code_name: str = "", country_uid: str = "", postal_code: str = "", street_name: str = "", city_name: str = "", county_name: str = "", state_name: str = "", region_name: str = ""):
        return cls(location_postal_code_uid, location_postal_code_name, country_uid, postal_code, street_name, city_name, county_name, state_name, region_name)
    @classmethod
    def new_write_random_uid(cls, location_postal_code_name: str, country_uid: str, postal_code: str, street_name: str, city_name: str, county_name: str, state_name: str, region_name: str):
        return cls(base_dto.get_random_uid(), location_postal_code_name, country_uid, postal_code, street_name, city_name, county_name, state_name, region_name)
    @classmethod
    def get_class_model(cls) -> base_model:
        return db_models.location_postal_code_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["location_postal_code_uid"], d["location_postal_code_name"], d["country_uid"], d["postal_code"], d["street_name"], d["city_name"], d["county_name"], d["state_name"], d["region_name"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return location_postal_code_write_dto(self.location_postal_code_uid, self.location_postal_code_name, self.country_uid, self.postal_code, self.street_name, self.city_name, self.county_name, self.state_name, self.region_name, self.custom_attributes)
    def clone_write_new_uid(self):
        return location_postal_code_write_dto(base_dto.get_random_uid(), self.location_postal_code_name, self.country_uid, self.postal_code, self.street_name, self.city_name, self.county_name, self.state_name, self.region_name, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return location_postal_code_write_dto(uid, self.location_postal_code_name, self.country_uid, self.postal_code, self.street_name, self.city_name, self.county_name, self.state_name, self.region_name, self.custom_attributes)
    def get_model(self) -> base_model:
        return db_models.location_postal_code_model
    def get_uid(self) -> str:
        return self.location_postal_code_uid
    def get_name(self) -> str:
        return self.location_postal_code_name
    def get_list_values(self) -> list[any]:
        return [self.location_postal_code_uid, self.location_postal_code_name, self.country_uid, self.postal_code, self.street_name, self.city_name, self.county_name, self.state_name, self.region_name, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.location_postal_code_uid, self.location_postal_code_name, self.country_uid, self.postal_code, self.street_name, self.city_name, self.county_name, self.state_name, self.region_name]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.location_postal_code_name, self.country_uid, self.postal_code, self.street_name, self.city_name, self.county_name, self.state_name, self.region_name, self.custom_attributes, updated_by, self.location_postal_code_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.location_postal_code_uid, self.location_postal_code_name, self.country_uid, self.postal_code, self.street_name, self.city_name, self.county_name, self.state_name, self.region_name, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.location_postal_code_name, self.country_uid, self.postal_code, self.street_name, self.city_name, self.county_name, self.state_name, self.region_name]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.location_postal_code_name, self.country_uid, self.postal_code, self.street_name, self.city_name, self.county_name, self.state_name, self.region_name, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_uid() == obj.get_uid()
    def update_uid(self, uid: str):
        self.location_postal_code_uid = uid
    def update_uid_attributes(self, location_postal_code_uid: str, location_postal_code_name: str, country_uid: str, postal_code: str, street_name: str, city_name: str, county_name: str, state_name: str, region_name: str):
        self.location_postal_code_uid = location_postal_code_uid
        self.location_postal_code_name = location_postal_code_name
        self.country_uid = country_uid
        self.postal_code = postal_code
        self.street_name = street_name
        self.city_name = city_name
        self.county_name = county_name
        self.state_name = state_name
        self.region_name = region_name
    def update_attributes(self, location_postal_code_name: str, country_uid: str, postal_code: str, street_name: str, city_name: str, county_name: str, state_name: str, region_name: str):
        self.location_postal_code_name = location_postal_code_name
        self.country_uid = country_uid
        self.postal_code = postal_code
        self.street_name = street_name
        self.city_name = city_name
        self.county_name = county_name
        self.state_name = state_name
        self.region_name = region_name


@dataclass(frozen=False)
class location_region_write_dto(base_write_dto):
    location_region_uid: str
    location_region_name: str
    tenant_uid: str
    location_hierarchy_uid: str
    location_territory_uid: str | None
    parent_location_region_uid: str | None
    country_uid: str | None
    region_latitude: str
    region_longitude: str
    region_description: str
    def __init__(self, location_region_uid: str, location_region_name: str, tenant_uid: str, location_hierarchy_uid: str, location_territory_uid: str | None, parent_location_region_uid: str | None, country_uid: str | None, region_latitude: str, region_longitude: str, region_description: str, custom_attributes: str = "{}"):
        self.location_region_uid = location_region_uid
        self.location_region_name = location_region_name
        self.tenant_uid = tenant_uid
        self.location_hierarchy_uid = location_hierarchy_uid
        self.location_territory_uid = location_territory_uid
        self.parent_location_region_uid = parent_location_region_uid
        self.country_uid = country_uid
        self.region_latitude = region_latitude
        self.region_longitude = region_longitude
        self.region_description = region_description
        self.custom_attributes = custom_attributes
    @classmethod
    def empty_write(cls):
        return cls("", "", "", "", "", "", "", "", "", "")
    @classmethod
    def default_write(cls):
        return cls(base_dto.get_random_uid(), "", "", "", "", "", "", "", "", "")
    @classmethod
    def random_write(cls):
        return cls(base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), "", "", base_dto.get_random_uid())
    @classmethod
    def new_write(cls, location_region_uid: str, location_region_name: str, tenant_uid: str, location_hierarchy_uid: str, location_territory_uid: str | None, parent_location_region_uid: str | None, country_uid: str | None, region_latitude: str, region_longitude: str, region_description: str):
        return cls(location_region_uid, location_region_name, tenant_uid, location_hierarchy_uid, location_territory_uid, parent_location_region_uid, country_uid, region_latitude, region_longitude, region_description)
    @classmethod
    def new_write_with_defaults(cls, location_region_uid: str = "", location_region_name: str = "", tenant_uid: str = "", location_hierarchy_uid: str = "", location_territory_uid: str | None = "", parent_location_region_uid: str | None = "", country_uid: str | None = "", region_latitude: str = "", region_longitude: str = "", region_description: str = ""):
        return cls(location_region_uid, location_region_name, tenant_uid, location_hierarchy_uid, location_territory_uid, parent_location_region_uid, country_uid, region_latitude, region_longitude, region_description)
    @classmethod
    def new_write_random_uid(cls, location_region_name: str, tenant_uid: str, location_hierarchy_uid: str, location_territory_uid: str | None, parent_location_region_uid: str | None, country_uid: str | None, region_latitude: str, region_longitude: str, region_description: str):
        return cls(base_dto.get_random_uid(), location_region_name, tenant_uid, location_hierarchy_uid, location_territory_uid, parent_location_region_uid, country_uid, region_latitude, region_longitude, region_description)
    @classmethod
    def get_class_model(cls) -> base_model:
        return db_models.location_region_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["location_region_uid"], d["location_region_name"], d["tenant_uid"], d["location_hierarchy_uid"], d["location_territory_uid"], d["parent_location_region_uid"], d["country_uid"], d["region_latitude"], d["region_longitude"], d["region_description"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return location_region_write_dto(self.location_region_uid, self.location_region_name, self.tenant_uid, self.location_hierarchy_uid, self.location_territory_uid, self.parent_location_region_uid, self.country_uid, self.region_latitude, self.region_longitude, self.region_description, self.custom_attributes)
    def clone_write_new_uid(self):
        return location_region_write_dto(base_dto.get_random_uid(), self.location_region_name, self.tenant_uid, self.location_hierarchy_uid, self.location_territory_uid, self.parent_location_region_uid, self.country_uid, self.region_latitude, self.region_longitude, self.region_description, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return location_region_write_dto(uid, self.location_region_name, self.tenant_uid, self.location_hierarchy_uid, self.location_territory_uid, self.parent_location_region_uid, self.country_uid, self.region_latitude, self.region_longitude, self.region_description, self.custom_attributes)
    def get_model(self) -> base_model:
        return db_models.location_region_model
    def get_uid(self) -> str:
        return self.location_region_uid
    def get_name(self) -> str:
        return self.location_region_name
    def get_list_values(self) -> list[any]:
        return [self.location_region_uid, self.location_region_name, self.tenant_uid, self.location_hierarchy_uid, self.location_territory_uid, self.parent_location_region_uid, self.country_uid, self.region_latitude, self.region_longitude, self.region_description, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.location_region_uid, self.location_region_name, self.tenant_uid, self.location_hierarchy_uid, self.location_territory_uid, self.parent_location_region_uid, self.country_uid, self.region_latitude, self.region_longitude, self.region_description]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.location_region_name, self.tenant_uid, self.location_hierarchy_uid, self.location_territory_uid, self.parent_location_region_uid, self.country_uid, self.region_latitude, self.region_longitude, self.region_description, self.custom_attributes, updated_by, self.location_region_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.location_region_uid, self.location_region_name, self.tenant_uid, self.location_hierarchy_uid, self.location_territory_uid, self.parent_location_region_uid, self.country_uid, self.region_latitude, self.region_longitude, self.region_description, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.location_region_name, self.tenant_uid, self.location_hierarchy_uid, self.location_territory_uid, self.parent_location_region_uid, self.country_uid, self.region_latitude, self.region_longitude, self.region_description]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.location_region_name, self.tenant_uid, self.location_hierarchy_uid, self.location_territory_uid, self.parent_location_region_uid, self.country_uid, self.region_latitude, self.region_longitude, self.region_description, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_uid() == obj.get_uid()
    def update_uid(self, uid: str):
        self.location_region_uid = uid
    def update_uid_attributes(self, location_region_uid: str, location_region_name: str, tenant_uid: str, location_hierarchy_uid: str, location_territory_uid: str | None, parent_location_region_uid: str | None, country_uid: str | None, region_latitude: str, region_longitude: str, region_description: str):
        self.location_region_uid = location_region_uid
        self.location_region_name = location_region_name
        self.tenant_uid = tenant_uid
        self.location_hierarchy_uid = location_hierarchy_uid
        self.location_territory_uid = location_territory_uid
        self.parent_location_region_uid = parent_location_region_uid
        self.country_uid = country_uid
        self.region_latitude = region_latitude
        self.region_longitude = region_longitude
        self.region_description = region_description
    def update_attributes(self, location_region_name: str, tenant_uid: str, location_hierarchy_uid: str, location_territory_uid: str | None, parent_location_region_uid: str | None, country_uid: str | None, region_latitude: str, region_longitude: str, region_description: str):
        self.location_region_name = location_region_name
        self.tenant_uid = tenant_uid
        self.location_hierarchy_uid = location_hierarchy_uid
        self.location_territory_uid = location_territory_uid
        self.parent_location_region_uid = parent_location_region_uid
        self.country_uid = country_uid
        self.region_latitude = region_latitude
        self.region_longitude = region_longitude
        self.region_description = region_description


@dataclass(frozen=False)
class location_territory_write_dto(base_write_dto):
    location_territory_uid: str
    location_territory_name: str
    tenant_uid: str
    location_postal_code_uid: str
    territory_latitude: str
    territory_longitude: str
    territory_description: str
    def __init__(self, location_territory_uid: str, location_territory_name: str, tenant_uid: str, location_postal_code_uid: str, territory_latitude: str, territory_longitude: str, territory_description: str, custom_attributes: str = "{}"):
        self.location_territory_uid = location_territory_uid
        self.location_territory_name = location_territory_name
        self.tenant_uid = tenant_uid
        self.location_postal_code_uid = location_postal_code_uid
        self.territory_latitude = territory_latitude
        self.territory_longitude = territory_longitude
        self.territory_description = territory_description
        self.custom_attributes = custom_attributes
    @classmethod
    def empty_write(cls):
        return cls("", "", "", "", "", "", "")
    @classmethod
    def default_write(cls):
        return cls(base_dto.get_random_uid(), "", "", "", "", "", "")
    @classmethod
    def random_write(cls):
        return cls(base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), "", "", base_dto.get_random_uid())
    @classmethod
    def new_write(cls, location_territory_uid: str, location_territory_name: str, tenant_uid: str, location_postal_code_uid: str, territory_latitude: str, territory_longitude: str, territory_description: str):
        return cls(location_territory_uid, location_territory_name, tenant_uid, location_postal_code_uid, territory_latitude, territory_longitude, territory_description)
    @classmethod
    def new_write_with_defaults(cls, location_territory_uid: str = "", location_territory_name: str = "", tenant_uid: str = "", location_postal_code_uid: str = "", territory_latitude: str = "", territory_longitude: str = "", territory_description: str = ""):
        return cls(location_territory_uid, location_territory_name, tenant_uid, location_postal_code_uid, territory_latitude, territory_longitude, territory_description)
    @classmethod
    def new_write_random_uid(cls, location_territory_name: str, tenant_uid: str, location_postal_code_uid: str, territory_latitude: str, territory_longitude: str, territory_description: str):
        return cls(base_dto.get_random_uid(), location_territory_name, tenant_uid, location_postal_code_uid, territory_latitude, territory_longitude, territory_description)
    @classmethod
    def get_class_model(cls) -> base_model:
        return db_models.location_territory_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["location_territory_uid"], d["location_territory_name"], d["tenant_uid"], d["location_postal_code_uid"], d["territory_latitude"], d["territory_longitude"], d["territory_description"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return location_territory_write_dto(self.location_territory_uid, self.location_territory_name, self.tenant_uid, self.location_postal_code_uid, self.territory_latitude, self.territory_longitude, self.territory_description, self.custom_attributes)
    def clone_write_new_uid(self):
        return location_territory_write_dto(base_dto.get_random_uid(), self.location_territory_name, self.tenant_uid, self.location_postal_code_uid, self.territory_latitude, self.territory_longitude, self.territory_description, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return location_territory_write_dto(uid, self.location_territory_name, self.tenant_uid, self.location_postal_code_uid, self.territory_latitude, self.territory_longitude, self.territory_description, self.custom_attributes)
    def get_model(self) -> base_model:
        return db_models.location_territory_model
    def get_uid(self) -> str:
        return self.location_territory_uid
    def get_name(self) -> str:
        return self.location_territory_name
    def get_list_values(self) -> list[any]:
        return [self.location_territory_uid, self.location_territory_name, self.tenant_uid, self.location_postal_code_uid, self.territory_latitude, self.territory_longitude, self.territory_description, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.location_territory_uid, self.location_territory_name, self.tenant_uid, self.location_postal_code_uid, self.territory_latitude, self.territory_longitude, self.territory_description]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.location_territory_name, self.tenant_uid, self.location_postal_code_uid, self.territory_latitude, self.territory_longitude, self.territory_description, self.custom_attributes, updated_by, self.location_territory_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.location_territory_uid, self.location_territory_name, self.tenant_uid, self.location_postal_code_uid, self.territory_latitude, self.territory_longitude, self.territory_description, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.location_territory_name, self.tenant_uid, self.location_postal_code_uid, self.territory_latitude, self.territory_longitude, self.territory_description]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.location_territory_name, self.tenant_uid, self.location_postal_code_uid, self.territory_latitude, self.territory_longitude, self.territory_description, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_uid() == obj.get_uid()
    def update_uid(self, uid: str):
        self.location_territory_uid = uid
    def update_uid_attributes(self, location_territory_uid: str, location_territory_name: str, tenant_uid: str, location_postal_code_uid: str, territory_latitude: str, territory_longitude: str, territory_description: str):
        self.location_territory_uid = location_territory_uid
        self.location_territory_name = location_territory_name
        self.tenant_uid = tenant_uid
        self.location_postal_code_uid = location_postal_code_uid
        self.territory_latitude = territory_latitude
        self.territory_longitude = territory_longitude
        self.territory_description = territory_description
    def update_attributes(self, location_territory_name: str, tenant_uid: str, location_postal_code_uid: str, territory_latitude: str, territory_longitude: str, territory_description: str):
        self.location_territory_name = location_territory_name
        self.tenant_uid = tenant_uid
        self.location_postal_code_uid = location_postal_code_uid
        self.territory_latitude = territory_latitude
        self.territory_longitude = territory_longitude
        self.territory_description = territory_description


@dataclass(frozen=False)
class monitor_write_dto(base_write_dto):
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
    def __init__(self, monitor_uid: str, monitor_name: str, tenant_uid: str, account_uid: str, monitor_type_uid: str, schedule_expression: str, monitor_protocol: str, monitor_url: str, monitor_user: str, monitor_priority: int, is_on_hold: int, last_status_name: str, last_run_time: str, last_exception_message: str, custom_attributes: str = "{}"):
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
        self.custom_attributes = custom_attributes
    @classmethod
    def empty_write(cls):
        return cls("", "", "", "", "", "", "", "", "", 0, 0, "", "", "")
    @classmethod
    def default_write(cls):
        return cls(base_dto.get_random_uid(), "", "", "", "", "", "", "", "", 0, 0, "", "", "")
    @classmethod
    def random_write(cls):
        return cls(base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), 0, 0, base_dto.get_random_uid(), "", base_dto.get_random_uid())
    @classmethod
    def new_write(cls, monitor_uid: str, monitor_name: str, tenant_uid: str, account_uid: str, monitor_type_uid: str, schedule_expression: str, monitor_protocol: str, monitor_url: str, monitor_user: str, monitor_priority: int, is_on_hold: int, last_status_name: str, last_run_time: str, last_exception_message: str):
        return cls(monitor_uid, monitor_name, tenant_uid, account_uid, monitor_type_uid, schedule_expression, monitor_protocol, monitor_url, monitor_user, monitor_priority, is_on_hold, last_status_name, last_run_time, last_exception_message)
    @classmethod
    def new_write_with_defaults(cls, monitor_uid: str = "", monitor_name: str = "", tenant_uid: str = "", account_uid: str = "", monitor_type_uid: str = "", schedule_expression: str = "", monitor_protocol: str = "", monitor_url: str = "", monitor_user: str = "", monitor_priority: int = 0, is_on_hold: int = 0, last_status_name: str = "", last_run_time: str = "", last_exception_message: str = ""):
        return cls(monitor_uid, monitor_name, tenant_uid, account_uid, monitor_type_uid, schedule_expression, monitor_protocol, monitor_url, monitor_user, monitor_priority, is_on_hold, last_status_name, last_run_time, last_exception_message)
    @classmethod
    def new_write_random_uid(cls, monitor_name: str, tenant_uid: str, account_uid: str, monitor_type_uid: str, schedule_expression: str, monitor_protocol: str, monitor_url: str, monitor_user: str, monitor_priority: int, is_on_hold: int, last_status_name: str, last_run_time: str, last_exception_message: str):
        return cls(base_dto.get_random_uid(), monitor_name, tenant_uid, account_uid, monitor_type_uid, schedule_expression, monitor_protocol, monitor_url, monitor_user, monitor_priority, is_on_hold, last_status_name, last_run_time, last_exception_message)
    @classmethod
    def get_class_model(cls) -> base_model:
        return db_models.monitor_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["monitor_uid"], d["monitor_name"], d["tenant_uid"], d["account_uid"], d["monitor_type_uid"], d["schedule_expression"], d["monitor_protocol"], d["monitor_url"], d["monitor_user"], d["monitor_priority"], d["is_on_hold"], d["last_status_name"], d["last_run_time"], d["last_exception_message"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return monitor_write_dto(self.monitor_uid, self.monitor_name, self.tenant_uid, self.account_uid, self.monitor_type_uid, self.schedule_expression, self.monitor_protocol, self.monitor_url, self.monitor_user, self.monitor_priority, self.is_on_hold, self.last_status_name, self.last_run_time, self.last_exception_message, self.custom_attributes)
    def clone_write_new_uid(self):
        return monitor_write_dto(base_dto.get_random_uid(), self.monitor_name, self.tenant_uid, self.account_uid, self.monitor_type_uid, self.schedule_expression, self.monitor_protocol, self.monitor_url, self.monitor_user, self.monitor_priority, self.is_on_hold, self.last_status_name, self.last_run_time, self.last_exception_message, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return monitor_write_dto(uid, self.monitor_name, self.tenant_uid, self.account_uid, self.monitor_type_uid, self.schedule_expression, self.monitor_protocol, self.monitor_url, self.monitor_user, self.monitor_priority, self.is_on_hold, self.last_status_name, self.last_run_time, self.last_exception_message, self.custom_attributes)
    def get_model(self) -> base_model:
        return db_models.monitor_model
    def get_uid(self) -> str:
        return self.monitor_uid
    def get_name(self) -> str:
        return self.monitor_name
    def get_list_values(self) -> list[any]:
        return [self.monitor_uid, self.monitor_name, self.tenant_uid, self.account_uid, self.monitor_type_uid, self.schedule_expression, self.monitor_protocol, self.monitor_url, self.monitor_user, self.monitor_priority, self.is_on_hold, self.last_status_name, self.last_run_time, self.last_exception_message, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.monitor_uid, self.monitor_name, self.tenant_uid, self.account_uid, self.monitor_type_uid, self.schedule_expression, self.monitor_protocol, self.monitor_url, self.monitor_user, self.monitor_priority, self.is_on_hold, self.last_status_name, self.last_run_time, self.last_exception_message]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.monitor_name, self.tenant_uid, self.account_uid, self.monitor_type_uid, self.schedule_expression, self.monitor_protocol, self.monitor_url, self.monitor_user, self.monitor_priority, self.is_on_hold, self.last_status_name, self.last_run_time, self.last_exception_message, self.custom_attributes, updated_by, self.monitor_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.monitor_uid, self.monitor_name, self.tenant_uid, self.account_uid, self.monitor_type_uid, self.schedule_expression, self.monitor_protocol, self.monitor_url, self.monitor_user, self.monitor_priority, self.is_on_hold, self.last_status_name, self.last_run_time, self.last_exception_message, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.monitor_name, self.tenant_uid, self.account_uid, self.monitor_type_uid, self.schedule_expression, self.monitor_protocol, self.monitor_url, self.monitor_user, self.monitor_priority, self.is_on_hold, self.last_status_name, self.last_run_time, self.last_exception_message]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.monitor_name, self.tenant_uid, self.account_uid, self.monitor_type_uid, self.schedule_expression, self.monitor_protocol, self.monitor_url, self.monitor_user, self.monitor_priority, self.is_on_hold, self.last_status_name, self.last_run_time, self.last_exception_message, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_uid() == obj.get_uid()
    def update_uid(self, uid: str):
        self.monitor_uid = uid
    def update_uid_attributes(self, monitor_uid: str, monitor_name: str, tenant_uid: str, account_uid: str, monitor_type_uid: str, schedule_expression: str, monitor_protocol: str, monitor_url: str, monitor_user: str, monitor_priority: int, is_on_hold: int, last_status_name: str, last_run_time: str, last_exception_message: str):
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
    def update_attributes(self, monitor_name: str, tenant_uid: str, account_uid: str, monitor_type_uid: str, schedule_expression: str, monitor_protocol: str, monitor_url: str, monitor_user: str, monitor_priority: int, is_on_hold: int, last_status_name: str, last_run_time: str, last_exception_message: str):
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


@dataclass(frozen=False)
class monitor_run_write_dto(base_write_dto):
    monitor_run_uid: str
    monitor_run_name: str
    tenant_uid: str
    account_uid: str
    monitor_uid: str
    status_name: str
    run_time: str
    exception_message: str
    def __init__(self, monitor_run_uid: str, monitor_run_name: str, tenant_uid: str, account_uid: str, monitor_uid: str, status_name: str, run_time: str, exception_message: str, custom_attributes: str = "{}"):
        self.monitor_run_uid = monitor_run_uid
        self.monitor_run_name = monitor_run_name
        self.tenant_uid = tenant_uid
        self.account_uid = account_uid
        self.monitor_uid = monitor_uid
        self.status_name = status_name
        self.run_time = run_time
        self.exception_message = exception_message
        self.custom_attributes = custom_attributes
    @classmethod
    def empty_write(cls):
        return cls("", "", "", "", "", "", "", "")
    @classmethod
    def default_write(cls):
        return cls(base_dto.get_random_uid(), "", "", "", "", "", "", "")
    @classmethod
    def random_write(cls):
        return cls(base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), "", base_dto.get_random_uid())
    @classmethod
    def new_write(cls, monitor_run_uid: str, monitor_run_name: str, tenant_uid: str, account_uid: str, monitor_uid: str, status_name: str, run_time: str, exception_message: str):
        return cls(monitor_run_uid, monitor_run_name, tenant_uid, account_uid, monitor_uid, status_name, run_time, exception_message)
    @classmethod
    def new_write_with_defaults(cls, monitor_run_uid: str = "", monitor_run_name: str = "", tenant_uid: str = "", account_uid: str = "", monitor_uid: str = "", status_name: str = "", run_time: str = "", exception_message: str = ""):
        return cls(monitor_run_uid, monitor_run_name, tenant_uid, account_uid, monitor_uid, status_name, run_time, exception_message)
    @classmethod
    def new_write_random_uid(cls, monitor_run_name: str, tenant_uid: str, account_uid: str, monitor_uid: str, status_name: str, run_time: str, exception_message: str):
        return cls(base_dto.get_random_uid(), monitor_run_name, tenant_uid, account_uid, monitor_uid, status_name, run_time, exception_message)
    @classmethod
    def get_class_model(cls) -> base_model:
        return db_models.monitor_run_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["monitor_run_uid"], d["monitor_run_name"], d["tenant_uid"], d["account_uid"], d["monitor_uid"], d["status_name"], d["run_time"], d["exception_message"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return monitor_run_write_dto(self.monitor_run_uid, self.monitor_run_name, self.tenant_uid, self.account_uid, self.monitor_uid, self.status_name, self.run_time, self.exception_message, self.custom_attributes)
    def clone_write_new_uid(self):
        return monitor_run_write_dto(base_dto.get_random_uid(), self.monitor_run_name, self.tenant_uid, self.account_uid, self.monitor_uid, self.status_name, self.run_time, self.exception_message, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return monitor_run_write_dto(uid, self.monitor_run_name, self.tenant_uid, self.account_uid, self.monitor_uid, self.status_name, self.run_time, self.exception_message, self.custom_attributes)
    def get_model(self) -> base_model:
        return db_models.monitor_run_model
    def get_uid(self) -> str:
        return self.monitor_run_uid
    def get_name(self) -> str:
        return self.monitor_run_name
    def get_list_values(self) -> list[any]:
        return [self.monitor_run_uid, self.monitor_run_name, self.tenant_uid, self.account_uid, self.monitor_uid, self.status_name, self.run_time, self.exception_message, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.monitor_run_uid, self.monitor_run_name, self.tenant_uid, self.account_uid, self.monitor_uid, self.status_name, self.run_time, self.exception_message]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.monitor_run_name, self.tenant_uid, self.account_uid, self.monitor_uid, self.status_name, self.run_time, self.exception_message, self.custom_attributes, updated_by, self.monitor_run_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.monitor_run_uid, self.monitor_run_name, self.tenant_uid, self.account_uid, self.monitor_uid, self.status_name, self.run_time, self.exception_message, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.monitor_run_name, self.tenant_uid, self.account_uid, self.monitor_uid, self.status_name, self.run_time, self.exception_message]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.monitor_run_name, self.tenant_uid, self.account_uid, self.monitor_uid, self.status_name, self.run_time, self.exception_message, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_uid() == obj.get_uid()
    def update_uid(self, uid: str):
        self.monitor_run_uid = uid
    def update_uid_attributes(self, monitor_run_uid: str, monitor_run_name: str, tenant_uid: str, account_uid: str, monitor_uid: str, status_name: str, run_time: str, exception_message: str):
        self.monitor_run_uid = monitor_run_uid
        self.monitor_run_name = monitor_run_name
        self.tenant_uid = tenant_uid
        self.account_uid = account_uid
        self.monitor_uid = monitor_uid
        self.status_name = status_name
        self.run_time = run_time
        self.exception_message = exception_message
    def update_attributes(self, monitor_run_name: str, tenant_uid: str, account_uid: str, monitor_uid: str, status_name: str, run_time: str, exception_message: str):
        self.monitor_run_name = monitor_run_name
        self.tenant_uid = tenant_uid
        self.account_uid = account_uid
        self.monitor_uid = monitor_uid
        self.status_name = status_name
        self.run_time = run_time
        self.exception_message = exception_message


@dataclass(frozen=False)
class monitor_type_write_dto(base_write_dto):
    monitor_type_uid: str
    monitor_type_name: str
    class_name: str
    parameters_json: str
    def __init__(self, monitor_type_uid: str, monitor_type_name: str, class_name: str, parameters_json: str, custom_attributes: str = "{}"):
        self.monitor_type_uid = monitor_type_uid
        self.monitor_type_name = monitor_type_name
        self.class_name = class_name
        self.parameters_json = parameters_json
        self.custom_attributes = custom_attributes
    @classmethod
    def empty_write(cls):
        return cls("", "", "", "")
    @classmethod
    def default_write(cls):
        return cls(base_dto.get_random_uid(), "", "", "")
    @classmethod
    def random_write(cls):
        return cls(base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid())
    @classmethod
    def new_write(cls, monitor_type_uid: str, monitor_type_name: str, class_name: str, parameters_json: str):
        return cls(monitor_type_uid, monitor_type_name, class_name, parameters_json)
    @classmethod
    def new_write_with_defaults(cls, monitor_type_uid: str = "", monitor_type_name: str = "", class_name: str = "", parameters_json: str = ""):
        return cls(monitor_type_uid, monitor_type_name, class_name, parameters_json)
    @classmethod
    def new_write_random_uid(cls, monitor_type_name: str, class_name: str, parameters_json: str):
        return cls(base_dto.get_random_uid(), monitor_type_name, class_name, parameters_json)
    @classmethod
    def get_class_model(cls) -> base_model:
        return db_models.monitor_type_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["monitor_type_uid"], d["monitor_type_name"], d["class_name"], d["parameters_json"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return monitor_type_write_dto(self.monitor_type_uid, self.monitor_type_name, self.class_name, self.parameters_json, self.custom_attributes)
    def clone_write_new_uid(self):
        return monitor_type_write_dto(base_dto.get_random_uid(), self.monitor_type_name, self.class_name, self.parameters_json, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return monitor_type_write_dto(uid, self.monitor_type_name, self.class_name, self.parameters_json, self.custom_attributes)
    def get_model(self) -> base_model:
        return db_models.monitor_type_model
    def get_uid(self) -> str:
        return self.monitor_type_uid
    def get_name(self) -> str:
        return self.monitor_type_name
    def get_list_values(self) -> list[any]:
        return [self.monitor_type_uid, self.monitor_type_name, self.class_name, self.parameters_json, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.monitor_type_uid, self.monitor_type_name, self.class_name, self.parameters_json]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.monitor_type_name, self.class_name, self.parameters_json, self.custom_attributes, updated_by, self.monitor_type_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.monitor_type_uid, self.monitor_type_name, self.class_name, self.parameters_json, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.monitor_type_name, self.class_name, self.parameters_json]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.monitor_type_name, self.class_name, self.parameters_json, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_uid() == obj.get_uid()
    def update_uid(self, uid: str):
        self.monitor_type_uid = uid
    def update_uid_attributes(self, monitor_type_uid: str, monitor_type_name: str, class_name: str, parameters_json: str):
        self.monitor_type_uid = monitor_type_uid
        self.monitor_type_name = monitor_type_name
        self.class_name = class_name
        self.parameters_json = parameters_json
    def update_attributes(self, monitor_type_name: str, class_name: str, parameters_json: str):
        self.monitor_type_name = monitor_type_name
        self.class_name = class_name
        self.parameters_json = parameters_json


@dataclass(frozen=False)
class period_write_dto(base_write_dto):
    period_uid: str
    period_name: str
    period_full_name: str
    period_number: int
    period_type: str
    period_start_time: datetime.datetime
    period_end_time: datetime.datetime
    period_year: int | None
    period_semester: int | None
    period_trimester: int | None
    period_quarter: int | None
    period_month: int | None
    period_week: int | None
    period_day: int | None
    period_day_of_year: int | None
    parent_year_period_uid: str | None
    parent_quarter_period_uid: str | None
    parent_month_period_uid: str | None
    parent_week_period_uid: str | None
    def __init__(self, period_uid: str, period_name: str, period_full_name: str, period_number: int, period_type: str, period_start_time: datetime.datetime, period_end_time: datetime.datetime, period_year: int | None, period_semester: int | None, period_trimester: int | None, period_quarter: int | None, period_month: int | None, period_week: int | None, period_day: int | None, period_day_of_year: int | None, parent_year_period_uid: str | None, parent_quarter_period_uid: str | None, parent_month_period_uid: str | None, parent_week_period_uid: str | None, custom_attributes: str = "{}"):
        self.period_uid = period_uid
        self.period_name = period_name
        self.period_full_name = period_full_name
        self.period_number = period_number
        self.period_type = period_type
        self.period_start_time = period_start_time
        self.period_end_time = period_end_time
        self.period_year = period_year
        self.period_semester = period_semester
        self.period_trimester = period_trimester
        self.period_quarter = period_quarter
        self.period_month = period_month
        self.period_week = period_week
        self.period_day = period_day
        self.period_day_of_year = period_day_of_year
        self.parent_year_period_uid = parent_year_period_uid
        self.parent_quarter_period_uid = parent_quarter_period_uid
        self.parent_month_period_uid = parent_month_period_uid
        self.parent_week_period_uid = parent_week_period_uid
        self.custom_attributes = custom_attributes
    @classmethod
    def empty_write(cls):
        return cls("", "", "", 0, "", datetime.datetime.now(), datetime.datetime.now(), 0, 0, 0, 0, 0, 0, 0, 0, "", "", "", "")
    @classmethod
    def default_write(cls):
        return cls(base_dto.get_random_uid(), "", "", 0, "", datetime.datetime.now(), datetime.datetime.now(), 0, 0, 0, 0, 0, 0, 0, 0, "", "", "", "")
    @classmethod
    def random_write(cls):
        return cls(base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), 0, base_dto.get_random_uid(), datetime.datetime.now(), datetime.datetime.now(), 0, 0, 0, 0, 0, 0, 0, 0, base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid())
    @classmethod
    def new_write(cls, period_uid: str, period_name: str, period_full_name: str, period_number: int, period_type: str, period_start_time: datetime.datetime, period_end_time: datetime.datetime, period_year: int | None, period_semester: int | None, period_trimester: int | None, period_quarter: int | None, period_month: int | None, period_week: int | None, period_day: int | None, period_day_of_year: int | None, parent_year_period_uid: str | None, parent_quarter_period_uid: str | None, parent_month_period_uid: str | None, parent_week_period_uid: str | None):
        return cls(period_uid, period_name, period_full_name, period_number, period_type, period_start_time, period_end_time, period_year, period_semester, period_trimester, period_quarter, period_month, period_week, period_day, period_day_of_year, parent_year_period_uid, parent_quarter_period_uid, parent_month_period_uid, parent_week_period_uid)
    @classmethod
    def new_write_with_defaults(cls, period_uid: str = "", period_name: str = "", period_full_name: str = "", period_number: int = 0, period_type: str = "", period_start_time: datetime.datetime = datetime.datetime.now(), period_end_time: datetime.datetime = datetime.datetime.now(), period_year: int | None = 0, period_semester: int | None = 0, period_trimester: int | None = 0, period_quarter: int | None = 0, period_month: int | None = 0, period_week: int | None = 0, period_day: int | None = 0, period_day_of_year: int | None = 0, parent_year_period_uid: str | None = "", parent_quarter_period_uid: str | None = "", parent_month_period_uid: str | None = "", parent_week_period_uid: str | None = ""):
        return cls(period_uid, period_name, period_full_name, period_number, period_type, period_start_time, period_end_time, period_year, period_semester, period_trimester, period_quarter, period_month, period_week, period_day, period_day_of_year, parent_year_period_uid, parent_quarter_period_uid, parent_month_period_uid, parent_week_period_uid)
    @classmethod
    def new_write_random_uid(cls, period_name: str, period_full_name: str, period_number: int, period_type: str, period_start_time: datetime.datetime, period_end_time: datetime.datetime, period_year: int | None, period_semester: int | None, period_trimester: int | None, period_quarter: int | None, period_month: int | None, period_week: int | None, period_day: int | None, period_day_of_year: int | None, parent_year_period_uid: str | None, parent_quarter_period_uid: str | None, parent_month_period_uid: str | None, parent_week_period_uid: str | None):
        return cls(base_dto.get_random_uid(), period_name, period_full_name, period_number, period_type, period_start_time, period_end_time, period_year, period_semester, period_trimester, period_quarter, period_month, period_week, period_day, period_day_of_year, parent_year_period_uid, parent_quarter_period_uid, parent_month_period_uid, parent_week_period_uid)
    @classmethod
    def get_class_model(cls) -> base_model:
        return db_models.period_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["period_uid"], d["period_name"], d["period_full_name"], d["period_number"], d["period_type"], d["period_start_time"], d["period_end_time"], d["period_year"], d["period_semester"], d["period_trimester"], d["period_quarter"], d["period_month"], d["period_week"], d["period_day"], d["period_day_of_year"], d["parent_year_period_uid"], d["parent_quarter_period_uid"], d["parent_month_period_uid"], d["parent_week_period_uid"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return period_write_dto(self.period_uid, self.period_name, self.period_full_name, self.period_number, self.period_type, self.period_start_time, self.period_end_time, self.period_year, self.period_semester, self.period_trimester, self.period_quarter, self.period_month, self.period_week, self.period_day, self.period_day_of_year, self.parent_year_period_uid, self.parent_quarter_period_uid, self.parent_month_period_uid, self.parent_week_period_uid, self.custom_attributes)
    def clone_write_new_uid(self):
        return period_write_dto(base_dto.get_random_uid(), self.period_name, self.period_full_name, self.period_number, self.period_type, self.period_start_time, self.period_end_time, self.period_year, self.period_semester, self.period_trimester, self.period_quarter, self.period_month, self.period_week, self.period_day, self.period_day_of_year, self.parent_year_period_uid, self.parent_quarter_period_uid, self.parent_month_period_uid, self.parent_week_period_uid, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return period_write_dto(uid, self.period_name, self.period_full_name, self.period_number, self.period_type, self.period_start_time, self.period_end_time, self.period_year, self.period_semester, self.period_trimester, self.period_quarter, self.period_month, self.period_week, self.period_day, self.period_day_of_year, self.parent_year_period_uid, self.parent_quarter_period_uid, self.parent_month_period_uid, self.parent_week_period_uid, self.custom_attributes)
    def get_model(self) -> base_model:
        return db_models.period_model
    def get_uid(self) -> str:
        return self.period_uid
    def get_name(self) -> str:
        return self.period_name
    def get_list_values(self) -> list[any]:
        return [self.period_uid, self.period_name, self.period_full_name, self.period_number, self.period_type, self.period_start_time, self.period_end_time, self.period_year, self.period_semester, self.period_trimester, self.period_quarter, self.period_month, self.period_week, self.period_day, self.period_day_of_year, self.parent_year_period_uid, self.parent_quarter_period_uid, self.parent_month_period_uid, self.parent_week_period_uid, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.period_uid, self.period_name, self.period_full_name, self.period_number, self.period_type, self.period_start_time, self.period_end_time, self.period_year, self.period_semester, self.period_trimester, self.period_quarter, self.period_month, self.period_week, self.period_day, self.period_day_of_year, self.parent_year_period_uid, self.parent_quarter_period_uid, self.parent_month_period_uid, self.parent_week_period_uid]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.period_name, self.period_full_name, self.period_number, self.period_type, self.period_start_time, self.period_end_time, self.period_year, self.period_semester, self.period_trimester, self.period_quarter, self.period_month, self.period_week, self.period_day, self.period_day_of_year, self.parent_year_period_uid, self.parent_quarter_period_uid, self.parent_month_period_uid, self.parent_week_period_uid, self.custom_attributes, updated_by, self.period_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.period_uid, self.period_name, self.period_full_name, self.period_number, self.period_type, self.period_start_time, self.period_end_time, self.period_year, self.period_semester, self.period_trimester, self.period_quarter, self.period_month, self.period_week, self.period_day, self.period_day_of_year, self.parent_year_period_uid, self.parent_quarter_period_uid, self.parent_month_period_uid, self.parent_week_period_uid, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.period_name, self.period_full_name, self.period_number, self.period_type, self.period_start_time, self.period_end_time, self.period_year, self.period_semester, self.period_trimester, self.period_quarter, self.period_month, self.period_week, self.period_day, self.period_day_of_year, self.parent_year_period_uid, self.parent_quarter_period_uid, self.parent_month_period_uid, self.parent_week_period_uid]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.period_name, self.period_full_name, self.period_number, self.period_type, self.period_start_time, self.period_end_time, self.period_year, self.period_semester, self.period_trimester, self.period_quarter, self.period_month, self.period_week, self.period_day, self.period_day_of_year, self.parent_year_period_uid, self.parent_quarter_period_uid, self.parent_month_period_uid, self.parent_week_period_uid, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_uid() == obj.get_uid()
    def update_uid(self, uid: str):
        self.period_uid = uid
    def update_uid_attributes(self, period_uid: str, period_name: str, period_full_name: str, period_number: int, period_type: str, period_start_time: datetime.datetime, period_end_time: datetime.datetime, period_year: int | None, period_semester: int | None, period_trimester: int | None, period_quarter: int | None, period_month: int | None, period_week: int | None, period_day: int | None, period_day_of_year: int | None, parent_year_period_uid: str | None, parent_quarter_period_uid: str | None, parent_month_period_uid: str | None, parent_week_period_uid: str | None):
        self.period_uid = period_uid
        self.period_name = period_name
        self.period_full_name = period_full_name
        self.period_number = period_number
        self.period_type = period_type
        self.period_start_time = period_start_time
        self.period_end_time = period_end_time
        self.period_year = period_year
        self.period_semester = period_semester
        self.period_trimester = period_trimester
        self.period_quarter = period_quarter
        self.period_month = period_month
        self.period_week = period_week
        self.period_day = period_day
        self.period_day_of_year = period_day_of_year
        self.parent_year_period_uid = parent_year_period_uid
        self.parent_quarter_period_uid = parent_quarter_period_uid
        self.parent_month_period_uid = parent_month_period_uid
        self.parent_week_period_uid = parent_week_period_uid
    def update_attributes(self, period_name: str, period_full_name: str, period_number: int, period_type: str, period_start_time: datetime.datetime, period_end_time: datetime.datetime, period_year: int | None, period_semester: int | None, period_trimester: int | None, period_quarter: int | None, period_month: int | None, period_week: int | None, period_day: int | None, period_day_of_year: int | None, parent_year_period_uid: str | None, parent_quarter_period_uid: str | None, parent_month_period_uid: str | None, parent_week_period_uid: str | None):
        self.period_name = period_name
        self.period_full_name = period_full_name
        self.period_number = period_number
        self.period_type = period_type
        self.period_start_time = period_start_time
        self.period_end_time = period_end_time
        self.period_year = period_year
        self.period_semester = period_semester
        self.period_trimester = period_trimester
        self.period_quarter = period_quarter
        self.period_month = period_month
        self.period_week = period_week
        self.period_day = period_day
        self.period_day_of_year = period_day_of_year
        self.parent_year_period_uid = parent_year_period_uid
        self.parent_quarter_period_uid = parent_quarter_period_uid
        self.parent_month_period_uid = parent_month_period_uid
        self.parent_week_period_uid = parent_week_period_uid


@dataclass(frozen=False)
class process_write_dto(base_write_dto):
    process_uid: str
    process_name: str
    tenant_uid: str
    account_uid: str
    process_type_uid: str
    status_name: str
    def __init__(self, process_uid: str, process_name: str, tenant_uid: str, account_uid: str, process_type_uid: str, status_name: str, custom_attributes: str = "{}"):
        self.process_uid = process_uid
        self.process_name = process_name
        self.tenant_uid = tenant_uid
        self.account_uid = account_uid
        self.process_type_uid = process_type_uid
        self.status_name = status_name
        self.custom_attributes = custom_attributes
    @classmethod
    def empty_write(cls):
        return cls("", "", "", "", "", "")
    @classmethod
    def default_write(cls):
        return cls(base_dto.get_random_uid(), "", "", "", "", "")
    @classmethod
    def random_write(cls):
        return cls(base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid())
    @classmethod
    def new_write(cls, process_uid: str, process_name: str, tenant_uid: str, account_uid: str, process_type_uid: str, status_name: str):
        return cls(process_uid, process_name, tenant_uid, account_uid, process_type_uid, status_name)
    @classmethod
    def new_write_with_defaults(cls, process_uid: str = "", process_name: str = "", tenant_uid: str = "", account_uid: str = "", process_type_uid: str = "", status_name: str = ""):
        return cls(process_uid, process_name, tenant_uid, account_uid, process_type_uid, status_name)
    @classmethod
    def new_write_random_uid(cls, process_name: str, tenant_uid: str, account_uid: str, process_type_uid: str, status_name: str):
        return cls(base_dto.get_random_uid(), process_name, tenant_uid, account_uid, process_type_uid, status_name)
    @classmethod
    def get_class_model(cls) -> base_model:
        return db_models.process_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["process_uid"], d["process_name"], d["tenant_uid"], d["account_uid"], d["process_type_uid"], d["status_name"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return process_write_dto(self.process_uid, self.process_name, self.tenant_uid, self.account_uid, self.process_type_uid, self.status_name, self.custom_attributes)
    def clone_write_new_uid(self):
        return process_write_dto(base_dto.get_random_uid(), self.process_name, self.tenant_uid, self.account_uid, self.process_type_uid, self.status_name, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return process_write_dto(uid, self.process_name, self.tenant_uid, self.account_uid, self.process_type_uid, self.status_name, self.custom_attributes)
    def get_model(self) -> base_model:
        return db_models.process_model
    def get_uid(self) -> str:
        return self.process_uid
    def get_name(self) -> str:
        return self.process_name
    def get_list_values(self) -> list[any]:
        return [self.process_uid, self.process_name, self.tenant_uid, self.account_uid, self.process_type_uid, self.status_name, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.process_uid, self.process_name, self.tenant_uid, self.account_uid, self.process_type_uid, self.status_name]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.process_name, self.tenant_uid, self.account_uid, self.process_type_uid, self.status_name, self.custom_attributes, updated_by, self.process_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.process_uid, self.process_name, self.tenant_uid, self.account_uid, self.process_type_uid, self.status_name, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.process_name, self.tenant_uid, self.account_uid, self.process_type_uid, self.status_name]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.process_name, self.tenant_uid, self.account_uid, self.process_type_uid, self.status_name, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_uid() == obj.get_uid()
    def update_uid(self, uid: str):
        self.process_uid = uid
    def update_uid_attributes(self, process_uid: str, process_name: str, tenant_uid: str, account_uid: str, process_type_uid: str, status_name: str):
        self.process_uid = process_uid
        self.process_name = process_name
        self.tenant_uid = tenant_uid
        self.account_uid = account_uid
        self.process_type_uid = process_type_uid
        self.status_name = status_name
    def update_attributes(self, process_name: str, tenant_uid: str, account_uid: str, process_type_uid: str, status_name: str):
        self.process_name = process_name
        self.tenant_uid = tenant_uid
        self.account_uid = account_uid
        self.process_type_uid = process_type_uid
        self.status_name = status_name


@dataclass(frozen=False)
class process_result_write_dto(base_write_dto):
    process_result_uid: str
    process_result_name: str
    tenant_uid: str
    account_uid: str
    process_uid: str
    process_run_uid: str
    result_type: str
    result_text: str
    def __init__(self, process_result_uid: str, process_result_name: str, tenant_uid: str, account_uid: str, process_uid: str, process_run_uid: str, result_type: str, result_text: str, custom_attributes: str = "{}"):
        self.process_result_uid = process_result_uid
        self.process_result_name = process_result_name
        self.tenant_uid = tenant_uid
        self.account_uid = account_uid
        self.process_uid = process_uid
        self.process_run_uid = process_run_uid
        self.result_type = result_type
        self.result_text = result_text
        self.custom_attributes = custom_attributes
    @classmethod
    def empty_write(cls):
        return cls("", "", "", "", "", "", "", "")
    @classmethod
    def default_write(cls):
        return cls(base_dto.get_random_uid(), "", "", "", "", "", "", "")
    @classmethod
    def random_write(cls):
        return cls(base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid())
    @classmethod
    def new_write(cls, process_result_uid: str, process_result_name: str, tenant_uid: str, account_uid: str, process_uid: str, process_run_uid: str, result_type: str, result_text: str):
        return cls(process_result_uid, process_result_name, tenant_uid, account_uid, process_uid, process_run_uid, result_type, result_text)
    @classmethod
    def new_write_with_defaults(cls, process_result_uid: str = "", process_result_name: str = "", tenant_uid: str = "", account_uid: str = "", process_uid: str = "", process_run_uid: str = "", result_type: str = "", result_text: str = ""):
        return cls(process_result_uid, process_result_name, tenant_uid, account_uid, process_uid, process_run_uid, result_type, result_text)
    @classmethod
    def new_write_random_uid(cls, process_result_name: str, tenant_uid: str, account_uid: str, process_uid: str, process_run_uid: str, result_type: str, result_text: str):
        return cls(base_dto.get_random_uid(), process_result_name, tenant_uid, account_uid, process_uid, process_run_uid, result_type, result_text)
    @classmethod
    def get_class_model(cls) -> base_model:
        return db_models.process_result_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["process_result_uid"], d["process_result_name"], d["tenant_uid"], d["account_uid"], d["process_uid"], d["process_run_uid"], d["result_type"], d["result_text"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return process_result_write_dto(self.process_result_uid, self.process_result_name, self.tenant_uid, self.account_uid, self.process_uid, self.process_run_uid, self.result_type, self.result_text, self.custom_attributes)
    def clone_write_new_uid(self):
        return process_result_write_dto(base_dto.get_random_uid(), self.process_result_name, self.tenant_uid, self.account_uid, self.process_uid, self.process_run_uid, self.result_type, self.result_text, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return process_result_write_dto(uid, self.process_result_name, self.tenant_uid, self.account_uid, self.process_uid, self.process_run_uid, self.result_type, self.result_text, self.custom_attributes)
    def get_model(self) -> base_model:
        return db_models.process_result_model
    def get_uid(self) -> str:
        return self.process_result_uid
    def get_name(self) -> str:
        return self.process_result_name
    def get_list_values(self) -> list[any]:
        return [self.process_result_uid, self.process_result_name, self.tenant_uid, self.account_uid, self.process_uid, self.process_run_uid, self.result_type, self.result_text, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.process_result_uid, self.process_result_name, self.tenant_uid, self.account_uid, self.process_uid, self.process_run_uid, self.result_type, self.result_text]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.process_result_name, self.tenant_uid, self.account_uid, self.process_uid, self.process_run_uid, self.result_type, self.result_text, self.custom_attributes, updated_by, self.process_result_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.process_result_uid, self.process_result_name, self.tenant_uid, self.account_uid, self.process_uid, self.process_run_uid, self.result_type, self.result_text, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.process_result_name, self.tenant_uid, self.account_uid, self.process_uid, self.process_run_uid, self.result_type, self.result_text]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.process_result_name, self.tenant_uid, self.account_uid, self.process_uid, self.process_run_uid, self.result_type, self.result_text, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_uid() == obj.get_uid()
    def update_uid(self, uid: str):
        self.process_result_uid = uid
    def update_uid_attributes(self, process_result_uid: str, process_result_name: str, tenant_uid: str, account_uid: str, process_uid: str, process_run_uid: str, result_type: str, result_text: str):
        self.process_result_uid = process_result_uid
        self.process_result_name = process_result_name
        self.tenant_uid = tenant_uid
        self.account_uid = account_uid
        self.process_uid = process_uid
        self.process_run_uid = process_run_uid
        self.result_type = result_type
        self.result_text = result_text
    def update_attributes(self, process_result_name: str, tenant_uid: str, account_uid: str, process_uid: str, process_run_uid: str, result_type: str, result_text: str):
        self.process_result_name = process_result_name
        self.tenant_uid = tenant_uid
        self.account_uid = account_uid
        self.process_uid = process_uid
        self.process_run_uid = process_run_uid
        self.result_type = result_type
        self.result_text = result_text


@dataclass(frozen=False)
class process_run_write_dto(base_write_dto):
    process_run_uid: str
    process_run_name: str
    tenant_uid: str
    account_uid: str
    process_uid: str
    status_name: str
    run_time: int
    def __init__(self, process_run_uid: str, process_run_name: str, tenant_uid: str, account_uid: str, process_uid: str, status_name: str, run_time: int, custom_attributes: str = "{}"):
        self.process_run_uid = process_run_uid
        self.process_run_name = process_run_name
        self.tenant_uid = tenant_uid
        self.account_uid = account_uid
        self.process_uid = process_uid
        self.status_name = status_name
        self.run_time = run_time
        self.custom_attributes = custom_attributes
    @classmethod
    def empty_write(cls):
        return cls("", "", "", "", "", "", 0)
    @classmethod
    def default_write(cls):
        return cls(base_dto.get_random_uid(), "", "", "", "", "", 0)
    @classmethod
    def random_write(cls):
        return cls(base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), 0)
    @classmethod
    def new_write(cls, process_run_uid: str, process_run_name: str, tenant_uid: str, account_uid: str, process_uid: str, status_name: str, run_time: int):
        return cls(process_run_uid, process_run_name, tenant_uid, account_uid, process_uid, status_name, run_time)
    @classmethod
    def new_write_with_defaults(cls, process_run_uid: str = "", process_run_name: str = "", tenant_uid: str = "", account_uid: str = "", process_uid: str = "", status_name: str = "", run_time: int = 0):
        return cls(process_run_uid, process_run_name, tenant_uid, account_uid, process_uid, status_name, run_time)
    @classmethod
    def new_write_random_uid(cls, process_run_name: str, tenant_uid: str, account_uid: str, process_uid: str, status_name: str, run_time: int):
        return cls(base_dto.get_random_uid(), process_run_name, tenant_uid, account_uid, process_uid, status_name, run_time)
    @classmethod
    def get_class_model(cls) -> base_model:
        return db_models.process_run_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["process_run_uid"], d["process_run_name"], d["tenant_uid"], d["account_uid"], d["process_uid"], d["status_name"], d["run_time"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return process_run_write_dto(self.process_run_uid, self.process_run_name, self.tenant_uid, self.account_uid, self.process_uid, self.status_name, self.run_time, self.custom_attributes)
    def clone_write_new_uid(self):
        return process_run_write_dto(base_dto.get_random_uid(), self.process_run_name, self.tenant_uid, self.account_uid, self.process_uid, self.status_name, self.run_time, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return process_run_write_dto(uid, self.process_run_name, self.tenant_uid, self.account_uid, self.process_uid, self.status_name, self.run_time, self.custom_attributes)
    def get_model(self) -> base_model:
        return db_models.process_run_model
    def get_uid(self) -> str:
        return self.process_run_uid
    def get_name(self) -> str:
        return self.process_run_name
    def get_list_values(self) -> list[any]:
        return [self.process_run_uid, self.process_run_name, self.tenant_uid, self.account_uid, self.process_uid, self.status_name, self.run_time, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.process_run_uid, self.process_run_name, self.tenant_uid, self.account_uid, self.process_uid, self.status_name, self.run_time]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.process_run_name, self.tenant_uid, self.account_uid, self.process_uid, self.status_name, self.run_time, self.custom_attributes, updated_by, self.process_run_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.process_run_uid, self.process_run_name, self.tenant_uid, self.account_uid, self.process_uid, self.status_name, self.run_time, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.process_run_name, self.tenant_uid, self.account_uid, self.process_uid, self.status_name, self.run_time]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.process_run_name, self.tenant_uid, self.account_uid, self.process_uid, self.status_name, self.run_time, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_uid() == obj.get_uid()
    def update_uid(self, uid: str):
        self.process_run_uid = uid
    def update_uid_attributes(self, process_run_uid: str, process_run_name: str, tenant_uid: str, account_uid: str, process_uid: str, status_name: str, run_time: int):
        self.process_run_uid = process_run_uid
        self.process_run_name = process_run_name
        self.tenant_uid = tenant_uid
        self.account_uid = account_uid
        self.process_uid = process_uid
        self.status_name = status_name
        self.run_time = run_time
    def update_attributes(self, process_run_name: str, tenant_uid: str, account_uid: str, process_uid: str, status_name: str, run_time: int):
        self.process_run_name = process_run_name
        self.tenant_uid = tenant_uid
        self.account_uid = account_uid
        self.process_uid = process_uid
        self.status_name = status_name
        self.run_time = run_time


@dataclass(frozen=False)
class process_type_write_dto(base_write_dto):
    process_type_uid: str
    process_type_name: str
    class_name: str
    def __init__(self, process_type_uid: str, process_type_name: str, class_name: str, custom_attributes: str = "{}"):
        self.process_type_uid = process_type_uid
        self.process_type_name = process_type_name
        self.class_name = class_name
        self.custom_attributes = custom_attributes
    @classmethod
    def empty_write(cls):
        return cls("", "", "")
    @classmethod
    def default_write(cls):
        return cls(base_dto.get_random_uid(), "", "")
    @classmethod
    def random_write(cls):
        return cls(base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid())
    @classmethod
    def new_write(cls, process_type_uid: str, process_type_name: str, class_name: str):
        return cls(process_type_uid, process_type_name, class_name)
    @classmethod
    def new_write_with_defaults(cls, process_type_uid: str = "", process_type_name: str = "", class_name: str = ""):
        return cls(process_type_uid, process_type_name, class_name)
    @classmethod
    def new_write_random_uid(cls, process_type_name: str, class_name: str):
        return cls(base_dto.get_random_uid(), process_type_name, class_name)
    @classmethod
    def get_class_model(cls) -> base_model:
        return db_models.process_type_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["process_type_uid"], d["process_type_name"], d["class_name"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return process_type_write_dto(self.process_type_uid, self.process_type_name, self.class_name, self.custom_attributes)
    def clone_write_new_uid(self):
        return process_type_write_dto(base_dto.get_random_uid(), self.process_type_name, self.class_name, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return process_type_write_dto(uid, self.process_type_name, self.class_name, self.custom_attributes)
    def get_model(self) -> base_model:
        return db_models.process_type_model
    def get_uid(self) -> str:
        return self.process_type_uid
    def get_name(self) -> str:
        return self.process_type_name
    def get_list_values(self) -> list[any]:
        return [self.process_type_uid, self.process_type_name, self.class_name, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.process_type_uid, self.process_type_name, self.class_name]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.process_type_name, self.class_name, self.custom_attributes, updated_by, self.process_type_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.process_type_uid, self.process_type_name, self.class_name, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.process_type_name, self.class_name]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.process_type_name, self.class_name, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_uid() == obj.get_uid()
    def update_uid(self, uid: str):
        self.process_type_uid = uid
    def update_uid_attributes(self, process_type_uid: str, process_type_name: str, class_name: str):
        self.process_type_uid = process_type_uid
        self.process_type_name = process_type_name
        self.class_name = class_name
    def update_attributes(self, process_type_name: str, class_name: str):
        self.process_type_name = process_type_name
        self.class_name = class_name


@dataclass(frozen=False)
class project_account_write_dto(base_write_dto):
    project_account_uid: str
    project_account_name: str
    tenant_uid: str
    client_uid: str
    account_uid: str
    project_instance_uid: str
    start_date: datetime.datetime | None
    end_date: datetime.datetime | None
    def __init__(self, project_account_uid: str, project_account_name: str, tenant_uid: str, client_uid: str, account_uid: str, project_instance_uid: str, start_date: datetime.datetime | None, end_date: datetime.datetime | None, custom_attributes: str = "{}"):
        self.project_account_uid = project_account_uid
        self.project_account_name = project_account_name
        self.tenant_uid = tenant_uid
        self.client_uid = client_uid
        self.account_uid = account_uid
        self.project_instance_uid = project_instance_uid
        self.start_date = start_date
        self.end_date = end_date
        self.custom_attributes = custom_attributes
    @classmethod
    def empty_write(cls):
        return cls("", "", "", "", "", "", datetime.datetime.now(), datetime.datetime.now())
    @classmethod
    def default_write(cls):
        return cls(base_dto.get_random_uid(), "", "", "", "", "", datetime.datetime.now(), datetime.datetime.now())
    @classmethod
    def random_write(cls):
        return cls(base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), datetime.datetime.now(), datetime.datetime.now())
    @classmethod
    def new_write(cls, project_account_uid: str, project_account_name: str, tenant_uid: str, client_uid: str, account_uid: str, project_instance_uid: str, start_date: datetime.datetime | None, end_date: datetime.datetime | None):
        return cls(project_account_uid, project_account_name, tenant_uid, client_uid, account_uid, project_instance_uid, start_date, end_date)
    @classmethod
    def new_write_with_defaults(cls, project_account_uid: str = "", project_account_name: str = "", tenant_uid: str = "", client_uid: str = "", account_uid: str = "", project_instance_uid: str = "", start_date: datetime.datetime | None = datetime.datetime.now(), end_date: datetime.datetime | None = datetime.datetime.now()):
        return cls(project_account_uid, project_account_name, tenant_uid, client_uid, account_uid, project_instance_uid, start_date, end_date)
    @classmethod
    def new_write_random_uid(cls, project_account_name: str, tenant_uid: str, client_uid: str, account_uid: str, project_instance_uid: str, start_date: datetime.datetime | None, end_date: datetime.datetime | None):
        return cls(base_dto.get_random_uid(), project_account_name, tenant_uid, client_uid, account_uid, project_instance_uid, start_date, end_date)
    @classmethod
    def get_class_model(cls) -> base_model:
        return db_models.project_account_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["project_account_uid"], d["project_account_name"], d["tenant_uid"], d["client_uid"], d["account_uid"], d["project_instance_uid"], d["start_date"], d["end_date"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return project_account_write_dto(self.project_account_uid, self.project_account_name, self.tenant_uid, self.client_uid, self.account_uid, self.project_instance_uid, self.start_date, self.end_date, self.custom_attributes)
    def clone_write_new_uid(self):
        return project_account_write_dto(base_dto.get_random_uid(), self.project_account_name, self.tenant_uid, self.client_uid, self.account_uid, self.project_instance_uid, self.start_date, self.end_date, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return project_account_write_dto(uid, self.project_account_name, self.tenant_uid, self.client_uid, self.account_uid, self.project_instance_uid, self.start_date, self.end_date, self.custom_attributes)
    def get_model(self) -> base_model:
        return db_models.project_account_model
    def get_uid(self) -> str:
        return self.project_account_uid
    def get_name(self) -> str:
        return self.project_account_name
    def get_list_values(self) -> list[any]:
        return [self.project_account_uid, self.project_account_name, self.tenant_uid, self.client_uid, self.account_uid, self.project_instance_uid, self.start_date, self.end_date, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.project_account_uid, self.project_account_name, self.tenant_uid, self.client_uid, self.account_uid, self.project_instance_uid, self.start_date, self.end_date]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.project_account_name, self.tenant_uid, self.client_uid, self.account_uid, self.project_instance_uid, self.start_date, self.end_date, self.custom_attributes, updated_by, self.project_account_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.project_account_uid, self.project_account_name, self.tenant_uid, self.client_uid, self.account_uid, self.project_instance_uid, self.start_date, self.end_date, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.project_account_name, self.tenant_uid, self.client_uid, self.account_uid, self.project_instance_uid, self.start_date, self.end_date]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.project_account_name, self.tenant_uid, self.client_uid, self.account_uid, self.project_instance_uid, self.start_date, self.end_date, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_uid() == obj.get_uid()
    def update_uid(self, uid: str):
        self.project_account_uid = uid
    def update_uid_attributes(self, project_account_uid: str, project_account_name: str, tenant_uid: str, client_uid: str, account_uid: str, project_instance_uid: str, start_date: datetime.datetime | None, end_date: datetime.datetime | None):
        self.project_account_uid = project_account_uid
        self.project_account_name = project_account_name
        self.tenant_uid = tenant_uid
        self.client_uid = client_uid
        self.account_uid = account_uid
        self.project_instance_uid = project_instance_uid
        self.start_date = start_date
        self.end_date = end_date
    def update_attributes(self, project_account_name: str, tenant_uid: str, client_uid: str, account_uid: str, project_instance_uid: str, start_date: datetime.datetime | None, end_date: datetime.datetime | None):
        self.project_account_name = project_account_name
        self.tenant_uid = tenant_uid
        self.client_uid = client_uid
        self.account_uid = account_uid
        self.project_instance_uid = project_instance_uid
        self.start_date = start_date
        self.end_date = end_date


@dataclass(frozen=False)
class project_budget_write_dto(base_write_dto):
    project_budget_uid: str
    project_budget_name: str
    tenant_uid: str
    client_uid: str
    project_instance_uid: str
    currency_uid: str
    budget_value: str
    is_approved: int
    is_current: int
    def __init__(self, project_budget_uid: str, project_budget_name: str, tenant_uid: str, client_uid: str, project_instance_uid: str, currency_uid: str, budget_value: str, is_approved: int, is_current: int, custom_attributes: str = "{}"):
        self.project_budget_uid = project_budget_uid
        self.project_budget_name = project_budget_name
        self.tenant_uid = tenant_uid
        self.client_uid = client_uid
        self.project_instance_uid = project_instance_uid
        self.currency_uid = currency_uid
        self.budget_value = budget_value
        self.is_approved = is_approved
        self.is_current = is_current
        self.custom_attributes = custom_attributes
    @classmethod
    def empty_write(cls):
        return cls("", "", "", "", "", "", "", 0, 0)
    @classmethod
    def default_write(cls):
        return cls(base_dto.get_random_uid(), "", "", "", "", "", "", 0, 0)
    @classmethod
    def random_write(cls):
        return cls(base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), "", 0, 0)
    @classmethod
    def new_write(cls, project_budget_uid: str, project_budget_name: str, tenant_uid: str, client_uid: str, project_instance_uid: str, currency_uid: str, budget_value: str, is_approved: int, is_current: int):
        return cls(project_budget_uid, project_budget_name, tenant_uid, client_uid, project_instance_uid, currency_uid, budget_value, is_approved, is_current)
    @classmethod
    def new_write_with_defaults(cls, project_budget_uid: str = "", project_budget_name: str = "", tenant_uid: str = "", client_uid: str = "", project_instance_uid: str = "", currency_uid: str = "", budget_value: str = "", is_approved: int = 0, is_current: int = 0):
        return cls(project_budget_uid, project_budget_name, tenant_uid, client_uid, project_instance_uid, currency_uid, budget_value, is_approved, is_current)
    @classmethod
    def new_write_random_uid(cls, project_budget_name: str, tenant_uid: str, client_uid: str, project_instance_uid: str, currency_uid: str, budget_value: str, is_approved: int, is_current: int):
        return cls(base_dto.get_random_uid(), project_budget_name, tenant_uid, client_uid, project_instance_uid, currency_uid, budget_value, is_approved, is_current)
    @classmethod
    def get_class_model(cls) -> base_model:
        return db_models.project_budget_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["project_budget_uid"], d["project_budget_name"], d["tenant_uid"], d["client_uid"], d["project_instance_uid"], d["currency_uid"], d["budget_value"], d["is_approved"], d["is_current"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return project_budget_write_dto(self.project_budget_uid, self.project_budget_name, self.tenant_uid, self.client_uid, self.project_instance_uid, self.currency_uid, self.budget_value, self.is_approved, self.is_current, self.custom_attributes)
    def clone_write_new_uid(self):
        return project_budget_write_dto(base_dto.get_random_uid(), self.project_budget_name, self.tenant_uid, self.client_uid, self.project_instance_uid, self.currency_uid, self.budget_value, self.is_approved, self.is_current, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return project_budget_write_dto(uid, self.project_budget_name, self.tenant_uid, self.client_uid, self.project_instance_uid, self.currency_uid, self.budget_value, self.is_approved, self.is_current, self.custom_attributes)
    def get_model(self) -> base_model:
        return db_models.project_budget_model
    def get_uid(self) -> str:
        return self.project_budget_uid
    def get_name(self) -> str:
        return self.project_budget_name
    def get_list_values(self) -> list[any]:
        return [self.project_budget_uid, self.project_budget_name, self.tenant_uid, self.client_uid, self.project_instance_uid, self.currency_uid, self.budget_value, self.is_approved, self.is_current, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.project_budget_uid, self.project_budget_name, self.tenant_uid, self.client_uid, self.project_instance_uid, self.currency_uid, self.budget_value, self.is_approved, self.is_current]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.project_budget_name, self.tenant_uid, self.client_uid, self.project_instance_uid, self.currency_uid, self.budget_value, self.is_approved, self.is_current, self.custom_attributes, updated_by, self.project_budget_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.project_budget_uid, self.project_budget_name, self.tenant_uid, self.client_uid, self.project_instance_uid, self.currency_uid, self.budget_value, self.is_approved, self.is_current, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.project_budget_name, self.tenant_uid, self.client_uid, self.project_instance_uid, self.currency_uid, self.budget_value, self.is_approved, self.is_current]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.project_budget_name, self.tenant_uid, self.client_uid, self.project_instance_uid, self.currency_uid, self.budget_value, self.is_approved, self.is_current, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_uid() == obj.get_uid()
    def update_uid(self, uid: str):
        self.project_budget_uid = uid
    def update_uid_attributes(self, project_budget_uid: str, project_budget_name: str, tenant_uid: str, client_uid: str, project_instance_uid: str, currency_uid: str, budget_value: str, is_approved: int, is_current: int):
        self.project_budget_uid = project_budget_uid
        self.project_budget_name = project_budget_name
        self.tenant_uid = tenant_uid
        self.client_uid = client_uid
        self.project_instance_uid = project_instance_uid
        self.currency_uid = currency_uid
        self.budget_value = budget_value
        self.is_approved = is_approved
        self.is_current = is_current
    def update_attributes(self, project_budget_name: str, tenant_uid: str, client_uid: str, project_instance_uid: str, currency_uid: str, budget_value: str, is_approved: int, is_current: int):
        self.project_budget_name = project_budget_name
        self.tenant_uid = tenant_uid
        self.client_uid = client_uid
        self.project_instance_uid = project_instance_uid
        self.currency_uid = currency_uid
        self.budget_value = budget_value
        self.is_approved = is_approved
        self.is_current = is_current


@dataclass(frozen=False)
class project_group_write_dto(base_write_dto):
    project_group_uid: str
    project_group_name: str
    tenant_uid: str
    project_group_description: str
    def __init__(self, project_group_uid: str, project_group_name: str, tenant_uid: str, project_group_description: str, custom_attributes: str = "{}"):
        self.project_group_uid = project_group_uid
        self.project_group_name = project_group_name
        self.tenant_uid = tenant_uid
        self.project_group_description = project_group_description
        self.custom_attributes = custom_attributes
    @classmethod
    def empty_write(cls):
        return cls("", "", "", "")
    @classmethod
    def default_write(cls):
        return cls(base_dto.get_random_uid(), "", "", "")
    @classmethod
    def random_write(cls):
        return cls(base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid())
    @classmethod
    def new_write(cls, project_group_uid: str, project_group_name: str, tenant_uid: str, project_group_description: str):
        return cls(project_group_uid, project_group_name, tenant_uid, project_group_description)
    @classmethod
    def new_write_with_defaults(cls, project_group_uid: str = "", project_group_name: str = "", tenant_uid: str = "", project_group_description: str = ""):
        return cls(project_group_uid, project_group_name, tenant_uid, project_group_description)
    @classmethod
    def new_write_random_uid(cls, project_group_name: str, tenant_uid: str, project_group_description: str):
        return cls(base_dto.get_random_uid(), project_group_name, tenant_uid, project_group_description)
    @classmethod
    def get_class_model(cls) -> base_model:
        return db_models.project_group_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["project_group_uid"], d["project_group_name"], d["tenant_uid"], d["project_group_description"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return project_group_write_dto(self.project_group_uid, self.project_group_name, self.tenant_uid, self.project_group_description, self.custom_attributes)
    def clone_write_new_uid(self):
        return project_group_write_dto(base_dto.get_random_uid(), self.project_group_name, self.tenant_uid, self.project_group_description, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return project_group_write_dto(uid, self.project_group_name, self.tenant_uid, self.project_group_description, self.custom_attributes)
    def get_model(self) -> base_model:
        return db_models.project_group_model
    def get_uid(self) -> str:
        return self.project_group_uid
    def get_name(self) -> str:
        return self.project_group_name
    def get_list_values(self) -> list[any]:
        return [self.project_group_uid, self.project_group_name, self.tenant_uid, self.project_group_description, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.project_group_uid, self.project_group_name, self.tenant_uid, self.project_group_description]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.project_group_name, self.tenant_uid, self.project_group_description, self.custom_attributes, updated_by, self.project_group_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.project_group_uid, self.project_group_name, self.tenant_uid, self.project_group_description, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.project_group_name, self.tenant_uid, self.project_group_description]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.project_group_name, self.tenant_uid, self.project_group_description, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_uid() == obj.get_uid()
    def update_uid(self, uid: str):
        self.project_group_uid = uid
    def update_uid_attributes(self, project_group_uid: str, project_group_name: str, tenant_uid: str, project_group_description: str):
        self.project_group_uid = project_group_uid
        self.project_group_name = project_group_name
        self.tenant_uid = tenant_uid
        self.project_group_description = project_group_description
    def update_attributes(self, project_group_name: str, tenant_uid: str, project_group_description: str):
        self.project_group_name = project_group_name
        self.tenant_uid = tenant_uid
        self.project_group_description = project_group_description


@dataclass(frozen=False)
class project_instance_write_dto(base_write_dto):
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
    def __init__(self, project_instance_uid: str, project_instance_name: str, tenant_uid: str, client_uid: str, project_type_uid: str, manager_account_uid: str, project_group_uid: str, project_code: str, project_description: str, is_billable: int, start_date: datetime.datetime | None, end_date: datetime.datetime | None, current_billed: str, budget: str, custom_attributes: str = "{}"):
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
        self.custom_attributes = custom_attributes
    @classmethod
    def empty_write(cls):
        return cls("", "", "", "", "", "", "", "", "", 0, datetime.datetime.now(), datetime.datetime.now(), "", "")
    @classmethod
    def default_write(cls):
        return cls(base_dto.get_random_uid(), "", "", "", "", "", "", "", "", 0, datetime.datetime.now(), datetime.datetime.now(), "", "")
    @classmethod
    def random_write(cls):
        return cls(base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), 0, datetime.datetime.now(), datetime.datetime.now(), "", "")
    @classmethod
    def new_write(cls, project_instance_uid: str, project_instance_name: str, tenant_uid: str, client_uid: str, project_type_uid: str, manager_account_uid: str, project_group_uid: str, project_code: str, project_description: str, is_billable: int, start_date: datetime.datetime | None, end_date: datetime.datetime | None, current_billed: str, budget: str):
        return cls(project_instance_uid, project_instance_name, tenant_uid, client_uid, project_type_uid, manager_account_uid, project_group_uid, project_code, project_description, is_billable, start_date, end_date, current_billed, budget)
    @classmethod
    def new_write_with_defaults(cls, project_instance_uid: str = "", project_instance_name: str = "", tenant_uid: str = "", client_uid: str = "", project_type_uid: str = "", manager_account_uid: str = "", project_group_uid: str = "", project_code: str = "", project_description: str = "", is_billable: int = 0, start_date: datetime.datetime | None = datetime.datetime.now(), end_date: datetime.datetime | None = datetime.datetime.now(), current_billed: str = "", budget: str = ""):
        return cls(project_instance_uid, project_instance_name, tenant_uid, client_uid, project_type_uid, manager_account_uid, project_group_uid, project_code, project_description, is_billable, start_date, end_date, current_billed, budget)
    @classmethod
    def new_write_random_uid(cls, project_instance_name: str, tenant_uid: str, client_uid: str, project_type_uid: str, manager_account_uid: str, project_group_uid: str, project_code: str, project_description: str, is_billable: int, start_date: datetime.datetime | None, end_date: datetime.datetime | None, current_billed: str, budget: str):
        return cls(base_dto.get_random_uid(), project_instance_name, tenant_uid, client_uid, project_type_uid, manager_account_uid, project_group_uid, project_code, project_description, is_billable, start_date, end_date, current_billed, budget)
    @classmethod
    def get_class_model(cls) -> base_model:
        return db_models.project_instance_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["project_instance_uid"], d["project_instance_name"], d["tenant_uid"], d["client_uid"], d["project_type_uid"], d["manager_account_uid"], d["project_group_uid"], d["project_code"], d["project_description"], d["is_billable"], d["start_date"], d["end_date"], d["current_billed"], d["budget"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return project_instance_write_dto(self.project_instance_uid, self.project_instance_name, self.tenant_uid, self.client_uid, self.project_type_uid, self.manager_account_uid, self.project_group_uid, self.project_code, self.project_description, self.is_billable, self.start_date, self.end_date, self.current_billed, self.budget, self.custom_attributes)
    def clone_write_new_uid(self):
        return project_instance_write_dto(base_dto.get_random_uid(), self.project_instance_name, self.tenant_uid, self.client_uid, self.project_type_uid, self.manager_account_uid, self.project_group_uid, self.project_code, self.project_description, self.is_billable, self.start_date, self.end_date, self.current_billed, self.budget, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return project_instance_write_dto(uid, self.project_instance_name, self.tenant_uid, self.client_uid, self.project_type_uid, self.manager_account_uid, self.project_group_uid, self.project_code, self.project_description, self.is_billable, self.start_date, self.end_date, self.current_billed, self.budget, self.custom_attributes)
    def get_model(self) -> base_model:
        return db_models.project_instance_model
    def get_uid(self) -> str:
        return self.project_instance_uid
    def get_name(self) -> str:
        return self.project_instance_name
    def get_list_values(self) -> list[any]:
        return [self.project_instance_uid, self.project_instance_name, self.tenant_uid, self.client_uid, self.project_type_uid, self.manager_account_uid, self.project_group_uid, self.project_code, self.project_description, self.is_billable, self.start_date, self.end_date, self.current_billed, self.budget, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.project_instance_uid, self.project_instance_name, self.tenant_uid, self.client_uid, self.project_type_uid, self.manager_account_uid, self.project_group_uid, self.project_code, self.project_description, self.is_billable, self.start_date, self.end_date, self.current_billed, self.budget]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.project_instance_name, self.tenant_uid, self.client_uid, self.project_type_uid, self.manager_account_uid, self.project_group_uid, self.project_code, self.project_description, self.is_billable, self.start_date, self.end_date, self.current_billed, self.budget, self.custom_attributes, updated_by, self.project_instance_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.project_instance_uid, self.project_instance_name, self.tenant_uid, self.client_uid, self.project_type_uid, self.manager_account_uid, self.project_group_uid, self.project_code, self.project_description, self.is_billable, self.start_date, self.end_date, self.current_billed, self.budget, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.project_instance_name, self.tenant_uid, self.client_uid, self.project_type_uid, self.manager_account_uid, self.project_group_uid, self.project_code, self.project_description, self.is_billable, self.start_date, self.end_date, self.current_billed, self.budget]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.project_instance_name, self.tenant_uid, self.client_uid, self.project_type_uid, self.manager_account_uid, self.project_group_uid, self.project_code, self.project_description, self.is_billable, self.start_date, self.end_date, self.current_billed, self.budget, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_uid() == obj.get_uid()
    def update_uid(self, uid: str):
        self.project_instance_uid = uid
    def update_uid_attributes(self, project_instance_uid: str, project_instance_name: str, tenant_uid: str, client_uid: str, project_type_uid: str, manager_account_uid: str, project_group_uid: str, project_code: str, project_description: str, is_billable: int, start_date: datetime.datetime | None, end_date: datetime.datetime | None, current_billed: str, budget: str):
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
    def update_attributes(self, project_instance_name: str, tenant_uid: str, client_uid: str, project_type_uid: str, manager_account_uid: str, project_group_uid: str, project_code: str, project_description: str, is_billable: int, start_date: datetime.datetime | None, end_date: datetime.datetime | None, current_billed: str, budget: str):
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


@dataclass(frozen=False)
class project_milestone_write_dto(base_write_dto):
    project_milestone_uid: str
    project_milestone_name: str
    tenant_uid: str
    client_uid: str
    project_instance_uid: str
    project_budget_uid: str | None
    project_phase_uid: str | None
    start_date: datetime.datetime
    end_date: datetime.datetime
    status_name: str
    def __init__(self, project_milestone_uid: str, project_milestone_name: str, tenant_uid: str, client_uid: str, project_instance_uid: str, project_budget_uid: str | None, project_phase_uid: str | None, start_date: datetime.datetime, end_date: datetime.datetime, status_name: str, custom_attributes: str = "{}"):
        self.project_milestone_uid = project_milestone_uid
        self.project_milestone_name = project_milestone_name
        self.tenant_uid = tenant_uid
        self.client_uid = client_uid
        self.project_instance_uid = project_instance_uid
        self.project_budget_uid = project_budget_uid
        self.project_phase_uid = project_phase_uid
        self.start_date = start_date
        self.end_date = end_date
        self.status_name = status_name
        self.custom_attributes = custom_attributes
    @classmethod
    def empty_write(cls):
        return cls("", "", "", "", "", "", "", datetime.datetime.now(), datetime.datetime.now(), "")
    @classmethod
    def default_write(cls):
        return cls(base_dto.get_random_uid(), "", "", "", "", "", "", datetime.datetime.now(), datetime.datetime.now(), "")
    @classmethod
    def random_write(cls):
        return cls(base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), datetime.datetime.now(), datetime.datetime.now(), base_dto.get_random_uid())
    @classmethod
    def new_write(cls, project_milestone_uid: str, project_milestone_name: str, tenant_uid: str, client_uid: str, project_instance_uid: str, project_budget_uid: str | None, project_phase_uid: str | None, start_date: datetime.datetime, end_date: datetime.datetime, status_name: str):
        return cls(project_milestone_uid, project_milestone_name, tenant_uid, client_uid, project_instance_uid, project_budget_uid, project_phase_uid, start_date, end_date, status_name)
    @classmethod
    def new_write_with_defaults(cls, project_milestone_uid: str = "", project_milestone_name: str = "", tenant_uid: str = "", client_uid: str = "", project_instance_uid: str = "", project_budget_uid: str | None = "", project_phase_uid: str | None = "", start_date: datetime.datetime = datetime.datetime.now(), end_date: datetime.datetime = datetime.datetime.now(), status_name: str = ""):
        return cls(project_milestone_uid, project_milestone_name, tenant_uid, client_uid, project_instance_uid, project_budget_uid, project_phase_uid, start_date, end_date, status_name)
    @classmethod
    def new_write_random_uid(cls, project_milestone_name: str, tenant_uid: str, client_uid: str, project_instance_uid: str, project_budget_uid: str | None, project_phase_uid: str | None, start_date: datetime.datetime, end_date: datetime.datetime, status_name: str):
        return cls(base_dto.get_random_uid(), project_milestone_name, tenant_uid, client_uid, project_instance_uid, project_budget_uid, project_phase_uid, start_date, end_date, status_name)
    @classmethod
    def get_class_model(cls) -> base_model:
        return db_models.project_milestone_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["project_milestone_uid"], d["project_milestone_name"], d["tenant_uid"], d["client_uid"], d["project_instance_uid"], d["project_budget_uid"], d["project_phase_uid"], d["start_date"], d["end_date"], d["status_name"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return project_milestone_write_dto(self.project_milestone_uid, self.project_milestone_name, self.tenant_uid, self.client_uid, self.project_instance_uid, self.project_budget_uid, self.project_phase_uid, self.start_date, self.end_date, self.status_name, self.custom_attributes)
    def clone_write_new_uid(self):
        return project_milestone_write_dto(base_dto.get_random_uid(), self.project_milestone_name, self.tenant_uid, self.client_uid, self.project_instance_uid, self.project_budget_uid, self.project_phase_uid, self.start_date, self.end_date, self.status_name, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return project_milestone_write_dto(uid, self.project_milestone_name, self.tenant_uid, self.client_uid, self.project_instance_uid, self.project_budget_uid, self.project_phase_uid, self.start_date, self.end_date, self.status_name, self.custom_attributes)
    def get_model(self) -> base_model:
        return db_models.project_milestone_model
    def get_uid(self) -> str:
        return self.project_milestone_uid
    def get_name(self) -> str:
        return self.project_milestone_name
    def get_list_values(self) -> list[any]:
        return [self.project_milestone_uid, self.project_milestone_name, self.tenant_uid, self.client_uid, self.project_instance_uid, self.project_budget_uid, self.project_phase_uid, self.start_date, self.end_date, self.status_name, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.project_milestone_uid, self.project_milestone_name, self.tenant_uid, self.client_uid, self.project_instance_uid, self.project_budget_uid, self.project_phase_uid, self.start_date, self.end_date, self.status_name]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.project_milestone_name, self.tenant_uid, self.client_uid, self.project_instance_uid, self.project_budget_uid, self.project_phase_uid, self.start_date, self.end_date, self.status_name, self.custom_attributes, updated_by, self.project_milestone_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.project_milestone_uid, self.project_milestone_name, self.tenant_uid, self.client_uid, self.project_instance_uid, self.project_budget_uid, self.project_phase_uid, self.start_date, self.end_date, self.status_name, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.project_milestone_name, self.tenant_uid, self.client_uid, self.project_instance_uid, self.project_budget_uid, self.project_phase_uid, self.start_date, self.end_date, self.status_name]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.project_milestone_name, self.tenant_uid, self.client_uid, self.project_instance_uid, self.project_budget_uid, self.project_phase_uid, self.start_date, self.end_date, self.status_name, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_uid() == obj.get_uid()
    def update_uid(self, uid: str):
        self.project_milestone_uid = uid
    def update_uid_attributes(self, project_milestone_uid: str, project_milestone_name: str, tenant_uid: str, client_uid: str, project_instance_uid: str, project_budget_uid: str | None, project_phase_uid: str | None, start_date: datetime.datetime, end_date: datetime.datetime, status_name: str):
        self.project_milestone_uid = project_milestone_uid
        self.project_milestone_name = project_milestone_name
        self.tenant_uid = tenant_uid
        self.client_uid = client_uid
        self.project_instance_uid = project_instance_uid
        self.project_budget_uid = project_budget_uid
        self.project_phase_uid = project_phase_uid
        self.start_date = start_date
        self.end_date = end_date
        self.status_name = status_name
    def update_attributes(self, project_milestone_name: str, tenant_uid: str, client_uid: str, project_instance_uid: str, project_budget_uid: str | None, project_phase_uid: str | None, start_date: datetime.datetime, end_date: datetime.datetime, status_name: str):
        self.project_milestone_name = project_milestone_name
        self.tenant_uid = tenant_uid
        self.client_uid = client_uid
        self.project_instance_uid = project_instance_uid
        self.project_budget_uid = project_budget_uid
        self.project_phase_uid = project_phase_uid
        self.start_date = start_date
        self.end_date = end_date
        self.status_name = status_name


@dataclass(frozen=False)
class project_phase_write_dto(base_write_dto):
    project_phase_uid: str
    project_phase_name: str
    tenant_uid: str
    client_uid: str
    project_instance_uid: str
    project_budget_uid: str | None
    previous_project_phase_uid: str | None
    client_contract_uid: str | None
    start_date: datetime.datetime
    end_date: datetime.datetime
    status_name: str
    def __init__(self, project_phase_uid: str, project_phase_name: str, tenant_uid: str, client_uid: str, project_instance_uid: str, project_budget_uid: str | None, previous_project_phase_uid: str | None, client_contract_uid: str | None, start_date: datetime.datetime, end_date: datetime.datetime, status_name: str, custom_attributes: str = "{}"):
        self.project_phase_uid = project_phase_uid
        self.project_phase_name = project_phase_name
        self.tenant_uid = tenant_uid
        self.client_uid = client_uid
        self.project_instance_uid = project_instance_uid
        self.project_budget_uid = project_budget_uid
        self.previous_project_phase_uid = previous_project_phase_uid
        self.client_contract_uid = client_contract_uid
        self.start_date = start_date
        self.end_date = end_date
        self.status_name = status_name
        self.custom_attributes = custom_attributes
    @classmethod
    def empty_write(cls):
        return cls("", "", "", "", "", "", "", "", datetime.datetime.now(), datetime.datetime.now(), "")
    @classmethod
    def default_write(cls):
        return cls(base_dto.get_random_uid(), "", "", "", "", "", "", "", datetime.datetime.now(), datetime.datetime.now(), "")
    @classmethod
    def random_write(cls):
        return cls(base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), datetime.datetime.now(), datetime.datetime.now(), base_dto.get_random_uid())
    @classmethod
    def new_write(cls, project_phase_uid: str, project_phase_name: str, tenant_uid: str, client_uid: str, project_instance_uid: str, project_budget_uid: str | None, previous_project_phase_uid: str | None, client_contract_uid: str | None, start_date: datetime.datetime, end_date: datetime.datetime, status_name: str):
        return cls(project_phase_uid, project_phase_name, tenant_uid, client_uid, project_instance_uid, project_budget_uid, previous_project_phase_uid, client_contract_uid, start_date, end_date, status_name)
    @classmethod
    def new_write_with_defaults(cls, project_phase_uid: str = "", project_phase_name: str = "", tenant_uid: str = "", client_uid: str = "", project_instance_uid: str = "", project_budget_uid: str | None = "", previous_project_phase_uid: str | None = "", client_contract_uid: str | None = "", start_date: datetime.datetime = datetime.datetime.now(), end_date: datetime.datetime = datetime.datetime.now(), status_name: str = ""):
        return cls(project_phase_uid, project_phase_name, tenant_uid, client_uid, project_instance_uid, project_budget_uid, previous_project_phase_uid, client_contract_uid, start_date, end_date, status_name)
    @classmethod
    def new_write_random_uid(cls, project_phase_name: str, tenant_uid: str, client_uid: str, project_instance_uid: str, project_budget_uid: str | None, previous_project_phase_uid: str | None, client_contract_uid: str | None, start_date: datetime.datetime, end_date: datetime.datetime, status_name: str):
        return cls(base_dto.get_random_uid(), project_phase_name, tenant_uid, client_uid, project_instance_uid, project_budget_uid, previous_project_phase_uid, client_contract_uid, start_date, end_date, status_name)
    @classmethod
    def get_class_model(cls) -> base_model:
        return db_models.project_phase_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["project_phase_uid"], d["project_phase_name"], d["tenant_uid"], d["client_uid"], d["project_instance_uid"], d["project_budget_uid"], d["previous_project_phase_uid"], d["client_contract_uid"], d["start_date"], d["end_date"], d["status_name"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return project_phase_write_dto(self.project_phase_uid, self.project_phase_name, self.tenant_uid, self.client_uid, self.project_instance_uid, self.project_budget_uid, self.previous_project_phase_uid, self.client_contract_uid, self.start_date, self.end_date, self.status_name, self.custom_attributes)
    def clone_write_new_uid(self):
        return project_phase_write_dto(base_dto.get_random_uid(), self.project_phase_name, self.tenant_uid, self.client_uid, self.project_instance_uid, self.project_budget_uid, self.previous_project_phase_uid, self.client_contract_uid, self.start_date, self.end_date, self.status_name, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return project_phase_write_dto(uid, self.project_phase_name, self.tenant_uid, self.client_uid, self.project_instance_uid, self.project_budget_uid, self.previous_project_phase_uid, self.client_contract_uid, self.start_date, self.end_date, self.status_name, self.custom_attributes)
    def get_model(self) -> base_model:
        return db_models.project_phase_model
    def get_uid(self) -> str:
        return self.project_phase_uid
    def get_name(self) -> str:
        return self.project_phase_name
    def get_list_values(self) -> list[any]:
        return [self.project_phase_uid, self.project_phase_name, self.tenant_uid, self.client_uid, self.project_instance_uid, self.project_budget_uid, self.previous_project_phase_uid, self.client_contract_uid, self.start_date, self.end_date, self.status_name, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.project_phase_uid, self.project_phase_name, self.tenant_uid, self.client_uid, self.project_instance_uid, self.project_budget_uid, self.previous_project_phase_uid, self.client_contract_uid, self.start_date, self.end_date, self.status_name]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.project_phase_name, self.tenant_uid, self.client_uid, self.project_instance_uid, self.project_budget_uid, self.previous_project_phase_uid, self.client_contract_uid, self.start_date, self.end_date, self.status_name, self.custom_attributes, updated_by, self.project_phase_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.project_phase_uid, self.project_phase_name, self.tenant_uid, self.client_uid, self.project_instance_uid, self.project_budget_uid, self.previous_project_phase_uid, self.client_contract_uid, self.start_date, self.end_date, self.status_name, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.project_phase_name, self.tenant_uid, self.client_uid, self.project_instance_uid, self.project_budget_uid, self.previous_project_phase_uid, self.client_contract_uid, self.start_date, self.end_date, self.status_name]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.project_phase_name, self.tenant_uid, self.client_uid, self.project_instance_uid, self.project_budget_uid, self.previous_project_phase_uid, self.client_contract_uid, self.start_date, self.end_date, self.status_name, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_uid() == obj.get_uid()
    def update_uid(self, uid: str):
        self.project_phase_uid = uid
    def update_uid_attributes(self, project_phase_uid: str, project_phase_name: str, tenant_uid: str, client_uid: str, project_instance_uid: str, project_budget_uid: str | None, previous_project_phase_uid: str | None, client_contract_uid: str | None, start_date: datetime.datetime, end_date: datetime.datetime, status_name: str):
        self.project_phase_uid = project_phase_uid
        self.project_phase_name = project_phase_name
        self.tenant_uid = tenant_uid
        self.client_uid = client_uid
        self.project_instance_uid = project_instance_uid
        self.project_budget_uid = project_budget_uid
        self.previous_project_phase_uid = previous_project_phase_uid
        self.client_contract_uid = client_contract_uid
        self.start_date = start_date
        self.end_date = end_date
        self.status_name = status_name
    def update_attributes(self, project_phase_name: str, tenant_uid: str, client_uid: str, project_instance_uid: str, project_budget_uid: str | None, previous_project_phase_uid: str | None, client_contract_uid: str | None, start_date: datetime.datetime, end_date: datetime.datetime, status_name: str):
        self.project_phase_name = project_phase_name
        self.tenant_uid = tenant_uid
        self.client_uid = client_uid
        self.project_instance_uid = project_instance_uid
        self.project_budget_uid = project_budget_uid
        self.previous_project_phase_uid = previous_project_phase_uid
        self.client_contract_uid = client_contract_uid
        self.start_date = start_date
        self.end_date = end_date
        self.status_name = status_name


@dataclass(frozen=False)
class project_type_write_dto(base_write_dto):
    project_type_uid: str
    project_type_name: str
    project_type_description: str
    def __init__(self, project_type_uid: str, project_type_name: str, project_type_description: str, custom_attributes: str = "{}"):
        self.project_type_uid = project_type_uid
        self.project_type_name = project_type_name
        self.project_type_description = project_type_description
        self.custom_attributes = custom_attributes
    @classmethod
    def empty_write(cls):
        return cls("", "", "")
    @classmethod
    def default_write(cls):
        return cls(base_dto.get_random_uid(), "", "")
    @classmethod
    def random_write(cls):
        return cls(base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid())
    @classmethod
    def new_write(cls, project_type_uid: str, project_type_name: str, project_type_description: str):
        return cls(project_type_uid, project_type_name, project_type_description)
    @classmethod
    def new_write_with_defaults(cls, project_type_uid: str = "", project_type_name: str = "", project_type_description: str = ""):
        return cls(project_type_uid, project_type_name, project_type_description)
    @classmethod
    def new_write_random_uid(cls, project_type_name: str, project_type_description: str):
        return cls(base_dto.get_random_uid(), project_type_name, project_type_description)
    @classmethod
    def get_class_model(cls) -> base_model:
        return db_models.project_type_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["project_type_uid"], d["project_type_name"], d["project_type_description"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return project_type_write_dto(self.project_type_uid, self.project_type_name, self.project_type_description, self.custom_attributes)
    def clone_write_new_uid(self):
        return project_type_write_dto(base_dto.get_random_uid(), self.project_type_name, self.project_type_description, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return project_type_write_dto(uid, self.project_type_name, self.project_type_description, self.custom_attributes)
    def get_model(self) -> base_model:
        return db_models.project_type_model
    def get_uid(self) -> str:
        return self.project_type_uid
    def get_name(self) -> str:
        return self.project_type_name
    def get_list_values(self) -> list[any]:
        return [self.project_type_uid, self.project_type_name, self.project_type_description, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.project_type_uid, self.project_type_name, self.project_type_description]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.project_type_name, self.project_type_description, self.custom_attributes, updated_by, self.project_type_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.project_type_uid, self.project_type_name, self.project_type_description, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.project_type_name, self.project_type_description]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.project_type_name, self.project_type_description, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_uid() == obj.get_uid()
    def update_uid(self, uid: str):
        self.project_type_uid = uid
    def update_uid_attributes(self, project_type_uid: str, project_type_name: str, project_type_description: str):
        self.project_type_uid = project_type_uid
        self.project_type_name = project_type_name
        self.project_type_description = project_type_description
    def update_attributes(self, project_type_name: str, project_type_description: str):
        self.project_type_name = project_type_name
        self.project_type_description = project_type_description


@dataclass(frozen=False)
class report_write_dto(base_write_dto):
    report_uid: str
    report_name: str
    tenant_uid: str
    account_uid: str
    report_status_uid: str
    report_query: str
    report_parameters: str
    def __init__(self, report_uid: str, report_name: str, tenant_uid: str, account_uid: str, report_status_uid: str, report_query: str, report_parameters: str, custom_attributes: str = "{}"):
        self.report_uid = report_uid
        self.report_name = report_name
        self.tenant_uid = tenant_uid
        self.account_uid = account_uid
        self.report_status_uid = report_status_uid
        self.report_query = report_query
        self.report_parameters = report_parameters
        self.custom_attributes = custom_attributes
    @classmethod
    def empty_write(cls):
        return cls("", "", "", "", "", "", "")
    @classmethod
    def default_write(cls):
        return cls(base_dto.get_random_uid(), "", "", "", "", "", "")
    @classmethod
    def random_write(cls):
        return cls(base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid())
    @classmethod
    def new_write(cls, report_uid: str, report_name: str, tenant_uid: str, account_uid: str, report_status_uid: str, report_query: str, report_parameters: str):
        return cls(report_uid, report_name, tenant_uid, account_uid, report_status_uid, report_query, report_parameters)
    @classmethod
    def new_write_with_defaults(cls, report_uid: str = "", report_name: str = "", tenant_uid: str = "", account_uid: str = "", report_status_uid: str = "", report_query: str = "", report_parameters: str = ""):
        return cls(report_uid, report_name, tenant_uid, account_uid, report_status_uid, report_query, report_parameters)
    @classmethod
    def new_write_random_uid(cls, report_name: str, tenant_uid: str, account_uid: str, report_status_uid: str, report_query: str, report_parameters: str):
        return cls(base_dto.get_random_uid(), report_name, tenant_uid, account_uid, report_status_uid, report_query, report_parameters)
    @classmethod
    def get_class_model(cls) -> base_model:
        return db_models.report_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["report_uid"], d["report_name"], d["tenant_uid"], d["account_uid"], d["report_status_uid"], d["report_query"], d["report_parameters"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return report_write_dto(self.report_uid, self.report_name, self.tenant_uid, self.account_uid, self.report_status_uid, self.report_query, self.report_parameters, self.custom_attributes)
    def clone_write_new_uid(self):
        return report_write_dto(base_dto.get_random_uid(), self.report_name, self.tenant_uid, self.account_uid, self.report_status_uid, self.report_query, self.report_parameters, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return report_write_dto(uid, self.report_name, self.tenant_uid, self.account_uid, self.report_status_uid, self.report_query, self.report_parameters, self.custom_attributes)
    def get_model(self) -> base_model:
        return db_models.report_model
    def get_uid(self) -> str:
        return self.report_uid
    def get_name(self) -> str:
        return self.report_name
    def get_list_values(self) -> list[any]:
        return [self.report_uid, self.report_name, self.tenant_uid, self.account_uid, self.report_status_uid, self.report_query, self.report_parameters, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.report_uid, self.report_name, self.tenant_uid, self.account_uid, self.report_status_uid, self.report_query, self.report_parameters]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.report_name, self.tenant_uid, self.account_uid, self.report_status_uid, self.report_query, self.report_parameters, self.custom_attributes, updated_by, self.report_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.report_uid, self.report_name, self.tenant_uid, self.account_uid, self.report_status_uid, self.report_query, self.report_parameters, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.report_name, self.tenant_uid, self.account_uid, self.report_status_uid, self.report_query, self.report_parameters]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.report_name, self.tenant_uid, self.account_uid, self.report_status_uid, self.report_query, self.report_parameters, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_uid() == obj.get_uid()
    def update_uid(self, uid: str):
        self.report_uid = uid
    def update_uid_attributes(self, report_uid: str, report_name: str, tenant_uid: str, account_uid: str, report_status_uid: str, report_query: str, report_parameters: str):
        self.report_uid = report_uid
        self.report_name = report_name
        self.tenant_uid = tenant_uid
        self.account_uid = account_uid
        self.report_status_uid = report_status_uid
        self.report_query = report_query
        self.report_parameters = report_parameters
    def update_attributes(self, report_name: str, tenant_uid: str, account_uid: str, report_status_uid: str, report_query: str, report_parameters: str):
        self.report_name = report_name
        self.tenant_uid = tenant_uid
        self.account_uid = account_uid
        self.report_status_uid = report_status_uid
        self.report_query = report_query
        self.report_parameters = report_parameters


@dataclass(frozen=False)
class report_content_type_write_dto(base_write_dto):
    report_content_type_uid: str
    report_content_type_name: str
    def __init__(self, report_content_type_uid: str, report_content_type_name: str, custom_attributes: str = "{}"):
        self.report_content_type_uid = report_content_type_uid
        self.report_content_type_name = report_content_type_name
        self.custom_attributes = custom_attributes
    @classmethod
    def empty_write(cls):
        return cls("", "")
    @classmethod
    def default_write(cls):
        return cls(base_dto.get_random_uid(), "")
    @classmethod
    def random_write(cls):
        return cls(base_dto.get_random_uid(), base_dto.get_random_uid())
    @classmethod
    def new_write(cls, report_content_type_uid: str, report_content_type_name: str):
        return cls(report_content_type_uid, report_content_type_name)
    @classmethod
    def new_write_with_defaults(cls, report_content_type_uid: str = "", report_content_type_name: str = ""):
        return cls(report_content_type_uid, report_content_type_name)
    @classmethod
    def new_write_random_uid(cls, report_content_type_name: str):
        return cls(base_dto.get_random_uid(), report_content_type_name)
    @classmethod
    def get_class_model(cls) -> base_model:
        return db_models.report_content_type_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["report_content_type_uid"], d["report_content_type_name"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return report_content_type_write_dto(self.report_content_type_uid, self.report_content_type_name, self.custom_attributes)
    def clone_write_new_uid(self):
        return report_content_type_write_dto(base_dto.get_random_uid(), self.report_content_type_name, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return report_content_type_write_dto(uid, self.report_content_type_name, self.custom_attributes)
    def get_model(self) -> base_model:
        return db_models.report_content_type_model
    def get_uid(self) -> str:
        return self.report_content_type_uid
    def get_name(self) -> str:
        return self.report_content_type_name
    def get_list_values(self) -> list[any]:
        return [self.report_content_type_uid, self.report_content_type_name, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.report_content_type_uid, self.report_content_type_name]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.report_content_type_name, self.custom_attributes, updated_by, self.report_content_type_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.report_content_type_uid, self.report_content_type_name, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.report_content_type_name]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.report_content_type_name, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_uid() == obj.get_uid()
    def update_uid(self, uid: str):
        self.report_content_type_uid = uid
    def update_uid_attributes(self, report_content_type_uid: str, report_content_type_name: str):
        self.report_content_type_uid = report_content_type_uid
        self.report_content_type_name = report_content_type_name
    def update_attributes(self, report_content_type_name: str):
        self.report_content_type_name = report_content_type_name


@dataclass(frozen=False)
class report_format_write_dto(base_write_dto):
    report_format_uid: str
    report_format_name: str
    class_name: str
    def __init__(self, report_format_uid: str, report_format_name: str, class_name: str, custom_attributes: str = "{}"):
        self.report_format_uid = report_format_uid
        self.report_format_name = report_format_name
        self.class_name = class_name
        self.custom_attributes = custom_attributes
    @classmethod
    def empty_write(cls):
        return cls("", "", "")
    @classmethod
    def default_write(cls):
        return cls(base_dto.get_random_uid(), "", "")
    @classmethod
    def random_write(cls):
        return cls(base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid())
    @classmethod
    def new_write(cls, report_format_uid: str, report_format_name: str, class_name: str):
        return cls(report_format_uid, report_format_name, class_name)
    @classmethod
    def new_write_with_defaults(cls, report_format_uid: str = "", report_format_name: str = "", class_name: str = ""):
        return cls(report_format_uid, report_format_name, class_name)
    @classmethod
    def new_write_random_uid(cls, report_format_name: str, class_name: str):
        return cls(base_dto.get_random_uid(), report_format_name, class_name)
    @classmethod
    def get_class_model(cls) -> base_model:
        return db_models.report_format_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["report_format_uid"], d["report_format_name"], d["class_name"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return report_format_write_dto(self.report_format_uid, self.report_format_name, self.class_name, self.custom_attributes)
    def clone_write_new_uid(self):
        return report_format_write_dto(base_dto.get_random_uid(), self.report_format_name, self.class_name, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return report_format_write_dto(uid, self.report_format_name, self.class_name, self.custom_attributes)
    def get_model(self) -> base_model:
        return db_models.report_format_model
    def get_uid(self) -> str:
        return self.report_format_uid
    def get_name(self) -> str:
        return self.report_format_name
    def get_list_values(self) -> list[any]:
        return [self.report_format_uid, self.report_format_name, self.class_name, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.report_format_uid, self.report_format_name, self.class_name]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.report_format_name, self.class_name, self.custom_attributes, updated_by, self.report_format_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.report_format_uid, self.report_format_name, self.class_name, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.report_format_name, self.class_name]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.report_format_name, self.class_name, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_uid() == obj.get_uid()
    def update_uid(self, uid: str):
        self.report_format_uid = uid
    def update_uid_attributes(self, report_format_uid: str, report_format_name: str, class_name: str):
        self.report_format_uid = report_format_uid
        self.report_format_name = report_format_name
        self.class_name = class_name
    def update_attributes(self, report_format_name: str, class_name: str):
        self.report_format_name = report_format_name
        self.class_name = class_name


@dataclass(frozen=False)
class report_run_write_dto(base_write_dto):
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
    def __init__(self, report_run_uid: str, report_run_name: str, tenant_uid: str, account_uid: str, report_uid: str, report_format_uid: str, report_status_uid: str, report_content_type_uid: str, input_parameters_json: str, run_time_ms: int, returned_rows: int, content_size: int, custom_attributes: str = "{}"):
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
        self.custom_attributes = custom_attributes
    @classmethod
    def empty_write(cls):
        return cls("", "", "", "", "", "", "", "", "", 0, 0, 0)
    @classmethod
    def default_write(cls):
        return cls(base_dto.get_random_uid(), "", "", "", "", "", "", "", "", 0, 0, 0)
    @classmethod
    def random_write(cls):
        return cls(base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), 0, 0, 0)
    @classmethod
    def new_write(cls, report_run_uid: str, report_run_name: str, tenant_uid: str, account_uid: str, report_uid: str, report_format_uid: str, report_status_uid: str, report_content_type_uid: str, input_parameters_json: str, run_time_ms: int, returned_rows: int, content_size: int):
        return cls(report_run_uid, report_run_name, tenant_uid, account_uid, report_uid, report_format_uid, report_status_uid, report_content_type_uid, input_parameters_json, run_time_ms, returned_rows, content_size)
    @classmethod
    def new_write_with_defaults(cls, report_run_uid: str = "", report_run_name: str = "", tenant_uid: str = "", account_uid: str = "", report_uid: str = "", report_format_uid: str = "", report_status_uid: str = "", report_content_type_uid: str = "", input_parameters_json: str = "", run_time_ms: int = 0, returned_rows: int = 0, content_size: int = 0):
        return cls(report_run_uid, report_run_name, tenant_uid, account_uid, report_uid, report_format_uid, report_status_uid, report_content_type_uid, input_parameters_json, run_time_ms, returned_rows, content_size)
    @classmethod
    def new_write_random_uid(cls, report_run_name: str, tenant_uid: str, account_uid: str, report_uid: str, report_format_uid: str, report_status_uid: str, report_content_type_uid: str, input_parameters_json: str, run_time_ms: int, returned_rows: int, content_size: int):
        return cls(base_dto.get_random_uid(), report_run_name, tenant_uid, account_uid, report_uid, report_format_uid, report_status_uid, report_content_type_uid, input_parameters_json, run_time_ms, returned_rows, content_size)
    @classmethod
    def get_class_model(cls) -> base_model:
        return db_models.report_run_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["report_run_uid"], d["report_run_name"], d["tenant_uid"], d["account_uid"], d["report_uid"], d["report_format_uid"], d["report_status_uid"], d["report_content_type_uid"], d["input_parameters_json"], d["run_time_ms"], d["returned_rows"], d["content_size"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return report_run_write_dto(self.report_run_uid, self.report_run_name, self.tenant_uid, self.account_uid, self.report_uid, self.report_format_uid, self.report_status_uid, self.report_content_type_uid, self.input_parameters_json, self.run_time_ms, self.returned_rows, self.content_size, self.custom_attributes)
    def clone_write_new_uid(self):
        return report_run_write_dto(base_dto.get_random_uid(), self.report_run_name, self.tenant_uid, self.account_uid, self.report_uid, self.report_format_uid, self.report_status_uid, self.report_content_type_uid, self.input_parameters_json, self.run_time_ms, self.returned_rows, self.content_size, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return report_run_write_dto(uid, self.report_run_name, self.tenant_uid, self.account_uid, self.report_uid, self.report_format_uid, self.report_status_uid, self.report_content_type_uid, self.input_parameters_json, self.run_time_ms, self.returned_rows, self.content_size, self.custom_attributes)
    def get_model(self) -> base_model:
        return db_models.report_run_model
    def get_uid(self) -> str:
        return self.report_run_uid
    def get_name(self) -> str:
        return self.report_run_name
    def get_list_values(self) -> list[any]:
        return [self.report_run_uid, self.report_run_name, self.tenant_uid, self.account_uid, self.report_uid, self.report_format_uid, self.report_status_uid, self.report_content_type_uid, self.input_parameters_json, self.run_time_ms, self.returned_rows, self.content_size, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.report_run_uid, self.report_run_name, self.tenant_uid, self.account_uid, self.report_uid, self.report_format_uid, self.report_status_uid, self.report_content_type_uid, self.input_parameters_json, self.run_time_ms, self.returned_rows, self.content_size]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.report_run_name, self.tenant_uid, self.account_uid, self.report_uid, self.report_format_uid, self.report_status_uid, self.report_content_type_uid, self.input_parameters_json, self.run_time_ms, self.returned_rows, self.content_size, self.custom_attributes, updated_by, self.report_run_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.report_run_uid, self.report_run_name, self.tenant_uid, self.account_uid, self.report_uid, self.report_format_uid, self.report_status_uid, self.report_content_type_uid, self.input_parameters_json, self.run_time_ms, self.returned_rows, self.content_size, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.report_run_name, self.tenant_uid, self.account_uid, self.report_uid, self.report_format_uid, self.report_status_uid, self.report_content_type_uid, self.input_parameters_json, self.run_time_ms, self.returned_rows, self.content_size]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.report_run_name, self.tenant_uid, self.account_uid, self.report_uid, self.report_format_uid, self.report_status_uid, self.report_content_type_uid, self.input_parameters_json, self.run_time_ms, self.returned_rows, self.content_size, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_uid() == obj.get_uid()
    def update_uid(self, uid: str):
        self.report_run_uid = uid
    def update_uid_attributes(self, report_run_uid: str, report_run_name: str, tenant_uid: str, account_uid: str, report_uid: str, report_format_uid: str, report_status_uid: str, report_content_type_uid: str, input_parameters_json: str, run_time_ms: int, returned_rows: int, content_size: int):
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
    def update_attributes(self, report_run_name: str, tenant_uid: str, account_uid: str, report_uid: str, report_format_uid: str, report_status_uid: str, report_content_type_uid: str, input_parameters_json: str, run_time_ms: int, returned_rows: int, content_size: int):
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


@dataclass(frozen=False)
class report_status_write_dto(base_write_dto):
    report_status_uid: str
    report_status_name: str
    def __init__(self, report_status_uid: str, report_status_name: str, custom_attributes: str = "{}"):
        self.report_status_uid = report_status_uid
        self.report_status_name = report_status_name
        self.custom_attributes = custom_attributes
    @classmethod
    def empty_write(cls):
        return cls("", "")
    @classmethod
    def default_write(cls):
        return cls(base_dto.get_random_uid(), "")
    @classmethod
    def random_write(cls):
        return cls(base_dto.get_random_uid(), base_dto.get_random_uid())
    @classmethod
    def new_write(cls, report_status_uid: str, report_status_name: str):
        return cls(report_status_uid, report_status_name)
    @classmethod
    def new_write_with_defaults(cls, report_status_uid: str = "", report_status_name: str = ""):
        return cls(report_status_uid, report_status_name)
    @classmethod
    def new_write_random_uid(cls, report_status_name: str):
        return cls(base_dto.get_random_uid(), report_status_name)
    @classmethod
    def get_class_model(cls) -> base_model:
        return db_models.report_status_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["report_status_uid"], d["report_status_name"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return report_status_write_dto(self.report_status_uid, self.report_status_name, self.custom_attributes)
    def clone_write_new_uid(self):
        return report_status_write_dto(base_dto.get_random_uid(), self.report_status_name, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return report_status_write_dto(uid, self.report_status_name, self.custom_attributes)
    def get_model(self) -> base_model:
        return db_models.report_status_model
    def get_uid(self) -> str:
        return self.report_status_uid
    def get_name(self) -> str:
        return self.report_status_name
    def get_list_values(self) -> list[any]:
        return [self.report_status_uid, self.report_status_name, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.report_status_uid, self.report_status_name]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.report_status_name, self.custom_attributes, updated_by, self.report_status_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.report_status_uid, self.report_status_name, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.report_status_name]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.report_status_name, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_uid() == obj.get_uid()
    def update_uid(self, uid: str):
        self.report_status_uid = uid
    def update_uid_attributes(self, report_status_uid: str, report_status_name: str):
        self.report_status_uid = report_status_uid
        self.report_status_name = report_status_name
    def update_attributes(self, report_status_name: str):
        self.report_status_name = report_status_name


@dataclass(frozen=False)
class report_type_write_dto(base_write_dto):
    report_type_uid: str
    report_type_name: str
    def __init__(self, report_type_uid: str, report_type_name: str, custom_attributes: str = "{}"):
        self.report_type_uid = report_type_uid
        self.report_type_name = report_type_name
        self.custom_attributes = custom_attributes
    @classmethod
    def empty_write(cls):
        return cls("", "")
    @classmethod
    def default_write(cls):
        return cls(base_dto.get_random_uid(), "")
    @classmethod
    def random_write(cls):
        return cls(base_dto.get_random_uid(), base_dto.get_random_uid())
    @classmethod
    def new_write(cls, report_type_uid: str, report_type_name: str):
        return cls(report_type_uid, report_type_name)
    @classmethod
    def new_write_with_defaults(cls, report_type_uid: str = "", report_type_name: str = ""):
        return cls(report_type_uid, report_type_name)
    @classmethod
    def new_write_random_uid(cls, report_type_name: str):
        return cls(base_dto.get_random_uid(), report_type_name)
    @classmethod
    def get_class_model(cls) -> base_model:
        return db_models.report_type_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["report_type_uid"], d["report_type_name"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return report_type_write_dto(self.report_type_uid, self.report_type_name, self.custom_attributes)
    def clone_write_new_uid(self):
        return report_type_write_dto(base_dto.get_random_uid(), self.report_type_name, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return report_type_write_dto(uid, self.report_type_name, self.custom_attributes)
    def get_model(self) -> base_model:
        return db_models.report_type_model
    def get_uid(self) -> str:
        return self.report_type_uid
    def get_name(self) -> str:
        return self.report_type_name
    def get_list_values(self) -> list[any]:
        return [self.report_type_uid, self.report_type_name, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.report_type_uid, self.report_type_name]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.report_type_name, self.custom_attributes, updated_by, self.report_type_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.report_type_uid, self.report_type_name, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.report_type_name]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.report_type_name, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_uid() == obj.get_uid()
    def update_uid(self, uid: str):
        self.report_type_uid = uid
    def update_uid_attributes(self, report_type_uid: str, report_type_name: str):
        self.report_type_uid = report_type_uid
        self.report_type_name = report_type_name
    def update_attributes(self, report_type_name: str):
        self.report_type_name = report_type_name


@dataclass(frozen=False)
class storage_write_dto(base_write_dto):
    storage_uid: str
    storage_name: str
    tenant_uid: str
    account_uid: str
    storage_type_uid: str
    storage_category_uid: str
    storage_parameters_json: str
    def __init__(self, storage_uid: str, storage_name: str, tenant_uid: str, account_uid: str, storage_type_uid: str, storage_category_uid: str, storage_parameters_json: str, custom_attributes: str = "{}"):
        self.storage_uid = storage_uid
        self.storage_name = storage_name
        self.tenant_uid = tenant_uid
        self.account_uid = account_uid
        self.storage_type_uid = storage_type_uid
        self.storage_category_uid = storage_category_uid
        self.storage_parameters_json = storage_parameters_json
        self.custom_attributes = custom_attributes
    @classmethod
    def empty_write(cls):
        return cls("", "", "", "", "", "", "")
    @classmethod
    def default_write(cls):
        return cls(base_dto.get_random_uid(), "", "", "", "", "", "")
    @classmethod
    def random_write(cls):
        return cls(base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid())
    @classmethod
    def new_write(cls, storage_uid: str, storage_name: str, tenant_uid: str, account_uid: str, storage_type_uid: str, storage_category_uid: str, storage_parameters_json: str):
        return cls(storage_uid, storage_name, tenant_uid, account_uid, storage_type_uid, storage_category_uid, storage_parameters_json)
    @classmethod
    def new_write_with_defaults(cls, storage_uid: str = "", storage_name: str = "", tenant_uid: str = "", account_uid: str = "", storage_type_uid: str = "", storage_category_uid: str = "", storage_parameters_json: str = ""):
        return cls(storage_uid, storage_name, tenant_uid, account_uid, storage_type_uid, storage_category_uid, storage_parameters_json)
    @classmethod
    def new_write_random_uid(cls, storage_name: str, tenant_uid: str, account_uid: str, storage_type_uid: str, storage_category_uid: str, storage_parameters_json: str):
        return cls(base_dto.get_random_uid(), storage_name, tenant_uid, account_uid, storage_type_uid, storage_category_uid, storage_parameters_json)
    @classmethod
    def get_class_model(cls) -> base_model:
        return db_models.storage_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["storage_uid"], d["storage_name"], d["tenant_uid"], d["account_uid"], d["storage_type_uid"], d["storage_category_uid"], d["storage_parameters_json"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return storage_write_dto(self.storage_uid, self.storage_name, self.tenant_uid, self.account_uid, self.storage_type_uid, self.storage_category_uid, self.storage_parameters_json, self.custom_attributes)
    def clone_write_new_uid(self):
        return storage_write_dto(base_dto.get_random_uid(), self.storage_name, self.tenant_uid, self.account_uid, self.storage_type_uid, self.storage_category_uid, self.storage_parameters_json, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return storage_write_dto(uid, self.storage_name, self.tenant_uid, self.account_uid, self.storage_type_uid, self.storage_category_uid, self.storage_parameters_json, self.custom_attributes)
    def get_model(self) -> base_model:
        return db_models.storage_model
    def get_uid(self) -> str:
        return self.storage_uid
    def get_name(self) -> str:
        return self.storage_name
    def get_list_values(self) -> list[any]:
        return [self.storage_uid, self.storage_name, self.tenant_uid, self.account_uid, self.storage_type_uid, self.storage_category_uid, self.storage_parameters_json, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.storage_uid, self.storage_name, self.tenant_uid, self.account_uid, self.storage_type_uid, self.storage_category_uid, self.storage_parameters_json]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.storage_name, self.tenant_uid, self.account_uid, self.storage_type_uid, self.storage_category_uid, self.storage_parameters_json, self.custom_attributes, updated_by, self.storage_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.storage_uid, self.storage_name, self.tenant_uid, self.account_uid, self.storage_type_uid, self.storage_category_uid, self.storage_parameters_json, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.storage_name, self.tenant_uid, self.account_uid, self.storage_type_uid, self.storage_category_uid, self.storage_parameters_json]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.storage_name, self.tenant_uid, self.account_uid, self.storage_type_uid, self.storage_category_uid, self.storage_parameters_json, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_uid() == obj.get_uid()
    def update_uid(self, uid: str):
        self.storage_uid = uid
    def update_uid_attributes(self, storage_uid: str, storage_name: str, tenant_uid: str, account_uid: str, storage_type_uid: str, storage_category_uid: str, storage_parameters_json: str):
        self.storage_uid = storage_uid
        self.storage_name = storage_name
        self.tenant_uid = tenant_uid
        self.account_uid = account_uid
        self.storage_type_uid = storage_type_uid
        self.storage_category_uid = storage_category_uid
        self.storage_parameters_json = storage_parameters_json
    def update_attributes(self, storage_name: str, tenant_uid: str, account_uid: str, storage_type_uid: str, storage_category_uid: str, storage_parameters_json: str):
        self.storage_name = storage_name
        self.tenant_uid = tenant_uid
        self.account_uid = account_uid
        self.storage_type_uid = storage_type_uid
        self.storage_category_uid = storage_category_uid
        self.storage_parameters_json = storage_parameters_json


@dataclass(frozen=False)
class storage_category_write_dto(base_write_dto):
    storage_category_uid: str
    storage_category_name: str
    def __init__(self, storage_category_uid: str, storage_category_name: str, custom_attributes: str = "{}"):
        self.storage_category_uid = storage_category_uid
        self.storage_category_name = storage_category_name
        self.custom_attributes = custom_attributes
    @classmethod
    def empty_write(cls):
        return cls("", "")
    @classmethod
    def default_write(cls):
        return cls(base_dto.get_random_uid(), "")
    @classmethod
    def random_write(cls):
        return cls(base_dto.get_random_uid(), base_dto.get_random_uid())
    @classmethod
    def new_write(cls, storage_category_uid: str, storage_category_name: str):
        return cls(storage_category_uid, storage_category_name)
    @classmethod
    def new_write_with_defaults(cls, storage_category_uid: str = "", storage_category_name: str = ""):
        return cls(storage_category_uid, storage_category_name)
    @classmethod
    def new_write_random_uid(cls, storage_category_name: str):
        return cls(base_dto.get_random_uid(), storage_category_name)
    @classmethod
    def get_class_model(cls) -> base_model:
        return db_models.storage_category_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["storage_category_uid"], d["storage_category_name"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return storage_category_write_dto(self.storage_category_uid, self.storage_category_name, self.custom_attributes)
    def clone_write_new_uid(self):
        return storage_category_write_dto(base_dto.get_random_uid(), self.storage_category_name, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return storage_category_write_dto(uid, self.storage_category_name, self.custom_attributes)
    def get_model(self) -> base_model:
        return db_models.storage_category_model
    def get_uid(self) -> str:
        return self.storage_category_uid
    def get_name(self) -> str:
        return self.storage_category_name
    def get_list_values(self) -> list[any]:
        return [self.storage_category_uid, self.storage_category_name, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.storage_category_uid, self.storage_category_name]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.storage_category_name, self.custom_attributes, updated_by, self.storage_category_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.storage_category_uid, self.storage_category_name, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.storage_category_name]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.storage_category_name, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_uid() == obj.get_uid()
    def update_uid(self, uid: str):
        self.storage_category_uid = uid
    def update_uid_attributes(self, storage_category_uid: str, storage_category_name: str):
        self.storage_category_uid = storage_category_uid
        self.storage_category_name = storage_category_name
    def update_attributes(self, storage_category_name: str):
        self.storage_category_name = storage_category_name


@dataclass(frozen=False)
class storage_connection_write_dto(base_write_dto):
    storage_connection_uid: str
    storage_connection_name: str
    storage_uid: str
    connection_type: str
    storage_parameters_json: str
    def __init__(self, storage_connection_uid: str, storage_connection_name: str, storage_uid: str, connection_type: str, storage_parameters_json: str, custom_attributes: str = "{}"):
        self.storage_connection_uid = storage_connection_uid
        self.storage_connection_name = storage_connection_name
        self.storage_uid = storage_uid
        self.connection_type = connection_type
        self.storage_parameters_json = storage_parameters_json
        self.custom_attributes = custom_attributes
    @classmethod
    def empty_write(cls):
        return cls("", "", "", "", "")
    @classmethod
    def default_write(cls):
        return cls(base_dto.get_random_uid(), "", "", "", "")
    @classmethod
    def random_write(cls):
        return cls(base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid())
    @classmethod
    def new_write(cls, storage_connection_uid: str, storage_connection_name: str, storage_uid: str, connection_type: str, storage_parameters_json: str):
        return cls(storage_connection_uid, storage_connection_name, storage_uid, connection_type, storage_parameters_json)
    @classmethod
    def new_write_with_defaults(cls, storage_connection_uid: str = "", storage_connection_name: str = "", storage_uid: str = "", connection_type: str = "", storage_parameters_json: str = ""):
        return cls(storage_connection_uid, storage_connection_name, storage_uid, connection_type, storage_parameters_json)
    @classmethod
    def new_write_random_uid(cls, storage_connection_name: str, storage_uid: str, connection_type: str, storage_parameters_json: str):
        return cls(base_dto.get_random_uid(), storage_connection_name, storage_uid, connection_type, storage_parameters_json)
    @classmethod
    def get_class_model(cls) -> base_model:
        return db_models.storage_connection_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["storage_connection_uid"], d["storage_connection_name"], d["storage_uid"], d["connection_type"], d["storage_parameters_json"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return storage_connection_write_dto(self.storage_connection_uid, self.storage_connection_name, self.storage_uid, self.connection_type, self.storage_parameters_json, self.custom_attributes)
    def clone_write_new_uid(self):
        return storage_connection_write_dto(base_dto.get_random_uid(), self.storage_connection_name, self.storage_uid, self.connection_type, self.storage_parameters_json, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return storage_connection_write_dto(uid, self.storage_connection_name, self.storage_uid, self.connection_type, self.storage_parameters_json, self.custom_attributes)
    def get_model(self) -> base_model:
        return db_models.storage_connection_model
    def get_uid(self) -> str:
        return self.storage_connection_uid
    def get_name(self) -> str:
        return self.storage_connection_name
    def get_list_values(self) -> list[any]:
        return [self.storage_connection_uid, self.storage_connection_name, self.storage_uid, self.connection_type, self.storage_parameters_json, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.storage_connection_uid, self.storage_connection_name, self.storage_uid, self.connection_type, self.storage_parameters_json]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.storage_connection_name, self.storage_uid, self.connection_type, self.storage_parameters_json, self.custom_attributes, updated_by, self.storage_connection_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.storage_connection_uid, self.storage_connection_name, self.storage_uid, self.connection_type, self.storage_parameters_json, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.storage_connection_name, self.storage_uid, self.connection_type, self.storage_parameters_json]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.storage_connection_name, self.storage_uid, self.connection_type, self.storage_parameters_json, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_uid() == obj.get_uid()
    def update_uid(self, uid: str):
        self.storage_connection_uid = uid
    def update_uid_attributes(self, storage_connection_uid: str, storage_connection_name: str, storage_uid: str, connection_type: str, storage_parameters_json: str):
        self.storage_connection_uid = storage_connection_uid
        self.storage_connection_name = storage_connection_name
        self.storage_uid = storage_uid
        self.connection_type = connection_type
        self.storage_parameters_json = storage_parameters_json
    def update_attributes(self, storage_connection_name: str, storage_uid: str, connection_type: str, storage_parameters_json: str):
        self.storage_connection_name = storage_connection_name
        self.storage_uid = storage_uid
        self.connection_type = connection_type
        self.storage_parameters_json = storage_parameters_json


@dataclass(frozen=False)
class storage_query_write_dto(base_write_dto):
    storage_query_uid: str
    storage_query_name: str
    storage_uid: str
    query_content: str
    query_parameters_json: str
    execution_status: str
    execution_time: int | None
    execution_rows: int | None
    def __init__(self, storage_query_uid: str, storage_query_name: str, storage_uid: str, query_content: str, query_parameters_json: str, execution_status: str, execution_time: int | None, execution_rows: int | None, custom_attributes: str = "{}"):
        self.storage_query_uid = storage_query_uid
        self.storage_query_name = storage_query_name
        self.storage_uid = storage_uid
        self.query_content = query_content
        self.query_parameters_json = query_parameters_json
        self.execution_status = execution_status
        self.execution_time = execution_time
        self.execution_rows = execution_rows
        self.custom_attributes = custom_attributes
    @classmethod
    def empty_write(cls):
        return cls("", "", "", "", "", "", 0, 0)
    @classmethod
    def default_write(cls):
        return cls(base_dto.get_random_uid(), "", "", "", "", "", 0, 0)
    @classmethod
    def random_write(cls):
        return cls(base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), 0, 0)
    @classmethod
    def new_write(cls, storage_query_uid: str, storage_query_name: str, storage_uid: str, query_content: str, query_parameters_json: str, execution_status: str, execution_time: int | None, execution_rows: int | None):
        return cls(storage_query_uid, storage_query_name, storage_uid, query_content, query_parameters_json, execution_status, execution_time, execution_rows)
    @classmethod
    def new_write_with_defaults(cls, storage_query_uid: str = "", storage_query_name: str = "", storage_uid: str = "", query_content: str = "", query_parameters_json: str = "", execution_status: str = "", execution_time: int | None = 0, execution_rows: int | None = 0):
        return cls(storage_query_uid, storage_query_name, storage_uid, query_content, query_parameters_json, execution_status, execution_time, execution_rows)
    @classmethod
    def new_write_random_uid(cls, storage_query_name: str, storage_uid: str, query_content: str, query_parameters_json: str, execution_status: str, execution_time: int | None, execution_rows: int | None):
        return cls(base_dto.get_random_uid(), storage_query_name, storage_uid, query_content, query_parameters_json, execution_status, execution_time, execution_rows)
    @classmethod
    def get_class_model(cls) -> base_model:
        return db_models.storage_query_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["storage_query_uid"], d["storage_query_name"], d["storage_uid"], d["query_content"], d["query_parameters_json"], d["execution_status"], d["execution_time"], d["execution_rows"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return storage_query_write_dto(self.storage_query_uid, self.storage_query_name, self.storage_uid, self.query_content, self.query_parameters_json, self.execution_status, self.execution_time, self.execution_rows, self.custom_attributes)
    def clone_write_new_uid(self):
        return storage_query_write_dto(base_dto.get_random_uid(), self.storage_query_name, self.storage_uid, self.query_content, self.query_parameters_json, self.execution_status, self.execution_time, self.execution_rows, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return storage_query_write_dto(uid, self.storage_query_name, self.storage_uid, self.query_content, self.query_parameters_json, self.execution_status, self.execution_time, self.execution_rows, self.custom_attributes)
    def get_model(self) -> base_model:
        return db_models.storage_query_model
    def get_uid(self) -> str:
        return self.storage_query_uid
    def get_name(self) -> str:
        return self.storage_query_name
    def get_list_values(self) -> list[any]:
        return [self.storage_query_uid, self.storage_query_name, self.storage_uid, self.query_content, self.query_parameters_json, self.execution_status, self.execution_time, self.execution_rows, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.storage_query_uid, self.storage_query_name, self.storage_uid, self.query_content, self.query_parameters_json, self.execution_status, self.execution_time, self.execution_rows]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.storage_query_name, self.storage_uid, self.query_content, self.query_parameters_json, self.execution_status, self.execution_time, self.execution_rows, self.custom_attributes, updated_by, self.storage_query_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.storage_query_uid, self.storage_query_name, self.storage_uid, self.query_content, self.query_parameters_json, self.execution_status, self.execution_time, self.execution_rows, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.storage_query_name, self.storage_uid, self.query_content, self.query_parameters_json, self.execution_status, self.execution_time, self.execution_rows]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.storage_query_name, self.storage_uid, self.query_content, self.query_parameters_json, self.execution_status, self.execution_time, self.execution_rows, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_uid() == obj.get_uid()
    def update_uid(self, uid: str):
        self.storage_query_uid = uid
    def update_uid_attributes(self, storage_query_uid: str, storage_query_name: str, storage_uid: str, query_content: str, query_parameters_json: str, execution_status: str, execution_time: int | None, execution_rows: int | None):
        self.storage_query_uid = storage_query_uid
        self.storage_query_name = storage_query_name
        self.storage_uid = storage_uid
        self.query_content = query_content
        self.query_parameters_json = query_parameters_json
        self.execution_status = execution_status
        self.execution_time = execution_time
        self.execution_rows = execution_rows
    def update_attributes(self, storage_query_name: str, storage_uid: str, query_content: str, query_parameters_json: str, execution_status: str, execution_time: int | None, execution_rows: int | None):
        self.storage_query_name = storage_query_name
        self.storage_uid = storage_uid
        self.query_content = query_content
        self.query_parameters_json = query_parameters_json
        self.execution_status = execution_status
        self.execution_time = execution_time
        self.execution_rows = execution_rows


@dataclass(frozen=False)
class storage_type_write_dto(base_write_dto):
    storage_type_uid: str
    storage_type_name: str
    storage_class: str
    def __init__(self, storage_type_uid: str, storage_type_name: str, storage_class: str, custom_attributes: str = "{}"):
        self.storage_type_uid = storage_type_uid
        self.storage_type_name = storage_type_name
        self.storage_class = storage_class
        self.custom_attributes = custom_attributes
    @classmethod
    def empty_write(cls):
        return cls("", "", "")
    @classmethod
    def default_write(cls):
        return cls(base_dto.get_random_uid(), "", "")
    @classmethod
    def random_write(cls):
        return cls(base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid())
    @classmethod
    def new_write(cls, storage_type_uid: str, storage_type_name: str, storage_class: str):
        return cls(storage_type_uid, storage_type_name, storage_class)
    @classmethod
    def new_write_with_defaults(cls, storage_type_uid: str = "", storage_type_name: str = "", storage_class: str = ""):
        return cls(storage_type_uid, storage_type_name, storage_class)
    @classmethod
    def new_write_random_uid(cls, storage_type_name: str, storage_class: str):
        return cls(base_dto.get_random_uid(), storage_type_name, storage_class)
    @classmethod
    def get_class_model(cls) -> base_model:
        return db_models.storage_type_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["storage_type_uid"], d["storage_type_name"], d["storage_class"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return storage_type_write_dto(self.storage_type_uid, self.storage_type_name, self.storage_class, self.custom_attributes)
    def clone_write_new_uid(self):
        return storage_type_write_dto(base_dto.get_random_uid(), self.storage_type_name, self.storage_class, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return storage_type_write_dto(uid, self.storage_type_name, self.storage_class, self.custom_attributes)
    def get_model(self) -> base_model:
        return db_models.storage_type_model
    def get_uid(self) -> str:
        return self.storage_type_uid
    def get_name(self) -> str:
        return self.storage_type_name
    def get_list_values(self) -> list[any]:
        return [self.storage_type_uid, self.storage_type_name, self.storage_class, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.storage_type_uid, self.storage_type_name, self.storage_class]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.storage_type_name, self.storage_class, self.custom_attributes, updated_by, self.storage_type_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.storage_type_uid, self.storage_type_name, self.storage_class, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.storage_type_name, self.storage_class]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.storage_type_name, self.storage_class, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_uid() == obj.get_uid()
    def update_uid(self, uid: str):
        self.storage_type_uid = uid
    def update_uid_attributes(self, storage_type_uid: str, storage_type_name: str, storage_class: str):
        self.storage_type_uid = storage_type_uid
        self.storage_type_name = storage_type_name
        self.storage_class = storage_class
    def update_attributes(self, storage_type_name: str, storage_class: str):
        self.storage_type_name = storage_type_name
        self.storage_class = storage_class


@dataclass(frozen=False)
class synchronization_write_dto(base_write_dto):
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
    def __init__(self, synchronization_uid: str, synchronization_name: str, tenant_uid: str, synchronization_type_uid: str, storage_uid: str, sync_expression: str, sync_query: str, sync_definition: str, sync_priority: int, last_run_date: datetime.datetime | None, last_run_seconds: str | None, custom_attributes: str = "{}"):
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
        self.custom_attributes = custom_attributes
    @classmethod
    def empty_write(cls):
        return cls("", "", "", "", "", "", "", "", 0, datetime.datetime.now(), "")
    @classmethod
    def default_write(cls):
        return cls(base_dto.get_random_uid(), "", "", "", "", "", "", "", 0, datetime.datetime.now(), "")
    @classmethod
    def random_write(cls):
        return cls(base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), 0, datetime.datetime.now(), "")
    @classmethod
    def new_write(cls, synchronization_uid: str, synchronization_name: str, tenant_uid: str, synchronization_type_uid: str, storage_uid: str, sync_expression: str, sync_query: str, sync_definition: str, sync_priority: int, last_run_date: datetime.datetime | None, last_run_seconds: str | None):
        return cls(synchronization_uid, synchronization_name, tenant_uid, synchronization_type_uid, storage_uid, sync_expression, sync_query, sync_definition, sync_priority, last_run_date, last_run_seconds)
    @classmethod
    def new_write_with_defaults(cls, synchronization_uid: str = "", synchronization_name: str = "", tenant_uid: str = "", synchronization_type_uid: str = "", storage_uid: str = "", sync_expression: str = "", sync_query: str = "", sync_definition: str = "", sync_priority: int = 0, last_run_date: datetime.datetime | None = datetime.datetime.now(), last_run_seconds: str | None = ""):
        return cls(synchronization_uid, synchronization_name, tenant_uid, synchronization_type_uid, storage_uid, sync_expression, sync_query, sync_definition, sync_priority, last_run_date, last_run_seconds)
    @classmethod
    def new_write_random_uid(cls, synchronization_name: str, tenant_uid: str, synchronization_type_uid: str, storage_uid: str, sync_expression: str, sync_query: str, sync_definition: str, sync_priority: int, last_run_date: datetime.datetime | None, last_run_seconds: str | None):
        return cls(base_dto.get_random_uid(), synchronization_name, tenant_uid, synchronization_type_uid, storage_uid, sync_expression, sync_query, sync_definition, sync_priority, last_run_date, last_run_seconds)
    @classmethod
    def get_class_model(cls) -> base_model:
        return db_models.synchronization_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["synchronization_uid"], d["synchronization_name"], d["tenant_uid"], d["synchronization_type_uid"], d["storage_uid"], d["sync_expression"], d["sync_query"], d["sync_definition"], d["sync_priority"], d["last_run_date"], d["last_run_seconds"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return synchronization_write_dto(self.synchronization_uid, self.synchronization_name, self.tenant_uid, self.synchronization_type_uid, self.storage_uid, self.sync_expression, self.sync_query, self.sync_definition, self.sync_priority, self.last_run_date, self.last_run_seconds, self.custom_attributes)
    def clone_write_new_uid(self):
        return synchronization_write_dto(base_dto.get_random_uid(), self.synchronization_name, self.tenant_uid, self.synchronization_type_uid, self.storage_uid, self.sync_expression, self.sync_query, self.sync_definition, self.sync_priority, self.last_run_date, self.last_run_seconds, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return synchronization_write_dto(uid, self.synchronization_name, self.tenant_uid, self.synchronization_type_uid, self.storage_uid, self.sync_expression, self.sync_query, self.sync_definition, self.sync_priority, self.last_run_date, self.last_run_seconds, self.custom_attributes)
    def get_model(self) -> base_model:
        return db_models.synchronization_model
    def get_uid(self) -> str:
        return self.synchronization_uid
    def get_name(self) -> str:
        return self.synchronization_name
    def get_list_values(self) -> list[any]:
        return [self.synchronization_uid, self.synchronization_name, self.tenant_uid, self.synchronization_type_uid, self.storage_uid, self.sync_expression, self.sync_query, self.sync_definition, self.sync_priority, self.last_run_date, self.last_run_seconds, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.synchronization_uid, self.synchronization_name, self.tenant_uid, self.synchronization_type_uid, self.storage_uid, self.sync_expression, self.sync_query, self.sync_definition, self.sync_priority, self.last_run_date, self.last_run_seconds]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.synchronization_name, self.tenant_uid, self.synchronization_type_uid, self.storage_uid, self.sync_expression, self.sync_query, self.sync_definition, self.sync_priority, self.last_run_date, self.last_run_seconds, self.custom_attributes, updated_by, self.synchronization_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.synchronization_uid, self.synchronization_name, self.tenant_uid, self.synchronization_type_uid, self.storage_uid, self.sync_expression, self.sync_query, self.sync_definition, self.sync_priority, self.last_run_date, self.last_run_seconds, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.synchronization_name, self.tenant_uid, self.synchronization_type_uid, self.storage_uid, self.sync_expression, self.sync_query, self.sync_definition, self.sync_priority, self.last_run_date, self.last_run_seconds]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.synchronization_name, self.tenant_uid, self.synchronization_type_uid, self.storage_uid, self.sync_expression, self.sync_query, self.sync_definition, self.sync_priority, self.last_run_date, self.last_run_seconds, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_uid() == obj.get_uid()
    def update_uid(self, uid: str):
        self.synchronization_uid = uid
    def update_uid_attributes(self, synchronization_uid: str, synchronization_name: str, tenant_uid: str, synchronization_type_uid: str, storage_uid: str, sync_expression: str, sync_query: str, sync_definition: str, sync_priority: int, last_run_date: datetime.datetime | None, last_run_seconds: str | None):
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
    def update_attributes(self, synchronization_name: str, tenant_uid: str, synchronization_type_uid: str, storage_uid: str, sync_expression: str, sync_query: str, sync_definition: str, sync_priority: int, last_run_date: datetime.datetime | None, last_run_seconds: str | None):
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


@dataclass(frozen=False)
class synchronization_run_write_dto(base_write_dto):
    synchronization_run_uid: str
    synchronization_run_name: str
    synchronization_uid: str
    run_status: str
    run_time_seconds: str
    copied_items: int
    def __init__(self, synchronization_run_uid: str, synchronization_run_name: str, synchronization_uid: str, run_status: str, run_time_seconds: str, copied_items: int, custom_attributes: str = "{}"):
        self.synchronization_run_uid = synchronization_run_uid
        self.synchronization_run_name = synchronization_run_name
        self.synchronization_uid = synchronization_uid
        self.run_status = run_status
        self.run_time_seconds = run_time_seconds
        self.copied_items = copied_items
        self.custom_attributes = custom_attributes
    @classmethod
    def empty_write(cls):
        return cls("", "", "", "", "", 0)
    @classmethod
    def default_write(cls):
        return cls(base_dto.get_random_uid(), "", "", "", "", 0)
    @classmethod
    def random_write(cls):
        return cls(base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), "", 0)
    @classmethod
    def new_write(cls, synchronization_run_uid: str, synchronization_run_name: str, synchronization_uid: str, run_status: str, run_time_seconds: str, copied_items: int):
        return cls(synchronization_run_uid, synchronization_run_name, synchronization_uid, run_status, run_time_seconds, copied_items)
    @classmethod
    def new_write_with_defaults(cls, synchronization_run_uid: str = "", synchronization_run_name: str = "", synchronization_uid: str = "", run_status: str = "", run_time_seconds: str = "", copied_items: int = 0):
        return cls(synchronization_run_uid, synchronization_run_name, synchronization_uid, run_status, run_time_seconds, copied_items)
    @classmethod
    def new_write_random_uid(cls, synchronization_run_name: str, synchronization_uid: str, run_status: str, run_time_seconds: str, copied_items: int):
        return cls(base_dto.get_random_uid(), synchronization_run_name, synchronization_uid, run_status, run_time_seconds, copied_items)
    @classmethod
    def get_class_model(cls) -> base_model:
        return db_models.synchronization_run_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["synchronization_run_uid"], d["synchronization_run_name"], d["synchronization_uid"], d["run_status"], d["run_time_seconds"], d["copied_items"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return synchronization_run_write_dto(self.synchronization_run_uid, self.synchronization_run_name, self.synchronization_uid, self.run_status, self.run_time_seconds, self.copied_items, self.custom_attributes)
    def clone_write_new_uid(self):
        return synchronization_run_write_dto(base_dto.get_random_uid(), self.synchronization_run_name, self.synchronization_uid, self.run_status, self.run_time_seconds, self.copied_items, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return synchronization_run_write_dto(uid, self.synchronization_run_name, self.synchronization_uid, self.run_status, self.run_time_seconds, self.copied_items, self.custom_attributes)
    def get_model(self) -> base_model:
        return db_models.synchronization_run_model
    def get_uid(self) -> str:
        return self.synchronization_run_uid
    def get_name(self) -> str:
        return self.synchronization_run_name
    def get_list_values(self) -> list[any]:
        return [self.synchronization_run_uid, self.synchronization_run_name, self.synchronization_uid, self.run_status, self.run_time_seconds, self.copied_items, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.synchronization_run_uid, self.synchronization_run_name, self.synchronization_uid, self.run_status, self.run_time_seconds, self.copied_items]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.synchronization_run_name, self.synchronization_uid, self.run_status, self.run_time_seconds, self.copied_items, self.custom_attributes, updated_by, self.synchronization_run_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.synchronization_run_uid, self.synchronization_run_name, self.synchronization_uid, self.run_status, self.run_time_seconds, self.copied_items, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.synchronization_run_name, self.synchronization_uid, self.run_status, self.run_time_seconds, self.copied_items]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.synchronization_run_name, self.synchronization_uid, self.run_status, self.run_time_seconds, self.copied_items, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_uid() == obj.get_uid()
    def update_uid(self, uid: str):
        self.synchronization_run_uid = uid
    def update_uid_attributes(self, synchronization_run_uid: str, synchronization_run_name: str, synchronization_uid: str, run_status: str, run_time_seconds: str, copied_items: int):
        self.synchronization_run_uid = synchronization_run_uid
        self.synchronization_run_name = synchronization_run_name
        self.synchronization_uid = synchronization_uid
        self.run_status = run_status
        self.run_time_seconds = run_time_seconds
        self.copied_items = copied_items
    def update_attributes(self, synchronization_run_name: str, synchronization_uid: str, run_status: str, run_time_seconds: str, copied_items: int):
        self.synchronization_run_name = synchronization_run_name
        self.synchronization_uid = synchronization_uid
        self.run_status = run_status
        self.run_time_seconds = run_time_seconds
        self.copied_items = copied_items


@dataclass(frozen=False)
class synchronization_type_write_dto(base_write_dto):
    synchronization_type_uid: str
    synchronization_type_name: str
    sync_type: str
    sync_class_name: str
    def __init__(self, synchronization_type_uid: str, synchronization_type_name: str, sync_type: str, sync_class_name: str, custom_attributes: str = "{}"):
        self.synchronization_type_uid = synchronization_type_uid
        self.synchronization_type_name = synchronization_type_name
        self.sync_type = sync_type
        self.sync_class_name = sync_class_name
        self.custom_attributes = custom_attributes
    @classmethod
    def empty_write(cls):
        return cls("", "", "", "")
    @classmethod
    def default_write(cls):
        return cls(base_dto.get_random_uid(), "", "", "")
    @classmethod
    def random_write(cls):
        return cls(base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid())
    @classmethod
    def new_write(cls, synchronization_type_uid: str, synchronization_type_name: str, sync_type: str, sync_class_name: str):
        return cls(synchronization_type_uid, synchronization_type_name, sync_type, sync_class_name)
    @classmethod
    def new_write_with_defaults(cls, synchronization_type_uid: str = "", synchronization_type_name: str = "", sync_type: str = "", sync_class_name: str = ""):
        return cls(synchronization_type_uid, synchronization_type_name, sync_type, sync_class_name)
    @classmethod
    def new_write_random_uid(cls, synchronization_type_name: str, sync_type: str, sync_class_name: str):
        return cls(base_dto.get_random_uid(), synchronization_type_name, sync_type, sync_class_name)
    @classmethod
    def get_class_model(cls) -> base_model:
        return db_models.synchronization_type_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["synchronization_type_uid"], d["synchronization_type_name"], d["sync_type"], d["sync_class_name"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return synchronization_type_write_dto(self.synchronization_type_uid, self.synchronization_type_name, self.sync_type, self.sync_class_name, self.custom_attributes)
    def clone_write_new_uid(self):
        return synchronization_type_write_dto(base_dto.get_random_uid(), self.synchronization_type_name, self.sync_type, self.sync_class_name, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return synchronization_type_write_dto(uid, self.synchronization_type_name, self.sync_type, self.sync_class_name, self.custom_attributes)
    def get_model(self) -> base_model:
        return db_models.synchronization_type_model
    def get_uid(self) -> str:
        return self.synchronization_type_uid
    def get_name(self) -> str:
        return self.synchronization_type_name
    def get_list_values(self) -> list[any]:
        return [self.synchronization_type_uid, self.synchronization_type_name, self.sync_type, self.sync_class_name, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.synchronization_type_uid, self.synchronization_type_name, self.sync_type, self.sync_class_name]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.synchronization_type_name, self.sync_type, self.sync_class_name, self.custom_attributes, updated_by, self.synchronization_type_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.synchronization_type_uid, self.synchronization_type_name, self.sync_type, self.sync_class_name, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.synchronization_type_name, self.sync_type, self.sync_class_name]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.synchronization_type_name, self.sync_type, self.sync_class_name, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_uid() == obj.get_uid()
    def update_uid(self, uid: str):
        self.synchronization_type_uid = uid
    def update_uid_attributes(self, synchronization_type_uid: str, synchronization_type_name: str, sync_type: str, sync_class_name: str):
        self.synchronization_type_uid = synchronization_type_uid
        self.synchronization_type_name = synchronization_type_name
        self.sync_type = sync_type
        self.sync_class_name = sync_class_name
    def update_attributes(self, synchronization_type_name: str, sync_type: str, sync_class_name: str):
        self.synchronization_type_name = synchronization_type_name
        self.sync_type = sync_type
        self.sync_class_name = sync_class_name


@dataclass(frozen=False)
class system_attribute_write_dto(base_write_dto):
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
    def __init__(self, system_attribute_uid: str, system_attribute_name: str, system_table_uid: str, column_name: str, attribute_type: str, attribute_category: str, attribute_label: str, attribute_description: str, ordinal_position: int, is_hidden: int, is_meta: int, is_secret: int, is_full_search: int, custom_attributes: str = "{}"):
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
        self.custom_attributes = custom_attributes
    @classmethod
    def empty_write(cls):
        return cls("", "", "", "", "", "", "", "", 0, 0, 0, 0, 0)
    @classmethod
    def default_write(cls):
        return cls(base_dto.get_random_uid(), "", "", "", "", "", "", "", 0, 0, 0, 0, 0)
    @classmethod
    def random_write(cls):
        return cls(base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), 0, 0, 0, 0, 0)
    @classmethod
    def new_write(cls, system_attribute_uid: str, system_attribute_name: str, system_table_uid: str, column_name: str, attribute_type: str, attribute_category: str, attribute_label: str, attribute_description: str, ordinal_position: int, is_hidden: int, is_meta: int, is_secret: int, is_full_search: int):
        return cls(system_attribute_uid, system_attribute_name, system_table_uid, column_name, attribute_type, attribute_category, attribute_label, attribute_description, ordinal_position, is_hidden, is_meta, is_secret, is_full_search)
    @classmethod
    def new_write_with_defaults(cls, system_attribute_uid: str = "", system_attribute_name: str = "", system_table_uid: str = "", column_name: str = "", attribute_type: str = "", attribute_category: str = "", attribute_label: str = "", attribute_description: str = "", ordinal_position: int = 0, is_hidden: int = 0, is_meta: int = 0, is_secret: int = 0, is_full_search: int = 0):
        return cls(system_attribute_uid, system_attribute_name, system_table_uid, column_name, attribute_type, attribute_category, attribute_label, attribute_description, ordinal_position, is_hidden, is_meta, is_secret, is_full_search)
    @classmethod
    def new_write_random_uid(cls, system_attribute_name: str, system_table_uid: str, column_name: str, attribute_type: str, attribute_category: str, attribute_label: str, attribute_description: str, ordinal_position: int, is_hidden: int, is_meta: int, is_secret: int, is_full_search: int):
        return cls(base_dto.get_random_uid(), system_attribute_name, system_table_uid, column_name, attribute_type, attribute_category, attribute_label, attribute_description, ordinal_position, is_hidden, is_meta, is_secret, is_full_search)
    @classmethod
    def get_class_model(cls) -> base_model:
        return db_models.system_attribute_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["system_attribute_uid"], d["system_attribute_name"], d["system_table_uid"], d["column_name"], d["attribute_type"], d["attribute_category"], d["attribute_label"], d["attribute_description"], d["ordinal_position"], d["is_hidden"], d["is_meta"], d["is_secret"], d["is_full_search"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return system_attribute_write_dto(self.system_attribute_uid, self.system_attribute_name, self.system_table_uid, self.column_name, self.attribute_type, self.attribute_category, self.attribute_label, self.attribute_description, self.ordinal_position, self.is_hidden, self.is_meta, self.is_secret, self.is_full_search, self.custom_attributes)
    def clone_write_new_uid(self):
        return system_attribute_write_dto(base_dto.get_random_uid(), self.system_attribute_name, self.system_table_uid, self.column_name, self.attribute_type, self.attribute_category, self.attribute_label, self.attribute_description, self.ordinal_position, self.is_hidden, self.is_meta, self.is_secret, self.is_full_search, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return system_attribute_write_dto(uid, self.system_attribute_name, self.system_table_uid, self.column_name, self.attribute_type, self.attribute_category, self.attribute_label, self.attribute_description, self.ordinal_position, self.is_hidden, self.is_meta, self.is_secret, self.is_full_search, self.custom_attributes)
    def get_model(self) -> base_model:
        return db_models.system_attribute_model
    def get_uid(self) -> str:
        return self.system_attribute_uid
    def get_name(self) -> str:
        return self.system_attribute_name
    def get_list_values(self) -> list[any]:
        return [self.system_attribute_uid, self.system_attribute_name, self.system_table_uid, self.column_name, self.attribute_type, self.attribute_category, self.attribute_label, self.attribute_description, self.ordinal_position, self.is_hidden, self.is_meta, self.is_secret, self.is_full_search, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.system_attribute_uid, self.system_attribute_name, self.system_table_uid, self.column_name, self.attribute_type, self.attribute_category, self.attribute_label, self.attribute_description, self.ordinal_position, self.is_hidden, self.is_meta, self.is_secret, self.is_full_search]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.system_attribute_name, self.system_table_uid, self.column_name, self.attribute_type, self.attribute_category, self.attribute_label, self.attribute_description, self.ordinal_position, self.is_hidden, self.is_meta, self.is_secret, self.is_full_search, self.custom_attributes, updated_by, self.system_attribute_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.system_attribute_uid, self.system_attribute_name, self.system_table_uid, self.column_name, self.attribute_type, self.attribute_category, self.attribute_label, self.attribute_description, self.ordinal_position, self.is_hidden, self.is_meta, self.is_secret, self.is_full_search, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.system_attribute_name, self.system_table_uid, self.column_name, self.attribute_type, self.attribute_category, self.attribute_label, self.attribute_description, self.ordinal_position, self.is_hidden, self.is_meta, self.is_secret, self.is_full_search]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.system_attribute_name, self.system_table_uid, self.column_name, self.attribute_type, self.attribute_category, self.attribute_label, self.attribute_description, self.ordinal_position, self.is_hidden, self.is_meta, self.is_secret, self.is_full_search, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_uid() == obj.get_uid()
    def update_uid(self, uid: str):
        self.system_attribute_uid = uid
    def update_uid_attributes(self, system_attribute_uid: str, system_attribute_name: str, system_table_uid: str, column_name: str, attribute_type: str, attribute_category: str, attribute_label: str, attribute_description: str, ordinal_position: int, is_hidden: int, is_meta: int, is_secret: int, is_full_search: int):
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
    def update_attributes(self, system_attribute_name: str, system_table_uid: str, column_name: str, attribute_type: str, attribute_category: str, attribute_label: str, attribute_description: str, ordinal_position: int, is_hidden: int, is_meta: int, is_secret: int, is_full_search: int):
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


@dataclass(frozen=False)
class system_constraint_write_dto(base_write_dto):
    system_constraint_uid: str
    system_constraint_name: str
    system_table_uid: str
    system_attribute_uid: str
    tenant_uid: str
    constraint_class: str
    constraint_params_json: str
    def __init__(self, system_constraint_uid: str, system_constraint_name: str, system_table_uid: str, system_attribute_uid: str, tenant_uid: str, constraint_class: str, constraint_params_json: str, custom_attributes: str = "{}"):
        self.system_constraint_uid = system_constraint_uid
        self.system_constraint_name = system_constraint_name
        self.system_table_uid = system_table_uid
        self.system_attribute_uid = system_attribute_uid
        self.tenant_uid = tenant_uid
        self.constraint_class = constraint_class
        self.constraint_params_json = constraint_params_json
        self.custom_attributes = custom_attributes
    @classmethod
    def empty_write(cls):
        return cls("", "", "", "", "", "", "")
    @classmethod
    def default_write(cls):
        return cls(base_dto.get_random_uid(), "", "", "", "", "", "")
    @classmethod
    def random_write(cls):
        return cls(base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid())
    @classmethod
    def new_write(cls, system_constraint_uid: str, system_constraint_name: str, system_table_uid: str, system_attribute_uid: str, tenant_uid: str, constraint_class: str, constraint_params_json: str):
        return cls(system_constraint_uid, system_constraint_name, system_table_uid, system_attribute_uid, tenant_uid, constraint_class, constraint_params_json)
    @classmethod
    def new_write_with_defaults(cls, system_constraint_uid: str = "", system_constraint_name: str = "", system_table_uid: str = "", system_attribute_uid: str = "", tenant_uid: str = "", constraint_class: str = "", constraint_params_json: str = ""):
        return cls(system_constraint_uid, system_constraint_name, system_table_uid, system_attribute_uid, tenant_uid, constraint_class, constraint_params_json)
    @classmethod
    def new_write_random_uid(cls, system_constraint_name: str, system_table_uid: str, system_attribute_uid: str, tenant_uid: str, constraint_class: str, constraint_params_json: str):
        return cls(base_dto.get_random_uid(), system_constraint_name, system_table_uid, system_attribute_uid, tenant_uid, constraint_class, constraint_params_json)
    @classmethod
    def get_class_model(cls) -> base_model:
        return db_models.system_constraint_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["system_constraint_uid"], d["system_constraint_name"], d["system_table_uid"], d["system_attribute_uid"], d["tenant_uid"], d["constraint_class"], d["constraint_params_json"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return system_constraint_write_dto(self.system_constraint_uid, self.system_constraint_name, self.system_table_uid, self.system_attribute_uid, self.tenant_uid, self.constraint_class, self.constraint_params_json, self.custom_attributes)
    def clone_write_new_uid(self):
        return system_constraint_write_dto(base_dto.get_random_uid(), self.system_constraint_name, self.system_table_uid, self.system_attribute_uid, self.tenant_uid, self.constraint_class, self.constraint_params_json, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return system_constraint_write_dto(uid, self.system_constraint_name, self.system_table_uid, self.system_attribute_uid, self.tenant_uid, self.constraint_class, self.constraint_params_json, self.custom_attributes)
    def get_model(self) -> base_model:
        return db_models.system_constraint_model
    def get_uid(self) -> str:
        return self.system_constraint_uid
    def get_name(self) -> str:
        return self.system_constraint_name
    def get_list_values(self) -> list[any]:
        return [self.system_constraint_uid, self.system_constraint_name, self.system_table_uid, self.system_attribute_uid, self.tenant_uid, self.constraint_class, self.constraint_params_json, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.system_constraint_uid, self.system_constraint_name, self.system_table_uid, self.system_attribute_uid, self.tenant_uid, self.constraint_class, self.constraint_params_json]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.system_constraint_name, self.system_table_uid, self.system_attribute_uid, self.tenant_uid, self.constraint_class, self.constraint_params_json, self.custom_attributes, updated_by, self.system_constraint_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.system_constraint_uid, self.system_constraint_name, self.system_table_uid, self.system_attribute_uid, self.tenant_uid, self.constraint_class, self.constraint_params_json, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.system_constraint_name, self.system_table_uid, self.system_attribute_uid, self.tenant_uid, self.constraint_class, self.constraint_params_json]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.system_constraint_name, self.system_table_uid, self.system_attribute_uid, self.tenant_uid, self.constraint_class, self.constraint_params_json, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_uid() == obj.get_uid()
    def update_uid(self, uid: str):
        self.system_constraint_uid = uid
    def update_uid_attributes(self, system_constraint_uid: str, system_constraint_name: str, system_table_uid: str, system_attribute_uid: str, tenant_uid: str, constraint_class: str, constraint_params_json: str):
        self.system_constraint_uid = system_constraint_uid
        self.system_constraint_name = system_constraint_name
        self.system_table_uid = system_table_uid
        self.system_attribute_uid = system_attribute_uid
        self.tenant_uid = tenant_uid
        self.constraint_class = constraint_class
        self.constraint_params_json = constraint_params_json
    def update_attributes(self, system_constraint_name: str, system_table_uid: str, system_attribute_uid: str, tenant_uid: str, constraint_class: str, constraint_params_json: str):
        self.system_constraint_name = system_constraint_name
        self.system_table_uid = system_table_uid
        self.system_attribute_uid = system_attribute_uid
        self.tenant_uid = tenant_uid
        self.constraint_class = constraint_class
        self.constraint_params_json = constraint_params_json


@dataclass(frozen=False)
class system_database_write_dto(base_write_dto):
    system_database_uid: str
    system_database_name: str
    db_url: str
    db_host: str
    db_name: str
    db_user: str
    last_status_name: str
    last_db_size: int
    created_connections: int
    released_connections: int
    def __init__(self, system_database_uid: str, system_database_name: str, db_url: str, db_host: str, db_name: str, db_user: str, last_status_name: str, last_db_size: int, created_connections: int, released_connections: int, custom_attributes: str = "{}"):
        self.system_database_uid = system_database_uid
        self.system_database_name = system_database_name
        self.db_url = db_url
        self.db_host = db_host
        self.db_name = db_name
        self.db_user = db_user
        self.last_status_name = last_status_name
        self.last_db_size = last_db_size
        self.created_connections = created_connections
        self.released_connections = released_connections
        self.custom_attributes = custom_attributes
    @classmethod
    def empty_write(cls):
        return cls("", "", "", "", "", "", "", 0, 0, 0)
    @classmethod
    def default_write(cls):
        return cls(base_dto.get_random_uid(), "", "", "", "", "", "", 0, 0, 0)
    @classmethod
    def random_write(cls):
        return cls(base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), 0, 0, 0)
    @classmethod
    def new_write(cls, system_database_uid: str, system_database_name: str, db_url: str, db_host: str, db_name: str, db_user: str, last_status_name: str, last_db_size: int, created_connections: int, released_connections: int):
        return cls(system_database_uid, system_database_name, db_url, db_host, db_name, db_user, last_status_name, last_db_size, created_connections, released_connections)
    @classmethod
    def new_write_with_defaults(cls, system_database_uid: str = "", system_database_name: str = "", db_url: str = "", db_host: str = "", db_name: str = "", db_user: str = "", last_status_name: str = "", last_db_size: int = 0, created_connections: int = 0, released_connections: int = 0):
        return cls(system_database_uid, system_database_name, db_url, db_host, db_name, db_user, last_status_name, last_db_size, created_connections, released_connections)
    @classmethod
    def new_write_random_uid(cls, system_database_name: str, db_url: str, db_host: str, db_name: str, db_user: str, last_status_name: str, last_db_size: int, created_connections: int, released_connections: int):
        return cls(base_dto.get_random_uid(), system_database_name, db_url, db_host, db_name, db_user, last_status_name, last_db_size, created_connections, released_connections)
    @classmethod
    def get_class_model(cls) -> base_model:
        return db_models.system_database_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["system_database_uid"], d["system_database_name"], d["db_url"], d["db_host"], d["db_name"], d["db_user"], d["last_status_name"], d["last_db_size"], d["created_connections"], d["released_connections"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return system_database_write_dto(self.system_database_uid, self.system_database_name, self.db_url, self.db_host, self.db_name, self.db_user, self.last_status_name, self.last_db_size, self.created_connections, self.released_connections, self.custom_attributes)
    def clone_write_new_uid(self):
        return system_database_write_dto(base_dto.get_random_uid(), self.system_database_name, self.db_url, self.db_host, self.db_name, self.db_user, self.last_status_name, self.last_db_size, self.created_connections, self.released_connections, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return system_database_write_dto(uid, self.system_database_name, self.db_url, self.db_host, self.db_name, self.db_user, self.last_status_name, self.last_db_size, self.created_connections, self.released_connections, self.custom_attributes)
    def get_model(self) -> base_model:
        return db_models.system_database_model
    def get_uid(self) -> str:
        return self.system_database_uid
    def get_name(self) -> str:
        return self.system_database_name
    def get_list_values(self) -> list[any]:
        return [self.system_database_uid, self.system_database_name, self.db_url, self.db_host, self.db_name, self.db_user, self.last_status_name, self.last_db_size, self.created_connections, self.released_connections, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.system_database_uid, self.system_database_name, self.db_url, self.db_host, self.db_name, self.db_user, self.last_status_name, self.last_db_size, self.created_connections, self.released_connections]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.system_database_name, self.db_url, self.db_host, self.db_name, self.db_user, self.last_status_name, self.last_db_size, self.created_connections, self.released_connections, self.custom_attributes, updated_by, self.system_database_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.system_database_uid, self.system_database_name, self.db_url, self.db_host, self.db_name, self.db_user, self.last_status_name, self.last_db_size, self.created_connections, self.released_connections, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.system_database_name, self.db_url, self.db_host, self.db_name, self.db_user, self.last_status_name, self.last_db_size, self.created_connections, self.released_connections]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.system_database_name, self.db_url, self.db_host, self.db_name, self.db_user, self.last_status_name, self.last_db_size, self.created_connections, self.released_connections, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_uid() == obj.get_uid()
    def update_uid(self, uid: str):
        self.system_database_uid = uid
    def update_uid_attributes(self, system_database_uid: str, system_database_name: str, db_url: str, db_host: str, db_name: str, db_user: str, last_status_name: str, last_db_size: int, created_connections: int, released_connections: int):
        self.system_database_uid = system_database_uid
        self.system_database_name = system_database_name
        self.db_url = db_url
        self.db_host = db_host
        self.db_name = db_name
        self.db_user = db_user
        self.last_status_name = last_status_name
        self.last_db_size = last_db_size
        self.created_connections = created_connections
        self.released_connections = released_connections
    def update_attributes(self, system_database_name: str, db_url: str, db_host: str, db_name: str, db_user: str, last_status_name: str, last_db_size: int, created_connections: int, released_connections: int):
        self.system_database_name = system_database_name
        self.db_url = db_url
        self.db_host = db_host
        self.db_name = db_name
        self.db_user = db_user
        self.last_status_name = last_status_name
        self.last_db_size = last_db_size
        self.created_connections = created_connections
        self.released_connections = released_connections


@dataclass(frozen=False)
class system_exception_write_dto(base_write_dto):
    system_exception_uid: str
    system_exception_name: str
    exception_class: str
    exception_message: str
    exception_stacktrace: str
    def __init__(self, system_exception_uid: str, system_exception_name: str, exception_class: str, exception_message: str, exception_stacktrace: str, custom_attributes: str = "{}"):
        self.system_exception_uid = system_exception_uid
        self.system_exception_name = system_exception_name
        self.exception_class = exception_class
        self.exception_message = exception_message
        self.exception_stacktrace = exception_stacktrace
        self.custom_attributes = custom_attributes
    @classmethod
    def empty_write(cls):
        return cls("", "", "", "", "")
    @classmethod
    def default_write(cls):
        return cls(base_dto.get_random_uid(), "", "", "", "")
    @classmethod
    def random_write(cls):
        return cls(base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid())
    @classmethod
    def new_write(cls, system_exception_uid: str, system_exception_name: str, exception_class: str, exception_message: str, exception_stacktrace: str):
        return cls(system_exception_uid, system_exception_name, exception_class, exception_message, exception_stacktrace)
    @classmethod
    def new_write_with_defaults(cls, system_exception_uid: str = "", system_exception_name: str = "", exception_class: str = "", exception_message: str = "", exception_stacktrace: str = ""):
        return cls(system_exception_uid, system_exception_name, exception_class, exception_message, exception_stacktrace)
    @classmethod
    def new_write_random_uid(cls, system_exception_name: str, exception_class: str, exception_message: str, exception_stacktrace: str):
        return cls(base_dto.get_random_uid(), system_exception_name, exception_class, exception_message, exception_stacktrace)
    @classmethod
    def get_class_model(cls) -> base_model:
        return db_models.system_exception_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["system_exception_uid"], d["system_exception_name"], d["exception_class"], d["exception_message"], d["exception_stacktrace"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return system_exception_write_dto(self.system_exception_uid, self.system_exception_name, self.exception_class, self.exception_message, self.exception_stacktrace, self.custom_attributes)
    def clone_write_new_uid(self):
        return system_exception_write_dto(base_dto.get_random_uid(), self.system_exception_name, self.exception_class, self.exception_message, self.exception_stacktrace, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return system_exception_write_dto(uid, self.system_exception_name, self.exception_class, self.exception_message, self.exception_stacktrace, self.custom_attributes)
    def get_model(self) -> base_model:
        return db_models.system_exception_model
    def get_uid(self) -> str:
        return self.system_exception_uid
    def get_name(self) -> str:
        return self.system_exception_name
    def get_list_values(self) -> list[any]:
        return [self.system_exception_uid, self.system_exception_name, self.exception_class, self.exception_message, self.exception_stacktrace, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.system_exception_uid, self.system_exception_name, self.exception_class, self.exception_message, self.exception_stacktrace]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.system_exception_name, self.exception_class, self.exception_message, self.exception_stacktrace, self.custom_attributes, updated_by, self.system_exception_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.system_exception_uid, self.system_exception_name, self.exception_class, self.exception_message, self.exception_stacktrace, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.system_exception_name, self.exception_class, self.exception_message, self.exception_stacktrace]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.system_exception_name, self.exception_class, self.exception_message, self.exception_stacktrace, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_uid() == obj.get_uid()
    def update_uid(self, uid: str):
        self.system_exception_uid = uid
    def update_uid_attributes(self, system_exception_uid: str, system_exception_name: str, exception_class: str, exception_message: str, exception_stacktrace: str):
        self.system_exception_uid = system_exception_uid
        self.system_exception_name = system_exception_name
        self.exception_class = exception_class
        self.exception_message = exception_message
        self.exception_stacktrace = exception_stacktrace
    def update_attributes(self, system_exception_name: str, exception_class: str, exception_message: str, exception_stacktrace: str):
        self.system_exception_name = system_exception_name
        self.exception_class = exception_class
        self.exception_message = exception_message
        self.exception_stacktrace = exception_stacktrace


@dataclass(frozen=False)
class system_instance_write_dto(base_write_dto):
    system_instance_uid: str
    system_instance_name: str
    system_version_uid: str
    host_name: str
    host_ip: str
    local_path: str
    mode_name: str
    ticks_count: int
    def __init__(self, system_instance_uid: str, system_instance_name: str, system_version_uid: str, host_name: str, host_ip: str, local_path: str, mode_name: str, ticks_count: int, custom_attributes: str = "{}"):
        self.system_instance_uid = system_instance_uid
        self.system_instance_name = system_instance_name
        self.system_version_uid = system_version_uid
        self.host_name = host_name
        self.host_ip = host_ip
        self.local_path = local_path
        self.mode_name = mode_name
        self.ticks_count = ticks_count
        self.custom_attributes = custom_attributes
    @classmethod
    def empty_write(cls):
        return cls("", "", "", "", "", "", "", 0)
    @classmethod
    def default_write(cls):
        return cls(base_dto.get_random_uid(), "", "", "", "", "", "", 0)
    @classmethod
    def random_write(cls):
        return cls(base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), 0)
    @classmethod
    def new_write(cls, system_instance_uid: str, system_instance_name: str, system_version_uid: str, host_name: str, host_ip: str, local_path: str, mode_name: str, ticks_count: int):
        return cls(system_instance_uid, system_instance_name, system_version_uid, host_name, host_ip, local_path, mode_name, ticks_count)
    @classmethod
    def new_write_with_defaults(cls, system_instance_uid: str = objects.system_instance_uid, system_instance_name: str = "", system_version_uid: str = objects.system_version_uid, host_name: str = "", host_ip: str = "", local_path: str = "", mode_name: str = "", ticks_count: int = 0):
        return cls(system_instance_uid, system_instance_name, system_version_uid, host_name, host_ip, local_path, mode_name, ticks_count)
    @classmethod
    def new_write_random_uid(cls, system_instance_name: str, system_version_uid: str, host_name: str, host_ip: str, local_path: str, mode_name: str, ticks_count: int):
        return cls(base_dto.get_random_uid(), system_instance_name, system_version_uid, host_name, host_ip, local_path, mode_name, ticks_count)
    @classmethod
    def get_class_model(cls) -> base_model:
        return db_models.system_instance_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["system_instance_uid"], d["system_instance_name"], d["system_version_uid"], d["host_name"], d["host_ip"], d["local_path"], d["mode_name"], d["ticks_count"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return system_instance_write_dto(self.system_instance_uid, self.system_instance_name, self.system_version_uid, self.host_name, self.host_ip, self.local_path, self.mode_name, self.ticks_count, self.custom_attributes)
    def clone_write_new_uid(self):
        return system_instance_write_dto(base_dto.get_random_uid(), self.system_instance_name, self.system_version_uid, self.host_name, self.host_ip, self.local_path, self.mode_name, self.ticks_count, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return system_instance_write_dto(uid, self.system_instance_name, self.system_version_uid, self.host_name, self.host_ip, self.local_path, self.mode_name, self.ticks_count, self.custom_attributes)
    def get_model(self) -> base_model:
        return db_models.system_instance_model
    def get_uid(self) -> str:
        return self.system_instance_uid
    def get_name(self) -> str:
        return self.system_instance_name
    def get_list_values(self) -> list[any]:
        return [self.system_instance_uid, self.system_instance_name, self.system_version_uid, self.host_name, self.host_ip, self.local_path, self.mode_name, self.ticks_count, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.system_instance_uid, self.system_instance_name, self.system_version_uid, self.host_name, self.host_ip, self.local_path, self.mode_name, self.ticks_count]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.system_instance_name, self.system_version_uid, self.host_name, self.host_ip, self.local_path, self.mode_name, self.ticks_count, self.custom_attributes, updated_by, self.system_instance_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.system_instance_uid, self.system_instance_name, self.system_version_uid, self.host_name, self.host_ip, self.local_path, self.mode_name, self.ticks_count, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.system_instance_name, self.system_version_uid, self.host_name, self.host_ip, self.local_path, self.mode_name, self.ticks_count]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.system_instance_name, self.system_version_uid, self.host_name, self.host_ip, self.local_path, self.mode_name, self.ticks_count, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_uid() == obj.get_uid()
    def update_uid(self, uid: str):
        self.system_instance_uid = uid
    def update_uid_attributes(self, system_instance_uid: str, system_instance_name: str, system_version_uid: str, host_name: str, host_ip: str, local_path: str, mode_name: str, ticks_count: int):
        self.system_instance_uid = system_instance_uid
        self.system_instance_name = system_instance_name
        self.system_version_uid = system_version_uid
        self.host_name = host_name
        self.host_ip = host_ip
        self.local_path = local_path
        self.mode_name = mode_name
        self.ticks_count = ticks_count
    def update_attributes(self, system_instance_name: str, system_version_uid: str, host_name: str, host_ip: str, local_path: str, mode_name: str, ticks_count: int):
        self.system_instance_name = system_instance_name
        self.system_version_uid = system_version_uid
        self.host_name = host_name
        self.host_ip = host_ip
        self.local_path = local_path
        self.mode_name = mode_name
        self.ticks_count = ticks_count


@dataclass(frozen=False)
class system_license_write_dto(base_write_dto):
    system_license_uid: str
    system_license_name: str
    class_name: str
    license_definition_json: str
    license_description: str
    def __init__(self, system_license_uid: str, system_license_name: str, class_name: str, license_definition_json: str, license_description: str, custom_attributes: str = "{}"):
        self.system_license_uid = system_license_uid
        self.system_license_name = system_license_name
        self.class_name = class_name
        self.license_definition_json = license_definition_json
        self.license_description = license_description
        self.custom_attributes = custom_attributes
    @classmethod
    def empty_write(cls):
        return cls("", "", "", "", "")
    @classmethod
    def default_write(cls):
        return cls(base_dto.get_random_uid(), "", "", "", "")
    @classmethod
    def random_write(cls):
        return cls(base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid())
    @classmethod
    def new_write(cls, system_license_uid: str, system_license_name: str, class_name: str, license_definition_json: str, license_description: str):
        return cls(system_license_uid, system_license_name, class_name, license_definition_json, license_description)
    @classmethod
    def new_write_with_defaults(cls, system_license_uid: str = "", system_license_name: str = "", class_name: str = "", license_definition_json: str = "", license_description: str = ""):
        return cls(system_license_uid, system_license_name, class_name, license_definition_json, license_description)
    @classmethod
    def new_write_random_uid(cls, system_license_name: str, class_name: str, license_definition_json: str, license_description: str):
        return cls(base_dto.get_random_uid(), system_license_name, class_name, license_definition_json, license_description)
    @classmethod
    def get_class_model(cls) -> base_model:
        return db_models.system_license_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["system_license_uid"], d["system_license_name"], d["class_name"], d["license_definition_json"], d["license_description"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return system_license_write_dto(self.system_license_uid, self.system_license_name, self.class_name, self.license_definition_json, self.license_description, self.custom_attributes)
    def clone_write_new_uid(self):
        return system_license_write_dto(base_dto.get_random_uid(), self.system_license_name, self.class_name, self.license_definition_json, self.license_description, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return system_license_write_dto(uid, self.system_license_name, self.class_name, self.license_definition_json, self.license_description, self.custom_attributes)
    def get_model(self) -> base_model:
        return db_models.system_license_model
    def get_uid(self) -> str:
        return self.system_license_uid
    def get_name(self) -> str:
        return self.system_license_name
    def get_list_values(self) -> list[any]:
        return [self.system_license_uid, self.system_license_name, self.class_name, self.license_definition_json, self.license_description, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.system_license_uid, self.system_license_name, self.class_name, self.license_definition_json, self.license_description]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.system_license_name, self.class_name, self.license_definition_json, self.license_description, self.custom_attributes, updated_by, self.system_license_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.system_license_uid, self.system_license_name, self.class_name, self.license_definition_json, self.license_description, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.system_license_name, self.class_name, self.license_definition_json, self.license_description]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.system_license_name, self.class_name, self.license_definition_json, self.license_description, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_uid() == obj.get_uid()
    def update_uid(self, uid: str):
        self.system_license_uid = uid
    def update_uid_attributes(self, system_license_uid: str, system_license_name: str, class_name: str, license_definition_json: str, license_description: str):
        self.system_license_uid = system_license_uid
        self.system_license_name = system_license_name
        self.class_name = class_name
        self.license_definition_json = license_definition_json
        self.license_description = license_description
    def update_attributes(self, system_license_name: str, class_name: str, license_definition_json: str, license_description: str):
        self.system_license_name = system_license_name
        self.class_name = class_name
        self.license_definition_json = license_definition_json
        self.license_description = license_description


@dataclass(frozen=False)
class system_lock_write_dto(base_write_dto):
    system_lock_uid: str
    system_lock_name: str
    lock_account_uid: str
    lock_comment: str
    lock_reason: str
    def __init__(self, system_lock_uid: str, system_lock_name: str, lock_account_uid: str, lock_comment: str, lock_reason: str, custom_attributes: str = "{}"):
        self.system_lock_uid = system_lock_uid
        self.system_lock_name = system_lock_name
        self.lock_account_uid = lock_account_uid
        self.lock_comment = lock_comment
        self.lock_reason = lock_reason
        self.custom_attributes = custom_attributes
    @classmethod
    def empty_write(cls):
        return cls("", "", "", "", "")
    @classmethod
    def default_write(cls):
        return cls(base_dto.get_random_uid(), "", "", "", "")
    @classmethod
    def random_write(cls):
        return cls(base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid())
    @classmethod
    def new_write(cls, system_lock_uid: str, system_lock_name: str, lock_account_uid: str, lock_comment: str, lock_reason: str):
        return cls(system_lock_uid, system_lock_name, lock_account_uid, lock_comment, lock_reason)
    @classmethod
    def new_write_with_defaults(cls, system_lock_uid: str = "", system_lock_name: str = "", lock_account_uid: str = "", lock_comment: str = "", lock_reason: str = ""):
        return cls(system_lock_uid, system_lock_name, lock_account_uid, lock_comment, lock_reason)
    @classmethod
    def new_write_random_uid(cls, system_lock_name: str, lock_account_uid: str, lock_comment: str, lock_reason: str):
        return cls(base_dto.get_random_uid(), system_lock_name, lock_account_uid, lock_comment, lock_reason)
    @classmethod
    def get_class_model(cls) -> base_model:
        return db_models.system_lock_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["system_lock_uid"], d["system_lock_name"], d["lock_account_uid"], d["lock_comment"], d["lock_reason"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return system_lock_write_dto(self.system_lock_uid, self.system_lock_name, self.lock_account_uid, self.lock_comment, self.lock_reason, self.custom_attributes)
    def clone_write_new_uid(self):
        return system_lock_write_dto(base_dto.get_random_uid(), self.system_lock_name, self.lock_account_uid, self.lock_comment, self.lock_reason, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return system_lock_write_dto(uid, self.system_lock_name, self.lock_account_uid, self.lock_comment, self.lock_reason, self.custom_attributes)
    def get_model(self) -> base_model:
        return db_models.system_lock_model
    def get_uid(self) -> str:
        return self.system_lock_uid
    def get_name(self) -> str:
        return self.system_lock_name
    def get_list_values(self) -> list[any]:
        return [self.system_lock_uid, self.system_lock_name, self.lock_account_uid, self.lock_comment, self.lock_reason, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.system_lock_uid, self.system_lock_name, self.lock_account_uid, self.lock_comment, self.lock_reason]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.system_lock_name, self.lock_account_uid, self.lock_comment, self.lock_reason, self.custom_attributes, updated_by, self.system_lock_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.system_lock_uid, self.system_lock_name, self.lock_account_uid, self.lock_comment, self.lock_reason, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.system_lock_name, self.lock_account_uid, self.lock_comment, self.lock_reason]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.system_lock_name, self.lock_account_uid, self.lock_comment, self.lock_reason, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_uid() == obj.get_uid()
    def update_uid(self, uid: str):
        self.system_lock_uid = uid
    def update_uid_attributes(self, system_lock_uid: str, system_lock_name: str, lock_account_uid: str, lock_comment: str, lock_reason: str):
        self.system_lock_uid = system_lock_uid
        self.system_lock_name = system_lock_name
        self.lock_account_uid = lock_account_uid
        self.lock_comment = lock_comment
        self.lock_reason = lock_reason
    def update_attributes(self, system_lock_name: str, lock_account_uid: str, lock_comment: str, lock_reason: str):
        self.system_lock_name = system_lock_name
        self.lock_account_uid = lock_account_uid
        self.lock_comment = lock_comment
        self.lock_reason = lock_reason


@dataclass(frozen=False)
class system_module_write_dto(base_write_dto):
    system_module_uid: str
    system_module_name: str
    system_module_description: str
    def __init__(self, system_module_uid: str, system_module_name: str, system_module_description: str, custom_attributes: str = "{}"):
        self.system_module_uid = system_module_uid
        self.system_module_name = system_module_name
        self.system_module_description = system_module_description
        self.custom_attributes = custom_attributes
    @classmethod
    def empty_write(cls):
        return cls("", "", "")
    @classmethod
    def default_write(cls):
        return cls(base_dto.get_random_uid(), "", "")
    @classmethod
    def random_write(cls):
        return cls(base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid())
    @classmethod
    def new_write(cls, system_module_uid: str, system_module_name: str, system_module_description: str):
        return cls(system_module_uid, system_module_name, system_module_description)
    @classmethod
    def new_write_with_defaults(cls, system_module_uid: str = "", system_module_name: str = "", system_module_description: str = ""):
        return cls(system_module_uid, system_module_name, system_module_description)
    @classmethod
    def new_write_random_uid(cls, system_module_name: str, system_module_description: str):
        return cls(base_dto.get_random_uid(), system_module_name, system_module_description)
    @classmethod
    def get_class_model(cls) -> base_model:
        return db_models.system_module_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["system_module_uid"], d["system_module_name"], d["system_module_description"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return system_module_write_dto(self.system_module_uid, self.system_module_name, self.system_module_description, self.custom_attributes)
    def clone_write_new_uid(self):
        return system_module_write_dto(base_dto.get_random_uid(), self.system_module_name, self.system_module_description, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return system_module_write_dto(uid, self.system_module_name, self.system_module_description, self.custom_attributes)
    def get_model(self) -> base_model:
        return db_models.system_module_model
    def get_uid(self) -> str:
        return self.system_module_uid
    def get_name(self) -> str:
        return self.system_module_name
    def get_list_values(self) -> list[any]:
        return [self.system_module_uid, self.system_module_name, self.system_module_description, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.system_module_uid, self.system_module_name, self.system_module_description]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.system_module_name, self.system_module_description, self.custom_attributes, updated_by, self.system_module_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.system_module_uid, self.system_module_name, self.system_module_description, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.system_module_name, self.system_module_description]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.system_module_name, self.system_module_description, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_uid() == obj.get_uid()
    def update_uid(self, uid: str):
        self.system_module_uid = uid
    def update_uid_attributes(self, system_module_uid: str, system_module_name: str, system_module_description: str):
        self.system_module_uid = system_module_uid
        self.system_module_name = system_module_name
        self.system_module_description = system_module_description
    def update_attributes(self, system_module_name: str, system_module_description: str):
        self.system_module_name = system_module_name
        self.system_module_description = system_module_description


@dataclass(frozen=False)
class system_query_write_dto(base_write_dto):
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
    def __init__(self, system_query_uid: str, system_query_name: str, time_start: int, total_query_time: int, query_seq: int, execution_counter: int, connection_counter: int, release_counter: int, current_active: int, current_idle: int, table_name: str, rows_count: int, sql: str, custom_attributes: str = "{}"):
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
        self.custom_attributes = custom_attributes
    @classmethod
    def empty_write(cls):
        return cls("", "", 0, 0, 0, 0, 0, 0, 0, 0, "", 0, "")
    @classmethod
    def default_write(cls):
        return cls(base_dto.get_random_uid(), "", 0, 0, 0, 0, 0, 0, 0, 0, "", 0, "")
    @classmethod
    def random_write(cls):
        return cls(base_dto.get_random_uid(), base_dto.get_random_uid(), 0, 0, 0, 0, 0, 0, 0, 0, base_dto.get_random_uid(), 0, base_dto.get_random_uid())
    @classmethod
    def new_write(cls, system_query_uid: str, system_query_name: str, time_start: int, total_query_time: int, query_seq: int, execution_counter: int, connection_counter: int, release_counter: int, current_active: int, current_idle: int, table_name: str, rows_count: int, sql: str):
        return cls(system_query_uid, system_query_name, time_start, total_query_time, query_seq, execution_counter, connection_counter, release_counter, current_active, current_idle, table_name, rows_count, sql)
    @classmethod
    def new_write_with_defaults(cls, system_query_uid: str = "", system_query_name: str = "", time_start: int = 0, total_query_time: int = 0, query_seq: int = 0, execution_counter: int = 0, connection_counter: int = 0, release_counter: int = 0, current_active: int = 0, current_idle: int = 0, table_name: str = "", rows_count: int = 0, sql: str = ""):
        return cls(system_query_uid, system_query_name, time_start, total_query_time, query_seq, execution_counter, connection_counter, release_counter, current_active, current_idle, table_name, rows_count, sql)
    @classmethod
    def new_write_random_uid(cls, system_query_name: str, time_start: int, total_query_time: int, query_seq: int, execution_counter: int, connection_counter: int, release_counter: int, current_active: int, current_idle: int, table_name: str, rows_count: int, sql: str):
        return cls(base_dto.get_random_uid(), system_query_name, time_start, total_query_time, query_seq, execution_counter, connection_counter, release_counter, current_active, current_idle, table_name, rows_count, sql)
    @classmethod
    def get_class_model(cls) -> base_model:
        return db_models.system_query_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["system_query_uid"], d["system_query_name"], d["time_start"], d["total_query_time"], d["query_seq"], d["execution_counter"], d["connection_counter"], d["release_counter"], d["current_active"], d["current_idle"], d["table_name"], d["rows_count"], d["sql"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return system_query_write_dto(self.system_query_uid, self.system_query_name, self.time_start, self.total_query_time, self.query_seq, self.execution_counter, self.connection_counter, self.release_counter, self.current_active, self.current_idle, self.table_name, self.rows_count, self.sql, self.custom_attributes)
    def clone_write_new_uid(self):
        return system_query_write_dto(base_dto.get_random_uid(), self.system_query_name, self.time_start, self.total_query_time, self.query_seq, self.execution_counter, self.connection_counter, self.release_counter, self.current_active, self.current_idle, self.table_name, self.rows_count, self.sql, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return system_query_write_dto(uid, self.system_query_name, self.time_start, self.total_query_time, self.query_seq, self.execution_counter, self.connection_counter, self.release_counter, self.current_active, self.current_idle, self.table_name, self.rows_count, self.sql, self.custom_attributes)
    def get_model(self) -> base_model:
        return db_models.system_query_model
    def get_uid(self) -> str:
        return self.system_query_uid
    def get_name(self) -> str:
        return self.system_query_name
    def get_list_values(self) -> list[any]:
        return [self.system_query_uid, self.system_query_name, self.time_start, self.total_query_time, self.query_seq, self.execution_counter, self.connection_counter, self.release_counter, self.current_active, self.current_idle, self.table_name, self.rows_count, self.sql, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.system_query_uid, self.system_query_name, self.time_start, self.total_query_time, self.query_seq, self.execution_counter, self.connection_counter, self.release_counter, self.current_active, self.current_idle, self.table_name, self.rows_count, self.sql]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.system_query_name, self.time_start, self.total_query_time, self.query_seq, self.execution_counter, self.connection_counter, self.release_counter, self.current_active, self.current_idle, self.table_name, self.rows_count, self.sql, self.custom_attributes, updated_by, self.system_query_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.system_query_uid, self.system_query_name, self.time_start, self.total_query_time, self.query_seq, self.execution_counter, self.connection_counter, self.release_counter, self.current_active, self.current_idle, self.table_name, self.rows_count, self.sql, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.system_query_name, self.time_start, self.total_query_time, self.query_seq, self.execution_counter, self.connection_counter, self.release_counter, self.current_active, self.current_idle, self.table_name, self.rows_count, self.sql]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.system_query_name, self.time_start, self.total_query_time, self.query_seq, self.execution_counter, self.connection_counter, self.release_counter, self.current_active, self.current_idle, self.table_name, self.rows_count, self.sql, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_uid() == obj.get_uid()
    def update_uid(self, uid: str):
        self.system_query_uid = uid
    def update_uid_attributes(self, system_query_uid: str, system_query_name: str, time_start: int, total_query_time: int, query_seq: int, execution_counter: int, connection_counter: int, release_counter: int, current_active: int, current_idle: int, table_name: str, rows_count: int, sql: str):
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
    def update_attributes(self, system_query_name: str, time_start: int, total_query_time: int, query_seq: int, execution_counter: int, connection_counter: int, release_counter: int, current_active: int, current_idle: int, table_name: str, rows_count: int, sql: str):
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


@dataclass(frozen=False)
class system_request_write_dto(base_write_dto):
    system_request_uid: str
    system_request_name: str
    account_uid: str | None
    request_method: str
    request_url: str
    request_body_size: int
    request_host: str
    request_time: int
    response_code: int
    def __init__(self, system_request_uid: str, system_request_name: str, account_uid: str | None, request_method: str, request_url: str, request_body_size: int, request_host: str, request_time: int, response_code: int, custom_attributes: str = "{}"):
        self.system_request_uid = system_request_uid
        self.system_request_name = system_request_name
        self.account_uid = account_uid
        self.request_method = request_method
        self.request_url = request_url
        self.request_body_size = request_body_size
        self.request_host = request_host
        self.request_time = request_time
        self.response_code = response_code
        self.custom_attributes = custom_attributes
    @classmethod
    def empty_write(cls):
        return cls("", "", "", "", "", 0, "", 0, 0)
    @classmethod
    def default_write(cls):
        return cls(base_dto.get_random_uid(), "", "", "", "", 0, "", 0, 0)
    @classmethod
    def random_write(cls):
        return cls(base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), 0, base_dto.get_random_uid(), 0, 0)
    @classmethod
    def new_write(cls, system_request_uid: str, system_request_name: str, account_uid: str | None, request_method: str, request_url: str, request_body_size: int, request_host: str, request_time: int, response_code: int):
        return cls(system_request_uid, system_request_name, account_uid, request_method, request_url, request_body_size, request_host, request_time, response_code)
    @classmethod
    def new_write_with_defaults(cls, system_request_uid: str = "", system_request_name: str = "", account_uid: str | None = "", request_method: str = "", request_url: str = "", request_body_size: int = 0, request_host: str = "", request_time: int = 0, response_code: int = 0):
        return cls(system_request_uid, system_request_name, account_uid, request_method, request_url, request_body_size, request_host, request_time, response_code)
    @classmethod
    def new_write_random_uid(cls, system_request_name: str, account_uid: str | None, request_method: str, request_url: str, request_body_size: int, request_host: str, request_time: int, response_code: int):
        return cls(base_dto.get_random_uid(), system_request_name, account_uid, request_method, request_url, request_body_size, request_host, request_time, response_code)
    @classmethod
    def get_class_model(cls) -> base_model:
        return db_models.system_request_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["system_request_uid"], d["system_request_name"], d["account_uid"], d["request_method"], d["request_url"], d["request_body_size"], d["request_host"], d["request_time"], d["response_code"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return system_request_write_dto(self.system_request_uid, self.system_request_name, self.account_uid, self.request_method, self.request_url, self.request_body_size, self.request_host, self.request_time, self.response_code, self.custom_attributes)
    def clone_write_new_uid(self):
        return system_request_write_dto(base_dto.get_random_uid(), self.system_request_name, self.account_uid, self.request_method, self.request_url, self.request_body_size, self.request_host, self.request_time, self.response_code, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return system_request_write_dto(uid, self.system_request_name, self.account_uid, self.request_method, self.request_url, self.request_body_size, self.request_host, self.request_time, self.response_code, self.custom_attributes)
    def get_model(self) -> base_model:
        return db_models.system_request_model
    def get_uid(self) -> str:
        return self.system_request_uid
    def get_name(self) -> str:
        return self.system_request_name
    def get_list_values(self) -> list[any]:
        return [self.system_request_uid, self.system_request_name, self.account_uid, self.request_method, self.request_url, self.request_body_size, self.request_host, self.request_time, self.response_code, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.system_request_uid, self.system_request_name, self.account_uid, self.request_method, self.request_url, self.request_body_size, self.request_host, self.request_time, self.response_code]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.system_request_name, self.account_uid, self.request_method, self.request_url, self.request_body_size, self.request_host, self.request_time, self.response_code, self.custom_attributes, updated_by, self.system_request_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.system_request_uid, self.system_request_name, self.account_uid, self.request_method, self.request_url, self.request_body_size, self.request_host, self.request_time, self.response_code, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.system_request_name, self.account_uid, self.request_method, self.request_url, self.request_body_size, self.request_host, self.request_time, self.response_code]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.system_request_name, self.account_uid, self.request_method, self.request_url, self.request_body_size, self.request_host, self.request_time, self.response_code, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_uid() == obj.get_uid()
    def update_uid(self, uid: str):
        self.system_request_uid = uid
    def update_uid_attributes(self, system_request_uid: str, system_request_name: str, account_uid: str | None, request_method: str, request_url: str, request_body_size: int, request_host: str, request_time: int, response_code: int):
        self.system_request_uid = system_request_uid
        self.system_request_name = system_request_name
        self.account_uid = account_uid
        self.request_method = request_method
        self.request_url = request_url
        self.request_body_size = request_body_size
        self.request_host = request_host
        self.request_time = request_time
        self.response_code = response_code
    def update_attributes(self, system_request_name: str, account_uid: str | None, request_method: str, request_url: str, request_body_size: int, request_host: str, request_time: int, response_code: int):
        self.system_request_name = system_request_name
        self.account_uid = account_uid
        self.request_method = request_method
        self.request_url = request_url
        self.request_body_size = request_body_size
        self.request_host = request_host
        self.request_time = request_time
        self.response_code = response_code


@dataclass(frozen=False)
class system_setting_write_dto(base_write_dto):
    system_setting_uid: str
    system_setting_name: str
    setting_value: str
    setting_type: str
    is_public: int
    def __init__(self, system_setting_uid: str, system_setting_name: str, setting_value: str, setting_type: str, is_public: int, custom_attributes: str = "{}"):
        self.system_setting_uid = system_setting_uid
        self.system_setting_name = system_setting_name
        self.setting_value = setting_value
        self.setting_type = setting_type
        self.is_public = is_public
        self.custom_attributes = custom_attributes
    @classmethod
    def empty_write(cls):
        return cls("", "", "", "", 0)
    @classmethod
    def default_write(cls):
        return cls(base_dto.get_random_uid(), "", "", "", 0)
    @classmethod
    def random_write(cls):
        return cls(base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), 0)
    @classmethod
    def new_write(cls, system_setting_uid: str, system_setting_name: str, setting_value: str, setting_type: str, is_public: int):
        return cls(system_setting_uid, system_setting_name, setting_value, setting_type, is_public)
    @classmethod
    def new_write_with_defaults(cls, system_setting_uid: str = "", system_setting_name: str = "", setting_value: str = "", setting_type: str = "", is_public: int = 0):
        return cls(system_setting_uid, system_setting_name, setting_value, setting_type, is_public)
    @classmethod
    def new_write_random_uid(cls, system_setting_name: str, setting_value: str, setting_type: str, is_public: int):
        return cls(base_dto.get_random_uid(), system_setting_name, setting_value, setting_type, is_public)
    @classmethod
    def get_class_model(cls) -> base_model:
        return db_models.system_setting_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["system_setting_uid"], d["system_setting_name"], d["setting_value"], d["setting_type"], d["is_public"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return system_setting_write_dto(self.system_setting_uid, self.system_setting_name, self.setting_value, self.setting_type, self.is_public, self.custom_attributes)
    def clone_write_new_uid(self):
        return system_setting_write_dto(base_dto.get_random_uid(), self.system_setting_name, self.setting_value, self.setting_type, self.is_public, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return system_setting_write_dto(uid, self.system_setting_name, self.setting_value, self.setting_type, self.is_public, self.custom_attributes)
    def get_model(self) -> base_model:
        return db_models.system_setting_model
    def get_uid(self) -> str:
        return self.system_setting_uid
    def get_name(self) -> str:
        return self.system_setting_name
    def get_list_values(self) -> list[any]:
        return [self.system_setting_uid, self.system_setting_name, self.setting_value, self.setting_type, self.is_public, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.system_setting_uid, self.system_setting_name, self.setting_value, self.setting_type, self.is_public]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.system_setting_name, self.setting_value, self.setting_type, self.is_public, self.custom_attributes, updated_by, self.system_setting_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.system_setting_uid, self.system_setting_name, self.setting_value, self.setting_type, self.is_public, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.system_setting_name, self.setting_value, self.setting_type, self.is_public]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.system_setting_name, self.setting_value, self.setting_type, self.is_public, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_uid() == obj.get_uid()
    def update_uid(self, uid: str):
        self.system_setting_uid = uid
    def update_uid_attributes(self, system_setting_uid: str, system_setting_name: str, setting_value: str, setting_type: str, is_public: int):
        self.system_setting_uid = system_setting_uid
        self.system_setting_name = system_setting_name
        self.setting_value = setting_value
        self.setting_type = setting_type
        self.is_public = is_public
    def update_attributes(self, system_setting_name: str, setting_value: str, setting_type: str, is_public: int):
        self.system_setting_name = system_setting_name
        self.setting_value = setting_value
        self.setting_type = setting_type
        self.is_public = is_public


@dataclass(frozen=False)
class system_setting_account_write_dto(base_write_dto):
    system_setting_account_uid: str
    system_setting_account_name: str
    account_uid: str
    setting_value: str
    is_public: int
    def __init__(self, system_setting_account_uid: str, system_setting_account_name: str, account_uid: str, setting_value: str, is_public: int, custom_attributes: str = "{}"):
        self.system_setting_account_uid = system_setting_account_uid
        self.system_setting_account_name = system_setting_account_name
        self.account_uid = account_uid
        self.setting_value = setting_value
        self.is_public = is_public
        self.custom_attributes = custom_attributes
    @classmethod
    def empty_write(cls):
        return cls("", "", "", "", 0)
    @classmethod
    def default_write(cls):
        return cls(base_dto.get_random_uid(), "", "", "", 0)
    @classmethod
    def random_write(cls):
        return cls(base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), 0)
    @classmethod
    def new_write(cls, system_setting_account_uid: str, system_setting_account_name: str, account_uid: str, setting_value: str, is_public: int):
        return cls(system_setting_account_uid, system_setting_account_name, account_uid, setting_value, is_public)
    @classmethod
    def new_write_with_defaults(cls, system_setting_account_uid: str = "", system_setting_account_name: str = "", account_uid: str = "", setting_value: str = "", is_public: int = 0):
        return cls(system_setting_account_uid, system_setting_account_name, account_uid, setting_value, is_public)
    @classmethod
    def new_write_random_uid(cls, system_setting_account_name: str, account_uid: str, setting_value: str, is_public: int):
        return cls(base_dto.get_random_uid(), system_setting_account_name, account_uid, setting_value, is_public)
    @classmethod
    def get_class_model(cls) -> base_model:
        return db_models.system_setting_account_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["system_setting_account_uid"], d["system_setting_account_name"], d["account_uid"], d["setting_value"], d["is_public"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return system_setting_account_write_dto(self.system_setting_account_uid, self.system_setting_account_name, self.account_uid, self.setting_value, self.is_public, self.custom_attributes)
    def clone_write_new_uid(self):
        return system_setting_account_write_dto(base_dto.get_random_uid(), self.system_setting_account_name, self.account_uid, self.setting_value, self.is_public, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return system_setting_account_write_dto(uid, self.system_setting_account_name, self.account_uid, self.setting_value, self.is_public, self.custom_attributes)
    def get_model(self) -> base_model:
        return db_models.system_setting_account_model
    def get_uid(self) -> str:
        return self.system_setting_account_uid
    def get_name(self) -> str:
        return self.system_setting_account_name
    def get_list_values(self) -> list[any]:
        return [self.system_setting_account_uid, self.system_setting_account_name, self.account_uid, self.setting_value, self.is_public, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.system_setting_account_uid, self.system_setting_account_name, self.account_uid, self.setting_value, self.is_public]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.system_setting_account_name, self.account_uid, self.setting_value, self.is_public, self.custom_attributes, updated_by, self.system_setting_account_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.system_setting_account_uid, self.system_setting_account_name, self.account_uid, self.setting_value, self.is_public, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.system_setting_account_name, self.account_uid, self.setting_value, self.is_public]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.system_setting_account_name, self.account_uid, self.setting_value, self.is_public, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_uid() == obj.get_uid()
    def update_uid(self, uid: str):
        self.system_setting_account_uid = uid
    def update_uid_attributes(self, system_setting_account_uid: str, system_setting_account_name: str, account_uid: str, setting_value: str, is_public: int):
        self.system_setting_account_uid = system_setting_account_uid
        self.system_setting_account_name = system_setting_account_name
        self.account_uid = account_uid
        self.setting_value = setting_value
        self.is_public = is_public
    def update_attributes(self, system_setting_account_name: str, account_uid: str, setting_value: str, is_public: int):
        self.system_setting_account_name = system_setting_account_name
        self.account_uid = account_uid
        self.setting_value = setting_value
        self.is_public = is_public


@dataclass(frozen=False)
class system_state_write_dto(base_write_dto):
    system_state_uid: str
    system_state_name: str
    mem_free: int
    mem_max: int
    objects_count: int
    def __init__(self, system_state_uid: str, system_state_name: str, mem_free: int, mem_max: int, objects_count: int, custom_attributes: str = "{}"):
        self.system_state_uid = system_state_uid
        self.system_state_name = system_state_name
        self.mem_free = mem_free
        self.mem_max = mem_max
        self.objects_count = objects_count
        self.custom_attributes = custom_attributes
    @classmethod
    def empty_write(cls):
        return cls("", "", 0, 0, 0)
    @classmethod
    def default_write(cls):
        return cls(base_dto.get_random_uid(), "", 0, 0, 0)
    @classmethod
    def random_write(cls):
        return cls(base_dto.get_random_uid(), base_dto.get_random_uid(), 0, 0, 0)
    @classmethod
    def new_write(cls, system_state_uid: str, system_state_name: str, mem_free: int, mem_max: int, objects_count: int):
        return cls(system_state_uid, system_state_name, mem_free, mem_max, objects_count)
    @classmethod
    def new_write_with_defaults(cls, system_state_uid: str = "", system_state_name: str = "", mem_free: int = 0, mem_max: int = 0, objects_count: int = 0):
        return cls(system_state_uid, system_state_name, mem_free, mem_max, objects_count)
    @classmethod
    def new_write_random_uid(cls, system_state_name: str, mem_free: int, mem_max: int, objects_count: int):
        return cls(base_dto.get_random_uid(), system_state_name, mem_free, mem_max, objects_count)
    @classmethod
    def get_class_model(cls) -> base_model:
        return db_models.system_state_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["system_state_uid"], d["system_state_name"], d["mem_free"], d["mem_max"], d["objects_count"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return system_state_write_dto(self.system_state_uid, self.system_state_name, self.mem_free, self.mem_max, self.objects_count, self.custom_attributes)
    def clone_write_new_uid(self):
        return system_state_write_dto(base_dto.get_random_uid(), self.system_state_name, self.mem_free, self.mem_max, self.objects_count, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return system_state_write_dto(uid, self.system_state_name, self.mem_free, self.mem_max, self.objects_count, self.custom_attributes)
    def get_model(self) -> base_model:
        return db_models.system_state_model
    def get_uid(self) -> str:
        return self.system_state_uid
    def get_name(self) -> str:
        return self.system_state_name
    def get_list_values(self) -> list[any]:
        return [self.system_state_uid, self.system_state_name, self.mem_free, self.mem_max, self.objects_count, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.system_state_uid, self.system_state_name, self.mem_free, self.mem_max, self.objects_count]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.system_state_name, self.mem_free, self.mem_max, self.objects_count, self.custom_attributes, updated_by, self.system_state_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.system_state_uid, self.system_state_name, self.mem_free, self.mem_max, self.objects_count, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.system_state_name, self.mem_free, self.mem_max, self.objects_count]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.system_state_name, self.mem_free, self.mem_max, self.objects_count, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_uid() == obj.get_uid()
    def update_uid(self, uid: str):
        self.system_state_uid = uid
    def update_uid_attributes(self, system_state_uid: str, system_state_name: str, mem_free: int, mem_max: int, objects_count: int):
        self.system_state_uid = system_state_uid
        self.system_state_name = system_state_name
        self.mem_free = mem_free
        self.mem_max = mem_max
        self.objects_count = objects_count
    def update_attributes(self, system_state_name: str, mem_free: int, mem_max: int, objects_count: int):
        self.system_state_name = system_state_name
        self.mem_free = mem_free
        self.mem_max = mem_max
        self.objects_count = objects_count


@dataclass(frozen=False)
class system_table_write_dto(base_write_dto):
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
    def __init__(self, system_table_uid: str, system_table_name: str, parent_system_table_uid: str | None, table_label: str, uid_name: str, table_group: str, table_code: str, table_type: str, table_category: str, cardinality: int, is_object: int, is_rich: int, is_tenant: int, is_local: int, table_comment: str, custom_attributes: str = "{}"):
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
        self.custom_attributes = custom_attributes
    @classmethod
    def empty_write(cls):
        return cls("", "", "", "", "", "", "", "", "", 0, 0, 0, 0, 0, "")
    @classmethod
    def default_write(cls):
        return cls(base_dto.get_random_uid(), "", "", "", "", "", "", "", "", 0, 0, 0, 0, 0, "")
    @classmethod
    def random_write(cls):
        return cls(base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), 0, 0, 0, 0, 0, base_dto.get_random_uid())
    @classmethod
    def new_write(cls, system_table_uid: str, system_table_name: str, parent_system_table_uid: str | None, table_label: str, uid_name: str, table_group: str, table_code: str, table_type: str, table_category: str, cardinality: int, is_object: int, is_rich: int, is_tenant: int, is_local: int, table_comment: str):
        return cls(system_table_uid, system_table_name, parent_system_table_uid, table_label, uid_name, table_group, table_code, table_type, table_category, cardinality, is_object, is_rich, is_tenant, is_local, table_comment)
    @classmethod
    def new_write_with_defaults(cls, system_table_uid: str = "", system_table_name: str = "", parent_system_table_uid: str | None = "", table_label: str = "", uid_name: str = "", table_group: str = "", table_code: str = "", table_type: str = "", table_category: str = "", cardinality: int = 0, is_object: int = 0, is_rich: int = 0, is_tenant: int = 0, is_local: int = 0, table_comment: str = ""):
        return cls(system_table_uid, system_table_name, parent_system_table_uid, table_label, uid_name, table_group, table_code, table_type, table_category, cardinality, is_object, is_rich, is_tenant, is_local, table_comment)
    @classmethod
    def new_write_random_uid(cls, system_table_name: str, parent_system_table_uid: str | None, table_label: str, uid_name: str, table_group: str, table_code: str, table_type: str, table_category: str, cardinality: int, is_object: int, is_rich: int, is_tenant: int, is_local: int, table_comment: str):
        return cls(base_dto.get_random_uid(), system_table_name, parent_system_table_uid, table_label, uid_name, table_group, table_code, table_type, table_category, cardinality, is_object, is_rich, is_tenant, is_local, table_comment)
    @classmethod
    def get_class_model(cls) -> base_model:
        return db_models.system_table_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["system_table_uid"], d["system_table_name"], d["parent_system_table_uid"], d["table_label"], d["uid_name"], d["table_group"], d["table_code"], d["table_type"], d["table_category"], d["cardinality"], d["is_object"], d["is_rich"], d["is_tenant"], d["is_local"], d["table_comment"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return system_table_write_dto(self.system_table_uid, self.system_table_name, self.parent_system_table_uid, self.table_label, self.uid_name, self.table_group, self.table_code, self.table_type, self.table_category, self.cardinality, self.is_object, self.is_rich, self.is_tenant, self.is_local, self.table_comment, self.custom_attributes)
    def clone_write_new_uid(self):
        return system_table_write_dto(base_dto.get_random_uid(), self.system_table_name, self.parent_system_table_uid, self.table_label, self.uid_name, self.table_group, self.table_code, self.table_type, self.table_category, self.cardinality, self.is_object, self.is_rich, self.is_tenant, self.is_local, self.table_comment, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return system_table_write_dto(uid, self.system_table_name, self.parent_system_table_uid, self.table_label, self.uid_name, self.table_group, self.table_code, self.table_type, self.table_category, self.cardinality, self.is_object, self.is_rich, self.is_tenant, self.is_local, self.table_comment, self.custom_attributes)
    def get_model(self) -> base_model:
        return db_models.system_table_model
    def get_uid(self) -> str:
        return self.system_table_uid
    def get_name(self) -> str:
        return self.system_table_name
    def get_list_values(self) -> list[any]:
        return [self.system_table_uid, self.system_table_name, self.parent_system_table_uid, self.table_label, self.uid_name, self.table_group, self.table_code, self.table_type, self.table_category, self.cardinality, self.is_object, self.is_rich, self.is_tenant, self.is_local, self.table_comment, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.system_table_uid, self.system_table_name, self.parent_system_table_uid, self.table_label, self.uid_name, self.table_group, self.table_code, self.table_type, self.table_category, self.cardinality, self.is_object, self.is_rich, self.is_tenant, self.is_local, self.table_comment]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.system_table_name, self.parent_system_table_uid, self.table_label, self.uid_name, self.table_group, self.table_code, self.table_type, self.table_category, self.cardinality, self.is_object, self.is_rich, self.is_tenant, self.is_local, self.table_comment, self.custom_attributes, updated_by, self.system_table_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.system_table_uid, self.system_table_name, self.parent_system_table_uid, self.table_label, self.uid_name, self.table_group, self.table_code, self.table_type, self.table_category, self.cardinality, self.is_object, self.is_rich, self.is_tenant, self.is_local, self.table_comment, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.system_table_name, self.parent_system_table_uid, self.table_label, self.uid_name, self.table_group, self.table_code, self.table_type, self.table_category, self.cardinality, self.is_object, self.is_rich, self.is_tenant, self.is_local, self.table_comment]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.system_table_name, self.parent_system_table_uid, self.table_label, self.uid_name, self.table_group, self.table_code, self.table_type, self.table_category, self.cardinality, self.is_object, self.is_rich, self.is_tenant, self.is_local, self.table_comment, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_uid() == obj.get_uid()
    def update_uid(self, uid: str):
        self.system_table_uid = uid
    def update_uid_attributes(self, system_table_uid: str, system_table_name: str, parent_system_table_uid: str | None, table_label: str, uid_name: str, table_group: str, table_code: str, table_type: str, table_category: str, cardinality: int, is_object: int, is_rich: int, is_tenant: int, is_local: int, table_comment: str):
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
    def update_attributes(self, system_table_name: str, parent_system_table_uid: str | None, table_label: str, uid_name: str, table_group: str, table_code: str, table_type: str, table_category: str, cardinality: int, is_object: int, is_rich: int, is_tenant: int, is_local: int, table_comment: str):
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


@dataclass(frozen=False)
class system_thread_write_dto(base_write_dto):
    system_thread_uid: str
    system_thread_name: str
    thread_name: str
    thread_id: int
    parent_object: str
    ticks_count: int
    is_alive: int
    sleep_time: int
    def __init__(self, system_thread_uid: str, system_thread_name: str, thread_name: str, thread_id: int, parent_object: str, ticks_count: int, is_alive: int, sleep_time: int, custom_attributes: str = "{}"):
        self.system_thread_uid = system_thread_uid
        self.system_thread_name = system_thread_name
        self.thread_name = thread_name
        self.thread_id = thread_id
        self.parent_object = parent_object
        self.ticks_count = ticks_count
        self.is_alive = is_alive
        self.sleep_time = sleep_time
        self.custom_attributes = custom_attributes
    @classmethod
    def empty_write(cls):
        return cls("", "", "", 0, "", 0, 0, 0)
    @classmethod
    def default_write(cls):
        return cls(base_dto.get_random_uid(), "", "", 0, "", 0, 0, 0)
    @classmethod
    def random_write(cls):
        return cls(base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), 0, base_dto.get_random_uid(), 0, 0, 0)
    @classmethod
    def new_write(cls, system_thread_uid: str, system_thread_name: str, thread_name: str, thread_id: int, parent_object: str, ticks_count: int, is_alive: int, sleep_time: int):
        return cls(system_thread_uid, system_thread_name, thread_name, thread_id, parent_object, ticks_count, is_alive, sleep_time)
    @classmethod
    def new_write_with_defaults(cls, system_thread_uid: str = "", system_thread_name: str = "", thread_name: str = "", thread_id: int = 0, parent_object: str = "", ticks_count: int = 0, is_alive: int = 0, sleep_time: int = 0):
        return cls(system_thread_uid, system_thread_name, thread_name, thread_id, parent_object, ticks_count, is_alive, sleep_time)
    @classmethod
    def new_write_random_uid(cls, system_thread_name: str, thread_name: str, thread_id: int, parent_object: str, ticks_count: int, is_alive: int, sleep_time: int):
        return cls(base_dto.get_random_uid(), system_thread_name, thread_name, thread_id, parent_object, ticks_count, is_alive, sleep_time)
    @classmethod
    def get_class_model(cls) -> base_model:
        return db_models.system_thread_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["system_thread_uid"], d["system_thread_name"], d["thread_name"], d["thread_id"], d["parent_object"], d["ticks_count"], d["is_alive"], d["sleep_time"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return system_thread_write_dto(self.system_thread_uid, self.system_thread_name, self.thread_name, self.thread_id, self.parent_object, self.ticks_count, self.is_alive, self.sleep_time, self.custom_attributes)
    def clone_write_new_uid(self):
        return system_thread_write_dto(base_dto.get_random_uid(), self.system_thread_name, self.thread_name, self.thread_id, self.parent_object, self.ticks_count, self.is_alive, self.sleep_time, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return system_thread_write_dto(uid, self.system_thread_name, self.thread_name, self.thread_id, self.parent_object, self.ticks_count, self.is_alive, self.sleep_time, self.custom_attributes)
    def get_model(self) -> base_model:
        return db_models.system_thread_model
    def get_uid(self) -> str:
        return self.system_thread_uid
    def get_name(self) -> str:
        return self.system_thread_name
    def get_list_values(self) -> list[any]:
        return [self.system_thread_uid, self.system_thread_name, self.thread_name, self.thread_id, self.parent_object, self.ticks_count, self.is_alive, self.sleep_time, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.system_thread_uid, self.system_thread_name, self.thread_name, self.thread_id, self.parent_object, self.ticks_count, self.is_alive, self.sleep_time]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.system_thread_name, self.thread_name, self.thread_id, self.parent_object, self.ticks_count, self.is_alive, self.sleep_time, self.custom_attributes, updated_by, self.system_thread_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.system_thread_uid, self.system_thread_name, self.thread_name, self.thread_id, self.parent_object, self.ticks_count, self.is_alive, self.sleep_time, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.system_thread_name, self.thread_name, self.thread_id, self.parent_object, self.ticks_count, self.is_alive, self.sleep_time]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.system_thread_name, self.thread_name, self.thread_id, self.parent_object, self.ticks_count, self.is_alive, self.sleep_time, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_uid() == obj.get_uid()
    def update_uid(self, uid: str):
        self.system_thread_uid = uid
    def update_uid_attributes(self, system_thread_uid: str, system_thread_name: str, thread_name: str, thread_id: int, parent_object: str, ticks_count: int, is_alive: int, sleep_time: int):
        self.system_thread_uid = system_thread_uid
        self.system_thread_name = system_thread_name
        self.thread_name = thread_name
        self.thread_id = thread_id
        self.parent_object = parent_object
        self.ticks_count = ticks_count
        self.is_alive = is_alive
        self.sleep_time = sleep_time
    def update_attributes(self, system_thread_name: str, thread_name: str, thread_id: int, parent_object: str, ticks_count: int, is_alive: int, sleep_time: int):
        self.system_thread_name = system_thread_name
        self.thread_name = thread_name
        self.thread_id = thread_id
        self.parent_object = parent_object
        self.ticks_count = ticks_count
        self.is_alive = is_alive
        self.sleep_time = sleep_time


@dataclass(frozen=False)
class system_version_write_dto(base_write_dto):
    system_version_uid: str
    system_version_name: str
    version_description: str
    def __init__(self, system_version_uid: str, system_version_name: str, version_description: str, custom_attributes: str = "{}"):
        self.system_version_uid = system_version_uid
        self.system_version_name = system_version_name
        self.version_description = version_description
        self.custom_attributes = custom_attributes
    @classmethod
    def empty_write(cls):
        return cls("", "", "")
    @classmethod
    def default_write(cls):
        return cls(base_dto.get_random_uid(), "", "")
    @classmethod
    def random_write(cls):
        return cls(base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid())
    @classmethod
    def new_write(cls, system_version_uid: str, system_version_name: str, version_description: str):
        return cls(system_version_uid, system_version_name, version_description)
    @classmethod
    def new_write_with_defaults(cls, system_version_uid: str = objects.system_version_uid, system_version_name: str = "", version_description: str = ""):
        return cls(system_version_uid, system_version_name, version_description)
    @classmethod
    def new_write_random_uid(cls, system_version_name: str, version_description: str):
        return cls(base_dto.get_random_uid(), system_version_name, version_description)
    @classmethod
    def get_class_model(cls) -> base_model:
        return db_models.system_version_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["system_version_uid"], d["system_version_name"], d["version_description"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return system_version_write_dto(self.system_version_uid, self.system_version_name, self.version_description, self.custom_attributes)
    def clone_write_new_uid(self):
        return system_version_write_dto(base_dto.get_random_uid(), self.system_version_name, self.version_description, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return system_version_write_dto(uid, self.system_version_name, self.version_description, self.custom_attributes)
    def get_model(self) -> base_model:
        return db_models.system_version_model
    def get_uid(self) -> str:
        return self.system_version_uid
    def get_name(self) -> str:
        return self.system_version_name
    def get_list_values(self) -> list[any]:
        return [self.system_version_uid, self.system_version_name, self.version_description, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.system_version_uid, self.system_version_name, self.version_description]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.system_version_name, self.version_description, self.custom_attributes, updated_by, self.system_version_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.system_version_uid, self.system_version_name, self.version_description, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.system_version_name, self.version_description]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.system_version_name, self.version_description, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_uid() == obj.get_uid()
    def update_uid(self, uid: str):
        self.system_version_uid = uid
    def update_uid_attributes(self, system_version_uid: str, system_version_name: str, version_description: str):
        self.system_version_uid = system_version_uid
        self.system_version_name = system_version_name
        self.version_description = version_description
    def update_attributes(self, system_version_name: str, version_description: str):
        self.system_version_name = system_version_name
        self.version_description = version_description


@dataclass(frozen=False)
class tenant_write_dto(base_write_dto):
    tenant_uid: str
    tenant_name: str
    country_uid: str
    tenant_type_uid: str
    tenant_category_uid: str
    tenant_status_uid: str
    tenant_code: str
    tenant_description: str
    start_date: datetime.datetime
    end_date: datetime.datetime | None
    is_internal: int
    is_system: int
    is_test: int
    account_uid: str | None
    def __init__(self, tenant_uid: str, tenant_name: str, country_uid: str, tenant_type_uid: str, tenant_category_uid: str, tenant_status_uid: str, tenant_code: str, tenant_description: str, start_date: datetime.datetime, end_date: datetime.datetime | None, is_internal: int, is_system: int, is_test: int, account_uid: str | None, custom_attributes: str = "{}"):
        self.tenant_uid = tenant_uid
        self.tenant_name = tenant_name
        self.country_uid = country_uid
        self.tenant_type_uid = tenant_type_uid
        self.tenant_category_uid = tenant_category_uid
        self.tenant_status_uid = tenant_status_uid
        self.tenant_code = tenant_code
        self.tenant_description = tenant_description
        self.start_date = start_date
        self.end_date = end_date
        self.is_internal = is_internal
        self.is_system = is_system
        self.is_test = is_test
        self.account_uid = account_uid
        self.custom_attributes = custom_attributes
    @classmethod
    def empty_write(cls):
        return cls("", "", "", "", "", "", "", "", datetime.datetime.now(), datetime.datetime.now(), 0, 0, 0, "")
    @classmethod
    def default_write(cls):
        return cls(base_dto.get_random_uid(), "", "", "", "", "", "", "", datetime.datetime.now(), datetime.datetime.now(), 0, 0, 0, "")
    @classmethod
    def random_write(cls):
        return cls(base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), datetime.datetime.now(), datetime.datetime.now(), 0, 0, 0, base_dto.get_random_uid())
    @classmethod
    def new_write(cls, tenant_uid: str, tenant_name: str, country_uid: str, tenant_type_uid: str, tenant_category_uid: str, tenant_status_uid: str, tenant_code: str, tenant_description: str, start_date: datetime.datetime, end_date: datetime.datetime | None, is_internal: int, is_system: int, is_test: int, account_uid: str | None):
        return cls(tenant_uid, tenant_name, country_uid, tenant_type_uid, tenant_category_uid, tenant_status_uid, tenant_code, tenant_description, start_date, end_date, is_internal, is_system, is_test, account_uid)
    @classmethod
    def new_write_with_defaults(cls, tenant_uid: str = "", tenant_name: str = "", country_uid: str = "", tenant_type_uid: str = "", tenant_category_uid: str = "", tenant_status_uid: str = "", tenant_code: str = "", tenant_description: str = "", start_date: datetime.datetime = datetime.datetime.now(), end_date: datetime.datetime | None = datetime.datetime.now(), is_internal: int = 0, is_system: int = 0, is_test: int = 0, account_uid: str | None = ""):
        return cls(tenant_uid, tenant_name, country_uid, tenant_type_uid, tenant_category_uid, tenant_status_uid, tenant_code, tenant_description, start_date, end_date, is_internal, is_system, is_test, account_uid)
    @classmethod
    def new_write_random_uid(cls, tenant_name: str, country_uid: str, tenant_type_uid: str, tenant_category_uid: str, tenant_status_uid: str, tenant_code: str, tenant_description: str, start_date: datetime.datetime, end_date: datetime.datetime | None, is_internal: int, is_system: int, is_test: int, account_uid: str | None):
        return cls(base_dto.get_random_uid(), tenant_name, country_uid, tenant_type_uid, tenant_category_uid, tenant_status_uid, tenant_code, tenant_description, start_date, end_date, is_internal, is_system, is_test, account_uid)
    @classmethod
    def get_class_model(cls) -> base_model:
        return db_models.tenant_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["tenant_uid"], d["tenant_name"], d["country_uid"], d["tenant_type_uid"], d["tenant_category_uid"], d["tenant_status_uid"], d["tenant_code"], d["tenant_description"], d["start_date"], d["end_date"], d["is_internal"], d["is_system"], d["is_test"], d["account_uid"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return tenant_write_dto(self.tenant_uid, self.tenant_name, self.country_uid, self.tenant_type_uid, self.tenant_category_uid, self.tenant_status_uid, self.tenant_code, self.tenant_description, self.start_date, self.end_date, self.is_internal, self.is_system, self.is_test, self.account_uid, self.custom_attributes)
    def clone_write_new_uid(self):
        return tenant_write_dto(base_dto.get_random_uid(), self.tenant_name, self.country_uid, self.tenant_type_uid, self.tenant_category_uid, self.tenant_status_uid, self.tenant_code, self.tenant_description, self.start_date, self.end_date, self.is_internal, self.is_system, self.is_test, self.account_uid, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return tenant_write_dto(uid, self.tenant_name, self.country_uid, self.tenant_type_uid, self.tenant_category_uid, self.tenant_status_uid, self.tenant_code, self.tenant_description, self.start_date, self.end_date, self.is_internal, self.is_system, self.is_test, self.account_uid, self.custom_attributes)
    def get_model(self) -> base_model:
        return db_models.tenant_model
    def get_uid(self) -> str:
        return self.tenant_uid
    def get_name(self) -> str:
        return self.tenant_name
    def get_list_values(self) -> list[any]:
        return [self.tenant_uid, self.tenant_name, self.country_uid, self.tenant_type_uid, self.tenant_category_uid, self.tenant_status_uid, self.tenant_code, self.tenant_description, self.start_date, self.end_date, self.is_internal, self.is_system, self.is_test, self.account_uid, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.tenant_uid, self.tenant_name, self.country_uid, self.tenant_type_uid, self.tenant_category_uid, self.tenant_status_uid, self.tenant_code, self.tenant_description, self.start_date, self.end_date, self.is_internal, self.is_system, self.is_test, self.account_uid]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.tenant_name, self.country_uid, self.tenant_type_uid, self.tenant_category_uid, self.tenant_status_uid, self.tenant_code, self.tenant_description, self.start_date, self.end_date, self.is_internal, self.is_system, self.is_test, self.account_uid, self.custom_attributes, updated_by, self.tenant_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.tenant_uid, self.tenant_name, self.country_uid, self.tenant_type_uid, self.tenant_category_uid, self.tenant_status_uid, self.tenant_code, self.tenant_description, self.start_date, self.end_date, self.is_internal, self.is_system, self.is_test, self.account_uid, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.tenant_name, self.country_uid, self.tenant_type_uid, self.tenant_category_uid, self.tenant_status_uid, self.tenant_code, self.tenant_description, self.start_date, self.end_date, self.is_internal, self.is_system, self.is_test, self.account_uid]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.tenant_name, self.country_uid, self.tenant_type_uid, self.tenant_category_uid, self.tenant_status_uid, self.tenant_code, self.tenant_description, self.start_date, self.end_date, self.is_internal, self.is_system, self.is_test, self.account_uid, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_uid() == obj.get_uid()
    def update_uid(self, uid: str):
        self.tenant_uid = uid
    def update_uid_attributes(self, tenant_uid: str, tenant_name: str, country_uid: str, tenant_type_uid: str, tenant_category_uid: str, tenant_status_uid: str, tenant_code: str, tenant_description: str, start_date: datetime.datetime, end_date: datetime.datetime | None, is_internal: int, is_system: int, is_test: int, account_uid: str | None):
        self.tenant_uid = tenant_uid
        self.tenant_name = tenant_name
        self.country_uid = country_uid
        self.tenant_type_uid = tenant_type_uid
        self.tenant_category_uid = tenant_category_uid
        self.tenant_status_uid = tenant_status_uid
        self.tenant_code = tenant_code
        self.tenant_description = tenant_description
        self.start_date = start_date
        self.end_date = end_date
        self.is_internal = is_internal
        self.is_system = is_system
        self.is_test = is_test
        self.account_uid = account_uid
    def update_attributes(self, tenant_name: str, country_uid: str, tenant_type_uid: str, tenant_category_uid: str, tenant_status_uid: str, tenant_code: str, tenant_description: str, start_date: datetime.datetime, end_date: datetime.datetime | None, is_internal: int, is_system: int, is_test: int, account_uid: str | None):
        self.tenant_name = tenant_name
        self.country_uid = country_uid
        self.tenant_type_uid = tenant_type_uid
        self.tenant_category_uid = tenant_category_uid
        self.tenant_status_uid = tenant_status_uid
        self.tenant_code = tenant_code
        self.tenant_description = tenant_description
        self.start_date = start_date
        self.end_date = end_date
        self.is_internal = is_internal
        self.is_system = is_system
        self.is_test = is_test
        self.account_uid = account_uid


@dataclass(frozen=False)
class tenant_account_write_dto(base_write_dto):
    tenant_account_uid: str
    tenant_account_name: str
    tenant_uid: str
    account_uid: str
    tenant_role_uid: str
    def __init__(self, tenant_account_uid: str, tenant_account_name: str, tenant_uid: str, account_uid: str, tenant_role_uid: str, custom_attributes: str = "{}"):
        self.tenant_account_uid = tenant_account_uid
        self.tenant_account_name = tenant_account_name
        self.tenant_uid = tenant_uid
        self.account_uid = account_uid
        self.tenant_role_uid = tenant_role_uid
        self.custom_attributes = custom_attributes
    @classmethod
    def empty_write(cls):
        return cls("", "", "", "", "")
    @classmethod
    def default_write(cls):
        return cls(base_dto.get_random_uid(), "", "", "", "")
    @classmethod
    def random_write(cls):
        return cls(base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid())
    @classmethod
    def new_write(cls, tenant_account_uid: str, tenant_account_name: str, tenant_uid: str, account_uid: str, tenant_role_uid: str):
        return cls(tenant_account_uid, tenant_account_name, tenant_uid, account_uid, tenant_role_uid)
    @classmethod
    def new_write_with_defaults(cls, tenant_account_uid: str = "", tenant_account_name: str = "", tenant_uid: str = "", account_uid: str = "", tenant_role_uid: str = ""):
        return cls(tenant_account_uid, tenant_account_name, tenant_uid, account_uid, tenant_role_uid)
    @classmethod
    def new_write_random_uid(cls, tenant_account_name: str, tenant_uid: str, account_uid: str, tenant_role_uid: str):
        return cls(base_dto.get_random_uid(), tenant_account_name, tenant_uid, account_uid, tenant_role_uid)
    @classmethod
    def get_class_model(cls) -> base_model:
        return db_models.tenant_account_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["tenant_account_uid"], d["tenant_account_name"], d["tenant_uid"], d["account_uid"], d["tenant_role_uid"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return tenant_account_write_dto(self.tenant_account_uid, self.tenant_account_name, self.tenant_uid, self.account_uid, self.tenant_role_uid, self.custom_attributes)
    def clone_write_new_uid(self):
        return tenant_account_write_dto(base_dto.get_random_uid(), self.tenant_account_name, self.tenant_uid, self.account_uid, self.tenant_role_uid, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return tenant_account_write_dto(uid, self.tenant_account_name, self.tenant_uid, self.account_uid, self.tenant_role_uid, self.custom_attributes)
    def get_model(self) -> base_model:
        return db_models.tenant_account_model
    def get_uid(self) -> str:
        return self.tenant_account_uid
    def get_name(self) -> str:
        return self.tenant_account_name
    def get_list_values(self) -> list[any]:
        return [self.tenant_account_uid, self.tenant_account_name, self.tenant_uid, self.account_uid, self.tenant_role_uid, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.tenant_account_uid, self.tenant_account_name, self.tenant_uid, self.account_uid, self.tenant_role_uid]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.tenant_account_name, self.tenant_uid, self.account_uid, self.tenant_role_uid, self.custom_attributes, updated_by, self.tenant_account_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.tenant_account_uid, self.tenant_account_name, self.tenant_uid, self.account_uid, self.tenant_role_uid, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.tenant_account_name, self.tenant_uid, self.account_uid, self.tenant_role_uid]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.tenant_account_name, self.tenant_uid, self.account_uid, self.tenant_role_uid, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_uid() == obj.get_uid()
    def update_uid(self, uid: str):
        self.tenant_account_uid = uid
    def update_uid_attributes(self, tenant_account_uid: str, tenant_account_name: str, tenant_uid: str, account_uid: str, tenant_role_uid: str):
        self.tenant_account_uid = tenant_account_uid
        self.tenant_account_name = tenant_account_name
        self.tenant_uid = tenant_uid
        self.account_uid = account_uid
        self.tenant_role_uid = tenant_role_uid
    def update_attributes(self, tenant_account_name: str, tenant_uid: str, account_uid: str, tenant_role_uid: str):
        self.tenant_account_name = tenant_account_name
        self.tenant_uid = tenant_uid
        self.account_uid = account_uid
        self.tenant_role_uid = tenant_role_uid


@dataclass(frozen=False)
class tenant_category_write_dto(base_write_dto):
    tenant_category_uid: str
    tenant_category_name: str
    tenant_category_description: str
    def __init__(self, tenant_category_uid: str, tenant_category_name: str, tenant_category_description: str, custom_attributes: str = "{}"):
        self.tenant_category_uid = tenant_category_uid
        self.tenant_category_name = tenant_category_name
        self.tenant_category_description = tenant_category_description
        self.custom_attributes = custom_attributes
    @classmethod
    def empty_write(cls):
        return cls("", "", "")
    @classmethod
    def default_write(cls):
        return cls(base_dto.get_random_uid(), "", "")
    @classmethod
    def random_write(cls):
        return cls(base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid())
    @classmethod
    def new_write(cls, tenant_category_uid: str, tenant_category_name: str, tenant_category_description: str):
        return cls(tenant_category_uid, tenant_category_name, tenant_category_description)
    @classmethod
    def new_write_with_defaults(cls, tenant_category_uid: str = "", tenant_category_name: str = "", tenant_category_description: str = ""):
        return cls(tenant_category_uid, tenant_category_name, tenant_category_description)
    @classmethod
    def new_write_random_uid(cls, tenant_category_name: str, tenant_category_description: str):
        return cls(base_dto.get_random_uid(), tenant_category_name, tenant_category_description)
    @classmethod
    def get_class_model(cls) -> base_model:
        return db_models.tenant_category_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["tenant_category_uid"], d["tenant_category_name"], d["tenant_category_description"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return tenant_category_write_dto(self.tenant_category_uid, self.tenant_category_name, self.tenant_category_description, self.custom_attributes)
    def clone_write_new_uid(self):
        return tenant_category_write_dto(base_dto.get_random_uid(), self.tenant_category_name, self.tenant_category_description, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return tenant_category_write_dto(uid, self.tenant_category_name, self.tenant_category_description, self.custom_attributes)
    def get_model(self) -> base_model:
        return db_models.tenant_category_model
    def get_uid(self) -> str:
        return self.tenant_category_uid
    def get_name(self) -> str:
        return self.tenant_category_name
    def get_list_values(self) -> list[any]:
        return [self.tenant_category_uid, self.tenant_category_name, self.tenant_category_description, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.tenant_category_uid, self.tenant_category_name, self.tenant_category_description]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.tenant_category_name, self.tenant_category_description, self.custom_attributes, updated_by, self.tenant_category_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.tenant_category_uid, self.tenant_category_name, self.tenant_category_description, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.tenant_category_name, self.tenant_category_description]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.tenant_category_name, self.tenant_category_description, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_uid() == obj.get_uid()
    def update_uid(self, uid: str):
        self.tenant_category_uid = uid
    def update_uid_attributes(self, tenant_category_uid: str, tenant_category_name: str, tenant_category_description: str):
        self.tenant_category_uid = tenant_category_uid
        self.tenant_category_name = tenant_category_name
        self.tenant_category_description = tenant_category_description
    def update_attributes(self, tenant_category_name: str, tenant_category_description: str):
        self.tenant_category_name = tenant_category_name
        self.tenant_category_description = tenant_category_description


@dataclass(frozen=False)
class tenant_country_write_dto(base_write_dto):
    tenant_country_uid: str
    tenant_country_name: str
    country_uid: str
    tenant_uid: str
    country_priority: int
    def __init__(self, tenant_country_uid: str, tenant_country_name: str, country_uid: str, tenant_uid: str, country_priority: int, custom_attributes: str = "{}"):
        self.tenant_country_uid = tenant_country_uid
        self.tenant_country_name = tenant_country_name
        self.country_uid = country_uid
        self.tenant_uid = tenant_uid
        self.country_priority = country_priority
        self.custom_attributes = custom_attributes
    @classmethod
    def empty_write(cls):
        return cls("", "", "", "", 0)
    @classmethod
    def default_write(cls):
        return cls(base_dto.get_random_uid(), "", "", "", 0)
    @classmethod
    def random_write(cls):
        return cls(base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), 0)
    @classmethod
    def new_write(cls, tenant_country_uid: str, tenant_country_name: str, country_uid: str, tenant_uid: str, country_priority: int):
        return cls(tenant_country_uid, tenant_country_name, country_uid, tenant_uid, country_priority)
    @classmethod
    def new_write_with_defaults(cls, tenant_country_uid: str = "", tenant_country_name: str = "", country_uid: str = "", tenant_uid: str = "", country_priority: int = 0):
        return cls(tenant_country_uid, tenant_country_name, country_uid, tenant_uid, country_priority)
    @classmethod
    def new_write_random_uid(cls, tenant_country_name: str, country_uid: str, tenant_uid: str, country_priority: int):
        return cls(base_dto.get_random_uid(), tenant_country_name, country_uid, tenant_uid, country_priority)
    @classmethod
    def get_class_model(cls) -> base_model:
        return db_models.tenant_country_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["tenant_country_uid"], d["tenant_country_name"], d["country_uid"], d["tenant_uid"], d["country_priority"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return tenant_country_write_dto(self.tenant_country_uid, self.tenant_country_name, self.country_uid, self.tenant_uid, self.country_priority, self.custom_attributes)
    def clone_write_new_uid(self):
        return tenant_country_write_dto(base_dto.get_random_uid(), self.tenant_country_name, self.country_uid, self.tenant_uid, self.country_priority, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return tenant_country_write_dto(uid, self.tenant_country_name, self.country_uid, self.tenant_uid, self.country_priority, self.custom_attributes)
    def get_model(self) -> base_model:
        return db_models.tenant_country_model
    def get_uid(self) -> str:
        return self.tenant_country_uid
    def get_name(self) -> str:
        return self.tenant_country_name
    def get_list_values(self) -> list[any]:
        return [self.tenant_country_uid, self.tenant_country_name, self.country_uid, self.tenant_uid, self.country_priority, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.tenant_country_uid, self.tenant_country_name, self.country_uid, self.tenant_uid, self.country_priority]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.tenant_country_name, self.country_uid, self.tenant_uid, self.country_priority, self.custom_attributes, updated_by, self.tenant_country_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.tenant_country_uid, self.tenant_country_name, self.country_uid, self.tenant_uid, self.country_priority, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.tenant_country_name, self.country_uid, self.tenant_uid, self.country_priority]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.tenant_country_name, self.country_uid, self.tenant_uid, self.country_priority, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_uid() == obj.get_uid()
    def update_uid(self, uid: str):
        self.tenant_country_uid = uid
    def update_uid_attributes(self, tenant_country_uid: str, tenant_country_name: str, country_uid: str, tenant_uid: str, country_priority: int):
        self.tenant_country_uid = tenant_country_uid
        self.tenant_country_name = tenant_country_name
        self.country_uid = country_uid
        self.tenant_uid = tenant_uid
        self.country_priority = country_priority
    def update_attributes(self, tenant_country_name: str, country_uid: str, tenant_uid: str, country_priority: int):
        self.tenant_country_name = tenant_country_name
        self.country_uid = country_uid
        self.tenant_uid = tenant_uid
        self.country_priority = country_priority


@dataclass(frozen=False)
class tenant_license_write_dto(base_write_dto):
    tenant_license_uid: str
    tenant_license_name: str
    tenant_uid: str
    system_license_uid: str
    start_date: datetime.datetime
    end_date: datetime.datetime
    accounts_count: int
    is_approved: int
    def __init__(self, tenant_license_uid: str, tenant_license_name: str, tenant_uid: str, system_license_uid: str, start_date: datetime.datetime, end_date: datetime.datetime, accounts_count: int, is_approved: int, custom_attributes: str = "{}"):
        self.tenant_license_uid = tenant_license_uid
        self.tenant_license_name = tenant_license_name
        self.tenant_uid = tenant_uid
        self.system_license_uid = system_license_uid
        self.start_date = start_date
        self.end_date = end_date
        self.accounts_count = accounts_count
        self.is_approved = is_approved
        self.custom_attributes = custom_attributes
    @classmethod
    def empty_write(cls):
        return cls("", "", "", "", datetime.datetime.now(), datetime.datetime.now(), 0, 0)
    @classmethod
    def default_write(cls):
        return cls(base_dto.get_random_uid(), "", "", "", datetime.datetime.now(), datetime.datetime.now(), 0, 0)
    @classmethod
    def random_write(cls):
        return cls(base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), datetime.datetime.now(), datetime.datetime.now(), 0, 0)
    @classmethod
    def new_write(cls, tenant_license_uid: str, tenant_license_name: str, tenant_uid: str, system_license_uid: str, start_date: datetime.datetime, end_date: datetime.datetime, accounts_count: int, is_approved: int):
        return cls(tenant_license_uid, tenant_license_name, tenant_uid, system_license_uid, start_date, end_date, accounts_count, is_approved)
    @classmethod
    def new_write_with_defaults(cls, tenant_license_uid: str = "", tenant_license_name: str = "", tenant_uid: str = "", system_license_uid: str = "", start_date: datetime.datetime = datetime.datetime.now(), end_date: datetime.datetime = datetime.datetime.now(), accounts_count: int = 0, is_approved: int = 0):
        return cls(tenant_license_uid, tenant_license_name, tenant_uid, system_license_uid, start_date, end_date, accounts_count, is_approved)
    @classmethod
    def new_write_random_uid(cls, tenant_license_name: str, tenant_uid: str, system_license_uid: str, start_date: datetime.datetime, end_date: datetime.datetime, accounts_count: int, is_approved: int):
        return cls(base_dto.get_random_uid(), tenant_license_name, tenant_uid, system_license_uid, start_date, end_date, accounts_count, is_approved)
    @classmethod
    def get_class_model(cls) -> base_model:
        return db_models.tenant_license_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["tenant_license_uid"], d["tenant_license_name"], d["tenant_uid"], d["system_license_uid"], d["start_date"], d["end_date"], d["accounts_count"], d["is_approved"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return tenant_license_write_dto(self.tenant_license_uid, self.tenant_license_name, self.tenant_uid, self.system_license_uid, self.start_date, self.end_date, self.accounts_count, self.is_approved, self.custom_attributes)
    def clone_write_new_uid(self):
        return tenant_license_write_dto(base_dto.get_random_uid(), self.tenant_license_name, self.tenant_uid, self.system_license_uid, self.start_date, self.end_date, self.accounts_count, self.is_approved, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return tenant_license_write_dto(uid, self.tenant_license_name, self.tenant_uid, self.system_license_uid, self.start_date, self.end_date, self.accounts_count, self.is_approved, self.custom_attributes)
    def get_model(self) -> base_model:
        return db_models.tenant_license_model
    def get_uid(self) -> str:
        return self.tenant_license_uid
    def get_name(self) -> str:
        return self.tenant_license_name
    def get_list_values(self) -> list[any]:
        return [self.tenant_license_uid, self.tenant_license_name, self.tenant_uid, self.system_license_uid, self.start_date, self.end_date, self.accounts_count, self.is_approved, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.tenant_license_uid, self.tenant_license_name, self.tenant_uid, self.system_license_uid, self.start_date, self.end_date, self.accounts_count, self.is_approved]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.tenant_license_name, self.tenant_uid, self.system_license_uid, self.start_date, self.end_date, self.accounts_count, self.is_approved, self.custom_attributes, updated_by, self.tenant_license_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.tenant_license_uid, self.tenant_license_name, self.tenant_uid, self.system_license_uid, self.start_date, self.end_date, self.accounts_count, self.is_approved, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.tenant_license_name, self.tenant_uid, self.system_license_uid, self.start_date, self.end_date, self.accounts_count, self.is_approved]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.tenant_license_name, self.tenant_uid, self.system_license_uid, self.start_date, self.end_date, self.accounts_count, self.is_approved, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_uid() == obj.get_uid()
    def update_uid(self, uid: str):
        self.tenant_license_uid = uid
    def update_uid_attributes(self, tenant_license_uid: str, tenant_license_name: str, tenant_uid: str, system_license_uid: str, start_date: datetime.datetime, end_date: datetime.datetime, accounts_count: int, is_approved: int):
        self.tenant_license_uid = tenant_license_uid
        self.tenant_license_name = tenant_license_name
        self.tenant_uid = tenant_uid
        self.system_license_uid = system_license_uid
        self.start_date = start_date
        self.end_date = end_date
        self.accounts_count = accounts_count
        self.is_approved = is_approved
    def update_attributes(self, tenant_license_name: str, tenant_uid: str, system_license_uid: str, start_date: datetime.datetime, end_date: datetime.datetime, accounts_count: int, is_approved: int):
        self.tenant_license_name = tenant_license_name
        self.tenant_uid = tenant_uid
        self.system_license_uid = system_license_uid
        self.start_date = start_date
        self.end_date = end_date
        self.accounts_count = accounts_count
        self.is_approved = is_approved


@dataclass(frozen=False)
class tenant_payment_write_dto(base_write_dto):
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
    def __init__(self, tenant_payment_uid: str, tenant_payment_name: str, tenant_uid: str, account_uid: str, currency_uid: str, tenant_payment_type_uid: str, start_date: datetime.datetime, end_date: datetime.datetime | None, payment_value: str, source_number: str, source_reference: str, is_approved: int, custom_attributes: str = "{}"):
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
        self.custom_attributes = custom_attributes
    @classmethod
    def empty_write(cls):
        return cls("", "", "", "", "", "", datetime.datetime.now(), datetime.datetime.now(), "", "", "", 0)
    @classmethod
    def default_write(cls):
        return cls(base_dto.get_random_uid(), "", "", "", "", "", datetime.datetime.now(), datetime.datetime.now(), "", "", "", 0)
    @classmethod
    def random_write(cls):
        return cls(base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), datetime.datetime.now(), datetime.datetime.now(), "", base_dto.get_random_uid(), base_dto.get_random_uid(), 0)
    @classmethod
    def new_write(cls, tenant_payment_uid: str, tenant_payment_name: str, tenant_uid: str, account_uid: str, currency_uid: str, tenant_payment_type_uid: str, start_date: datetime.datetime, end_date: datetime.datetime | None, payment_value: str, source_number: str, source_reference: str, is_approved: int):
        return cls(tenant_payment_uid, tenant_payment_name, tenant_uid, account_uid, currency_uid, tenant_payment_type_uid, start_date, end_date, payment_value, source_number, source_reference, is_approved)
    @classmethod
    def new_write_with_defaults(cls, tenant_payment_uid: str = "", tenant_payment_name: str = "", tenant_uid: str = "", account_uid: str = "", currency_uid: str = "", tenant_payment_type_uid: str = "", start_date: datetime.datetime = datetime.datetime.now(), end_date: datetime.datetime | None = datetime.datetime.now(), payment_value: str = "", source_number: str = "", source_reference: str = "", is_approved: int = 0):
        return cls(tenant_payment_uid, tenant_payment_name, tenant_uid, account_uid, currency_uid, tenant_payment_type_uid, start_date, end_date, payment_value, source_number, source_reference, is_approved)
    @classmethod
    def new_write_random_uid(cls, tenant_payment_name: str, tenant_uid: str, account_uid: str, currency_uid: str, tenant_payment_type_uid: str, start_date: datetime.datetime, end_date: datetime.datetime | None, payment_value: str, source_number: str, source_reference: str, is_approved: int):
        return cls(base_dto.get_random_uid(), tenant_payment_name, tenant_uid, account_uid, currency_uid, tenant_payment_type_uid, start_date, end_date, payment_value, source_number, source_reference, is_approved)
    @classmethod
    def get_class_model(cls) -> base_model:
        return db_models.tenant_payment_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["tenant_payment_uid"], d["tenant_payment_name"], d["tenant_uid"], d["account_uid"], d["currency_uid"], d["tenant_payment_type_uid"], d["start_date"], d["end_date"], d["payment_value"], d["source_number"], d["source_reference"], d["is_approved"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return tenant_payment_write_dto(self.tenant_payment_uid, self.tenant_payment_name, self.tenant_uid, self.account_uid, self.currency_uid, self.tenant_payment_type_uid, self.start_date, self.end_date, self.payment_value, self.source_number, self.source_reference, self.is_approved, self.custom_attributes)
    def clone_write_new_uid(self):
        return tenant_payment_write_dto(base_dto.get_random_uid(), self.tenant_payment_name, self.tenant_uid, self.account_uid, self.currency_uid, self.tenant_payment_type_uid, self.start_date, self.end_date, self.payment_value, self.source_number, self.source_reference, self.is_approved, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return tenant_payment_write_dto(uid, self.tenant_payment_name, self.tenant_uid, self.account_uid, self.currency_uid, self.tenant_payment_type_uid, self.start_date, self.end_date, self.payment_value, self.source_number, self.source_reference, self.is_approved, self.custom_attributes)
    def get_model(self) -> base_model:
        return db_models.tenant_payment_model
    def get_uid(self) -> str:
        return self.tenant_payment_uid
    def get_name(self) -> str:
        return self.tenant_payment_name
    def get_list_values(self) -> list[any]:
        return [self.tenant_payment_uid, self.tenant_payment_name, self.tenant_uid, self.account_uid, self.currency_uid, self.tenant_payment_type_uid, self.start_date, self.end_date, self.payment_value, self.source_number, self.source_reference, self.is_approved, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.tenant_payment_uid, self.tenant_payment_name, self.tenant_uid, self.account_uid, self.currency_uid, self.tenant_payment_type_uid, self.start_date, self.end_date, self.payment_value, self.source_number, self.source_reference, self.is_approved]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.tenant_payment_name, self.tenant_uid, self.account_uid, self.currency_uid, self.tenant_payment_type_uid, self.start_date, self.end_date, self.payment_value, self.source_number, self.source_reference, self.is_approved, self.custom_attributes, updated_by, self.tenant_payment_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.tenant_payment_uid, self.tenant_payment_name, self.tenant_uid, self.account_uid, self.currency_uid, self.tenant_payment_type_uid, self.start_date, self.end_date, self.payment_value, self.source_number, self.source_reference, self.is_approved, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.tenant_payment_name, self.tenant_uid, self.account_uid, self.currency_uid, self.tenant_payment_type_uid, self.start_date, self.end_date, self.payment_value, self.source_number, self.source_reference, self.is_approved]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.tenant_payment_name, self.tenant_uid, self.account_uid, self.currency_uid, self.tenant_payment_type_uid, self.start_date, self.end_date, self.payment_value, self.source_number, self.source_reference, self.is_approved, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_uid() == obj.get_uid()
    def update_uid(self, uid: str):
        self.tenant_payment_uid = uid
    def update_uid_attributes(self, tenant_payment_uid: str, tenant_payment_name: str, tenant_uid: str, account_uid: str, currency_uid: str, tenant_payment_type_uid: str, start_date: datetime.datetime, end_date: datetime.datetime | None, payment_value: str, source_number: str, source_reference: str, is_approved: int):
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
    def update_attributes(self, tenant_payment_name: str, tenant_uid: str, account_uid: str, currency_uid: str, tenant_payment_type_uid: str, start_date: datetime.datetime, end_date: datetime.datetime | None, payment_value: str, source_number: str, source_reference: str, is_approved: int):
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


@dataclass(frozen=False)
class tenant_payment_type_write_dto(base_write_dto):
    tenant_payment_type_uid: str
    tenant_payment_type_name: str
    def __init__(self, tenant_payment_type_uid: str, tenant_payment_type_name: str, custom_attributes: str = "{}"):
        self.tenant_payment_type_uid = tenant_payment_type_uid
        self.tenant_payment_type_name = tenant_payment_type_name
        self.custom_attributes = custom_attributes
    @classmethod
    def empty_write(cls):
        return cls("", "")
    @classmethod
    def default_write(cls):
        return cls(base_dto.get_random_uid(), "")
    @classmethod
    def random_write(cls):
        return cls(base_dto.get_random_uid(), base_dto.get_random_uid())
    @classmethod
    def new_write(cls, tenant_payment_type_uid: str, tenant_payment_type_name: str):
        return cls(tenant_payment_type_uid, tenant_payment_type_name)
    @classmethod
    def new_write_with_defaults(cls, tenant_payment_type_uid: str = "", tenant_payment_type_name: str = ""):
        return cls(tenant_payment_type_uid, tenant_payment_type_name)
    @classmethod
    def new_write_random_uid(cls, tenant_payment_type_name: str):
        return cls(base_dto.get_random_uid(), tenant_payment_type_name)
    @classmethod
    def get_class_model(cls) -> base_model:
        return db_models.tenant_payment_type_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["tenant_payment_type_uid"], d["tenant_payment_type_name"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return tenant_payment_type_write_dto(self.tenant_payment_type_uid, self.tenant_payment_type_name, self.custom_attributes)
    def clone_write_new_uid(self):
        return tenant_payment_type_write_dto(base_dto.get_random_uid(), self.tenant_payment_type_name, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return tenant_payment_type_write_dto(uid, self.tenant_payment_type_name, self.custom_attributes)
    def get_model(self) -> base_model:
        return db_models.tenant_payment_type_model
    def get_uid(self) -> str:
        return self.tenant_payment_type_uid
    def get_name(self) -> str:
        return self.tenant_payment_type_name
    def get_list_values(self) -> list[any]:
        return [self.tenant_payment_type_uid, self.tenant_payment_type_name, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.tenant_payment_type_uid, self.tenant_payment_type_name]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.tenant_payment_type_name, self.custom_attributes, updated_by, self.tenant_payment_type_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.tenant_payment_type_uid, self.tenant_payment_type_name, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.tenant_payment_type_name]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.tenant_payment_type_name, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_uid() == obj.get_uid()
    def update_uid(self, uid: str):
        self.tenant_payment_type_uid = uid
    def update_uid_attributes(self, tenant_payment_type_uid: str, tenant_payment_type_name: str):
        self.tenant_payment_type_uid = tenant_payment_type_uid
        self.tenant_payment_type_name = tenant_payment_type_name
    def update_attributes(self, tenant_payment_type_name: str):
        self.tenant_payment_type_name = tenant_payment_type_name


@dataclass(frozen=False)
class tenant_role_write_dto(base_write_dto):
    tenant_role_uid: str
    tenant_role_name: str
    role_description: str
    def __init__(self, tenant_role_uid: str, tenant_role_name: str, role_description: str, custom_attributes: str = "{}"):
        self.tenant_role_uid = tenant_role_uid
        self.tenant_role_name = tenant_role_name
        self.role_description = role_description
        self.custom_attributes = custom_attributes
    @classmethod
    def empty_write(cls):
        return cls("", "", "")
    @classmethod
    def default_write(cls):
        return cls(base_dto.get_random_uid(), "", "")
    @classmethod
    def random_write(cls):
        return cls(base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid())
    @classmethod
    def new_write(cls, tenant_role_uid: str, tenant_role_name: str, role_description: str):
        return cls(tenant_role_uid, tenant_role_name, role_description)
    @classmethod
    def new_write_with_defaults(cls, tenant_role_uid: str = "", tenant_role_name: str = "", role_description: str = ""):
        return cls(tenant_role_uid, tenant_role_name, role_description)
    @classmethod
    def new_write_random_uid(cls, tenant_role_name: str, role_description: str):
        return cls(base_dto.get_random_uid(), tenant_role_name, role_description)
    @classmethod
    def get_class_model(cls) -> base_model:
        return db_models.tenant_role_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["tenant_role_uid"], d["tenant_role_name"], d["role_description"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return tenant_role_write_dto(self.tenant_role_uid, self.tenant_role_name, self.role_description, self.custom_attributes)
    def clone_write_new_uid(self):
        return tenant_role_write_dto(base_dto.get_random_uid(), self.tenant_role_name, self.role_description, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return tenant_role_write_dto(uid, self.tenant_role_name, self.role_description, self.custom_attributes)
    def get_model(self) -> base_model:
        return db_models.tenant_role_model
    def get_uid(self) -> str:
        return self.tenant_role_uid
    def get_name(self) -> str:
        return self.tenant_role_name
    def get_list_values(self) -> list[any]:
        return [self.tenant_role_uid, self.tenant_role_name, self.role_description, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.tenant_role_uid, self.tenant_role_name, self.role_description]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.tenant_role_name, self.role_description, self.custom_attributes, updated_by, self.tenant_role_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.tenant_role_uid, self.tenant_role_name, self.role_description, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.tenant_role_name, self.role_description]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.tenant_role_name, self.role_description, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_uid() == obj.get_uid()
    def update_uid(self, uid: str):
        self.tenant_role_uid = uid
    def update_uid_attributes(self, tenant_role_uid: str, tenant_role_name: str, role_description: str):
        self.tenant_role_uid = tenant_role_uid
        self.tenant_role_name = tenant_role_name
        self.role_description = role_description
    def update_attributes(self, tenant_role_name: str, role_description: str):
        self.tenant_role_name = tenant_role_name
        self.role_description = role_description


@dataclass(frozen=False)
class tenant_status_write_dto(base_write_dto):
    tenant_status_uid: str
    tenant_status_name: str
    tenant_status_description: str
    def __init__(self, tenant_status_uid: str, tenant_status_name: str, tenant_status_description: str, custom_attributes: str = "{}"):
        self.tenant_status_uid = tenant_status_uid
        self.tenant_status_name = tenant_status_name
        self.tenant_status_description = tenant_status_description
        self.custom_attributes = custom_attributes
    @classmethod
    def empty_write(cls):
        return cls("", "", "")
    @classmethod
    def default_write(cls):
        return cls(base_dto.get_random_uid(), "", "")
    @classmethod
    def random_write(cls):
        return cls(base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid())
    @classmethod
    def new_write(cls, tenant_status_uid: str, tenant_status_name: str, tenant_status_description: str):
        return cls(tenant_status_uid, tenant_status_name, tenant_status_description)
    @classmethod
    def new_write_with_defaults(cls, tenant_status_uid: str = "", tenant_status_name: str = "", tenant_status_description: str = ""):
        return cls(tenant_status_uid, tenant_status_name, tenant_status_description)
    @classmethod
    def new_write_random_uid(cls, tenant_status_name: str, tenant_status_description: str):
        return cls(base_dto.get_random_uid(), tenant_status_name, tenant_status_description)
    @classmethod
    def get_class_model(cls) -> base_model:
        return db_models.tenant_status_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["tenant_status_uid"], d["tenant_status_name"], d["tenant_status_description"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return tenant_status_write_dto(self.tenant_status_uid, self.tenant_status_name, self.tenant_status_description, self.custom_attributes)
    def clone_write_new_uid(self):
        return tenant_status_write_dto(base_dto.get_random_uid(), self.tenant_status_name, self.tenant_status_description, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return tenant_status_write_dto(uid, self.tenant_status_name, self.tenant_status_description, self.custom_attributes)
    def get_model(self) -> base_model:
        return db_models.tenant_status_model
    def get_uid(self) -> str:
        return self.tenant_status_uid
    def get_name(self) -> str:
        return self.tenant_status_name
    def get_list_values(self) -> list[any]:
        return [self.tenant_status_uid, self.tenant_status_name, self.tenant_status_description, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.tenant_status_uid, self.tenant_status_name, self.tenant_status_description]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.tenant_status_name, self.tenant_status_description, self.custom_attributes, updated_by, self.tenant_status_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.tenant_status_uid, self.tenant_status_name, self.tenant_status_description, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.tenant_status_name, self.tenant_status_description]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.tenant_status_name, self.tenant_status_description, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_uid() == obj.get_uid()
    def update_uid(self, uid: str):
        self.tenant_status_uid = uid
    def update_uid_attributes(self, tenant_status_uid: str, tenant_status_name: str, tenant_status_description: str):
        self.tenant_status_uid = tenant_status_uid
        self.tenant_status_name = tenant_status_name
        self.tenant_status_description = tenant_status_description
    def update_attributes(self, tenant_status_name: str, tenant_status_description: str):
        self.tenant_status_name = tenant_status_name
        self.tenant_status_description = tenant_status_description


@dataclass(frozen=False)
class tenant_type_write_dto(base_write_dto):
    tenant_type_uid: str
    tenant_type_name: str
    tenant_type_description: str
    tenant_class: str
    def __init__(self, tenant_type_uid: str, tenant_type_name: str, tenant_type_description: str, tenant_class: str, custom_attributes: str = "{}"):
        self.tenant_type_uid = tenant_type_uid
        self.tenant_type_name = tenant_type_name
        self.tenant_type_description = tenant_type_description
        self.tenant_class = tenant_class
        self.custom_attributes = custom_attributes
    @classmethod
    def empty_write(cls):
        return cls("", "", "", "")
    @classmethod
    def default_write(cls):
        return cls(base_dto.get_random_uid(), "", "", "")
    @classmethod
    def random_write(cls):
        return cls(base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid())
    @classmethod
    def new_write(cls, tenant_type_uid: str, tenant_type_name: str, tenant_type_description: str, tenant_class: str):
        return cls(tenant_type_uid, tenant_type_name, tenant_type_description, tenant_class)
    @classmethod
    def new_write_with_defaults(cls, tenant_type_uid: str = "", tenant_type_name: str = "", tenant_type_description: str = "", tenant_class: str = ""):
        return cls(tenant_type_uid, tenant_type_name, tenant_type_description, tenant_class)
    @classmethod
    def new_write_random_uid(cls, tenant_type_name: str, tenant_type_description: str, tenant_class: str):
        return cls(base_dto.get_random_uid(), tenant_type_name, tenant_type_description, tenant_class)
    @classmethod
    def get_class_model(cls) -> base_model:
        return db_models.tenant_type_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["tenant_type_uid"], d["tenant_type_name"], d["tenant_type_description"], d["tenant_class"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return tenant_type_write_dto(self.tenant_type_uid, self.tenant_type_name, self.tenant_type_description, self.tenant_class, self.custom_attributes)
    def clone_write_new_uid(self):
        return tenant_type_write_dto(base_dto.get_random_uid(), self.tenant_type_name, self.tenant_type_description, self.tenant_class, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return tenant_type_write_dto(uid, self.tenant_type_name, self.tenant_type_description, self.tenant_class, self.custom_attributes)
    def get_model(self) -> base_model:
        return db_models.tenant_type_model
    def get_uid(self) -> str:
        return self.tenant_type_uid
    def get_name(self) -> str:
        return self.tenant_type_name
    def get_list_values(self) -> list[any]:
        return [self.tenant_type_uid, self.tenant_type_name, self.tenant_type_description, self.tenant_class, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.tenant_type_uid, self.tenant_type_name, self.tenant_type_description, self.tenant_class]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.tenant_type_name, self.tenant_type_description, self.tenant_class, self.custom_attributes, updated_by, self.tenant_type_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.tenant_type_uid, self.tenant_type_name, self.tenant_type_description, self.tenant_class, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.tenant_type_name, self.tenant_type_description, self.tenant_class]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.tenant_type_name, self.tenant_type_description, self.tenant_class, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_uid() == obj.get_uid()
    def update_uid(self, uid: str):
        self.tenant_type_uid = uid
    def update_uid_attributes(self, tenant_type_uid: str, tenant_type_name: str, tenant_type_description: str, tenant_class: str):
        self.tenant_type_uid = tenant_type_uid
        self.tenant_type_name = tenant_type_name
        self.tenant_type_description = tenant_type_description
        self.tenant_class = tenant_class
    def update_attributes(self, tenant_type_name: str, tenant_type_description: str, tenant_class: str):
        self.tenant_type_name = tenant_type_name
        self.tenant_type_description = tenant_type_description
        self.tenant_class = tenant_class


@dataclass(frozen=False)
class time_approval_write_dto(base_write_dto):
    time_approval_uid: str
    time_approval_name: str
    tenant_uid: str
    account_uid: str
    time_entry_uid: str
    approval_comment: str
    def __init__(self, time_approval_uid: str, time_approval_name: str, tenant_uid: str, account_uid: str, time_entry_uid: str, approval_comment: str, custom_attributes: str = "{}"):
        self.time_approval_uid = time_approval_uid
        self.time_approval_name = time_approval_name
        self.tenant_uid = tenant_uid
        self.account_uid = account_uid
        self.time_entry_uid = time_entry_uid
        self.approval_comment = approval_comment
        self.custom_attributes = custom_attributes
    @classmethod
    def empty_write(cls):
        return cls("", "", "", "", "", "")
    @classmethod
    def default_write(cls):
        return cls(base_dto.get_random_uid(), "", "", "", "", "")
    @classmethod
    def random_write(cls):
        return cls(base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid())
    @classmethod
    def new_write(cls, time_approval_uid: str, time_approval_name: str, tenant_uid: str, account_uid: str, time_entry_uid: str, approval_comment: str):
        return cls(time_approval_uid, time_approval_name, tenant_uid, account_uid, time_entry_uid, approval_comment)
    @classmethod
    def new_write_with_defaults(cls, time_approval_uid: str = "", time_approval_name: str = "", tenant_uid: str = "", account_uid: str = "", time_entry_uid: str = "", approval_comment: str = ""):
        return cls(time_approval_uid, time_approval_name, tenant_uid, account_uid, time_entry_uid, approval_comment)
    @classmethod
    def new_write_random_uid(cls, time_approval_name: str, tenant_uid: str, account_uid: str, time_entry_uid: str, approval_comment: str):
        return cls(base_dto.get_random_uid(), time_approval_name, tenant_uid, account_uid, time_entry_uid, approval_comment)
    @classmethod
    def get_class_model(cls) -> base_model:
        return db_models.time_approval_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["time_approval_uid"], d["time_approval_name"], d["tenant_uid"], d["account_uid"], d["time_entry_uid"], d["approval_comment"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return time_approval_write_dto(self.time_approval_uid, self.time_approval_name, self.tenant_uid, self.account_uid, self.time_entry_uid, self.approval_comment, self.custom_attributes)
    def clone_write_new_uid(self):
        return time_approval_write_dto(base_dto.get_random_uid(), self.time_approval_name, self.tenant_uid, self.account_uid, self.time_entry_uid, self.approval_comment, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return time_approval_write_dto(uid, self.time_approval_name, self.tenant_uid, self.account_uid, self.time_entry_uid, self.approval_comment, self.custom_attributes)
    def get_model(self) -> base_model:
        return db_models.time_approval_model
    def get_uid(self) -> str:
        return self.time_approval_uid
    def get_name(self) -> str:
        return self.time_approval_name
    def get_list_values(self) -> list[any]:
        return [self.time_approval_uid, self.time_approval_name, self.tenant_uid, self.account_uid, self.time_entry_uid, self.approval_comment, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.time_approval_uid, self.time_approval_name, self.tenant_uid, self.account_uid, self.time_entry_uid, self.approval_comment]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.time_approval_name, self.tenant_uid, self.account_uid, self.time_entry_uid, self.approval_comment, self.custom_attributes, updated_by, self.time_approval_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.time_approval_uid, self.time_approval_name, self.tenant_uid, self.account_uid, self.time_entry_uid, self.approval_comment, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.time_approval_name, self.tenant_uid, self.account_uid, self.time_entry_uid, self.approval_comment]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.time_approval_name, self.tenant_uid, self.account_uid, self.time_entry_uid, self.approval_comment, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_uid() == obj.get_uid()
    def update_uid(self, uid: str):
        self.time_approval_uid = uid
    def update_uid_attributes(self, time_approval_uid: str, time_approval_name: str, tenant_uid: str, account_uid: str, time_entry_uid: str, approval_comment: str):
        self.time_approval_uid = time_approval_uid
        self.time_approval_name = time_approval_name
        self.tenant_uid = tenant_uid
        self.account_uid = account_uid
        self.time_entry_uid = time_entry_uid
        self.approval_comment = approval_comment
    def update_attributes(self, time_approval_name: str, tenant_uid: str, account_uid: str, time_entry_uid: str, approval_comment: str):
        self.time_approval_name = time_approval_name
        self.tenant_uid = tenant_uid
        self.account_uid = account_uid
        self.time_entry_uid = time_entry_uid
        self.approval_comment = approval_comment


@dataclass(frozen=False)
class time_entry_write_dto(base_write_dto):
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
    def __init__(self, time_entry_uid: str, time_entry_name: str, time_submit_uid: str, tenant_uid: str, account_uid: str, project_instance_uid: str, project_milestone_uid: str, period_uid: str, invoice_instance_uid: str | None, entry_period: str, entry_note: str, lock_row: str | None, start_date: datetime.datetime | None, end_date: datetime.datetime | None, entry_minutes: int, is_approved: int, custom_attributes: str = "{}"):
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
        self.custom_attributes = custom_attributes
    @classmethod
    def empty_write(cls):
        return cls("", "", "", "", "", "", "", "", "", "", "", "", datetime.datetime.now(), datetime.datetime.now(), 0, 0)
    @classmethod
    def default_write(cls):
        return cls(base_dto.get_random_uid(), "", "", "", "", "", "", "", "", "", "", "", datetime.datetime.now(), datetime.datetime.now(), 0, 0)
    @classmethod
    def random_write(cls):
        return cls(base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), datetime.datetime.now(), datetime.datetime.now(), 0, 0)
    @classmethod
    def new_write(cls, time_entry_uid: str, time_entry_name: str, time_submit_uid: str, tenant_uid: str, account_uid: str, project_instance_uid: str, project_milestone_uid: str, period_uid: str, invoice_instance_uid: str | None, entry_period: str, entry_note: str, lock_row: str | None, start_date: datetime.datetime | None, end_date: datetime.datetime | None, entry_minutes: int, is_approved: int):
        return cls(time_entry_uid, time_entry_name, time_submit_uid, tenant_uid, account_uid, project_instance_uid, project_milestone_uid, period_uid, invoice_instance_uid, entry_period, entry_note, lock_row, start_date, end_date, entry_minutes, is_approved)
    @classmethod
    def new_write_with_defaults(cls, time_entry_uid: str = "", time_entry_name: str = "", time_submit_uid: str = "", tenant_uid: str = "", account_uid: str = "", project_instance_uid: str = "", project_milestone_uid: str = "", period_uid: str = "", invoice_instance_uid: str | None = "", entry_period: str = "", entry_note: str = "", lock_row: str | None = "", start_date: datetime.datetime | None = datetime.datetime.now(), end_date: datetime.datetime | None = datetime.datetime.now(), entry_minutes: int = 0, is_approved: int = 0):
        return cls(time_entry_uid, time_entry_name, time_submit_uid, tenant_uid, account_uid, project_instance_uid, project_milestone_uid, period_uid, invoice_instance_uid, entry_period, entry_note, lock_row, start_date, end_date, entry_minutes, is_approved)
    @classmethod
    def new_write_random_uid(cls, time_entry_name: str, time_submit_uid: str, tenant_uid: str, account_uid: str, project_instance_uid: str, project_milestone_uid: str, period_uid: str, invoice_instance_uid: str | None, entry_period: str, entry_note: str, lock_row: str | None, start_date: datetime.datetime | None, end_date: datetime.datetime | None, entry_minutes: int, is_approved: int):
        return cls(base_dto.get_random_uid(), time_entry_name, time_submit_uid, tenant_uid, account_uid, project_instance_uid, project_milestone_uid, period_uid, invoice_instance_uid, entry_period, entry_note, lock_row, start_date, end_date, entry_minutes, is_approved)
    @classmethod
    def get_class_model(cls) -> base_model:
        return db_models.time_entry_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["time_entry_uid"], d["time_entry_name"], d["time_submit_uid"], d["tenant_uid"], d["account_uid"], d["project_instance_uid"], d["project_milestone_uid"], d["period_uid"], d["invoice_instance_uid"], d["entry_period"], d["entry_note"], d["lock_row"], d["start_date"], d["end_date"], d["entry_minutes"], d["is_approved"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return time_entry_write_dto(self.time_entry_uid, self.time_entry_name, self.time_submit_uid, self.tenant_uid, self.account_uid, self.project_instance_uid, self.project_milestone_uid, self.period_uid, self.invoice_instance_uid, self.entry_period, self.entry_note, self.lock_row, self.start_date, self.end_date, self.entry_minutes, self.is_approved, self.custom_attributes)
    def clone_write_new_uid(self):
        return time_entry_write_dto(base_dto.get_random_uid(), self.time_entry_name, self.time_submit_uid, self.tenant_uid, self.account_uid, self.project_instance_uid, self.project_milestone_uid, self.period_uid, self.invoice_instance_uid, self.entry_period, self.entry_note, self.lock_row, self.start_date, self.end_date, self.entry_minutes, self.is_approved, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return time_entry_write_dto(uid, self.time_entry_name, self.time_submit_uid, self.tenant_uid, self.account_uid, self.project_instance_uid, self.project_milestone_uid, self.period_uid, self.invoice_instance_uid, self.entry_period, self.entry_note, self.lock_row, self.start_date, self.end_date, self.entry_minutes, self.is_approved, self.custom_attributes)
    def get_model(self) -> base_model:
        return db_models.time_entry_model
    def get_uid(self) -> str:
        return self.time_entry_uid
    def get_name(self) -> str:
        return self.time_entry_name
    def get_list_values(self) -> list[any]:
        return [self.time_entry_uid, self.time_entry_name, self.time_submit_uid, self.tenant_uid, self.account_uid, self.project_instance_uid, self.project_milestone_uid, self.period_uid, self.invoice_instance_uid, self.entry_period, self.entry_note, self.lock_row, self.start_date, self.end_date, self.entry_minutes, self.is_approved, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.time_entry_uid, self.time_entry_name, self.time_submit_uid, self.tenant_uid, self.account_uid, self.project_instance_uid, self.project_milestone_uid, self.period_uid, self.invoice_instance_uid, self.entry_period, self.entry_note, self.lock_row, self.start_date, self.end_date, self.entry_minutes, self.is_approved]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.time_entry_name, self.time_submit_uid, self.tenant_uid, self.account_uid, self.project_instance_uid, self.project_milestone_uid, self.period_uid, self.invoice_instance_uid, self.entry_period, self.entry_note, self.lock_row, self.start_date, self.end_date, self.entry_minutes, self.is_approved, self.custom_attributes, updated_by, self.time_entry_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.time_entry_uid, self.time_entry_name, self.time_submit_uid, self.tenant_uid, self.account_uid, self.project_instance_uid, self.project_milestone_uid, self.period_uid, self.invoice_instance_uid, self.entry_period, self.entry_note, self.lock_row, self.start_date, self.end_date, self.entry_minutes, self.is_approved, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.time_entry_name, self.time_submit_uid, self.tenant_uid, self.account_uid, self.project_instance_uid, self.project_milestone_uid, self.period_uid, self.invoice_instance_uid, self.entry_period, self.entry_note, self.lock_row, self.start_date, self.end_date, self.entry_minutes, self.is_approved]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.time_entry_name, self.time_submit_uid, self.tenant_uid, self.account_uid, self.project_instance_uid, self.project_milestone_uid, self.period_uid, self.invoice_instance_uid, self.entry_period, self.entry_note, self.lock_row, self.start_date, self.end_date, self.entry_minutes, self.is_approved, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_uid() == obj.get_uid()
    def update_uid(self, uid: str):
        self.time_entry_uid = uid
    def update_uid_attributes(self, time_entry_uid: str, time_entry_name: str, time_submit_uid: str, tenant_uid: str, account_uid: str, project_instance_uid: str, project_milestone_uid: str, period_uid: str, invoice_instance_uid: str | None, entry_period: str, entry_note: str, lock_row: str | None, start_date: datetime.datetime | None, end_date: datetime.datetime | None, entry_minutes: int, is_approved: int):
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
    def update_attributes(self, time_entry_name: str, time_submit_uid: str, tenant_uid: str, account_uid: str, project_instance_uid: str, project_milestone_uid: str, period_uid: str, invoice_instance_uid: str | None, entry_period: str, entry_note: str, lock_row: str | None, start_date: datetime.datetime | None, end_date: datetime.datetime | None, entry_minutes: int, is_approved: int):
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


@dataclass(frozen=False)
class time_entry_final_write_dto(base_write_dto):
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
    def __init__(self, time_entry_final_uid: str, time_entry_final_name: str, tenant_uid: str, account_uid: str, project_instance_uid: str, project_milestone_uid: str, invoice_instance_uid: str | None, entry_period: str, entry_note: str, lock_uid: str | None, start_date: datetime.datetime | None, end_date: datetime.datetime | None, entry_minutes: int, is_approved: int, custom_attributes: str = "{}"):
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
        self.custom_attributes = custom_attributes
    @classmethod
    def empty_write(cls):
        return cls("", "", "", "", "", "", "", "", "", "", datetime.datetime.now(), datetime.datetime.now(), 0, 0)
    @classmethod
    def default_write(cls):
        return cls(base_dto.get_random_uid(), "", "", "", "", "", "", "", "", "", datetime.datetime.now(), datetime.datetime.now(), 0, 0)
    @classmethod
    def random_write(cls):
        return cls(base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), datetime.datetime.now(), datetime.datetime.now(), 0, 0)
    @classmethod
    def new_write(cls, time_entry_final_uid: str, time_entry_final_name: str, tenant_uid: str, account_uid: str, project_instance_uid: str, project_milestone_uid: str, invoice_instance_uid: str | None, entry_period: str, entry_note: str, lock_uid: str | None, start_date: datetime.datetime | None, end_date: datetime.datetime | None, entry_minutes: int, is_approved: int):
        return cls(time_entry_final_uid, time_entry_final_name, tenant_uid, account_uid, project_instance_uid, project_milestone_uid, invoice_instance_uid, entry_period, entry_note, lock_uid, start_date, end_date, entry_minutes, is_approved)
    @classmethod
    def new_write_with_defaults(cls, time_entry_final_uid: str = "", time_entry_final_name: str = "", tenant_uid: str = "", account_uid: str = "", project_instance_uid: str = "", project_milestone_uid: str = "", invoice_instance_uid: str | None = "", entry_period: str = "", entry_note: str = "", lock_uid: str | None = "", start_date: datetime.datetime | None = datetime.datetime.now(), end_date: datetime.datetime | None = datetime.datetime.now(), entry_minutes: int = 0, is_approved: int = 0):
        return cls(time_entry_final_uid, time_entry_final_name, tenant_uid, account_uid, project_instance_uid, project_milestone_uid, invoice_instance_uid, entry_period, entry_note, lock_uid, start_date, end_date, entry_minutes, is_approved)
    @classmethod
    def new_write_random_uid(cls, time_entry_final_name: str, tenant_uid: str, account_uid: str, project_instance_uid: str, project_milestone_uid: str, invoice_instance_uid: str | None, entry_period: str, entry_note: str, lock_uid: str | None, start_date: datetime.datetime | None, end_date: datetime.datetime | None, entry_minutes: int, is_approved: int):
        return cls(base_dto.get_random_uid(), time_entry_final_name, tenant_uid, account_uid, project_instance_uid, project_milestone_uid, invoice_instance_uid, entry_period, entry_note, lock_uid, start_date, end_date, entry_minutes, is_approved)
    @classmethod
    def get_class_model(cls) -> base_model:
        return db_models.time_entry_final_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["time_entry_final_uid"], d["time_entry_final_name"], d["tenant_uid"], d["account_uid"], d["project_instance_uid"], d["project_milestone_uid"], d["invoice_instance_uid"], d["entry_period"], d["entry_note"], d["lock_uid"], d["start_date"], d["end_date"], d["entry_minutes"], d["is_approved"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return time_entry_final_write_dto(self.time_entry_final_uid, self.time_entry_final_name, self.tenant_uid, self.account_uid, self.project_instance_uid, self.project_milestone_uid, self.invoice_instance_uid, self.entry_period, self.entry_note, self.lock_uid, self.start_date, self.end_date, self.entry_minutes, self.is_approved, self.custom_attributes)
    def clone_write_new_uid(self):
        return time_entry_final_write_dto(base_dto.get_random_uid(), self.time_entry_final_name, self.tenant_uid, self.account_uid, self.project_instance_uid, self.project_milestone_uid, self.invoice_instance_uid, self.entry_period, self.entry_note, self.lock_uid, self.start_date, self.end_date, self.entry_minutes, self.is_approved, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return time_entry_final_write_dto(uid, self.time_entry_final_name, self.tenant_uid, self.account_uid, self.project_instance_uid, self.project_milestone_uid, self.invoice_instance_uid, self.entry_period, self.entry_note, self.lock_uid, self.start_date, self.end_date, self.entry_minutes, self.is_approved, self.custom_attributes)
    def get_model(self) -> base_model:
        return db_models.time_entry_final_model
    def get_uid(self) -> str:
        return self.time_entry_final_uid
    def get_name(self) -> str:
        return self.time_entry_final_name
    def get_list_values(self) -> list[any]:
        return [self.time_entry_final_uid, self.time_entry_final_name, self.tenant_uid, self.account_uid, self.project_instance_uid, self.project_milestone_uid, self.invoice_instance_uid, self.entry_period, self.entry_note, self.lock_uid, self.start_date, self.end_date, self.entry_minutes, self.is_approved, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.time_entry_final_uid, self.time_entry_final_name, self.tenant_uid, self.account_uid, self.project_instance_uid, self.project_milestone_uid, self.invoice_instance_uid, self.entry_period, self.entry_note, self.lock_uid, self.start_date, self.end_date, self.entry_minutes, self.is_approved]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.time_entry_final_name, self.tenant_uid, self.account_uid, self.project_instance_uid, self.project_milestone_uid, self.invoice_instance_uid, self.entry_period, self.entry_note, self.lock_uid, self.start_date, self.end_date, self.entry_minutes, self.is_approved, self.custom_attributes, updated_by, self.time_entry_final_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.time_entry_final_uid, self.time_entry_final_name, self.tenant_uid, self.account_uid, self.project_instance_uid, self.project_milestone_uid, self.invoice_instance_uid, self.entry_period, self.entry_note, self.lock_uid, self.start_date, self.end_date, self.entry_minutes, self.is_approved, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.time_entry_final_name, self.tenant_uid, self.account_uid, self.project_instance_uid, self.project_milestone_uid, self.invoice_instance_uid, self.entry_period, self.entry_note, self.lock_uid, self.start_date, self.end_date, self.entry_minutes, self.is_approved]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.time_entry_final_name, self.tenant_uid, self.account_uid, self.project_instance_uid, self.project_milestone_uid, self.invoice_instance_uid, self.entry_period, self.entry_note, self.lock_uid, self.start_date, self.end_date, self.entry_minutes, self.is_approved, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_uid() == obj.get_uid()
    def update_uid(self, uid: str):
        self.time_entry_final_uid = uid
    def update_uid_attributes(self, time_entry_final_uid: str, time_entry_final_name: str, tenant_uid: str, account_uid: str, project_instance_uid: str, project_milestone_uid: str, invoice_instance_uid: str | None, entry_period: str, entry_note: str, lock_uid: str | None, start_date: datetime.datetime | None, end_date: datetime.datetime | None, entry_minutes: int, is_approved: int):
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
    def update_attributes(self, time_entry_final_name: str, tenant_uid: str, account_uid: str, project_instance_uid: str, project_milestone_uid: str, invoice_instance_uid: str | None, entry_period: str, entry_note: str, lock_uid: str | None, start_date: datetime.datetime | None, end_date: datetime.datetime | None, entry_minutes: int, is_approved: int):
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


@dataclass(frozen=False)
class time_entry_invoice_write_dto(base_write_dto):
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
    def __init__(self, time_entry_invoice_uid: str, time_entry_invoice_name: str, tenant_uid: str, account_uid: str, time_submit_uid: str, time_entry_uid: str, project_instance_uid: str, project_milestone_uid: str, period_uid: str, invoice_instance_uid: str, entry_period: str, entry_note: str, lock_row: str | None, start_date: datetime.datetime | None, end_date: datetime.datetime | None, entry_minutes: int, is_approved: int, custom_attributes: str = "{}"):
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
        self.custom_attributes = custom_attributes
    @classmethod
    def empty_write(cls):
        return cls("", "", "", "", "", "", "", "", "", "", "", "", "", datetime.datetime.now(), datetime.datetime.now(), 0, 0)
    @classmethod
    def default_write(cls):
        return cls(base_dto.get_random_uid(), "", "", "", "", "", "", "", "", "", "", "", "", datetime.datetime.now(), datetime.datetime.now(), 0, 0)
    @classmethod
    def random_write(cls):
        return cls(base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), datetime.datetime.now(), datetime.datetime.now(), 0, 0)
    @classmethod
    def new_write(cls, time_entry_invoice_uid: str, time_entry_invoice_name: str, tenant_uid: str, account_uid: str, time_submit_uid: str, time_entry_uid: str, project_instance_uid: str, project_milestone_uid: str, period_uid: str, invoice_instance_uid: str, entry_period: str, entry_note: str, lock_row: str | None, start_date: datetime.datetime | None, end_date: datetime.datetime | None, entry_minutes: int, is_approved: int):
        return cls(time_entry_invoice_uid, time_entry_invoice_name, tenant_uid, account_uid, time_submit_uid, time_entry_uid, project_instance_uid, project_milestone_uid, period_uid, invoice_instance_uid, entry_period, entry_note, lock_row, start_date, end_date, entry_minutes, is_approved)
    @classmethod
    def new_write_with_defaults(cls, time_entry_invoice_uid: str = "", time_entry_invoice_name: str = "", tenant_uid: str = "", account_uid: str = "", time_submit_uid: str = "", time_entry_uid: str = "", project_instance_uid: str = "", project_milestone_uid: str = "", period_uid: str = "", invoice_instance_uid: str = "", entry_period: str = "", entry_note: str = "", lock_row: str | None = "", start_date: datetime.datetime | None = datetime.datetime.now(), end_date: datetime.datetime | None = datetime.datetime.now(), entry_minutes: int = 0, is_approved: int = 0):
        return cls(time_entry_invoice_uid, time_entry_invoice_name, tenant_uid, account_uid, time_submit_uid, time_entry_uid, project_instance_uid, project_milestone_uid, period_uid, invoice_instance_uid, entry_period, entry_note, lock_row, start_date, end_date, entry_minutes, is_approved)
    @classmethod
    def new_write_random_uid(cls, time_entry_invoice_name: str, tenant_uid: str, account_uid: str, time_submit_uid: str, time_entry_uid: str, project_instance_uid: str, project_milestone_uid: str, period_uid: str, invoice_instance_uid: str, entry_period: str, entry_note: str, lock_row: str | None, start_date: datetime.datetime | None, end_date: datetime.datetime | None, entry_minutes: int, is_approved: int):
        return cls(base_dto.get_random_uid(), time_entry_invoice_name, tenant_uid, account_uid, time_submit_uid, time_entry_uid, project_instance_uid, project_milestone_uid, period_uid, invoice_instance_uid, entry_period, entry_note, lock_row, start_date, end_date, entry_minutes, is_approved)
    @classmethod
    def get_class_model(cls) -> base_model:
        return db_models.time_entry_invoice_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["time_entry_invoice_uid"], d["time_entry_invoice_name"], d["tenant_uid"], d["account_uid"], d["time_submit_uid"], d["time_entry_uid"], d["project_instance_uid"], d["project_milestone_uid"], d["period_uid"], d["invoice_instance_uid"], d["entry_period"], d["entry_note"], d["lock_row"], d["start_date"], d["end_date"], d["entry_minutes"], d["is_approved"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return time_entry_invoice_write_dto(self.time_entry_invoice_uid, self.time_entry_invoice_name, self.tenant_uid, self.account_uid, self.time_submit_uid, self.time_entry_uid, self.project_instance_uid, self.project_milestone_uid, self.period_uid, self.invoice_instance_uid, self.entry_period, self.entry_note, self.lock_row, self.start_date, self.end_date, self.entry_minutes, self.is_approved, self.custom_attributes)
    def clone_write_new_uid(self):
        return time_entry_invoice_write_dto(base_dto.get_random_uid(), self.time_entry_invoice_name, self.tenant_uid, self.account_uid, self.time_submit_uid, self.time_entry_uid, self.project_instance_uid, self.project_milestone_uid, self.period_uid, self.invoice_instance_uid, self.entry_period, self.entry_note, self.lock_row, self.start_date, self.end_date, self.entry_minutes, self.is_approved, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return time_entry_invoice_write_dto(uid, self.time_entry_invoice_name, self.tenant_uid, self.account_uid, self.time_submit_uid, self.time_entry_uid, self.project_instance_uid, self.project_milestone_uid, self.period_uid, self.invoice_instance_uid, self.entry_period, self.entry_note, self.lock_row, self.start_date, self.end_date, self.entry_minutes, self.is_approved, self.custom_attributes)
    def get_model(self) -> base_model:
        return db_models.time_entry_invoice_model
    def get_uid(self) -> str:
        return self.time_entry_invoice_uid
    def get_name(self) -> str:
        return self.time_entry_invoice_name
    def get_list_values(self) -> list[any]:
        return [self.time_entry_invoice_uid, self.time_entry_invoice_name, self.tenant_uid, self.account_uid, self.time_submit_uid, self.time_entry_uid, self.project_instance_uid, self.project_milestone_uid, self.period_uid, self.invoice_instance_uid, self.entry_period, self.entry_note, self.lock_row, self.start_date, self.end_date, self.entry_minutes, self.is_approved, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.time_entry_invoice_uid, self.time_entry_invoice_name, self.tenant_uid, self.account_uid, self.time_submit_uid, self.time_entry_uid, self.project_instance_uid, self.project_milestone_uid, self.period_uid, self.invoice_instance_uid, self.entry_period, self.entry_note, self.lock_row, self.start_date, self.end_date, self.entry_minutes, self.is_approved]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.time_entry_invoice_name, self.tenant_uid, self.account_uid, self.time_submit_uid, self.time_entry_uid, self.project_instance_uid, self.project_milestone_uid, self.period_uid, self.invoice_instance_uid, self.entry_period, self.entry_note, self.lock_row, self.start_date, self.end_date, self.entry_minutes, self.is_approved, self.custom_attributes, updated_by, self.time_entry_invoice_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.time_entry_invoice_uid, self.time_entry_invoice_name, self.tenant_uid, self.account_uid, self.time_submit_uid, self.time_entry_uid, self.project_instance_uid, self.project_milestone_uid, self.period_uid, self.invoice_instance_uid, self.entry_period, self.entry_note, self.lock_row, self.start_date, self.end_date, self.entry_minutes, self.is_approved, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.time_entry_invoice_name, self.tenant_uid, self.account_uid, self.time_submit_uid, self.time_entry_uid, self.project_instance_uid, self.project_milestone_uid, self.period_uid, self.invoice_instance_uid, self.entry_period, self.entry_note, self.lock_row, self.start_date, self.end_date, self.entry_minutes, self.is_approved]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.time_entry_invoice_name, self.tenant_uid, self.account_uid, self.time_submit_uid, self.time_entry_uid, self.project_instance_uid, self.project_milestone_uid, self.period_uid, self.invoice_instance_uid, self.entry_period, self.entry_note, self.lock_row, self.start_date, self.end_date, self.entry_minutes, self.is_approved, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_uid() == obj.get_uid()
    def update_uid(self, uid: str):
        self.time_entry_invoice_uid = uid
    def update_uid_attributes(self, time_entry_invoice_uid: str, time_entry_invoice_name: str, tenant_uid: str, account_uid: str, time_submit_uid: str, time_entry_uid: str, project_instance_uid: str, project_milestone_uid: str, period_uid: str, invoice_instance_uid: str, entry_period: str, entry_note: str, lock_row: str | None, start_date: datetime.datetime | None, end_date: datetime.datetime | None, entry_minutes: int, is_approved: int):
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
    def update_attributes(self, time_entry_invoice_name: str, tenant_uid: str, account_uid: str, time_submit_uid: str, time_entry_uid: str, project_instance_uid: str, project_milestone_uid: str, period_uid: str, invoice_instance_uid: str, entry_period: str, entry_note: str, lock_row: str | None, start_date: datetime.datetime | None, end_date: datetime.datetime | None, entry_minutes: int, is_approved: int):
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


@dataclass(frozen=False)
class time_rule_write_dto(base_write_dto):
    time_rule_uid: str
    time_rule_name: str
    def __init__(self, time_rule_uid: str, time_rule_name: str, custom_attributes: str = "{}"):
        self.time_rule_uid = time_rule_uid
        self.time_rule_name = time_rule_name
        self.custom_attributes = custom_attributes
    @classmethod
    def empty_write(cls):
        return cls("", "")
    @classmethod
    def default_write(cls):
        return cls(base_dto.get_random_uid(), "")
    @classmethod
    def random_write(cls):
        return cls(base_dto.get_random_uid(), base_dto.get_random_uid())
    @classmethod
    def new_write(cls, time_rule_uid: str, time_rule_name: str):
        return cls(time_rule_uid, time_rule_name)
    @classmethod
    def new_write_with_defaults(cls, time_rule_uid: str = "", time_rule_name: str = ""):
        return cls(time_rule_uid, time_rule_name)
    @classmethod
    def new_write_random_uid(cls, time_rule_name: str):
        return cls(base_dto.get_random_uid(), time_rule_name)
    @classmethod
    def get_class_model(cls) -> base_model:
        return db_models.time_rule_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["time_rule_uid"], d["time_rule_name"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return time_rule_write_dto(self.time_rule_uid, self.time_rule_name, self.custom_attributes)
    def clone_write_new_uid(self):
        return time_rule_write_dto(base_dto.get_random_uid(), self.time_rule_name, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return time_rule_write_dto(uid, self.time_rule_name, self.custom_attributes)
    def get_model(self) -> base_model:
        return db_models.time_rule_model
    def get_uid(self) -> str:
        return self.time_rule_uid
    def get_name(self) -> str:
        return self.time_rule_name
    def get_list_values(self) -> list[any]:
        return [self.time_rule_uid, self.time_rule_name, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.time_rule_uid, self.time_rule_name]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.time_rule_name, self.custom_attributes, updated_by, self.time_rule_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.time_rule_uid, self.time_rule_name, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.time_rule_name]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.time_rule_name, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_uid() == obj.get_uid()
    def update_uid(self, uid: str):
        self.time_rule_uid = uid
    def update_uid_attributes(self, time_rule_uid: str, time_rule_name: str):
        self.time_rule_uid = time_rule_uid
        self.time_rule_name = time_rule_name
    def update_attributes(self, time_rule_name: str):
        self.time_rule_name = time_rule_name


@dataclass(frozen=False)
class time_rule_client_write_dto(base_write_dto):
    time_rule_client_uid: str
    time_rule_client_name: str
    time_rule_definition: str
    def __init__(self, time_rule_client_uid: str, time_rule_client_name: str, time_rule_definition: str, custom_attributes: str = "{}"):
        self.time_rule_client_uid = time_rule_client_uid
        self.time_rule_client_name = time_rule_client_name
        self.time_rule_definition = time_rule_definition
        self.custom_attributes = custom_attributes
    @classmethod
    def empty_write(cls):
        return cls("", "", "")
    @classmethod
    def default_write(cls):
        return cls(base_dto.get_random_uid(), "", "")
    @classmethod
    def random_write(cls):
        return cls(base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid())
    @classmethod
    def new_write(cls, time_rule_client_uid: str, time_rule_client_name: str, time_rule_definition: str):
        return cls(time_rule_client_uid, time_rule_client_name, time_rule_definition)
    @classmethod
    def new_write_with_defaults(cls, time_rule_client_uid: str = "", time_rule_client_name: str = "", time_rule_definition: str = ""):
        return cls(time_rule_client_uid, time_rule_client_name, time_rule_definition)
    @classmethod
    def new_write_random_uid(cls, time_rule_client_name: str, time_rule_definition: str):
        return cls(base_dto.get_random_uid(), time_rule_client_name, time_rule_definition)
    @classmethod
    def get_class_model(cls) -> base_model:
        return db_models.time_rule_client_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["time_rule_client_uid"], d["time_rule_client_name"], d["time_rule_definition"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return time_rule_client_write_dto(self.time_rule_client_uid, self.time_rule_client_name, self.time_rule_definition, self.custom_attributes)
    def clone_write_new_uid(self):
        return time_rule_client_write_dto(base_dto.get_random_uid(), self.time_rule_client_name, self.time_rule_definition, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return time_rule_client_write_dto(uid, self.time_rule_client_name, self.time_rule_definition, self.custom_attributes)
    def get_model(self) -> base_model:
        return db_models.time_rule_client_model
    def get_uid(self) -> str:
        return self.time_rule_client_uid
    def get_name(self) -> str:
        return self.time_rule_client_name
    def get_list_values(self) -> list[any]:
        return [self.time_rule_client_uid, self.time_rule_client_name, self.time_rule_definition, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.time_rule_client_uid, self.time_rule_client_name, self.time_rule_definition]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.time_rule_client_name, self.time_rule_definition, self.custom_attributes, updated_by, self.time_rule_client_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.time_rule_client_uid, self.time_rule_client_name, self.time_rule_definition, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.time_rule_client_name, self.time_rule_definition]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.time_rule_client_name, self.time_rule_definition, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_uid() == obj.get_uid()
    def update_uid(self, uid: str):
        self.time_rule_client_uid = uid
    def update_uid_attributes(self, time_rule_client_uid: str, time_rule_client_name: str, time_rule_definition: str):
        self.time_rule_client_uid = time_rule_client_uid
        self.time_rule_client_name = time_rule_client_name
        self.time_rule_definition = time_rule_definition
    def update_attributes(self, time_rule_client_name: str, time_rule_definition: str):
        self.time_rule_client_name = time_rule_client_name
        self.time_rule_definition = time_rule_definition


@dataclass(frozen=False)
class time_submit_write_dto(base_write_dto):
    time_submit_uid: str
    time_submit_name: str
    tenant_uid: str
    account_uid: str
    period_uid: str
    time_submit_description: str
    def __init__(self, time_submit_uid: str, time_submit_name: str, tenant_uid: str, account_uid: str, period_uid: str, time_submit_description: str, custom_attributes: str = "{}"):
        self.time_submit_uid = time_submit_uid
        self.time_submit_name = time_submit_name
        self.tenant_uid = tenant_uid
        self.account_uid = account_uid
        self.period_uid = period_uid
        self.time_submit_description = time_submit_description
        self.custom_attributes = custom_attributes
    @classmethod
    def empty_write(cls):
        return cls("", "", "", "", "", "")
    @classmethod
    def default_write(cls):
        return cls(base_dto.get_random_uid(), "", "", "", "", "")
    @classmethod
    def random_write(cls):
        return cls(base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid())
    @classmethod
    def new_write(cls, time_submit_uid: str, time_submit_name: str, tenant_uid: str, account_uid: str, period_uid: str, time_submit_description: str):
        return cls(time_submit_uid, time_submit_name, tenant_uid, account_uid, period_uid, time_submit_description)
    @classmethod
    def new_write_with_defaults(cls, time_submit_uid: str = "", time_submit_name: str = "", tenant_uid: str = "", account_uid: str = "", period_uid: str = "", time_submit_description: str = ""):
        return cls(time_submit_uid, time_submit_name, tenant_uid, account_uid, period_uid, time_submit_description)
    @classmethod
    def new_write_random_uid(cls, time_submit_name: str, tenant_uid: str, account_uid: str, period_uid: str, time_submit_description: str):
        return cls(base_dto.get_random_uid(), time_submit_name, tenant_uid, account_uid, period_uid, time_submit_description)
    @classmethod
    def get_class_model(cls) -> base_model:
        return db_models.time_submit_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["time_submit_uid"], d["time_submit_name"], d["tenant_uid"], d["account_uid"], d["period_uid"], d["time_submit_description"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return time_submit_write_dto(self.time_submit_uid, self.time_submit_name, self.tenant_uid, self.account_uid, self.period_uid, self.time_submit_description, self.custom_attributes)
    def clone_write_new_uid(self):
        return time_submit_write_dto(base_dto.get_random_uid(), self.time_submit_name, self.tenant_uid, self.account_uid, self.period_uid, self.time_submit_description, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return time_submit_write_dto(uid, self.time_submit_name, self.tenant_uid, self.account_uid, self.period_uid, self.time_submit_description, self.custom_attributes)
    def get_model(self) -> base_model:
        return db_models.time_submit_model
    def get_uid(self) -> str:
        return self.time_submit_uid
    def get_name(self) -> str:
        return self.time_submit_name
    def get_list_values(self) -> list[any]:
        return [self.time_submit_uid, self.time_submit_name, self.tenant_uid, self.account_uid, self.period_uid, self.time_submit_description, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.time_submit_uid, self.time_submit_name, self.tenant_uid, self.account_uid, self.period_uid, self.time_submit_description]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.time_submit_name, self.tenant_uid, self.account_uid, self.period_uid, self.time_submit_description, self.custom_attributes, updated_by, self.time_submit_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.time_submit_uid, self.time_submit_name, self.tenant_uid, self.account_uid, self.period_uid, self.time_submit_description, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.time_submit_name, self.tenant_uid, self.account_uid, self.period_uid, self.time_submit_description]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.time_submit_name, self.tenant_uid, self.account_uid, self.period_uid, self.time_submit_description, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_uid() == obj.get_uid()
    def update_uid(self, uid: str):
        self.time_submit_uid = uid
    def update_uid_attributes(self, time_submit_uid: str, time_submit_name: str, tenant_uid: str, account_uid: str, period_uid: str, time_submit_description: str):
        self.time_submit_uid = time_submit_uid
        self.time_submit_name = time_submit_name
        self.tenant_uid = tenant_uid
        self.account_uid = account_uid
        self.period_uid = period_uid
        self.time_submit_description = time_submit_description
    def update_attributes(self, time_submit_name: str, tenant_uid: str, account_uid: str, period_uid: str, time_submit_description: str):
        self.time_submit_name = time_submit_name
        self.tenant_uid = tenant_uid
        self.account_uid = account_uid
        self.period_uid = period_uid
        self.time_submit_description = time_submit_description


@dataclass(frozen=False)
class time_submit_type_write_dto(base_write_dto):
    time_submit_type_uid: str
    time_submit_type_name: str
    time_submit_type_description: str
    def __init__(self, time_submit_type_uid: str, time_submit_type_name: str, time_submit_type_description: str, custom_attributes: str = "{}"):
        self.time_submit_type_uid = time_submit_type_uid
        self.time_submit_type_name = time_submit_type_name
        self.time_submit_type_description = time_submit_type_description
        self.custom_attributes = custom_attributes
    @classmethod
    def empty_write(cls):
        return cls("", "", "")
    @classmethod
    def default_write(cls):
        return cls(base_dto.get_random_uid(), "", "")
    @classmethod
    def random_write(cls):
        return cls(base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid())
    @classmethod
    def new_write(cls, time_submit_type_uid: str, time_submit_type_name: str, time_submit_type_description: str):
        return cls(time_submit_type_uid, time_submit_type_name, time_submit_type_description)
    @classmethod
    def new_write_with_defaults(cls, time_submit_type_uid: str = "", time_submit_type_name: str = "", time_submit_type_description: str = ""):
        return cls(time_submit_type_uid, time_submit_type_name, time_submit_type_description)
    @classmethod
    def new_write_random_uid(cls, time_submit_type_name: str, time_submit_type_description: str):
        return cls(base_dto.get_random_uid(), time_submit_type_name, time_submit_type_description)
    @classmethod
    def get_class_model(cls) -> base_model:
        return db_models.time_submit_type_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["time_submit_type_uid"], d["time_submit_type_name"], d["time_submit_type_description"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return time_submit_type_write_dto(self.time_submit_type_uid, self.time_submit_type_name, self.time_submit_type_description, self.custom_attributes)
    def clone_write_new_uid(self):
        return time_submit_type_write_dto(base_dto.get_random_uid(), self.time_submit_type_name, self.time_submit_type_description, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return time_submit_type_write_dto(uid, self.time_submit_type_name, self.time_submit_type_description, self.custom_attributes)
    def get_model(self) -> base_model:
        return db_models.time_submit_type_model
    def get_uid(self) -> str:
        return self.time_submit_type_uid
    def get_name(self) -> str:
        return self.time_submit_type_name
    def get_list_values(self) -> list[any]:
        return [self.time_submit_type_uid, self.time_submit_type_name, self.time_submit_type_description, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.time_submit_type_uid, self.time_submit_type_name, self.time_submit_type_description]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.time_submit_type_name, self.time_submit_type_description, self.custom_attributes, updated_by, self.time_submit_type_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.time_submit_type_uid, self.time_submit_type_name, self.time_submit_type_description, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.time_submit_type_name, self.time_submit_type_description]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.time_submit_type_name, self.time_submit_type_description, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_uid() == obj.get_uid()
    def update_uid(self, uid: str):
        self.time_submit_type_uid = uid
    def update_uid_attributes(self, time_submit_type_uid: str, time_submit_type_name: str, time_submit_type_description: str):
        self.time_submit_type_uid = time_submit_type_uid
        self.time_submit_type_name = time_submit_type_name
        self.time_submit_type_description = time_submit_type_description
    def update_attributes(self, time_submit_type_name: str, time_submit_type_description: str):
        self.time_submit_type_name = time_submit_type_name
        self.time_submit_type_description = time_submit_type_description


# auto-generated - v_definition_python_dtos_write - END
