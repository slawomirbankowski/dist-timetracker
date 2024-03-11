import datetime
from abc import abstractmethod
from dataclasses import dataclass, asdict
import json

from dto.dtos import *
from dto.dtos_models import *


@dataclass(frozen=False)
class account_division_write_dto(base_write_dto):
    account_division_uid: str
    division_name: str
    division_description: str
    def __init__(self, account_division_uid: str , division_name: str , division_description: str , custom_attributes: str = "{}"):
        self.account_division_uid = account_division_uid
        self.division_name = division_name
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
    def new_write(cls, account_division_uid: str , division_name: str , division_description: str ):
        return cls(account_division_uid, division_name, division_description)
    @classmethod
    def new_write_random_uid(cls, division_name: str , division_description: str ):
        return cls(base_dto.get_random_uid(), division_name, division_description)
    @classmethod
    def get_class_model(cls) -> base_model:
        return account_division_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["account_division_uid"], d["division_name"], d["division_description"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return account_division_write_dto(self.account_division_uid, self.division_name, self.division_description, self.custom_attributes)
    def clone_write_new_uid(self):
        return account_division_write_dto(base_dto.get_random_uid(), self.division_name, self.division_description, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return account_division_write_dto(uid, self.division_name, self.division_description, self.custom_attributes)
    def get_model(self) -> base_model:
        return account_division_model
    def get_key(self) -> str:
        return self.account_division_uid
    def get_uid(self) -> str:
        return self.account_division_uid
    def get_list_values(self) -> list[any]:
        return [self.account_division_uid, self.division_name, self.division_description, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.account_division_uid, self.division_name, self.division_description]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.division_name, self.division_description, self.custom_attributes, updated_by, self.account_division_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.account_division_uid, self.division_name, self.division_description, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.division_name, self.division_description]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.division_name, self.division_description, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_key() == obj.get_key()
    def update_uid(self, uid: str):
        self.account_division_uid = uid
    def update_uid_attributes(self, account_division_uid: str , division_name: str , division_description: str ):
        self.account_division_uid = account_division_uid
        self.division_name = division_name
        self.division_description = division_description
    def update_attributes(self, division_name: str , division_description: str ):
        self.division_name = division_name
        self.division_description = division_description


@dataclass(frozen=False)
class account_group_write_dto(base_write_dto):
    account_group_uid: str
    account_group_name: str
    account_group_description: str
    def __init__(self, account_group_uid: str , account_group_name: str , account_group_description: str , custom_attributes: str = "{}"):
        self.account_group_uid = account_group_uid
        self.account_group_name = account_group_name
        self.account_group_description = account_group_description
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
    def new_write(cls, account_group_uid: str , account_group_name: str , account_group_description: str ):
        return cls(account_group_uid, account_group_name, account_group_description)
    @classmethod
    def new_write_random_uid(cls, account_group_name: str , account_group_description: str ):
        return cls(base_dto.get_random_uid(), account_group_name, account_group_description)
    @classmethod
    def get_class_model(cls) -> base_model:
        return account_group_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["account_group_uid"], d["account_group_name"], d["account_group_description"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return account_group_write_dto(self.account_group_uid, self.account_group_name, self.account_group_description, self.custom_attributes)
    def clone_write_new_uid(self):
        return account_group_write_dto(base_dto.get_random_uid(), self.account_group_name, self.account_group_description, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return account_group_write_dto(uid, self.account_group_name, self.account_group_description, self.custom_attributes)
    def get_model(self) -> base_model:
        return account_group_model
    def get_key(self) -> str:
        return self.account_group_uid
    def get_uid(self) -> str:
        return self.account_group_uid
    def get_list_values(self) -> list[any]:
        return [self.account_group_uid, self.account_group_name, self.account_group_description, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.account_group_uid, self.account_group_name, self.account_group_description]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.account_group_name, self.account_group_description, self.custom_attributes, updated_by, self.account_group_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.account_group_uid, self.account_group_name, self.account_group_description, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.account_group_name, self.account_group_description]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.account_group_name, self.account_group_description, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_key() == obj.get_key()
    def update_uid(self, uid: str):
        self.account_group_uid = uid
    def update_uid_attributes(self, account_group_uid: str , account_group_name: str , account_group_description: str ):
        self.account_group_uid = account_group_uid
        self.account_group_name = account_group_name
        self.account_group_description = account_group_description
    def update_attributes(self, account_group_name: str , account_group_description: str ):
        self.account_group_name = account_group_name
        self.account_group_description = account_group_description


@dataclass(frozen=False)
class account_instance_write_dto(base_write_dto):
    account_instance_uid: str
    account_title_uid: str
    account_division_uid: str
    account_group_uid: str
    auth_identity_uid: str
    account_email: str
    account_name: str
    display_name: str
    is_system: int
    def __init__(self, account_instance_uid: str , account_title_uid: str , account_division_uid: str , account_group_uid: str , auth_identity_uid: str , account_email: str , account_name: str , display_name: str , is_system: int , custom_attributes: str = "{}"):
        self.account_instance_uid = account_instance_uid
        self.account_title_uid = account_title_uid
        self.account_division_uid = account_division_uid
        self.account_group_uid = account_group_uid
        self.auth_identity_uid = auth_identity_uid
        self.account_email = account_email
        self.account_name = account_name
        self.display_name = display_name
        self.is_system = is_system
        self.custom_attributes = custom_attributes
    @classmethod
    def empty_write(cls):
        return cls("", "", "", "", "", "", "", "", 0)
    @classmethod
    def default_write(cls):
        return cls(base_dto.get_random_uid(), "", "", "", "", "", "", "", 0)
    @classmethod
    def random_write(cls):
        return cls(base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), 0)
    @classmethod
    def new_write(cls, account_instance_uid: str , account_title_uid: str , account_division_uid: str , account_group_uid: str , auth_identity_uid: str , account_email: str , account_name: str , display_name: str , is_system: int ):
        return cls(account_instance_uid, account_title_uid, account_division_uid, account_group_uid, auth_identity_uid, account_email, account_name, display_name, is_system)
    @classmethod
    def new_write_random_uid(cls, account_title_uid: str , account_division_uid: str , account_group_uid: str , auth_identity_uid: str , account_email: str , account_name: str , display_name: str , is_system: int ):
        return cls(base_dto.get_random_uid(), account_title_uid, account_division_uid, account_group_uid, auth_identity_uid, account_email, account_name, display_name, is_system)
    @classmethod
    def get_class_model(cls) -> base_model:
        return account_instance_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["account_instance_uid"], d["account_title_uid"], d["account_division_uid"], d["account_group_uid"], d["auth_identity_uid"], d["account_email"], d["account_name"], d["display_name"], d["is_system"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return account_instance_write_dto(self.account_instance_uid, self.account_title_uid, self.account_division_uid, self.account_group_uid, self.auth_identity_uid, self.account_email, self.account_name, self.display_name, self.is_system, self.custom_attributes)
    def clone_write_new_uid(self):
        return account_instance_write_dto(base_dto.get_random_uid(), self.account_title_uid, self.account_division_uid, self.account_group_uid, self.auth_identity_uid, self.account_email, self.account_name, self.display_name, self.is_system, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return account_instance_write_dto(uid, self.account_title_uid, self.account_division_uid, self.account_group_uid, self.auth_identity_uid, self.account_email, self.account_name, self.display_name, self.is_system, self.custom_attributes)
    def get_model(self) -> base_model:
        return account_instance_model
    def get_key(self) -> str:
        return self.account_instance_uid
    def get_uid(self) -> str:
        return self.account_instance_uid
    def get_list_values(self) -> list[any]:
        return [self.account_instance_uid, self.account_title_uid, self.account_division_uid, self.account_group_uid, self.auth_identity_uid, self.account_email, self.account_name, self.display_name, self.is_system, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.account_instance_uid, self.account_title_uid, self.account_division_uid, self.account_group_uid, self.auth_identity_uid, self.account_email, self.account_name, self.display_name, self.is_system]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.account_title_uid, self.account_division_uid, self.account_group_uid, self.auth_identity_uid, self.account_email, self.account_name, self.display_name, self.is_system, self.custom_attributes, updated_by, self.account_instance_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.account_instance_uid, self.account_title_uid, self.account_division_uid, self.account_group_uid, self.auth_identity_uid, self.account_email, self.account_name, self.display_name, self.is_system, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.account_title_uid, self.account_division_uid, self.account_group_uid, self.auth_identity_uid, self.account_email, self.account_name, self.display_name, self.is_system]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.account_title_uid, self.account_division_uid, self.account_group_uid, self.auth_identity_uid, self.account_email, self.account_name, self.display_name, self.is_system, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_key() == obj.get_key()
    def update_uid(self, uid: str):
        self.account_instance_uid = uid
    def update_uid_attributes(self, account_instance_uid: str , account_title_uid: str , account_division_uid: str , account_group_uid: str , auth_identity_uid: str , account_email: str , account_name: str , display_name: str , is_system: int ):
        self.account_instance_uid = account_instance_uid
        self.account_title_uid = account_title_uid
        self.account_division_uid = account_division_uid
        self.account_group_uid = account_group_uid
        self.auth_identity_uid = auth_identity_uid
        self.account_email = account_email
        self.account_name = account_name
        self.display_name = display_name
        self.is_system = is_system
    def update_attributes(self, account_title_uid: str , account_division_uid: str , account_group_uid: str , auth_identity_uid: str , account_email: str , account_name: str , display_name: str , is_system: int ):
        self.account_title_uid = account_title_uid
        self.account_division_uid = account_division_uid
        self.account_group_uid = account_group_uid
        self.auth_identity_uid = auth_identity_uid
        self.account_email = account_email
        self.account_name = account_name
        self.display_name = display_name
        self.is_system = is_system


@dataclass(frozen=False)
class account_title_write_dto(base_write_dto):
    account_title_uid: str
    title_name: str
    title_description: str
    def __init__(self, account_title_uid: str , title_name: str , title_description: str , custom_attributes: str = "{}"):
        self.account_title_uid = account_title_uid
        self.title_name = title_name
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
    def new_write(cls, account_title_uid: str , title_name: str , title_description: str ):
        return cls(account_title_uid, title_name, title_description)
    @classmethod
    def new_write_random_uid(cls, title_name: str , title_description: str ):
        return cls(base_dto.get_random_uid(), title_name, title_description)
    @classmethod
    def get_class_model(cls) -> base_model:
        return account_title_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["account_title_uid"], d["title_name"], d["title_description"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return account_title_write_dto(self.account_title_uid, self.title_name, self.title_description, self.custom_attributes)
    def clone_write_new_uid(self):
        return account_title_write_dto(base_dto.get_random_uid(), self.title_name, self.title_description, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return account_title_write_dto(uid, self.title_name, self.title_description, self.custom_attributes)
    def get_model(self) -> base_model:
        return account_title_model
    def get_key(self) -> str:
        return self.account_title_uid
    def get_uid(self) -> str:
        return self.account_title_uid
    def get_list_values(self) -> list[any]:
        return [self.account_title_uid, self.title_name, self.title_description, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.account_title_uid, self.title_name, self.title_description]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.title_name, self.title_description, self.custom_attributes, updated_by, self.account_title_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.account_title_uid, self.title_name, self.title_description, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.title_name, self.title_description]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.title_name, self.title_description, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_key() == obj.get_key()
    def update_uid(self, uid: str):
        self.account_title_uid = uid
    def update_uid_attributes(self, account_title_uid: str , title_name: str , title_description: str ):
        self.account_title_uid = account_title_uid
        self.title_name = title_name
        self.title_description = title_description
    def update_attributes(self, title_name: str , title_description: str ):
        self.title_name = title_name
        self.title_description = title_description


@dataclass(frozen=False)
class auth_identity_write_dto(base_write_dto):
    auth_identity_uid: str
    identity_name: str
    identity_type: str
    identity_parameters: str
    last_status_name: str
    def __init__(self, auth_identity_uid: str , identity_name: str , identity_type: str , identity_parameters: str , last_status_name: str , custom_attributes: str = "{}"):
        self.auth_identity_uid = auth_identity_uid
        self.identity_name = identity_name
        self.identity_type = identity_type
        self.identity_parameters = identity_parameters
        self.last_status_name = last_status_name
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
    def new_write(cls, auth_identity_uid: str , identity_name: str , identity_type: str , identity_parameters: str , last_status_name: str ):
        return cls(auth_identity_uid, identity_name, identity_type, identity_parameters, last_status_name)
    @classmethod
    def new_write_random_uid(cls, identity_name: str , identity_type: str , identity_parameters: str , last_status_name: str ):
        return cls(base_dto.get_random_uid(), identity_name, identity_type, identity_parameters, last_status_name)
    @classmethod
    def get_class_model(cls) -> base_model:
        return auth_identity_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["auth_identity_uid"], d["identity_name"], d["identity_type"], d["identity_parameters"], d["last_status_name"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return auth_identity_write_dto(self.auth_identity_uid, self.identity_name, self.identity_type, self.identity_parameters, self.last_status_name, self.custom_attributes)
    def clone_write_new_uid(self):
        return auth_identity_write_dto(base_dto.get_random_uid(), self.identity_name, self.identity_type, self.identity_parameters, self.last_status_name, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return auth_identity_write_dto(uid, self.identity_name, self.identity_type, self.identity_parameters, self.last_status_name, self.custom_attributes)
    def get_model(self) -> base_model:
        return auth_identity_model
    def get_key(self) -> str:
        return self.auth_identity_uid
    def get_uid(self) -> str:
        return self.auth_identity_uid
    def get_list_values(self) -> list[any]:
        return [self.auth_identity_uid, self.identity_name, self.identity_type, self.identity_parameters, self.last_status_name, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.auth_identity_uid, self.identity_name, self.identity_type, self.identity_parameters, self.last_status_name]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.identity_name, self.identity_type, self.identity_parameters, self.last_status_name, self.custom_attributes, updated_by, self.auth_identity_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.auth_identity_uid, self.identity_name, self.identity_type, self.identity_parameters, self.last_status_name, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.identity_name, self.identity_type, self.identity_parameters, self.last_status_name]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.identity_name, self.identity_type, self.identity_parameters, self.last_status_name, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_key() == obj.get_key()
    def update_uid(self, uid: str):
        self.auth_identity_uid = uid
    def update_uid_attributes(self, auth_identity_uid: str , identity_name: str , identity_type: str , identity_parameters: str , last_status_name: str ):
        self.auth_identity_uid = auth_identity_uid
        self.identity_name = identity_name
        self.identity_type = identity_type
        self.identity_parameters = identity_parameters
        self.last_status_name = last_status_name
    def update_attributes(self, identity_name: str , identity_type: str , identity_parameters: str , last_status_name: str ):
        self.identity_name = identity_name
        self.identity_type = identity_type
        self.identity_parameters = identity_parameters
        self.last_status_name = last_status_name


@dataclass(frozen=False)
class auth_password_write_dto(base_write_dto):
    auth_password_uid: str
    account_instance_uid: str
    password_hash: str
    password_salt: str
    date_from: datetime.datetime
    date_to: datetime.datetime
    usage_count: int
    def __init__(self, auth_password_uid: str , account_instance_uid: str , password_hash: str , password_salt: str , date_from: datetime.datetime , date_to: datetime.datetime , usage_count: int , custom_attributes: str = "{}"):
        self.auth_password_uid = auth_password_uid
        self.account_instance_uid = account_instance_uid
        self.password_hash = password_hash
        self.password_salt = password_salt
        self.date_from = date_from
        self.date_to = date_to
        self.usage_count = usage_count
        self.custom_attributes = custom_attributes
    @classmethod
    def empty_write(cls):
        return cls("", "", "", "", datetime.datetime.now(), datetime.datetime.now(), 0)
    @classmethod
    def default_write(cls):
        return cls(base_dto.get_random_uid(), "", "", "", datetime.datetime.now(), datetime.datetime.now(), 0)
    @classmethod
    def random_write(cls):
        return cls(base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), datetime.datetime.now(), datetime.datetime.now(), 0)
    @classmethod
    def new_write(cls, auth_password_uid: str , account_instance_uid: str , password_hash: str , password_salt: str , date_from: datetime.datetime , date_to: datetime.datetime , usage_count: int ):
        return cls(auth_password_uid, account_instance_uid, password_hash, password_salt, date_from, date_to, usage_count)
    @classmethod
    def new_write_random_uid(cls, account_instance_uid: str , password_hash: str , password_salt: str , date_from: datetime.datetime , date_to: datetime.datetime , usage_count: int ):
        return cls(base_dto.get_random_uid(), account_instance_uid, password_hash, password_salt, date_from, date_to, usage_count)
    @classmethod
    def get_class_model(cls) -> base_model:
        return auth_password_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["auth_password_uid"], d["account_instance_uid"], d["password_hash"], d["password_salt"], d["date_from"], d["date_to"], d["usage_count"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return auth_password_write_dto(self.auth_password_uid, self.account_instance_uid, self.password_hash, self.password_salt, self.date_from, self.date_to, self.usage_count, self.custom_attributes)
    def clone_write_new_uid(self):
        return auth_password_write_dto(base_dto.get_random_uid(), self.account_instance_uid, self.password_hash, self.password_salt, self.date_from, self.date_to, self.usage_count, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return auth_password_write_dto(uid, self.account_instance_uid, self.password_hash, self.password_salt, self.date_from, self.date_to, self.usage_count, self.custom_attributes)
    def get_model(self) -> base_model:
        return auth_password_model
    def get_key(self) -> str:
        return self.auth_password_uid
    def get_uid(self) -> str:
        return self.auth_password_uid
    def get_list_values(self) -> list[any]:
        return [self.auth_password_uid, self.account_instance_uid, self.password_hash, self.password_salt, self.date_from, self.date_to, self.usage_count, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.auth_password_uid, self.account_instance_uid, self.password_hash, self.password_salt, self.date_from, self.date_to, self.usage_count]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.account_instance_uid, self.password_hash, self.password_salt, self.date_from, self.date_to, self.usage_count, self.custom_attributes, updated_by, self.auth_password_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.auth_password_uid, self.account_instance_uid, self.password_hash, self.password_salt, self.date_from, self.date_to, self.usage_count, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.account_instance_uid, self.password_hash, self.password_salt, self.date_from, self.date_to, self.usage_count]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.account_instance_uid, self.password_hash, self.password_salt, self.date_from, self.date_to, self.usage_count, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_key() == obj.get_key()
    def update_uid(self, uid: str):
        self.auth_password_uid = uid
    def update_uid_attributes(self, auth_password_uid: str , account_instance_uid: str , password_hash: str , password_salt: str , date_from: datetime.datetime , date_to: datetime.datetime , usage_count: int ):
        self.auth_password_uid = auth_password_uid
        self.account_instance_uid = account_instance_uid
        self.password_hash = password_hash
        self.password_salt = password_salt
        self.date_from = date_from
        self.date_to = date_to
        self.usage_count = usage_count
    def update_attributes(self, account_instance_uid: str , password_hash: str , password_salt: str , date_from: datetime.datetime , date_to: datetime.datetime , usage_count: int ):
        self.account_instance_uid = account_instance_uid
        self.password_hash = password_hash
        self.password_salt = password_salt
        self.date_from = date_from
        self.date_to = date_to
        self.usage_count = usage_count


@dataclass(frozen=False)
class auth_permission_write_dto(base_write_dto):
    auth_permission_uid: str
    account_instance_uid: str
    auth_role_uid: str
    client_instance_uid: str  | None
    project_instance_uid: str  | None
    valid_from_date: datetime.datetime
    valid_till_date: datetime.datetime
    def __init__(self, auth_permission_uid: str , account_instance_uid: str , auth_role_uid: str , client_instance_uid: str  | None, project_instance_uid: str  | None, valid_from_date: datetime.datetime , valid_till_date: datetime.datetime , custom_attributes: str = "{}"):
        self.auth_permission_uid = auth_permission_uid
        self.account_instance_uid = account_instance_uid
        self.auth_role_uid = auth_role_uid
        self.client_instance_uid = client_instance_uid
        self.project_instance_uid = project_instance_uid
        self.valid_from_date = valid_from_date
        self.valid_till_date = valid_till_date
        self.custom_attributes = custom_attributes
    @classmethod
    def empty_write(cls):
        return cls("", "", "", "", "", datetime.datetime.now(), datetime.datetime.now())
    @classmethod
    def default_write(cls):
        return cls(base_dto.get_random_uid(), "", "", "", "", datetime.datetime.now(), datetime.datetime.now())
    @classmethod
    def random_write(cls):
        return cls(base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), datetime.datetime.now(), datetime.datetime.now())
    @classmethod
    def new_write(cls, auth_permission_uid: str , account_instance_uid: str , auth_role_uid: str , client_instance_uid: str  | None, project_instance_uid: str  | None, valid_from_date: datetime.datetime , valid_till_date: datetime.datetime ):
        return cls(auth_permission_uid, account_instance_uid, auth_role_uid, client_instance_uid, project_instance_uid, valid_from_date, valid_till_date)
    @classmethod
    def new_write_random_uid(cls, account_instance_uid: str , auth_role_uid: str , client_instance_uid: str  | None, project_instance_uid: str  | None, valid_from_date: datetime.datetime , valid_till_date: datetime.datetime ):
        return cls(base_dto.get_random_uid(), account_instance_uid, auth_role_uid, client_instance_uid, project_instance_uid, valid_from_date, valid_till_date)
    @classmethod
    def get_class_model(cls) -> base_model:
        return auth_permission_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["auth_permission_uid"], d["account_instance_uid"], d["auth_role_uid"], d["client_instance_uid"], d["project_instance_uid"], d["valid_from_date"], d["valid_till_date"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return auth_permission_write_dto(self.auth_permission_uid, self.account_instance_uid, self.auth_role_uid, self.client_instance_uid, self.project_instance_uid, self.valid_from_date, self.valid_till_date, self.custom_attributes)
    def clone_write_new_uid(self):
        return auth_permission_write_dto(base_dto.get_random_uid(), self.account_instance_uid, self.auth_role_uid, self.client_instance_uid, self.project_instance_uid, self.valid_from_date, self.valid_till_date, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return auth_permission_write_dto(uid, self.account_instance_uid, self.auth_role_uid, self.client_instance_uid, self.project_instance_uid, self.valid_from_date, self.valid_till_date, self.custom_attributes)
    def get_model(self) -> base_model:
        return auth_permission_model
    def get_key(self) -> str:
        return self.auth_permission_uid
    def get_uid(self) -> str:
        return self.auth_permission_uid
    def get_list_values(self) -> list[any]:
        return [self.auth_permission_uid, self.account_instance_uid, self.auth_role_uid, self.client_instance_uid, self.project_instance_uid, self.valid_from_date, self.valid_till_date, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.auth_permission_uid, self.account_instance_uid, self.auth_role_uid, self.client_instance_uid, self.project_instance_uid, self.valid_from_date, self.valid_till_date]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.account_instance_uid, self.auth_role_uid, self.client_instance_uid, self.project_instance_uid, self.valid_from_date, self.valid_till_date, self.custom_attributes, updated_by, self.auth_permission_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.auth_permission_uid, self.account_instance_uid, self.auth_role_uid, self.client_instance_uid, self.project_instance_uid, self.valid_from_date, self.valid_till_date, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.account_instance_uid, self.auth_role_uid, self.client_instance_uid, self.project_instance_uid, self.valid_from_date, self.valid_till_date]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.account_instance_uid, self.auth_role_uid, self.client_instance_uid, self.project_instance_uid, self.valid_from_date, self.valid_till_date, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_key() == obj.get_key()
    def update_uid(self, uid: str):
        self.auth_permission_uid = uid
    def update_uid_attributes(self, auth_permission_uid: str , account_instance_uid: str , auth_role_uid: str , client_instance_uid: str  | None, project_instance_uid: str  | None, valid_from_date: datetime.datetime , valid_till_date: datetime.datetime ):
        self.auth_permission_uid = auth_permission_uid
        self.account_instance_uid = account_instance_uid
        self.auth_role_uid = auth_role_uid
        self.client_instance_uid = client_instance_uid
        self.project_instance_uid = project_instance_uid
        self.valid_from_date = valid_from_date
        self.valid_till_date = valid_till_date
    def update_attributes(self, account_instance_uid: str , auth_role_uid: str , client_instance_uid: str  | None, project_instance_uid: str  | None, valid_from_date: datetime.datetime , valid_till_date: datetime.datetime ):
        self.account_instance_uid = account_instance_uid
        self.auth_role_uid = auth_role_uid
        self.client_instance_uid = client_instance_uid
        self.project_instance_uid = project_instance_uid
        self.valid_from_date = valid_from_date
        self.valid_till_date = valid_till_date


@dataclass(frozen=False)
class auth_request_write_dto(base_write_dto):
    auth_request_uid: str
    by_account_instance_uid: str
    account_instance_uid: str
    reset_guid: str
    valid_till_date: datetime.datetime
    lock_guid: str  | None
    lock_by: str  | None
    lock_date: datetime.datetime  | None
    is_checked: int
    is_used: int
    check_date: datetime.datetime  | None
    use_date: datetime.datetime  | None
    def __init__(self, auth_request_uid: str , by_account_instance_uid: str , account_instance_uid: str , reset_guid: str , valid_till_date: datetime.datetime , lock_guid: str  | None, lock_by: str  | None, lock_date: datetime.datetime  | None, is_checked: int , is_used: int , check_date: datetime.datetime  | None, use_date: datetime.datetime  | None, custom_attributes: str = "{}"):
        self.auth_request_uid = auth_request_uid
        self.by_account_instance_uid = by_account_instance_uid
        self.account_instance_uid = account_instance_uid
        self.reset_guid = reset_guid
        self.valid_till_date = valid_till_date
        self.lock_guid = lock_guid
        self.lock_by = lock_by
        self.lock_date = lock_date
        self.is_checked = is_checked
        self.is_used = is_used
        self.check_date = check_date
        self.use_date = use_date
        self.custom_attributes = custom_attributes
    @classmethod
    def empty_write(cls):
        return cls("", "", "", "", datetime.datetime.now(), "", "", datetime.datetime.now(), 0, 0, datetime.datetime.now(), datetime.datetime.now())
    @classmethod
    def default_write(cls):
        return cls(base_dto.get_random_uid(), "", "", "", datetime.datetime.now(), "", "", datetime.datetime.now(), 0, 0, datetime.datetime.now(), datetime.datetime.now())
    @classmethod
    def random_write(cls):
        return cls(base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), datetime.datetime.now(), base_dto.get_random_uid(), base_dto.get_random_uid(), datetime.datetime.now(), 0, 0, datetime.datetime.now(), datetime.datetime.now())
    @classmethod
    def new_write(cls, auth_request_uid: str , by_account_instance_uid: str , account_instance_uid: str , reset_guid: str , valid_till_date: datetime.datetime , lock_guid: str  | None, lock_by: str  | None, lock_date: datetime.datetime  | None, is_checked: int , is_used: int , check_date: datetime.datetime  | None, use_date: datetime.datetime  | None):
        return cls(auth_request_uid, by_account_instance_uid, account_instance_uid, reset_guid, valid_till_date, lock_guid, lock_by, lock_date, is_checked, is_used, check_date, use_date)
    @classmethod
    def new_write_random_uid(cls, by_account_instance_uid: str , account_instance_uid: str , reset_guid: str , valid_till_date: datetime.datetime , lock_guid: str  | None, lock_by: str  | None, lock_date: datetime.datetime  | None, is_checked: int , is_used: int , check_date: datetime.datetime  | None, use_date: datetime.datetime  | None):
        return cls(base_dto.get_random_uid(), by_account_instance_uid, account_instance_uid, reset_guid, valid_till_date, lock_guid, lock_by, lock_date, is_checked, is_used, check_date, use_date)
    @classmethod
    def get_class_model(cls) -> base_model:
        return auth_request_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["auth_request_uid"], d["by_account_instance_uid"], d["account_instance_uid"], d["reset_guid"], d["valid_till_date"], d["lock_guid"], d["lock_by"], d["lock_date"], d["is_checked"], d["is_used"], d["check_date"], d["use_date"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return auth_request_write_dto(self.auth_request_uid, self.by_account_instance_uid, self.account_instance_uid, self.reset_guid, self.valid_till_date, self.lock_guid, self.lock_by, self.lock_date, self.is_checked, self.is_used, self.check_date, self.use_date, self.custom_attributes)
    def clone_write_new_uid(self):
        return auth_request_write_dto(base_dto.get_random_uid(), self.by_account_instance_uid, self.account_instance_uid, self.reset_guid, self.valid_till_date, self.lock_guid, self.lock_by, self.lock_date, self.is_checked, self.is_used, self.check_date, self.use_date, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return auth_request_write_dto(uid, self.by_account_instance_uid, self.account_instance_uid, self.reset_guid, self.valid_till_date, self.lock_guid, self.lock_by, self.lock_date, self.is_checked, self.is_used, self.check_date, self.use_date, self.custom_attributes)
    def get_model(self) -> base_model:
        return auth_request_model
    def get_key(self) -> str:
        return self.auth_request_uid
    def get_uid(self) -> str:
        return self.auth_request_uid
    def get_list_values(self) -> list[any]:
        return [self.auth_request_uid, self.by_account_instance_uid, self.account_instance_uid, self.reset_guid, self.valid_till_date, self.lock_guid, self.lock_by, self.lock_date, self.is_checked, self.is_used, self.check_date, self.use_date, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.auth_request_uid, self.by_account_instance_uid, self.account_instance_uid, self.reset_guid, self.valid_till_date, self.lock_guid, self.lock_by, self.lock_date, self.is_checked, self.is_used, self.check_date, self.use_date]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.by_account_instance_uid, self.account_instance_uid, self.reset_guid, self.valid_till_date, self.lock_guid, self.lock_by, self.lock_date, self.is_checked, self.is_used, self.check_date, self.use_date, self.custom_attributes, updated_by, self.auth_request_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.auth_request_uid, self.by_account_instance_uid, self.account_instance_uid, self.reset_guid, self.valid_till_date, self.lock_guid, self.lock_by, self.lock_date, self.is_checked, self.is_used, self.check_date, self.use_date, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.by_account_instance_uid, self.account_instance_uid, self.reset_guid, self.valid_till_date, self.lock_guid, self.lock_by, self.lock_date, self.is_checked, self.is_used, self.check_date, self.use_date]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.by_account_instance_uid, self.account_instance_uid, self.reset_guid, self.valid_till_date, self.lock_guid, self.lock_by, self.lock_date, self.is_checked, self.is_used, self.check_date, self.use_date, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_key() == obj.get_key()
    def update_uid(self, uid: str):
        self.auth_request_uid = uid
    def update_uid_attributes(self, auth_request_uid: str , by_account_instance_uid: str , account_instance_uid: str , reset_guid: str , valid_till_date: datetime.datetime , lock_guid: str  | None, lock_by: str  | None, lock_date: datetime.datetime  | None, is_checked: int , is_used: int , check_date: datetime.datetime  | None, use_date: datetime.datetime  | None):
        self.auth_request_uid = auth_request_uid
        self.by_account_instance_uid = by_account_instance_uid
        self.account_instance_uid = account_instance_uid
        self.reset_guid = reset_guid
        self.valid_till_date = valid_till_date
        self.lock_guid = lock_guid
        self.lock_by = lock_by
        self.lock_date = lock_date
        self.is_checked = is_checked
        self.is_used = is_used
        self.check_date = check_date
        self.use_date = use_date
    def update_attributes(self, by_account_instance_uid: str , account_instance_uid: str , reset_guid: str , valid_till_date: datetime.datetime , lock_guid: str  | None, lock_by: str  | None, lock_date: datetime.datetime  | None, is_checked: int , is_used: int , check_date: datetime.datetime  | None, use_date: datetime.datetime  | None):
        self.by_account_instance_uid = by_account_instance_uid
        self.account_instance_uid = account_instance_uid
        self.reset_guid = reset_guid
        self.valid_till_date = valid_till_date
        self.lock_guid = lock_guid
        self.lock_by = lock_by
        self.lock_date = lock_date
        self.is_checked = is_checked
        self.is_used = is_used
        self.check_date = check_date
        self.use_date = use_date


@dataclass(frozen=False)
class auth_role_write_dto(base_write_dto):
    auth_role_uid: str
    parent_auth_role_uid: str  | None
    role_name: str
    role_description: str
    access_uris: str
    is_project: int
    is_client: int
    is_custom: int
    def __init__(self, auth_role_uid: str , parent_auth_role_uid: str  | None, role_name: str , role_description: str , access_uris: str , is_project: int , is_client: int , is_custom: int , custom_attributes: str = "{}"):
        self.auth_role_uid = auth_role_uid
        self.parent_auth_role_uid = parent_auth_role_uid
        self.role_name = role_name
        self.role_description = role_description
        self.access_uris = access_uris
        self.is_project = is_project
        self.is_client = is_client
        self.is_custom = is_custom
        self.custom_attributes = custom_attributes
    @classmethod
    def empty_write(cls):
        return cls("", "", "", "", "", 0, 0, 0)
    @classmethod
    def default_write(cls):
        return cls(base_dto.get_random_uid(), "", "", "", "", 0, 0, 0)
    @classmethod
    def random_write(cls):
        return cls(base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), 0, 0, 0)
    @classmethod
    def new_write(cls, auth_role_uid: str , parent_auth_role_uid: str  | None, role_name: str , role_description: str , access_uris: str , is_project: int , is_client: int , is_custom: int ):
        return cls(auth_role_uid, parent_auth_role_uid, role_name, role_description, access_uris, is_project, is_client, is_custom)
    @classmethod
    def new_write_random_uid(cls, parent_auth_role_uid: str  | None, role_name: str , role_description: str , access_uris: str , is_project: int , is_client: int , is_custom: int ):
        return cls(base_dto.get_random_uid(), parent_auth_role_uid, role_name, role_description, access_uris, is_project, is_client, is_custom)
    @classmethod
    def get_class_model(cls) -> base_model:
        return auth_role_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["auth_role_uid"], d["parent_auth_role_uid"], d["role_name"], d["role_description"], d["access_uris"], d["is_project"], d["is_client"], d["is_custom"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return auth_role_write_dto(self.auth_role_uid, self.parent_auth_role_uid, self.role_name, self.role_description, self.access_uris, self.is_project, self.is_client, self.is_custom, self.custom_attributes)
    def clone_write_new_uid(self):
        return auth_role_write_dto(base_dto.get_random_uid(), self.parent_auth_role_uid, self.role_name, self.role_description, self.access_uris, self.is_project, self.is_client, self.is_custom, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return auth_role_write_dto(uid, self.parent_auth_role_uid, self.role_name, self.role_description, self.access_uris, self.is_project, self.is_client, self.is_custom, self.custom_attributes)
    def get_model(self) -> base_model:
        return auth_role_model
    def get_key(self) -> str:
        return self.auth_role_uid
    def get_uid(self) -> str:
        return self.auth_role_uid
    def get_list_values(self) -> list[any]:
        return [self.auth_role_uid, self.parent_auth_role_uid, self.role_name, self.role_description, self.access_uris, self.is_project, self.is_client, self.is_custom, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.auth_role_uid, self.parent_auth_role_uid, self.role_name, self.role_description, self.access_uris, self.is_project, self.is_client, self.is_custom]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.parent_auth_role_uid, self.role_name, self.role_description, self.access_uris, self.is_project, self.is_client, self.is_custom, self.custom_attributes, updated_by, self.auth_role_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.auth_role_uid, self.parent_auth_role_uid, self.role_name, self.role_description, self.access_uris, self.is_project, self.is_client, self.is_custom, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.parent_auth_role_uid, self.role_name, self.role_description, self.access_uris, self.is_project, self.is_client, self.is_custom]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.parent_auth_role_uid, self.role_name, self.role_description, self.access_uris, self.is_project, self.is_client, self.is_custom, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_key() == obj.get_key()
    def update_uid(self, uid: str):
        self.auth_role_uid = uid
    def update_uid_attributes(self, auth_role_uid: str , parent_auth_role_uid: str  | None, role_name: str , role_description: str , access_uris: str , is_project: int , is_client: int , is_custom: int ):
        self.auth_role_uid = auth_role_uid
        self.parent_auth_role_uid = parent_auth_role_uid
        self.role_name = role_name
        self.role_description = role_description
        self.access_uris = access_uris
        self.is_project = is_project
        self.is_client = is_client
        self.is_custom = is_custom
    def update_attributes(self, parent_auth_role_uid: str  | None, role_name: str , role_description: str , access_uris: str , is_project: int , is_client: int , is_custom: int ):
        self.parent_auth_role_uid = parent_auth_role_uid
        self.role_name = role_name
        self.role_description = role_description
        self.access_uris = access_uris
        self.is_project = is_project
        self.is_client = is_client
        self.is_custom = is_custom


@dataclass(frozen=False)
class auth_token_write_dto(base_write_dto):
    auth_token_uid: str
    account_instance_uid: str
    token_seq: int
    token_hash: str
    token_salt: str
    valid_till_date: datetime.datetime  | None
    last_use_date: datetime.datetime  | None
    is_last: int
    def __init__(self, auth_token_uid: str , account_instance_uid: str , token_seq: int , token_hash: str , token_salt: str , valid_till_date: datetime.datetime  | None, last_use_date: datetime.datetime  | None, is_last: int , custom_attributes: str = "{}"):
        self.auth_token_uid = auth_token_uid
        self.account_instance_uid = account_instance_uid
        self.token_seq = token_seq
        self.token_hash = token_hash
        self.token_salt = token_salt
        self.valid_till_date = valid_till_date
        self.last_use_date = last_use_date
        self.is_last = is_last
        self.custom_attributes = custom_attributes
    @classmethod
    def empty_write(cls):
        return cls("", "", 0, "", "", datetime.datetime.now(), datetime.datetime.now(), 0)
    @classmethod
    def default_write(cls):
        return cls(base_dto.get_random_uid(), "", 0, "", "", datetime.datetime.now(), datetime.datetime.now(), 0)
    @classmethod
    def random_write(cls):
        return cls(base_dto.get_random_uid(), base_dto.get_random_uid(), 0, base_dto.get_random_uid(), base_dto.get_random_uid(), datetime.datetime.now(), datetime.datetime.now(), 0)
    @classmethod
    def new_write(cls, auth_token_uid: str , account_instance_uid: str , token_seq: int , token_hash: str , token_salt: str , valid_till_date: datetime.datetime  | None, last_use_date: datetime.datetime  | None, is_last: int ):
        return cls(auth_token_uid, account_instance_uid, token_seq, token_hash, token_salt, valid_till_date, last_use_date, is_last)
    @classmethod
    def new_write_random_uid(cls, account_instance_uid: str , token_seq: int , token_hash: str , token_salt: str , valid_till_date: datetime.datetime  | None, last_use_date: datetime.datetime  | None, is_last: int ):
        return cls(base_dto.get_random_uid(), account_instance_uid, token_seq, token_hash, token_salt, valid_till_date, last_use_date, is_last)
    @classmethod
    def get_class_model(cls) -> base_model:
        return auth_token_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["auth_token_uid"], d["account_instance_uid"], d["token_seq"], d["token_hash"], d["token_salt"], d["valid_till_date"], d["last_use_date"], d["is_last"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return auth_token_write_dto(self.auth_token_uid, self.account_instance_uid, self.token_seq, self.token_hash, self.token_salt, self.valid_till_date, self.last_use_date, self.is_last, self.custom_attributes)
    def clone_write_new_uid(self):
        return auth_token_write_dto(base_dto.get_random_uid(), self.account_instance_uid, self.token_seq, self.token_hash, self.token_salt, self.valid_till_date, self.last_use_date, self.is_last, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return auth_token_write_dto(uid, self.account_instance_uid, self.token_seq, self.token_hash, self.token_salt, self.valid_till_date, self.last_use_date, self.is_last, self.custom_attributes)
    def get_model(self) -> base_model:
        return auth_token_model
    def get_key(self) -> str:
        return self.auth_token_uid
    def get_uid(self) -> str:
        return self.auth_token_uid
    def get_list_values(self) -> list[any]:
        return [self.auth_token_uid, self.account_instance_uid, self.token_seq, self.token_hash, self.token_salt, self.valid_till_date, self.last_use_date, self.is_last, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.auth_token_uid, self.account_instance_uid, self.token_seq, self.token_hash, self.token_salt, self.valid_till_date, self.last_use_date, self.is_last]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.account_instance_uid, self.token_seq, self.token_hash, self.token_salt, self.valid_till_date, self.last_use_date, self.is_last, self.custom_attributes, updated_by, self.auth_token_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.auth_token_uid, self.account_instance_uid, self.token_seq, self.token_hash, self.token_salt, self.valid_till_date, self.last_use_date, self.is_last, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.account_instance_uid, self.token_seq, self.token_hash, self.token_salt, self.valid_till_date, self.last_use_date, self.is_last]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.account_instance_uid, self.token_seq, self.token_hash, self.token_salt, self.valid_till_date, self.last_use_date, self.is_last, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_key() == obj.get_key()
    def update_uid(self, uid: str):
        self.auth_token_uid = uid
    def update_uid_attributes(self, auth_token_uid: str , account_instance_uid: str , token_seq: int , token_hash: str , token_salt: str , valid_till_date: datetime.datetime  | None, last_use_date: datetime.datetime  | None, is_last: int ):
        self.auth_token_uid = auth_token_uid
        self.account_instance_uid = account_instance_uid
        self.token_seq = token_seq
        self.token_hash = token_hash
        self.token_salt = token_salt
        self.valid_till_date = valid_till_date
        self.last_use_date = last_use_date
        self.is_last = is_last
    def update_attributes(self, account_instance_uid: str , token_seq: int , token_hash: str , token_salt: str , valid_till_date: datetime.datetime  | None, last_use_date: datetime.datetime  | None, is_last: int ):
        self.account_instance_uid = account_instance_uid
        self.token_seq = token_seq
        self.token_hash = token_hash
        self.token_salt = token_salt
        self.valid_till_date = valid_till_date
        self.last_use_date = last_use_date
        self.is_last = is_last


@dataclass(frozen=False)
class client_instance_write_dto(base_write_dto):
    client_instance_uid: str
    country_uid: str
    client_name: str
    client_code: str
    client_description: str
    start_date: datetime.datetime
    end_date: datetime.datetime  | None
    is_internal: int
    is_system: int
    is_test: int
    def __init__(self, client_instance_uid: str , country_uid: str , client_name: str , client_code: str , client_description: str , start_date: datetime.datetime , end_date: datetime.datetime  | None, is_internal: int , is_system: int , is_test: int , custom_attributes: str = "{}"):
        self.client_instance_uid = client_instance_uid
        self.country_uid = country_uid
        self.client_name = client_name
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
        return cls("", "", "", "", "", datetime.datetime.now(), datetime.datetime.now(), 0, 0, 0)
    @classmethod
    def default_write(cls):
        return cls(base_dto.get_random_uid(), "", "", "", "", datetime.datetime.now(), datetime.datetime.now(), 0, 0, 0)
    @classmethod
    def random_write(cls):
        return cls(base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), datetime.datetime.now(), datetime.datetime.now(), 0, 0, 0)
    @classmethod
    def new_write(cls, client_instance_uid: str , country_uid: str , client_name: str , client_code: str , client_description: str , start_date: datetime.datetime , end_date: datetime.datetime  | None, is_internal: int , is_system: int , is_test: int ):
        return cls(client_instance_uid, country_uid, client_name, client_code, client_description, start_date, end_date, is_internal, is_system, is_test)
    @classmethod
    def new_write_random_uid(cls, country_uid: str , client_name: str , client_code: str , client_description: str , start_date: datetime.datetime , end_date: datetime.datetime  | None, is_internal: int , is_system: int , is_test: int ):
        return cls(base_dto.get_random_uid(), country_uid, client_name, client_code, client_description, start_date, end_date, is_internal, is_system, is_test)
    @classmethod
    def get_class_model(cls) -> base_model:
        return client_instance_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["client_instance_uid"], d["country_uid"], d["client_name"], d["client_code"], d["client_description"], d["start_date"], d["end_date"], d["is_internal"], d["is_system"], d["is_test"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return client_instance_write_dto(self.client_instance_uid, self.country_uid, self.client_name, self.client_code, self.client_description, self.start_date, self.end_date, self.is_internal, self.is_system, self.is_test, self.custom_attributes)
    def clone_write_new_uid(self):
        return client_instance_write_dto(base_dto.get_random_uid(), self.country_uid, self.client_name, self.client_code, self.client_description, self.start_date, self.end_date, self.is_internal, self.is_system, self.is_test, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return client_instance_write_dto(uid, self.country_uid, self.client_name, self.client_code, self.client_description, self.start_date, self.end_date, self.is_internal, self.is_system, self.is_test, self.custom_attributes)
    def get_model(self) -> base_model:
        return client_instance_model
    def get_key(self) -> str:
        return self.client_instance_uid
    def get_uid(self) -> str:
        return self.client_instance_uid
    def get_list_values(self) -> list[any]:
        return [self.client_instance_uid, self.country_uid, self.client_name, self.client_code, self.client_description, self.start_date, self.end_date, self.is_internal, self.is_system, self.is_test, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.client_instance_uid, self.country_uid, self.client_name, self.client_code, self.client_description, self.start_date, self.end_date, self.is_internal, self.is_system, self.is_test]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.country_uid, self.client_name, self.client_code, self.client_description, self.start_date, self.end_date, self.is_internal, self.is_system, self.is_test, self.custom_attributes, updated_by, self.client_instance_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.client_instance_uid, self.country_uid, self.client_name, self.client_code, self.client_description, self.start_date, self.end_date, self.is_internal, self.is_system, self.is_test, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.country_uid, self.client_name, self.client_code, self.client_description, self.start_date, self.end_date, self.is_internal, self.is_system, self.is_test]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.country_uid, self.client_name, self.client_code, self.client_description, self.start_date, self.end_date, self.is_internal, self.is_system, self.is_test, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_key() == obj.get_key()
    def update_uid(self, uid: str):
        self.client_instance_uid = uid
    def update_uid_attributes(self, client_instance_uid: str , country_uid: str , client_name: str , client_code: str , client_description: str , start_date: datetime.datetime , end_date: datetime.datetime  | None, is_internal: int , is_system: int , is_test: int ):
        self.client_instance_uid = client_instance_uid
        self.country_uid = country_uid
        self.client_name = client_name
        self.client_code = client_code
        self.client_description = client_description
        self.start_date = start_date
        self.end_date = end_date
        self.is_internal = is_internal
        self.is_system = is_system
        self.is_test = is_test
    def update_attributes(self, country_uid: str , client_name: str , client_code: str , client_description: str , start_date: datetime.datetime , end_date: datetime.datetime  | None, is_internal: int , is_system: int , is_test: int ):
        self.country_uid = country_uid
        self.client_name = client_name
        self.client_code = client_code
        self.client_description = client_description
        self.start_date = start_date
        self.end_date = end_date
        self.is_internal = is_internal
        self.is_system = is_system
        self.is_test = is_test


@dataclass(frozen=False)
class country_write_dto(base_write_dto):
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
    def __init__(self, country_uid: str , continent_name: str , continent_code: str , country_name: str , country_iso3: str , country_code: str , phone_code: str , currency_code: str , capital_name: str , region_name: str , subregion_name: str , region_code: str , latitude: str , longitude: str , currency_name: str , population: str , languages: str , area: str , bar_code: str , top_level_domain: str , is_focused: int , custom_attributes: str = "{}"):
        self.country_uid = country_uid
        self.continent_name = continent_name
        self.continent_code = continent_code
        self.country_name = country_name
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
    def new_write(cls, country_uid: str , continent_name: str , continent_code: str , country_name: str , country_iso3: str , country_code: str , phone_code: str , currency_code: str , capital_name: str , region_name: str , subregion_name: str , region_code: str , latitude: str , longitude: str , currency_name: str , population: str , languages: str , area: str , bar_code: str , top_level_domain: str , is_focused: int ):
        return cls(country_uid, continent_name, continent_code, country_name, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain, is_focused)
    @classmethod
    def new_write_random_uid(cls, continent_name: str , continent_code: str , country_name: str , country_iso3: str , country_code: str , phone_code: str , currency_code: str , capital_name: str , region_name: str , subregion_name: str , region_code: str , latitude: str , longitude: str , currency_name: str , population: str , languages: str , area: str , bar_code: str , top_level_domain: str , is_focused: int ):
        return cls(base_dto.get_random_uid(), continent_name, continent_code, country_name, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain, is_focused)
    @classmethod
    def get_class_model(cls) -> base_model:
        return country_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["country_uid"], d["continent_name"], d["continent_code"], d["country_name"], d["country_iso3"], d["country_code"], d["phone_code"], d["currency_code"], d["capital_name"], d["region_name"], d["subregion_name"], d["region_code"], d["latitude"], d["longitude"], d["currency_name"], d["population"], d["languages"], d["area"], d["bar_code"], d["top_level_domain"], d["is_focused"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return country_write_dto(self.country_uid, self.continent_name, self.continent_code, self.country_name, self.country_iso3, self.country_code, self.phone_code, self.currency_code, self.capital_name, self.region_name, self.subregion_name, self.region_code, self.latitude, self.longitude, self.currency_name, self.population, self.languages, self.area, self.bar_code, self.top_level_domain, self.is_focused, self.custom_attributes)
    def clone_write_new_uid(self):
        return country_write_dto(base_dto.get_random_uid(), self.continent_name, self.continent_code, self.country_name, self.country_iso3, self.country_code, self.phone_code, self.currency_code, self.capital_name, self.region_name, self.subregion_name, self.region_code, self.latitude, self.longitude, self.currency_name, self.population, self.languages, self.area, self.bar_code, self.top_level_domain, self.is_focused, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return country_write_dto(uid, self.continent_name, self.continent_code, self.country_name, self.country_iso3, self.country_code, self.phone_code, self.currency_code, self.capital_name, self.region_name, self.subregion_name, self.region_code, self.latitude, self.longitude, self.currency_name, self.population, self.languages, self.area, self.bar_code, self.top_level_domain, self.is_focused, self.custom_attributes)
    def get_model(self) -> base_model:
        return country_model
    def get_key(self) -> str:
        return self.country_uid
    def get_uid(self) -> str:
        return self.country_uid
    def get_list_values(self) -> list[any]:
        return [self.country_uid, self.continent_name, self.continent_code, self.country_name, self.country_iso3, self.country_code, self.phone_code, self.currency_code, self.capital_name, self.region_name, self.subregion_name, self.region_code, self.latitude, self.longitude, self.currency_name, self.population, self.languages, self.area, self.bar_code, self.top_level_domain, self.is_focused, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.country_uid, self.continent_name, self.continent_code, self.country_name, self.country_iso3, self.country_code, self.phone_code, self.currency_code, self.capital_name, self.region_name, self.subregion_name, self.region_code, self.latitude, self.longitude, self.currency_name, self.population, self.languages, self.area, self.bar_code, self.top_level_domain, self.is_focused]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.continent_name, self.continent_code, self.country_name, self.country_iso3, self.country_code, self.phone_code, self.currency_code, self.capital_name, self.region_name, self.subregion_name, self.region_code, self.latitude, self.longitude, self.currency_name, self.population, self.languages, self.area, self.bar_code, self.top_level_domain, self.is_focused, self.custom_attributes, updated_by, self.country_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.country_uid, self.continent_name, self.continent_code, self.country_name, self.country_iso3, self.country_code, self.phone_code, self.currency_code, self.capital_name, self.region_name, self.subregion_name, self.region_code, self.latitude, self.longitude, self.currency_name, self.population, self.languages, self.area, self.bar_code, self.top_level_domain, self.is_focused, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.continent_name, self.continent_code, self.country_name, self.country_iso3, self.country_code, self.phone_code, self.currency_code, self.capital_name, self.region_name, self.subregion_name, self.region_code, self.latitude, self.longitude, self.currency_name, self.population, self.languages, self.area, self.bar_code, self.top_level_domain, self.is_focused]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.continent_name, self.continent_code, self.country_name, self.country_iso3, self.country_code, self.phone_code, self.currency_code, self.capital_name, self.region_name, self.subregion_name, self.region_code, self.latitude, self.longitude, self.currency_name, self.population, self.languages, self.area, self.bar_code, self.top_level_domain, self.is_focused, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_key() == obj.get_key()
    def update_uid(self, uid: str):
        self.country_uid = uid
    def update_uid_attributes(self, country_uid: str , continent_name: str , continent_code: str , country_name: str , country_iso3: str , country_code: str , phone_code: str , currency_code: str , capital_name: str , region_name: str , subregion_name: str , region_code: str , latitude: str , longitude: str , currency_name: str , population: str , languages: str , area: str , bar_code: str , top_level_domain: str , is_focused: int ):
        self.country_uid = country_uid
        self.continent_name = continent_name
        self.continent_code = continent_code
        self.country_name = country_name
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
    def update_attributes(self, continent_name: str , continent_code: str , country_name: str , country_iso3: str , country_code: str , phone_code: str , currency_code: str , capital_name: str , region_name: str , subregion_name: str , region_code: str , latitude: str , longitude: str , currency_name: str , population: str , languages: str , area: str , bar_code: str , top_level_domain: str , is_focused: int ):
        self.continent_name = continent_name
        self.continent_code = continent_code
        self.country_name = country_name
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
    def __init__(self, currency_uid: str , currency_name: str , is_focused: int , custom_attributes: str = "{}"):
        self.currency_uid = currency_uid
        self.currency_name = currency_name
        self.is_focused = is_focused
        self.custom_attributes = custom_attributes
    @classmethod
    def empty_write(cls):
        return cls("", "", 0)
    @classmethod
    def default_write(cls):
        return cls(base_dto.get_random_uid(), "", 0)
    @classmethod
    def random_write(cls):
        return cls(base_dto.get_random_uid(), base_dto.get_random_uid(), 0)
    @classmethod
    def new_write(cls, currency_uid: str , currency_name: str , is_focused: int ):
        return cls(currency_uid, currency_name, is_focused)
    @classmethod
    def new_write_random_uid(cls, currency_name: str , is_focused: int ):
        return cls(base_dto.get_random_uid(), currency_name, is_focused)
    @classmethod
    def get_class_model(cls) -> base_model:
        return currency_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["currency_uid"], d["currency_name"], d["is_focused"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return currency_write_dto(self.currency_uid, self.currency_name, self.is_focused, self.custom_attributes)
    def clone_write_new_uid(self):
        return currency_write_dto(base_dto.get_random_uid(), self.currency_name, self.is_focused, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return currency_write_dto(uid, self.currency_name, self.is_focused, self.custom_attributes)
    def get_model(self) -> base_model:
        return currency_model
    def get_key(self) -> str:
        return self.currency_uid
    def get_uid(self) -> str:
        return self.currency_uid
    def get_list_values(self) -> list[any]:
        return [self.currency_uid, self.currency_name, self.is_focused, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.currency_uid, self.currency_name, self.is_focused]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.currency_name, self.is_focused, self.custom_attributes, updated_by, self.currency_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.currency_uid, self.currency_name, self.is_focused, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.currency_name, self.is_focused]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.currency_name, self.is_focused, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_key() == obj.get_key()
    def update_uid(self, uid: str):
        self.currency_uid = uid
    def update_uid_attributes(self, currency_uid: str , currency_name: str , is_focused: int ):
        self.currency_uid = currency_uid
        self.currency_name = currency_name
        self.is_focused = is_focused
    def update_attributes(self, currency_name: str , is_focused: int ):
        self.currency_name = currency_name
        self.is_focused = is_focused


@dataclass(frozen=False)
class entry_final_write_dto(base_write_dto):
    entry_final_uid: str
    account_instance_uid: str
    project_instance_uid: str
    project_milestone_uid: str
    invoice_instance_uid: str  | None
    entry_period: str
    entry_note: str
    lock_uid: str  | None
    start_date: datetime.datetime  | None
    end_date: datetime.datetime  | None
    entry_minutes: int
    is_approved: int
    def __init__(self, entry_final_uid: str , account_instance_uid: str , project_instance_uid: str , project_milestone_uid: str , invoice_instance_uid: str  | None, entry_period: str , entry_note: str , lock_uid: str  | None, start_date: datetime.datetime  | None, end_date: datetime.datetime  | None, entry_minutes: int , is_approved: int , custom_attributes: str = "{}"):
        self.entry_final_uid = entry_final_uid
        self.account_instance_uid = account_instance_uid
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
        return cls("", "", "", "", "", "", "", "", datetime.datetime.now(), datetime.datetime.now(), 0, 0)
    @classmethod
    def default_write(cls):
        return cls(base_dto.get_random_uid(), "", "", "", "", "", "", "", datetime.datetime.now(), datetime.datetime.now(), 0, 0)
    @classmethod
    def random_write(cls):
        return cls(base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), datetime.datetime.now(), datetime.datetime.now(), 0, 0)
    @classmethod
    def new_write(cls, entry_final_uid: str , account_instance_uid: str , project_instance_uid: str , project_milestone_uid: str , invoice_instance_uid: str  | None, entry_period: str , entry_note: str , lock_uid: str  | None, start_date: datetime.datetime  | None, end_date: datetime.datetime  | None, entry_minutes: int , is_approved: int ):
        return cls(entry_final_uid, account_instance_uid, project_instance_uid, project_milestone_uid, invoice_instance_uid, entry_period, entry_note, lock_uid, start_date, end_date, entry_minutes, is_approved)
    @classmethod
    def new_write_random_uid(cls, account_instance_uid: str , project_instance_uid: str , project_milestone_uid: str , invoice_instance_uid: str  | None, entry_period: str , entry_note: str , lock_uid: str  | None, start_date: datetime.datetime  | None, end_date: datetime.datetime  | None, entry_minutes: int , is_approved: int ):
        return cls(base_dto.get_random_uid(), account_instance_uid, project_instance_uid, project_milestone_uid, invoice_instance_uid, entry_period, entry_note, lock_uid, start_date, end_date, entry_minutes, is_approved)
    @classmethod
    def get_class_model(cls) -> base_model:
        return entry_final_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["entry_final_uid"], d["account_instance_uid"], d["project_instance_uid"], d["project_milestone_uid"], d["invoice_instance_uid"], d["entry_period"], d["entry_note"], d["lock_uid"], d["start_date"], d["end_date"], d["entry_minutes"], d["is_approved"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return entry_final_write_dto(self.entry_final_uid, self.account_instance_uid, self.project_instance_uid, self.project_milestone_uid, self.invoice_instance_uid, self.entry_period, self.entry_note, self.lock_uid, self.start_date, self.end_date, self.entry_minutes, self.is_approved, self.custom_attributes)
    def clone_write_new_uid(self):
        return entry_final_write_dto(base_dto.get_random_uid(), self.account_instance_uid, self.project_instance_uid, self.project_milestone_uid, self.invoice_instance_uid, self.entry_period, self.entry_note, self.lock_uid, self.start_date, self.end_date, self.entry_minutes, self.is_approved, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return entry_final_write_dto(uid, self.account_instance_uid, self.project_instance_uid, self.project_milestone_uid, self.invoice_instance_uid, self.entry_period, self.entry_note, self.lock_uid, self.start_date, self.end_date, self.entry_minutes, self.is_approved, self.custom_attributes)
    def get_model(self) -> base_model:
        return entry_final_model
    def get_key(self) -> str:
        return self.entry_final_uid
    def get_uid(self) -> str:
        return self.entry_final_uid
    def get_list_values(self) -> list[any]:
        return [self.entry_final_uid, self.account_instance_uid, self.project_instance_uid, self.project_milestone_uid, self.invoice_instance_uid, self.entry_period, self.entry_note, self.lock_uid, self.start_date, self.end_date, self.entry_minutes, self.is_approved, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.entry_final_uid, self.account_instance_uid, self.project_instance_uid, self.project_milestone_uid, self.invoice_instance_uid, self.entry_period, self.entry_note, self.lock_uid, self.start_date, self.end_date, self.entry_minutes, self.is_approved]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.account_instance_uid, self.project_instance_uid, self.project_milestone_uid, self.invoice_instance_uid, self.entry_period, self.entry_note, self.lock_uid, self.start_date, self.end_date, self.entry_minutes, self.is_approved, self.custom_attributes, updated_by, self.entry_final_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.entry_final_uid, self.account_instance_uid, self.project_instance_uid, self.project_milestone_uid, self.invoice_instance_uid, self.entry_period, self.entry_note, self.lock_uid, self.start_date, self.end_date, self.entry_minutes, self.is_approved, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.account_instance_uid, self.project_instance_uid, self.project_milestone_uid, self.invoice_instance_uid, self.entry_period, self.entry_note, self.lock_uid, self.start_date, self.end_date, self.entry_minutes, self.is_approved]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.account_instance_uid, self.project_instance_uid, self.project_milestone_uid, self.invoice_instance_uid, self.entry_period, self.entry_note, self.lock_uid, self.start_date, self.end_date, self.entry_minutes, self.is_approved, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_key() == obj.get_key()
    def update_uid(self, uid: str):
        self.entry_final_uid = uid
    def update_uid_attributes(self, entry_final_uid: str , account_instance_uid: str , project_instance_uid: str , project_milestone_uid: str , invoice_instance_uid: str  | None, entry_period: str , entry_note: str , lock_uid: str  | None, start_date: datetime.datetime  | None, end_date: datetime.datetime  | None, entry_minutes: int , is_approved: int ):
        self.entry_final_uid = entry_final_uid
        self.account_instance_uid = account_instance_uid
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
    def update_attributes(self, account_instance_uid: str , project_instance_uid: str , project_milestone_uid: str , invoice_instance_uid: str  | None, entry_period: str , entry_note: str , lock_uid: str  | None, start_date: datetime.datetime  | None, end_date: datetime.datetime  | None, entry_minutes: int , is_approved: int ):
        self.account_instance_uid = account_instance_uid
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
class entry_save_write_dto(base_write_dto):
    entry_save_uid: str
    account_instance_uid: str
    project_instance_uid: str
    project_milestone_uid: str
    invoice_instance_uid: str  | None
    entry_period: str
    entry_note: str
    lock_uid: str  | None
    start_date: datetime.datetime  | None
    end_date: datetime.datetime  | None
    entry_minutes: int
    is_approved: int
    def __init__(self, entry_save_uid: str , account_instance_uid: str , project_instance_uid: str , project_milestone_uid: str , invoice_instance_uid: str  | None, entry_period: str , entry_note: str , lock_uid: str  | None, start_date: datetime.datetime  | None, end_date: datetime.datetime  | None, entry_minutes: int , is_approved: int , custom_attributes: str = "{}"):
        self.entry_save_uid = entry_save_uid
        self.account_instance_uid = account_instance_uid
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
        return cls("", "", "", "", "", "", "", "", datetime.datetime.now(), datetime.datetime.now(), 0, 0)
    @classmethod
    def default_write(cls):
        return cls(base_dto.get_random_uid(), "", "", "", "", "", "", "", datetime.datetime.now(), datetime.datetime.now(), 0, 0)
    @classmethod
    def random_write(cls):
        return cls(base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), datetime.datetime.now(), datetime.datetime.now(), 0, 0)
    @classmethod
    def new_write(cls, entry_save_uid: str , account_instance_uid: str , project_instance_uid: str , project_milestone_uid: str , invoice_instance_uid: str  | None, entry_period: str , entry_note: str , lock_uid: str  | None, start_date: datetime.datetime  | None, end_date: datetime.datetime  | None, entry_minutes: int , is_approved: int ):
        return cls(entry_save_uid, account_instance_uid, project_instance_uid, project_milestone_uid, invoice_instance_uid, entry_period, entry_note, lock_uid, start_date, end_date, entry_minutes, is_approved)
    @classmethod
    def new_write_random_uid(cls, account_instance_uid: str , project_instance_uid: str , project_milestone_uid: str , invoice_instance_uid: str  | None, entry_period: str , entry_note: str , lock_uid: str  | None, start_date: datetime.datetime  | None, end_date: datetime.datetime  | None, entry_minutes: int , is_approved: int ):
        return cls(base_dto.get_random_uid(), account_instance_uid, project_instance_uid, project_milestone_uid, invoice_instance_uid, entry_period, entry_note, lock_uid, start_date, end_date, entry_minutes, is_approved)
    @classmethod
    def get_class_model(cls) -> base_model:
        return entry_save_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["entry_save_uid"], d["account_instance_uid"], d["project_instance_uid"], d["project_milestone_uid"], d["invoice_instance_uid"], d["entry_period"], d["entry_note"], d["lock_uid"], d["start_date"], d["end_date"], d["entry_minutes"], d["is_approved"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return entry_save_write_dto(self.entry_save_uid, self.account_instance_uid, self.project_instance_uid, self.project_milestone_uid, self.invoice_instance_uid, self.entry_period, self.entry_note, self.lock_uid, self.start_date, self.end_date, self.entry_minutes, self.is_approved, self.custom_attributes)
    def clone_write_new_uid(self):
        return entry_save_write_dto(base_dto.get_random_uid(), self.account_instance_uid, self.project_instance_uid, self.project_milestone_uid, self.invoice_instance_uid, self.entry_period, self.entry_note, self.lock_uid, self.start_date, self.end_date, self.entry_minutes, self.is_approved, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return entry_save_write_dto(uid, self.account_instance_uid, self.project_instance_uid, self.project_milestone_uid, self.invoice_instance_uid, self.entry_period, self.entry_note, self.lock_uid, self.start_date, self.end_date, self.entry_minutes, self.is_approved, self.custom_attributes)
    def get_model(self) -> base_model:
        return entry_save_model
    def get_key(self) -> str:
        return self.entry_save_uid
    def get_uid(self) -> str:
        return self.entry_save_uid
    def get_list_values(self) -> list[any]:
        return [self.entry_save_uid, self.account_instance_uid, self.project_instance_uid, self.project_milestone_uid, self.invoice_instance_uid, self.entry_period, self.entry_note, self.lock_uid, self.start_date, self.end_date, self.entry_minutes, self.is_approved, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.entry_save_uid, self.account_instance_uid, self.project_instance_uid, self.project_milestone_uid, self.invoice_instance_uid, self.entry_period, self.entry_note, self.lock_uid, self.start_date, self.end_date, self.entry_minutes, self.is_approved]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.account_instance_uid, self.project_instance_uid, self.project_milestone_uid, self.invoice_instance_uid, self.entry_period, self.entry_note, self.lock_uid, self.start_date, self.end_date, self.entry_minutes, self.is_approved, self.custom_attributes, updated_by, self.entry_save_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.entry_save_uid, self.account_instance_uid, self.project_instance_uid, self.project_milestone_uid, self.invoice_instance_uid, self.entry_period, self.entry_note, self.lock_uid, self.start_date, self.end_date, self.entry_minutes, self.is_approved, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.account_instance_uid, self.project_instance_uid, self.project_milestone_uid, self.invoice_instance_uid, self.entry_period, self.entry_note, self.lock_uid, self.start_date, self.end_date, self.entry_minutes, self.is_approved]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.account_instance_uid, self.project_instance_uid, self.project_milestone_uid, self.invoice_instance_uid, self.entry_period, self.entry_note, self.lock_uid, self.start_date, self.end_date, self.entry_minutes, self.is_approved, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_key() == obj.get_key()
    def update_uid(self, uid: str):
        self.entry_save_uid = uid
    def update_uid_attributes(self, entry_save_uid: str , account_instance_uid: str , project_instance_uid: str , project_milestone_uid: str , invoice_instance_uid: str  | None, entry_period: str , entry_note: str , lock_uid: str  | None, start_date: datetime.datetime  | None, end_date: datetime.datetime  | None, entry_minutes: int , is_approved: int ):
        self.entry_save_uid = entry_save_uid
        self.account_instance_uid = account_instance_uid
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
    def update_attributes(self, account_instance_uid: str , project_instance_uid: str , project_milestone_uid: str , invoice_instance_uid: str  | None, entry_period: str , entry_note: str , lock_uid: str  | None, start_date: datetime.datetime  | None, end_date: datetime.datetime  | None, entry_minutes: int , is_approved: int ):
        self.account_instance_uid = account_instance_uid
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
class event_channel_write_dto(base_write_dto):
    event_channel_uid: str
    channel_type: str
    channel_name: str
    channel_definition: str
    def __init__(self, event_channel_uid: str , channel_type: str , channel_name: str , channel_definition: str , custom_attributes: str = "{}"):
        self.event_channel_uid = event_channel_uid
        self.channel_type = channel_type
        self.channel_name = channel_name
        self.channel_definition = channel_definition
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
    def new_write(cls, event_channel_uid: str , channel_type: str , channel_name: str , channel_definition: str ):
        return cls(event_channel_uid, channel_type, channel_name, channel_definition)
    @classmethod
    def new_write_random_uid(cls, channel_type: str , channel_name: str , channel_definition: str ):
        return cls(base_dto.get_random_uid(), channel_type, channel_name, channel_definition)
    @classmethod
    def get_class_model(cls) -> base_model:
        return event_channel_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["event_channel_uid"], d["channel_type"], d["channel_name"], d["channel_definition"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return event_channel_write_dto(self.event_channel_uid, self.channel_type, self.channel_name, self.channel_definition, self.custom_attributes)
    def clone_write_new_uid(self):
        return event_channel_write_dto(base_dto.get_random_uid(), self.channel_type, self.channel_name, self.channel_definition, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return event_channel_write_dto(uid, self.channel_type, self.channel_name, self.channel_definition, self.custom_attributes)
    def get_model(self) -> base_model:
        return event_channel_model
    def get_key(self) -> str:
        return self.event_channel_uid
    def get_uid(self) -> str:
        return self.event_channel_uid
    def get_list_values(self) -> list[any]:
        return [self.event_channel_uid, self.channel_type, self.channel_name, self.channel_definition, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.event_channel_uid, self.channel_type, self.channel_name, self.channel_definition]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.channel_type, self.channel_name, self.channel_definition, self.custom_attributes, updated_by, self.event_channel_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.event_channel_uid, self.channel_type, self.channel_name, self.channel_definition, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.channel_type, self.channel_name, self.channel_definition]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.channel_type, self.channel_name, self.channel_definition, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_key() == obj.get_key()
    def update_uid(self, uid: str):
        self.event_channel_uid = uid
    def update_uid_attributes(self, event_channel_uid: str , channel_type: str , channel_name: str , channel_definition: str ):
        self.event_channel_uid = event_channel_uid
        self.channel_type = channel_type
        self.channel_name = channel_name
        self.channel_definition = channel_definition
    def update_attributes(self, channel_type: str , channel_name: str , channel_definition: str ):
        self.channel_type = channel_type
        self.channel_name = channel_name
        self.channel_definition = channel_definition


@dataclass(frozen=False)
class event_instance_write_dto(base_write_dto):
    event_instance_uid: str
    event_type: str
    event_object: str
    event_method: str
    event_parameters: str
    event_signature: str
    published_count: int
    event_date: datetime.datetime
    def __init__(self, event_instance_uid: str , event_type: str , event_object: str , event_method: str , event_parameters: str , event_signature: str , published_count: int , event_date: datetime.datetime , custom_attributes: str = "{}"):
        self.event_instance_uid = event_instance_uid
        self.event_type = event_type
        self.event_object = event_object
        self.event_method = event_method
        self.event_parameters = event_parameters
        self.event_signature = event_signature
        self.published_count = published_count
        self.event_date = event_date
        self.custom_attributes = custom_attributes
    @classmethod
    def empty_write(cls):
        return cls("", "", "", "", "", "", 0, datetime.datetime.now())
    @classmethod
    def default_write(cls):
        return cls(base_dto.get_random_uid(), "", "", "", "", "", 0, datetime.datetime.now())
    @classmethod
    def random_write(cls):
        return cls(base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), 0, datetime.datetime.now())
    @classmethod
    def new_write(cls, event_instance_uid: str , event_type: str , event_object: str , event_method: str , event_parameters: str , event_signature: str , published_count: int , event_date: datetime.datetime ):
        return cls(event_instance_uid, event_type, event_object, event_method, event_parameters, event_signature, published_count, event_date)
    @classmethod
    def new_write_random_uid(cls, event_type: str , event_object: str , event_method: str , event_parameters: str , event_signature: str , published_count: int , event_date: datetime.datetime ):
        return cls(base_dto.get_random_uid(), event_type, event_object, event_method, event_parameters, event_signature, published_count, event_date)
    @classmethod
    def get_class_model(cls) -> base_model:
        return event_instance_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["event_instance_uid"], d["event_type"], d["event_object"], d["event_method"], d["event_parameters"], d["event_signature"], d["published_count"], d["event_date"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return event_instance_write_dto(self.event_instance_uid, self.event_type, self.event_object, self.event_method, self.event_parameters, self.event_signature, self.published_count, self.event_date, self.custom_attributes)
    def clone_write_new_uid(self):
        return event_instance_write_dto(base_dto.get_random_uid(), self.event_type, self.event_object, self.event_method, self.event_parameters, self.event_signature, self.published_count, self.event_date, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return event_instance_write_dto(uid, self.event_type, self.event_object, self.event_method, self.event_parameters, self.event_signature, self.published_count, self.event_date, self.custom_attributes)
    def get_model(self) -> base_model:
        return event_instance_model
    def get_key(self) -> str:
        return self.event_instance_uid
    def get_uid(self) -> str:
        return self.event_instance_uid
    def get_list_values(self) -> list[any]:
        return [self.event_instance_uid, self.event_type, self.event_object, self.event_method, self.event_parameters, self.event_signature, self.published_count, self.event_date, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.event_instance_uid, self.event_type, self.event_object, self.event_method, self.event_parameters, self.event_signature, self.published_count, self.event_date]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.event_type, self.event_object, self.event_method, self.event_parameters, self.event_signature, self.published_count, self.event_date, self.custom_attributes, updated_by, self.event_instance_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.event_instance_uid, self.event_type, self.event_object, self.event_method, self.event_parameters, self.event_signature, self.published_count, self.event_date, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.event_type, self.event_object, self.event_method, self.event_parameters, self.event_signature, self.published_count, self.event_date]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.event_type, self.event_object, self.event_method, self.event_parameters, self.event_signature, self.published_count, self.event_date, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_key() == obj.get_key()
    def update_uid(self, uid: str):
        self.event_instance_uid = uid
    def update_uid_attributes(self, event_instance_uid: str , event_type: str , event_object: str , event_method: str , event_parameters: str , event_signature: str , published_count: int , event_date: datetime.datetime ):
        self.event_instance_uid = event_instance_uid
        self.event_type = event_type
        self.event_object = event_object
        self.event_method = event_method
        self.event_parameters = event_parameters
        self.event_signature = event_signature
        self.published_count = published_count
        self.event_date = event_date
    def update_attributes(self, event_type: str , event_object: str , event_method: str , event_parameters: str , event_signature: str , published_count: int , event_date: datetime.datetime ):
        self.event_type = event_type
        self.event_object = event_object
        self.event_method = event_method
        self.event_parameters = event_parameters
        self.event_signature = event_signature
        self.published_count = published_count
        self.event_date = event_date


@dataclass(frozen=False)
class event_subscription_write_dto(base_write_dto):
    event_subscription_uid: str
    event_channel_uid: str
    subscription_name: str
    subscription_filter: str
    subscription_topic: str
    subscription_template: str
    def __init__(self, event_subscription_uid: str , event_channel_uid: str , subscription_name: str , subscription_filter: str , subscription_topic: str , subscription_template: str , custom_attributes: str = "{}"):
        self.event_subscription_uid = event_subscription_uid
        self.event_channel_uid = event_channel_uid
        self.subscription_name = subscription_name
        self.subscription_filter = subscription_filter
        self.subscription_topic = subscription_topic
        self.subscription_template = subscription_template
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
    def new_write(cls, event_subscription_uid: str , event_channel_uid: str , subscription_name: str , subscription_filter: str , subscription_topic: str , subscription_template: str ):
        return cls(event_subscription_uid, event_channel_uid, subscription_name, subscription_filter, subscription_topic, subscription_template)
    @classmethod
    def new_write_random_uid(cls, event_channel_uid: str , subscription_name: str , subscription_filter: str , subscription_topic: str , subscription_template: str ):
        return cls(base_dto.get_random_uid(), event_channel_uid, subscription_name, subscription_filter, subscription_topic, subscription_template)
    @classmethod
    def get_class_model(cls) -> base_model:
        return event_subscription_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["event_subscription_uid"], d["event_channel_uid"], d["subscription_name"], d["subscription_filter"], d["subscription_topic"], d["subscription_template"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return event_subscription_write_dto(self.event_subscription_uid, self.event_channel_uid, self.subscription_name, self.subscription_filter, self.subscription_topic, self.subscription_template, self.custom_attributes)
    def clone_write_new_uid(self):
        return event_subscription_write_dto(base_dto.get_random_uid(), self.event_channel_uid, self.subscription_name, self.subscription_filter, self.subscription_topic, self.subscription_template, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return event_subscription_write_dto(uid, self.event_channel_uid, self.subscription_name, self.subscription_filter, self.subscription_topic, self.subscription_template, self.custom_attributes)
    def get_model(self) -> base_model:
        return event_subscription_model
    def get_key(self) -> str:
        return self.event_subscription_uid
    def get_uid(self) -> str:
        return self.event_subscription_uid
    def get_list_values(self) -> list[any]:
        return [self.event_subscription_uid, self.event_channel_uid, self.subscription_name, self.subscription_filter, self.subscription_topic, self.subscription_template, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.event_subscription_uid, self.event_channel_uid, self.subscription_name, self.subscription_filter, self.subscription_topic, self.subscription_template]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.event_channel_uid, self.subscription_name, self.subscription_filter, self.subscription_topic, self.subscription_template, self.custom_attributes, updated_by, self.event_subscription_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.event_subscription_uid, self.event_channel_uid, self.subscription_name, self.subscription_filter, self.subscription_topic, self.subscription_template, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.event_channel_uid, self.subscription_name, self.subscription_filter, self.subscription_topic, self.subscription_template]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.event_channel_uid, self.subscription_name, self.subscription_filter, self.subscription_topic, self.subscription_template, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_key() == obj.get_key()
    def update_uid(self, uid: str):
        self.event_subscription_uid = uid
    def update_uid_attributes(self, event_subscription_uid: str , event_channel_uid: str , subscription_name: str , subscription_filter: str , subscription_topic: str , subscription_template: str ):
        self.event_subscription_uid = event_subscription_uid
        self.event_channel_uid = event_channel_uid
        self.subscription_name = subscription_name
        self.subscription_filter = subscription_filter
        self.subscription_topic = subscription_topic
        self.subscription_template = subscription_template
    def update_attributes(self, event_channel_uid: str , subscription_name: str , subscription_filter: str , subscription_topic: str , subscription_template: str ):
        self.event_channel_uid = event_channel_uid
        self.subscription_name = subscription_name
        self.subscription_filter = subscription_filter
        self.subscription_topic = subscription_topic
        self.subscription_template = subscription_template


@dataclass(frozen=False)
class invoice_instance_write_dto(base_write_dto):
    invoice_instance_uid: str
    client_instance_uid: str
    account_instance_uid: str
    period_code: str
    invoice_number: str
    invoice_details: str
    invoice_status: str
    invoice_currency: str
    invoice_amount: str
    def __init__(self, invoice_instance_uid: str , client_instance_uid: str , account_instance_uid: str , period_code: str , invoice_number: str , invoice_details: str , invoice_status: str , invoice_currency: str , invoice_amount: str , custom_attributes: str = "{}"):
        self.invoice_instance_uid = invoice_instance_uid
        self.client_instance_uid = client_instance_uid
        self.account_instance_uid = account_instance_uid
        self.period_code = period_code
        self.invoice_number = invoice_number
        self.invoice_details = invoice_details
        self.invoice_status = invoice_status
        self.invoice_currency = invoice_currency
        self.invoice_amount = invoice_amount
        self.custom_attributes = custom_attributes
    @classmethod
    def empty_write(cls):
        return cls("", "", "", "", "", "", "", "", "")
    @classmethod
    def default_write(cls):
        return cls(base_dto.get_random_uid(), "", "", "", "", "", "", "", "")
    @classmethod
    def random_write(cls):
        return cls(base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), "")
    @classmethod
    def new_write(cls, invoice_instance_uid: str , client_instance_uid: str , account_instance_uid: str , period_code: str , invoice_number: str , invoice_details: str , invoice_status: str , invoice_currency: str , invoice_amount: str ):
        return cls(invoice_instance_uid, client_instance_uid, account_instance_uid, period_code, invoice_number, invoice_details, invoice_status, invoice_currency, invoice_amount)
    @classmethod
    def new_write_random_uid(cls, client_instance_uid: str , account_instance_uid: str , period_code: str , invoice_number: str , invoice_details: str , invoice_status: str , invoice_currency: str , invoice_amount: str ):
        return cls(base_dto.get_random_uid(), client_instance_uid, account_instance_uid, period_code, invoice_number, invoice_details, invoice_status, invoice_currency, invoice_amount)
    @classmethod
    def get_class_model(cls) -> base_model:
        return invoice_instance_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["invoice_instance_uid"], d["client_instance_uid"], d["account_instance_uid"], d["period_code"], d["invoice_number"], d["invoice_details"], d["invoice_status"], d["invoice_currency"], d["invoice_amount"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return invoice_instance_write_dto(self.invoice_instance_uid, self.client_instance_uid, self.account_instance_uid, self.period_code, self.invoice_number, self.invoice_details, self.invoice_status, self.invoice_currency, self.invoice_amount, self.custom_attributes)
    def clone_write_new_uid(self):
        return invoice_instance_write_dto(base_dto.get_random_uid(), self.client_instance_uid, self.account_instance_uid, self.period_code, self.invoice_number, self.invoice_details, self.invoice_status, self.invoice_currency, self.invoice_amount, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return invoice_instance_write_dto(uid, self.client_instance_uid, self.account_instance_uid, self.period_code, self.invoice_number, self.invoice_details, self.invoice_status, self.invoice_currency, self.invoice_amount, self.custom_attributes)
    def get_model(self) -> base_model:
        return invoice_instance_model
    def get_key(self) -> str:
        return self.invoice_instance_uid
    def get_uid(self) -> str:
        return self.invoice_instance_uid
    def get_list_values(self) -> list[any]:
        return [self.invoice_instance_uid, self.client_instance_uid, self.account_instance_uid, self.period_code, self.invoice_number, self.invoice_details, self.invoice_status, self.invoice_currency, self.invoice_amount, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.invoice_instance_uid, self.client_instance_uid, self.account_instance_uid, self.period_code, self.invoice_number, self.invoice_details, self.invoice_status, self.invoice_currency, self.invoice_amount]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.client_instance_uid, self.account_instance_uid, self.period_code, self.invoice_number, self.invoice_details, self.invoice_status, self.invoice_currency, self.invoice_amount, self.custom_attributes, updated_by, self.invoice_instance_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.invoice_instance_uid, self.client_instance_uid, self.account_instance_uid, self.period_code, self.invoice_number, self.invoice_details, self.invoice_status, self.invoice_currency, self.invoice_amount, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.client_instance_uid, self.account_instance_uid, self.period_code, self.invoice_number, self.invoice_details, self.invoice_status, self.invoice_currency, self.invoice_amount]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.client_instance_uid, self.account_instance_uid, self.period_code, self.invoice_number, self.invoice_details, self.invoice_status, self.invoice_currency, self.invoice_amount, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_key() == obj.get_key()
    def update_uid(self, uid: str):
        self.invoice_instance_uid = uid
    def update_uid_attributes(self, invoice_instance_uid: str , client_instance_uid: str , account_instance_uid: str , period_code: str , invoice_number: str , invoice_details: str , invoice_status: str , invoice_currency: str , invoice_amount: str ):
        self.invoice_instance_uid = invoice_instance_uid
        self.client_instance_uid = client_instance_uid
        self.account_instance_uid = account_instance_uid
        self.period_code = period_code
        self.invoice_number = invoice_number
        self.invoice_details = invoice_details
        self.invoice_status = invoice_status
        self.invoice_currency = invoice_currency
        self.invoice_amount = invoice_amount
    def update_attributes(self, client_instance_uid: str , account_instance_uid: str , period_code: str , invoice_number: str , invoice_details: str , invoice_status: str , invoice_currency: str , invoice_amount: str ):
        self.client_instance_uid = client_instance_uid
        self.account_instance_uid = account_instance_uid
        self.period_code = period_code
        self.invoice_number = invoice_number
        self.invoice_details = invoice_details
        self.invoice_status = invoice_status
        self.invoice_currency = invoice_currency
        self.invoice_amount = invoice_amount


@dataclass(frozen=False)
class notification_instance_write_dto(base_write_dto):
    notification_instance_uid: str
    account_instance_uid: str
    notification_type: str
    notification_topic: str
    notification_format: str
    notification_content: str
    sending_status: str
    def __init__(self, notification_instance_uid: str , account_instance_uid: str , notification_type: str , notification_topic: str , notification_format: str , notification_content: str , sending_status: str , custom_attributes: str = "{}"):
        self.notification_instance_uid = notification_instance_uid
        self.account_instance_uid = account_instance_uid
        self.notification_type = notification_type
        self.notification_topic = notification_topic
        self.notification_format = notification_format
        self.notification_content = notification_content
        self.sending_status = sending_status
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
    def new_write(cls, notification_instance_uid: str , account_instance_uid: str , notification_type: str , notification_topic: str , notification_format: str , notification_content: str , sending_status: str ):
        return cls(notification_instance_uid, account_instance_uid, notification_type, notification_topic, notification_format, notification_content, sending_status)
    @classmethod
    def new_write_random_uid(cls, account_instance_uid: str , notification_type: str , notification_topic: str , notification_format: str , notification_content: str , sending_status: str ):
        return cls(base_dto.get_random_uid(), account_instance_uid, notification_type, notification_topic, notification_format, notification_content, sending_status)
    @classmethod
    def get_class_model(cls) -> base_model:
        return notification_instance_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["notification_instance_uid"], d["account_instance_uid"], d["notification_type"], d["notification_topic"], d["notification_format"], d["notification_content"], d["sending_status"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return notification_instance_write_dto(self.notification_instance_uid, self.account_instance_uid, self.notification_type, self.notification_topic, self.notification_format, self.notification_content, self.sending_status, self.custom_attributes)
    def clone_write_new_uid(self):
        return notification_instance_write_dto(base_dto.get_random_uid(), self.account_instance_uid, self.notification_type, self.notification_topic, self.notification_format, self.notification_content, self.sending_status, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return notification_instance_write_dto(uid, self.account_instance_uid, self.notification_type, self.notification_topic, self.notification_format, self.notification_content, self.sending_status, self.custom_attributes)
    def get_model(self) -> base_model:
        return notification_instance_model
    def get_key(self) -> str:
        return self.notification_instance_uid
    def get_uid(self) -> str:
        return self.notification_instance_uid
    def get_list_values(self) -> list[any]:
        return [self.notification_instance_uid, self.account_instance_uid, self.notification_type, self.notification_topic, self.notification_format, self.notification_content, self.sending_status, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.notification_instance_uid, self.account_instance_uid, self.notification_type, self.notification_topic, self.notification_format, self.notification_content, self.sending_status]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.account_instance_uid, self.notification_type, self.notification_topic, self.notification_format, self.notification_content, self.sending_status, self.custom_attributes, updated_by, self.notification_instance_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.notification_instance_uid, self.account_instance_uid, self.notification_type, self.notification_topic, self.notification_format, self.notification_content, self.sending_status, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.account_instance_uid, self.notification_type, self.notification_topic, self.notification_format, self.notification_content, self.sending_status]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.account_instance_uid, self.notification_type, self.notification_topic, self.notification_format, self.notification_content, self.sending_status, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_key() == obj.get_key()
    def update_uid(self, uid: str):
        self.notification_instance_uid = uid
    def update_uid_attributes(self, notification_instance_uid: str , account_instance_uid: str , notification_type: str , notification_topic: str , notification_format: str , notification_content: str , sending_status: str ):
        self.notification_instance_uid = notification_instance_uid
        self.account_instance_uid = account_instance_uid
        self.notification_type = notification_type
        self.notification_topic = notification_topic
        self.notification_format = notification_format
        self.notification_content = notification_content
        self.sending_status = sending_status
    def update_attributes(self, account_instance_uid: str , notification_type: str , notification_topic: str , notification_format: str , notification_content: str , sending_status: str ):
        self.account_instance_uid = account_instance_uid
        self.notification_type = notification_type
        self.notification_topic = notification_topic
        self.notification_format = notification_format
        self.notification_content = notification_content
        self.sending_status = sending_status


@dataclass(frozen=False)
class project_budget_write_dto(base_write_dto):
    project_budget_uid: str
    project_instance_uid: str
    budget_name: str
    budget_currency: str
    budget_value: str
    is_current: int
    def __init__(self, project_budget_uid: str , project_instance_uid: str , budget_name: str , budget_currency: str , budget_value: str , is_current: int , custom_attributes: str = "{}"):
        self.project_budget_uid = project_budget_uid
        self.project_instance_uid = project_instance_uid
        self.budget_name = budget_name
        self.budget_currency = budget_currency
        self.budget_value = budget_value
        self.is_current = is_current
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
    def new_write(cls, project_budget_uid: str , project_instance_uid: str , budget_name: str , budget_currency: str , budget_value: str , is_current: int ):
        return cls(project_budget_uid, project_instance_uid, budget_name, budget_currency, budget_value, is_current)
    @classmethod
    def new_write_random_uid(cls, project_instance_uid: str , budget_name: str , budget_currency: str , budget_value: str , is_current: int ):
        return cls(base_dto.get_random_uid(), project_instance_uid, budget_name, budget_currency, budget_value, is_current)
    @classmethod
    def get_class_model(cls) -> base_model:
        return project_budget_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["project_budget_uid"], d["project_instance_uid"], d["budget_name"], d["budget_currency"], d["budget_value"], d["is_current"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return project_budget_write_dto(self.project_budget_uid, self.project_instance_uid, self.budget_name, self.budget_currency, self.budget_value, self.is_current, self.custom_attributes)
    def clone_write_new_uid(self):
        return project_budget_write_dto(base_dto.get_random_uid(), self.project_instance_uid, self.budget_name, self.budget_currency, self.budget_value, self.is_current, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return project_budget_write_dto(uid, self.project_instance_uid, self.budget_name, self.budget_currency, self.budget_value, self.is_current, self.custom_attributes)
    def get_model(self) -> base_model:
        return project_budget_model
    def get_key(self) -> str:
        return self.project_budget_uid
    def get_uid(self) -> str:
        return self.project_budget_uid
    def get_list_values(self) -> list[any]:
        return [self.project_budget_uid, self.project_instance_uid, self.budget_name, self.budget_currency, self.budget_value, self.is_current, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.project_budget_uid, self.project_instance_uid, self.budget_name, self.budget_currency, self.budget_value, self.is_current]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.project_instance_uid, self.budget_name, self.budget_currency, self.budget_value, self.is_current, self.custom_attributes, updated_by, self.project_budget_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.project_budget_uid, self.project_instance_uid, self.budget_name, self.budget_currency, self.budget_value, self.is_current, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.project_instance_uid, self.budget_name, self.budget_currency, self.budget_value, self.is_current]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.project_instance_uid, self.budget_name, self.budget_currency, self.budget_value, self.is_current, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_key() == obj.get_key()
    def update_uid(self, uid: str):
        self.project_budget_uid = uid
    def update_uid_attributes(self, project_budget_uid: str , project_instance_uid: str , budget_name: str , budget_currency: str , budget_value: str , is_current: int ):
        self.project_budget_uid = project_budget_uid
        self.project_instance_uid = project_instance_uid
        self.budget_name = budget_name
        self.budget_currency = budget_currency
        self.budget_value = budget_value
        self.is_current = is_current
    def update_attributes(self, project_instance_uid: str , budget_name: str , budget_currency: str , budget_value: str , is_current: int ):
        self.project_instance_uid = project_instance_uid
        self.budget_name = budget_name
        self.budget_currency = budget_currency
        self.budget_value = budget_value
        self.is_current = is_current


@dataclass(frozen=False)
class project_group_write_dto(base_write_dto):
    project_group_uid: str
    project_group_name: str
    project_group_description: str
    def __init__(self, project_group_uid: str , project_group_name: str , project_group_description: str , custom_attributes: str = "{}"):
        self.project_group_uid = project_group_uid
        self.project_group_name = project_group_name
        self.project_group_description = project_group_description
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
    def new_write(cls, project_group_uid: str , project_group_name: str , project_group_description: str ):
        return cls(project_group_uid, project_group_name, project_group_description)
    @classmethod
    def new_write_random_uid(cls, project_group_name: str , project_group_description: str ):
        return cls(base_dto.get_random_uid(), project_group_name, project_group_description)
    @classmethod
    def get_class_model(cls) -> base_model:
        return project_group_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["project_group_uid"], d["project_group_name"], d["project_group_description"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return project_group_write_dto(self.project_group_uid, self.project_group_name, self.project_group_description, self.custom_attributes)
    def clone_write_new_uid(self):
        return project_group_write_dto(base_dto.get_random_uid(), self.project_group_name, self.project_group_description, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return project_group_write_dto(uid, self.project_group_name, self.project_group_description, self.custom_attributes)
    def get_model(self) -> base_model:
        return project_group_model
    def get_key(self) -> str:
        return self.project_group_uid
    def get_uid(self) -> str:
        return self.project_group_uid
    def get_list_values(self) -> list[any]:
        return [self.project_group_uid, self.project_group_name, self.project_group_description, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.project_group_uid, self.project_group_name, self.project_group_description]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.project_group_name, self.project_group_description, self.custom_attributes, updated_by, self.project_group_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.project_group_uid, self.project_group_name, self.project_group_description, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.project_group_name, self.project_group_description]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.project_group_name, self.project_group_description, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_key() == obj.get_key()
    def update_uid(self, uid: str):
        self.project_group_uid = uid
    def update_uid_attributes(self, project_group_uid: str , project_group_name: str , project_group_description: str ):
        self.project_group_uid = project_group_uid
        self.project_group_name = project_group_name
        self.project_group_description = project_group_description
    def update_attributes(self, project_group_name: str , project_group_description: str ):
        self.project_group_name = project_group_name
        self.project_group_description = project_group_description


@dataclass(frozen=False)
class project_instance_write_dto(base_write_dto):
    project_instance_uid: str
    client_instance_uid: str
    manager_account_instance_uid: str
    project_group_uid: str
    project_name: str
    project_code: str
    is_billable: int
    start_date: datetime.datetime  | None
    end_date: datetime.datetime  | None
    current_billed: str
    budget: str
    def __init__(self, project_instance_uid: str , client_instance_uid: str , manager_account_instance_uid: str , project_group_uid: str , project_name: str , project_code: str , is_billable: int , start_date: datetime.datetime  | None, end_date: datetime.datetime  | None, current_billed: str , budget: str , custom_attributes: str = "{}"):
        self.project_instance_uid = project_instance_uid
        self.client_instance_uid = client_instance_uid
        self.manager_account_instance_uid = manager_account_instance_uid
        self.project_group_uid = project_group_uid
        self.project_name = project_name
        self.project_code = project_code
        self.is_billable = is_billable
        self.start_date = start_date
        self.end_date = end_date
        self.current_billed = current_billed
        self.budget = budget
        self.custom_attributes = custom_attributes
    @classmethod
    def empty_write(cls):
        return cls("", "", "", "", "", "", 0, datetime.datetime.now(), datetime.datetime.now(), "", "")
    @classmethod
    def default_write(cls):
        return cls(base_dto.get_random_uid(), "", "", "", "", "", 0, datetime.datetime.now(), datetime.datetime.now(), "", "")
    @classmethod
    def random_write(cls):
        return cls(base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), 0, datetime.datetime.now(), datetime.datetime.now(), "", "")
    @classmethod
    def new_write(cls, project_instance_uid: str , client_instance_uid: str , manager_account_instance_uid: str , project_group_uid: str , project_name: str , project_code: str , is_billable: int , start_date: datetime.datetime  | None, end_date: datetime.datetime  | None, current_billed: str , budget: str ):
        return cls(project_instance_uid, client_instance_uid, manager_account_instance_uid, project_group_uid, project_name, project_code, is_billable, start_date, end_date, current_billed, budget)
    @classmethod
    def new_write_random_uid(cls, client_instance_uid: str , manager_account_instance_uid: str , project_group_uid: str , project_name: str , project_code: str , is_billable: int , start_date: datetime.datetime  | None, end_date: datetime.datetime  | None, current_billed: str , budget: str ):
        return cls(base_dto.get_random_uid(), client_instance_uid, manager_account_instance_uid, project_group_uid, project_name, project_code, is_billable, start_date, end_date, current_billed, budget)
    @classmethod
    def get_class_model(cls) -> base_model:
        return project_instance_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["project_instance_uid"], d["client_instance_uid"], d["manager_account_instance_uid"], d["project_group_uid"], d["project_name"], d["project_code"], d["is_billable"], d["start_date"], d["end_date"], d["current_billed"], d["budget"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return project_instance_write_dto(self.project_instance_uid, self.client_instance_uid, self.manager_account_instance_uid, self.project_group_uid, self.project_name, self.project_code, self.is_billable, self.start_date, self.end_date, self.current_billed, self.budget, self.custom_attributes)
    def clone_write_new_uid(self):
        return project_instance_write_dto(base_dto.get_random_uid(), self.client_instance_uid, self.manager_account_instance_uid, self.project_group_uid, self.project_name, self.project_code, self.is_billable, self.start_date, self.end_date, self.current_billed, self.budget, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return project_instance_write_dto(uid, self.client_instance_uid, self.manager_account_instance_uid, self.project_group_uid, self.project_name, self.project_code, self.is_billable, self.start_date, self.end_date, self.current_billed, self.budget, self.custom_attributes)
    def get_model(self) -> base_model:
        return project_instance_model
    def get_key(self) -> str:
        return self.project_instance_uid
    def get_uid(self) -> str:
        return self.project_instance_uid
    def get_list_values(self) -> list[any]:
        return [self.project_instance_uid, self.client_instance_uid, self.manager_account_instance_uid, self.project_group_uid, self.project_name, self.project_code, self.is_billable, self.start_date, self.end_date, self.current_billed, self.budget, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.project_instance_uid, self.client_instance_uid, self.manager_account_instance_uid, self.project_group_uid, self.project_name, self.project_code, self.is_billable, self.start_date, self.end_date, self.current_billed, self.budget]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.client_instance_uid, self.manager_account_instance_uid, self.project_group_uid, self.project_name, self.project_code, self.is_billable, self.start_date, self.end_date, self.current_billed, self.budget, self.custom_attributes, updated_by, self.project_instance_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.project_instance_uid, self.client_instance_uid, self.manager_account_instance_uid, self.project_group_uid, self.project_name, self.project_code, self.is_billable, self.start_date, self.end_date, self.current_billed, self.budget, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.client_instance_uid, self.manager_account_instance_uid, self.project_group_uid, self.project_name, self.project_code, self.is_billable, self.start_date, self.end_date, self.current_billed, self.budget]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.client_instance_uid, self.manager_account_instance_uid, self.project_group_uid, self.project_name, self.project_code, self.is_billable, self.start_date, self.end_date, self.current_billed, self.budget, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_key() == obj.get_key()
    def update_uid(self, uid: str):
        self.project_instance_uid = uid
    def update_uid_attributes(self, project_instance_uid: str , client_instance_uid: str , manager_account_instance_uid: str , project_group_uid: str , project_name: str , project_code: str , is_billable: int , start_date: datetime.datetime  | None, end_date: datetime.datetime  | None, current_billed: str , budget: str ):
        self.project_instance_uid = project_instance_uid
        self.client_instance_uid = client_instance_uid
        self.manager_account_instance_uid = manager_account_instance_uid
        self.project_group_uid = project_group_uid
        self.project_name = project_name
        self.project_code = project_code
        self.is_billable = is_billable
        self.start_date = start_date
        self.end_date = end_date
        self.current_billed = current_billed
        self.budget = budget
    def update_attributes(self, client_instance_uid: str , manager_account_instance_uid: str , project_group_uid: str , project_name: str , project_code: str , is_billable: int , start_date: datetime.datetime  | None, end_date: datetime.datetime  | None, current_billed: str , budget: str ):
        self.client_instance_uid = client_instance_uid
        self.manager_account_instance_uid = manager_account_instance_uid
        self.project_group_uid = project_group_uid
        self.project_name = project_name
        self.project_code = project_code
        self.is_billable = is_billable
        self.start_date = start_date
        self.end_date = end_date
        self.current_billed = current_billed
        self.budget = budget


@dataclass(frozen=False)
class project_milestone_write_dto(base_write_dto):
    project_milestone_uid: str
    project_instance_uid: str
    project_budget_uid: str  | None
    milestone_name: str
    start_date: datetime.datetime
    end_date: datetime.datetime
    status_name: str
    def __init__(self, project_milestone_uid: str , project_instance_uid: str , project_budget_uid: str  | None, milestone_name: str , start_date: datetime.datetime , end_date: datetime.datetime , status_name: str , custom_attributes: str = "{}"):
        self.project_milestone_uid = project_milestone_uid
        self.project_instance_uid = project_instance_uid
        self.project_budget_uid = project_budget_uid
        self.milestone_name = milestone_name
        self.start_date = start_date
        self.end_date = end_date
        self.status_name = status_name
        self.custom_attributes = custom_attributes
    @classmethod
    def empty_write(cls):
        return cls("", "", "", "", datetime.datetime.now(), datetime.datetime.now(), "")
    @classmethod
    def default_write(cls):
        return cls(base_dto.get_random_uid(), "", "", "", datetime.datetime.now(), datetime.datetime.now(), "")
    @classmethod
    def random_write(cls):
        return cls(base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), datetime.datetime.now(), datetime.datetime.now(), base_dto.get_random_uid())
    @classmethod
    def new_write(cls, project_milestone_uid: str , project_instance_uid: str , project_budget_uid: str  | None, milestone_name: str , start_date: datetime.datetime , end_date: datetime.datetime , status_name: str ):
        return cls(project_milestone_uid, project_instance_uid, project_budget_uid, milestone_name, start_date, end_date, status_name)
    @classmethod
    def new_write_random_uid(cls, project_instance_uid: str , project_budget_uid: str  | None, milestone_name: str , start_date: datetime.datetime , end_date: datetime.datetime , status_name: str ):
        return cls(base_dto.get_random_uid(), project_instance_uid, project_budget_uid, milestone_name, start_date, end_date, status_name)
    @classmethod
    def get_class_model(cls) -> base_model:
        return project_milestone_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["project_milestone_uid"], d["project_instance_uid"], d["project_budget_uid"], d["milestone_name"], d["start_date"], d["end_date"], d["status_name"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return project_milestone_write_dto(self.project_milestone_uid, self.project_instance_uid, self.project_budget_uid, self.milestone_name, self.start_date, self.end_date, self.status_name, self.custom_attributes)
    def clone_write_new_uid(self):
        return project_milestone_write_dto(base_dto.get_random_uid(), self.project_instance_uid, self.project_budget_uid, self.milestone_name, self.start_date, self.end_date, self.status_name, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return project_milestone_write_dto(uid, self.project_instance_uid, self.project_budget_uid, self.milestone_name, self.start_date, self.end_date, self.status_name, self.custom_attributes)
    def get_model(self) -> base_model:
        return project_milestone_model
    def get_key(self) -> str:
        return self.project_milestone_uid
    def get_uid(self) -> str:
        return self.project_milestone_uid
    def get_list_values(self) -> list[any]:
        return [self.project_milestone_uid, self.project_instance_uid, self.project_budget_uid, self.milestone_name, self.start_date, self.end_date, self.status_name, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.project_milestone_uid, self.project_instance_uid, self.project_budget_uid, self.milestone_name, self.start_date, self.end_date, self.status_name]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.project_instance_uid, self.project_budget_uid, self.milestone_name, self.start_date, self.end_date, self.status_name, self.custom_attributes, updated_by, self.project_milestone_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.project_milestone_uid, self.project_instance_uid, self.project_budget_uid, self.milestone_name, self.start_date, self.end_date, self.status_name, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.project_instance_uid, self.project_budget_uid, self.milestone_name, self.start_date, self.end_date, self.status_name]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.project_instance_uid, self.project_budget_uid, self.milestone_name, self.start_date, self.end_date, self.status_name, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_key() == obj.get_key()
    def update_uid(self, uid: str):
        self.project_milestone_uid = uid
    def update_uid_attributes(self, project_milestone_uid: str , project_instance_uid: str , project_budget_uid: str  | None, milestone_name: str , start_date: datetime.datetime , end_date: datetime.datetime , status_name: str ):
        self.project_milestone_uid = project_milestone_uid
        self.project_instance_uid = project_instance_uid
        self.project_budget_uid = project_budget_uid
        self.milestone_name = milestone_name
        self.start_date = start_date
        self.end_date = end_date
        self.status_name = status_name
    def update_attributes(self, project_instance_uid: str , project_budget_uid: str  | None, milestone_name: str , start_date: datetime.datetime , end_date: datetime.datetime , status_name: str ):
        self.project_instance_uid = project_instance_uid
        self.project_budget_uid = project_budget_uid
        self.milestone_name = milestone_name
        self.start_date = start_date
        self.end_date = end_date
        self.status_name = status_name


@dataclass(frozen=False)
class system_attribute_write_dto(base_write_dto):
    system_attribute_uid: str
    system_object_uid: str
    column_name: str
    attribute_name: str
    attribute_type: str
    attribute_label: str
    attribute_description: str
    def __init__(self, system_attribute_uid: str , system_object_uid: str , column_name: str , attribute_name: str , attribute_type: str , attribute_label: str , attribute_description: str , custom_attributes: str = "{}"):
        self.system_attribute_uid = system_attribute_uid
        self.system_object_uid = system_object_uid
        self.column_name = column_name
        self.attribute_name = attribute_name
        self.attribute_type = attribute_type
        self.attribute_label = attribute_label
        self.attribute_description = attribute_description
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
    def new_write(cls, system_attribute_uid: str , system_object_uid: str , column_name: str , attribute_name: str , attribute_type: str , attribute_label: str , attribute_description: str ):
        return cls(system_attribute_uid, system_object_uid, column_name, attribute_name, attribute_type, attribute_label, attribute_description)
    @classmethod
    def new_write_random_uid(cls, system_object_uid: str , column_name: str , attribute_name: str , attribute_type: str , attribute_label: str , attribute_description: str ):
        return cls(base_dto.get_random_uid(), system_object_uid, column_name, attribute_name, attribute_type, attribute_label, attribute_description)
    @classmethod
    def get_class_model(cls) -> base_model:
        return system_attribute_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["system_attribute_uid"], d["system_object_uid"], d["column_name"], d["attribute_name"], d["attribute_type"], d["attribute_label"], d["attribute_description"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return system_attribute_write_dto(self.system_attribute_uid, self.system_object_uid, self.column_name, self.attribute_name, self.attribute_type, self.attribute_label, self.attribute_description, self.custom_attributes)
    def clone_write_new_uid(self):
        return system_attribute_write_dto(base_dto.get_random_uid(), self.system_object_uid, self.column_name, self.attribute_name, self.attribute_type, self.attribute_label, self.attribute_description, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return system_attribute_write_dto(uid, self.system_object_uid, self.column_name, self.attribute_name, self.attribute_type, self.attribute_label, self.attribute_description, self.custom_attributes)
    def get_model(self) -> base_model:
        return system_attribute_model
    def get_key(self) -> str:
        return self.system_attribute_uid
    def get_uid(self) -> str:
        return self.system_attribute_uid
    def get_list_values(self) -> list[any]:
        return [self.system_attribute_uid, self.system_object_uid, self.column_name, self.attribute_name, self.attribute_type, self.attribute_label, self.attribute_description, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.system_attribute_uid, self.system_object_uid, self.column_name, self.attribute_name, self.attribute_type, self.attribute_label, self.attribute_description]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.system_object_uid, self.column_name, self.attribute_name, self.attribute_type, self.attribute_label, self.attribute_description, self.custom_attributes, updated_by, self.system_attribute_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.system_attribute_uid, self.system_object_uid, self.column_name, self.attribute_name, self.attribute_type, self.attribute_label, self.attribute_description, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.system_object_uid, self.column_name, self.attribute_name, self.attribute_type, self.attribute_label, self.attribute_description]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.system_object_uid, self.column_name, self.attribute_name, self.attribute_type, self.attribute_label, self.attribute_description, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_key() == obj.get_key()
    def update_uid(self, uid: str):
        self.system_attribute_uid = uid
    def update_uid_attributes(self, system_attribute_uid: str , system_object_uid: str , column_name: str , attribute_name: str , attribute_type: str , attribute_label: str , attribute_description: str ):
        self.system_attribute_uid = system_attribute_uid
        self.system_object_uid = system_object_uid
        self.column_name = column_name
        self.attribute_name = attribute_name
        self.attribute_type = attribute_type
        self.attribute_label = attribute_label
        self.attribute_description = attribute_description
    def update_attributes(self, system_object_uid: str , column_name: str , attribute_name: str , attribute_type: str , attribute_label: str , attribute_description: str ):
        self.system_object_uid = system_object_uid
        self.column_name = column_name
        self.attribute_name = attribute_name
        self.attribute_type = attribute_type
        self.attribute_label = attribute_label
        self.attribute_description = attribute_description


@dataclass(frozen=False)
class system_change_write_dto(base_write_dto):
    system_change_uid: str
    account_instance_uid: str
    change_type: str
    change_name: str
    change_json: str
    def __init__(self, system_change_uid: str , account_instance_uid: str , change_type: str , change_name: str , change_json: str , custom_attributes: str = "{}"):
        self.system_change_uid = system_change_uid
        self.account_instance_uid = account_instance_uid
        self.change_type = change_type
        self.change_name = change_name
        self.change_json = change_json
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
    def new_write(cls, system_change_uid: str , account_instance_uid: str , change_type: str , change_name: str , change_json: str ):
        return cls(system_change_uid, account_instance_uid, change_type, change_name, change_json)
    @classmethod
    def new_write_random_uid(cls, account_instance_uid: str , change_type: str , change_name: str , change_json: str ):
        return cls(base_dto.get_random_uid(), account_instance_uid, change_type, change_name, change_json)
    @classmethod
    def get_class_model(cls) -> base_model:
        return system_change_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["system_change_uid"], d["account_instance_uid"], d["change_type"], d["change_name"], d["change_json"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return system_change_write_dto(self.system_change_uid, self.account_instance_uid, self.change_type, self.change_name, self.change_json, self.custom_attributes)
    def clone_write_new_uid(self):
        return system_change_write_dto(base_dto.get_random_uid(), self.account_instance_uid, self.change_type, self.change_name, self.change_json, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return system_change_write_dto(uid, self.account_instance_uid, self.change_type, self.change_name, self.change_json, self.custom_attributes)
    def get_model(self) -> base_model:
        return system_change_model
    def get_key(self) -> str:
        return self.system_change_uid
    def get_uid(self) -> str:
        return self.system_change_uid
    def get_list_values(self) -> list[any]:
        return [self.system_change_uid, self.account_instance_uid, self.change_type, self.change_name, self.change_json, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.system_change_uid, self.account_instance_uid, self.change_type, self.change_name, self.change_json]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.account_instance_uid, self.change_type, self.change_name, self.change_json, self.custom_attributes, updated_by, self.system_change_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.system_change_uid, self.account_instance_uid, self.change_type, self.change_name, self.change_json, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.account_instance_uid, self.change_type, self.change_name, self.change_json]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.account_instance_uid, self.change_type, self.change_name, self.change_json, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_key() == obj.get_key()
    def update_uid(self, uid: str):
        self.system_change_uid = uid
    def update_uid_attributes(self, system_change_uid: str , account_instance_uid: str , change_type: str , change_name: str , change_json: str ):
        self.system_change_uid = system_change_uid
        self.account_instance_uid = account_instance_uid
        self.change_type = change_type
        self.change_name = change_name
        self.change_json = change_json
    def update_attributes(self, account_instance_uid: str , change_type: str , change_name: str , change_json: str ):
        self.account_instance_uid = account_instance_uid
        self.change_type = change_type
        self.change_name = change_name
        self.change_json = change_json


@dataclass(frozen=False)
class system_exception_write_dto(base_write_dto):
    system_exception_uid: str
    system_instance_uid: str
    exception_class: str
    exception_message: str
    exception_stacktrace: str
    def __init__(self, system_exception_uid: str , system_instance_uid: str , exception_class: str , exception_message: str , exception_stacktrace: str , custom_attributes: str = "{}"):
        self.system_exception_uid = system_exception_uid
        self.system_instance_uid = system_instance_uid
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
    def new_write(cls, system_exception_uid: str , system_instance_uid: str , exception_class: str , exception_message: str , exception_stacktrace: str ):
        return cls(system_exception_uid, system_instance_uid, exception_class, exception_message, exception_stacktrace)
    @classmethod
    def new_write_random_uid(cls, system_instance_uid: str , exception_class: str , exception_message: str , exception_stacktrace: str ):
        return cls(base_dto.get_random_uid(), system_instance_uid, exception_class, exception_message, exception_stacktrace)
    @classmethod
    def get_class_model(cls) -> base_model:
        return system_exception_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["system_exception_uid"], d["system_instance_uid"], d["exception_class"], d["exception_message"], d["exception_stacktrace"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return system_exception_write_dto(self.system_exception_uid, self.system_instance_uid, self.exception_class, self.exception_message, self.exception_stacktrace, self.custom_attributes)
    def clone_write_new_uid(self):
        return system_exception_write_dto(base_dto.get_random_uid(), self.system_instance_uid, self.exception_class, self.exception_message, self.exception_stacktrace, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return system_exception_write_dto(uid, self.system_instance_uid, self.exception_class, self.exception_message, self.exception_stacktrace, self.custom_attributes)
    def get_model(self) -> base_model:
        return system_exception_model
    def get_key(self) -> str:
        return self.system_exception_uid
    def get_uid(self) -> str:
        return self.system_exception_uid
    def get_list_values(self) -> list[any]:
        return [self.system_exception_uid, self.system_instance_uid, self.exception_class, self.exception_message, self.exception_stacktrace, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.system_exception_uid, self.system_instance_uid, self.exception_class, self.exception_message, self.exception_stacktrace]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.system_instance_uid, self.exception_class, self.exception_message, self.exception_stacktrace, self.custom_attributes, updated_by, self.system_exception_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.system_exception_uid, self.system_instance_uid, self.exception_class, self.exception_message, self.exception_stacktrace, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.system_instance_uid, self.exception_class, self.exception_message, self.exception_stacktrace]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.system_instance_uid, self.exception_class, self.exception_message, self.exception_stacktrace, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_key() == obj.get_key()
    def update_uid(self, uid: str):
        self.system_exception_uid = uid
    def update_uid_attributes(self, system_exception_uid: str , system_instance_uid: str , exception_class: str , exception_message: str , exception_stacktrace: str ):
        self.system_exception_uid = system_exception_uid
        self.system_instance_uid = system_instance_uid
        self.exception_class = exception_class
        self.exception_message = exception_message
        self.exception_stacktrace = exception_stacktrace
    def update_attributes(self, system_instance_uid: str , exception_class: str , exception_message: str , exception_stacktrace: str ):
        self.system_instance_uid = system_instance_uid
        self.exception_class = exception_class
        self.exception_message = exception_message
        self.exception_stacktrace = exception_stacktrace


@dataclass(frozen=False)
class system_instance_write_dto(base_write_dto):
    system_instance_uid: str
    host_name: str
    host_ip: str
    local_path: str
    app_version: str
    mode_name: str
    def __init__(self, system_instance_uid: str , host_name: str , host_ip: str , local_path: str , app_version: str , mode_name: str , custom_attributes: str = "{}"):
        self.system_instance_uid = system_instance_uid
        self.host_name = host_name
        self.host_ip = host_ip
        self.local_path = local_path
        self.app_version = app_version
        self.mode_name = mode_name
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
    def new_write(cls, system_instance_uid: str , host_name: str , host_ip: str , local_path: str , app_version: str , mode_name: str ):
        return cls(system_instance_uid, host_name, host_ip, local_path, app_version, mode_name)
    @classmethod
    def new_write_random_uid(cls, host_name: str , host_ip: str , local_path: str , app_version: str , mode_name: str ):
        return cls(base_dto.get_random_uid(), host_name, host_ip, local_path, app_version, mode_name)
    @classmethod
    def get_class_model(cls) -> base_model:
        return system_instance_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["system_instance_uid"], d["host_name"], d["host_ip"], d["local_path"], d["app_version"], d["mode_name"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return system_instance_write_dto(self.system_instance_uid, self.host_name, self.host_ip, self.local_path, self.app_version, self.mode_name, self.custom_attributes)
    def clone_write_new_uid(self):
        return system_instance_write_dto(base_dto.get_random_uid(), self.host_name, self.host_ip, self.local_path, self.app_version, self.mode_name, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return system_instance_write_dto(uid, self.host_name, self.host_ip, self.local_path, self.app_version, self.mode_name, self.custom_attributes)
    def get_model(self) -> base_model:
        return system_instance_model
    def get_key(self) -> str:
        return self.system_instance_uid
    def get_uid(self) -> str:
        return self.system_instance_uid
    def get_list_values(self) -> list[any]:
        return [self.system_instance_uid, self.host_name, self.host_ip, self.local_path, self.app_version, self.mode_name, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.system_instance_uid, self.host_name, self.host_ip, self.local_path, self.app_version, self.mode_name]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.host_name, self.host_ip, self.local_path, self.app_version, self.mode_name, self.custom_attributes, updated_by, self.system_instance_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.system_instance_uid, self.host_name, self.host_ip, self.local_path, self.app_version, self.mode_name, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.host_name, self.host_ip, self.local_path, self.app_version, self.mode_name]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.host_name, self.host_ip, self.local_path, self.app_version, self.mode_name, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_key() == obj.get_key()
    def update_uid(self, uid: str):
        self.system_instance_uid = uid
    def update_uid_attributes(self, system_instance_uid: str , host_name: str , host_ip: str , local_path: str , app_version: str , mode_name: str ):
        self.system_instance_uid = system_instance_uid
        self.host_name = host_name
        self.host_ip = host_ip
        self.local_path = local_path
        self.app_version = app_version
        self.mode_name = mode_name
    def update_attributes(self, host_name: str , host_ip: str , local_path: str , app_version: str , mode_name: str ):
        self.host_name = host_name
        self.host_ip = host_ip
        self.local_path = local_path
        self.app_version = app_version
        self.mode_name = mode_name


@dataclass(frozen=False)
class system_object_write_dto(base_write_dto):
    system_object_uid: str
    object_name: str
    object_type: str
    table_name: str
    key_name: str
    parent_system_object_uid: str  | None
    def __init__(self, system_object_uid: str , object_name: str , object_type: str , table_name: str , key_name: str , parent_system_object_uid: str  | None, custom_attributes: str = "{}"):
        self.system_object_uid = system_object_uid
        self.object_name = object_name
        self.object_type = object_type
        self.table_name = table_name
        self.key_name = key_name
        self.parent_system_object_uid = parent_system_object_uid
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
    def new_write(cls, system_object_uid: str , object_name: str , object_type: str , table_name: str , key_name: str , parent_system_object_uid: str  | None):
        return cls(system_object_uid, object_name, object_type, table_name, key_name, parent_system_object_uid)
    @classmethod
    def new_write_random_uid(cls, object_name: str , object_type: str , table_name: str , key_name: str , parent_system_object_uid: str  | None):
        return cls(base_dto.get_random_uid(), object_name, object_type, table_name, key_name, parent_system_object_uid)
    @classmethod
    def get_class_model(cls) -> base_model:
        return system_object_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["system_object_uid"], d["object_name"], d["object_type"], d["table_name"], d["key_name"], d["parent_system_object_uid"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return system_object_write_dto(self.system_object_uid, self.object_name, self.object_type, self.table_name, self.key_name, self.parent_system_object_uid, self.custom_attributes)
    def clone_write_new_uid(self):
        return system_object_write_dto(base_dto.get_random_uid(), self.object_name, self.object_type, self.table_name, self.key_name, self.parent_system_object_uid, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return system_object_write_dto(uid, self.object_name, self.object_type, self.table_name, self.key_name, self.parent_system_object_uid, self.custom_attributes)
    def get_model(self) -> base_model:
        return system_object_model
    def get_key(self) -> str:
        return self.system_object_uid
    def get_uid(self) -> str:
        return self.system_object_uid
    def get_list_values(self) -> list[any]:
        return [self.system_object_uid, self.object_name, self.object_type, self.table_name, self.key_name, self.parent_system_object_uid, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.system_object_uid, self.object_name, self.object_type, self.table_name, self.key_name, self.parent_system_object_uid]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.object_name, self.object_type, self.table_name, self.key_name, self.parent_system_object_uid, self.custom_attributes, updated_by, self.system_object_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.system_object_uid, self.object_name, self.object_type, self.table_name, self.key_name, self.parent_system_object_uid, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.object_name, self.object_type, self.table_name, self.key_name, self.parent_system_object_uid]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.object_name, self.object_type, self.table_name, self.key_name, self.parent_system_object_uid, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_key() == obj.get_key()
    def update_uid(self, uid: str):
        self.system_object_uid = uid
    def update_uid_attributes(self, system_object_uid: str , object_name: str , object_type: str , table_name: str , key_name: str , parent_system_object_uid: str  | None):
        self.system_object_uid = system_object_uid
        self.object_name = object_name
        self.object_type = object_type
        self.table_name = table_name
        self.key_name = key_name
        self.parent_system_object_uid = parent_system_object_uid
    def update_attributes(self, object_name: str , object_type: str , table_name: str , key_name: str , parent_system_object_uid: str  | None):
        self.object_name = object_name
        self.object_type = object_type
        self.table_name = table_name
        self.key_name = key_name
        self.parent_system_object_uid = parent_system_object_uid


@dataclass(frozen=False)
class system_setting_write_dto(base_write_dto):
    system_setting_uid: str
    account_instance_uid: str  | None
    setting_name: str
    setting_value: str
    def __init__(self, system_setting_uid: str , account_instance_uid: str  | None, setting_name: str , setting_value: str , custom_attributes: str = "{}"):
        self.system_setting_uid = system_setting_uid
        self.account_instance_uid = account_instance_uid
        self.setting_name = setting_name
        self.setting_value = setting_value
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
    def new_write(cls, system_setting_uid: str , account_instance_uid: str  | None, setting_name: str , setting_value: str ):
        return cls(system_setting_uid, account_instance_uid, setting_name, setting_value)
    @classmethod
    def new_write_random_uid(cls, account_instance_uid: str  | None, setting_name: str , setting_value: str ):
        return cls(base_dto.get_random_uid(), account_instance_uid, setting_name, setting_value)
    @classmethod
    def get_class_model(cls) -> base_model:
        return system_setting_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["system_setting_uid"], d["account_instance_uid"], d["setting_name"], d["setting_value"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return system_setting_write_dto(self.system_setting_uid, self.account_instance_uid, self.setting_name, self.setting_value, self.custom_attributes)
    def clone_write_new_uid(self):
        return system_setting_write_dto(base_dto.get_random_uid(), self.account_instance_uid, self.setting_name, self.setting_value, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return system_setting_write_dto(uid, self.account_instance_uid, self.setting_name, self.setting_value, self.custom_attributes)
    def get_model(self) -> base_model:
        return system_setting_model
    def get_key(self) -> str:
        return self.system_setting_uid
    def get_uid(self) -> str:
        return self.system_setting_uid
    def get_list_values(self) -> list[any]:
        return [self.system_setting_uid, self.account_instance_uid, self.setting_name, self.setting_value, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.system_setting_uid, self.account_instance_uid, self.setting_name, self.setting_value]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.account_instance_uid, self.setting_name, self.setting_value, self.custom_attributes, updated_by, self.system_setting_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.system_setting_uid, self.account_instance_uid, self.setting_name, self.setting_value, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.account_instance_uid, self.setting_name, self.setting_value]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.account_instance_uid, self.setting_name, self.setting_value, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_key() == obj.get_key()
    def update_uid(self, uid: str):
        self.system_setting_uid = uid
    def update_uid_attributes(self, system_setting_uid: str , account_instance_uid: str  | None, setting_name: str , setting_value: str ):
        self.system_setting_uid = system_setting_uid
        self.account_instance_uid = account_instance_uid
        self.setting_name = setting_name
        self.setting_value = setting_value
    def update_attributes(self, account_instance_uid: str  | None, setting_name: str , setting_value: str ):
        self.account_instance_uid = account_instance_uid
        self.setting_name = setting_name
        self.setting_value = setting_value


@dataclass(frozen=False)
class system_state_write_dto(base_write_dto):
    system_state_uid: str
    system_instance_uid: str
    host_name: str
    host_ip: str
    local_path: str
    app_version: str
    mode_name: str
    def __init__(self, system_state_uid: str , system_instance_uid: str , host_name: str , host_ip: str , local_path: str , app_version: str , mode_name: str , custom_attributes: str = "{}"):
        self.system_state_uid = system_state_uid
        self.system_instance_uid = system_instance_uid
        self.host_name = host_name
        self.host_ip = host_ip
        self.local_path = local_path
        self.app_version = app_version
        self.mode_name = mode_name
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
    def new_write(cls, system_state_uid: str , system_instance_uid: str , host_name: str , host_ip: str , local_path: str , app_version: str , mode_name: str ):
        return cls(system_state_uid, system_instance_uid, host_name, host_ip, local_path, app_version, mode_name)
    @classmethod
    def new_write_random_uid(cls, system_instance_uid: str , host_name: str , host_ip: str , local_path: str , app_version: str , mode_name: str ):
        return cls(base_dto.get_random_uid(), system_instance_uid, host_name, host_ip, local_path, app_version, mode_name)
    @classmethod
    def get_class_model(cls) -> base_model:
        return system_state_model
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["system_state_uid"], d["system_instance_uid"], d["host_name"], d["host_ip"], d["local_path"], d["app_version"], d["mode_name"])
    def to_write_dict(self) -> dict:
        return asdict(self)
    def clone_write(self):
        return system_state_write_dto(self.system_state_uid, self.system_instance_uid, self.host_name, self.host_ip, self.local_path, self.app_version, self.mode_name, self.custom_attributes)
    def clone_write_new_uid(self):
        return system_state_write_dto(base_dto.get_random_uid(), self.system_instance_uid, self.host_name, self.host_ip, self.local_path, self.app_version, self.mode_name, self.custom_attributes)
    def clone_with_uid(self, uid: str):
        return system_state_write_dto(uid, self.system_instance_uid, self.host_name, self.host_ip, self.local_path, self.app_version, self.mode_name, self.custom_attributes)
    def get_model(self) -> base_model:
        return system_state_model
    def get_key(self) -> str:
        return self.system_state_uid
    def get_uid(self) -> str:
        return self.system_state_uid
    def get_list_values(self) -> list[any]:
        return [self.system_state_uid, self.system_instance_uid, self.host_name, self.host_ip, self.local_path, self.app_version, self.mode_name, self.custom_attributes]
    def get_list_values_no_custom(self) -> list[any]:
        return [self.system_state_uid, self.system_instance_uid, self.host_name, self.host_ip, self.local_path, self.app_version, self.mode_name]
    def get_list_write_update(self, updated_by: str) -> list[any]:
        return [self.system_instance_uid, self.host_name, self.host_ip, self.local_path, self.app_version, self.mode_name, self.custom_attributes, updated_by, self.system_state_uid]
    def get_list_write_insert(self, created_by: str) -> list[any]:
        return [self.system_state_uid, self.system_instance_uid, self.host_name, self.host_ip, self.local_path, self.app_version, self.mode_name, created_by, created_by, self.custom_attributes]
    def get_nonkey_values(self) -> list[any]:
        return [self.system_instance_uid, self.host_name, self.host_ip, self.local_path, self.app_version, self.mode_name]
    def get_nonkey_values_with_custom(self) -> list[any]:
        return [self.system_instance_uid, self.host_name, self.host_ip, self.local_path, self.app_version, self.mode_name, self.custom_attributes]
    def to_json_write(self) -> str:
        return json.dumps(self.to_write_dict())
    def compare_uid(self, obj: base_write_dto) -> bool:
        return self.get_key() == obj.get_key()
    def update_uid(self, uid: str):
        self.system_state_uid = uid
    def update_uid_attributes(self, system_state_uid: str , system_instance_uid: str , host_name: str , host_ip: str , local_path: str , app_version: str , mode_name: str ):
        self.system_state_uid = system_state_uid
        self.system_instance_uid = system_instance_uid
        self.host_name = host_name
        self.host_ip = host_ip
        self.local_path = local_path
        self.app_version = app_version
        self.mode_name = mode_name
    def update_attributes(self, system_instance_uid: str , host_name: str , host_ip: str , local_path: str , app_version: str , mode_name: str ):
        self.system_instance_uid = system_instance_uid
        self.host_name = host_name
        self.host_ip = host_ip
        self.local_path = local_path
        self.app_version = app_version
        self.mode_name = mode_name

