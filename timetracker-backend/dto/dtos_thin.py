# auto-generated - v_definition_python_dtos_thin - START at 2024-08-04 09:35:55.647508+00
import datetime
from abc import abstractmethod
from dataclasses import dataclass, asdict
import json
from base.base_objects import objects
from dto.dtos import *
from dto.dtos_models import *
from dto.dtos_write import *


@dataclass(frozen=False)
class account_thin_dto(base_dto):
    account_uid: str
    account_name: str
    created_date: datetime.datetime
    is_active: int
    def __init__(self, account_uid: str,account_name: str, created_date: datetime.datetime, is_active: int):
        self.account_uid = account_uid
        self.account_name = account_name
        self.created_date = created_date
        self.is_active = is_active


@dataclass(frozen=False)
class account_division_thin_dto(base_dto):
    account_division_uid: str
    account_division_name: str
    created_date: datetime.datetime
    is_active: int
    def __init__(self, account_division_uid: str,account_division_name: str, created_date: datetime.datetime, is_active: int):
        self.account_division_uid = account_division_uid
        self.account_division_name = account_division_name
        self.created_date = created_date
        self.is_active = is_active


@dataclass(frozen=False)
class account_division_template_thin_dto(base_dto):
    account_division_template_uid: str
    account_division_template_name: str
    created_date: datetime.datetime
    is_active: int
    def __init__(self, account_division_template_uid: str,account_division_template_name: str, created_date: datetime.datetime, is_active: int):
        self.account_division_template_uid = account_division_template_uid
        self.account_division_template_name = account_division_template_name
        self.created_date = created_date
        self.is_active = is_active


@dataclass(frozen=False)
class account_group_thin_dto(base_dto):
    account_group_uid: str
    account_group_name: str
    created_date: datetime.datetime
    is_active: int
    def __init__(self, account_group_uid: str,account_group_name: str, created_date: datetime.datetime, is_active: int):
        self.account_group_uid = account_group_uid
        self.account_group_name = account_group_name
        self.created_date = created_date
        self.is_active = is_active


@dataclass(frozen=False)
class account_group_assignment_thin_dto(base_dto):
    account_group_assignment_uid: str
    account_group_assignment_name: str
    created_date: datetime.datetime
    is_active: int
    def __init__(self, account_group_assignment_uid: str,account_group_assignment_name: str, created_date: datetime.datetime, is_active: int):
        self.account_group_assignment_uid = account_group_assignment_uid
        self.account_group_assignment_name = account_group_assignment_name
        self.created_date = created_date
        self.is_active = is_active


@dataclass(frozen=False)
class account_group_role_thin_dto(base_dto):
    account_group_role_uid: str
    account_group_role_name: str
    created_date: datetime.datetime
    is_active: int
    def __init__(self, account_group_role_uid: str,account_group_role_name: str, created_date: datetime.datetime, is_active: int):
        self.account_group_role_uid = account_group_role_uid
        self.account_group_role_name = account_group_role_name
        self.created_date = created_date
        self.is_active = is_active


@dataclass(frozen=False)
class account_hierarchy_thin_dto(base_dto):
    account_hierarchy_uid: str
    account_hierarchy_name: str
    created_date: datetime.datetime
    is_active: int
    def __init__(self, account_hierarchy_uid: str,account_hierarchy_name: str, created_date: datetime.datetime, is_active: int):
        self.account_hierarchy_uid = account_hierarchy_uid
        self.account_hierarchy_name = account_hierarchy_name
        self.created_date = created_date
        self.is_active = is_active


@dataclass(frozen=False)
class account_rate_thin_dto(base_dto):
    account_rate_uid: str
    account_rate_name: str
    created_date: datetime.datetime
    is_active: int
    def __init__(self, account_rate_uid: str,account_rate_name: str, created_date: datetime.datetime, is_active: int):
        self.account_rate_uid = account_rate_uid
        self.account_rate_name = account_rate_name
        self.created_date = created_date
        self.is_active = is_active


@dataclass(frozen=False)
class account_skill_thin_dto(base_dto):
    account_skill_uid: str
    account_skill_name: str
    created_date: datetime.datetime
    is_active: int
    def __init__(self, account_skill_uid: str,account_skill_name: str, created_date: datetime.datetime, is_active: int):
        self.account_skill_uid = account_skill_uid
        self.account_skill_name = account_skill_name
        self.created_date = created_date
        self.is_active = is_active


@dataclass(frozen=False)
class account_skill_assignment_thin_dto(base_dto):
    account_skill_assignment_uid: str
    account_skill_assignment_name: str
    created_date: datetime.datetime
    is_active: int
    def __init__(self, account_skill_assignment_uid: str,account_skill_assignment_name: str, created_date: datetime.datetime, is_active: int):
        self.account_skill_assignment_uid = account_skill_assignment_uid
        self.account_skill_assignment_name = account_skill_assignment_name
        self.created_date = created_date
        self.is_active = is_active


@dataclass(frozen=False)
class account_skill_group_thin_dto(base_dto):
    account_skill_group_uid: str
    account_skill_group_name: str
    created_date: datetime.datetime
    is_active: int
    def __init__(self, account_skill_group_uid: str,account_skill_group_name: str, created_date: datetime.datetime, is_active: int):
        self.account_skill_group_uid = account_skill_group_uid
        self.account_skill_group_name = account_skill_group_name
        self.created_date = created_date
        self.is_active = is_active


@dataclass(frozen=False)
class account_team_thin_dto(base_dto):
    account_team_uid: str
    account_team_name: str
    created_date: datetime.datetime
    is_active: int
    def __init__(self, account_team_uid: str,account_team_name: str, created_date: datetime.datetime, is_active: int):
        self.account_team_uid = account_team_uid
        self.account_team_name = account_team_name
        self.created_date = created_date
        self.is_active = is_active


@dataclass(frozen=False)
class account_title_thin_dto(base_dto):
    account_title_uid: str
    account_title_name: str
    created_date: datetime.datetime
    is_active: int
    def __init__(self, account_title_uid: str,account_title_name: str, created_date: datetime.datetime, is_active: int):
        self.account_title_uid = account_title_uid
        self.account_title_name = account_title_name
        self.created_date = created_date
        self.is_active = is_active


@dataclass(frozen=False)
class account_title_assignment_thin_dto(base_dto):
    account_title_assignment_uid: str
    account_title_assignment_name: str
    created_date: datetime.datetime
    is_active: int
    def __init__(self, account_title_assignment_uid: str,account_title_assignment_name: str, created_date: datetime.datetime, is_active: int):
        self.account_title_assignment_uid = account_title_assignment_uid
        self.account_title_assignment_name = account_title_assignment_name
        self.created_date = created_date
        self.is_active = is_active


@dataclass(frozen=False)
class account_title_responsibility_thin_dto(base_dto):
    account_title_responsibility_uid: str
    account_title_responsibility_name: str
    created_date: datetime.datetime
    is_active: int
    def __init__(self, account_title_responsibility_uid: str,account_title_responsibility_name: str, created_date: datetime.datetime, is_active: int):
        self.account_title_responsibility_uid = account_title_responsibility_uid
        self.account_title_responsibility_name = account_title_responsibility_name
        self.created_date = created_date
        self.is_active = is_active


@dataclass(frozen=False)
class account_type_thin_dto(base_dto):
    account_type_uid: str
    account_type_name: str
    created_date: datetime.datetime
    is_active: int
    def __init__(self, account_type_uid: str,account_type_name: str, created_date: datetime.datetime, is_active: int):
        self.account_type_uid = account_type_uid
        self.account_type_name = account_type_name
        self.created_date = created_date
        self.is_active = is_active


@dataclass(frozen=False)
class audit_change_thin_dto(base_dto):
    audit_change_uid: str
    audit_change_name: str
    created_date: datetime.datetime
    is_active: int
    def __init__(self, audit_change_uid: str,audit_change_name: str, created_date: datetime.datetime, is_active: int):
        self.audit_change_uid = audit_change_uid
        self.audit_change_name = audit_change_name
        self.created_date = created_date
        self.is_active = is_active


@dataclass(frozen=False)
class audit_type_thin_dto(base_dto):
    audit_type_uid: str
    audit_type_name: str
    created_date: datetime.datetime
    is_active: int
    def __init__(self, audit_type_uid: str,audit_type_name: str, created_date: datetime.datetime, is_active: int):
        self.audit_type_uid = audit_type_uid
        self.audit_type_name = audit_type_name
        self.created_date = created_date
        self.is_active = is_active


@dataclass(frozen=False)
class auth_attempt_thin_dto(base_dto):
    auth_attempt_uid: str
    auth_attempt_name: str
    created_date: datetime.datetime
    is_active: int
    def __init__(self, auth_attempt_uid: str,auth_attempt_name: str, created_date: datetime.datetime, is_active: int):
        self.auth_attempt_uid = auth_attempt_uid
        self.auth_attempt_name = auth_attempt_name
        self.created_date = created_date
        self.is_active = is_active


@dataclass(frozen=False)
class auth_identity_thin_dto(base_dto):
    auth_identity_uid: str
    auth_identity_name: str
    created_date: datetime.datetime
    is_active: int
    def __init__(self, auth_identity_uid: str,auth_identity_name: str, created_date: datetime.datetime, is_active: int):
        self.auth_identity_uid = auth_identity_uid
        self.auth_identity_name = auth_identity_name
        self.created_date = created_date
        self.is_active = is_active


@dataclass(frozen=False)
class auth_identity_tenant_thin_dto(base_dto):
    auth_identity_tenant_uid: str
    auth_identity_tenant_name: str
    created_date: datetime.datetime
    is_active: int
    def __init__(self, auth_identity_tenant_uid: str,auth_identity_tenant_name: str, created_date: datetime.datetime, is_active: int):
        self.auth_identity_tenant_uid = auth_identity_tenant_uid
        self.auth_identity_tenant_name = auth_identity_tenant_name
        self.created_date = created_date
        self.is_active = is_active


@dataclass(frozen=False)
class auth_key_thin_dto(base_dto):
    auth_key_uid: str
    auth_key_name: str
    created_date: datetime.datetime
    is_active: int
    def __init__(self, auth_key_uid: str,auth_key_name: str, created_date: datetime.datetime, is_active: int):
        self.auth_key_uid = auth_key_uid
        self.auth_key_name = auth_key_name
        self.created_date = created_date
        self.is_active = is_active


@dataclass(frozen=False)
class auth_key_type_thin_dto(base_dto):
    auth_key_type_uid: str
    auth_key_type_name: str
    created_date: datetime.datetime
    is_active: int
    def __init__(self, auth_key_type_uid: str,auth_key_type_name: str, created_date: datetime.datetime, is_active: int):
        self.auth_key_type_uid = auth_key_type_uid
        self.auth_key_type_name = auth_key_type_name
        self.created_date = created_date
        self.is_active = is_active


@dataclass(frozen=False)
class auth_password_thin_dto(base_dto):
    auth_password_uid: str
    auth_password_name: str
    created_date: datetime.datetime
    is_active: int
    def __init__(self, auth_password_uid: str,auth_password_name: str, created_date: datetime.datetime, is_active: int):
        self.auth_password_uid = auth_password_uid
        self.auth_password_name = auth_password_name
        self.created_date = created_date
        self.is_active = is_active


@dataclass(frozen=False)
class auth_password_current_thin_dto(base_dto):
    auth_password_current_uid: str
    auth_password_current_name: str
    created_date: datetime.datetime
    is_active: int
    def __init__(self, auth_password_current_uid: str,auth_password_current_name: str, created_date: datetime.datetime, is_active: int):
        self.auth_password_current_uid = auth_password_current_uid
        self.auth_password_current_name = auth_password_current_name
        self.created_date = created_date
        self.is_active = is_active


@dataclass(frozen=False)
class auth_password_rule_thin_dto(base_dto):
    auth_password_rule_uid: str
    auth_password_rule_name: str
    created_date: datetime.datetime
    is_active: int
    def __init__(self, auth_password_rule_uid: str,auth_password_rule_name: str, created_date: datetime.datetime, is_active: int):
        self.auth_password_rule_uid = auth_password_rule_uid
        self.auth_password_rule_name = auth_password_rule_name
        self.created_date = created_date
        self.is_active = is_active


@dataclass(frozen=False)
class auth_permission_thin_dto(base_dto):
    auth_permission_uid: str
    auth_permission_name: str
    created_date: datetime.datetime
    is_active: int
    def __init__(self, auth_permission_uid: str,auth_permission_name: str, created_date: datetime.datetime, is_active: int):
        self.auth_permission_uid = auth_permission_uid
        self.auth_permission_name = auth_permission_name
        self.created_date = created_date
        self.is_active = is_active


@dataclass(frozen=False)
class auth_permission_type_thin_dto(base_dto):
    auth_permission_type_uid: str
    auth_permission_type_name: str
    created_date: datetime.datetime
    is_active: int
    def __init__(self, auth_permission_type_uid: str,auth_permission_type_name: str, created_date: datetime.datetime, is_active: int):
        self.auth_permission_type_uid = auth_permission_type_uid
        self.auth_permission_type_name = auth_permission_type_name
        self.created_date = created_date
        self.is_active = is_active


@dataclass(frozen=False)
class auth_pin_thin_dto(base_dto):
    auth_pin_uid: str
    auth_pin_name: str
    created_date: datetime.datetime
    is_active: int
    def __init__(self, auth_pin_uid: str,auth_pin_name: str, created_date: datetime.datetime, is_active: int):
        self.auth_pin_uid = auth_pin_uid
        self.auth_pin_name = auth_pin_name
        self.created_date = created_date
        self.is_active = is_active


@dataclass(frozen=False)
class auth_request_thin_dto(base_dto):
    auth_request_uid: str
    auth_request_name: str
    created_date: datetime.datetime
    is_active: int
    def __init__(self, auth_request_uid: str,auth_request_name: str, created_date: datetime.datetime, is_active: int):
        self.auth_request_uid = auth_request_uid
        self.auth_request_name = auth_request_name
        self.created_date = created_date
        self.is_active = is_active


@dataclass(frozen=False)
class auth_role_thin_dto(base_dto):
    auth_role_uid: str
    auth_role_name: str
    created_date: datetime.datetime
    is_active: int
    def __init__(self, auth_role_uid: str,auth_role_name: str, created_date: datetime.datetime, is_active: int):
        self.auth_role_uid = auth_role_uid
        self.auth_role_name = auth_role_name
        self.created_date = created_date
        self.is_active = is_active


@dataclass(frozen=False)
class auth_role_uri_thin_dto(base_dto):
    auth_role_uri_uid: str
    auth_role_uri_name: str
    created_date: datetime.datetime
    is_active: int
    def __init__(self, auth_role_uri_uid: str,auth_role_uri_name: str, created_date: datetime.datetime, is_active: int):
        self.auth_role_uri_uid = auth_role_uri_uid
        self.auth_role_uri_name = auth_role_uri_name
        self.created_date = created_date
        self.is_active = is_active


@dataclass(frozen=False)
class auth_session_thin_dto(base_dto):
    auth_session_uid: str
    auth_session_name: str
    created_date: datetime.datetime
    is_active: int
    def __init__(self, auth_session_uid: str,auth_session_name: str, created_date: datetime.datetime, is_active: int):
        self.auth_session_uid = auth_session_uid
        self.auth_session_name = auth_session_name
        self.created_date = created_date
        self.is_active = is_active


@dataclass(frozen=False)
class auth_sso_thin_dto(base_dto):
    auth_sso_uid: str
    auth_sso_name: str
    created_date: datetime.datetime
    is_active: int
    def __init__(self, auth_sso_uid: str,auth_sso_name: str, created_date: datetime.datetime, is_active: int):
        self.auth_sso_uid = auth_sso_uid
        self.auth_sso_name = auth_sso_name
        self.created_date = created_date
        self.is_active = is_active


@dataclass(frozen=False)
class auth_token_thin_dto(base_dto):
    auth_token_uid: str
    auth_token_name: str
    created_date: datetime.datetime
    is_active: int
    def __init__(self, auth_token_uid: str,auth_token_name: str, created_date: datetime.datetime, is_active: int):
        self.auth_token_uid = auth_token_uid
        self.auth_token_name = auth_token_name
        self.created_date = created_date
        self.is_active = is_active


@dataclass(frozen=False)
class auth_token_type_thin_dto(base_dto):
    auth_token_type_uid: str
    auth_token_type_name: str
    created_date: datetime.datetime
    is_active: int
    def __init__(self, auth_token_type_uid: str,auth_token_type_name: str, created_date: datetime.datetime, is_active: int):
        self.auth_token_type_uid = auth_token_type_uid
        self.auth_token_type_name = auth_token_type_name
        self.created_date = created_date
        self.is_active = is_active


@dataclass(frozen=False)
class calendar_account_thin_dto(base_dto):
    calendar_account_uid: str
    calendar_account_name: str
    created_date: datetime.datetime
    is_active: int
    def __init__(self, calendar_account_uid: str,calendar_account_name: str, created_date: datetime.datetime, is_active: int):
        self.calendar_account_uid = calendar_account_uid
        self.calendar_account_name = calendar_account_name
        self.created_date = created_date
        self.is_active = is_active


@dataclass(frozen=False)
class calendar_approval_thin_dto(base_dto):
    calendar_approval_uid: str
    calendar_approval_name: str
    created_date: datetime.datetime
    is_active: int
    def __init__(self, calendar_approval_uid: str,calendar_approval_name: str, created_date: datetime.datetime, is_active: int):
        self.calendar_approval_uid = calendar_approval_uid
        self.calendar_approval_name = calendar_approval_name
        self.created_date = created_date
        self.is_active = is_active


@dataclass(frozen=False)
class calendar_approval_type_thin_dto(base_dto):
    calendar_approval_type_uid: str
    calendar_approval_type_name: str
    created_date: datetime.datetime
    is_active: int
    def __init__(self, calendar_approval_type_uid: str,calendar_approval_type_name: str, created_date: datetime.datetime, is_active: int):
        self.calendar_approval_type_uid = calendar_approval_type_uid
        self.calendar_approval_type_name = calendar_approval_type_name
        self.created_date = created_date
        self.is_active = is_active


@dataclass(frozen=False)
class calendar_event_thin_dto(base_dto):
    calendar_event_uid: str
    calendar_event_name: str
    created_date: datetime.datetime
    is_active: int
    def __init__(self, calendar_event_uid: str,calendar_event_name: str, created_date: datetime.datetime, is_active: int):
        self.calendar_event_uid = calendar_event_uid
        self.calendar_event_name = calendar_event_name
        self.created_date = created_date
        self.is_active = is_active


@dataclass(frozen=False)
class calendar_event_group_thin_dto(base_dto):
    calendar_event_group_uid: str
    calendar_event_group_name: str
    created_date: datetime.datetime
    is_active: int
    def __init__(self, calendar_event_group_uid: str,calendar_event_group_name: str, created_date: datetime.datetime, is_active: int):
        self.calendar_event_group_uid = calendar_event_group_uid
        self.calendar_event_group_name = calendar_event_group_name
        self.created_date = created_date
        self.is_active = is_active


@dataclass(frozen=False)
class calendar_event_type_thin_dto(base_dto):
    calendar_event_type_uid: str
    calendar_event_type_name: str
    created_date: datetime.datetime
    is_active: int
    def __init__(self, calendar_event_type_uid: str,calendar_event_type_name: str, created_date: datetime.datetime, is_active: int):
        self.calendar_event_type_uid = calendar_event_type_uid
        self.calendar_event_type_name = calendar_event_type_name
        self.created_date = created_date
        self.is_active = is_active


@dataclass(frozen=False)
class calendar_type_thin_dto(base_dto):
    calendar_type_uid: str
    calendar_type_name: str
    created_date: datetime.datetime
    is_active: int
    def __init__(self, calendar_type_uid: str,calendar_type_name: str, created_date: datetime.datetime, is_active: int):
        self.calendar_type_uid = calendar_type_uid
        self.calendar_type_name = calendar_type_name
        self.created_date = created_date
        self.is_active = is_active


@dataclass(frozen=False)
class client_thin_dto(base_dto):
    client_uid: str
    client_name: str
    created_date: datetime.datetime
    is_active: int
    def __init__(self, client_uid: str,client_name: str, created_date: datetime.datetime, is_active: int):
        self.client_uid = client_uid
        self.client_name = client_name
        self.created_date = created_date
        self.is_active = is_active


@dataclass(frozen=False)
class client_account_thin_dto(base_dto):
    client_account_uid: str
    client_account_name: str
    created_date: datetime.datetime
    is_active: int
    def __init__(self, client_account_uid: str,client_account_name: str, created_date: datetime.datetime, is_active: int):
        self.client_account_uid = client_account_uid
        self.client_account_name = client_account_name
        self.created_date = created_date
        self.is_active = is_active


@dataclass(frozen=False)
class client_contract_thin_dto(base_dto):
    client_contract_uid: str
    client_contract_name: str
    created_date: datetime.datetime
    is_active: int
    def __init__(self, client_contract_uid: str,client_contract_name: str, created_date: datetime.datetime, is_active: int):
        self.client_contract_uid = client_contract_uid
        self.client_contract_name = client_contract_name
        self.created_date = created_date
        self.is_active = is_active


@dataclass(frozen=False)
class client_country_thin_dto(base_dto):
    client_country_uid: str
    client_country_name: str
    created_date: datetime.datetime
    is_active: int
    def __init__(self, client_country_uid: str,client_country_name: str, created_date: datetime.datetime, is_active: int):
        self.client_country_uid = client_country_uid
        self.client_country_name = client_country_name
        self.created_date = created_date
        self.is_active = is_active


@dataclass(frozen=False)
class client_payment_thin_dto(base_dto):
    client_payment_uid: str
    client_payment_name: str
    created_date: datetime.datetime
    is_active: int
    def __init__(self, client_payment_uid: str,client_payment_name: str, created_date: datetime.datetime, is_active: int):
        self.client_payment_uid = client_payment_uid
        self.client_payment_name = client_payment_name
        self.created_date = created_date
        self.is_active = is_active


@dataclass(frozen=False)
class client_role_thin_dto(base_dto):
    client_role_uid: str
    client_role_name: str
    created_date: datetime.datetime
    is_active: int
    def __init__(self, client_role_uid: str,client_role_name: str, created_date: datetime.datetime, is_active: int):
        self.client_role_uid = client_role_uid
        self.client_role_name = client_role_name
        self.created_date = created_date
        self.is_active = is_active


@dataclass(frozen=False)
class client_status_thin_dto(base_dto):
    client_status_uid: str
    client_status_name: str
    created_date: datetime.datetime
    is_active: int
    def __init__(self, client_status_uid: str,client_status_name: str, created_date: datetime.datetime, is_active: int):
        self.client_status_uid = client_status_uid
        self.client_status_name = client_status_name
        self.created_date = created_date
        self.is_active = is_active


@dataclass(frozen=False)
class client_type_thin_dto(base_dto):
    client_type_uid: str
    client_type_name: str
    created_date: datetime.datetime
    is_active: int
    def __init__(self, client_type_uid: str,client_type_name: str, created_date: datetime.datetime, is_active: int):
        self.client_type_uid = client_type_uid
        self.client_type_name = client_type_name
        self.created_date = created_date
        self.is_active = is_active


@dataclass(frozen=False)
class competency_entry_thin_dto(base_dto):
    competency_entry_uid: str
    competency_entry_name: str
    created_date: datetime.datetime
    is_active: int
    def __init__(self, competency_entry_uid: str,competency_entry_name: str, created_date: datetime.datetime, is_active: int):
        self.competency_entry_uid = competency_entry_uid
        self.competency_entry_name = competency_entry_name
        self.created_date = created_date
        self.is_active = is_active


@dataclass(frozen=False)
class competency_entry_account_thin_dto(base_dto):
    competency_entry_account_uid: str
    competency_entry_account_name: str
    created_date: datetime.datetime
    is_active: int
    def __init__(self, competency_entry_account_uid: str,competency_entry_account_name: str, created_date: datetime.datetime, is_active: int):
        self.competency_entry_account_uid = competency_entry_account_uid
        self.competency_entry_account_name = competency_entry_account_name
        self.created_date = created_date
        self.is_active = is_active


@dataclass(frozen=False)
class competency_group_thin_dto(base_dto):
    competency_group_uid: str
    competency_group_name: str
    created_date: datetime.datetime
    is_active: int
    def __init__(self, competency_group_uid: str,competency_group_name: str, created_date: datetime.datetime, is_active: int):
        self.competency_group_uid = competency_group_uid
        self.competency_group_name = competency_group_name
        self.created_date = created_date
        self.is_active = is_active


@dataclass(frozen=False)
class competency_group_account_thin_dto(base_dto):
    competency_group_account_uid: str
    competency_group_account_name: str
    created_date: datetime.datetime
    is_active: int
    def __init__(self, competency_group_account_uid: str,competency_group_account_name: str, created_date: datetime.datetime, is_active: int):
        self.competency_group_account_uid = competency_group_account_uid
        self.competency_group_account_name = competency_group_account_name
        self.created_date = created_date
        self.is_active = is_active


@dataclass(frozen=False)
class competency_group_type_thin_dto(base_dto):
    competency_group_type_uid: str
    competency_group_type_name: str
    created_date: datetime.datetime
    is_active: int
    def __init__(self, competency_group_type_uid: str,competency_group_type_name: str, created_date: datetime.datetime, is_active: int):
        self.competency_group_type_uid = competency_group_type_uid
        self.competency_group_type_name = competency_group_type_name
        self.created_date = created_date
        self.is_active = is_active


@dataclass(frozen=False)
class competency_item_thin_dto(base_dto):
    competency_item_uid: str
    competency_item_name: str
    created_date: datetime.datetime
    is_active: int
    def __init__(self, competency_item_uid: str,competency_item_name: str, created_date: datetime.datetime, is_active: int):
        self.competency_item_uid = competency_item_uid
        self.competency_item_name = competency_item_name
        self.created_date = created_date
        self.is_active = is_active


@dataclass(frozen=False)
class competency_item_account_thin_dto(base_dto):
    competency_item_account_uid: str
    competency_item_account_name: str
    created_date: datetime.datetime
    is_active: int
    def __init__(self, competency_item_account_uid: str,competency_item_account_name: str, created_date: datetime.datetime, is_active: int):
        self.competency_item_account_uid = competency_item_account_uid
        self.competency_item_account_name = competency_item_account_name
        self.created_date = created_date
        self.is_active = is_active


@dataclass(frozen=False)
class competency_item_type_thin_dto(base_dto):
    competency_item_type_uid: str
    competency_item_type_name: str
    created_date: datetime.datetime
    is_active: int
    def __init__(self, competency_item_type_uid: str,competency_item_type_name: str, created_date: datetime.datetime, is_active: int):
        self.competency_item_type_uid = competency_item_type_uid
        self.competency_item_type_name = competency_item_type_name
        self.created_date = created_date
        self.is_active = is_active


@dataclass(frozen=False)
class competency_process_thin_dto(base_dto):
    competency_process_uid: str
    competency_process_name: str
    created_date: datetime.datetime
    is_active: int
    def __init__(self, competency_process_uid: str,competency_process_name: str, created_date: datetime.datetime, is_active: int):
        self.competency_process_uid = competency_process_uid
        self.competency_process_name = competency_process_name
        self.created_date = created_date
        self.is_active = is_active


@dataclass(frozen=False)
class competency_process_account_thin_dto(base_dto):
    competency_process_account_uid: str
    competency_process_account_name: str
    created_date: datetime.datetime
    is_active: int
    def __init__(self, competency_process_account_uid: str,competency_process_account_name: str, created_date: datetime.datetime, is_active: int):
        self.competency_process_account_uid = competency_process_account_uid
        self.competency_process_account_name = competency_process_account_name
        self.created_date = created_date
        self.is_active = is_active


@dataclass(frozen=False)
class competency_process_type_thin_dto(base_dto):
    competency_process_type_uid: str
    competency_process_type_name: str
    created_date: datetime.datetime
    is_active: int
    def __init__(self, competency_process_type_uid: str,competency_process_type_name: str, created_date: datetime.datetime, is_active: int):
        self.competency_process_type_uid = competency_process_type_uid
        self.competency_process_type_name = competency_process_type_name
        self.created_date = created_date
        self.is_active = is_active


@dataclass(frozen=False)
class competency_ranking_thin_dto(base_dto):
    competency_ranking_uid: str
    competency_ranking_name: str
    created_date: datetime.datetime
    is_active: int
    def __init__(self, competency_ranking_uid: str,competency_ranking_name: str, created_date: datetime.datetime, is_active: int):
        self.competency_ranking_uid = competency_ranking_uid
        self.competency_ranking_name = competency_ranking_name
        self.created_date = created_date
        self.is_active = is_active


@dataclass(frozen=False)
class connection_engine_thin_dto(base_dto):
    connection_engine_uid: str
    connection_engine_name: str
    created_date: datetime.datetime
    is_active: int
    def __init__(self, connection_engine_uid: str,connection_engine_name: str, created_date: datetime.datetime, is_active: int):
        self.connection_engine_uid = connection_engine_uid
        self.connection_engine_name = connection_engine_name
        self.created_date = created_date
        self.is_active = is_active


@dataclass(frozen=False)
class connection_host_thin_dto(base_dto):
    connection_host_uid: str
    connection_host_name: str
    created_date: datetime.datetime
    is_active: int
    def __init__(self, connection_host_uid: str,connection_host_name: str, created_date: datetime.datetime, is_active: int):
        self.connection_host_uid = connection_host_uid
        self.connection_host_name = connection_host_name
        self.created_date = created_date
        self.is_active = is_active


@dataclass(frozen=False)
class connection_tenant_thin_dto(base_dto):
    connection_tenant_uid: str
    connection_tenant_name: str
    created_date: datetime.datetime
    is_active: int
    def __init__(self, connection_tenant_uid: str,connection_tenant_name: str, created_date: datetime.datetime, is_active: int):
        self.connection_tenant_uid = connection_tenant_uid
        self.connection_tenant_name = connection_tenant_name
        self.created_date = created_date
        self.is_active = is_active


@dataclass(frozen=False)
class connection_user_thin_dto(base_dto):
    connection_user_uid: str
    connection_user_name: str
    created_date: datetime.datetime
    is_active: int
    def __init__(self, connection_user_uid: str,connection_user_name: str, created_date: datetime.datetime, is_active: int):
        self.connection_user_uid = connection_user_uid
        self.connection_user_name = connection_user_name
        self.created_date = created_date
        self.is_active = is_active


@dataclass(frozen=False)
class country_thin_dto(base_dto):
    country_uid: str
    country_name: str
    created_date: datetime.datetime
    is_active: int
    def __init__(self, country_uid: str,country_name: str, created_date: datetime.datetime, is_active: int):
        self.country_uid = country_uid
        self.country_name = country_name
        self.created_date = created_date
        self.is_active = is_active


@dataclass(frozen=False)
class currency_thin_dto(base_dto):
    currency_uid: str
    currency_name: str
    created_date: datetime.datetime
    is_active: int
    def __init__(self, currency_uid: str,currency_name: str, created_date: datetime.datetime, is_active: int):
        self.currency_uid = currency_uid
        self.currency_name = currency_name
        self.created_date = created_date
        self.is_active = is_active


@dataclass(frozen=False)
class currency_rate_thin_dto(base_dto):
    currency_rate_uid: str
    currency_rate_name: str
    created_date: datetime.datetime
    is_active: int
    def __init__(self, currency_rate_uid: str,currency_rate_name: str, created_date: datetime.datetime, is_active: int):
        self.currency_rate_uid = currency_rate_uid
        self.currency_rate_name = currency_rate_name
        self.created_date = created_date
        self.is_active = is_active


@dataclass(frozen=False)
class currency_source_thin_dto(base_dto):
    currency_source_uid: str
    currency_source_name: str
    created_date: datetime.datetime
    is_active: int
    def __init__(self, currency_source_uid: str,currency_source_name: str, created_date: datetime.datetime, is_active: int):
        self.currency_source_uid = currency_source_uid
        self.currency_source_name = currency_source_name
        self.created_date = created_date
        self.is_active = is_active


@dataclass(frozen=False)
class event_acknowledge_thin_dto(base_dto):
    event_acknowledge_uid: str
    event_acknowledge_name: str
    created_date: datetime.datetime
    is_active: int
    def __init__(self, event_acknowledge_uid: str,event_acknowledge_name: str, created_date: datetime.datetime, is_active: int):
        self.event_acknowledge_uid = event_acknowledge_uid
        self.event_acknowledge_name = event_acknowledge_name
        self.created_date = created_date
        self.is_active = is_active


@dataclass(frozen=False)
class event_channel_thin_dto(base_dto):
    event_channel_uid: str
    event_channel_name: str
    created_date: datetime.datetime
    is_active: int
    def __init__(self, event_channel_uid: str,event_channel_name: str, created_date: datetime.datetime, is_active: int):
        self.event_channel_uid = event_channel_uid
        self.event_channel_name = event_channel_name
        self.created_date = created_date
        self.is_active = is_active


@dataclass(frozen=False)
class event_channel_type_thin_dto(base_dto):
    event_channel_type_uid: str
    event_channel_type_name: str
    created_date: datetime.datetime
    is_active: int
    def __init__(self, event_channel_type_uid: str,event_channel_type_name: str, created_date: datetime.datetime, is_active: int):
        self.event_channel_type_uid = event_channel_type_uid
        self.event_channel_type_name = event_channel_type_name
        self.created_date = created_date
        self.is_active = is_active


@dataclass(frozen=False)
class event_instance_thin_dto(base_dto):
    event_instance_uid: str
    event_instance_name: str
    created_date: datetime.datetime
    is_active: int
    def __init__(self, event_instance_uid: str,event_instance_name: str, created_date: datetime.datetime, is_active: int):
        self.event_instance_uid = event_instance_uid
        self.event_instance_name = event_instance_name
        self.created_date = created_date
        self.is_active = is_active


@dataclass(frozen=False)
class event_notification_thin_dto(base_dto):
    event_notification_uid: str
    event_notification_name: str
    created_date: datetime.datetime
    is_active: int
    def __init__(self, event_notification_uid: str,event_notification_name: str, created_date: datetime.datetime, is_active: int):
        self.event_notification_uid = event_notification_uid
        self.event_notification_name = event_notification_name
        self.created_date = created_date
        self.is_active = is_active


@dataclass(frozen=False)
class event_observer_thin_dto(base_dto):
    event_observer_uid: str
    event_observer_name: str
    created_date: datetime.datetime
    is_active: int
    def __init__(self, event_observer_uid: str,event_observer_name: str, created_date: datetime.datetime, is_active: int):
        self.event_observer_uid = event_observer_uid
        self.event_observer_name = event_observer_name
        self.created_date = created_date
        self.is_active = is_active


@dataclass(frozen=False)
class event_subscription_thin_dto(base_dto):
    event_subscription_uid: str
    event_subscription_name: str
    created_date: datetime.datetime
    is_active: int
    def __init__(self, event_subscription_uid: str,event_subscription_name: str, created_date: datetime.datetime, is_active: int):
        self.event_subscription_uid = event_subscription_uid
        self.event_subscription_name = event_subscription_name
        self.created_date = created_date
        self.is_active = is_active


@dataclass(frozen=False)
class event_template_thin_dto(base_dto):
    event_template_uid: str
    event_template_name: str
    created_date: datetime.datetime
    is_active: int
    def __init__(self, event_template_uid: str,event_template_name: str, created_date: datetime.datetime, is_active: int):
        self.event_template_uid = event_template_uid
        self.event_template_name = event_template_name
        self.created_date = created_date
        self.is_active = is_active


@dataclass(frozen=False)
class event_type_thin_dto(base_dto):
    event_type_uid: str
    event_type_name: str
    created_date: datetime.datetime
    is_active: int
    def __init__(self, event_type_uid: str,event_type_name: str, created_date: datetime.datetime, is_active: int):
        self.event_type_uid = event_type_uid
        self.event_type_name = event_type_name
        self.created_date = created_date
        self.is_active = is_active


@dataclass(frozen=False)
class invoice_action_thin_dto(base_dto):
    invoice_action_uid: str
    invoice_action_name: str
    created_date: datetime.datetime
    is_active: int
    def __init__(self, invoice_action_uid: str,invoice_action_name: str, created_date: datetime.datetime, is_active: int):
        self.invoice_action_uid = invoice_action_uid
        self.invoice_action_name = invoice_action_name
        self.created_date = created_date
        self.is_active = is_active


@dataclass(frozen=False)
class invoice_action_type_thin_dto(base_dto):
    invoice_action_type_uid: str
    invoice_action_type_name: str
    created_date: datetime.datetime
    is_active: int
    def __init__(self, invoice_action_type_uid: str,invoice_action_type_name: str, created_date: datetime.datetime, is_active: int):
        self.invoice_action_type_uid = invoice_action_type_uid
        self.invoice_action_type_name = invoice_action_type_name
        self.created_date = created_date
        self.is_active = is_active


@dataclass(frozen=False)
class invoice_category_thin_dto(base_dto):
    invoice_category_uid: str
    invoice_category_name: str
    created_date: datetime.datetime
    is_active: int
    def __init__(self, invoice_category_uid: str,invoice_category_name: str, created_date: datetime.datetime, is_active: int):
        self.invoice_category_uid = invoice_category_uid
        self.invoice_category_name = invoice_category_name
        self.created_date = created_date
        self.is_active = is_active


@dataclass(frozen=False)
class invoice_entry_thin_dto(base_dto):
    invoice_entry_uid: str
    invoice_entry_name: str
    created_date: datetime.datetime
    is_active: int
    def __init__(self, invoice_entry_uid: str,invoice_entry_name: str, created_date: datetime.datetime, is_active: int):
        self.invoice_entry_uid = invoice_entry_uid
        self.invoice_entry_name = invoice_entry_name
        self.created_date = created_date
        self.is_active = is_active


@dataclass(frozen=False)
class invoice_flow_thin_dto(base_dto):
    invoice_flow_uid: str
    invoice_flow_name: str
    created_date: datetime.datetime
    is_active: int
    def __init__(self, invoice_flow_uid: str,invoice_flow_name: str, created_date: datetime.datetime, is_active: int):
        self.invoice_flow_uid = invoice_flow_uid
        self.invoice_flow_name = invoice_flow_name
        self.created_date = created_date
        self.is_active = is_active


@dataclass(frozen=False)
class invoice_flow_state_thin_dto(base_dto):
    invoice_flow_state_uid: str
    invoice_flow_state_name: str
    created_date: datetime.datetime
    is_active: int
    def __init__(self, invoice_flow_state_uid: str,invoice_flow_state_name: str, created_date: datetime.datetime, is_active: int):
        self.invoice_flow_state_uid = invoice_flow_state_uid
        self.invoice_flow_state_name = invoice_flow_state_name
        self.created_date = created_date
        self.is_active = is_active


@dataclass(frozen=False)
class invoice_instance_thin_dto(base_dto):
    invoice_instance_uid: str
    invoice_instance_name: str
    created_date: datetime.datetime
    is_active: int
    def __init__(self, invoice_instance_uid: str,invoice_instance_name: str, created_date: datetime.datetime, is_active: int):
        self.invoice_instance_uid = invoice_instance_uid
        self.invoice_instance_name = invoice_instance_name
        self.created_date = created_date
        self.is_active = is_active


@dataclass(frozen=False)
class invoice_status_thin_dto(base_dto):
    invoice_status_uid: str
    invoice_status_name: str
    created_date: datetime.datetime
    is_active: int
    def __init__(self, invoice_status_uid: str,invoice_status_name: str, created_date: datetime.datetime, is_active: int):
        self.invoice_status_uid = invoice_status_uid
        self.invoice_status_name = invoice_status_name
        self.created_date = created_date
        self.is_active = is_active


@dataclass(frozen=False)
class invoice_type_thin_dto(base_dto):
    invoice_type_uid: str
    invoice_type_name: str
    created_date: datetime.datetime
    is_active: int
    def __init__(self, invoice_type_uid: str,invoice_type_name: str, created_date: datetime.datetime, is_active: int):
        self.invoice_type_uid = invoice_type_uid
        self.invoice_type_name = invoice_type_name
        self.created_date = created_date
        self.is_active = is_active


@dataclass(frozen=False)
class location_hierarchy_thin_dto(base_dto):
    location_hierarchy_uid: str
    location_hierarchy_name: str
    created_date: datetime.datetime
    is_active: int
    def __init__(self, location_hierarchy_uid: str,location_hierarchy_name: str, created_date: datetime.datetime, is_active: int):
        self.location_hierarchy_uid = location_hierarchy_uid
        self.location_hierarchy_name = location_hierarchy_name
        self.created_date = created_date
        self.is_active = is_active


@dataclass(frozen=False)
class location_postal_code_thin_dto(base_dto):
    location_postal_code_uid: str
    location_postal_code_name: str
    created_date: datetime.datetime
    is_active: int
    def __init__(self, location_postal_code_uid: str,location_postal_code_name: str, created_date: datetime.datetime, is_active: int):
        self.location_postal_code_uid = location_postal_code_uid
        self.location_postal_code_name = location_postal_code_name
        self.created_date = created_date
        self.is_active = is_active


@dataclass(frozen=False)
class location_region_thin_dto(base_dto):
    location_region_uid: str
    location_region_name: str
    created_date: datetime.datetime
    is_active: int
    def __init__(self, location_region_uid: str,location_region_name: str, created_date: datetime.datetime, is_active: int):
        self.location_region_uid = location_region_uid
        self.location_region_name = location_region_name
        self.created_date = created_date
        self.is_active = is_active


@dataclass(frozen=False)
class location_territory_thin_dto(base_dto):
    location_territory_uid: str
    location_territory_name: str
    created_date: datetime.datetime
    is_active: int
    def __init__(self, location_territory_uid: str,location_territory_name: str, created_date: datetime.datetime, is_active: int):
        self.location_territory_uid = location_territory_uid
        self.location_territory_name = location_territory_name
        self.created_date = created_date
        self.is_active = is_active


@dataclass(frozen=False)
class monitor_thin_dto(base_dto):
    monitor_uid: str
    monitor_name: str
    created_date: datetime.datetime
    is_active: int
    def __init__(self, monitor_uid: str,monitor_name: str, created_date: datetime.datetime, is_active: int):
        self.monitor_uid = monitor_uid
        self.monitor_name = monitor_name
        self.created_date = created_date
        self.is_active = is_active


@dataclass(frozen=False)
class monitor_run_thin_dto(base_dto):
    monitor_run_uid: str
    monitor_run_name: str
    created_date: datetime.datetime
    is_active: int
    def __init__(self, monitor_run_uid: str,monitor_run_name: str, created_date: datetime.datetime, is_active: int):
        self.monitor_run_uid = monitor_run_uid
        self.monitor_run_name = monitor_run_name
        self.created_date = created_date
        self.is_active = is_active


@dataclass(frozen=False)
class monitor_type_thin_dto(base_dto):
    monitor_type_uid: str
    monitor_type_name: str
    created_date: datetime.datetime
    is_active: int
    def __init__(self, monitor_type_uid: str,monitor_type_name: str, created_date: datetime.datetime, is_active: int):
        self.monitor_type_uid = monitor_type_uid
        self.monitor_type_name = monitor_type_name
        self.created_date = created_date
        self.is_active = is_active


@dataclass(frozen=False)
class period_thin_dto(base_dto):
    period_uid: str
    period_name: str
    created_date: datetime.datetime
    is_active: int
    def __init__(self, period_uid: str,period_name: str, created_date: datetime.datetime, is_active: int):
        self.period_uid = period_uid
        self.period_name = period_name
        self.created_date = created_date
        self.is_active = is_active


@dataclass(frozen=False)
class process_thin_dto(base_dto):
    process_uid: str
    process_name: str
    created_date: datetime.datetime
    is_active: int
    def __init__(self, process_uid: str,process_name: str, created_date: datetime.datetime, is_active: int):
        self.process_uid = process_uid
        self.process_name = process_name
        self.created_date = created_date
        self.is_active = is_active


@dataclass(frozen=False)
class process_result_thin_dto(base_dto):
    process_result_uid: str
    process_result_name: str
    created_date: datetime.datetime
    is_active: int
    def __init__(self, process_result_uid: str,process_result_name: str, created_date: datetime.datetime, is_active: int):
        self.process_result_uid = process_result_uid
        self.process_result_name = process_result_name
        self.created_date = created_date
        self.is_active = is_active


@dataclass(frozen=False)
class process_run_thin_dto(base_dto):
    process_run_uid: str
    process_run_name: str
    created_date: datetime.datetime
    is_active: int
    def __init__(self, process_run_uid: str,process_run_name: str, created_date: datetime.datetime, is_active: int):
        self.process_run_uid = process_run_uid
        self.process_run_name = process_run_name
        self.created_date = created_date
        self.is_active = is_active


@dataclass(frozen=False)
class process_type_thin_dto(base_dto):
    process_type_uid: str
    process_type_name: str
    created_date: datetime.datetime
    is_active: int
    def __init__(self, process_type_uid: str,process_type_name: str, created_date: datetime.datetime, is_active: int):
        self.process_type_uid = process_type_uid
        self.process_type_name = process_type_name
        self.created_date = created_date
        self.is_active = is_active


@dataclass(frozen=False)
class project_account_thin_dto(base_dto):
    project_account_uid: str
    project_account_name: str
    created_date: datetime.datetime
    is_active: int
    def __init__(self, project_account_uid: str,project_account_name: str, created_date: datetime.datetime, is_active: int):
        self.project_account_uid = project_account_uid
        self.project_account_name = project_account_name
        self.created_date = created_date
        self.is_active = is_active


@dataclass(frozen=False)
class project_budget_thin_dto(base_dto):
    project_budget_uid: str
    project_budget_name: str
    created_date: datetime.datetime
    is_active: int
    def __init__(self, project_budget_uid: str,project_budget_name: str, created_date: datetime.datetime, is_active: int):
        self.project_budget_uid = project_budget_uid
        self.project_budget_name = project_budget_name
        self.created_date = created_date
        self.is_active = is_active


@dataclass(frozen=False)
class project_group_thin_dto(base_dto):
    project_group_uid: str
    project_group_name: str
    created_date: datetime.datetime
    is_active: int
    def __init__(self, project_group_uid: str,project_group_name: str, created_date: datetime.datetime, is_active: int):
        self.project_group_uid = project_group_uid
        self.project_group_name = project_group_name
        self.created_date = created_date
        self.is_active = is_active


@dataclass(frozen=False)
class project_instance_thin_dto(base_dto):
    project_instance_uid: str
    project_instance_name: str
    created_date: datetime.datetime
    is_active: int
    def __init__(self, project_instance_uid: str,project_instance_name: str, created_date: datetime.datetime, is_active: int):
        self.project_instance_uid = project_instance_uid
        self.project_instance_name = project_instance_name
        self.created_date = created_date
        self.is_active = is_active


@dataclass(frozen=False)
class project_milestone_thin_dto(base_dto):
    project_milestone_uid: str
    project_milestone_name: str
    created_date: datetime.datetime
    is_active: int
    def __init__(self, project_milestone_uid: str,project_milestone_name: str, created_date: datetime.datetime, is_active: int):
        self.project_milestone_uid = project_milestone_uid
        self.project_milestone_name = project_milestone_name
        self.created_date = created_date
        self.is_active = is_active


@dataclass(frozen=False)
class project_phase_thin_dto(base_dto):
    project_phase_uid: str
    project_phase_name: str
    created_date: datetime.datetime
    is_active: int
    def __init__(self, project_phase_uid: str,project_phase_name: str, created_date: datetime.datetime, is_active: int):
        self.project_phase_uid = project_phase_uid
        self.project_phase_name = project_phase_name
        self.created_date = created_date
        self.is_active = is_active


@dataclass(frozen=False)
class project_type_thin_dto(base_dto):
    project_type_uid: str
    project_type_name: str
    created_date: datetime.datetime
    is_active: int
    def __init__(self, project_type_uid: str,project_type_name: str, created_date: datetime.datetime, is_active: int):
        self.project_type_uid = project_type_uid
        self.project_type_name = project_type_name
        self.created_date = created_date
        self.is_active = is_active


@dataclass(frozen=False)
class report_thin_dto(base_dto):
    report_uid: str
    report_name: str
    created_date: datetime.datetime
    is_active: int
    def __init__(self, report_uid: str,report_name: str, created_date: datetime.datetime, is_active: int):
        self.report_uid = report_uid
        self.report_name = report_name
        self.created_date = created_date
        self.is_active = is_active


@dataclass(frozen=False)
class report_content_type_thin_dto(base_dto):
    report_content_type_uid: str
    report_content_type_name: str
    created_date: datetime.datetime
    is_active: int
    def __init__(self, report_content_type_uid: str,report_content_type_name: str, created_date: datetime.datetime, is_active: int):
        self.report_content_type_uid = report_content_type_uid
        self.report_content_type_name = report_content_type_name
        self.created_date = created_date
        self.is_active = is_active


@dataclass(frozen=False)
class report_format_thin_dto(base_dto):
    report_format_uid: str
    report_format_name: str
    created_date: datetime.datetime
    is_active: int
    def __init__(self, report_format_uid: str,report_format_name: str, created_date: datetime.datetime, is_active: int):
        self.report_format_uid = report_format_uid
        self.report_format_name = report_format_name
        self.created_date = created_date
        self.is_active = is_active


@dataclass(frozen=False)
class report_run_thin_dto(base_dto):
    report_run_uid: str
    report_run_name: str
    created_date: datetime.datetime
    is_active: int
    def __init__(self, report_run_uid: str,report_run_name: str, created_date: datetime.datetime, is_active: int):
        self.report_run_uid = report_run_uid
        self.report_run_name = report_run_name
        self.created_date = created_date
        self.is_active = is_active


@dataclass(frozen=False)
class report_status_thin_dto(base_dto):
    report_status_uid: str
    report_status_name: str
    created_date: datetime.datetime
    is_active: int
    def __init__(self, report_status_uid: str,report_status_name: str, created_date: datetime.datetime, is_active: int):
        self.report_status_uid = report_status_uid
        self.report_status_name = report_status_name
        self.created_date = created_date
        self.is_active = is_active


@dataclass(frozen=False)
class report_type_thin_dto(base_dto):
    report_type_uid: str
    report_type_name: str
    created_date: datetime.datetime
    is_active: int
    def __init__(self, report_type_uid: str,report_type_name: str, created_date: datetime.datetime, is_active: int):
        self.report_type_uid = report_type_uid
        self.report_type_name = report_type_name
        self.created_date = created_date
        self.is_active = is_active


@dataclass(frozen=False)
class storage_thin_dto(base_dto):
    storage_uid: str
    storage_name: str
    created_date: datetime.datetime
    is_active: int
    def __init__(self, storage_uid: str,storage_name: str, created_date: datetime.datetime, is_active: int):
        self.storage_uid = storage_uid
        self.storage_name = storage_name
        self.created_date = created_date
        self.is_active = is_active


@dataclass(frozen=False)
class storage_category_thin_dto(base_dto):
    storage_category_uid: str
    storage_category_name: str
    created_date: datetime.datetime
    is_active: int
    def __init__(self, storage_category_uid: str,storage_category_name: str, created_date: datetime.datetime, is_active: int):
        self.storage_category_uid = storage_category_uid
        self.storage_category_name = storage_category_name
        self.created_date = created_date
        self.is_active = is_active


@dataclass(frozen=False)
class storage_connection_thin_dto(base_dto):
    storage_connection_uid: str
    storage_connection_name: str
    created_date: datetime.datetime
    is_active: int
    def __init__(self, storage_connection_uid: str,storage_connection_name: str, created_date: datetime.datetime, is_active: int):
        self.storage_connection_uid = storage_connection_uid
        self.storage_connection_name = storage_connection_name
        self.created_date = created_date
        self.is_active = is_active


@dataclass(frozen=False)
class storage_query_thin_dto(base_dto):
    storage_query_uid: str
    storage_query_name: str
    created_date: datetime.datetime
    is_active: int
    def __init__(self, storage_query_uid: str,storage_query_name: str, created_date: datetime.datetime, is_active: int):
        self.storage_query_uid = storage_query_uid
        self.storage_query_name = storage_query_name
        self.created_date = created_date
        self.is_active = is_active


@dataclass(frozen=False)
class storage_type_thin_dto(base_dto):
    storage_type_uid: str
    storage_type_name: str
    created_date: datetime.datetime
    is_active: int
    def __init__(self, storage_type_uid: str,storage_type_name: str, created_date: datetime.datetime, is_active: int):
        self.storage_type_uid = storage_type_uid
        self.storage_type_name = storage_type_name
        self.created_date = created_date
        self.is_active = is_active


@dataclass(frozen=False)
class synchronization_thin_dto(base_dto):
    synchronization_uid: str
    synchronization_name: str
    created_date: datetime.datetime
    is_active: int
    def __init__(self, synchronization_uid: str,synchronization_name: str, created_date: datetime.datetime, is_active: int):
        self.synchronization_uid = synchronization_uid
        self.synchronization_name = synchronization_name
        self.created_date = created_date
        self.is_active = is_active


@dataclass(frozen=False)
class synchronization_run_thin_dto(base_dto):
    synchronization_run_uid: str
    synchronization_run_name: str
    created_date: datetime.datetime
    is_active: int
    def __init__(self, synchronization_run_uid: str,synchronization_run_name: str, created_date: datetime.datetime, is_active: int):
        self.synchronization_run_uid = synchronization_run_uid
        self.synchronization_run_name = synchronization_run_name
        self.created_date = created_date
        self.is_active = is_active


@dataclass(frozen=False)
class synchronization_type_thin_dto(base_dto):
    synchronization_type_uid: str
    synchronization_type_name: str
    created_date: datetime.datetime
    is_active: int
    def __init__(self, synchronization_type_uid: str,synchronization_type_name: str, created_date: datetime.datetime, is_active: int):
        self.synchronization_type_uid = synchronization_type_uid
        self.synchronization_type_name = synchronization_type_name
        self.created_date = created_date
        self.is_active = is_active


@dataclass(frozen=False)
class system_attribute_thin_dto(base_dto):
    system_attribute_uid: str
    system_attribute_name: str
    created_date: datetime.datetime
    is_active: int
    def __init__(self, system_attribute_uid: str,system_attribute_name: str, created_date: datetime.datetime, is_active: int):
        self.system_attribute_uid = system_attribute_uid
        self.system_attribute_name = system_attribute_name
        self.created_date = created_date
        self.is_active = is_active


@dataclass(frozen=False)
class system_constraint_thin_dto(base_dto):
    system_constraint_uid: str
    system_constraint_name: str
    created_date: datetime.datetime
    is_active: int
    def __init__(self, system_constraint_uid: str,system_constraint_name: str, created_date: datetime.datetime, is_active: int):
        self.system_constraint_uid = system_constraint_uid
        self.system_constraint_name = system_constraint_name
        self.created_date = created_date
        self.is_active = is_active


@dataclass(frozen=False)
class system_database_thin_dto(base_dto):
    system_database_uid: str
    system_database_name: str
    created_date: datetime.datetime
    is_active: int
    def __init__(self, system_database_uid: str,system_database_name: str, created_date: datetime.datetime, is_active: int):
        self.system_database_uid = system_database_uid
        self.system_database_name = system_database_name
        self.created_date = created_date
        self.is_active = is_active


@dataclass(frozen=False)
class system_exception_thin_dto(base_dto):
    system_exception_uid: str
    system_exception_name: str
    created_date: datetime.datetime
    is_active: int
    def __init__(self, system_exception_uid: str,system_exception_name: str, created_date: datetime.datetime, is_active: int):
        self.system_exception_uid = system_exception_uid
        self.system_exception_name = system_exception_name
        self.created_date = created_date
        self.is_active = is_active


@dataclass(frozen=False)
class system_instance_thin_dto(base_dto):
    system_instance_uid: str
    system_instance_name: str
    created_date: datetime.datetime
    is_active: int
    def __init__(self, system_instance_uid: str,system_instance_name: str, created_date: datetime.datetime, is_active: int):
        self.system_instance_uid = system_instance_uid
        self.system_instance_name = system_instance_name
        self.created_date = created_date
        self.is_active = is_active


@dataclass(frozen=False)
class system_license_thin_dto(base_dto):
    system_license_uid: str
    system_license_name: str
    created_date: datetime.datetime
    is_active: int
    def __init__(self, system_license_uid: str,system_license_name: str, created_date: datetime.datetime, is_active: int):
        self.system_license_uid = system_license_uid
        self.system_license_name = system_license_name
        self.created_date = created_date
        self.is_active = is_active


@dataclass(frozen=False)
class system_lock_thin_dto(base_dto):
    system_lock_uid: str
    system_lock_name: str
    created_date: datetime.datetime
    is_active: int
    def __init__(self, system_lock_uid: str,system_lock_name: str, created_date: datetime.datetime, is_active: int):
        self.system_lock_uid = system_lock_uid
        self.system_lock_name = system_lock_name
        self.created_date = created_date
        self.is_active = is_active


@dataclass(frozen=False)
class system_module_thin_dto(base_dto):
    system_module_uid: str
    system_module_name: str
    created_date: datetime.datetime
    is_active: int
    def __init__(self, system_module_uid: str,system_module_name: str, created_date: datetime.datetime, is_active: int):
        self.system_module_uid = system_module_uid
        self.system_module_name = system_module_name
        self.created_date = created_date
        self.is_active = is_active


@dataclass(frozen=False)
class system_query_thin_dto(base_dto):
    system_query_uid: str
    system_query_name: str
    created_date: datetime.datetime
    is_active: int
    def __init__(self, system_query_uid: str,system_query_name: str, created_date: datetime.datetime, is_active: int):
        self.system_query_uid = system_query_uid
        self.system_query_name = system_query_name
        self.created_date = created_date
        self.is_active = is_active


@dataclass(frozen=False)
class system_request_thin_dto(base_dto):
    system_request_uid: str
    system_request_name: str
    created_date: datetime.datetime
    is_active: int
    def __init__(self, system_request_uid: str,system_request_name: str, created_date: datetime.datetime, is_active: int):
        self.system_request_uid = system_request_uid
        self.system_request_name = system_request_name
        self.created_date = created_date
        self.is_active = is_active


@dataclass(frozen=False)
class system_setting_thin_dto(base_dto):
    system_setting_uid: str
    system_setting_name: str
    created_date: datetime.datetime
    is_active: int
    def __init__(self, system_setting_uid: str,system_setting_name: str, created_date: datetime.datetime, is_active: int):
        self.system_setting_uid = system_setting_uid
        self.system_setting_name = system_setting_name
        self.created_date = created_date
        self.is_active = is_active


@dataclass(frozen=False)
class system_setting_account_thin_dto(base_dto):
    system_setting_account_uid: str
    system_setting_account_name: str
    created_date: datetime.datetime
    is_active: int
    def __init__(self, system_setting_account_uid: str,system_setting_account_name: str, created_date: datetime.datetime, is_active: int):
        self.system_setting_account_uid = system_setting_account_uid
        self.system_setting_account_name = system_setting_account_name
        self.created_date = created_date
        self.is_active = is_active


@dataclass(frozen=False)
class system_state_thin_dto(base_dto):
    system_state_uid: str
    system_state_name: str
    created_date: datetime.datetime
    is_active: int
    def __init__(self, system_state_uid: str,system_state_name: str, created_date: datetime.datetime, is_active: int):
        self.system_state_uid = system_state_uid
        self.system_state_name = system_state_name
        self.created_date = created_date
        self.is_active = is_active


@dataclass(frozen=False)
class system_table_thin_dto(base_dto):
    system_table_uid: str
    system_table_name: str
    created_date: datetime.datetime
    is_active: int
    def __init__(self, system_table_uid: str,system_table_name: str, created_date: datetime.datetime, is_active: int):
        self.system_table_uid = system_table_uid
        self.system_table_name = system_table_name
        self.created_date = created_date
        self.is_active = is_active


@dataclass(frozen=False)
class system_thread_thin_dto(base_dto):
    system_thread_uid: str
    system_thread_name: str
    created_date: datetime.datetime
    is_active: int
    def __init__(self, system_thread_uid: str,system_thread_name: str, created_date: datetime.datetime, is_active: int):
        self.system_thread_uid = system_thread_uid
        self.system_thread_name = system_thread_name
        self.created_date = created_date
        self.is_active = is_active


@dataclass(frozen=False)
class system_version_thin_dto(base_dto):
    system_version_uid: str
    system_version_name: str
    created_date: datetime.datetime
    is_active: int
    def __init__(self, system_version_uid: str,system_version_name: str, created_date: datetime.datetime, is_active: int):
        self.system_version_uid = system_version_uid
        self.system_version_name = system_version_name
        self.created_date = created_date
        self.is_active = is_active


@dataclass(frozen=False)
class tenant_thin_dto(base_dto):
    tenant_uid: str
    tenant_name: str
    created_date: datetime.datetime
    is_active: int
    def __init__(self, tenant_uid: str,tenant_name: str, created_date: datetime.datetime, is_active: int):
        self.tenant_uid = tenant_uid
        self.tenant_name = tenant_name
        self.created_date = created_date
        self.is_active = is_active


@dataclass(frozen=False)
class tenant_account_thin_dto(base_dto):
    tenant_account_uid: str
    tenant_account_name: str
    created_date: datetime.datetime
    is_active: int
    def __init__(self, tenant_account_uid: str,tenant_account_name: str, created_date: datetime.datetime, is_active: int):
        self.tenant_account_uid = tenant_account_uid
        self.tenant_account_name = tenant_account_name
        self.created_date = created_date
        self.is_active = is_active


@dataclass(frozen=False)
class tenant_category_thin_dto(base_dto):
    tenant_category_uid: str
    tenant_category_name: str
    created_date: datetime.datetime
    is_active: int
    def __init__(self, tenant_category_uid: str,tenant_category_name: str, created_date: datetime.datetime, is_active: int):
        self.tenant_category_uid = tenant_category_uid
        self.tenant_category_name = tenant_category_name
        self.created_date = created_date
        self.is_active = is_active


@dataclass(frozen=False)
class tenant_country_thin_dto(base_dto):
    tenant_country_uid: str
    tenant_country_name: str
    created_date: datetime.datetime
    is_active: int
    def __init__(self, tenant_country_uid: str,tenant_country_name: str, created_date: datetime.datetime, is_active: int):
        self.tenant_country_uid = tenant_country_uid
        self.tenant_country_name = tenant_country_name
        self.created_date = created_date
        self.is_active = is_active


@dataclass(frozen=False)
class tenant_license_thin_dto(base_dto):
    tenant_license_uid: str
    tenant_license_name: str
    created_date: datetime.datetime
    is_active: int
    def __init__(self, tenant_license_uid: str,tenant_license_name: str, created_date: datetime.datetime, is_active: int):
        self.tenant_license_uid = tenant_license_uid
        self.tenant_license_name = tenant_license_name
        self.created_date = created_date
        self.is_active = is_active


@dataclass(frozen=False)
class tenant_payment_thin_dto(base_dto):
    tenant_payment_uid: str
    tenant_payment_name: str
    created_date: datetime.datetime
    is_active: int
    def __init__(self, tenant_payment_uid: str,tenant_payment_name: str, created_date: datetime.datetime, is_active: int):
        self.tenant_payment_uid = tenant_payment_uid
        self.tenant_payment_name = tenant_payment_name
        self.created_date = created_date
        self.is_active = is_active


@dataclass(frozen=False)
class tenant_payment_type_thin_dto(base_dto):
    tenant_payment_type_uid: str
    tenant_payment_type_name: str
    created_date: datetime.datetime
    is_active: int
    def __init__(self, tenant_payment_type_uid: str,tenant_payment_type_name: str, created_date: datetime.datetime, is_active: int):
        self.tenant_payment_type_uid = tenant_payment_type_uid
        self.tenant_payment_type_name = tenant_payment_type_name
        self.created_date = created_date
        self.is_active = is_active


@dataclass(frozen=False)
class tenant_role_thin_dto(base_dto):
    tenant_role_uid: str
    tenant_role_name: str
    created_date: datetime.datetime
    is_active: int
    def __init__(self, tenant_role_uid: str,tenant_role_name: str, created_date: datetime.datetime, is_active: int):
        self.tenant_role_uid = tenant_role_uid
        self.tenant_role_name = tenant_role_name
        self.created_date = created_date
        self.is_active = is_active


@dataclass(frozen=False)
class tenant_status_thin_dto(base_dto):
    tenant_status_uid: str
    tenant_status_name: str
    created_date: datetime.datetime
    is_active: int
    def __init__(self, tenant_status_uid: str,tenant_status_name: str, created_date: datetime.datetime, is_active: int):
        self.tenant_status_uid = tenant_status_uid
        self.tenant_status_name = tenant_status_name
        self.created_date = created_date
        self.is_active = is_active


@dataclass(frozen=False)
class tenant_type_thin_dto(base_dto):
    tenant_type_uid: str
    tenant_type_name: str
    created_date: datetime.datetime
    is_active: int
    def __init__(self, tenant_type_uid: str,tenant_type_name: str, created_date: datetime.datetime, is_active: int):
        self.tenant_type_uid = tenant_type_uid
        self.tenant_type_name = tenant_type_name
        self.created_date = created_date
        self.is_active = is_active


@dataclass(frozen=False)
class time_approval_thin_dto(base_dto):
    time_approval_uid: str
    time_approval_name: str
    created_date: datetime.datetime
    is_active: int
    def __init__(self, time_approval_uid: str,time_approval_name: str, created_date: datetime.datetime, is_active: int):
        self.time_approval_uid = time_approval_uid
        self.time_approval_name = time_approval_name
        self.created_date = created_date
        self.is_active = is_active


@dataclass(frozen=False)
class time_entry_thin_dto(base_dto):
    time_entry_uid: str
    time_entry_name: str
    created_date: datetime.datetime
    is_active: int
    def __init__(self, time_entry_uid: str,time_entry_name: str, created_date: datetime.datetime, is_active: int):
        self.time_entry_uid = time_entry_uid
        self.time_entry_name = time_entry_name
        self.created_date = created_date
        self.is_active = is_active


@dataclass(frozen=False)
class time_entry_final_thin_dto(base_dto):
    time_entry_final_uid: str
    time_entry_final_name: str
    created_date: datetime.datetime
    is_active: int
    def __init__(self, time_entry_final_uid: str,time_entry_final_name: str, created_date: datetime.datetime, is_active: int):
        self.time_entry_final_uid = time_entry_final_uid
        self.time_entry_final_name = time_entry_final_name
        self.created_date = created_date
        self.is_active = is_active


@dataclass(frozen=False)
class time_entry_invoice_thin_dto(base_dto):
    time_entry_invoice_uid: str
    time_entry_invoice_name: str
    created_date: datetime.datetime
    is_active: int
    def __init__(self, time_entry_invoice_uid: str,time_entry_invoice_name: str, created_date: datetime.datetime, is_active: int):
        self.time_entry_invoice_uid = time_entry_invoice_uid
        self.time_entry_invoice_name = time_entry_invoice_name
        self.created_date = created_date
        self.is_active = is_active


@dataclass(frozen=False)
class time_rule_thin_dto(base_dto):
    time_rule_uid: str
    time_rule_name: str
    created_date: datetime.datetime
    is_active: int
    def __init__(self, time_rule_uid: str,time_rule_name: str, created_date: datetime.datetime, is_active: int):
        self.time_rule_uid = time_rule_uid
        self.time_rule_name = time_rule_name
        self.created_date = created_date
        self.is_active = is_active


@dataclass(frozen=False)
class time_rule_client_thin_dto(base_dto):
    time_rule_client_uid: str
    time_rule_client_name: str
    created_date: datetime.datetime
    is_active: int
    def __init__(self, time_rule_client_uid: str,time_rule_client_name: str, created_date: datetime.datetime, is_active: int):
        self.time_rule_client_uid = time_rule_client_uid
        self.time_rule_client_name = time_rule_client_name
        self.created_date = created_date
        self.is_active = is_active


@dataclass(frozen=False)
class time_submit_thin_dto(base_dto):
    time_submit_uid: str
    time_submit_name: str
    created_date: datetime.datetime
    is_active: int
    def __init__(self, time_submit_uid: str,time_submit_name: str, created_date: datetime.datetime, is_active: int):
        self.time_submit_uid = time_submit_uid
        self.time_submit_name = time_submit_name
        self.created_date = created_date
        self.is_active = is_active


@dataclass(frozen=False)
class time_submit_type_thin_dto(base_dto):
    time_submit_type_uid: str
    time_submit_type_name: str
    created_date: datetime.datetime
    is_active: int
    def __init__(self, time_submit_type_uid: str,time_submit_type_name: str, created_date: datetime.datetime, is_active: int):
        self.time_submit_type_uid = time_submit_type_uid
        self.time_submit_type_name = time_submit_type_name
        self.created_date = created_date
        self.is_active = is_active


# auto-generated - v_definition_python_dtos_thin - END
