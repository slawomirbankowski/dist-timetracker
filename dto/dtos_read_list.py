from __future__ import annotations
import datetime
from datetime import datetime
from abc import abstractmethod
from dataclasses import dataclass
from dto.dtos import *
from dto.dtos_read import *
from dto.dtos_write import *
from typing import Dict, Callable

# auto-generated - DtosRead - START

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
        return cls(list([dto]))
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
    def to_dict_by_uid(self) -> dict[str, account_division_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def to_dict_by_account_division_uid(self) -> dict[str, account_division_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.account_division_uid] = dto
        return d
    def to_dict_by_system_version_uid(self) -> dict[str, account_division_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.system_version_uid] = dto
        return d
    def to_dict_by_division_name(self) -> dict[str, account_division_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.division_name] = dto
        return d
    def to_dict_by_division_description(self) -> dict[str, account_division_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.division_description] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_all(self, check_method: Callable[[account_division_read_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def for_any(self, check_method: Callable[[account_division_read_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[account_division_read_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[account_division_read_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[account_division_read_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, account_division_read_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, account_division_read_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, account_division_read_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[account_division_read_dto], bool]) -> account_division_read_dtos:
        return account_division_read_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[account_division_read_dto], str]) -> dict[str, account_division_read_dtos]:
        grp_data: dict[str, account_division_read_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = account_division_read_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[account_division_read_dto], str], agg_method: Callable[[account_division_read_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, account_division_read_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res


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
        return cls(list([dto]))
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
    def to_dict_by_uid(self) -> dict[str, account_group_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def to_dict_by_account_group_uid(self) -> dict[str, account_group_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.account_group_uid] = dto
        return d
    def to_dict_by_system_version_uid(self) -> dict[str, account_group_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.system_version_uid] = dto
        return d
    def to_dict_by_account_group_name(self) -> dict[str, account_group_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.account_group_name] = dto
        return d
    def to_dict_by_account_group_description(self) -> dict[str, account_group_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.account_group_description] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_all(self, check_method: Callable[[account_group_read_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def for_any(self, check_method: Callable[[account_group_read_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[account_group_read_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[account_group_read_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[account_group_read_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, account_group_read_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, account_group_read_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, account_group_read_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[account_group_read_dto], bool]) -> account_group_read_dtos:
        return account_group_read_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[account_group_read_dto], str]) -> dict[str, account_group_read_dtos]:
        grp_data: dict[str, account_group_read_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = account_group_read_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[account_group_read_dto], str], agg_method: Callable[[account_group_read_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, account_group_read_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res


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
        return cls(list([dto]))
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
    def to_dict_by_uid(self) -> dict[str, account_instance_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def to_dict_by_account_instance_uid(self) -> dict[str, account_instance_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.account_instance_uid] = dto
        return d
    def to_dict_by_client_instance_uid(self) -> dict[str, account_instance_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.client_instance_uid] = dto
        return d
    def to_dict_by_account_type_uid(self) -> dict[str, account_instance_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.account_type_uid] = dto
        return d
    def to_dict_by_account_title_uid(self) -> dict[str, account_instance_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.account_title_uid] = dto
        return d
    def to_dict_by_account_division_uid(self) -> dict[str, account_instance_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.account_division_uid] = dto
        return d
    def to_dict_by_account_group_uid(self) -> dict[str, account_instance_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.account_group_uid] = dto
        return d
    def to_dict_by_auth_identity_uid(self) -> dict[str, account_instance_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.auth_identity_uid] = dto
        return d
    def to_dict_by_account_email(self) -> dict[str, account_instance_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.account_email] = dto
        return d
    def to_dict_by_account_name(self) -> dict[str, account_instance_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.account_name] = dto
        return d
    def to_dict_by_display_name(self) -> dict[str, account_instance_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.display_name] = dto
        return d
    def to_dict_by_is_system(self) -> dict[str, account_instance_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.is_system] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_all(self, check_method: Callable[[account_instance_read_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def for_any(self, check_method: Callable[[account_instance_read_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[account_instance_read_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[account_instance_read_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[account_instance_read_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, account_instance_read_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, account_instance_read_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, account_instance_read_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[account_instance_read_dto], bool]) -> account_instance_read_dtos:
        return account_instance_read_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[account_instance_read_dto], str]) -> dict[str, account_instance_read_dtos]:
        grp_data: dict[str, account_instance_read_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = account_instance_read_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[account_instance_read_dto], str], agg_method: Callable[[account_instance_read_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, account_instance_read_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res


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
        return cls(list([dto]))
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
    def to_dict_by_uid(self) -> dict[str, account_title_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def to_dict_by_account_title_uid(self) -> dict[str, account_title_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.account_title_uid] = dto
        return d
    def to_dict_by_system_version_uid(self) -> dict[str, account_title_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.system_version_uid] = dto
        return d
    def to_dict_by_title_name(self) -> dict[str, account_title_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.title_name] = dto
        return d
    def to_dict_by_title_description(self) -> dict[str, account_title_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.title_description] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_all(self, check_method: Callable[[account_title_read_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def for_any(self, check_method: Callable[[account_title_read_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[account_title_read_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[account_title_read_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[account_title_read_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, account_title_read_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, account_title_read_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, account_title_read_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[account_title_read_dto], bool]) -> account_title_read_dtos:
        return account_title_read_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[account_title_read_dto], str]) -> dict[str, account_title_read_dtos]:
        grp_data: dict[str, account_title_read_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = account_title_read_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[account_title_read_dto], str], agg_method: Callable[[account_title_read_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, account_title_read_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res


@dataclass(frozen=False)
class account_type_read_dtos(base_dtos):
    dtos: list[account_type_read_dto]
    def __init__(self, dtos: list[account_type_read_dto]):
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[account_type_read_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: account_type_read_dto):
        return cls(list([dto]))
    @classmethod
    def from_lists(cls, dtos1: list[account_type_read_dto], dtos2: list[account_type_read_dto]):
        return cls(dtos1 + dtos2)
    def get_active(self):
        return account_type_read_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return account_type_read_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_write_dtos(self) -> list[account_type_write_dto]:
        return list(filter(lambda x: x.to_write() != 1, self.dtos))
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write().to_write_dict(), self.dtos))
    def get_read_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> account_type_read_dto | None:
        found_dtos = list(filter(lambda x: x.account_type_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def get_first(self) -> account_type_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, account_type_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def to_dict_by_account_type_uid(self) -> dict[str, account_type_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.account_type_uid] = dto
        return d
    def to_dict_by_system_version_uid(self) -> dict[str, account_type_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.system_version_uid] = dto
        return d
    def to_dict_by_account_type_name(self) -> dict[str, account_type_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.account_type_name] = dto
        return d
    def to_dict_by_account_type_description(self) -> dict[str, account_type_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.account_type_description] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_all(self, check_method: Callable[[account_type_read_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def for_any(self, check_method: Callable[[account_type_read_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[account_type_read_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[account_type_read_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[account_type_read_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, account_type_read_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, account_type_read_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, account_type_read_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[account_type_read_dto], bool]) -> account_type_read_dtos:
        return account_type_read_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[account_type_read_dto], str]) -> dict[str, account_type_read_dtos]:
        grp_data: dict[str, account_type_read_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = account_type_read_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[account_type_read_dto], str], agg_method: Callable[[account_type_read_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, account_type_read_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res


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
        return cls(list([dto]))
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
    def to_dict_by_uid(self) -> dict[str, auth_identity_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def to_dict_by_auth_identity_uid(self) -> dict[str, auth_identity_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.auth_identity_uid] = dto
        return d
    def to_dict_by_client_instance_uid(self) -> dict[str, auth_identity_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.client_instance_uid] = dto
        return d
    def to_dict_by_identity_name(self) -> dict[str, auth_identity_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.identity_name] = dto
        return d
    def to_dict_by_identity_type(self) -> dict[str, auth_identity_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.identity_type] = dto
        return d
    def to_dict_by_identity_parameters(self) -> dict[str, auth_identity_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.identity_parameters] = dto
        return d
    def to_dict_by_last_status_name(self) -> dict[str, auth_identity_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.last_status_name] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_all(self, check_method: Callable[[auth_identity_read_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def for_any(self, check_method: Callable[[auth_identity_read_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[auth_identity_read_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[auth_identity_read_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[auth_identity_read_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, auth_identity_read_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, auth_identity_read_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, auth_identity_read_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[auth_identity_read_dto], bool]) -> auth_identity_read_dtos:
        return auth_identity_read_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[auth_identity_read_dto], str]) -> dict[str, auth_identity_read_dtos]:
        grp_data: dict[str, auth_identity_read_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = auth_identity_read_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[auth_identity_read_dto], str], agg_method: Callable[[auth_identity_read_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, auth_identity_read_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res


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
        return cls(list([dto]))
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
    def to_dict_by_uid(self) -> dict[str, auth_password_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def to_dict_by_auth_password_uid(self) -> dict[str, auth_password_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.auth_password_uid] = dto
        return d
    def to_dict_by_account_instance_uid(self) -> dict[str, auth_password_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.account_instance_uid] = dto
        return d
    def to_dict_by_system_instance_uid(self) -> dict[str, auth_password_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.system_instance_uid] = dto
        return d
    def to_dict_by_password_hash(self) -> dict[str, auth_password_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.password_hash] = dto
        return d
    def to_dict_by_password_salt(self) -> dict[str, auth_password_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.password_salt] = dto
        return d
    def to_dict_by_date_from(self) -> dict[str, auth_password_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.date_from] = dto
        return d
    def to_dict_by_date_to(self) -> dict[str, auth_password_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.date_to] = dto
        return d
    def to_dict_by_usage_count(self) -> dict[str, auth_password_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.usage_count] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_all(self, check_method: Callable[[auth_password_read_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def for_any(self, check_method: Callable[[auth_password_read_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[auth_password_read_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[auth_password_read_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[auth_password_read_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, auth_password_read_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, auth_password_read_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, auth_password_read_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[auth_password_read_dto], bool]) -> auth_password_read_dtos:
        return auth_password_read_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[auth_password_read_dto], str]) -> dict[str, auth_password_read_dtos]:
        grp_data: dict[str, auth_password_read_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = auth_password_read_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[auth_password_read_dto], str], agg_method: Callable[[auth_password_read_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, auth_password_read_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res


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
        return cls(list([dto]))
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
    def to_dict_by_uid(self) -> dict[str, auth_permission_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def to_dict_by_auth_permission_uid(self) -> dict[str, auth_permission_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.auth_permission_uid] = dto
        return d
    def to_dict_by_account_instance_uid(self) -> dict[str, auth_permission_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.account_instance_uid] = dto
        return d
    def to_dict_by_system_instance_uid(self) -> dict[str, auth_permission_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.system_instance_uid] = dto
        return d
    def to_dict_by_auth_role_uid(self) -> dict[str, auth_permission_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.auth_role_uid] = dto
        return d
    def to_dict_by_client_instance_uid(self) -> dict[str, auth_permission_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.client_instance_uid] = dto
        return d
    def to_dict_by_project_instance_uid(self) -> dict[str, auth_permission_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.project_instance_uid] = dto
        return d
    def to_dict_by_valid_from_date(self) -> dict[str, auth_permission_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.valid_from_date] = dto
        return d
    def to_dict_by_valid_till_date(self) -> dict[str, auth_permission_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.valid_till_date] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_all(self, check_method: Callable[[auth_permission_read_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def for_any(self, check_method: Callable[[auth_permission_read_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[auth_permission_read_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[auth_permission_read_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[auth_permission_read_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, auth_permission_read_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, auth_permission_read_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, auth_permission_read_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[auth_permission_read_dto], bool]) -> auth_permission_read_dtos:
        return auth_permission_read_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[auth_permission_read_dto], str]) -> dict[str, auth_permission_read_dtos]:
        grp_data: dict[str, auth_permission_read_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = auth_permission_read_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[auth_permission_read_dto], str], agg_method: Callable[[auth_permission_read_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, auth_permission_read_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res


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
        return cls(list([dto]))
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
    def to_dict_by_uid(self) -> dict[str, auth_request_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def to_dict_by_auth_request_uid(self) -> dict[str, auth_request_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.auth_request_uid] = dto
        return d
    def to_dict_by_by_account_instance_uid(self) -> dict[str, auth_request_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.by_account_instance_uid] = dto
        return d
    def to_dict_by_account_instance_uid(self) -> dict[str, auth_request_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.account_instance_uid] = dto
        return d
    def to_dict_by_system_instance_uid(self) -> dict[str, auth_request_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.system_instance_uid] = dto
        return d
    def to_dict_by_reset_guid(self) -> dict[str, auth_request_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.reset_guid] = dto
        return d
    def to_dict_by_valid_till_date(self) -> dict[str, auth_request_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.valid_till_date] = dto
        return d
    def to_dict_by_lock_guid(self) -> dict[str, auth_request_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.lock_guid] = dto
        return d
    def to_dict_by_lock_by(self) -> dict[str, auth_request_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.lock_by] = dto
        return d
    def to_dict_by_lock_date(self) -> dict[str, auth_request_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.lock_date] = dto
        return d
    def to_dict_by_is_checked(self) -> dict[str, auth_request_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.is_checked] = dto
        return d
    def to_dict_by_is_used(self) -> dict[str, auth_request_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.is_used] = dto
        return d
    def to_dict_by_check_date(self) -> dict[str, auth_request_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.check_date] = dto
        return d
    def to_dict_by_use_date(self) -> dict[str, auth_request_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.use_date] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_all(self, check_method: Callable[[auth_request_read_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def for_any(self, check_method: Callable[[auth_request_read_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[auth_request_read_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[auth_request_read_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[auth_request_read_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, auth_request_read_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, auth_request_read_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, auth_request_read_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[auth_request_read_dto], bool]) -> auth_request_read_dtos:
        return auth_request_read_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[auth_request_read_dto], str]) -> dict[str, auth_request_read_dtos]:
        grp_data: dict[str, auth_request_read_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = auth_request_read_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[auth_request_read_dto], str], agg_method: Callable[[auth_request_read_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, auth_request_read_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res


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
        return cls(list([dto]))
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
    def to_dict_by_uid(self) -> dict[str, auth_role_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def to_dict_by_auth_role_uid(self) -> dict[str, auth_role_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.auth_role_uid] = dto
        return d
    def to_dict_by_parent_auth_role_uid(self) -> dict[str, auth_role_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.parent_auth_role_uid] = dto
        return d
    def to_dict_by_role_name(self) -> dict[str, auth_role_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.role_name] = dto
        return d
    def to_dict_by_role_description(self) -> dict[str, auth_role_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.role_description] = dto
        return d
    def to_dict_by_access_uris(self) -> dict[str, auth_role_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.access_uris] = dto
        return d
    def to_dict_by_is_project(self) -> dict[str, auth_role_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.is_project] = dto
        return d
    def to_dict_by_is_client(self) -> dict[str, auth_role_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.is_client] = dto
        return d
    def to_dict_by_is_custom(self) -> dict[str, auth_role_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.is_custom] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_all(self, check_method: Callable[[auth_role_read_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def for_any(self, check_method: Callable[[auth_role_read_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[auth_role_read_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[auth_role_read_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[auth_role_read_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, auth_role_read_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, auth_role_read_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, auth_role_read_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[auth_role_read_dto], bool]) -> auth_role_read_dtos:
        return auth_role_read_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[auth_role_read_dto], str]) -> dict[str, auth_role_read_dtos]:
        grp_data: dict[str, auth_role_read_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = auth_role_read_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[auth_role_read_dto], str], agg_method: Callable[[auth_role_read_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, auth_role_read_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res


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
        return cls(list([dto]))
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
    def to_dict_by_uid(self) -> dict[str, auth_token_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def to_dict_by_auth_token_uid(self) -> dict[str, auth_token_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.auth_token_uid] = dto
        return d
    def to_dict_by_account_instance_uid(self) -> dict[str, auth_token_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.account_instance_uid] = dto
        return d
    def to_dict_by_system_instance_uid(self) -> dict[str, auth_token_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.system_instance_uid] = dto
        return d
    def to_dict_by_token_seq(self) -> dict[str, auth_token_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.token_seq] = dto
        return d
    def to_dict_by_token_hash(self) -> dict[str, auth_token_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.token_hash] = dto
        return d
    def to_dict_by_token_salt(self) -> dict[str, auth_token_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.token_salt] = dto
        return d
    def to_dict_by_valid_till_date(self) -> dict[str, auth_token_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.valid_till_date] = dto
        return d
    def to_dict_by_last_use_date(self) -> dict[str, auth_token_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.last_use_date] = dto
        return d
    def to_dict_by_is_last(self) -> dict[str, auth_token_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.is_last] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_all(self, check_method: Callable[[auth_token_read_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def for_any(self, check_method: Callable[[auth_token_read_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[auth_token_read_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[auth_token_read_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[auth_token_read_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, auth_token_read_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, auth_token_read_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, auth_token_read_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[auth_token_read_dto], bool]) -> auth_token_read_dtos:
        return auth_token_read_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[auth_token_read_dto], str]) -> dict[str, auth_token_read_dtos]:
        grp_data: dict[str, auth_token_read_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = auth_token_read_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[auth_token_read_dto], str], agg_method: Callable[[auth_token_read_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, auth_token_read_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res


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
        return cls(list([dto]))
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
    def to_dict_by_uid(self) -> dict[str, client_instance_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def to_dict_by_client_instance_uid(self) -> dict[str, client_instance_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.client_instance_uid] = dto
        return d
    def to_dict_by_country_uid(self) -> dict[str, client_instance_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.country_uid] = dto
        return d
    def to_dict_by_client_name(self) -> dict[str, client_instance_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.client_name] = dto
        return d
    def to_dict_by_client_code(self) -> dict[str, client_instance_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.client_code] = dto
        return d
    def to_dict_by_client_description(self) -> dict[str, client_instance_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.client_description] = dto
        return d
    def to_dict_by_start_date(self) -> dict[str, client_instance_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.start_date] = dto
        return d
    def to_dict_by_end_date(self) -> dict[str, client_instance_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.end_date] = dto
        return d
    def to_dict_by_is_internal(self) -> dict[str, client_instance_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.is_internal] = dto
        return d
    def to_dict_by_is_system(self) -> dict[str, client_instance_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.is_system] = dto
        return d
    def to_dict_by_is_test(self) -> dict[str, client_instance_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.is_test] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_all(self, check_method: Callable[[client_instance_read_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def for_any(self, check_method: Callable[[client_instance_read_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[client_instance_read_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[client_instance_read_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[client_instance_read_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, client_instance_read_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, client_instance_read_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, client_instance_read_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[client_instance_read_dto], bool]) -> client_instance_read_dtos:
        return client_instance_read_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[client_instance_read_dto], str]) -> dict[str, client_instance_read_dtos]:
        grp_data: dict[str, client_instance_read_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = client_instance_read_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[client_instance_read_dto], str], agg_method: Callable[[client_instance_read_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, client_instance_read_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res


@dataclass(frozen=False)
class client_type_read_dtos(base_dtos):
    dtos: list[client_type_read_dto]
    def __init__(self, dtos: list[client_type_read_dto]):
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[client_type_read_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: client_type_read_dto):
        return cls(list([dto]))
    @classmethod
    def from_lists(cls, dtos1: list[client_type_read_dto], dtos2: list[client_type_read_dto]):
        return cls(dtos1 + dtos2)
    def get_active(self):
        return client_type_read_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return client_type_read_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_write_dtos(self) -> list[client_type_write_dto]:
        return list(filter(lambda x: x.to_write() != 1, self.dtos))
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write().to_write_dict(), self.dtos))
    def get_read_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> client_type_read_dto | None:
        found_dtos = list(filter(lambda x: x.client_type_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def get_first(self) -> client_type_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, client_type_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def to_dict_by_client_type_uid(self) -> dict[str, client_type_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.client_type_uid] = dto
        return d
    def to_dict_by_system_version_uid(self) -> dict[str, client_type_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.system_version_uid] = dto
        return d
    def to_dict_by_client_type_name(self) -> dict[str, client_type_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.client_type_name] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_all(self, check_method: Callable[[client_type_read_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def for_any(self, check_method: Callable[[client_type_read_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[client_type_read_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[client_type_read_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[client_type_read_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, client_type_read_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, client_type_read_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, client_type_read_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[client_type_read_dto], bool]) -> client_type_read_dtos:
        return client_type_read_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[client_type_read_dto], str]) -> dict[str, client_type_read_dtos]:
        grp_data: dict[str, client_type_read_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = client_type_read_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[client_type_read_dto], str], agg_method: Callable[[client_type_read_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, client_type_read_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res


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
        return cls(list([dto]))
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
    def to_dict_by_uid(self) -> dict[str, country_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def to_dict_by_country_uid(self) -> dict[str, country_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.country_uid] = dto
        return d
    def to_dict_by_continent_name(self) -> dict[str, country_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.continent_name] = dto
        return d
    def to_dict_by_continent_code(self) -> dict[str, country_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.continent_code] = dto
        return d
    def to_dict_by_country_name(self) -> dict[str, country_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.country_name] = dto
        return d
    def to_dict_by_country_iso3(self) -> dict[str, country_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.country_iso3] = dto
        return d
    def to_dict_by_country_code(self) -> dict[str, country_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.country_code] = dto
        return d
    def to_dict_by_phone_code(self) -> dict[str, country_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.phone_code] = dto
        return d
    def to_dict_by_currency_code(self) -> dict[str, country_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.currency_code] = dto
        return d
    def to_dict_by_capital_name(self) -> dict[str, country_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.capital_name] = dto
        return d
    def to_dict_by_region_name(self) -> dict[str, country_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.region_name] = dto
        return d
    def to_dict_by_subregion_name(self) -> dict[str, country_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.subregion_name] = dto
        return d
    def to_dict_by_region_code(self) -> dict[str, country_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.region_code] = dto
        return d
    def to_dict_by_latitude(self) -> dict[str, country_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.latitude] = dto
        return d
    def to_dict_by_longitude(self) -> dict[str, country_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.longitude] = dto
        return d
    def to_dict_by_currency_name(self) -> dict[str, country_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.currency_name] = dto
        return d
    def to_dict_by_population(self) -> dict[str, country_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.population] = dto
        return d
    def to_dict_by_languages(self) -> dict[str, country_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.languages] = dto
        return d
    def to_dict_by_area(self) -> dict[str, country_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.area] = dto
        return d
    def to_dict_by_bar_code(self) -> dict[str, country_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.bar_code] = dto
        return d
    def to_dict_by_top_level_domain(self) -> dict[str, country_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.top_level_domain] = dto
        return d
    def to_dict_by_is_focused(self) -> dict[str, country_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.is_focused] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_all(self, check_method: Callable[[country_read_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def for_any(self, check_method: Callable[[country_read_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[country_read_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[country_read_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[country_read_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, country_read_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, country_read_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, country_read_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[country_read_dto], bool]) -> country_read_dtos:
        return country_read_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[country_read_dto], str]) -> dict[str, country_read_dtos]:
        grp_data: dict[str, country_read_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = country_read_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[country_read_dto], str], agg_method: Callable[[country_read_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, country_read_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res


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
        return cls(list([dto]))
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
    def to_dict_by_uid(self) -> dict[str, currency_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def to_dict_by_currency_uid(self) -> dict[str, currency_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.currency_uid] = dto
        return d
    def to_dict_by_currency_name(self) -> dict[str, currency_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.currency_name] = dto
        return d
    def to_dict_by_is_focused(self) -> dict[str, currency_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.is_focused] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_all(self, check_method: Callable[[currency_read_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def for_any(self, check_method: Callable[[currency_read_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[currency_read_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[currency_read_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[currency_read_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, currency_read_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, currency_read_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, currency_read_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[currency_read_dto], bool]) -> currency_read_dtos:
        return currency_read_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[currency_read_dto], str]) -> dict[str, currency_read_dtos]:
        grp_data: dict[str, currency_read_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = currency_read_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[currency_read_dto], str], agg_method: Callable[[currency_read_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, currency_read_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res


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
        return cls(list([dto]))
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
    def to_dict_by_uid(self) -> dict[str, entry_final_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def to_dict_by_entry_final_uid(self) -> dict[str, entry_final_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.entry_final_uid] = dto
        return d
    def to_dict_by_account_instance_uid(self) -> dict[str, entry_final_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.account_instance_uid] = dto
        return d
    def to_dict_by_project_instance_uid(self) -> dict[str, entry_final_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.project_instance_uid] = dto
        return d
    def to_dict_by_project_milestone_uid(self) -> dict[str, entry_final_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.project_milestone_uid] = dto
        return d
    def to_dict_by_invoice_instance_uid(self) -> dict[str, entry_final_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.invoice_instance_uid] = dto
        return d
    def to_dict_by_entry_period(self) -> dict[str, entry_final_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.entry_period] = dto
        return d
    def to_dict_by_entry_note(self) -> dict[str, entry_final_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.entry_note] = dto
        return d
    def to_dict_by_lock_uid(self) -> dict[str, entry_final_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.lock_uid] = dto
        return d
    def to_dict_by_start_date(self) -> dict[str, entry_final_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.start_date] = dto
        return d
    def to_dict_by_end_date(self) -> dict[str, entry_final_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.end_date] = dto
        return d
    def to_dict_by_entry_minutes(self) -> dict[str, entry_final_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.entry_minutes] = dto
        return d
    def to_dict_by_is_approved(self) -> dict[str, entry_final_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.is_approved] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_all(self, check_method: Callable[[entry_final_read_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def for_any(self, check_method: Callable[[entry_final_read_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[entry_final_read_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[entry_final_read_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[entry_final_read_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, entry_final_read_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, entry_final_read_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, entry_final_read_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[entry_final_read_dto], bool]) -> entry_final_read_dtos:
        return entry_final_read_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[entry_final_read_dto], str]) -> dict[str, entry_final_read_dtos]:
        grp_data: dict[str, entry_final_read_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = entry_final_read_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[entry_final_read_dto], str], agg_method: Callable[[entry_final_read_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, entry_final_read_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res


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
        return cls(list([dto]))
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
    def to_dict_by_uid(self) -> dict[str, entry_save_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def to_dict_by_entry_save_uid(self) -> dict[str, entry_save_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.entry_save_uid] = dto
        return d
    def to_dict_by_account_instance_uid(self) -> dict[str, entry_save_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.account_instance_uid] = dto
        return d
    def to_dict_by_project_instance_uid(self) -> dict[str, entry_save_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.project_instance_uid] = dto
        return d
    def to_dict_by_project_milestone_uid(self) -> dict[str, entry_save_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.project_milestone_uid] = dto
        return d
    def to_dict_by_invoice_instance_uid(self) -> dict[str, entry_save_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.invoice_instance_uid] = dto
        return d
    def to_dict_by_entry_period(self) -> dict[str, entry_save_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.entry_period] = dto
        return d
    def to_dict_by_entry_note(self) -> dict[str, entry_save_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.entry_note] = dto
        return d
    def to_dict_by_lock_uid(self) -> dict[str, entry_save_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.lock_uid] = dto
        return d
    def to_dict_by_start_date(self) -> dict[str, entry_save_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.start_date] = dto
        return d
    def to_dict_by_end_date(self) -> dict[str, entry_save_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.end_date] = dto
        return d
    def to_dict_by_entry_minutes(self) -> dict[str, entry_save_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.entry_minutes] = dto
        return d
    def to_dict_by_is_approved(self) -> dict[str, entry_save_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.is_approved] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_all(self, check_method: Callable[[entry_save_read_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def for_any(self, check_method: Callable[[entry_save_read_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[entry_save_read_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[entry_save_read_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[entry_save_read_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, entry_save_read_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, entry_save_read_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, entry_save_read_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[entry_save_read_dto], bool]) -> entry_save_read_dtos:
        return entry_save_read_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[entry_save_read_dto], str]) -> dict[str, entry_save_read_dtos]:
        grp_data: dict[str, entry_save_read_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = entry_save_read_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[entry_save_read_dto], str], agg_method: Callable[[entry_save_read_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, entry_save_read_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res


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
        return cls(list([dto]))
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
    def to_dict_by_uid(self) -> dict[str, event_channel_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def to_dict_by_event_channel_uid(self) -> dict[str, event_channel_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.event_channel_uid] = dto
        return d
    def to_dict_by_system_version_uid(self) -> dict[str, event_channel_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.system_version_uid] = dto
        return d
    def to_dict_by_channel_type(self) -> dict[str, event_channel_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.channel_type] = dto
        return d
    def to_dict_by_channel_name(self) -> dict[str, event_channel_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.channel_name] = dto
        return d
    def to_dict_by_channel_definition(self) -> dict[str, event_channel_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.channel_definition] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_all(self, check_method: Callable[[event_channel_read_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def for_any(self, check_method: Callable[[event_channel_read_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[event_channel_read_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[event_channel_read_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[event_channel_read_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, event_channel_read_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, event_channel_read_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, event_channel_read_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[event_channel_read_dto], bool]) -> event_channel_read_dtos:
        return event_channel_read_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[event_channel_read_dto], str]) -> dict[str, event_channel_read_dtos]:
        grp_data: dict[str, event_channel_read_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = event_channel_read_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[event_channel_read_dto], str], agg_method: Callable[[event_channel_read_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, event_channel_read_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res


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
        return cls(list([dto]))
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
    def to_dict_by_uid(self) -> dict[str, event_instance_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def to_dict_by_event_instance_uid(self) -> dict[str, event_instance_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.event_instance_uid] = dto
        return d
    def to_dict_by_system_instance_uid(self) -> dict[str, event_instance_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.system_instance_uid] = dto
        return d
    def to_dict_by_event_type(self) -> dict[str, event_instance_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.event_type] = dto
        return d
    def to_dict_by_event_object(self) -> dict[str, event_instance_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.event_object] = dto
        return d
    def to_dict_by_event_method(self) -> dict[str, event_instance_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.event_method] = dto
        return d
    def to_dict_by_event_parameters(self) -> dict[str, event_instance_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.event_parameters] = dto
        return d
    def to_dict_by_event_signature(self) -> dict[str, event_instance_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.event_signature] = dto
        return d
    def to_dict_by_published_count(self) -> dict[str, event_instance_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.published_count] = dto
        return d
    def to_dict_by_event_date(self) -> dict[str, event_instance_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.event_date] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_all(self, check_method: Callable[[event_instance_read_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def for_any(self, check_method: Callable[[event_instance_read_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[event_instance_read_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[event_instance_read_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[event_instance_read_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, event_instance_read_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, event_instance_read_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, event_instance_read_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[event_instance_read_dto], bool]) -> event_instance_read_dtos:
        return event_instance_read_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[event_instance_read_dto], str]) -> dict[str, event_instance_read_dtos]:
        grp_data: dict[str, event_instance_read_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = event_instance_read_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[event_instance_read_dto], str], agg_method: Callable[[event_instance_read_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, event_instance_read_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res


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
        return cls(list([dto]))
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
    def to_dict_by_uid(self) -> dict[str, event_subscription_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def to_dict_by_event_subscription_uid(self) -> dict[str, event_subscription_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.event_subscription_uid] = dto
        return d
    def to_dict_by_event_channel_uid(self) -> dict[str, event_subscription_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.event_channel_uid] = dto
        return d
    def to_dict_by_subscription_name(self) -> dict[str, event_subscription_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.subscription_name] = dto
        return d
    def to_dict_by_subscription_filter(self) -> dict[str, event_subscription_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.subscription_filter] = dto
        return d
    def to_dict_by_subscription_topic(self) -> dict[str, event_subscription_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.subscription_topic] = dto
        return d
    def to_dict_by_subscription_template(self) -> dict[str, event_subscription_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.subscription_template] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_all(self, check_method: Callable[[event_subscription_read_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def for_any(self, check_method: Callable[[event_subscription_read_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[event_subscription_read_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[event_subscription_read_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[event_subscription_read_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, event_subscription_read_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, event_subscription_read_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, event_subscription_read_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[event_subscription_read_dto], bool]) -> event_subscription_read_dtos:
        return event_subscription_read_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[event_subscription_read_dto], str]) -> dict[str, event_subscription_read_dtos]:
        grp_data: dict[str, event_subscription_read_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = event_subscription_read_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[event_subscription_read_dto], str], agg_method: Callable[[event_subscription_read_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, event_subscription_read_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res


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
        return cls(list([dto]))
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
    def to_dict_by_uid(self) -> dict[str, invoice_instance_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def to_dict_by_invoice_instance_uid(self) -> dict[str, invoice_instance_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.invoice_instance_uid] = dto
        return d
    def to_dict_by_client_instance_uid(self) -> dict[str, invoice_instance_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.client_instance_uid] = dto
        return d
    def to_dict_by_account_instance_uid(self) -> dict[str, invoice_instance_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.account_instance_uid] = dto
        return d
    def to_dict_by_period_code(self) -> dict[str, invoice_instance_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.period_code] = dto
        return d
    def to_dict_by_invoice_number(self) -> dict[str, invoice_instance_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.invoice_number] = dto
        return d
    def to_dict_by_invoice_details(self) -> dict[str, invoice_instance_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.invoice_details] = dto
        return d
    def to_dict_by_invoice_status(self) -> dict[str, invoice_instance_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.invoice_status] = dto
        return d
    def to_dict_by_invoice_currency(self) -> dict[str, invoice_instance_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.invoice_currency] = dto
        return d
    def to_dict_by_invoice_amount(self) -> dict[str, invoice_instance_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.invoice_amount] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_all(self, check_method: Callable[[invoice_instance_read_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def for_any(self, check_method: Callable[[invoice_instance_read_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[invoice_instance_read_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[invoice_instance_read_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[invoice_instance_read_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, invoice_instance_read_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, invoice_instance_read_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, invoice_instance_read_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[invoice_instance_read_dto], bool]) -> invoice_instance_read_dtos:
        return invoice_instance_read_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[invoice_instance_read_dto], str]) -> dict[str, invoice_instance_read_dtos]:
        grp_data: dict[str, invoice_instance_read_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = invoice_instance_read_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[invoice_instance_read_dto], str], agg_method: Callable[[invoice_instance_read_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, invoice_instance_read_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res


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
        return cls(list([dto]))
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
    def to_dict_by_uid(self) -> dict[str, notification_instance_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def to_dict_by_notification_instance_uid(self) -> dict[str, notification_instance_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.notification_instance_uid] = dto
        return d
    def to_dict_by_client_instance_uid(self) -> dict[str, notification_instance_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.client_instance_uid] = dto
        return d
    def to_dict_by_account_instance_uid(self) -> dict[str, notification_instance_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.account_instance_uid] = dto
        return d
    def to_dict_by_notification_type(self) -> dict[str, notification_instance_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.notification_type] = dto
        return d
    def to_dict_by_notification_topic(self) -> dict[str, notification_instance_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.notification_topic] = dto
        return d
    def to_dict_by_notification_format(self) -> dict[str, notification_instance_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.notification_format] = dto
        return d
    def to_dict_by_notification_content(self) -> dict[str, notification_instance_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.notification_content] = dto
        return d
    def to_dict_by_sending_status(self) -> dict[str, notification_instance_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.sending_status] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_all(self, check_method: Callable[[notification_instance_read_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def for_any(self, check_method: Callable[[notification_instance_read_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[notification_instance_read_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[notification_instance_read_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[notification_instance_read_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, notification_instance_read_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, notification_instance_read_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, notification_instance_read_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[notification_instance_read_dto], bool]) -> notification_instance_read_dtos:
        return notification_instance_read_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[notification_instance_read_dto], str]) -> dict[str, notification_instance_read_dtos]:
        grp_data: dict[str, notification_instance_read_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = notification_instance_read_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[notification_instance_read_dto], str], agg_method: Callable[[notification_instance_read_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, notification_instance_read_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res


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
        return cls(list([dto]))
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
    def to_dict_by_uid(self) -> dict[str, project_budget_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def to_dict_by_project_budget_uid(self) -> dict[str, project_budget_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.project_budget_uid] = dto
        return d
    def to_dict_by_project_instance_uid(self) -> dict[str, project_budget_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.project_instance_uid] = dto
        return d
    def to_dict_by_budget_name(self) -> dict[str, project_budget_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.budget_name] = dto
        return d
    def to_dict_by_budget_currency(self) -> dict[str, project_budget_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.budget_currency] = dto
        return d
    def to_dict_by_budget_value(self) -> dict[str, project_budget_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.budget_value] = dto
        return d
    def to_dict_by_is_current(self) -> dict[str, project_budget_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.is_current] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_all(self, check_method: Callable[[project_budget_read_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def for_any(self, check_method: Callable[[project_budget_read_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[project_budget_read_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[project_budget_read_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[project_budget_read_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, project_budget_read_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, project_budget_read_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, project_budget_read_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[project_budget_read_dto], bool]) -> project_budget_read_dtos:
        return project_budget_read_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[project_budget_read_dto], str]) -> dict[str, project_budget_read_dtos]:
        grp_data: dict[str, project_budget_read_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = project_budget_read_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[project_budget_read_dto], str], agg_method: Callable[[project_budget_read_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, project_budget_read_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res


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
        return cls(list([dto]))
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
    def to_dict_by_uid(self) -> dict[str, project_group_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def to_dict_by_project_group_uid(self) -> dict[str, project_group_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.project_group_uid] = dto
        return d
    def to_dict_by_project_group_name(self) -> dict[str, project_group_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.project_group_name] = dto
        return d
    def to_dict_by_project_group_description(self) -> dict[str, project_group_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.project_group_description] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_all(self, check_method: Callable[[project_group_read_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def for_any(self, check_method: Callable[[project_group_read_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[project_group_read_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[project_group_read_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[project_group_read_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, project_group_read_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, project_group_read_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, project_group_read_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[project_group_read_dto], bool]) -> project_group_read_dtos:
        return project_group_read_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[project_group_read_dto], str]) -> dict[str, project_group_read_dtos]:
        grp_data: dict[str, project_group_read_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = project_group_read_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[project_group_read_dto], str], agg_method: Callable[[project_group_read_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, project_group_read_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res


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
        return cls(list([dto]))
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
    def to_dict_by_uid(self) -> dict[str, project_instance_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def to_dict_by_project_instance_uid(self) -> dict[str, project_instance_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.project_instance_uid] = dto
        return d
    def to_dict_by_client_instance_uid(self) -> dict[str, project_instance_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.client_instance_uid] = dto
        return d
    def to_dict_by_manager_account_instance_uid(self) -> dict[str, project_instance_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.manager_account_instance_uid] = dto
        return d
    def to_dict_by_project_group_uid(self) -> dict[str, project_instance_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.project_group_uid] = dto
        return d
    def to_dict_by_project_name(self) -> dict[str, project_instance_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.project_name] = dto
        return d
    def to_dict_by_project_code(self) -> dict[str, project_instance_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.project_code] = dto
        return d
    def to_dict_by_is_billable(self) -> dict[str, project_instance_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.is_billable] = dto
        return d
    def to_dict_by_start_date(self) -> dict[str, project_instance_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.start_date] = dto
        return d
    def to_dict_by_end_date(self) -> dict[str, project_instance_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.end_date] = dto
        return d
    def to_dict_by_current_billed(self) -> dict[str, project_instance_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.current_billed] = dto
        return d
    def to_dict_by_budget(self) -> dict[str, project_instance_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.budget] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_all(self, check_method: Callable[[project_instance_read_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def for_any(self, check_method: Callable[[project_instance_read_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[project_instance_read_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[project_instance_read_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[project_instance_read_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, project_instance_read_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, project_instance_read_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, project_instance_read_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[project_instance_read_dto], bool]) -> project_instance_read_dtos:
        return project_instance_read_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[project_instance_read_dto], str]) -> dict[str, project_instance_read_dtos]:
        grp_data: dict[str, project_instance_read_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = project_instance_read_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[project_instance_read_dto], str], agg_method: Callable[[project_instance_read_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, project_instance_read_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res


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
        return cls(list([dto]))
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
    def to_dict_by_uid(self) -> dict[str, project_milestone_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def to_dict_by_project_milestone_uid(self) -> dict[str, project_milestone_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.project_milestone_uid] = dto
        return d
    def to_dict_by_project_instance_uid(self) -> dict[str, project_milestone_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.project_instance_uid] = dto
        return d
    def to_dict_by_project_budget_uid(self) -> dict[str, project_milestone_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.project_budget_uid] = dto
        return d
    def to_dict_by_milestone_name(self) -> dict[str, project_milestone_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.milestone_name] = dto
        return d
    def to_dict_by_start_date(self) -> dict[str, project_milestone_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.start_date] = dto
        return d
    def to_dict_by_end_date(self) -> dict[str, project_milestone_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.end_date] = dto
        return d
    def to_dict_by_status_name(self) -> dict[str, project_milestone_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.status_name] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_all(self, check_method: Callable[[project_milestone_read_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def for_any(self, check_method: Callable[[project_milestone_read_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[project_milestone_read_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[project_milestone_read_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[project_milestone_read_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, project_milestone_read_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, project_milestone_read_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, project_milestone_read_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[project_milestone_read_dto], bool]) -> project_milestone_read_dtos:
        return project_milestone_read_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[project_milestone_read_dto], str]) -> dict[str, project_milestone_read_dtos]:
        grp_data: dict[str, project_milestone_read_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = project_milestone_read_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[project_milestone_read_dto], str], agg_method: Callable[[project_milestone_read_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, project_milestone_read_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res


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
        return cls(list([dto]))
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
    def to_dict_by_uid(self) -> dict[str, system_attribute_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def to_dict_by_system_attribute_uid(self) -> dict[str, system_attribute_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.system_attribute_uid] = dto
        return d
    def to_dict_by_system_object_uid(self) -> dict[str, system_attribute_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.system_object_uid] = dto
        return d
    def to_dict_by_system_version_uid(self) -> dict[str, system_attribute_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.system_version_uid] = dto
        return d
    def to_dict_by_column_name(self) -> dict[str, system_attribute_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.column_name] = dto
        return d
    def to_dict_by_attribute_name(self) -> dict[str, system_attribute_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.attribute_name] = dto
        return d
    def to_dict_by_attribute_type(self) -> dict[str, system_attribute_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.attribute_type] = dto
        return d
    def to_dict_by_attribute_label(self) -> dict[str, system_attribute_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.attribute_label] = dto
        return d
    def to_dict_by_attribute_description(self) -> dict[str, system_attribute_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.attribute_description] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_all(self, check_method: Callable[[system_attribute_read_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def for_any(self, check_method: Callable[[system_attribute_read_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[system_attribute_read_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[system_attribute_read_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[system_attribute_read_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, system_attribute_read_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, system_attribute_read_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, system_attribute_read_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[system_attribute_read_dto], bool]) -> system_attribute_read_dtos:
        return system_attribute_read_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[system_attribute_read_dto], str]) -> dict[str, system_attribute_read_dtos]:
        grp_data: dict[str, system_attribute_read_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = system_attribute_read_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[system_attribute_read_dto], str], agg_method: Callable[[system_attribute_read_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, system_attribute_read_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res


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
        return cls(list([dto]))
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
    def to_dict_by_uid(self) -> dict[str, system_change_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def to_dict_by_system_change_uid(self) -> dict[str, system_change_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.system_change_uid] = dto
        return d
    def to_dict_by_account_instance_uid(self) -> dict[str, system_change_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.account_instance_uid] = dto
        return d
    def to_dict_by_system_instance_uid(self) -> dict[str, system_change_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.system_instance_uid] = dto
        return d
    def to_dict_by_change_type(self) -> dict[str, system_change_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.change_type] = dto
        return d
    def to_dict_by_change_name(self) -> dict[str, system_change_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.change_name] = dto
        return d
    def to_dict_by_change_json(self) -> dict[str, system_change_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.change_json] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_all(self, check_method: Callable[[system_change_read_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def for_any(self, check_method: Callable[[system_change_read_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[system_change_read_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[system_change_read_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[system_change_read_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, system_change_read_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, system_change_read_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, system_change_read_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[system_change_read_dto], bool]) -> system_change_read_dtos:
        return system_change_read_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[system_change_read_dto], str]) -> dict[str, system_change_read_dtos]:
        grp_data: dict[str, system_change_read_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = system_change_read_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[system_change_read_dto], str], agg_method: Callable[[system_change_read_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, system_change_read_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res


@dataclass(frozen=False)
class system_database_read_dtos(base_dtos):
    dtos: list[system_database_read_dto]
    def __init__(self, dtos: list[system_database_read_dto]):
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[system_database_read_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: system_database_read_dto):
        return cls(list([dto]))
    @classmethod
    def from_lists(cls, dtos1: list[system_database_read_dto], dtos2: list[system_database_read_dto]):
        return cls(dtos1 + dtos2)
    def get_active(self):
        return system_database_read_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return system_database_read_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_write_dtos(self) -> list[system_database_write_dto]:
        return list(filter(lambda x: x.to_write() != 1, self.dtos))
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write().to_write_dict(), self.dtos))
    def get_read_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> system_database_read_dto | None:
        found_dtos = list(filter(lambda x: x.system_database_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def get_first(self) -> system_database_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, system_database_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def to_dict_by_system_database_uid(self) -> dict[str, system_database_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.system_database_uid] = dto
        return d
    def to_dict_by_db_url(self) -> dict[str, system_database_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.db_url] = dto
        return d
    def to_dict_by_db_host(self) -> dict[str, system_database_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.db_host] = dto
        return d
    def to_dict_by_db_name(self) -> dict[str, system_database_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.db_name] = dto
        return d
    def to_dict_by_db_user(self) -> dict[str, system_database_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.db_user] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_all(self, check_method: Callable[[system_database_read_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def for_any(self, check_method: Callable[[system_database_read_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[system_database_read_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[system_database_read_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[system_database_read_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, system_database_read_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, system_database_read_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, system_database_read_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[system_database_read_dto], bool]) -> system_database_read_dtos:
        return system_database_read_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[system_database_read_dto], str]) -> dict[str, system_database_read_dtos]:
        grp_data: dict[str, system_database_read_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = system_database_read_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[system_database_read_dto], str], agg_method: Callable[[system_database_read_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, system_database_read_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res


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
        return cls(list([dto]))
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
    def to_dict_by_uid(self) -> dict[str, system_exception_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def to_dict_by_system_exception_uid(self) -> dict[str, system_exception_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.system_exception_uid] = dto
        return d
    def to_dict_by_system_instance_uid(self) -> dict[str, system_exception_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.system_instance_uid] = dto
        return d
    def to_dict_by_exception_class(self) -> dict[str, system_exception_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.exception_class] = dto
        return d
    def to_dict_by_exception_message(self) -> dict[str, system_exception_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.exception_message] = dto
        return d
    def to_dict_by_exception_stacktrace(self) -> dict[str, system_exception_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.exception_stacktrace] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_all(self, check_method: Callable[[system_exception_read_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def for_any(self, check_method: Callable[[system_exception_read_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[system_exception_read_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[system_exception_read_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[system_exception_read_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, system_exception_read_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, system_exception_read_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, system_exception_read_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[system_exception_read_dto], bool]) -> system_exception_read_dtos:
        return system_exception_read_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[system_exception_read_dto], str]) -> dict[str, system_exception_read_dtos]:
        grp_data: dict[str, system_exception_read_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = system_exception_read_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[system_exception_read_dto], str], agg_method: Callable[[system_exception_read_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, system_exception_read_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res


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
        return cls(list([dto]))
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
    def to_dict_by_uid(self) -> dict[str, system_instance_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def to_dict_by_system_instance_uid(self) -> dict[str, system_instance_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.system_instance_uid] = dto
        return d
    def to_dict_by_system_version_uid(self) -> dict[str, system_instance_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.system_version_uid] = dto
        return d
    def to_dict_by_host_name(self) -> dict[str, system_instance_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.host_name] = dto
        return d
    def to_dict_by_host_ip(self) -> dict[str, system_instance_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.host_ip] = dto
        return d
    def to_dict_by_local_path(self) -> dict[str, system_instance_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.local_path] = dto
        return d
    def to_dict_by_mode_name(self) -> dict[str, system_instance_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.mode_name] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_all(self, check_method: Callable[[system_instance_read_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def for_any(self, check_method: Callable[[system_instance_read_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[system_instance_read_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[system_instance_read_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[system_instance_read_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, system_instance_read_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, system_instance_read_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, system_instance_read_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[system_instance_read_dto], bool]) -> system_instance_read_dtos:
        return system_instance_read_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[system_instance_read_dto], str]) -> dict[str, system_instance_read_dtos]:
        grp_data: dict[str, system_instance_read_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = system_instance_read_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[system_instance_read_dto], str], agg_method: Callable[[system_instance_read_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, system_instance_read_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res


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
        return cls(list([dto]))
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
    def to_dict_by_uid(self) -> dict[str, system_object_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def to_dict_by_system_object_uid(self) -> dict[str, system_object_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.system_object_uid] = dto
        return d
    def to_dict_by_system_version_uid(self) -> dict[str, system_object_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.system_version_uid] = dto
        return d
    def to_dict_by_object_name(self) -> dict[str, system_object_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.object_name] = dto
        return d
    def to_dict_by_object_type(self) -> dict[str, system_object_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.object_type] = dto
        return d
    def to_dict_by_table_name(self) -> dict[str, system_object_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.table_name] = dto
        return d
    def to_dict_by_key_name(self) -> dict[str, system_object_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.key_name] = dto
        return d
    def to_dict_by_parent_system_object_uid(self) -> dict[str, system_object_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.parent_system_object_uid] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_all(self, check_method: Callable[[system_object_read_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def for_any(self, check_method: Callable[[system_object_read_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[system_object_read_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[system_object_read_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[system_object_read_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, system_object_read_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, system_object_read_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, system_object_read_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[system_object_read_dto], bool]) -> system_object_read_dtos:
        return system_object_read_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[system_object_read_dto], str]) -> dict[str, system_object_read_dtos]:
        grp_data: dict[str, system_object_read_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = system_object_read_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[system_object_read_dto], str], agg_method: Callable[[system_object_read_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, system_object_read_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res


@dataclass(frozen=False)
class system_object_type_read_dtos(base_dtos):
    dtos: list[system_object_type_read_dto]
    def __init__(self, dtos: list[system_object_type_read_dto]):
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[system_object_type_read_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: system_object_type_read_dto):
        return cls(list([dto]))
    @classmethod
    def from_lists(cls, dtos1: list[system_object_type_read_dto], dtos2: list[system_object_type_read_dto]):
        return cls(dtos1 + dtos2)
    def get_active(self):
        return system_object_type_read_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return system_object_type_read_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_write_dtos(self) -> list[system_object_type_write_dto]:
        return list(filter(lambda x: x.to_write() != 1, self.dtos))
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write().to_write_dict(), self.dtos))
    def get_read_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> system_object_type_read_dto | None:
        found_dtos = list(filter(lambda x: x.system_object_type_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def get_first(self) -> system_object_type_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, system_object_type_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def to_dict_by_system_object_type_uid(self) -> dict[str, system_object_type_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.system_object_type_uid] = dto
        return d
    def to_dict_by_system_version_uid(self) -> dict[str, system_object_type_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.system_version_uid] = dto
        return d
    def to_dict_by_system_object_uid(self) -> dict[str, system_object_type_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.system_object_uid] = dto
        return d
    def to_dict_by_object_type_name(self) -> dict[str, system_object_type_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.object_type_name] = dto
        return d
    def to_dict_by_object_type_description(self) -> dict[str, system_object_type_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.object_type_description] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_all(self, check_method: Callable[[system_object_type_read_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def for_any(self, check_method: Callable[[system_object_type_read_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[system_object_type_read_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[system_object_type_read_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[system_object_type_read_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, system_object_type_read_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, system_object_type_read_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, system_object_type_read_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[system_object_type_read_dto], bool]) -> system_object_type_read_dtos:
        return system_object_type_read_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[system_object_type_read_dto], str]) -> dict[str, system_object_type_read_dtos]:
        grp_data: dict[str, system_object_type_read_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = system_object_type_read_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[system_object_type_read_dto], str], agg_method: Callable[[system_object_type_read_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, system_object_type_read_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res


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
        return cls(list([dto]))
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
    def to_dict_by_uid(self) -> dict[str, system_setting_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def to_dict_by_system_setting_uid(self) -> dict[str, system_setting_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.system_setting_uid] = dto
        return d
    def to_dict_by_account_instance_uid(self) -> dict[str, system_setting_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.account_instance_uid] = dto
        return d
    def to_dict_by_setting_name(self) -> dict[str, system_setting_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.setting_name] = dto
        return d
    def to_dict_by_setting_value(self) -> dict[str, system_setting_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.setting_value] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_all(self, check_method: Callable[[system_setting_read_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def for_any(self, check_method: Callable[[system_setting_read_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[system_setting_read_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[system_setting_read_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[system_setting_read_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, system_setting_read_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, system_setting_read_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, system_setting_read_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[system_setting_read_dto], bool]) -> system_setting_read_dtos:
        return system_setting_read_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[system_setting_read_dto], str]) -> dict[str, system_setting_read_dtos]:
        grp_data: dict[str, system_setting_read_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = system_setting_read_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[system_setting_read_dto], str], agg_method: Callable[[system_setting_read_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, system_setting_read_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res


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
        return cls(list([dto]))
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
    def to_dict_by_uid(self) -> dict[str, system_state_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def to_dict_by_system_state_uid(self) -> dict[str, system_state_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.system_state_uid] = dto
        return d
    def to_dict_by_system_instance_uid(self) -> dict[str, system_state_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.system_instance_uid] = dto
        return d
    def to_dict_by_mem_free(self) -> dict[str, system_state_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.mem_free] = dto
        return d
    def to_dict_by_mem_max(self) -> dict[str, system_state_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.mem_max] = dto
        return d
    def to_dict_by_objects_count(self) -> dict[str, system_state_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.objects_count] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_all(self, check_method: Callable[[system_state_read_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def for_any(self, check_method: Callable[[system_state_read_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[system_state_read_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[system_state_read_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[system_state_read_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, system_state_read_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, system_state_read_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, system_state_read_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[system_state_read_dto], bool]) -> system_state_read_dtos:
        return system_state_read_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[system_state_read_dto], str]) -> dict[str, system_state_read_dtos]:
        grp_data: dict[str, system_state_read_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = system_state_read_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[system_state_read_dto], str], agg_method: Callable[[system_state_read_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, system_state_read_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res


@dataclass(frozen=False)
class system_version_read_dtos(base_dtos):
    dtos: list[system_version_read_dto]
    def __init__(self, dtos: list[system_version_read_dto]):
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[system_version_read_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: system_version_read_dto):
        return cls(list([dto]))
    @classmethod
    def from_lists(cls, dtos1: list[system_version_read_dto], dtos2: list[system_version_read_dto]):
        return cls(dtos1 + dtos2)
    def get_active(self):
        return system_version_read_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return system_version_read_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_write_dtos(self) -> list[system_version_write_dto]:
        return list(filter(lambda x: x.to_write() != 1, self.dtos))
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write().to_write_dict(), self.dtos))
    def get_read_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> system_version_read_dto | None:
        found_dtos = list(filter(lambda x: x.system_version_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def get_first(self) -> system_version_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, system_version_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def to_dict_by_system_version_uid(self) -> dict[str, system_version_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.system_version_uid] = dto
        return d
    def to_dict_by_version_description(self) -> dict[str, system_version_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.version_description] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_all(self, check_method: Callable[[system_version_read_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def for_any(self, check_method: Callable[[system_version_read_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[system_version_read_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[system_version_read_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[system_version_read_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, system_version_read_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, system_version_read_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, system_version_read_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[system_version_read_dto], bool]) -> system_version_read_dtos:
        return system_version_read_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[system_version_read_dto], str]) -> dict[str, system_version_read_dtos]:
        grp_data: dict[str, system_version_read_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = system_version_read_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[system_version_read_dto], str], agg_method: Callable[[system_version_read_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, system_version_read_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res


# auto-generated - DtosRead - END
