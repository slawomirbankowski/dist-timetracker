# auto-generated - v_definition_python_dtos_write_list - START at 2024-08-04 09:36:01.623698+00
from __future__ import annotations
from datetime import datetime
from abc import abstractmethod
from dataclasses import dataclass
from dto.dtos import *
from dto.dtos_thin import *
from dto.dtos_write import *
from dto.dtos_read import *
import datetime

from typing import Dict, Callable

@dataclass(frozen=False)
class account_write_dtos(base_write_dtos):
    dtos: list[account_write_dto]
    def __init__(self, dtos: list[account_write_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[account_write_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: account_write_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[account_write_dto], dtos2: list[account_write_dto]):
        return cls(dtos1 + dtos2)
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> account_write_dto | None:
        found_dtos = list(filter(lambda x: x.account_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, account_write_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.account_uid] = dto
        return res
    def get_active(self):
        return account_write_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return account_write_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_first(self) -> account_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> account_write_dtos:
        if len(self.dtos) > n:
            return account_write_dtos(self.dtos[:n])
        else:
            return account_write_dtos(self.dtos)
    def get_last(self) -> account_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, account_write_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[account_write_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[account_write_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def check_any(self, check_method: Callable[[account_write_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[account_write_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[account_write_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[account_write_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, account_write_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, account_write_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, account_write_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[account_write_dto], bool]) -> account_write_dtos:
        return account_write_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[account_write_dto], str]) -> dict[str, account_write_dtos]:
        grp_data: dict[str, account_write_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = account_write_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[account_write_dto], str], agg_method: Callable[[account_write_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, account_write_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[account_write_dto], bool]) -> account_write_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[account_write_dto], any], compare_method: Callable[[any, any], bool]) -> account_write_dto | None:
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
class account_division_write_dtos(base_write_dtos):
    dtos: list[account_division_write_dto]
    def __init__(self, dtos: list[account_division_write_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[account_division_write_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: account_division_write_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[account_division_write_dto], dtos2: list[account_division_write_dto]):
        return cls(dtos1 + dtos2)
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> account_division_write_dto | None:
        found_dtos = list(filter(lambda x: x.account_division_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, account_division_write_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.account_division_uid] = dto
        return res
    def get_active(self):
        return account_division_write_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return account_division_write_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_first(self) -> account_division_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> account_division_write_dtos:
        if len(self.dtos) > n:
            return account_division_write_dtos(self.dtos[:n])
        else:
            return account_division_write_dtos(self.dtos)
    def get_last(self) -> account_division_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, account_division_write_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[account_division_write_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[account_division_write_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def check_any(self, check_method: Callable[[account_division_write_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[account_division_write_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[account_division_write_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[account_division_write_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, account_division_write_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, account_division_write_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, account_division_write_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[account_division_write_dto], bool]) -> account_division_write_dtos:
        return account_division_write_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[account_division_write_dto], str]) -> dict[str, account_division_write_dtos]:
        grp_data: dict[str, account_division_write_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = account_division_write_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[account_division_write_dto], str], agg_method: Callable[[account_division_write_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, account_division_write_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[account_division_write_dto], bool]) -> account_division_write_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[account_division_write_dto], any], compare_method: Callable[[any, any], bool]) -> account_division_write_dto | None:
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
class account_division_template_write_dtos(base_write_dtos):
    dtos: list[account_division_template_write_dto]
    def __init__(self, dtos: list[account_division_template_write_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[account_division_template_write_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: account_division_template_write_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[account_division_template_write_dto], dtos2: list[account_division_template_write_dto]):
        return cls(dtos1 + dtos2)
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> account_division_template_write_dto | None:
        found_dtos = list(filter(lambda x: x.account_division_template_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, account_division_template_write_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.account_division_template_uid] = dto
        return res
    def get_active(self):
        return account_division_template_write_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return account_division_template_write_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_first(self) -> account_division_template_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> account_division_template_write_dtos:
        if len(self.dtos) > n:
            return account_division_template_write_dtos(self.dtos[:n])
        else:
            return account_division_template_write_dtos(self.dtos)
    def get_last(self) -> account_division_template_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, account_division_template_write_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[account_division_template_write_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[account_division_template_write_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def check_any(self, check_method: Callable[[account_division_template_write_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[account_division_template_write_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[account_division_template_write_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[account_division_template_write_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, account_division_template_write_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, account_division_template_write_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, account_division_template_write_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[account_division_template_write_dto], bool]) -> account_division_template_write_dtos:
        return account_division_template_write_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[account_division_template_write_dto], str]) -> dict[str, account_division_template_write_dtos]:
        grp_data: dict[str, account_division_template_write_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = account_division_template_write_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[account_division_template_write_dto], str], agg_method: Callable[[account_division_template_write_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, account_division_template_write_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[account_division_template_write_dto], bool]) -> account_division_template_write_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[account_division_template_write_dto], any], compare_method: Callable[[any, any], bool]) -> account_division_template_write_dto | None:
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
class account_group_write_dtos(base_write_dtos):
    dtos: list[account_group_write_dto]
    def __init__(self, dtos: list[account_group_write_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[account_group_write_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: account_group_write_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[account_group_write_dto], dtos2: list[account_group_write_dto]):
        return cls(dtos1 + dtos2)
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> account_group_write_dto | None:
        found_dtos = list(filter(lambda x: x.account_group_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, account_group_write_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.account_group_uid] = dto
        return res
    def get_active(self):
        return account_group_write_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return account_group_write_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_first(self) -> account_group_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> account_group_write_dtos:
        if len(self.dtos) > n:
            return account_group_write_dtos(self.dtos[:n])
        else:
            return account_group_write_dtos(self.dtos)
    def get_last(self) -> account_group_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, account_group_write_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[account_group_write_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[account_group_write_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def check_any(self, check_method: Callable[[account_group_write_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[account_group_write_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[account_group_write_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[account_group_write_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, account_group_write_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, account_group_write_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, account_group_write_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[account_group_write_dto], bool]) -> account_group_write_dtos:
        return account_group_write_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[account_group_write_dto], str]) -> dict[str, account_group_write_dtos]:
        grp_data: dict[str, account_group_write_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = account_group_write_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[account_group_write_dto], str], agg_method: Callable[[account_group_write_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, account_group_write_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[account_group_write_dto], bool]) -> account_group_write_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[account_group_write_dto], any], compare_method: Callable[[any, any], bool]) -> account_group_write_dto | None:
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
class account_group_assignment_write_dtos(base_write_dtos):
    dtos: list[account_group_assignment_write_dto]
    def __init__(self, dtos: list[account_group_assignment_write_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[account_group_assignment_write_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: account_group_assignment_write_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[account_group_assignment_write_dto], dtos2: list[account_group_assignment_write_dto]):
        return cls(dtos1 + dtos2)
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> account_group_assignment_write_dto | None:
        found_dtos = list(filter(lambda x: x.account_group_assignment_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, account_group_assignment_write_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.account_group_assignment_uid] = dto
        return res
    def get_active(self):
        return account_group_assignment_write_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return account_group_assignment_write_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_first(self) -> account_group_assignment_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> account_group_assignment_write_dtos:
        if len(self.dtos) > n:
            return account_group_assignment_write_dtos(self.dtos[:n])
        else:
            return account_group_assignment_write_dtos(self.dtos)
    def get_last(self) -> account_group_assignment_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, account_group_assignment_write_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[account_group_assignment_write_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[account_group_assignment_write_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def check_any(self, check_method: Callable[[account_group_assignment_write_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[account_group_assignment_write_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[account_group_assignment_write_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[account_group_assignment_write_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, account_group_assignment_write_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, account_group_assignment_write_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, account_group_assignment_write_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[account_group_assignment_write_dto], bool]) -> account_group_assignment_write_dtos:
        return account_group_assignment_write_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[account_group_assignment_write_dto], str]) -> dict[str, account_group_assignment_write_dtos]:
        grp_data: dict[str, account_group_assignment_write_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = account_group_assignment_write_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[account_group_assignment_write_dto], str], agg_method: Callable[[account_group_assignment_write_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, account_group_assignment_write_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[account_group_assignment_write_dto], bool]) -> account_group_assignment_write_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[account_group_assignment_write_dto], any], compare_method: Callable[[any, any], bool]) -> account_group_assignment_write_dto | None:
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
class account_group_role_write_dtos(base_write_dtos):
    dtos: list[account_group_role_write_dto]
    def __init__(self, dtos: list[account_group_role_write_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[account_group_role_write_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: account_group_role_write_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[account_group_role_write_dto], dtos2: list[account_group_role_write_dto]):
        return cls(dtos1 + dtos2)
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> account_group_role_write_dto | None:
        found_dtos = list(filter(lambda x: x.account_group_role_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, account_group_role_write_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.account_group_role_uid] = dto
        return res
    def get_active(self):
        return account_group_role_write_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return account_group_role_write_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_first(self) -> account_group_role_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> account_group_role_write_dtos:
        if len(self.dtos) > n:
            return account_group_role_write_dtos(self.dtos[:n])
        else:
            return account_group_role_write_dtos(self.dtos)
    def get_last(self) -> account_group_role_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, account_group_role_write_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[account_group_role_write_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[account_group_role_write_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def check_any(self, check_method: Callable[[account_group_role_write_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[account_group_role_write_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[account_group_role_write_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[account_group_role_write_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, account_group_role_write_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, account_group_role_write_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, account_group_role_write_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[account_group_role_write_dto], bool]) -> account_group_role_write_dtos:
        return account_group_role_write_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[account_group_role_write_dto], str]) -> dict[str, account_group_role_write_dtos]:
        grp_data: dict[str, account_group_role_write_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = account_group_role_write_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[account_group_role_write_dto], str], agg_method: Callable[[account_group_role_write_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, account_group_role_write_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[account_group_role_write_dto], bool]) -> account_group_role_write_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[account_group_role_write_dto], any], compare_method: Callable[[any, any], bool]) -> account_group_role_write_dto | None:
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
class account_hierarchy_write_dtos(base_write_dtos):
    dtos: list[account_hierarchy_write_dto]
    def __init__(self, dtos: list[account_hierarchy_write_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[account_hierarchy_write_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: account_hierarchy_write_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[account_hierarchy_write_dto], dtos2: list[account_hierarchy_write_dto]):
        return cls(dtos1 + dtos2)
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> account_hierarchy_write_dto | None:
        found_dtos = list(filter(lambda x: x.account_hierarchy_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, account_hierarchy_write_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.account_hierarchy_uid] = dto
        return res
    def get_active(self):
        return account_hierarchy_write_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return account_hierarchy_write_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_first(self) -> account_hierarchy_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> account_hierarchy_write_dtos:
        if len(self.dtos) > n:
            return account_hierarchy_write_dtos(self.dtos[:n])
        else:
            return account_hierarchy_write_dtos(self.dtos)
    def get_last(self) -> account_hierarchy_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, account_hierarchy_write_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[account_hierarchy_write_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[account_hierarchy_write_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def check_any(self, check_method: Callable[[account_hierarchy_write_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[account_hierarchy_write_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[account_hierarchy_write_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[account_hierarchy_write_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, account_hierarchy_write_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, account_hierarchy_write_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, account_hierarchy_write_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[account_hierarchy_write_dto], bool]) -> account_hierarchy_write_dtos:
        return account_hierarchy_write_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[account_hierarchy_write_dto], str]) -> dict[str, account_hierarchy_write_dtos]:
        grp_data: dict[str, account_hierarchy_write_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = account_hierarchy_write_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[account_hierarchy_write_dto], str], agg_method: Callable[[account_hierarchy_write_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, account_hierarchy_write_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[account_hierarchy_write_dto], bool]) -> account_hierarchy_write_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[account_hierarchy_write_dto], any], compare_method: Callable[[any, any], bool]) -> account_hierarchy_write_dto | None:
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
class account_rate_write_dtos(base_write_dtos):
    dtos: list[account_rate_write_dto]
    def __init__(self, dtos: list[account_rate_write_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[account_rate_write_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: account_rate_write_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[account_rate_write_dto], dtos2: list[account_rate_write_dto]):
        return cls(dtos1 + dtos2)
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> account_rate_write_dto | None:
        found_dtos = list(filter(lambda x: x.account_rate_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, account_rate_write_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.account_rate_uid] = dto
        return res
    def get_active(self):
        return account_rate_write_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return account_rate_write_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_first(self) -> account_rate_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> account_rate_write_dtos:
        if len(self.dtos) > n:
            return account_rate_write_dtos(self.dtos[:n])
        else:
            return account_rate_write_dtos(self.dtos)
    def get_last(self) -> account_rate_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, account_rate_write_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[account_rate_write_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[account_rate_write_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def check_any(self, check_method: Callable[[account_rate_write_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[account_rate_write_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[account_rate_write_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[account_rate_write_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, account_rate_write_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, account_rate_write_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, account_rate_write_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[account_rate_write_dto], bool]) -> account_rate_write_dtos:
        return account_rate_write_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[account_rate_write_dto], str]) -> dict[str, account_rate_write_dtos]:
        grp_data: dict[str, account_rate_write_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = account_rate_write_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[account_rate_write_dto], str], agg_method: Callable[[account_rate_write_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, account_rate_write_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[account_rate_write_dto], bool]) -> account_rate_write_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[account_rate_write_dto], any], compare_method: Callable[[any, any], bool]) -> account_rate_write_dto | None:
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
class account_skill_write_dtos(base_write_dtos):
    dtos: list[account_skill_write_dto]
    def __init__(self, dtos: list[account_skill_write_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[account_skill_write_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: account_skill_write_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[account_skill_write_dto], dtos2: list[account_skill_write_dto]):
        return cls(dtos1 + dtos2)
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> account_skill_write_dto | None:
        found_dtos = list(filter(lambda x: x.account_skill_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, account_skill_write_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.account_skill_uid] = dto
        return res
    def get_active(self):
        return account_skill_write_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return account_skill_write_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_first(self) -> account_skill_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> account_skill_write_dtos:
        if len(self.dtos) > n:
            return account_skill_write_dtos(self.dtos[:n])
        else:
            return account_skill_write_dtos(self.dtos)
    def get_last(self) -> account_skill_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, account_skill_write_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[account_skill_write_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[account_skill_write_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def check_any(self, check_method: Callable[[account_skill_write_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[account_skill_write_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[account_skill_write_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[account_skill_write_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, account_skill_write_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, account_skill_write_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, account_skill_write_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[account_skill_write_dto], bool]) -> account_skill_write_dtos:
        return account_skill_write_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[account_skill_write_dto], str]) -> dict[str, account_skill_write_dtos]:
        grp_data: dict[str, account_skill_write_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = account_skill_write_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[account_skill_write_dto], str], agg_method: Callable[[account_skill_write_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, account_skill_write_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[account_skill_write_dto], bool]) -> account_skill_write_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[account_skill_write_dto], any], compare_method: Callable[[any, any], bool]) -> account_skill_write_dto | None:
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
class account_skill_assignment_write_dtos(base_write_dtos):
    dtos: list[account_skill_assignment_write_dto]
    def __init__(self, dtos: list[account_skill_assignment_write_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[account_skill_assignment_write_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: account_skill_assignment_write_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[account_skill_assignment_write_dto], dtos2: list[account_skill_assignment_write_dto]):
        return cls(dtos1 + dtos2)
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> account_skill_assignment_write_dto | None:
        found_dtos = list(filter(lambda x: x.account_skill_assignment_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, account_skill_assignment_write_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.account_skill_assignment_uid] = dto
        return res
    def get_active(self):
        return account_skill_assignment_write_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return account_skill_assignment_write_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_first(self) -> account_skill_assignment_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> account_skill_assignment_write_dtos:
        if len(self.dtos) > n:
            return account_skill_assignment_write_dtos(self.dtos[:n])
        else:
            return account_skill_assignment_write_dtos(self.dtos)
    def get_last(self) -> account_skill_assignment_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, account_skill_assignment_write_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[account_skill_assignment_write_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[account_skill_assignment_write_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def check_any(self, check_method: Callable[[account_skill_assignment_write_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[account_skill_assignment_write_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[account_skill_assignment_write_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[account_skill_assignment_write_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, account_skill_assignment_write_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, account_skill_assignment_write_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, account_skill_assignment_write_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[account_skill_assignment_write_dto], bool]) -> account_skill_assignment_write_dtos:
        return account_skill_assignment_write_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[account_skill_assignment_write_dto], str]) -> dict[str, account_skill_assignment_write_dtos]:
        grp_data: dict[str, account_skill_assignment_write_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = account_skill_assignment_write_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[account_skill_assignment_write_dto], str], agg_method: Callable[[account_skill_assignment_write_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, account_skill_assignment_write_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[account_skill_assignment_write_dto], bool]) -> account_skill_assignment_write_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[account_skill_assignment_write_dto], any], compare_method: Callable[[any, any], bool]) -> account_skill_assignment_write_dto | None:
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
class account_skill_group_write_dtos(base_write_dtos):
    dtos: list[account_skill_group_write_dto]
    def __init__(self, dtos: list[account_skill_group_write_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[account_skill_group_write_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: account_skill_group_write_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[account_skill_group_write_dto], dtos2: list[account_skill_group_write_dto]):
        return cls(dtos1 + dtos2)
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> account_skill_group_write_dto | None:
        found_dtos = list(filter(lambda x: x.account_skill_group_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, account_skill_group_write_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.account_skill_group_uid] = dto
        return res
    def get_active(self):
        return account_skill_group_write_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return account_skill_group_write_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_first(self) -> account_skill_group_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> account_skill_group_write_dtos:
        if len(self.dtos) > n:
            return account_skill_group_write_dtos(self.dtos[:n])
        else:
            return account_skill_group_write_dtos(self.dtos)
    def get_last(self) -> account_skill_group_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, account_skill_group_write_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[account_skill_group_write_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[account_skill_group_write_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def check_any(self, check_method: Callable[[account_skill_group_write_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[account_skill_group_write_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[account_skill_group_write_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[account_skill_group_write_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, account_skill_group_write_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, account_skill_group_write_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, account_skill_group_write_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[account_skill_group_write_dto], bool]) -> account_skill_group_write_dtos:
        return account_skill_group_write_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[account_skill_group_write_dto], str]) -> dict[str, account_skill_group_write_dtos]:
        grp_data: dict[str, account_skill_group_write_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = account_skill_group_write_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[account_skill_group_write_dto], str], agg_method: Callable[[account_skill_group_write_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, account_skill_group_write_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[account_skill_group_write_dto], bool]) -> account_skill_group_write_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[account_skill_group_write_dto], any], compare_method: Callable[[any, any], bool]) -> account_skill_group_write_dto | None:
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
class account_team_write_dtos(base_write_dtos):
    dtos: list[account_team_write_dto]
    def __init__(self, dtos: list[account_team_write_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[account_team_write_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: account_team_write_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[account_team_write_dto], dtos2: list[account_team_write_dto]):
        return cls(dtos1 + dtos2)
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> account_team_write_dto | None:
        found_dtos = list(filter(lambda x: x.account_team_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, account_team_write_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.account_team_uid] = dto
        return res
    def get_active(self):
        return account_team_write_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return account_team_write_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_first(self) -> account_team_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> account_team_write_dtos:
        if len(self.dtos) > n:
            return account_team_write_dtos(self.dtos[:n])
        else:
            return account_team_write_dtos(self.dtos)
    def get_last(self) -> account_team_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, account_team_write_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[account_team_write_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[account_team_write_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def check_any(self, check_method: Callable[[account_team_write_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[account_team_write_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[account_team_write_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[account_team_write_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, account_team_write_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, account_team_write_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, account_team_write_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[account_team_write_dto], bool]) -> account_team_write_dtos:
        return account_team_write_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[account_team_write_dto], str]) -> dict[str, account_team_write_dtos]:
        grp_data: dict[str, account_team_write_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = account_team_write_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[account_team_write_dto], str], agg_method: Callable[[account_team_write_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, account_team_write_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[account_team_write_dto], bool]) -> account_team_write_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[account_team_write_dto], any], compare_method: Callable[[any, any], bool]) -> account_team_write_dto | None:
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
class account_title_write_dtos(base_write_dtos):
    dtos: list[account_title_write_dto]
    def __init__(self, dtos: list[account_title_write_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[account_title_write_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: account_title_write_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[account_title_write_dto], dtos2: list[account_title_write_dto]):
        return cls(dtos1 + dtos2)
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> account_title_write_dto | None:
        found_dtos = list(filter(lambda x: x.account_title_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, account_title_write_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.account_title_uid] = dto
        return res
    def get_active(self):
        return account_title_write_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return account_title_write_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_first(self) -> account_title_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> account_title_write_dtos:
        if len(self.dtos) > n:
            return account_title_write_dtos(self.dtos[:n])
        else:
            return account_title_write_dtos(self.dtos)
    def get_last(self) -> account_title_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, account_title_write_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[account_title_write_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[account_title_write_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def check_any(self, check_method: Callable[[account_title_write_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[account_title_write_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[account_title_write_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[account_title_write_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, account_title_write_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, account_title_write_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, account_title_write_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[account_title_write_dto], bool]) -> account_title_write_dtos:
        return account_title_write_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[account_title_write_dto], str]) -> dict[str, account_title_write_dtos]:
        grp_data: dict[str, account_title_write_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = account_title_write_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[account_title_write_dto], str], agg_method: Callable[[account_title_write_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, account_title_write_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[account_title_write_dto], bool]) -> account_title_write_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[account_title_write_dto], any], compare_method: Callable[[any, any], bool]) -> account_title_write_dto | None:
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
class account_title_assignment_write_dtos(base_write_dtos):
    dtos: list[account_title_assignment_write_dto]
    def __init__(self, dtos: list[account_title_assignment_write_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[account_title_assignment_write_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: account_title_assignment_write_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[account_title_assignment_write_dto], dtos2: list[account_title_assignment_write_dto]):
        return cls(dtos1 + dtos2)
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> account_title_assignment_write_dto | None:
        found_dtos = list(filter(lambda x: x.account_title_assignment_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, account_title_assignment_write_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.account_title_assignment_uid] = dto
        return res
    def get_active(self):
        return account_title_assignment_write_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return account_title_assignment_write_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_first(self) -> account_title_assignment_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> account_title_assignment_write_dtos:
        if len(self.dtos) > n:
            return account_title_assignment_write_dtos(self.dtos[:n])
        else:
            return account_title_assignment_write_dtos(self.dtos)
    def get_last(self) -> account_title_assignment_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, account_title_assignment_write_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[account_title_assignment_write_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[account_title_assignment_write_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def check_any(self, check_method: Callable[[account_title_assignment_write_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[account_title_assignment_write_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[account_title_assignment_write_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[account_title_assignment_write_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, account_title_assignment_write_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, account_title_assignment_write_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, account_title_assignment_write_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[account_title_assignment_write_dto], bool]) -> account_title_assignment_write_dtos:
        return account_title_assignment_write_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[account_title_assignment_write_dto], str]) -> dict[str, account_title_assignment_write_dtos]:
        grp_data: dict[str, account_title_assignment_write_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = account_title_assignment_write_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[account_title_assignment_write_dto], str], agg_method: Callable[[account_title_assignment_write_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, account_title_assignment_write_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[account_title_assignment_write_dto], bool]) -> account_title_assignment_write_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[account_title_assignment_write_dto], any], compare_method: Callable[[any, any], bool]) -> account_title_assignment_write_dto | None:
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
class account_title_responsibility_write_dtos(base_write_dtos):
    dtos: list[account_title_responsibility_write_dto]
    def __init__(self, dtos: list[account_title_responsibility_write_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[account_title_responsibility_write_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: account_title_responsibility_write_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[account_title_responsibility_write_dto], dtos2: list[account_title_responsibility_write_dto]):
        return cls(dtos1 + dtos2)
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> account_title_responsibility_write_dto | None:
        found_dtos = list(filter(lambda x: x.account_title_responsibility_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, account_title_responsibility_write_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.account_title_responsibility_uid] = dto
        return res
    def get_active(self):
        return account_title_responsibility_write_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return account_title_responsibility_write_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_first(self) -> account_title_responsibility_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> account_title_responsibility_write_dtos:
        if len(self.dtos) > n:
            return account_title_responsibility_write_dtos(self.dtos[:n])
        else:
            return account_title_responsibility_write_dtos(self.dtos)
    def get_last(self) -> account_title_responsibility_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, account_title_responsibility_write_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[account_title_responsibility_write_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[account_title_responsibility_write_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def check_any(self, check_method: Callable[[account_title_responsibility_write_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[account_title_responsibility_write_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[account_title_responsibility_write_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[account_title_responsibility_write_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, account_title_responsibility_write_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, account_title_responsibility_write_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, account_title_responsibility_write_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[account_title_responsibility_write_dto], bool]) -> account_title_responsibility_write_dtos:
        return account_title_responsibility_write_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[account_title_responsibility_write_dto], str]) -> dict[str, account_title_responsibility_write_dtos]:
        grp_data: dict[str, account_title_responsibility_write_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = account_title_responsibility_write_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[account_title_responsibility_write_dto], str], agg_method: Callable[[account_title_responsibility_write_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, account_title_responsibility_write_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[account_title_responsibility_write_dto], bool]) -> account_title_responsibility_write_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[account_title_responsibility_write_dto], any], compare_method: Callable[[any, any], bool]) -> account_title_responsibility_write_dto | None:
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
class account_type_write_dtos(base_write_dtos):
    dtos: list[account_type_write_dto]
    def __init__(self, dtos: list[account_type_write_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[account_type_write_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: account_type_write_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[account_type_write_dto], dtos2: list[account_type_write_dto]):
        return cls(dtos1 + dtos2)
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> account_type_write_dto | None:
        found_dtos = list(filter(lambda x: x.account_type_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, account_type_write_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.account_type_uid] = dto
        return res
    def get_active(self):
        return account_type_write_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return account_type_write_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_first(self) -> account_type_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> account_type_write_dtos:
        if len(self.dtos) > n:
            return account_type_write_dtos(self.dtos[:n])
        else:
            return account_type_write_dtos(self.dtos)
    def get_last(self) -> account_type_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, account_type_write_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[account_type_write_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[account_type_write_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def check_any(self, check_method: Callable[[account_type_write_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[account_type_write_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[account_type_write_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[account_type_write_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, account_type_write_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, account_type_write_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, account_type_write_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[account_type_write_dto], bool]) -> account_type_write_dtos:
        return account_type_write_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[account_type_write_dto], str]) -> dict[str, account_type_write_dtos]:
        grp_data: dict[str, account_type_write_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = account_type_write_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[account_type_write_dto], str], agg_method: Callable[[account_type_write_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, account_type_write_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[account_type_write_dto], bool]) -> account_type_write_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[account_type_write_dto], any], compare_method: Callable[[any, any], bool]) -> account_type_write_dto | None:
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
class audit_change_write_dtos(base_write_dtos):
    dtos: list[audit_change_write_dto]
    def __init__(self, dtos: list[audit_change_write_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[audit_change_write_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: audit_change_write_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[audit_change_write_dto], dtos2: list[audit_change_write_dto]):
        return cls(dtos1 + dtos2)
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> audit_change_write_dto | None:
        found_dtos = list(filter(lambda x: x.audit_change_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, audit_change_write_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.audit_change_uid] = dto
        return res
    def get_active(self):
        return audit_change_write_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return audit_change_write_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_first(self) -> audit_change_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> audit_change_write_dtos:
        if len(self.dtos) > n:
            return audit_change_write_dtos(self.dtos[:n])
        else:
            return audit_change_write_dtos(self.dtos)
    def get_last(self) -> audit_change_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, audit_change_write_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[audit_change_write_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[audit_change_write_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def check_any(self, check_method: Callable[[audit_change_write_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[audit_change_write_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[audit_change_write_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[audit_change_write_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, audit_change_write_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, audit_change_write_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, audit_change_write_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[audit_change_write_dto], bool]) -> audit_change_write_dtos:
        return audit_change_write_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[audit_change_write_dto], str]) -> dict[str, audit_change_write_dtos]:
        grp_data: dict[str, audit_change_write_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = audit_change_write_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[audit_change_write_dto], str], agg_method: Callable[[audit_change_write_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, audit_change_write_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[audit_change_write_dto], bool]) -> audit_change_write_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[audit_change_write_dto], any], compare_method: Callable[[any, any], bool]) -> audit_change_write_dto | None:
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
class audit_type_write_dtos(base_write_dtos):
    dtos: list[audit_type_write_dto]
    def __init__(self, dtos: list[audit_type_write_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[audit_type_write_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: audit_type_write_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[audit_type_write_dto], dtos2: list[audit_type_write_dto]):
        return cls(dtos1 + dtos2)
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> audit_type_write_dto | None:
        found_dtos = list(filter(lambda x: x.audit_type_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, audit_type_write_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.audit_type_uid] = dto
        return res
    def get_active(self):
        return audit_type_write_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return audit_type_write_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_first(self) -> audit_type_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> audit_type_write_dtos:
        if len(self.dtos) > n:
            return audit_type_write_dtos(self.dtos[:n])
        else:
            return audit_type_write_dtos(self.dtos)
    def get_last(self) -> audit_type_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, audit_type_write_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[audit_type_write_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[audit_type_write_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def check_any(self, check_method: Callable[[audit_type_write_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[audit_type_write_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[audit_type_write_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[audit_type_write_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, audit_type_write_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, audit_type_write_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, audit_type_write_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[audit_type_write_dto], bool]) -> audit_type_write_dtos:
        return audit_type_write_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[audit_type_write_dto], str]) -> dict[str, audit_type_write_dtos]:
        grp_data: dict[str, audit_type_write_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = audit_type_write_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[audit_type_write_dto], str], agg_method: Callable[[audit_type_write_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, audit_type_write_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[audit_type_write_dto], bool]) -> audit_type_write_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[audit_type_write_dto], any], compare_method: Callable[[any, any], bool]) -> audit_type_write_dto | None:
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
class auth_attempt_write_dtos(base_write_dtos):
    dtos: list[auth_attempt_write_dto]
    def __init__(self, dtos: list[auth_attempt_write_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[auth_attempt_write_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: auth_attempt_write_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[auth_attempt_write_dto], dtos2: list[auth_attempt_write_dto]):
        return cls(dtos1 + dtos2)
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> auth_attempt_write_dto | None:
        found_dtos = list(filter(lambda x: x.auth_attempt_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, auth_attempt_write_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.auth_attempt_uid] = dto
        return res
    def get_active(self):
        return auth_attempt_write_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return auth_attempt_write_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_first(self) -> auth_attempt_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> auth_attempt_write_dtos:
        if len(self.dtos) > n:
            return auth_attempt_write_dtos(self.dtos[:n])
        else:
            return auth_attempt_write_dtos(self.dtos)
    def get_last(self) -> auth_attempt_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, auth_attempt_write_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[auth_attempt_write_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[auth_attempt_write_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def check_any(self, check_method: Callable[[auth_attempt_write_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[auth_attempt_write_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[auth_attempt_write_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[auth_attempt_write_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, auth_attempt_write_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, auth_attempt_write_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, auth_attempt_write_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[auth_attempt_write_dto], bool]) -> auth_attempt_write_dtos:
        return auth_attempt_write_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[auth_attempt_write_dto], str]) -> dict[str, auth_attempt_write_dtos]:
        grp_data: dict[str, auth_attempt_write_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = auth_attempt_write_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[auth_attempt_write_dto], str], agg_method: Callable[[auth_attempt_write_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, auth_attempt_write_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[auth_attempt_write_dto], bool]) -> auth_attempt_write_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[auth_attempt_write_dto], any], compare_method: Callable[[any, any], bool]) -> auth_attempt_write_dto | None:
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
class auth_identity_write_dtos(base_write_dtos):
    dtos: list[auth_identity_write_dto]
    def __init__(self, dtos: list[auth_identity_write_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[auth_identity_write_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: auth_identity_write_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[auth_identity_write_dto], dtos2: list[auth_identity_write_dto]):
        return cls(dtos1 + dtos2)
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> auth_identity_write_dto | None:
        found_dtos = list(filter(lambda x: x.auth_identity_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, auth_identity_write_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.auth_identity_uid] = dto
        return res
    def get_active(self):
        return auth_identity_write_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return auth_identity_write_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_first(self) -> auth_identity_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> auth_identity_write_dtos:
        if len(self.dtos) > n:
            return auth_identity_write_dtos(self.dtos[:n])
        else:
            return auth_identity_write_dtos(self.dtos)
    def get_last(self) -> auth_identity_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, auth_identity_write_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[auth_identity_write_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[auth_identity_write_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def check_any(self, check_method: Callable[[auth_identity_write_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[auth_identity_write_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[auth_identity_write_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[auth_identity_write_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, auth_identity_write_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, auth_identity_write_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, auth_identity_write_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[auth_identity_write_dto], bool]) -> auth_identity_write_dtos:
        return auth_identity_write_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[auth_identity_write_dto], str]) -> dict[str, auth_identity_write_dtos]:
        grp_data: dict[str, auth_identity_write_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = auth_identity_write_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[auth_identity_write_dto], str], agg_method: Callable[[auth_identity_write_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, auth_identity_write_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[auth_identity_write_dto], bool]) -> auth_identity_write_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[auth_identity_write_dto], any], compare_method: Callable[[any, any], bool]) -> auth_identity_write_dto | None:
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
class auth_identity_tenant_write_dtos(base_write_dtos):
    dtos: list[auth_identity_tenant_write_dto]
    def __init__(self, dtos: list[auth_identity_tenant_write_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[auth_identity_tenant_write_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: auth_identity_tenant_write_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[auth_identity_tenant_write_dto], dtos2: list[auth_identity_tenant_write_dto]):
        return cls(dtos1 + dtos2)
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> auth_identity_tenant_write_dto | None:
        found_dtos = list(filter(lambda x: x.auth_identity_tenant_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, auth_identity_tenant_write_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.auth_identity_tenant_uid] = dto
        return res
    def get_active(self):
        return auth_identity_tenant_write_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return auth_identity_tenant_write_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_first(self) -> auth_identity_tenant_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> auth_identity_tenant_write_dtos:
        if len(self.dtos) > n:
            return auth_identity_tenant_write_dtos(self.dtos[:n])
        else:
            return auth_identity_tenant_write_dtos(self.dtos)
    def get_last(self) -> auth_identity_tenant_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, auth_identity_tenant_write_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[auth_identity_tenant_write_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[auth_identity_tenant_write_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def check_any(self, check_method: Callable[[auth_identity_tenant_write_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[auth_identity_tenant_write_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[auth_identity_tenant_write_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[auth_identity_tenant_write_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, auth_identity_tenant_write_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, auth_identity_tenant_write_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, auth_identity_tenant_write_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[auth_identity_tenant_write_dto], bool]) -> auth_identity_tenant_write_dtos:
        return auth_identity_tenant_write_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[auth_identity_tenant_write_dto], str]) -> dict[str, auth_identity_tenant_write_dtos]:
        grp_data: dict[str, auth_identity_tenant_write_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = auth_identity_tenant_write_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[auth_identity_tenant_write_dto], str], agg_method: Callable[[auth_identity_tenant_write_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, auth_identity_tenant_write_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[auth_identity_tenant_write_dto], bool]) -> auth_identity_tenant_write_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[auth_identity_tenant_write_dto], any], compare_method: Callable[[any, any], bool]) -> auth_identity_tenant_write_dto | None:
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
class auth_key_write_dtos(base_write_dtos):
    dtos: list[auth_key_write_dto]
    def __init__(self, dtos: list[auth_key_write_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[auth_key_write_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: auth_key_write_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[auth_key_write_dto], dtos2: list[auth_key_write_dto]):
        return cls(dtos1 + dtos2)
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> auth_key_write_dto | None:
        found_dtos = list(filter(lambda x: x.auth_key_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, auth_key_write_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.auth_key_uid] = dto
        return res
    def get_active(self):
        return auth_key_write_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return auth_key_write_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_first(self) -> auth_key_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> auth_key_write_dtos:
        if len(self.dtos) > n:
            return auth_key_write_dtos(self.dtos[:n])
        else:
            return auth_key_write_dtos(self.dtos)
    def get_last(self) -> auth_key_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, auth_key_write_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[auth_key_write_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[auth_key_write_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def check_any(self, check_method: Callable[[auth_key_write_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[auth_key_write_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[auth_key_write_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[auth_key_write_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, auth_key_write_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, auth_key_write_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, auth_key_write_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[auth_key_write_dto], bool]) -> auth_key_write_dtos:
        return auth_key_write_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[auth_key_write_dto], str]) -> dict[str, auth_key_write_dtos]:
        grp_data: dict[str, auth_key_write_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = auth_key_write_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[auth_key_write_dto], str], agg_method: Callable[[auth_key_write_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, auth_key_write_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[auth_key_write_dto], bool]) -> auth_key_write_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[auth_key_write_dto], any], compare_method: Callable[[any, any], bool]) -> auth_key_write_dto | None:
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
class auth_key_type_write_dtos(base_write_dtos):
    dtos: list[auth_key_type_write_dto]
    def __init__(self, dtos: list[auth_key_type_write_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[auth_key_type_write_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: auth_key_type_write_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[auth_key_type_write_dto], dtos2: list[auth_key_type_write_dto]):
        return cls(dtos1 + dtos2)
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> auth_key_type_write_dto | None:
        found_dtos = list(filter(lambda x: x.auth_key_type_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, auth_key_type_write_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.auth_key_type_uid] = dto
        return res
    def get_active(self):
        return auth_key_type_write_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return auth_key_type_write_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_first(self) -> auth_key_type_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> auth_key_type_write_dtos:
        if len(self.dtos) > n:
            return auth_key_type_write_dtos(self.dtos[:n])
        else:
            return auth_key_type_write_dtos(self.dtos)
    def get_last(self) -> auth_key_type_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, auth_key_type_write_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[auth_key_type_write_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[auth_key_type_write_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def check_any(self, check_method: Callable[[auth_key_type_write_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[auth_key_type_write_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[auth_key_type_write_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[auth_key_type_write_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, auth_key_type_write_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, auth_key_type_write_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, auth_key_type_write_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[auth_key_type_write_dto], bool]) -> auth_key_type_write_dtos:
        return auth_key_type_write_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[auth_key_type_write_dto], str]) -> dict[str, auth_key_type_write_dtos]:
        grp_data: dict[str, auth_key_type_write_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = auth_key_type_write_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[auth_key_type_write_dto], str], agg_method: Callable[[auth_key_type_write_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, auth_key_type_write_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[auth_key_type_write_dto], bool]) -> auth_key_type_write_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[auth_key_type_write_dto], any], compare_method: Callable[[any, any], bool]) -> auth_key_type_write_dto | None:
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
class auth_password_write_dtos(base_write_dtos):
    dtos: list[auth_password_write_dto]
    def __init__(self, dtos: list[auth_password_write_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[auth_password_write_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: auth_password_write_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[auth_password_write_dto], dtos2: list[auth_password_write_dto]):
        return cls(dtos1 + dtos2)
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> auth_password_write_dto | None:
        found_dtos = list(filter(lambda x: x.auth_password_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, auth_password_write_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.auth_password_uid] = dto
        return res
    def get_active(self):
        return auth_password_write_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return auth_password_write_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_first(self) -> auth_password_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> auth_password_write_dtos:
        if len(self.dtos) > n:
            return auth_password_write_dtos(self.dtos[:n])
        else:
            return auth_password_write_dtos(self.dtos)
    def get_last(self) -> auth_password_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, auth_password_write_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[auth_password_write_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[auth_password_write_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def check_any(self, check_method: Callable[[auth_password_write_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[auth_password_write_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[auth_password_write_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[auth_password_write_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, auth_password_write_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, auth_password_write_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, auth_password_write_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[auth_password_write_dto], bool]) -> auth_password_write_dtos:
        return auth_password_write_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[auth_password_write_dto], str]) -> dict[str, auth_password_write_dtos]:
        grp_data: dict[str, auth_password_write_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = auth_password_write_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[auth_password_write_dto], str], agg_method: Callable[[auth_password_write_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, auth_password_write_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[auth_password_write_dto], bool]) -> auth_password_write_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[auth_password_write_dto], any], compare_method: Callable[[any, any], bool]) -> auth_password_write_dto | None:
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
class auth_password_current_write_dtos(base_write_dtos):
    dtos: list[auth_password_current_write_dto]
    def __init__(self, dtos: list[auth_password_current_write_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[auth_password_current_write_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: auth_password_current_write_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[auth_password_current_write_dto], dtos2: list[auth_password_current_write_dto]):
        return cls(dtos1 + dtos2)
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> auth_password_current_write_dto | None:
        found_dtos = list(filter(lambda x: x.auth_password_current_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, auth_password_current_write_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.auth_password_current_uid] = dto
        return res
    def get_active(self):
        return auth_password_current_write_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return auth_password_current_write_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_first(self) -> auth_password_current_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> auth_password_current_write_dtos:
        if len(self.dtos) > n:
            return auth_password_current_write_dtos(self.dtos[:n])
        else:
            return auth_password_current_write_dtos(self.dtos)
    def get_last(self) -> auth_password_current_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, auth_password_current_write_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[auth_password_current_write_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[auth_password_current_write_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def check_any(self, check_method: Callable[[auth_password_current_write_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[auth_password_current_write_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[auth_password_current_write_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[auth_password_current_write_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, auth_password_current_write_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, auth_password_current_write_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, auth_password_current_write_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[auth_password_current_write_dto], bool]) -> auth_password_current_write_dtos:
        return auth_password_current_write_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[auth_password_current_write_dto], str]) -> dict[str, auth_password_current_write_dtos]:
        grp_data: dict[str, auth_password_current_write_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = auth_password_current_write_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[auth_password_current_write_dto], str], agg_method: Callable[[auth_password_current_write_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, auth_password_current_write_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[auth_password_current_write_dto], bool]) -> auth_password_current_write_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[auth_password_current_write_dto], any], compare_method: Callable[[any, any], bool]) -> auth_password_current_write_dto | None:
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
class auth_password_rule_write_dtos(base_write_dtos):
    dtos: list[auth_password_rule_write_dto]
    def __init__(self, dtos: list[auth_password_rule_write_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[auth_password_rule_write_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: auth_password_rule_write_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[auth_password_rule_write_dto], dtos2: list[auth_password_rule_write_dto]):
        return cls(dtos1 + dtos2)
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> auth_password_rule_write_dto | None:
        found_dtos = list(filter(lambda x: x.auth_password_rule_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, auth_password_rule_write_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.auth_password_rule_uid] = dto
        return res
    def get_active(self):
        return auth_password_rule_write_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return auth_password_rule_write_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_first(self) -> auth_password_rule_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> auth_password_rule_write_dtos:
        if len(self.dtos) > n:
            return auth_password_rule_write_dtos(self.dtos[:n])
        else:
            return auth_password_rule_write_dtos(self.dtos)
    def get_last(self) -> auth_password_rule_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, auth_password_rule_write_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[auth_password_rule_write_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[auth_password_rule_write_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def check_any(self, check_method: Callable[[auth_password_rule_write_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[auth_password_rule_write_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[auth_password_rule_write_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[auth_password_rule_write_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, auth_password_rule_write_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, auth_password_rule_write_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, auth_password_rule_write_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[auth_password_rule_write_dto], bool]) -> auth_password_rule_write_dtos:
        return auth_password_rule_write_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[auth_password_rule_write_dto], str]) -> dict[str, auth_password_rule_write_dtos]:
        grp_data: dict[str, auth_password_rule_write_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = auth_password_rule_write_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[auth_password_rule_write_dto], str], agg_method: Callable[[auth_password_rule_write_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, auth_password_rule_write_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[auth_password_rule_write_dto], bool]) -> auth_password_rule_write_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[auth_password_rule_write_dto], any], compare_method: Callable[[any, any], bool]) -> auth_password_rule_write_dto | None:
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
class auth_permission_write_dtos(base_write_dtos):
    dtos: list[auth_permission_write_dto]
    def __init__(self, dtos: list[auth_permission_write_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[auth_permission_write_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: auth_permission_write_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[auth_permission_write_dto], dtos2: list[auth_permission_write_dto]):
        return cls(dtos1 + dtos2)
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> auth_permission_write_dto | None:
        found_dtos = list(filter(lambda x: x.auth_permission_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, auth_permission_write_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.auth_permission_uid] = dto
        return res
    def get_active(self):
        return auth_permission_write_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return auth_permission_write_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_first(self) -> auth_permission_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> auth_permission_write_dtos:
        if len(self.dtos) > n:
            return auth_permission_write_dtos(self.dtos[:n])
        else:
            return auth_permission_write_dtos(self.dtos)
    def get_last(self) -> auth_permission_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, auth_permission_write_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[auth_permission_write_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[auth_permission_write_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def check_any(self, check_method: Callable[[auth_permission_write_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[auth_permission_write_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[auth_permission_write_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[auth_permission_write_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, auth_permission_write_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, auth_permission_write_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, auth_permission_write_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[auth_permission_write_dto], bool]) -> auth_permission_write_dtos:
        return auth_permission_write_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[auth_permission_write_dto], str]) -> dict[str, auth_permission_write_dtos]:
        grp_data: dict[str, auth_permission_write_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = auth_permission_write_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[auth_permission_write_dto], str], agg_method: Callable[[auth_permission_write_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, auth_permission_write_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[auth_permission_write_dto], bool]) -> auth_permission_write_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[auth_permission_write_dto], any], compare_method: Callable[[any, any], bool]) -> auth_permission_write_dto | None:
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
class auth_permission_type_write_dtos(base_write_dtos):
    dtos: list[auth_permission_type_write_dto]
    def __init__(self, dtos: list[auth_permission_type_write_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[auth_permission_type_write_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: auth_permission_type_write_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[auth_permission_type_write_dto], dtos2: list[auth_permission_type_write_dto]):
        return cls(dtos1 + dtos2)
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> auth_permission_type_write_dto | None:
        found_dtos = list(filter(lambda x: x.auth_permission_type_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, auth_permission_type_write_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.auth_permission_type_uid] = dto
        return res
    def get_active(self):
        return auth_permission_type_write_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return auth_permission_type_write_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_first(self) -> auth_permission_type_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> auth_permission_type_write_dtos:
        if len(self.dtos) > n:
            return auth_permission_type_write_dtos(self.dtos[:n])
        else:
            return auth_permission_type_write_dtos(self.dtos)
    def get_last(self) -> auth_permission_type_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, auth_permission_type_write_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[auth_permission_type_write_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[auth_permission_type_write_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def check_any(self, check_method: Callable[[auth_permission_type_write_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[auth_permission_type_write_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[auth_permission_type_write_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[auth_permission_type_write_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, auth_permission_type_write_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, auth_permission_type_write_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, auth_permission_type_write_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[auth_permission_type_write_dto], bool]) -> auth_permission_type_write_dtos:
        return auth_permission_type_write_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[auth_permission_type_write_dto], str]) -> dict[str, auth_permission_type_write_dtos]:
        grp_data: dict[str, auth_permission_type_write_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = auth_permission_type_write_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[auth_permission_type_write_dto], str], agg_method: Callable[[auth_permission_type_write_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, auth_permission_type_write_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[auth_permission_type_write_dto], bool]) -> auth_permission_type_write_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[auth_permission_type_write_dto], any], compare_method: Callable[[any, any], bool]) -> auth_permission_type_write_dto | None:
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
class auth_pin_write_dtos(base_write_dtos):
    dtos: list[auth_pin_write_dto]
    def __init__(self, dtos: list[auth_pin_write_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[auth_pin_write_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: auth_pin_write_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[auth_pin_write_dto], dtos2: list[auth_pin_write_dto]):
        return cls(dtos1 + dtos2)
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> auth_pin_write_dto | None:
        found_dtos = list(filter(lambda x: x.auth_pin_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, auth_pin_write_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.auth_pin_uid] = dto
        return res
    def get_active(self):
        return auth_pin_write_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return auth_pin_write_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_first(self) -> auth_pin_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> auth_pin_write_dtos:
        if len(self.dtos) > n:
            return auth_pin_write_dtos(self.dtos[:n])
        else:
            return auth_pin_write_dtos(self.dtos)
    def get_last(self) -> auth_pin_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, auth_pin_write_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[auth_pin_write_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[auth_pin_write_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def check_any(self, check_method: Callable[[auth_pin_write_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[auth_pin_write_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[auth_pin_write_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[auth_pin_write_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, auth_pin_write_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, auth_pin_write_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, auth_pin_write_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[auth_pin_write_dto], bool]) -> auth_pin_write_dtos:
        return auth_pin_write_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[auth_pin_write_dto], str]) -> dict[str, auth_pin_write_dtos]:
        grp_data: dict[str, auth_pin_write_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = auth_pin_write_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[auth_pin_write_dto], str], agg_method: Callable[[auth_pin_write_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, auth_pin_write_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[auth_pin_write_dto], bool]) -> auth_pin_write_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[auth_pin_write_dto], any], compare_method: Callable[[any, any], bool]) -> auth_pin_write_dto | None:
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
class auth_request_write_dtos(base_write_dtos):
    dtos: list[auth_request_write_dto]
    def __init__(self, dtos: list[auth_request_write_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[auth_request_write_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: auth_request_write_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[auth_request_write_dto], dtos2: list[auth_request_write_dto]):
        return cls(dtos1 + dtos2)
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> auth_request_write_dto | None:
        found_dtos = list(filter(lambda x: x.auth_request_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, auth_request_write_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.auth_request_uid] = dto
        return res
    def get_active(self):
        return auth_request_write_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return auth_request_write_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_first(self) -> auth_request_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> auth_request_write_dtos:
        if len(self.dtos) > n:
            return auth_request_write_dtos(self.dtos[:n])
        else:
            return auth_request_write_dtos(self.dtos)
    def get_last(self) -> auth_request_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, auth_request_write_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[auth_request_write_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[auth_request_write_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def check_any(self, check_method: Callable[[auth_request_write_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[auth_request_write_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[auth_request_write_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[auth_request_write_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, auth_request_write_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, auth_request_write_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, auth_request_write_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[auth_request_write_dto], bool]) -> auth_request_write_dtos:
        return auth_request_write_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[auth_request_write_dto], str]) -> dict[str, auth_request_write_dtos]:
        grp_data: dict[str, auth_request_write_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = auth_request_write_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[auth_request_write_dto], str], agg_method: Callable[[auth_request_write_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, auth_request_write_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[auth_request_write_dto], bool]) -> auth_request_write_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[auth_request_write_dto], any], compare_method: Callable[[any, any], bool]) -> auth_request_write_dto | None:
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
class auth_role_write_dtos(base_write_dtos):
    dtos: list[auth_role_write_dto]
    def __init__(self, dtos: list[auth_role_write_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[auth_role_write_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: auth_role_write_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[auth_role_write_dto], dtos2: list[auth_role_write_dto]):
        return cls(dtos1 + dtos2)
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> auth_role_write_dto | None:
        found_dtos = list(filter(lambda x: x.auth_role_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, auth_role_write_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.auth_role_uid] = dto
        return res
    def get_active(self):
        return auth_role_write_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return auth_role_write_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_first(self) -> auth_role_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> auth_role_write_dtos:
        if len(self.dtos) > n:
            return auth_role_write_dtos(self.dtos[:n])
        else:
            return auth_role_write_dtos(self.dtos)
    def get_last(self) -> auth_role_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, auth_role_write_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[auth_role_write_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[auth_role_write_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def check_any(self, check_method: Callable[[auth_role_write_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[auth_role_write_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[auth_role_write_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[auth_role_write_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, auth_role_write_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, auth_role_write_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, auth_role_write_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[auth_role_write_dto], bool]) -> auth_role_write_dtos:
        return auth_role_write_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[auth_role_write_dto], str]) -> dict[str, auth_role_write_dtos]:
        grp_data: dict[str, auth_role_write_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = auth_role_write_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[auth_role_write_dto], str], agg_method: Callable[[auth_role_write_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, auth_role_write_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[auth_role_write_dto], bool]) -> auth_role_write_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[auth_role_write_dto], any], compare_method: Callable[[any, any], bool]) -> auth_role_write_dto | None:
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
class auth_role_uri_write_dtos(base_write_dtos):
    dtos: list[auth_role_uri_write_dto]
    def __init__(self, dtos: list[auth_role_uri_write_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[auth_role_uri_write_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: auth_role_uri_write_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[auth_role_uri_write_dto], dtos2: list[auth_role_uri_write_dto]):
        return cls(dtos1 + dtos2)
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> auth_role_uri_write_dto | None:
        found_dtos = list(filter(lambda x: x.auth_role_uri_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, auth_role_uri_write_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.auth_role_uri_uid] = dto
        return res
    def get_active(self):
        return auth_role_uri_write_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return auth_role_uri_write_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_first(self) -> auth_role_uri_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> auth_role_uri_write_dtos:
        if len(self.dtos) > n:
            return auth_role_uri_write_dtos(self.dtos[:n])
        else:
            return auth_role_uri_write_dtos(self.dtos)
    def get_last(self) -> auth_role_uri_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, auth_role_uri_write_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[auth_role_uri_write_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[auth_role_uri_write_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def check_any(self, check_method: Callable[[auth_role_uri_write_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[auth_role_uri_write_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[auth_role_uri_write_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[auth_role_uri_write_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, auth_role_uri_write_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, auth_role_uri_write_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, auth_role_uri_write_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[auth_role_uri_write_dto], bool]) -> auth_role_uri_write_dtos:
        return auth_role_uri_write_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[auth_role_uri_write_dto], str]) -> dict[str, auth_role_uri_write_dtos]:
        grp_data: dict[str, auth_role_uri_write_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = auth_role_uri_write_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[auth_role_uri_write_dto], str], agg_method: Callable[[auth_role_uri_write_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, auth_role_uri_write_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[auth_role_uri_write_dto], bool]) -> auth_role_uri_write_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[auth_role_uri_write_dto], any], compare_method: Callable[[any, any], bool]) -> auth_role_uri_write_dto | None:
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
class auth_session_write_dtos(base_write_dtos):
    dtos: list[auth_session_write_dto]
    def __init__(self, dtos: list[auth_session_write_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[auth_session_write_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: auth_session_write_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[auth_session_write_dto], dtos2: list[auth_session_write_dto]):
        return cls(dtos1 + dtos2)
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> auth_session_write_dto | None:
        found_dtos = list(filter(lambda x: x.auth_session_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, auth_session_write_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.auth_session_uid] = dto
        return res
    def get_active(self):
        return auth_session_write_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return auth_session_write_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_first(self) -> auth_session_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> auth_session_write_dtos:
        if len(self.dtos) > n:
            return auth_session_write_dtos(self.dtos[:n])
        else:
            return auth_session_write_dtos(self.dtos)
    def get_last(self) -> auth_session_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, auth_session_write_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[auth_session_write_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[auth_session_write_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def check_any(self, check_method: Callable[[auth_session_write_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[auth_session_write_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[auth_session_write_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[auth_session_write_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, auth_session_write_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, auth_session_write_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, auth_session_write_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[auth_session_write_dto], bool]) -> auth_session_write_dtos:
        return auth_session_write_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[auth_session_write_dto], str]) -> dict[str, auth_session_write_dtos]:
        grp_data: dict[str, auth_session_write_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = auth_session_write_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[auth_session_write_dto], str], agg_method: Callable[[auth_session_write_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, auth_session_write_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[auth_session_write_dto], bool]) -> auth_session_write_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[auth_session_write_dto], any], compare_method: Callable[[any, any], bool]) -> auth_session_write_dto | None:
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
class auth_sso_write_dtos(base_write_dtos):
    dtos: list[auth_sso_write_dto]
    def __init__(self, dtos: list[auth_sso_write_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[auth_sso_write_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: auth_sso_write_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[auth_sso_write_dto], dtos2: list[auth_sso_write_dto]):
        return cls(dtos1 + dtos2)
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> auth_sso_write_dto | None:
        found_dtos = list(filter(lambda x: x.auth_sso_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, auth_sso_write_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.auth_sso_uid] = dto
        return res
    def get_active(self):
        return auth_sso_write_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return auth_sso_write_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_first(self) -> auth_sso_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> auth_sso_write_dtos:
        if len(self.dtos) > n:
            return auth_sso_write_dtos(self.dtos[:n])
        else:
            return auth_sso_write_dtos(self.dtos)
    def get_last(self) -> auth_sso_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, auth_sso_write_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[auth_sso_write_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[auth_sso_write_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def check_any(self, check_method: Callable[[auth_sso_write_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[auth_sso_write_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[auth_sso_write_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[auth_sso_write_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, auth_sso_write_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, auth_sso_write_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, auth_sso_write_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[auth_sso_write_dto], bool]) -> auth_sso_write_dtos:
        return auth_sso_write_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[auth_sso_write_dto], str]) -> dict[str, auth_sso_write_dtos]:
        grp_data: dict[str, auth_sso_write_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = auth_sso_write_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[auth_sso_write_dto], str], agg_method: Callable[[auth_sso_write_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, auth_sso_write_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[auth_sso_write_dto], bool]) -> auth_sso_write_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[auth_sso_write_dto], any], compare_method: Callable[[any, any], bool]) -> auth_sso_write_dto | None:
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
class auth_token_write_dtos(base_write_dtos):
    dtos: list[auth_token_write_dto]
    def __init__(self, dtos: list[auth_token_write_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[auth_token_write_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: auth_token_write_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[auth_token_write_dto], dtos2: list[auth_token_write_dto]):
        return cls(dtos1 + dtos2)
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> auth_token_write_dto | None:
        found_dtos = list(filter(lambda x: x.auth_token_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, auth_token_write_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.auth_token_uid] = dto
        return res
    def get_active(self):
        return auth_token_write_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return auth_token_write_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_first(self) -> auth_token_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> auth_token_write_dtos:
        if len(self.dtos) > n:
            return auth_token_write_dtos(self.dtos[:n])
        else:
            return auth_token_write_dtos(self.dtos)
    def get_last(self) -> auth_token_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, auth_token_write_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[auth_token_write_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[auth_token_write_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def check_any(self, check_method: Callable[[auth_token_write_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[auth_token_write_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[auth_token_write_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[auth_token_write_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, auth_token_write_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, auth_token_write_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, auth_token_write_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[auth_token_write_dto], bool]) -> auth_token_write_dtos:
        return auth_token_write_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[auth_token_write_dto], str]) -> dict[str, auth_token_write_dtos]:
        grp_data: dict[str, auth_token_write_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = auth_token_write_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[auth_token_write_dto], str], agg_method: Callable[[auth_token_write_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, auth_token_write_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[auth_token_write_dto], bool]) -> auth_token_write_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[auth_token_write_dto], any], compare_method: Callable[[any, any], bool]) -> auth_token_write_dto | None:
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
class auth_token_type_write_dtos(base_write_dtos):
    dtos: list[auth_token_type_write_dto]
    def __init__(self, dtos: list[auth_token_type_write_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[auth_token_type_write_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: auth_token_type_write_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[auth_token_type_write_dto], dtos2: list[auth_token_type_write_dto]):
        return cls(dtos1 + dtos2)
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> auth_token_type_write_dto | None:
        found_dtos = list(filter(lambda x: x.auth_token_type_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, auth_token_type_write_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.auth_token_type_uid] = dto
        return res
    def get_active(self):
        return auth_token_type_write_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return auth_token_type_write_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_first(self) -> auth_token_type_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> auth_token_type_write_dtos:
        if len(self.dtos) > n:
            return auth_token_type_write_dtos(self.dtos[:n])
        else:
            return auth_token_type_write_dtos(self.dtos)
    def get_last(self) -> auth_token_type_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, auth_token_type_write_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[auth_token_type_write_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[auth_token_type_write_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def check_any(self, check_method: Callable[[auth_token_type_write_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[auth_token_type_write_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[auth_token_type_write_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[auth_token_type_write_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, auth_token_type_write_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, auth_token_type_write_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, auth_token_type_write_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[auth_token_type_write_dto], bool]) -> auth_token_type_write_dtos:
        return auth_token_type_write_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[auth_token_type_write_dto], str]) -> dict[str, auth_token_type_write_dtos]:
        grp_data: dict[str, auth_token_type_write_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = auth_token_type_write_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[auth_token_type_write_dto], str], agg_method: Callable[[auth_token_type_write_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, auth_token_type_write_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[auth_token_type_write_dto], bool]) -> auth_token_type_write_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[auth_token_type_write_dto], any], compare_method: Callable[[any, any], bool]) -> auth_token_type_write_dto | None:
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
class calendar_account_write_dtos(base_write_dtos):
    dtos: list[calendar_account_write_dto]
    def __init__(self, dtos: list[calendar_account_write_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[calendar_account_write_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: calendar_account_write_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[calendar_account_write_dto], dtos2: list[calendar_account_write_dto]):
        return cls(dtos1 + dtos2)
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> calendar_account_write_dto | None:
        found_dtos = list(filter(lambda x: x.calendar_account_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, calendar_account_write_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.calendar_account_uid] = dto
        return res
    def get_active(self):
        return calendar_account_write_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return calendar_account_write_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_first(self) -> calendar_account_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> calendar_account_write_dtos:
        if len(self.dtos) > n:
            return calendar_account_write_dtos(self.dtos[:n])
        else:
            return calendar_account_write_dtos(self.dtos)
    def get_last(self) -> calendar_account_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, calendar_account_write_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[calendar_account_write_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[calendar_account_write_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def check_any(self, check_method: Callable[[calendar_account_write_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[calendar_account_write_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[calendar_account_write_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[calendar_account_write_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, calendar_account_write_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, calendar_account_write_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, calendar_account_write_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[calendar_account_write_dto], bool]) -> calendar_account_write_dtos:
        return calendar_account_write_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[calendar_account_write_dto], str]) -> dict[str, calendar_account_write_dtos]:
        grp_data: dict[str, calendar_account_write_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = calendar_account_write_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[calendar_account_write_dto], str], agg_method: Callable[[calendar_account_write_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, calendar_account_write_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[calendar_account_write_dto], bool]) -> calendar_account_write_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[calendar_account_write_dto], any], compare_method: Callable[[any, any], bool]) -> calendar_account_write_dto | None:
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
class calendar_approval_write_dtos(base_write_dtos):
    dtos: list[calendar_approval_write_dto]
    def __init__(self, dtos: list[calendar_approval_write_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[calendar_approval_write_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: calendar_approval_write_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[calendar_approval_write_dto], dtos2: list[calendar_approval_write_dto]):
        return cls(dtos1 + dtos2)
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> calendar_approval_write_dto | None:
        found_dtos = list(filter(lambda x: x.calendar_approval_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, calendar_approval_write_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.calendar_approval_uid] = dto
        return res
    def get_active(self):
        return calendar_approval_write_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return calendar_approval_write_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_first(self) -> calendar_approval_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> calendar_approval_write_dtos:
        if len(self.dtos) > n:
            return calendar_approval_write_dtos(self.dtos[:n])
        else:
            return calendar_approval_write_dtos(self.dtos)
    def get_last(self) -> calendar_approval_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, calendar_approval_write_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[calendar_approval_write_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[calendar_approval_write_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def check_any(self, check_method: Callable[[calendar_approval_write_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[calendar_approval_write_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[calendar_approval_write_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[calendar_approval_write_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, calendar_approval_write_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, calendar_approval_write_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, calendar_approval_write_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[calendar_approval_write_dto], bool]) -> calendar_approval_write_dtos:
        return calendar_approval_write_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[calendar_approval_write_dto], str]) -> dict[str, calendar_approval_write_dtos]:
        grp_data: dict[str, calendar_approval_write_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = calendar_approval_write_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[calendar_approval_write_dto], str], agg_method: Callable[[calendar_approval_write_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, calendar_approval_write_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[calendar_approval_write_dto], bool]) -> calendar_approval_write_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[calendar_approval_write_dto], any], compare_method: Callable[[any, any], bool]) -> calendar_approval_write_dto | None:
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
class calendar_approval_type_write_dtos(base_write_dtos):
    dtos: list[calendar_approval_type_write_dto]
    def __init__(self, dtos: list[calendar_approval_type_write_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[calendar_approval_type_write_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: calendar_approval_type_write_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[calendar_approval_type_write_dto], dtos2: list[calendar_approval_type_write_dto]):
        return cls(dtos1 + dtos2)
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> calendar_approval_type_write_dto | None:
        found_dtos = list(filter(lambda x: x.calendar_approval_type_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, calendar_approval_type_write_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.calendar_approval_type_uid] = dto
        return res
    def get_active(self):
        return calendar_approval_type_write_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return calendar_approval_type_write_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_first(self) -> calendar_approval_type_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> calendar_approval_type_write_dtos:
        if len(self.dtos) > n:
            return calendar_approval_type_write_dtos(self.dtos[:n])
        else:
            return calendar_approval_type_write_dtos(self.dtos)
    def get_last(self) -> calendar_approval_type_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, calendar_approval_type_write_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[calendar_approval_type_write_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[calendar_approval_type_write_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def check_any(self, check_method: Callable[[calendar_approval_type_write_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[calendar_approval_type_write_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[calendar_approval_type_write_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[calendar_approval_type_write_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, calendar_approval_type_write_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, calendar_approval_type_write_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, calendar_approval_type_write_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[calendar_approval_type_write_dto], bool]) -> calendar_approval_type_write_dtos:
        return calendar_approval_type_write_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[calendar_approval_type_write_dto], str]) -> dict[str, calendar_approval_type_write_dtos]:
        grp_data: dict[str, calendar_approval_type_write_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = calendar_approval_type_write_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[calendar_approval_type_write_dto], str], agg_method: Callable[[calendar_approval_type_write_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, calendar_approval_type_write_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[calendar_approval_type_write_dto], bool]) -> calendar_approval_type_write_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[calendar_approval_type_write_dto], any], compare_method: Callable[[any, any], bool]) -> calendar_approval_type_write_dto | None:
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
class calendar_event_write_dtos(base_write_dtos):
    dtos: list[calendar_event_write_dto]
    def __init__(self, dtos: list[calendar_event_write_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[calendar_event_write_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: calendar_event_write_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[calendar_event_write_dto], dtos2: list[calendar_event_write_dto]):
        return cls(dtos1 + dtos2)
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> calendar_event_write_dto | None:
        found_dtos = list(filter(lambda x: x.calendar_event_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, calendar_event_write_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.calendar_event_uid] = dto
        return res
    def get_active(self):
        return calendar_event_write_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return calendar_event_write_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_first(self) -> calendar_event_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> calendar_event_write_dtos:
        if len(self.dtos) > n:
            return calendar_event_write_dtos(self.dtos[:n])
        else:
            return calendar_event_write_dtos(self.dtos)
    def get_last(self) -> calendar_event_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, calendar_event_write_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[calendar_event_write_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[calendar_event_write_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def check_any(self, check_method: Callable[[calendar_event_write_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[calendar_event_write_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[calendar_event_write_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[calendar_event_write_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, calendar_event_write_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, calendar_event_write_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, calendar_event_write_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[calendar_event_write_dto], bool]) -> calendar_event_write_dtos:
        return calendar_event_write_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[calendar_event_write_dto], str]) -> dict[str, calendar_event_write_dtos]:
        grp_data: dict[str, calendar_event_write_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = calendar_event_write_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[calendar_event_write_dto], str], agg_method: Callable[[calendar_event_write_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, calendar_event_write_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[calendar_event_write_dto], bool]) -> calendar_event_write_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[calendar_event_write_dto], any], compare_method: Callable[[any, any], bool]) -> calendar_event_write_dto | None:
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
class calendar_event_group_write_dtos(base_write_dtos):
    dtos: list[calendar_event_group_write_dto]
    def __init__(self, dtos: list[calendar_event_group_write_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[calendar_event_group_write_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: calendar_event_group_write_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[calendar_event_group_write_dto], dtos2: list[calendar_event_group_write_dto]):
        return cls(dtos1 + dtos2)
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> calendar_event_group_write_dto | None:
        found_dtos = list(filter(lambda x: x.calendar_event_group_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, calendar_event_group_write_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.calendar_event_group_uid] = dto
        return res
    def get_active(self):
        return calendar_event_group_write_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return calendar_event_group_write_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_first(self) -> calendar_event_group_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> calendar_event_group_write_dtos:
        if len(self.dtos) > n:
            return calendar_event_group_write_dtos(self.dtos[:n])
        else:
            return calendar_event_group_write_dtos(self.dtos)
    def get_last(self) -> calendar_event_group_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, calendar_event_group_write_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[calendar_event_group_write_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[calendar_event_group_write_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def check_any(self, check_method: Callable[[calendar_event_group_write_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[calendar_event_group_write_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[calendar_event_group_write_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[calendar_event_group_write_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, calendar_event_group_write_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, calendar_event_group_write_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, calendar_event_group_write_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[calendar_event_group_write_dto], bool]) -> calendar_event_group_write_dtos:
        return calendar_event_group_write_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[calendar_event_group_write_dto], str]) -> dict[str, calendar_event_group_write_dtos]:
        grp_data: dict[str, calendar_event_group_write_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = calendar_event_group_write_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[calendar_event_group_write_dto], str], agg_method: Callable[[calendar_event_group_write_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, calendar_event_group_write_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[calendar_event_group_write_dto], bool]) -> calendar_event_group_write_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[calendar_event_group_write_dto], any], compare_method: Callable[[any, any], bool]) -> calendar_event_group_write_dto | None:
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
class calendar_event_type_write_dtos(base_write_dtos):
    dtos: list[calendar_event_type_write_dto]
    def __init__(self, dtos: list[calendar_event_type_write_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[calendar_event_type_write_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: calendar_event_type_write_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[calendar_event_type_write_dto], dtos2: list[calendar_event_type_write_dto]):
        return cls(dtos1 + dtos2)
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> calendar_event_type_write_dto | None:
        found_dtos = list(filter(lambda x: x.calendar_event_type_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, calendar_event_type_write_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.calendar_event_type_uid] = dto
        return res
    def get_active(self):
        return calendar_event_type_write_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return calendar_event_type_write_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_first(self) -> calendar_event_type_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> calendar_event_type_write_dtos:
        if len(self.dtos) > n:
            return calendar_event_type_write_dtos(self.dtos[:n])
        else:
            return calendar_event_type_write_dtos(self.dtos)
    def get_last(self) -> calendar_event_type_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, calendar_event_type_write_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[calendar_event_type_write_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[calendar_event_type_write_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def check_any(self, check_method: Callable[[calendar_event_type_write_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[calendar_event_type_write_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[calendar_event_type_write_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[calendar_event_type_write_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, calendar_event_type_write_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, calendar_event_type_write_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, calendar_event_type_write_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[calendar_event_type_write_dto], bool]) -> calendar_event_type_write_dtos:
        return calendar_event_type_write_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[calendar_event_type_write_dto], str]) -> dict[str, calendar_event_type_write_dtos]:
        grp_data: dict[str, calendar_event_type_write_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = calendar_event_type_write_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[calendar_event_type_write_dto], str], agg_method: Callable[[calendar_event_type_write_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, calendar_event_type_write_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[calendar_event_type_write_dto], bool]) -> calendar_event_type_write_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[calendar_event_type_write_dto], any], compare_method: Callable[[any, any], bool]) -> calendar_event_type_write_dto | None:
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
class calendar_type_write_dtos(base_write_dtos):
    dtos: list[calendar_type_write_dto]
    def __init__(self, dtos: list[calendar_type_write_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[calendar_type_write_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: calendar_type_write_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[calendar_type_write_dto], dtos2: list[calendar_type_write_dto]):
        return cls(dtos1 + dtos2)
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> calendar_type_write_dto | None:
        found_dtos = list(filter(lambda x: x.calendar_type_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, calendar_type_write_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.calendar_type_uid] = dto
        return res
    def get_active(self):
        return calendar_type_write_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return calendar_type_write_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_first(self) -> calendar_type_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> calendar_type_write_dtos:
        if len(self.dtos) > n:
            return calendar_type_write_dtos(self.dtos[:n])
        else:
            return calendar_type_write_dtos(self.dtos)
    def get_last(self) -> calendar_type_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, calendar_type_write_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[calendar_type_write_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[calendar_type_write_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def check_any(self, check_method: Callable[[calendar_type_write_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[calendar_type_write_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[calendar_type_write_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[calendar_type_write_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, calendar_type_write_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, calendar_type_write_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, calendar_type_write_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[calendar_type_write_dto], bool]) -> calendar_type_write_dtos:
        return calendar_type_write_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[calendar_type_write_dto], str]) -> dict[str, calendar_type_write_dtos]:
        grp_data: dict[str, calendar_type_write_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = calendar_type_write_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[calendar_type_write_dto], str], agg_method: Callable[[calendar_type_write_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, calendar_type_write_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[calendar_type_write_dto], bool]) -> calendar_type_write_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[calendar_type_write_dto], any], compare_method: Callable[[any, any], bool]) -> calendar_type_write_dto | None:
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
class client_write_dtos(base_write_dtos):
    dtos: list[client_write_dto]
    def __init__(self, dtos: list[client_write_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[client_write_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: client_write_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[client_write_dto], dtos2: list[client_write_dto]):
        return cls(dtos1 + dtos2)
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> client_write_dto | None:
        found_dtos = list(filter(lambda x: x.client_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, client_write_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.client_uid] = dto
        return res
    def get_active(self):
        return client_write_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return client_write_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_first(self) -> client_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> client_write_dtos:
        if len(self.dtos) > n:
            return client_write_dtos(self.dtos[:n])
        else:
            return client_write_dtos(self.dtos)
    def get_last(self) -> client_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, client_write_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[client_write_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[client_write_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def check_any(self, check_method: Callable[[client_write_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[client_write_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[client_write_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[client_write_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, client_write_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, client_write_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, client_write_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[client_write_dto], bool]) -> client_write_dtos:
        return client_write_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[client_write_dto], str]) -> dict[str, client_write_dtos]:
        grp_data: dict[str, client_write_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = client_write_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[client_write_dto], str], agg_method: Callable[[client_write_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, client_write_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[client_write_dto], bool]) -> client_write_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[client_write_dto], any], compare_method: Callable[[any, any], bool]) -> client_write_dto | None:
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
class client_account_write_dtos(base_write_dtos):
    dtos: list[client_account_write_dto]
    def __init__(self, dtos: list[client_account_write_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[client_account_write_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: client_account_write_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[client_account_write_dto], dtos2: list[client_account_write_dto]):
        return cls(dtos1 + dtos2)
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> client_account_write_dto | None:
        found_dtos = list(filter(lambda x: x.client_account_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, client_account_write_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.client_account_uid] = dto
        return res
    def get_active(self):
        return client_account_write_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return client_account_write_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_first(self) -> client_account_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> client_account_write_dtos:
        if len(self.dtos) > n:
            return client_account_write_dtos(self.dtos[:n])
        else:
            return client_account_write_dtos(self.dtos)
    def get_last(self) -> client_account_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, client_account_write_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[client_account_write_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[client_account_write_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def check_any(self, check_method: Callable[[client_account_write_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[client_account_write_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[client_account_write_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[client_account_write_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, client_account_write_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, client_account_write_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, client_account_write_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[client_account_write_dto], bool]) -> client_account_write_dtos:
        return client_account_write_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[client_account_write_dto], str]) -> dict[str, client_account_write_dtos]:
        grp_data: dict[str, client_account_write_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = client_account_write_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[client_account_write_dto], str], agg_method: Callable[[client_account_write_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, client_account_write_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[client_account_write_dto], bool]) -> client_account_write_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[client_account_write_dto], any], compare_method: Callable[[any, any], bool]) -> client_account_write_dto | None:
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
class client_contract_write_dtos(base_write_dtos):
    dtos: list[client_contract_write_dto]
    def __init__(self, dtos: list[client_contract_write_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[client_contract_write_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: client_contract_write_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[client_contract_write_dto], dtos2: list[client_contract_write_dto]):
        return cls(dtos1 + dtos2)
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> client_contract_write_dto | None:
        found_dtos = list(filter(lambda x: x.client_contract_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, client_contract_write_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.client_contract_uid] = dto
        return res
    def get_active(self):
        return client_contract_write_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return client_contract_write_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_first(self) -> client_contract_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> client_contract_write_dtos:
        if len(self.dtos) > n:
            return client_contract_write_dtos(self.dtos[:n])
        else:
            return client_contract_write_dtos(self.dtos)
    def get_last(self) -> client_contract_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, client_contract_write_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[client_contract_write_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[client_contract_write_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def check_any(self, check_method: Callable[[client_contract_write_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[client_contract_write_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[client_contract_write_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[client_contract_write_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, client_contract_write_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, client_contract_write_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, client_contract_write_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[client_contract_write_dto], bool]) -> client_contract_write_dtos:
        return client_contract_write_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[client_contract_write_dto], str]) -> dict[str, client_contract_write_dtos]:
        grp_data: dict[str, client_contract_write_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = client_contract_write_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[client_contract_write_dto], str], agg_method: Callable[[client_contract_write_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, client_contract_write_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[client_contract_write_dto], bool]) -> client_contract_write_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[client_contract_write_dto], any], compare_method: Callable[[any, any], bool]) -> client_contract_write_dto | None:
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
class client_country_write_dtos(base_write_dtos):
    dtos: list[client_country_write_dto]
    def __init__(self, dtos: list[client_country_write_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[client_country_write_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: client_country_write_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[client_country_write_dto], dtos2: list[client_country_write_dto]):
        return cls(dtos1 + dtos2)
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> client_country_write_dto | None:
        found_dtos = list(filter(lambda x: x.client_country_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, client_country_write_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.client_country_uid] = dto
        return res
    def get_active(self):
        return client_country_write_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return client_country_write_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_first(self) -> client_country_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> client_country_write_dtos:
        if len(self.dtos) > n:
            return client_country_write_dtos(self.dtos[:n])
        else:
            return client_country_write_dtos(self.dtos)
    def get_last(self) -> client_country_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, client_country_write_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[client_country_write_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[client_country_write_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def check_any(self, check_method: Callable[[client_country_write_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[client_country_write_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[client_country_write_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[client_country_write_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, client_country_write_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, client_country_write_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, client_country_write_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[client_country_write_dto], bool]) -> client_country_write_dtos:
        return client_country_write_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[client_country_write_dto], str]) -> dict[str, client_country_write_dtos]:
        grp_data: dict[str, client_country_write_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = client_country_write_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[client_country_write_dto], str], agg_method: Callable[[client_country_write_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, client_country_write_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[client_country_write_dto], bool]) -> client_country_write_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[client_country_write_dto], any], compare_method: Callable[[any, any], bool]) -> client_country_write_dto | None:
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
class client_payment_write_dtos(base_write_dtos):
    dtos: list[client_payment_write_dto]
    def __init__(self, dtos: list[client_payment_write_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[client_payment_write_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: client_payment_write_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[client_payment_write_dto], dtos2: list[client_payment_write_dto]):
        return cls(dtos1 + dtos2)
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> client_payment_write_dto | None:
        found_dtos = list(filter(lambda x: x.client_payment_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, client_payment_write_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.client_payment_uid] = dto
        return res
    def get_active(self):
        return client_payment_write_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return client_payment_write_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_first(self) -> client_payment_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> client_payment_write_dtos:
        if len(self.dtos) > n:
            return client_payment_write_dtos(self.dtos[:n])
        else:
            return client_payment_write_dtos(self.dtos)
    def get_last(self) -> client_payment_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, client_payment_write_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[client_payment_write_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[client_payment_write_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def check_any(self, check_method: Callable[[client_payment_write_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[client_payment_write_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[client_payment_write_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[client_payment_write_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, client_payment_write_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, client_payment_write_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, client_payment_write_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[client_payment_write_dto], bool]) -> client_payment_write_dtos:
        return client_payment_write_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[client_payment_write_dto], str]) -> dict[str, client_payment_write_dtos]:
        grp_data: dict[str, client_payment_write_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = client_payment_write_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[client_payment_write_dto], str], agg_method: Callable[[client_payment_write_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, client_payment_write_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[client_payment_write_dto], bool]) -> client_payment_write_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[client_payment_write_dto], any], compare_method: Callable[[any, any], bool]) -> client_payment_write_dto | None:
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
class client_role_write_dtos(base_write_dtos):
    dtos: list[client_role_write_dto]
    def __init__(self, dtos: list[client_role_write_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[client_role_write_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: client_role_write_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[client_role_write_dto], dtos2: list[client_role_write_dto]):
        return cls(dtos1 + dtos2)
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> client_role_write_dto | None:
        found_dtos = list(filter(lambda x: x.client_role_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, client_role_write_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.client_role_uid] = dto
        return res
    def get_active(self):
        return client_role_write_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return client_role_write_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_first(self) -> client_role_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> client_role_write_dtos:
        if len(self.dtos) > n:
            return client_role_write_dtos(self.dtos[:n])
        else:
            return client_role_write_dtos(self.dtos)
    def get_last(self) -> client_role_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, client_role_write_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[client_role_write_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[client_role_write_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def check_any(self, check_method: Callable[[client_role_write_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[client_role_write_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[client_role_write_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[client_role_write_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, client_role_write_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, client_role_write_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, client_role_write_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[client_role_write_dto], bool]) -> client_role_write_dtos:
        return client_role_write_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[client_role_write_dto], str]) -> dict[str, client_role_write_dtos]:
        grp_data: dict[str, client_role_write_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = client_role_write_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[client_role_write_dto], str], agg_method: Callable[[client_role_write_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, client_role_write_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[client_role_write_dto], bool]) -> client_role_write_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[client_role_write_dto], any], compare_method: Callable[[any, any], bool]) -> client_role_write_dto | None:
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
class client_status_write_dtos(base_write_dtos):
    dtos: list[client_status_write_dto]
    def __init__(self, dtos: list[client_status_write_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[client_status_write_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: client_status_write_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[client_status_write_dto], dtos2: list[client_status_write_dto]):
        return cls(dtos1 + dtos2)
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> client_status_write_dto | None:
        found_dtos = list(filter(lambda x: x.client_status_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, client_status_write_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.client_status_uid] = dto
        return res
    def get_active(self):
        return client_status_write_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return client_status_write_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_first(self) -> client_status_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> client_status_write_dtos:
        if len(self.dtos) > n:
            return client_status_write_dtos(self.dtos[:n])
        else:
            return client_status_write_dtos(self.dtos)
    def get_last(self) -> client_status_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, client_status_write_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[client_status_write_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[client_status_write_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def check_any(self, check_method: Callable[[client_status_write_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[client_status_write_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[client_status_write_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[client_status_write_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, client_status_write_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, client_status_write_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, client_status_write_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[client_status_write_dto], bool]) -> client_status_write_dtos:
        return client_status_write_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[client_status_write_dto], str]) -> dict[str, client_status_write_dtos]:
        grp_data: dict[str, client_status_write_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = client_status_write_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[client_status_write_dto], str], agg_method: Callable[[client_status_write_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, client_status_write_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[client_status_write_dto], bool]) -> client_status_write_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[client_status_write_dto], any], compare_method: Callable[[any, any], bool]) -> client_status_write_dto | None:
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
class client_type_write_dtos(base_write_dtos):
    dtos: list[client_type_write_dto]
    def __init__(self, dtos: list[client_type_write_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[client_type_write_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: client_type_write_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[client_type_write_dto], dtos2: list[client_type_write_dto]):
        return cls(dtos1 + dtos2)
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> client_type_write_dto | None:
        found_dtos = list(filter(lambda x: x.client_type_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, client_type_write_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.client_type_uid] = dto
        return res
    def get_active(self):
        return client_type_write_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return client_type_write_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_first(self) -> client_type_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> client_type_write_dtos:
        if len(self.dtos) > n:
            return client_type_write_dtos(self.dtos[:n])
        else:
            return client_type_write_dtos(self.dtos)
    def get_last(self) -> client_type_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, client_type_write_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[client_type_write_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[client_type_write_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def check_any(self, check_method: Callable[[client_type_write_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[client_type_write_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[client_type_write_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[client_type_write_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, client_type_write_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, client_type_write_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, client_type_write_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[client_type_write_dto], bool]) -> client_type_write_dtos:
        return client_type_write_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[client_type_write_dto], str]) -> dict[str, client_type_write_dtos]:
        grp_data: dict[str, client_type_write_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = client_type_write_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[client_type_write_dto], str], agg_method: Callable[[client_type_write_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, client_type_write_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[client_type_write_dto], bool]) -> client_type_write_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[client_type_write_dto], any], compare_method: Callable[[any, any], bool]) -> client_type_write_dto | None:
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
class competency_entry_write_dtos(base_write_dtos):
    dtos: list[competency_entry_write_dto]
    def __init__(self, dtos: list[competency_entry_write_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[competency_entry_write_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: competency_entry_write_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[competency_entry_write_dto], dtos2: list[competency_entry_write_dto]):
        return cls(dtos1 + dtos2)
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> competency_entry_write_dto | None:
        found_dtos = list(filter(lambda x: x.competency_entry_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, competency_entry_write_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.competency_entry_uid] = dto
        return res
    def get_active(self):
        return competency_entry_write_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return competency_entry_write_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_first(self) -> competency_entry_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> competency_entry_write_dtos:
        if len(self.dtos) > n:
            return competency_entry_write_dtos(self.dtos[:n])
        else:
            return competency_entry_write_dtos(self.dtos)
    def get_last(self) -> competency_entry_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, competency_entry_write_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[competency_entry_write_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[competency_entry_write_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def check_any(self, check_method: Callable[[competency_entry_write_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[competency_entry_write_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[competency_entry_write_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[competency_entry_write_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, competency_entry_write_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, competency_entry_write_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, competency_entry_write_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[competency_entry_write_dto], bool]) -> competency_entry_write_dtos:
        return competency_entry_write_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[competency_entry_write_dto], str]) -> dict[str, competency_entry_write_dtos]:
        grp_data: dict[str, competency_entry_write_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = competency_entry_write_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[competency_entry_write_dto], str], agg_method: Callable[[competency_entry_write_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, competency_entry_write_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[competency_entry_write_dto], bool]) -> competency_entry_write_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[competency_entry_write_dto], any], compare_method: Callable[[any, any], bool]) -> competency_entry_write_dto | None:
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
class competency_entry_account_write_dtos(base_write_dtos):
    dtos: list[competency_entry_account_write_dto]
    def __init__(self, dtos: list[competency_entry_account_write_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[competency_entry_account_write_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: competency_entry_account_write_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[competency_entry_account_write_dto], dtos2: list[competency_entry_account_write_dto]):
        return cls(dtos1 + dtos2)
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> competency_entry_account_write_dto | None:
        found_dtos = list(filter(lambda x: x.competency_entry_account_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, competency_entry_account_write_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.competency_entry_account_uid] = dto
        return res
    def get_active(self):
        return competency_entry_account_write_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return competency_entry_account_write_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_first(self) -> competency_entry_account_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> competency_entry_account_write_dtos:
        if len(self.dtos) > n:
            return competency_entry_account_write_dtos(self.dtos[:n])
        else:
            return competency_entry_account_write_dtos(self.dtos)
    def get_last(self) -> competency_entry_account_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, competency_entry_account_write_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[competency_entry_account_write_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[competency_entry_account_write_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def check_any(self, check_method: Callable[[competency_entry_account_write_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[competency_entry_account_write_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[competency_entry_account_write_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[competency_entry_account_write_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, competency_entry_account_write_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, competency_entry_account_write_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, competency_entry_account_write_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[competency_entry_account_write_dto], bool]) -> competency_entry_account_write_dtos:
        return competency_entry_account_write_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[competency_entry_account_write_dto], str]) -> dict[str, competency_entry_account_write_dtos]:
        grp_data: dict[str, competency_entry_account_write_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = competency_entry_account_write_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[competency_entry_account_write_dto], str], agg_method: Callable[[competency_entry_account_write_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, competency_entry_account_write_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[competency_entry_account_write_dto], bool]) -> competency_entry_account_write_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[competency_entry_account_write_dto], any], compare_method: Callable[[any, any], bool]) -> competency_entry_account_write_dto | None:
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
class competency_group_write_dtos(base_write_dtos):
    dtos: list[competency_group_write_dto]
    def __init__(self, dtos: list[competency_group_write_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[competency_group_write_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: competency_group_write_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[competency_group_write_dto], dtos2: list[competency_group_write_dto]):
        return cls(dtos1 + dtos2)
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> competency_group_write_dto | None:
        found_dtos = list(filter(lambda x: x.competency_group_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, competency_group_write_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.competency_group_uid] = dto
        return res
    def get_active(self):
        return competency_group_write_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return competency_group_write_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_first(self) -> competency_group_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> competency_group_write_dtos:
        if len(self.dtos) > n:
            return competency_group_write_dtos(self.dtos[:n])
        else:
            return competency_group_write_dtos(self.dtos)
    def get_last(self) -> competency_group_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, competency_group_write_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[competency_group_write_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[competency_group_write_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def check_any(self, check_method: Callable[[competency_group_write_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[competency_group_write_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[competency_group_write_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[competency_group_write_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, competency_group_write_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, competency_group_write_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, competency_group_write_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[competency_group_write_dto], bool]) -> competency_group_write_dtos:
        return competency_group_write_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[competency_group_write_dto], str]) -> dict[str, competency_group_write_dtos]:
        grp_data: dict[str, competency_group_write_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = competency_group_write_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[competency_group_write_dto], str], agg_method: Callable[[competency_group_write_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, competency_group_write_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[competency_group_write_dto], bool]) -> competency_group_write_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[competency_group_write_dto], any], compare_method: Callable[[any, any], bool]) -> competency_group_write_dto | None:
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
class competency_group_account_write_dtos(base_write_dtos):
    dtos: list[competency_group_account_write_dto]
    def __init__(self, dtos: list[competency_group_account_write_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[competency_group_account_write_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: competency_group_account_write_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[competency_group_account_write_dto], dtos2: list[competency_group_account_write_dto]):
        return cls(dtos1 + dtos2)
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> competency_group_account_write_dto | None:
        found_dtos = list(filter(lambda x: x.competency_group_account_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, competency_group_account_write_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.competency_group_account_uid] = dto
        return res
    def get_active(self):
        return competency_group_account_write_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return competency_group_account_write_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_first(self) -> competency_group_account_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> competency_group_account_write_dtos:
        if len(self.dtos) > n:
            return competency_group_account_write_dtos(self.dtos[:n])
        else:
            return competency_group_account_write_dtos(self.dtos)
    def get_last(self) -> competency_group_account_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, competency_group_account_write_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[competency_group_account_write_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[competency_group_account_write_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def check_any(self, check_method: Callable[[competency_group_account_write_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[competency_group_account_write_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[competency_group_account_write_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[competency_group_account_write_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, competency_group_account_write_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, competency_group_account_write_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, competency_group_account_write_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[competency_group_account_write_dto], bool]) -> competency_group_account_write_dtos:
        return competency_group_account_write_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[competency_group_account_write_dto], str]) -> dict[str, competency_group_account_write_dtos]:
        grp_data: dict[str, competency_group_account_write_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = competency_group_account_write_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[competency_group_account_write_dto], str], agg_method: Callable[[competency_group_account_write_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, competency_group_account_write_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[competency_group_account_write_dto], bool]) -> competency_group_account_write_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[competency_group_account_write_dto], any], compare_method: Callable[[any, any], bool]) -> competency_group_account_write_dto | None:
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
class competency_group_type_write_dtos(base_write_dtos):
    dtos: list[competency_group_type_write_dto]
    def __init__(self, dtos: list[competency_group_type_write_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[competency_group_type_write_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: competency_group_type_write_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[competency_group_type_write_dto], dtos2: list[competency_group_type_write_dto]):
        return cls(dtos1 + dtos2)
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> competency_group_type_write_dto | None:
        found_dtos = list(filter(lambda x: x.competency_group_type_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, competency_group_type_write_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.competency_group_type_uid] = dto
        return res
    def get_active(self):
        return competency_group_type_write_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return competency_group_type_write_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_first(self) -> competency_group_type_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> competency_group_type_write_dtos:
        if len(self.dtos) > n:
            return competency_group_type_write_dtos(self.dtos[:n])
        else:
            return competency_group_type_write_dtos(self.dtos)
    def get_last(self) -> competency_group_type_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, competency_group_type_write_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[competency_group_type_write_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[competency_group_type_write_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def check_any(self, check_method: Callable[[competency_group_type_write_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[competency_group_type_write_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[competency_group_type_write_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[competency_group_type_write_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, competency_group_type_write_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, competency_group_type_write_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, competency_group_type_write_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[competency_group_type_write_dto], bool]) -> competency_group_type_write_dtos:
        return competency_group_type_write_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[competency_group_type_write_dto], str]) -> dict[str, competency_group_type_write_dtos]:
        grp_data: dict[str, competency_group_type_write_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = competency_group_type_write_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[competency_group_type_write_dto], str], agg_method: Callable[[competency_group_type_write_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, competency_group_type_write_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[competency_group_type_write_dto], bool]) -> competency_group_type_write_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[competency_group_type_write_dto], any], compare_method: Callable[[any, any], bool]) -> competency_group_type_write_dto | None:
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
class competency_item_write_dtos(base_write_dtos):
    dtos: list[competency_item_write_dto]
    def __init__(self, dtos: list[competency_item_write_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[competency_item_write_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: competency_item_write_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[competency_item_write_dto], dtos2: list[competency_item_write_dto]):
        return cls(dtos1 + dtos2)
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> competency_item_write_dto | None:
        found_dtos = list(filter(lambda x: x.competency_item_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, competency_item_write_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.competency_item_uid] = dto
        return res
    def get_active(self):
        return competency_item_write_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return competency_item_write_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_first(self) -> competency_item_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> competency_item_write_dtos:
        if len(self.dtos) > n:
            return competency_item_write_dtos(self.dtos[:n])
        else:
            return competency_item_write_dtos(self.dtos)
    def get_last(self) -> competency_item_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, competency_item_write_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[competency_item_write_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[competency_item_write_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def check_any(self, check_method: Callable[[competency_item_write_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[competency_item_write_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[competency_item_write_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[competency_item_write_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, competency_item_write_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, competency_item_write_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, competency_item_write_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[competency_item_write_dto], bool]) -> competency_item_write_dtos:
        return competency_item_write_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[competency_item_write_dto], str]) -> dict[str, competency_item_write_dtos]:
        grp_data: dict[str, competency_item_write_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = competency_item_write_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[competency_item_write_dto], str], agg_method: Callable[[competency_item_write_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, competency_item_write_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[competency_item_write_dto], bool]) -> competency_item_write_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[competency_item_write_dto], any], compare_method: Callable[[any, any], bool]) -> competency_item_write_dto | None:
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
class competency_item_account_write_dtos(base_write_dtos):
    dtos: list[competency_item_account_write_dto]
    def __init__(self, dtos: list[competency_item_account_write_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[competency_item_account_write_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: competency_item_account_write_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[competency_item_account_write_dto], dtos2: list[competency_item_account_write_dto]):
        return cls(dtos1 + dtos2)
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> competency_item_account_write_dto | None:
        found_dtos = list(filter(lambda x: x.competency_item_account_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, competency_item_account_write_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.competency_item_account_uid] = dto
        return res
    def get_active(self):
        return competency_item_account_write_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return competency_item_account_write_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_first(self) -> competency_item_account_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> competency_item_account_write_dtos:
        if len(self.dtos) > n:
            return competency_item_account_write_dtos(self.dtos[:n])
        else:
            return competency_item_account_write_dtos(self.dtos)
    def get_last(self) -> competency_item_account_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, competency_item_account_write_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[competency_item_account_write_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[competency_item_account_write_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def check_any(self, check_method: Callable[[competency_item_account_write_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[competency_item_account_write_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[competency_item_account_write_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[competency_item_account_write_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, competency_item_account_write_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, competency_item_account_write_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, competency_item_account_write_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[competency_item_account_write_dto], bool]) -> competency_item_account_write_dtos:
        return competency_item_account_write_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[competency_item_account_write_dto], str]) -> dict[str, competency_item_account_write_dtos]:
        grp_data: dict[str, competency_item_account_write_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = competency_item_account_write_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[competency_item_account_write_dto], str], agg_method: Callable[[competency_item_account_write_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, competency_item_account_write_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[competency_item_account_write_dto], bool]) -> competency_item_account_write_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[competency_item_account_write_dto], any], compare_method: Callable[[any, any], bool]) -> competency_item_account_write_dto | None:
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
class competency_item_type_write_dtos(base_write_dtos):
    dtos: list[competency_item_type_write_dto]
    def __init__(self, dtos: list[competency_item_type_write_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[competency_item_type_write_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: competency_item_type_write_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[competency_item_type_write_dto], dtos2: list[competency_item_type_write_dto]):
        return cls(dtos1 + dtos2)
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> competency_item_type_write_dto | None:
        found_dtos = list(filter(lambda x: x.competency_item_type_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, competency_item_type_write_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.competency_item_type_uid] = dto
        return res
    def get_active(self):
        return competency_item_type_write_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return competency_item_type_write_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_first(self) -> competency_item_type_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> competency_item_type_write_dtos:
        if len(self.dtos) > n:
            return competency_item_type_write_dtos(self.dtos[:n])
        else:
            return competency_item_type_write_dtos(self.dtos)
    def get_last(self) -> competency_item_type_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, competency_item_type_write_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[competency_item_type_write_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[competency_item_type_write_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def check_any(self, check_method: Callable[[competency_item_type_write_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[competency_item_type_write_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[competency_item_type_write_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[competency_item_type_write_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, competency_item_type_write_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, competency_item_type_write_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, competency_item_type_write_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[competency_item_type_write_dto], bool]) -> competency_item_type_write_dtos:
        return competency_item_type_write_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[competency_item_type_write_dto], str]) -> dict[str, competency_item_type_write_dtos]:
        grp_data: dict[str, competency_item_type_write_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = competency_item_type_write_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[competency_item_type_write_dto], str], agg_method: Callable[[competency_item_type_write_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, competency_item_type_write_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[competency_item_type_write_dto], bool]) -> competency_item_type_write_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[competency_item_type_write_dto], any], compare_method: Callable[[any, any], bool]) -> competency_item_type_write_dto | None:
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
class competency_process_write_dtos(base_write_dtos):
    dtos: list[competency_process_write_dto]
    def __init__(self, dtos: list[competency_process_write_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[competency_process_write_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: competency_process_write_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[competency_process_write_dto], dtos2: list[competency_process_write_dto]):
        return cls(dtos1 + dtos2)
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> competency_process_write_dto | None:
        found_dtos = list(filter(lambda x: x.competency_process_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, competency_process_write_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.competency_process_uid] = dto
        return res
    def get_active(self):
        return competency_process_write_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return competency_process_write_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_first(self) -> competency_process_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> competency_process_write_dtos:
        if len(self.dtos) > n:
            return competency_process_write_dtos(self.dtos[:n])
        else:
            return competency_process_write_dtos(self.dtos)
    def get_last(self) -> competency_process_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, competency_process_write_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[competency_process_write_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[competency_process_write_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def check_any(self, check_method: Callable[[competency_process_write_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[competency_process_write_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[competency_process_write_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[competency_process_write_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, competency_process_write_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, competency_process_write_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, competency_process_write_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[competency_process_write_dto], bool]) -> competency_process_write_dtos:
        return competency_process_write_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[competency_process_write_dto], str]) -> dict[str, competency_process_write_dtos]:
        grp_data: dict[str, competency_process_write_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = competency_process_write_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[competency_process_write_dto], str], agg_method: Callable[[competency_process_write_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, competency_process_write_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[competency_process_write_dto], bool]) -> competency_process_write_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[competency_process_write_dto], any], compare_method: Callable[[any, any], bool]) -> competency_process_write_dto | None:
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
class competency_process_account_write_dtos(base_write_dtos):
    dtos: list[competency_process_account_write_dto]
    def __init__(self, dtos: list[competency_process_account_write_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[competency_process_account_write_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: competency_process_account_write_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[competency_process_account_write_dto], dtos2: list[competency_process_account_write_dto]):
        return cls(dtos1 + dtos2)
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> competency_process_account_write_dto | None:
        found_dtos = list(filter(lambda x: x.competency_process_account_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, competency_process_account_write_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.competency_process_account_uid] = dto
        return res
    def get_active(self):
        return competency_process_account_write_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return competency_process_account_write_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_first(self) -> competency_process_account_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> competency_process_account_write_dtos:
        if len(self.dtos) > n:
            return competency_process_account_write_dtos(self.dtos[:n])
        else:
            return competency_process_account_write_dtos(self.dtos)
    def get_last(self) -> competency_process_account_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, competency_process_account_write_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[competency_process_account_write_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[competency_process_account_write_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def check_any(self, check_method: Callable[[competency_process_account_write_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[competency_process_account_write_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[competency_process_account_write_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[competency_process_account_write_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, competency_process_account_write_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, competency_process_account_write_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, competency_process_account_write_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[competency_process_account_write_dto], bool]) -> competency_process_account_write_dtos:
        return competency_process_account_write_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[competency_process_account_write_dto], str]) -> dict[str, competency_process_account_write_dtos]:
        grp_data: dict[str, competency_process_account_write_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = competency_process_account_write_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[competency_process_account_write_dto], str], agg_method: Callable[[competency_process_account_write_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, competency_process_account_write_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[competency_process_account_write_dto], bool]) -> competency_process_account_write_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[competency_process_account_write_dto], any], compare_method: Callable[[any, any], bool]) -> competency_process_account_write_dto | None:
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
class competency_process_type_write_dtos(base_write_dtos):
    dtos: list[competency_process_type_write_dto]
    def __init__(self, dtos: list[competency_process_type_write_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[competency_process_type_write_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: competency_process_type_write_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[competency_process_type_write_dto], dtos2: list[competency_process_type_write_dto]):
        return cls(dtos1 + dtos2)
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> competency_process_type_write_dto | None:
        found_dtos = list(filter(lambda x: x.competency_process_type_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, competency_process_type_write_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.competency_process_type_uid] = dto
        return res
    def get_active(self):
        return competency_process_type_write_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return competency_process_type_write_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_first(self) -> competency_process_type_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> competency_process_type_write_dtos:
        if len(self.dtos) > n:
            return competency_process_type_write_dtos(self.dtos[:n])
        else:
            return competency_process_type_write_dtos(self.dtos)
    def get_last(self) -> competency_process_type_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, competency_process_type_write_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[competency_process_type_write_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[competency_process_type_write_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def check_any(self, check_method: Callable[[competency_process_type_write_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[competency_process_type_write_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[competency_process_type_write_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[competency_process_type_write_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, competency_process_type_write_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, competency_process_type_write_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, competency_process_type_write_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[competency_process_type_write_dto], bool]) -> competency_process_type_write_dtos:
        return competency_process_type_write_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[competency_process_type_write_dto], str]) -> dict[str, competency_process_type_write_dtos]:
        grp_data: dict[str, competency_process_type_write_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = competency_process_type_write_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[competency_process_type_write_dto], str], agg_method: Callable[[competency_process_type_write_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, competency_process_type_write_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[competency_process_type_write_dto], bool]) -> competency_process_type_write_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[competency_process_type_write_dto], any], compare_method: Callable[[any, any], bool]) -> competency_process_type_write_dto | None:
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
class competency_ranking_write_dtos(base_write_dtos):
    dtos: list[competency_ranking_write_dto]
    def __init__(self, dtos: list[competency_ranking_write_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[competency_ranking_write_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: competency_ranking_write_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[competency_ranking_write_dto], dtos2: list[competency_ranking_write_dto]):
        return cls(dtos1 + dtos2)
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> competency_ranking_write_dto | None:
        found_dtos = list(filter(lambda x: x.competency_ranking_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, competency_ranking_write_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.competency_ranking_uid] = dto
        return res
    def get_active(self):
        return competency_ranking_write_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return competency_ranking_write_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_first(self) -> competency_ranking_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> competency_ranking_write_dtos:
        if len(self.dtos) > n:
            return competency_ranking_write_dtos(self.dtos[:n])
        else:
            return competency_ranking_write_dtos(self.dtos)
    def get_last(self) -> competency_ranking_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, competency_ranking_write_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[competency_ranking_write_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[competency_ranking_write_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def check_any(self, check_method: Callable[[competency_ranking_write_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[competency_ranking_write_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[competency_ranking_write_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[competency_ranking_write_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, competency_ranking_write_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, competency_ranking_write_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, competency_ranking_write_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[competency_ranking_write_dto], bool]) -> competency_ranking_write_dtos:
        return competency_ranking_write_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[competency_ranking_write_dto], str]) -> dict[str, competency_ranking_write_dtos]:
        grp_data: dict[str, competency_ranking_write_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = competency_ranking_write_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[competency_ranking_write_dto], str], agg_method: Callable[[competency_ranking_write_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, competency_ranking_write_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[competency_ranking_write_dto], bool]) -> competency_ranking_write_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[competency_ranking_write_dto], any], compare_method: Callable[[any, any], bool]) -> competency_ranking_write_dto | None:
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
class connection_engine_write_dtos(base_write_dtos):
    dtos: list[connection_engine_write_dto]
    def __init__(self, dtos: list[connection_engine_write_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[connection_engine_write_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: connection_engine_write_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[connection_engine_write_dto], dtos2: list[connection_engine_write_dto]):
        return cls(dtos1 + dtos2)
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> connection_engine_write_dto | None:
        found_dtos = list(filter(lambda x: x.connection_engine_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, connection_engine_write_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.connection_engine_uid] = dto
        return res
    def get_active(self):
        return connection_engine_write_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return connection_engine_write_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_first(self) -> connection_engine_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> connection_engine_write_dtos:
        if len(self.dtos) > n:
            return connection_engine_write_dtos(self.dtos[:n])
        else:
            return connection_engine_write_dtos(self.dtos)
    def get_last(self) -> connection_engine_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, connection_engine_write_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[connection_engine_write_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[connection_engine_write_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def check_any(self, check_method: Callable[[connection_engine_write_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[connection_engine_write_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[connection_engine_write_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[connection_engine_write_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, connection_engine_write_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, connection_engine_write_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, connection_engine_write_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[connection_engine_write_dto], bool]) -> connection_engine_write_dtos:
        return connection_engine_write_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[connection_engine_write_dto], str]) -> dict[str, connection_engine_write_dtos]:
        grp_data: dict[str, connection_engine_write_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = connection_engine_write_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[connection_engine_write_dto], str], agg_method: Callable[[connection_engine_write_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, connection_engine_write_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[connection_engine_write_dto], bool]) -> connection_engine_write_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[connection_engine_write_dto], any], compare_method: Callable[[any, any], bool]) -> connection_engine_write_dto | None:
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
class connection_host_write_dtos(base_write_dtos):
    dtos: list[connection_host_write_dto]
    def __init__(self, dtos: list[connection_host_write_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[connection_host_write_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: connection_host_write_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[connection_host_write_dto], dtos2: list[connection_host_write_dto]):
        return cls(dtos1 + dtos2)
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> connection_host_write_dto | None:
        found_dtos = list(filter(lambda x: x.connection_host_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, connection_host_write_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.connection_host_uid] = dto
        return res
    def get_active(self):
        return connection_host_write_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return connection_host_write_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_first(self) -> connection_host_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> connection_host_write_dtos:
        if len(self.dtos) > n:
            return connection_host_write_dtos(self.dtos[:n])
        else:
            return connection_host_write_dtos(self.dtos)
    def get_last(self) -> connection_host_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, connection_host_write_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[connection_host_write_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[connection_host_write_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def check_any(self, check_method: Callable[[connection_host_write_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[connection_host_write_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[connection_host_write_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[connection_host_write_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, connection_host_write_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, connection_host_write_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, connection_host_write_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[connection_host_write_dto], bool]) -> connection_host_write_dtos:
        return connection_host_write_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[connection_host_write_dto], str]) -> dict[str, connection_host_write_dtos]:
        grp_data: dict[str, connection_host_write_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = connection_host_write_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[connection_host_write_dto], str], agg_method: Callable[[connection_host_write_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, connection_host_write_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[connection_host_write_dto], bool]) -> connection_host_write_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[connection_host_write_dto], any], compare_method: Callable[[any, any], bool]) -> connection_host_write_dto | None:
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
class connection_tenant_write_dtos(base_write_dtos):
    dtos: list[connection_tenant_write_dto]
    def __init__(self, dtos: list[connection_tenant_write_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[connection_tenant_write_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: connection_tenant_write_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[connection_tenant_write_dto], dtos2: list[connection_tenant_write_dto]):
        return cls(dtos1 + dtos2)
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> connection_tenant_write_dto | None:
        found_dtos = list(filter(lambda x: x.connection_tenant_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, connection_tenant_write_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.connection_tenant_uid] = dto
        return res
    def get_active(self):
        return connection_tenant_write_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return connection_tenant_write_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_first(self) -> connection_tenant_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> connection_tenant_write_dtos:
        if len(self.dtos) > n:
            return connection_tenant_write_dtos(self.dtos[:n])
        else:
            return connection_tenant_write_dtos(self.dtos)
    def get_last(self) -> connection_tenant_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, connection_tenant_write_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[connection_tenant_write_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[connection_tenant_write_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def check_any(self, check_method: Callable[[connection_tenant_write_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[connection_tenant_write_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[connection_tenant_write_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[connection_tenant_write_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, connection_tenant_write_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, connection_tenant_write_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, connection_tenant_write_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[connection_tenant_write_dto], bool]) -> connection_tenant_write_dtos:
        return connection_tenant_write_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[connection_tenant_write_dto], str]) -> dict[str, connection_tenant_write_dtos]:
        grp_data: dict[str, connection_tenant_write_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = connection_tenant_write_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[connection_tenant_write_dto], str], agg_method: Callable[[connection_tenant_write_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, connection_tenant_write_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[connection_tenant_write_dto], bool]) -> connection_tenant_write_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[connection_tenant_write_dto], any], compare_method: Callable[[any, any], bool]) -> connection_tenant_write_dto | None:
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
class connection_user_write_dtos(base_write_dtos):
    dtos: list[connection_user_write_dto]
    def __init__(self, dtos: list[connection_user_write_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[connection_user_write_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: connection_user_write_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[connection_user_write_dto], dtos2: list[connection_user_write_dto]):
        return cls(dtos1 + dtos2)
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> connection_user_write_dto | None:
        found_dtos = list(filter(lambda x: x.connection_user_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, connection_user_write_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.connection_user_uid] = dto
        return res
    def get_active(self):
        return connection_user_write_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return connection_user_write_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_first(self) -> connection_user_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> connection_user_write_dtos:
        if len(self.dtos) > n:
            return connection_user_write_dtos(self.dtos[:n])
        else:
            return connection_user_write_dtos(self.dtos)
    def get_last(self) -> connection_user_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, connection_user_write_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[connection_user_write_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[connection_user_write_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def check_any(self, check_method: Callable[[connection_user_write_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[connection_user_write_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[connection_user_write_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[connection_user_write_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, connection_user_write_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, connection_user_write_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, connection_user_write_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[connection_user_write_dto], bool]) -> connection_user_write_dtos:
        return connection_user_write_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[connection_user_write_dto], str]) -> dict[str, connection_user_write_dtos]:
        grp_data: dict[str, connection_user_write_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = connection_user_write_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[connection_user_write_dto], str], agg_method: Callable[[connection_user_write_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, connection_user_write_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[connection_user_write_dto], bool]) -> connection_user_write_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[connection_user_write_dto], any], compare_method: Callable[[any, any], bool]) -> connection_user_write_dto | None:
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
class country_write_dtos(base_write_dtos):
    dtos: list[country_write_dto]
    def __init__(self, dtos: list[country_write_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[country_write_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: country_write_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[country_write_dto], dtos2: list[country_write_dto]):
        return cls(dtos1 + dtos2)
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> country_write_dto | None:
        found_dtos = list(filter(lambda x: x.country_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, country_write_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.country_uid] = dto
        return res
    def get_active(self):
        return country_write_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return country_write_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_first(self) -> country_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> country_write_dtos:
        if len(self.dtos) > n:
            return country_write_dtos(self.dtos[:n])
        else:
            return country_write_dtos(self.dtos)
    def get_last(self) -> country_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, country_write_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[country_write_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[country_write_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def check_any(self, check_method: Callable[[country_write_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[country_write_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[country_write_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[country_write_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, country_write_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, country_write_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, country_write_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[country_write_dto], bool]) -> country_write_dtos:
        return country_write_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[country_write_dto], str]) -> dict[str, country_write_dtos]:
        grp_data: dict[str, country_write_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = country_write_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[country_write_dto], str], agg_method: Callable[[country_write_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, country_write_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[country_write_dto], bool]) -> country_write_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[country_write_dto], any], compare_method: Callable[[any, any], bool]) -> country_write_dto | None:
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
class currency_write_dtos(base_write_dtos):
    dtos: list[currency_write_dto]
    def __init__(self, dtos: list[currency_write_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[currency_write_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: currency_write_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[currency_write_dto], dtos2: list[currency_write_dto]):
        return cls(dtos1 + dtos2)
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> currency_write_dto | None:
        found_dtos = list(filter(lambda x: x.currency_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, currency_write_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.currency_uid] = dto
        return res
    def get_active(self):
        return currency_write_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return currency_write_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_first(self) -> currency_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> currency_write_dtos:
        if len(self.dtos) > n:
            return currency_write_dtos(self.dtos[:n])
        else:
            return currency_write_dtos(self.dtos)
    def get_last(self) -> currency_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, currency_write_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[currency_write_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[currency_write_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def check_any(self, check_method: Callable[[currency_write_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[currency_write_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[currency_write_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[currency_write_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, currency_write_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, currency_write_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, currency_write_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[currency_write_dto], bool]) -> currency_write_dtos:
        return currency_write_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[currency_write_dto], str]) -> dict[str, currency_write_dtos]:
        grp_data: dict[str, currency_write_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = currency_write_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[currency_write_dto], str], agg_method: Callable[[currency_write_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, currency_write_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[currency_write_dto], bool]) -> currency_write_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[currency_write_dto], any], compare_method: Callable[[any, any], bool]) -> currency_write_dto | None:
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
class currency_rate_write_dtos(base_write_dtos):
    dtos: list[currency_rate_write_dto]
    def __init__(self, dtos: list[currency_rate_write_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[currency_rate_write_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: currency_rate_write_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[currency_rate_write_dto], dtos2: list[currency_rate_write_dto]):
        return cls(dtos1 + dtos2)
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> currency_rate_write_dto | None:
        found_dtos = list(filter(lambda x: x.currency_rate_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, currency_rate_write_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.currency_rate_uid] = dto
        return res
    def get_active(self):
        return currency_rate_write_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return currency_rate_write_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_first(self) -> currency_rate_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> currency_rate_write_dtos:
        if len(self.dtos) > n:
            return currency_rate_write_dtos(self.dtos[:n])
        else:
            return currency_rate_write_dtos(self.dtos)
    def get_last(self) -> currency_rate_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, currency_rate_write_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[currency_rate_write_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[currency_rate_write_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def check_any(self, check_method: Callable[[currency_rate_write_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[currency_rate_write_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[currency_rate_write_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[currency_rate_write_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, currency_rate_write_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, currency_rate_write_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, currency_rate_write_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[currency_rate_write_dto], bool]) -> currency_rate_write_dtos:
        return currency_rate_write_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[currency_rate_write_dto], str]) -> dict[str, currency_rate_write_dtos]:
        grp_data: dict[str, currency_rate_write_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = currency_rate_write_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[currency_rate_write_dto], str], agg_method: Callable[[currency_rate_write_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, currency_rate_write_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[currency_rate_write_dto], bool]) -> currency_rate_write_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[currency_rate_write_dto], any], compare_method: Callable[[any, any], bool]) -> currency_rate_write_dto | None:
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
class currency_source_write_dtos(base_write_dtos):
    dtos: list[currency_source_write_dto]
    def __init__(self, dtos: list[currency_source_write_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[currency_source_write_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: currency_source_write_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[currency_source_write_dto], dtos2: list[currency_source_write_dto]):
        return cls(dtos1 + dtos2)
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> currency_source_write_dto | None:
        found_dtos = list(filter(lambda x: x.currency_source_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, currency_source_write_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.currency_source_uid] = dto
        return res
    def get_active(self):
        return currency_source_write_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return currency_source_write_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_first(self) -> currency_source_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> currency_source_write_dtos:
        if len(self.dtos) > n:
            return currency_source_write_dtos(self.dtos[:n])
        else:
            return currency_source_write_dtos(self.dtos)
    def get_last(self) -> currency_source_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, currency_source_write_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[currency_source_write_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[currency_source_write_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def check_any(self, check_method: Callable[[currency_source_write_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[currency_source_write_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[currency_source_write_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[currency_source_write_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, currency_source_write_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, currency_source_write_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, currency_source_write_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[currency_source_write_dto], bool]) -> currency_source_write_dtos:
        return currency_source_write_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[currency_source_write_dto], str]) -> dict[str, currency_source_write_dtos]:
        grp_data: dict[str, currency_source_write_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = currency_source_write_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[currency_source_write_dto], str], agg_method: Callable[[currency_source_write_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, currency_source_write_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[currency_source_write_dto], bool]) -> currency_source_write_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[currency_source_write_dto], any], compare_method: Callable[[any, any], bool]) -> currency_source_write_dto | None:
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
class event_acknowledge_write_dtos(base_write_dtos):
    dtos: list[event_acknowledge_write_dto]
    def __init__(self, dtos: list[event_acknowledge_write_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[event_acknowledge_write_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: event_acknowledge_write_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[event_acknowledge_write_dto], dtos2: list[event_acknowledge_write_dto]):
        return cls(dtos1 + dtos2)
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> event_acknowledge_write_dto | None:
        found_dtos = list(filter(lambda x: x.event_acknowledge_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, event_acknowledge_write_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.event_acknowledge_uid] = dto
        return res
    def get_active(self):
        return event_acknowledge_write_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return event_acknowledge_write_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_first(self) -> event_acknowledge_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> event_acknowledge_write_dtos:
        if len(self.dtos) > n:
            return event_acknowledge_write_dtos(self.dtos[:n])
        else:
            return event_acknowledge_write_dtos(self.dtos)
    def get_last(self) -> event_acknowledge_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, event_acknowledge_write_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[event_acknowledge_write_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[event_acknowledge_write_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def check_any(self, check_method: Callable[[event_acknowledge_write_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[event_acknowledge_write_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[event_acknowledge_write_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[event_acknowledge_write_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, event_acknowledge_write_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, event_acknowledge_write_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, event_acknowledge_write_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[event_acknowledge_write_dto], bool]) -> event_acknowledge_write_dtos:
        return event_acknowledge_write_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[event_acknowledge_write_dto], str]) -> dict[str, event_acknowledge_write_dtos]:
        grp_data: dict[str, event_acknowledge_write_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = event_acknowledge_write_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[event_acknowledge_write_dto], str], agg_method: Callable[[event_acknowledge_write_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, event_acknowledge_write_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[event_acknowledge_write_dto], bool]) -> event_acknowledge_write_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[event_acknowledge_write_dto], any], compare_method: Callable[[any, any], bool]) -> event_acknowledge_write_dto | None:
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
class event_channel_write_dtos(base_write_dtos):
    dtos: list[event_channel_write_dto]
    def __init__(self, dtos: list[event_channel_write_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[event_channel_write_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: event_channel_write_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[event_channel_write_dto], dtos2: list[event_channel_write_dto]):
        return cls(dtos1 + dtos2)
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> event_channel_write_dto | None:
        found_dtos = list(filter(lambda x: x.event_channel_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, event_channel_write_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.event_channel_uid] = dto
        return res
    def get_active(self):
        return event_channel_write_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return event_channel_write_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_first(self) -> event_channel_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> event_channel_write_dtos:
        if len(self.dtos) > n:
            return event_channel_write_dtos(self.dtos[:n])
        else:
            return event_channel_write_dtos(self.dtos)
    def get_last(self) -> event_channel_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, event_channel_write_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[event_channel_write_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[event_channel_write_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def check_any(self, check_method: Callable[[event_channel_write_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[event_channel_write_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[event_channel_write_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[event_channel_write_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, event_channel_write_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, event_channel_write_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, event_channel_write_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[event_channel_write_dto], bool]) -> event_channel_write_dtos:
        return event_channel_write_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[event_channel_write_dto], str]) -> dict[str, event_channel_write_dtos]:
        grp_data: dict[str, event_channel_write_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = event_channel_write_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[event_channel_write_dto], str], agg_method: Callable[[event_channel_write_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, event_channel_write_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[event_channel_write_dto], bool]) -> event_channel_write_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[event_channel_write_dto], any], compare_method: Callable[[any, any], bool]) -> event_channel_write_dto | None:
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
class event_channel_type_write_dtos(base_write_dtos):
    dtos: list[event_channel_type_write_dto]
    def __init__(self, dtos: list[event_channel_type_write_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[event_channel_type_write_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: event_channel_type_write_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[event_channel_type_write_dto], dtos2: list[event_channel_type_write_dto]):
        return cls(dtos1 + dtos2)
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> event_channel_type_write_dto | None:
        found_dtos = list(filter(lambda x: x.event_channel_type_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, event_channel_type_write_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.event_channel_type_uid] = dto
        return res
    def get_active(self):
        return event_channel_type_write_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return event_channel_type_write_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_first(self) -> event_channel_type_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> event_channel_type_write_dtos:
        if len(self.dtos) > n:
            return event_channel_type_write_dtos(self.dtos[:n])
        else:
            return event_channel_type_write_dtos(self.dtos)
    def get_last(self) -> event_channel_type_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, event_channel_type_write_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[event_channel_type_write_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[event_channel_type_write_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def check_any(self, check_method: Callable[[event_channel_type_write_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[event_channel_type_write_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[event_channel_type_write_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[event_channel_type_write_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, event_channel_type_write_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, event_channel_type_write_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, event_channel_type_write_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[event_channel_type_write_dto], bool]) -> event_channel_type_write_dtos:
        return event_channel_type_write_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[event_channel_type_write_dto], str]) -> dict[str, event_channel_type_write_dtos]:
        grp_data: dict[str, event_channel_type_write_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = event_channel_type_write_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[event_channel_type_write_dto], str], agg_method: Callable[[event_channel_type_write_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, event_channel_type_write_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[event_channel_type_write_dto], bool]) -> event_channel_type_write_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[event_channel_type_write_dto], any], compare_method: Callable[[any, any], bool]) -> event_channel_type_write_dto | None:
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
class event_instance_write_dtos(base_write_dtos):
    dtos: list[event_instance_write_dto]
    def __init__(self, dtos: list[event_instance_write_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[event_instance_write_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: event_instance_write_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[event_instance_write_dto], dtos2: list[event_instance_write_dto]):
        return cls(dtos1 + dtos2)
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> event_instance_write_dto | None:
        found_dtos = list(filter(lambda x: x.event_instance_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, event_instance_write_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.event_instance_uid] = dto
        return res
    def get_active(self):
        return event_instance_write_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return event_instance_write_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_first(self) -> event_instance_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> event_instance_write_dtos:
        if len(self.dtos) > n:
            return event_instance_write_dtos(self.dtos[:n])
        else:
            return event_instance_write_dtos(self.dtos)
    def get_last(self) -> event_instance_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, event_instance_write_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[event_instance_write_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[event_instance_write_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def check_any(self, check_method: Callable[[event_instance_write_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[event_instance_write_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[event_instance_write_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[event_instance_write_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, event_instance_write_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, event_instance_write_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, event_instance_write_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[event_instance_write_dto], bool]) -> event_instance_write_dtos:
        return event_instance_write_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[event_instance_write_dto], str]) -> dict[str, event_instance_write_dtos]:
        grp_data: dict[str, event_instance_write_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = event_instance_write_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[event_instance_write_dto], str], agg_method: Callable[[event_instance_write_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, event_instance_write_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[event_instance_write_dto], bool]) -> event_instance_write_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[event_instance_write_dto], any], compare_method: Callable[[any, any], bool]) -> event_instance_write_dto | None:
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
class event_notification_write_dtos(base_write_dtos):
    dtos: list[event_notification_write_dto]
    def __init__(self, dtos: list[event_notification_write_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[event_notification_write_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: event_notification_write_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[event_notification_write_dto], dtos2: list[event_notification_write_dto]):
        return cls(dtos1 + dtos2)
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> event_notification_write_dto | None:
        found_dtos = list(filter(lambda x: x.event_notification_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, event_notification_write_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.event_notification_uid] = dto
        return res
    def get_active(self):
        return event_notification_write_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return event_notification_write_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_first(self) -> event_notification_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> event_notification_write_dtos:
        if len(self.dtos) > n:
            return event_notification_write_dtos(self.dtos[:n])
        else:
            return event_notification_write_dtos(self.dtos)
    def get_last(self) -> event_notification_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, event_notification_write_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[event_notification_write_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[event_notification_write_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def check_any(self, check_method: Callable[[event_notification_write_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[event_notification_write_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[event_notification_write_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[event_notification_write_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, event_notification_write_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, event_notification_write_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, event_notification_write_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[event_notification_write_dto], bool]) -> event_notification_write_dtos:
        return event_notification_write_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[event_notification_write_dto], str]) -> dict[str, event_notification_write_dtos]:
        grp_data: dict[str, event_notification_write_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = event_notification_write_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[event_notification_write_dto], str], agg_method: Callable[[event_notification_write_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, event_notification_write_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[event_notification_write_dto], bool]) -> event_notification_write_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[event_notification_write_dto], any], compare_method: Callable[[any, any], bool]) -> event_notification_write_dto | None:
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
class event_observer_write_dtos(base_write_dtos):
    dtos: list[event_observer_write_dto]
    def __init__(self, dtos: list[event_observer_write_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[event_observer_write_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: event_observer_write_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[event_observer_write_dto], dtos2: list[event_observer_write_dto]):
        return cls(dtos1 + dtos2)
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> event_observer_write_dto | None:
        found_dtos = list(filter(lambda x: x.event_observer_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, event_observer_write_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.event_observer_uid] = dto
        return res
    def get_active(self):
        return event_observer_write_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return event_observer_write_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_first(self) -> event_observer_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> event_observer_write_dtos:
        if len(self.dtos) > n:
            return event_observer_write_dtos(self.dtos[:n])
        else:
            return event_observer_write_dtos(self.dtos)
    def get_last(self) -> event_observer_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, event_observer_write_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[event_observer_write_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[event_observer_write_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def check_any(self, check_method: Callable[[event_observer_write_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[event_observer_write_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[event_observer_write_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[event_observer_write_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, event_observer_write_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, event_observer_write_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, event_observer_write_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[event_observer_write_dto], bool]) -> event_observer_write_dtos:
        return event_observer_write_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[event_observer_write_dto], str]) -> dict[str, event_observer_write_dtos]:
        grp_data: dict[str, event_observer_write_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = event_observer_write_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[event_observer_write_dto], str], agg_method: Callable[[event_observer_write_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, event_observer_write_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[event_observer_write_dto], bool]) -> event_observer_write_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[event_observer_write_dto], any], compare_method: Callable[[any, any], bool]) -> event_observer_write_dto | None:
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
class event_subscription_write_dtos(base_write_dtos):
    dtos: list[event_subscription_write_dto]
    def __init__(self, dtos: list[event_subscription_write_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[event_subscription_write_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: event_subscription_write_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[event_subscription_write_dto], dtos2: list[event_subscription_write_dto]):
        return cls(dtos1 + dtos2)
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> event_subscription_write_dto | None:
        found_dtos = list(filter(lambda x: x.event_subscription_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, event_subscription_write_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.event_subscription_uid] = dto
        return res
    def get_active(self):
        return event_subscription_write_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return event_subscription_write_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_first(self) -> event_subscription_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> event_subscription_write_dtos:
        if len(self.dtos) > n:
            return event_subscription_write_dtos(self.dtos[:n])
        else:
            return event_subscription_write_dtos(self.dtos)
    def get_last(self) -> event_subscription_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, event_subscription_write_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[event_subscription_write_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[event_subscription_write_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def check_any(self, check_method: Callable[[event_subscription_write_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[event_subscription_write_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[event_subscription_write_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[event_subscription_write_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, event_subscription_write_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, event_subscription_write_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, event_subscription_write_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[event_subscription_write_dto], bool]) -> event_subscription_write_dtos:
        return event_subscription_write_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[event_subscription_write_dto], str]) -> dict[str, event_subscription_write_dtos]:
        grp_data: dict[str, event_subscription_write_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = event_subscription_write_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[event_subscription_write_dto], str], agg_method: Callable[[event_subscription_write_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, event_subscription_write_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[event_subscription_write_dto], bool]) -> event_subscription_write_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[event_subscription_write_dto], any], compare_method: Callable[[any, any], bool]) -> event_subscription_write_dto | None:
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
class event_template_write_dtos(base_write_dtos):
    dtos: list[event_template_write_dto]
    def __init__(self, dtos: list[event_template_write_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[event_template_write_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: event_template_write_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[event_template_write_dto], dtos2: list[event_template_write_dto]):
        return cls(dtos1 + dtos2)
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> event_template_write_dto | None:
        found_dtos = list(filter(lambda x: x.event_template_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, event_template_write_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.event_template_uid] = dto
        return res
    def get_active(self):
        return event_template_write_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return event_template_write_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_first(self) -> event_template_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> event_template_write_dtos:
        if len(self.dtos) > n:
            return event_template_write_dtos(self.dtos[:n])
        else:
            return event_template_write_dtos(self.dtos)
    def get_last(self) -> event_template_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, event_template_write_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[event_template_write_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[event_template_write_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def check_any(self, check_method: Callable[[event_template_write_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[event_template_write_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[event_template_write_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[event_template_write_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, event_template_write_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, event_template_write_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, event_template_write_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[event_template_write_dto], bool]) -> event_template_write_dtos:
        return event_template_write_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[event_template_write_dto], str]) -> dict[str, event_template_write_dtos]:
        grp_data: dict[str, event_template_write_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = event_template_write_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[event_template_write_dto], str], agg_method: Callable[[event_template_write_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, event_template_write_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[event_template_write_dto], bool]) -> event_template_write_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[event_template_write_dto], any], compare_method: Callable[[any, any], bool]) -> event_template_write_dto | None:
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
class event_type_write_dtos(base_write_dtos):
    dtos: list[event_type_write_dto]
    def __init__(self, dtos: list[event_type_write_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[event_type_write_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: event_type_write_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[event_type_write_dto], dtos2: list[event_type_write_dto]):
        return cls(dtos1 + dtos2)
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> event_type_write_dto | None:
        found_dtos = list(filter(lambda x: x.event_type_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, event_type_write_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.event_type_uid] = dto
        return res
    def get_active(self):
        return event_type_write_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return event_type_write_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_first(self) -> event_type_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> event_type_write_dtos:
        if len(self.dtos) > n:
            return event_type_write_dtos(self.dtos[:n])
        else:
            return event_type_write_dtos(self.dtos)
    def get_last(self) -> event_type_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, event_type_write_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[event_type_write_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[event_type_write_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def check_any(self, check_method: Callable[[event_type_write_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[event_type_write_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[event_type_write_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[event_type_write_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, event_type_write_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, event_type_write_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, event_type_write_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[event_type_write_dto], bool]) -> event_type_write_dtos:
        return event_type_write_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[event_type_write_dto], str]) -> dict[str, event_type_write_dtos]:
        grp_data: dict[str, event_type_write_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = event_type_write_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[event_type_write_dto], str], agg_method: Callable[[event_type_write_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, event_type_write_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[event_type_write_dto], bool]) -> event_type_write_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[event_type_write_dto], any], compare_method: Callable[[any, any], bool]) -> event_type_write_dto | None:
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
class invoice_action_write_dtos(base_write_dtos):
    dtos: list[invoice_action_write_dto]
    def __init__(self, dtos: list[invoice_action_write_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[invoice_action_write_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: invoice_action_write_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[invoice_action_write_dto], dtos2: list[invoice_action_write_dto]):
        return cls(dtos1 + dtos2)
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> invoice_action_write_dto | None:
        found_dtos = list(filter(lambda x: x.invoice_action_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, invoice_action_write_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.invoice_action_uid] = dto
        return res
    def get_active(self):
        return invoice_action_write_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return invoice_action_write_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_first(self) -> invoice_action_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> invoice_action_write_dtos:
        if len(self.dtos) > n:
            return invoice_action_write_dtos(self.dtos[:n])
        else:
            return invoice_action_write_dtos(self.dtos)
    def get_last(self) -> invoice_action_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, invoice_action_write_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[invoice_action_write_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[invoice_action_write_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def check_any(self, check_method: Callable[[invoice_action_write_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[invoice_action_write_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[invoice_action_write_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[invoice_action_write_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, invoice_action_write_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, invoice_action_write_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, invoice_action_write_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[invoice_action_write_dto], bool]) -> invoice_action_write_dtos:
        return invoice_action_write_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[invoice_action_write_dto], str]) -> dict[str, invoice_action_write_dtos]:
        grp_data: dict[str, invoice_action_write_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = invoice_action_write_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[invoice_action_write_dto], str], agg_method: Callable[[invoice_action_write_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, invoice_action_write_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[invoice_action_write_dto], bool]) -> invoice_action_write_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[invoice_action_write_dto], any], compare_method: Callable[[any, any], bool]) -> invoice_action_write_dto | None:
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
class invoice_action_type_write_dtos(base_write_dtos):
    dtos: list[invoice_action_type_write_dto]
    def __init__(self, dtos: list[invoice_action_type_write_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[invoice_action_type_write_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: invoice_action_type_write_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[invoice_action_type_write_dto], dtos2: list[invoice_action_type_write_dto]):
        return cls(dtos1 + dtos2)
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> invoice_action_type_write_dto | None:
        found_dtos = list(filter(lambda x: x.invoice_action_type_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, invoice_action_type_write_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.invoice_action_type_uid] = dto
        return res
    def get_active(self):
        return invoice_action_type_write_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return invoice_action_type_write_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_first(self) -> invoice_action_type_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> invoice_action_type_write_dtos:
        if len(self.dtos) > n:
            return invoice_action_type_write_dtos(self.dtos[:n])
        else:
            return invoice_action_type_write_dtos(self.dtos)
    def get_last(self) -> invoice_action_type_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, invoice_action_type_write_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[invoice_action_type_write_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[invoice_action_type_write_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def check_any(self, check_method: Callable[[invoice_action_type_write_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[invoice_action_type_write_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[invoice_action_type_write_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[invoice_action_type_write_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, invoice_action_type_write_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, invoice_action_type_write_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, invoice_action_type_write_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[invoice_action_type_write_dto], bool]) -> invoice_action_type_write_dtos:
        return invoice_action_type_write_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[invoice_action_type_write_dto], str]) -> dict[str, invoice_action_type_write_dtos]:
        grp_data: dict[str, invoice_action_type_write_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = invoice_action_type_write_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[invoice_action_type_write_dto], str], agg_method: Callable[[invoice_action_type_write_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, invoice_action_type_write_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[invoice_action_type_write_dto], bool]) -> invoice_action_type_write_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[invoice_action_type_write_dto], any], compare_method: Callable[[any, any], bool]) -> invoice_action_type_write_dto | None:
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
class invoice_category_write_dtos(base_write_dtos):
    dtos: list[invoice_category_write_dto]
    def __init__(self, dtos: list[invoice_category_write_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[invoice_category_write_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: invoice_category_write_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[invoice_category_write_dto], dtos2: list[invoice_category_write_dto]):
        return cls(dtos1 + dtos2)
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> invoice_category_write_dto | None:
        found_dtos = list(filter(lambda x: x.invoice_category_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, invoice_category_write_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.invoice_category_uid] = dto
        return res
    def get_active(self):
        return invoice_category_write_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return invoice_category_write_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_first(self) -> invoice_category_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> invoice_category_write_dtos:
        if len(self.dtos) > n:
            return invoice_category_write_dtos(self.dtos[:n])
        else:
            return invoice_category_write_dtos(self.dtos)
    def get_last(self) -> invoice_category_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, invoice_category_write_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[invoice_category_write_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[invoice_category_write_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def check_any(self, check_method: Callable[[invoice_category_write_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[invoice_category_write_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[invoice_category_write_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[invoice_category_write_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, invoice_category_write_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, invoice_category_write_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, invoice_category_write_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[invoice_category_write_dto], bool]) -> invoice_category_write_dtos:
        return invoice_category_write_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[invoice_category_write_dto], str]) -> dict[str, invoice_category_write_dtos]:
        grp_data: dict[str, invoice_category_write_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = invoice_category_write_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[invoice_category_write_dto], str], agg_method: Callable[[invoice_category_write_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, invoice_category_write_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[invoice_category_write_dto], bool]) -> invoice_category_write_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[invoice_category_write_dto], any], compare_method: Callable[[any, any], bool]) -> invoice_category_write_dto | None:
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
class invoice_entry_write_dtos(base_write_dtos):
    dtos: list[invoice_entry_write_dto]
    def __init__(self, dtos: list[invoice_entry_write_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[invoice_entry_write_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: invoice_entry_write_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[invoice_entry_write_dto], dtos2: list[invoice_entry_write_dto]):
        return cls(dtos1 + dtos2)
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> invoice_entry_write_dto | None:
        found_dtos = list(filter(lambda x: x.invoice_entry_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, invoice_entry_write_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.invoice_entry_uid] = dto
        return res
    def get_active(self):
        return invoice_entry_write_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return invoice_entry_write_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_first(self) -> invoice_entry_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> invoice_entry_write_dtos:
        if len(self.dtos) > n:
            return invoice_entry_write_dtos(self.dtos[:n])
        else:
            return invoice_entry_write_dtos(self.dtos)
    def get_last(self) -> invoice_entry_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, invoice_entry_write_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[invoice_entry_write_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[invoice_entry_write_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def check_any(self, check_method: Callable[[invoice_entry_write_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[invoice_entry_write_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[invoice_entry_write_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[invoice_entry_write_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, invoice_entry_write_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, invoice_entry_write_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, invoice_entry_write_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[invoice_entry_write_dto], bool]) -> invoice_entry_write_dtos:
        return invoice_entry_write_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[invoice_entry_write_dto], str]) -> dict[str, invoice_entry_write_dtos]:
        grp_data: dict[str, invoice_entry_write_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = invoice_entry_write_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[invoice_entry_write_dto], str], agg_method: Callable[[invoice_entry_write_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, invoice_entry_write_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[invoice_entry_write_dto], bool]) -> invoice_entry_write_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[invoice_entry_write_dto], any], compare_method: Callable[[any, any], bool]) -> invoice_entry_write_dto | None:
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
class invoice_flow_write_dtos(base_write_dtos):
    dtos: list[invoice_flow_write_dto]
    def __init__(self, dtos: list[invoice_flow_write_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[invoice_flow_write_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: invoice_flow_write_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[invoice_flow_write_dto], dtos2: list[invoice_flow_write_dto]):
        return cls(dtos1 + dtos2)
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> invoice_flow_write_dto | None:
        found_dtos = list(filter(lambda x: x.invoice_flow_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, invoice_flow_write_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.invoice_flow_uid] = dto
        return res
    def get_active(self):
        return invoice_flow_write_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return invoice_flow_write_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_first(self) -> invoice_flow_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> invoice_flow_write_dtos:
        if len(self.dtos) > n:
            return invoice_flow_write_dtos(self.dtos[:n])
        else:
            return invoice_flow_write_dtos(self.dtos)
    def get_last(self) -> invoice_flow_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, invoice_flow_write_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[invoice_flow_write_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[invoice_flow_write_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def check_any(self, check_method: Callable[[invoice_flow_write_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[invoice_flow_write_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[invoice_flow_write_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[invoice_flow_write_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, invoice_flow_write_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, invoice_flow_write_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, invoice_flow_write_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[invoice_flow_write_dto], bool]) -> invoice_flow_write_dtos:
        return invoice_flow_write_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[invoice_flow_write_dto], str]) -> dict[str, invoice_flow_write_dtos]:
        grp_data: dict[str, invoice_flow_write_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = invoice_flow_write_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[invoice_flow_write_dto], str], agg_method: Callable[[invoice_flow_write_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, invoice_flow_write_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[invoice_flow_write_dto], bool]) -> invoice_flow_write_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[invoice_flow_write_dto], any], compare_method: Callable[[any, any], bool]) -> invoice_flow_write_dto | None:
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
class invoice_flow_state_write_dtos(base_write_dtos):
    dtos: list[invoice_flow_state_write_dto]
    def __init__(self, dtos: list[invoice_flow_state_write_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[invoice_flow_state_write_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: invoice_flow_state_write_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[invoice_flow_state_write_dto], dtos2: list[invoice_flow_state_write_dto]):
        return cls(dtos1 + dtos2)
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> invoice_flow_state_write_dto | None:
        found_dtos = list(filter(lambda x: x.invoice_flow_state_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, invoice_flow_state_write_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.invoice_flow_state_uid] = dto
        return res
    def get_active(self):
        return invoice_flow_state_write_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return invoice_flow_state_write_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_first(self) -> invoice_flow_state_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> invoice_flow_state_write_dtos:
        if len(self.dtos) > n:
            return invoice_flow_state_write_dtos(self.dtos[:n])
        else:
            return invoice_flow_state_write_dtos(self.dtos)
    def get_last(self) -> invoice_flow_state_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, invoice_flow_state_write_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[invoice_flow_state_write_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[invoice_flow_state_write_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def check_any(self, check_method: Callable[[invoice_flow_state_write_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[invoice_flow_state_write_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[invoice_flow_state_write_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[invoice_flow_state_write_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, invoice_flow_state_write_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, invoice_flow_state_write_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, invoice_flow_state_write_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[invoice_flow_state_write_dto], bool]) -> invoice_flow_state_write_dtos:
        return invoice_flow_state_write_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[invoice_flow_state_write_dto], str]) -> dict[str, invoice_flow_state_write_dtos]:
        grp_data: dict[str, invoice_flow_state_write_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = invoice_flow_state_write_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[invoice_flow_state_write_dto], str], agg_method: Callable[[invoice_flow_state_write_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, invoice_flow_state_write_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[invoice_flow_state_write_dto], bool]) -> invoice_flow_state_write_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[invoice_flow_state_write_dto], any], compare_method: Callable[[any, any], bool]) -> invoice_flow_state_write_dto | None:
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
class invoice_instance_write_dtos(base_write_dtos):
    dtos: list[invoice_instance_write_dto]
    def __init__(self, dtos: list[invoice_instance_write_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[invoice_instance_write_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: invoice_instance_write_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[invoice_instance_write_dto], dtos2: list[invoice_instance_write_dto]):
        return cls(dtos1 + dtos2)
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> invoice_instance_write_dto | None:
        found_dtos = list(filter(lambda x: x.invoice_instance_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, invoice_instance_write_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.invoice_instance_uid] = dto
        return res
    def get_active(self):
        return invoice_instance_write_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return invoice_instance_write_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_first(self) -> invoice_instance_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> invoice_instance_write_dtos:
        if len(self.dtos) > n:
            return invoice_instance_write_dtos(self.dtos[:n])
        else:
            return invoice_instance_write_dtos(self.dtos)
    def get_last(self) -> invoice_instance_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, invoice_instance_write_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[invoice_instance_write_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[invoice_instance_write_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def check_any(self, check_method: Callable[[invoice_instance_write_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[invoice_instance_write_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[invoice_instance_write_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[invoice_instance_write_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, invoice_instance_write_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, invoice_instance_write_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, invoice_instance_write_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[invoice_instance_write_dto], bool]) -> invoice_instance_write_dtos:
        return invoice_instance_write_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[invoice_instance_write_dto], str]) -> dict[str, invoice_instance_write_dtos]:
        grp_data: dict[str, invoice_instance_write_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = invoice_instance_write_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[invoice_instance_write_dto], str], agg_method: Callable[[invoice_instance_write_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, invoice_instance_write_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[invoice_instance_write_dto], bool]) -> invoice_instance_write_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[invoice_instance_write_dto], any], compare_method: Callable[[any, any], bool]) -> invoice_instance_write_dto | None:
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
class invoice_status_write_dtos(base_write_dtos):
    dtos: list[invoice_status_write_dto]
    def __init__(self, dtos: list[invoice_status_write_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[invoice_status_write_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: invoice_status_write_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[invoice_status_write_dto], dtos2: list[invoice_status_write_dto]):
        return cls(dtos1 + dtos2)
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> invoice_status_write_dto | None:
        found_dtos = list(filter(lambda x: x.invoice_status_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, invoice_status_write_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.invoice_status_uid] = dto
        return res
    def get_active(self):
        return invoice_status_write_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return invoice_status_write_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_first(self) -> invoice_status_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> invoice_status_write_dtos:
        if len(self.dtos) > n:
            return invoice_status_write_dtos(self.dtos[:n])
        else:
            return invoice_status_write_dtos(self.dtos)
    def get_last(self) -> invoice_status_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, invoice_status_write_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[invoice_status_write_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[invoice_status_write_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def check_any(self, check_method: Callable[[invoice_status_write_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[invoice_status_write_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[invoice_status_write_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[invoice_status_write_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, invoice_status_write_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, invoice_status_write_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, invoice_status_write_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[invoice_status_write_dto], bool]) -> invoice_status_write_dtos:
        return invoice_status_write_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[invoice_status_write_dto], str]) -> dict[str, invoice_status_write_dtos]:
        grp_data: dict[str, invoice_status_write_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = invoice_status_write_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[invoice_status_write_dto], str], agg_method: Callable[[invoice_status_write_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, invoice_status_write_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[invoice_status_write_dto], bool]) -> invoice_status_write_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[invoice_status_write_dto], any], compare_method: Callable[[any, any], bool]) -> invoice_status_write_dto | None:
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
class invoice_type_write_dtos(base_write_dtos):
    dtos: list[invoice_type_write_dto]
    def __init__(self, dtos: list[invoice_type_write_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[invoice_type_write_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: invoice_type_write_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[invoice_type_write_dto], dtos2: list[invoice_type_write_dto]):
        return cls(dtos1 + dtos2)
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> invoice_type_write_dto | None:
        found_dtos = list(filter(lambda x: x.invoice_type_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, invoice_type_write_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.invoice_type_uid] = dto
        return res
    def get_active(self):
        return invoice_type_write_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return invoice_type_write_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_first(self) -> invoice_type_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> invoice_type_write_dtos:
        if len(self.dtos) > n:
            return invoice_type_write_dtos(self.dtos[:n])
        else:
            return invoice_type_write_dtos(self.dtos)
    def get_last(self) -> invoice_type_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, invoice_type_write_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[invoice_type_write_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[invoice_type_write_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def check_any(self, check_method: Callable[[invoice_type_write_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[invoice_type_write_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[invoice_type_write_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[invoice_type_write_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, invoice_type_write_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, invoice_type_write_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, invoice_type_write_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[invoice_type_write_dto], bool]) -> invoice_type_write_dtos:
        return invoice_type_write_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[invoice_type_write_dto], str]) -> dict[str, invoice_type_write_dtos]:
        grp_data: dict[str, invoice_type_write_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = invoice_type_write_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[invoice_type_write_dto], str], agg_method: Callable[[invoice_type_write_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, invoice_type_write_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[invoice_type_write_dto], bool]) -> invoice_type_write_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[invoice_type_write_dto], any], compare_method: Callable[[any, any], bool]) -> invoice_type_write_dto | None:
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
class location_hierarchy_write_dtos(base_write_dtos):
    dtos: list[location_hierarchy_write_dto]
    def __init__(self, dtos: list[location_hierarchy_write_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[location_hierarchy_write_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: location_hierarchy_write_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[location_hierarchy_write_dto], dtos2: list[location_hierarchy_write_dto]):
        return cls(dtos1 + dtos2)
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> location_hierarchy_write_dto | None:
        found_dtos = list(filter(lambda x: x.location_hierarchy_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, location_hierarchy_write_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.location_hierarchy_uid] = dto
        return res
    def get_active(self):
        return location_hierarchy_write_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return location_hierarchy_write_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_first(self) -> location_hierarchy_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> location_hierarchy_write_dtos:
        if len(self.dtos) > n:
            return location_hierarchy_write_dtos(self.dtos[:n])
        else:
            return location_hierarchy_write_dtos(self.dtos)
    def get_last(self) -> location_hierarchy_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, location_hierarchy_write_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[location_hierarchy_write_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[location_hierarchy_write_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def check_any(self, check_method: Callable[[location_hierarchy_write_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[location_hierarchy_write_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[location_hierarchy_write_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[location_hierarchy_write_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, location_hierarchy_write_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, location_hierarchy_write_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, location_hierarchy_write_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[location_hierarchy_write_dto], bool]) -> location_hierarchy_write_dtos:
        return location_hierarchy_write_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[location_hierarchy_write_dto], str]) -> dict[str, location_hierarchy_write_dtos]:
        grp_data: dict[str, location_hierarchy_write_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = location_hierarchy_write_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[location_hierarchy_write_dto], str], agg_method: Callable[[location_hierarchy_write_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, location_hierarchy_write_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[location_hierarchy_write_dto], bool]) -> location_hierarchy_write_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[location_hierarchy_write_dto], any], compare_method: Callable[[any, any], bool]) -> location_hierarchy_write_dto | None:
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
class location_postal_code_write_dtos(base_write_dtos):
    dtos: list[location_postal_code_write_dto]
    def __init__(self, dtos: list[location_postal_code_write_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[location_postal_code_write_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: location_postal_code_write_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[location_postal_code_write_dto], dtos2: list[location_postal_code_write_dto]):
        return cls(dtos1 + dtos2)
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> location_postal_code_write_dto | None:
        found_dtos = list(filter(lambda x: x.location_postal_code_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, location_postal_code_write_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.location_postal_code_uid] = dto
        return res
    def get_active(self):
        return location_postal_code_write_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return location_postal_code_write_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_first(self) -> location_postal_code_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> location_postal_code_write_dtos:
        if len(self.dtos) > n:
            return location_postal_code_write_dtos(self.dtos[:n])
        else:
            return location_postal_code_write_dtos(self.dtos)
    def get_last(self) -> location_postal_code_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, location_postal_code_write_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[location_postal_code_write_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[location_postal_code_write_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def check_any(self, check_method: Callable[[location_postal_code_write_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[location_postal_code_write_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[location_postal_code_write_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[location_postal_code_write_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, location_postal_code_write_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, location_postal_code_write_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, location_postal_code_write_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[location_postal_code_write_dto], bool]) -> location_postal_code_write_dtos:
        return location_postal_code_write_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[location_postal_code_write_dto], str]) -> dict[str, location_postal_code_write_dtos]:
        grp_data: dict[str, location_postal_code_write_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = location_postal_code_write_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[location_postal_code_write_dto], str], agg_method: Callable[[location_postal_code_write_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, location_postal_code_write_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[location_postal_code_write_dto], bool]) -> location_postal_code_write_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[location_postal_code_write_dto], any], compare_method: Callable[[any, any], bool]) -> location_postal_code_write_dto | None:
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
class location_region_write_dtos(base_write_dtos):
    dtos: list[location_region_write_dto]
    def __init__(self, dtos: list[location_region_write_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[location_region_write_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: location_region_write_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[location_region_write_dto], dtos2: list[location_region_write_dto]):
        return cls(dtos1 + dtos2)
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> location_region_write_dto | None:
        found_dtos = list(filter(lambda x: x.location_region_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, location_region_write_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.location_region_uid] = dto
        return res
    def get_active(self):
        return location_region_write_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return location_region_write_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_first(self) -> location_region_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> location_region_write_dtos:
        if len(self.dtos) > n:
            return location_region_write_dtos(self.dtos[:n])
        else:
            return location_region_write_dtos(self.dtos)
    def get_last(self) -> location_region_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, location_region_write_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[location_region_write_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[location_region_write_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def check_any(self, check_method: Callable[[location_region_write_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[location_region_write_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[location_region_write_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[location_region_write_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, location_region_write_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, location_region_write_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, location_region_write_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[location_region_write_dto], bool]) -> location_region_write_dtos:
        return location_region_write_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[location_region_write_dto], str]) -> dict[str, location_region_write_dtos]:
        grp_data: dict[str, location_region_write_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = location_region_write_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[location_region_write_dto], str], agg_method: Callable[[location_region_write_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, location_region_write_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[location_region_write_dto], bool]) -> location_region_write_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[location_region_write_dto], any], compare_method: Callable[[any, any], bool]) -> location_region_write_dto | None:
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
class location_territory_write_dtos(base_write_dtos):
    dtos: list[location_territory_write_dto]
    def __init__(self, dtos: list[location_territory_write_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[location_territory_write_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: location_territory_write_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[location_territory_write_dto], dtos2: list[location_territory_write_dto]):
        return cls(dtos1 + dtos2)
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> location_territory_write_dto | None:
        found_dtos = list(filter(lambda x: x.location_territory_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, location_territory_write_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.location_territory_uid] = dto
        return res
    def get_active(self):
        return location_territory_write_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return location_territory_write_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_first(self) -> location_territory_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> location_territory_write_dtos:
        if len(self.dtos) > n:
            return location_territory_write_dtos(self.dtos[:n])
        else:
            return location_territory_write_dtos(self.dtos)
    def get_last(self) -> location_territory_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, location_territory_write_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[location_territory_write_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[location_territory_write_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def check_any(self, check_method: Callable[[location_territory_write_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[location_territory_write_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[location_territory_write_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[location_territory_write_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, location_territory_write_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, location_territory_write_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, location_territory_write_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[location_territory_write_dto], bool]) -> location_territory_write_dtos:
        return location_territory_write_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[location_territory_write_dto], str]) -> dict[str, location_territory_write_dtos]:
        grp_data: dict[str, location_territory_write_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = location_territory_write_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[location_territory_write_dto], str], agg_method: Callable[[location_territory_write_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, location_territory_write_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[location_territory_write_dto], bool]) -> location_territory_write_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[location_territory_write_dto], any], compare_method: Callable[[any, any], bool]) -> location_territory_write_dto | None:
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
class monitor_write_dtos(base_write_dtos):
    dtos: list[monitor_write_dto]
    def __init__(self, dtos: list[monitor_write_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[monitor_write_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: monitor_write_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[monitor_write_dto], dtos2: list[monitor_write_dto]):
        return cls(dtos1 + dtos2)
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> monitor_write_dto | None:
        found_dtos = list(filter(lambda x: x.monitor_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, monitor_write_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.monitor_uid] = dto
        return res
    def get_active(self):
        return monitor_write_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return monitor_write_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_first(self) -> monitor_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> monitor_write_dtos:
        if len(self.dtos) > n:
            return monitor_write_dtos(self.dtos[:n])
        else:
            return monitor_write_dtos(self.dtos)
    def get_last(self) -> monitor_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, monitor_write_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[monitor_write_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[monitor_write_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def check_any(self, check_method: Callable[[monitor_write_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[monitor_write_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[monitor_write_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[monitor_write_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, monitor_write_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, monitor_write_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, monitor_write_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[monitor_write_dto], bool]) -> monitor_write_dtos:
        return monitor_write_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[monitor_write_dto], str]) -> dict[str, monitor_write_dtos]:
        grp_data: dict[str, monitor_write_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = monitor_write_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[monitor_write_dto], str], agg_method: Callable[[monitor_write_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, monitor_write_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[monitor_write_dto], bool]) -> monitor_write_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[monitor_write_dto], any], compare_method: Callable[[any, any], bool]) -> monitor_write_dto | None:
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
class monitor_run_write_dtos(base_write_dtos):
    dtos: list[monitor_run_write_dto]
    def __init__(self, dtos: list[monitor_run_write_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[monitor_run_write_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: monitor_run_write_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[monitor_run_write_dto], dtos2: list[monitor_run_write_dto]):
        return cls(dtos1 + dtos2)
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> monitor_run_write_dto | None:
        found_dtos = list(filter(lambda x: x.monitor_run_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, monitor_run_write_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.monitor_run_uid] = dto
        return res
    def get_active(self):
        return monitor_run_write_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return monitor_run_write_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_first(self) -> monitor_run_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> monitor_run_write_dtos:
        if len(self.dtos) > n:
            return monitor_run_write_dtos(self.dtos[:n])
        else:
            return monitor_run_write_dtos(self.dtos)
    def get_last(self) -> monitor_run_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, monitor_run_write_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[monitor_run_write_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[monitor_run_write_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def check_any(self, check_method: Callable[[monitor_run_write_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[monitor_run_write_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[monitor_run_write_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[monitor_run_write_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, monitor_run_write_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, monitor_run_write_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, monitor_run_write_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[monitor_run_write_dto], bool]) -> monitor_run_write_dtos:
        return monitor_run_write_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[monitor_run_write_dto], str]) -> dict[str, monitor_run_write_dtos]:
        grp_data: dict[str, monitor_run_write_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = monitor_run_write_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[monitor_run_write_dto], str], agg_method: Callable[[monitor_run_write_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, monitor_run_write_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[monitor_run_write_dto], bool]) -> monitor_run_write_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[monitor_run_write_dto], any], compare_method: Callable[[any, any], bool]) -> monitor_run_write_dto | None:
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
class monitor_type_write_dtos(base_write_dtos):
    dtos: list[monitor_type_write_dto]
    def __init__(self, dtos: list[monitor_type_write_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[monitor_type_write_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: monitor_type_write_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[monitor_type_write_dto], dtos2: list[monitor_type_write_dto]):
        return cls(dtos1 + dtos2)
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> monitor_type_write_dto | None:
        found_dtos = list(filter(lambda x: x.monitor_type_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, monitor_type_write_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.monitor_type_uid] = dto
        return res
    def get_active(self):
        return monitor_type_write_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return monitor_type_write_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_first(self) -> monitor_type_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> monitor_type_write_dtos:
        if len(self.dtos) > n:
            return monitor_type_write_dtos(self.dtos[:n])
        else:
            return monitor_type_write_dtos(self.dtos)
    def get_last(self) -> monitor_type_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, monitor_type_write_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[monitor_type_write_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[monitor_type_write_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def check_any(self, check_method: Callable[[monitor_type_write_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[monitor_type_write_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[monitor_type_write_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[monitor_type_write_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, monitor_type_write_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, monitor_type_write_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, monitor_type_write_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[monitor_type_write_dto], bool]) -> monitor_type_write_dtos:
        return monitor_type_write_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[monitor_type_write_dto], str]) -> dict[str, monitor_type_write_dtos]:
        grp_data: dict[str, monitor_type_write_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = monitor_type_write_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[monitor_type_write_dto], str], agg_method: Callable[[monitor_type_write_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, monitor_type_write_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[monitor_type_write_dto], bool]) -> monitor_type_write_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[monitor_type_write_dto], any], compare_method: Callable[[any, any], bool]) -> monitor_type_write_dto | None:
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
class period_write_dtos(base_write_dtos):
    dtos: list[period_write_dto]
    def __init__(self, dtos: list[period_write_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[period_write_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: period_write_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[period_write_dto], dtos2: list[period_write_dto]):
        return cls(dtos1 + dtos2)
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> period_write_dto | None:
        found_dtos = list(filter(lambda x: x.period_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, period_write_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.period_uid] = dto
        return res
    def get_active(self):
        return period_write_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return period_write_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_first(self) -> period_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> period_write_dtos:
        if len(self.dtos) > n:
            return period_write_dtos(self.dtos[:n])
        else:
            return period_write_dtos(self.dtos)
    def get_last(self) -> period_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, period_write_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[period_write_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[period_write_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def check_any(self, check_method: Callable[[period_write_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[period_write_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[period_write_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[period_write_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, period_write_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, period_write_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, period_write_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[period_write_dto], bool]) -> period_write_dtos:
        return period_write_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[period_write_dto], str]) -> dict[str, period_write_dtos]:
        grp_data: dict[str, period_write_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = period_write_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[period_write_dto], str], agg_method: Callable[[period_write_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, period_write_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[period_write_dto], bool]) -> period_write_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[period_write_dto], any], compare_method: Callable[[any, any], bool]) -> period_write_dto | None:
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
class process_write_dtos(base_write_dtos):
    dtos: list[process_write_dto]
    def __init__(self, dtos: list[process_write_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[process_write_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: process_write_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[process_write_dto], dtos2: list[process_write_dto]):
        return cls(dtos1 + dtos2)
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> process_write_dto | None:
        found_dtos = list(filter(lambda x: x.process_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, process_write_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.process_uid] = dto
        return res
    def get_active(self):
        return process_write_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return process_write_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_first(self) -> process_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> process_write_dtos:
        if len(self.dtos) > n:
            return process_write_dtos(self.dtos[:n])
        else:
            return process_write_dtos(self.dtos)
    def get_last(self) -> process_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, process_write_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[process_write_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[process_write_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def check_any(self, check_method: Callable[[process_write_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[process_write_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[process_write_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[process_write_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, process_write_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, process_write_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, process_write_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[process_write_dto], bool]) -> process_write_dtos:
        return process_write_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[process_write_dto], str]) -> dict[str, process_write_dtos]:
        grp_data: dict[str, process_write_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = process_write_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[process_write_dto], str], agg_method: Callable[[process_write_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, process_write_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[process_write_dto], bool]) -> process_write_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[process_write_dto], any], compare_method: Callable[[any, any], bool]) -> process_write_dto | None:
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
class process_result_write_dtos(base_write_dtos):
    dtos: list[process_result_write_dto]
    def __init__(self, dtos: list[process_result_write_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[process_result_write_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: process_result_write_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[process_result_write_dto], dtos2: list[process_result_write_dto]):
        return cls(dtos1 + dtos2)
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> process_result_write_dto | None:
        found_dtos = list(filter(lambda x: x.process_result_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, process_result_write_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.process_result_uid] = dto
        return res
    def get_active(self):
        return process_result_write_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return process_result_write_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_first(self) -> process_result_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> process_result_write_dtos:
        if len(self.dtos) > n:
            return process_result_write_dtos(self.dtos[:n])
        else:
            return process_result_write_dtos(self.dtos)
    def get_last(self) -> process_result_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, process_result_write_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[process_result_write_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[process_result_write_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def check_any(self, check_method: Callable[[process_result_write_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[process_result_write_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[process_result_write_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[process_result_write_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, process_result_write_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, process_result_write_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, process_result_write_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[process_result_write_dto], bool]) -> process_result_write_dtos:
        return process_result_write_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[process_result_write_dto], str]) -> dict[str, process_result_write_dtos]:
        grp_data: dict[str, process_result_write_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = process_result_write_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[process_result_write_dto], str], agg_method: Callable[[process_result_write_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, process_result_write_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[process_result_write_dto], bool]) -> process_result_write_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[process_result_write_dto], any], compare_method: Callable[[any, any], bool]) -> process_result_write_dto | None:
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
class process_run_write_dtos(base_write_dtos):
    dtos: list[process_run_write_dto]
    def __init__(self, dtos: list[process_run_write_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[process_run_write_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: process_run_write_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[process_run_write_dto], dtos2: list[process_run_write_dto]):
        return cls(dtos1 + dtos2)
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> process_run_write_dto | None:
        found_dtos = list(filter(lambda x: x.process_run_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, process_run_write_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.process_run_uid] = dto
        return res
    def get_active(self):
        return process_run_write_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return process_run_write_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_first(self) -> process_run_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> process_run_write_dtos:
        if len(self.dtos) > n:
            return process_run_write_dtos(self.dtos[:n])
        else:
            return process_run_write_dtos(self.dtos)
    def get_last(self) -> process_run_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, process_run_write_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[process_run_write_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[process_run_write_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def check_any(self, check_method: Callable[[process_run_write_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[process_run_write_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[process_run_write_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[process_run_write_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, process_run_write_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, process_run_write_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, process_run_write_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[process_run_write_dto], bool]) -> process_run_write_dtos:
        return process_run_write_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[process_run_write_dto], str]) -> dict[str, process_run_write_dtos]:
        grp_data: dict[str, process_run_write_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = process_run_write_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[process_run_write_dto], str], agg_method: Callable[[process_run_write_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, process_run_write_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[process_run_write_dto], bool]) -> process_run_write_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[process_run_write_dto], any], compare_method: Callable[[any, any], bool]) -> process_run_write_dto | None:
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
class process_type_write_dtos(base_write_dtos):
    dtos: list[process_type_write_dto]
    def __init__(self, dtos: list[process_type_write_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[process_type_write_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: process_type_write_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[process_type_write_dto], dtos2: list[process_type_write_dto]):
        return cls(dtos1 + dtos2)
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> process_type_write_dto | None:
        found_dtos = list(filter(lambda x: x.process_type_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, process_type_write_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.process_type_uid] = dto
        return res
    def get_active(self):
        return process_type_write_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return process_type_write_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_first(self) -> process_type_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> process_type_write_dtos:
        if len(self.dtos) > n:
            return process_type_write_dtos(self.dtos[:n])
        else:
            return process_type_write_dtos(self.dtos)
    def get_last(self) -> process_type_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, process_type_write_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[process_type_write_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[process_type_write_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def check_any(self, check_method: Callable[[process_type_write_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[process_type_write_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[process_type_write_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[process_type_write_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, process_type_write_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, process_type_write_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, process_type_write_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[process_type_write_dto], bool]) -> process_type_write_dtos:
        return process_type_write_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[process_type_write_dto], str]) -> dict[str, process_type_write_dtos]:
        grp_data: dict[str, process_type_write_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = process_type_write_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[process_type_write_dto], str], agg_method: Callable[[process_type_write_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, process_type_write_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[process_type_write_dto], bool]) -> process_type_write_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[process_type_write_dto], any], compare_method: Callable[[any, any], bool]) -> process_type_write_dto | None:
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
class project_account_write_dtos(base_write_dtos):
    dtos: list[project_account_write_dto]
    def __init__(self, dtos: list[project_account_write_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[project_account_write_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: project_account_write_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[project_account_write_dto], dtos2: list[project_account_write_dto]):
        return cls(dtos1 + dtos2)
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> project_account_write_dto | None:
        found_dtos = list(filter(lambda x: x.project_account_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, project_account_write_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.project_account_uid] = dto
        return res
    def get_active(self):
        return project_account_write_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return project_account_write_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_first(self) -> project_account_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> project_account_write_dtos:
        if len(self.dtos) > n:
            return project_account_write_dtos(self.dtos[:n])
        else:
            return project_account_write_dtos(self.dtos)
    def get_last(self) -> project_account_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, project_account_write_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[project_account_write_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[project_account_write_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def check_any(self, check_method: Callable[[project_account_write_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[project_account_write_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[project_account_write_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[project_account_write_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, project_account_write_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, project_account_write_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, project_account_write_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[project_account_write_dto], bool]) -> project_account_write_dtos:
        return project_account_write_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[project_account_write_dto], str]) -> dict[str, project_account_write_dtos]:
        grp_data: dict[str, project_account_write_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = project_account_write_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[project_account_write_dto], str], agg_method: Callable[[project_account_write_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, project_account_write_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[project_account_write_dto], bool]) -> project_account_write_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[project_account_write_dto], any], compare_method: Callable[[any, any], bool]) -> project_account_write_dto | None:
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
class project_budget_write_dtos(base_write_dtos):
    dtos: list[project_budget_write_dto]
    def __init__(self, dtos: list[project_budget_write_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[project_budget_write_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: project_budget_write_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[project_budget_write_dto], dtos2: list[project_budget_write_dto]):
        return cls(dtos1 + dtos2)
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> project_budget_write_dto | None:
        found_dtos = list(filter(lambda x: x.project_budget_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, project_budget_write_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.project_budget_uid] = dto
        return res
    def get_active(self):
        return project_budget_write_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return project_budget_write_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_first(self) -> project_budget_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> project_budget_write_dtos:
        if len(self.dtos) > n:
            return project_budget_write_dtos(self.dtos[:n])
        else:
            return project_budget_write_dtos(self.dtos)
    def get_last(self) -> project_budget_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, project_budget_write_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[project_budget_write_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[project_budget_write_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def check_any(self, check_method: Callable[[project_budget_write_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[project_budget_write_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[project_budget_write_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[project_budget_write_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, project_budget_write_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, project_budget_write_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, project_budget_write_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[project_budget_write_dto], bool]) -> project_budget_write_dtos:
        return project_budget_write_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[project_budget_write_dto], str]) -> dict[str, project_budget_write_dtos]:
        grp_data: dict[str, project_budget_write_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = project_budget_write_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[project_budget_write_dto], str], agg_method: Callable[[project_budget_write_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, project_budget_write_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[project_budget_write_dto], bool]) -> project_budget_write_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[project_budget_write_dto], any], compare_method: Callable[[any, any], bool]) -> project_budget_write_dto | None:
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
class project_group_write_dtos(base_write_dtos):
    dtos: list[project_group_write_dto]
    def __init__(self, dtos: list[project_group_write_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[project_group_write_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: project_group_write_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[project_group_write_dto], dtos2: list[project_group_write_dto]):
        return cls(dtos1 + dtos2)
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> project_group_write_dto | None:
        found_dtos = list(filter(lambda x: x.project_group_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, project_group_write_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.project_group_uid] = dto
        return res
    def get_active(self):
        return project_group_write_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return project_group_write_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_first(self) -> project_group_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> project_group_write_dtos:
        if len(self.dtos) > n:
            return project_group_write_dtos(self.dtos[:n])
        else:
            return project_group_write_dtos(self.dtos)
    def get_last(self) -> project_group_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, project_group_write_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[project_group_write_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[project_group_write_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def check_any(self, check_method: Callable[[project_group_write_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[project_group_write_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[project_group_write_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[project_group_write_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, project_group_write_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, project_group_write_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, project_group_write_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[project_group_write_dto], bool]) -> project_group_write_dtos:
        return project_group_write_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[project_group_write_dto], str]) -> dict[str, project_group_write_dtos]:
        grp_data: dict[str, project_group_write_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = project_group_write_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[project_group_write_dto], str], agg_method: Callable[[project_group_write_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, project_group_write_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[project_group_write_dto], bool]) -> project_group_write_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[project_group_write_dto], any], compare_method: Callable[[any, any], bool]) -> project_group_write_dto | None:
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
class project_instance_write_dtos(base_write_dtos):
    dtos: list[project_instance_write_dto]
    def __init__(self, dtos: list[project_instance_write_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[project_instance_write_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: project_instance_write_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[project_instance_write_dto], dtos2: list[project_instance_write_dto]):
        return cls(dtos1 + dtos2)
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> project_instance_write_dto | None:
        found_dtos = list(filter(lambda x: x.project_instance_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, project_instance_write_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.project_instance_uid] = dto
        return res
    def get_active(self):
        return project_instance_write_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return project_instance_write_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_first(self) -> project_instance_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> project_instance_write_dtos:
        if len(self.dtos) > n:
            return project_instance_write_dtos(self.dtos[:n])
        else:
            return project_instance_write_dtos(self.dtos)
    def get_last(self) -> project_instance_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, project_instance_write_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[project_instance_write_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[project_instance_write_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def check_any(self, check_method: Callable[[project_instance_write_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[project_instance_write_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[project_instance_write_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[project_instance_write_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, project_instance_write_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, project_instance_write_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, project_instance_write_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[project_instance_write_dto], bool]) -> project_instance_write_dtos:
        return project_instance_write_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[project_instance_write_dto], str]) -> dict[str, project_instance_write_dtos]:
        grp_data: dict[str, project_instance_write_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = project_instance_write_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[project_instance_write_dto], str], agg_method: Callable[[project_instance_write_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, project_instance_write_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[project_instance_write_dto], bool]) -> project_instance_write_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[project_instance_write_dto], any], compare_method: Callable[[any, any], bool]) -> project_instance_write_dto | None:
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
class project_milestone_write_dtos(base_write_dtos):
    dtos: list[project_milestone_write_dto]
    def __init__(self, dtos: list[project_milestone_write_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[project_milestone_write_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: project_milestone_write_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[project_milestone_write_dto], dtos2: list[project_milestone_write_dto]):
        return cls(dtos1 + dtos2)
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> project_milestone_write_dto | None:
        found_dtos = list(filter(lambda x: x.project_milestone_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, project_milestone_write_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.project_milestone_uid] = dto
        return res
    def get_active(self):
        return project_milestone_write_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return project_milestone_write_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_first(self) -> project_milestone_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> project_milestone_write_dtos:
        if len(self.dtos) > n:
            return project_milestone_write_dtos(self.dtos[:n])
        else:
            return project_milestone_write_dtos(self.dtos)
    def get_last(self) -> project_milestone_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, project_milestone_write_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[project_milestone_write_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[project_milestone_write_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def check_any(self, check_method: Callable[[project_milestone_write_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[project_milestone_write_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[project_milestone_write_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[project_milestone_write_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, project_milestone_write_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, project_milestone_write_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, project_milestone_write_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[project_milestone_write_dto], bool]) -> project_milestone_write_dtos:
        return project_milestone_write_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[project_milestone_write_dto], str]) -> dict[str, project_milestone_write_dtos]:
        grp_data: dict[str, project_milestone_write_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = project_milestone_write_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[project_milestone_write_dto], str], agg_method: Callable[[project_milestone_write_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, project_milestone_write_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[project_milestone_write_dto], bool]) -> project_milestone_write_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[project_milestone_write_dto], any], compare_method: Callable[[any, any], bool]) -> project_milestone_write_dto | None:
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
class project_phase_write_dtos(base_write_dtos):
    dtos: list[project_phase_write_dto]
    def __init__(self, dtos: list[project_phase_write_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[project_phase_write_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: project_phase_write_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[project_phase_write_dto], dtos2: list[project_phase_write_dto]):
        return cls(dtos1 + dtos2)
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> project_phase_write_dto | None:
        found_dtos = list(filter(lambda x: x.project_phase_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, project_phase_write_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.project_phase_uid] = dto
        return res
    def get_active(self):
        return project_phase_write_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return project_phase_write_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_first(self) -> project_phase_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> project_phase_write_dtos:
        if len(self.dtos) > n:
            return project_phase_write_dtos(self.dtos[:n])
        else:
            return project_phase_write_dtos(self.dtos)
    def get_last(self) -> project_phase_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, project_phase_write_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[project_phase_write_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[project_phase_write_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def check_any(self, check_method: Callable[[project_phase_write_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[project_phase_write_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[project_phase_write_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[project_phase_write_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, project_phase_write_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, project_phase_write_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, project_phase_write_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[project_phase_write_dto], bool]) -> project_phase_write_dtos:
        return project_phase_write_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[project_phase_write_dto], str]) -> dict[str, project_phase_write_dtos]:
        grp_data: dict[str, project_phase_write_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = project_phase_write_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[project_phase_write_dto], str], agg_method: Callable[[project_phase_write_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, project_phase_write_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[project_phase_write_dto], bool]) -> project_phase_write_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[project_phase_write_dto], any], compare_method: Callable[[any, any], bool]) -> project_phase_write_dto | None:
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
class project_type_write_dtos(base_write_dtos):
    dtos: list[project_type_write_dto]
    def __init__(self, dtos: list[project_type_write_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[project_type_write_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: project_type_write_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[project_type_write_dto], dtos2: list[project_type_write_dto]):
        return cls(dtos1 + dtos2)
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> project_type_write_dto | None:
        found_dtos = list(filter(lambda x: x.project_type_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, project_type_write_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.project_type_uid] = dto
        return res
    def get_active(self):
        return project_type_write_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return project_type_write_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_first(self) -> project_type_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> project_type_write_dtos:
        if len(self.dtos) > n:
            return project_type_write_dtos(self.dtos[:n])
        else:
            return project_type_write_dtos(self.dtos)
    def get_last(self) -> project_type_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, project_type_write_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[project_type_write_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[project_type_write_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def check_any(self, check_method: Callable[[project_type_write_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[project_type_write_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[project_type_write_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[project_type_write_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, project_type_write_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, project_type_write_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, project_type_write_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[project_type_write_dto], bool]) -> project_type_write_dtos:
        return project_type_write_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[project_type_write_dto], str]) -> dict[str, project_type_write_dtos]:
        grp_data: dict[str, project_type_write_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = project_type_write_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[project_type_write_dto], str], agg_method: Callable[[project_type_write_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, project_type_write_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[project_type_write_dto], bool]) -> project_type_write_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[project_type_write_dto], any], compare_method: Callable[[any, any], bool]) -> project_type_write_dto | None:
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
class report_write_dtos(base_write_dtos):
    dtos: list[report_write_dto]
    def __init__(self, dtos: list[report_write_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[report_write_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: report_write_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[report_write_dto], dtos2: list[report_write_dto]):
        return cls(dtos1 + dtos2)
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> report_write_dto | None:
        found_dtos = list(filter(lambda x: x.report_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, report_write_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.report_uid] = dto
        return res
    def get_active(self):
        return report_write_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return report_write_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_first(self) -> report_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> report_write_dtos:
        if len(self.dtos) > n:
            return report_write_dtos(self.dtos[:n])
        else:
            return report_write_dtos(self.dtos)
    def get_last(self) -> report_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, report_write_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[report_write_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[report_write_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def check_any(self, check_method: Callable[[report_write_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[report_write_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[report_write_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[report_write_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, report_write_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, report_write_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, report_write_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[report_write_dto], bool]) -> report_write_dtos:
        return report_write_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[report_write_dto], str]) -> dict[str, report_write_dtos]:
        grp_data: dict[str, report_write_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = report_write_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[report_write_dto], str], agg_method: Callable[[report_write_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, report_write_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[report_write_dto], bool]) -> report_write_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[report_write_dto], any], compare_method: Callable[[any, any], bool]) -> report_write_dto | None:
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
class report_content_type_write_dtos(base_write_dtos):
    dtos: list[report_content_type_write_dto]
    def __init__(self, dtos: list[report_content_type_write_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[report_content_type_write_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: report_content_type_write_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[report_content_type_write_dto], dtos2: list[report_content_type_write_dto]):
        return cls(dtos1 + dtos2)
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> report_content_type_write_dto | None:
        found_dtos = list(filter(lambda x: x.report_content_type_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, report_content_type_write_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.report_content_type_uid] = dto
        return res
    def get_active(self):
        return report_content_type_write_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return report_content_type_write_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_first(self) -> report_content_type_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> report_content_type_write_dtos:
        if len(self.dtos) > n:
            return report_content_type_write_dtos(self.dtos[:n])
        else:
            return report_content_type_write_dtos(self.dtos)
    def get_last(self) -> report_content_type_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, report_content_type_write_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[report_content_type_write_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[report_content_type_write_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def check_any(self, check_method: Callable[[report_content_type_write_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[report_content_type_write_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[report_content_type_write_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[report_content_type_write_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, report_content_type_write_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, report_content_type_write_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, report_content_type_write_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[report_content_type_write_dto], bool]) -> report_content_type_write_dtos:
        return report_content_type_write_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[report_content_type_write_dto], str]) -> dict[str, report_content_type_write_dtos]:
        grp_data: dict[str, report_content_type_write_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = report_content_type_write_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[report_content_type_write_dto], str], agg_method: Callable[[report_content_type_write_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, report_content_type_write_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[report_content_type_write_dto], bool]) -> report_content_type_write_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[report_content_type_write_dto], any], compare_method: Callable[[any, any], bool]) -> report_content_type_write_dto | None:
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
class report_format_write_dtos(base_write_dtos):
    dtos: list[report_format_write_dto]
    def __init__(self, dtos: list[report_format_write_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[report_format_write_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: report_format_write_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[report_format_write_dto], dtos2: list[report_format_write_dto]):
        return cls(dtos1 + dtos2)
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> report_format_write_dto | None:
        found_dtos = list(filter(lambda x: x.report_format_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, report_format_write_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.report_format_uid] = dto
        return res
    def get_active(self):
        return report_format_write_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return report_format_write_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_first(self) -> report_format_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> report_format_write_dtos:
        if len(self.dtos) > n:
            return report_format_write_dtos(self.dtos[:n])
        else:
            return report_format_write_dtos(self.dtos)
    def get_last(self) -> report_format_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, report_format_write_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[report_format_write_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[report_format_write_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def check_any(self, check_method: Callable[[report_format_write_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[report_format_write_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[report_format_write_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[report_format_write_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, report_format_write_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, report_format_write_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, report_format_write_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[report_format_write_dto], bool]) -> report_format_write_dtos:
        return report_format_write_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[report_format_write_dto], str]) -> dict[str, report_format_write_dtos]:
        grp_data: dict[str, report_format_write_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = report_format_write_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[report_format_write_dto], str], agg_method: Callable[[report_format_write_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, report_format_write_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[report_format_write_dto], bool]) -> report_format_write_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[report_format_write_dto], any], compare_method: Callable[[any, any], bool]) -> report_format_write_dto | None:
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
class report_run_write_dtos(base_write_dtos):
    dtos: list[report_run_write_dto]
    def __init__(self, dtos: list[report_run_write_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[report_run_write_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: report_run_write_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[report_run_write_dto], dtos2: list[report_run_write_dto]):
        return cls(dtos1 + dtos2)
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> report_run_write_dto | None:
        found_dtos = list(filter(lambda x: x.report_run_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, report_run_write_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.report_run_uid] = dto
        return res
    def get_active(self):
        return report_run_write_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return report_run_write_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_first(self) -> report_run_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> report_run_write_dtos:
        if len(self.dtos) > n:
            return report_run_write_dtos(self.dtos[:n])
        else:
            return report_run_write_dtos(self.dtos)
    def get_last(self) -> report_run_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, report_run_write_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[report_run_write_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[report_run_write_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def check_any(self, check_method: Callable[[report_run_write_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[report_run_write_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[report_run_write_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[report_run_write_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, report_run_write_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, report_run_write_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, report_run_write_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[report_run_write_dto], bool]) -> report_run_write_dtos:
        return report_run_write_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[report_run_write_dto], str]) -> dict[str, report_run_write_dtos]:
        grp_data: dict[str, report_run_write_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = report_run_write_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[report_run_write_dto], str], agg_method: Callable[[report_run_write_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, report_run_write_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[report_run_write_dto], bool]) -> report_run_write_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[report_run_write_dto], any], compare_method: Callable[[any, any], bool]) -> report_run_write_dto | None:
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
class report_status_write_dtos(base_write_dtos):
    dtos: list[report_status_write_dto]
    def __init__(self, dtos: list[report_status_write_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[report_status_write_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: report_status_write_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[report_status_write_dto], dtos2: list[report_status_write_dto]):
        return cls(dtos1 + dtos2)
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> report_status_write_dto | None:
        found_dtos = list(filter(lambda x: x.report_status_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, report_status_write_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.report_status_uid] = dto
        return res
    def get_active(self):
        return report_status_write_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return report_status_write_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_first(self) -> report_status_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> report_status_write_dtos:
        if len(self.dtos) > n:
            return report_status_write_dtos(self.dtos[:n])
        else:
            return report_status_write_dtos(self.dtos)
    def get_last(self) -> report_status_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, report_status_write_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[report_status_write_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[report_status_write_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def check_any(self, check_method: Callable[[report_status_write_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[report_status_write_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[report_status_write_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[report_status_write_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, report_status_write_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, report_status_write_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, report_status_write_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[report_status_write_dto], bool]) -> report_status_write_dtos:
        return report_status_write_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[report_status_write_dto], str]) -> dict[str, report_status_write_dtos]:
        grp_data: dict[str, report_status_write_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = report_status_write_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[report_status_write_dto], str], agg_method: Callable[[report_status_write_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, report_status_write_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[report_status_write_dto], bool]) -> report_status_write_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[report_status_write_dto], any], compare_method: Callable[[any, any], bool]) -> report_status_write_dto | None:
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
class report_type_write_dtos(base_write_dtos):
    dtos: list[report_type_write_dto]
    def __init__(self, dtos: list[report_type_write_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[report_type_write_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: report_type_write_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[report_type_write_dto], dtos2: list[report_type_write_dto]):
        return cls(dtos1 + dtos2)
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> report_type_write_dto | None:
        found_dtos = list(filter(lambda x: x.report_type_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, report_type_write_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.report_type_uid] = dto
        return res
    def get_active(self):
        return report_type_write_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return report_type_write_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_first(self) -> report_type_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> report_type_write_dtos:
        if len(self.dtos) > n:
            return report_type_write_dtos(self.dtos[:n])
        else:
            return report_type_write_dtos(self.dtos)
    def get_last(self) -> report_type_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, report_type_write_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[report_type_write_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[report_type_write_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def check_any(self, check_method: Callable[[report_type_write_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[report_type_write_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[report_type_write_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[report_type_write_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, report_type_write_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, report_type_write_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, report_type_write_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[report_type_write_dto], bool]) -> report_type_write_dtos:
        return report_type_write_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[report_type_write_dto], str]) -> dict[str, report_type_write_dtos]:
        grp_data: dict[str, report_type_write_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = report_type_write_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[report_type_write_dto], str], agg_method: Callable[[report_type_write_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, report_type_write_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[report_type_write_dto], bool]) -> report_type_write_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[report_type_write_dto], any], compare_method: Callable[[any, any], bool]) -> report_type_write_dto | None:
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
class storage_write_dtos(base_write_dtos):
    dtos: list[storage_write_dto]
    def __init__(self, dtos: list[storage_write_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[storage_write_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: storage_write_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[storage_write_dto], dtos2: list[storage_write_dto]):
        return cls(dtos1 + dtos2)
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> storage_write_dto | None:
        found_dtos = list(filter(lambda x: x.storage_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, storage_write_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.storage_uid] = dto
        return res
    def get_active(self):
        return storage_write_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return storage_write_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_first(self) -> storage_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> storage_write_dtos:
        if len(self.dtos) > n:
            return storage_write_dtos(self.dtos[:n])
        else:
            return storage_write_dtos(self.dtos)
    def get_last(self) -> storage_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, storage_write_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[storage_write_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[storage_write_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def check_any(self, check_method: Callable[[storage_write_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[storage_write_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[storage_write_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[storage_write_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, storage_write_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, storage_write_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, storage_write_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[storage_write_dto], bool]) -> storage_write_dtos:
        return storage_write_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[storage_write_dto], str]) -> dict[str, storage_write_dtos]:
        grp_data: dict[str, storage_write_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = storage_write_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[storage_write_dto], str], agg_method: Callable[[storage_write_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, storage_write_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[storage_write_dto], bool]) -> storage_write_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[storage_write_dto], any], compare_method: Callable[[any, any], bool]) -> storage_write_dto | None:
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
class storage_category_write_dtos(base_write_dtos):
    dtos: list[storage_category_write_dto]
    def __init__(self, dtos: list[storage_category_write_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[storage_category_write_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: storage_category_write_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[storage_category_write_dto], dtos2: list[storage_category_write_dto]):
        return cls(dtos1 + dtos2)
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> storage_category_write_dto | None:
        found_dtos = list(filter(lambda x: x.storage_category_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, storage_category_write_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.storage_category_uid] = dto
        return res
    def get_active(self):
        return storage_category_write_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return storage_category_write_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_first(self) -> storage_category_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> storage_category_write_dtos:
        if len(self.dtos) > n:
            return storage_category_write_dtos(self.dtos[:n])
        else:
            return storage_category_write_dtos(self.dtos)
    def get_last(self) -> storage_category_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, storage_category_write_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[storage_category_write_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[storage_category_write_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def check_any(self, check_method: Callable[[storage_category_write_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[storage_category_write_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[storage_category_write_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[storage_category_write_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, storage_category_write_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, storage_category_write_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, storage_category_write_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[storage_category_write_dto], bool]) -> storage_category_write_dtos:
        return storage_category_write_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[storage_category_write_dto], str]) -> dict[str, storage_category_write_dtos]:
        grp_data: dict[str, storage_category_write_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = storage_category_write_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[storage_category_write_dto], str], agg_method: Callable[[storage_category_write_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, storage_category_write_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[storage_category_write_dto], bool]) -> storage_category_write_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[storage_category_write_dto], any], compare_method: Callable[[any, any], bool]) -> storage_category_write_dto | None:
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
class storage_connection_write_dtos(base_write_dtos):
    dtos: list[storage_connection_write_dto]
    def __init__(self, dtos: list[storage_connection_write_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[storage_connection_write_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: storage_connection_write_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[storage_connection_write_dto], dtos2: list[storage_connection_write_dto]):
        return cls(dtos1 + dtos2)
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> storage_connection_write_dto | None:
        found_dtos = list(filter(lambda x: x.storage_connection_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, storage_connection_write_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.storage_connection_uid] = dto
        return res
    def get_active(self):
        return storage_connection_write_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return storage_connection_write_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_first(self) -> storage_connection_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> storage_connection_write_dtos:
        if len(self.dtos) > n:
            return storage_connection_write_dtos(self.dtos[:n])
        else:
            return storage_connection_write_dtos(self.dtos)
    def get_last(self) -> storage_connection_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, storage_connection_write_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[storage_connection_write_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[storage_connection_write_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def check_any(self, check_method: Callable[[storage_connection_write_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[storage_connection_write_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[storage_connection_write_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[storage_connection_write_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, storage_connection_write_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, storage_connection_write_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, storage_connection_write_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[storage_connection_write_dto], bool]) -> storage_connection_write_dtos:
        return storage_connection_write_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[storage_connection_write_dto], str]) -> dict[str, storage_connection_write_dtos]:
        grp_data: dict[str, storage_connection_write_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = storage_connection_write_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[storage_connection_write_dto], str], agg_method: Callable[[storage_connection_write_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, storage_connection_write_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[storage_connection_write_dto], bool]) -> storage_connection_write_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[storage_connection_write_dto], any], compare_method: Callable[[any, any], bool]) -> storage_connection_write_dto | None:
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
class storage_query_write_dtos(base_write_dtos):
    dtos: list[storage_query_write_dto]
    def __init__(self, dtos: list[storage_query_write_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[storage_query_write_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: storage_query_write_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[storage_query_write_dto], dtos2: list[storage_query_write_dto]):
        return cls(dtos1 + dtos2)
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> storage_query_write_dto | None:
        found_dtos = list(filter(lambda x: x.storage_query_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, storage_query_write_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.storage_query_uid] = dto
        return res
    def get_active(self):
        return storage_query_write_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return storage_query_write_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_first(self) -> storage_query_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> storage_query_write_dtos:
        if len(self.dtos) > n:
            return storage_query_write_dtos(self.dtos[:n])
        else:
            return storage_query_write_dtos(self.dtos)
    def get_last(self) -> storage_query_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, storage_query_write_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[storage_query_write_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[storage_query_write_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def check_any(self, check_method: Callable[[storage_query_write_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[storage_query_write_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[storage_query_write_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[storage_query_write_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, storage_query_write_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, storage_query_write_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, storage_query_write_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[storage_query_write_dto], bool]) -> storage_query_write_dtos:
        return storage_query_write_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[storage_query_write_dto], str]) -> dict[str, storage_query_write_dtos]:
        grp_data: dict[str, storage_query_write_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = storage_query_write_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[storage_query_write_dto], str], agg_method: Callable[[storage_query_write_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, storage_query_write_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[storage_query_write_dto], bool]) -> storage_query_write_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[storage_query_write_dto], any], compare_method: Callable[[any, any], bool]) -> storage_query_write_dto | None:
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
class storage_type_write_dtos(base_write_dtos):
    dtos: list[storage_type_write_dto]
    def __init__(self, dtos: list[storage_type_write_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[storage_type_write_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: storage_type_write_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[storage_type_write_dto], dtos2: list[storage_type_write_dto]):
        return cls(dtos1 + dtos2)
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> storage_type_write_dto | None:
        found_dtos = list(filter(lambda x: x.storage_type_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, storage_type_write_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.storage_type_uid] = dto
        return res
    def get_active(self):
        return storage_type_write_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return storage_type_write_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_first(self) -> storage_type_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> storage_type_write_dtos:
        if len(self.dtos) > n:
            return storage_type_write_dtos(self.dtos[:n])
        else:
            return storage_type_write_dtos(self.dtos)
    def get_last(self) -> storage_type_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, storage_type_write_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[storage_type_write_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[storage_type_write_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def check_any(self, check_method: Callable[[storage_type_write_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[storage_type_write_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[storage_type_write_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[storage_type_write_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, storage_type_write_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, storage_type_write_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, storage_type_write_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[storage_type_write_dto], bool]) -> storage_type_write_dtos:
        return storage_type_write_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[storage_type_write_dto], str]) -> dict[str, storage_type_write_dtos]:
        grp_data: dict[str, storage_type_write_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = storage_type_write_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[storage_type_write_dto], str], agg_method: Callable[[storage_type_write_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, storage_type_write_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[storage_type_write_dto], bool]) -> storage_type_write_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[storage_type_write_dto], any], compare_method: Callable[[any, any], bool]) -> storage_type_write_dto | None:
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
class synchronization_write_dtos(base_write_dtos):
    dtos: list[synchronization_write_dto]
    def __init__(self, dtos: list[synchronization_write_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[synchronization_write_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: synchronization_write_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[synchronization_write_dto], dtos2: list[synchronization_write_dto]):
        return cls(dtos1 + dtos2)
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> synchronization_write_dto | None:
        found_dtos = list(filter(lambda x: x.synchronization_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, synchronization_write_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.synchronization_uid] = dto
        return res
    def get_active(self):
        return synchronization_write_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return synchronization_write_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_first(self) -> synchronization_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> synchronization_write_dtos:
        if len(self.dtos) > n:
            return synchronization_write_dtos(self.dtos[:n])
        else:
            return synchronization_write_dtos(self.dtos)
    def get_last(self) -> synchronization_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, synchronization_write_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[synchronization_write_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[synchronization_write_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def check_any(self, check_method: Callable[[synchronization_write_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[synchronization_write_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[synchronization_write_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[synchronization_write_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, synchronization_write_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, synchronization_write_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, synchronization_write_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[synchronization_write_dto], bool]) -> synchronization_write_dtos:
        return synchronization_write_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[synchronization_write_dto], str]) -> dict[str, synchronization_write_dtos]:
        grp_data: dict[str, synchronization_write_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = synchronization_write_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[synchronization_write_dto], str], agg_method: Callable[[synchronization_write_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, synchronization_write_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[synchronization_write_dto], bool]) -> synchronization_write_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[synchronization_write_dto], any], compare_method: Callable[[any, any], bool]) -> synchronization_write_dto | None:
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
class synchronization_run_write_dtos(base_write_dtos):
    dtos: list[synchronization_run_write_dto]
    def __init__(self, dtos: list[synchronization_run_write_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[synchronization_run_write_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: synchronization_run_write_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[synchronization_run_write_dto], dtos2: list[synchronization_run_write_dto]):
        return cls(dtos1 + dtos2)
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> synchronization_run_write_dto | None:
        found_dtos = list(filter(lambda x: x.synchronization_run_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, synchronization_run_write_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.synchronization_run_uid] = dto
        return res
    def get_active(self):
        return synchronization_run_write_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return synchronization_run_write_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_first(self) -> synchronization_run_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> synchronization_run_write_dtos:
        if len(self.dtos) > n:
            return synchronization_run_write_dtos(self.dtos[:n])
        else:
            return synchronization_run_write_dtos(self.dtos)
    def get_last(self) -> synchronization_run_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, synchronization_run_write_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[synchronization_run_write_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[synchronization_run_write_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def check_any(self, check_method: Callable[[synchronization_run_write_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[synchronization_run_write_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[synchronization_run_write_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[synchronization_run_write_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, synchronization_run_write_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, synchronization_run_write_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, synchronization_run_write_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[synchronization_run_write_dto], bool]) -> synchronization_run_write_dtos:
        return synchronization_run_write_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[synchronization_run_write_dto], str]) -> dict[str, synchronization_run_write_dtos]:
        grp_data: dict[str, synchronization_run_write_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = synchronization_run_write_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[synchronization_run_write_dto], str], agg_method: Callable[[synchronization_run_write_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, synchronization_run_write_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[synchronization_run_write_dto], bool]) -> synchronization_run_write_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[synchronization_run_write_dto], any], compare_method: Callable[[any, any], bool]) -> synchronization_run_write_dto | None:
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
class synchronization_type_write_dtos(base_write_dtos):
    dtos: list[synchronization_type_write_dto]
    def __init__(self, dtos: list[synchronization_type_write_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[synchronization_type_write_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: synchronization_type_write_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[synchronization_type_write_dto], dtos2: list[synchronization_type_write_dto]):
        return cls(dtos1 + dtos2)
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> synchronization_type_write_dto | None:
        found_dtos = list(filter(lambda x: x.synchronization_type_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, synchronization_type_write_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.synchronization_type_uid] = dto
        return res
    def get_active(self):
        return synchronization_type_write_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return synchronization_type_write_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_first(self) -> synchronization_type_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> synchronization_type_write_dtos:
        if len(self.dtos) > n:
            return synchronization_type_write_dtos(self.dtos[:n])
        else:
            return synchronization_type_write_dtos(self.dtos)
    def get_last(self) -> synchronization_type_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, synchronization_type_write_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[synchronization_type_write_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[synchronization_type_write_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def check_any(self, check_method: Callable[[synchronization_type_write_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[synchronization_type_write_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[synchronization_type_write_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[synchronization_type_write_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, synchronization_type_write_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, synchronization_type_write_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, synchronization_type_write_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[synchronization_type_write_dto], bool]) -> synchronization_type_write_dtos:
        return synchronization_type_write_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[synchronization_type_write_dto], str]) -> dict[str, synchronization_type_write_dtos]:
        grp_data: dict[str, synchronization_type_write_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = synchronization_type_write_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[synchronization_type_write_dto], str], agg_method: Callable[[synchronization_type_write_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, synchronization_type_write_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[synchronization_type_write_dto], bool]) -> synchronization_type_write_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[synchronization_type_write_dto], any], compare_method: Callable[[any, any], bool]) -> synchronization_type_write_dto | None:
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
class system_attribute_write_dtos(base_write_dtos):
    dtos: list[system_attribute_write_dto]
    def __init__(self, dtos: list[system_attribute_write_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[system_attribute_write_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: system_attribute_write_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[system_attribute_write_dto], dtos2: list[system_attribute_write_dto]):
        return cls(dtos1 + dtos2)
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> system_attribute_write_dto | None:
        found_dtos = list(filter(lambda x: x.system_attribute_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, system_attribute_write_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.system_attribute_uid] = dto
        return res
    def get_active(self):
        return system_attribute_write_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return system_attribute_write_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_first(self) -> system_attribute_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> system_attribute_write_dtos:
        if len(self.dtos) > n:
            return system_attribute_write_dtos(self.dtos[:n])
        else:
            return system_attribute_write_dtos(self.dtos)
    def get_last(self) -> system_attribute_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, system_attribute_write_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[system_attribute_write_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[system_attribute_write_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def check_any(self, check_method: Callable[[system_attribute_write_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[system_attribute_write_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[system_attribute_write_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[system_attribute_write_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, system_attribute_write_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, system_attribute_write_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, system_attribute_write_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[system_attribute_write_dto], bool]) -> system_attribute_write_dtos:
        return system_attribute_write_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[system_attribute_write_dto], str]) -> dict[str, system_attribute_write_dtos]:
        grp_data: dict[str, system_attribute_write_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = system_attribute_write_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[system_attribute_write_dto], str], agg_method: Callable[[system_attribute_write_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, system_attribute_write_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[system_attribute_write_dto], bool]) -> system_attribute_write_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[system_attribute_write_dto], any], compare_method: Callable[[any, any], bool]) -> system_attribute_write_dto | None:
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
class system_constraint_write_dtos(base_write_dtos):
    dtos: list[system_constraint_write_dto]
    def __init__(self, dtos: list[system_constraint_write_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[system_constraint_write_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: system_constraint_write_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[system_constraint_write_dto], dtos2: list[system_constraint_write_dto]):
        return cls(dtos1 + dtos2)
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> system_constraint_write_dto | None:
        found_dtos = list(filter(lambda x: x.system_constraint_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, system_constraint_write_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.system_constraint_uid] = dto
        return res
    def get_active(self):
        return system_constraint_write_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return system_constraint_write_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_first(self) -> system_constraint_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> system_constraint_write_dtos:
        if len(self.dtos) > n:
            return system_constraint_write_dtos(self.dtos[:n])
        else:
            return system_constraint_write_dtos(self.dtos)
    def get_last(self) -> system_constraint_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, system_constraint_write_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[system_constraint_write_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[system_constraint_write_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def check_any(self, check_method: Callable[[system_constraint_write_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[system_constraint_write_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[system_constraint_write_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[system_constraint_write_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, system_constraint_write_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, system_constraint_write_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, system_constraint_write_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[system_constraint_write_dto], bool]) -> system_constraint_write_dtos:
        return system_constraint_write_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[system_constraint_write_dto], str]) -> dict[str, system_constraint_write_dtos]:
        grp_data: dict[str, system_constraint_write_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = system_constraint_write_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[system_constraint_write_dto], str], agg_method: Callable[[system_constraint_write_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, system_constraint_write_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[system_constraint_write_dto], bool]) -> system_constraint_write_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[system_constraint_write_dto], any], compare_method: Callable[[any, any], bool]) -> system_constraint_write_dto | None:
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
class system_database_write_dtos(base_write_dtos):
    dtos: list[system_database_write_dto]
    def __init__(self, dtos: list[system_database_write_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[system_database_write_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: system_database_write_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[system_database_write_dto], dtos2: list[system_database_write_dto]):
        return cls(dtos1 + dtos2)
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> system_database_write_dto | None:
        found_dtos = list(filter(lambda x: x.system_database_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, system_database_write_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.system_database_uid] = dto
        return res
    def get_active(self):
        return system_database_write_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return system_database_write_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_first(self) -> system_database_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> system_database_write_dtos:
        if len(self.dtos) > n:
            return system_database_write_dtos(self.dtos[:n])
        else:
            return system_database_write_dtos(self.dtos)
    def get_last(self) -> system_database_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, system_database_write_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[system_database_write_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[system_database_write_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def check_any(self, check_method: Callable[[system_database_write_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[system_database_write_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[system_database_write_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[system_database_write_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, system_database_write_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, system_database_write_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, system_database_write_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[system_database_write_dto], bool]) -> system_database_write_dtos:
        return system_database_write_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[system_database_write_dto], str]) -> dict[str, system_database_write_dtos]:
        grp_data: dict[str, system_database_write_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = system_database_write_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[system_database_write_dto], str], agg_method: Callable[[system_database_write_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, system_database_write_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[system_database_write_dto], bool]) -> system_database_write_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[system_database_write_dto], any], compare_method: Callable[[any, any], bool]) -> system_database_write_dto | None:
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
class system_exception_write_dtos(base_write_dtos):
    dtos: list[system_exception_write_dto]
    def __init__(self, dtos: list[system_exception_write_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[system_exception_write_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: system_exception_write_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[system_exception_write_dto], dtos2: list[system_exception_write_dto]):
        return cls(dtos1 + dtos2)
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> system_exception_write_dto | None:
        found_dtos = list(filter(lambda x: x.system_exception_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, system_exception_write_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.system_exception_uid] = dto
        return res
    def get_active(self):
        return system_exception_write_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return system_exception_write_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_first(self) -> system_exception_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> system_exception_write_dtos:
        if len(self.dtos) > n:
            return system_exception_write_dtos(self.dtos[:n])
        else:
            return system_exception_write_dtos(self.dtos)
    def get_last(self) -> system_exception_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, system_exception_write_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[system_exception_write_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[system_exception_write_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def check_any(self, check_method: Callable[[system_exception_write_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[system_exception_write_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[system_exception_write_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[system_exception_write_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, system_exception_write_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, system_exception_write_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, system_exception_write_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[system_exception_write_dto], bool]) -> system_exception_write_dtos:
        return system_exception_write_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[system_exception_write_dto], str]) -> dict[str, system_exception_write_dtos]:
        grp_data: dict[str, system_exception_write_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = system_exception_write_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[system_exception_write_dto], str], agg_method: Callable[[system_exception_write_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, system_exception_write_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[system_exception_write_dto], bool]) -> system_exception_write_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[system_exception_write_dto], any], compare_method: Callable[[any, any], bool]) -> system_exception_write_dto | None:
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
class system_instance_write_dtos(base_write_dtos):
    dtos: list[system_instance_write_dto]
    def __init__(self, dtos: list[system_instance_write_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[system_instance_write_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: system_instance_write_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[system_instance_write_dto], dtos2: list[system_instance_write_dto]):
        return cls(dtos1 + dtos2)
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> system_instance_write_dto | None:
        found_dtos = list(filter(lambda x: x.system_instance_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, system_instance_write_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.system_instance_uid] = dto
        return res
    def get_active(self):
        return system_instance_write_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return system_instance_write_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_first(self) -> system_instance_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> system_instance_write_dtos:
        if len(self.dtos) > n:
            return system_instance_write_dtos(self.dtos[:n])
        else:
            return system_instance_write_dtos(self.dtos)
    def get_last(self) -> system_instance_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, system_instance_write_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[system_instance_write_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[system_instance_write_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def check_any(self, check_method: Callable[[system_instance_write_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[system_instance_write_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[system_instance_write_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[system_instance_write_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, system_instance_write_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, system_instance_write_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, system_instance_write_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[system_instance_write_dto], bool]) -> system_instance_write_dtos:
        return system_instance_write_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[system_instance_write_dto], str]) -> dict[str, system_instance_write_dtos]:
        grp_data: dict[str, system_instance_write_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = system_instance_write_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[system_instance_write_dto], str], agg_method: Callable[[system_instance_write_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, system_instance_write_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[system_instance_write_dto], bool]) -> system_instance_write_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[system_instance_write_dto], any], compare_method: Callable[[any, any], bool]) -> system_instance_write_dto | None:
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
class system_license_write_dtos(base_write_dtos):
    dtos: list[system_license_write_dto]
    def __init__(self, dtos: list[system_license_write_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[system_license_write_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: system_license_write_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[system_license_write_dto], dtos2: list[system_license_write_dto]):
        return cls(dtos1 + dtos2)
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> system_license_write_dto | None:
        found_dtos = list(filter(lambda x: x.system_license_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, system_license_write_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.system_license_uid] = dto
        return res
    def get_active(self):
        return system_license_write_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return system_license_write_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_first(self) -> system_license_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> system_license_write_dtos:
        if len(self.dtos) > n:
            return system_license_write_dtos(self.dtos[:n])
        else:
            return system_license_write_dtos(self.dtos)
    def get_last(self) -> system_license_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, system_license_write_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[system_license_write_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[system_license_write_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def check_any(self, check_method: Callable[[system_license_write_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[system_license_write_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[system_license_write_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[system_license_write_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, system_license_write_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, system_license_write_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, system_license_write_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[system_license_write_dto], bool]) -> system_license_write_dtos:
        return system_license_write_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[system_license_write_dto], str]) -> dict[str, system_license_write_dtos]:
        grp_data: dict[str, system_license_write_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = system_license_write_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[system_license_write_dto], str], agg_method: Callable[[system_license_write_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, system_license_write_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[system_license_write_dto], bool]) -> system_license_write_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[system_license_write_dto], any], compare_method: Callable[[any, any], bool]) -> system_license_write_dto | None:
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
class system_lock_write_dtos(base_write_dtos):
    dtos: list[system_lock_write_dto]
    def __init__(self, dtos: list[system_lock_write_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[system_lock_write_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: system_lock_write_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[system_lock_write_dto], dtos2: list[system_lock_write_dto]):
        return cls(dtos1 + dtos2)
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> system_lock_write_dto | None:
        found_dtos = list(filter(lambda x: x.system_lock_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, system_lock_write_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.system_lock_uid] = dto
        return res
    def get_active(self):
        return system_lock_write_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return system_lock_write_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_first(self) -> system_lock_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> system_lock_write_dtos:
        if len(self.dtos) > n:
            return system_lock_write_dtos(self.dtos[:n])
        else:
            return system_lock_write_dtos(self.dtos)
    def get_last(self) -> system_lock_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, system_lock_write_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[system_lock_write_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[system_lock_write_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def check_any(self, check_method: Callable[[system_lock_write_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[system_lock_write_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[system_lock_write_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[system_lock_write_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, system_lock_write_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, system_lock_write_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, system_lock_write_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[system_lock_write_dto], bool]) -> system_lock_write_dtos:
        return system_lock_write_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[system_lock_write_dto], str]) -> dict[str, system_lock_write_dtos]:
        grp_data: dict[str, system_lock_write_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = system_lock_write_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[system_lock_write_dto], str], agg_method: Callable[[system_lock_write_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, system_lock_write_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[system_lock_write_dto], bool]) -> system_lock_write_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[system_lock_write_dto], any], compare_method: Callable[[any, any], bool]) -> system_lock_write_dto | None:
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
class system_module_write_dtos(base_write_dtos):
    dtos: list[system_module_write_dto]
    def __init__(self, dtos: list[system_module_write_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[system_module_write_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: system_module_write_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[system_module_write_dto], dtos2: list[system_module_write_dto]):
        return cls(dtos1 + dtos2)
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> system_module_write_dto | None:
        found_dtos = list(filter(lambda x: x.system_module_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, system_module_write_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.system_module_uid] = dto
        return res
    def get_active(self):
        return system_module_write_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return system_module_write_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_first(self) -> system_module_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> system_module_write_dtos:
        if len(self.dtos) > n:
            return system_module_write_dtos(self.dtos[:n])
        else:
            return system_module_write_dtos(self.dtos)
    def get_last(self) -> system_module_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, system_module_write_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[system_module_write_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[system_module_write_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def check_any(self, check_method: Callable[[system_module_write_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[system_module_write_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[system_module_write_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[system_module_write_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, system_module_write_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, system_module_write_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, system_module_write_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[system_module_write_dto], bool]) -> system_module_write_dtos:
        return system_module_write_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[system_module_write_dto], str]) -> dict[str, system_module_write_dtos]:
        grp_data: dict[str, system_module_write_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = system_module_write_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[system_module_write_dto], str], agg_method: Callable[[system_module_write_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, system_module_write_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[system_module_write_dto], bool]) -> system_module_write_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[system_module_write_dto], any], compare_method: Callable[[any, any], bool]) -> system_module_write_dto | None:
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
class system_query_write_dtos(base_write_dtos):
    dtos: list[system_query_write_dto]
    def __init__(self, dtos: list[system_query_write_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[system_query_write_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: system_query_write_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[system_query_write_dto], dtos2: list[system_query_write_dto]):
        return cls(dtos1 + dtos2)
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> system_query_write_dto | None:
        found_dtos = list(filter(lambda x: x.system_query_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, system_query_write_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.system_query_uid] = dto
        return res
    def get_active(self):
        return system_query_write_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return system_query_write_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_first(self) -> system_query_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> system_query_write_dtos:
        if len(self.dtos) > n:
            return system_query_write_dtos(self.dtos[:n])
        else:
            return system_query_write_dtos(self.dtos)
    def get_last(self) -> system_query_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, system_query_write_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[system_query_write_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[system_query_write_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def check_any(self, check_method: Callable[[system_query_write_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[system_query_write_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[system_query_write_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[system_query_write_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, system_query_write_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, system_query_write_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, system_query_write_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[system_query_write_dto], bool]) -> system_query_write_dtos:
        return system_query_write_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[system_query_write_dto], str]) -> dict[str, system_query_write_dtos]:
        grp_data: dict[str, system_query_write_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = system_query_write_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[system_query_write_dto], str], agg_method: Callable[[system_query_write_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, system_query_write_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[system_query_write_dto], bool]) -> system_query_write_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[system_query_write_dto], any], compare_method: Callable[[any, any], bool]) -> system_query_write_dto | None:
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
class system_request_write_dtos(base_write_dtos):
    dtos: list[system_request_write_dto]
    def __init__(self, dtos: list[system_request_write_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[system_request_write_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: system_request_write_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[system_request_write_dto], dtos2: list[system_request_write_dto]):
        return cls(dtos1 + dtos2)
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> system_request_write_dto | None:
        found_dtos = list(filter(lambda x: x.system_request_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, system_request_write_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.system_request_uid] = dto
        return res
    def get_active(self):
        return system_request_write_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return system_request_write_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_first(self) -> system_request_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> system_request_write_dtos:
        if len(self.dtos) > n:
            return system_request_write_dtos(self.dtos[:n])
        else:
            return system_request_write_dtos(self.dtos)
    def get_last(self) -> system_request_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, system_request_write_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[system_request_write_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[system_request_write_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def check_any(self, check_method: Callable[[system_request_write_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[system_request_write_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[system_request_write_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[system_request_write_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, system_request_write_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, system_request_write_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, system_request_write_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[system_request_write_dto], bool]) -> system_request_write_dtos:
        return system_request_write_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[system_request_write_dto], str]) -> dict[str, system_request_write_dtos]:
        grp_data: dict[str, system_request_write_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = system_request_write_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[system_request_write_dto], str], agg_method: Callable[[system_request_write_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, system_request_write_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[system_request_write_dto], bool]) -> system_request_write_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[system_request_write_dto], any], compare_method: Callable[[any, any], bool]) -> system_request_write_dto | None:
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
class system_setting_write_dtos(base_write_dtos):
    dtos: list[system_setting_write_dto]
    def __init__(self, dtos: list[system_setting_write_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[system_setting_write_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: system_setting_write_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[system_setting_write_dto], dtos2: list[system_setting_write_dto]):
        return cls(dtos1 + dtos2)
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> system_setting_write_dto | None:
        found_dtos = list(filter(lambda x: x.system_setting_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, system_setting_write_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.system_setting_uid] = dto
        return res
    def get_active(self):
        return system_setting_write_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return system_setting_write_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_first(self) -> system_setting_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> system_setting_write_dtos:
        if len(self.dtos) > n:
            return system_setting_write_dtos(self.dtos[:n])
        else:
            return system_setting_write_dtos(self.dtos)
    def get_last(self) -> system_setting_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, system_setting_write_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[system_setting_write_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[system_setting_write_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def check_any(self, check_method: Callable[[system_setting_write_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[system_setting_write_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[system_setting_write_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[system_setting_write_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, system_setting_write_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, system_setting_write_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, system_setting_write_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[system_setting_write_dto], bool]) -> system_setting_write_dtos:
        return system_setting_write_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[system_setting_write_dto], str]) -> dict[str, system_setting_write_dtos]:
        grp_data: dict[str, system_setting_write_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = system_setting_write_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[system_setting_write_dto], str], agg_method: Callable[[system_setting_write_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, system_setting_write_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[system_setting_write_dto], bool]) -> system_setting_write_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[system_setting_write_dto], any], compare_method: Callable[[any, any], bool]) -> system_setting_write_dto | None:
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
class system_setting_account_write_dtos(base_write_dtos):
    dtos: list[system_setting_account_write_dto]
    def __init__(self, dtos: list[system_setting_account_write_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[system_setting_account_write_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: system_setting_account_write_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[system_setting_account_write_dto], dtos2: list[system_setting_account_write_dto]):
        return cls(dtos1 + dtos2)
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> system_setting_account_write_dto | None:
        found_dtos = list(filter(lambda x: x.system_setting_account_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, system_setting_account_write_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.system_setting_account_uid] = dto
        return res
    def get_active(self):
        return system_setting_account_write_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return system_setting_account_write_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_first(self) -> system_setting_account_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> system_setting_account_write_dtos:
        if len(self.dtos) > n:
            return system_setting_account_write_dtos(self.dtos[:n])
        else:
            return system_setting_account_write_dtos(self.dtos)
    def get_last(self) -> system_setting_account_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, system_setting_account_write_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[system_setting_account_write_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[system_setting_account_write_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def check_any(self, check_method: Callable[[system_setting_account_write_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[system_setting_account_write_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[system_setting_account_write_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[system_setting_account_write_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, system_setting_account_write_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, system_setting_account_write_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, system_setting_account_write_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[system_setting_account_write_dto], bool]) -> system_setting_account_write_dtos:
        return system_setting_account_write_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[system_setting_account_write_dto], str]) -> dict[str, system_setting_account_write_dtos]:
        grp_data: dict[str, system_setting_account_write_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = system_setting_account_write_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[system_setting_account_write_dto], str], agg_method: Callable[[system_setting_account_write_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, system_setting_account_write_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[system_setting_account_write_dto], bool]) -> system_setting_account_write_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[system_setting_account_write_dto], any], compare_method: Callable[[any, any], bool]) -> system_setting_account_write_dto | None:
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
class system_state_write_dtos(base_write_dtos):
    dtos: list[system_state_write_dto]
    def __init__(self, dtos: list[system_state_write_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[system_state_write_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: system_state_write_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[system_state_write_dto], dtos2: list[system_state_write_dto]):
        return cls(dtos1 + dtos2)
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> system_state_write_dto | None:
        found_dtos = list(filter(lambda x: x.system_state_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, system_state_write_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.system_state_uid] = dto
        return res
    def get_active(self):
        return system_state_write_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return system_state_write_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_first(self) -> system_state_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> system_state_write_dtos:
        if len(self.dtos) > n:
            return system_state_write_dtos(self.dtos[:n])
        else:
            return system_state_write_dtos(self.dtos)
    def get_last(self) -> system_state_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, system_state_write_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[system_state_write_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[system_state_write_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def check_any(self, check_method: Callable[[system_state_write_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[system_state_write_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[system_state_write_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[system_state_write_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, system_state_write_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, system_state_write_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, system_state_write_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[system_state_write_dto], bool]) -> system_state_write_dtos:
        return system_state_write_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[system_state_write_dto], str]) -> dict[str, system_state_write_dtos]:
        grp_data: dict[str, system_state_write_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = system_state_write_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[system_state_write_dto], str], agg_method: Callable[[system_state_write_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, system_state_write_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[system_state_write_dto], bool]) -> system_state_write_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[system_state_write_dto], any], compare_method: Callable[[any, any], bool]) -> system_state_write_dto | None:
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
class system_table_write_dtos(base_write_dtos):
    dtos: list[system_table_write_dto]
    def __init__(self, dtos: list[system_table_write_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[system_table_write_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: system_table_write_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[system_table_write_dto], dtos2: list[system_table_write_dto]):
        return cls(dtos1 + dtos2)
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> system_table_write_dto | None:
        found_dtos = list(filter(lambda x: x.system_table_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, system_table_write_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.system_table_uid] = dto
        return res
    def get_active(self):
        return system_table_write_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return system_table_write_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_first(self) -> system_table_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> system_table_write_dtos:
        if len(self.dtos) > n:
            return system_table_write_dtos(self.dtos[:n])
        else:
            return system_table_write_dtos(self.dtos)
    def get_last(self) -> system_table_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, system_table_write_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[system_table_write_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[system_table_write_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def check_any(self, check_method: Callable[[system_table_write_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[system_table_write_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[system_table_write_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[system_table_write_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, system_table_write_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, system_table_write_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, system_table_write_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[system_table_write_dto], bool]) -> system_table_write_dtos:
        return system_table_write_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[system_table_write_dto], str]) -> dict[str, system_table_write_dtos]:
        grp_data: dict[str, system_table_write_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = system_table_write_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[system_table_write_dto], str], agg_method: Callable[[system_table_write_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, system_table_write_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[system_table_write_dto], bool]) -> system_table_write_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[system_table_write_dto], any], compare_method: Callable[[any, any], bool]) -> system_table_write_dto | None:
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
class system_thread_write_dtos(base_write_dtos):
    dtos: list[system_thread_write_dto]
    def __init__(self, dtos: list[system_thread_write_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[system_thread_write_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: system_thread_write_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[system_thread_write_dto], dtos2: list[system_thread_write_dto]):
        return cls(dtos1 + dtos2)
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> system_thread_write_dto | None:
        found_dtos = list(filter(lambda x: x.system_thread_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, system_thread_write_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.system_thread_uid] = dto
        return res
    def get_active(self):
        return system_thread_write_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return system_thread_write_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_first(self) -> system_thread_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> system_thread_write_dtos:
        if len(self.dtos) > n:
            return system_thread_write_dtos(self.dtos[:n])
        else:
            return system_thread_write_dtos(self.dtos)
    def get_last(self) -> system_thread_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, system_thread_write_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[system_thread_write_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[system_thread_write_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def check_any(self, check_method: Callable[[system_thread_write_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[system_thread_write_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[system_thread_write_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[system_thread_write_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, system_thread_write_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, system_thread_write_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, system_thread_write_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[system_thread_write_dto], bool]) -> system_thread_write_dtos:
        return system_thread_write_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[system_thread_write_dto], str]) -> dict[str, system_thread_write_dtos]:
        grp_data: dict[str, system_thread_write_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = system_thread_write_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[system_thread_write_dto], str], agg_method: Callable[[system_thread_write_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, system_thread_write_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[system_thread_write_dto], bool]) -> system_thread_write_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[system_thread_write_dto], any], compare_method: Callable[[any, any], bool]) -> system_thread_write_dto | None:
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
class system_version_write_dtos(base_write_dtos):
    dtos: list[system_version_write_dto]
    def __init__(self, dtos: list[system_version_write_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[system_version_write_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: system_version_write_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[system_version_write_dto], dtos2: list[system_version_write_dto]):
        return cls(dtos1 + dtos2)
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> system_version_write_dto | None:
        found_dtos = list(filter(lambda x: x.system_version_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, system_version_write_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.system_version_uid] = dto
        return res
    def get_active(self):
        return system_version_write_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return system_version_write_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_first(self) -> system_version_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> system_version_write_dtos:
        if len(self.dtos) > n:
            return system_version_write_dtos(self.dtos[:n])
        else:
            return system_version_write_dtos(self.dtos)
    def get_last(self) -> system_version_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, system_version_write_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[system_version_write_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[system_version_write_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def check_any(self, check_method: Callable[[system_version_write_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[system_version_write_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[system_version_write_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[system_version_write_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, system_version_write_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, system_version_write_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, system_version_write_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[system_version_write_dto], bool]) -> system_version_write_dtos:
        return system_version_write_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[system_version_write_dto], str]) -> dict[str, system_version_write_dtos]:
        grp_data: dict[str, system_version_write_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = system_version_write_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[system_version_write_dto], str], agg_method: Callable[[system_version_write_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, system_version_write_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[system_version_write_dto], bool]) -> system_version_write_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[system_version_write_dto], any], compare_method: Callable[[any, any], bool]) -> system_version_write_dto | None:
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
class tenant_write_dtos(base_write_dtos):
    dtos: list[tenant_write_dto]
    def __init__(self, dtos: list[tenant_write_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[tenant_write_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: tenant_write_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[tenant_write_dto], dtos2: list[tenant_write_dto]):
        return cls(dtos1 + dtos2)
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> tenant_write_dto | None:
        found_dtos = list(filter(lambda x: x.tenant_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, tenant_write_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.tenant_uid] = dto
        return res
    def get_active(self):
        return tenant_write_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return tenant_write_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_first(self) -> tenant_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> tenant_write_dtos:
        if len(self.dtos) > n:
            return tenant_write_dtos(self.dtos[:n])
        else:
            return tenant_write_dtos(self.dtos)
    def get_last(self) -> tenant_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, tenant_write_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[tenant_write_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[tenant_write_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def check_any(self, check_method: Callable[[tenant_write_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[tenant_write_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[tenant_write_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[tenant_write_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, tenant_write_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, tenant_write_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, tenant_write_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[tenant_write_dto], bool]) -> tenant_write_dtos:
        return tenant_write_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[tenant_write_dto], str]) -> dict[str, tenant_write_dtos]:
        grp_data: dict[str, tenant_write_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = tenant_write_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[tenant_write_dto], str], agg_method: Callable[[tenant_write_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, tenant_write_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[tenant_write_dto], bool]) -> tenant_write_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[tenant_write_dto], any], compare_method: Callable[[any, any], bool]) -> tenant_write_dto | None:
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
class tenant_account_write_dtos(base_write_dtos):
    dtos: list[tenant_account_write_dto]
    def __init__(self, dtos: list[tenant_account_write_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[tenant_account_write_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: tenant_account_write_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[tenant_account_write_dto], dtos2: list[tenant_account_write_dto]):
        return cls(dtos1 + dtos2)
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> tenant_account_write_dto | None:
        found_dtos = list(filter(lambda x: x.tenant_account_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, tenant_account_write_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.tenant_account_uid] = dto
        return res
    def get_active(self):
        return tenant_account_write_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return tenant_account_write_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_first(self) -> tenant_account_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> tenant_account_write_dtos:
        if len(self.dtos) > n:
            return tenant_account_write_dtos(self.dtos[:n])
        else:
            return tenant_account_write_dtos(self.dtos)
    def get_last(self) -> tenant_account_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, tenant_account_write_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[tenant_account_write_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[tenant_account_write_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def check_any(self, check_method: Callable[[tenant_account_write_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[tenant_account_write_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[tenant_account_write_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[tenant_account_write_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, tenant_account_write_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, tenant_account_write_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, tenant_account_write_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[tenant_account_write_dto], bool]) -> tenant_account_write_dtos:
        return tenant_account_write_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[tenant_account_write_dto], str]) -> dict[str, tenant_account_write_dtos]:
        grp_data: dict[str, tenant_account_write_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = tenant_account_write_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[tenant_account_write_dto], str], agg_method: Callable[[tenant_account_write_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, tenant_account_write_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[tenant_account_write_dto], bool]) -> tenant_account_write_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[tenant_account_write_dto], any], compare_method: Callable[[any, any], bool]) -> tenant_account_write_dto | None:
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
class tenant_category_write_dtos(base_write_dtos):
    dtos: list[tenant_category_write_dto]
    def __init__(self, dtos: list[tenant_category_write_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[tenant_category_write_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: tenant_category_write_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[tenant_category_write_dto], dtos2: list[tenant_category_write_dto]):
        return cls(dtos1 + dtos2)
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> tenant_category_write_dto | None:
        found_dtos = list(filter(lambda x: x.tenant_category_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, tenant_category_write_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.tenant_category_uid] = dto
        return res
    def get_active(self):
        return tenant_category_write_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return tenant_category_write_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_first(self) -> tenant_category_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> tenant_category_write_dtos:
        if len(self.dtos) > n:
            return tenant_category_write_dtos(self.dtos[:n])
        else:
            return tenant_category_write_dtos(self.dtos)
    def get_last(self) -> tenant_category_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, tenant_category_write_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[tenant_category_write_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[tenant_category_write_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def check_any(self, check_method: Callable[[tenant_category_write_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[tenant_category_write_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[tenant_category_write_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[tenant_category_write_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, tenant_category_write_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, tenant_category_write_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, tenant_category_write_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[tenant_category_write_dto], bool]) -> tenant_category_write_dtos:
        return tenant_category_write_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[tenant_category_write_dto], str]) -> dict[str, tenant_category_write_dtos]:
        grp_data: dict[str, tenant_category_write_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = tenant_category_write_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[tenant_category_write_dto], str], agg_method: Callable[[tenant_category_write_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, tenant_category_write_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[tenant_category_write_dto], bool]) -> tenant_category_write_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[tenant_category_write_dto], any], compare_method: Callable[[any, any], bool]) -> tenant_category_write_dto | None:
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
class tenant_country_write_dtos(base_write_dtos):
    dtos: list[tenant_country_write_dto]
    def __init__(self, dtos: list[tenant_country_write_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[tenant_country_write_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: tenant_country_write_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[tenant_country_write_dto], dtos2: list[tenant_country_write_dto]):
        return cls(dtos1 + dtos2)
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> tenant_country_write_dto | None:
        found_dtos = list(filter(lambda x: x.tenant_country_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, tenant_country_write_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.tenant_country_uid] = dto
        return res
    def get_active(self):
        return tenant_country_write_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return tenant_country_write_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_first(self) -> tenant_country_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> tenant_country_write_dtos:
        if len(self.dtos) > n:
            return tenant_country_write_dtos(self.dtos[:n])
        else:
            return tenant_country_write_dtos(self.dtos)
    def get_last(self) -> tenant_country_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, tenant_country_write_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[tenant_country_write_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[tenant_country_write_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def check_any(self, check_method: Callable[[tenant_country_write_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[tenant_country_write_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[tenant_country_write_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[tenant_country_write_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, tenant_country_write_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, tenant_country_write_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, tenant_country_write_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[tenant_country_write_dto], bool]) -> tenant_country_write_dtos:
        return tenant_country_write_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[tenant_country_write_dto], str]) -> dict[str, tenant_country_write_dtos]:
        grp_data: dict[str, tenant_country_write_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = tenant_country_write_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[tenant_country_write_dto], str], agg_method: Callable[[tenant_country_write_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, tenant_country_write_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[tenant_country_write_dto], bool]) -> tenant_country_write_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[tenant_country_write_dto], any], compare_method: Callable[[any, any], bool]) -> tenant_country_write_dto | None:
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
class tenant_license_write_dtos(base_write_dtos):
    dtos: list[tenant_license_write_dto]
    def __init__(self, dtos: list[tenant_license_write_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[tenant_license_write_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: tenant_license_write_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[tenant_license_write_dto], dtos2: list[tenant_license_write_dto]):
        return cls(dtos1 + dtos2)
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> tenant_license_write_dto | None:
        found_dtos = list(filter(lambda x: x.tenant_license_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, tenant_license_write_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.tenant_license_uid] = dto
        return res
    def get_active(self):
        return tenant_license_write_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return tenant_license_write_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_first(self) -> tenant_license_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> tenant_license_write_dtos:
        if len(self.dtos) > n:
            return tenant_license_write_dtos(self.dtos[:n])
        else:
            return tenant_license_write_dtos(self.dtos)
    def get_last(self) -> tenant_license_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, tenant_license_write_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[tenant_license_write_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[tenant_license_write_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def check_any(self, check_method: Callable[[tenant_license_write_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[tenant_license_write_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[tenant_license_write_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[tenant_license_write_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, tenant_license_write_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, tenant_license_write_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, tenant_license_write_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[tenant_license_write_dto], bool]) -> tenant_license_write_dtos:
        return tenant_license_write_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[tenant_license_write_dto], str]) -> dict[str, tenant_license_write_dtos]:
        grp_data: dict[str, tenant_license_write_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = tenant_license_write_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[tenant_license_write_dto], str], agg_method: Callable[[tenant_license_write_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, tenant_license_write_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[tenant_license_write_dto], bool]) -> tenant_license_write_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[tenant_license_write_dto], any], compare_method: Callable[[any, any], bool]) -> tenant_license_write_dto | None:
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
class tenant_payment_write_dtos(base_write_dtos):
    dtos: list[tenant_payment_write_dto]
    def __init__(self, dtos: list[tenant_payment_write_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[tenant_payment_write_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: tenant_payment_write_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[tenant_payment_write_dto], dtos2: list[tenant_payment_write_dto]):
        return cls(dtos1 + dtos2)
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> tenant_payment_write_dto | None:
        found_dtos = list(filter(lambda x: x.tenant_payment_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, tenant_payment_write_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.tenant_payment_uid] = dto
        return res
    def get_active(self):
        return tenant_payment_write_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return tenant_payment_write_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_first(self) -> tenant_payment_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> tenant_payment_write_dtos:
        if len(self.dtos) > n:
            return tenant_payment_write_dtos(self.dtos[:n])
        else:
            return tenant_payment_write_dtos(self.dtos)
    def get_last(self) -> tenant_payment_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, tenant_payment_write_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[tenant_payment_write_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[tenant_payment_write_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def check_any(self, check_method: Callable[[tenant_payment_write_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[tenant_payment_write_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[tenant_payment_write_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[tenant_payment_write_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, tenant_payment_write_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, tenant_payment_write_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, tenant_payment_write_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[tenant_payment_write_dto], bool]) -> tenant_payment_write_dtos:
        return tenant_payment_write_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[tenant_payment_write_dto], str]) -> dict[str, tenant_payment_write_dtos]:
        grp_data: dict[str, tenant_payment_write_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = tenant_payment_write_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[tenant_payment_write_dto], str], agg_method: Callable[[tenant_payment_write_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, tenant_payment_write_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[tenant_payment_write_dto], bool]) -> tenant_payment_write_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[tenant_payment_write_dto], any], compare_method: Callable[[any, any], bool]) -> tenant_payment_write_dto | None:
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
class tenant_payment_type_write_dtos(base_write_dtos):
    dtos: list[tenant_payment_type_write_dto]
    def __init__(self, dtos: list[tenant_payment_type_write_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[tenant_payment_type_write_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: tenant_payment_type_write_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[tenant_payment_type_write_dto], dtos2: list[tenant_payment_type_write_dto]):
        return cls(dtos1 + dtos2)
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> tenant_payment_type_write_dto | None:
        found_dtos = list(filter(lambda x: x.tenant_payment_type_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, tenant_payment_type_write_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.tenant_payment_type_uid] = dto
        return res
    def get_active(self):
        return tenant_payment_type_write_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return tenant_payment_type_write_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_first(self) -> tenant_payment_type_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> tenant_payment_type_write_dtos:
        if len(self.dtos) > n:
            return tenant_payment_type_write_dtos(self.dtos[:n])
        else:
            return tenant_payment_type_write_dtos(self.dtos)
    def get_last(self) -> tenant_payment_type_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, tenant_payment_type_write_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[tenant_payment_type_write_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[tenant_payment_type_write_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def check_any(self, check_method: Callable[[tenant_payment_type_write_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[tenant_payment_type_write_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[tenant_payment_type_write_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[tenant_payment_type_write_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, tenant_payment_type_write_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, tenant_payment_type_write_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, tenant_payment_type_write_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[tenant_payment_type_write_dto], bool]) -> tenant_payment_type_write_dtos:
        return tenant_payment_type_write_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[tenant_payment_type_write_dto], str]) -> dict[str, tenant_payment_type_write_dtos]:
        grp_data: dict[str, tenant_payment_type_write_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = tenant_payment_type_write_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[tenant_payment_type_write_dto], str], agg_method: Callable[[tenant_payment_type_write_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, tenant_payment_type_write_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[tenant_payment_type_write_dto], bool]) -> tenant_payment_type_write_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[tenant_payment_type_write_dto], any], compare_method: Callable[[any, any], bool]) -> tenant_payment_type_write_dto | None:
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
class tenant_role_write_dtos(base_write_dtos):
    dtos: list[tenant_role_write_dto]
    def __init__(self, dtos: list[tenant_role_write_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[tenant_role_write_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: tenant_role_write_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[tenant_role_write_dto], dtos2: list[tenant_role_write_dto]):
        return cls(dtos1 + dtos2)
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> tenant_role_write_dto | None:
        found_dtos = list(filter(lambda x: x.tenant_role_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, tenant_role_write_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.tenant_role_uid] = dto
        return res
    def get_active(self):
        return tenant_role_write_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return tenant_role_write_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_first(self) -> tenant_role_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> tenant_role_write_dtos:
        if len(self.dtos) > n:
            return tenant_role_write_dtos(self.dtos[:n])
        else:
            return tenant_role_write_dtos(self.dtos)
    def get_last(self) -> tenant_role_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, tenant_role_write_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[tenant_role_write_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[tenant_role_write_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def check_any(self, check_method: Callable[[tenant_role_write_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[tenant_role_write_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[tenant_role_write_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[tenant_role_write_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, tenant_role_write_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, tenant_role_write_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, tenant_role_write_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[tenant_role_write_dto], bool]) -> tenant_role_write_dtos:
        return tenant_role_write_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[tenant_role_write_dto], str]) -> dict[str, tenant_role_write_dtos]:
        grp_data: dict[str, tenant_role_write_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = tenant_role_write_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[tenant_role_write_dto], str], agg_method: Callable[[tenant_role_write_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, tenant_role_write_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[tenant_role_write_dto], bool]) -> tenant_role_write_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[tenant_role_write_dto], any], compare_method: Callable[[any, any], bool]) -> tenant_role_write_dto | None:
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
class tenant_status_write_dtos(base_write_dtos):
    dtos: list[tenant_status_write_dto]
    def __init__(self, dtos: list[tenant_status_write_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[tenant_status_write_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: tenant_status_write_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[tenant_status_write_dto], dtos2: list[tenant_status_write_dto]):
        return cls(dtos1 + dtos2)
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> tenant_status_write_dto | None:
        found_dtos = list(filter(lambda x: x.tenant_status_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, tenant_status_write_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.tenant_status_uid] = dto
        return res
    def get_active(self):
        return tenant_status_write_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return tenant_status_write_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_first(self) -> tenant_status_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> tenant_status_write_dtos:
        if len(self.dtos) > n:
            return tenant_status_write_dtos(self.dtos[:n])
        else:
            return tenant_status_write_dtos(self.dtos)
    def get_last(self) -> tenant_status_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, tenant_status_write_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[tenant_status_write_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[tenant_status_write_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def check_any(self, check_method: Callable[[tenant_status_write_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[tenant_status_write_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[tenant_status_write_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[tenant_status_write_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, tenant_status_write_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, tenant_status_write_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, tenant_status_write_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[tenant_status_write_dto], bool]) -> tenant_status_write_dtos:
        return tenant_status_write_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[tenant_status_write_dto], str]) -> dict[str, tenant_status_write_dtos]:
        grp_data: dict[str, tenant_status_write_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = tenant_status_write_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[tenant_status_write_dto], str], agg_method: Callable[[tenant_status_write_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, tenant_status_write_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[tenant_status_write_dto], bool]) -> tenant_status_write_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[tenant_status_write_dto], any], compare_method: Callable[[any, any], bool]) -> tenant_status_write_dto | None:
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
class tenant_type_write_dtos(base_write_dtos):
    dtos: list[tenant_type_write_dto]
    def __init__(self, dtos: list[tenant_type_write_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[tenant_type_write_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: tenant_type_write_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[tenant_type_write_dto], dtos2: list[tenant_type_write_dto]):
        return cls(dtos1 + dtos2)
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> tenant_type_write_dto | None:
        found_dtos = list(filter(lambda x: x.tenant_type_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, tenant_type_write_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.tenant_type_uid] = dto
        return res
    def get_active(self):
        return tenant_type_write_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return tenant_type_write_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_first(self) -> tenant_type_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> tenant_type_write_dtos:
        if len(self.dtos) > n:
            return tenant_type_write_dtos(self.dtos[:n])
        else:
            return tenant_type_write_dtos(self.dtos)
    def get_last(self) -> tenant_type_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, tenant_type_write_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[tenant_type_write_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[tenant_type_write_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def check_any(self, check_method: Callable[[tenant_type_write_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[tenant_type_write_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[tenant_type_write_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[tenant_type_write_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, tenant_type_write_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, tenant_type_write_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, tenant_type_write_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[tenant_type_write_dto], bool]) -> tenant_type_write_dtos:
        return tenant_type_write_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[tenant_type_write_dto], str]) -> dict[str, tenant_type_write_dtos]:
        grp_data: dict[str, tenant_type_write_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = tenant_type_write_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[tenant_type_write_dto], str], agg_method: Callable[[tenant_type_write_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, tenant_type_write_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[tenant_type_write_dto], bool]) -> tenant_type_write_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[tenant_type_write_dto], any], compare_method: Callable[[any, any], bool]) -> tenant_type_write_dto | None:
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
class time_approval_write_dtos(base_write_dtos):
    dtos: list[time_approval_write_dto]
    def __init__(self, dtos: list[time_approval_write_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[time_approval_write_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: time_approval_write_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[time_approval_write_dto], dtos2: list[time_approval_write_dto]):
        return cls(dtos1 + dtos2)
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> time_approval_write_dto | None:
        found_dtos = list(filter(lambda x: x.time_approval_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, time_approval_write_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.time_approval_uid] = dto
        return res
    def get_active(self):
        return time_approval_write_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return time_approval_write_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_first(self) -> time_approval_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> time_approval_write_dtos:
        if len(self.dtos) > n:
            return time_approval_write_dtos(self.dtos[:n])
        else:
            return time_approval_write_dtos(self.dtos)
    def get_last(self) -> time_approval_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, time_approval_write_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[time_approval_write_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[time_approval_write_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def check_any(self, check_method: Callable[[time_approval_write_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[time_approval_write_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[time_approval_write_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[time_approval_write_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, time_approval_write_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, time_approval_write_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, time_approval_write_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[time_approval_write_dto], bool]) -> time_approval_write_dtos:
        return time_approval_write_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[time_approval_write_dto], str]) -> dict[str, time_approval_write_dtos]:
        grp_data: dict[str, time_approval_write_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = time_approval_write_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[time_approval_write_dto], str], agg_method: Callable[[time_approval_write_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, time_approval_write_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[time_approval_write_dto], bool]) -> time_approval_write_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[time_approval_write_dto], any], compare_method: Callable[[any, any], bool]) -> time_approval_write_dto | None:
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
class time_entry_write_dtos(base_write_dtos):
    dtos: list[time_entry_write_dto]
    def __init__(self, dtos: list[time_entry_write_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[time_entry_write_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: time_entry_write_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[time_entry_write_dto], dtos2: list[time_entry_write_dto]):
        return cls(dtos1 + dtos2)
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> time_entry_write_dto | None:
        found_dtos = list(filter(lambda x: x.time_entry_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, time_entry_write_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.time_entry_uid] = dto
        return res
    def get_active(self):
        return time_entry_write_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return time_entry_write_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_first(self) -> time_entry_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> time_entry_write_dtos:
        if len(self.dtos) > n:
            return time_entry_write_dtos(self.dtos[:n])
        else:
            return time_entry_write_dtos(self.dtos)
    def get_last(self) -> time_entry_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, time_entry_write_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[time_entry_write_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[time_entry_write_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def check_any(self, check_method: Callable[[time_entry_write_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[time_entry_write_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[time_entry_write_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[time_entry_write_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, time_entry_write_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, time_entry_write_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, time_entry_write_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[time_entry_write_dto], bool]) -> time_entry_write_dtos:
        return time_entry_write_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[time_entry_write_dto], str]) -> dict[str, time_entry_write_dtos]:
        grp_data: dict[str, time_entry_write_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = time_entry_write_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[time_entry_write_dto], str], agg_method: Callable[[time_entry_write_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, time_entry_write_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[time_entry_write_dto], bool]) -> time_entry_write_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[time_entry_write_dto], any], compare_method: Callable[[any, any], bool]) -> time_entry_write_dto | None:
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
class time_entry_final_write_dtos(base_write_dtos):
    dtos: list[time_entry_final_write_dto]
    def __init__(self, dtos: list[time_entry_final_write_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[time_entry_final_write_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: time_entry_final_write_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[time_entry_final_write_dto], dtos2: list[time_entry_final_write_dto]):
        return cls(dtos1 + dtos2)
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> time_entry_final_write_dto | None:
        found_dtos = list(filter(lambda x: x.time_entry_final_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, time_entry_final_write_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.time_entry_final_uid] = dto
        return res
    def get_active(self):
        return time_entry_final_write_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return time_entry_final_write_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_first(self) -> time_entry_final_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> time_entry_final_write_dtos:
        if len(self.dtos) > n:
            return time_entry_final_write_dtos(self.dtos[:n])
        else:
            return time_entry_final_write_dtos(self.dtos)
    def get_last(self) -> time_entry_final_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, time_entry_final_write_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[time_entry_final_write_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[time_entry_final_write_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def check_any(self, check_method: Callable[[time_entry_final_write_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[time_entry_final_write_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[time_entry_final_write_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[time_entry_final_write_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, time_entry_final_write_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, time_entry_final_write_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, time_entry_final_write_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[time_entry_final_write_dto], bool]) -> time_entry_final_write_dtos:
        return time_entry_final_write_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[time_entry_final_write_dto], str]) -> dict[str, time_entry_final_write_dtos]:
        grp_data: dict[str, time_entry_final_write_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = time_entry_final_write_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[time_entry_final_write_dto], str], agg_method: Callable[[time_entry_final_write_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, time_entry_final_write_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[time_entry_final_write_dto], bool]) -> time_entry_final_write_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[time_entry_final_write_dto], any], compare_method: Callable[[any, any], bool]) -> time_entry_final_write_dto | None:
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
class time_entry_invoice_write_dtos(base_write_dtos):
    dtos: list[time_entry_invoice_write_dto]
    def __init__(self, dtos: list[time_entry_invoice_write_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[time_entry_invoice_write_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: time_entry_invoice_write_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[time_entry_invoice_write_dto], dtos2: list[time_entry_invoice_write_dto]):
        return cls(dtos1 + dtos2)
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> time_entry_invoice_write_dto | None:
        found_dtos = list(filter(lambda x: x.time_entry_invoice_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, time_entry_invoice_write_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.time_entry_invoice_uid] = dto
        return res
    def get_active(self):
        return time_entry_invoice_write_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return time_entry_invoice_write_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_first(self) -> time_entry_invoice_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> time_entry_invoice_write_dtos:
        if len(self.dtos) > n:
            return time_entry_invoice_write_dtos(self.dtos[:n])
        else:
            return time_entry_invoice_write_dtos(self.dtos)
    def get_last(self) -> time_entry_invoice_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, time_entry_invoice_write_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[time_entry_invoice_write_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[time_entry_invoice_write_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def check_any(self, check_method: Callable[[time_entry_invoice_write_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[time_entry_invoice_write_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[time_entry_invoice_write_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[time_entry_invoice_write_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, time_entry_invoice_write_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, time_entry_invoice_write_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, time_entry_invoice_write_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[time_entry_invoice_write_dto], bool]) -> time_entry_invoice_write_dtos:
        return time_entry_invoice_write_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[time_entry_invoice_write_dto], str]) -> dict[str, time_entry_invoice_write_dtos]:
        grp_data: dict[str, time_entry_invoice_write_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = time_entry_invoice_write_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[time_entry_invoice_write_dto], str], agg_method: Callable[[time_entry_invoice_write_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, time_entry_invoice_write_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[time_entry_invoice_write_dto], bool]) -> time_entry_invoice_write_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[time_entry_invoice_write_dto], any], compare_method: Callable[[any, any], bool]) -> time_entry_invoice_write_dto | None:
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
class time_rule_write_dtos(base_write_dtos):
    dtos: list[time_rule_write_dto]
    def __init__(self, dtos: list[time_rule_write_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[time_rule_write_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: time_rule_write_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[time_rule_write_dto], dtos2: list[time_rule_write_dto]):
        return cls(dtos1 + dtos2)
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> time_rule_write_dto | None:
        found_dtos = list(filter(lambda x: x.time_rule_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, time_rule_write_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.time_rule_uid] = dto
        return res
    def get_active(self):
        return time_rule_write_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return time_rule_write_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_first(self) -> time_rule_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> time_rule_write_dtos:
        if len(self.dtos) > n:
            return time_rule_write_dtos(self.dtos[:n])
        else:
            return time_rule_write_dtos(self.dtos)
    def get_last(self) -> time_rule_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, time_rule_write_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[time_rule_write_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[time_rule_write_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def check_any(self, check_method: Callable[[time_rule_write_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[time_rule_write_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[time_rule_write_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[time_rule_write_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, time_rule_write_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, time_rule_write_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, time_rule_write_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[time_rule_write_dto], bool]) -> time_rule_write_dtos:
        return time_rule_write_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[time_rule_write_dto], str]) -> dict[str, time_rule_write_dtos]:
        grp_data: dict[str, time_rule_write_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = time_rule_write_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[time_rule_write_dto], str], agg_method: Callable[[time_rule_write_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, time_rule_write_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[time_rule_write_dto], bool]) -> time_rule_write_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[time_rule_write_dto], any], compare_method: Callable[[any, any], bool]) -> time_rule_write_dto | None:
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
class time_rule_client_write_dtos(base_write_dtos):
    dtos: list[time_rule_client_write_dto]
    def __init__(self, dtos: list[time_rule_client_write_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[time_rule_client_write_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: time_rule_client_write_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[time_rule_client_write_dto], dtos2: list[time_rule_client_write_dto]):
        return cls(dtos1 + dtos2)
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> time_rule_client_write_dto | None:
        found_dtos = list(filter(lambda x: x.time_rule_client_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, time_rule_client_write_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.time_rule_client_uid] = dto
        return res
    def get_active(self):
        return time_rule_client_write_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return time_rule_client_write_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_first(self) -> time_rule_client_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> time_rule_client_write_dtos:
        if len(self.dtos) > n:
            return time_rule_client_write_dtos(self.dtos[:n])
        else:
            return time_rule_client_write_dtos(self.dtos)
    def get_last(self) -> time_rule_client_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, time_rule_client_write_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[time_rule_client_write_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[time_rule_client_write_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def check_any(self, check_method: Callable[[time_rule_client_write_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[time_rule_client_write_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[time_rule_client_write_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[time_rule_client_write_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, time_rule_client_write_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, time_rule_client_write_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, time_rule_client_write_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[time_rule_client_write_dto], bool]) -> time_rule_client_write_dtos:
        return time_rule_client_write_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[time_rule_client_write_dto], str]) -> dict[str, time_rule_client_write_dtos]:
        grp_data: dict[str, time_rule_client_write_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = time_rule_client_write_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[time_rule_client_write_dto], str], agg_method: Callable[[time_rule_client_write_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, time_rule_client_write_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[time_rule_client_write_dto], bool]) -> time_rule_client_write_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[time_rule_client_write_dto], any], compare_method: Callable[[any, any], bool]) -> time_rule_client_write_dto | None:
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
class time_submit_write_dtos(base_write_dtos):
    dtos: list[time_submit_write_dto]
    def __init__(self, dtos: list[time_submit_write_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[time_submit_write_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: time_submit_write_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[time_submit_write_dto], dtos2: list[time_submit_write_dto]):
        return cls(dtos1 + dtos2)
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> time_submit_write_dto | None:
        found_dtos = list(filter(lambda x: x.time_submit_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, time_submit_write_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.time_submit_uid] = dto
        return res
    def get_active(self):
        return time_submit_write_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return time_submit_write_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_first(self) -> time_submit_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> time_submit_write_dtos:
        if len(self.dtos) > n:
            return time_submit_write_dtos(self.dtos[:n])
        else:
            return time_submit_write_dtos(self.dtos)
    def get_last(self) -> time_submit_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, time_submit_write_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[time_submit_write_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[time_submit_write_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def check_any(self, check_method: Callable[[time_submit_write_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[time_submit_write_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[time_submit_write_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[time_submit_write_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, time_submit_write_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, time_submit_write_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, time_submit_write_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[time_submit_write_dto], bool]) -> time_submit_write_dtos:
        return time_submit_write_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[time_submit_write_dto], str]) -> dict[str, time_submit_write_dtos]:
        grp_data: dict[str, time_submit_write_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = time_submit_write_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[time_submit_write_dto], str], agg_method: Callable[[time_submit_write_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, time_submit_write_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[time_submit_write_dto], bool]) -> time_submit_write_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[time_submit_write_dto], any], compare_method: Callable[[any, any], bool]) -> time_submit_write_dto | None:
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
class time_submit_type_write_dtos(base_write_dtos):
    dtos: list[time_submit_type_write_dto]
    def __init__(self, dtos: list[time_submit_type_write_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[time_submit_type_write_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: time_submit_type_write_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[time_submit_type_write_dto], dtos2: list[time_submit_type_write_dto]):
        return cls(dtos1 + dtos2)
    def get_write_dicts(self) -> list[dict]:
        return list(map(lambda x: x.to_write_dict(), self.dtos))
    def find_by_uid(self, uid: str) -> time_submit_type_write_dto | None:
        found_dtos = list(filter(lambda x: x.time_submit_type_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, time_submit_type_write_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.time_submit_type_uid] = dto
        return res
    def get_active(self):
        return time_submit_type_write_dtos(list(filter(lambda x: x.is_active == 1, self.dtos)))
    def get_inactive(self):
        return time_submit_type_write_dtos(list(filter(lambda x: x.is_active != 1, self.dtos)))
    def get_first(self) -> time_submit_type_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[0]
        else:
            return None
    def get_first_n(self, n: int) -> time_submit_type_write_dtos:
        if len(self.dtos) > n:
            return time_submit_type_write_dtos(self.dtos[:n])
        else:
            return time_submit_type_write_dtos(self.dtos)
    def get_last(self) -> time_submit_type_write_dto | None:
        if len(self.dtos) > 0:
            return self.dtos[-1]
        else:
            return None
    def to_dict_by_uid(self) -> dict[str, time_submit_type_write_dto]:
        d = {}
        for dto in self.dtos:
            d[dto.get_uid()] = dto
        return d
    def for_each(self, do_method: Callable):
        for dto in self.dtos:
            do_method(dto)
    def for_first(self, do_method: Callable):
        if len(self.dtos) > 0:
            return do_method(self.dtos[0])
    def for_filter(self, check_method: Callable[[time_submit_type_write_dto], bool], do_method: Callable):
        for dto in self.dtos:
            if check_method(dto):
                do_method(dto)
    def check_all(self, check_method: Callable[[time_submit_type_write_dto], bool]) -> bool:
        init = True
        for dto in self.dtos:
            init = init and check_method(dto)
        return False
    def check_any(self, check_method: Callable[[time_submit_type_write_dto], bool]) -> bool:
        init = False
        for dto in self.dtos:
            init = init or check_method(dto)
        return False
    def map_to_string(self, map_method: Callable[[time_submit_type_write_dto], str]) -> list[str]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_int(self, map_method: Callable[[time_submit_type_write_dto], int]) -> list[int]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def map_to_float(self, map_method: Callable[[time_submit_type_write_dto], float]) -> list[float]:
        return list(map(lambda dto:  map_method(dto), self.dtos))
    def aggregate_string(self, map_method: Callable[[str, time_submit_type_write_dto], str], init: str = "") -> str:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_int(self, map_method: Callable[[int, time_submit_type_write_dto], int], init: int = 0) -> int:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def aggregate_float(self, map_method: Callable[[float, time_submit_type_write_dto], float], init: float = 0) -> float:
        init_value = init
        for dto in self.dtos:
            init_value = map_method(init_value, dto)
        return init_value
    def filter(self, filter_method: Callable[[time_submit_type_write_dto], bool]) -> time_submit_type_write_dtos:
        return time_submit_type_write_dtos(list(filter(filter_method, self.dtos)))
    def group_by(self, group_method: Callable[[time_submit_type_write_dto], str]) -> dict[str, time_submit_type_write_dtos]:
        grp_data: dict[str, time_submit_type_write_dtos] = {}
        for dto in self.dtos:
            key = group_method(dto)
            grp_list = grp_data[key]
            if grp_list is None:
                grp_list = time_submit_type_write_dtos([])
                grp_data[key] = grp_list
            grp_list.dtos.append(dto)
        return grp_data
    def aggregate_by(self, group_method: Callable[[time_submit_type_write_dto], str], agg_method: Callable[[time_submit_type_write_dtos], any]) -> dict[str, any]:
        grp_data: dict[str, time_submit_type_write_dtos] = self.group_by(group_method)
        res: dict[str, any] = {}
        for key in grp_data:
            value = agg_method(grp_data[key])
            res[key] = value
        return res
    def find(self, check_method: Callable[[time_submit_type_write_dto], bool]) -> time_submit_type_write_dto | None:
        for dto in self.dtos:
            if check_method(dto):
                return dto
        return None
    def compare_by(self, value_method: Callable[[time_submit_type_write_dto], any], compare_method: Callable[[any, any], bool]) -> time_submit_type_write_dto | None:
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


# auto-generated - v_definition_python_dtos_write_list - END
