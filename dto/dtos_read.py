import datetime
from datetime import datetime
from abc import abstractmethod
from dataclasses import dataclass
from dto.dtos import *
from dto.dtos_thin import *
from dto.dtos_write import *


@dataclass(frozen=False)
class account_division_read_dto(base_read_dto, account_division_write_dto):
    id: int
    account_division_uid: str
    division_name: str
    division_description: str
    row_guid: str
    row_version: int
    is_active: int
    created_date: datetime.datetime
    created_by: str
    last_updated_date: datetime.datetime
    last_updated_by: str
    removed_date: datetime.datetime  | None
    removed_by: str  | None
    custom_attributes: str
    def __init__(self, id: int , account_division_uid: str , division_name: str , division_description: str , row_guid: str , row_version: int , is_active: int , created_date: datetime.datetime , created_by: str , last_updated_date: datetime.datetime , last_updated_by: str , removed_date: datetime.datetime  | None, removed_by: str  | None, custom_attributes: str ):
        self.id = id
        self.account_division_uid = account_division_uid
        self.division_name = division_name
        self.division_description = division_description
        self.row_guid = row_guid
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
    def new_read_default(cls, account_division_uid: str , division_name: str , division_description: str ):
        return cls(0, account_division_uid, division_name, division_description, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_full(cls, id: int , account_division_uid: str , division_name: str , division_description: str , row_guid: str , row_version: int , is_active: int , created_date: datetime.datetime , created_by: str , last_updated_date: datetime.datetime , last_updated_by: str , removed_date: datetime.datetime  | None, removed_by: str  | None, custom_attributes: str ):
        return cls(id, account_division_uid, division_name, division_description, row_guid, row_version, is_active, created_date, created_by, last_updated_date, last_updated_by, removed_date, removed_by, custom_attributes)
    @classmethod
    def from_write(cls, dto: account_division_write_dto):
        return cls(0, dto.account_division_uid, dto.division_name, dto.division_description, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, dto.custom_attributes)
    def clone_read(self):
        return account_division_read_dto(self.id, self.account_division_uid, self.division_name, self.division_description, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes)
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["id"], d["account_division_uid"], d["division_name"], d["division_description"], d["row_guid"], d["row_version"], d["is_active"], d["created_date"], d["created_by"], d["last_updated_date"], d["last_updated_by"], d["removed_date"], d["removed_by"], d["custom_attributes"])
    def to_read_dict(self) -> dict:
        return asdict(self)
    def to_write(self) -> account_division_write_dto:
        return account_division_write_dto(self.account_division_uid, self.division_name, self.division_description, self.custom_attributes)
    def to_thin(self) -> account_division_thin_dto:
        return account_division_thin_dto(self.account_division_uid, self.row_guid, self.is_active)
    def touch(self, updated_by: str = "system"):
        self.last_updated_date = datetime.datetime.now()
        self.last_updated_by = updated_by
        self.row_version = self.row_version+1
    def get_list_all_values(self) -> list[any]:
        return [self.id, self.account_division_uid, self.division_name, self.division_description, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]
    def get_list_update_values(self, updated_by: str) -> list[any]:
        return [self.division_name, self.division_description, self.custom_attributes, updated_by, self.account_division_uid]
    def is_older_than(self, dt: datetime.datetime) -> bool:
        return self.created_date < dt
    def is_newer_than(self, dt: datetime.datetime) -> bool:
        return self.created_date > dt
    def to_json_read(self) -> str:
        return json.dumps(self.to_read_dict())


@dataclass(frozen=False)
class account_group_read_dto(base_read_dto, account_group_write_dto):
    id: int
    account_group_uid: str
    account_group_name: str
    account_group_description: str
    row_guid: str
    row_version: int
    is_active: int
    created_date: datetime.datetime
    created_by: str
    last_updated_date: datetime.datetime
    last_updated_by: str
    removed_date: datetime.datetime  | None
    removed_by: str  | None
    custom_attributes: str
    def __init__(self, id: int , account_group_uid: str , account_group_name: str , account_group_description: str , row_guid: str , row_version: int , is_active: int , created_date: datetime.datetime , created_by: str , last_updated_date: datetime.datetime , last_updated_by: str , removed_date: datetime.datetime  | None, removed_by: str  | None, custom_attributes: str ):
        self.id = id
        self.account_group_uid = account_group_uid
        self.account_group_name = account_group_name
        self.account_group_description = account_group_description
        self.row_guid = row_guid
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
    def new_read_default(cls, account_group_uid: str , account_group_name: str , account_group_description: str ):
        return cls(0, account_group_uid, account_group_name, account_group_description, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_full(cls, id: int , account_group_uid: str , account_group_name: str , account_group_description: str , row_guid: str , row_version: int , is_active: int , created_date: datetime.datetime , created_by: str , last_updated_date: datetime.datetime , last_updated_by: str , removed_date: datetime.datetime  | None, removed_by: str  | None, custom_attributes: str ):
        return cls(id, account_group_uid, account_group_name, account_group_description, row_guid, row_version, is_active, created_date, created_by, last_updated_date, last_updated_by, removed_date, removed_by, custom_attributes)
    @classmethod
    def from_write(cls, dto: account_group_write_dto):
        return cls(0, dto.account_group_uid, dto.account_group_name, dto.account_group_description, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, dto.custom_attributes)
    def clone_read(self):
        return account_group_read_dto(self.id, self.account_group_uid, self.account_group_name, self.account_group_description, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes)
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["id"], d["account_group_uid"], d["account_group_name"], d["account_group_description"], d["row_guid"], d["row_version"], d["is_active"], d["created_date"], d["created_by"], d["last_updated_date"], d["last_updated_by"], d["removed_date"], d["removed_by"], d["custom_attributes"])
    def to_read_dict(self) -> dict:
        return asdict(self)
    def to_write(self) -> account_group_write_dto:
        return account_group_write_dto(self.account_group_uid, self.account_group_name, self.account_group_description, self.custom_attributes)
    def to_thin(self) -> account_group_thin_dto:
        return account_group_thin_dto(self.account_group_uid, self.row_guid, self.is_active)
    def touch(self, updated_by: str = "system"):
        self.last_updated_date = datetime.datetime.now()
        self.last_updated_by = updated_by
        self.row_version = self.row_version+1
    def get_list_all_values(self) -> list[any]:
        return [self.id, self.account_group_uid, self.account_group_name, self.account_group_description, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]
    def get_list_update_values(self, updated_by: str) -> list[any]:
        return [self.account_group_name, self.account_group_description, self.custom_attributes, updated_by, self.account_group_uid]
    def is_older_than(self, dt: datetime.datetime) -> bool:
        return self.created_date < dt
    def is_newer_than(self, dt: datetime.datetime) -> bool:
        return self.created_date > dt
    def to_json_read(self) -> str:
        return json.dumps(self.to_read_dict())


@dataclass(frozen=False)
class account_instance_read_dto(base_read_dto, account_instance_write_dto):
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
    row_version: int
    is_active: int
    created_date: datetime.datetime
    created_by: str
    last_updated_date: datetime.datetime
    last_updated_by: str
    removed_date: datetime.datetime  | None
    removed_by: str  | None
    custom_attributes: str
    def __init__(self, id: int , account_instance_uid: str , account_title_uid: str , account_division_uid: str , account_group_uid: str , auth_identity_uid: str , account_email: str , account_name: str , display_name: str , is_system: int , row_guid: str , row_version: int , is_active: int , created_date: datetime.datetime , created_by: str , last_updated_date: datetime.datetime , last_updated_by: str , removed_date: datetime.datetime  | None, removed_by: str  | None, custom_attributes: str ):
        self.id = id
        self.account_instance_uid = account_instance_uid
        self.account_title_uid = account_title_uid
        self.account_division_uid = account_division_uid
        self.account_group_uid = account_group_uid
        self.auth_identity_uid = auth_identity_uid
        self.account_email = account_email
        self.account_name = account_name
        self.display_name = display_name
        self.is_system = is_system
        self.row_guid = row_guid
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
        return cls(0, "", "", "", "", "", "", "", "", 0, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def default_read(cls):
        return cls(0, base_dto.get_random_uid(), "", "", "", "", "", "", "", 0, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def random_read(cls):
        return cls(0, base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), 0, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_default(cls, account_instance_uid: str , account_title_uid: str , account_division_uid: str , account_group_uid: str , auth_identity_uid: str , account_email: str , account_name: str , display_name: str , is_system: int ):
        return cls(0, account_instance_uid, account_title_uid, account_division_uid, account_group_uid, auth_identity_uid, account_email, account_name, display_name, is_system, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_full(cls, id: int , account_instance_uid: str , account_title_uid: str , account_division_uid: str , account_group_uid: str , auth_identity_uid: str , account_email: str , account_name: str , display_name: str , is_system: int , row_guid: str , row_version: int , is_active: int , created_date: datetime.datetime , created_by: str , last_updated_date: datetime.datetime , last_updated_by: str , removed_date: datetime.datetime  | None, removed_by: str  | None, custom_attributes: str ):
        return cls(id, account_instance_uid, account_title_uid, account_division_uid, account_group_uid, auth_identity_uid, account_email, account_name, display_name, is_system, row_guid, row_version, is_active, created_date, created_by, last_updated_date, last_updated_by, removed_date, removed_by, custom_attributes)
    @classmethod
    def from_write(cls, dto: account_instance_write_dto):
        return cls(0, dto.account_instance_uid, dto.account_title_uid, dto.account_division_uid, dto.account_group_uid, dto.auth_identity_uid, dto.account_email, dto.account_name, dto.display_name, dto.is_system, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, dto.custom_attributes)
    def clone_read(self):
        return account_instance_read_dto(self.id, self.account_instance_uid, self.account_title_uid, self.account_division_uid, self.account_group_uid, self.auth_identity_uid, self.account_email, self.account_name, self.display_name, self.is_system, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes)
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["id"], d["account_instance_uid"], d["account_title_uid"], d["account_division_uid"], d["account_group_uid"], d["auth_identity_uid"], d["account_email"], d["account_name"], d["display_name"], d["is_system"], d["row_guid"], d["row_version"], d["is_active"], d["created_date"], d["created_by"], d["last_updated_date"], d["last_updated_by"], d["removed_date"], d["removed_by"], d["custom_attributes"])
    def to_read_dict(self) -> dict:
        return asdict(self)
    def to_write(self) -> account_instance_write_dto:
        return account_instance_write_dto(self.account_instance_uid, self.account_title_uid, self.account_division_uid, self.account_group_uid, self.auth_identity_uid, self.account_email, self.account_name, self.display_name, self.is_system, self.custom_attributes)
    def to_thin(self) -> account_instance_thin_dto:
        return account_instance_thin_dto(self.account_instance_uid, self.row_guid, self.is_active)
    def touch(self, updated_by: str = "system"):
        self.last_updated_date = datetime.datetime.now()
        self.last_updated_by = updated_by
        self.row_version = self.row_version+1
    def get_list_all_values(self) -> list[any]:
        return [self.id, self.account_instance_uid, self.account_title_uid, self.account_division_uid, self.account_group_uid, self.auth_identity_uid, self.account_email, self.account_name, self.display_name, self.is_system, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]
    def get_list_update_values(self, updated_by: str) -> list[any]:
        return [self.account_title_uid, self.account_division_uid, self.account_group_uid, self.auth_identity_uid, self.account_email, self.account_name, self.display_name, self.is_system, self.custom_attributes, updated_by, self.account_instance_uid]
    def is_older_than(self, dt: datetime.datetime) -> bool:
        return self.created_date < dt
    def is_newer_than(self, dt: datetime.datetime) -> bool:
        return self.created_date > dt
    def to_json_read(self) -> str:
        return json.dumps(self.to_read_dict())


@dataclass(frozen=False)
class account_title_read_dto(base_read_dto, account_title_write_dto):
    id: int
    account_title_uid: str
    title_name: str
    title_description: str
    row_guid: str
    row_version: int
    is_active: int
    created_date: datetime.datetime
    created_by: str
    last_updated_date: datetime.datetime
    last_updated_by: str
    removed_date: datetime.datetime  | None
    removed_by: str  | None
    custom_attributes: str
    def __init__(self, id: int , account_title_uid: str , title_name: str , title_description: str , row_guid: str , row_version: int , is_active: int , created_date: datetime.datetime , created_by: str , last_updated_date: datetime.datetime , last_updated_by: str , removed_date: datetime.datetime  | None, removed_by: str  | None, custom_attributes: str ):
        self.id = id
        self.account_title_uid = account_title_uid
        self.title_name = title_name
        self.title_description = title_description
        self.row_guid = row_guid
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
    def new_read_default(cls, account_title_uid: str , title_name: str , title_description: str ):
        return cls(0, account_title_uid, title_name, title_description, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_full(cls, id: int , account_title_uid: str , title_name: str , title_description: str , row_guid: str , row_version: int , is_active: int , created_date: datetime.datetime , created_by: str , last_updated_date: datetime.datetime , last_updated_by: str , removed_date: datetime.datetime  | None, removed_by: str  | None, custom_attributes: str ):
        return cls(id, account_title_uid, title_name, title_description, row_guid, row_version, is_active, created_date, created_by, last_updated_date, last_updated_by, removed_date, removed_by, custom_attributes)
    @classmethod
    def from_write(cls, dto: account_title_write_dto):
        return cls(0, dto.account_title_uid, dto.title_name, dto.title_description, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, dto.custom_attributes)
    def clone_read(self):
        return account_title_read_dto(self.id, self.account_title_uid, self.title_name, self.title_description, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes)
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["id"], d["account_title_uid"], d["title_name"], d["title_description"], d["row_guid"], d["row_version"], d["is_active"], d["created_date"], d["created_by"], d["last_updated_date"], d["last_updated_by"], d["removed_date"], d["removed_by"], d["custom_attributes"])
    def to_read_dict(self) -> dict:
        return asdict(self)
    def to_write(self) -> account_title_write_dto:
        return account_title_write_dto(self.account_title_uid, self.title_name, self.title_description, self.custom_attributes)
    def to_thin(self) -> account_title_thin_dto:
        return account_title_thin_dto(self.account_title_uid, self.row_guid, self.is_active)
    def touch(self, updated_by: str = "system"):
        self.last_updated_date = datetime.datetime.now()
        self.last_updated_by = updated_by
        self.row_version = self.row_version+1
    def get_list_all_values(self) -> list[any]:
        return [self.id, self.account_title_uid, self.title_name, self.title_description, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]
    def get_list_update_values(self, updated_by: str) -> list[any]:
        return [self.title_name, self.title_description, self.custom_attributes, updated_by, self.account_title_uid]
    def is_older_than(self, dt: datetime.datetime) -> bool:
        return self.created_date < dt
    def is_newer_than(self, dt: datetime.datetime) -> bool:
        return self.created_date > dt
    def to_json_read(self) -> str:
        return json.dumps(self.to_read_dict())


@dataclass(frozen=False)
class auth_identity_read_dto(base_read_dto, auth_identity_write_dto):
    id: int
    auth_identity_uid: str
    identity_name: str
    identity_type: str
    identity_parameters: str
    last_status_name: str
    row_guid: str
    row_version: int
    is_active: int
    created_date: datetime.datetime
    created_by: str
    last_updated_date: datetime.datetime
    last_updated_by: str
    removed_date: datetime.datetime  | None
    removed_by: str  | None
    custom_attributes: str
    def __init__(self, id: int , auth_identity_uid: str , identity_name: str , identity_type: str , identity_parameters: str , last_status_name: str , row_guid: str , row_version: int , is_active: int , created_date: datetime.datetime , created_by: str , last_updated_date: datetime.datetime , last_updated_by: str , removed_date: datetime.datetime  | None, removed_by: str  | None, custom_attributes: str ):
        self.id = id
        self.auth_identity_uid = auth_identity_uid
        self.identity_name = identity_name
        self.identity_type = identity_type
        self.identity_parameters = identity_parameters
        self.last_status_name = last_status_name
        self.row_guid = row_guid
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
    def new_read_default(cls, auth_identity_uid: str , identity_name: str , identity_type: str , identity_parameters: str , last_status_name: str ):
        return cls(0, auth_identity_uid, identity_name, identity_type, identity_parameters, last_status_name, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_full(cls, id: int , auth_identity_uid: str , identity_name: str , identity_type: str , identity_parameters: str , last_status_name: str , row_guid: str , row_version: int , is_active: int , created_date: datetime.datetime , created_by: str , last_updated_date: datetime.datetime , last_updated_by: str , removed_date: datetime.datetime  | None, removed_by: str  | None, custom_attributes: str ):
        return cls(id, auth_identity_uid, identity_name, identity_type, identity_parameters, last_status_name, row_guid, row_version, is_active, created_date, created_by, last_updated_date, last_updated_by, removed_date, removed_by, custom_attributes)
    @classmethod
    def from_write(cls, dto: auth_identity_write_dto):
        return cls(0, dto.auth_identity_uid, dto.identity_name, dto.identity_type, dto.identity_parameters, dto.last_status_name, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, dto.custom_attributes)
    def clone_read(self):
        return auth_identity_read_dto(self.id, self.auth_identity_uid, self.identity_name, self.identity_type, self.identity_parameters, self.last_status_name, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes)
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["id"], d["auth_identity_uid"], d["identity_name"], d["identity_type"], d["identity_parameters"], d["last_status_name"], d["row_guid"], d["row_version"], d["is_active"], d["created_date"], d["created_by"], d["last_updated_date"], d["last_updated_by"], d["removed_date"], d["removed_by"], d["custom_attributes"])
    def to_read_dict(self) -> dict:
        return asdict(self)
    def to_write(self) -> auth_identity_write_dto:
        return auth_identity_write_dto(self.auth_identity_uid, self.identity_name, self.identity_type, self.identity_parameters, self.last_status_name, self.custom_attributes)
    def to_thin(self) -> auth_identity_thin_dto:
        return auth_identity_thin_dto(self.auth_identity_uid, self.row_guid, self.is_active)
    def touch(self, updated_by: str = "system"):
        self.last_updated_date = datetime.datetime.now()
        self.last_updated_by = updated_by
        self.row_version = self.row_version+1
    def get_list_all_values(self) -> list[any]:
        return [self.id, self.auth_identity_uid, self.identity_name, self.identity_type, self.identity_parameters, self.last_status_name, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]
    def get_list_update_values(self, updated_by: str) -> list[any]:
        return [self.identity_name, self.identity_type, self.identity_parameters, self.last_status_name, self.custom_attributes, updated_by, self.auth_identity_uid]
    def is_older_than(self, dt: datetime.datetime) -> bool:
        return self.created_date < dt
    def is_newer_than(self, dt: datetime.datetime) -> bool:
        return self.created_date > dt
    def to_json_read(self) -> str:
        return json.dumps(self.to_read_dict())


@dataclass(frozen=False)
class auth_password_read_dto(base_read_dto, auth_password_write_dto):
    id: int
    auth_password_uid: str
    account_instance_uid: str
    password_hash: str
    password_salt: str
    date_from: datetime.datetime
    date_to: datetime.datetime
    usage_count: int
    row_guid: str
    row_version: int
    is_active: int
    created_date: datetime.datetime
    created_by: str
    last_updated_date: datetime.datetime
    last_updated_by: str
    removed_date: datetime.datetime  | None
    removed_by: str  | None
    custom_attributes: str
    def __init__(self, id: int , auth_password_uid: str , account_instance_uid: str , password_hash: str , password_salt: str , date_from: datetime.datetime , date_to: datetime.datetime , usage_count: int , row_guid: str , row_version: int , is_active: int , created_date: datetime.datetime , created_by: str , last_updated_date: datetime.datetime , last_updated_by: str , removed_date: datetime.datetime  | None, removed_by: str  | None, custom_attributes: str ):
        self.id = id
        self.auth_password_uid = auth_password_uid
        self.account_instance_uid = account_instance_uid
        self.password_hash = password_hash
        self.password_salt = password_salt
        self.date_from = date_from
        self.date_to = date_to
        self.usage_count = usage_count
        self.row_guid = row_guid
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
        return cls(0, "", "", "", "", datetime.datetime.now(), datetime.datetime.now(), 0, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def default_read(cls):
        return cls(0, base_dto.get_random_uid(), "", "", "", datetime.datetime.now(), datetime.datetime.now(), 0, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def random_read(cls):
        return cls(0, base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), datetime.datetime.now(), datetime.datetime.now(), 0, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_default(cls, auth_password_uid: str , account_instance_uid: str , password_hash: str , password_salt: str , date_from: datetime.datetime , date_to: datetime.datetime , usage_count: int ):
        return cls(0, auth_password_uid, account_instance_uid, password_hash, password_salt, date_from, date_to, usage_count, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_full(cls, id: int , auth_password_uid: str , account_instance_uid: str , password_hash: str , password_salt: str , date_from: datetime.datetime , date_to: datetime.datetime , usage_count: int , row_guid: str , row_version: int , is_active: int , created_date: datetime.datetime , created_by: str , last_updated_date: datetime.datetime , last_updated_by: str , removed_date: datetime.datetime  | None, removed_by: str  | None, custom_attributes: str ):
        return cls(id, auth_password_uid, account_instance_uid, password_hash, password_salt, date_from, date_to, usage_count, row_guid, row_version, is_active, created_date, created_by, last_updated_date, last_updated_by, removed_date, removed_by, custom_attributes)
    @classmethod
    def from_write(cls, dto: auth_password_write_dto):
        return cls(0, dto.auth_password_uid, dto.account_instance_uid, dto.password_hash, dto.password_salt, dto.date_from, dto.date_to, dto.usage_count, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, dto.custom_attributes)
    def clone_read(self):
        return auth_password_read_dto(self.id, self.auth_password_uid, self.account_instance_uid, self.password_hash, self.password_salt, self.date_from, self.date_to, self.usage_count, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes)
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["id"], d["auth_password_uid"], d["account_instance_uid"], d["password_hash"], d["password_salt"], d["date_from"], d["date_to"], d["usage_count"], d["row_guid"], d["row_version"], d["is_active"], d["created_date"], d["created_by"], d["last_updated_date"], d["last_updated_by"], d["removed_date"], d["removed_by"], d["custom_attributes"])
    def to_read_dict(self) -> dict:
        return asdict(self)
    def to_write(self) -> auth_password_write_dto:
        return auth_password_write_dto(self.auth_password_uid, self.account_instance_uid, self.password_hash, self.password_salt, self.date_from, self.date_to, self.usage_count, self.custom_attributes)
    def to_thin(self) -> auth_password_thin_dto:
        return auth_password_thin_dto(self.auth_password_uid, self.row_guid, self.is_active)
    def touch(self, updated_by: str = "system"):
        self.last_updated_date = datetime.datetime.now()
        self.last_updated_by = updated_by
        self.row_version = self.row_version+1
    def get_list_all_values(self) -> list[any]:
        return [self.id, self.auth_password_uid, self.account_instance_uid, self.password_hash, self.password_salt, self.date_from, self.date_to, self.usage_count, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]
    def get_list_update_values(self, updated_by: str) -> list[any]:
        return [self.account_instance_uid, self.password_hash, self.password_salt, self.date_from, self.date_to, self.usage_count, self.custom_attributes, updated_by, self.auth_password_uid]
    def is_older_than(self, dt: datetime.datetime) -> bool:
        return self.created_date < dt
    def is_newer_than(self, dt: datetime.datetime) -> bool:
        return self.created_date > dt
    def to_json_read(self) -> str:
        return json.dumps(self.to_read_dict())


@dataclass(frozen=False)
class auth_permission_read_dto(base_read_dto, auth_permission_write_dto):
    id: int
    auth_permission_uid: str
    account_instance_uid: str
    auth_role_uid: str
    client_instance_uid: str  | None
    project_instance_uid: str  | None
    valid_from_date: datetime.datetime
    valid_till_date: datetime.datetime
    row_guid: str
    row_version: int
    is_active: int
    created_date: datetime.datetime
    created_by: str
    last_updated_date: datetime.datetime
    last_updated_by: str
    removed_date: datetime.datetime  | None
    removed_by: str  | None
    custom_attributes: str
    def __init__(self, id: int , auth_permission_uid: str , account_instance_uid: str , auth_role_uid: str , client_instance_uid: str  | None, project_instance_uid: str  | None, valid_from_date: datetime.datetime , valid_till_date: datetime.datetime , row_guid: str , row_version: int , is_active: int , created_date: datetime.datetime , created_by: str , last_updated_date: datetime.datetime , last_updated_by: str , removed_date: datetime.datetime  | None, removed_by: str  | None, custom_attributes: str ):
        self.id = id
        self.auth_permission_uid = auth_permission_uid
        self.account_instance_uid = account_instance_uid
        self.auth_role_uid = auth_role_uid
        self.client_instance_uid = client_instance_uid
        self.project_instance_uid = project_instance_uid
        self.valid_from_date = valid_from_date
        self.valid_till_date = valid_till_date
        self.row_guid = row_guid
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
        return cls(0, "", "", "", "", "", datetime.datetime.now(), datetime.datetime.now(), "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def default_read(cls):
        return cls(0, base_dto.get_random_uid(), "", "", "", "", datetime.datetime.now(), datetime.datetime.now(), "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def random_read(cls):
        return cls(0, base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), datetime.datetime.now(), datetime.datetime.now(), "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_default(cls, auth_permission_uid: str , account_instance_uid: str , auth_role_uid: str , client_instance_uid: str  | None, project_instance_uid: str  | None, valid_from_date: datetime.datetime , valid_till_date: datetime.datetime ):
        return cls(0, auth_permission_uid, account_instance_uid, auth_role_uid, client_instance_uid, project_instance_uid, valid_from_date, valid_till_date, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_full(cls, id: int , auth_permission_uid: str , account_instance_uid: str , auth_role_uid: str , client_instance_uid: str  | None, project_instance_uid: str  | None, valid_from_date: datetime.datetime , valid_till_date: datetime.datetime , row_guid: str , row_version: int , is_active: int , created_date: datetime.datetime , created_by: str , last_updated_date: datetime.datetime , last_updated_by: str , removed_date: datetime.datetime  | None, removed_by: str  | None, custom_attributes: str ):
        return cls(id, auth_permission_uid, account_instance_uid, auth_role_uid, client_instance_uid, project_instance_uid, valid_from_date, valid_till_date, row_guid, row_version, is_active, created_date, created_by, last_updated_date, last_updated_by, removed_date, removed_by, custom_attributes)
    @classmethod
    def from_write(cls, dto: auth_permission_write_dto):
        return cls(0, dto.auth_permission_uid, dto.account_instance_uid, dto.auth_role_uid, dto.client_instance_uid, dto.project_instance_uid, dto.valid_from_date, dto.valid_till_date, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, dto.custom_attributes)
    def clone_read(self):
        return auth_permission_read_dto(self.id, self.auth_permission_uid, self.account_instance_uid, self.auth_role_uid, self.client_instance_uid, self.project_instance_uid, self.valid_from_date, self.valid_till_date, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes)
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["id"], d["auth_permission_uid"], d["account_instance_uid"], d["auth_role_uid"], d["client_instance_uid"], d["project_instance_uid"], d["valid_from_date"], d["valid_till_date"], d["row_guid"], d["row_version"], d["is_active"], d["created_date"], d["created_by"], d["last_updated_date"], d["last_updated_by"], d["removed_date"], d["removed_by"], d["custom_attributes"])
    def to_read_dict(self) -> dict:
        return asdict(self)
    def to_write(self) -> auth_permission_write_dto:
        return auth_permission_write_dto(self.auth_permission_uid, self.account_instance_uid, self.auth_role_uid, self.client_instance_uid, self.project_instance_uid, self.valid_from_date, self.valid_till_date, self.custom_attributes)
    def to_thin(self) -> auth_permission_thin_dto:
        return auth_permission_thin_dto(self.auth_permission_uid, self.row_guid, self.is_active)
    def touch(self, updated_by: str = "system"):
        self.last_updated_date = datetime.datetime.now()
        self.last_updated_by = updated_by
        self.row_version = self.row_version+1
    def get_list_all_values(self) -> list[any]:
        return [self.id, self.auth_permission_uid, self.account_instance_uid, self.auth_role_uid, self.client_instance_uid, self.project_instance_uid, self.valid_from_date, self.valid_till_date, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]
    def get_list_update_values(self, updated_by: str) -> list[any]:
        return [self.account_instance_uid, self.auth_role_uid, self.client_instance_uid, self.project_instance_uid, self.valid_from_date, self.valid_till_date, self.custom_attributes, updated_by, self.auth_permission_uid]
    def is_older_than(self, dt: datetime.datetime) -> bool:
        return self.created_date < dt
    def is_newer_than(self, dt: datetime.datetime) -> bool:
        return self.created_date > dt
    def to_json_read(self) -> str:
        return json.dumps(self.to_read_dict())


@dataclass(frozen=False)
class auth_request_read_dto(base_read_dto, auth_request_write_dto):
    id: int
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
    row_guid: str
    row_version: int
    is_active: int
    created_date: datetime.datetime
    created_by: str
    last_updated_date: datetime.datetime
    last_updated_by: str
    removed_date: datetime.datetime  | None
    removed_by: str  | None
    custom_attributes: str
    def __init__(self, id: int , auth_request_uid: str , by_account_instance_uid: str , account_instance_uid: str , reset_guid: str , valid_till_date: datetime.datetime , lock_guid: str  | None, lock_by: str  | None, lock_date: datetime.datetime  | None, is_checked: int , is_used: int , check_date: datetime.datetime  | None, use_date: datetime.datetime  | None, row_guid: str , row_version: int , is_active: int , created_date: datetime.datetime , created_by: str , last_updated_date: datetime.datetime , last_updated_by: str , removed_date: datetime.datetime  | None, removed_by: str  | None, custom_attributes: str ):
        self.id = id
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
        self.row_guid = row_guid
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
        return cls(0, "", "", "", "", datetime.datetime.now(), "", "", datetime.datetime.now(), 0, 0, datetime.datetime.now(), datetime.datetime.now(), "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def default_read(cls):
        return cls(0, base_dto.get_random_uid(), "", "", "", datetime.datetime.now(), "", "", datetime.datetime.now(), 0, 0, datetime.datetime.now(), datetime.datetime.now(), "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def random_read(cls):
        return cls(0, base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), datetime.datetime.now(), base_dto.get_random_uid(), base_dto.get_random_uid(), datetime.datetime.now(), 0, 0, datetime.datetime.now(), datetime.datetime.now(), "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_default(cls, auth_request_uid: str , by_account_instance_uid: str , account_instance_uid: str , reset_guid: str , valid_till_date: datetime.datetime , lock_guid: str  | None, lock_by: str  | None, lock_date: datetime.datetime  | None, is_checked: int , is_used: int , check_date: datetime.datetime  | None, use_date: datetime.datetime  | None):
        return cls(0, auth_request_uid, by_account_instance_uid, account_instance_uid, reset_guid, valid_till_date, lock_guid, lock_by, lock_date, is_checked, is_used, check_date, use_date, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_full(cls, id: int , auth_request_uid: str , by_account_instance_uid: str , account_instance_uid: str , reset_guid: str , valid_till_date: datetime.datetime , lock_guid: str  | None, lock_by: str  | None, lock_date: datetime.datetime  | None, is_checked: int , is_used: int , check_date: datetime.datetime  | None, use_date: datetime.datetime  | None, row_guid: str , row_version: int , is_active: int , created_date: datetime.datetime , created_by: str , last_updated_date: datetime.datetime , last_updated_by: str , removed_date: datetime.datetime  | None, removed_by: str  | None, custom_attributes: str ):
        return cls(id, auth_request_uid, by_account_instance_uid, account_instance_uid, reset_guid, valid_till_date, lock_guid, lock_by, lock_date, is_checked, is_used, check_date, use_date, row_guid, row_version, is_active, created_date, created_by, last_updated_date, last_updated_by, removed_date, removed_by, custom_attributes)
    @classmethod
    def from_write(cls, dto: auth_request_write_dto):
        return cls(0, dto.auth_request_uid, dto.by_account_instance_uid, dto.account_instance_uid, dto.reset_guid, dto.valid_till_date, dto.lock_guid, dto.lock_by, dto.lock_date, dto.is_checked, dto.is_used, dto.check_date, dto.use_date, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, dto.custom_attributes)
    def clone_read(self):
        return auth_request_read_dto(self.id, self.auth_request_uid, self.by_account_instance_uid, self.account_instance_uid, self.reset_guid, self.valid_till_date, self.lock_guid, self.lock_by, self.lock_date, self.is_checked, self.is_used, self.check_date, self.use_date, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes)
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["id"], d["auth_request_uid"], d["by_account_instance_uid"], d["account_instance_uid"], d["reset_guid"], d["valid_till_date"], d["lock_guid"], d["lock_by"], d["lock_date"], d["is_checked"], d["is_used"], d["check_date"], d["use_date"], d["row_guid"], d["row_version"], d["is_active"], d["created_date"], d["created_by"], d["last_updated_date"], d["last_updated_by"], d["removed_date"], d["removed_by"], d["custom_attributes"])
    def to_read_dict(self) -> dict:
        return asdict(self)
    def to_write(self) -> auth_request_write_dto:
        return auth_request_write_dto(self.auth_request_uid, self.by_account_instance_uid, self.account_instance_uid, self.reset_guid, self.valid_till_date, self.lock_guid, self.lock_by, self.lock_date, self.is_checked, self.is_used, self.check_date, self.use_date, self.custom_attributes)
    def to_thin(self) -> auth_request_thin_dto:
        return auth_request_thin_dto(self.auth_request_uid, self.row_guid, self.is_active)
    def touch(self, updated_by: str = "system"):
        self.last_updated_date = datetime.datetime.now()
        self.last_updated_by = updated_by
        self.row_version = self.row_version+1
    def get_list_all_values(self) -> list[any]:
        return [self.id, self.auth_request_uid, self.by_account_instance_uid, self.account_instance_uid, self.reset_guid, self.valid_till_date, self.lock_guid, self.lock_by, self.lock_date, self.is_checked, self.is_used, self.check_date, self.use_date, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]
    def get_list_update_values(self, updated_by: str) -> list[any]:
        return [self.by_account_instance_uid, self.account_instance_uid, self.reset_guid, self.valid_till_date, self.lock_guid, self.lock_by, self.lock_date, self.is_checked, self.is_used, self.check_date, self.use_date, self.custom_attributes, updated_by, self.auth_request_uid]
    def is_older_than(self, dt: datetime.datetime) -> bool:
        return self.created_date < dt
    def is_newer_than(self, dt: datetime.datetime) -> bool:
        return self.created_date > dt
    def to_json_read(self) -> str:
        return json.dumps(self.to_read_dict())


@dataclass(frozen=False)
class auth_role_read_dto(base_read_dto, auth_role_write_dto):
    id: int
    auth_role_uid: str
    parent_auth_role_uid: str  | None
    role_name: str
    role_description: str
    access_uris: str
    is_project: int
    is_client: int
    is_custom: int
    row_guid: str
    row_version: int
    is_active: int
    created_date: datetime.datetime
    created_by: str
    last_updated_date: datetime.datetime
    last_updated_by: str
    removed_date: datetime.datetime  | None
    removed_by: str  | None
    custom_attributes: str
    def __init__(self, id: int , auth_role_uid: str , parent_auth_role_uid: str  | None, role_name: str , role_description: str , access_uris: str , is_project: int , is_client: int , is_custom: int , row_guid: str , row_version: int , is_active: int , created_date: datetime.datetime , created_by: str , last_updated_date: datetime.datetime , last_updated_by: str , removed_date: datetime.datetime  | None, removed_by: str  | None, custom_attributes: str ):
        self.id = id
        self.auth_role_uid = auth_role_uid
        self.parent_auth_role_uid = parent_auth_role_uid
        self.role_name = role_name
        self.role_description = role_description
        self.access_uris = access_uris
        self.is_project = is_project
        self.is_client = is_client
        self.is_custom = is_custom
        self.row_guid = row_guid
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
        return cls(0, "", "", "", "", "", 0, 0, 0, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def default_read(cls):
        return cls(0, base_dto.get_random_uid(), "", "", "", "", 0, 0, 0, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def random_read(cls):
        return cls(0, base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), 0, 0, 0, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_default(cls, auth_role_uid: str , parent_auth_role_uid: str  | None, role_name: str , role_description: str , access_uris: str , is_project: int , is_client: int , is_custom: int ):
        return cls(0, auth_role_uid, parent_auth_role_uid, role_name, role_description, access_uris, is_project, is_client, is_custom, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_full(cls, id: int , auth_role_uid: str , parent_auth_role_uid: str  | None, role_name: str , role_description: str , access_uris: str , is_project: int , is_client: int , is_custom: int , row_guid: str , row_version: int , is_active: int , created_date: datetime.datetime , created_by: str , last_updated_date: datetime.datetime , last_updated_by: str , removed_date: datetime.datetime  | None, removed_by: str  | None, custom_attributes: str ):
        return cls(id, auth_role_uid, parent_auth_role_uid, role_name, role_description, access_uris, is_project, is_client, is_custom, row_guid, row_version, is_active, created_date, created_by, last_updated_date, last_updated_by, removed_date, removed_by, custom_attributes)
    @classmethod
    def from_write(cls, dto: auth_role_write_dto):
        return cls(0, dto.auth_role_uid, dto.parent_auth_role_uid, dto.role_name, dto.role_description, dto.access_uris, dto.is_project, dto.is_client, dto.is_custom, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, dto.custom_attributes)
    def clone_read(self):
        return auth_role_read_dto(self.id, self.auth_role_uid, self.parent_auth_role_uid, self.role_name, self.role_description, self.access_uris, self.is_project, self.is_client, self.is_custom, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes)
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["id"], d["auth_role_uid"], d["parent_auth_role_uid"], d["role_name"], d["role_description"], d["access_uris"], d["is_project"], d["is_client"], d["is_custom"], d["row_guid"], d["row_version"], d["is_active"], d["created_date"], d["created_by"], d["last_updated_date"], d["last_updated_by"], d["removed_date"], d["removed_by"], d["custom_attributes"])
    def to_read_dict(self) -> dict:
        return asdict(self)
    def to_write(self) -> auth_role_write_dto:
        return auth_role_write_dto(self.auth_role_uid, self.parent_auth_role_uid, self.role_name, self.role_description, self.access_uris, self.is_project, self.is_client, self.is_custom, self.custom_attributes)
    def to_thin(self) -> auth_role_thin_dto:
        return auth_role_thin_dto(self.auth_role_uid, self.row_guid, self.is_active)
    def touch(self, updated_by: str = "system"):
        self.last_updated_date = datetime.datetime.now()
        self.last_updated_by = updated_by
        self.row_version = self.row_version+1
    def get_list_all_values(self) -> list[any]:
        return [self.id, self.auth_role_uid, self.parent_auth_role_uid, self.role_name, self.role_description, self.access_uris, self.is_project, self.is_client, self.is_custom, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]
    def get_list_update_values(self, updated_by: str) -> list[any]:
        return [self.parent_auth_role_uid, self.role_name, self.role_description, self.access_uris, self.is_project, self.is_client, self.is_custom, self.custom_attributes, updated_by, self.auth_role_uid]
    def is_older_than(self, dt: datetime.datetime) -> bool:
        return self.created_date < dt
    def is_newer_than(self, dt: datetime.datetime) -> bool:
        return self.created_date > dt
    def to_json_read(self) -> str:
        return json.dumps(self.to_read_dict())


@dataclass(frozen=False)
class auth_token_read_dto(base_read_dto, auth_token_write_dto):
    id: int
    auth_token_uid: str
    account_instance_uid: str
    token_seq: int
    token_hash: str
    token_salt: str
    valid_till_date: datetime.datetime  | None
    last_use_date: datetime.datetime  | None
    is_last: int
    row_guid: str
    row_version: int
    is_active: int
    created_date: datetime.datetime
    created_by: str
    last_updated_date: datetime.datetime
    last_updated_by: str
    removed_date: datetime.datetime  | None
    removed_by: str  | None
    custom_attributes: str
    def __init__(self, id: int , auth_token_uid: str , account_instance_uid: str , token_seq: int , token_hash: str , token_salt: str , valid_till_date: datetime.datetime  | None, last_use_date: datetime.datetime  | None, is_last: int , row_guid: str , row_version: int , is_active: int , created_date: datetime.datetime , created_by: str , last_updated_date: datetime.datetime , last_updated_by: str , removed_date: datetime.datetime  | None, removed_by: str  | None, custom_attributes: str ):
        self.id = id
        self.auth_token_uid = auth_token_uid
        self.account_instance_uid = account_instance_uid
        self.token_seq = token_seq
        self.token_hash = token_hash
        self.token_salt = token_salt
        self.valid_till_date = valid_till_date
        self.last_use_date = last_use_date
        self.is_last = is_last
        self.row_guid = row_guid
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
        return cls(0, "", "", 0, "", "", datetime.datetime.now(), datetime.datetime.now(), 0, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def default_read(cls):
        return cls(0, base_dto.get_random_uid(), "", 0, "", "", datetime.datetime.now(), datetime.datetime.now(), 0, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def random_read(cls):
        return cls(0, base_dto.get_random_uid(), base_dto.get_random_uid(), 0, base_dto.get_random_uid(), base_dto.get_random_uid(), datetime.datetime.now(), datetime.datetime.now(), 0, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_default(cls, auth_token_uid: str , account_instance_uid: str , token_seq: int , token_hash: str , token_salt: str , valid_till_date: datetime.datetime  | None, last_use_date: datetime.datetime  | None, is_last: int ):
        return cls(0, auth_token_uid, account_instance_uid, token_seq, token_hash, token_salt, valid_till_date, last_use_date, is_last, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_full(cls, id: int , auth_token_uid: str , account_instance_uid: str , token_seq: int , token_hash: str , token_salt: str , valid_till_date: datetime.datetime  | None, last_use_date: datetime.datetime  | None, is_last: int , row_guid: str , row_version: int , is_active: int , created_date: datetime.datetime , created_by: str , last_updated_date: datetime.datetime , last_updated_by: str , removed_date: datetime.datetime  | None, removed_by: str  | None, custom_attributes: str ):
        return cls(id, auth_token_uid, account_instance_uid, token_seq, token_hash, token_salt, valid_till_date, last_use_date, is_last, row_guid, row_version, is_active, created_date, created_by, last_updated_date, last_updated_by, removed_date, removed_by, custom_attributes)
    @classmethod
    def from_write(cls, dto: auth_token_write_dto):
        return cls(0, dto.auth_token_uid, dto.account_instance_uid, dto.token_seq, dto.token_hash, dto.token_salt, dto.valid_till_date, dto.last_use_date, dto.is_last, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, dto.custom_attributes)
    def clone_read(self):
        return auth_token_read_dto(self.id, self.auth_token_uid, self.account_instance_uid, self.token_seq, self.token_hash, self.token_salt, self.valid_till_date, self.last_use_date, self.is_last, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes)
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["id"], d["auth_token_uid"], d["account_instance_uid"], d["token_seq"], d["token_hash"], d["token_salt"], d["valid_till_date"], d["last_use_date"], d["is_last"], d["row_guid"], d["row_version"], d["is_active"], d["created_date"], d["created_by"], d["last_updated_date"], d["last_updated_by"], d["removed_date"], d["removed_by"], d["custom_attributes"])
    def to_read_dict(self) -> dict:
        return asdict(self)
    def to_write(self) -> auth_token_write_dto:
        return auth_token_write_dto(self.auth_token_uid, self.account_instance_uid, self.token_seq, self.token_hash, self.token_salt, self.valid_till_date, self.last_use_date, self.is_last, self.custom_attributes)
    def to_thin(self) -> auth_token_thin_dto:
        return auth_token_thin_dto(self.auth_token_uid, self.row_guid, self.is_active)
    def touch(self, updated_by: str = "system"):
        self.last_updated_date = datetime.datetime.now()
        self.last_updated_by = updated_by
        self.row_version = self.row_version+1
    def get_list_all_values(self) -> list[any]:
        return [self.id, self.auth_token_uid, self.account_instance_uid, self.token_seq, self.token_hash, self.token_salt, self.valid_till_date, self.last_use_date, self.is_last, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]
    def get_list_update_values(self, updated_by: str) -> list[any]:
        return [self.account_instance_uid, self.token_seq, self.token_hash, self.token_salt, self.valid_till_date, self.last_use_date, self.is_last, self.custom_attributes, updated_by, self.auth_token_uid]
    def is_older_than(self, dt: datetime.datetime) -> bool:
        return self.created_date < dt
    def is_newer_than(self, dt: datetime.datetime) -> bool:
        return self.created_date > dt
    def to_json_read(self) -> str:
        return json.dumps(self.to_read_dict())


@dataclass(frozen=False)
class client_instance_read_dto(base_read_dto, client_instance_write_dto):
    id: int
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
    row_guid: str
    row_version: int
    is_active: int
    created_date: datetime.datetime
    created_by: str
    last_updated_date: datetime.datetime
    last_updated_by: str
    removed_date: datetime.datetime  | None
    removed_by: str  | None
    custom_attributes: str
    def __init__(self, id: int , client_instance_uid: str , country_uid: str , client_name: str , client_code: str , client_description: str , start_date: datetime.datetime , end_date: datetime.datetime  | None, is_internal: int , is_system: int , is_test: int , row_guid: str , row_version: int , is_active: int , created_date: datetime.datetime , created_by: str , last_updated_date: datetime.datetime , last_updated_by: str , removed_date: datetime.datetime  | None, removed_by: str  | None, custom_attributes: str ):
        self.id = id
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
        self.row_guid = row_guid
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
        return cls(0, "", "", "", "", "", datetime.datetime.now(), datetime.datetime.now(), 0, 0, 0, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def default_read(cls):
        return cls(0, base_dto.get_random_uid(), "", "", "", "", datetime.datetime.now(), datetime.datetime.now(), 0, 0, 0, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def random_read(cls):
        return cls(0, base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), datetime.datetime.now(), datetime.datetime.now(), 0, 0, 0, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_default(cls, client_instance_uid: str , country_uid: str , client_name: str , client_code: str , client_description: str , start_date: datetime.datetime , end_date: datetime.datetime  | None, is_internal: int , is_system: int , is_test: int ):
        return cls(0, client_instance_uid, country_uid, client_name, client_code, client_description, start_date, end_date, is_internal, is_system, is_test, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_full(cls, id: int , client_instance_uid: str , country_uid: str , client_name: str , client_code: str , client_description: str , start_date: datetime.datetime , end_date: datetime.datetime  | None, is_internal: int , is_system: int , is_test: int , row_guid: str , row_version: int , is_active: int , created_date: datetime.datetime , created_by: str , last_updated_date: datetime.datetime , last_updated_by: str , removed_date: datetime.datetime  | None, removed_by: str  | None, custom_attributes: str ):
        return cls(id, client_instance_uid, country_uid, client_name, client_code, client_description, start_date, end_date, is_internal, is_system, is_test, row_guid, row_version, is_active, created_date, created_by, last_updated_date, last_updated_by, removed_date, removed_by, custom_attributes)
    @classmethod
    def from_write(cls, dto: client_instance_write_dto):
        return cls(0, dto.client_instance_uid, dto.country_uid, dto.client_name, dto.client_code, dto.client_description, dto.start_date, dto.end_date, dto.is_internal, dto.is_system, dto.is_test, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, dto.custom_attributes)
    def clone_read(self):
        return client_instance_read_dto(self.id, self.client_instance_uid, self.country_uid, self.client_name, self.client_code, self.client_description, self.start_date, self.end_date, self.is_internal, self.is_system, self.is_test, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes)
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["id"], d["client_instance_uid"], d["country_uid"], d["client_name"], d["client_code"], d["client_description"], d["start_date"], d["end_date"], d["is_internal"], d["is_system"], d["is_test"], d["row_guid"], d["row_version"], d["is_active"], d["created_date"], d["created_by"], d["last_updated_date"], d["last_updated_by"], d["removed_date"], d["removed_by"], d["custom_attributes"])
    def to_read_dict(self) -> dict:
        return asdict(self)
    def to_write(self) -> client_instance_write_dto:
        return client_instance_write_dto(self.client_instance_uid, self.country_uid, self.client_name, self.client_code, self.client_description, self.start_date, self.end_date, self.is_internal, self.is_system, self.is_test, self.custom_attributes)
    def to_thin(self) -> client_instance_thin_dto:
        return client_instance_thin_dto(self.client_instance_uid, self.row_guid, self.is_active)
    def touch(self, updated_by: str = "system"):
        self.last_updated_date = datetime.datetime.now()
        self.last_updated_by = updated_by
        self.row_version = self.row_version+1
    def get_list_all_values(self) -> list[any]:
        return [self.id, self.client_instance_uid, self.country_uid, self.client_name, self.client_code, self.client_description, self.start_date, self.end_date, self.is_internal, self.is_system, self.is_test, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]
    def get_list_update_values(self, updated_by: str) -> list[any]:
        return [self.country_uid, self.client_name, self.client_code, self.client_description, self.start_date, self.end_date, self.is_internal, self.is_system, self.is_test, self.custom_attributes, updated_by, self.client_instance_uid]
    def is_older_than(self, dt: datetime.datetime) -> bool:
        return self.created_date < dt
    def is_newer_than(self, dt: datetime.datetime) -> bool:
        return self.created_date > dt
    def to_json_read(self) -> str:
        return json.dumps(self.to_read_dict())


@dataclass(frozen=False)
class country_read_dto(base_read_dto, country_write_dto):
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
    row_version: int
    is_active: int
    created_date: datetime.datetime
    created_by: str
    last_updated_date: datetime.datetime
    last_updated_by: str
    removed_date: datetime.datetime  | None
    removed_by: str  | None
    custom_attributes: str
    def __init__(self, id: int , country_uid: str , continent_name: str , continent_code: str , country_name: str , country_iso3: str , country_code: str , phone_code: str , currency_code: str , capital_name: str , region_name: str , subregion_name: str , region_code: str , latitude: str , longitude: str , currency_name: str , population: str , languages: str , area: str , bar_code: str , top_level_domain: str , is_focused: int , row_guid: str , row_version: int , is_active: int , created_date: datetime.datetime , created_by: str , last_updated_date: datetime.datetime , last_updated_by: str , removed_date: datetime.datetime  | None, removed_by: str  | None, custom_attributes: str ):
        self.id = id
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
        self.row_guid = row_guid
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
    def new_read_default(cls, country_uid: str , continent_name: str , continent_code: str , country_name: str , country_iso3: str , country_code: str , phone_code: str , currency_code: str , capital_name: str , region_name: str , subregion_name: str , region_code: str , latitude: str , longitude: str , currency_name: str , population: str , languages: str , area: str , bar_code: str , top_level_domain: str , is_focused: int ):
        return cls(0, country_uid, continent_name, continent_code, country_name, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain, is_focused, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_full(cls, id: int , country_uid: str , continent_name: str , continent_code: str , country_name: str , country_iso3: str , country_code: str , phone_code: str , currency_code: str , capital_name: str , region_name: str , subregion_name: str , region_code: str , latitude: str , longitude: str , currency_name: str , population: str , languages: str , area: str , bar_code: str , top_level_domain: str , is_focused: int , row_guid: str , row_version: int , is_active: int , created_date: datetime.datetime , created_by: str , last_updated_date: datetime.datetime , last_updated_by: str , removed_date: datetime.datetime  | None, removed_by: str  | None, custom_attributes: str ):
        return cls(id, country_uid, continent_name, continent_code, country_name, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain, is_focused, row_guid, row_version, is_active, created_date, created_by, last_updated_date, last_updated_by, removed_date, removed_by, custom_attributes)
    @classmethod
    def from_write(cls, dto: country_write_dto):
        return cls(0, dto.country_uid, dto.continent_name, dto.continent_code, dto.country_name, dto.country_iso3, dto.country_code, dto.phone_code, dto.currency_code, dto.capital_name, dto.region_name, dto.subregion_name, dto.region_code, dto.latitude, dto.longitude, dto.currency_name, dto.population, dto.languages, dto.area, dto.bar_code, dto.top_level_domain, dto.is_focused, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, dto.custom_attributes)
    def clone_read(self):
        return country_read_dto(self.id, self.country_uid, self.continent_name, self.continent_code, self.country_name, self.country_iso3, self.country_code, self.phone_code, self.currency_code, self.capital_name, self.region_name, self.subregion_name, self.region_code, self.latitude, self.longitude, self.currency_name, self.population, self.languages, self.area, self.bar_code, self.top_level_domain, self.is_focused, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes)
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["id"], d["country_uid"], d["continent_name"], d["continent_code"], d["country_name"], d["country_iso3"], d["country_code"], d["phone_code"], d["currency_code"], d["capital_name"], d["region_name"], d["subregion_name"], d["region_code"], d["latitude"], d["longitude"], d["currency_name"], d["population"], d["languages"], d["area"], d["bar_code"], d["top_level_domain"], d["is_focused"], d["row_guid"], d["row_version"], d["is_active"], d["created_date"], d["created_by"], d["last_updated_date"], d["last_updated_by"], d["removed_date"], d["removed_by"], d["custom_attributes"])
    def to_read_dict(self) -> dict:
        return asdict(self)
    def to_write(self) -> country_write_dto:
        return country_write_dto(self.country_uid, self.continent_name, self.continent_code, self.country_name, self.country_iso3, self.country_code, self.phone_code, self.currency_code, self.capital_name, self.region_name, self.subregion_name, self.region_code, self.latitude, self.longitude, self.currency_name, self.population, self.languages, self.area, self.bar_code, self.top_level_domain, self.is_focused, self.custom_attributes)
    def to_thin(self) -> country_thin_dto:
        return country_thin_dto(self.country_uid, self.row_guid, self.is_active)
    def touch(self, updated_by: str = "system"):
        self.last_updated_date = datetime.datetime.now()
        self.last_updated_by = updated_by
        self.row_version = self.row_version+1
    def get_list_all_values(self) -> list[any]:
        return [self.id, self.country_uid, self.continent_name, self.continent_code, self.country_name, self.country_iso3, self.country_code, self.phone_code, self.currency_code, self.capital_name, self.region_name, self.subregion_name, self.region_code, self.latitude, self.longitude, self.currency_name, self.population, self.languages, self.area, self.bar_code, self.top_level_domain, self.is_focused, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]
    def get_list_update_values(self, updated_by: str) -> list[any]:
        return [self.continent_name, self.continent_code, self.country_name, self.country_iso3, self.country_code, self.phone_code, self.currency_code, self.capital_name, self.region_name, self.subregion_name, self.region_code, self.latitude, self.longitude, self.currency_name, self.population, self.languages, self.area, self.bar_code, self.top_level_domain, self.is_focused, self.custom_attributes, updated_by, self.country_uid]
    def is_older_than(self, dt: datetime.datetime) -> bool:
        return self.created_date < dt
    def is_newer_than(self, dt: datetime.datetime) -> bool:
        return self.created_date > dt
    def to_json_read(self) -> str:
        return json.dumps(self.to_read_dict())


@dataclass(frozen=False)
class currency_read_dto(base_read_dto, currency_write_dto):
    id: int
    currency_uid: str
    currency_name: str
    is_focused: int
    row_guid: str
    row_version: int
    is_active: int
    created_date: datetime.datetime
    created_by: str
    last_updated_date: datetime.datetime
    last_updated_by: str
    removed_date: datetime.datetime  | None
    removed_by: str  | None
    custom_attributes: str
    def __init__(self, id: int , currency_uid: str , currency_name: str , is_focused: int , row_guid: str , row_version: int , is_active: int , created_date: datetime.datetime , created_by: str , last_updated_date: datetime.datetime , last_updated_by: str , removed_date: datetime.datetime  | None, removed_by: str  | None, custom_attributes: str ):
        self.id = id
        self.currency_uid = currency_uid
        self.currency_name = currency_name
        self.is_focused = is_focused
        self.row_guid = row_guid
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
        return cls(0, "", "", 0, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def default_read(cls):
        return cls(0, base_dto.get_random_uid(), "", 0, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def random_read(cls):
        return cls(0, base_dto.get_random_uid(), base_dto.get_random_uid(), 0, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_default(cls, currency_uid: str , currency_name: str , is_focused: int ):
        return cls(0, currency_uid, currency_name, is_focused, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_full(cls, id: int , currency_uid: str , currency_name: str , is_focused: int , row_guid: str , row_version: int , is_active: int , created_date: datetime.datetime , created_by: str , last_updated_date: datetime.datetime , last_updated_by: str , removed_date: datetime.datetime  | None, removed_by: str  | None, custom_attributes: str ):
        return cls(id, currency_uid, currency_name, is_focused, row_guid, row_version, is_active, created_date, created_by, last_updated_date, last_updated_by, removed_date, removed_by, custom_attributes)
    @classmethod
    def from_write(cls, dto: currency_write_dto):
        return cls(0, dto.currency_uid, dto.currency_name, dto.is_focused, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, dto.custom_attributes)
    def clone_read(self):
        return currency_read_dto(self.id, self.currency_uid, self.currency_name, self.is_focused, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes)
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["id"], d["currency_uid"], d["currency_name"], d["is_focused"], d["row_guid"], d["row_version"], d["is_active"], d["created_date"], d["created_by"], d["last_updated_date"], d["last_updated_by"], d["removed_date"], d["removed_by"], d["custom_attributes"])
    def to_read_dict(self) -> dict:
        return asdict(self)
    def to_write(self) -> currency_write_dto:
        return currency_write_dto(self.currency_uid, self.currency_name, self.is_focused, self.custom_attributes)
    def to_thin(self) -> currency_thin_dto:
        return currency_thin_dto(self.currency_uid, self.row_guid, self.is_active)
    def touch(self, updated_by: str = "system"):
        self.last_updated_date = datetime.datetime.now()
        self.last_updated_by = updated_by
        self.row_version = self.row_version+1
    def get_list_all_values(self) -> list[any]:
        return [self.id, self.currency_uid, self.currency_name, self.is_focused, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]
    def get_list_update_values(self, updated_by: str) -> list[any]:
        return [self.currency_name, self.is_focused, self.custom_attributes, updated_by, self.currency_uid]
    def is_older_than(self, dt: datetime.datetime) -> bool:
        return self.created_date < dt
    def is_newer_than(self, dt: datetime.datetime) -> bool:
        return self.created_date > dt
    def to_json_read(self) -> str:
        return json.dumps(self.to_read_dict())


@dataclass(frozen=False)
class entry_final_read_dto(base_read_dto, entry_final_write_dto):
    id: int
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
    row_guid: str
    row_version: int
    is_active: int
    created_date: datetime.datetime
    created_by: str
    last_updated_date: datetime.datetime
    last_updated_by: str
    removed_date: datetime.datetime  | None
    removed_by: str  | None
    custom_attributes: str
    def __init__(self, id: int , entry_final_uid: str , account_instance_uid: str , project_instance_uid: str , project_milestone_uid: str , invoice_instance_uid: str  | None, entry_period: str , entry_note: str , lock_uid: str  | None, start_date: datetime.datetime  | None, end_date: datetime.datetime  | None, entry_minutes: int , is_approved: int , row_guid: str , row_version: int , is_active: int , created_date: datetime.datetime , created_by: str , last_updated_date: datetime.datetime , last_updated_by: str , removed_date: datetime.datetime  | None, removed_by: str  | None, custom_attributes: str ):
        self.id = id
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
        self.row_guid = row_guid
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
        return cls(0, "", "", "", "", "", "", "", "", datetime.datetime.now(), datetime.datetime.now(), 0, 0, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def default_read(cls):
        return cls(0, base_dto.get_random_uid(), "", "", "", "", "", "", "", datetime.datetime.now(), datetime.datetime.now(), 0, 0, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def random_read(cls):
        return cls(0, base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), datetime.datetime.now(), datetime.datetime.now(), 0, 0, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_default(cls, entry_final_uid: str , account_instance_uid: str , project_instance_uid: str , project_milestone_uid: str , invoice_instance_uid: str  | None, entry_period: str , entry_note: str , lock_uid: str  | None, start_date: datetime.datetime  | None, end_date: datetime.datetime  | None, entry_minutes: int , is_approved: int ):
        return cls(0, entry_final_uid, account_instance_uid, project_instance_uid, project_milestone_uid, invoice_instance_uid, entry_period, entry_note, lock_uid, start_date, end_date, entry_minutes, is_approved, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_full(cls, id: int , entry_final_uid: str , account_instance_uid: str , project_instance_uid: str , project_milestone_uid: str , invoice_instance_uid: str  | None, entry_period: str , entry_note: str , lock_uid: str  | None, start_date: datetime.datetime  | None, end_date: datetime.datetime  | None, entry_minutes: int , is_approved: int , row_guid: str , row_version: int , is_active: int , created_date: datetime.datetime , created_by: str , last_updated_date: datetime.datetime , last_updated_by: str , removed_date: datetime.datetime  | None, removed_by: str  | None, custom_attributes: str ):
        return cls(id, entry_final_uid, account_instance_uid, project_instance_uid, project_milestone_uid, invoice_instance_uid, entry_period, entry_note, lock_uid, start_date, end_date, entry_minutes, is_approved, row_guid, row_version, is_active, created_date, created_by, last_updated_date, last_updated_by, removed_date, removed_by, custom_attributes)
    @classmethod
    def from_write(cls, dto: entry_final_write_dto):
        return cls(0, dto.entry_final_uid, dto.account_instance_uid, dto.project_instance_uid, dto.project_milestone_uid, dto.invoice_instance_uid, dto.entry_period, dto.entry_note, dto.lock_uid, dto.start_date, dto.end_date, dto.entry_minutes, dto.is_approved, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, dto.custom_attributes)
    def clone_read(self):
        return entry_final_read_dto(self.id, self.entry_final_uid, self.account_instance_uid, self.project_instance_uid, self.project_milestone_uid, self.invoice_instance_uid, self.entry_period, self.entry_note, self.lock_uid, self.start_date, self.end_date, self.entry_minutes, self.is_approved, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes)
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["id"], d["entry_final_uid"], d["account_instance_uid"], d["project_instance_uid"], d["project_milestone_uid"], d["invoice_instance_uid"], d["entry_period"], d["entry_note"], d["lock_uid"], d["start_date"], d["end_date"], d["entry_minutes"], d["is_approved"], d["row_guid"], d["row_version"], d["is_active"], d["created_date"], d["created_by"], d["last_updated_date"], d["last_updated_by"], d["removed_date"], d["removed_by"], d["custom_attributes"])
    def to_read_dict(self) -> dict:
        return asdict(self)
    def to_write(self) -> entry_final_write_dto:
        return entry_final_write_dto(self.entry_final_uid, self.account_instance_uid, self.project_instance_uid, self.project_milestone_uid, self.invoice_instance_uid, self.entry_period, self.entry_note, self.lock_uid, self.start_date, self.end_date, self.entry_minutes, self.is_approved, self.custom_attributes)
    def to_thin(self) -> entry_final_thin_dto:
        return entry_final_thin_dto(self.entry_final_uid, self.row_guid, self.is_active)
    def touch(self, updated_by: str = "system"):
        self.last_updated_date = datetime.datetime.now()
        self.last_updated_by = updated_by
        self.row_version = self.row_version+1
    def get_list_all_values(self) -> list[any]:
        return [self.id, self.entry_final_uid, self.account_instance_uid, self.project_instance_uid, self.project_milestone_uid, self.invoice_instance_uid, self.entry_period, self.entry_note, self.lock_uid, self.start_date, self.end_date, self.entry_minutes, self.is_approved, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]
    def get_list_update_values(self, updated_by: str) -> list[any]:
        return [self.account_instance_uid, self.project_instance_uid, self.project_milestone_uid, self.invoice_instance_uid, self.entry_period, self.entry_note, self.lock_uid, self.start_date, self.end_date, self.entry_minutes, self.is_approved, self.custom_attributes, updated_by, self.entry_final_uid]
    def is_older_than(self, dt: datetime.datetime) -> bool:
        return self.created_date < dt
    def is_newer_than(self, dt: datetime.datetime) -> bool:
        return self.created_date > dt
    def to_json_read(self) -> str:
        return json.dumps(self.to_read_dict())


@dataclass(frozen=False)
class entry_save_read_dto(base_read_dto, entry_save_write_dto):
    id: int
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
    row_guid: str
    row_version: int
    is_active: int
    created_date: datetime.datetime
    created_by: str
    last_updated_date: datetime.datetime
    last_updated_by: str
    removed_date: datetime.datetime  | None
    removed_by: str  | None
    custom_attributes: str
    def __init__(self, id: int , entry_save_uid: str , account_instance_uid: str , project_instance_uid: str , project_milestone_uid: str , invoice_instance_uid: str  | None, entry_period: str , entry_note: str , lock_uid: str  | None, start_date: datetime.datetime  | None, end_date: datetime.datetime  | None, entry_minutes: int , is_approved: int , row_guid: str , row_version: int , is_active: int , created_date: datetime.datetime , created_by: str , last_updated_date: datetime.datetime , last_updated_by: str , removed_date: datetime.datetime  | None, removed_by: str  | None, custom_attributes: str ):
        self.id = id
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
        self.row_guid = row_guid
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
        return cls(0, "", "", "", "", "", "", "", "", datetime.datetime.now(), datetime.datetime.now(), 0, 0, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def default_read(cls):
        return cls(0, base_dto.get_random_uid(), "", "", "", "", "", "", "", datetime.datetime.now(), datetime.datetime.now(), 0, 0, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def random_read(cls):
        return cls(0, base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), datetime.datetime.now(), datetime.datetime.now(), 0, 0, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_default(cls, entry_save_uid: str , account_instance_uid: str , project_instance_uid: str , project_milestone_uid: str , invoice_instance_uid: str  | None, entry_period: str , entry_note: str , lock_uid: str  | None, start_date: datetime.datetime  | None, end_date: datetime.datetime  | None, entry_minutes: int , is_approved: int ):
        return cls(0, entry_save_uid, account_instance_uid, project_instance_uid, project_milestone_uid, invoice_instance_uid, entry_period, entry_note, lock_uid, start_date, end_date, entry_minutes, is_approved, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_full(cls, id: int , entry_save_uid: str , account_instance_uid: str , project_instance_uid: str , project_milestone_uid: str , invoice_instance_uid: str  | None, entry_period: str , entry_note: str , lock_uid: str  | None, start_date: datetime.datetime  | None, end_date: datetime.datetime  | None, entry_minutes: int , is_approved: int , row_guid: str , row_version: int , is_active: int , created_date: datetime.datetime , created_by: str , last_updated_date: datetime.datetime , last_updated_by: str , removed_date: datetime.datetime  | None, removed_by: str  | None, custom_attributes: str ):
        return cls(id, entry_save_uid, account_instance_uid, project_instance_uid, project_milestone_uid, invoice_instance_uid, entry_period, entry_note, lock_uid, start_date, end_date, entry_minutes, is_approved, row_guid, row_version, is_active, created_date, created_by, last_updated_date, last_updated_by, removed_date, removed_by, custom_attributes)
    @classmethod
    def from_write(cls, dto: entry_save_write_dto):
        return cls(0, dto.entry_save_uid, dto.account_instance_uid, dto.project_instance_uid, dto.project_milestone_uid, dto.invoice_instance_uid, dto.entry_period, dto.entry_note, dto.lock_uid, dto.start_date, dto.end_date, dto.entry_minutes, dto.is_approved, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, dto.custom_attributes)
    def clone_read(self):
        return entry_save_read_dto(self.id, self.entry_save_uid, self.account_instance_uid, self.project_instance_uid, self.project_milestone_uid, self.invoice_instance_uid, self.entry_period, self.entry_note, self.lock_uid, self.start_date, self.end_date, self.entry_minutes, self.is_approved, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes)
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["id"], d["entry_save_uid"], d["account_instance_uid"], d["project_instance_uid"], d["project_milestone_uid"], d["invoice_instance_uid"], d["entry_period"], d["entry_note"], d["lock_uid"], d["start_date"], d["end_date"], d["entry_minutes"], d["is_approved"], d["row_guid"], d["row_version"], d["is_active"], d["created_date"], d["created_by"], d["last_updated_date"], d["last_updated_by"], d["removed_date"], d["removed_by"], d["custom_attributes"])
    def to_read_dict(self) -> dict:
        return asdict(self)
    def to_write(self) -> entry_save_write_dto:
        return entry_save_write_dto(self.entry_save_uid, self.account_instance_uid, self.project_instance_uid, self.project_milestone_uid, self.invoice_instance_uid, self.entry_period, self.entry_note, self.lock_uid, self.start_date, self.end_date, self.entry_minutes, self.is_approved, self.custom_attributes)
    def to_thin(self) -> entry_save_thin_dto:
        return entry_save_thin_dto(self.entry_save_uid, self.row_guid, self.is_active)
    def touch(self, updated_by: str = "system"):
        self.last_updated_date = datetime.datetime.now()
        self.last_updated_by = updated_by
        self.row_version = self.row_version+1
    def get_list_all_values(self) -> list[any]:
        return [self.id, self.entry_save_uid, self.account_instance_uid, self.project_instance_uid, self.project_milestone_uid, self.invoice_instance_uid, self.entry_period, self.entry_note, self.lock_uid, self.start_date, self.end_date, self.entry_minutes, self.is_approved, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]
    def get_list_update_values(self, updated_by: str) -> list[any]:
        return [self.account_instance_uid, self.project_instance_uid, self.project_milestone_uid, self.invoice_instance_uid, self.entry_period, self.entry_note, self.lock_uid, self.start_date, self.end_date, self.entry_minutes, self.is_approved, self.custom_attributes, updated_by, self.entry_save_uid]
    def is_older_than(self, dt: datetime.datetime) -> bool:
        return self.created_date < dt
    def is_newer_than(self, dt: datetime.datetime) -> bool:
        return self.created_date > dt
    def to_json_read(self) -> str:
        return json.dumps(self.to_read_dict())


@dataclass(frozen=False)
class event_channel_read_dto(base_read_dto, event_channel_write_dto):
    id: int
    event_channel_uid: str
    channel_type: str
    channel_name: str
    channel_definition: str
    row_guid: str
    row_version: int
    is_active: int
    created_date: datetime.datetime
    created_by: str
    last_updated_date: datetime.datetime
    last_updated_by: str
    removed_date: datetime.datetime  | None
    removed_by: str  | None
    custom_attributes: str
    def __init__(self, id: int , event_channel_uid: str , channel_type: str , channel_name: str , channel_definition: str , row_guid: str , row_version: int , is_active: int , created_date: datetime.datetime , created_by: str , last_updated_date: datetime.datetime , last_updated_by: str , removed_date: datetime.datetime  | None, removed_by: str  | None, custom_attributes: str ):
        self.id = id
        self.event_channel_uid = event_channel_uid
        self.channel_type = channel_type
        self.channel_name = channel_name
        self.channel_definition = channel_definition
        self.row_guid = row_guid
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
    def new_read_default(cls, event_channel_uid: str , channel_type: str , channel_name: str , channel_definition: str ):
        return cls(0, event_channel_uid, channel_type, channel_name, channel_definition, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_full(cls, id: int , event_channel_uid: str , channel_type: str , channel_name: str , channel_definition: str , row_guid: str , row_version: int , is_active: int , created_date: datetime.datetime , created_by: str , last_updated_date: datetime.datetime , last_updated_by: str , removed_date: datetime.datetime  | None, removed_by: str  | None, custom_attributes: str ):
        return cls(id, event_channel_uid, channel_type, channel_name, channel_definition, row_guid, row_version, is_active, created_date, created_by, last_updated_date, last_updated_by, removed_date, removed_by, custom_attributes)
    @classmethod
    def from_write(cls, dto: event_channel_write_dto):
        return cls(0, dto.event_channel_uid, dto.channel_type, dto.channel_name, dto.channel_definition, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, dto.custom_attributes)
    def clone_read(self):
        return event_channel_read_dto(self.id, self.event_channel_uid, self.channel_type, self.channel_name, self.channel_definition, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes)
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["id"], d["event_channel_uid"], d["channel_type"], d["channel_name"], d["channel_definition"], d["row_guid"], d["row_version"], d["is_active"], d["created_date"], d["created_by"], d["last_updated_date"], d["last_updated_by"], d["removed_date"], d["removed_by"], d["custom_attributes"])
    def to_read_dict(self) -> dict:
        return asdict(self)
    def to_write(self) -> event_channel_write_dto:
        return event_channel_write_dto(self.event_channel_uid, self.channel_type, self.channel_name, self.channel_definition, self.custom_attributes)
    def to_thin(self) -> event_channel_thin_dto:
        return event_channel_thin_dto(self.event_channel_uid, self.row_guid, self.is_active)
    def touch(self, updated_by: str = "system"):
        self.last_updated_date = datetime.datetime.now()
        self.last_updated_by = updated_by
        self.row_version = self.row_version+1
    def get_list_all_values(self) -> list[any]:
        return [self.id, self.event_channel_uid, self.channel_type, self.channel_name, self.channel_definition, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]
    def get_list_update_values(self, updated_by: str) -> list[any]:
        return [self.channel_type, self.channel_name, self.channel_definition, self.custom_attributes, updated_by, self.event_channel_uid]
    def is_older_than(self, dt: datetime.datetime) -> bool:
        return self.created_date < dt
    def is_newer_than(self, dt: datetime.datetime) -> bool:
        return self.created_date > dt
    def to_json_read(self) -> str:
        return json.dumps(self.to_read_dict())


@dataclass(frozen=False)
class event_instance_read_dto(base_read_dto, event_instance_write_dto):
    id: int
    event_instance_uid: str
    event_type: str
    event_object: str
    event_method: str
    event_parameters: str
    event_signature: str
    published_count: int
    event_date: datetime.datetime
    row_guid: str
    row_version: int
    is_active: int
    created_date: datetime.datetime
    created_by: str
    last_updated_date: datetime.datetime
    last_updated_by: str
    removed_date: datetime.datetime  | None
    removed_by: str  | None
    custom_attributes: str
    def __init__(self, id: int , event_instance_uid: str , event_type: str , event_object: str , event_method: str , event_parameters: str , event_signature: str , published_count: int , event_date: datetime.datetime , row_guid: str , row_version: int , is_active: int , created_date: datetime.datetime , created_by: str , last_updated_date: datetime.datetime , last_updated_by: str , removed_date: datetime.datetime  | None, removed_by: str  | None, custom_attributes: str ):
        self.id = id
        self.event_instance_uid = event_instance_uid
        self.event_type = event_type
        self.event_object = event_object
        self.event_method = event_method
        self.event_parameters = event_parameters
        self.event_signature = event_signature
        self.published_count = published_count
        self.event_date = event_date
        self.row_guid = row_guid
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
        return cls(0, "", "", "", "", "", "", 0, datetime.datetime.now(), "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def default_read(cls):
        return cls(0, base_dto.get_random_uid(), "", "", "", "", "", 0, datetime.datetime.now(), "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def random_read(cls):
        return cls(0, base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), 0, datetime.datetime.now(), "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_default(cls, event_instance_uid: str , event_type: str , event_object: str , event_method: str , event_parameters: str , event_signature: str , published_count: int , event_date: datetime.datetime ):
        return cls(0, event_instance_uid, event_type, event_object, event_method, event_parameters, event_signature, published_count, event_date, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_full(cls, id: int , event_instance_uid: str , event_type: str , event_object: str , event_method: str , event_parameters: str , event_signature: str , published_count: int , event_date: datetime.datetime , row_guid: str , row_version: int , is_active: int , created_date: datetime.datetime , created_by: str , last_updated_date: datetime.datetime , last_updated_by: str , removed_date: datetime.datetime  | None, removed_by: str  | None, custom_attributes: str ):
        return cls(id, event_instance_uid, event_type, event_object, event_method, event_parameters, event_signature, published_count, event_date, row_guid, row_version, is_active, created_date, created_by, last_updated_date, last_updated_by, removed_date, removed_by, custom_attributes)
    @classmethod
    def from_write(cls, dto: event_instance_write_dto):
        return cls(0, dto.event_instance_uid, dto.event_type, dto.event_object, dto.event_method, dto.event_parameters, dto.event_signature, dto.published_count, dto.event_date, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, dto.custom_attributes)
    def clone_read(self):
        return event_instance_read_dto(self.id, self.event_instance_uid, self.event_type, self.event_object, self.event_method, self.event_parameters, self.event_signature, self.published_count, self.event_date, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes)
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["id"], d["event_instance_uid"], d["event_type"], d["event_object"], d["event_method"], d["event_parameters"], d["event_signature"], d["published_count"], d["event_date"], d["row_guid"], d["row_version"], d["is_active"], d["created_date"], d["created_by"], d["last_updated_date"], d["last_updated_by"], d["removed_date"], d["removed_by"], d["custom_attributes"])
    def to_read_dict(self) -> dict:
        return asdict(self)
    def to_write(self) -> event_instance_write_dto:
        return event_instance_write_dto(self.event_instance_uid, self.event_type, self.event_object, self.event_method, self.event_parameters, self.event_signature, self.published_count, self.event_date, self.custom_attributes)
    def to_thin(self) -> event_instance_thin_dto:
        return event_instance_thin_dto(self.event_instance_uid, self.row_guid, self.is_active)
    def touch(self, updated_by: str = "system"):
        self.last_updated_date = datetime.datetime.now()
        self.last_updated_by = updated_by
        self.row_version = self.row_version+1
    def get_list_all_values(self) -> list[any]:
        return [self.id, self.event_instance_uid, self.event_type, self.event_object, self.event_method, self.event_parameters, self.event_signature, self.published_count, self.event_date, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]
    def get_list_update_values(self, updated_by: str) -> list[any]:
        return [self.event_type, self.event_object, self.event_method, self.event_parameters, self.event_signature, self.published_count, self.event_date, self.custom_attributes, updated_by, self.event_instance_uid]
    def is_older_than(self, dt: datetime.datetime) -> bool:
        return self.created_date < dt
    def is_newer_than(self, dt: datetime.datetime) -> bool:
        return self.created_date > dt
    def to_json_read(self) -> str:
        return json.dumps(self.to_read_dict())


@dataclass(frozen=False)
class event_subscription_read_dto(base_read_dto, event_subscription_write_dto):
    id: int
    event_subscription_uid: str
    event_channel_uid: str
    subscription_name: str
    subscription_filter: str
    subscription_topic: str
    subscription_template: str
    row_guid: str
    row_version: int
    is_active: int
    created_date: datetime.datetime
    created_by: str
    last_updated_date: datetime.datetime
    last_updated_by: str
    removed_date: datetime.datetime  | None
    removed_by: str  | None
    custom_attributes: str
    def __init__(self, id: int , event_subscription_uid: str , event_channel_uid: str , subscription_name: str , subscription_filter: str , subscription_topic: str , subscription_template: str , row_guid: str , row_version: int , is_active: int , created_date: datetime.datetime , created_by: str , last_updated_date: datetime.datetime , last_updated_by: str , removed_date: datetime.datetime  | None, removed_by: str  | None, custom_attributes: str ):
        self.id = id
        self.event_subscription_uid = event_subscription_uid
        self.event_channel_uid = event_channel_uid
        self.subscription_name = subscription_name
        self.subscription_filter = subscription_filter
        self.subscription_topic = subscription_topic
        self.subscription_template = subscription_template
        self.row_guid = row_guid
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
    def new_read_default(cls, event_subscription_uid: str , event_channel_uid: str , subscription_name: str , subscription_filter: str , subscription_topic: str , subscription_template: str ):
        return cls(0, event_subscription_uid, event_channel_uid, subscription_name, subscription_filter, subscription_topic, subscription_template, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_full(cls, id: int , event_subscription_uid: str , event_channel_uid: str , subscription_name: str , subscription_filter: str , subscription_topic: str , subscription_template: str , row_guid: str , row_version: int , is_active: int , created_date: datetime.datetime , created_by: str , last_updated_date: datetime.datetime , last_updated_by: str , removed_date: datetime.datetime  | None, removed_by: str  | None, custom_attributes: str ):
        return cls(id, event_subscription_uid, event_channel_uid, subscription_name, subscription_filter, subscription_topic, subscription_template, row_guid, row_version, is_active, created_date, created_by, last_updated_date, last_updated_by, removed_date, removed_by, custom_attributes)
    @classmethod
    def from_write(cls, dto: event_subscription_write_dto):
        return cls(0, dto.event_subscription_uid, dto.event_channel_uid, dto.subscription_name, dto.subscription_filter, dto.subscription_topic, dto.subscription_template, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, dto.custom_attributes)
    def clone_read(self):
        return event_subscription_read_dto(self.id, self.event_subscription_uid, self.event_channel_uid, self.subscription_name, self.subscription_filter, self.subscription_topic, self.subscription_template, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes)
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["id"], d["event_subscription_uid"], d["event_channel_uid"], d["subscription_name"], d["subscription_filter"], d["subscription_topic"], d["subscription_template"], d["row_guid"], d["row_version"], d["is_active"], d["created_date"], d["created_by"], d["last_updated_date"], d["last_updated_by"], d["removed_date"], d["removed_by"], d["custom_attributes"])
    def to_read_dict(self) -> dict:
        return asdict(self)
    def to_write(self) -> event_subscription_write_dto:
        return event_subscription_write_dto(self.event_subscription_uid, self.event_channel_uid, self.subscription_name, self.subscription_filter, self.subscription_topic, self.subscription_template, self.custom_attributes)
    def to_thin(self) -> event_subscription_thin_dto:
        return event_subscription_thin_dto(self.event_subscription_uid, self.row_guid, self.is_active)
    def touch(self, updated_by: str = "system"):
        self.last_updated_date = datetime.datetime.now()
        self.last_updated_by = updated_by
        self.row_version = self.row_version+1
    def get_list_all_values(self) -> list[any]:
        return [self.id, self.event_subscription_uid, self.event_channel_uid, self.subscription_name, self.subscription_filter, self.subscription_topic, self.subscription_template, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]
    def get_list_update_values(self, updated_by: str) -> list[any]:
        return [self.event_channel_uid, self.subscription_name, self.subscription_filter, self.subscription_topic, self.subscription_template, self.custom_attributes, updated_by, self.event_subscription_uid]
    def is_older_than(self, dt: datetime.datetime) -> bool:
        return self.created_date < dt
    def is_newer_than(self, dt: datetime.datetime) -> bool:
        return self.created_date > dt
    def to_json_read(self) -> str:
        return json.dumps(self.to_read_dict())


@dataclass(frozen=False)
class invoice_instance_read_dto(base_read_dto, invoice_instance_write_dto):
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
    row_version: int
    is_active: int
    created_date: datetime.datetime
    created_by: str
    last_updated_date: datetime.datetime
    last_updated_by: str
    removed_date: datetime.datetime  | None
    removed_by: str  | None
    custom_attributes: str
    def __init__(self, id: int , invoice_instance_uid: str , client_instance_uid: str , account_instance_uid: str , period_code: str , invoice_number: str , invoice_details: str , invoice_status: str , invoice_currency: str , invoice_amount: str , row_guid: str , row_version: int , is_active: int , created_date: datetime.datetime , created_by: str , last_updated_date: datetime.datetime , last_updated_by: str , removed_date: datetime.datetime  | None, removed_by: str  | None, custom_attributes: str ):
        self.id = id
        self.invoice_instance_uid = invoice_instance_uid
        self.client_instance_uid = client_instance_uid
        self.account_instance_uid = account_instance_uid
        self.period_code = period_code
        self.invoice_number = invoice_number
        self.invoice_details = invoice_details
        self.invoice_status = invoice_status
        self.invoice_currency = invoice_currency
        self.invoice_amount = invoice_amount
        self.row_guid = row_guid
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
        return cls(0, base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_default(cls, invoice_instance_uid: str , client_instance_uid: str , account_instance_uid: str , period_code: str , invoice_number: str , invoice_details: str , invoice_status: str , invoice_currency: str , invoice_amount: str ):
        return cls(0, invoice_instance_uid, client_instance_uid, account_instance_uid, period_code, invoice_number, invoice_details, invoice_status, invoice_currency, invoice_amount, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_full(cls, id: int , invoice_instance_uid: str , client_instance_uid: str , account_instance_uid: str , period_code: str , invoice_number: str , invoice_details: str , invoice_status: str , invoice_currency: str , invoice_amount: str , row_guid: str , row_version: int , is_active: int , created_date: datetime.datetime , created_by: str , last_updated_date: datetime.datetime , last_updated_by: str , removed_date: datetime.datetime  | None, removed_by: str  | None, custom_attributes: str ):
        return cls(id, invoice_instance_uid, client_instance_uid, account_instance_uid, period_code, invoice_number, invoice_details, invoice_status, invoice_currency, invoice_amount, row_guid, row_version, is_active, created_date, created_by, last_updated_date, last_updated_by, removed_date, removed_by, custom_attributes)
    @classmethod
    def from_write(cls, dto: invoice_instance_write_dto):
        return cls(0, dto.invoice_instance_uid, dto.client_instance_uid, dto.account_instance_uid, dto.period_code, dto.invoice_number, dto.invoice_details, dto.invoice_status, dto.invoice_currency, dto.invoice_amount, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, dto.custom_attributes)
    def clone_read(self):
        return invoice_instance_read_dto(self.id, self.invoice_instance_uid, self.client_instance_uid, self.account_instance_uid, self.period_code, self.invoice_number, self.invoice_details, self.invoice_status, self.invoice_currency, self.invoice_amount, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes)
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["id"], d["invoice_instance_uid"], d["client_instance_uid"], d["account_instance_uid"], d["period_code"], d["invoice_number"], d["invoice_details"], d["invoice_status"], d["invoice_currency"], d["invoice_amount"], d["row_guid"], d["row_version"], d["is_active"], d["created_date"], d["created_by"], d["last_updated_date"], d["last_updated_by"], d["removed_date"], d["removed_by"], d["custom_attributes"])
    def to_read_dict(self) -> dict:
        return asdict(self)
    def to_write(self) -> invoice_instance_write_dto:
        return invoice_instance_write_dto(self.invoice_instance_uid, self.client_instance_uid, self.account_instance_uid, self.period_code, self.invoice_number, self.invoice_details, self.invoice_status, self.invoice_currency, self.invoice_amount, self.custom_attributes)
    def to_thin(self) -> invoice_instance_thin_dto:
        return invoice_instance_thin_dto(self.invoice_instance_uid, self.row_guid, self.is_active)
    def touch(self, updated_by: str = "system"):
        self.last_updated_date = datetime.datetime.now()
        self.last_updated_by = updated_by
        self.row_version = self.row_version+1
    def get_list_all_values(self) -> list[any]:
        return [self.id, self.invoice_instance_uid, self.client_instance_uid, self.account_instance_uid, self.period_code, self.invoice_number, self.invoice_details, self.invoice_status, self.invoice_currency, self.invoice_amount, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]
    def get_list_update_values(self, updated_by: str) -> list[any]:
        return [self.client_instance_uid, self.account_instance_uid, self.period_code, self.invoice_number, self.invoice_details, self.invoice_status, self.invoice_currency, self.invoice_amount, self.custom_attributes, updated_by, self.invoice_instance_uid]
    def is_older_than(self, dt: datetime.datetime) -> bool:
        return self.created_date < dt
    def is_newer_than(self, dt: datetime.datetime) -> bool:
        return self.created_date > dt
    def to_json_read(self) -> str:
        return json.dumps(self.to_read_dict())


@dataclass(frozen=False)
class notification_instance_read_dto(base_read_dto, notification_instance_write_dto):
    id: int
    notification_instance_uid: str
    account_instance_uid: str
    notification_type: str
    notification_topic: str
    notification_format: str
    notification_content: str
    sending_status: str
    row_guid: str
    row_version: int
    is_active: int
    created_date: datetime.datetime
    created_by: str
    last_updated_date: datetime.datetime
    last_updated_by: str
    removed_date: datetime.datetime  | None
    removed_by: str  | None
    custom_attributes: str
    def __init__(self, id: int , notification_instance_uid: str , account_instance_uid: str , notification_type: str , notification_topic: str , notification_format: str , notification_content: str , sending_status: str , row_guid: str , row_version: int , is_active: int , created_date: datetime.datetime , created_by: str , last_updated_date: datetime.datetime , last_updated_by: str , removed_date: datetime.datetime  | None, removed_by: str  | None, custom_attributes: str ):
        self.id = id
        self.notification_instance_uid = notification_instance_uid
        self.account_instance_uid = account_instance_uid
        self.notification_type = notification_type
        self.notification_topic = notification_topic
        self.notification_format = notification_format
        self.notification_content = notification_content
        self.sending_status = sending_status
        self.row_guid = row_guid
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
    def new_read_default(cls, notification_instance_uid: str , account_instance_uid: str , notification_type: str , notification_topic: str , notification_format: str , notification_content: str , sending_status: str ):
        return cls(0, notification_instance_uid, account_instance_uid, notification_type, notification_topic, notification_format, notification_content, sending_status, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_full(cls, id: int , notification_instance_uid: str , account_instance_uid: str , notification_type: str , notification_topic: str , notification_format: str , notification_content: str , sending_status: str , row_guid: str , row_version: int , is_active: int , created_date: datetime.datetime , created_by: str , last_updated_date: datetime.datetime , last_updated_by: str , removed_date: datetime.datetime  | None, removed_by: str  | None, custom_attributes: str ):
        return cls(id, notification_instance_uid, account_instance_uid, notification_type, notification_topic, notification_format, notification_content, sending_status, row_guid, row_version, is_active, created_date, created_by, last_updated_date, last_updated_by, removed_date, removed_by, custom_attributes)
    @classmethod
    def from_write(cls, dto: notification_instance_write_dto):
        return cls(0, dto.notification_instance_uid, dto.account_instance_uid, dto.notification_type, dto.notification_topic, dto.notification_format, dto.notification_content, dto.sending_status, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, dto.custom_attributes)
    def clone_read(self):
        return notification_instance_read_dto(self.id, self.notification_instance_uid, self.account_instance_uid, self.notification_type, self.notification_topic, self.notification_format, self.notification_content, self.sending_status, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes)
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["id"], d["notification_instance_uid"], d["account_instance_uid"], d["notification_type"], d["notification_topic"], d["notification_format"], d["notification_content"], d["sending_status"], d["row_guid"], d["row_version"], d["is_active"], d["created_date"], d["created_by"], d["last_updated_date"], d["last_updated_by"], d["removed_date"], d["removed_by"], d["custom_attributes"])
    def to_read_dict(self) -> dict:
        return asdict(self)
    def to_write(self) -> notification_instance_write_dto:
        return notification_instance_write_dto(self.notification_instance_uid, self.account_instance_uid, self.notification_type, self.notification_topic, self.notification_format, self.notification_content, self.sending_status, self.custom_attributes)
    def to_thin(self) -> notification_instance_thin_dto:
        return notification_instance_thin_dto(self.notification_instance_uid, self.row_guid, self.is_active)
    def touch(self, updated_by: str = "system"):
        self.last_updated_date = datetime.datetime.now()
        self.last_updated_by = updated_by
        self.row_version = self.row_version+1
    def get_list_all_values(self) -> list[any]:
        return [self.id, self.notification_instance_uid, self.account_instance_uid, self.notification_type, self.notification_topic, self.notification_format, self.notification_content, self.sending_status, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]
    def get_list_update_values(self, updated_by: str) -> list[any]:
        return [self.account_instance_uid, self.notification_type, self.notification_topic, self.notification_format, self.notification_content, self.sending_status, self.custom_attributes, updated_by, self.notification_instance_uid]
    def is_older_than(self, dt: datetime.datetime) -> bool:
        return self.created_date < dt
    def is_newer_than(self, dt: datetime.datetime) -> bool:
        return self.created_date > dt
    def to_json_read(self) -> str:
        return json.dumps(self.to_read_dict())


@dataclass(frozen=False)
class project_budget_read_dto(base_read_dto, project_budget_write_dto):
    id: int
    project_budget_uid: str
    project_instance_uid: str
    budget_name: str
    budget_currency: str
    budget_value: str
    is_current: int
    row_guid: str
    row_version: int
    is_active: int
    created_date: datetime.datetime
    created_by: str
    last_updated_date: datetime.datetime
    last_updated_by: str
    removed_date: datetime.datetime  | None
    removed_by: str  | None
    custom_attributes: str
    def __init__(self, id: int , project_budget_uid: str , project_instance_uid: str , budget_name: str , budget_currency: str , budget_value: str , is_current: int , row_guid: str , row_version: int , is_active: int , created_date: datetime.datetime , created_by: str , last_updated_date: datetime.datetime , last_updated_by: str , removed_date: datetime.datetime  | None, removed_by: str  | None, custom_attributes: str ):
        self.id = id
        self.project_budget_uid = project_budget_uid
        self.project_instance_uid = project_instance_uid
        self.budget_name = budget_name
        self.budget_currency = budget_currency
        self.budget_value = budget_value
        self.is_current = is_current
        self.row_guid = row_guid
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
    def new_read_default(cls, project_budget_uid: str , project_instance_uid: str , budget_name: str , budget_currency: str , budget_value: str , is_current: int ):
        return cls(0, project_budget_uid, project_instance_uid, budget_name, budget_currency, budget_value, is_current, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_full(cls, id: int , project_budget_uid: str , project_instance_uid: str , budget_name: str , budget_currency: str , budget_value: str , is_current: int , row_guid: str , row_version: int , is_active: int , created_date: datetime.datetime , created_by: str , last_updated_date: datetime.datetime , last_updated_by: str , removed_date: datetime.datetime  | None, removed_by: str  | None, custom_attributes: str ):
        return cls(id, project_budget_uid, project_instance_uid, budget_name, budget_currency, budget_value, is_current, row_guid, row_version, is_active, created_date, created_by, last_updated_date, last_updated_by, removed_date, removed_by, custom_attributes)
    @classmethod
    def from_write(cls, dto: project_budget_write_dto):
        return cls(0, dto.project_budget_uid, dto.project_instance_uid, dto.budget_name, dto.budget_currency, dto.budget_value, dto.is_current, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, dto.custom_attributes)
    def clone_read(self):
        return project_budget_read_dto(self.id, self.project_budget_uid, self.project_instance_uid, self.budget_name, self.budget_currency, self.budget_value, self.is_current, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes)
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["id"], d["project_budget_uid"], d["project_instance_uid"], d["budget_name"], d["budget_currency"], d["budget_value"], d["is_current"], d["row_guid"], d["row_version"], d["is_active"], d["created_date"], d["created_by"], d["last_updated_date"], d["last_updated_by"], d["removed_date"], d["removed_by"], d["custom_attributes"])
    def to_read_dict(self) -> dict:
        return asdict(self)
    def to_write(self) -> project_budget_write_dto:
        return project_budget_write_dto(self.project_budget_uid, self.project_instance_uid, self.budget_name, self.budget_currency, self.budget_value, self.is_current, self.custom_attributes)
    def to_thin(self) -> project_budget_thin_dto:
        return project_budget_thin_dto(self.project_budget_uid, self.row_guid, self.is_active)
    def touch(self, updated_by: str = "system"):
        self.last_updated_date = datetime.datetime.now()
        self.last_updated_by = updated_by
        self.row_version = self.row_version+1
    def get_list_all_values(self) -> list[any]:
        return [self.id, self.project_budget_uid, self.project_instance_uid, self.budget_name, self.budget_currency, self.budget_value, self.is_current, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]
    def get_list_update_values(self, updated_by: str) -> list[any]:
        return [self.project_instance_uid, self.budget_name, self.budget_currency, self.budget_value, self.is_current, self.custom_attributes, updated_by, self.project_budget_uid]
    def is_older_than(self, dt: datetime.datetime) -> bool:
        return self.created_date < dt
    def is_newer_than(self, dt: datetime.datetime) -> bool:
        return self.created_date > dt
    def to_json_read(self) -> str:
        return json.dumps(self.to_read_dict())


@dataclass(frozen=False)
class project_group_read_dto(base_read_dto, project_group_write_dto):
    id: int
    project_group_uid: str
    project_group_name: str
    project_group_description: str
    row_guid: str
    row_version: int
    is_active: int
    created_date: datetime.datetime
    created_by: str
    last_updated_date: datetime.datetime
    last_updated_by: str
    removed_date: datetime.datetime  | None
    removed_by: str  | None
    custom_attributes: str
    def __init__(self, id: int , project_group_uid: str , project_group_name: str , project_group_description: str , row_guid: str , row_version: int , is_active: int , created_date: datetime.datetime , created_by: str , last_updated_date: datetime.datetime , last_updated_by: str , removed_date: datetime.datetime  | None, removed_by: str  | None, custom_attributes: str ):
        self.id = id
        self.project_group_uid = project_group_uid
        self.project_group_name = project_group_name
        self.project_group_description = project_group_description
        self.row_guid = row_guid
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
    def new_read_default(cls, project_group_uid: str , project_group_name: str , project_group_description: str ):
        return cls(0, project_group_uid, project_group_name, project_group_description, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_full(cls, id: int , project_group_uid: str , project_group_name: str , project_group_description: str , row_guid: str , row_version: int , is_active: int , created_date: datetime.datetime , created_by: str , last_updated_date: datetime.datetime , last_updated_by: str , removed_date: datetime.datetime  | None, removed_by: str  | None, custom_attributes: str ):
        return cls(id, project_group_uid, project_group_name, project_group_description, row_guid, row_version, is_active, created_date, created_by, last_updated_date, last_updated_by, removed_date, removed_by, custom_attributes)
    @classmethod
    def from_write(cls, dto: project_group_write_dto):
        return cls(0, dto.project_group_uid, dto.project_group_name, dto.project_group_description, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, dto.custom_attributes)
    def clone_read(self):
        return project_group_read_dto(self.id, self.project_group_uid, self.project_group_name, self.project_group_description, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes)
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["id"], d["project_group_uid"], d["project_group_name"], d["project_group_description"], d["row_guid"], d["row_version"], d["is_active"], d["created_date"], d["created_by"], d["last_updated_date"], d["last_updated_by"], d["removed_date"], d["removed_by"], d["custom_attributes"])
    def to_read_dict(self) -> dict:
        return asdict(self)
    def to_write(self) -> project_group_write_dto:
        return project_group_write_dto(self.project_group_uid, self.project_group_name, self.project_group_description, self.custom_attributes)
    def to_thin(self) -> project_group_thin_dto:
        return project_group_thin_dto(self.project_group_uid, self.row_guid, self.is_active)
    def touch(self, updated_by: str = "system"):
        self.last_updated_date = datetime.datetime.now()
        self.last_updated_by = updated_by
        self.row_version = self.row_version+1
    def get_list_all_values(self) -> list[any]:
        return [self.id, self.project_group_uid, self.project_group_name, self.project_group_description, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]
    def get_list_update_values(self, updated_by: str) -> list[any]:
        return [self.project_group_name, self.project_group_description, self.custom_attributes, updated_by, self.project_group_uid]
    def is_older_than(self, dt: datetime.datetime) -> bool:
        return self.created_date < dt
    def is_newer_than(self, dt: datetime.datetime) -> bool:
        return self.created_date > dt
    def to_json_read(self) -> str:
        return json.dumps(self.to_read_dict())


@dataclass(frozen=False)
class project_instance_read_dto(base_read_dto, project_instance_write_dto):
    id: int
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
    row_guid: str
    row_version: int
    is_active: int
    created_date: datetime.datetime
    created_by: str
    last_updated_date: datetime.datetime
    last_updated_by: str
    removed_date: datetime.datetime  | None
    removed_by: str  | None
    custom_attributes: str
    def __init__(self, id: int , project_instance_uid: str , client_instance_uid: str , manager_account_instance_uid: str , project_group_uid: str , project_name: str , project_code: str , is_billable: int , start_date: datetime.datetime  | None, end_date: datetime.datetime  | None, current_billed: str , budget: str , row_guid: str , row_version: int , is_active: int , created_date: datetime.datetime , created_by: str , last_updated_date: datetime.datetime , last_updated_by: str , removed_date: datetime.datetime  | None, removed_by: str  | None, custom_attributes: str ):
        self.id = id
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
        self.row_guid = row_guid
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
        return cls(0, "", "", "", "", "", "", 0, datetime.datetime.now(), datetime.datetime.now(), "", "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def default_read(cls):
        return cls(0, base_dto.get_random_uid(), "", "", "", "", "", 0, datetime.datetime.now(), datetime.datetime.now(), "", "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def random_read(cls):
        return cls(0, base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), 0, datetime.datetime.now(), datetime.datetime.now(), "", "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_default(cls, project_instance_uid: str , client_instance_uid: str , manager_account_instance_uid: str , project_group_uid: str , project_name: str , project_code: str , is_billable: int , start_date: datetime.datetime  | None, end_date: datetime.datetime  | None, current_billed: str , budget: str ):
        return cls(0, project_instance_uid, client_instance_uid, manager_account_instance_uid, project_group_uid, project_name, project_code, is_billable, start_date, end_date, current_billed, budget, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_full(cls, id: int , project_instance_uid: str , client_instance_uid: str , manager_account_instance_uid: str , project_group_uid: str , project_name: str , project_code: str , is_billable: int , start_date: datetime.datetime  | None, end_date: datetime.datetime  | None, current_billed: str , budget: str , row_guid: str , row_version: int , is_active: int , created_date: datetime.datetime , created_by: str , last_updated_date: datetime.datetime , last_updated_by: str , removed_date: datetime.datetime  | None, removed_by: str  | None, custom_attributes: str ):
        return cls(id, project_instance_uid, client_instance_uid, manager_account_instance_uid, project_group_uid, project_name, project_code, is_billable, start_date, end_date, current_billed, budget, row_guid, row_version, is_active, created_date, created_by, last_updated_date, last_updated_by, removed_date, removed_by, custom_attributes)
    @classmethod
    def from_write(cls, dto: project_instance_write_dto):
        return cls(0, dto.project_instance_uid, dto.client_instance_uid, dto.manager_account_instance_uid, dto.project_group_uid, dto.project_name, dto.project_code, dto.is_billable, dto.start_date, dto.end_date, dto.current_billed, dto.budget, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, dto.custom_attributes)
    def clone_read(self):
        return project_instance_read_dto(self.id, self.project_instance_uid, self.client_instance_uid, self.manager_account_instance_uid, self.project_group_uid, self.project_name, self.project_code, self.is_billable, self.start_date, self.end_date, self.current_billed, self.budget, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes)
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["id"], d["project_instance_uid"], d["client_instance_uid"], d["manager_account_instance_uid"], d["project_group_uid"], d["project_name"], d["project_code"], d["is_billable"], d["start_date"], d["end_date"], d["current_billed"], d["budget"], d["row_guid"], d["row_version"], d["is_active"], d["created_date"], d["created_by"], d["last_updated_date"], d["last_updated_by"], d["removed_date"], d["removed_by"], d["custom_attributes"])
    def to_read_dict(self) -> dict:
        return asdict(self)
    def to_write(self) -> project_instance_write_dto:
        return project_instance_write_dto(self.project_instance_uid, self.client_instance_uid, self.manager_account_instance_uid, self.project_group_uid, self.project_name, self.project_code, self.is_billable, self.start_date, self.end_date, self.current_billed, self.budget, self.custom_attributes)
    def to_thin(self) -> project_instance_thin_dto:
        return project_instance_thin_dto(self.project_instance_uid, self.row_guid, self.is_active)
    def touch(self, updated_by: str = "system"):
        self.last_updated_date = datetime.datetime.now()
        self.last_updated_by = updated_by
        self.row_version = self.row_version+1
    def get_list_all_values(self) -> list[any]:
        return [self.id, self.project_instance_uid, self.client_instance_uid, self.manager_account_instance_uid, self.project_group_uid, self.project_name, self.project_code, self.is_billable, self.start_date, self.end_date, self.current_billed, self.budget, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]
    def get_list_update_values(self, updated_by: str) -> list[any]:
        return [self.client_instance_uid, self.manager_account_instance_uid, self.project_group_uid, self.project_name, self.project_code, self.is_billable, self.start_date, self.end_date, self.current_billed, self.budget, self.custom_attributes, updated_by, self.project_instance_uid]
    def is_older_than(self, dt: datetime.datetime) -> bool:
        return self.created_date < dt
    def is_newer_than(self, dt: datetime.datetime) -> bool:
        return self.created_date > dt
    def to_json_read(self) -> str:
        return json.dumps(self.to_read_dict())


@dataclass(frozen=False)
class project_milestone_read_dto(base_read_dto, project_milestone_write_dto):
    id: int
    project_milestone_uid: str
    project_instance_uid: str
    project_budget_uid: str  | None
    milestone_name: str
    start_date: datetime.datetime
    end_date: datetime.datetime
    status_name: str
    row_guid: str
    row_version: int
    is_active: int
    created_date: datetime.datetime
    created_by: str
    last_updated_date: datetime.datetime
    last_updated_by: str
    removed_date: datetime.datetime  | None
    removed_by: str  | None
    custom_attributes: str
    def __init__(self, id: int , project_milestone_uid: str , project_instance_uid: str , project_budget_uid: str  | None, milestone_name: str , start_date: datetime.datetime , end_date: datetime.datetime , status_name: str , row_guid: str , row_version: int , is_active: int , created_date: datetime.datetime , created_by: str , last_updated_date: datetime.datetime , last_updated_by: str , removed_date: datetime.datetime  | None, removed_by: str  | None, custom_attributes: str ):
        self.id = id
        self.project_milestone_uid = project_milestone_uid
        self.project_instance_uid = project_instance_uid
        self.project_budget_uid = project_budget_uid
        self.milestone_name = milestone_name
        self.start_date = start_date
        self.end_date = end_date
        self.status_name = status_name
        self.row_guid = row_guid
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
        return cls(0, "", "", "", "", datetime.datetime.now(), datetime.datetime.now(), "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def default_read(cls):
        return cls(0, base_dto.get_random_uid(), "", "", "", datetime.datetime.now(), datetime.datetime.now(), "", "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def random_read(cls):
        return cls(0, base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), base_dto.get_random_uid(), datetime.datetime.now(), datetime.datetime.now(), base_dto.get_random_uid(), "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_default(cls, project_milestone_uid: str , project_instance_uid: str , project_budget_uid: str  | None, milestone_name: str , start_date: datetime.datetime , end_date: datetime.datetime , status_name: str ):
        return cls(0, project_milestone_uid, project_instance_uid, project_budget_uid, milestone_name, start_date, end_date, status_name, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_full(cls, id: int , project_milestone_uid: str , project_instance_uid: str , project_budget_uid: str  | None, milestone_name: str , start_date: datetime.datetime , end_date: datetime.datetime , status_name: str , row_guid: str , row_version: int , is_active: int , created_date: datetime.datetime , created_by: str , last_updated_date: datetime.datetime , last_updated_by: str , removed_date: datetime.datetime  | None, removed_by: str  | None, custom_attributes: str ):
        return cls(id, project_milestone_uid, project_instance_uid, project_budget_uid, milestone_name, start_date, end_date, status_name, row_guid, row_version, is_active, created_date, created_by, last_updated_date, last_updated_by, removed_date, removed_by, custom_attributes)
    @classmethod
    def from_write(cls, dto: project_milestone_write_dto):
        return cls(0, dto.project_milestone_uid, dto.project_instance_uid, dto.project_budget_uid, dto.milestone_name, dto.start_date, dto.end_date, dto.status_name, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, dto.custom_attributes)
    def clone_read(self):
        return project_milestone_read_dto(self.id, self.project_milestone_uid, self.project_instance_uid, self.project_budget_uid, self.milestone_name, self.start_date, self.end_date, self.status_name, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes)
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["id"], d["project_milestone_uid"], d["project_instance_uid"], d["project_budget_uid"], d["milestone_name"], d["start_date"], d["end_date"], d["status_name"], d["row_guid"], d["row_version"], d["is_active"], d["created_date"], d["created_by"], d["last_updated_date"], d["last_updated_by"], d["removed_date"], d["removed_by"], d["custom_attributes"])
    def to_read_dict(self) -> dict:
        return asdict(self)
    def to_write(self) -> project_milestone_write_dto:
        return project_milestone_write_dto(self.project_milestone_uid, self.project_instance_uid, self.project_budget_uid, self.milestone_name, self.start_date, self.end_date, self.status_name, self.custom_attributes)
    def to_thin(self) -> project_milestone_thin_dto:
        return project_milestone_thin_dto(self.project_milestone_uid, self.row_guid, self.is_active)
    def touch(self, updated_by: str = "system"):
        self.last_updated_date = datetime.datetime.now()
        self.last_updated_by = updated_by
        self.row_version = self.row_version+1
    def get_list_all_values(self) -> list[any]:
        return [self.id, self.project_milestone_uid, self.project_instance_uid, self.project_budget_uid, self.milestone_name, self.start_date, self.end_date, self.status_name, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]
    def get_list_update_values(self, updated_by: str) -> list[any]:
        return [self.project_instance_uid, self.project_budget_uid, self.milestone_name, self.start_date, self.end_date, self.status_name, self.custom_attributes, updated_by, self.project_milestone_uid]
    def is_older_than(self, dt: datetime.datetime) -> bool:
        return self.created_date < dt
    def is_newer_than(self, dt: datetime.datetime) -> bool:
        return self.created_date > dt
    def to_json_read(self) -> str:
        return json.dumps(self.to_read_dict())


@dataclass(frozen=False)
class system_attribute_read_dto(base_read_dto, system_attribute_write_dto):
    id: int
    system_attribute_uid: str
    system_object_uid: str
    column_name: str
    attribute_name: str
    attribute_type: str
    attribute_label: str
    attribute_description: str
    row_guid: str
    row_version: int
    is_active: int
    created_date: datetime.datetime
    created_by: str
    last_updated_date: datetime.datetime
    last_updated_by: str
    removed_date: datetime.datetime  | None
    removed_by: str  | None
    custom_attributes: str
    def __init__(self, id: int , system_attribute_uid: str , system_object_uid: str , column_name: str , attribute_name: str , attribute_type: str , attribute_label: str , attribute_description: str , row_guid: str , row_version: int , is_active: int , created_date: datetime.datetime , created_by: str , last_updated_date: datetime.datetime , last_updated_by: str , removed_date: datetime.datetime  | None, removed_by: str  | None, custom_attributes: str ):
        self.id = id
        self.system_attribute_uid = system_attribute_uid
        self.system_object_uid = system_object_uid
        self.column_name = column_name
        self.attribute_name = attribute_name
        self.attribute_type = attribute_type
        self.attribute_label = attribute_label
        self.attribute_description = attribute_description
        self.row_guid = row_guid
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
    def new_read_default(cls, system_attribute_uid: str , system_object_uid: str , column_name: str , attribute_name: str , attribute_type: str , attribute_label: str , attribute_description: str ):
        return cls(0, system_attribute_uid, system_object_uid, column_name, attribute_name, attribute_type, attribute_label, attribute_description, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_full(cls, id: int , system_attribute_uid: str , system_object_uid: str , column_name: str , attribute_name: str , attribute_type: str , attribute_label: str , attribute_description: str , row_guid: str , row_version: int , is_active: int , created_date: datetime.datetime , created_by: str , last_updated_date: datetime.datetime , last_updated_by: str , removed_date: datetime.datetime  | None, removed_by: str  | None, custom_attributes: str ):
        return cls(id, system_attribute_uid, system_object_uid, column_name, attribute_name, attribute_type, attribute_label, attribute_description, row_guid, row_version, is_active, created_date, created_by, last_updated_date, last_updated_by, removed_date, removed_by, custom_attributes)
    @classmethod
    def from_write(cls, dto: system_attribute_write_dto):
        return cls(0, dto.system_attribute_uid, dto.system_object_uid, dto.column_name, dto.attribute_name, dto.attribute_type, dto.attribute_label, dto.attribute_description, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, dto.custom_attributes)
    def clone_read(self):
        return system_attribute_read_dto(self.id, self.system_attribute_uid, self.system_object_uid, self.column_name, self.attribute_name, self.attribute_type, self.attribute_label, self.attribute_description, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes)
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["id"], d["system_attribute_uid"], d["system_object_uid"], d["column_name"], d["attribute_name"], d["attribute_type"], d["attribute_label"], d["attribute_description"], d["row_guid"], d["row_version"], d["is_active"], d["created_date"], d["created_by"], d["last_updated_date"], d["last_updated_by"], d["removed_date"], d["removed_by"], d["custom_attributes"])
    def to_read_dict(self) -> dict:
        return asdict(self)
    def to_write(self) -> system_attribute_write_dto:
        return system_attribute_write_dto(self.system_attribute_uid, self.system_object_uid, self.column_name, self.attribute_name, self.attribute_type, self.attribute_label, self.attribute_description, self.custom_attributes)
    def to_thin(self) -> system_attribute_thin_dto:
        return system_attribute_thin_dto(self.system_attribute_uid, self.row_guid, self.is_active)
    def touch(self, updated_by: str = "system"):
        self.last_updated_date = datetime.datetime.now()
        self.last_updated_by = updated_by
        self.row_version = self.row_version+1
    def get_list_all_values(self) -> list[any]:
        return [self.id, self.system_attribute_uid, self.system_object_uid, self.column_name, self.attribute_name, self.attribute_type, self.attribute_label, self.attribute_description, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]
    def get_list_update_values(self, updated_by: str) -> list[any]:
        return [self.system_object_uid, self.column_name, self.attribute_name, self.attribute_type, self.attribute_label, self.attribute_description, self.custom_attributes, updated_by, self.system_attribute_uid]
    def is_older_than(self, dt: datetime.datetime) -> bool:
        return self.created_date < dt
    def is_newer_than(self, dt: datetime.datetime) -> bool:
        return self.created_date > dt
    def to_json_read(self) -> str:
        return json.dumps(self.to_read_dict())


@dataclass(frozen=False)
class system_change_read_dto(base_read_dto, system_change_write_dto):
    id: int
    system_change_uid: str
    account_instance_uid: str
    change_type: str
    change_name: str
    change_json: str
    row_guid: str
    row_version: int
    is_active: int
    created_date: datetime.datetime
    created_by: str
    last_updated_date: datetime.datetime
    last_updated_by: str
    removed_date: datetime.datetime  | None
    removed_by: str  | None
    custom_attributes: str
    def __init__(self, id: int , system_change_uid: str , account_instance_uid: str , change_type: str , change_name: str , change_json: str , row_guid: str , row_version: int , is_active: int , created_date: datetime.datetime , created_by: str , last_updated_date: datetime.datetime , last_updated_by: str , removed_date: datetime.datetime  | None, removed_by: str  | None, custom_attributes: str ):
        self.id = id
        self.system_change_uid = system_change_uid
        self.account_instance_uid = account_instance_uid
        self.change_type = change_type
        self.change_name = change_name
        self.change_json = change_json
        self.row_guid = row_guid
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
    def new_read_default(cls, system_change_uid: str , account_instance_uid: str , change_type: str , change_name: str , change_json: str ):
        return cls(0, system_change_uid, account_instance_uid, change_type, change_name, change_json, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_full(cls, id: int , system_change_uid: str , account_instance_uid: str , change_type: str , change_name: str , change_json: str , row_guid: str , row_version: int , is_active: int , created_date: datetime.datetime , created_by: str , last_updated_date: datetime.datetime , last_updated_by: str , removed_date: datetime.datetime  | None, removed_by: str  | None, custom_attributes: str ):
        return cls(id, system_change_uid, account_instance_uid, change_type, change_name, change_json, row_guid, row_version, is_active, created_date, created_by, last_updated_date, last_updated_by, removed_date, removed_by, custom_attributes)
    @classmethod
    def from_write(cls, dto: system_change_write_dto):
        return cls(0, dto.system_change_uid, dto.account_instance_uid, dto.change_type, dto.change_name, dto.change_json, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, dto.custom_attributes)
    def clone_read(self):
        return system_change_read_dto(self.id, self.system_change_uid, self.account_instance_uid, self.change_type, self.change_name, self.change_json, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes)
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["id"], d["system_change_uid"], d["account_instance_uid"], d["change_type"], d["change_name"], d["change_json"], d["row_guid"], d["row_version"], d["is_active"], d["created_date"], d["created_by"], d["last_updated_date"], d["last_updated_by"], d["removed_date"], d["removed_by"], d["custom_attributes"])
    def to_read_dict(self) -> dict:
        return asdict(self)
    def to_write(self) -> system_change_write_dto:
        return system_change_write_dto(self.system_change_uid, self.account_instance_uid, self.change_type, self.change_name, self.change_json, self.custom_attributes)
    def to_thin(self) -> system_change_thin_dto:
        return system_change_thin_dto(self.system_change_uid, self.row_guid, self.is_active)
    def touch(self, updated_by: str = "system"):
        self.last_updated_date = datetime.datetime.now()
        self.last_updated_by = updated_by
        self.row_version = self.row_version+1
    def get_list_all_values(self) -> list[any]:
        return [self.id, self.system_change_uid, self.account_instance_uid, self.change_type, self.change_name, self.change_json, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]
    def get_list_update_values(self, updated_by: str) -> list[any]:
        return [self.account_instance_uid, self.change_type, self.change_name, self.change_json, self.custom_attributes, updated_by, self.system_change_uid]
    def is_older_than(self, dt: datetime.datetime) -> bool:
        return self.created_date < dt
    def is_newer_than(self, dt: datetime.datetime) -> bool:
        return self.created_date > dt
    def to_json_read(self) -> str:
        return json.dumps(self.to_read_dict())


@dataclass(frozen=False)
class system_exception_read_dto(base_read_dto, system_exception_write_dto):
    id: int
    system_exception_uid: str
    system_instance_uid: str
    exception_class: str
    exception_message: str
    exception_stacktrace: str
    row_guid: str
    row_version: int
    is_active: int
    created_date: datetime.datetime
    created_by: str
    last_updated_date: datetime.datetime
    last_updated_by: str
    removed_date: datetime.datetime  | None
    removed_by: str  | None
    custom_attributes: str
    def __init__(self, id: int , system_exception_uid: str , system_instance_uid: str , exception_class: str , exception_message: str , exception_stacktrace: str , row_guid: str , row_version: int , is_active: int , created_date: datetime.datetime , created_by: str , last_updated_date: datetime.datetime , last_updated_by: str , removed_date: datetime.datetime  | None, removed_by: str  | None, custom_attributes: str ):
        self.id = id
        self.system_exception_uid = system_exception_uid
        self.system_instance_uid = system_instance_uid
        self.exception_class = exception_class
        self.exception_message = exception_message
        self.exception_stacktrace = exception_stacktrace
        self.row_guid = row_guid
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
    def new_read_default(cls, system_exception_uid: str , system_instance_uid: str , exception_class: str , exception_message: str , exception_stacktrace: str ):
        return cls(0, system_exception_uid, system_instance_uid, exception_class, exception_message, exception_stacktrace, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_full(cls, id: int , system_exception_uid: str , system_instance_uid: str , exception_class: str , exception_message: str , exception_stacktrace: str , row_guid: str , row_version: int , is_active: int , created_date: datetime.datetime , created_by: str , last_updated_date: datetime.datetime , last_updated_by: str , removed_date: datetime.datetime  | None, removed_by: str  | None, custom_attributes: str ):
        return cls(id, system_exception_uid, system_instance_uid, exception_class, exception_message, exception_stacktrace, row_guid, row_version, is_active, created_date, created_by, last_updated_date, last_updated_by, removed_date, removed_by, custom_attributes)
    @classmethod
    def from_write(cls, dto: system_exception_write_dto):
        return cls(0, dto.system_exception_uid, dto.system_instance_uid, dto.exception_class, dto.exception_message, dto.exception_stacktrace, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, dto.custom_attributes)
    def clone_read(self):
        return system_exception_read_dto(self.id, self.system_exception_uid, self.system_instance_uid, self.exception_class, self.exception_message, self.exception_stacktrace, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes)
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["id"], d["system_exception_uid"], d["system_instance_uid"], d["exception_class"], d["exception_message"], d["exception_stacktrace"], d["row_guid"], d["row_version"], d["is_active"], d["created_date"], d["created_by"], d["last_updated_date"], d["last_updated_by"], d["removed_date"], d["removed_by"], d["custom_attributes"])
    def to_read_dict(self) -> dict:
        return asdict(self)
    def to_write(self) -> system_exception_write_dto:
        return system_exception_write_dto(self.system_exception_uid, self.system_instance_uid, self.exception_class, self.exception_message, self.exception_stacktrace, self.custom_attributes)
    def to_thin(self) -> system_exception_thin_dto:
        return system_exception_thin_dto(self.system_exception_uid, self.row_guid, self.is_active)
    def touch(self, updated_by: str = "system"):
        self.last_updated_date = datetime.datetime.now()
        self.last_updated_by = updated_by
        self.row_version = self.row_version+1
    def get_list_all_values(self) -> list[any]:
        return [self.id, self.system_exception_uid, self.system_instance_uid, self.exception_class, self.exception_message, self.exception_stacktrace, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]
    def get_list_update_values(self, updated_by: str) -> list[any]:
        return [self.system_instance_uid, self.exception_class, self.exception_message, self.exception_stacktrace, self.custom_attributes, updated_by, self.system_exception_uid]
    def is_older_than(self, dt: datetime.datetime) -> bool:
        return self.created_date < dt
    def is_newer_than(self, dt: datetime.datetime) -> bool:
        return self.created_date > dt
    def to_json_read(self) -> str:
        return json.dumps(self.to_read_dict())


@dataclass(frozen=False)
class system_instance_read_dto(base_read_dto, system_instance_write_dto):
    id: int
    system_instance_uid: str
    host_name: str
    host_ip: str
    local_path: str
    app_version: str
    mode_name: str
    row_guid: str
    row_version: int
    is_active: int
    created_date: datetime.datetime
    created_by: str
    last_updated_date: datetime.datetime
    last_updated_by: str
    removed_date: datetime.datetime  | None
    removed_by: str  | None
    custom_attributes: str
    def __init__(self, id: int , system_instance_uid: str , host_name: str , host_ip: str , local_path: str , app_version: str , mode_name: str , row_guid: str , row_version: int , is_active: int , created_date: datetime.datetime , created_by: str , last_updated_date: datetime.datetime , last_updated_by: str , removed_date: datetime.datetime  | None, removed_by: str  | None, custom_attributes: str ):
        self.id = id
        self.system_instance_uid = system_instance_uid
        self.host_name = host_name
        self.host_ip = host_ip
        self.local_path = local_path
        self.app_version = app_version
        self.mode_name = mode_name
        self.row_guid = row_guid
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
    def new_read_default(cls, system_instance_uid: str , host_name: str , host_ip: str , local_path: str , app_version: str , mode_name: str ):
        return cls(0, system_instance_uid, host_name, host_ip, local_path, app_version, mode_name, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_full(cls, id: int , system_instance_uid: str , host_name: str , host_ip: str , local_path: str , app_version: str , mode_name: str , row_guid: str , row_version: int , is_active: int , created_date: datetime.datetime , created_by: str , last_updated_date: datetime.datetime , last_updated_by: str , removed_date: datetime.datetime  | None, removed_by: str  | None, custom_attributes: str ):
        return cls(id, system_instance_uid, host_name, host_ip, local_path, app_version, mode_name, row_guid, row_version, is_active, created_date, created_by, last_updated_date, last_updated_by, removed_date, removed_by, custom_attributes)
    @classmethod
    def from_write(cls, dto: system_instance_write_dto):
        return cls(0, dto.system_instance_uid, dto.host_name, dto.host_ip, dto.local_path, dto.app_version, dto.mode_name, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, dto.custom_attributes)
    def clone_read(self):
        return system_instance_read_dto(self.id, self.system_instance_uid, self.host_name, self.host_ip, self.local_path, self.app_version, self.mode_name, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes)
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["id"], d["system_instance_uid"], d["host_name"], d["host_ip"], d["local_path"], d["app_version"], d["mode_name"], d["row_guid"], d["row_version"], d["is_active"], d["created_date"], d["created_by"], d["last_updated_date"], d["last_updated_by"], d["removed_date"], d["removed_by"], d["custom_attributes"])
    def to_read_dict(self) -> dict:
        return asdict(self)
    def to_write(self) -> system_instance_write_dto:
        return system_instance_write_dto(self.system_instance_uid, self.host_name, self.host_ip, self.local_path, self.app_version, self.mode_name, self.custom_attributes)
    def to_thin(self) -> system_instance_thin_dto:
        return system_instance_thin_dto(self.system_instance_uid, self.row_guid, self.is_active)
    def touch(self, updated_by: str = "system"):
        self.last_updated_date = datetime.datetime.now()
        self.last_updated_by = updated_by
        self.row_version = self.row_version+1
    def get_list_all_values(self) -> list[any]:
        return [self.id, self.system_instance_uid, self.host_name, self.host_ip, self.local_path, self.app_version, self.mode_name, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]
    def get_list_update_values(self, updated_by: str) -> list[any]:
        return [self.host_name, self.host_ip, self.local_path, self.app_version, self.mode_name, self.custom_attributes, updated_by, self.system_instance_uid]
    def is_older_than(self, dt: datetime.datetime) -> bool:
        return self.created_date < dt
    def is_newer_than(self, dt: datetime.datetime) -> bool:
        return self.created_date > dt
    def to_json_read(self) -> str:
        return json.dumps(self.to_read_dict())


@dataclass(frozen=False)
class system_object_read_dto(base_read_dto, system_object_write_dto):
    id: int
    system_object_uid: str
    object_name: str
    object_type: str
    table_name: str
    key_name: str
    parent_system_object_uid: str  | None
    row_guid: str
    row_version: int
    is_active: int
    created_date: datetime.datetime
    created_by: str
    last_updated_date: datetime.datetime
    last_updated_by: str
    removed_date: datetime.datetime  | None
    removed_by: str  | None
    custom_attributes: str
    def __init__(self, id: int , system_object_uid: str , object_name: str , object_type: str , table_name: str , key_name: str , parent_system_object_uid: str  | None, row_guid: str , row_version: int , is_active: int , created_date: datetime.datetime , created_by: str , last_updated_date: datetime.datetime , last_updated_by: str , removed_date: datetime.datetime  | None, removed_by: str  | None, custom_attributes: str ):
        self.id = id
        self.system_object_uid = system_object_uid
        self.object_name = object_name
        self.object_type = object_type
        self.table_name = table_name
        self.key_name = key_name
        self.parent_system_object_uid = parent_system_object_uid
        self.row_guid = row_guid
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
    def new_read_default(cls, system_object_uid: str , object_name: str , object_type: str , table_name: str , key_name: str , parent_system_object_uid: str  | None):
        return cls(0, system_object_uid, object_name, object_type, table_name, key_name, parent_system_object_uid, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_full(cls, id: int , system_object_uid: str , object_name: str , object_type: str , table_name: str , key_name: str , parent_system_object_uid: str  | None, row_guid: str , row_version: int , is_active: int , created_date: datetime.datetime , created_by: str , last_updated_date: datetime.datetime , last_updated_by: str , removed_date: datetime.datetime  | None, removed_by: str  | None, custom_attributes: str ):
        return cls(id, system_object_uid, object_name, object_type, table_name, key_name, parent_system_object_uid, row_guid, row_version, is_active, created_date, created_by, last_updated_date, last_updated_by, removed_date, removed_by, custom_attributes)
    @classmethod
    def from_write(cls, dto: system_object_write_dto):
        return cls(0, dto.system_object_uid, dto.object_name, dto.object_type, dto.table_name, dto.key_name, dto.parent_system_object_uid, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, dto.custom_attributes)
    def clone_read(self):
        return system_object_read_dto(self.id, self.system_object_uid, self.object_name, self.object_type, self.table_name, self.key_name, self.parent_system_object_uid, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes)
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["id"], d["system_object_uid"], d["object_name"], d["object_type"], d["table_name"], d["key_name"], d["parent_system_object_uid"], d["row_guid"], d["row_version"], d["is_active"], d["created_date"], d["created_by"], d["last_updated_date"], d["last_updated_by"], d["removed_date"], d["removed_by"], d["custom_attributes"])
    def to_read_dict(self) -> dict:
        return asdict(self)
    def to_write(self) -> system_object_write_dto:
        return system_object_write_dto(self.system_object_uid, self.object_name, self.object_type, self.table_name, self.key_name, self.parent_system_object_uid, self.custom_attributes)
    def to_thin(self) -> system_object_thin_dto:
        return system_object_thin_dto(self.system_object_uid, self.row_guid, self.is_active)
    def touch(self, updated_by: str = "system"):
        self.last_updated_date = datetime.datetime.now()
        self.last_updated_by = updated_by
        self.row_version = self.row_version+1
    def get_list_all_values(self) -> list[any]:
        return [self.id, self.system_object_uid, self.object_name, self.object_type, self.table_name, self.key_name, self.parent_system_object_uid, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]
    def get_list_update_values(self, updated_by: str) -> list[any]:
        return [self.object_name, self.object_type, self.table_name, self.key_name, self.parent_system_object_uid, self.custom_attributes, updated_by, self.system_object_uid]
    def is_older_than(self, dt: datetime.datetime) -> bool:
        return self.created_date < dt
    def is_newer_than(self, dt: datetime.datetime) -> bool:
        return self.created_date > dt
    def to_json_read(self) -> str:
        return json.dumps(self.to_read_dict())


@dataclass(frozen=False)
class system_setting_read_dto(base_read_dto, system_setting_write_dto):
    id: int
    system_setting_uid: str
    account_instance_uid: str  | None
    setting_name: str
    setting_value: str
    row_guid: str
    row_version: int
    is_active: int
    created_date: datetime.datetime
    created_by: str
    last_updated_date: datetime.datetime
    last_updated_by: str
    removed_date: datetime.datetime  | None
    removed_by: str  | None
    custom_attributes: str
    def __init__(self, id: int , system_setting_uid: str , account_instance_uid: str  | None, setting_name: str , setting_value: str , row_guid: str , row_version: int , is_active: int , created_date: datetime.datetime , created_by: str , last_updated_date: datetime.datetime , last_updated_by: str , removed_date: datetime.datetime  | None, removed_by: str  | None, custom_attributes: str ):
        self.id = id
        self.system_setting_uid = system_setting_uid
        self.account_instance_uid = account_instance_uid
        self.setting_name = setting_name
        self.setting_value = setting_value
        self.row_guid = row_guid
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
    def new_read_default(cls, system_setting_uid: str , account_instance_uid: str  | None, setting_name: str , setting_value: str ):
        return cls(0, system_setting_uid, account_instance_uid, setting_name, setting_value, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_full(cls, id: int , system_setting_uid: str , account_instance_uid: str  | None, setting_name: str , setting_value: str , row_guid: str , row_version: int , is_active: int , created_date: datetime.datetime , created_by: str , last_updated_date: datetime.datetime , last_updated_by: str , removed_date: datetime.datetime  | None, removed_by: str  | None, custom_attributes: str ):
        return cls(id, system_setting_uid, account_instance_uid, setting_name, setting_value, row_guid, row_version, is_active, created_date, created_by, last_updated_date, last_updated_by, removed_date, removed_by, custom_attributes)
    @classmethod
    def from_write(cls, dto: system_setting_write_dto):
        return cls(0, dto.system_setting_uid, dto.account_instance_uid, dto.setting_name, dto.setting_value, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, dto.custom_attributes)
    def clone_read(self):
        return system_setting_read_dto(self.id, self.system_setting_uid, self.account_instance_uid, self.setting_name, self.setting_value, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes)
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["id"], d["system_setting_uid"], d["account_instance_uid"], d["setting_name"], d["setting_value"], d["row_guid"], d["row_version"], d["is_active"], d["created_date"], d["created_by"], d["last_updated_date"], d["last_updated_by"], d["removed_date"], d["removed_by"], d["custom_attributes"])
    def to_read_dict(self) -> dict:
        return asdict(self)
    def to_write(self) -> system_setting_write_dto:
        return system_setting_write_dto(self.system_setting_uid, self.account_instance_uid, self.setting_name, self.setting_value, self.custom_attributes)
    def to_thin(self) -> system_setting_thin_dto:
        return system_setting_thin_dto(self.system_setting_uid, self.row_guid, self.is_active)
    def touch(self, updated_by: str = "system"):
        self.last_updated_date = datetime.datetime.now()
        self.last_updated_by = updated_by
        self.row_version = self.row_version+1
    def get_list_all_values(self) -> list[any]:
        return [self.id, self.system_setting_uid, self.account_instance_uid, self.setting_name, self.setting_value, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]
    def get_list_update_values(self, updated_by: str) -> list[any]:
        return [self.account_instance_uid, self.setting_name, self.setting_value, self.custom_attributes, updated_by, self.system_setting_uid]
    def is_older_than(self, dt: datetime.datetime) -> bool:
        return self.created_date < dt
    def is_newer_than(self, dt: datetime.datetime) -> bool:
        return self.created_date > dt
    def to_json_read(self) -> str:
        return json.dumps(self.to_read_dict())


@dataclass(frozen=False)
class system_state_read_dto(base_read_dto, system_state_write_dto):
    id: int
    system_state_uid: str
    system_instance_uid: str
    host_name: str
    host_ip: str
    local_path: str
    app_version: str
    mode_name: str
    row_guid: str
    row_version: int
    is_active: int
    created_date: datetime.datetime
    created_by: str
    last_updated_date: datetime.datetime
    last_updated_by: str
    removed_date: datetime.datetime  | None
    removed_by: str  | None
    custom_attributes: str
    def __init__(self, id: int , system_state_uid: str , system_instance_uid: str , host_name: str , host_ip: str , local_path: str , app_version: str , mode_name: str , row_guid: str , row_version: int , is_active: int , created_date: datetime.datetime , created_by: str , last_updated_date: datetime.datetime , last_updated_by: str , removed_date: datetime.datetime  | None, removed_by: str  | None, custom_attributes: str ):
        self.id = id
        self.system_state_uid = system_state_uid
        self.system_instance_uid = system_instance_uid
        self.host_name = host_name
        self.host_ip = host_ip
        self.local_path = local_path
        self.app_version = app_version
        self.mode_name = mode_name
        self.row_guid = row_guid
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
    def new_read_default(cls, system_state_uid: str , system_instance_uid: str , host_name: str , host_ip: str , local_path: str , app_version: str , mode_name: str ):
        return cls(0, system_state_uid, system_instance_uid, host_name, host_ip, local_path, app_version, mode_name, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")
    @classmethod
    def new_read_full(cls, id: int , system_state_uid: str , system_instance_uid: str , host_name: str , host_ip: str , local_path: str , app_version: str , mode_name: str , row_guid: str , row_version: int , is_active: int , created_date: datetime.datetime , created_by: str , last_updated_date: datetime.datetime , last_updated_by: str , removed_date: datetime.datetime  | None, removed_by: str  | None, custom_attributes: str ):
        return cls(id, system_state_uid, system_instance_uid, host_name, host_ip, local_path, app_version, mode_name, row_guid, row_version, is_active, created_date, created_by, last_updated_date, last_updated_by, removed_date, removed_by, custom_attributes)
    @classmethod
    def from_write(cls, dto: system_state_write_dto):
        return cls(0, dto.system_state_uid, dto.system_instance_uid, dto.host_name, dto.host_ip, dto.local_path, dto.app_version, dto.mode_name, "", 0, 1, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, dto.custom_attributes)
    def clone_read(self):
        return system_state_read_dto(self.id, self.system_state_uid, self.system_instance_uid, self.host_name, self.host_ip, self.local_path, self.app_version, self.mode_name, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes)
    @classmethod
    def from_dictionary(cls, d: dict[str, any]):
        return cls(d["id"], d["system_state_uid"], d["system_instance_uid"], d["host_name"], d["host_ip"], d["local_path"], d["app_version"], d["mode_name"], d["row_guid"], d["row_version"], d["is_active"], d["created_date"], d["created_by"], d["last_updated_date"], d["last_updated_by"], d["removed_date"], d["removed_by"], d["custom_attributes"])
    def to_read_dict(self) -> dict:
        return asdict(self)
    def to_write(self) -> system_state_write_dto:
        return system_state_write_dto(self.system_state_uid, self.system_instance_uid, self.host_name, self.host_ip, self.local_path, self.app_version, self.mode_name, self.custom_attributes)
    def to_thin(self) -> system_state_thin_dto:
        return system_state_thin_dto(self.system_state_uid, self.row_guid, self.is_active)
    def touch(self, updated_by: str = "system"):
        self.last_updated_date = datetime.datetime.now()
        self.last_updated_by = updated_by
        self.row_version = self.row_version+1
    def get_list_all_values(self) -> list[any]:
        return [self.id, self.system_state_uid, self.system_instance_uid, self.host_name, self.host_ip, self.local_path, self.app_version, self.mode_name, self.row_guid, self.row_version, self.is_active, self.created_date, self.created_by, self.last_updated_date, self.last_updated_by, self.removed_date, self.removed_by, self.custom_attributes]
    def get_list_update_values(self, updated_by: str) -> list[any]:
        return [self.system_instance_uid, self.host_name, self.host_ip, self.local_path, self.app_version, self.mode_name, self.custom_attributes, updated_by, self.system_state_uid]
    def is_older_than(self, dt: datetime.datetime) -> bool:
        return self.created_date < dt
    def is_newer_than(self, dt: datetime.datetime) -> bool:
        return self.created_date > dt
    def to_json_read(self) -> str:
        return json.dumps(self.to_read_dict())

