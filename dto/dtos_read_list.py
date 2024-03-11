import datetime
from datetime import datetime
from abc import abstractmethod
from dataclasses import dataclass
from dto.dtos import *
from dto.dtos_read import *
from dto.dtos_write import *


@dataclass(frozen=False)
class account_division_read_dtos(base_dtos):
    dtos: list[account_division_read_dto]
    def __init__(self, dtos: list[account_division_read_dto]):
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[account_division_read_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: account_division_read_dto):
        return cls(list(dto))
    @classmethod
    def from_lists(cls, dtos1: list[account_division_read_dto], dtos2: list[account_division_read_dto]):
        return cls(dtos1 + dtos2)
    def get_active(self):
        return account_division_read_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return account_division_read_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_write_dtos(self) -> list[account_division_write_dto]:
        return list(filter(lambda x: x.to_write() != 1, self.dtos))
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write().to_write_dict(), self.dtos))
    def get_read_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> account_division_read_dto | None:
        found_dtos = list(filter(lambda x: x.account_division_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def get_first(self) -> account_division_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None


@dataclass(frozen=False)
class account_group_read_dtos(base_dtos):
    dtos: list[account_group_read_dto]
    def __init__(self, dtos: list[account_group_read_dto]):
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[account_group_read_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: account_group_read_dto):
        return cls(list(dto))
    @classmethod
    def from_lists(cls, dtos1: list[account_group_read_dto], dtos2: list[account_group_read_dto]):
        return cls(dtos1 + dtos2)
    def get_active(self):
        return account_group_read_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return account_group_read_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_write_dtos(self) -> list[account_group_write_dto]:
        return list(filter(lambda x: x.to_write() != 1, self.dtos))
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write().to_write_dict(), self.dtos))
    def get_read_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> account_group_read_dto | None:
        found_dtos = list(filter(lambda x: x.account_group_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def get_first(self) -> account_group_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None


@dataclass(frozen=False)
class account_instance_read_dtos(base_dtos):
    dtos: list[account_instance_read_dto]
    def __init__(self, dtos: list[account_instance_read_dto]):
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[account_instance_read_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: account_instance_read_dto):
        return cls(list(dto))
    @classmethod
    def from_lists(cls, dtos1: list[account_instance_read_dto], dtos2: list[account_instance_read_dto]):
        return cls(dtos1 + dtos2)
    def get_active(self):
        return account_instance_read_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return account_instance_read_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_write_dtos(self) -> list[account_instance_write_dto]:
        return list(filter(lambda x: x.to_write() != 1, self.dtos))
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write().to_write_dict(), self.dtos))
    def get_read_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> account_instance_read_dto | None:
        found_dtos = list(filter(lambda x: x.account_instance_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def get_first(self) -> account_instance_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None


@dataclass(frozen=False)
class account_title_read_dtos(base_dtos):
    dtos: list[account_title_read_dto]
    def __init__(self, dtos: list[account_title_read_dto]):
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[account_title_read_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: account_title_read_dto):
        return cls(list(dto))
    @classmethod
    def from_lists(cls, dtos1: list[account_title_read_dto], dtos2: list[account_title_read_dto]):
        return cls(dtos1 + dtos2)
    def get_active(self):
        return account_title_read_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return account_title_read_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_write_dtos(self) -> list[account_title_write_dto]:
        return list(filter(lambda x: x.to_write() != 1, self.dtos))
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write().to_write_dict(), self.dtos))
    def get_read_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> account_title_read_dto | None:
        found_dtos = list(filter(lambda x: x.account_title_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def get_first(self) -> account_title_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None


@dataclass(frozen=False)
class auth_identity_read_dtos(base_dtos):
    dtos: list[auth_identity_read_dto]
    def __init__(self, dtos: list[auth_identity_read_dto]):
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[auth_identity_read_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: auth_identity_read_dto):
        return cls(list(dto))
    @classmethod
    def from_lists(cls, dtos1: list[auth_identity_read_dto], dtos2: list[auth_identity_read_dto]):
        return cls(dtos1 + dtos2)
    def get_active(self):
        return auth_identity_read_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return auth_identity_read_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_write_dtos(self) -> list[auth_identity_write_dto]:
        return list(filter(lambda x: x.to_write() != 1, self.dtos))
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write().to_write_dict(), self.dtos))
    def get_read_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> auth_identity_read_dto | None:
        found_dtos = list(filter(lambda x: x.auth_identity_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def get_first(self) -> auth_identity_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None


@dataclass(frozen=False)
class auth_password_read_dtos(base_dtos):
    dtos: list[auth_password_read_dto]
    def __init__(self, dtos: list[auth_password_read_dto]):
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[auth_password_read_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: auth_password_read_dto):
        return cls(list(dto))
    @classmethod
    def from_lists(cls, dtos1: list[auth_password_read_dto], dtos2: list[auth_password_read_dto]):
        return cls(dtos1 + dtos2)
    def get_active(self):
        return auth_password_read_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return auth_password_read_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_write_dtos(self) -> list[auth_password_write_dto]:
        return list(filter(lambda x: x.to_write() != 1, self.dtos))
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write().to_write_dict(), self.dtos))
    def get_read_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> auth_password_read_dto | None:
        found_dtos = list(filter(lambda x: x.auth_password_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def get_first(self) -> auth_password_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None


@dataclass(frozen=False)
class auth_permission_read_dtos(base_dtos):
    dtos: list[auth_permission_read_dto]
    def __init__(self, dtos: list[auth_permission_read_dto]):
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[auth_permission_read_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: auth_permission_read_dto):
        return cls(list(dto))
    @classmethod
    def from_lists(cls, dtos1: list[auth_permission_read_dto], dtos2: list[auth_permission_read_dto]):
        return cls(dtos1 + dtos2)
    def get_active(self):
        return auth_permission_read_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return auth_permission_read_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_write_dtos(self) -> list[auth_permission_write_dto]:
        return list(filter(lambda x: x.to_write() != 1, self.dtos))
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write().to_write_dict(), self.dtos))
    def get_read_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> auth_permission_read_dto | None:
        found_dtos = list(filter(lambda x: x.auth_permission_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def get_first(self) -> auth_permission_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None


@dataclass(frozen=False)
class auth_request_read_dtos(base_dtos):
    dtos: list[auth_request_read_dto]
    def __init__(self, dtos: list[auth_request_read_dto]):
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[auth_request_read_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: auth_request_read_dto):
        return cls(list(dto))
    @classmethod
    def from_lists(cls, dtos1: list[auth_request_read_dto], dtos2: list[auth_request_read_dto]):
        return cls(dtos1 + dtos2)
    def get_active(self):
        return auth_request_read_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return auth_request_read_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_write_dtos(self) -> list[auth_request_write_dto]:
        return list(filter(lambda x: x.to_write() != 1, self.dtos))
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write().to_write_dict(), self.dtos))
    def get_read_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> auth_request_read_dto | None:
        found_dtos = list(filter(lambda x: x.auth_request_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def get_first(self) -> auth_request_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None


@dataclass(frozen=False)
class auth_role_read_dtos(base_dtos):
    dtos: list[auth_role_read_dto]
    def __init__(self, dtos: list[auth_role_read_dto]):
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[auth_role_read_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: auth_role_read_dto):
        return cls(list(dto))
    @classmethod
    def from_lists(cls, dtos1: list[auth_role_read_dto], dtos2: list[auth_role_read_dto]):
        return cls(dtos1 + dtos2)
    def get_active(self):
        return auth_role_read_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return auth_role_read_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_write_dtos(self) -> list[auth_role_write_dto]:
        return list(filter(lambda x: x.to_write() != 1, self.dtos))
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write().to_write_dict(), self.dtos))
    def get_read_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> auth_role_read_dto | None:
        found_dtos = list(filter(lambda x: x.auth_role_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def get_first(self) -> auth_role_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None


@dataclass(frozen=False)
class auth_token_read_dtos(base_dtos):
    dtos: list[auth_token_read_dto]
    def __init__(self, dtos: list[auth_token_read_dto]):
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[auth_token_read_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: auth_token_read_dto):
        return cls(list(dto))
    @classmethod
    def from_lists(cls, dtos1: list[auth_token_read_dto], dtos2: list[auth_token_read_dto]):
        return cls(dtos1 + dtos2)
    def get_active(self):
        return auth_token_read_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return auth_token_read_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_write_dtos(self) -> list[auth_token_write_dto]:
        return list(filter(lambda x: x.to_write() != 1, self.dtos))
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write().to_write_dict(), self.dtos))
    def get_read_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> auth_token_read_dto | None:
        found_dtos = list(filter(lambda x: x.auth_token_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def get_first(self) -> auth_token_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None


@dataclass(frozen=False)
class client_instance_read_dtos(base_dtos):
    dtos: list[client_instance_read_dto]
    def __init__(self, dtos: list[client_instance_read_dto]):
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[client_instance_read_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: client_instance_read_dto):
        return cls(list(dto))
    @classmethod
    def from_lists(cls, dtos1: list[client_instance_read_dto], dtos2: list[client_instance_read_dto]):
        return cls(dtos1 + dtos2)
    def get_active(self):
        return client_instance_read_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return client_instance_read_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_write_dtos(self) -> list[client_instance_write_dto]:
        return list(filter(lambda x: x.to_write() != 1, self.dtos))
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write().to_write_dict(), self.dtos))
    def get_read_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> client_instance_read_dto | None:
        found_dtos = list(filter(lambda x: x.client_instance_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def get_first(self) -> client_instance_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None


@dataclass(frozen=False)
class country_read_dtos(base_dtos):
    dtos: list[country_read_dto]
    def __init__(self, dtos: list[country_read_dto]):
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[country_read_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: country_read_dto):
        return cls(list(dto))
    @classmethod
    def from_lists(cls, dtos1: list[country_read_dto], dtos2: list[country_read_dto]):
        return cls(dtos1 + dtos2)
    def get_active(self):
        return country_read_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return country_read_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_write_dtos(self) -> list[country_write_dto]:
        return list(filter(lambda x: x.to_write() != 1, self.dtos))
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write().to_write_dict(), self.dtos))
    def get_read_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> country_read_dto | None:
        found_dtos = list(filter(lambda x: x.country_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def get_first(self) -> country_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None


@dataclass(frozen=False)
class currency_read_dtos(base_dtos):
    dtos: list[currency_read_dto]
    def __init__(self, dtos: list[currency_read_dto]):
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[currency_read_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: currency_read_dto):
        return cls(list(dto))
    @classmethod
    def from_lists(cls, dtos1: list[currency_read_dto], dtos2: list[currency_read_dto]):
        return cls(dtos1 + dtos2)
    def get_active(self):
        return currency_read_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return currency_read_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_write_dtos(self) -> list[currency_write_dto]:
        return list(filter(lambda x: x.to_write() != 1, self.dtos))
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write().to_write_dict(), self.dtos))
    def get_read_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> currency_read_dto | None:
        found_dtos = list(filter(lambda x: x.currency_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def get_first(self) -> currency_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None


@dataclass(frozen=False)
class entry_final_read_dtos(base_dtos):
    dtos: list[entry_final_read_dto]
    def __init__(self, dtos: list[entry_final_read_dto]):
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[entry_final_read_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: entry_final_read_dto):
        return cls(list(dto))
    @classmethod
    def from_lists(cls, dtos1: list[entry_final_read_dto], dtos2: list[entry_final_read_dto]):
        return cls(dtos1 + dtos2)
    def get_active(self):
        return entry_final_read_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return entry_final_read_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_write_dtos(self) -> list[entry_final_write_dto]:
        return list(filter(lambda x: x.to_write() != 1, self.dtos))
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write().to_write_dict(), self.dtos))
    def get_read_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> entry_final_read_dto | None:
        found_dtos = list(filter(lambda x: x.entry_final_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def get_first(self) -> entry_final_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None


@dataclass(frozen=False)
class entry_save_read_dtos(base_dtos):
    dtos: list[entry_save_read_dto]
    def __init__(self, dtos: list[entry_save_read_dto]):
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[entry_save_read_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: entry_save_read_dto):
        return cls(list(dto))
    @classmethod
    def from_lists(cls, dtos1: list[entry_save_read_dto], dtos2: list[entry_save_read_dto]):
        return cls(dtos1 + dtos2)
    def get_active(self):
        return entry_save_read_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return entry_save_read_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_write_dtos(self) -> list[entry_save_write_dto]:
        return list(filter(lambda x: x.to_write() != 1, self.dtos))
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write().to_write_dict(), self.dtos))
    def get_read_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> entry_save_read_dto | None:
        found_dtos = list(filter(lambda x: x.entry_save_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def get_first(self) -> entry_save_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None


@dataclass(frozen=False)
class event_channel_read_dtos(base_dtos):
    dtos: list[event_channel_read_dto]
    def __init__(self, dtos: list[event_channel_read_dto]):
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[event_channel_read_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: event_channel_read_dto):
        return cls(list(dto))
    @classmethod
    def from_lists(cls, dtos1: list[event_channel_read_dto], dtos2: list[event_channel_read_dto]):
        return cls(dtos1 + dtos2)
    def get_active(self):
        return event_channel_read_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return event_channel_read_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_write_dtos(self) -> list[event_channel_write_dto]:
        return list(filter(lambda x: x.to_write() != 1, self.dtos))
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write().to_write_dict(), self.dtos))
    def get_read_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> event_channel_read_dto | None:
        found_dtos = list(filter(lambda x: x.event_channel_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def get_first(self) -> event_channel_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None


@dataclass(frozen=False)
class event_instance_read_dtos(base_dtos):
    dtos: list[event_instance_read_dto]
    def __init__(self, dtos: list[event_instance_read_dto]):
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[event_instance_read_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: event_instance_read_dto):
        return cls(list(dto))
    @classmethod
    def from_lists(cls, dtos1: list[event_instance_read_dto], dtos2: list[event_instance_read_dto]):
        return cls(dtos1 + dtos2)
    def get_active(self):
        return event_instance_read_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return event_instance_read_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_write_dtos(self) -> list[event_instance_write_dto]:
        return list(filter(lambda x: x.to_write() != 1, self.dtos))
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write().to_write_dict(), self.dtos))
    def get_read_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> event_instance_read_dto | None:
        found_dtos = list(filter(lambda x: x.event_instance_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def get_first(self) -> event_instance_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None


@dataclass(frozen=False)
class event_subscription_read_dtos(base_dtos):
    dtos: list[event_subscription_read_dto]
    def __init__(self, dtos: list[event_subscription_read_dto]):
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[event_subscription_read_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: event_subscription_read_dto):
        return cls(list(dto))
    @classmethod
    def from_lists(cls, dtos1: list[event_subscription_read_dto], dtos2: list[event_subscription_read_dto]):
        return cls(dtos1 + dtos2)
    def get_active(self):
        return event_subscription_read_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return event_subscription_read_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_write_dtos(self) -> list[event_subscription_write_dto]:
        return list(filter(lambda x: x.to_write() != 1, self.dtos))
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write().to_write_dict(), self.dtos))
    def get_read_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> event_subscription_read_dto | None:
        found_dtos = list(filter(lambda x: x.event_subscription_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def get_first(self) -> event_subscription_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None


@dataclass(frozen=False)
class invoice_instance_read_dtos(base_dtos):
    dtos: list[invoice_instance_read_dto]
    def __init__(self, dtos: list[invoice_instance_read_dto]):
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[invoice_instance_read_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: invoice_instance_read_dto):
        return cls(list(dto))
    @classmethod
    def from_lists(cls, dtos1: list[invoice_instance_read_dto], dtos2: list[invoice_instance_read_dto]):
        return cls(dtos1 + dtos2)
    def get_active(self):
        return invoice_instance_read_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return invoice_instance_read_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_write_dtos(self) -> list[invoice_instance_write_dto]:
        return list(filter(lambda x: x.to_write() != 1, self.dtos))
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write().to_write_dict(), self.dtos))
    def get_read_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> invoice_instance_read_dto | None:
        found_dtos = list(filter(lambda x: x.invoice_instance_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def get_first(self) -> invoice_instance_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None


@dataclass(frozen=False)
class notification_instance_read_dtos(base_dtos):
    dtos: list[notification_instance_read_dto]
    def __init__(self, dtos: list[notification_instance_read_dto]):
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[notification_instance_read_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: notification_instance_read_dto):
        return cls(list(dto))
    @classmethod
    def from_lists(cls, dtos1: list[notification_instance_read_dto], dtos2: list[notification_instance_read_dto]):
        return cls(dtos1 + dtos2)
    def get_active(self):
        return notification_instance_read_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return notification_instance_read_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_write_dtos(self) -> list[notification_instance_write_dto]:
        return list(filter(lambda x: x.to_write() != 1, self.dtos))
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write().to_write_dict(), self.dtos))
    def get_read_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> notification_instance_read_dto | None:
        found_dtos = list(filter(lambda x: x.notification_instance_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def get_first(self) -> notification_instance_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None


@dataclass(frozen=False)
class project_budget_read_dtos(base_dtos):
    dtos: list[project_budget_read_dto]
    def __init__(self, dtos: list[project_budget_read_dto]):
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[project_budget_read_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: project_budget_read_dto):
        return cls(list(dto))
    @classmethod
    def from_lists(cls, dtos1: list[project_budget_read_dto], dtos2: list[project_budget_read_dto]):
        return cls(dtos1 + dtos2)
    def get_active(self):
        return project_budget_read_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return project_budget_read_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_write_dtos(self) -> list[project_budget_write_dto]:
        return list(filter(lambda x: x.to_write() != 1, self.dtos))
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write().to_write_dict(), self.dtos))
    def get_read_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> project_budget_read_dto | None:
        found_dtos = list(filter(lambda x: x.project_budget_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def get_first(self) -> project_budget_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None


@dataclass(frozen=False)
class project_group_read_dtos(base_dtos):
    dtos: list[project_group_read_dto]
    def __init__(self, dtos: list[project_group_read_dto]):
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[project_group_read_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: project_group_read_dto):
        return cls(list(dto))
    @classmethod
    def from_lists(cls, dtos1: list[project_group_read_dto], dtos2: list[project_group_read_dto]):
        return cls(dtos1 + dtos2)
    def get_active(self):
        return project_group_read_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return project_group_read_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_write_dtos(self) -> list[project_group_write_dto]:
        return list(filter(lambda x: x.to_write() != 1, self.dtos))
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write().to_write_dict(), self.dtos))
    def get_read_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> project_group_read_dto | None:
        found_dtos = list(filter(lambda x: x.project_group_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def get_first(self) -> project_group_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None


@dataclass(frozen=False)
class project_instance_read_dtos(base_dtos):
    dtos: list[project_instance_read_dto]
    def __init__(self, dtos: list[project_instance_read_dto]):
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[project_instance_read_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: project_instance_read_dto):
        return cls(list(dto))
    @classmethod
    def from_lists(cls, dtos1: list[project_instance_read_dto], dtos2: list[project_instance_read_dto]):
        return cls(dtos1 + dtos2)
    def get_active(self):
        return project_instance_read_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return project_instance_read_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_write_dtos(self) -> list[project_instance_write_dto]:
        return list(filter(lambda x: x.to_write() != 1, self.dtos))
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write().to_write_dict(), self.dtos))
    def get_read_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> project_instance_read_dto | None:
        found_dtos = list(filter(lambda x: x.project_instance_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def get_first(self) -> project_instance_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None


@dataclass(frozen=False)
class project_milestone_read_dtos(base_dtos):
    dtos: list[project_milestone_read_dto]
    def __init__(self, dtos: list[project_milestone_read_dto]):
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[project_milestone_read_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: project_milestone_read_dto):
        return cls(list(dto))
    @classmethod
    def from_lists(cls, dtos1: list[project_milestone_read_dto], dtos2: list[project_milestone_read_dto]):
        return cls(dtos1 + dtos2)
    def get_active(self):
        return project_milestone_read_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return project_milestone_read_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_write_dtos(self) -> list[project_milestone_write_dto]:
        return list(filter(lambda x: x.to_write() != 1, self.dtos))
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write().to_write_dict(), self.dtos))
    def get_read_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> project_milestone_read_dto | None:
        found_dtos = list(filter(lambda x: x.project_milestone_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def get_first(self) -> project_milestone_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None


@dataclass(frozen=False)
class system_attribute_read_dtos(base_dtos):
    dtos: list[system_attribute_read_dto]
    def __init__(self, dtos: list[system_attribute_read_dto]):
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[system_attribute_read_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: system_attribute_read_dto):
        return cls(list(dto))
    @classmethod
    def from_lists(cls, dtos1: list[system_attribute_read_dto], dtos2: list[system_attribute_read_dto]):
        return cls(dtos1 + dtos2)
    def get_active(self):
        return system_attribute_read_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return system_attribute_read_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_write_dtos(self) -> list[system_attribute_write_dto]:
        return list(filter(lambda x: x.to_write() != 1, self.dtos))
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write().to_write_dict(), self.dtos))
    def get_read_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> system_attribute_read_dto | None:
        found_dtos = list(filter(lambda x: x.system_attribute_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def get_first(self) -> system_attribute_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None


@dataclass(frozen=False)
class system_change_read_dtos(base_dtos):
    dtos: list[system_change_read_dto]
    def __init__(self, dtos: list[system_change_read_dto]):
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[system_change_read_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: system_change_read_dto):
        return cls(list(dto))
    @classmethod
    def from_lists(cls, dtos1: list[system_change_read_dto], dtos2: list[system_change_read_dto]):
        return cls(dtos1 + dtos2)
    def get_active(self):
        return system_change_read_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return system_change_read_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_write_dtos(self) -> list[system_change_write_dto]:
        return list(filter(lambda x: x.to_write() != 1, self.dtos))
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write().to_write_dict(), self.dtos))
    def get_read_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> system_change_read_dto | None:
        found_dtos = list(filter(lambda x: x.system_change_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def get_first(self) -> system_change_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None


@dataclass(frozen=False)
class system_exception_read_dtos(base_dtos):
    dtos: list[system_exception_read_dto]
    def __init__(self, dtos: list[system_exception_read_dto]):
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[system_exception_read_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: system_exception_read_dto):
        return cls(list(dto))
    @classmethod
    def from_lists(cls, dtos1: list[system_exception_read_dto], dtos2: list[system_exception_read_dto]):
        return cls(dtos1 + dtos2)
    def get_active(self):
        return system_exception_read_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return system_exception_read_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_write_dtos(self) -> list[system_exception_write_dto]:
        return list(filter(lambda x: x.to_write() != 1, self.dtos))
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write().to_write_dict(), self.dtos))
    def get_read_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> system_exception_read_dto | None:
        found_dtos = list(filter(lambda x: x.system_exception_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def get_first(self) -> system_exception_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None


@dataclass(frozen=False)
class system_instance_read_dtos(base_dtos):
    dtos: list[system_instance_read_dto]
    def __init__(self, dtos: list[system_instance_read_dto]):
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[system_instance_read_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: system_instance_read_dto):
        return cls(list(dto))
    @classmethod
    def from_lists(cls, dtos1: list[system_instance_read_dto], dtos2: list[system_instance_read_dto]):
        return cls(dtos1 + dtos2)
    def get_active(self):
        return system_instance_read_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return system_instance_read_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_write_dtos(self) -> list[system_instance_write_dto]:
        return list(filter(lambda x: x.to_write() != 1, self.dtos))
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write().to_write_dict(), self.dtos))
    def get_read_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> system_instance_read_dto | None:
        found_dtos = list(filter(lambda x: x.system_instance_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def get_first(self) -> system_instance_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None


@dataclass(frozen=False)
class system_object_read_dtos(base_dtos):
    dtos: list[system_object_read_dto]
    def __init__(self, dtos: list[system_object_read_dto]):
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[system_object_read_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: system_object_read_dto):
        return cls(list(dto))
    @classmethod
    def from_lists(cls, dtos1: list[system_object_read_dto], dtos2: list[system_object_read_dto]):
        return cls(dtos1 + dtos2)
    def get_active(self):
        return system_object_read_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return system_object_read_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_write_dtos(self) -> list[system_object_write_dto]:
        return list(filter(lambda x: x.to_write() != 1, self.dtos))
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write().to_write_dict(), self.dtos))
    def get_read_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> system_object_read_dto | None:
        found_dtos = list(filter(lambda x: x.system_object_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def get_first(self) -> system_object_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None


@dataclass(frozen=False)
class system_setting_read_dtos(base_dtos):
    dtos: list[system_setting_read_dto]
    def __init__(self, dtos: list[system_setting_read_dto]):
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[system_setting_read_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: system_setting_read_dto):
        return cls(list(dto))
    @classmethod
    def from_lists(cls, dtos1: list[system_setting_read_dto], dtos2: list[system_setting_read_dto]):
        return cls(dtos1 + dtos2)
    def get_active(self):
        return system_setting_read_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return system_setting_read_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_write_dtos(self) -> list[system_setting_write_dto]:
        return list(filter(lambda x: x.to_write() != 1, self.dtos))
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write().to_write_dict(), self.dtos))
    def get_read_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> system_setting_read_dto | None:
        found_dtos = list(filter(lambda x: x.system_setting_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def get_first(self) -> system_setting_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None


@dataclass(frozen=False)
class system_state_read_dtos(base_dtos):
    dtos: list[system_state_read_dto]
    def __init__(self, dtos: list[system_state_read_dto]):
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[system_state_read_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: system_state_read_dto):
        return cls(list(dto))
    @classmethod
    def from_lists(cls, dtos1: list[system_state_read_dto], dtos2: list[system_state_read_dto]):
        return cls(dtos1 + dtos2)
    def get_active(self):
        return system_state_read_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return system_state_read_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_write_dtos(self) -> list[system_state_write_dto]:
        return list(filter(lambda x: x.to_write() != 1, self.dtos))
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write().to_write_dict(), self.dtos))
    def get_read_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> system_state_read_dto | None:
        found_dtos = list(filter(lambda x: x.system_state_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def get_first(self) -> system_state_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None



