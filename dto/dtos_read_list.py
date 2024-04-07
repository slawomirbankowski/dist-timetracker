# auto-generated - v_definition_python_dtos_read_list - START at 2024-03-30 17:20:33.248385+01
from __future__ import annotations
from datetime import datetime
import logging
from logging import config
from abc import abstractmethod
from dataclasses import dataclass
from dto.dtos import *
from dto.dtos_thin import *
from dto.dtos_write import *
from dto.dtos_read import *
import datetime
from typing import Dict, Callable


@dataclass(frozen=False)
class account_read_dtos(base_read_dtos):
    dtos: list[account_read_dto]
    def __init__(self, dtos: list[account_read_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[account_read_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: account_read_dto):
        return cls(list([dto]))
    @classmethod
    def from_lists(cls, dtos1: list[account_read_dto], dtos2: list[account_read_dto]):
        return cls(dtos1 + dtos2)
    def get_active(self):
        return account_read_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return account_read_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_write_dtos(self) -> list[account_write_dto]:
        return list(map(lambda x: x.to_write(), self.dtos))
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write().to_write_dict(), self.dtos))
    def get_read_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> account_read_dto | None:
        found_dtos = list(filter(lambda x: x.account_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def get_first(self) -> account_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> account_read_dtos:
        if len(self.dtos) > n:
            return account_read_dtos(self.dtos[:n])
        else:
            return account_read_dtos(self.dtos)
    def get_last(self) -> account_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, account_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def to_dict_by_account_uid(self) -> dict[str, account_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.account_uid] = dto
        return d
    def to_dict_by_account_name(self) -> dict[str, account_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.account_name] = dto
        return d
    def to_dict_by_tenant_uid(self) -> dict[str, account_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.tenant_uid] = dto
        return d
    def to_dict_by_account_type_uid(self) -> dict[str, account_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.account_type_uid] = dto
        return d
    def to_dict_by_account_title_uid(self) -> dict[str, account_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.account_title_uid] = dto
        return d
    def to_dict_by_account_division_uid(self) -> dict[str, account_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.account_division_uid] = dto
        return d
    def to_dict_by_account_group_uid(self) -> dict[str, account_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.account_group_uid] = dto
        return d
    def to_dict_by_auth_identity_uid(self) -> dict[str, account_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.auth_identity_uid] = dto
        return d
    def to_dict_by_account_email(self) -> dict[str, account_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.account_email] = dto
        return d
    def to_dict_by_display_name(self) -> dict[str, account_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.display_name] = dto
        return d
    def to_dict_by_is_system(self) -> dict[str, account_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.is_system] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[account_read_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[account_read_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return init
    def check_any(self, check_method: Callable[[account_read_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return init
    def map_to_string(self, map_method: Callable[[account_read_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[account_read_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[account_read_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, account_read_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, account_read_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, account_read_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[account_read_dto], bool]) -> account_read_dtos:
        return account_read_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[account_read_dto], str]) -> dict[str, account_read_dtos]:
        grp_data: dict[str, account_read_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = account_read_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[account_read_dto], str], agg_method: Callable[[account_read_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, account_read_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[account_read_dto], bool]) -> account_read_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[account_read_dto], any], compare_method: Callable[[any, any], bool]) -> account_read_dto | None:
        if len(self.dtos) == 0:
            return None
        else:
            max_value = value_method(self.dtos[0])
            max_elem = self.dtos[0]
            for dto in self.dtos:
                next_value = value_method(dto)
                if compare_method(next_value, max_value):
                    max_value = next_value
                    max_elem = dto
            return max_elem


@dataclass(frozen=False)
class account_division_read_dtos(base_read_dtos):
    dtos: list[account_division_read_dto]
    def __init__(self, dtos: list[account_division_read_dto]):
        super().__init__(dtos)
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
        return list(map(lambda x: x.to_write(), self.dtos))
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
    def get_first_n(self, n: int) -> account_division_read_dtos:
        if len(self.dtos) > n:
            return account_division_read_dtos(self.dtos[:n])
        else:
            return account_division_read_dtos(self.dtos)
    def get_last(self) -> account_division_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
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
    def to_dict_by_account_division_name(self) -> dict[str, account_division_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.account_division_name] = dto
        return d
    def to_dict_by_tenant_uid(self) -> dict[str, account_division_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.tenant_uid] = dto
        return d
    def to_dict_by_account_uid(self) -> dict[str, account_division_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.account_uid] = dto
        return d
    def to_dict_by_account_division_template_uid(self) -> dict[str, account_division_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.account_division_template_uid] = dto
        return d
    def to_dict_by_division_description(self) -> dict[str, account_division_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.division_description] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[account_division_read_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[account_division_read_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return init
    def check_any(self, check_method: Callable[[account_division_read_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return init
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
    def find(self, check_method: Callable[[account_division_read_dto], bool]) -> account_division_read_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[account_division_read_dto], any], compare_method: Callable[[any, any], bool]) -> account_division_read_dto | None:
        if len(self.dtos) == 0:
            return None
        else:
            max_value = value_method(self.dtos[0])
            max_elem = self.dtos[0]
            for dto in self.dtos:
                next_value = value_method(dto)
                if compare_method(next_value, max_value):
                    max_value = next_value
                    max_elem = dto
            return max_elem


@dataclass(frozen=False)
class account_division_template_read_dtos(base_read_dtos):
    dtos: list[account_division_template_read_dto]
    def __init__(self, dtos: list[account_division_template_read_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[account_division_template_read_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: account_division_template_read_dto):
        return cls(list([dto]))
    @classmethod
    def from_lists(cls, dtos1: list[account_division_template_read_dto], dtos2: list[account_division_template_read_dto]):
        return cls(dtos1 + dtos2)
    def get_active(self):
        return account_division_template_read_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return account_division_template_read_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_write_dtos(self) -> list[account_division_template_write_dto]:
        return list(map(lambda x: x.to_write(), self.dtos))
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write().to_write_dict(), self.dtos))
    def get_read_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> account_division_template_read_dto | None:
        found_dtos = list(filter(lambda x: x.account_division_template_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def get_first(self) -> account_division_template_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> account_division_template_read_dtos:
        if len(self.dtos) > n:
            return account_division_template_read_dtos(self.dtos[:n])
        else:
            return account_division_template_read_dtos(self.dtos)
    def get_last(self) -> account_division_template_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, account_division_template_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def to_dict_by_account_division_template_uid(self) -> dict[str, account_division_template_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.account_division_template_uid] = dto
        return d
    def to_dict_by_account_division_template_name(self) -> dict[str, account_division_template_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.account_division_template_name] = dto
        return d
    def to_dict_by_division_description(self) -> dict[str, account_division_template_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.division_description] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[account_division_template_read_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[account_division_template_read_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return init
    def check_any(self, check_method: Callable[[account_division_template_read_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return init
    def map_to_string(self, map_method: Callable[[account_division_template_read_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[account_division_template_read_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[account_division_template_read_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, account_division_template_read_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, account_division_template_read_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, account_division_template_read_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[account_division_template_read_dto], bool]) -> account_division_template_read_dtos:
        return account_division_template_read_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[account_division_template_read_dto], str]) -> dict[str, account_division_template_read_dtos]:
        grp_data: dict[str, account_division_template_read_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = account_division_template_read_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[account_division_template_read_dto], str], agg_method: Callable[[account_division_template_read_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, account_division_template_read_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[account_division_template_read_dto], bool]) -> account_division_template_read_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[account_division_template_read_dto], any], compare_method: Callable[[any, any], bool]) -> account_division_template_read_dto | None:
        if len(self.dtos) == 0:
            return None
        else:
            max_value = value_method(self.dtos[0])
            max_elem = self.dtos[0]
            for dto in self.dtos:
                next_value = value_method(dto)
                if compare_method(next_value, max_value):
                    max_value = next_value
                    max_elem = dto
            return max_elem


@dataclass(frozen=False)
class account_group_read_dtos(base_read_dtos):
    dtos: list[account_group_read_dto]
    def __init__(self, dtos: list[account_group_read_dto]):
        super().__init__(dtos)
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
        return list(map(lambda x: x.to_write(), self.dtos))
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
    def get_first_n(self, n: int) -> account_group_read_dtos:
        if len(self.dtos) > n:
            return account_group_read_dtos(self.dtos[:n])
        else:
            return account_group_read_dtos(self.dtos)
    def get_last(self) -> account_group_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
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
    def to_dict_by_account_group_name(self) -> dict[str, account_group_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.account_group_name] = dto
        return d
    def to_dict_by_tenant_uid(self) -> dict[str, account_group_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.tenant_uid] = dto
        return d
    def to_dict_by_account_group_description(self) -> dict[str, account_group_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.account_group_description] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[account_group_read_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[account_group_read_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return init
    def check_any(self, check_method: Callable[[account_group_read_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return init
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
    def find(self, check_method: Callable[[account_group_read_dto], bool]) -> account_group_read_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[account_group_read_dto], any], compare_method: Callable[[any, any], bool]) -> account_group_read_dto | None:
        if len(self.dtos) == 0:
            return None
        else:
            max_value = value_method(self.dtos[0])
            max_elem = self.dtos[0]
            for dto in self.dtos:
                next_value = value_method(dto)
                if compare_method(next_value, max_value):
                    max_value = next_value
                    max_elem = dto
            return max_elem


@dataclass(frozen=False)
class account_hierarchy_read_dtos(base_read_dtos):
    dtos: list[account_hierarchy_read_dto]
    def __init__(self, dtos: list[account_hierarchy_read_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[account_hierarchy_read_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: account_hierarchy_read_dto):
        return cls(list([dto]))
    @classmethod
    def from_lists(cls, dtos1: list[account_hierarchy_read_dto], dtos2: list[account_hierarchy_read_dto]):
        return cls(dtos1 + dtos2)
    def get_active(self):
        return account_hierarchy_read_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return account_hierarchy_read_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_write_dtos(self) -> list[account_hierarchy_write_dto]:
        return list(map(lambda x: x.to_write(), self.dtos))
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write().to_write_dict(), self.dtos))
    def get_read_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> account_hierarchy_read_dto | None:
        found_dtos = list(filter(lambda x: x.account_hierarchy_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def get_first(self) -> account_hierarchy_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> account_hierarchy_read_dtos:
        if len(self.dtos) > n:
            return account_hierarchy_read_dtos(self.dtos[:n])
        else:
            return account_hierarchy_read_dtos(self.dtos)
    def get_last(self) -> account_hierarchy_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, account_hierarchy_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def to_dict_by_account_hierarchy_uid(self) -> dict[str, account_hierarchy_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.account_hierarchy_uid] = dto
        return d
    def to_dict_by_account_hierarchy_name(self) -> dict[str, account_hierarchy_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.account_hierarchy_name] = dto
        return d
    def to_dict_by_tenant_uid(self) -> dict[str, account_hierarchy_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.tenant_uid] = dto
        return d
    def to_dict_by_parent_account_uid(self) -> dict[str, account_hierarchy_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.parent_account_uid] = dto
        return d
    def to_dict_by_child_account_uid(self) -> dict[str, account_hierarchy_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.child_account_uid] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[account_hierarchy_read_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[account_hierarchy_read_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return init
    def check_any(self, check_method: Callable[[account_hierarchy_read_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return init
    def map_to_string(self, map_method: Callable[[account_hierarchy_read_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[account_hierarchy_read_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[account_hierarchy_read_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, account_hierarchy_read_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, account_hierarchy_read_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, account_hierarchy_read_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[account_hierarchy_read_dto], bool]) -> account_hierarchy_read_dtos:
        return account_hierarchy_read_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[account_hierarchy_read_dto], str]) -> dict[str, account_hierarchy_read_dtos]:
        grp_data: dict[str, account_hierarchy_read_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = account_hierarchy_read_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[account_hierarchy_read_dto], str], agg_method: Callable[[account_hierarchy_read_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, account_hierarchy_read_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[account_hierarchy_read_dto], bool]) -> account_hierarchy_read_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[account_hierarchy_read_dto], any], compare_method: Callable[[any, any], bool]) -> account_hierarchy_read_dto | None:
        if len(self.dtos) == 0:
            return None
        else:
            max_value = value_method(self.dtos[0])
            max_elem = self.dtos[0]
            for dto in self.dtos:
                next_value = value_method(dto)
                if compare_method(next_value, max_value):
                    max_value = next_value
                    max_elem = dto
            return max_elem


@dataclass(frozen=False)
class account_rate_read_dtos(base_read_dtos):
    dtos: list[account_rate_read_dto]
    def __init__(self, dtos: list[account_rate_read_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[account_rate_read_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: account_rate_read_dto):
        return cls(list([dto]))
    @classmethod
    def from_lists(cls, dtos1: list[account_rate_read_dto], dtos2: list[account_rate_read_dto]):
        return cls(dtos1 + dtos2)
    def get_active(self):
        return account_rate_read_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return account_rate_read_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_write_dtos(self) -> list[account_rate_write_dto]:
        return list(map(lambda x: x.to_write(), self.dtos))
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write().to_write_dict(), self.dtos))
    def get_read_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> account_rate_read_dto | None:
        found_dtos = list(filter(lambda x: x.account_rate_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def get_first(self) -> account_rate_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> account_rate_read_dtos:
        if len(self.dtos) > n:
            return account_rate_read_dtos(self.dtos[:n])
        else:
            return account_rate_read_dtos(self.dtos)
    def get_last(self) -> account_rate_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, account_rate_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def to_dict_by_account_rate_uid(self) -> dict[str, account_rate_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.account_rate_uid] = dto
        return d
    def to_dict_by_account_rate_name(self) -> dict[str, account_rate_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.account_rate_name] = dto
        return d
    def to_dict_by_tenant_uid(self) -> dict[str, account_rate_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.tenant_uid] = dto
        return d
    def to_dict_by_account_uid(self) -> dict[str, account_rate_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.account_uid] = dto
        return d
    def to_dict_by_currency_uid(self) -> dict[str, account_rate_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.currency_uid] = dto
        return d
    def to_dict_by_rate(self) -> dict[str, account_rate_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.rate] = dto
        return d
    def to_dict_by_start_date(self) -> dict[str, account_rate_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.start_date] = dto
        return d
    def to_dict_by_end_date(self) -> dict[str, account_rate_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.end_date] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[account_rate_read_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[account_rate_read_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return init
    def check_any(self, check_method: Callable[[account_rate_read_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return init
    def map_to_string(self, map_method: Callable[[account_rate_read_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[account_rate_read_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[account_rate_read_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, account_rate_read_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, account_rate_read_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, account_rate_read_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[account_rate_read_dto], bool]) -> account_rate_read_dtos:
        return account_rate_read_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[account_rate_read_dto], str]) -> dict[str, account_rate_read_dtos]:
        grp_data: dict[str, account_rate_read_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = account_rate_read_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[account_rate_read_dto], str], agg_method: Callable[[account_rate_read_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, account_rate_read_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[account_rate_read_dto], bool]) -> account_rate_read_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[account_rate_read_dto], any], compare_method: Callable[[any, any], bool]) -> account_rate_read_dto | None:
        if len(self.dtos) == 0:
            return None
        else:
            max_value = value_method(self.dtos[0])
            max_elem = self.dtos[0]
            for dto in self.dtos:
                next_value = value_method(dto)
                if compare_method(next_value, max_value):
                    max_value = next_value
                    max_elem = dto
            return max_elem


@dataclass(frozen=False)
class account_skill_read_dtos(base_read_dtos):
    dtos: list[account_skill_read_dto]
    def __init__(self, dtos: list[account_skill_read_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[account_skill_read_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: account_skill_read_dto):
        return cls(list([dto]))
    @classmethod
    def from_lists(cls, dtos1: list[account_skill_read_dto], dtos2: list[account_skill_read_dto]):
        return cls(dtos1 + dtos2)
    def get_active(self):
        return account_skill_read_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return account_skill_read_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_write_dtos(self) -> list[account_skill_write_dto]:
        return list(map(lambda x: x.to_write(), self.dtos))
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write().to_write_dict(), self.dtos))
    def get_read_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> account_skill_read_dto | None:
        found_dtos = list(filter(lambda x: x.account_skill_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def get_first(self) -> account_skill_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> account_skill_read_dtos:
        if len(self.dtos) > n:
            return account_skill_read_dtos(self.dtos[:n])
        else:
            return account_skill_read_dtos(self.dtos)
    def get_last(self) -> account_skill_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, account_skill_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def to_dict_by_account_skill_uid(self) -> dict[str, account_skill_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.account_skill_uid] = dto
        return d
    def to_dict_by_account_skill_name(self) -> dict[str, account_skill_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.account_skill_name] = dto
        return d
    def to_dict_by_account_skill_description(self) -> dict[str, account_skill_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.account_skill_description] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[account_skill_read_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[account_skill_read_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return init
    def check_any(self, check_method: Callable[[account_skill_read_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return init
    def map_to_string(self, map_method: Callable[[account_skill_read_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[account_skill_read_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[account_skill_read_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, account_skill_read_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, account_skill_read_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, account_skill_read_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[account_skill_read_dto], bool]) -> account_skill_read_dtos:
        return account_skill_read_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[account_skill_read_dto], str]) -> dict[str, account_skill_read_dtos]:
        grp_data: dict[str, account_skill_read_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = account_skill_read_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[account_skill_read_dto], str], agg_method: Callable[[account_skill_read_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, account_skill_read_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[account_skill_read_dto], bool]) -> account_skill_read_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[account_skill_read_dto], any], compare_method: Callable[[any, any], bool]) -> account_skill_read_dto | None:
        if len(self.dtos) == 0:
            return None
        else:
            max_value = value_method(self.dtos[0])
            max_elem = self.dtos[0]
            for dto in self.dtos:
                next_value = value_method(dto)
                if compare_method(next_value, max_value):
                    max_value = next_value
                    max_elem = dto
            return max_elem


@dataclass(frozen=False)
class account_team_read_dtos(base_read_dtos):
    dtos: list[account_team_read_dto]
    def __init__(self, dtos: list[account_team_read_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[account_team_read_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: account_team_read_dto):
        return cls(list([dto]))
    @classmethod
    def from_lists(cls, dtos1: list[account_team_read_dto], dtos2: list[account_team_read_dto]):
        return cls(dtos1 + dtos2)
    def get_active(self):
        return account_team_read_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return account_team_read_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_write_dtos(self) -> list[account_team_write_dto]:
        return list(map(lambda x: x.to_write(), self.dtos))
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write().to_write_dict(), self.dtos))
    def get_read_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> account_team_read_dto | None:
        found_dtos = list(filter(lambda x: x.account_team_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def get_first(self) -> account_team_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> account_team_read_dtos:
        if len(self.dtos) > n:
            return account_team_read_dtos(self.dtos[:n])
        else:
            return account_team_read_dtos(self.dtos)
    def get_last(self) -> account_team_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, account_team_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def to_dict_by_account_team_uid(self) -> dict[str, account_team_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.account_team_uid] = dto
        return d
    def to_dict_by_account_team_name(self) -> dict[str, account_team_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.account_team_name] = dto
        return d
    def to_dict_by_tenant_uid(self) -> dict[str, account_team_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.tenant_uid] = dto
        return d
    def to_dict_by_owner_account_uid(self) -> dict[str, account_team_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.owner_account_uid] = dto
        return d
    def to_dict_by_is_public(self) -> dict[str, account_team_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.is_public] = dto
        return d
    def to_dict_by_is_tenant(self) -> dict[str, account_team_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.is_tenant] = dto
        return d
    def to_dict_by_is_private(self) -> dict[str, account_team_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.is_private] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[account_team_read_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[account_team_read_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return init
    def check_any(self, check_method: Callable[[account_team_read_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return init
    def map_to_string(self, map_method: Callable[[account_team_read_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[account_team_read_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[account_team_read_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, account_team_read_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, account_team_read_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, account_team_read_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[account_team_read_dto], bool]) -> account_team_read_dtos:
        return account_team_read_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[account_team_read_dto], str]) -> dict[str, account_team_read_dtos]:
        grp_data: dict[str, account_team_read_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = account_team_read_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[account_team_read_dto], str], agg_method: Callable[[account_team_read_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, account_team_read_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[account_team_read_dto], bool]) -> account_team_read_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[account_team_read_dto], any], compare_method: Callable[[any, any], bool]) -> account_team_read_dto | None:
        if len(self.dtos) == 0:
            return None
        else:
            max_value = value_method(self.dtos[0])
            max_elem = self.dtos[0]
            for dto in self.dtos:
                next_value = value_method(dto)
                if compare_method(next_value, max_value):
                    max_value = next_value
                    max_elem = dto
            return max_elem


@dataclass(frozen=False)
class account_title_read_dtos(base_read_dtos):
    dtos: list[account_title_read_dto]
    def __init__(self, dtos: list[account_title_read_dto]):
        super().__init__(dtos)
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
        return list(map(lambda x: x.to_write(), self.dtos))
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
    def get_first_n(self, n: int) -> account_title_read_dtos:
        if len(self.dtos) > n:
            return account_title_read_dtos(self.dtos[:n])
        else:
            return account_title_read_dtos(self.dtos)
    def get_last(self) -> account_title_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
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
    def to_dict_by_account_title_name(self) -> dict[str, account_title_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.account_title_name] = dto
        return d
    def to_dict_by_title_description(self) -> dict[str, account_title_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.title_description] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[account_title_read_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[account_title_read_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return init
    def check_any(self, check_method: Callable[[account_title_read_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return init
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
    def find(self, check_method: Callable[[account_title_read_dto], bool]) -> account_title_read_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[account_title_read_dto], any], compare_method: Callable[[any, any], bool]) -> account_title_read_dto | None:
        if len(self.dtos) == 0:
            return None
        else:
            max_value = value_method(self.dtos[0])
            max_elem = self.dtos[0]
            for dto in self.dtos:
                next_value = value_method(dto)
                if compare_method(next_value, max_value):
                    max_value = next_value
                    max_elem = dto
            return max_elem


@dataclass(frozen=False)
class account_title_responsibility_read_dtos(base_read_dtos):
    dtos: list[account_title_responsibility_read_dto]
    def __init__(self, dtos: list[account_title_responsibility_read_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[account_title_responsibility_read_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: account_title_responsibility_read_dto):
        return cls(list([dto]))
    @classmethod
    def from_lists(cls, dtos1: list[account_title_responsibility_read_dto], dtos2: list[account_title_responsibility_read_dto]):
        return cls(dtos1 + dtos2)
    def get_active(self):
        return account_title_responsibility_read_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return account_title_responsibility_read_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_write_dtos(self) -> list[account_title_responsibility_write_dto]:
        return list(map(lambda x: x.to_write(), self.dtos))
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write().to_write_dict(), self.dtos))
    def get_read_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> account_title_responsibility_read_dto | None:
        found_dtos = list(filter(lambda x: x.account_title_responsibility_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def get_first(self) -> account_title_responsibility_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> account_title_responsibility_read_dtos:
        if len(self.dtos) > n:
            return account_title_responsibility_read_dtos(self.dtos[:n])
        else:
            return account_title_responsibility_read_dtos(self.dtos)
    def get_last(self) -> account_title_responsibility_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, account_title_responsibility_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def to_dict_by_account_title_responsibility_uid(self) -> dict[str, account_title_responsibility_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.account_title_responsibility_uid] = dto
        return d
    def to_dict_by_account_title_responsibility_name(self) -> dict[str, account_title_responsibility_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.account_title_responsibility_name] = dto
        return d
    def to_dict_by_tenant_uid(self) -> dict[str, account_title_responsibility_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.tenant_uid] = dto
        return d
    def to_dict_by_account_title_uid(self) -> dict[str, account_title_responsibility_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.account_title_uid] = dto
        return d
    def to_dict_by_responsibility_description(self) -> dict[str, account_title_responsibility_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.responsibility_description] = dto
        return d
    def to_dict_by_responsibility_priority(self) -> dict[str, account_title_responsibility_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.responsibility_priority] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[account_title_responsibility_read_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[account_title_responsibility_read_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return init
    def check_any(self, check_method: Callable[[account_title_responsibility_read_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return init
    def map_to_string(self, map_method: Callable[[account_title_responsibility_read_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[account_title_responsibility_read_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[account_title_responsibility_read_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, account_title_responsibility_read_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, account_title_responsibility_read_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, account_title_responsibility_read_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[account_title_responsibility_read_dto], bool]) -> account_title_responsibility_read_dtos:
        return account_title_responsibility_read_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[account_title_responsibility_read_dto], str]) -> dict[str, account_title_responsibility_read_dtos]:
        grp_data: dict[str, account_title_responsibility_read_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = account_title_responsibility_read_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[account_title_responsibility_read_dto], str], agg_method: Callable[[account_title_responsibility_read_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, account_title_responsibility_read_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[account_title_responsibility_read_dto], bool]) -> account_title_responsibility_read_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[account_title_responsibility_read_dto], any], compare_method: Callable[[any, any], bool]) -> account_title_responsibility_read_dto | None:
        if len(self.dtos) == 0:
            return None
        else:
            max_value = value_method(self.dtos[0])
            max_elem = self.dtos[0]
            for dto in self.dtos:
                next_value = value_method(dto)
                if compare_method(next_value, max_value):
                    max_value = next_value
                    max_elem = dto
            return max_elem


@dataclass(frozen=False)
class account_type_read_dtos(base_read_dtos):
    dtos: list[account_type_read_dto]
    def __init__(self, dtos: list[account_type_read_dto]):
        super().__init__(dtos)
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
        return list(map(lambda x: x.to_write(), self.dtos))
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
    def get_first_n(self, n: int) -> account_type_read_dtos:
        if len(self.dtos) > n:
            return account_type_read_dtos(self.dtos[:n])
        else:
            return account_type_read_dtos(self.dtos)
    def get_last(self) -> account_type_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
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
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[account_type_read_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[account_type_read_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return init
    def check_any(self, check_method: Callable[[account_type_read_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return init
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
    def find(self, check_method: Callable[[account_type_read_dto], bool]) -> account_type_read_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[account_type_read_dto], any], compare_method: Callable[[any, any], bool]) -> account_type_read_dto | None:
        if len(self.dtos) == 0:
            return None
        else:
            max_value = value_method(self.dtos[0])
            max_elem = self.dtos[0]
            for dto in self.dtos:
                next_value = value_method(dto)
                if compare_method(next_value, max_value):
                    max_value = next_value
                    max_elem = dto
            return max_elem


@dataclass(frozen=False)
class audit_change_read_dtos(base_read_dtos):
    dtos: list[audit_change_read_dto]
    def __init__(self, dtos: list[audit_change_read_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[audit_change_read_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: audit_change_read_dto):
        return cls(list([dto]))
    @classmethod
    def from_lists(cls, dtos1: list[audit_change_read_dto], dtos2: list[audit_change_read_dto]):
        return cls(dtos1 + dtos2)
    def get_active(self):
        return audit_change_read_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return audit_change_read_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_write_dtos(self) -> list[audit_change_write_dto]:
        return list(map(lambda x: x.to_write(), self.dtos))
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write().to_write_dict(), self.dtos))
    def get_read_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> audit_change_read_dto | None:
        found_dtos = list(filter(lambda x: x.audit_change_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def get_first(self) -> audit_change_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> audit_change_read_dtos:
        if len(self.dtos) > n:
            return audit_change_read_dtos(self.dtos[:n])
        else:
            return audit_change_read_dtos(self.dtos)
    def get_last(self) -> audit_change_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, audit_change_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def to_dict_by_system_change_uid(self) -> dict[str, audit_change_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.system_change_uid] = dto
        return d
    def to_dict_by_system_change_name(self) -> dict[str, audit_change_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.system_change_name] = dto
        return d
    def to_dict_by_account_uid(self) -> dict[str, audit_change_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.account_uid] = dto
        return d
    def to_dict_by_audit_type_uid(self) -> dict[str, audit_change_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.audit_type_uid] = dto
        return d
    def to_dict_by_change_type(self) -> dict[str, audit_change_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.change_type] = dto
        return d
    def to_dict_by_change_json(self) -> dict[str, audit_change_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.change_json] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[audit_change_read_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[audit_change_read_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return init
    def check_any(self, check_method: Callable[[audit_change_read_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return init
    def map_to_string(self, map_method: Callable[[audit_change_read_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[audit_change_read_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[audit_change_read_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, audit_change_read_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, audit_change_read_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, audit_change_read_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[audit_change_read_dto], bool]) -> audit_change_read_dtos:
        return audit_change_read_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[audit_change_read_dto], str]) -> dict[str, audit_change_read_dtos]:
        grp_data: dict[str, audit_change_read_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = audit_change_read_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[audit_change_read_dto], str], agg_method: Callable[[audit_change_read_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, audit_change_read_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[audit_change_read_dto], bool]) -> audit_change_read_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[audit_change_read_dto], any], compare_method: Callable[[any, any], bool]) -> audit_change_read_dto | None:
        if len(self.dtos) == 0:
            return None
        else:
            max_value = value_method(self.dtos[0])
            max_elem = self.dtos[0]
            for dto in self.dtos:
                next_value = value_method(dto)
                if compare_method(next_value, max_value):
                    max_value = next_value
                    max_elem = dto
            return max_elem


@dataclass(frozen=False)
class audit_type_read_dtos(base_read_dtos):
    dtos: list[audit_type_read_dto]
    def __init__(self, dtos: list[audit_type_read_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[audit_type_read_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: audit_type_read_dto):
        return cls(list([dto]))
    @classmethod
    def from_lists(cls, dtos1: list[audit_type_read_dto], dtos2: list[audit_type_read_dto]):
        return cls(dtos1 + dtos2)
    def get_active(self):
        return audit_type_read_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return audit_type_read_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_write_dtos(self) -> list[audit_type_write_dto]:
        return list(map(lambda x: x.to_write(), self.dtos))
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write().to_write_dict(), self.dtos))
    def get_read_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> audit_type_read_dto | None:
        found_dtos = list(filter(lambda x: x.audit_type_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def get_first(self) -> audit_type_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> audit_type_read_dtos:
        if len(self.dtos) > n:
            return audit_type_read_dtos(self.dtos[:n])
        else:
            return audit_type_read_dtos(self.dtos)
    def get_last(self) -> audit_type_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, audit_type_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def to_dict_by_audit_type_uid(self) -> dict[str, audit_type_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.audit_type_uid] = dto
        return d
    def to_dict_by_audit_type_name(self) -> dict[str, audit_type_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.audit_type_name] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[audit_type_read_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[audit_type_read_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return init
    def check_any(self, check_method: Callable[[audit_type_read_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return init
    def map_to_string(self, map_method: Callable[[audit_type_read_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[audit_type_read_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[audit_type_read_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, audit_type_read_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, audit_type_read_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, audit_type_read_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[audit_type_read_dto], bool]) -> audit_type_read_dtos:
        return audit_type_read_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[audit_type_read_dto], str]) -> dict[str, audit_type_read_dtos]:
        grp_data: dict[str, audit_type_read_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = audit_type_read_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[audit_type_read_dto], str], agg_method: Callable[[audit_type_read_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, audit_type_read_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[audit_type_read_dto], bool]) -> audit_type_read_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[audit_type_read_dto], any], compare_method: Callable[[any, any], bool]) -> audit_type_read_dto | None:
        if len(self.dtos) == 0:
            return None
        else:
            max_value = value_method(self.dtos[0])
            max_elem = self.dtos[0]
            for dto in self.dtos:
                next_value = value_method(dto)
                if compare_method(next_value, max_value):
                    max_value = next_value
                    max_elem = dto
            return max_elem


@dataclass(frozen=False)
class auth_attempt_read_dtos(base_read_dtos):
    dtos: list[auth_attempt_read_dto]
    def __init__(self, dtos: list[auth_attempt_read_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[auth_attempt_read_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: auth_attempt_read_dto):
        return cls(list([dto]))
    @classmethod
    def from_lists(cls, dtos1: list[auth_attempt_read_dto], dtos2: list[auth_attempt_read_dto]):
        return cls(dtos1 + dtos2)
    def get_active(self):
        return auth_attempt_read_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return auth_attempt_read_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_write_dtos(self) -> list[auth_attempt_write_dto]:
        return list(map(lambda x: x.to_write(), self.dtos))
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write().to_write_dict(), self.dtos))
    def get_read_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> auth_attempt_read_dto | None:
        found_dtos = list(filter(lambda x: x.auth_attempt_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def get_first(self) -> auth_attempt_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> auth_attempt_read_dtos:
        if len(self.dtos) > n:
            return auth_attempt_read_dtos(self.dtos[:n])
        else:
            return auth_attempt_read_dtos(self.dtos)
    def get_last(self) -> auth_attempt_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, auth_attempt_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def to_dict_by_auth_attempt_uid(self) -> dict[str, auth_attempt_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.auth_attempt_uid] = dto
        return d
    def to_dict_by_auth_attempt_name(self) -> dict[str, auth_attempt_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.auth_attempt_name] = dto
        return d
    def to_dict_by_tenant_uid(self) -> dict[str, auth_attempt_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.tenant_uid] = dto
        return d
    def to_dict_by_account_uid(self) -> dict[str, auth_attempt_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.account_uid] = dto
        return d
    def to_dict_by_account_login(self) -> dict[str, auth_attempt_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.account_login] = dto
        return d
    def to_dict_by_identity_type(self) -> dict[str, auth_attempt_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.identity_type] = dto
        return d
    def to_dict_by_identity_parameters(self) -> dict[str, auth_attempt_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.identity_parameters] = dto
        return d
    def to_dict_by_last_status_name(self) -> dict[str, auth_attempt_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.last_status_name] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[auth_attempt_read_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[auth_attempt_read_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return init
    def check_any(self, check_method: Callable[[auth_attempt_read_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return init
    def map_to_string(self, map_method: Callable[[auth_attempt_read_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[auth_attempt_read_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[auth_attempt_read_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, auth_attempt_read_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, auth_attempt_read_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, auth_attempt_read_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[auth_attempt_read_dto], bool]) -> auth_attempt_read_dtos:
        return auth_attempt_read_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[auth_attempt_read_dto], str]) -> dict[str, auth_attempt_read_dtos]:
        grp_data: dict[str, auth_attempt_read_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = auth_attempt_read_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[auth_attempt_read_dto], str], agg_method: Callable[[auth_attempt_read_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, auth_attempt_read_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[auth_attempt_read_dto], bool]) -> auth_attempt_read_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[auth_attempt_read_dto], any], compare_method: Callable[[any, any], bool]) -> auth_attempt_read_dto | None:
        if len(self.dtos) == 0:
            return None
        else:
            max_value = value_method(self.dtos[0])
            max_elem = self.dtos[0]
            for dto in self.dtos:
                next_value = value_method(dto)
                if compare_method(next_value, max_value):
                    max_value = next_value
                    max_elem = dto
            return max_elem


@dataclass(frozen=False)
class auth_identity_read_dtos(base_read_dtos):
    dtos: list[auth_identity_read_dto]
    def __init__(self, dtos: list[auth_identity_read_dto]):
        super().__init__(dtos)
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
        return list(map(lambda x: x.to_write(), self.dtos))
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
    def get_first_n(self, n: int) -> auth_identity_read_dtos:
        if len(self.dtos) > n:
            return auth_identity_read_dtos(self.dtos[:n])
        else:
            return auth_identity_read_dtos(self.dtos)
    def get_last(self) -> auth_identity_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
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
    def to_dict_by_auth_identity_name(self) -> dict[str, auth_identity_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.auth_identity_name] = dto
        return d
    def to_dict_by_class_name(self) -> dict[str, auth_identity_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.class_name] = dto
        return d
    def to_dict_by_default_parameters_json(self) -> dict[str, auth_identity_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.default_parameters_json] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[auth_identity_read_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[auth_identity_read_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return init
    def check_any(self, check_method: Callable[[auth_identity_read_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return init
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
    def find(self, check_method: Callable[[auth_identity_read_dto], bool]) -> auth_identity_read_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[auth_identity_read_dto], any], compare_method: Callable[[any, any], bool]) -> auth_identity_read_dto | None:
        if len(self.dtos) == 0:
            return None
        else:
            max_value = value_method(self.dtos[0])
            max_elem = self.dtos[0]
            for dto in self.dtos:
                next_value = value_method(dto)
                if compare_method(next_value, max_value):
                    max_value = next_value
                    max_elem = dto
            return max_elem


@dataclass(frozen=False)
class auth_identity_tenant_read_dtos(base_read_dtos):
    dtos: list[auth_identity_tenant_read_dto]
    def __init__(self, dtos: list[auth_identity_tenant_read_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[auth_identity_tenant_read_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: auth_identity_tenant_read_dto):
        return cls(list([dto]))
    @classmethod
    def from_lists(cls, dtos1: list[auth_identity_tenant_read_dto], dtos2: list[auth_identity_tenant_read_dto]):
        return cls(dtos1 + dtos2)
    def get_active(self):
        return auth_identity_tenant_read_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return auth_identity_tenant_read_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_write_dtos(self) -> list[auth_identity_tenant_write_dto]:
        return list(map(lambda x: x.to_write(), self.dtos))
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write().to_write_dict(), self.dtos))
    def get_read_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> auth_identity_tenant_read_dto | None:
        found_dtos = list(filter(lambda x: x.auth_identity_tenant_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def get_first(self) -> auth_identity_tenant_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> auth_identity_tenant_read_dtos:
        if len(self.dtos) > n:
            return auth_identity_tenant_read_dtos(self.dtos[:n])
        else:
            return auth_identity_tenant_read_dtos(self.dtos)
    def get_last(self) -> auth_identity_tenant_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, auth_identity_tenant_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def to_dict_by_auth_identity_tenant_uid(self) -> dict[str, auth_identity_tenant_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.auth_identity_tenant_uid] = dto
        return d
    def to_dict_by_auth_identity_tenant_name(self) -> dict[str, auth_identity_tenant_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.auth_identity_tenant_name] = dto
        return d
    def to_dict_by_tenant_uid(self) -> dict[str, auth_identity_tenant_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.tenant_uid] = dto
        return d
    def to_dict_by_auth_identity_uid(self) -> dict[str, auth_identity_tenant_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.auth_identity_uid] = dto
        return d
    def to_dict_by_auth_sso_uid(self) -> dict[str, auth_identity_tenant_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.auth_sso_uid] = dto
        return d
    def to_dict_by_identity_parameters_json(self) -> dict[str, auth_identity_tenant_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.identity_parameters_json] = dto
        return d
    def to_dict_by_last_status_name(self) -> dict[str, auth_identity_tenant_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.last_status_name] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[auth_identity_tenant_read_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[auth_identity_tenant_read_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return init
    def check_any(self, check_method: Callable[[auth_identity_tenant_read_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return init
    def map_to_string(self, map_method: Callable[[auth_identity_tenant_read_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[auth_identity_tenant_read_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[auth_identity_tenant_read_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, auth_identity_tenant_read_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, auth_identity_tenant_read_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, auth_identity_tenant_read_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[auth_identity_tenant_read_dto], bool]) -> auth_identity_tenant_read_dtos:
        return auth_identity_tenant_read_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[auth_identity_tenant_read_dto], str]) -> dict[str, auth_identity_tenant_read_dtos]:
        grp_data: dict[str, auth_identity_tenant_read_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = auth_identity_tenant_read_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[auth_identity_tenant_read_dto], str], agg_method: Callable[[auth_identity_tenant_read_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, auth_identity_tenant_read_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[auth_identity_tenant_read_dto], bool]) -> auth_identity_tenant_read_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[auth_identity_tenant_read_dto], any], compare_method: Callable[[any, any], bool]) -> auth_identity_tenant_read_dto | None:
        if len(self.dtos) == 0:
            return None
        else:
            max_value = value_method(self.dtos[0])
            max_elem = self.dtos[0]
            for dto in self.dtos:
                next_value = value_method(dto)
                if compare_method(next_value, max_value):
                    max_value = next_value
                    max_elem = dto
            return max_elem


@dataclass(frozen=False)
class auth_key_read_dtos(base_read_dtos):
    dtos: list[auth_key_read_dto]
    def __init__(self, dtos: list[auth_key_read_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[auth_key_read_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: auth_key_read_dto):
        return cls(list([dto]))
    @classmethod
    def from_lists(cls, dtos1: list[auth_key_read_dto], dtos2: list[auth_key_read_dto]):
        return cls(dtos1 + dtos2)
    def get_active(self):
        return auth_key_read_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return auth_key_read_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_write_dtos(self) -> list[auth_key_write_dto]:
        return list(map(lambda x: x.to_write(), self.dtos))
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write().to_write_dict(), self.dtos))
    def get_read_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> auth_key_read_dto | None:
        found_dtos = list(filter(lambda x: x.auth_key_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def get_first(self) -> auth_key_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> auth_key_read_dtos:
        if len(self.dtos) > n:
            return auth_key_read_dtos(self.dtos[:n])
        else:
            return auth_key_read_dtos(self.dtos)
    def get_last(self) -> auth_key_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, auth_key_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def to_dict_by_auth_key_uid(self) -> dict[str, auth_key_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.auth_key_uid] = dto
        return d
    def to_dict_by_auth_key_name(self) -> dict[str, auth_key_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.auth_key_name] = dto
        return d
    def to_dict_by_tenant_uid(self) -> dict[str, auth_key_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.tenant_uid] = dto
        return d
    def to_dict_by_owner_account_uid(self) -> dict[str, auth_key_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.owner_account_uid] = dto
        return d
    def to_dict_by_auth_key_type_uid(self) -> dict[str, auth_key_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.auth_key_type_uid] = dto
        return d
    def to_dict_by_key_private(self) -> dict[str, auth_key_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.key_private] = dto
        return d
    def to_dict_by_key_public(self) -> dict[str, auth_key_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.key_public] = dto
        return d
    def to_dict_by_key_length(self) -> dict[str, auth_key_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.key_length] = dto
        return d
    def to_dict_by_key_exponent(self) -> dict[str, auth_key_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.key_exponent] = dto
        return d
    def to_dict_by_key_modulus(self) -> dict[str, auth_key_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.key_modulus] = dto
        return d
    def to_dict_by_key_parameters_json(self) -> dict[str, auth_key_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.key_parameters_json] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[auth_key_read_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[auth_key_read_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return init
    def check_any(self, check_method: Callable[[auth_key_read_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return init
    def map_to_string(self, map_method: Callable[[auth_key_read_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[auth_key_read_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[auth_key_read_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, auth_key_read_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, auth_key_read_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, auth_key_read_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[auth_key_read_dto], bool]) -> auth_key_read_dtos:
        return auth_key_read_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[auth_key_read_dto], str]) -> dict[str, auth_key_read_dtos]:
        grp_data: dict[str, auth_key_read_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = auth_key_read_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[auth_key_read_dto], str], agg_method: Callable[[auth_key_read_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, auth_key_read_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[auth_key_read_dto], bool]) -> auth_key_read_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[auth_key_read_dto], any], compare_method: Callable[[any, any], bool]) -> auth_key_read_dto | None:
        if len(self.dtos) == 0:
            return None
        else:
            max_value = value_method(self.dtos[0])
            max_elem = self.dtos[0]
            for dto in self.dtos:
                next_value = value_method(dto)
                if compare_method(next_value, max_value):
                    max_value = next_value
                    max_elem = dto
            return max_elem


@dataclass(frozen=False)
class auth_key_type_read_dtos(base_read_dtos):
    dtos: list[auth_key_type_read_dto]
    def __init__(self, dtos: list[auth_key_type_read_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[auth_key_type_read_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: auth_key_type_read_dto):
        return cls(list([dto]))
    @classmethod
    def from_lists(cls, dtos1: list[auth_key_type_read_dto], dtos2: list[auth_key_type_read_dto]):
        return cls(dtos1 + dtos2)
    def get_active(self):
        return auth_key_type_read_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return auth_key_type_read_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_write_dtos(self) -> list[auth_key_type_write_dto]:
        return list(map(lambda x: x.to_write(), self.dtos))
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write().to_write_dict(), self.dtos))
    def get_read_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> auth_key_type_read_dto | None:
        found_dtos = list(filter(lambda x: x.auth_key_type_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def get_first(self) -> auth_key_type_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> auth_key_type_read_dtos:
        if len(self.dtos) > n:
            return auth_key_type_read_dtos(self.dtos[:n])
        else:
            return auth_key_type_read_dtos(self.dtos)
    def get_last(self) -> auth_key_type_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, auth_key_type_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def to_dict_by_auth_key_type_uid(self) -> dict[str, auth_key_type_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.auth_key_type_uid] = dto
        return d
    def to_dict_by_auth_key_type_name(self) -> dict[str, auth_key_type_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.auth_key_type_name] = dto
        return d
    def to_dict_by_class_name(self) -> dict[str, auth_key_type_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.class_name] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[auth_key_type_read_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[auth_key_type_read_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return init
    def check_any(self, check_method: Callable[[auth_key_type_read_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return init
    def map_to_string(self, map_method: Callable[[auth_key_type_read_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[auth_key_type_read_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[auth_key_type_read_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, auth_key_type_read_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, auth_key_type_read_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, auth_key_type_read_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[auth_key_type_read_dto], bool]) -> auth_key_type_read_dtos:
        return auth_key_type_read_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[auth_key_type_read_dto], str]) -> dict[str, auth_key_type_read_dtos]:
        grp_data: dict[str, auth_key_type_read_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = auth_key_type_read_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[auth_key_type_read_dto], str], agg_method: Callable[[auth_key_type_read_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, auth_key_type_read_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[auth_key_type_read_dto], bool]) -> auth_key_type_read_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[auth_key_type_read_dto], any], compare_method: Callable[[any, any], bool]) -> auth_key_type_read_dto | None:
        if len(self.dtos) == 0:
            return None
        else:
            max_value = value_method(self.dtos[0])
            max_elem = self.dtos[0]
            for dto in self.dtos:
                next_value = value_method(dto)
                if compare_method(next_value, max_value):
                    max_value = next_value
                    max_elem = dto
            return max_elem


@dataclass(frozen=False)
class auth_password_read_dtos(base_read_dtos):
    dtos: list[auth_password_read_dto]
    def __init__(self, dtos: list[auth_password_read_dto]):
        super().__init__(dtos)
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
        return list(map(lambda x: x.to_write(), self.dtos))
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
    def get_first_n(self, n: int) -> auth_password_read_dtos:
        if len(self.dtos) > n:
            return auth_password_read_dtos(self.dtos[:n])
        else:
            return auth_password_read_dtos(self.dtos)
    def get_last(self) -> auth_password_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
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
    def to_dict_by_auth_password_name(self) -> dict[str, auth_password_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.auth_password_name] = dto
        return d
    def to_dict_by_tenant_uid(self) -> dict[str, auth_password_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.tenant_uid] = dto
        return d
    def to_dict_by_account_uid(self) -> dict[str, auth_password_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.account_uid] = dto
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
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[auth_password_read_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[auth_password_read_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return init
    def check_any(self, check_method: Callable[[auth_password_read_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return init
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
    def find(self, check_method: Callable[[auth_password_read_dto], bool]) -> auth_password_read_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[auth_password_read_dto], any], compare_method: Callable[[any, any], bool]) -> auth_password_read_dto | None:
        if len(self.dtos) == 0:
            return None
        else:
            max_value = value_method(self.dtos[0])
            max_elem = self.dtos[0]
            for dto in self.dtos:
                next_value = value_method(dto)
                if compare_method(next_value, max_value):
                    max_value = next_value
                    max_elem = dto
            return max_elem


@dataclass(frozen=False)
class auth_password_current_read_dtos(base_read_dtos):
    dtos: list[auth_password_current_read_dto]
    def __init__(self, dtos: list[auth_password_current_read_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[auth_password_current_read_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: auth_password_current_read_dto):
        return cls(list([dto]))
    @classmethod
    def from_lists(cls, dtos1: list[auth_password_current_read_dto], dtos2: list[auth_password_current_read_dto]):
        return cls(dtos1 + dtos2)
    def get_active(self):
        return auth_password_current_read_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return auth_password_current_read_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_write_dtos(self) -> list[auth_password_current_write_dto]:
        return list(map(lambda x: x.to_write(), self.dtos))
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write().to_write_dict(), self.dtos))
    def get_read_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> auth_password_current_read_dto | None:
        found_dtos = list(filter(lambda x: x.auth_password_current_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def get_first(self) -> auth_password_current_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> auth_password_current_read_dtos:
        if len(self.dtos) > n:
            return auth_password_current_read_dtos(self.dtos[:n])
        else:
            return auth_password_current_read_dtos(self.dtos)
    def get_last(self) -> auth_password_current_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, auth_password_current_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def to_dict_by_auth_password_current_uid(self) -> dict[str, auth_password_current_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.auth_password_current_uid] = dto
        return d
    def to_dict_by_auth_password_current_name(self) -> dict[str, auth_password_current_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.auth_password_current_name] = dto
        return d
    def to_dict_by_tenant_uid(self) -> dict[str, auth_password_current_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.tenant_uid] = dto
        return d
    def to_dict_by_account_uid(self) -> dict[str, auth_password_current_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.account_uid] = dto
        return d
    def to_dict_by_password_hash(self) -> dict[str, auth_password_current_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.password_hash] = dto
        return d
    def to_dict_by_password_salt(self) -> dict[str, auth_password_current_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.password_salt] = dto
        return d
    def to_dict_by_date_from(self) -> dict[str, auth_password_current_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.date_from] = dto
        return d
    def to_dict_by_date_to(self) -> dict[str, auth_password_current_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.date_to] = dto
        return d
    def to_dict_by_usage_count(self) -> dict[str, auth_password_current_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.usage_count] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[auth_password_current_read_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[auth_password_current_read_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return init
    def check_any(self, check_method: Callable[[auth_password_current_read_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return init
    def map_to_string(self, map_method: Callable[[auth_password_current_read_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[auth_password_current_read_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[auth_password_current_read_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, auth_password_current_read_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, auth_password_current_read_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, auth_password_current_read_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[auth_password_current_read_dto], bool]) -> auth_password_current_read_dtos:
        return auth_password_current_read_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[auth_password_current_read_dto], str]) -> dict[str, auth_password_current_read_dtos]:
        grp_data: dict[str, auth_password_current_read_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = auth_password_current_read_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[auth_password_current_read_dto], str], agg_method: Callable[[auth_password_current_read_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, auth_password_current_read_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[auth_password_current_read_dto], bool]) -> auth_password_current_read_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[auth_password_current_read_dto], any], compare_method: Callable[[any, any], bool]) -> auth_password_current_read_dto | None:
        if len(self.dtos) == 0:
            return None
        else:
            max_value = value_method(self.dtos[0])
            max_elem = self.dtos[0]
            for dto in self.dtos:
                next_value = value_method(dto)
                if compare_method(next_value, max_value):
                    max_value = next_value
                    max_elem = dto
            return max_elem


@dataclass(frozen=False)
class auth_password_rule_read_dtos(base_read_dtos):
    dtos: list[auth_password_rule_read_dto]
    def __init__(self, dtos: list[auth_password_rule_read_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[auth_password_rule_read_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: auth_password_rule_read_dto):
        return cls(list([dto]))
    @classmethod
    def from_lists(cls, dtos1: list[auth_password_rule_read_dto], dtos2: list[auth_password_rule_read_dto]):
        return cls(dtos1 + dtos2)
    def get_active(self):
        return auth_password_rule_read_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return auth_password_rule_read_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_write_dtos(self) -> list[auth_password_rule_write_dto]:
        return list(map(lambda x: x.to_write(), self.dtos))
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write().to_write_dict(), self.dtos))
    def get_read_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> auth_password_rule_read_dto | None:
        found_dtos = list(filter(lambda x: x.auth_password_rule_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def get_first(self) -> auth_password_rule_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> auth_password_rule_read_dtos:
        if len(self.dtos) > n:
            return auth_password_rule_read_dtos(self.dtos[:n])
        else:
            return auth_password_rule_read_dtos(self.dtos)
    def get_last(self) -> auth_password_rule_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, auth_password_rule_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def to_dict_by_auth_password_uid(self) -> dict[str, auth_password_rule_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.auth_password_uid] = dto
        return d
    def to_dict_by_auth_password_name(self) -> dict[str, auth_password_rule_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.auth_password_name] = dto
        return d
    def to_dict_by_rule_type(self) -> dict[str, auth_password_rule_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.rule_type] = dto
        return d
    def to_dict_by_rule_parameters(self) -> dict[str, auth_password_rule_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.rule_parameters] = dto
        return d
    def to_dict_by_user_scope(self) -> dict[str, auth_password_rule_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.user_scope] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[auth_password_rule_read_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[auth_password_rule_read_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return init
    def check_any(self, check_method: Callable[[auth_password_rule_read_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return init
    def map_to_string(self, map_method: Callable[[auth_password_rule_read_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[auth_password_rule_read_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[auth_password_rule_read_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, auth_password_rule_read_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, auth_password_rule_read_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, auth_password_rule_read_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[auth_password_rule_read_dto], bool]) -> auth_password_rule_read_dtos:
        return auth_password_rule_read_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[auth_password_rule_read_dto], str]) -> dict[str, auth_password_rule_read_dtos]:
        grp_data: dict[str, auth_password_rule_read_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = auth_password_rule_read_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[auth_password_rule_read_dto], str], agg_method: Callable[[auth_password_rule_read_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, auth_password_rule_read_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[auth_password_rule_read_dto], bool]) -> auth_password_rule_read_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[auth_password_rule_read_dto], any], compare_method: Callable[[any, any], bool]) -> auth_password_rule_read_dto | None:
        if len(self.dtos) == 0:
            return None
        else:
            max_value = value_method(self.dtos[0])
            max_elem = self.dtos[0]
            for dto in self.dtos:
                next_value = value_method(dto)
                if compare_method(next_value, max_value):
                    max_value = next_value
                    max_elem = dto
            return max_elem


@dataclass(frozen=False)
class auth_permission_read_dtos(base_read_dtos):
    dtos: list[auth_permission_read_dto]
    def __init__(self, dtos: list[auth_permission_read_dto]):
        super().__init__(dtos)
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
        return list(map(lambda x: x.to_write(), self.dtos))
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
    def get_first_n(self, n: int) -> auth_permission_read_dtos:
        if len(self.dtos) > n:
            return auth_permission_read_dtos(self.dtos[:n])
        else:
            return auth_permission_read_dtos(self.dtos)
    def get_last(self) -> auth_permission_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
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
    def to_dict_by_auth_permission_name(self) -> dict[str, auth_permission_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.auth_permission_name] = dto
        return d
    def to_dict_by_tenant_uid(self) -> dict[str, auth_permission_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.tenant_uid] = dto
        return d
    def to_dict_by_account_uid(self) -> dict[str, auth_permission_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.account_uid] = dto
        return d
    def to_dict_by_auth_role_uid(self) -> dict[str, auth_permission_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.auth_role_uid] = dto
        return d
    def to_dict_by_client_uid(self) -> dict[str, auth_permission_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.client_uid] = dto
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
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[auth_permission_read_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[auth_permission_read_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return init
    def check_any(self, check_method: Callable[[auth_permission_read_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return init
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
    def find(self, check_method: Callable[[auth_permission_read_dto], bool]) -> auth_permission_read_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[auth_permission_read_dto], any], compare_method: Callable[[any, any], bool]) -> auth_permission_read_dto | None:
        if len(self.dtos) == 0:
            return None
        else:
            max_value = value_method(self.dtos[0])
            max_elem = self.dtos[0]
            for dto in self.dtos:
                next_value = value_method(dto)
                if compare_method(next_value, max_value):
                    max_value = next_value
                    max_elem = dto
            return max_elem


@dataclass(frozen=False)
class auth_request_read_dtos(base_read_dtos):
    dtos: list[auth_request_read_dto]
    def __init__(self, dtos: list[auth_request_read_dto]):
        super().__init__(dtos)
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
        return list(map(lambda x: x.to_write(), self.dtos))
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
    def get_first_n(self, n: int) -> auth_request_read_dtos:
        if len(self.dtos) > n:
            return auth_request_read_dtos(self.dtos[:n])
        else:
            return auth_request_read_dtos(self.dtos)
    def get_last(self) -> auth_request_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
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
    def to_dict_by_auth_request_name(self) -> dict[str, auth_request_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.auth_request_name] = dto
        return d
    def to_dict_by_tenant_uid(self) -> dict[str, auth_request_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.tenant_uid] = dto
        return d
    def to_dict_by_account_uid(self) -> dict[str, auth_request_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.account_uid] = dto
        return d
    def to_dict_by_requestor_email(self) -> dict[str, auth_request_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.requestor_email] = dto
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
    def to_dict_by_event_notification_uid(self) -> dict[str, auth_request_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.event_notification_uid] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[auth_request_read_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[auth_request_read_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return init
    def check_any(self, check_method: Callable[[auth_request_read_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return init
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
    def find(self, check_method: Callable[[auth_request_read_dto], bool]) -> auth_request_read_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[auth_request_read_dto], any], compare_method: Callable[[any, any], bool]) -> auth_request_read_dto | None:
        if len(self.dtos) == 0:
            return None
        else:
            max_value = value_method(self.dtos[0])
            max_elem = self.dtos[0]
            for dto in self.dtos:
                next_value = value_method(dto)
                if compare_method(next_value, max_value):
                    max_value = next_value
                    max_elem = dto
            return max_elem


@dataclass(frozen=False)
class auth_role_read_dtos(base_read_dtos):
    dtos: list[auth_role_read_dto]
    def __init__(self, dtos: list[auth_role_read_dto]):
        super().__init__(dtos)
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
        return list(map(lambda x: x.to_write(), self.dtos))
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
    def get_first_n(self, n: int) -> auth_role_read_dtos:
        if len(self.dtos) > n:
            return auth_role_read_dtos(self.dtos[:n])
        else:
            return auth_role_read_dtos(self.dtos)
    def get_last(self) -> auth_role_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
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
    def to_dict_by_auth_role_name(self) -> dict[str, auth_role_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.auth_role_name] = dto
        return d
    def to_dict_by_parent_auth_role_uid(self) -> dict[str, auth_role_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.parent_auth_role_uid] = dto
        return d
    def to_dict_by_tenant_uid(self) -> dict[str, auth_role_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.tenant_uid] = dto
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
    def to_dict_by_is_tenant(self) -> dict[str, auth_role_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.is_tenant] = dto
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
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[auth_role_read_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[auth_role_read_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return init
    def check_any(self, check_method: Callable[[auth_role_read_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return init
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
    def find(self, check_method: Callable[[auth_role_read_dto], bool]) -> auth_role_read_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[auth_role_read_dto], any], compare_method: Callable[[any, any], bool]) -> auth_role_read_dto | None:
        if len(self.dtos) == 0:
            return None
        else:
            max_value = value_method(self.dtos[0])
            max_elem = self.dtos[0]
            for dto in self.dtos:
                next_value = value_method(dto)
                if compare_method(next_value, max_value):
                    max_value = next_value
                    max_elem = dto
            return max_elem


@dataclass(frozen=False)
class auth_role_uri_read_dtos(base_read_dtos):
    dtos: list[auth_role_uri_read_dto]
    def __init__(self, dtos: list[auth_role_uri_read_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[auth_role_uri_read_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: auth_role_uri_read_dto):
        return cls(list([dto]))
    @classmethod
    def from_lists(cls, dtos1: list[auth_role_uri_read_dto], dtos2: list[auth_role_uri_read_dto]):
        return cls(dtos1 + dtos2)
    def get_active(self):
        return auth_role_uri_read_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return auth_role_uri_read_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_write_dtos(self) -> list[auth_role_uri_write_dto]:
        return list(map(lambda x: x.to_write(), self.dtos))
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write().to_write_dict(), self.dtos))
    def get_read_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> auth_role_uri_read_dto | None:
        found_dtos = list(filter(lambda x: x.auth_role_uri_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def get_first(self) -> auth_role_uri_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> auth_role_uri_read_dtos:
        if len(self.dtos) > n:
            return auth_role_uri_read_dtos(self.dtos[:n])
        else:
            return auth_role_uri_read_dtos(self.dtos)
    def get_last(self) -> auth_role_uri_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, auth_role_uri_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def to_dict_by_auth_role_uri_uid(self) -> dict[str, auth_role_uri_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.auth_role_uri_uid] = dto
        return d
    def to_dict_by_auth_role_uri_name(self) -> dict[str, auth_role_uri_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.auth_role_uri_name] = dto
        return d
    def to_dict_by_auth_role_uid(self) -> dict[str, auth_role_uri_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.auth_role_uid] = dto
        return d
    def to_dict_by_uri(self) -> dict[str, auth_role_uri_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.uri] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[auth_role_uri_read_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[auth_role_uri_read_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return init
    def check_any(self, check_method: Callable[[auth_role_uri_read_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return init
    def map_to_string(self, map_method: Callable[[auth_role_uri_read_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[auth_role_uri_read_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[auth_role_uri_read_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, auth_role_uri_read_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, auth_role_uri_read_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, auth_role_uri_read_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[auth_role_uri_read_dto], bool]) -> auth_role_uri_read_dtos:
        return auth_role_uri_read_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[auth_role_uri_read_dto], str]) -> dict[str, auth_role_uri_read_dtos]:
        grp_data: dict[str, auth_role_uri_read_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = auth_role_uri_read_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[auth_role_uri_read_dto], str], agg_method: Callable[[auth_role_uri_read_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, auth_role_uri_read_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[auth_role_uri_read_dto], bool]) -> auth_role_uri_read_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[auth_role_uri_read_dto], any], compare_method: Callable[[any, any], bool]) -> auth_role_uri_read_dto | None:
        if len(self.dtos) == 0:
            return None
        else:
            max_value = value_method(self.dtos[0])
            max_elem = self.dtos[0]
            for dto in self.dtos:
                next_value = value_method(dto)
                if compare_method(next_value, max_value):
                    max_value = next_value
                    max_elem = dto
            return max_elem


@dataclass(frozen=False)
class auth_session_read_dtos(base_read_dtos):
    dtos: list[auth_session_read_dto]
    def __init__(self, dtos: list[auth_session_read_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[auth_session_read_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: auth_session_read_dto):
        return cls(list([dto]))
    @classmethod
    def from_lists(cls, dtos1: list[auth_session_read_dto], dtos2: list[auth_session_read_dto]):
        return cls(dtos1 + dtos2)
    def get_active(self):
        return auth_session_read_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return auth_session_read_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_write_dtos(self) -> list[auth_session_write_dto]:
        return list(map(lambda x: x.to_write(), self.dtos))
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write().to_write_dict(), self.dtos))
    def get_read_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> auth_session_read_dto | None:
        found_dtos = list(filter(lambda x: x.auth_session_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def get_first(self) -> auth_session_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> auth_session_read_dtos:
        if len(self.dtos) > n:
            return auth_session_read_dtos(self.dtos[:n])
        else:
            return auth_session_read_dtos(self.dtos)
    def get_last(self) -> auth_session_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, auth_session_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def to_dict_by_auth_session_uid(self) -> dict[str, auth_session_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.auth_session_uid] = dto
        return d
    def to_dict_by_auth_session_name(self) -> dict[str, auth_session_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.auth_session_name] = dto
        return d
    def to_dict_by_tenant_uid(self) -> dict[str, auth_session_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.tenant_uid] = dto
        return d
    def to_dict_by_account_uid(self) -> dict[str, auth_session_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.account_uid] = dto
        return d
    def to_dict_by_session_token(self) -> dict[str, auth_session_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.session_token] = dto
        return d
    def to_dict_by_browser_name(self) -> dict[str, auth_session_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.browser_name] = dto
        return d
    def to_dict_by_browser_(self) -> dict[str, auth_session_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.browser_] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[auth_session_read_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[auth_session_read_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return init
    def check_any(self, check_method: Callable[[auth_session_read_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return init
    def map_to_string(self, map_method: Callable[[auth_session_read_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[auth_session_read_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[auth_session_read_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, auth_session_read_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, auth_session_read_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, auth_session_read_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[auth_session_read_dto], bool]) -> auth_session_read_dtos:
        return auth_session_read_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[auth_session_read_dto], str]) -> dict[str, auth_session_read_dtos]:
        grp_data: dict[str, auth_session_read_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = auth_session_read_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[auth_session_read_dto], str], agg_method: Callable[[auth_session_read_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, auth_session_read_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[auth_session_read_dto], bool]) -> auth_session_read_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[auth_session_read_dto], any], compare_method: Callable[[any, any], bool]) -> auth_session_read_dto | None:
        if len(self.dtos) == 0:
            return None
        else:
            max_value = value_method(self.dtos[0])
            max_elem = self.dtos[0]
            for dto in self.dtos:
                next_value = value_method(dto)
                if compare_method(next_value, max_value):
                    max_value = next_value
                    max_elem = dto
            return max_elem


@dataclass(frozen=False)
class auth_sso_read_dtos(base_read_dtos):
    dtos: list[auth_sso_read_dto]
    def __init__(self, dtos: list[auth_sso_read_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[auth_sso_read_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: auth_sso_read_dto):
        return cls(list([dto]))
    @classmethod
    def from_lists(cls, dtos1: list[auth_sso_read_dto], dtos2: list[auth_sso_read_dto]):
        return cls(dtos1 + dtos2)
    def get_active(self):
        return auth_sso_read_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return auth_sso_read_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_write_dtos(self) -> list[auth_sso_write_dto]:
        return list(map(lambda x: x.to_write(), self.dtos))
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write().to_write_dict(), self.dtos))
    def get_read_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> auth_sso_read_dto | None:
        found_dtos = list(filter(lambda x: x.auth_sso_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def get_first(self) -> auth_sso_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> auth_sso_read_dtos:
        if len(self.dtos) > n:
            return auth_sso_read_dtos(self.dtos[:n])
        else:
            return auth_sso_read_dtos(self.dtos)
    def get_last(self) -> auth_sso_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, auth_sso_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def to_dict_by_auth_sso_uid(self) -> dict[str, auth_sso_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.auth_sso_uid] = dto
        return d
    def to_dict_by_auth_sso_name(self) -> dict[str, auth_sso_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.auth_sso_name] = dto
        return d
    def to_dict_by_tenant_uid(self) -> dict[str, auth_sso_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.tenant_uid] = dto
        return d
    def to_dict_by_owner_account_uid(self) -> dict[str, auth_sso_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.owner_account_uid] = dto
        return d
    def to_dict_by_sso_name(self) -> dict[str, auth_sso_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.sso_name] = dto
        return d
    def to_dict_by_sso_url(self) -> dict[str, auth_sso_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.sso_url] = dto
        return d
    def to_dict_by_sso_key(self) -> dict[str, auth_sso_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.sso_key] = dto
        return d
    def to_dict_by_sso_secret(self) -> dict[str, auth_sso_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.sso_secret] = dto
        return d
    def to_dict_by_sso_code(self) -> dict[str, auth_sso_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.sso_code] = dto
        return d
    def to_dict_by_clientid(self) -> dict[str, auth_sso_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.clientid] = dto
        return d
    def to_dict_by_clientsecret(self) -> dict[str, auth_sso_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.clientsecret] = dto
        return d
    def to_dict_by_callback_url(self) -> dict[str, auth_sso_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.callback_url] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[auth_sso_read_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[auth_sso_read_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return init
    def check_any(self, check_method: Callable[[auth_sso_read_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return init
    def map_to_string(self, map_method: Callable[[auth_sso_read_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[auth_sso_read_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[auth_sso_read_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, auth_sso_read_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, auth_sso_read_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, auth_sso_read_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[auth_sso_read_dto], bool]) -> auth_sso_read_dtos:
        return auth_sso_read_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[auth_sso_read_dto], str]) -> dict[str, auth_sso_read_dtos]:
        grp_data: dict[str, auth_sso_read_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = auth_sso_read_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[auth_sso_read_dto], str], agg_method: Callable[[auth_sso_read_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, auth_sso_read_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[auth_sso_read_dto], bool]) -> auth_sso_read_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[auth_sso_read_dto], any], compare_method: Callable[[any, any], bool]) -> auth_sso_read_dto | None:
        if len(self.dtos) == 0:
            return None
        else:
            max_value = value_method(self.dtos[0])
            max_elem = self.dtos[0]
            for dto in self.dtos:
                next_value = value_method(dto)
                if compare_method(next_value, max_value):
                    max_value = next_value
                    max_elem = dto
            return max_elem


@dataclass(frozen=False)
class auth_token_read_dtos(base_read_dtos):
    dtos: list[auth_token_read_dto]
    def __init__(self, dtos: list[auth_token_read_dto]):
        super().__init__(dtos)
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
        return list(map(lambda x: x.to_write(), self.dtos))
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
    def get_first_n(self, n: int) -> auth_token_read_dtos:
        if len(self.dtos) > n:
            return auth_token_read_dtos(self.dtos[:n])
        else:
            return auth_token_read_dtos(self.dtos)
    def get_last(self) -> auth_token_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
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
    def to_dict_by_auth_token_name(self) -> dict[str, auth_token_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.auth_token_name] = dto
        return d
    def to_dict_by_tenant_uid(self) -> dict[str, auth_token_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.tenant_uid] = dto
        return d
    def to_dict_by_account_uid(self) -> dict[str, auth_token_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.account_uid] = dto
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
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[auth_token_read_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[auth_token_read_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return init
    def check_any(self, check_method: Callable[[auth_token_read_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return init
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
    def find(self, check_method: Callable[[auth_token_read_dto], bool]) -> auth_token_read_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[auth_token_read_dto], any], compare_method: Callable[[any, any], bool]) -> auth_token_read_dto | None:
        if len(self.dtos) == 0:
            return None
        else:
            max_value = value_method(self.dtos[0])
            max_elem = self.dtos[0]
            for dto in self.dtos:
                next_value = value_method(dto)
                if compare_method(next_value, max_value):
                    max_value = next_value
                    max_elem = dto
            return max_elem


@dataclass(frozen=False)
class calendar_account_read_dtos(base_read_dtos):
    dtos: list[calendar_account_read_dto]
    def __init__(self, dtos: list[calendar_account_read_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[calendar_account_read_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: calendar_account_read_dto):
        return cls(list([dto]))
    @classmethod
    def from_lists(cls, dtos1: list[calendar_account_read_dto], dtos2: list[calendar_account_read_dto]):
        return cls(dtos1 + dtos2)
    def get_active(self):
        return calendar_account_read_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return calendar_account_read_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_write_dtos(self) -> list[calendar_account_write_dto]:
        return list(map(lambda x: x.to_write(), self.dtos))
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write().to_write_dict(), self.dtos))
    def get_read_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> calendar_account_read_dto | None:
        found_dtos = list(filter(lambda x: x.calendar_account_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def get_first(self) -> calendar_account_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> calendar_account_read_dtos:
        if len(self.dtos) > n:
            return calendar_account_read_dtos(self.dtos[:n])
        else:
            return calendar_account_read_dtos(self.dtos)
    def get_last(self) -> calendar_account_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, calendar_account_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def to_dict_by_calendar_account_uid(self) -> dict[str, calendar_account_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.calendar_account_uid] = dto
        return d
    def to_dict_by_calendar_account_name(self) -> dict[str, calendar_account_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.calendar_account_name] = dto
        return d
    def to_dict_by_tenant_uid(self) -> dict[str, calendar_account_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.tenant_uid] = dto
        return d
    def to_dict_by_account_uid(self) -> dict[str, calendar_account_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.account_uid] = dto
        return d
    def to_dict_by_calendar_type_uid(self) -> dict[str, calendar_account_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.calendar_type_uid] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[calendar_account_read_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[calendar_account_read_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return init
    def check_any(self, check_method: Callable[[calendar_account_read_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return init
    def map_to_string(self, map_method: Callable[[calendar_account_read_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[calendar_account_read_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[calendar_account_read_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, calendar_account_read_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, calendar_account_read_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, calendar_account_read_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[calendar_account_read_dto], bool]) -> calendar_account_read_dtos:
        return calendar_account_read_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[calendar_account_read_dto], str]) -> dict[str, calendar_account_read_dtos]:
        grp_data: dict[str, calendar_account_read_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = calendar_account_read_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[calendar_account_read_dto], str], agg_method: Callable[[calendar_account_read_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, calendar_account_read_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[calendar_account_read_dto], bool]) -> calendar_account_read_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[calendar_account_read_dto], any], compare_method: Callable[[any, any], bool]) -> calendar_account_read_dto | None:
        if len(self.dtos) == 0:
            return None
        else:
            max_value = value_method(self.dtos[0])
            max_elem = self.dtos[0]
            for dto in self.dtos:
                next_value = value_method(dto)
                if compare_method(next_value, max_value):
                    max_value = next_value
                    max_elem = dto
            return max_elem


@dataclass(frozen=False)
class calendar_approval_read_dtos(base_read_dtos):
    dtos: list[calendar_approval_read_dto]
    def __init__(self, dtos: list[calendar_approval_read_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[calendar_approval_read_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: calendar_approval_read_dto):
        return cls(list([dto]))
    @classmethod
    def from_lists(cls, dtos1: list[calendar_approval_read_dto], dtos2: list[calendar_approval_read_dto]):
        return cls(dtos1 + dtos2)
    def get_active(self):
        return calendar_approval_read_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return calendar_approval_read_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_write_dtos(self) -> list[calendar_approval_write_dto]:
        return list(map(lambda x: x.to_write(), self.dtos))
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write().to_write_dict(), self.dtos))
    def get_read_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> calendar_approval_read_dto | None:
        found_dtos = list(filter(lambda x: x.calendar_approval_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def get_first(self) -> calendar_approval_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> calendar_approval_read_dtos:
        if len(self.dtos) > n:
            return calendar_approval_read_dtos(self.dtos[:n])
        else:
            return calendar_approval_read_dtos(self.dtos)
    def get_last(self) -> calendar_approval_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, calendar_approval_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def to_dict_by_calendar_approval_uid(self) -> dict[str, calendar_approval_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.calendar_approval_uid] = dto
        return d
    def to_dict_by_calendar_approval_name(self) -> dict[str, calendar_approval_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.calendar_approval_name] = dto
        return d
    def to_dict_by_client_uid(self) -> dict[str, calendar_approval_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.client_uid] = dto
        return d
    def to_dict_by_account_uid(self) -> dict[str, calendar_approval_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.account_uid] = dto
        return d
    def to_dict_by_calendar_approval_type_uid(self) -> dict[str, calendar_approval_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.calendar_approval_type_uid] = dto
        return d
    def to_dict_by_calendar_event_group_uid(self) -> dict[str, calendar_approval_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.calendar_event_group_uid] = dto
        return d
    def to_dict_by_calendar_type_uid(self) -> dict[str, calendar_approval_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.calendar_type_uid] = dto
        return d
    def to_dict_by_time_submit_type_name(self) -> dict[str, calendar_approval_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.time_submit_type_name] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[calendar_approval_read_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[calendar_approval_read_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return init
    def check_any(self, check_method: Callable[[calendar_approval_read_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return init
    def map_to_string(self, map_method: Callable[[calendar_approval_read_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[calendar_approval_read_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[calendar_approval_read_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, calendar_approval_read_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, calendar_approval_read_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, calendar_approval_read_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[calendar_approval_read_dto], bool]) -> calendar_approval_read_dtos:
        return calendar_approval_read_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[calendar_approval_read_dto], str]) -> dict[str, calendar_approval_read_dtos]:
        grp_data: dict[str, calendar_approval_read_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = calendar_approval_read_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[calendar_approval_read_dto], str], agg_method: Callable[[calendar_approval_read_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, calendar_approval_read_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[calendar_approval_read_dto], bool]) -> calendar_approval_read_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[calendar_approval_read_dto], any], compare_method: Callable[[any, any], bool]) -> calendar_approval_read_dto | None:
        if len(self.dtos) == 0:
            return None
        else:
            max_value = value_method(self.dtos[0])
            max_elem = self.dtos[0]
            for dto in self.dtos:
                next_value = value_method(dto)
                if compare_method(next_value, max_value):
                    max_value = next_value
                    max_elem = dto
            return max_elem


@dataclass(frozen=False)
class calendar_approval_type_read_dtos(base_read_dtos):
    dtos: list[calendar_approval_type_read_dto]
    def __init__(self, dtos: list[calendar_approval_type_read_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[calendar_approval_type_read_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: calendar_approval_type_read_dto):
        return cls(list([dto]))
    @classmethod
    def from_lists(cls, dtos1: list[calendar_approval_type_read_dto], dtos2: list[calendar_approval_type_read_dto]):
        return cls(dtos1 + dtos2)
    def get_active(self):
        return calendar_approval_type_read_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return calendar_approval_type_read_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_write_dtos(self) -> list[calendar_approval_type_write_dto]:
        return list(map(lambda x: x.to_write(), self.dtos))
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write().to_write_dict(), self.dtos))
    def get_read_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> calendar_approval_type_read_dto | None:
        found_dtos = list(filter(lambda x: x.calendar_approval_type_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def get_first(self) -> calendar_approval_type_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> calendar_approval_type_read_dtos:
        if len(self.dtos) > n:
            return calendar_approval_type_read_dtos(self.dtos[:n])
        else:
            return calendar_approval_type_read_dtos(self.dtos)
    def get_last(self) -> calendar_approval_type_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, calendar_approval_type_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def to_dict_by_calendar_approval_type_uid(self) -> dict[str, calendar_approval_type_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.calendar_approval_type_uid] = dto
        return d
    def to_dict_by_calendar_approval_type_name(self) -> dict[str, calendar_approval_type_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.calendar_approval_type_name] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[calendar_approval_type_read_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[calendar_approval_type_read_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return init
    def check_any(self, check_method: Callable[[calendar_approval_type_read_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return init
    def map_to_string(self, map_method: Callable[[calendar_approval_type_read_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[calendar_approval_type_read_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[calendar_approval_type_read_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, calendar_approval_type_read_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, calendar_approval_type_read_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, calendar_approval_type_read_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[calendar_approval_type_read_dto], bool]) -> calendar_approval_type_read_dtos:
        return calendar_approval_type_read_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[calendar_approval_type_read_dto], str]) -> dict[str, calendar_approval_type_read_dtos]:
        grp_data: dict[str, calendar_approval_type_read_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = calendar_approval_type_read_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[calendar_approval_type_read_dto], str], agg_method: Callable[[calendar_approval_type_read_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, calendar_approval_type_read_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[calendar_approval_type_read_dto], bool]) -> calendar_approval_type_read_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[calendar_approval_type_read_dto], any], compare_method: Callable[[any, any], bool]) -> calendar_approval_type_read_dto | None:
        if len(self.dtos) == 0:
            return None
        else:
            max_value = value_method(self.dtos[0])
            max_elem = self.dtos[0]
            for dto in self.dtos:
                next_value = value_method(dto)
                if compare_method(next_value, max_value):
                    max_value = next_value
                    max_elem = dto
            return max_elem


@dataclass(frozen=False)
class calendar_event_read_dtos(base_read_dtos):
    dtos: list[calendar_event_read_dto]
    def __init__(self, dtos: list[calendar_event_read_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[calendar_event_read_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: calendar_event_read_dto):
        return cls(list([dto]))
    @classmethod
    def from_lists(cls, dtos1: list[calendar_event_read_dto], dtos2: list[calendar_event_read_dto]):
        return cls(dtos1 + dtos2)
    def get_active(self):
        return calendar_event_read_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return calendar_event_read_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_write_dtos(self) -> list[calendar_event_write_dto]:
        return list(map(lambda x: x.to_write(), self.dtos))
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write().to_write_dict(), self.dtos))
    def get_read_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> calendar_event_read_dto | None:
        found_dtos = list(filter(lambda x: x.calendar_event_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def get_first(self) -> calendar_event_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> calendar_event_read_dtos:
        if len(self.dtos) > n:
            return calendar_event_read_dtos(self.dtos[:n])
        else:
            return calendar_event_read_dtos(self.dtos)
    def get_last(self) -> calendar_event_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, calendar_event_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def to_dict_by_calendar_event_uid(self) -> dict[str, calendar_event_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.calendar_event_uid] = dto
        return d
    def to_dict_by_calendar_event_name(self) -> dict[str, calendar_event_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.calendar_event_name] = dto
        return d
    def to_dict_by_client_uid(self) -> dict[str, calendar_event_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.client_uid] = dto
        return d
    def to_dict_by_account_uid(self) -> dict[str, calendar_event_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.account_uid] = dto
        return d
    def to_dict_by_calendar_event_group_uid(self) -> dict[str, calendar_event_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.calendar_event_group_uid] = dto
        return d
    def to_dict_by_calendar_type_uid(self) -> dict[str, calendar_event_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.calendar_type_uid] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[calendar_event_read_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[calendar_event_read_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return init
    def check_any(self, check_method: Callable[[calendar_event_read_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return init
    def map_to_string(self, map_method: Callable[[calendar_event_read_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[calendar_event_read_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[calendar_event_read_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, calendar_event_read_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, calendar_event_read_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, calendar_event_read_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[calendar_event_read_dto], bool]) -> calendar_event_read_dtos:
        return calendar_event_read_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[calendar_event_read_dto], str]) -> dict[str, calendar_event_read_dtos]:
        grp_data: dict[str, calendar_event_read_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = calendar_event_read_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[calendar_event_read_dto], str], agg_method: Callable[[calendar_event_read_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, calendar_event_read_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[calendar_event_read_dto], bool]) -> calendar_event_read_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[calendar_event_read_dto], any], compare_method: Callable[[any, any], bool]) -> calendar_event_read_dto | None:
        if len(self.dtos) == 0:
            return None
        else:
            max_value = value_method(self.dtos[0])
            max_elem = self.dtos[0]
            for dto in self.dtos:
                next_value = value_method(dto)
                if compare_method(next_value, max_value):
                    max_value = next_value
                    max_elem = dto
            return max_elem


@dataclass(frozen=False)
class calendar_event_group_read_dtos(base_read_dtos):
    dtos: list[calendar_event_group_read_dto]
    def __init__(self, dtos: list[calendar_event_group_read_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[calendar_event_group_read_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: calendar_event_group_read_dto):
        return cls(list([dto]))
    @classmethod
    def from_lists(cls, dtos1: list[calendar_event_group_read_dto], dtos2: list[calendar_event_group_read_dto]):
        return cls(dtos1 + dtos2)
    def get_active(self):
        return calendar_event_group_read_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return calendar_event_group_read_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_write_dtos(self) -> list[calendar_event_group_write_dto]:
        return list(map(lambda x: x.to_write(), self.dtos))
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write().to_write_dict(), self.dtos))
    def get_read_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> calendar_event_group_read_dto | None:
        found_dtos = list(filter(lambda x: x.calendar_event_group_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def get_first(self) -> calendar_event_group_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> calendar_event_group_read_dtos:
        if len(self.dtos) > n:
            return calendar_event_group_read_dtos(self.dtos[:n])
        else:
            return calendar_event_group_read_dtos(self.dtos)
    def get_last(self) -> calendar_event_group_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, calendar_event_group_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def to_dict_by_calendar_event_group_uid(self) -> dict[str, calendar_event_group_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.calendar_event_group_uid] = dto
        return d
    def to_dict_by_calendar_event_group_name(self) -> dict[str, calendar_event_group_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.calendar_event_group_name] = dto
        return d
    def to_dict_by_client_uid(self) -> dict[str, calendar_event_group_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.client_uid] = dto
        return d
    def to_dict_by_account_uid(self) -> dict[str, calendar_event_group_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.account_uid] = dto
        return d
    def to_dict_by_calendar_account_uid(self) -> dict[str, calendar_event_group_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.calendar_account_uid] = dto
        return d
    def to_dict_by_calendar_event_type_uid(self) -> dict[str, calendar_event_group_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.calendar_event_type_uid] = dto
        return d
    def to_dict_by_group_comment(self) -> dict[str, calendar_event_group_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.group_comment] = dto
        return d
    def to_dict_by_event_start_date(self) -> dict[str, calendar_event_group_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.event_start_date] = dto
        return d
    def to_dict_by_event_end_date(self) -> dict[str, calendar_event_group_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.event_end_date] = dto
        return d
    def to_dict_by_is_approved(self) -> dict[str, calendar_event_group_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.is_approved] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[calendar_event_group_read_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[calendar_event_group_read_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return init
    def check_any(self, check_method: Callable[[calendar_event_group_read_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return init
    def map_to_string(self, map_method: Callable[[calendar_event_group_read_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[calendar_event_group_read_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[calendar_event_group_read_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, calendar_event_group_read_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, calendar_event_group_read_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, calendar_event_group_read_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[calendar_event_group_read_dto], bool]) -> calendar_event_group_read_dtos:
        return calendar_event_group_read_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[calendar_event_group_read_dto], str]) -> dict[str, calendar_event_group_read_dtos]:
        grp_data: dict[str, calendar_event_group_read_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = calendar_event_group_read_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[calendar_event_group_read_dto], str], agg_method: Callable[[calendar_event_group_read_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, calendar_event_group_read_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[calendar_event_group_read_dto], bool]) -> calendar_event_group_read_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[calendar_event_group_read_dto], any], compare_method: Callable[[any, any], bool]) -> calendar_event_group_read_dto | None:
        if len(self.dtos) == 0:
            return None
        else:
            max_value = value_method(self.dtos[0])
            max_elem = self.dtos[0]
            for dto in self.dtos:
                next_value = value_method(dto)
                if compare_method(next_value, max_value):
                    max_value = next_value
                    max_elem = dto
            return max_elem


@dataclass(frozen=False)
class calendar_event_type_read_dtos(base_read_dtos):
    dtos: list[calendar_event_type_read_dto]
    def __init__(self, dtos: list[calendar_event_type_read_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[calendar_event_type_read_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: calendar_event_type_read_dto):
        return cls(list([dto]))
    @classmethod
    def from_lists(cls, dtos1: list[calendar_event_type_read_dto], dtos2: list[calendar_event_type_read_dto]):
        return cls(dtos1 + dtos2)
    def get_active(self):
        return calendar_event_type_read_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return calendar_event_type_read_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_write_dtos(self) -> list[calendar_event_type_write_dto]:
        return list(map(lambda x: x.to_write(), self.dtos))
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write().to_write_dict(), self.dtos))
    def get_read_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> calendar_event_type_read_dto | None:
        found_dtos = list(filter(lambda x: x.calendar_event_type_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def get_first(self) -> calendar_event_type_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> calendar_event_type_read_dtos:
        if len(self.dtos) > n:
            return calendar_event_type_read_dtos(self.dtos[:n])
        else:
            return calendar_event_type_read_dtos(self.dtos)
    def get_last(self) -> calendar_event_type_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, calendar_event_type_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def to_dict_by_calendar_event_type_uid(self) -> dict[str, calendar_event_type_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.calendar_event_type_uid] = dto
        return d
    def to_dict_by_calendar_event_type_name(self) -> dict[str, calendar_event_type_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.calendar_event_type_name] = dto
        return d
    def to_dict_by_client_uid(self) -> dict[str, calendar_event_type_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.client_uid] = dto
        return d
    def to_dict_by_calendar_type_uid(self) -> dict[str, calendar_event_type_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.calendar_type_uid] = dto
        return d
    def to_dict_by_auto_approved(self) -> dict[str, calendar_event_type_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.auto_approved] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[calendar_event_type_read_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[calendar_event_type_read_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return init
    def check_any(self, check_method: Callable[[calendar_event_type_read_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return init
    def map_to_string(self, map_method: Callable[[calendar_event_type_read_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[calendar_event_type_read_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[calendar_event_type_read_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, calendar_event_type_read_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, calendar_event_type_read_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, calendar_event_type_read_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[calendar_event_type_read_dto], bool]) -> calendar_event_type_read_dtos:
        return calendar_event_type_read_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[calendar_event_type_read_dto], str]) -> dict[str, calendar_event_type_read_dtos]:
        grp_data: dict[str, calendar_event_type_read_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = calendar_event_type_read_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[calendar_event_type_read_dto], str], agg_method: Callable[[calendar_event_type_read_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, calendar_event_type_read_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[calendar_event_type_read_dto], bool]) -> calendar_event_type_read_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[calendar_event_type_read_dto], any], compare_method: Callable[[any, any], bool]) -> calendar_event_type_read_dto | None:
        if len(self.dtos) == 0:
            return None
        else:
            max_value = value_method(self.dtos[0])
            max_elem = self.dtos[0]
            for dto in self.dtos:
                next_value = value_method(dto)
                if compare_method(next_value, max_value):
                    max_value = next_value
                    max_elem = dto
            return max_elem


@dataclass(frozen=False)
class calendar_type_read_dtos(base_read_dtos):
    dtos: list[calendar_type_read_dto]
    def __init__(self, dtos: list[calendar_type_read_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[calendar_type_read_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: calendar_type_read_dto):
        return cls(list([dto]))
    @classmethod
    def from_lists(cls, dtos1: list[calendar_type_read_dto], dtos2: list[calendar_type_read_dto]):
        return cls(dtos1 + dtos2)
    def get_active(self):
        return calendar_type_read_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return calendar_type_read_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_write_dtos(self) -> list[calendar_type_write_dto]:
        return list(map(lambda x: x.to_write(), self.dtos))
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write().to_write_dict(), self.dtos))
    def get_read_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> calendar_type_read_dto | None:
        found_dtos = list(filter(lambda x: x.calendar_type_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def get_first(self) -> calendar_type_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> calendar_type_read_dtos:
        if len(self.dtos) > n:
            return calendar_type_read_dtos(self.dtos[:n])
        else:
            return calendar_type_read_dtos(self.dtos)
    def get_last(self) -> calendar_type_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, calendar_type_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def to_dict_by_calendar_type_uid(self) -> dict[str, calendar_type_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.calendar_type_uid] = dto
        return d
    def to_dict_by_calendar_type_name(self) -> dict[str, calendar_type_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.calendar_type_name] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[calendar_type_read_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[calendar_type_read_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return init
    def check_any(self, check_method: Callable[[calendar_type_read_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return init
    def map_to_string(self, map_method: Callable[[calendar_type_read_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[calendar_type_read_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[calendar_type_read_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, calendar_type_read_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, calendar_type_read_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, calendar_type_read_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[calendar_type_read_dto], bool]) -> calendar_type_read_dtos:
        return calendar_type_read_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[calendar_type_read_dto], str]) -> dict[str, calendar_type_read_dtos]:
        grp_data: dict[str, calendar_type_read_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = calendar_type_read_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[calendar_type_read_dto], str], agg_method: Callable[[calendar_type_read_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, calendar_type_read_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[calendar_type_read_dto], bool]) -> calendar_type_read_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[calendar_type_read_dto], any], compare_method: Callable[[any, any], bool]) -> calendar_type_read_dto | None:
        if len(self.dtos) == 0:
            return None
        else:
            max_value = value_method(self.dtos[0])
            max_elem = self.dtos[0]
            for dto in self.dtos:
                next_value = value_method(dto)
                if compare_method(next_value, max_value):
                    max_value = next_value
                    max_elem = dto
            return max_elem


@dataclass(frozen=False)
class client_read_dtos(base_read_dtos):
    dtos: list[client_read_dto]
    def __init__(self, dtos: list[client_read_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[client_read_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: client_read_dto):
        return cls(list([dto]))
    @classmethod
    def from_lists(cls, dtos1: list[client_read_dto], dtos2: list[client_read_dto]):
        return cls(dtos1 + dtos2)
    def get_active(self):
        return client_read_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return client_read_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_write_dtos(self) -> list[client_write_dto]:
        return list(map(lambda x: x.to_write(), self.dtos))
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write().to_write_dict(), self.dtos))
    def get_read_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> client_read_dto | None:
        found_dtos = list(filter(lambda x: x.client_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def get_first(self) -> client_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> client_read_dtos:
        if len(self.dtos) > n:
            return client_read_dtos(self.dtos[:n])
        else:
            return client_read_dtos(self.dtos)
    def get_last(self) -> client_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, client_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def to_dict_by_client_uid(self) -> dict[str, client_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.client_uid] = dto
        return d
    def to_dict_by_client_name(self) -> dict[str, client_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.client_name] = dto
        return d
    def to_dict_by_tenant_uid(self) -> dict[str, client_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.tenant_uid] = dto
        return d
    def to_dict_by_country_uid(self) -> dict[str, client_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.country_uid] = dto
        return d
    def to_dict_by_client_type_uid(self) -> dict[str, client_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.client_type_uid] = dto
        return d
    def to_dict_by_client_category_uid(self) -> dict[str, client_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.client_category_uid] = dto
        return d
    def to_dict_by_account_uid(self) -> dict[str, client_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.account_uid] = dto
        return d
    def to_dict_by_client_code(self) -> dict[str, client_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.client_code] = dto
        return d
    def to_dict_by_client_description(self) -> dict[str, client_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.client_description] = dto
        return d
    def to_dict_by_start_date(self) -> dict[str, client_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.start_date] = dto
        return d
    def to_dict_by_end_date(self) -> dict[str, client_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.end_date] = dto
        return d
    def to_dict_by_is_internal(self) -> dict[str, client_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.is_internal] = dto
        return d
    def to_dict_by_is_system(self) -> dict[str, client_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.is_system] = dto
        return d
    def to_dict_by_is_test(self) -> dict[str, client_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.is_test] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[client_read_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[client_read_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return init
    def check_any(self, check_method: Callable[[client_read_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return init
    def map_to_string(self, map_method: Callable[[client_read_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[client_read_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[client_read_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, client_read_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, client_read_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, client_read_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[client_read_dto], bool]) -> client_read_dtos:
        return client_read_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[client_read_dto], str]) -> dict[str, client_read_dtos]:
        grp_data: dict[str, client_read_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = client_read_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[client_read_dto], str], agg_method: Callable[[client_read_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, client_read_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[client_read_dto], bool]) -> client_read_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[client_read_dto], any], compare_method: Callable[[any, any], bool]) -> client_read_dto | None:
        if len(self.dtos) == 0:
            return None
        else:
            max_value = value_method(self.dtos[0])
            max_elem = self.dtos[0]
            for dto in self.dtos:
                next_value = value_method(dto)
                if compare_method(next_value, max_value):
                    max_value = next_value
                    max_elem = dto
            return max_elem


@dataclass(frozen=False)
class client_account_read_dtos(base_read_dtos):
    dtos: list[client_account_read_dto]
    def __init__(self, dtos: list[client_account_read_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[client_account_read_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: client_account_read_dto):
        return cls(list([dto]))
    @classmethod
    def from_lists(cls, dtos1: list[client_account_read_dto], dtos2: list[client_account_read_dto]):
        return cls(dtos1 + dtos2)
    def get_active(self):
        return client_account_read_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return client_account_read_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_write_dtos(self) -> list[client_account_write_dto]:
        return list(map(lambda x: x.to_write(), self.dtos))
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write().to_write_dict(), self.dtos))
    def get_read_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> client_account_read_dto | None:
        found_dtos = list(filter(lambda x: x.client_account_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def get_first(self) -> client_account_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> client_account_read_dtos:
        if len(self.dtos) > n:
            return client_account_read_dtos(self.dtos[:n])
        else:
            return client_account_read_dtos(self.dtos)
    def get_last(self) -> client_account_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, client_account_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def to_dict_by_client_account_uid(self) -> dict[str, client_account_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.client_account_uid] = dto
        return d
    def to_dict_by_client_account_name(self) -> dict[str, client_account_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.client_account_name] = dto
        return d
    def to_dict_by_tenant_uid(self) -> dict[str, client_account_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.tenant_uid] = dto
        return d
    def to_dict_by_client_uid(self) -> dict[str, client_account_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.client_uid] = dto
        return d
    def to_dict_by_account_uid(self) -> dict[str, client_account_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.account_uid] = dto
        return d
    def to_dict_by_client_role_uid(self) -> dict[str, client_account_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.client_role_uid] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[client_account_read_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[client_account_read_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return init
    def check_any(self, check_method: Callable[[client_account_read_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return init
    def map_to_string(self, map_method: Callable[[client_account_read_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[client_account_read_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[client_account_read_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, client_account_read_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, client_account_read_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, client_account_read_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[client_account_read_dto], bool]) -> client_account_read_dtos:
        return client_account_read_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[client_account_read_dto], str]) -> dict[str, client_account_read_dtos]:
        grp_data: dict[str, client_account_read_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = client_account_read_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[client_account_read_dto], str], agg_method: Callable[[client_account_read_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, client_account_read_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[client_account_read_dto], bool]) -> client_account_read_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[client_account_read_dto], any], compare_method: Callable[[any, any], bool]) -> client_account_read_dto | None:
        if len(self.dtos) == 0:
            return None
        else:
            max_value = value_method(self.dtos[0])
            max_elem = self.dtos[0]
            for dto in self.dtos:
                next_value = value_method(dto)
                if compare_method(next_value, max_value):
                    max_value = next_value
                    max_elem = dto
            return max_elem


@dataclass(frozen=False)
class client_country_read_dtos(base_read_dtos):
    dtos: list[client_country_read_dto]
    def __init__(self, dtos: list[client_country_read_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[client_country_read_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: client_country_read_dto):
        return cls(list([dto]))
    @classmethod
    def from_lists(cls, dtos1: list[client_country_read_dto], dtos2: list[client_country_read_dto]):
        return cls(dtos1 + dtos2)
    def get_active(self):
        return client_country_read_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return client_country_read_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_write_dtos(self) -> list[client_country_write_dto]:
        return list(map(lambda x: x.to_write(), self.dtos))
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write().to_write_dict(), self.dtos))
    def get_read_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> client_country_read_dto | None:
        found_dtos = list(filter(lambda x: x.client_country_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def get_first(self) -> client_country_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> client_country_read_dtos:
        if len(self.dtos) > n:
            return client_country_read_dtos(self.dtos[:n])
        else:
            return client_country_read_dtos(self.dtos)
    def get_last(self) -> client_country_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, client_country_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def to_dict_by_client_country_uid(self) -> dict[str, client_country_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.client_country_uid] = dto
        return d
    def to_dict_by_client_country_name(self) -> dict[str, client_country_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.client_country_name] = dto
        return d
    def to_dict_by_tenant_uid(self) -> dict[str, client_country_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.tenant_uid] = dto
        return d
    def to_dict_by_client_uid(self) -> dict[str, client_country_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.client_uid] = dto
        return d
    def to_dict_by_country_uid(self) -> dict[str, client_country_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.country_uid] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[client_country_read_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[client_country_read_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return init
    def check_any(self, check_method: Callable[[client_country_read_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return init
    def map_to_string(self, map_method: Callable[[client_country_read_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[client_country_read_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[client_country_read_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, client_country_read_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, client_country_read_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, client_country_read_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[client_country_read_dto], bool]) -> client_country_read_dtos:
        return client_country_read_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[client_country_read_dto], str]) -> dict[str, client_country_read_dtos]:
        grp_data: dict[str, client_country_read_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = client_country_read_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[client_country_read_dto], str], agg_method: Callable[[client_country_read_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, client_country_read_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[client_country_read_dto], bool]) -> client_country_read_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[client_country_read_dto], any], compare_method: Callable[[any, any], bool]) -> client_country_read_dto | None:
        if len(self.dtos) == 0:
            return None
        else:
            max_value = value_method(self.dtos[0])
            max_elem = self.dtos[0]
            for dto in self.dtos:
                next_value = value_method(dto)
                if compare_method(next_value, max_value):
                    max_value = next_value
                    max_elem = dto
            return max_elem


@dataclass(frozen=False)
class client_payment_read_dtos(base_read_dtos):
    dtos: list[client_payment_read_dto]
    def __init__(self, dtos: list[client_payment_read_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[client_payment_read_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: client_payment_read_dto):
        return cls(list([dto]))
    @classmethod
    def from_lists(cls, dtos1: list[client_payment_read_dto], dtos2: list[client_payment_read_dto]):
        return cls(dtos1 + dtos2)
    def get_active(self):
        return client_payment_read_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return client_payment_read_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_write_dtos(self) -> list[client_payment_write_dto]:
        return list(map(lambda x: x.to_write(), self.dtos))
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write().to_write_dict(), self.dtos))
    def get_read_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> client_payment_read_dto | None:
        found_dtos = list(filter(lambda x: x.client_payment_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def get_first(self) -> client_payment_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> client_payment_read_dtos:
        if len(self.dtos) > n:
            return client_payment_read_dtos(self.dtos[:n])
        else:
            return client_payment_read_dtos(self.dtos)
    def get_last(self) -> client_payment_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, client_payment_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def to_dict_by_client_payment_uid(self) -> dict[str, client_payment_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.client_payment_uid] = dto
        return d
    def to_dict_by_client_payment_name(self) -> dict[str, client_payment_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.client_payment_name] = dto
        return d
    def to_dict_by_tenant_uid(self) -> dict[str, client_payment_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.tenant_uid] = dto
        return d
    def to_dict_by_client_uid(self) -> dict[str, client_payment_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.client_uid] = dto
        return d
    def to_dict_by_account_uid(self) -> dict[str, client_payment_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.account_uid] = dto
        return d
    def to_dict_by_currency_uid(self) -> dict[str, client_payment_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.currency_uid] = dto
        return d
    def to_dict_by_start_date(self) -> dict[str, client_payment_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.start_date] = dto
        return d
    def to_dict_by_end_date(self) -> dict[str, client_payment_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.end_date] = dto
        return d
    def to_dict_by_payment_value(self) -> dict[str, client_payment_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.payment_value] = dto
        return d
    def to_dict_by_payment_type(self) -> dict[str, client_payment_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.payment_type] = dto
        return d
    def to_dict_by_source_number(self) -> dict[str, client_payment_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.source_number] = dto
        return d
    def to_dict_by_source_reference(self) -> dict[str, client_payment_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.source_reference] = dto
        return d
    def to_dict_by_is_approved(self) -> dict[str, client_payment_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.is_approved] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[client_payment_read_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[client_payment_read_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return init
    def check_any(self, check_method: Callable[[client_payment_read_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return init
    def map_to_string(self, map_method: Callable[[client_payment_read_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[client_payment_read_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[client_payment_read_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, client_payment_read_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, client_payment_read_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, client_payment_read_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[client_payment_read_dto], bool]) -> client_payment_read_dtos:
        return client_payment_read_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[client_payment_read_dto], str]) -> dict[str, client_payment_read_dtos]:
        grp_data: dict[str, client_payment_read_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = client_payment_read_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[client_payment_read_dto], str], agg_method: Callable[[client_payment_read_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, client_payment_read_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[client_payment_read_dto], bool]) -> client_payment_read_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[client_payment_read_dto], any], compare_method: Callable[[any, any], bool]) -> client_payment_read_dto | None:
        if len(self.dtos) == 0:
            return None
        else:
            max_value = value_method(self.dtos[0])
            max_elem = self.dtos[0]
            for dto in self.dtos:
                next_value = value_method(dto)
                if compare_method(next_value, max_value):
                    max_value = next_value
                    max_elem = dto
            return max_elem


@dataclass(frozen=False)
class client_role_read_dtos(base_read_dtos):
    dtos: list[client_role_read_dto]
    def __init__(self, dtos: list[client_role_read_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[client_role_read_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: client_role_read_dto):
        return cls(list([dto]))
    @classmethod
    def from_lists(cls, dtos1: list[client_role_read_dto], dtos2: list[client_role_read_dto]):
        return cls(dtos1 + dtos2)
    def get_active(self):
        return client_role_read_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return client_role_read_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_write_dtos(self) -> list[client_role_write_dto]:
        return list(map(lambda x: x.to_write(), self.dtos))
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write().to_write_dict(), self.dtos))
    def get_read_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> client_role_read_dto | None:
        found_dtos = list(filter(lambda x: x.client_role_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def get_first(self) -> client_role_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> client_role_read_dtos:
        if len(self.dtos) > n:
            return client_role_read_dtos(self.dtos[:n])
        else:
            return client_role_read_dtos(self.dtos)
    def get_last(self) -> client_role_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, client_role_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def to_dict_by_client_role_uid(self) -> dict[str, client_role_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.client_role_uid] = dto
        return d
    def to_dict_by_client_role_name(self) -> dict[str, client_role_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.client_role_name] = dto
        return d
    def to_dict_by_role_description(self) -> dict[str, client_role_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.role_description] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[client_role_read_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[client_role_read_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return init
    def check_any(self, check_method: Callable[[client_role_read_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return init
    def map_to_string(self, map_method: Callable[[client_role_read_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[client_role_read_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[client_role_read_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, client_role_read_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, client_role_read_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, client_role_read_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[client_role_read_dto], bool]) -> client_role_read_dtos:
        return client_role_read_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[client_role_read_dto], str]) -> dict[str, client_role_read_dtos]:
        grp_data: dict[str, client_role_read_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = client_role_read_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[client_role_read_dto], str], agg_method: Callable[[client_role_read_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, client_role_read_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[client_role_read_dto], bool]) -> client_role_read_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[client_role_read_dto], any], compare_method: Callable[[any, any], bool]) -> client_role_read_dto | None:
        if len(self.dtos) == 0:
            return None
        else:
            max_value = value_method(self.dtos[0])
            max_elem = self.dtos[0]
            for dto in self.dtos:
                next_value = value_method(dto)
                if compare_method(next_value, max_value):
                    max_value = next_value
                    max_elem = dto
            return max_elem


@dataclass(frozen=False)
class client_status_read_dtos(base_read_dtos):
    dtos: list[client_status_read_dto]
    def __init__(self, dtos: list[client_status_read_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[client_status_read_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: client_status_read_dto):
        return cls(list([dto]))
    @classmethod
    def from_lists(cls, dtos1: list[client_status_read_dto], dtos2: list[client_status_read_dto]):
        return cls(dtos1 + dtos2)
    def get_active(self):
        return client_status_read_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return client_status_read_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_write_dtos(self) -> list[client_status_write_dto]:
        return list(map(lambda x: x.to_write(), self.dtos))
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write().to_write_dict(), self.dtos))
    def get_read_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> client_status_read_dto | None:
        found_dtos = list(filter(lambda x: x.client_status_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def get_first(self) -> client_status_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> client_status_read_dtos:
        if len(self.dtos) > n:
            return client_status_read_dtos(self.dtos[:n])
        else:
            return client_status_read_dtos(self.dtos)
    def get_last(self) -> client_status_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, client_status_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def to_dict_by_client_status_uid(self) -> dict[str, client_status_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.client_status_uid] = dto
        return d
    def to_dict_by_client_status_name(self) -> dict[str, client_status_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.client_status_name] = dto
        return d
    def to_dict_by_client_status_description(self) -> dict[str, client_status_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.client_status_description] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[client_status_read_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[client_status_read_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return init
    def check_any(self, check_method: Callable[[client_status_read_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return init
    def map_to_string(self, map_method: Callable[[client_status_read_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[client_status_read_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[client_status_read_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, client_status_read_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, client_status_read_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, client_status_read_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[client_status_read_dto], bool]) -> client_status_read_dtos:
        return client_status_read_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[client_status_read_dto], str]) -> dict[str, client_status_read_dtos]:
        grp_data: dict[str, client_status_read_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = client_status_read_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[client_status_read_dto], str], agg_method: Callable[[client_status_read_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, client_status_read_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[client_status_read_dto], bool]) -> client_status_read_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[client_status_read_dto], any], compare_method: Callable[[any, any], bool]) -> client_status_read_dto | None:
        if len(self.dtos) == 0:
            return None
        else:
            max_value = value_method(self.dtos[0])
            max_elem = self.dtos[0]
            for dto in self.dtos:
                next_value = value_method(dto)
                if compare_method(next_value, max_value):
                    max_value = next_value
                    max_elem = dto
            return max_elem


@dataclass(frozen=False)
class client_type_read_dtos(base_read_dtos):
    dtos: list[client_type_read_dto]
    def __init__(self, dtos: list[client_type_read_dto]):
        super().__init__(dtos)
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
        return list(map(lambda x: x.to_write(), self.dtos))
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
    def get_first_n(self, n: int) -> client_type_read_dtos:
        if len(self.dtos) > n:
            return client_type_read_dtos(self.dtos[:n])
        else:
            return client_type_read_dtos(self.dtos)
    def get_last(self) -> client_type_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
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
    def to_dict_by_client_type_name(self) -> dict[str, client_type_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.client_type_name] = dto
        return d
    def to_dict_by_client_type_description(self) -> dict[str, client_type_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.client_type_description] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[client_type_read_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[client_type_read_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return init
    def check_any(self, check_method: Callable[[client_type_read_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return init
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
    def find(self, check_method: Callable[[client_type_read_dto], bool]) -> client_type_read_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[client_type_read_dto], any], compare_method: Callable[[any, any], bool]) -> client_type_read_dto | None:
        if len(self.dtos) == 0:
            return None
        else:
            max_value = value_method(self.dtos[0])
            max_elem = self.dtos[0]
            for dto in self.dtos:
                next_value = value_method(dto)
                if compare_method(next_value, max_value):
                    max_value = next_value
                    max_elem = dto
            return max_elem


@dataclass(frozen=False)
class connection_engine_read_dtos(base_read_dtos):
    dtos: list[connection_engine_read_dto]
    def __init__(self, dtos: list[connection_engine_read_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[connection_engine_read_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: connection_engine_read_dto):
        return cls(list([dto]))
    @classmethod
    def from_lists(cls, dtos1: list[connection_engine_read_dto], dtos2: list[connection_engine_read_dto]):
        return cls(dtos1 + dtos2)
    def get_active(self):
        return connection_engine_read_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return connection_engine_read_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_write_dtos(self) -> list[connection_engine_write_dto]:
        return list(map(lambda x: x.to_write(), self.dtos))
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write().to_write_dict(), self.dtos))
    def get_read_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> connection_engine_read_dto | None:
        found_dtos = list(filter(lambda x: x.connection_engine_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def get_first(self) -> connection_engine_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> connection_engine_read_dtos:
        if len(self.dtos) > n:
            return connection_engine_read_dtos(self.dtos[:n])
        else:
            return connection_engine_read_dtos(self.dtos)
    def get_last(self) -> connection_engine_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, connection_engine_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def to_dict_by_connection_engine_uid(self) -> dict[str, connection_engine_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.connection_engine_uid] = dto
        return d
    def to_dict_by_connection_engine_name(self) -> dict[str, connection_engine_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.connection_engine_name] = dto
        return d
    def to_dict_by_start_date(self) -> dict[str, connection_engine_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.start_date] = dto
        return d
    def to_dict_by_calls_count(self) -> dict[str, connection_engine_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.calls_count] = dto
        return d
    def to_dict_by_last_time(self) -> dict[str, connection_engine_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.last_time] = dto
        return d
    def to_dict_by_host_count(self) -> dict[str, connection_engine_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.host_count] = dto
        return d
    def to_dict_by_user_count(self) -> dict[str, connection_engine_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.user_count] = dto
        return d
    def to_dict_by_token_count(self) -> dict[str, connection_engine_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.token_count] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[connection_engine_read_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[connection_engine_read_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return init
    def check_any(self, check_method: Callable[[connection_engine_read_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return init
    def map_to_string(self, map_method: Callable[[connection_engine_read_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[connection_engine_read_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[connection_engine_read_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, connection_engine_read_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, connection_engine_read_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, connection_engine_read_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[connection_engine_read_dto], bool]) -> connection_engine_read_dtos:
        return connection_engine_read_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[connection_engine_read_dto], str]) -> dict[str, connection_engine_read_dtos]:
        grp_data: dict[str, connection_engine_read_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = connection_engine_read_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[connection_engine_read_dto], str], agg_method: Callable[[connection_engine_read_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, connection_engine_read_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[connection_engine_read_dto], bool]) -> connection_engine_read_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[connection_engine_read_dto], any], compare_method: Callable[[any, any], bool]) -> connection_engine_read_dto | None:
        if len(self.dtos) == 0:
            return None
        else:
            max_value = value_method(self.dtos[0])
            max_elem = self.dtos[0]
            for dto in self.dtos:
                next_value = value_method(dto)
                if compare_method(next_value, max_value):
                    max_value = next_value
                    max_elem = dto
            return max_elem


@dataclass(frozen=False)
class connection_host_read_dtos(base_read_dtos):
    dtos: list[connection_host_read_dto]
    def __init__(self, dtos: list[connection_host_read_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[connection_host_read_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: connection_host_read_dto):
        return cls(list([dto]))
    @classmethod
    def from_lists(cls, dtos1: list[connection_host_read_dto], dtos2: list[connection_host_read_dto]):
        return cls(dtos1 + dtos2)
    def get_active(self):
        return connection_host_read_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return connection_host_read_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_write_dtos(self) -> list[connection_host_write_dto]:
        return list(map(lambda x: x.to_write(), self.dtos))
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write().to_write_dict(), self.dtos))
    def get_read_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> connection_host_read_dto | None:
        found_dtos = list(filter(lambda x: x.connection_host_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def get_first(self) -> connection_host_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> connection_host_read_dtos:
        if len(self.dtos) > n:
            return connection_host_read_dtos(self.dtos[:n])
        else:
            return connection_host_read_dtos(self.dtos)
    def get_last(self) -> connection_host_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, connection_host_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def to_dict_by_connection_host_uid(self) -> dict[str, connection_host_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.connection_host_uid] = dto
        return d
    def to_dict_by_connection_host_name(self) -> dict[str, connection_host_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.connection_host_name] = dto
        return d
    def to_dict_by_connection_engine_uid(self) -> dict[str, connection_host_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.connection_engine_uid] = dto
        return d
    def to_dict_by_host_ip(self) -> dict[str, connection_host_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.host_ip] = dto
        return d
    def to_dict_by_calls_count(self) -> dict[str, connection_host_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.calls_count] = dto
        return d
    def to_dict_by_start_time(self) -> dict[str, connection_host_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.start_time] = dto
        return d
    def to_dict_by_last_call_time(self) -> dict[str, connection_host_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.last_call_time] = dto
        return d
    def to_dict_by_user_count(self) -> dict[str, connection_host_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.user_count] = dto
        return d
    def to_dict_by_token_count(self) -> dict[str, connection_host_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.token_count] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[connection_host_read_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[connection_host_read_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return init
    def check_any(self, check_method: Callable[[connection_host_read_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return init
    def map_to_string(self, map_method: Callable[[connection_host_read_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[connection_host_read_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[connection_host_read_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, connection_host_read_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, connection_host_read_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, connection_host_read_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[connection_host_read_dto], bool]) -> connection_host_read_dtos:
        return connection_host_read_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[connection_host_read_dto], str]) -> dict[str, connection_host_read_dtos]:
        grp_data: dict[str, connection_host_read_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = connection_host_read_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[connection_host_read_dto], str], agg_method: Callable[[connection_host_read_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, connection_host_read_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[connection_host_read_dto], bool]) -> connection_host_read_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[connection_host_read_dto], any], compare_method: Callable[[any, any], bool]) -> connection_host_read_dto | None:
        if len(self.dtos) == 0:
            return None
        else:
            max_value = value_method(self.dtos[0])
            max_elem = self.dtos[0]
            for dto in self.dtos:
                next_value = value_method(dto)
                if compare_method(next_value, max_value):
                    max_value = next_value
                    max_elem = dto
            return max_elem


@dataclass(frozen=False)
class connection_user_read_dtos(base_read_dtos):
    dtos: list[connection_user_read_dto]
    def __init__(self, dtos: list[connection_user_read_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[connection_user_read_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: connection_user_read_dto):
        return cls(list([dto]))
    @classmethod
    def from_lists(cls, dtos1: list[connection_user_read_dto], dtos2: list[connection_user_read_dto]):
        return cls(dtos1 + dtos2)
    def get_active(self):
        return connection_user_read_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return connection_user_read_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_write_dtos(self) -> list[connection_user_write_dto]:
        return list(map(lambda x: x.to_write(), self.dtos))
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write().to_write_dict(), self.dtos))
    def get_read_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> connection_user_read_dto | None:
        found_dtos = list(filter(lambda x: x.connection_user_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def get_first(self) -> connection_user_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> connection_user_read_dtos:
        if len(self.dtos) > n:
            return connection_user_read_dtos(self.dtos[:n])
        else:
            return connection_user_read_dtos(self.dtos)
    def get_last(self) -> connection_user_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, connection_user_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def to_dict_by_connection_user_uid(self) -> dict[str, connection_user_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.connection_user_uid] = dto
        return d
    def to_dict_by_connection_user_name(self) -> dict[str, connection_user_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.connection_user_name] = dto
        return d
    def to_dict_by_connection_engine_uid(self) -> dict[str, connection_user_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.connection_engine_uid] = dto
        return d
    def to_dict_by_account_uid(self) -> dict[str, connection_user_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.account_uid] = dto
        return d
    def to_dict_by_call_count(self) -> dict[str, connection_user_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.call_count] = dto
        return d
    def to_dict_by_host_count(self) -> dict[str, connection_user_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.host_count] = dto
        return d
    def to_dict_by_token_count(self) -> dict[str, connection_user_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.token_count] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[connection_user_read_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[connection_user_read_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return init
    def check_any(self, check_method: Callable[[connection_user_read_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return init
    def map_to_string(self, map_method: Callable[[connection_user_read_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[connection_user_read_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[connection_user_read_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, connection_user_read_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, connection_user_read_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, connection_user_read_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[connection_user_read_dto], bool]) -> connection_user_read_dtos:
        return connection_user_read_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[connection_user_read_dto], str]) -> dict[str, connection_user_read_dtos]:
        grp_data: dict[str, connection_user_read_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = connection_user_read_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[connection_user_read_dto], str], agg_method: Callable[[connection_user_read_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, connection_user_read_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[connection_user_read_dto], bool]) -> connection_user_read_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[connection_user_read_dto], any], compare_method: Callable[[any, any], bool]) -> connection_user_read_dto | None:
        if len(self.dtos) == 0:
            return None
        else:
            max_value = value_method(self.dtos[0])
            max_elem = self.dtos[0]
            for dto in self.dtos:
                next_value = value_method(dto)
                if compare_method(next_value, max_value):
                    max_value = next_value
                    max_elem = dto
            return max_elem


@dataclass(frozen=False)
class country_read_dtos(base_read_dtos):
    dtos: list[country_read_dto]
    def __init__(self, dtos: list[country_read_dto]):
        super().__init__(dtos)
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
        return list(map(lambda x: x.to_write(), self.dtos))
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
    def get_first_n(self, n: int) -> country_read_dtos:
        if len(self.dtos) > n:
            return country_read_dtos(self.dtos[:n])
        else:
            return country_read_dtos(self.dtos)
    def get_last(self) -> country_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
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
    def to_dict_by_country_name(self) -> dict[str, country_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.country_name] = dto
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
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[country_read_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[country_read_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return init
    def check_any(self, check_method: Callable[[country_read_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return init
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
    def find(self, check_method: Callable[[country_read_dto], bool]) -> country_read_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[country_read_dto], any], compare_method: Callable[[any, any], bool]) -> country_read_dto | None:
        if len(self.dtos) == 0:
            return None
        else:
            max_value = value_method(self.dtos[0])
            max_elem = self.dtos[0]
            for dto in self.dtos:
                next_value = value_method(dto)
                if compare_method(next_value, max_value):
                    max_value = next_value
                    max_elem = dto
            return max_elem


@dataclass(frozen=False)
class currency_read_dtos(base_read_dtos):
    dtos: list[currency_read_dto]
    def __init__(self, dtos: list[currency_read_dto]):
        super().__init__(dtos)
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
        return list(map(lambda x: x.to_write(), self.dtos))
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
    def get_first_n(self, n: int) -> currency_read_dtos:
        if len(self.dtos) > n:
            return currency_read_dtos(self.dtos[:n])
        else:
            return currency_read_dtos(self.dtos)
    def get_last(self) -> currency_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
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
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[currency_read_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[currency_read_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return init
    def check_any(self, check_method: Callable[[currency_read_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return init
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
    def find(self, check_method: Callable[[currency_read_dto], bool]) -> currency_read_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[currency_read_dto], any], compare_method: Callable[[any, any], bool]) -> currency_read_dto | None:
        if len(self.dtos) == 0:
            return None
        else:
            max_value = value_method(self.dtos[0])
            max_elem = self.dtos[0]
            for dto in self.dtos:
                next_value = value_method(dto)
                if compare_method(next_value, max_value):
                    max_value = next_value
                    max_elem = dto
            return max_elem


@dataclass(frozen=False)
class event_acknowledge_read_dtos(base_read_dtos):
    dtos: list[event_acknowledge_read_dto]
    def __init__(self, dtos: list[event_acknowledge_read_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[event_acknowledge_read_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: event_acknowledge_read_dto):
        return cls(list([dto]))
    @classmethod
    def from_lists(cls, dtos1: list[event_acknowledge_read_dto], dtos2: list[event_acknowledge_read_dto]):
        return cls(dtos1 + dtos2)
    def get_active(self):
        return event_acknowledge_read_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return event_acknowledge_read_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_write_dtos(self) -> list[event_acknowledge_write_dto]:
        return list(map(lambda x: x.to_write(), self.dtos))
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write().to_write_dict(), self.dtos))
    def get_read_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> event_acknowledge_read_dto | None:
        found_dtos = list(filter(lambda x: x.event_acknowledge_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def get_first(self) -> event_acknowledge_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> event_acknowledge_read_dtos:
        if len(self.dtos) > n:
            return event_acknowledge_read_dtos(self.dtos[:n])
        else:
            return event_acknowledge_read_dtos(self.dtos)
    def get_last(self) -> event_acknowledge_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, event_acknowledge_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def to_dict_by_event_acknowledge_uid(self) -> dict[str, event_acknowledge_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.event_acknowledge_uid] = dto
        return d
    def to_dict_by_event_acknowledge_name(self) -> dict[str, event_acknowledge_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.event_acknowledge_name] = dto
        return d
    def to_dict_by_event_notification_uid(self) -> dict[str, event_acknowledge_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.event_notification_uid] = dto
        return d
    def to_dict_by_tenant_uid(self) -> dict[str, event_acknowledge_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.tenant_uid] = dto
        return d
    def to_dict_by_account_uid(self) -> dict[str, event_acknowledge_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.account_uid] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[event_acknowledge_read_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[event_acknowledge_read_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return init
    def check_any(self, check_method: Callable[[event_acknowledge_read_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return init
    def map_to_string(self, map_method: Callable[[event_acknowledge_read_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[event_acknowledge_read_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[event_acknowledge_read_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, event_acknowledge_read_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, event_acknowledge_read_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, event_acknowledge_read_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[event_acknowledge_read_dto], bool]) -> event_acknowledge_read_dtos:
        return event_acknowledge_read_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[event_acknowledge_read_dto], str]) -> dict[str, event_acknowledge_read_dtos]:
        grp_data: dict[str, event_acknowledge_read_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = event_acknowledge_read_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[event_acknowledge_read_dto], str], agg_method: Callable[[event_acknowledge_read_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, event_acknowledge_read_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[event_acknowledge_read_dto], bool]) -> event_acknowledge_read_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[event_acknowledge_read_dto], any], compare_method: Callable[[any, any], bool]) -> event_acknowledge_read_dto | None:
        if len(self.dtos) == 0:
            return None
        else:
            max_value = value_method(self.dtos[0])
            max_elem = self.dtos[0]
            for dto in self.dtos:
                next_value = value_method(dto)
                if compare_method(next_value, max_value):
                    max_value = next_value
                    max_elem = dto
            return max_elem


@dataclass(frozen=False)
class event_channel_read_dtos(base_read_dtos):
    dtos: list[event_channel_read_dto]
    def __init__(self, dtos: list[event_channel_read_dto]):
        super().__init__(dtos)
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
        return list(map(lambda x: x.to_write(), self.dtos))
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
    def get_first_n(self, n: int) -> event_channel_read_dtos:
        if len(self.dtos) > n:
            return event_channel_read_dtos(self.dtos[:n])
        else:
            return event_channel_read_dtos(self.dtos)
    def get_last(self) -> event_channel_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
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
    def to_dict_by_event_channel_name(self) -> dict[str, event_channel_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.event_channel_name] = dto
        return d
    def to_dict_by_event_channel_type_uid(self) -> dict[str, event_channel_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.event_channel_type_uid] = dto
        return d
    def to_dict_by_channel_definition(self) -> dict[str, event_channel_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.channel_definition] = dto
        return d
    def to_dict_by_last_status_name(self) -> dict[str, event_channel_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.last_status_name] = dto
        return d
    def to_dict_by_tenant_uid(self) -> dict[str, event_channel_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.tenant_uid] = dto
        return d
    def to_dict_by_account_uid(self) -> dict[str, event_channel_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.account_uid] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[event_channel_read_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[event_channel_read_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return init
    def check_any(self, check_method: Callable[[event_channel_read_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return init
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
    def find(self, check_method: Callable[[event_channel_read_dto], bool]) -> event_channel_read_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[event_channel_read_dto], any], compare_method: Callable[[any, any], bool]) -> event_channel_read_dto | None:
        if len(self.dtos) == 0:
            return None
        else:
            max_value = value_method(self.dtos[0])
            max_elem = self.dtos[0]
            for dto in self.dtos:
                next_value = value_method(dto)
                if compare_method(next_value, max_value):
                    max_value = next_value
                    max_elem = dto
            return max_elem


@dataclass(frozen=False)
class event_channel_type_read_dtos(base_read_dtos):
    dtos: list[event_channel_type_read_dto]
    def __init__(self, dtos: list[event_channel_type_read_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[event_channel_type_read_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: event_channel_type_read_dto):
        return cls(list([dto]))
    @classmethod
    def from_lists(cls, dtos1: list[event_channel_type_read_dto], dtos2: list[event_channel_type_read_dto]):
        return cls(dtos1 + dtos2)
    def get_active(self):
        return event_channel_type_read_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return event_channel_type_read_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_write_dtos(self) -> list[event_channel_type_write_dto]:
        return list(map(lambda x: x.to_write(), self.dtos))
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write().to_write_dict(), self.dtos))
    def get_read_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> event_channel_type_read_dto | None:
        found_dtos = list(filter(lambda x: x.event_channel_type_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def get_first(self) -> event_channel_type_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> event_channel_type_read_dtos:
        if len(self.dtos) > n:
            return event_channel_type_read_dtos(self.dtos[:n])
        else:
            return event_channel_type_read_dtos(self.dtos)
    def get_last(self) -> event_channel_type_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, event_channel_type_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def to_dict_by_event_channel_type_uid(self) -> dict[str, event_channel_type_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.event_channel_type_uid] = dto
        return d
    def to_dict_by_event_channel_type_name(self) -> dict[str, event_channel_type_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.event_channel_type_name] = dto
        return d
    def to_dict_by_channel_type_description(self) -> dict[str, event_channel_type_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.channel_type_description] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[event_channel_type_read_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[event_channel_type_read_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return init
    def check_any(self, check_method: Callable[[event_channel_type_read_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return init
    def map_to_string(self, map_method: Callable[[event_channel_type_read_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[event_channel_type_read_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[event_channel_type_read_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, event_channel_type_read_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, event_channel_type_read_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, event_channel_type_read_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[event_channel_type_read_dto], bool]) -> event_channel_type_read_dtos:
        return event_channel_type_read_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[event_channel_type_read_dto], str]) -> dict[str, event_channel_type_read_dtos]:
        grp_data: dict[str, event_channel_type_read_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = event_channel_type_read_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[event_channel_type_read_dto], str], agg_method: Callable[[event_channel_type_read_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, event_channel_type_read_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[event_channel_type_read_dto], bool]) -> event_channel_type_read_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[event_channel_type_read_dto], any], compare_method: Callable[[any, any], bool]) -> event_channel_type_read_dto | None:
        if len(self.dtos) == 0:
            return None
        else:
            max_value = value_method(self.dtos[0])
            max_elem = self.dtos[0]
            for dto in self.dtos:
                next_value = value_method(dto)
                if compare_method(next_value, max_value):
                    max_value = next_value
                    max_elem = dto
            return max_elem


@dataclass(frozen=False)
class event_instance_read_dtos(base_read_dtos):
    dtos: list[event_instance_read_dto]
    def __init__(self, dtos: list[event_instance_read_dto]):
        super().__init__(dtos)
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
        return list(map(lambda x: x.to_write(), self.dtos))
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
    def get_first_n(self, n: int) -> event_instance_read_dtos:
        if len(self.dtos) > n:
            return event_instance_read_dtos(self.dtos[:n])
        else:
            return event_instance_read_dtos(self.dtos)
    def get_last(self) -> event_instance_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
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
    def to_dict_by_event_instance_name(self) -> dict[str, event_instance_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.event_instance_name] = dto
        return d
    def to_dict_by_client_uid(self) -> dict[str, event_instance_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.client_uid] = dto
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
    def to_dict_by_event_date(self) -> dict[str, event_instance_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.event_date] = dto
        return d
    def to_dict_by_published_count(self) -> dict[str, event_instance_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.published_count] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[event_instance_read_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[event_instance_read_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return init
    def check_any(self, check_method: Callable[[event_instance_read_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return init
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
    def find(self, check_method: Callable[[event_instance_read_dto], bool]) -> event_instance_read_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[event_instance_read_dto], any], compare_method: Callable[[any, any], bool]) -> event_instance_read_dto | None:
        if len(self.dtos) == 0:
            return None
        else:
            max_value = value_method(self.dtos[0])
            max_elem = self.dtos[0]
            for dto in self.dtos:
                next_value = value_method(dto)
                if compare_method(next_value, max_value):
                    max_value = next_value
                    max_elem = dto
            return max_elem


@dataclass(frozen=False)
class event_notification_read_dtos(base_read_dtos):
    dtos: list[event_notification_read_dto]
    def __init__(self, dtos: list[event_notification_read_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[event_notification_read_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: event_notification_read_dto):
        return cls(list([dto]))
    @classmethod
    def from_lists(cls, dtos1: list[event_notification_read_dto], dtos2: list[event_notification_read_dto]):
        return cls(dtos1 + dtos2)
    def get_active(self):
        return event_notification_read_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return event_notification_read_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_write_dtos(self) -> list[event_notification_write_dto]:
        return list(map(lambda x: x.to_write(), self.dtos))
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write().to_write_dict(), self.dtos))
    def get_read_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> event_notification_read_dto | None:
        found_dtos = list(filter(lambda x: x.event_notification_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def get_first(self) -> event_notification_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> event_notification_read_dtos:
        if len(self.dtos) > n:
            return event_notification_read_dtos(self.dtos[:n])
        else:
            return event_notification_read_dtos(self.dtos)
    def get_last(self) -> event_notification_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, event_notification_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def to_dict_by_event_notification_uid(self) -> dict[str, event_notification_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.event_notification_uid] = dto
        return d
    def to_dict_by_event_notification_name(self) -> dict[str, event_notification_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.event_notification_name] = dto
        return d
    def to_dict_by_tenant_uid(self) -> dict[str, event_notification_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.tenant_uid] = dto
        return d
    def to_dict_by_account_uid(self) -> dict[str, event_notification_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.account_uid] = dto
        return d
    def to_dict_by_notification_type(self) -> dict[str, event_notification_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.notification_type] = dto
        return d
    def to_dict_by_notification_topic(self) -> dict[str, event_notification_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.notification_topic] = dto
        return d
    def to_dict_by_notification_format(self) -> dict[str, event_notification_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.notification_format] = dto
        return d
    def to_dict_by_notification_content(self) -> dict[str, event_notification_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.notification_content] = dto
        return d
    def to_dict_by_sending_status(self) -> dict[str, event_notification_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.sending_status] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[event_notification_read_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[event_notification_read_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return init
    def check_any(self, check_method: Callable[[event_notification_read_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return init
    def map_to_string(self, map_method: Callable[[event_notification_read_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[event_notification_read_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[event_notification_read_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, event_notification_read_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, event_notification_read_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, event_notification_read_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[event_notification_read_dto], bool]) -> event_notification_read_dtos:
        return event_notification_read_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[event_notification_read_dto], str]) -> dict[str, event_notification_read_dtos]:
        grp_data: dict[str, event_notification_read_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = event_notification_read_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[event_notification_read_dto], str], agg_method: Callable[[event_notification_read_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, event_notification_read_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[event_notification_read_dto], bool]) -> event_notification_read_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[event_notification_read_dto], any], compare_method: Callable[[any, any], bool]) -> event_notification_read_dto | None:
        if len(self.dtos) == 0:
            return None
        else:
            max_value = value_method(self.dtos[0])
            max_elem = self.dtos[0]
            for dto in self.dtos:
                next_value = value_method(dto)
                if compare_method(next_value, max_value):
                    max_value = next_value
                    max_elem = dto
            return max_elem


@dataclass(frozen=False)
class event_observer_read_dtos(base_read_dtos):
    dtos: list[event_observer_read_dto]
    def __init__(self, dtos: list[event_observer_read_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[event_observer_read_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: event_observer_read_dto):
        return cls(list([dto]))
    @classmethod
    def from_lists(cls, dtos1: list[event_observer_read_dto], dtos2: list[event_observer_read_dto]):
        return cls(dtos1 + dtos2)
    def get_active(self):
        return event_observer_read_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return event_observer_read_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_write_dtos(self) -> list[event_observer_write_dto]:
        return list(map(lambda x: x.to_write(), self.dtos))
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write().to_write_dict(), self.dtos))
    def get_read_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> event_observer_read_dto | None:
        found_dtos = list(filter(lambda x: x.event_observer_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def get_first(self) -> event_observer_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> event_observer_read_dtos:
        if len(self.dtos) > n:
            return event_observer_read_dtos(self.dtos[:n])
        else:
            return event_observer_read_dtos(self.dtos)
    def get_last(self) -> event_observer_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, event_observer_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def to_dict_by_event_observer_uid(self) -> dict[str, event_observer_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.event_observer_uid] = dto
        return d
    def to_dict_by_event_observer_name(self) -> dict[str, event_observer_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.event_observer_name] = dto
        return d
    def to_dict_by_event_observer_definition(self) -> dict[str, event_observer_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.event_observer_definition] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[event_observer_read_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[event_observer_read_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return init
    def check_any(self, check_method: Callable[[event_observer_read_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return init
    def map_to_string(self, map_method: Callable[[event_observer_read_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[event_observer_read_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[event_observer_read_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, event_observer_read_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, event_observer_read_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, event_observer_read_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[event_observer_read_dto], bool]) -> event_observer_read_dtos:
        return event_observer_read_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[event_observer_read_dto], str]) -> dict[str, event_observer_read_dtos]:
        grp_data: dict[str, event_observer_read_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = event_observer_read_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[event_observer_read_dto], str], agg_method: Callable[[event_observer_read_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, event_observer_read_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[event_observer_read_dto], bool]) -> event_observer_read_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[event_observer_read_dto], any], compare_method: Callable[[any, any], bool]) -> event_observer_read_dto | None:
        if len(self.dtos) == 0:
            return None
        else:
            max_value = value_method(self.dtos[0])
            max_elem = self.dtos[0]
            for dto in self.dtos:
                next_value = value_method(dto)
                if compare_method(next_value, max_value):
                    max_value = next_value
                    max_elem = dto
            return max_elem


@dataclass(frozen=False)
class event_subscription_read_dtos(base_read_dtos):
    dtos: list[event_subscription_read_dto]
    def __init__(self, dtos: list[event_subscription_read_dto]):
        super().__init__(dtos)
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
        return list(map(lambda x: x.to_write(), self.dtos))
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
    def get_first_n(self, n: int) -> event_subscription_read_dtos:
        if len(self.dtos) > n:
            return event_subscription_read_dtos(self.dtos[:n])
        else:
            return event_subscription_read_dtos(self.dtos)
    def get_last(self) -> event_subscription_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
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
    def to_dict_by_event_subscription_name(self) -> dict[str, event_subscription_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.event_subscription_name] = dto
        return d
    def to_dict_by_event_channel_uid(self) -> dict[str, event_subscription_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.event_channel_uid] = dto
        return d
    def to_dict_by_tenant_uid(self) -> dict[str, event_subscription_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.tenant_uid] = dto
        return d
    def to_dict_by_account_uid(self) -> dict[str, event_subscription_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.account_uid] = dto
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
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[event_subscription_read_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[event_subscription_read_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return init
    def check_any(self, check_method: Callable[[event_subscription_read_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return init
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
    def find(self, check_method: Callable[[event_subscription_read_dto], bool]) -> event_subscription_read_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[event_subscription_read_dto], any], compare_method: Callable[[any, any], bool]) -> event_subscription_read_dto | None:
        if len(self.dtos) == 0:
            return None
        else:
            max_value = value_method(self.dtos[0])
            max_elem = self.dtos[0]
            for dto in self.dtos:
                next_value = value_method(dto)
                if compare_method(next_value, max_value):
                    max_value = next_value
                    max_elem = dto
            return max_elem


@dataclass(frozen=False)
class event_template_read_dtos(base_read_dtos):
    dtos: list[event_template_read_dto]
    def __init__(self, dtos: list[event_template_read_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[event_template_read_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: event_template_read_dto):
        return cls(list([dto]))
    @classmethod
    def from_lists(cls, dtos1: list[event_template_read_dto], dtos2: list[event_template_read_dto]):
        return cls(dtos1 + dtos2)
    def get_active(self):
        return event_template_read_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return event_template_read_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_write_dtos(self) -> list[event_template_write_dto]:
        return list(map(lambda x: x.to_write(), self.dtos))
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write().to_write_dict(), self.dtos))
    def get_read_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> event_template_read_dto | None:
        found_dtos = list(filter(lambda x: x.event_template_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def get_first(self) -> event_template_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> event_template_read_dtos:
        if len(self.dtos) > n:
            return event_template_read_dtos(self.dtos[:n])
        else:
            return event_template_read_dtos(self.dtos)
    def get_last(self) -> event_template_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, event_template_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def to_dict_by_event_template_uid(self) -> dict[str, event_template_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.event_template_uid] = dto
        return d
    def to_dict_by_event_template_name(self) -> dict[str, event_template_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.event_template_name] = dto
        return d
    def to_dict_by_tenant_uid(self) -> dict[str, event_template_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.tenant_uid] = dto
        return d
    def to_dict_by_notification_type(self) -> dict[str, event_template_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.notification_type] = dto
        return d
    def to_dict_by_notification_topic(self) -> dict[str, event_template_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.notification_topic] = dto
        return d
    def to_dict_by_notification_format(self) -> dict[str, event_template_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.notification_format] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[event_template_read_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[event_template_read_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return init
    def check_any(self, check_method: Callable[[event_template_read_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return init
    def map_to_string(self, map_method: Callable[[event_template_read_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[event_template_read_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[event_template_read_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, event_template_read_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, event_template_read_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, event_template_read_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[event_template_read_dto], bool]) -> event_template_read_dtos:
        return event_template_read_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[event_template_read_dto], str]) -> dict[str, event_template_read_dtos]:
        grp_data: dict[str, event_template_read_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = event_template_read_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[event_template_read_dto], str], agg_method: Callable[[event_template_read_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, event_template_read_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[event_template_read_dto], bool]) -> event_template_read_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[event_template_read_dto], any], compare_method: Callable[[any, any], bool]) -> event_template_read_dto | None:
        if len(self.dtos) == 0:
            return None
        else:
            max_value = value_method(self.dtos[0])
            max_elem = self.dtos[0]
            for dto in self.dtos:
                next_value = value_method(dto)
                if compare_method(next_value, max_value):
                    max_value = next_value
                    max_elem = dto
            return max_elem


@dataclass(frozen=False)
class event_type_read_dtos(base_read_dtos):
    dtos: list[event_type_read_dto]
    def __init__(self, dtos: list[event_type_read_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[event_type_read_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: event_type_read_dto):
        return cls(list([dto]))
    @classmethod
    def from_lists(cls, dtos1: list[event_type_read_dto], dtos2: list[event_type_read_dto]):
        return cls(dtos1 + dtos2)
    def get_active(self):
        return event_type_read_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return event_type_read_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_write_dtos(self) -> list[event_type_write_dto]:
        return list(map(lambda x: x.to_write(), self.dtos))
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write().to_write_dict(), self.dtos))
    def get_read_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> event_type_read_dto | None:
        found_dtos = list(filter(lambda x: x.event_type_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def get_first(self) -> event_type_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> event_type_read_dtos:
        if len(self.dtos) > n:
            return event_type_read_dtos(self.dtos[:n])
        else:
            return event_type_read_dtos(self.dtos)
    def get_last(self) -> event_type_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, event_type_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def to_dict_by_event_type_uid(self) -> dict[str, event_type_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.event_type_uid] = dto
        return d
    def to_dict_by_event_type_name(self) -> dict[str, event_type_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.event_type_name] = dto
        return d
    def to_dict_by_event_type_description(self) -> dict[str, event_type_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.event_type_description] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[event_type_read_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[event_type_read_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return init
    def check_any(self, check_method: Callable[[event_type_read_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return init
    def map_to_string(self, map_method: Callable[[event_type_read_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[event_type_read_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[event_type_read_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, event_type_read_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, event_type_read_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, event_type_read_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[event_type_read_dto], bool]) -> event_type_read_dtos:
        return event_type_read_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[event_type_read_dto], str]) -> dict[str, event_type_read_dtos]:
        grp_data: dict[str, event_type_read_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = event_type_read_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[event_type_read_dto], str], agg_method: Callable[[event_type_read_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, event_type_read_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[event_type_read_dto], bool]) -> event_type_read_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[event_type_read_dto], any], compare_method: Callable[[any, any], bool]) -> event_type_read_dto | None:
        if len(self.dtos) == 0:
            return None
        else:
            max_value = value_method(self.dtos[0])
            max_elem = self.dtos[0]
            for dto in self.dtos:
                next_value = value_method(dto)
                if compare_method(next_value, max_value):
                    max_value = next_value
                    max_elem = dto
            return max_elem


@dataclass(frozen=False)
class invoice_action_read_dtos(base_read_dtos):
    dtos: list[invoice_action_read_dto]
    def __init__(self, dtos: list[invoice_action_read_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[invoice_action_read_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: invoice_action_read_dto):
        return cls(list([dto]))
    @classmethod
    def from_lists(cls, dtos1: list[invoice_action_read_dto], dtos2: list[invoice_action_read_dto]):
        return cls(dtos1 + dtos2)
    def get_active(self):
        return invoice_action_read_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return invoice_action_read_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_write_dtos(self) -> list[invoice_action_write_dto]:
        return list(map(lambda x: x.to_write(), self.dtos))
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write().to_write_dict(), self.dtos))
    def get_read_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> invoice_action_read_dto | None:
        found_dtos = list(filter(lambda x: x.invoice_action_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def get_first(self) -> invoice_action_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> invoice_action_read_dtos:
        if len(self.dtos) > n:
            return invoice_action_read_dtos(self.dtos[:n])
        else:
            return invoice_action_read_dtos(self.dtos)
    def get_last(self) -> invoice_action_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, invoice_action_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def to_dict_by_invoice_action_uid(self) -> dict[str, invoice_action_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.invoice_action_uid] = dto
        return d
    def to_dict_by_invoice_action_name(self) -> dict[str, invoice_action_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.invoice_action_name] = dto
        return d
    def to_dict_by_tenant_uid(self) -> dict[str, invoice_action_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.tenant_uid] = dto
        return d
    def to_dict_by_account_uid(self) -> dict[str, invoice_action_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.account_uid] = dto
        return d
    def to_dict_by_invoice_instance_uid(self) -> dict[str, invoice_action_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.invoice_instance_uid] = dto
        return d
    def to_dict_by_invoice_action_type_uid(self) -> dict[str, invoice_action_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.invoice_action_type_uid] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[invoice_action_read_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[invoice_action_read_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return init
    def check_any(self, check_method: Callable[[invoice_action_read_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return init
    def map_to_string(self, map_method: Callable[[invoice_action_read_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[invoice_action_read_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[invoice_action_read_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, invoice_action_read_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, invoice_action_read_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, invoice_action_read_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[invoice_action_read_dto], bool]) -> invoice_action_read_dtos:
        return invoice_action_read_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[invoice_action_read_dto], str]) -> dict[str, invoice_action_read_dtos]:
        grp_data: dict[str, invoice_action_read_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = invoice_action_read_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[invoice_action_read_dto], str], agg_method: Callable[[invoice_action_read_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, invoice_action_read_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[invoice_action_read_dto], bool]) -> invoice_action_read_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[invoice_action_read_dto], any], compare_method: Callable[[any, any], bool]) -> invoice_action_read_dto | None:
        if len(self.dtos) == 0:
            return None
        else:
            max_value = value_method(self.dtos[0])
            max_elem = self.dtos[0]
            for dto in self.dtos:
                next_value = value_method(dto)
                if compare_method(next_value, max_value):
                    max_value = next_value
                    max_elem = dto
            return max_elem


@dataclass(frozen=False)
class invoice_action_type_read_dtos(base_read_dtos):
    dtos: list[invoice_action_type_read_dto]
    def __init__(self, dtos: list[invoice_action_type_read_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[invoice_action_type_read_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: invoice_action_type_read_dto):
        return cls(list([dto]))
    @classmethod
    def from_lists(cls, dtos1: list[invoice_action_type_read_dto], dtos2: list[invoice_action_type_read_dto]):
        return cls(dtos1 + dtos2)
    def get_active(self):
        return invoice_action_type_read_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return invoice_action_type_read_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_write_dtos(self) -> list[invoice_action_type_write_dto]:
        return list(map(lambda x: x.to_write(), self.dtos))
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write().to_write_dict(), self.dtos))
    def get_read_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> invoice_action_type_read_dto | None:
        found_dtos = list(filter(lambda x: x.invoice_action_type_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def get_first(self) -> invoice_action_type_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> invoice_action_type_read_dtos:
        if len(self.dtos) > n:
            return invoice_action_type_read_dtos(self.dtos[:n])
        else:
            return invoice_action_type_read_dtos(self.dtos)
    def get_last(self) -> invoice_action_type_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, invoice_action_type_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def to_dict_by_invoice_action_type_uid(self) -> dict[str, invoice_action_type_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.invoice_action_type_uid] = dto
        return d
    def to_dict_by_invoice_action_type_name(self) -> dict[str, invoice_action_type_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.invoice_action_type_name] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[invoice_action_type_read_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[invoice_action_type_read_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return init
    def check_any(self, check_method: Callable[[invoice_action_type_read_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return init
    def map_to_string(self, map_method: Callable[[invoice_action_type_read_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[invoice_action_type_read_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[invoice_action_type_read_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, invoice_action_type_read_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, invoice_action_type_read_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, invoice_action_type_read_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[invoice_action_type_read_dto], bool]) -> invoice_action_type_read_dtos:
        return invoice_action_type_read_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[invoice_action_type_read_dto], str]) -> dict[str, invoice_action_type_read_dtos]:
        grp_data: dict[str, invoice_action_type_read_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = invoice_action_type_read_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[invoice_action_type_read_dto], str], agg_method: Callable[[invoice_action_type_read_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, invoice_action_type_read_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[invoice_action_type_read_dto], bool]) -> invoice_action_type_read_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[invoice_action_type_read_dto], any], compare_method: Callable[[any, any], bool]) -> invoice_action_type_read_dto | None:
        if len(self.dtos) == 0:
            return None
        else:
            max_value = value_method(self.dtos[0])
            max_elem = self.dtos[0]
            for dto in self.dtos:
                next_value = value_method(dto)
                if compare_method(next_value, max_value):
                    max_value = next_value
                    max_elem = dto
            return max_elem


@dataclass(frozen=False)
class invoice_category_read_dtos(base_read_dtos):
    dtos: list[invoice_category_read_dto]
    def __init__(self, dtos: list[invoice_category_read_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[invoice_category_read_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: invoice_category_read_dto):
        return cls(list([dto]))
    @classmethod
    def from_lists(cls, dtos1: list[invoice_category_read_dto], dtos2: list[invoice_category_read_dto]):
        return cls(dtos1 + dtos2)
    def get_active(self):
        return invoice_category_read_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return invoice_category_read_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_write_dtos(self) -> list[invoice_category_write_dto]:
        return list(map(lambda x: x.to_write(), self.dtos))
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write().to_write_dict(), self.dtos))
    def get_read_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> invoice_category_read_dto | None:
        found_dtos = list(filter(lambda x: x.invoice_category_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def get_first(self) -> invoice_category_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> invoice_category_read_dtos:
        if len(self.dtos) > n:
            return invoice_category_read_dtos(self.dtos[:n])
        else:
            return invoice_category_read_dtos(self.dtos)
    def get_last(self) -> invoice_category_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, invoice_category_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def to_dict_by_invoice_category_uid(self) -> dict[str, invoice_category_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.invoice_category_uid] = dto
        return d
    def to_dict_by_invoice_category_name(self) -> dict[str, invoice_category_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.invoice_category_name] = dto
        return d
    def to_dict_by_tenant_uid(self) -> dict[str, invoice_category_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.tenant_uid] = dto
        return d
    def to_dict_by_invoice_category_description(self) -> dict[str, invoice_category_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.invoice_category_description] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[invoice_category_read_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[invoice_category_read_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return init
    def check_any(self, check_method: Callable[[invoice_category_read_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return init
    def map_to_string(self, map_method: Callable[[invoice_category_read_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[invoice_category_read_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[invoice_category_read_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, invoice_category_read_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, invoice_category_read_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, invoice_category_read_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[invoice_category_read_dto], bool]) -> invoice_category_read_dtos:
        return invoice_category_read_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[invoice_category_read_dto], str]) -> dict[str, invoice_category_read_dtos]:
        grp_data: dict[str, invoice_category_read_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = invoice_category_read_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[invoice_category_read_dto], str], agg_method: Callable[[invoice_category_read_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, invoice_category_read_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[invoice_category_read_dto], bool]) -> invoice_category_read_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[invoice_category_read_dto], any], compare_method: Callable[[any, any], bool]) -> invoice_category_read_dto | None:
        if len(self.dtos) == 0:
            return None
        else:
            max_value = value_method(self.dtos[0])
            max_elem = self.dtos[0]
            for dto in self.dtos:
                next_value = value_method(dto)
                if compare_method(next_value, max_value):
                    max_value = next_value
                    max_elem = dto
            return max_elem


@dataclass(frozen=False)
class invoice_entry_read_dtos(base_read_dtos):
    dtos: list[invoice_entry_read_dto]
    def __init__(self, dtos: list[invoice_entry_read_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[invoice_entry_read_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: invoice_entry_read_dto):
        return cls(list([dto]))
    @classmethod
    def from_lists(cls, dtos1: list[invoice_entry_read_dto], dtos2: list[invoice_entry_read_dto]):
        return cls(dtos1 + dtos2)
    def get_active(self):
        return invoice_entry_read_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return invoice_entry_read_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_write_dtos(self) -> list[invoice_entry_write_dto]:
        return list(map(lambda x: x.to_write(), self.dtos))
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write().to_write_dict(), self.dtos))
    def get_read_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> invoice_entry_read_dto | None:
        found_dtos = list(filter(lambda x: x.invoice_entry_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def get_first(self) -> invoice_entry_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> invoice_entry_read_dtos:
        if len(self.dtos) > n:
            return invoice_entry_read_dtos(self.dtos[:n])
        else:
            return invoice_entry_read_dtos(self.dtos)
    def get_last(self) -> invoice_entry_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, invoice_entry_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def to_dict_by_invoice_entry_uid(self) -> dict[str, invoice_entry_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.invoice_entry_uid] = dto
        return d
    def to_dict_by_invoice_entry_name(self) -> dict[str, invoice_entry_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.invoice_entry_name] = dto
        return d
    def to_dict_by_tenant_uid(self) -> dict[str, invoice_entry_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.tenant_uid] = dto
        return d
    def to_dict_by_account_uid(self) -> dict[str, invoice_entry_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.account_uid] = dto
        return d
    def to_dict_by_invoice_instance_uid(self) -> dict[str, invoice_entry_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.invoice_instance_uid] = dto
        return d
    def to_dict_by_entry_details(self) -> dict[str, invoice_entry_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.entry_details] = dto
        return d
    def to_dict_by_entry_amount_net(self) -> dict[str, invoice_entry_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.entry_amount_net] = dto
        return d
    def to_dict_by_entry_amount_tax(self) -> dict[str, invoice_entry_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.entry_amount_tax] = dto
        return d
    def to_dict_by_entry_amount_gross(self) -> dict[str, invoice_entry_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.entry_amount_gross] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[invoice_entry_read_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[invoice_entry_read_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return init
    def check_any(self, check_method: Callable[[invoice_entry_read_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return init
    def map_to_string(self, map_method: Callable[[invoice_entry_read_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[invoice_entry_read_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[invoice_entry_read_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, invoice_entry_read_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, invoice_entry_read_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, invoice_entry_read_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[invoice_entry_read_dto], bool]) -> invoice_entry_read_dtos:
        return invoice_entry_read_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[invoice_entry_read_dto], str]) -> dict[str, invoice_entry_read_dtos]:
        grp_data: dict[str, invoice_entry_read_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = invoice_entry_read_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[invoice_entry_read_dto], str], agg_method: Callable[[invoice_entry_read_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, invoice_entry_read_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[invoice_entry_read_dto], bool]) -> invoice_entry_read_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[invoice_entry_read_dto], any], compare_method: Callable[[any, any], bool]) -> invoice_entry_read_dto | None:
        if len(self.dtos) == 0:
            return None
        else:
            max_value = value_method(self.dtos[0])
            max_elem = self.dtos[0]
            for dto in self.dtos:
                next_value = value_method(dto)
                if compare_method(next_value, max_value):
                    max_value = next_value
                    max_elem = dto
            return max_elem


@dataclass(frozen=False)
class invoice_flow_read_dtos(base_read_dtos):
    dtos: list[invoice_flow_read_dto]
    def __init__(self, dtos: list[invoice_flow_read_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[invoice_flow_read_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: invoice_flow_read_dto):
        return cls(list([dto]))
    @classmethod
    def from_lists(cls, dtos1: list[invoice_flow_read_dto], dtos2: list[invoice_flow_read_dto]):
        return cls(dtos1 + dtos2)
    def get_active(self):
        return invoice_flow_read_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return invoice_flow_read_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_write_dtos(self) -> list[invoice_flow_write_dto]:
        return list(map(lambda x: x.to_write(), self.dtos))
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write().to_write_dict(), self.dtos))
    def get_read_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> invoice_flow_read_dto | None:
        found_dtos = list(filter(lambda x: x.invoice_flow_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def get_first(self) -> invoice_flow_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> invoice_flow_read_dtos:
        if len(self.dtos) > n:
            return invoice_flow_read_dtos(self.dtos[:n])
        else:
            return invoice_flow_read_dtos(self.dtos)
    def get_last(self) -> invoice_flow_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, invoice_flow_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def to_dict_by_invoice_flow_uid(self) -> dict[str, invoice_flow_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.invoice_flow_uid] = dto
        return d
    def to_dict_by_invoice_flow_name(self) -> dict[str, invoice_flow_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.invoice_flow_name] = dto
        return d
    def to_dict_by_flow_description(self) -> dict[str, invoice_flow_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.flow_description] = dto
        return d
    def to_dict_by_flow_definition_json(self) -> dict[str, invoice_flow_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.flow_definition_json] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[invoice_flow_read_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[invoice_flow_read_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return init
    def check_any(self, check_method: Callable[[invoice_flow_read_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return init
    def map_to_string(self, map_method: Callable[[invoice_flow_read_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[invoice_flow_read_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[invoice_flow_read_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, invoice_flow_read_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, invoice_flow_read_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, invoice_flow_read_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[invoice_flow_read_dto], bool]) -> invoice_flow_read_dtos:
        return invoice_flow_read_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[invoice_flow_read_dto], str]) -> dict[str, invoice_flow_read_dtos]:
        grp_data: dict[str, invoice_flow_read_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = invoice_flow_read_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[invoice_flow_read_dto], str], agg_method: Callable[[invoice_flow_read_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, invoice_flow_read_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[invoice_flow_read_dto], bool]) -> invoice_flow_read_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[invoice_flow_read_dto], any], compare_method: Callable[[any, any], bool]) -> invoice_flow_read_dto | None:
        if len(self.dtos) == 0:
            return None
        else:
            max_value = value_method(self.dtos[0])
            max_elem = self.dtos[0]
            for dto in self.dtos:
                next_value = value_method(dto)
                if compare_method(next_value, max_value):
                    max_value = next_value
                    max_elem = dto
            return max_elem


@dataclass(frozen=False)
class invoice_flow_state_read_dtos(base_read_dtos):
    dtos: list[invoice_flow_state_read_dto]
    def __init__(self, dtos: list[invoice_flow_state_read_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[invoice_flow_state_read_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: invoice_flow_state_read_dto):
        return cls(list([dto]))
    @classmethod
    def from_lists(cls, dtos1: list[invoice_flow_state_read_dto], dtos2: list[invoice_flow_state_read_dto]):
        return cls(dtos1 + dtos2)
    def get_active(self):
        return invoice_flow_state_read_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return invoice_flow_state_read_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_write_dtos(self) -> list[invoice_flow_state_write_dto]:
        return list(map(lambda x: x.to_write(), self.dtos))
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write().to_write_dict(), self.dtos))
    def get_read_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> invoice_flow_state_read_dto | None:
        found_dtos = list(filter(lambda x: x.invoice_flow_state_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def get_first(self) -> invoice_flow_state_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> invoice_flow_state_read_dtos:
        if len(self.dtos) > n:
            return invoice_flow_state_read_dtos(self.dtos[:n])
        else:
            return invoice_flow_state_read_dtos(self.dtos)
    def get_last(self) -> invoice_flow_state_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, invoice_flow_state_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def to_dict_by_invoice_flow_state_uid(self) -> dict[str, invoice_flow_state_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.invoice_flow_state_uid] = dto
        return d
    def to_dict_by_invoice_flow_state_name(self) -> dict[str, invoice_flow_state_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.invoice_flow_state_name] = dto
        return d
    def to_dict_by_invoice_flow_uid(self) -> dict[str, invoice_flow_state_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.invoice_flow_uid] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[invoice_flow_state_read_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[invoice_flow_state_read_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return init
    def check_any(self, check_method: Callable[[invoice_flow_state_read_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return init
    def map_to_string(self, map_method: Callable[[invoice_flow_state_read_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[invoice_flow_state_read_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[invoice_flow_state_read_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, invoice_flow_state_read_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, invoice_flow_state_read_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, invoice_flow_state_read_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[invoice_flow_state_read_dto], bool]) -> invoice_flow_state_read_dtos:
        return invoice_flow_state_read_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[invoice_flow_state_read_dto], str]) -> dict[str, invoice_flow_state_read_dtos]:
        grp_data: dict[str, invoice_flow_state_read_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = invoice_flow_state_read_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[invoice_flow_state_read_dto], str], agg_method: Callable[[invoice_flow_state_read_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, invoice_flow_state_read_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[invoice_flow_state_read_dto], bool]) -> invoice_flow_state_read_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[invoice_flow_state_read_dto], any], compare_method: Callable[[any, any], bool]) -> invoice_flow_state_read_dto | None:
        if len(self.dtos) == 0:
            return None
        else:
            max_value = value_method(self.dtos[0])
            max_elem = self.dtos[0]
            for dto in self.dtos:
                next_value = value_method(dto)
                if compare_method(next_value, max_value):
                    max_value = next_value
                    max_elem = dto
            return max_elem


@dataclass(frozen=False)
class invoice_instance_read_dtos(base_read_dtos):
    dtos: list[invoice_instance_read_dto]
    def __init__(self, dtos: list[invoice_instance_read_dto]):
        super().__init__(dtos)
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
        return list(map(lambda x: x.to_write(), self.dtos))
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
    def get_first_n(self, n: int) -> invoice_instance_read_dtos:
        if len(self.dtos) > n:
            return invoice_instance_read_dtos(self.dtos[:n])
        else:
            return invoice_instance_read_dtos(self.dtos)
    def get_last(self) -> invoice_instance_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
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
    def to_dict_by_invoice_instance_name(self) -> dict[str, invoice_instance_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.invoice_instance_name] = dto
        return d
    def to_dict_by_tenant_uid(self) -> dict[str, invoice_instance_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.tenant_uid] = dto
        return d
    def to_dict_by_account_uid(self) -> dict[str, invoice_instance_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.account_uid] = dto
        return d
    def to_dict_by_invoice_flow_uid(self) -> dict[str, invoice_instance_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.invoice_flow_uid] = dto
        return d
    def to_dict_by_invoice_status_uid(self) -> dict[str, invoice_instance_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.invoice_status_uid] = dto
        return d
    def to_dict_by_invoice_category_uid(self) -> dict[str, invoice_instance_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.invoice_category_uid] = dto
        return d
    def to_dict_by_invoice_type_uid(self) -> dict[str, invoice_instance_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.invoice_type_uid] = dto
        return d
    def to_dict_by_period_uid(self) -> dict[str, invoice_instance_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.period_uid] = dto
        return d
    def to_dict_by_currency_uid(self) -> dict[str, invoice_instance_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.currency_uid] = dto
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
    def to_dict_by_invoice_amount_net(self) -> dict[str, invoice_instance_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.invoice_amount_net] = dto
        return d
    def to_dict_by_invoice_amount_tax(self) -> dict[str, invoice_instance_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.invoice_amount_tax] = dto
        return d
    def to_dict_by_invoice_amount_gross(self) -> dict[str, invoice_instance_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.invoice_amount_gross] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[invoice_instance_read_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[invoice_instance_read_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return init
    def check_any(self, check_method: Callable[[invoice_instance_read_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return init
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
    def find(self, check_method: Callable[[invoice_instance_read_dto], bool]) -> invoice_instance_read_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[invoice_instance_read_dto], any], compare_method: Callable[[any, any], bool]) -> invoice_instance_read_dto | None:
        if len(self.dtos) == 0:
            return None
        else:
            max_value = value_method(self.dtos[0])
            max_elem = self.dtos[0]
            for dto in self.dtos:
                next_value = value_method(dto)
                if compare_method(next_value, max_value):
                    max_value = next_value
                    max_elem = dto
            return max_elem


@dataclass(frozen=False)
class invoice_status_read_dtos(base_read_dtos):
    dtos: list[invoice_status_read_dto]
    def __init__(self, dtos: list[invoice_status_read_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[invoice_status_read_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: invoice_status_read_dto):
        return cls(list([dto]))
    @classmethod
    def from_lists(cls, dtos1: list[invoice_status_read_dto], dtos2: list[invoice_status_read_dto]):
        return cls(dtos1 + dtos2)
    def get_active(self):
        return invoice_status_read_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return invoice_status_read_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_write_dtos(self) -> list[invoice_status_write_dto]:
        return list(map(lambda x: x.to_write(), self.dtos))
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write().to_write_dict(), self.dtos))
    def get_read_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> invoice_status_read_dto | None:
        found_dtos = list(filter(lambda x: x.invoice_status_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def get_first(self) -> invoice_status_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> invoice_status_read_dtos:
        if len(self.dtos) > n:
            return invoice_status_read_dtos(self.dtos[:n])
        else:
            return invoice_status_read_dtos(self.dtos)
    def get_last(self) -> invoice_status_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, invoice_status_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def to_dict_by_invoice_status_uid(self) -> dict[str, invoice_status_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.invoice_status_uid] = dto
        return d
    def to_dict_by_invoice_status_name(self) -> dict[str, invoice_status_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.invoice_status_name] = dto
        return d
    def to_dict_by_status_description(self) -> dict[str, invoice_status_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.status_description] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[invoice_status_read_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[invoice_status_read_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return init
    def check_any(self, check_method: Callable[[invoice_status_read_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return init
    def map_to_string(self, map_method: Callable[[invoice_status_read_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[invoice_status_read_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[invoice_status_read_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, invoice_status_read_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, invoice_status_read_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, invoice_status_read_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[invoice_status_read_dto], bool]) -> invoice_status_read_dtos:
        return invoice_status_read_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[invoice_status_read_dto], str]) -> dict[str, invoice_status_read_dtos]:
        grp_data: dict[str, invoice_status_read_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = invoice_status_read_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[invoice_status_read_dto], str], agg_method: Callable[[invoice_status_read_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, invoice_status_read_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[invoice_status_read_dto], bool]) -> invoice_status_read_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[invoice_status_read_dto], any], compare_method: Callable[[any, any], bool]) -> invoice_status_read_dto | None:
        if len(self.dtos) == 0:
            return None
        else:
            max_value = value_method(self.dtos[0])
            max_elem = self.dtos[0]
            for dto in self.dtos:
                next_value = value_method(dto)
                if compare_method(next_value, max_value):
                    max_value = next_value
                    max_elem = dto
            return max_elem


@dataclass(frozen=False)
class invoice_type_read_dtos(base_read_dtos):
    dtos: list[invoice_type_read_dto]
    def __init__(self, dtos: list[invoice_type_read_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[invoice_type_read_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: invoice_type_read_dto):
        return cls(list([dto]))
    @classmethod
    def from_lists(cls, dtos1: list[invoice_type_read_dto], dtos2: list[invoice_type_read_dto]):
        return cls(dtos1 + dtos2)
    def get_active(self):
        return invoice_type_read_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return invoice_type_read_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_write_dtos(self) -> list[invoice_type_write_dto]:
        return list(map(lambda x: x.to_write(), self.dtos))
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write().to_write_dict(), self.dtos))
    def get_read_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> invoice_type_read_dto | None:
        found_dtos = list(filter(lambda x: x.invoice_type_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def get_first(self) -> invoice_type_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> invoice_type_read_dtos:
        if len(self.dtos) > n:
            return invoice_type_read_dtos(self.dtos[:n])
        else:
            return invoice_type_read_dtos(self.dtos)
    def get_last(self) -> invoice_type_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, invoice_type_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def to_dict_by_invoice_type_uid(self) -> dict[str, invoice_type_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.invoice_type_uid] = dto
        return d
    def to_dict_by_invoice_type_name(self) -> dict[str, invoice_type_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.invoice_type_name] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[invoice_type_read_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[invoice_type_read_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return init
    def check_any(self, check_method: Callable[[invoice_type_read_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return init
    def map_to_string(self, map_method: Callable[[invoice_type_read_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[invoice_type_read_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[invoice_type_read_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, invoice_type_read_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, invoice_type_read_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, invoice_type_read_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[invoice_type_read_dto], bool]) -> invoice_type_read_dtos:
        return invoice_type_read_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[invoice_type_read_dto], str]) -> dict[str, invoice_type_read_dtos]:
        grp_data: dict[str, invoice_type_read_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = invoice_type_read_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[invoice_type_read_dto], str], agg_method: Callable[[invoice_type_read_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, invoice_type_read_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[invoice_type_read_dto], bool]) -> invoice_type_read_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[invoice_type_read_dto], any], compare_method: Callable[[any, any], bool]) -> invoice_type_read_dto | None:
        if len(self.dtos) == 0:
            return None
        else:
            max_value = value_method(self.dtos[0])
            max_elem = self.dtos[0]
            for dto in self.dtos:
                next_value = value_method(dto)
                if compare_method(next_value, max_value):
                    max_value = next_value
                    max_elem = dto
            return max_elem


@dataclass(frozen=False)
class monitor_read_dtos(base_read_dtos):
    dtos: list[monitor_read_dto]
    def __init__(self, dtos: list[monitor_read_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[monitor_read_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: monitor_read_dto):
        return cls(list([dto]))
    @classmethod
    def from_lists(cls, dtos1: list[monitor_read_dto], dtos2: list[monitor_read_dto]):
        return cls(dtos1 + dtos2)
    def get_active(self):
        return monitor_read_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return monitor_read_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_write_dtos(self) -> list[monitor_write_dto]:
        return list(map(lambda x: x.to_write(), self.dtos))
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write().to_write_dict(), self.dtos))
    def get_read_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> monitor_read_dto | None:
        found_dtos = list(filter(lambda x: x.monitor_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def get_first(self) -> monitor_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> monitor_read_dtos:
        if len(self.dtos) > n:
            return monitor_read_dtos(self.dtos[:n])
        else:
            return monitor_read_dtos(self.dtos)
    def get_last(self) -> monitor_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, monitor_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def to_dict_by_monitor_uid(self) -> dict[str, monitor_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.monitor_uid] = dto
        return d
    def to_dict_by_monitor_name(self) -> dict[str, monitor_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.monitor_name] = dto
        return d
    def to_dict_by_tenant_uid(self) -> dict[str, monitor_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.tenant_uid] = dto
        return d
    def to_dict_by_account_uid(self) -> dict[str, monitor_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.account_uid] = dto
        return d
    def to_dict_by_monitor_type_uid(self) -> dict[str, monitor_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.monitor_type_uid] = dto
        return d
    def to_dict_by_schedule_expression(self) -> dict[str, monitor_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.schedule_expression] = dto
        return d
    def to_dict_by_monitor_protocol(self) -> dict[str, monitor_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.monitor_protocol] = dto
        return d
    def to_dict_by_monitor_url(self) -> dict[str, monitor_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.monitor_url] = dto
        return d
    def to_dict_by_monitor_user(self) -> dict[str, monitor_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.monitor_user] = dto
        return d
    def to_dict_by_monitor_priority(self) -> dict[str, monitor_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.monitor_priority] = dto
        return d
    def to_dict_by_is_on_hold(self) -> dict[str, monitor_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.is_on_hold] = dto
        return d
    def to_dict_by_last_status_name(self) -> dict[str, monitor_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.last_status_name] = dto
        return d
    def to_dict_by_last_run_time(self) -> dict[str, monitor_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.last_run_time] = dto
        return d
    def to_dict_by_last_exception_message(self) -> dict[str, monitor_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.last_exception_message] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[monitor_read_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[monitor_read_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return init
    def check_any(self, check_method: Callable[[monitor_read_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return init
    def map_to_string(self, map_method: Callable[[monitor_read_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[monitor_read_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[monitor_read_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, monitor_read_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, monitor_read_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, monitor_read_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[monitor_read_dto], bool]) -> monitor_read_dtos:
        return monitor_read_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[monitor_read_dto], str]) -> dict[str, monitor_read_dtos]:
        grp_data: dict[str, monitor_read_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = monitor_read_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[monitor_read_dto], str], agg_method: Callable[[monitor_read_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, monitor_read_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[monitor_read_dto], bool]) -> monitor_read_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[monitor_read_dto], any], compare_method: Callable[[any, any], bool]) -> monitor_read_dto | None:
        if len(self.dtos) == 0:
            return None
        else:
            max_value = value_method(self.dtos[0])
            max_elem = self.dtos[0]
            for dto in self.dtos:
                next_value = value_method(dto)
                if compare_method(next_value, max_value):
                    max_value = next_value
                    max_elem = dto
            return max_elem


@dataclass(frozen=False)
class monitor_run_read_dtos(base_read_dtos):
    dtos: list[monitor_run_read_dto]
    def __init__(self, dtos: list[monitor_run_read_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[monitor_run_read_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: monitor_run_read_dto):
        return cls(list([dto]))
    @classmethod
    def from_lists(cls, dtos1: list[monitor_run_read_dto], dtos2: list[monitor_run_read_dto]):
        return cls(dtos1 + dtos2)
    def get_active(self):
        return monitor_run_read_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return monitor_run_read_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_write_dtos(self) -> list[monitor_run_write_dto]:
        return list(map(lambda x: x.to_write(), self.dtos))
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write().to_write_dict(), self.dtos))
    def get_read_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> monitor_run_read_dto | None:
        found_dtos = list(filter(lambda x: x.monitor_run_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def get_first(self) -> monitor_run_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> monitor_run_read_dtos:
        if len(self.dtos) > n:
            return monitor_run_read_dtos(self.dtos[:n])
        else:
            return monitor_run_read_dtos(self.dtos)
    def get_last(self) -> monitor_run_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, monitor_run_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def to_dict_by_monitor_run_uid(self) -> dict[str, monitor_run_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.monitor_run_uid] = dto
        return d
    def to_dict_by_monitor_run_name(self) -> dict[str, monitor_run_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.monitor_run_name] = dto
        return d
    def to_dict_by_tenant_uid(self) -> dict[str, monitor_run_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.tenant_uid] = dto
        return d
    def to_dict_by_account_uid(self) -> dict[str, monitor_run_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.account_uid] = dto
        return d
    def to_dict_by_monitor_uid(self) -> dict[str, monitor_run_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.monitor_uid] = dto
        return d
    def to_dict_by_status_name(self) -> dict[str, monitor_run_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.status_name] = dto
        return d
    def to_dict_by_run_time(self) -> dict[str, monitor_run_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.run_time] = dto
        return d
    def to_dict_by_exception_message(self) -> dict[str, monitor_run_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.exception_message] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[monitor_run_read_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[monitor_run_read_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return init
    def check_any(self, check_method: Callable[[monitor_run_read_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return init
    def map_to_string(self, map_method: Callable[[monitor_run_read_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[monitor_run_read_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[monitor_run_read_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, monitor_run_read_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, monitor_run_read_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, monitor_run_read_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[monitor_run_read_dto], bool]) -> monitor_run_read_dtos:
        return monitor_run_read_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[monitor_run_read_dto], str]) -> dict[str, monitor_run_read_dtos]:
        grp_data: dict[str, monitor_run_read_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = monitor_run_read_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[monitor_run_read_dto], str], agg_method: Callable[[monitor_run_read_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, monitor_run_read_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[monitor_run_read_dto], bool]) -> monitor_run_read_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[monitor_run_read_dto], any], compare_method: Callable[[any, any], bool]) -> monitor_run_read_dto | None:
        if len(self.dtos) == 0:
            return None
        else:
            max_value = value_method(self.dtos[0])
            max_elem = self.dtos[0]
            for dto in self.dtos:
                next_value = value_method(dto)
                if compare_method(next_value, max_value):
                    max_value = next_value
                    max_elem = dto
            return max_elem


@dataclass(frozen=False)
class monitor_type_read_dtos(base_read_dtos):
    dtos: list[monitor_type_read_dto]
    def __init__(self, dtos: list[monitor_type_read_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[monitor_type_read_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: monitor_type_read_dto):
        return cls(list([dto]))
    @classmethod
    def from_lists(cls, dtos1: list[monitor_type_read_dto], dtos2: list[monitor_type_read_dto]):
        return cls(dtos1 + dtos2)
    def get_active(self):
        return monitor_type_read_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return monitor_type_read_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_write_dtos(self) -> list[monitor_type_write_dto]:
        return list(map(lambda x: x.to_write(), self.dtos))
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write().to_write_dict(), self.dtos))
    def get_read_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> monitor_type_read_dto | None:
        found_dtos = list(filter(lambda x: x.monitor_type_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def get_first(self) -> monitor_type_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> monitor_type_read_dtos:
        if len(self.dtos) > n:
            return monitor_type_read_dtos(self.dtos[:n])
        else:
            return monitor_type_read_dtos(self.dtos)
    def get_last(self) -> monitor_type_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, monitor_type_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def to_dict_by_monitor_type_uid(self) -> dict[str, monitor_type_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.monitor_type_uid] = dto
        return d
    def to_dict_by_monitor_type_name(self) -> dict[str, monitor_type_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.monitor_type_name] = dto
        return d
    def to_dict_by_class_name(self) -> dict[str, monitor_type_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.class_name] = dto
        return d
    def to_dict_by_parameters_json(self) -> dict[str, monitor_type_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.parameters_json] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[monitor_type_read_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[monitor_type_read_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return init
    def check_any(self, check_method: Callable[[monitor_type_read_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return init
    def map_to_string(self, map_method: Callable[[monitor_type_read_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[monitor_type_read_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[monitor_type_read_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, monitor_type_read_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, monitor_type_read_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, monitor_type_read_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[monitor_type_read_dto], bool]) -> monitor_type_read_dtos:
        return monitor_type_read_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[monitor_type_read_dto], str]) -> dict[str, monitor_type_read_dtos]:
        grp_data: dict[str, monitor_type_read_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = monitor_type_read_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[monitor_type_read_dto], str], agg_method: Callable[[monitor_type_read_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, monitor_type_read_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[monitor_type_read_dto], bool]) -> monitor_type_read_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[monitor_type_read_dto], any], compare_method: Callable[[any, any], bool]) -> monitor_type_read_dto | None:
        if len(self.dtos) == 0:
            return None
        else:
            max_value = value_method(self.dtos[0])
            max_elem = self.dtos[0]
            for dto in self.dtos:
                next_value = value_method(dto)
                if compare_method(next_value, max_value):
                    max_value = next_value
                    max_elem = dto
            return max_elem


@dataclass(frozen=False)
class period_read_dtos(base_read_dtos):
    dtos: list[period_read_dto]
    def __init__(self, dtos: list[period_read_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[period_read_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: period_read_dto):
        return cls(list([dto]))
    @classmethod
    def from_lists(cls, dtos1: list[period_read_dto], dtos2: list[period_read_dto]):
        return cls(dtos1 + dtos2)
    def get_active(self):
        return period_read_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return period_read_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_write_dtos(self) -> list[period_write_dto]:
        return list(map(lambda x: x.to_write(), self.dtos))
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write().to_write_dict(), self.dtos))
    def get_read_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> period_read_dto | None:
        found_dtos = list(filter(lambda x: x.period_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def get_first(self) -> period_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> period_read_dtos:
        if len(self.dtos) > n:
            return period_read_dtos(self.dtos[:n])
        else:
            return period_read_dtos(self.dtos)
    def get_last(self) -> period_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, period_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def to_dict_by_period_uid(self) -> dict[str, period_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.period_uid] = dto
        return d
    def to_dict_by_period_name(self) -> dict[str, period_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.period_name] = dto
        return d
    def to_dict_by_period_number(self) -> dict[str, period_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.period_number] = dto
        return d
    def to_dict_by_period_type(self) -> dict[str, period_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.period_type] = dto
        return d
    def to_dict_by_period_start_time(self) -> dict[str, period_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.period_start_time] = dto
        return d
    def to_dict_by_period_end_time(self) -> dict[str, period_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.period_end_time] = dto
        return d
    def to_dict_by_period_year(self) -> dict[str, period_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.period_year] = dto
        return d
    def to_dict_by_period_quarter(self) -> dict[str, period_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.period_quarter] = dto
        return d
    def to_dict_by_period_month(self) -> dict[str, period_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.period_month] = dto
        return d
    def to_dict_by_period_week(self) -> dict[str, period_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.period_week] = dto
        return d
    def to_dict_by_period_day(self) -> dict[str, period_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.period_day] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[period_read_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[period_read_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return init
    def check_any(self, check_method: Callable[[period_read_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return init
    def map_to_string(self, map_method: Callable[[period_read_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[period_read_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[period_read_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, period_read_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, period_read_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, period_read_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[period_read_dto], bool]) -> period_read_dtos:
        return period_read_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[period_read_dto], str]) -> dict[str, period_read_dtos]:
        grp_data: dict[str, period_read_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = period_read_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[period_read_dto], str], agg_method: Callable[[period_read_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, period_read_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[period_read_dto], bool]) -> period_read_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[period_read_dto], any], compare_method: Callable[[any, any], bool]) -> period_read_dto | None:
        if len(self.dtos) == 0:
            return None
        else:
            max_value = value_method(self.dtos[0])
            max_elem = self.dtos[0]
            for dto in self.dtos:
                next_value = value_method(dto)
                if compare_method(next_value, max_value):
                    max_value = next_value
                    max_elem = dto
            return max_elem


@dataclass(frozen=False)
class process_read_dtos(base_read_dtos):
    dtos: list[process_read_dto]
    def __init__(self, dtos: list[process_read_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[process_read_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: process_read_dto):
        return cls(list([dto]))
    @classmethod
    def from_lists(cls, dtos1: list[process_read_dto], dtos2: list[process_read_dto]):
        return cls(dtos1 + dtos2)
    def get_active(self):
        return process_read_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return process_read_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_write_dtos(self) -> list[process_write_dto]:
        return list(map(lambda x: x.to_write(), self.dtos))
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write().to_write_dict(), self.dtos))
    def get_read_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> process_read_dto | None:
        found_dtos = list(filter(lambda x: x.process_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def get_first(self) -> process_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> process_read_dtos:
        if len(self.dtos) > n:
            return process_read_dtos(self.dtos[:n])
        else:
            return process_read_dtos(self.dtos)
    def get_last(self) -> process_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, process_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def to_dict_by_process_uid(self) -> dict[str, process_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.process_uid] = dto
        return d
    def to_dict_by_process_name(self) -> dict[str, process_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.process_name] = dto
        return d
    def to_dict_by_tenant_uid(self) -> dict[str, process_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.tenant_uid] = dto
        return d
    def to_dict_by_account_uid(self) -> dict[str, process_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.account_uid] = dto
        return d
    def to_dict_by_process_type_uid(self) -> dict[str, process_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.process_type_uid] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[process_read_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[process_read_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return init
    def check_any(self, check_method: Callable[[process_read_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return init
    def map_to_string(self, map_method: Callable[[process_read_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[process_read_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[process_read_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, process_read_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, process_read_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, process_read_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[process_read_dto], bool]) -> process_read_dtos:
        return process_read_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[process_read_dto], str]) -> dict[str, process_read_dtos]:
        grp_data: dict[str, process_read_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = process_read_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[process_read_dto], str], agg_method: Callable[[process_read_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, process_read_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[process_read_dto], bool]) -> process_read_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[process_read_dto], any], compare_method: Callable[[any, any], bool]) -> process_read_dto | None:
        if len(self.dtos) == 0:
            return None
        else:
            max_value = value_method(self.dtos[0])
            max_elem = self.dtos[0]
            for dto in self.dtos:
                next_value = value_method(dto)
                if compare_method(next_value, max_value):
                    max_value = next_value
                    max_elem = dto
            return max_elem


@dataclass(frozen=False)
class process_run_read_dtos(base_read_dtos):
    dtos: list[process_run_read_dto]
    def __init__(self, dtos: list[process_run_read_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[process_run_read_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: process_run_read_dto):
        return cls(list([dto]))
    @classmethod
    def from_lists(cls, dtos1: list[process_run_read_dto], dtos2: list[process_run_read_dto]):
        return cls(dtos1 + dtos2)
    def get_active(self):
        return process_run_read_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return process_run_read_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_write_dtos(self) -> list[process_run_write_dto]:
        return list(map(lambda x: x.to_write(), self.dtos))
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write().to_write_dict(), self.dtos))
    def get_read_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> process_run_read_dto | None:
        found_dtos = list(filter(lambda x: x.process_run_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def get_first(self) -> process_run_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> process_run_read_dtos:
        if len(self.dtos) > n:
            return process_run_read_dtos(self.dtos[:n])
        else:
            return process_run_read_dtos(self.dtos)
    def get_last(self) -> process_run_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, process_run_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def to_dict_by_process_run_uid(self) -> dict[str, process_run_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.process_run_uid] = dto
        return d
    def to_dict_by_process_run_name(self) -> dict[str, process_run_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.process_run_name] = dto
        return d
    def to_dict_by_tenant_uid(self) -> dict[str, process_run_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.tenant_uid] = dto
        return d
    def to_dict_by_account_uid(self) -> dict[str, process_run_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.account_uid] = dto
        return d
    def to_dict_by_process_uid(self) -> dict[str, process_run_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.process_uid] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[process_run_read_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[process_run_read_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return init
    def check_any(self, check_method: Callable[[process_run_read_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return init
    def map_to_string(self, map_method: Callable[[process_run_read_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[process_run_read_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[process_run_read_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, process_run_read_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, process_run_read_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, process_run_read_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[process_run_read_dto], bool]) -> process_run_read_dtos:
        return process_run_read_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[process_run_read_dto], str]) -> dict[str, process_run_read_dtos]:
        grp_data: dict[str, process_run_read_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = process_run_read_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[process_run_read_dto], str], agg_method: Callable[[process_run_read_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, process_run_read_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[process_run_read_dto], bool]) -> process_run_read_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[process_run_read_dto], any], compare_method: Callable[[any, any], bool]) -> process_run_read_dto | None:
        if len(self.dtos) == 0:
            return None
        else:
            max_value = value_method(self.dtos[0])
            max_elem = self.dtos[0]
            for dto in self.dtos:
                next_value = value_method(dto)
                if compare_method(next_value, max_value):
                    max_value = next_value
                    max_elem = dto
            return max_elem


@dataclass(frozen=False)
class process_type_read_dtos(base_read_dtos):
    dtos: list[process_type_read_dto]
    def __init__(self, dtos: list[process_type_read_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[process_type_read_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: process_type_read_dto):
        return cls(list([dto]))
    @classmethod
    def from_lists(cls, dtos1: list[process_type_read_dto], dtos2: list[process_type_read_dto]):
        return cls(dtos1 + dtos2)
    def get_active(self):
        return process_type_read_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return process_type_read_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_write_dtos(self) -> list[process_type_write_dto]:
        return list(map(lambda x: x.to_write(), self.dtos))
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write().to_write_dict(), self.dtos))
    def get_read_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> process_type_read_dto | None:
        found_dtos = list(filter(lambda x: x.process_type_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def get_first(self) -> process_type_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> process_type_read_dtos:
        if len(self.dtos) > n:
            return process_type_read_dtos(self.dtos[:n])
        else:
            return process_type_read_dtos(self.dtos)
    def get_last(self) -> process_type_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, process_type_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def to_dict_by_process_type_uid(self) -> dict[str, process_type_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.process_type_uid] = dto
        return d
    def to_dict_by_process_type_name(self) -> dict[str, process_type_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.process_type_name] = dto
        return d
    def to_dict_by_class_name(self) -> dict[str, process_type_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.class_name] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[process_type_read_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[process_type_read_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return init
    def check_any(self, check_method: Callable[[process_type_read_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return init
    def map_to_string(self, map_method: Callable[[process_type_read_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[process_type_read_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[process_type_read_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, process_type_read_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, process_type_read_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, process_type_read_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[process_type_read_dto], bool]) -> process_type_read_dtos:
        return process_type_read_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[process_type_read_dto], str]) -> dict[str, process_type_read_dtos]:
        grp_data: dict[str, process_type_read_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = process_type_read_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[process_type_read_dto], str], agg_method: Callable[[process_type_read_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, process_type_read_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[process_type_read_dto], bool]) -> process_type_read_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[process_type_read_dto], any], compare_method: Callable[[any, any], bool]) -> process_type_read_dto | None:
        if len(self.dtos) == 0:
            return None
        else:
            max_value = value_method(self.dtos[0])
            max_elem = self.dtos[0]
            for dto in self.dtos:
                next_value = value_method(dto)
                if compare_method(next_value, max_value):
                    max_value = next_value
                    max_elem = dto
            return max_elem


@dataclass(frozen=False)
class project_account_read_dtos(base_read_dtos):
    dtos: list[project_account_read_dto]
    def __init__(self, dtos: list[project_account_read_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[project_account_read_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: project_account_read_dto):
        return cls(list([dto]))
    @classmethod
    def from_lists(cls, dtos1: list[project_account_read_dto], dtos2: list[project_account_read_dto]):
        return cls(dtos1 + dtos2)
    def get_active(self):
        return project_account_read_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return project_account_read_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_write_dtos(self) -> list[project_account_write_dto]:
        return list(map(lambda x: x.to_write(), self.dtos))
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write().to_write_dict(), self.dtos))
    def get_read_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> project_account_read_dto | None:
        found_dtos = list(filter(lambda x: x.project_account_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def get_first(self) -> project_account_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> project_account_read_dtos:
        if len(self.dtos) > n:
            return project_account_read_dtos(self.dtos[:n])
        else:
            return project_account_read_dtos(self.dtos)
    def get_last(self) -> project_account_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, project_account_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def to_dict_by_project_account_uid(self) -> dict[str, project_account_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.project_account_uid] = dto
        return d
    def to_dict_by_project_account_name(self) -> dict[str, project_account_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.project_account_name] = dto
        return d
    def to_dict_by_tenant_uid(self) -> dict[str, project_account_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.tenant_uid] = dto
        return d
    def to_dict_by_client_uid(self) -> dict[str, project_account_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.client_uid] = dto
        return d
    def to_dict_by_account_uid(self) -> dict[str, project_account_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.account_uid] = dto
        return d
    def to_dict_by_project_instance_uid(self) -> dict[str, project_account_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.project_instance_uid] = dto
        return d
    def to_dict_by_start_date(self) -> dict[str, project_account_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.start_date] = dto
        return d
    def to_dict_by_end_date(self) -> dict[str, project_account_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.end_date] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[project_account_read_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[project_account_read_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return init
    def check_any(self, check_method: Callable[[project_account_read_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return init
    def map_to_string(self, map_method: Callable[[project_account_read_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[project_account_read_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[project_account_read_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, project_account_read_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, project_account_read_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, project_account_read_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[project_account_read_dto], bool]) -> project_account_read_dtos:
        return project_account_read_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[project_account_read_dto], str]) -> dict[str, project_account_read_dtos]:
        grp_data: dict[str, project_account_read_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = project_account_read_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[project_account_read_dto], str], agg_method: Callable[[project_account_read_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, project_account_read_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[project_account_read_dto], bool]) -> project_account_read_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[project_account_read_dto], any], compare_method: Callable[[any, any], bool]) -> project_account_read_dto | None:
        if len(self.dtos) == 0:
            return None
        else:
            max_value = value_method(self.dtos[0])
            max_elem = self.dtos[0]
            for dto in self.dtos:
                next_value = value_method(dto)
                if compare_method(next_value, max_value):
                    max_value = next_value
                    max_elem = dto
            return max_elem


@dataclass(frozen=False)
class project_budget_read_dtos(base_read_dtos):
    dtos: list[project_budget_read_dto]
    def __init__(self, dtos: list[project_budget_read_dto]):
        super().__init__(dtos)
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
        return list(map(lambda x: x.to_write(), self.dtos))
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
    def get_first_n(self, n: int) -> project_budget_read_dtos:
        if len(self.dtos) > n:
            return project_budget_read_dtos(self.dtos[:n])
        else:
            return project_budget_read_dtos(self.dtos)
    def get_last(self) -> project_budget_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
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
    def to_dict_by_project_budget_name(self) -> dict[str, project_budget_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.project_budget_name] = dto
        return d
    def to_dict_by_tenant_uid(self) -> dict[str, project_budget_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.tenant_uid] = dto
        return d
    def to_dict_by_client_uid(self) -> dict[str, project_budget_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.client_uid] = dto
        return d
    def to_dict_by_project_instance_uid(self) -> dict[str, project_budget_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.project_instance_uid] = dto
        return d
    def to_dict_by_currency_uid(self) -> dict[str, project_budget_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.currency_uid] = dto
        return d
    def to_dict_by_budget_value(self) -> dict[str, project_budget_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.budget_value] = dto
        return d
    def to_dict_by_is_approved(self) -> dict[str, project_budget_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.is_approved] = dto
        return d
    def to_dict_by_is_current(self) -> dict[str, project_budget_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.is_current] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[project_budget_read_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[project_budget_read_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return init
    def check_any(self, check_method: Callable[[project_budget_read_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return init
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
    def find(self, check_method: Callable[[project_budget_read_dto], bool]) -> project_budget_read_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[project_budget_read_dto], any], compare_method: Callable[[any, any], bool]) -> project_budget_read_dto | None:
        if len(self.dtos) == 0:
            return None
        else:
            max_value = value_method(self.dtos[0])
            max_elem = self.dtos[0]
            for dto in self.dtos:
                next_value = value_method(dto)
                if compare_method(next_value, max_value):
                    max_value = next_value
                    max_elem = dto
            return max_elem


@dataclass(frozen=False)
class project_group_read_dtos(base_read_dtos):
    dtos: list[project_group_read_dto]
    def __init__(self, dtos: list[project_group_read_dto]):
        super().__init__(dtos)
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
        return list(map(lambda x: x.to_write(), self.dtos))
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
    def get_first_n(self, n: int) -> project_group_read_dtos:
        if len(self.dtos) > n:
            return project_group_read_dtos(self.dtos[:n])
        else:
            return project_group_read_dtos(self.dtos)
    def get_last(self) -> project_group_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
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
    def to_dict_by_tenant_uid(self) -> dict[str, project_group_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.tenant_uid] = dto
        return d
    def to_dict_by_project_group_description(self) -> dict[str, project_group_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.project_group_description] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[project_group_read_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[project_group_read_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return init
    def check_any(self, check_method: Callable[[project_group_read_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return init
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
    def find(self, check_method: Callable[[project_group_read_dto], bool]) -> project_group_read_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[project_group_read_dto], any], compare_method: Callable[[any, any], bool]) -> project_group_read_dto | None:
        if len(self.dtos) == 0:
            return None
        else:
            max_value = value_method(self.dtos[0])
            max_elem = self.dtos[0]
            for dto in self.dtos:
                next_value = value_method(dto)
                if compare_method(next_value, max_value):
                    max_value = next_value
                    max_elem = dto
            return max_elem


@dataclass(frozen=False)
class project_instance_read_dtos(base_read_dtos):
    dtos: list[project_instance_read_dto]
    def __init__(self, dtos: list[project_instance_read_dto]):
        super().__init__(dtos)
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
        return list(map(lambda x: x.to_write(), self.dtos))
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
    def get_first_n(self, n: int) -> project_instance_read_dtos:
        if len(self.dtos) > n:
            return project_instance_read_dtos(self.dtos[:n])
        else:
            return project_instance_read_dtos(self.dtos)
    def get_last(self) -> project_instance_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
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
    def to_dict_by_project_instance_name(self) -> dict[str, project_instance_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.project_instance_name] = dto
        return d
    def to_dict_by_tenant_uid(self) -> dict[str, project_instance_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.tenant_uid] = dto
        return d
    def to_dict_by_client_uid(self) -> dict[str, project_instance_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.client_uid] = dto
        return d
    def to_dict_by_project_type_uid(self) -> dict[str, project_instance_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.project_type_uid] = dto
        return d
    def to_dict_by_manager_account_uid(self) -> dict[str, project_instance_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.manager_account_uid] = dto
        return d
    def to_dict_by_project_group_uid(self) -> dict[str, project_instance_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.project_group_uid] = dto
        return d
    def to_dict_by_project_code(self) -> dict[str, project_instance_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.project_code] = dto
        return d
    def to_dict_by_project_description(self) -> dict[str, project_instance_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.project_description] = dto
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
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[project_instance_read_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[project_instance_read_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return init
    def check_any(self, check_method: Callable[[project_instance_read_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return init
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
    def find(self, check_method: Callable[[project_instance_read_dto], bool]) -> project_instance_read_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[project_instance_read_dto], any], compare_method: Callable[[any, any], bool]) -> project_instance_read_dto | None:
        if len(self.dtos) == 0:
            return None
        else:
            max_value = value_method(self.dtos[0])
            max_elem = self.dtos[0]
            for dto in self.dtos:
                next_value = value_method(dto)
                if compare_method(next_value, max_value):
                    max_value = next_value
                    max_elem = dto
            return max_elem


@dataclass(frozen=False)
class project_milestone_read_dtos(base_read_dtos):
    dtos: list[project_milestone_read_dto]
    def __init__(self, dtos: list[project_milestone_read_dto]):
        super().__init__(dtos)
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
        return list(map(lambda x: x.to_write(), self.dtos))
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
    def get_first_n(self, n: int) -> project_milestone_read_dtos:
        if len(self.dtos) > n:
            return project_milestone_read_dtos(self.dtos[:n])
        else:
            return project_milestone_read_dtos(self.dtos)
    def get_last(self) -> project_milestone_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
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
    def to_dict_by_project_milestone_name(self) -> dict[str, project_milestone_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.project_milestone_name] = dto
        return d
    def to_dict_by_tenant_uid(self) -> dict[str, project_milestone_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.tenant_uid] = dto
        return d
    def to_dict_by_client_uid(self) -> dict[str, project_milestone_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.client_uid] = dto
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
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[project_milestone_read_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[project_milestone_read_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return init
    def check_any(self, check_method: Callable[[project_milestone_read_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return init
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
    def find(self, check_method: Callable[[project_milestone_read_dto], bool]) -> project_milestone_read_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[project_milestone_read_dto], any], compare_method: Callable[[any, any], bool]) -> project_milestone_read_dto | None:
        if len(self.dtos) == 0:
            return None
        else:
            max_value = value_method(self.dtos[0])
            max_elem = self.dtos[0]
            for dto in self.dtos:
                next_value = value_method(dto)
                if compare_method(next_value, max_value):
                    max_value = next_value
                    max_elem = dto
            return max_elem


@dataclass(frozen=False)
class project_type_read_dtos(base_read_dtos):
    dtos: list[project_type_read_dto]
    def __init__(self, dtos: list[project_type_read_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[project_type_read_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: project_type_read_dto):
        return cls(list([dto]))
    @classmethod
    def from_lists(cls, dtos1: list[project_type_read_dto], dtos2: list[project_type_read_dto]):
        return cls(dtos1 + dtos2)
    def get_active(self):
        return project_type_read_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return project_type_read_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_write_dtos(self) -> list[project_type_write_dto]:
        return list(map(lambda x: x.to_write(), self.dtos))
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write().to_write_dict(), self.dtos))
    def get_read_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> project_type_read_dto | None:
        found_dtos = list(filter(lambda x: x.project_type_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def get_first(self) -> project_type_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> project_type_read_dtos:
        if len(self.dtos) > n:
            return project_type_read_dtos(self.dtos[:n])
        else:
            return project_type_read_dtos(self.dtos)
    def get_last(self) -> project_type_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, project_type_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def to_dict_by_project_type_uid(self) -> dict[str, project_type_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.project_type_uid] = dto
        return d
    def to_dict_by_project_type_name(self) -> dict[str, project_type_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.project_type_name] = dto
        return d
    def to_dict_by_project_type_description(self) -> dict[str, project_type_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.project_type_description] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[project_type_read_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[project_type_read_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return init
    def check_any(self, check_method: Callable[[project_type_read_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return init
    def map_to_string(self, map_method: Callable[[project_type_read_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[project_type_read_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[project_type_read_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, project_type_read_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, project_type_read_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, project_type_read_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[project_type_read_dto], bool]) -> project_type_read_dtos:
        return project_type_read_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[project_type_read_dto], str]) -> dict[str, project_type_read_dtos]:
        grp_data: dict[str, project_type_read_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = project_type_read_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[project_type_read_dto], str], agg_method: Callable[[project_type_read_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, project_type_read_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[project_type_read_dto], bool]) -> project_type_read_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[project_type_read_dto], any], compare_method: Callable[[any, any], bool]) -> project_type_read_dto | None:
        if len(self.dtos) == 0:
            return None
        else:
            max_value = value_method(self.dtos[0])
            max_elem = self.dtos[0]
            for dto in self.dtos:
                next_value = value_method(dto)
                if compare_method(next_value, max_value):
                    max_value = next_value
                    max_elem = dto
            return max_elem


@dataclass(frozen=False)
class report_read_dtos(base_read_dtos):
    dtos: list[report_read_dto]
    def __init__(self, dtos: list[report_read_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[report_read_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: report_read_dto):
        return cls(list([dto]))
    @classmethod
    def from_lists(cls, dtos1: list[report_read_dto], dtos2: list[report_read_dto]):
        return cls(dtos1 + dtos2)
    def get_active(self):
        return report_read_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return report_read_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_write_dtos(self) -> list[report_write_dto]:
        return list(map(lambda x: x.to_write(), self.dtos))
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write().to_write_dict(), self.dtos))
    def get_read_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> report_read_dto | None:
        found_dtos = list(filter(lambda x: x.report_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def get_first(self) -> report_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> report_read_dtos:
        if len(self.dtos) > n:
            return report_read_dtos(self.dtos[:n])
        else:
            return report_read_dtos(self.dtos)
    def get_last(self) -> report_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, report_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def to_dict_by_report_uid(self) -> dict[str, report_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.report_uid] = dto
        return d
    def to_dict_by_report_name(self) -> dict[str, report_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.report_name] = dto
        return d
    def to_dict_by_tenant_uid(self) -> dict[str, report_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.tenant_uid] = dto
        return d
    def to_dict_by_account_uid(self) -> dict[str, report_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.account_uid] = dto
        return d
    def to_dict_by_report_status_uid(self) -> dict[str, report_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.report_status_uid] = dto
        return d
    def to_dict_by_report_query(self) -> dict[str, report_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.report_query] = dto
        return d
    def to_dict_by_report_parameters(self) -> dict[str, report_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.report_parameters] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[report_read_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[report_read_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return init
    def check_any(self, check_method: Callable[[report_read_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return init
    def map_to_string(self, map_method: Callable[[report_read_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[report_read_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[report_read_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, report_read_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, report_read_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, report_read_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[report_read_dto], bool]) -> report_read_dtos:
        return report_read_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[report_read_dto], str]) -> dict[str, report_read_dtos]:
        grp_data: dict[str, report_read_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = report_read_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[report_read_dto], str], agg_method: Callable[[report_read_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, report_read_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[report_read_dto], bool]) -> report_read_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[report_read_dto], any], compare_method: Callable[[any, any], bool]) -> report_read_dto | None:
        if len(self.dtos) == 0:
            return None
        else:
            max_value = value_method(self.dtos[0])
            max_elem = self.dtos[0]
            for dto in self.dtos:
                next_value = value_method(dto)
                if compare_method(next_value, max_value):
                    max_value = next_value
                    max_elem = dto
            return max_elem


@dataclass(frozen=False)
class report_content_type_read_dtos(base_read_dtos):
    dtos: list[report_content_type_read_dto]
    def __init__(self, dtos: list[report_content_type_read_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[report_content_type_read_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: report_content_type_read_dto):
        return cls(list([dto]))
    @classmethod
    def from_lists(cls, dtos1: list[report_content_type_read_dto], dtos2: list[report_content_type_read_dto]):
        return cls(dtos1 + dtos2)
    def get_active(self):
        return report_content_type_read_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return report_content_type_read_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_write_dtos(self) -> list[report_content_type_write_dto]:
        return list(map(lambda x: x.to_write(), self.dtos))
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write().to_write_dict(), self.dtos))
    def get_read_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> report_content_type_read_dto | None:
        found_dtos = list(filter(lambda x: x.report_content_type_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def get_first(self) -> report_content_type_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> report_content_type_read_dtos:
        if len(self.dtos) > n:
            return report_content_type_read_dtos(self.dtos[:n])
        else:
            return report_content_type_read_dtos(self.dtos)
    def get_last(self) -> report_content_type_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, report_content_type_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def to_dict_by_report_content_type_uid(self) -> dict[str, report_content_type_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.report_content_type_uid] = dto
        return d
    def to_dict_by_report_content_type_name(self) -> dict[str, report_content_type_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.report_content_type_name] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[report_content_type_read_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[report_content_type_read_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return init
    def check_any(self, check_method: Callable[[report_content_type_read_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return init
    def map_to_string(self, map_method: Callable[[report_content_type_read_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[report_content_type_read_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[report_content_type_read_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, report_content_type_read_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, report_content_type_read_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, report_content_type_read_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[report_content_type_read_dto], bool]) -> report_content_type_read_dtos:
        return report_content_type_read_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[report_content_type_read_dto], str]) -> dict[str, report_content_type_read_dtos]:
        grp_data: dict[str, report_content_type_read_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = report_content_type_read_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[report_content_type_read_dto], str], agg_method: Callable[[report_content_type_read_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, report_content_type_read_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[report_content_type_read_dto], bool]) -> report_content_type_read_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[report_content_type_read_dto], any], compare_method: Callable[[any, any], bool]) -> report_content_type_read_dto | None:
        if len(self.dtos) == 0:
            return None
        else:
            max_value = value_method(self.dtos[0])
            max_elem = self.dtos[0]
            for dto in self.dtos:
                next_value = value_method(dto)
                if compare_method(next_value, max_value):
                    max_value = next_value
                    max_elem = dto
            return max_elem


@dataclass(frozen=False)
class report_format_read_dtos(base_read_dtos):
    dtos: list[report_format_read_dto]
    def __init__(self, dtos: list[report_format_read_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[report_format_read_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: report_format_read_dto):
        return cls(list([dto]))
    @classmethod
    def from_lists(cls, dtos1: list[report_format_read_dto], dtos2: list[report_format_read_dto]):
        return cls(dtos1 + dtos2)
    def get_active(self):
        return report_format_read_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return report_format_read_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_write_dtos(self) -> list[report_format_write_dto]:
        return list(map(lambda x: x.to_write(), self.dtos))
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write().to_write_dict(), self.dtos))
    def get_read_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> report_format_read_dto | None:
        found_dtos = list(filter(lambda x: x.report_format_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def get_first(self) -> report_format_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> report_format_read_dtos:
        if len(self.dtos) > n:
            return report_format_read_dtos(self.dtos[:n])
        else:
            return report_format_read_dtos(self.dtos)
    def get_last(self) -> report_format_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, report_format_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def to_dict_by_report_format_uid(self) -> dict[str, report_format_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.report_format_uid] = dto
        return d
    def to_dict_by_report_format_name(self) -> dict[str, report_format_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.report_format_name] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[report_format_read_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[report_format_read_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return init
    def check_any(self, check_method: Callable[[report_format_read_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return init
    def map_to_string(self, map_method: Callable[[report_format_read_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[report_format_read_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[report_format_read_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, report_format_read_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, report_format_read_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, report_format_read_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[report_format_read_dto], bool]) -> report_format_read_dtos:
        return report_format_read_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[report_format_read_dto], str]) -> dict[str, report_format_read_dtos]:
        grp_data: dict[str, report_format_read_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = report_format_read_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[report_format_read_dto], str], agg_method: Callable[[report_format_read_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, report_format_read_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[report_format_read_dto], bool]) -> report_format_read_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[report_format_read_dto], any], compare_method: Callable[[any, any], bool]) -> report_format_read_dto | None:
        if len(self.dtos) == 0:
            return None
        else:
            max_value = value_method(self.dtos[0])
            max_elem = self.dtos[0]
            for dto in self.dtos:
                next_value = value_method(dto)
                if compare_method(next_value, max_value):
                    max_value = next_value
                    max_elem = dto
            return max_elem


@dataclass(frozen=False)
class report_run_read_dtos(base_read_dtos):
    dtos: list[report_run_read_dto]
    def __init__(self, dtos: list[report_run_read_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[report_run_read_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: report_run_read_dto):
        return cls(list([dto]))
    @classmethod
    def from_lists(cls, dtos1: list[report_run_read_dto], dtos2: list[report_run_read_dto]):
        return cls(dtos1 + dtos2)
    def get_active(self):
        return report_run_read_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return report_run_read_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_write_dtos(self) -> list[report_run_write_dto]:
        return list(map(lambda x: x.to_write(), self.dtos))
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write().to_write_dict(), self.dtos))
    def get_read_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> report_run_read_dto | None:
        found_dtos = list(filter(lambda x: x.report_run_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def get_first(self) -> report_run_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> report_run_read_dtos:
        if len(self.dtos) > n:
            return report_run_read_dtos(self.dtos[:n])
        else:
            return report_run_read_dtos(self.dtos)
    def get_last(self) -> report_run_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, report_run_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def to_dict_by_report_run_uid(self) -> dict[str, report_run_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.report_run_uid] = dto
        return d
    def to_dict_by_report_run_name(self) -> dict[str, report_run_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.report_run_name] = dto
        return d
    def to_dict_by_tenant_uid(self) -> dict[str, report_run_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.tenant_uid] = dto
        return d
    def to_dict_by_account_uid(self) -> dict[str, report_run_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.account_uid] = dto
        return d
    def to_dict_by_report_uid(self) -> dict[str, report_run_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.report_uid] = dto
        return d
    def to_dict_by_report_format_uid(self) -> dict[str, report_run_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.report_format_uid] = dto
        return d
    def to_dict_by_report_status_uid(self) -> dict[str, report_run_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.report_status_uid] = dto
        return d
    def to_dict_by_report_content_type_uid(self) -> dict[str, report_run_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.report_content_type_uid] = dto
        return d
    def to_dict_by_input_parameters_json(self) -> dict[str, report_run_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.input_parameters_json] = dto
        return d
    def to_dict_by_run_time_ms(self) -> dict[str, report_run_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.run_time_ms] = dto
        return d
    def to_dict_by_returned_rows(self) -> dict[str, report_run_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.returned_rows] = dto
        return d
    def to_dict_by_content_size(self) -> dict[str, report_run_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.content_size] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[report_run_read_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[report_run_read_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return init
    def check_any(self, check_method: Callable[[report_run_read_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return init
    def map_to_string(self, map_method: Callable[[report_run_read_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[report_run_read_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[report_run_read_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, report_run_read_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, report_run_read_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, report_run_read_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[report_run_read_dto], bool]) -> report_run_read_dtos:
        return report_run_read_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[report_run_read_dto], str]) -> dict[str, report_run_read_dtos]:
        grp_data: dict[str, report_run_read_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = report_run_read_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[report_run_read_dto], str], agg_method: Callable[[report_run_read_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, report_run_read_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[report_run_read_dto], bool]) -> report_run_read_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[report_run_read_dto], any], compare_method: Callable[[any, any], bool]) -> report_run_read_dto | None:
        if len(self.dtos) == 0:
            return None
        else:
            max_value = value_method(self.dtos[0])
            max_elem = self.dtos[0]
            for dto in self.dtos:
                next_value = value_method(dto)
                if compare_method(next_value, max_value):
                    max_value = next_value
                    max_elem = dto
            return max_elem


@dataclass(frozen=False)
class report_status_read_dtos(base_read_dtos):
    dtos: list[report_status_read_dto]
    def __init__(self, dtos: list[report_status_read_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[report_status_read_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: report_status_read_dto):
        return cls(list([dto]))
    @classmethod
    def from_lists(cls, dtos1: list[report_status_read_dto], dtos2: list[report_status_read_dto]):
        return cls(dtos1 + dtos2)
    def get_active(self):
        return report_status_read_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return report_status_read_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_write_dtos(self) -> list[report_status_write_dto]:
        return list(map(lambda x: x.to_write(), self.dtos))
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write().to_write_dict(), self.dtos))
    def get_read_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> report_status_read_dto | None:
        found_dtos = list(filter(lambda x: x.report_status_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def get_first(self) -> report_status_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> report_status_read_dtos:
        if len(self.dtos) > n:
            return report_status_read_dtos(self.dtos[:n])
        else:
            return report_status_read_dtos(self.dtos)
    def get_last(self) -> report_status_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, report_status_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def to_dict_by_report_status_uid(self) -> dict[str, report_status_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.report_status_uid] = dto
        return d
    def to_dict_by_report_status_name(self) -> dict[str, report_status_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.report_status_name] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[report_status_read_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[report_status_read_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return init
    def check_any(self, check_method: Callable[[report_status_read_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return init
    def map_to_string(self, map_method: Callable[[report_status_read_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[report_status_read_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[report_status_read_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, report_status_read_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, report_status_read_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, report_status_read_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[report_status_read_dto], bool]) -> report_status_read_dtos:
        return report_status_read_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[report_status_read_dto], str]) -> dict[str, report_status_read_dtos]:
        grp_data: dict[str, report_status_read_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = report_status_read_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[report_status_read_dto], str], agg_method: Callable[[report_status_read_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, report_status_read_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[report_status_read_dto], bool]) -> report_status_read_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[report_status_read_dto], any], compare_method: Callable[[any, any], bool]) -> report_status_read_dto | None:
        if len(self.dtos) == 0:
            return None
        else:
            max_value = value_method(self.dtos[0])
            max_elem = self.dtos[0]
            for dto in self.dtos:
                next_value = value_method(dto)
                if compare_method(next_value, max_value):
                    max_value = next_value
                    max_elem = dto
            return max_elem


@dataclass(frozen=False)
class report_type_read_dtos(base_read_dtos):
    dtos: list[report_type_read_dto]
    def __init__(self, dtos: list[report_type_read_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[report_type_read_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: report_type_read_dto):
        return cls(list([dto]))
    @classmethod
    def from_lists(cls, dtos1: list[report_type_read_dto], dtos2: list[report_type_read_dto]):
        return cls(dtos1 + dtos2)
    def get_active(self):
        return report_type_read_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return report_type_read_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_write_dtos(self) -> list[report_type_write_dto]:
        return list(map(lambda x: x.to_write(), self.dtos))
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write().to_write_dict(), self.dtos))
    def get_read_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> report_type_read_dto | None:
        found_dtos = list(filter(lambda x: x.report_type_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def get_first(self) -> report_type_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> report_type_read_dtos:
        if len(self.dtos) > n:
            return report_type_read_dtos(self.dtos[:n])
        else:
            return report_type_read_dtos(self.dtos)
    def get_last(self) -> report_type_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, report_type_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def to_dict_by_report_type_uid(self) -> dict[str, report_type_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.report_type_uid] = dto
        return d
    def to_dict_by_report_type_name(self) -> dict[str, report_type_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.report_type_name] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[report_type_read_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[report_type_read_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return init
    def check_any(self, check_method: Callable[[report_type_read_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return init
    def map_to_string(self, map_method: Callable[[report_type_read_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[report_type_read_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[report_type_read_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, report_type_read_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, report_type_read_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, report_type_read_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[report_type_read_dto], bool]) -> report_type_read_dtos:
        return report_type_read_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[report_type_read_dto], str]) -> dict[str, report_type_read_dtos]:
        grp_data: dict[str, report_type_read_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = report_type_read_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[report_type_read_dto], str], agg_method: Callable[[report_type_read_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, report_type_read_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[report_type_read_dto], bool]) -> report_type_read_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[report_type_read_dto], any], compare_method: Callable[[any, any], bool]) -> report_type_read_dto | None:
        if len(self.dtos) == 0:
            return None
        else:
            max_value = value_method(self.dtos[0])
            max_elem = self.dtos[0]
            for dto in self.dtos:
                next_value = value_method(dto)
                if compare_method(next_value, max_value):
                    max_value = next_value
                    max_elem = dto
            return max_elem


@dataclass(frozen=False)
class storage_read_dtos(base_read_dtos):
    dtos: list[storage_read_dto]
    def __init__(self, dtos: list[storage_read_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[storage_read_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: storage_read_dto):
        return cls(list([dto]))
    @classmethod
    def from_lists(cls, dtos1: list[storage_read_dto], dtos2: list[storage_read_dto]):
        return cls(dtos1 + dtos2)
    def get_active(self):
        return storage_read_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return storage_read_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_write_dtos(self) -> list[storage_write_dto]:
        return list(map(lambda x: x.to_write(), self.dtos))
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write().to_write_dict(), self.dtos))
    def get_read_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> storage_read_dto | None:
        found_dtos = list(filter(lambda x: x.storage_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def get_first(self) -> storage_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> storage_read_dtos:
        if len(self.dtos) > n:
            return storage_read_dtos(self.dtos[:n])
        else:
            return storage_read_dtos(self.dtos)
    def get_last(self) -> storage_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, storage_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def to_dict_by_storage_uid(self) -> dict[str, storage_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.storage_uid] = dto
        return d
    def to_dict_by_storage_name(self) -> dict[str, storage_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.storage_name] = dto
        return d
    def to_dict_by_storage_class(self) -> dict[str, storage_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.storage_class] = dto
        return d
    def to_dict_by_storage_parameters_json(self) -> dict[str, storage_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.storage_parameters_json] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[storage_read_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[storage_read_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return init
    def check_any(self, check_method: Callable[[storage_read_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return init
    def map_to_string(self, map_method: Callable[[storage_read_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[storage_read_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[storage_read_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, storage_read_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, storage_read_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, storage_read_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[storage_read_dto], bool]) -> storage_read_dtos:
        return storage_read_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[storage_read_dto], str]) -> dict[str, storage_read_dtos]:
        grp_data: dict[str, storage_read_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = storage_read_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[storage_read_dto], str], agg_method: Callable[[storage_read_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, storage_read_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[storage_read_dto], bool]) -> storage_read_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[storage_read_dto], any], compare_method: Callable[[any, any], bool]) -> storage_read_dto | None:
        if len(self.dtos) == 0:
            return None
        else:
            max_value = value_method(self.dtos[0])
            max_elem = self.dtos[0]
            for dto in self.dtos:
                next_value = value_method(dto)
                if compare_method(next_value, max_value):
                    max_value = next_value
                    max_elem = dto
            return max_elem


@dataclass(frozen=False)
class storage_connection_read_dtos(base_read_dtos):
    dtos: list[storage_connection_read_dto]
    def __init__(self, dtos: list[storage_connection_read_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[storage_connection_read_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: storage_connection_read_dto):
        return cls(list([dto]))
    @classmethod
    def from_lists(cls, dtos1: list[storage_connection_read_dto], dtos2: list[storage_connection_read_dto]):
        return cls(dtos1 + dtos2)
    def get_active(self):
        return storage_connection_read_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return storage_connection_read_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_write_dtos(self) -> list[storage_connection_write_dto]:
        return list(map(lambda x: x.to_write(), self.dtos))
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write().to_write_dict(), self.dtos))
    def get_read_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> storage_connection_read_dto | None:
        found_dtos = list(filter(lambda x: x.storage_connection_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def get_first(self) -> storage_connection_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> storage_connection_read_dtos:
        if len(self.dtos) > n:
            return storage_connection_read_dtos(self.dtos[:n])
        else:
            return storage_connection_read_dtos(self.dtos)
    def get_last(self) -> storage_connection_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, storage_connection_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def to_dict_by_storage_connection_uid(self) -> dict[str, storage_connection_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.storage_connection_uid] = dto
        return d
    def to_dict_by_storage_connection_name(self) -> dict[str, storage_connection_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.storage_connection_name] = dto
        return d
    def to_dict_by_storage_uid(self) -> dict[str, storage_connection_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.storage_uid] = dto
        return d
    def to_dict_by_connection_type(self) -> dict[str, storage_connection_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.connection_type] = dto
        return d
    def to_dict_by_storage_parameters_json(self) -> dict[str, storage_connection_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.storage_parameters_json] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[storage_connection_read_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[storage_connection_read_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return init
    def check_any(self, check_method: Callable[[storage_connection_read_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return init
    def map_to_string(self, map_method: Callable[[storage_connection_read_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[storage_connection_read_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[storage_connection_read_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, storage_connection_read_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, storage_connection_read_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, storage_connection_read_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[storage_connection_read_dto], bool]) -> storage_connection_read_dtos:
        return storage_connection_read_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[storage_connection_read_dto], str]) -> dict[str, storage_connection_read_dtos]:
        grp_data: dict[str, storage_connection_read_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = storage_connection_read_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[storage_connection_read_dto], str], agg_method: Callable[[storage_connection_read_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, storage_connection_read_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[storage_connection_read_dto], bool]) -> storage_connection_read_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[storage_connection_read_dto], any], compare_method: Callable[[any, any], bool]) -> storage_connection_read_dto | None:
        if len(self.dtos) == 0:
            return None
        else:
            max_value = value_method(self.dtos[0])
            max_elem = self.dtos[0]
            for dto in self.dtos:
                next_value = value_method(dto)
                if compare_method(next_value, max_value):
                    max_value = next_value
                    max_elem = dto
            return max_elem


@dataclass(frozen=False)
class storage_query_read_dtos(base_read_dtos):
    dtos: list[storage_query_read_dto]
    def __init__(self, dtos: list[storage_query_read_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[storage_query_read_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: storage_query_read_dto):
        return cls(list([dto]))
    @classmethod
    def from_lists(cls, dtos1: list[storage_query_read_dto], dtos2: list[storage_query_read_dto]):
        return cls(dtos1 + dtos2)
    def get_active(self):
        return storage_query_read_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return storage_query_read_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_write_dtos(self) -> list[storage_query_write_dto]:
        return list(map(lambda x: x.to_write(), self.dtos))
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write().to_write_dict(), self.dtos))
    def get_read_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> storage_query_read_dto | None:
        found_dtos = list(filter(lambda x: x.storage_query_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def get_first(self) -> storage_query_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> storage_query_read_dtos:
        if len(self.dtos) > n:
            return storage_query_read_dtos(self.dtos[:n])
        else:
            return storage_query_read_dtos(self.dtos)
    def get_last(self) -> storage_query_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, storage_query_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def to_dict_by_storage_connection_uid(self) -> dict[str, storage_query_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.storage_connection_uid] = dto
        return d
    def to_dict_by_storage_connection_name(self) -> dict[str, storage_query_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.storage_connection_name] = dto
        return d
    def to_dict_by_storage_uid(self) -> dict[str, storage_query_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.storage_uid] = dto
        return d
    def to_dict_by_storage_parameters_json(self) -> dict[str, storage_query_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.storage_parameters_json] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[storage_query_read_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[storage_query_read_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return init
    def check_any(self, check_method: Callable[[storage_query_read_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return init
    def map_to_string(self, map_method: Callable[[storage_query_read_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[storage_query_read_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[storage_query_read_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, storage_query_read_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, storage_query_read_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, storage_query_read_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[storage_query_read_dto], bool]) -> storage_query_read_dtos:
        return storage_query_read_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[storage_query_read_dto], str]) -> dict[str, storage_query_read_dtos]:
        grp_data: dict[str, storage_query_read_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = storage_query_read_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[storage_query_read_dto], str], agg_method: Callable[[storage_query_read_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, storage_query_read_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[storage_query_read_dto], bool]) -> storage_query_read_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[storage_query_read_dto], any], compare_method: Callable[[any, any], bool]) -> storage_query_read_dto | None:
        if len(self.dtos) == 0:
            return None
        else:
            max_value = value_method(self.dtos[0])
            max_elem = self.dtos[0]
            for dto in self.dtos:
                next_value = value_method(dto)
                if compare_method(next_value, max_value):
                    max_value = next_value
                    max_elem = dto
            return max_elem


@dataclass(frozen=False)
class storage_type_read_dtos(base_read_dtos):
    dtos: list[storage_type_read_dto]
    def __init__(self, dtos: list[storage_type_read_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[storage_type_read_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: storage_type_read_dto):
        return cls(list([dto]))
    @classmethod
    def from_lists(cls, dtos1: list[storage_type_read_dto], dtos2: list[storage_type_read_dto]):
        return cls(dtos1 + dtos2)
    def get_active(self):
        return storage_type_read_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return storage_type_read_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_write_dtos(self) -> list[storage_type_write_dto]:
        return list(map(lambda x: x.to_write(), self.dtos))
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write().to_write_dict(), self.dtos))
    def get_read_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> storage_type_read_dto | None:
        found_dtos = list(filter(lambda x: x.storage_type_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def get_first(self) -> storage_type_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> storage_type_read_dtos:
        if len(self.dtos) > n:
            return storage_type_read_dtos(self.dtos[:n])
        else:
            return storage_type_read_dtos(self.dtos)
    def get_last(self) -> storage_type_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, storage_type_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def to_dict_by_storage_type_uid(self) -> dict[str, storage_type_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.storage_type_uid] = dto
        return d
    def to_dict_by_storage_type_name(self) -> dict[str, storage_type_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.storage_type_name] = dto
        return d
    def to_dict_by_storage_class(self) -> dict[str, storage_type_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.storage_class] = dto
        return d
    def to_dict_by_storage_parameters_json(self) -> dict[str, storage_type_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.storage_parameters_json] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[storage_type_read_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[storage_type_read_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return init
    def check_any(self, check_method: Callable[[storage_type_read_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return init
    def map_to_string(self, map_method: Callable[[storage_type_read_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[storage_type_read_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[storage_type_read_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, storage_type_read_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, storage_type_read_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, storage_type_read_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[storage_type_read_dto], bool]) -> storage_type_read_dtos:
        return storage_type_read_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[storage_type_read_dto], str]) -> dict[str, storage_type_read_dtos]:
        grp_data: dict[str, storage_type_read_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = storage_type_read_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[storage_type_read_dto], str], agg_method: Callable[[storage_type_read_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, storage_type_read_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[storage_type_read_dto], bool]) -> storage_type_read_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[storage_type_read_dto], any], compare_method: Callable[[any, any], bool]) -> storage_type_read_dto | None:
        if len(self.dtos) == 0:
            return None
        else:
            max_value = value_method(self.dtos[0])
            max_elem = self.dtos[0]
            for dto in self.dtos:
                next_value = value_method(dto)
                if compare_method(next_value, max_value):
                    max_value = next_value
                    max_elem = dto
            return max_elem


@dataclass(frozen=False)
class synchronization_read_dtos(base_read_dtos):
    dtos: list[synchronization_read_dto]
    def __init__(self, dtos: list[synchronization_read_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[synchronization_read_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: synchronization_read_dto):
        return cls(list([dto]))
    @classmethod
    def from_lists(cls, dtos1: list[synchronization_read_dto], dtos2: list[synchronization_read_dto]):
        return cls(dtos1 + dtos2)
    def get_active(self):
        return synchronization_read_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return synchronization_read_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_write_dtos(self) -> list[synchronization_write_dto]:
        return list(map(lambda x: x.to_write(), self.dtos))
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write().to_write_dict(), self.dtos))
    def get_read_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> synchronization_read_dto | None:
        found_dtos = list(filter(lambda x: x.synchronization_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def get_first(self) -> synchronization_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> synchronization_read_dtos:
        if len(self.dtos) > n:
            return synchronization_read_dtos(self.dtos[:n])
        else:
            return synchronization_read_dtos(self.dtos)
    def get_last(self) -> synchronization_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, synchronization_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def to_dict_by_synchronization_uid(self) -> dict[str, synchronization_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.synchronization_uid] = dto
        return d
    def to_dict_by_synchronization_name(self) -> dict[str, synchronization_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.synchronization_name] = dto
        return d
    def to_dict_by_tenant_uid(self) -> dict[str, synchronization_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.tenant_uid] = dto
        return d
    def to_dict_by_synchronization_type_uid(self) -> dict[str, synchronization_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.synchronization_type_uid] = dto
        return d
    def to_dict_by_storage_uid(self) -> dict[str, synchronization_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.storage_uid] = dto
        return d
    def to_dict_by_sync_expression(self) -> dict[str, synchronization_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.sync_expression] = dto
        return d
    def to_dict_by_sync_query(self) -> dict[str, synchronization_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.sync_query] = dto
        return d
    def to_dict_by_sync_definition(self) -> dict[str, synchronization_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.sync_definition] = dto
        return d
    def to_dict_by_sync_priority(self) -> dict[str, synchronization_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.sync_priority] = dto
        return d
    def to_dict_by_last_run_date(self) -> dict[str, synchronization_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.last_run_date] = dto
        return d
    def to_dict_by_last_run_seconds(self) -> dict[str, synchronization_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.last_run_seconds] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[synchronization_read_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[synchronization_read_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return init
    def check_any(self, check_method: Callable[[synchronization_read_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return init
    def map_to_string(self, map_method: Callable[[synchronization_read_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[synchronization_read_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[synchronization_read_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, synchronization_read_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, synchronization_read_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, synchronization_read_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[synchronization_read_dto], bool]) -> synchronization_read_dtos:
        return synchronization_read_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[synchronization_read_dto], str]) -> dict[str, synchronization_read_dtos]:
        grp_data: dict[str, synchronization_read_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = synchronization_read_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[synchronization_read_dto], str], agg_method: Callable[[synchronization_read_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, synchronization_read_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[synchronization_read_dto], bool]) -> synchronization_read_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[synchronization_read_dto], any], compare_method: Callable[[any, any], bool]) -> synchronization_read_dto | None:
        if len(self.dtos) == 0:
            return None
        else:
            max_value = value_method(self.dtos[0])
            max_elem = self.dtos[0]
            for dto in self.dtos:
                next_value = value_method(dto)
                if compare_method(next_value, max_value):
                    max_value = next_value
                    max_elem = dto
            return max_elem


@dataclass(frozen=False)
class synchronization_run_read_dtos(base_read_dtos):
    dtos: list[synchronization_run_read_dto]
    def __init__(self, dtos: list[synchronization_run_read_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[synchronization_run_read_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: synchronization_run_read_dto):
        return cls(list([dto]))
    @classmethod
    def from_lists(cls, dtos1: list[synchronization_run_read_dto], dtos2: list[synchronization_run_read_dto]):
        return cls(dtos1 + dtos2)
    def get_active(self):
        return synchronization_run_read_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return synchronization_run_read_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_write_dtos(self) -> list[synchronization_run_write_dto]:
        return list(map(lambda x: x.to_write(), self.dtos))
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write().to_write_dict(), self.dtos))
    def get_read_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> synchronization_run_read_dto | None:
        found_dtos = list(filter(lambda x: x.synchronization_run_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def get_first(self) -> synchronization_run_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> synchronization_run_read_dtos:
        if len(self.dtos) > n:
            return synchronization_run_read_dtos(self.dtos[:n])
        else:
            return synchronization_run_read_dtos(self.dtos)
    def get_last(self) -> synchronization_run_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, synchronization_run_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def to_dict_by_synchronization_run_uid(self) -> dict[str, synchronization_run_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.synchronization_run_uid] = dto
        return d
    def to_dict_by_synchronization_run_name(self) -> dict[str, synchronization_run_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.synchronization_run_name] = dto
        return d
    def to_dict_by_synchronization_uid(self) -> dict[str, synchronization_run_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.synchronization_uid] = dto
        return d
    def to_dict_by_run_status(self) -> dict[str, synchronization_run_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.run_status] = dto
        return d
    def to_dict_by_run_time_seconds(self) -> dict[str, synchronization_run_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.run_time_seconds] = dto
        return d
    def to_dict_by_copied_items(self) -> dict[str, synchronization_run_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.copied_items] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[synchronization_run_read_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[synchronization_run_read_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return init
    def check_any(self, check_method: Callable[[synchronization_run_read_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return init
    def map_to_string(self, map_method: Callable[[synchronization_run_read_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[synchronization_run_read_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[synchronization_run_read_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, synchronization_run_read_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, synchronization_run_read_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, synchronization_run_read_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[synchronization_run_read_dto], bool]) -> synchronization_run_read_dtos:
        return synchronization_run_read_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[synchronization_run_read_dto], str]) -> dict[str, synchronization_run_read_dtos]:
        grp_data: dict[str, synchronization_run_read_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = synchronization_run_read_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[synchronization_run_read_dto], str], agg_method: Callable[[synchronization_run_read_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, synchronization_run_read_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[synchronization_run_read_dto], bool]) -> synchronization_run_read_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[synchronization_run_read_dto], any], compare_method: Callable[[any, any], bool]) -> synchronization_run_read_dto | None:
        if len(self.dtos) == 0:
            return None
        else:
            max_value = value_method(self.dtos[0])
            max_elem = self.dtos[0]
            for dto in self.dtos:
                next_value = value_method(dto)
                if compare_method(next_value, max_value):
                    max_value = next_value
                    max_elem = dto
            return max_elem


@dataclass(frozen=False)
class synchronization_type_read_dtos(base_read_dtos):
    dtos: list[synchronization_type_read_dto]
    def __init__(self, dtos: list[synchronization_type_read_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[synchronization_type_read_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: synchronization_type_read_dto):
        return cls(list([dto]))
    @classmethod
    def from_lists(cls, dtos1: list[synchronization_type_read_dto], dtos2: list[synchronization_type_read_dto]):
        return cls(dtos1 + dtos2)
    def get_active(self):
        return synchronization_type_read_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return synchronization_type_read_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_write_dtos(self) -> list[synchronization_type_write_dto]:
        return list(map(lambda x: x.to_write(), self.dtos))
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write().to_write_dict(), self.dtos))
    def get_read_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> synchronization_type_read_dto | None:
        found_dtos = list(filter(lambda x: x.synchronization_type_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def get_first(self) -> synchronization_type_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> synchronization_type_read_dtos:
        if len(self.dtos) > n:
            return synchronization_type_read_dtos(self.dtos[:n])
        else:
            return synchronization_type_read_dtos(self.dtos)
    def get_last(self) -> synchronization_type_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, synchronization_type_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def to_dict_by_synchronization_type_uid(self) -> dict[str, synchronization_type_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.synchronization_type_uid] = dto
        return d
    def to_dict_by_synchronization_type_name(self) -> dict[str, synchronization_type_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.synchronization_type_name] = dto
        return d
    def to_dict_by_sync_type(self) -> dict[str, synchronization_type_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.sync_type] = dto
        return d
    def to_dict_by_sync_class_came(self) -> dict[str, synchronization_type_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.sync_class_came] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[synchronization_type_read_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[synchronization_type_read_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return init
    def check_any(self, check_method: Callable[[synchronization_type_read_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return init
    def map_to_string(self, map_method: Callable[[synchronization_type_read_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[synchronization_type_read_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[synchronization_type_read_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, synchronization_type_read_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, synchronization_type_read_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, synchronization_type_read_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[synchronization_type_read_dto], bool]) -> synchronization_type_read_dtos:
        return synchronization_type_read_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[synchronization_type_read_dto], str]) -> dict[str, synchronization_type_read_dtos]:
        grp_data: dict[str, synchronization_type_read_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = synchronization_type_read_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[synchronization_type_read_dto], str], agg_method: Callable[[synchronization_type_read_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, synchronization_type_read_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[synchronization_type_read_dto], bool]) -> synchronization_type_read_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[synchronization_type_read_dto], any], compare_method: Callable[[any, any], bool]) -> synchronization_type_read_dto | None:
        if len(self.dtos) == 0:
            return None
        else:
            max_value = value_method(self.dtos[0])
            max_elem = self.dtos[0]
            for dto in self.dtos:
                next_value = value_method(dto)
                if compare_method(next_value, max_value):
                    max_value = next_value
                    max_elem = dto
            return max_elem


@dataclass(frozen=False)
class system_attribute_read_dtos(base_read_dtos):
    dtos: list[system_attribute_read_dto]
    def __init__(self, dtos: list[system_attribute_read_dto]):
        super().__init__(dtos)
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
        return list(map(lambda x: x.to_write(), self.dtos))
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
    def get_first_n(self, n: int) -> system_attribute_read_dtos:
        if len(self.dtos) > n:
            return system_attribute_read_dtos(self.dtos[:n])
        else:
            return system_attribute_read_dtos(self.dtos)
    def get_last(self) -> system_attribute_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
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
    def to_dict_by_system_attribute_name(self) -> dict[str, system_attribute_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.system_attribute_name] = dto
        return d
    def to_dict_by_system_object_uid(self) -> dict[str, system_attribute_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.system_object_uid] = dto
        return d
    def to_dict_by_column_name(self) -> dict[str, system_attribute_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.column_name] = dto
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
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[system_attribute_read_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[system_attribute_read_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return init
    def check_any(self, check_method: Callable[[system_attribute_read_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return init
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
    def find(self, check_method: Callable[[system_attribute_read_dto], bool]) -> system_attribute_read_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[system_attribute_read_dto], any], compare_method: Callable[[any, any], bool]) -> system_attribute_read_dto | None:
        if len(self.dtos) == 0:
            return None
        else:
            max_value = value_method(self.dtos[0])
            max_elem = self.dtos[0]
            for dto in self.dtos:
                next_value = value_method(dto)
                if compare_method(next_value, max_value):
                    max_value = next_value
                    max_elem = dto
            return max_elem


@dataclass(frozen=False)
class system_database_read_dtos(base_read_dtos):
    dtos: list[system_database_read_dto]
    def __init__(self, dtos: list[system_database_read_dto]):
        super().__init__(dtos)
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
        return list(map(lambda x: x.to_write(), self.dtos))
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
    def get_first_n(self, n: int) -> system_database_read_dtos:
        if len(self.dtos) > n:
            return system_database_read_dtos(self.dtos[:n])
        else:
            return system_database_read_dtos(self.dtos)
    def get_last(self) -> system_database_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
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
    def to_dict_by_system_database_name(self) -> dict[str, system_database_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.system_database_name] = dto
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
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[system_database_read_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[system_database_read_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return init
    def check_any(self, check_method: Callable[[system_database_read_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return init
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
    def find(self, check_method: Callable[[system_database_read_dto], bool]) -> system_database_read_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[system_database_read_dto], any], compare_method: Callable[[any, any], bool]) -> system_database_read_dto | None:
        if len(self.dtos) == 0:
            return None
        else:
            max_value = value_method(self.dtos[0])
            max_elem = self.dtos[0]
            for dto in self.dtos:
                next_value = value_method(dto)
                if compare_method(next_value, max_value):
                    max_value = next_value
                    max_elem = dto
            return max_elem


@dataclass(frozen=False)
class system_exception_read_dtos(base_read_dtos):
    dtos: list[system_exception_read_dto]
    def __init__(self, dtos: list[system_exception_read_dto]):
        super().__init__(dtos)
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
        return list(map(lambda x: x.to_write(), self.dtos))
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
    def get_first_n(self, n: int) -> system_exception_read_dtos:
        if len(self.dtos) > n:
            return system_exception_read_dtos(self.dtos[:n])
        else:
            return system_exception_read_dtos(self.dtos)
    def get_last(self) -> system_exception_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
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
    def to_dict_by_system_exception_name(self) -> dict[str, system_exception_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.system_exception_name] = dto
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
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[system_exception_read_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[system_exception_read_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return init
    def check_any(self, check_method: Callable[[system_exception_read_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return init
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
    def find(self, check_method: Callable[[system_exception_read_dto], bool]) -> system_exception_read_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[system_exception_read_dto], any], compare_method: Callable[[any, any], bool]) -> system_exception_read_dto | None:
        if len(self.dtos) == 0:
            return None
        else:
            max_value = value_method(self.dtos[0])
            max_elem = self.dtos[0]
            for dto in self.dtos:
                next_value = value_method(dto)
                if compare_method(next_value, max_value):
                    max_value = next_value
                    max_elem = dto
            return max_elem


@dataclass(frozen=False)
class system_instance_read_dtos(base_read_dtos):
    dtos: list[system_instance_read_dto]
    def __init__(self, dtos: list[system_instance_read_dto]):
        super().__init__(dtos)
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
        return list(map(lambda x: x.to_write(), self.dtos))
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
    def get_first_n(self, n: int) -> system_instance_read_dtos:
        if len(self.dtos) > n:
            return system_instance_read_dtos(self.dtos[:n])
        else:
            return system_instance_read_dtos(self.dtos)
    def get_last(self) -> system_instance_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
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
    def to_dict_by_system_instance_name(self) -> dict[str, system_instance_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.system_instance_name] = dto
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
    def to_dict_by_ticks_count(self) -> dict[str, system_instance_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.ticks_count] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[system_instance_read_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[system_instance_read_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return init
    def check_any(self, check_method: Callable[[system_instance_read_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return init
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
    def find(self, check_method: Callable[[system_instance_read_dto], bool]) -> system_instance_read_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[system_instance_read_dto], any], compare_method: Callable[[any, any], bool]) -> system_instance_read_dto | None:
        if len(self.dtos) == 0:
            return None
        else:
            max_value = value_method(self.dtos[0])
            max_elem = self.dtos[0]
            for dto in self.dtos:
                next_value = value_method(dto)
                if compare_method(next_value, max_value):
                    max_value = next_value
                    max_elem = dto
            return max_elem


@dataclass(frozen=False)
class system_license_read_dtos(base_read_dtos):
    dtos: list[system_license_read_dto]
    def __init__(self, dtos: list[system_license_read_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[system_license_read_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: system_license_read_dto):
        return cls(list([dto]))
    @classmethod
    def from_lists(cls, dtos1: list[system_license_read_dto], dtos2: list[system_license_read_dto]):
        return cls(dtos1 + dtos2)
    def get_active(self):
        return system_license_read_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return system_license_read_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_write_dtos(self) -> list[system_license_write_dto]:
        return list(map(lambda x: x.to_write(), self.dtos))
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write().to_write_dict(), self.dtos))
    def get_read_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> system_license_read_dto | None:
        found_dtos = list(filter(lambda x: x.system_license_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def get_first(self) -> system_license_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> system_license_read_dtos:
        if len(self.dtos) > n:
            return system_license_read_dtos(self.dtos[:n])
        else:
            return system_license_read_dtos(self.dtos)
    def get_last(self) -> system_license_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, system_license_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def to_dict_by_system_license_uid(self) -> dict[str, system_license_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.system_license_uid] = dto
        return d
    def to_dict_by_system_license_name(self) -> dict[str, system_license_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.system_license_name] = dto
        return d
    def to_dict_by_license_description(self) -> dict[str, system_license_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.license_description] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[system_license_read_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[system_license_read_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return init
    def check_any(self, check_method: Callable[[system_license_read_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return init
    def map_to_string(self, map_method: Callable[[system_license_read_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[system_license_read_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[system_license_read_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, system_license_read_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, system_license_read_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, system_license_read_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[system_license_read_dto], bool]) -> system_license_read_dtos:
        return system_license_read_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[system_license_read_dto], str]) -> dict[str, system_license_read_dtos]:
        grp_data: dict[str, system_license_read_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = system_license_read_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[system_license_read_dto], str], agg_method: Callable[[system_license_read_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, system_license_read_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[system_license_read_dto], bool]) -> system_license_read_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[system_license_read_dto], any], compare_method: Callable[[any, any], bool]) -> system_license_read_dto | None:
        if len(self.dtos) == 0:
            return None
        else:
            max_value = value_method(self.dtos[0])
            max_elem = self.dtos[0]
            for dto in self.dtos:
                next_value = value_method(dto)
                if compare_method(next_value, max_value):
                    max_value = next_value
                    max_elem = dto
            return max_elem


@dataclass(frozen=False)
class system_lock_read_dtos(base_read_dtos):
    dtos: list[system_lock_read_dto]
    def __init__(self, dtos: list[system_lock_read_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[system_lock_read_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: system_lock_read_dto):
        return cls(list([dto]))
    @classmethod
    def from_lists(cls, dtos1: list[system_lock_read_dto], dtos2: list[system_lock_read_dto]):
        return cls(dtos1 + dtos2)
    def get_active(self):
        return system_lock_read_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return system_lock_read_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_write_dtos(self) -> list[system_lock_write_dto]:
        return list(map(lambda x: x.to_write(), self.dtos))
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write().to_write_dict(), self.dtos))
    def get_read_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> system_lock_read_dto | None:
        found_dtos = list(filter(lambda x: x.system_lock_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def get_first(self) -> system_lock_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> system_lock_read_dtos:
        if len(self.dtos) > n:
            return system_lock_read_dtos(self.dtos[:n])
        else:
            return system_lock_read_dtos(self.dtos)
    def get_last(self) -> system_lock_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, system_lock_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def to_dict_by_system_lock_uid(self) -> dict[str, system_lock_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.system_lock_uid] = dto
        return d
    def to_dict_by_system_lock_name(self) -> dict[str, system_lock_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.system_lock_name] = dto
        return d
    def to_dict_by_lock_account_uid(self) -> dict[str, system_lock_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.lock_account_uid] = dto
        return d
    def to_dict_by_lock_comment(self) -> dict[str, system_lock_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.lock_comment] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[system_lock_read_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[system_lock_read_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return init
    def check_any(self, check_method: Callable[[system_lock_read_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return init
    def map_to_string(self, map_method: Callable[[system_lock_read_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[system_lock_read_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[system_lock_read_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, system_lock_read_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, system_lock_read_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, system_lock_read_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[system_lock_read_dto], bool]) -> system_lock_read_dtos:
        return system_lock_read_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[system_lock_read_dto], str]) -> dict[str, system_lock_read_dtos]:
        grp_data: dict[str, system_lock_read_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = system_lock_read_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[system_lock_read_dto], str], agg_method: Callable[[system_lock_read_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, system_lock_read_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[system_lock_read_dto], bool]) -> system_lock_read_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[system_lock_read_dto], any], compare_method: Callable[[any, any], bool]) -> system_lock_read_dto | None:
        if len(self.dtos) == 0:
            return None
        else:
            max_value = value_method(self.dtos[0])
            max_elem = self.dtos[0]
            for dto in self.dtos:
                next_value = value_method(dto)
                if compare_method(next_value, max_value):
                    max_value = next_value
                    max_elem = dto
            return max_elem


@dataclass(frozen=False)
class system_module_read_dtos(base_read_dtos):
    dtos: list[system_module_read_dto]
    def __init__(self, dtos: list[system_module_read_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[system_module_read_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: system_module_read_dto):
        return cls(list([dto]))
    @classmethod
    def from_lists(cls, dtos1: list[system_module_read_dto], dtos2: list[system_module_read_dto]):
        return cls(dtos1 + dtos2)
    def get_active(self):
        return system_module_read_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return system_module_read_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_write_dtos(self) -> list[system_module_write_dto]:
        return list(map(lambda x: x.to_write(), self.dtos))
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write().to_write_dict(), self.dtos))
    def get_read_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> system_module_read_dto | None:
        found_dtos = list(filter(lambda x: x.system_module_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def get_first(self) -> system_module_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> system_module_read_dtos:
        if len(self.dtos) > n:
            return system_module_read_dtos(self.dtos[:n])
        else:
            return system_module_read_dtos(self.dtos)
    def get_last(self) -> system_module_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, system_module_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def to_dict_by_system_module_uid(self) -> dict[str, system_module_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.system_module_uid] = dto
        return d
    def to_dict_by_system_module_name(self) -> dict[str, system_module_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.system_module_name] = dto
        return d
    def to_dict_by_system_module_description(self) -> dict[str, system_module_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.system_module_description] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[system_module_read_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[system_module_read_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return init
    def check_any(self, check_method: Callable[[system_module_read_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return init
    def map_to_string(self, map_method: Callable[[system_module_read_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[system_module_read_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[system_module_read_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, system_module_read_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, system_module_read_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, system_module_read_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[system_module_read_dto], bool]) -> system_module_read_dtos:
        return system_module_read_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[system_module_read_dto], str]) -> dict[str, system_module_read_dtos]:
        grp_data: dict[str, system_module_read_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = system_module_read_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[system_module_read_dto], str], agg_method: Callable[[system_module_read_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, system_module_read_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[system_module_read_dto], bool]) -> system_module_read_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[system_module_read_dto], any], compare_method: Callable[[any, any], bool]) -> system_module_read_dto | None:
        if len(self.dtos) == 0:
            return None
        else:
            max_value = value_method(self.dtos[0])
            max_elem = self.dtos[0]
            for dto in self.dtos:
                next_value = value_method(dto)
                if compare_method(next_value, max_value):
                    max_value = next_value
                    max_elem = dto
            return max_elem


@dataclass(frozen=False)
class system_object_read_dtos(base_read_dtos):
    dtos: list[system_object_read_dto]
    def __init__(self, dtos: list[system_object_read_dto]):
        super().__init__(dtos)
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
        return list(map(lambda x: x.to_write(), self.dtos))
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
    def get_first_n(self, n: int) -> system_object_read_dtos:
        if len(self.dtos) > n:
            return system_object_read_dtos(self.dtos[:n])
        else:
            return system_object_read_dtos(self.dtos)
    def get_last(self) -> system_object_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
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
    def to_dict_by_system_object_name(self) -> dict[str, system_object_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.system_object_name] = dto
        return d
    def to_dict_by_system_version_uid(self) -> dict[str, system_object_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.system_version_uid] = dto
        return d
    def to_dict_by_system_table_uid(self) -> dict[str, system_object_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.system_table_uid] = dto
        return d
    def to_dict_by_system_object_type_uid(self) -> dict[str, system_object_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.system_object_type_uid] = dto
        return d
    def to_dict_by_parent_system_object_uid(self) -> dict[str, system_object_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.parent_system_object_uid] = dto
        return d
    def to_dict_by_object_type(self) -> dict[str, system_object_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.object_type] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[system_object_read_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[system_object_read_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return init
    def check_any(self, check_method: Callable[[system_object_read_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return init
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
    def find(self, check_method: Callable[[system_object_read_dto], bool]) -> system_object_read_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[system_object_read_dto], any], compare_method: Callable[[any, any], bool]) -> system_object_read_dto | None:
        if len(self.dtos) == 0:
            return None
        else:
            max_value = value_method(self.dtos[0])
            max_elem = self.dtos[0]
            for dto in self.dtos:
                next_value = value_method(dto)
                if compare_method(next_value, max_value):
                    max_value = next_value
                    max_elem = dto
            return max_elem


@dataclass(frozen=False)
class system_object_type_read_dtos(base_read_dtos):
    dtos: list[system_object_type_read_dto]
    def __init__(self, dtos: list[system_object_type_read_dto]):
        super().__init__(dtos)
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
        return list(map(lambda x: x.to_write(), self.dtos))
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
    def get_first_n(self, n: int) -> system_object_type_read_dtos:
        if len(self.dtos) > n:
            return system_object_type_read_dtos(self.dtos[:n])
        else:
            return system_object_type_read_dtos(self.dtos)
    def get_last(self) -> system_object_type_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
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
    def to_dict_by_system_object_type_name(self) -> dict[str, system_object_type_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.system_object_type_name] = dto
        return d
    def to_dict_by_object_type_description(self) -> dict[str, system_object_type_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.object_type_description] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[system_object_type_read_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[system_object_type_read_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return init
    def check_any(self, check_method: Callable[[system_object_type_read_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return init
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
    def find(self, check_method: Callable[[system_object_type_read_dto], bool]) -> system_object_type_read_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[system_object_type_read_dto], any], compare_method: Callable[[any, any], bool]) -> system_object_type_read_dto | None:
        if len(self.dtos) == 0:
            return None
        else:
            max_value = value_method(self.dtos[0])
            max_elem = self.dtos[0]
            for dto in self.dtos:
                next_value = value_method(dto)
                if compare_method(next_value, max_value):
                    max_value = next_value
                    max_elem = dto
            return max_elem


@dataclass(frozen=False)
class system_query_read_dtos(base_read_dtos):
    dtos: list[system_query_read_dto]
    def __init__(self, dtos: list[system_query_read_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[system_query_read_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: system_query_read_dto):
        return cls(list([dto]))
    @classmethod
    def from_lists(cls, dtos1: list[system_query_read_dto], dtos2: list[system_query_read_dto]):
        return cls(dtos1 + dtos2)
    def get_active(self):
        return system_query_read_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return system_query_read_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_write_dtos(self) -> list[system_query_write_dto]:
        return list(map(lambda x: x.to_write(), self.dtos))
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write().to_write_dict(), self.dtos))
    def get_read_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> system_query_read_dto | None:
        found_dtos = list(filter(lambda x: x.system_query_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def get_first(self) -> system_query_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> system_query_read_dtos:
        if len(self.dtos) > n:
            return system_query_read_dtos(self.dtos[:n])
        else:
            return system_query_read_dtos(self.dtos)
    def get_last(self) -> system_query_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, system_query_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def to_dict_by_system_query_uid(self) -> dict[str, system_query_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.system_query_uid] = dto
        return d
    def to_dict_by_system_query_name(self) -> dict[str, system_query_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.system_query_name] = dto
        return d
    def to_dict_by_time_start(self) -> dict[str, system_query_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.time_start] = dto
        return d
    def to_dict_by_total_query_time(self) -> dict[str, system_query_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.total_query_time] = dto
        return d
    def to_dict_by_query_seq(self) -> dict[str, system_query_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.query_seq] = dto
        return d
    def to_dict_by_execution_counter(self) -> dict[str, system_query_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.execution_counter] = dto
        return d
    def to_dict_by_connection_counter(self) -> dict[str, system_query_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.connection_counter] = dto
        return d
    def to_dict_by_release_counter(self) -> dict[str, system_query_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.release_counter] = dto
        return d
    def to_dict_by_current_active(self) -> dict[str, system_query_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.current_active] = dto
        return d
    def to_dict_by_current_idle(self) -> dict[str, system_query_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.current_idle] = dto
        return d
    def to_dict_by_table_name(self) -> dict[str, system_query_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.table_name] = dto
        return d
    def to_dict_by_rows_count(self) -> dict[str, system_query_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.rows_count] = dto
        return d
    def to_dict_by_sql(self) -> dict[str, system_query_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.sql] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[system_query_read_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[system_query_read_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return init
    def check_any(self, check_method: Callable[[system_query_read_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return init
    def map_to_string(self, map_method: Callable[[system_query_read_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[system_query_read_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[system_query_read_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, system_query_read_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, system_query_read_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, system_query_read_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[system_query_read_dto], bool]) -> system_query_read_dtos:
        return system_query_read_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[system_query_read_dto], str]) -> dict[str, system_query_read_dtos]:
        grp_data: dict[str, system_query_read_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = system_query_read_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[system_query_read_dto], str], agg_method: Callable[[system_query_read_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, system_query_read_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[system_query_read_dto], bool]) -> system_query_read_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[system_query_read_dto], any], compare_method: Callable[[any, any], bool]) -> system_query_read_dto | None:
        if len(self.dtos) == 0:
            return None
        else:
            max_value = value_method(self.dtos[0])
            max_elem = self.dtos[0]
            for dto in self.dtos:
                next_value = value_method(dto)
                if compare_method(next_value, max_value):
                    max_value = next_value
                    max_elem = dto
            return max_elem


@dataclass(frozen=False)
class system_request_read_dtos(base_read_dtos):
    dtos: list[system_request_read_dto]
    def __init__(self, dtos: list[system_request_read_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[system_request_read_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: system_request_read_dto):
        return cls(list([dto]))
    @classmethod
    def from_lists(cls, dtos1: list[system_request_read_dto], dtos2: list[system_request_read_dto]):
        return cls(dtos1 + dtos2)
    def get_active(self):
        return system_request_read_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return system_request_read_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_write_dtos(self) -> list[system_request_write_dto]:
        return list(map(lambda x: x.to_write(), self.dtos))
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write().to_write_dict(), self.dtos))
    def get_read_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> system_request_read_dto | None:
        found_dtos = list(filter(lambda x: x.system_request_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def get_first(self) -> system_request_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> system_request_read_dtos:
        if len(self.dtos) > n:
            return system_request_read_dtos(self.dtos[:n])
        else:
            return system_request_read_dtos(self.dtos)
    def get_last(self) -> system_request_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, system_request_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def to_dict_by_system_request_uid(self) -> dict[str, system_request_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.system_request_uid] = dto
        return d
    def to_dict_by_system_request_name(self) -> dict[str, system_request_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.system_request_name] = dto
        return d
    def to_dict_by_account_uid(self) -> dict[str, system_request_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.account_uid] = dto
        return d
    def to_dict_by_request_method(self) -> dict[str, system_request_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.request_method] = dto
        return d
    def to_dict_by_request_url(self) -> dict[str, system_request_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.request_url] = dto
        return d
    def to_dict_by_request_body_size(self) -> dict[str, system_request_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.request_body_size] = dto
        return d
    def to_dict_by_request_host(self) -> dict[str, system_request_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.request_host] = dto
        return d
    def to_dict_by_request_time(self) -> dict[str, system_request_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.request_time] = dto
        return d
    def to_dict_by_response_code(self) -> dict[str, system_request_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.response_code] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[system_request_read_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[system_request_read_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return init
    def check_any(self, check_method: Callable[[system_request_read_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return init
    def map_to_string(self, map_method: Callable[[system_request_read_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[system_request_read_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[system_request_read_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, system_request_read_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, system_request_read_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, system_request_read_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[system_request_read_dto], bool]) -> system_request_read_dtos:
        return system_request_read_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[system_request_read_dto], str]) -> dict[str, system_request_read_dtos]:
        grp_data: dict[str, system_request_read_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = system_request_read_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[system_request_read_dto], str], agg_method: Callable[[system_request_read_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, system_request_read_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[system_request_read_dto], bool]) -> system_request_read_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[system_request_read_dto], any], compare_method: Callable[[any, any], bool]) -> system_request_read_dto | None:
        if len(self.dtos) == 0:
            return None
        else:
            max_value = value_method(self.dtos[0])
            max_elem = self.dtos[0]
            for dto in self.dtos:
                next_value = value_method(dto)
                if compare_method(next_value, max_value):
                    max_value = next_value
                    max_elem = dto
            return max_elem


@dataclass(frozen=False)
class system_setting_read_dtos(base_read_dtos):
    dtos: list[system_setting_read_dto]
    def __init__(self, dtos: list[system_setting_read_dto]):
        super().__init__(dtos)
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
        return list(map(lambda x: x.to_write(), self.dtos))
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
    def get_first_n(self, n: int) -> system_setting_read_dtos:
        if len(self.dtos) > n:
            return system_setting_read_dtos(self.dtos[:n])
        else:
            return system_setting_read_dtos(self.dtos)
    def get_last(self) -> system_setting_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
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
    def to_dict_by_system_setting_name(self) -> dict[str, system_setting_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.system_setting_name] = dto
        return d
    def to_dict_by_setting_value(self) -> dict[str, system_setting_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.setting_value] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[system_setting_read_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[system_setting_read_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return init
    def check_any(self, check_method: Callable[[system_setting_read_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return init
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
    def find(self, check_method: Callable[[system_setting_read_dto], bool]) -> system_setting_read_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[system_setting_read_dto], any], compare_method: Callable[[any, any], bool]) -> system_setting_read_dto | None:
        if len(self.dtos) == 0:
            return None
        else:
            max_value = value_method(self.dtos[0])
            max_elem = self.dtos[0]
            for dto in self.dtos:
                next_value = value_method(dto)
                if compare_method(next_value, max_value):
                    max_value = next_value
                    max_elem = dto
            return max_elem


@dataclass(frozen=False)
class system_setting_account_read_dtos(base_read_dtos):
    dtos: list[system_setting_account_read_dto]
    def __init__(self, dtos: list[system_setting_account_read_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[system_setting_account_read_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: system_setting_account_read_dto):
        return cls(list([dto]))
    @classmethod
    def from_lists(cls, dtos1: list[system_setting_account_read_dto], dtos2: list[system_setting_account_read_dto]):
        return cls(dtos1 + dtos2)
    def get_active(self):
        return system_setting_account_read_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return system_setting_account_read_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_write_dtos(self) -> list[system_setting_account_write_dto]:
        return list(map(lambda x: x.to_write(), self.dtos))
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write().to_write_dict(), self.dtos))
    def get_read_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> system_setting_account_read_dto | None:
        found_dtos = list(filter(lambda x: x.system_setting_account_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def get_first(self) -> system_setting_account_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> system_setting_account_read_dtos:
        if len(self.dtos) > n:
            return system_setting_account_read_dtos(self.dtos[:n])
        else:
            return system_setting_account_read_dtos(self.dtos)
    def get_last(self) -> system_setting_account_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, system_setting_account_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def to_dict_by_system_setting_account_uid(self) -> dict[str, system_setting_account_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.system_setting_account_uid] = dto
        return d
    def to_dict_by_system_setting_account_name(self) -> dict[str, system_setting_account_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.system_setting_account_name] = dto
        return d
    def to_dict_by_account_uid(self) -> dict[str, system_setting_account_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.account_uid] = dto
        return d
    def to_dict_by_setting_value(self) -> dict[str, system_setting_account_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.setting_value] = dto
        return d
    def to_dict_by_is_public(self) -> dict[str, system_setting_account_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.is_public] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[system_setting_account_read_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[system_setting_account_read_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return init
    def check_any(self, check_method: Callable[[system_setting_account_read_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return init
    def map_to_string(self, map_method: Callable[[system_setting_account_read_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[system_setting_account_read_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[system_setting_account_read_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, system_setting_account_read_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, system_setting_account_read_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, system_setting_account_read_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[system_setting_account_read_dto], bool]) -> system_setting_account_read_dtos:
        return system_setting_account_read_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[system_setting_account_read_dto], str]) -> dict[str, system_setting_account_read_dtos]:
        grp_data: dict[str, system_setting_account_read_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = system_setting_account_read_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[system_setting_account_read_dto], str], agg_method: Callable[[system_setting_account_read_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, system_setting_account_read_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[system_setting_account_read_dto], bool]) -> system_setting_account_read_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[system_setting_account_read_dto], any], compare_method: Callable[[any, any], bool]) -> system_setting_account_read_dto | None:
        if len(self.dtos) == 0:
            return None
        else:
            max_value = value_method(self.dtos[0])
            max_elem = self.dtos[0]
            for dto in self.dtos:
                next_value = value_method(dto)
                if compare_method(next_value, max_value):
                    max_value = next_value
                    max_elem = dto
            return max_elem


@dataclass(frozen=False)
class system_state_read_dtos(base_read_dtos):
    dtos: list[system_state_read_dto]
    def __init__(self, dtos: list[system_state_read_dto]):
        super().__init__(dtos)
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
        return list(map(lambda x: x.to_write(), self.dtos))
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
    def get_first_n(self, n: int) -> system_state_read_dtos:
        if len(self.dtos) > n:
            return system_state_read_dtos(self.dtos[:n])
        else:
            return system_state_read_dtos(self.dtos)
    def get_last(self) -> system_state_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
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
    def to_dict_by_system_state_name(self) -> dict[str, system_state_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.system_state_name] = dto
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
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[system_state_read_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[system_state_read_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return init
    def check_any(self, check_method: Callable[[system_state_read_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return init
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
    def find(self, check_method: Callable[[system_state_read_dto], bool]) -> system_state_read_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[system_state_read_dto], any], compare_method: Callable[[any, any], bool]) -> system_state_read_dto | None:
        if len(self.dtos) == 0:
            return None
        else:
            max_value = value_method(self.dtos[0])
            max_elem = self.dtos[0]
            for dto in self.dtos:
                next_value = value_method(dto)
                if compare_method(next_value, max_value):
                    max_value = next_value
                    max_elem = dto
            return max_elem


@dataclass(frozen=False)
class system_table_read_dtos(base_read_dtos):
    dtos: list[system_table_read_dto]
    def __init__(self, dtos: list[system_table_read_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[system_table_read_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: system_table_read_dto):
        return cls(list([dto]))
    @classmethod
    def from_lists(cls, dtos1: list[system_table_read_dto], dtos2: list[system_table_read_dto]):
        return cls(dtos1 + dtos2)
    def get_active(self):
        return system_table_read_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return system_table_read_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_write_dtos(self) -> list[system_table_write_dto]:
        return list(map(lambda x: x.to_write(), self.dtos))
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write().to_write_dict(), self.dtos))
    def get_read_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> system_table_read_dto | None:
        found_dtos = list(filter(lambda x: x.system_table_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def get_first(self) -> system_table_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> system_table_read_dtos:
        if len(self.dtos) > n:
            return system_table_read_dtos(self.dtos[:n])
        else:
            return system_table_read_dtos(self.dtos)
    def get_last(self) -> system_table_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, system_table_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def to_dict_by_system_table_uid(self) -> dict[str, system_table_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.system_table_uid] = dto
        return d
    def to_dict_by_system_table_name(self) -> dict[str, system_table_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.system_table_name] = dto
        return d
    def to_dict_by_parent_system_table_uid(self) -> dict[str, system_table_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.parent_system_table_uid] = dto
        return d
    def to_dict_by_key_name(self) -> dict[str, system_table_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.key_name] = dto
        return d
    def to_dict_by_table_code(self) -> dict[str, system_table_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.table_code] = dto
        return d
    def to_dict_by_table_comment(self) -> dict[str, system_table_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.table_comment] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[system_table_read_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[system_table_read_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return init
    def check_any(self, check_method: Callable[[system_table_read_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return init
    def map_to_string(self, map_method: Callable[[system_table_read_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[system_table_read_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[system_table_read_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, system_table_read_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, system_table_read_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, system_table_read_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[system_table_read_dto], bool]) -> system_table_read_dtos:
        return system_table_read_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[system_table_read_dto], str]) -> dict[str, system_table_read_dtos]:
        grp_data: dict[str, system_table_read_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = system_table_read_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[system_table_read_dto], str], agg_method: Callable[[system_table_read_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, system_table_read_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[system_table_read_dto], bool]) -> system_table_read_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[system_table_read_dto], any], compare_method: Callable[[any, any], bool]) -> system_table_read_dto | None:
        if len(self.dtos) == 0:
            return None
        else:
            max_value = value_method(self.dtos[0])
            max_elem = self.dtos[0]
            for dto in self.dtos:
                next_value = value_method(dto)
                if compare_method(next_value, max_value):
                    max_value = next_value
                    max_elem = dto
            return max_elem


@dataclass(frozen=False)
class system_thread_read_dtos(base_read_dtos):
    dtos: list[system_thread_read_dto]
    def __init__(self, dtos: list[system_thread_read_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[system_thread_read_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: system_thread_read_dto):
        return cls(list([dto]))
    @classmethod
    def from_lists(cls, dtos1: list[system_thread_read_dto], dtos2: list[system_thread_read_dto]):
        return cls(dtos1 + dtos2)
    def get_active(self):
        return system_thread_read_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return system_thread_read_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_write_dtos(self) -> list[system_thread_write_dto]:
        return list(map(lambda x: x.to_write(), self.dtos))
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write().to_write_dict(), self.dtos))
    def get_read_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> system_thread_read_dto | None:
        found_dtos = list(filter(lambda x: x.system_thread_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def get_first(self) -> system_thread_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> system_thread_read_dtos:
        if len(self.dtos) > n:
            return system_thread_read_dtos(self.dtos[:n])
        else:
            return system_thread_read_dtos(self.dtos)
    def get_last(self) -> system_thread_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, system_thread_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def to_dict_by_system_thread_uid(self) -> dict[str, system_thread_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.system_thread_uid] = dto
        return d
    def to_dict_by_system_thread_name(self) -> dict[str, system_thread_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.system_thread_name] = dto
        return d
    def to_dict_by_thread_name(self) -> dict[str, system_thread_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.thread_name] = dto
        return d
    def to_dict_by_parent_object(self) -> dict[str, system_thread_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.parent_object] = dto
        return d
    def to_dict_by_ticks_count(self) -> dict[str, system_thread_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.ticks_count] = dto
        return d
    def to_dict_by_sleep_time(self) -> dict[str, system_thread_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.sleep_time] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[system_thread_read_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[system_thread_read_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return init
    def check_any(self, check_method: Callable[[system_thread_read_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return init
    def map_to_string(self, map_method: Callable[[system_thread_read_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[system_thread_read_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[system_thread_read_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, system_thread_read_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, system_thread_read_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, system_thread_read_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[system_thread_read_dto], bool]) -> system_thread_read_dtos:
        return system_thread_read_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[system_thread_read_dto], str]) -> dict[str, system_thread_read_dtos]:
        grp_data: dict[str, system_thread_read_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = system_thread_read_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[system_thread_read_dto], str], agg_method: Callable[[system_thread_read_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, system_thread_read_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[system_thread_read_dto], bool]) -> system_thread_read_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[system_thread_read_dto], any], compare_method: Callable[[any, any], bool]) -> system_thread_read_dto | None:
        if len(self.dtos) == 0:
            return None
        else:
            max_value = value_method(self.dtos[0])
            max_elem = self.dtos[0]
            for dto in self.dtos:
                next_value = value_method(dto)
                if compare_method(next_value, max_value):
                    max_value = next_value
                    max_elem = dto
            return max_elem


@dataclass(frozen=False)
class system_version_read_dtos(base_read_dtos):
    dtos: list[system_version_read_dto]
    def __init__(self, dtos: list[system_version_read_dto]):
        super().__init__(dtos)
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
        return list(map(lambda x: x.to_write(), self.dtos))
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
    def get_first_n(self, n: int) -> system_version_read_dtos:
        if len(self.dtos) > n:
            return system_version_read_dtos(self.dtos[:n])
        else:
            return system_version_read_dtos(self.dtos)
    def get_last(self) -> system_version_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
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
    def to_dict_by_system_version_name(self) -> dict[str, system_version_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.system_version_name] = dto
        return d
    def to_dict_by_version_description(self) -> dict[str, system_version_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.version_description] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[system_version_read_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[system_version_read_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return init
    def check_any(self, check_method: Callable[[system_version_read_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return init
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
    def find(self, check_method: Callable[[system_version_read_dto], bool]) -> system_version_read_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[system_version_read_dto], any], compare_method: Callable[[any, any], bool]) -> system_version_read_dto | None:
        if len(self.dtos) == 0:
            return None
        else:
            max_value = value_method(self.dtos[0])
            max_elem = self.dtos[0]
            for dto in self.dtos:
                next_value = value_method(dto)
                if compare_method(next_value, max_value):
                    max_value = next_value
                    max_elem = dto
            return max_elem


@dataclass(frozen=False)
class tenant_read_dtos(base_read_dtos):
    dtos: list[tenant_read_dto]
    def __init__(self, dtos: list[tenant_read_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[tenant_read_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: tenant_read_dto):
        return cls(list([dto]))
    @classmethod
    def from_lists(cls, dtos1: list[tenant_read_dto], dtos2: list[tenant_read_dto]):
        return cls(dtos1 + dtos2)
    def get_active(self):
        return tenant_read_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return tenant_read_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_write_dtos(self) -> list[tenant_write_dto]:
        return list(map(lambda x: x.to_write(), self.dtos))
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write().to_write_dict(), self.dtos))
    def get_read_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> tenant_read_dto | None:
        found_dtos = list(filter(lambda x: x.tenant_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def get_first(self) -> tenant_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> tenant_read_dtos:
        if len(self.dtos) > n:
            return tenant_read_dtos(self.dtos[:n])
        else:
            return tenant_read_dtos(self.dtos)
    def get_last(self) -> tenant_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, tenant_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def to_dict_by_tenant_uid(self) -> dict[str, tenant_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.tenant_uid] = dto
        return d
    def to_dict_by_tenant_name(self) -> dict[str, tenant_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.tenant_name] = dto
        return d
    def to_dict_by_country_uid(self) -> dict[str, tenant_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.country_uid] = dto
        return d
    def to_dict_by_tenant_type_uid(self) -> dict[str, tenant_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.tenant_type_uid] = dto
        return d
    def to_dict_by_tenant_category_uid(self) -> dict[str, tenant_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.tenant_category_uid] = dto
        return d
    def to_dict_by_tenant_code(self) -> dict[str, tenant_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.tenant_code] = dto
        return d
    def to_dict_by_tenant_description(self) -> dict[str, tenant_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.tenant_description] = dto
        return d
    def to_dict_by_start_date(self) -> dict[str, tenant_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.start_date] = dto
        return d
    def to_dict_by_end_date(self) -> dict[str, tenant_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.end_date] = dto
        return d
    def to_dict_by_is_internal(self) -> dict[str, tenant_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.is_internal] = dto
        return d
    def to_dict_by_is_system(self) -> dict[str, tenant_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.is_system] = dto
        return d
    def to_dict_by_is_test(self) -> dict[str, tenant_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.is_test] = dto
        return d
    def to_dict_by_account_uid(self) -> dict[str, tenant_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.account_uid] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[tenant_read_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[tenant_read_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return init
    def check_any(self, check_method: Callable[[tenant_read_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return init
    def map_to_string(self, map_method: Callable[[tenant_read_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[tenant_read_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[tenant_read_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, tenant_read_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, tenant_read_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, tenant_read_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[tenant_read_dto], bool]) -> tenant_read_dtos:
        return tenant_read_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[tenant_read_dto], str]) -> dict[str, tenant_read_dtos]:
        grp_data: dict[str, tenant_read_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = tenant_read_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[tenant_read_dto], str], agg_method: Callable[[tenant_read_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, tenant_read_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[tenant_read_dto], bool]) -> tenant_read_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[tenant_read_dto], any], compare_method: Callable[[any, any], bool]) -> tenant_read_dto | None:
        if len(self.dtos) == 0:
            return None
        else:
            max_value = value_method(self.dtos[0])
            max_elem = self.dtos[0]
            for dto in self.dtos:
                next_value = value_method(dto)
                if compare_method(next_value, max_value):
                    max_value = next_value
                    max_elem = dto
            return max_elem


@dataclass(frozen=False)
class tenant_account_read_dtos(base_read_dtos):
    dtos: list[tenant_account_read_dto]
    def __init__(self, dtos: list[tenant_account_read_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[tenant_account_read_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: tenant_account_read_dto):
        return cls(list([dto]))
    @classmethod
    def from_lists(cls, dtos1: list[tenant_account_read_dto], dtos2: list[tenant_account_read_dto]):
        return cls(dtos1 + dtos2)
    def get_active(self):
        return tenant_account_read_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return tenant_account_read_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_write_dtos(self) -> list[tenant_account_write_dto]:
        return list(map(lambda x: x.to_write(), self.dtos))
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write().to_write_dict(), self.dtos))
    def get_read_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> tenant_account_read_dto | None:
        found_dtos = list(filter(lambda x: x.tenant_account_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def get_first(self) -> tenant_account_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> tenant_account_read_dtos:
        if len(self.dtos) > n:
            return tenant_account_read_dtos(self.dtos[:n])
        else:
            return tenant_account_read_dtos(self.dtos)
    def get_last(self) -> tenant_account_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, tenant_account_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def to_dict_by_tenant_account_uid(self) -> dict[str, tenant_account_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.tenant_account_uid] = dto
        return d
    def to_dict_by_tenant_account_name(self) -> dict[str, tenant_account_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.tenant_account_name] = dto
        return d
    def to_dict_by_tenant_uid(self) -> dict[str, tenant_account_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.tenant_uid] = dto
        return d
    def to_dict_by_account_uid(self) -> dict[str, tenant_account_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.account_uid] = dto
        return d
    def to_dict_by_tenant_role_uid(self) -> dict[str, tenant_account_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.tenant_role_uid] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[tenant_account_read_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[tenant_account_read_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return init
    def check_any(self, check_method: Callable[[tenant_account_read_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return init
    def map_to_string(self, map_method: Callable[[tenant_account_read_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[tenant_account_read_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[tenant_account_read_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, tenant_account_read_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, tenant_account_read_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, tenant_account_read_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[tenant_account_read_dto], bool]) -> tenant_account_read_dtos:
        return tenant_account_read_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[tenant_account_read_dto], str]) -> dict[str, tenant_account_read_dtos]:
        grp_data: dict[str, tenant_account_read_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = tenant_account_read_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[tenant_account_read_dto], str], agg_method: Callable[[tenant_account_read_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, tenant_account_read_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[tenant_account_read_dto], bool]) -> tenant_account_read_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[tenant_account_read_dto], any], compare_method: Callable[[any, any], bool]) -> tenant_account_read_dto | None:
        if len(self.dtos) == 0:
            return None
        else:
            max_value = value_method(self.dtos[0])
            max_elem = self.dtos[0]
            for dto in self.dtos:
                next_value = value_method(dto)
                if compare_method(next_value, max_value):
                    max_value = next_value
                    max_elem = dto
            return max_elem


@dataclass(frozen=False)
class tenant_category_read_dtos(base_read_dtos):
    dtos: list[tenant_category_read_dto]
    def __init__(self, dtos: list[tenant_category_read_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[tenant_category_read_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: tenant_category_read_dto):
        return cls(list([dto]))
    @classmethod
    def from_lists(cls, dtos1: list[tenant_category_read_dto], dtos2: list[tenant_category_read_dto]):
        return cls(dtos1 + dtos2)
    def get_active(self):
        return tenant_category_read_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return tenant_category_read_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_write_dtos(self) -> list[tenant_category_write_dto]:
        return list(map(lambda x: x.to_write(), self.dtos))
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write().to_write_dict(), self.dtos))
    def get_read_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> tenant_category_read_dto | None:
        found_dtos = list(filter(lambda x: x.tenant_category_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def get_first(self) -> tenant_category_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> tenant_category_read_dtos:
        if len(self.dtos) > n:
            return tenant_category_read_dtos(self.dtos[:n])
        else:
            return tenant_category_read_dtos(self.dtos)
    def get_last(self) -> tenant_category_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, tenant_category_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def to_dict_by_tenant_category_uid(self) -> dict[str, tenant_category_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.tenant_category_uid] = dto
        return d
    def to_dict_by_tenant_category_name(self) -> dict[str, tenant_category_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.tenant_category_name] = dto
        return d
    def to_dict_by_tenant_category_description(self) -> dict[str, tenant_category_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.tenant_category_description] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[tenant_category_read_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[tenant_category_read_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return init
    def check_any(self, check_method: Callable[[tenant_category_read_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return init
    def map_to_string(self, map_method: Callable[[tenant_category_read_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[tenant_category_read_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[tenant_category_read_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, tenant_category_read_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, tenant_category_read_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, tenant_category_read_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[tenant_category_read_dto], bool]) -> tenant_category_read_dtos:
        return tenant_category_read_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[tenant_category_read_dto], str]) -> dict[str, tenant_category_read_dtos]:
        grp_data: dict[str, tenant_category_read_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = tenant_category_read_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[tenant_category_read_dto], str], agg_method: Callable[[tenant_category_read_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, tenant_category_read_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[tenant_category_read_dto], bool]) -> tenant_category_read_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[tenant_category_read_dto], any], compare_method: Callable[[any, any], bool]) -> tenant_category_read_dto | None:
        if len(self.dtos) == 0:
            return None
        else:
            max_value = value_method(self.dtos[0])
            max_elem = self.dtos[0]
            for dto in self.dtos:
                next_value = value_method(dto)
                if compare_method(next_value, max_value):
                    max_value = next_value
                    max_elem = dto
            return max_elem


@dataclass(frozen=False)
class tenant_country_read_dtos(base_read_dtos):
    dtos: list[tenant_country_read_dto]
    def __init__(self, dtos: list[tenant_country_read_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[tenant_country_read_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: tenant_country_read_dto):
        return cls(list([dto]))
    @classmethod
    def from_lists(cls, dtos1: list[tenant_country_read_dto], dtos2: list[tenant_country_read_dto]):
        return cls(dtos1 + dtos2)
    def get_active(self):
        return tenant_country_read_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return tenant_country_read_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_write_dtos(self) -> list[tenant_country_write_dto]:
        return list(map(lambda x: x.to_write(), self.dtos))
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write().to_write_dict(), self.dtos))
    def get_read_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> tenant_country_read_dto | None:
        found_dtos = list(filter(lambda x: x.tenant_country_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def get_first(self) -> tenant_country_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> tenant_country_read_dtos:
        if len(self.dtos) > n:
            return tenant_country_read_dtos(self.dtos[:n])
        else:
            return tenant_country_read_dtos(self.dtos)
    def get_last(self) -> tenant_country_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, tenant_country_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def to_dict_by_tenant_country_uid(self) -> dict[str, tenant_country_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.tenant_country_uid] = dto
        return d
    def to_dict_by_tenant_country_name(self) -> dict[str, tenant_country_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.tenant_country_name] = dto
        return d
    def to_dict_by_country_uid(self) -> dict[str, tenant_country_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.country_uid] = dto
        return d
    def to_dict_by_tenant_uid(self) -> dict[str, tenant_country_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.tenant_uid] = dto
        return d
    def to_dict_by_country_priority(self) -> dict[str, tenant_country_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.country_priority] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[tenant_country_read_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[tenant_country_read_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return init
    def check_any(self, check_method: Callable[[tenant_country_read_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return init
    def map_to_string(self, map_method: Callable[[tenant_country_read_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[tenant_country_read_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[tenant_country_read_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, tenant_country_read_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, tenant_country_read_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, tenant_country_read_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[tenant_country_read_dto], bool]) -> tenant_country_read_dtos:
        return tenant_country_read_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[tenant_country_read_dto], str]) -> dict[str, tenant_country_read_dtos]:
        grp_data: dict[str, tenant_country_read_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = tenant_country_read_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[tenant_country_read_dto], str], agg_method: Callable[[tenant_country_read_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, tenant_country_read_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[tenant_country_read_dto], bool]) -> tenant_country_read_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[tenant_country_read_dto], any], compare_method: Callable[[any, any], bool]) -> tenant_country_read_dto | None:
        if len(self.dtos) == 0:
            return None
        else:
            max_value = value_method(self.dtos[0])
            max_elem = self.dtos[0]
            for dto in self.dtos:
                next_value = value_method(dto)
                if compare_method(next_value, max_value):
                    max_value = next_value
                    max_elem = dto
            return max_elem


@dataclass(frozen=False)
class tenant_license_read_dtos(base_read_dtos):
    dtos: list[tenant_license_read_dto]
    def __init__(self, dtos: list[tenant_license_read_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[tenant_license_read_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: tenant_license_read_dto):
        return cls(list([dto]))
    @classmethod
    def from_lists(cls, dtos1: list[tenant_license_read_dto], dtos2: list[tenant_license_read_dto]):
        return cls(dtos1 + dtos2)
    def get_active(self):
        return tenant_license_read_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return tenant_license_read_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_write_dtos(self) -> list[tenant_license_write_dto]:
        return list(map(lambda x: x.to_write(), self.dtos))
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write().to_write_dict(), self.dtos))
    def get_read_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> tenant_license_read_dto | None:
        found_dtos = list(filter(lambda x: x.tenant_license_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def get_first(self) -> tenant_license_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> tenant_license_read_dtos:
        if len(self.dtos) > n:
            return tenant_license_read_dtos(self.dtos[:n])
        else:
            return tenant_license_read_dtos(self.dtos)
    def get_last(self) -> tenant_license_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, tenant_license_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def to_dict_by_tenant_license_uid(self) -> dict[str, tenant_license_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.tenant_license_uid] = dto
        return d
    def to_dict_by_tenant_license_name(self) -> dict[str, tenant_license_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.tenant_license_name] = dto
        return d
    def to_dict_by_tenant_uid(self) -> dict[str, tenant_license_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.tenant_uid] = dto
        return d
    def to_dict_by_system_license_uid(self) -> dict[str, tenant_license_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.system_license_uid] = dto
        return d
    def to_dict_by_start_date(self) -> dict[str, tenant_license_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.start_date] = dto
        return d
    def to_dict_by_end_date(self) -> dict[str, tenant_license_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.end_date] = dto
        return d
    def to_dict_by_is_approved(self) -> dict[str, tenant_license_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.is_approved] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[tenant_license_read_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[tenant_license_read_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return init
    def check_any(self, check_method: Callable[[tenant_license_read_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return init
    def map_to_string(self, map_method: Callable[[tenant_license_read_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[tenant_license_read_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[tenant_license_read_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, tenant_license_read_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, tenant_license_read_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, tenant_license_read_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[tenant_license_read_dto], bool]) -> tenant_license_read_dtos:
        return tenant_license_read_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[tenant_license_read_dto], str]) -> dict[str, tenant_license_read_dtos]:
        grp_data: dict[str, tenant_license_read_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = tenant_license_read_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[tenant_license_read_dto], str], agg_method: Callable[[tenant_license_read_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, tenant_license_read_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[tenant_license_read_dto], bool]) -> tenant_license_read_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[tenant_license_read_dto], any], compare_method: Callable[[any, any], bool]) -> tenant_license_read_dto | None:
        if len(self.dtos) == 0:
            return None
        else:
            max_value = value_method(self.dtos[0])
            max_elem = self.dtos[0]
            for dto in self.dtos:
                next_value = value_method(dto)
                if compare_method(next_value, max_value):
                    max_value = next_value
                    max_elem = dto
            return max_elem


@dataclass(frozen=False)
class tenant_payment_read_dtos(base_read_dtos):
    dtos: list[tenant_payment_read_dto]
    def __init__(self, dtos: list[tenant_payment_read_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[tenant_payment_read_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: tenant_payment_read_dto):
        return cls(list([dto]))
    @classmethod
    def from_lists(cls, dtos1: list[tenant_payment_read_dto], dtos2: list[tenant_payment_read_dto]):
        return cls(dtos1 + dtos2)
    def get_active(self):
        return tenant_payment_read_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return tenant_payment_read_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_write_dtos(self) -> list[tenant_payment_write_dto]:
        return list(map(lambda x: x.to_write(), self.dtos))
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write().to_write_dict(), self.dtos))
    def get_read_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> tenant_payment_read_dto | None:
        found_dtos = list(filter(lambda x: x.tenant_payment_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def get_first(self) -> tenant_payment_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> tenant_payment_read_dtos:
        if len(self.dtos) > n:
            return tenant_payment_read_dtos(self.dtos[:n])
        else:
            return tenant_payment_read_dtos(self.dtos)
    def get_last(self) -> tenant_payment_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, tenant_payment_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def to_dict_by_tenant_payment_uid(self) -> dict[str, tenant_payment_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.tenant_payment_uid] = dto
        return d
    def to_dict_by_tenant_payment_name(self) -> dict[str, tenant_payment_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.tenant_payment_name] = dto
        return d
    def to_dict_by_tenant_uid(self) -> dict[str, tenant_payment_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.tenant_uid] = dto
        return d
    def to_dict_by_account_uid(self) -> dict[str, tenant_payment_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.account_uid] = dto
        return d
    def to_dict_by_currency_uid(self) -> dict[str, tenant_payment_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.currency_uid] = dto
        return d
    def to_dict_by_tenant_payment_type_uid(self) -> dict[str, tenant_payment_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.tenant_payment_type_uid] = dto
        return d
    def to_dict_by_start_date(self) -> dict[str, tenant_payment_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.start_date] = dto
        return d
    def to_dict_by_end_date(self) -> dict[str, tenant_payment_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.end_date] = dto
        return d
    def to_dict_by_payment_value(self) -> dict[str, tenant_payment_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.payment_value] = dto
        return d
    def to_dict_by_source_number(self) -> dict[str, tenant_payment_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.source_number] = dto
        return d
    def to_dict_by_source_reference(self) -> dict[str, tenant_payment_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.source_reference] = dto
        return d
    def to_dict_by_is_approved(self) -> dict[str, tenant_payment_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.is_approved] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[tenant_payment_read_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[tenant_payment_read_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return init
    def check_any(self, check_method: Callable[[tenant_payment_read_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return init
    def map_to_string(self, map_method: Callable[[tenant_payment_read_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[tenant_payment_read_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[tenant_payment_read_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, tenant_payment_read_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, tenant_payment_read_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, tenant_payment_read_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[tenant_payment_read_dto], bool]) -> tenant_payment_read_dtos:
        return tenant_payment_read_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[tenant_payment_read_dto], str]) -> dict[str, tenant_payment_read_dtos]:
        grp_data: dict[str, tenant_payment_read_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = tenant_payment_read_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[tenant_payment_read_dto], str], agg_method: Callable[[tenant_payment_read_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, tenant_payment_read_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[tenant_payment_read_dto], bool]) -> tenant_payment_read_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[tenant_payment_read_dto], any], compare_method: Callable[[any, any], bool]) -> tenant_payment_read_dto | None:
        if len(self.dtos) == 0:
            return None
        else:
            max_value = value_method(self.dtos[0])
            max_elem = self.dtos[0]
            for dto in self.dtos:
                next_value = value_method(dto)
                if compare_method(next_value, max_value):
                    max_value = next_value
                    max_elem = dto
            return max_elem


@dataclass(frozen=False)
class tenant_payment_type_read_dtos(base_read_dtos):
    dtos: list[tenant_payment_type_read_dto]
    def __init__(self, dtos: list[tenant_payment_type_read_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[tenant_payment_type_read_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: tenant_payment_type_read_dto):
        return cls(list([dto]))
    @classmethod
    def from_lists(cls, dtos1: list[tenant_payment_type_read_dto], dtos2: list[tenant_payment_type_read_dto]):
        return cls(dtos1 + dtos2)
    def get_active(self):
        return tenant_payment_type_read_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return tenant_payment_type_read_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_write_dtos(self) -> list[tenant_payment_type_write_dto]:
        return list(map(lambda x: x.to_write(), self.dtos))
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write().to_write_dict(), self.dtos))
    def get_read_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> tenant_payment_type_read_dto | None:
        found_dtos = list(filter(lambda x: x.tenant_payment_type_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def get_first(self) -> tenant_payment_type_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> tenant_payment_type_read_dtos:
        if len(self.dtos) > n:
            return tenant_payment_type_read_dtos(self.dtos[:n])
        else:
            return tenant_payment_type_read_dtos(self.dtos)
    def get_last(self) -> tenant_payment_type_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, tenant_payment_type_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def to_dict_by_tenant_payment_type_uid(self) -> dict[str, tenant_payment_type_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.tenant_payment_type_uid] = dto
        return d
    def to_dict_by_tenant_payment_type_name(self) -> dict[str, tenant_payment_type_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.tenant_payment_type_name] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[tenant_payment_type_read_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[tenant_payment_type_read_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return init
    def check_any(self, check_method: Callable[[tenant_payment_type_read_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return init
    def map_to_string(self, map_method: Callable[[tenant_payment_type_read_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[tenant_payment_type_read_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[tenant_payment_type_read_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, tenant_payment_type_read_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, tenant_payment_type_read_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, tenant_payment_type_read_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[tenant_payment_type_read_dto], bool]) -> tenant_payment_type_read_dtos:
        return tenant_payment_type_read_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[tenant_payment_type_read_dto], str]) -> dict[str, tenant_payment_type_read_dtos]:
        grp_data: dict[str, tenant_payment_type_read_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = tenant_payment_type_read_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[tenant_payment_type_read_dto], str], agg_method: Callable[[tenant_payment_type_read_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, tenant_payment_type_read_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[tenant_payment_type_read_dto], bool]) -> tenant_payment_type_read_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[tenant_payment_type_read_dto], any], compare_method: Callable[[any, any], bool]) -> tenant_payment_type_read_dto | None:
        if len(self.dtos) == 0:
            return None
        else:
            max_value = value_method(self.dtos[0])
            max_elem = self.dtos[0]
            for dto in self.dtos:
                next_value = value_method(dto)
                if compare_method(next_value, max_value):
                    max_value = next_value
                    max_elem = dto
            return max_elem


@dataclass(frozen=False)
class tenant_role_read_dtos(base_read_dtos):
    dtos: list[tenant_role_read_dto]
    def __init__(self, dtos: list[tenant_role_read_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[tenant_role_read_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: tenant_role_read_dto):
        return cls(list([dto]))
    @classmethod
    def from_lists(cls, dtos1: list[tenant_role_read_dto], dtos2: list[tenant_role_read_dto]):
        return cls(dtos1 + dtos2)
    def get_active(self):
        return tenant_role_read_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return tenant_role_read_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_write_dtos(self) -> list[tenant_role_write_dto]:
        return list(map(lambda x: x.to_write(), self.dtos))
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write().to_write_dict(), self.dtos))
    def get_read_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> tenant_role_read_dto | None:
        found_dtos = list(filter(lambda x: x.tenant_role_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def get_first(self) -> tenant_role_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> tenant_role_read_dtos:
        if len(self.dtos) > n:
            return tenant_role_read_dtos(self.dtos[:n])
        else:
            return tenant_role_read_dtos(self.dtos)
    def get_last(self) -> tenant_role_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, tenant_role_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def to_dict_by_tenant_role_uid(self) -> dict[str, tenant_role_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.tenant_role_uid] = dto
        return d
    def to_dict_by_tenant_role_name(self) -> dict[str, tenant_role_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.tenant_role_name] = dto
        return d
    def to_dict_by_role_description(self) -> dict[str, tenant_role_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.role_description] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[tenant_role_read_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[tenant_role_read_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return init
    def check_any(self, check_method: Callable[[tenant_role_read_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return init
    def map_to_string(self, map_method: Callable[[tenant_role_read_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[tenant_role_read_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[tenant_role_read_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, tenant_role_read_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, tenant_role_read_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, tenant_role_read_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[tenant_role_read_dto], bool]) -> tenant_role_read_dtos:
        return tenant_role_read_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[tenant_role_read_dto], str]) -> dict[str, tenant_role_read_dtos]:
        grp_data: dict[str, tenant_role_read_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = tenant_role_read_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[tenant_role_read_dto], str], agg_method: Callable[[tenant_role_read_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, tenant_role_read_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[tenant_role_read_dto], bool]) -> tenant_role_read_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[tenant_role_read_dto], any], compare_method: Callable[[any, any], bool]) -> tenant_role_read_dto | None:
        if len(self.dtos) == 0:
            return None
        else:
            max_value = value_method(self.dtos[0])
            max_elem = self.dtos[0]
            for dto in self.dtos:
                next_value = value_method(dto)
                if compare_method(next_value, max_value):
                    max_value = next_value
                    max_elem = dto
            return max_elem


@dataclass(frozen=False)
class tenant_status_read_dtos(base_read_dtos):
    dtos: list[tenant_status_read_dto]
    def __init__(self, dtos: list[tenant_status_read_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[tenant_status_read_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: tenant_status_read_dto):
        return cls(list([dto]))
    @classmethod
    def from_lists(cls, dtos1: list[tenant_status_read_dto], dtos2: list[tenant_status_read_dto]):
        return cls(dtos1 + dtos2)
    def get_active(self):
        return tenant_status_read_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return tenant_status_read_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_write_dtos(self) -> list[tenant_status_write_dto]:
        return list(map(lambda x: x.to_write(), self.dtos))
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write().to_write_dict(), self.dtos))
    def get_read_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> tenant_status_read_dto | None:
        found_dtos = list(filter(lambda x: x.tenant_status_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def get_first(self) -> tenant_status_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> tenant_status_read_dtos:
        if len(self.dtos) > n:
            return tenant_status_read_dtos(self.dtos[:n])
        else:
            return tenant_status_read_dtos(self.dtos)
    def get_last(self) -> tenant_status_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, tenant_status_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def to_dict_by_tenant_status_uid(self) -> dict[str, tenant_status_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.tenant_status_uid] = dto
        return d
    def to_dict_by_tenant_status_name(self) -> dict[str, tenant_status_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.tenant_status_name] = dto
        return d
    def to_dict_by_tenant_status_description(self) -> dict[str, tenant_status_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.tenant_status_description] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[tenant_status_read_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[tenant_status_read_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return init
    def check_any(self, check_method: Callable[[tenant_status_read_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return init
    def map_to_string(self, map_method: Callable[[tenant_status_read_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[tenant_status_read_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[tenant_status_read_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, tenant_status_read_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, tenant_status_read_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, tenant_status_read_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[tenant_status_read_dto], bool]) -> tenant_status_read_dtos:
        return tenant_status_read_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[tenant_status_read_dto], str]) -> dict[str, tenant_status_read_dtos]:
        grp_data: dict[str, tenant_status_read_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = tenant_status_read_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[tenant_status_read_dto], str], agg_method: Callable[[tenant_status_read_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, tenant_status_read_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[tenant_status_read_dto], bool]) -> tenant_status_read_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[tenant_status_read_dto], any], compare_method: Callable[[any, any], bool]) -> tenant_status_read_dto | None:
        if len(self.dtos) == 0:
            return None
        else:
            max_value = value_method(self.dtos[0])
            max_elem = self.dtos[0]
            for dto in self.dtos:
                next_value = value_method(dto)
                if compare_method(next_value, max_value):
                    max_value = next_value
                    max_elem = dto
            return max_elem


@dataclass(frozen=False)
class tenant_type_read_dtos(base_read_dtos):
    dtos: list[tenant_type_read_dto]
    def __init__(self, dtos: list[tenant_type_read_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[tenant_type_read_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: tenant_type_read_dto):
        return cls(list([dto]))
    @classmethod
    def from_lists(cls, dtos1: list[tenant_type_read_dto], dtos2: list[tenant_type_read_dto]):
        return cls(dtos1 + dtos2)
    def get_active(self):
        return tenant_type_read_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return tenant_type_read_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_write_dtos(self) -> list[tenant_type_write_dto]:
        return list(map(lambda x: x.to_write(), self.dtos))
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write().to_write_dict(), self.dtos))
    def get_read_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> tenant_type_read_dto | None:
        found_dtos = list(filter(lambda x: x.tenant_type_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def get_first(self) -> tenant_type_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> tenant_type_read_dtos:
        if len(self.dtos) > n:
            return tenant_type_read_dtos(self.dtos[:n])
        else:
            return tenant_type_read_dtos(self.dtos)
    def get_last(self) -> tenant_type_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, tenant_type_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def to_dict_by_tenant_type_uid(self) -> dict[str, tenant_type_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.tenant_type_uid] = dto
        return d
    def to_dict_by_tenant_type_name(self) -> dict[str, tenant_type_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.tenant_type_name] = dto
        return d
    def to_dict_by_tenant_type_description(self) -> dict[str, tenant_type_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.tenant_type_description] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[tenant_type_read_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[tenant_type_read_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return init
    def check_any(self, check_method: Callable[[tenant_type_read_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return init
    def map_to_string(self, map_method: Callable[[tenant_type_read_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[tenant_type_read_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[tenant_type_read_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, tenant_type_read_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, tenant_type_read_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, tenant_type_read_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[tenant_type_read_dto], bool]) -> tenant_type_read_dtos:
        return tenant_type_read_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[tenant_type_read_dto], str]) -> dict[str, tenant_type_read_dtos]:
        grp_data: dict[str, tenant_type_read_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = tenant_type_read_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[tenant_type_read_dto], str], agg_method: Callable[[tenant_type_read_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, tenant_type_read_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[tenant_type_read_dto], bool]) -> tenant_type_read_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[tenant_type_read_dto], any], compare_method: Callable[[any, any], bool]) -> tenant_type_read_dto | None:
        if len(self.dtos) == 0:
            return None
        else:
            max_value = value_method(self.dtos[0])
            max_elem = self.dtos[0]
            for dto in self.dtos:
                next_value = value_method(dto)
                if compare_method(next_value, max_value):
                    max_value = next_value
                    max_elem = dto
            return max_elem


@dataclass(frozen=False)
class time_approval_read_dtos(base_read_dtos):
    dtos: list[time_approval_read_dto]
    def __init__(self, dtos: list[time_approval_read_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[time_approval_read_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: time_approval_read_dto):
        return cls(list([dto]))
    @classmethod
    def from_lists(cls, dtos1: list[time_approval_read_dto], dtos2: list[time_approval_read_dto]):
        return cls(dtos1 + dtos2)
    def get_active(self):
        return time_approval_read_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return time_approval_read_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_write_dtos(self) -> list[time_approval_write_dto]:
        return list(map(lambda x: x.to_write(), self.dtos))
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write().to_write_dict(), self.dtos))
    def get_read_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> time_approval_read_dto | None:
        found_dtos = list(filter(lambda x: x.time_approval_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def get_first(self) -> time_approval_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> time_approval_read_dtos:
        if len(self.dtos) > n:
            return time_approval_read_dtos(self.dtos[:n])
        else:
            return time_approval_read_dtos(self.dtos)
    def get_last(self) -> time_approval_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, time_approval_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def to_dict_by_time_approval_uid(self) -> dict[str, time_approval_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.time_approval_uid] = dto
        return d
    def to_dict_by_time_approval_name(self) -> dict[str, time_approval_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.time_approval_name] = dto
        return d
    def to_dict_by_tenant_uid(self) -> dict[str, time_approval_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.tenant_uid] = dto
        return d
    def to_dict_by_account_uid(self) -> dict[str, time_approval_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.account_uid] = dto
        return d
    def to_dict_by_time_entry_uid(self) -> dict[str, time_approval_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.time_entry_uid] = dto
        return d
    def to_dict_by_approval_comment(self) -> dict[str, time_approval_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.approval_comment] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[time_approval_read_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[time_approval_read_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return init
    def check_any(self, check_method: Callable[[time_approval_read_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return init
    def map_to_string(self, map_method: Callable[[time_approval_read_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[time_approval_read_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[time_approval_read_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, time_approval_read_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, time_approval_read_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, time_approval_read_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[time_approval_read_dto], bool]) -> time_approval_read_dtos:
        return time_approval_read_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[time_approval_read_dto], str]) -> dict[str, time_approval_read_dtos]:
        grp_data: dict[str, time_approval_read_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = time_approval_read_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[time_approval_read_dto], str], agg_method: Callable[[time_approval_read_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, time_approval_read_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[time_approval_read_dto], bool]) -> time_approval_read_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[time_approval_read_dto], any], compare_method: Callable[[any, any], bool]) -> time_approval_read_dto | None:
        if len(self.dtos) == 0:
            return None
        else:
            max_value = value_method(self.dtos[0])
            max_elem = self.dtos[0]
            for dto in self.dtos:
                next_value = value_method(dto)
                if compare_method(next_value, max_value):
                    max_value = next_value
                    max_elem = dto
            return max_elem


@dataclass(frozen=False)
class time_entry_read_dtos(base_read_dtos):
    dtos: list[time_entry_read_dto]
    def __init__(self, dtos: list[time_entry_read_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[time_entry_read_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: time_entry_read_dto):
        return cls(list([dto]))
    @classmethod
    def from_lists(cls, dtos1: list[time_entry_read_dto], dtos2: list[time_entry_read_dto]):
        return cls(dtos1 + dtos2)
    def get_active(self):
        return time_entry_read_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return time_entry_read_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_write_dtos(self) -> list[time_entry_write_dto]:
        return list(map(lambda x: x.to_write(), self.dtos))
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write().to_write_dict(), self.dtos))
    def get_read_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> time_entry_read_dto | None:
        found_dtos = list(filter(lambda x: x.time_entry_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def get_first(self) -> time_entry_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> time_entry_read_dtos:
        if len(self.dtos) > n:
            return time_entry_read_dtos(self.dtos[:n])
        else:
            return time_entry_read_dtos(self.dtos)
    def get_last(self) -> time_entry_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, time_entry_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def to_dict_by_time_entry_uid(self) -> dict[str, time_entry_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.time_entry_uid] = dto
        return d
    def to_dict_by_time_entry_name(self) -> dict[str, time_entry_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.time_entry_name] = dto
        return d
    def to_dict_by_time_submit_uid(self) -> dict[str, time_entry_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.time_submit_uid] = dto
        return d
    def to_dict_by_tenant_uid(self) -> dict[str, time_entry_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.tenant_uid] = dto
        return d
    def to_dict_by_account_uid(self) -> dict[str, time_entry_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.account_uid] = dto
        return d
    def to_dict_by_project_instance_uid(self) -> dict[str, time_entry_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.project_instance_uid] = dto
        return d
    def to_dict_by_project_milestone_uid(self) -> dict[str, time_entry_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.project_milestone_uid] = dto
        return d
    def to_dict_by_period_uid(self) -> dict[str, time_entry_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.period_uid] = dto
        return d
    def to_dict_by_invoice_instance_uid(self) -> dict[str, time_entry_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.invoice_instance_uid] = dto
        return d
    def to_dict_by_entry_period(self) -> dict[str, time_entry_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.entry_period] = dto
        return d
    def to_dict_by_entry_note(self) -> dict[str, time_entry_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.entry_note] = dto
        return d
    def to_dict_by_lock_row(self) -> dict[str, time_entry_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.lock_row] = dto
        return d
    def to_dict_by_start_date(self) -> dict[str, time_entry_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.start_date] = dto
        return d
    def to_dict_by_end_date(self) -> dict[str, time_entry_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.end_date] = dto
        return d
    def to_dict_by_entry_minutes(self) -> dict[str, time_entry_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.entry_minutes] = dto
        return d
    def to_dict_by_is_approved(self) -> dict[str, time_entry_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.is_approved] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[time_entry_read_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[time_entry_read_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return init
    def check_any(self, check_method: Callable[[time_entry_read_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return init
    def map_to_string(self, map_method: Callable[[time_entry_read_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[time_entry_read_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[time_entry_read_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, time_entry_read_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, time_entry_read_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, time_entry_read_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[time_entry_read_dto], bool]) -> time_entry_read_dtos:
        return time_entry_read_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[time_entry_read_dto], str]) -> dict[str, time_entry_read_dtos]:
        grp_data: dict[str, time_entry_read_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = time_entry_read_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[time_entry_read_dto], str], agg_method: Callable[[time_entry_read_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, time_entry_read_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[time_entry_read_dto], bool]) -> time_entry_read_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[time_entry_read_dto], any], compare_method: Callable[[any, any], bool]) -> time_entry_read_dto | None:
        if len(self.dtos) == 0:
            return None
        else:
            max_value = value_method(self.dtos[0])
            max_elem = self.dtos[0]
            for dto in self.dtos:
                next_value = value_method(dto)
                if compare_method(next_value, max_value):
                    max_value = next_value
                    max_elem = dto
            return max_elem


@dataclass(frozen=False)
class time_entry_final_read_dtos(base_read_dtos):
    dtos: list[time_entry_final_read_dto]
    def __init__(self, dtos: list[time_entry_final_read_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[time_entry_final_read_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: time_entry_final_read_dto):
        return cls(list([dto]))
    @classmethod
    def from_lists(cls, dtos1: list[time_entry_final_read_dto], dtos2: list[time_entry_final_read_dto]):
        return cls(dtos1 + dtos2)
    def get_active(self):
        return time_entry_final_read_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return time_entry_final_read_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_write_dtos(self) -> list[time_entry_final_write_dto]:
        return list(map(lambda x: x.to_write(), self.dtos))
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write().to_write_dict(), self.dtos))
    def get_read_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> time_entry_final_read_dto | None:
        found_dtos = list(filter(lambda x: x.time_entry_final_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def get_first(self) -> time_entry_final_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> time_entry_final_read_dtos:
        if len(self.dtos) > n:
            return time_entry_final_read_dtos(self.dtos[:n])
        else:
            return time_entry_final_read_dtos(self.dtos)
    def get_last(self) -> time_entry_final_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, time_entry_final_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def to_dict_by_time_entry_final_uid(self) -> dict[str, time_entry_final_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.time_entry_final_uid] = dto
        return d
    def to_dict_by_time_entry_final_name(self) -> dict[str, time_entry_final_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.time_entry_final_name] = dto
        return d
    def to_dict_by_tenant_uid(self) -> dict[str, time_entry_final_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.tenant_uid] = dto
        return d
    def to_dict_by_account_uid(self) -> dict[str, time_entry_final_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.account_uid] = dto
        return d
    def to_dict_by_project_instance_uid(self) -> dict[str, time_entry_final_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.project_instance_uid] = dto
        return d
    def to_dict_by_project_milestone_uid(self) -> dict[str, time_entry_final_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.project_milestone_uid] = dto
        return d
    def to_dict_by_invoice_instance_uid(self) -> dict[str, time_entry_final_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.invoice_instance_uid] = dto
        return d
    def to_dict_by_entry_period(self) -> dict[str, time_entry_final_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.entry_period] = dto
        return d
    def to_dict_by_entry_note(self) -> dict[str, time_entry_final_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.entry_note] = dto
        return d
    def to_dict_by_lock_uid(self) -> dict[str, time_entry_final_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.lock_uid] = dto
        return d
    def to_dict_by_start_date(self) -> dict[str, time_entry_final_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.start_date] = dto
        return d
    def to_dict_by_end_date(self) -> dict[str, time_entry_final_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.end_date] = dto
        return d
    def to_dict_by_entry_minutes(self) -> dict[str, time_entry_final_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.entry_minutes] = dto
        return d
    def to_dict_by_is_approved(self) -> dict[str, time_entry_final_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.is_approved] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[time_entry_final_read_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[time_entry_final_read_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return init
    def check_any(self, check_method: Callable[[time_entry_final_read_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return init
    def map_to_string(self, map_method: Callable[[time_entry_final_read_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[time_entry_final_read_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[time_entry_final_read_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, time_entry_final_read_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, time_entry_final_read_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, time_entry_final_read_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[time_entry_final_read_dto], bool]) -> time_entry_final_read_dtos:
        return time_entry_final_read_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[time_entry_final_read_dto], str]) -> dict[str, time_entry_final_read_dtos]:
        grp_data: dict[str, time_entry_final_read_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = time_entry_final_read_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[time_entry_final_read_dto], str], agg_method: Callable[[time_entry_final_read_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, time_entry_final_read_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[time_entry_final_read_dto], bool]) -> time_entry_final_read_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[time_entry_final_read_dto], any], compare_method: Callable[[any, any], bool]) -> time_entry_final_read_dto | None:
        if len(self.dtos) == 0:
            return None
        else:
            max_value = value_method(self.dtos[0])
            max_elem = self.dtos[0]
            for dto in self.dtos:
                next_value = value_method(dto)
                if compare_method(next_value, max_value):
                    max_value = next_value
                    max_elem = dto
            return max_elem


@dataclass(frozen=False)
class time_entry_invoice_read_dtos(base_read_dtos):
    dtos: list[time_entry_invoice_read_dto]
    def __init__(self, dtos: list[time_entry_invoice_read_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[time_entry_invoice_read_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: time_entry_invoice_read_dto):
        return cls(list([dto]))
    @classmethod
    def from_lists(cls, dtos1: list[time_entry_invoice_read_dto], dtos2: list[time_entry_invoice_read_dto]):
        return cls(dtos1 + dtos2)
    def get_active(self):
        return time_entry_invoice_read_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return time_entry_invoice_read_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_write_dtos(self) -> list[time_entry_invoice_write_dto]:
        return list(map(lambda x: x.to_write(), self.dtos))
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write().to_write_dict(), self.dtos))
    def get_read_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> time_entry_invoice_read_dto | None:
        found_dtos = list(filter(lambda x: x.time_entry_invoice_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def get_first(self) -> time_entry_invoice_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> time_entry_invoice_read_dtos:
        if len(self.dtos) > n:
            return time_entry_invoice_read_dtos(self.dtos[:n])
        else:
            return time_entry_invoice_read_dtos(self.dtos)
    def get_last(self) -> time_entry_invoice_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, time_entry_invoice_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def to_dict_by_time_entry_invoice_uid(self) -> dict[str, time_entry_invoice_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.time_entry_invoice_uid] = dto
        return d
    def to_dict_by_time_entry_invoice_name(self) -> dict[str, time_entry_invoice_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.time_entry_invoice_name] = dto
        return d
    def to_dict_by_tenant_uid(self) -> dict[str, time_entry_invoice_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.tenant_uid] = dto
        return d
    def to_dict_by_account_uid(self) -> dict[str, time_entry_invoice_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.account_uid] = dto
        return d
    def to_dict_by_time_submit_uid(self) -> dict[str, time_entry_invoice_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.time_submit_uid] = dto
        return d
    def to_dict_by_time_entry_uid(self) -> dict[str, time_entry_invoice_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.time_entry_uid] = dto
        return d
    def to_dict_by_project_instance_uid(self) -> dict[str, time_entry_invoice_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.project_instance_uid] = dto
        return d
    def to_dict_by_project_milestone_uid(self) -> dict[str, time_entry_invoice_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.project_milestone_uid] = dto
        return d
    def to_dict_by_period_uid(self) -> dict[str, time_entry_invoice_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.period_uid] = dto
        return d
    def to_dict_by_invoice_instance_uid(self) -> dict[str, time_entry_invoice_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.invoice_instance_uid] = dto
        return d
    def to_dict_by_entry_period(self) -> dict[str, time_entry_invoice_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.entry_period] = dto
        return d
    def to_dict_by_entry_note(self) -> dict[str, time_entry_invoice_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.entry_note] = dto
        return d
    def to_dict_by_lock_row(self) -> dict[str, time_entry_invoice_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.lock_row] = dto
        return d
    def to_dict_by_start_date(self) -> dict[str, time_entry_invoice_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.start_date] = dto
        return d
    def to_dict_by_end_date(self) -> dict[str, time_entry_invoice_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.end_date] = dto
        return d
    def to_dict_by_entry_minutes(self) -> dict[str, time_entry_invoice_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.entry_minutes] = dto
        return d
    def to_dict_by_is_approved(self) -> dict[str, time_entry_invoice_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.is_approved] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[time_entry_invoice_read_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[time_entry_invoice_read_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return init
    def check_any(self, check_method: Callable[[time_entry_invoice_read_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return init
    def map_to_string(self, map_method: Callable[[time_entry_invoice_read_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[time_entry_invoice_read_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[time_entry_invoice_read_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, time_entry_invoice_read_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, time_entry_invoice_read_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, time_entry_invoice_read_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[time_entry_invoice_read_dto], bool]) -> time_entry_invoice_read_dtos:
        return time_entry_invoice_read_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[time_entry_invoice_read_dto], str]) -> dict[str, time_entry_invoice_read_dtos]:
        grp_data: dict[str, time_entry_invoice_read_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = time_entry_invoice_read_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[time_entry_invoice_read_dto], str], agg_method: Callable[[time_entry_invoice_read_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, time_entry_invoice_read_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[time_entry_invoice_read_dto], bool]) -> time_entry_invoice_read_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[time_entry_invoice_read_dto], any], compare_method: Callable[[any, any], bool]) -> time_entry_invoice_read_dto | None:
        if len(self.dtos) == 0:
            return None
        else:
            max_value = value_method(self.dtos[0])
            max_elem = self.dtos[0]
            for dto in self.dtos:
                next_value = value_method(dto)
                if compare_method(next_value, max_value):
                    max_value = next_value
                    max_elem = dto
            return max_elem


@dataclass(frozen=False)
class time_rule_read_dtos(base_read_dtos):
    dtos: list[time_rule_read_dto]
    def __init__(self, dtos: list[time_rule_read_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[time_rule_read_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: time_rule_read_dto):
        return cls(list([dto]))
    @classmethod
    def from_lists(cls, dtos1: list[time_rule_read_dto], dtos2: list[time_rule_read_dto]):
        return cls(dtos1 + dtos2)
    def get_active(self):
        return time_rule_read_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return time_rule_read_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_write_dtos(self) -> list[time_rule_write_dto]:
        return list(map(lambda x: x.to_write(), self.dtos))
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write().to_write_dict(), self.dtos))
    def get_read_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> time_rule_read_dto | None:
        found_dtos = list(filter(lambda x: x.time_rule_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def get_first(self) -> time_rule_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> time_rule_read_dtos:
        if len(self.dtos) > n:
            return time_rule_read_dtos(self.dtos[:n])
        else:
            return time_rule_read_dtos(self.dtos)
    def get_last(self) -> time_rule_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, time_rule_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def to_dict_by_time_rule_uid(self) -> dict[str, time_rule_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.time_rule_uid] = dto
        return d
    def to_dict_by_time_rule_name(self) -> dict[str, time_rule_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.time_rule_name] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[time_rule_read_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[time_rule_read_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return init
    def check_any(self, check_method: Callable[[time_rule_read_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return init
    def map_to_string(self, map_method: Callable[[time_rule_read_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[time_rule_read_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[time_rule_read_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, time_rule_read_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, time_rule_read_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, time_rule_read_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[time_rule_read_dto], bool]) -> time_rule_read_dtos:
        return time_rule_read_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[time_rule_read_dto], str]) -> dict[str, time_rule_read_dtos]:
        grp_data: dict[str, time_rule_read_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = time_rule_read_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[time_rule_read_dto], str], agg_method: Callable[[time_rule_read_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, time_rule_read_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[time_rule_read_dto], bool]) -> time_rule_read_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[time_rule_read_dto], any], compare_method: Callable[[any, any], bool]) -> time_rule_read_dto | None:
        if len(self.dtos) == 0:
            return None
        else:
            max_value = value_method(self.dtos[0])
            max_elem = self.dtos[0]
            for dto in self.dtos:
                next_value = value_method(dto)
                if compare_method(next_value, max_value):
                    max_value = next_value
                    max_elem = dto
            return max_elem


@dataclass(frozen=False)
class time_rule_client_read_dtos(base_read_dtos):
    dtos: list[time_rule_client_read_dto]
    def __init__(self, dtos: list[time_rule_client_read_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[time_rule_client_read_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: time_rule_client_read_dto):
        return cls(list([dto]))
    @classmethod
    def from_lists(cls, dtos1: list[time_rule_client_read_dto], dtos2: list[time_rule_client_read_dto]):
        return cls(dtos1 + dtos2)
    def get_active(self):
        return time_rule_client_read_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return time_rule_client_read_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_write_dtos(self) -> list[time_rule_client_write_dto]:
        return list(map(lambda x: x.to_write(), self.dtos))
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write().to_write_dict(), self.dtos))
    def get_read_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> time_rule_client_read_dto | None:
        found_dtos = list(filter(lambda x: x.time_rule_client_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def get_first(self) -> time_rule_client_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> time_rule_client_read_dtos:
        if len(self.dtos) > n:
            return time_rule_client_read_dtos(self.dtos[:n])
        else:
            return time_rule_client_read_dtos(self.dtos)
    def get_last(self) -> time_rule_client_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, time_rule_client_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def to_dict_by_time_rule_client_uid(self) -> dict[str, time_rule_client_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.time_rule_client_uid] = dto
        return d
    def to_dict_by_time_rule_client_name(self) -> dict[str, time_rule_client_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.time_rule_client_name] = dto
        return d
    def to_dict_by_time_rule_definition(self) -> dict[str, time_rule_client_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.time_rule_definition] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[time_rule_client_read_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[time_rule_client_read_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return init
    def check_any(self, check_method: Callable[[time_rule_client_read_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return init
    def map_to_string(self, map_method: Callable[[time_rule_client_read_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[time_rule_client_read_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[time_rule_client_read_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, time_rule_client_read_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, time_rule_client_read_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, time_rule_client_read_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[time_rule_client_read_dto], bool]) -> time_rule_client_read_dtos:
        return time_rule_client_read_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[time_rule_client_read_dto], str]) -> dict[str, time_rule_client_read_dtos]:
        grp_data: dict[str, time_rule_client_read_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = time_rule_client_read_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[time_rule_client_read_dto], str], agg_method: Callable[[time_rule_client_read_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, time_rule_client_read_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[time_rule_client_read_dto], bool]) -> time_rule_client_read_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[time_rule_client_read_dto], any], compare_method: Callable[[any, any], bool]) -> time_rule_client_read_dto | None:
        if len(self.dtos) == 0:
            return None
        else:
            max_value = value_method(self.dtos[0])
            max_elem = self.dtos[0]
            for dto in self.dtos:
                next_value = value_method(dto)
                if compare_method(next_value, max_value):
                    max_value = next_value
                    max_elem = dto
            return max_elem


@dataclass(frozen=False)
class time_submit_read_dtos(base_read_dtos):
    dtos: list[time_submit_read_dto]
    def __init__(self, dtos: list[time_submit_read_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[time_submit_read_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: time_submit_read_dto):
        return cls(list([dto]))
    @classmethod
    def from_lists(cls, dtos1: list[time_submit_read_dto], dtos2: list[time_submit_read_dto]):
        return cls(dtos1 + dtos2)
    def get_active(self):
        return time_submit_read_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return time_submit_read_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_write_dtos(self) -> list[time_submit_write_dto]:
        return list(map(lambda x: x.to_write(), self.dtos))
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write().to_write_dict(), self.dtos))
    def get_read_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> time_submit_read_dto | None:
        found_dtos = list(filter(lambda x: x.time_submit_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def get_first(self) -> time_submit_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> time_submit_read_dtos:
        if len(self.dtos) > n:
            return time_submit_read_dtos(self.dtos[:n])
        else:
            return time_submit_read_dtos(self.dtos)
    def get_last(self) -> time_submit_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, time_submit_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def to_dict_by_time_submit_uid(self) -> dict[str, time_submit_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.time_submit_uid] = dto
        return d
    def to_dict_by_time_submit_name(self) -> dict[str, time_submit_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.time_submit_name] = dto
        return d
    def to_dict_by_tenant_uid(self) -> dict[str, time_submit_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.tenant_uid] = dto
        return d
    def to_dict_by_account_uid(self) -> dict[str, time_submit_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.account_uid] = dto
        return d
    def to_dict_by_period_uid(self) -> dict[str, time_submit_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.period_uid] = dto
        return d
    def to_dict_by_time_submit_description(self) -> dict[str, time_submit_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.time_submit_description] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[time_submit_read_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[time_submit_read_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return init
    def check_any(self, check_method: Callable[[time_submit_read_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return init
    def map_to_string(self, map_method: Callable[[time_submit_read_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[time_submit_read_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[time_submit_read_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, time_submit_read_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, time_submit_read_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, time_submit_read_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[time_submit_read_dto], bool]) -> time_submit_read_dtos:
        return time_submit_read_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[time_submit_read_dto], str]) -> dict[str, time_submit_read_dtos]:
        grp_data: dict[str, time_submit_read_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = time_submit_read_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[time_submit_read_dto], str], agg_method: Callable[[time_submit_read_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, time_submit_read_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[time_submit_read_dto], bool]) -> time_submit_read_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[time_submit_read_dto], any], compare_method: Callable[[any, any], bool]) -> time_submit_read_dto | None:
        if len(self.dtos) == 0:
            return None
        else:
            max_value = value_method(self.dtos[0])
            max_elem = self.dtos[0]
            for dto in self.dtos:
                next_value = value_method(dto)
                if compare_method(next_value, max_value):
                    max_value = next_value
                    max_elem = dto
            return max_elem


@dataclass(frozen=False)
class time_submit_type_read_dtos(base_read_dtos):
    dtos: list[time_submit_type_read_dto]
    def __init__(self, dtos: list[time_submit_type_read_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[time_submit_type_read_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: time_submit_type_read_dto):
        return cls(list([dto]))
    @classmethod
    def from_lists(cls, dtos1: list[time_submit_type_read_dto], dtos2: list[time_submit_type_read_dto]):
        return cls(dtos1 + dtos2)
    def get_active(self):
        return time_submit_type_read_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return time_submit_type_read_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_write_dtos(self) -> list[time_submit_type_write_dto]:
        return list(map(lambda x: x.to_write(), self.dtos))
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write().to_write_dict(), self.dtos))
    def get_read_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> time_submit_type_read_dto | None:
        found_dtos = list(filter(lambda x: x.time_submit_type_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def get_first(self) -> time_submit_type_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> time_submit_type_read_dtos:
        if len(self.dtos) > n:
            return time_submit_type_read_dtos(self.dtos[:n])
        else:
            return time_submit_type_read_dtos(self.dtos)
    def get_last(self) -> time_submit_type_read_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, time_submit_type_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def to_dict_by_time_submit_type_uid(self) -> dict[str, time_submit_type_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.time_submit_type_uid] = dto
        return d
    def to_dict_by_time_submit_type_name(self) -> dict[str, time_submit_type_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.time_submit_type_name] = dto
        return d
    def to_dict_by_time_submit_type_description(self) -> dict[str, time_submit_type_read_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.time_submit_type_description] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[time_submit_type_read_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[time_submit_type_read_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return init
    def check_any(self, check_method: Callable[[time_submit_type_read_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return init
    def map_to_string(self, map_method: Callable[[time_submit_type_read_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[time_submit_type_read_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[time_submit_type_read_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, time_submit_type_read_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, time_submit_type_read_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, time_submit_type_read_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[time_submit_type_read_dto], bool]) -> time_submit_type_read_dtos:
        return time_submit_type_read_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[time_submit_type_read_dto], str]) -> dict[str, time_submit_type_read_dtos]:
        grp_data: dict[str, time_submit_type_read_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = time_submit_type_read_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[time_submit_type_read_dto], str], agg_method: Callable[[time_submit_type_read_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, time_submit_type_read_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[time_submit_type_read_dto], bool]) -> time_submit_type_read_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[time_submit_type_read_dto], any], compare_method: Callable[[any, any], bool]) -> time_submit_type_read_dto | None:
        if len(self.dtos) == 0:
            return None
        else:
            max_value = value_method(self.dtos[0])
            max_elem = self.dtos[0]
            for dto in self.dtos:
                next_value = value_method(dto)
                if compare_method(next_value, max_value):
                    max_value = next_value
                    max_elem = dto
            return max_elem


# auto-generated - v_definition_python_dtos_read_list - END