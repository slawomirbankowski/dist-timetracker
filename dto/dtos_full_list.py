# auto-generated - v_definition_python_dtos_full_list - START at 2024-03-29 22:26:17.028703+01
from __future__ import annotations
from datetime import datetime
from abc import abstractmethod
from dataclasses import dataclass
from dto.dtos import *
from dto.dtos_thin import *
from dto.dtos_write import *
from dto.dtos_read import *
from dto.dtos_full import *
import datetime
from typing import Dict, Callable


@dataclass(frozen=False)
class account_full_dtos(base_dtos):
    dtos: list[account_full_dto]
    def __init__(self, dtos: list[account_full_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[account_full_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: account_full_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[account_full_dto], dtos2: list[account_full_dto]):
        return cls(dtos1 + dtos2)
    def find_by_uid(self, uid: str) -> account_full_dto | None:
        found_dtos = list(filter(lambda x: x.account_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, account_full_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.account_uid] = dto
        return res


@dataclass(frozen=False)
class account_division_full_dtos(base_dtos):
    dtos: list[account_division_full_dto]
    def __init__(self, dtos: list[account_division_full_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[account_division_full_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: account_division_full_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[account_division_full_dto], dtos2: list[account_division_full_dto]):
        return cls(dtos1 + dtos2)
    def find_by_uid(self, uid: str) -> account_division_full_dto | None:
        found_dtos = list(filter(lambda x: x.account_division_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, account_division_full_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.account_division_uid] = dto
        return res


@dataclass(frozen=False)
class account_division_template_full_dtos(base_dtos):
    dtos: list[account_division_template_full_dto]
    def __init__(self, dtos: list[account_division_template_full_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[account_division_template_full_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: account_division_template_full_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[account_division_template_full_dto], dtos2: list[account_division_template_full_dto]):
        return cls(dtos1 + dtos2)
    def find_by_uid(self, uid: str) -> account_division_template_full_dto | None:
        found_dtos = list(filter(lambda x: x.account_division_template_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, account_division_template_full_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.account_division_template_uid] = dto
        return res


@dataclass(frozen=False)
class account_group_full_dtos(base_dtos):
    dtos: list[account_group_full_dto]
    def __init__(self, dtos: list[account_group_full_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[account_group_full_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: account_group_full_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[account_group_full_dto], dtos2: list[account_group_full_dto]):
        return cls(dtos1 + dtos2)
    def find_by_uid(self, uid: str) -> account_group_full_dto | None:
        found_dtos = list(filter(lambda x: x.account_group_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, account_group_full_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.account_group_uid] = dto
        return res


@dataclass(frozen=False)
class account_hierarchy_full_dtos(base_dtos):
    dtos: list[account_hierarchy_full_dto]
    def __init__(self, dtos: list[account_hierarchy_full_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[account_hierarchy_full_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: account_hierarchy_full_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[account_hierarchy_full_dto], dtos2: list[account_hierarchy_full_dto]):
        return cls(dtos1 + dtos2)
    def find_by_uid(self, uid: str) -> account_hierarchy_full_dto | None:
        found_dtos = list(filter(lambda x: x.account_hierarchy_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, account_hierarchy_full_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.account_hierarchy_uid] = dto
        return res


@dataclass(frozen=False)
class account_rate_full_dtos(base_dtos):
    dtos: list[account_rate_full_dto]
    def __init__(self, dtos: list[account_rate_full_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[account_rate_full_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: account_rate_full_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[account_rate_full_dto], dtos2: list[account_rate_full_dto]):
        return cls(dtos1 + dtos2)
    def find_by_uid(self, uid: str) -> account_rate_full_dto | None:
        found_dtos = list(filter(lambda x: x.account_rate_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, account_rate_full_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.account_rate_uid] = dto
        return res


@dataclass(frozen=False)
class account_skill_full_dtos(base_dtos):
    dtos: list[account_skill_full_dto]
    def __init__(self, dtos: list[account_skill_full_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[account_skill_full_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: account_skill_full_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[account_skill_full_dto], dtos2: list[account_skill_full_dto]):
        return cls(dtos1 + dtos2)
    def find_by_uid(self, uid: str) -> account_skill_full_dto | None:
        found_dtos = list(filter(lambda x: x.account_skill_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, account_skill_full_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.account_skill_uid] = dto
        return res


@dataclass(frozen=False)
class account_team_full_dtos(base_dtos):
    dtos: list[account_team_full_dto]
    def __init__(self, dtos: list[account_team_full_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[account_team_full_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: account_team_full_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[account_team_full_dto], dtos2: list[account_team_full_dto]):
        return cls(dtos1 + dtos2)
    def find_by_uid(self, uid: str) -> account_team_full_dto | None:
        found_dtos = list(filter(lambda x: x.account_team_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, account_team_full_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.account_team_uid] = dto
        return res


@dataclass(frozen=False)
class account_title_full_dtos(base_dtos):
    dtos: list[account_title_full_dto]
    def __init__(self, dtos: list[account_title_full_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[account_title_full_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: account_title_full_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[account_title_full_dto], dtos2: list[account_title_full_dto]):
        return cls(dtos1 + dtos2)
    def find_by_uid(self, uid: str) -> account_title_full_dto | None:
        found_dtos = list(filter(lambda x: x.account_title_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, account_title_full_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.account_title_uid] = dto
        return res


@dataclass(frozen=False)
class account_title_responsibility_full_dtos(base_dtos):
    dtos: list[account_title_responsibility_full_dto]
    def __init__(self, dtos: list[account_title_responsibility_full_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[account_title_responsibility_full_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: account_title_responsibility_full_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[account_title_responsibility_full_dto], dtos2: list[account_title_responsibility_full_dto]):
        return cls(dtos1 + dtos2)
    def find_by_uid(self, uid: str) -> account_title_responsibility_full_dto | None:
        found_dtos = list(filter(lambda x: x.account_title_responsibility_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, account_title_responsibility_full_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.account_title_responsibility_uid] = dto
        return res


@dataclass(frozen=False)
class account_type_full_dtos(base_dtos):
    dtos: list[account_type_full_dto]
    def __init__(self, dtos: list[account_type_full_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[account_type_full_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: account_type_full_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[account_type_full_dto], dtos2: list[account_type_full_dto]):
        return cls(dtos1 + dtos2)
    def find_by_uid(self, uid: str) -> account_type_full_dto | None:
        found_dtos = list(filter(lambda x: x.account_type_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, account_type_full_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.account_type_uid] = dto
        return res


@dataclass(frozen=False)
class audit_change_full_dtos(base_dtos):
    dtos: list[audit_change_full_dto]
    def __init__(self, dtos: list[audit_change_full_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[audit_change_full_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: audit_change_full_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[audit_change_full_dto], dtos2: list[audit_change_full_dto]):
        return cls(dtos1 + dtos2)
    def find_by_uid(self, uid: str) -> audit_change_full_dto | None:
        found_dtos = list(filter(lambda x: x.audit_change_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, audit_change_full_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.audit_change_uid] = dto
        return res


@dataclass(frozen=False)
class audit_type_full_dtos(base_dtos):
    dtos: list[audit_type_full_dto]
    def __init__(self, dtos: list[audit_type_full_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[audit_type_full_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: audit_type_full_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[audit_type_full_dto], dtos2: list[audit_type_full_dto]):
        return cls(dtos1 + dtos2)
    def find_by_uid(self, uid: str) -> audit_type_full_dto | None:
        found_dtos = list(filter(lambda x: x.audit_type_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, audit_type_full_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.audit_type_uid] = dto
        return res


@dataclass(frozen=False)
class auth_attempt_full_dtos(base_dtos):
    dtos: list[auth_attempt_full_dto]
    def __init__(self, dtos: list[auth_attempt_full_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[auth_attempt_full_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: auth_attempt_full_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[auth_attempt_full_dto], dtos2: list[auth_attempt_full_dto]):
        return cls(dtos1 + dtos2)
    def find_by_uid(self, uid: str) -> auth_attempt_full_dto | None:
        found_dtos = list(filter(lambda x: x.auth_attempt_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, auth_attempt_full_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.auth_attempt_uid] = dto
        return res


@dataclass(frozen=False)
class auth_identity_full_dtos(base_dtos):
    dtos: list[auth_identity_full_dto]
    def __init__(self, dtos: list[auth_identity_full_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[auth_identity_full_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: auth_identity_full_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[auth_identity_full_dto], dtos2: list[auth_identity_full_dto]):
        return cls(dtos1 + dtos2)
    def find_by_uid(self, uid: str) -> auth_identity_full_dto | None:
        found_dtos = list(filter(lambda x: x.auth_identity_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, auth_identity_full_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.auth_identity_uid] = dto
        return res


@dataclass(frozen=False)
class auth_identity_tenant_full_dtos(base_dtos):
    dtos: list[auth_identity_tenant_full_dto]
    def __init__(self, dtos: list[auth_identity_tenant_full_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[auth_identity_tenant_full_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: auth_identity_tenant_full_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[auth_identity_tenant_full_dto], dtos2: list[auth_identity_tenant_full_dto]):
        return cls(dtos1 + dtos2)
    def find_by_uid(self, uid: str) -> auth_identity_tenant_full_dto | None:
        found_dtos = list(filter(lambda x: x.auth_identity_tenant_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, auth_identity_tenant_full_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.auth_identity_tenant_uid] = dto
        return res


@dataclass(frozen=False)
class auth_key_full_dtos(base_dtos):
    dtos: list[auth_key_full_dto]
    def __init__(self, dtos: list[auth_key_full_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[auth_key_full_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: auth_key_full_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[auth_key_full_dto], dtos2: list[auth_key_full_dto]):
        return cls(dtos1 + dtos2)
    def find_by_uid(self, uid: str) -> auth_key_full_dto | None:
        found_dtos = list(filter(lambda x: x.auth_key_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, auth_key_full_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.auth_key_uid] = dto
        return res


@dataclass(frozen=False)
class auth_key_type_full_dtos(base_dtos):
    dtos: list[auth_key_type_full_dto]
    def __init__(self, dtos: list[auth_key_type_full_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[auth_key_type_full_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: auth_key_type_full_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[auth_key_type_full_dto], dtos2: list[auth_key_type_full_dto]):
        return cls(dtos1 + dtos2)
    def find_by_uid(self, uid: str) -> auth_key_type_full_dto | None:
        found_dtos = list(filter(lambda x: x.auth_key_type_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, auth_key_type_full_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.auth_key_type_uid] = dto
        return res


@dataclass(frozen=False)
class auth_password_full_dtos(base_dtos):
    dtos: list[auth_password_full_dto]
    def __init__(self, dtos: list[auth_password_full_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[auth_password_full_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: auth_password_full_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[auth_password_full_dto], dtos2: list[auth_password_full_dto]):
        return cls(dtos1 + dtos2)
    def find_by_uid(self, uid: str) -> auth_password_full_dto | None:
        found_dtos = list(filter(lambda x: x.auth_password_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, auth_password_full_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.auth_password_uid] = dto
        return res


@dataclass(frozen=False)
class auth_password_current_full_dtos(base_dtos):
    dtos: list[auth_password_current_full_dto]
    def __init__(self, dtos: list[auth_password_current_full_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[auth_password_current_full_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: auth_password_current_full_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[auth_password_current_full_dto], dtos2: list[auth_password_current_full_dto]):
        return cls(dtos1 + dtos2)
    def find_by_uid(self, uid: str) -> auth_password_current_full_dto | None:
        found_dtos = list(filter(lambda x: x.auth_password_current_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, auth_password_current_full_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.auth_password_current_uid] = dto
        return res


@dataclass(frozen=False)
class auth_password_rule_full_dtos(base_dtos):
    dtos: list[auth_password_rule_full_dto]
    def __init__(self, dtos: list[auth_password_rule_full_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[auth_password_rule_full_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: auth_password_rule_full_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[auth_password_rule_full_dto], dtos2: list[auth_password_rule_full_dto]):
        return cls(dtos1 + dtos2)
    def find_by_uid(self, uid: str) -> auth_password_rule_full_dto | None:
        found_dtos = list(filter(lambda x: x.auth_password_rule_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, auth_password_rule_full_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.auth_password_rule_uid] = dto
        return res


@dataclass(frozen=False)
class auth_permission_full_dtos(base_dtos):
    dtos: list[auth_permission_full_dto]
    def __init__(self, dtos: list[auth_permission_full_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[auth_permission_full_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: auth_permission_full_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[auth_permission_full_dto], dtos2: list[auth_permission_full_dto]):
        return cls(dtos1 + dtos2)
    def find_by_uid(self, uid: str) -> auth_permission_full_dto | None:
        found_dtos = list(filter(lambda x: x.auth_permission_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, auth_permission_full_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.auth_permission_uid] = dto
        return res


@dataclass(frozen=False)
class auth_request_full_dtos(base_dtos):
    dtos: list[auth_request_full_dto]
    def __init__(self, dtos: list[auth_request_full_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[auth_request_full_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: auth_request_full_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[auth_request_full_dto], dtos2: list[auth_request_full_dto]):
        return cls(dtos1 + dtos2)
    def find_by_uid(self, uid: str) -> auth_request_full_dto | None:
        found_dtos = list(filter(lambda x: x.auth_request_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, auth_request_full_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.auth_request_uid] = dto
        return res


@dataclass(frozen=False)
class auth_role_full_dtos(base_dtos):
    dtos: list[auth_role_full_dto]
    def __init__(self, dtos: list[auth_role_full_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[auth_role_full_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: auth_role_full_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[auth_role_full_dto], dtos2: list[auth_role_full_dto]):
        return cls(dtos1 + dtos2)
    def find_by_uid(self, uid: str) -> auth_role_full_dto | None:
        found_dtos = list(filter(lambda x: x.auth_role_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, auth_role_full_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.auth_role_uid] = dto
        return res


@dataclass(frozen=False)
class auth_role_uri_full_dtos(base_dtos):
    dtos: list[auth_role_uri_full_dto]
    def __init__(self, dtos: list[auth_role_uri_full_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[auth_role_uri_full_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: auth_role_uri_full_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[auth_role_uri_full_dto], dtos2: list[auth_role_uri_full_dto]):
        return cls(dtos1 + dtos2)
    def find_by_uid(self, uid: str) -> auth_role_uri_full_dto | None:
        found_dtos = list(filter(lambda x: x.auth_role_uri_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, auth_role_uri_full_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.auth_role_uri_uid] = dto
        return res


@dataclass(frozen=False)
class auth_session_full_dtos(base_dtos):
    dtos: list[auth_session_full_dto]
    def __init__(self, dtos: list[auth_session_full_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[auth_session_full_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: auth_session_full_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[auth_session_full_dto], dtos2: list[auth_session_full_dto]):
        return cls(dtos1 + dtos2)
    def find_by_uid(self, uid: str) -> auth_session_full_dto | None:
        found_dtos = list(filter(lambda x: x.auth_session_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, auth_session_full_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.auth_session_uid] = dto
        return res


@dataclass(frozen=False)
class auth_sso_full_dtos(base_dtos):
    dtos: list[auth_sso_full_dto]
    def __init__(self, dtos: list[auth_sso_full_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[auth_sso_full_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: auth_sso_full_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[auth_sso_full_dto], dtos2: list[auth_sso_full_dto]):
        return cls(dtos1 + dtos2)
    def find_by_uid(self, uid: str) -> auth_sso_full_dto | None:
        found_dtos = list(filter(lambda x: x.auth_sso_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, auth_sso_full_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.auth_sso_uid] = dto
        return res


@dataclass(frozen=False)
class auth_token_full_dtos(base_dtos):
    dtos: list[auth_token_full_dto]
    def __init__(self, dtos: list[auth_token_full_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[auth_token_full_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: auth_token_full_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[auth_token_full_dto], dtos2: list[auth_token_full_dto]):
        return cls(dtos1 + dtos2)
    def find_by_uid(self, uid: str) -> auth_token_full_dto | None:
        found_dtos = list(filter(lambda x: x.auth_token_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, auth_token_full_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.auth_token_uid] = dto
        return res


@dataclass(frozen=False)
class calendar_account_full_dtos(base_dtos):
    dtos: list[calendar_account_full_dto]
    def __init__(self, dtos: list[calendar_account_full_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[calendar_account_full_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: calendar_account_full_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[calendar_account_full_dto], dtos2: list[calendar_account_full_dto]):
        return cls(dtos1 + dtos2)
    def find_by_uid(self, uid: str) -> calendar_account_full_dto | None:
        found_dtos = list(filter(lambda x: x.calendar_account_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, calendar_account_full_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.calendar_account_uid] = dto
        return res


@dataclass(frozen=False)
class calendar_approval_full_dtos(base_dtos):
    dtos: list[calendar_approval_full_dto]
    def __init__(self, dtos: list[calendar_approval_full_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[calendar_approval_full_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: calendar_approval_full_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[calendar_approval_full_dto], dtos2: list[calendar_approval_full_dto]):
        return cls(dtos1 + dtos2)
    def find_by_uid(self, uid: str) -> calendar_approval_full_dto | None:
        found_dtos = list(filter(lambda x: x.calendar_approval_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, calendar_approval_full_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.calendar_approval_uid] = dto
        return res


@dataclass(frozen=False)
class calendar_approval_type_full_dtos(base_dtos):
    dtos: list[calendar_approval_type_full_dto]
    def __init__(self, dtos: list[calendar_approval_type_full_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[calendar_approval_type_full_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: calendar_approval_type_full_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[calendar_approval_type_full_dto], dtos2: list[calendar_approval_type_full_dto]):
        return cls(dtos1 + dtos2)
    def find_by_uid(self, uid: str) -> calendar_approval_type_full_dto | None:
        found_dtos = list(filter(lambda x: x.calendar_approval_type_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, calendar_approval_type_full_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.calendar_approval_type_uid] = dto
        return res


@dataclass(frozen=False)
class calendar_event_full_dtos(base_dtos):
    dtos: list[calendar_event_full_dto]
    def __init__(self, dtos: list[calendar_event_full_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[calendar_event_full_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: calendar_event_full_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[calendar_event_full_dto], dtos2: list[calendar_event_full_dto]):
        return cls(dtos1 + dtos2)
    def find_by_uid(self, uid: str) -> calendar_event_full_dto | None:
        found_dtos = list(filter(lambda x: x.calendar_event_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, calendar_event_full_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.calendar_event_uid] = dto
        return res


@dataclass(frozen=False)
class calendar_event_group_full_dtos(base_dtos):
    dtos: list[calendar_event_group_full_dto]
    def __init__(self, dtos: list[calendar_event_group_full_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[calendar_event_group_full_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: calendar_event_group_full_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[calendar_event_group_full_dto], dtos2: list[calendar_event_group_full_dto]):
        return cls(dtos1 + dtos2)
    def find_by_uid(self, uid: str) -> calendar_event_group_full_dto | None:
        found_dtos = list(filter(lambda x: x.calendar_event_group_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, calendar_event_group_full_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.calendar_event_group_uid] = dto
        return res


@dataclass(frozen=False)
class calendar_event_type_full_dtos(base_dtos):
    dtos: list[calendar_event_type_full_dto]
    def __init__(self, dtos: list[calendar_event_type_full_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[calendar_event_type_full_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: calendar_event_type_full_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[calendar_event_type_full_dto], dtos2: list[calendar_event_type_full_dto]):
        return cls(dtos1 + dtos2)
    def find_by_uid(self, uid: str) -> calendar_event_type_full_dto | None:
        found_dtos = list(filter(lambda x: x.calendar_event_type_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, calendar_event_type_full_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.calendar_event_type_uid] = dto
        return res


@dataclass(frozen=False)
class calendar_type_full_dtos(base_dtos):
    dtos: list[calendar_type_full_dto]
    def __init__(self, dtos: list[calendar_type_full_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[calendar_type_full_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: calendar_type_full_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[calendar_type_full_dto], dtos2: list[calendar_type_full_dto]):
        return cls(dtos1 + dtos2)
    def find_by_uid(self, uid: str) -> calendar_type_full_dto | None:
        found_dtos = list(filter(lambda x: x.calendar_type_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, calendar_type_full_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.calendar_type_uid] = dto
        return res


@dataclass(frozen=False)
class client_full_dtos(base_dtos):
    dtos: list[client_full_dto]
    def __init__(self, dtos: list[client_full_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[client_full_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: client_full_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[client_full_dto], dtos2: list[client_full_dto]):
        return cls(dtos1 + dtos2)
    def find_by_uid(self, uid: str) -> client_full_dto | None:
        found_dtos = list(filter(lambda x: x.client_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, client_full_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.client_uid] = dto
        return res


@dataclass(frozen=False)
class client_account_full_dtos(base_dtos):
    dtos: list[client_account_full_dto]
    def __init__(self, dtos: list[client_account_full_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[client_account_full_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: client_account_full_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[client_account_full_dto], dtos2: list[client_account_full_dto]):
        return cls(dtos1 + dtos2)
    def find_by_uid(self, uid: str) -> client_account_full_dto | None:
        found_dtos = list(filter(lambda x: x.client_account_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, client_account_full_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.client_account_uid] = dto
        return res


@dataclass(frozen=False)
class client_country_full_dtos(base_dtos):
    dtos: list[client_country_full_dto]
    def __init__(self, dtos: list[client_country_full_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[client_country_full_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: client_country_full_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[client_country_full_dto], dtos2: list[client_country_full_dto]):
        return cls(dtos1 + dtos2)
    def find_by_uid(self, uid: str) -> client_country_full_dto | None:
        found_dtos = list(filter(lambda x: x.client_country_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, client_country_full_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.client_country_uid] = dto
        return res


@dataclass(frozen=False)
class client_payment_full_dtos(base_dtos):
    dtos: list[client_payment_full_dto]
    def __init__(self, dtos: list[client_payment_full_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[client_payment_full_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: client_payment_full_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[client_payment_full_dto], dtos2: list[client_payment_full_dto]):
        return cls(dtos1 + dtos2)
    def find_by_uid(self, uid: str) -> client_payment_full_dto | None:
        found_dtos = list(filter(lambda x: x.client_payment_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, client_payment_full_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.client_payment_uid] = dto
        return res


@dataclass(frozen=False)
class client_role_full_dtos(base_dtos):
    dtos: list[client_role_full_dto]
    def __init__(self, dtos: list[client_role_full_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[client_role_full_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: client_role_full_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[client_role_full_dto], dtos2: list[client_role_full_dto]):
        return cls(dtos1 + dtos2)
    def find_by_uid(self, uid: str) -> client_role_full_dto | None:
        found_dtos = list(filter(lambda x: x.client_role_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, client_role_full_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.client_role_uid] = dto
        return res


@dataclass(frozen=False)
class client_status_full_dtos(base_dtos):
    dtos: list[client_status_full_dto]
    def __init__(self, dtos: list[client_status_full_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[client_status_full_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: client_status_full_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[client_status_full_dto], dtos2: list[client_status_full_dto]):
        return cls(dtos1 + dtos2)
    def find_by_uid(self, uid: str) -> client_status_full_dto | None:
        found_dtos = list(filter(lambda x: x.client_status_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, client_status_full_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.client_status_uid] = dto
        return res


@dataclass(frozen=False)
class client_type_full_dtos(base_dtos):
    dtos: list[client_type_full_dto]
    def __init__(self, dtos: list[client_type_full_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[client_type_full_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: client_type_full_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[client_type_full_dto], dtos2: list[client_type_full_dto]):
        return cls(dtos1 + dtos2)
    def find_by_uid(self, uid: str) -> client_type_full_dto | None:
        found_dtos = list(filter(lambda x: x.client_type_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, client_type_full_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.client_type_uid] = dto
        return res


@dataclass(frozen=False)
class connection_engine_full_dtos(base_dtos):
    dtos: list[connection_engine_full_dto]
    def __init__(self, dtos: list[connection_engine_full_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[connection_engine_full_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: connection_engine_full_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[connection_engine_full_dto], dtos2: list[connection_engine_full_dto]):
        return cls(dtos1 + dtos2)
    def find_by_uid(self, uid: str) -> connection_engine_full_dto | None:
        found_dtos = list(filter(lambda x: x.connection_engine_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, connection_engine_full_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.connection_engine_uid] = dto
        return res


@dataclass(frozen=False)
class connection_host_full_dtos(base_dtos):
    dtos: list[connection_host_full_dto]
    def __init__(self, dtos: list[connection_host_full_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[connection_host_full_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: connection_host_full_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[connection_host_full_dto], dtos2: list[connection_host_full_dto]):
        return cls(dtos1 + dtos2)
    def find_by_uid(self, uid: str) -> connection_host_full_dto | None:
        found_dtos = list(filter(lambda x: x.connection_host_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, connection_host_full_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.connection_host_uid] = dto
        return res


@dataclass(frozen=False)
class connection_user_full_dtos(base_dtos):
    dtos: list[connection_user_full_dto]
    def __init__(self, dtos: list[connection_user_full_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[connection_user_full_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: connection_user_full_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[connection_user_full_dto], dtos2: list[connection_user_full_dto]):
        return cls(dtos1 + dtos2)
    def find_by_uid(self, uid: str) -> connection_user_full_dto | None:
        found_dtos = list(filter(lambda x: x.connection_user_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, connection_user_full_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.connection_user_uid] = dto
        return res


@dataclass(frozen=False)
class country_full_dtos(base_dtos):
    dtos: list[country_full_dto]
    def __init__(self, dtos: list[country_full_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[country_full_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: country_full_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[country_full_dto], dtos2: list[country_full_dto]):
        return cls(dtos1 + dtos2)
    def find_by_uid(self, uid: str) -> country_full_dto | None:
        found_dtos = list(filter(lambda x: x.country_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, country_full_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.country_uid] = dto
        return res


@dataclass(frozen=False)
class currency_full_dtos(base_dtos):
    dtos: list[currency_full_dto]
    def __init__(self, dtos: list[currency_full_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[currency_full_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: currency_full_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[currency_full_dto], dtos2: list[currency_full_dto]):
        return cls(dtos1 + dtos2)
    def find_by_uid(self, uid: str) -> currency_full_dto | None:
        found_dtos = list(filter(lambda x: x.currency_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, currency_full_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.currency_uid] = dto
        return res


@dataclass(frozen=False)
class event_acknowledge_full_dtos(base_dtos):
    dtos: list[event_acknowledge_full_dto]
    def __init__(self, dtos: list[event_acknowledge_full_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[event_acknowledge_full_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: event_acknowledge_full_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[event_acknowledge_full_dto], dtos2: list[event_acknowledge_full_dto]):
        return cls(dtos1 + dtos2)
    def find_by_uid(self, uid: str) -> event_acknowledge_full_dto | None:
        found_dtos = list(filter(lambda x: x.event_acknowledge_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, event_acknowledge_full_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.event_acknowledge_uid] = dto
        return res


@dataclass(frozen=False)
class event_channel_full_dtos(base_dtos):
    dtos: list[event_channel_full_dto]
    def __init__(self, dtos: list[event_channel_full_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[event_channel_full_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: event_channel_full_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[event_channel_full_dto], dtos2: list[event_channel_full_dto]):
        return cls(dtos1 + dtos2)
    def find_by_uid(self, uid: str) -> event_channel_full_dto | None:
        found_dtos = list(filter(lambda x: x.event_channel_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, event_channel_full_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.event_channel_uid] = dto
        return res


@dataclass(frozen=False)
class event_channel_type_full_dtos(base_dtos):
    dtos: list[event_channel_type_full_dto]
    def __init__(self, dtos: list[event_channel_type_full_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[event_channel_type_full_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: event_channel_type_full_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[event_channel_type_full_dto], dtos2: list[event_channel_type_full_dto]):
        return cls(dtos1 + dtos2)
    def find_by_uid(self, uid: str) -> event_channel_type_full_dto | None:
        found_dtos = list(filter(lambda x: x.event_channel_type_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, event_channel_type_full_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.event_channel_type_uid] = dto
        return res


@dataclass(frozen=False)
class event_instance_full_dtos(base_dtos):
    dtos: list[event_instance_full_dto]
    def __init__(self, dtos: list[event_instance_full_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[event_instance_full_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: event_instance_full_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[event_instance_full_dto], dtos2: list[event_instance_full_dto]):
        return cls(dtos1 + dtos2)
    def find_by_uid(self, uid: str) -> event_instance_full_dto | None:
        found_dtos = list(filter(lambda x: x.event_instance_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, event_instance_full_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.event_instance_uid] = dto
        return res


@dataclass(frozen=False)
class event_notification_full_dtos(base_dtos):
    dtos: list[event_notification_full_dto]
    def __init__(self, dtos: list[event_notification_full_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[event_notification_full_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: event_notification_full_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[event_notification_full_dto], dtos2: list[event_notification_full_dto]):
        return cls(dtos1 + dtos2)
    def find_by_uid(self, uid: str) -> event_notification_full_dto | None:
        found_dtos = list(filter(lambda x: x.event_notification_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, event_notification_full_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.event_notification_uid] = dto
        return res


@dataclass(frozen=False)
class event_observer_full_dtos(base_dtos):
    dtos: list[event_observer_full_dto]
    def __init__(self, dtos: list[event_observer_full_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[event_observer_full_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: event_observer_full_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[event_observer_full_dto], dtos2: list[event_observer_full_dto]):
        return cls(dtos1 + dtos2)
    def find_by_uid(self, uid: str) -> event_observer_full_dto | None:
        found_dtos = list(filter(lambda x: x.event_observer_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, event_observer_full_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.event_observer_uid] = dto
        return res


@dataclass(frozen=False)
class event_subscription_full_dtos(base_dtos):
    dtos: list[event_subscription_full_dto]
    def __init__(self, dtos: list[event_subscription_full_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[event_subscription_full_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: event_subscription_full_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[event_subscription_full_dto], dtos2: list[event_subscription_full_dto]):
        return cls(dtos1 + dtos2)
    def find_by_uid(self, uid: str) -> event_subscription_full_dto | None:
        found_dtos = list(filter(lambda x: x.event_subscription_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, event_subscription_full_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.event_subscription_uid] = dto
        return res


@dataclass(frozen=False)
class event_template_full_dtos(base_dtos):
    dtos: list[event_template_full_dto]
    def __init__(self, dtos: list[event_template_full_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[event_template_full_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: event_template_full_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[event_template_full_dto], dtos2: list[event_template_full_dto]):
        return cls(dtos1 + dtos2)
    def find_by_uid(self, uid: str) -> event_template_full_dto | None:
        found_dtos = list(filter(lambda x: x.event_template_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, event_template_full_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.event_template_uid] = dto
        return res


@dataclass(frozen=False)
class event_type_full_dtos(base_dtos):
    dtos: list[event_type_full_dto]
    def __init__(self, dtos: list[event_type_full_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[event_type_full_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: event_type_full_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[event_type_full_dto], dtos2: list[event_type_full_dto]):
        return cls(dtos1 + dtos2)
    def find_by_uid(self, uid: str) -> event_type_full_dto | None:
        found_dtos = list(filter(lambda x: x.event_type_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, event_type_full_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.event_type_uid] = dto
        return res


@dataclass(frozen=False)
class invoice_action_full_dtos(base_dtos):
    dtos: list[invoice_action_full_dto]
    def __init__(self, dtos: list[invoice_action_full_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[invoice_action_full_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: invoice_action_full_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[invoice_action_full_dto], dtos2: list[invoice_action_full_dto]):
        return cls(dtos1 + dtos2)
    def find_by_uid(self, uid: str) -> invoice_action_full_dto | None:
        found_dtos = list(filter(lambda x: x.invoice_action_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, invoice_action_full_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.invoice_action_uid] = dto
        return res


@dataclass(frozen=False)
class invoice_action_type_full_dtos(base_dtos):
    dtos: list[invoice_action_type_full_dto]
    def __init__(self, dtos: list[invoice_action_type_full_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[invoice_action_type_full_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: invoice_action_type_full_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[invoice_action_type_full_dto], dtos2: list[invoice_action_type_full_dto]):
        return cls(dtos1 + dtos2)
    def find_by_uid(self, uid: str) -> invoice_action_type_full_dto | None:
        found_dtos = list(filter(lambda x: x.invoice_action_type_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, invoice_action_type_full_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.invoice_action_type_uid] = dto
        return res


@dataclass(frozen=False)
class invoice_category_full_dtos(base_dtos):
    dtos: list[invoice_category_full_dto]
    def __init__(self, dtos: list[invoice_category_full_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[invoice_category_full_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: invoice_category_full_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[invoice_category_full_dto], dtos2: list[invoice_category_full_dto]):
        return cls(dtos1 + dtos2)
    def find_by_uid(self, uid: str) -> invoice_category_full_dto | None:
        found_dtos = list(filter(lambda x: x.invoice_category_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, invoice_category_full_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.invoice_category_uid] = dto
        return res


@dataclass(frozen=False)
class invoice_entry_full_dtos(base_dtos):
    dtos: list[invoice_entry_full_dto]
    def __init__(self, dtos: list[invoice_entry_full_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[invoice_entry_full_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: invoice_entry_full_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[invoice_entry_full_dto], dtos2: list[invoice_entry_full_dto]):
        return cls(dtos1 + dtos2)
    def find_by_uid(self, uid: str) -> invoice_entry_full_dto | None:
        found_dtos = list(filter(lambda x: x.invoice_entry_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, invoice_entry_full_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.invoice_entry_uid] = dto
        return res


@dataclass(frozen=False)
class invoice_flow_full_dtos(base_dtos):
    dtos: list[invoice_flow_full_dto]
    def __init__(self, dtos: list[invoice_flow_full_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[invoice_flow_full_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: invoice_flow_full_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[invoice_flow_full_dto], dtos2: list[invoice_flow_full_dto]):
        return cls(dtos1 + dtos2)
    def find_by_uid(self, uid: str) -> invoice_flow_full_dto | None:
        found_dtos = list(filter(lambda x: x.invoice_flow_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, invoice_flow_full_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.invoice_flow_uid] = dto
        return res


@dataclass(frozen=False)
class invoice_flow_state_full_dtos(base_dtos):
    dtos: list[invoice_flow_state_full_dto]
    def __init__(self, dtos: list[invoice_flow_state_full_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[invoice_flow_state_full_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: invoice_flow_state_full_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[invoice_flow_state_full_dto], dtos2: list[invoice_flow_state_full_dto]):
        return cls(dtos1 + dtos2)
    def find_by_uid(self, uid: str) -> invoice_flow_state_full_dto | None:
        found_dtos = list(filter(lambda x: x.invoice_flow_state_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, invoice_flow_state_full_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.invoice_flow_state_uid] = dto
        return res


@dataclass(frozen=False)
class invoice_instance_full_dtos(base_dtos):
    dtos: list[invoice_instance_full_dto]
    def __init__(self, dtos: list[invoice_instance_full_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[invoice_instance_full_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: invoice_instance_full_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[invoice_instance_full_dto], dtos2: list[invoice_instance_full_dto]):
        return cls(dtos1 + dtos2)
    def find_by_uid(self, uid: str) -> invoice_instance_full_dto | None:
        found_dtos = list(filter(lambda x: x.invoice_instance_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, invoice_instance_full_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.invoice_instance_uid] = dto
        return res


@dataclass(frozen=False)
class invoice_status_full_dtos(base_dtos):
    dtos: list[invoice_status_full_dto]
    def __init__(self, dtos: list[invoice_status_full_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[invoice_status_full_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: invoice_status_full_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[invoice_status_full_dto], dtos2: list[invoice_status_full_dto]):
        return cls(dtos1 + dtos2)
    def find_by_uid(self, uid: str) -> invoice_status_full_dto | None:
        found_dtos = list(filter(lambda x: x.invoice_status_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, invoice_status_full_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.invoice_status_uid] = dto
        return res


@dataclass(frozen=False)
class invoice_type_full_dtos(base_dtos):
    dtos: list[invoice_type_full_dto]
    def __init__(self, dtos: list[invoice_type_full_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[invoice_type_full_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: invoice_type_full_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[invoice_type_full_dto], dtos2: list[invoice_type_full_dto]):
        return cls(dtos1 + dtos2)
    def find_by_uid(self, uid: str) -> invoice_type_full_dto | None:
        found_dtos = list(filter(lambda x: x.invoice_type_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, invoice_type_full_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.invoice_type_uid] = dto
        return res


@dataclass(frozen=False)
class monitor_full_dtos(base_dtos):
    dtos: list[monitor_full_dto]
    def __init__(self, dtos: list[monitor_full_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[monitor_full_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: monitor_full_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[monitor_full_dto], dtos2: list[monitor_full_dto]):
        return cls(dtos1 + dtos2)
    def find_by_uid(self, uid: str) -> monitor_full_dto | None:
        found_dtos = list(filter(lambda x: x.monitor_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, monitor_full_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.monitor_uid] = dto
        return res


@dataclass(frozen=False)
class monitor_run_full_dtos(base_dtos):
    dtos: list[monitor_run_full_dto]
    def __init__(self, dtos: list[monitor_run_full_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[monitor_run_full_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: monitor_run_full_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[monitor_run_full_dto], dtos2: list[monitor_run_full_dto]):
        return cls(dtos1 + dtos2)
    def find_by_uid(self, uid: str) -> monitor_run_full_dto | None:
        found_dtos = list(filter(lambda x: x.monitor_run_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, monitor_run_full_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.monitor_run_uid] = dto
        return res


@dataclass(frozen=False)
class monitor_type_full_dtos(base_dtos):
    dtos: list[monitor_type_full_dto]
    def __init__(self, dtos: list[monitor_type_full_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[monitor_type_full_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: monitor_type_full_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[monitor_type_full_dto], dtos2: list[monitor_type_full_dto]):
        return cls(dtos1 + dtos2)
    def find_by_uid(self, uid: str) -> monitor_type_full_dto | None:
        found_dtos = list(filter(lambda x: x.monitor_type_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, monitor_type_full_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.monitor_type_uid] = dto
        return res


@dataclass(frozen=False)
class period_full_dtos(base_dtos):
    dtos: list[period_full_dto]
    def __init__(self, dtos: list[period_full_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[period_full_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: period_full_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[period_full_dto], dtos2: list[period_full_dto]):
        return cls(dtos1 + dtos2)
    def find_by_uid(self, uid: str) -> period_full_dto | None:
        found_dtos = list(filter(lambda x: x.period_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, period_full_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.period_uid] = dto
        return res


@dataclass(frozen=False)
class process_full_dtos(base_dtos):
    dtos: list[process_full_dto]
    def __init__(self, dtos: list[process_full_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[process_full_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: process_full_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[process_full_dto], dtos2: list[process_full_dto]):
        return cls(dtos1 + dtos2)
    def find_by_uid(self, uid: str) -> process_full_dto | None:
        found_dtos = list(filter(lambda x: x.process_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, process_full_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.process_uid] = dto
        return res


@dataclass(frozen=False)
class process_run_full_dtos(base_dtos):
    dtos: list[process_run_full_dto]
    def __init__(self, dtos: list[process_run_full_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[process_run_full_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: process_run_full_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[process_run_full_dto], dtos2: list[process_run_full_dto]):
        return cls(dtos1 + dtos2)
    def find_by_uid(self, uid: str) -> process_run_full_dto | None:
        found_dtos = list(filter(lambda x: x.process_run_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, process_run_full_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.process_run_uid] = dto
        return res


@dataclass(frozen=False)
class process_type_full_dtos(base_dtos):
    dtos: list[process_type_full_dto]
    def __init__(self, dtos: list[process_type_full_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[process_type_full_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: process_type_full_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[process_type_full_dto], dtos2: list[process_type_full_dto]):
        return cls(dtos1 + dtos2)
    def find_by_uid(self, uid: str) -> process_type_full_dto | None:
        found_dtos = list(filter(lambda x: x.process_type_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, process_type_full_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.process_type_uid] = dto
        return res


@dataclass(frozen=False)
class project_account_full_dtos(base_dtos):
    dtos: list[project_account_full_dto]
    def __init__(self, dtos: list[project_account_full_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[project_account_full_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: project_account_full_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[project_account_full_dto], dtos2: list[project_account_full_dto]):
        return cls(dtos1 + dtos2)
    def find_by_uid(self, uid: str) -> project_account_full_dto | None:
        found_dtos = list(filter(lambda x: x.project_account_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, project_account_full_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.project_account_uid] = dto
        return res


@dataclass(frozen=False)
class project_budget_full_dtos(base_dtos):
    dtos: list[project_budget_full_dto]
    def __init__(self, dtos: list[project_budget_full_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[project_budget_full_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: project_budget_full_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[project_budget_full_dto], dtos2: list[project_budget_full_dto]):
        return cls(dtos1 + dtos2)
    def find_by_uid(self, uid: str) -> project_budget_full_dto | None:
        found_dtos = list(filter(lambda x: x.project_budget_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, project_budget_full_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.project_budget_uid] = dto
        return res


@dataclass(frozen=False)
class project_group_full_dtos(base_dtos):
    dtos: list[project_group_full_dto]
    def __init__(self, dtos: list[project_group_full_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[project_group_full_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: project_group_full_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[project_group_full_dto], dtos2: list[project_group_full_dto]):
        return cls(dtos1 + dtos2)
    def find_by_uid(self, uid: str) -> project_group_full_dto | None:
        found_dtos = list(filter(lambda x: x.project_group_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, project_group_full_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.project_group_uid] = dto
        return res


@dataclass(frozen=False)
class project_instance_full_dtos(base_dtos):
    dtos: list[project_instance_full_dto]
    def __init__(self, dtos: list[project_instance_full_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[project_instance_full_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: project_instance_full_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[project_instance_full_dto], dtos2: list[project_instance_full_dto]):
        return cls(dtos1 + dtos2)
    def find_by_uid(self, uid: str) -> project_instance_full_dto | None:
        found_dtos = list(filter(lambda x: x.project_instance_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, project_instance_full_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.project_instance_uid] = dto
        return res


@dataclass(frozen=False)
class project_milestone_full_dtos(base_dtos):
    dtos: list[project_milestone_full_dto]
    def __init__(self, dtos: list[project_milestone_full_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[project_milestone_full_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: project_milestone_full_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[project_milestone_full_dto], dtos2: list[project_milestone_full_dto]):
        return cls(dtos1 + dtos2)
    def find_by_uid(self, uid: str) -> project_milestone_full_dto | None:
        found_dtos = list(filter(lambda x: x.project_milestone_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, project_milestone_full_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.project_milestone_uid] = dto
        return res


@dataclass(frozen=False)
class project_type_full_dtos(base_dtos):
    dtos: list[project_type_full_dto]
    def __init__(self, dtos: list[project_type_full_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[project_type_full_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: project_type_full_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[project_type_full_dto], dtos2: list[project_type_full_dto]):
        return cls(dtos1 + dtos2)
    def find_by_uid(self, uid: str) -> project_type_full_dto | None:
        found_dtos = list(filter(lambda x: x.project_type_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, project_type_full_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.project_type_uid] = dto
        return res


@dataclass(frozen=False)
class report_full_dtos(base_dtos):
    dtos: list[report_full_dto]
    def __init__(self, dtos: list[report_full_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[report_full_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: report_full_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[report_full_dto], dtos2: list[report_full_dto]):
        return cls(dtos1 + dtos2)
    def find_by_uid(self, uid: str) -> report_full_dto | None:
        found_dtos = list(filter(lambda x: x.report_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, report_full_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.report_uid] = dto
        return res


@dataclass(frozen=False)
class report_content_type_full_dtos(base_dtos):
    dtos: list[report_content_type_full_dto]
    def __init__(self, dtos: list[report_content_type_full_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[report_content_type_full_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: report_content_type_full_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[report_content_type_full_dto], dtos2: list[report_content_type_full_dto]):
        return cls(dtos1 + dtos2)
    def find_by_uid(self, uid: str) -> report_content_type_full_dto | None:
        found_dtos = list(filter(lambda x: x.report_content_type_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, report_content_type_full_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.report_content_type_uid] = dto
        return res


@dataclass(frozen=False)
class report_format_full_dtos(base_dtos):
    dtos: list[report_format_full_dto]
    def __init__(self, dtos: list[report_format_full_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[report_format_full_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: report_format_full_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[report_format_full_dto], dtos2: list[report_format_full_dto]):
        return cls(dtos1 + dtos2)
    def find_by_uid(self, uid: str) -> report_format_full_dto | None:
        found_dtos = list(filter(lambda x: x.report_format_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, report_format_full_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.report_format_uid] = dto
        return res


@dataclass(frozen=False)
class report_run_full_dtos(base_dtos):
    dtos: list[report_run_full_dto]
    def __init__(self, dtos: list[report_run_full_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[report_run_full_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: report_run_full_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[report_run_full_dto], dtos2: list[report_run_full_dto]):
        return cls(dtos1 + dtos2)
    def find_by_uid(self, uid: str) -> report_run_full_dto | None:
        found_dtos = list(filter(lambda x: x.report_run_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, report_run_full_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.report_run_uid] = dto
        return res


@dataclass(frozen=False)
class report_status_full_dtos(base_dtos):
    dtos: list[report_status_full_dto]
    def __init__(self, dtos: list[report_status_full_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[report_status_full_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: report_status_full_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[report_status_full_dto], dtos2: list[report_status_full_dto]):
        return cls(dtos1 + dtos2)
    def find_by_uid(self, uid: str) -> report_status_full_dto | None:
        found_dtos = list(filter(lambda x: x.report_status_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, report_status_full_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.report_status_uid] = dto
        return res


@dataclass(frozen=False)
class report_type_full_dtos(base_dtos):
    dtos: list[report_type_full_dto]
    def __init__(self, dtos: list[report_type_full_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[report_type_full_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: report_type_full_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[report_type_full_dto], dtos2: list[report_type_full_dto]):
        return cls(dtos1 + dtos2)
    def find_by_uid(self, uid: str) -> report_type_full_dto | None:
        found_dtos = list(filter(lambda x: x.report_type_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, report_type_full_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.report_type_uid] = dto
        return res


@dataclass(frozen=False)
class storage_full_dtos(base_dtos):
    dtos: list[storage_full_dto]
    def __init__(self, dtos: list[storage_full_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[storage_full_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: storage_full_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[storage_full_dto], dtos2: list[storage_full_dto]):
        return cls(dtos1 + dtos2)
    def find_by_uid(self, uid: str) -> storage_full_dto | None:
        found_dtos = list(filter(lambda x: x.storage_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, storage_full_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.storage_uid] = dto
        return res


@dataclass(frozen=False)
class storage_connection_full_dtos(base_dtos):
    dtos: list[storage_connection_full_dto]
    def __init__(self, dtos: list[storage_connection_full_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[storage_connection_full_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: storage_connection_full_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[storage_connection_full_dto], dtos2: list[storage_connection_full_dto]):
        return cls(dtos1 + dtos2)
    def find_by_uid(self, uid: str) -> storage_connection_full_dto | None:
        found_dtos = list(filter(lambda x: x.storage_connection_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, storage_connection_full_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.storage_connection_uid] = dto
        return res


@dataclass(frozen=False)
class storage_query_full_dtos(base_dtos):
    dtos: list[storage_query_full_dto]
    def __init__(self, dtos: list[storage_query_full_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[storage_query_full_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: storage_query_full_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[storage_query_full_dto], dtos2: list[storage_query_full_dto]):
        return cls(dtos1 + dtos2)
    def find_by_uid(self, uid: str) -> storage_query_full_dto | None:
        found_dtos = list(filter(lambda x: x.storage_query_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, storage_query_full_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.storage_query_uid] = dto
        return res


@dataclass(frozen=False)
class storage_type_full_dtos(base_dtos):
    dtos: list[storage_type_full_dto]
    def __init__(self, dtos: list[storage_type_full_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[storage_type_full_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: storage_type_full_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[storage_type_full_dto], dtos2: list[storage_type_full_dto]):
        return cls(dtos1 + dtos2)
    def find_by_uid(self, uid: str) -> storage_type_full_dto | None:
        found_dtos = list(filter(lambda x: x.storage_type_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, storage_type_full_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.storage_type_uid] = dto
        return res


@dataclass(frozen=False)
class synchronization_full_dtos(base_dtos):
    dtos: list[synchronization_full_dto]
    def __init__(self, dtos: list[synchronization_full_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[synchronization_full_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: synchronization_full_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[synchronization_full_dto], dtos2: list[synchronization_full_dto]):
        return cls(dtos1 + dtos2)
    def find_by_uid(self, uid: str) -> synchronization_full_dto | None:
        found_dtos = list(filter(lambda x: x.synchronization_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, synchronization_full_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.synchronization_uid] = dto
        return res


@dataclass(frozen=False)
class synchronization_run_full_dtos(base_dtos):
    dtos: list[synchronization_run_full_dto]
    def __init__(self, dtos: list[synchronization_run_full_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[synchronization_run_full_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: synchronization_run_full_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[synchronization_run_full_dto], dtos2: list[synchronization_run_full_dto]):
        return cls(dtos1 + dtos2)
    def find_by_uid(self, uid: str) -> synchronization_run_full_dto | None:
        found_dtos = list(filter(lambda x: x.synchronization_run_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, synchronization_run_full_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.synchronization_run_uid] = dto
        return res


@dataclass(frozen=False)
class synchronization_type_full_dtos(base_dtos):
    dtos: list[synchronization_type_full_dto]
    def __init__(self, dtos: list[synchronization_type_full_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[synchronization_type_full_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: synchronization_type_full_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[synchronization_type_full_dto], dtos2: list[synchronization_type_full_dto]):
        return cls(dtos1 + dtos2)
    def find_by_uid(self, uid: str) -> synchronization_type_full_dto | None:
        found_dtos = list(filter(lambda x: x.synchronization_type_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, synchronization_type_full_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.synchronization_type_uid] = dto
        return res


@dataclass(frozen=False)
class system_attribute_full_dtos(base_dtos):
    dtos: list[system_attribute_full_dto]
    def __init__(self, dtos: list[system_attribute_full_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[system_attribute_full_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: system_attribute_full_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[system_attribute_full_dto], dtos2: list[system_attribute_full_dto]):
        return cls(dtos1 + dtos2)
    def find_by_uid(self, uid: str) -> system_attribute_full_dto | None:
        found_dtos = list(filter(lambda x: x.system_attribute_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, system_attribute_full_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.system_attribute_uid] = dto
        return res


@dataclass(frozen=False)
class system_database_full_dtos(base_dtos):
    dtos: list[system_database_full_dto]
    def __init__(self, dtos: list[system_database_full_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[system_database_full_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: system_database_full_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[system_database_full_dto], dtos2: list[system_database_full_dto]):
        return cls(dtos1 + dtos2)
    def find_by_uid(self, uid: str) -> system_database_full_dto | None:
        found_dtos = list(filter(lambda x: x.system_database_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, system_database_full_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.system_database_uid] = dto
        return res


@dataclass(frozen=False)
class system_exception_full_dtos(base_dtos):
    dtos: list[system_exception_full_dto]
    def __init__(self, dtos: list[system_exception_full_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[system_exception_full_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: system_exception_full_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[system_exception_full_dto], dtos2: list[system_exception_full_dto]):
        return cls(dtos1 + dtos2)
    def find_by_uid(self, uid: str) -> system_exception_full_dto | None:
        found_dtos = list(filter(lambda x: x.system_exception_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, system_exception_full_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.system_exception_uid] = dto
        return res


@dataclass(frozen=False)
class system_instance_full_dtos(base_dtos):
    dtos: list[system_instance_full_dto]
    def __init__(self, dtos: list[system_instance_full_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[system_instance_full_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: system_instance_full_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[system_instance_full_dto], dtos2: list[system_instance_full_dto]):
        return cls(dtos1 + dtos2)
    def find_by_uid(self, uid: str) -> system_instance_full_dto | None:
        found_dtos = list(filter(lambda x: x.system_instance_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, system_instance_full_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.system_instance_uid] = dto
        return res


@dataclass(frozen=False)
class system_license_full_dtos(base_dtos):
    dtos: list[system_license_full_dto]
    def __init__(self, dtos: list[system_license_full_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[system_license_full_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: system_license_full_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[system_license_full_dto], dtos2: list[system_license_full_dto]):
        return cls(dtos1 + dtos2)
    def find_by_uid(self, uid: str) -> system_license_full_dto | None:
        found_dtos = list(filter(lambda x: x.system_license_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, system_license_full_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.system_license_uid] = dto
        return res


@dataclass(frozen=False)
class system_lock_full_dtos(base_dtos):
    dtos: list[system_lock_full_dto]
    def __init__(self, dtos: list[system_lock_full_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[system_lock_full_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: system_lock_full_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[system_lock_full_dto], dtos2: list[system_lock_full_dto]):
        return cls(dtos1 + dtos2)
    def find_by_uid(self, uid: str) -> system_lock_full_dto | None:
        found_dtos = list(filter(lambda x: x.system_lock_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, system_lock_full_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.system_lock_uid] = dto
        return res


@dataclass(frozen=False)
class system_module_full_dtos(base_dtos):
    dtos: list[system_module_full_dto]
    def __init__(self, dtos: list[system_module_full_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[system_module_full_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: system_module_full_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[system_module_full_dto], dtos2: list[system_module_full_dto]):
        return cls(dtos1 + dtos2)
    def find_by_uid(self, uid: str) -> system_module_full_dto | None:
        found_dtos = list(filter(lambda x: x.system_module_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, system_module_full_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.system_module_uid] = dto
        return res


@dataclass(frozen=False)
class system_object_full_dtos(base_dtos):
    dtos: list[system_object_full_dto]
    def __init__(self, dtos: list[system_object_full_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[system_object_full_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: system_object_full_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[system_object_full_dto], dtos2: list[system_object_full_dto]):
        return cls(dtos1 + dtos2)
    def find_by_uid(self, uid: str) -> system_object_full_dto | None:
        found_dtos = list(filter(lambda x: x.system_object_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, system_object_full_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.system_object_uid] = dto
        return res


@dataclass(frozen=False)
class system_object_type_full_dtos(base_dtos):
    dtos: list[system_object_type_full_dto]
    def __init__(self, dtos: list[system_object_type_full_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[system_object_type_full_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: system_object_type_full_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[system_object_type_full_dto], dtos2: list[system_object_type_full_dto]):
        return cls(dtos1 + dtos2)
    def find_by_uid(self, uid: str) -> system_object_type_full_dto | None:
        found_dtos = list(filter(lambda x: x.system_object_type_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, system_object_type_full_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.system_object_type_uid] = dto
        return res


@dataclass(frozen=False)
class system_query_full_dtos(base_dtos):
    dtos: list[system_query_full_dto]
    def __init__(self, dtos: list[system_query_full_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[system_query_full_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: system_query_full_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[system_query_full_dto], dtos2: list[system_query_full_dto]):
        return cls(dtos1 + dtos2)
    def find_by_uid(self, uid: str) -> system_query_full_dto | None:
        found_dtos = list(filter(lambda x: x.system_query_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, system_query_full_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.system_query_uid] = dto
        return res


@dataclass(frozen=False)
class system_request_full_dtos(base_dtos):
    dtos: list[system_request_full_dto]
    def __init__(self, dtos: list[system_request_full_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[system_request_full_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: system_request_full_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[system_request_full_dto], dtos2: list[system_request_full_dto]):
        return cls(dtos1 + dtos2)
    def find_by_uid(self, uid: str) -> system_request_full_dto | None:
        found_dtos = list(filter(lambda x: x.system_request_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, system_request_full_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.system_request_uid] = dto
        return res


@dataclass(frozen=False)
class system_setting_full_dtos(base_dtos):
    dtos: list[system_setting_full_dto]
    def __init__(self, dtos: list[system_setting_full_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[system_setting_full_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: system_setting_full_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[system_setting_full_dto], dtos2: list[system_setting_full_dto]):
        return cls(dtos1 + dtos2)
    def find_by_uid(self, uid: str) -> system_setting_full_dto | None:
        found_dtos = list(filter(lambda x: x.system_setting_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, system_setting_full_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.system_setting_uid] = dto
        return res


@dataclass(frozen=False)
class system_setting_account_full_dtos(base_dtos):
    dtos: list[system_setting_account_full_dto]
    def __init__(self, dtos: list[system_setting_account_full_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[system_setting_account_full_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: system_setting_account_full_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[system_setting_account_full_dto], dtos2: list[system_setting_account_full_dto]):
        return cls(dtos1 + dtos2)
    def find_by_uid(self, uid: str) -> system_setting_account_full_dto | None:
        found_dtos = list(filter(lambda x: x.system_setting_account_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, system_setting_account_full_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.system_setting_account_uid] = dto
        return res


@dataclass(frozen=False)
class system_state_full_dtos(base_dtos):
    dtos: list[system_state_full_dto]
    def __init__(self, dtos: list[system_state_full_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[system_state_full_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: system_state_full_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[system_state_full_dto], dtos2: list[system_state_full_dto]):
        return cls(dtos1 + dtos2)
    def find_by_uid(self, uid: str) -> system_state_full_dto | None:
        found_dtos = list(filter(lambda x: x.system_state_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, system_state_full_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.system_state_uid] = dto
        return res


@dataclass(frozen=False)
class system_table_full_dtos(base_dtos):
    dtos: list[system_table_full_dto]
    def __init__(self, dtos: list[system_table_full_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[system_table_full_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: system_table_full_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[system_table_full_dto], dtos2: list[system_table_full_dto]):
        return cls(dtos1 + dtos2)
    def find_by_uid(self, uid: str) -> system_table_full_dto | None:
        found_dtos = list(filter(lambda x: x.system_table_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, system_table_full_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.system_table_uid] = dto
        return res


@dataclass(frozen=False)
class system_thread_full_dtos(base_dtos):
    dtos: list[system_thread_full_dto]
    def __init__(self, dtos: list[system_thread_full_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[system_thread_full_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: system_thread_full_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[system_thread_full_dto], dtos2: list[system_thread_full_dto]):
        return cls(dtos1 + dtos2)
    def find_by_uid(self, uid: str) -> system_thread_full_dto | None:
        found_dtos = list(filter(lambda x: x.system_thread_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, system_thread_full_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.system_thread_uid] = dto
        return res


@dataclass(frozen=False)
class system_version_full_dtos(base_dtos):
    dtos: list[system_version_full_dto]
    def __init__(self, dtos: list[system_version_full_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[system_version_full_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: system_version_full_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[system_version_full_dto], dtos2: list[system_version_full_dto]):
        return cls(dtos1 + dtos2)
    def find_by_uid(self, uid: str) -> system_version_full_dto | None:
        found_dtos = list(filter(lambda x: x.system_version_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, system_version_full_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.system_version_uid] = dto
        return res


@dataclass(frozen=False)
class tenant_full_dtos(base_dtos):
    dtos: list[tenant_full_dto]
    def __init__(self, dtos: list[tenant_full_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[tenant_full_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: tenant_full_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[tenant_full_dto], dtos2: list[tenant_full_dto]):
        return cls(dtos1 + dtos2)
    def find_by_uid(self, uid: str) -> tenant_full_dto | None:
        found_dtos = list(filter(lambda x: x.tenant_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, tenant_full_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.tenant_uid] = dto
        return res


@dataclass(frozen=False)
class tenant_account_full_dtos(base_dtos):
    dtos: list[tenant_account_full_dto]
    def __init__(self, dtos: list[tenant_account_full_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[tenant_account_full_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: tenant_account_full_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[tenant_account_full_dto], dtos2: list[tenant_account_full_dto]):
        return cls(dtos1 + dtos2)
    def find_by_uid(self, uid: str) -> tenant_account_full_dto | None:
        found_dtos = list(filter(lambda x: x.tenant_account_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, tenant_account_full_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.tenant_account_uid] = dto
        return res


@dataclass(frozen=False)
class tenant_category_full_dtos(base_dtos):
    dtos: list[tenant_category_full_dto]
    def __init__(self, dtos: list[tenant_category_full_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[tenant_category_full_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: tenant_category_full_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[tenant_category_full_dto], dtos2: list[tenant_category_full_dto]):
        return cls(dtos1 + dtos2)
    def find_by_uid(self, uid: str) -> tenant_category_full_dto | None:
        found_dtos = list(filter(lambda x: x.tenant_category_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, tenant_category_full_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.tenant_category_uid] = dto
        return res


@dataclass(frozen=False)
class tenant_country_full_dtos(base_dtos):
    dtos: list[tenant_country_full_dto]
    def __init__(self, dtos: list[tenant_country_full_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[tenant_country_full_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: tenant_country_full_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[tenant_country_full_dto], dtos2: list[tenant_country_full_dto]):
        return cls(dtos1 + dtos2)
    def find_by_uid(self, uid: str) -> tenant_country_full_dto | None:
        found_dtos = list(filter(lambda x: x.tenant_country_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, tenant_country_full_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.tenant_country_uid] = dto
        return res


@dataclass(frozen=False)
class tenant_license_full_dtos(base_dtos):
    dtos: list[tenant_license_full_dto]
    def __init__(self, dtos: list[tenant_license_full_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[tenant_license_full_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: tenant_license_full_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[tenant_license_full_dto], dtos2: list[tenant_license_full_dto]):
        return cls(dtos1 + dtos2)
    def find_by_uid(self, uid: str) -> tenant_license_full_dto | None:
        found_dtos = list(filter(lambda x: x.tenant_license_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, tenant_license_full_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.tenant_license_uid] = dto
        return res


@dataclass(frozen=False)
class tenant_payment_full_dtos(base_dtos):
    dtos: list[tenant_payment_full_dto]
    def __init__(self, dtos: list[tenant_payment_full_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[tenant_payment_full_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: tenant_payment_full_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[tenant_payment_full_dto], dtos2: list[tenant_payment_full_dto]):
        return cls(dtos1 + dtos2)
    def find_by_uid(self, uid: str) -> tenant_payment_full_dto | None:
        found_dtos = list(filter(lambda x: x.tenant_payment_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, tenant_payment_full_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.tenant_payment_uid] = dto
        return res


@dataclass(frozen=False)
class tenant_payment_type_full_dtos(base_dtos):
    dtos: list[tenant_payment_type_full_dto]
    def __init__(self, dtos: list[tenant_payment_type_full_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[tenant_payment_type_full_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: tenant_payment_type_full_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[tenant_payment_type_full_dto], dtos2: list[tenant_payment_type_full_dto]):
        return cls(dtos1 + dtos2)
    def find_by_uid(self, uid: str) -> tenant_payment_type_full_dto | None:
        found_dtos = list(filter(lambda x: x.tenant_payment_type_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, tenant_payment_type_full_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.tenant_payment_type_uid] = dto
        return res


@dataclass(frozen=False)
class tenant_role_full_dtos(base_dtos):
    dtos: list[tenant_role_full_dto]
    def __init__(self, dtos: list[tenant_role_full_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[tenant_role_full_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: tenant_role_full_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[tenant_role_full_dto], dtos2: list[tenant_role_full_dto]):
        return cls(dtos1 + dtos2)
    def find_by_uid(self, uid: str) -> tenant_role_full_dto | None:
        found_dtos = list(filter(lambda x: x.tenant_role_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, tenant_role_full_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.tenant_role_uid] = dto
        return res


@dataclass(frozen=False)
class tenant_status_full_dtos(base_dtos):
    dtos: list[tenant_status_full_dto]
    def __init__(self, dtos: list[tenant_status_full_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[tenant_status_full_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: tenant_status_full_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[tenant_status_full_dto], dtos2: list[tenant_status_full_dto]):
        return cls(dtos1 + dtos2)
    def find_by_uid(self, uid: str) -> tenant_status_full_dto | None:
        found_dtos = list(filter(lambda x: x.tenant_status_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, tenant_status_full_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.tenant_status_uid] = dto
        return res


@dataclass(frozen=False)
class tenant_type_full_dtos(base_dtos):
    dtos: list[tenant_type_full_dto]
    def __init__(self, dtos: list[tenant_type_full_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[tenant_type_full_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: tenant_type_full_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[tenant_type_full_dto], dtos2: list[tenant_type_full_dto]):
        return cls(dtos1 + dtos2)
    def find_by_uid(self, uid: str) -> tenant_type_full_dto | None:
        found_dtos = list(filter(lambda x: x.tenant_type_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, tenant_type_full_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.tenant_type_uid] = dto
        return res


@dataclass(frozen=False)
class time_approval_full_dtos(base_dtos):
    dtos: list[time_approval_full_dto]
    def __init__(self, dtos: list[time_approval_full_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[time_approval_full_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: time_approval_full_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[time_approval_full_dto], dtos2: list[time_approval_full_dto]):
        return cls(dtos1 + dtos2)
    def find_by_uid(self, uid: str) -> time_approval_full_dto | None:
        found_dtos = list(filter(lambda x: x.time_approval_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, time_approval_full_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.time_approval_uid] = dto
        return res


@dataclass(frozen=False)
class time_entry_full_dtos(base_dtos):
    dtos: list[time_entry_full_dto]
    def __init__(self, dtos: list[time_entry_full_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[time_entry_full_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: time_entry_full_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[time_entry_full_dto], dtos2: list[time_entry_full_dto]):
        return cls(dtos1 + dtos2)
    def find_by_uid(self, uid: str) -> time_entry_full_dto | None:
        found_dtos = list(filter(lambda x: x.time_entry_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, time_entry_full_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.time_entry_uid] = dto
        return res


@dataclass(frozen=False)
class time_entry_final_full_dtos(base_dtos):
    dtos: list[time_entry_final_full_dto]
    def __init__(self, dtos: list[time_entry_final_full_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[time_entry_final_full_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: time_entry_final_full_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[time_entry_final_full_dto], dtos2: list[time_entry_final_full_dto]):
        return cls(dtos1 + dtos2)
    def find_by_uid(self, uid: str) -> time_entry_final_full_dto | None:
        found_dtos = list(filter(lambda x: x.time_entry_final_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, time_entry_final_full_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.time_entry_final_uid] = dto
        return res


@dataclass(frozen=False)
class time_entry_invoice_full_dtos(base_dtos):
    dtos: list[time_entry_invoice_full_dto]
    def __init__(self, dtos: list[time_entry_invoice_full_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[time_entry_invoice_full_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: time_entry_invoice_full_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[time_entry_invoice_full_dto], dtos2: list[time_entry_invoice_full_dto]):
        return cls(dtos1 + dtos2)
    def find_by_uid(self, uid: str) -> time_entry_invoice_full_dto | None:
        found_dtos = list(filter(lambda x: x.time_entry_invoice_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, time_entry_invoice_full_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.time_entry_invoice_uid] = dto
        return res


@dataclass(frozen=False)
class time_rule_full_dtos(base_dtos):
    dtos: list[time_rule_full_dto]
    def __init__(self, dtos: list[time_rule_full_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[time_rule_full_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: time_rule_full_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[time_rule_full_dto], dtos2: list[time_rule_full_dto]):
        return cls(dtos1 + dtos2)
    def find_by_uid(self, uid: str) -> time_rule_full_dto | None:
        found_dtos = list(filter(lambda x: x.time_rule_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, time_rule_full_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.time_rule_uid] = dto
        return res


@dataclass(frozen=False)
class time_rule_client_full_dtos(base_dtos):
    dtos: list[time_rule_client_full_dto]
    def __init__(self, dtos: list[time_rule_client_full_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[time_rule_client_full_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: time_rule_client_full_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[time_rule_client_full_dto], dtos2: list[time_rule_client_full_dto]):
        return cls(dtos1 + dtos2)
    def find_by_uid(self, uid: str) -> time_rule_client_full_dto | None:
        found_dtos = list(filter(lambda x: x.time_rule_client_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, time_rule_client_full_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.time_rule_client_uid] = dto
        return res


@dataclass(frozen=False)
class time_submit_full_dtos(base_dtos):
    dtos: list[time_submit_full_dto]
    def __init__(self, dtos: list[time_submit_full_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[time_submit_full_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: time_submit_full_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[time_submit_full_dto], dtos2: list[time_submit_full_dto]):
        return cls(dtos1 + dtos2)
    def find_by_uid(self, uid: str) -> time_submit_full_dto | None:
        found_dtos = list(filter(lambda x: x.time_submit_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, time_submit_full_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.time_submit_uid] = dto
        return res


@dataclass(frozen=False)
class time_submit_type_full_dtos(base_dtos):
    dtos: list[time_submit_type_full_dto]
    def __init__(self, dtos: list[time_submit_type_full_dto]):
        super().__init__(dtos)
        self.dtos = dtos
    @classmethod
    def empty_list(cls):
        return cls(list())
    @classmethod
    def from_list(cls, dtos: list[time_submit_type_full_dto]):
        return cls(dtos)
    @classmethod
    def from_object(cls, dto: time_submit_type_full_dto):
        return cls([dto])
    @classmethod
    def from_lists(cls, dtos1: list[time_submit_type_full_dto], dtos2: list[time_submit_type_full_dto]):
        return cls(dtos1 + dtos2)
    def find_by_uid(self, uid: str) -> time_submit_type_full_dto | None:
        found_dtos = list(filter(lambda x: x.time_submit_type_uid == uid, self.dtos))
        if (len(found_dtos)>0):
            return found_dtos[0]
        else:
            return None
    def map_by_uid(self) -> dict[str, time_submit_type_full_dto]:
        res = {}
        for dto in self.dtos:
            res[dto.time_submit_type_uid] = dto
        return res


# auto-generated - v_definition_python_dtos_full_list - END