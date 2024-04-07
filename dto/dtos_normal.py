# auto-generated - v_definition_python_dtos_normal - START at 2024-04-07 12:05:58.840686+02
import datetime
from abc import abstractmethod
from dataclasses import dataclass, asdict
import json
from base.base_objects import objects
from dto.dtos import *
from dto.dtos_models import *
from dto.dtos_write import *


@dataclass(frozen=False)
class account_normal_dto(base_read_dto, account_write_dto):
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
    is_system: int
    created_date: datetime.datetime
    created_by: str
    def __init__(self, account_uid: str, account_name: str, tenant_uid: str, account_type_uid: str, account_title_uid: str, account_division_uid: str, account_group_uid: str, auth_identity_uid: str, account_email: str, display_name: str, is_system: int, created_date: datetime.datetime, created_by: str):
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
        self.is_system = is_system
        self.created_date = created_date
        self.created_by = created_by


@dataclass(frozen=False)
class account_division_normal_dto(base_read_dto, account_division_write_dto):
    account_division_uid: str
    account_division_name: str
    tenant_uid: str
    account_uid: str
    account_division_template_uid: str
    division_description: str
    created_date: datetime.datetime
    created_by: str
    def __init__(self, account_division_uid: str, account_division_name: str, tenant_uid: str, account_uid: str, account_division_template_uid: str, division_description: str, created_date: datetime.datetime, created_by: str):
        self.account_division_uid = account_division_uid
        self.account_division_name = account_division_name
        self.tenant_uid = tenant_uid
        self.account_uid = account_uid
        self.account_division_template_uid = account_division_template_uid
        self.division_description = division_description
        self.created_date = created_date
        self.created_by = created_by


@dataclass(frozen=False)
class account_division_template_normal_dto(base_read_dto, account_division_template_write_dto):
    account_division_template_uid: str
    account_division_template_name: str
    division_description: str
    created_date: datetime.datetime
    created_by: str
    def __init__(self, account_division_template_uid: str, account_division_template_name: str, division_description: str, created_date: datetime.datetime, created_by: str):
        self.account_division_template_uid = account_division_template_uid
        self.account_division_template_name = account_division_template_name
        self.division_description = division_description
        self.created_date = created_date
        self.created_by = created_by


@dataclass(frozen=False)
class account_group_normal_dto(base_read_dto, account_group_write_dto):
    account_group_uid: str
    account_group_name: str
    tenant_uid: str
    account_group_description: str
    created_date: datetime.datetime
    created_by: str
    def __init__(self, account_group_uid: str, account_group_name: str, tenant_uid: str, account_group_description: str, created_date: datetime.datetime, created_by: str):
        self.account_group_uid = account_group_uid
        self.account_group_name = account_group_name
        self.tenant_uid = tenant_uid
        self.account_group_description = account_group_description
        self.created_date = created_date
        self.created_by = created_by


@dataclass(frozen=False)
class account_hierarchy_normal_dto(base_read_dto, account_hierarchy_write_dto):
    account_hierarchy_uid: str
    account_hierarchy_name: str
    tenant_uid: str
    parent_account_uid: str
    child_account_uid: str
    created_date: datetime.datetime
    created_by: str
    def __init__(self, account_hierarchy_uid: str, account_hierarchy_name: str, tenant_uid: str, parent_account_uid: str, child_account_uid: str, created_date: datetime.datetime, created_by: str):
        self.account_hierarchy_uid = account_hierarchy_uid
        self.account_hierarchy_name = account_hierarchy_name
        self.tenant_uid = tenant_uid
        self.parent_account_uid = parent_account_uid
        self.child_account_uid = child_account_uid
        self.created_date = created_date
        self.created_by = created_by


@dataclass(frozen=False)
class account_rate_normal_dto(base_read_dto, account_rate_write_dto):
    account_rate_uid: str
    account_rate_name: str
    tenant_uid: str
    account_uid: str
    currency_uid: str
    rate: str
    start_date: datetime.datetime
    end_date: datetime.datetime
    created_date: datetime.datetime
    created_by: str
    def __init__(self, account_rate_uid: str, account_rate_name: str, tenant_uid: str, account_uid: str, currency_uid: str, rate: str, start_date: datetime.datetime, end_date: datetime.datetime, created_date: datetime.datetime, created_by: str):
        self.account_rate_uid = account_rate_uid
        self.account_rate_name = account_rate_name
        self.tenant_uid = tenant_uid
        self.account_uid = account_uid
        self.currency_uid = currency_uid
        self.rate = rate
        self.start_date = start_date
        self.end_date = end_date
        self.created_date = created_date
        self.created_by = created_by


@dataclass(frozen=False)
class account_skill_normal_dto(base_read_dto, account_skill_write_dto):
    account_skill_uid: str
    account_skill_name: str
    account_skill_description: str
    created_date: datetime.datetime
    created_by: str
    def __init__(self, account_skill_uid: str, account_skill_name: str, account_skill_description: str, created_date: datetime.datetime, created_by: str):
        self.account_skill_uid = account_skill_uid
        self.account_skill_name = account_skill_name
        self.account_skill_description = account_skill_description
        self.created_date = created_date
        self.created_by = created_by


@dataclass(frozen=False)
class account_team_normal_dto(base_read_dto, account_team_write_dto):
    account_team_uid: str
    account_team_name: str
    tenant_uid: str
    owner_account_uid: str
    is_public: int
    is_tenant: int
    is_private: int
    created_date: datetime.datetime
    created_by: str
    def __init__(self, account_team_uid: str, account_team_name: str, tenant_uid: str, owner_account_uid: str, is_public: int, is_tenant: int, is_private: int, created_date: datetime.datetime, created_by: str):
        self.account_team_uid = account_team_uid
        self.account_team_name = account_team_name
        self.tenant_uid = tenant_uid
        self.owner_account_uid = owner_account_uid
        self.is_public = is_public
        self.is_tenant = is_tenant
        self.is_private = is_private
        self.created_date = created_date
        self.created_by = created_by


@dataclass(frozen=False)
class account_title_normal_dto(base_read_dto, account_title_write_dto):
    account_title_uid: str
    account_title_name: str
    title_description: str
    created_date: datetime.datetime
    created_by: str
    def __init__(self, account_title_uid: str, account_title_name: str, title_description: str, created_date: datetime.datetime, created_by: str):
        self.account_title_uid = account_title_uid
        self.account_title_name = account_title_name
        self.title_description = title_description
        self.created_date = created_date
        self.created_by = created_by


@dataclass(frozen=False)
class account_title_responsibility_normal_dto(base_read_dto, account_title_responsibility_write_dto):
    account_title_responsibility_uid: str
    account_title_responsibility_name: str
    tenant_uid: str
    account_title_uid: str
    responsibility_description: str
    responsibility_priority: int
    created_date: datetime.datetime
    created_by: str
    def __init__(self, account_title_responsibility_uid: str, account_title_responsibility_name: str, tenant_uid: str, account_title_uid: str, responsibility_description: str, responsibility_priority: int, created_date: datetime.datetime, created_by: str):
        self.account_title_responsibility_uid = account_title_responsibility_uid
        self.account_title_responsibility_name = account_title_responsibility_name
        self.tenant_uid = tenant_uid
        self.account_title_uid = account_title_uid
        self.responsibility_description = responsibility_description
        self.responsibility_priority = responsibility_priority
        self.created_date = created_date
        self.created_by = created_by


@dataclass(frozen=False)
class account_type_normal_dto(base_read_dto, account_type_write_dto):
    account_type_uid: str
    account_type_name: str
    account_type_description: str
    created_date: datetime.datetime
    created_by: str
    def __init__(self, account_type_uid: str, account_type_name: str, account_type_description: str, created_date: datetime.datetime, created_by: str):
        self.account_type_uid = account_type_uid
        self.account_type_name = account_type_name
        self.account_type_description = account_type_description
        self.created_date = created_date
        self.created_by = created_by


@dataclass(frozen=False)
class audit_change_normal_dto(base_read_dto, audit_change_write_dto):
    system_change_uid: str
    system_change_name: str
    account_uid: str
    audit_type_uid: str
    change_type: str
    change_json: str
    created_date: datetime.datetime
    created_by: str
    def __init__(self, system_change_uid: str, system_change_name: str, account_uid: str, audit_type_uid: str, change_type: str, change_json: str, created_date: datetime.datetime, created_by: str):
        self.system_change_uid = system_change_uid
        self.system_change_name = system_change_name
        self.account_uid = account_uid
        self.audit_type_uid = audit_type_uid
        self.change_type = change_type
        self.change_json = change_json
        self.created_date = created_date
        self.created_by = created_by


@dataclass(frozen=False)
class audit_type_normal_dto(base_read_dto, audit_type_write_dto):
    audit_type_uid: str
    audit_type_name: str
    created_date: datetime.datetime
    created_by: str
    def __init__(self, audit_type_uid: str, audit_type_name: str, created_date: datetime.datetime, created_by: str):
        self.audit_type_uid = audit_type_uid
        self.audit_type_name = audit_type_name
        self.created_date = created_date
        self.created_by = created_by


@dataclass(frozen=False)
class auth_attempt_normal_dto(base_read_dto, auth_attempt_write_dto):
    auth_attempt_uid: str
    auth_attempt_name: str
    tenant_uid: str | None
    account_uid: str | None
    account_login: str
    identity_type: str
    identity_parameters: str
    last_status_name: str
    created_date: datetime.datetime
    created_by: str
    def __init__(self, auth_attempt_uid: str, auth_attempt_name: str, tenant_uid: str | None, account_uid: str | None, account_login: str, identity_type: str, identity_parameters: str, last_status_name: str, created_date: datetime.datetime, created_by: str):
        self.auth_attempt_uid = auth_attempt_uid
        self.auth_attempt_name = auth_attempt_name
        self.tenant_uid = tenant_uid
        self.account_uid = account_uid
        self.account_login = account_login
        self.identity_type = identity_type
        self.identity_parameters = identity_parameters
        self.last_status_name = last_status_name
        self.created_date = created_date
        self.created_by = created_by


@dataclass(frozen=False)
class auth_identity_normal_dto(base_read_dto, auth_identity_write_dto):
    auth_identity_uid: str
    auth_identity_name: str
    class_name: str
    default_parameters_json: str
    created_date: datetime.datetime
    created_by: str
    def __init__(self, auth_identity_uid: str, auth_identity_name: str, class_name: str, default_parameters_json: str, created_date: datetime.datetime, created_by: str):
        self.auth_identity_uid = auth_identity_uid
        self.auth_identity_name = auth_identity_name
        self.class_name = class_name
        self.default_parameters_json = default_parameters_json
        self.created_date = created_date
        self.created_by = created_by


@dataclass(frozen=False)
class auth_identity_tenant_normal_dto(base_read_dto, auth_identity_tenant_write_dto):
    auth_identity_tenant_uid: str
    auth_identity_tenant_name: str
    tenant_uid: str
    auth_identity_uid: str
    auth_sso_uid: str | None
    identity_parameters_json: str
    last_status_name: str
    created_date: datetime.datetime
    created_by: str
    def __init__(self, auth_identity_tenant_uid: str, auth_identity_tenant_name: str, tenant_uid: str, auth_identity_uid: str, auth_sso_uid: str | None, identity_parameters_json: str, last_status_name: str, created_date: datetime.datetime, created_by: str):
        self.auth_identity_tenant_uid = auth_identity_tenant_uid
        self.auth_identity_tenant_name = auth_identity_tenant_name
        self.tenant_uid = tenant_uid
        self.auth_identity_uid = auth_identity_uid
        self.auth_sso_uid = auth_sso_uid
        self.identity_parameters_json = identity_parameters_json
        self.last_status_name = last_status_name
        self.created_date = created_date
        self.created_by = created_by


@dataclass(frozen=False)
class auth_key_normal_dto(base_read_dto, auth_key_write_dto):
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
    created_date: datetime.datetime
    created_by: str
    def __init__(self, auth_key_uid: str, auth_key_name: str, tenant_uid: str, owner_account_uid: str | None, auth_key_type_uid: str, key_private: str, key_public: str, key_length: int, key_exponent: str, key_modulus: str, key_parameters_json: str, created_date: datetime.datetime, created_by: str):
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
        self.created_date = created_date
        self.created_by = created_by


@dataclass(frozen=False)
class auth_key_type_normal_dto(base_read_dto, auth_key_type_write_dto):
    auth_key_type_uid: str
    auth_key_type_name: str
    class_name: str
    created_date: datetime.datetime
    created_by: str
    def __init__(self, auth_key_type_uid: str, auth_key_type_name: str, class_name: str, created_date: datetime.datetime, created_by: str):
        self.auth_key_type_uid = auth_key_type_uid
        self.auth_key_type_name = auth_key_type_name
        self.class_name = class_name
        self.created_date = created_date
        self.created_by = created_by


@dataclass(frozen=False)
class auth_password_normal_dto(base_read_dto, auth_password_write_dto):
    auth_password_uid: str
    auth_password_name: str
    tenant_uid: str
    account_uid: str
    password_hash: str
    password_salt: str
    date_from: datetime.datetime
    date_to: datetime.datetime
    usage_count: int
    created_date: datetime.datetime
    created_by: str
    def __init__(self, auth_password_uid: str, auth_password_name: str, tenant_uid: str, account_uid: str, password_hash: str, password_salt: str, date_from: datetime.datetime, date_to: datetime.datetime, usage_count: int, created_date: datetime.datetime, created_by: str):
        self.auth_password_uid = auth_password_uid
        self.auth_password_name = auth_password_name
        self.tenant_uid = tenant_uid
        self.account_uid = account_uid
        self.password_hash = password_hash
        self.password_salt = password_salt
        self.date_from = date_from
        self.date_to = date_to
        self.usage_count = usage_count
        self.created_date = created_date
        self.created_by = created_by


@dataclass(frozen=False)
class auth_password_current_normal_dto(base_read_dto, auth_password_current_write_dto):
    auth_password_current_uid: str
    auth_password_current_name: str
    tenant_uid: str
    account_uid: str
    password_hash: str
    password_salt: str
    date_from: datetime.datetime
    date_to: datetime.datetime
    usage_count: int
    created_date: datetime.datetime
    created_by: str
    def __init__(self, auth_password_current_uid: str, auth_password_current_name: str, tenant_uid: str, account_uid: str, password_hash: str, password_salt: str, date_from: datetime.datetime, date_to: datetime.datetime, usage_count: int, created_date: datetime.datetime, created_by: str):
        self.auth_password_current_uid = auth_password_current_uid
        self.auth_password_current_name = auth_password_current_name
        self.tenant_uid = tenant_uid
        self.account_uid = account_uid
        self.password_hash = password_hash
        self.password_salt = password_salt
        self.date_from = date_from
        self.date_to = date_to
        self.usage_count = usage_count
        self.created_date = created_date
        self.created_by = created_by


@dataclass(frozen=False)
class auth_password_rule_normal_dto(base_read_dto, auth_password_rule_write_dto):
    auth_password_uid: str
    auth_password_name: str
    rule_type: int
    rule_parameters: str
    user_scope: str
    created_date: datetime.datetime
    created_by: str
    def __init__(self, auth_password_uid: str, auth_password_name: str, rule_type: int, rule_parameters: str, user_scope: str, created_date: datetime.datetime, created_by: str):
        self.auth_password_uid = auth_password_uid
        self.auth_password_name = auth_password_name
        self.rule_type = rule_type
        self.rule_parameters = rule_parameters
        self.user_scope = user_scope
        self.created_date = created_date
        self.created_by = created_by


@dataclass(frozen=False)
class auth_permission_normal_dto(base_read_dto, auth_permission_write_dto):
    auth_permission_uid: str
    auth_permission_name: str
    tenant_uid: str
    account_uid: str
    auth_role_uid: str
    client_uid: str | None
    project_instance_uid: str | None
    valid_from_date: datetime.datetime
    valid_till_date: datetime.datetime
    created_date: datetime.datetime
    created_by: str
    def __init__(self, auth_permission_uid: str, auth_permission_name: str, tenant_uid: str, account_uid: str, auth_role_uid: str, client_uid: str | None, project_instance_uid: str | None, valid_from_date: datetime.datetime, valid_till_date: datetime.datetime, created_date: datetime.datetime, created_by: str):
        self.auth_permission_uid = auth_permission_uid
        self.auth_permission_name = auth_permission_name
        self.tenant_uid = tenant_uid
        self.account_uid = account_uid
        self.auth_role_uid = auth_role_uid
        self.client_uid = client_uid
        self.project_instance_uid = project_instance_uid
        self.valid_from_date = valid_from_date
        self.valid_till_date = valid_till_date
        self.created_date = created_date
        self.created_by = created_by


@dataclass(frozen=False)
class auth_request_normal_dto(base_read_dto, auth_request_write_dto):
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
    created_date: datetime.datetime
    created_by: str
    def __init__(self, auth_request_uid: str, auth_request_name: str, tenant_uid: str, account_uid: str, requestor_email: str, reset_guid: str, valid_till_date: datetime.datetime, lock_guid: str | None, lock_by: str | None, lock_date: datetime.datetime | None, is_checked: int, is_used: int, check_date: datetime.datetime | None, use_date: datetime.datetime | None, event_notification_uid: str | None, created_date: datetime.datetime, created_by: str):
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
        self.created_date = created_date
        self.created_by = created_by


@dataclass(frozen=False)
class auth_role_normal_dto(base_read_dto, auth_role_write_dto):
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
    created_date: datetime.datetime
    created_by: str
    def __init__(self, auth_role_uid: str, auth_role_name: str, parent_auth_role_uid: str | None, tenant_uid: str | None, role_description: str, access_uris: str, is_project: int, is_tenant: int, is_client: int, is_custom: int, created_date: datetime.datetime, created_by: str):
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
        self.created_date = created_date
        self.created_by = created_by


@dataclass(frozen=False)
class auth_role_uri_normal_dto(base_read_dto, auth_role_uri_write_dto):
    auth_role_uri_uid: str
    auth_role_uri_name: str
    auth_role_uid: str | None
    uri: str
    created_date: datetime.datetime
    created_by: str
    def __init__(self, auth_role_uri_uid: str, auth_role_uri_name: str, auth_role_uid: str | None, uri: str, created_date: datetime.datetime, created_by: str):
        self.auth_role_uri_uid = auth_role_uri_uid
        self.auth_role_uri_name = auth_role_uri_name
        self.auth_role_uid = auth_role_uid
        self.uri = uri
        self.created_date = created_date
        self.created_by = created_by


@dataclass(frozen=False)
class auth_session_normal_dto(base_read_dto, auth_session_write_dto):
    auth_session_uid: str
    auth_session_name: str
    tenant_uid: str | None
    account_uid: str | None
    session_token: str
    browser_name: str
    browser_: str
    created_date: datetime.datetime
    created_by: str
    def __init__(self, auth_session_uid: str, auth_session_name: str, tenant_uid: str | None, account_uid: str | None, session_token: str, browser_name: str, browser_: str, created_date: datetime.datetime, created_by: str):
        self.auth_session_uid = auth_session_uid
        self.auth_session_name = auth_session_name
        self.tenant_uid = tenant_uid
        self.account_uid = account_uid
        self.session_token = session_token
        self.browser_name = browser_name
        self.browser_ = browser_
        self.created_date = created_date
        self.created_by = created_by


@dataclass(frozen=False)
class auth_sso_normal_dto(base_read_dto, auth_sso_write_dto):
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
    created_date: datetime.datetime
    created_by: str
    def __init__(self, auth_sso_uid: str, auth_sso_name: str, tenant_uid: str, owner_account_uid: str | None, sso_name: str, sso_url: str, sso_key: str, sso_secret: str, sso_code: str | None, clientid: str | None, clientsecret: str | None, callback_url: str | None, created_date: datetime.datetime, created_by: str):
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
        self.created_date = created_date
        self.created_by = created_by


@dataclass(frozen=False)
class auth_token_normal_dto(base_read_dto, auth_token_write_dto):
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
    created_date: datetime.datetime
    created_by: str
    def __init__(self, auth_token_uid: str, auth_token_name: str, tenant_uid: str, account_uid: str, token_seq: int, token_hash: str, token_salt: str, valid_till_date: datetime.datetime | None, last_use_date: datetime.datetime | None, is_last: int, created_date: datetime.datetime, created_by: str):
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
        self.created_date = created_date
        self.created_by = created_by


@dataclass(frozen=False)
class calendar_account_normal_dto(base_read_dto, calendar_account_write_dto):
    calendar_account_uid: str
    calendar_account_name: str
    tenant_uid: str
    account_uid: str
    calendar_type_uid: str
    created_date: datetime.datetime
    created_by: str
    def __init__(self, calendar_account_uid: str, calendar_account_name: str, tenant_uid: str, account_uid: str, calendar_type_uid: str, created_date: datetime.datetime, created_by: str):
        self.calendar_account_uid = calendar_account_uid
        self.calendar_account_name = calendar_account_name
        self.tenant_uid = tenant_uid
        self.account_uid = account_uid
        self.calendar_type_uid = calendar_type_uid
        self.created_date = created_date
        self.created_by = created_by


@dataclass(frozen=False)
class calendar_approval_normal_dto(base_read_dto, calendar_approval_write_dto):
    calendar_approval_uid: str
    calendar_approval_name: str
    client_uid: str
    account_uid: str
    calendar_approval_type_uid: str
    calendar_event_group_uid: str
    calendar_type_uid: str
    time_submit_type_name: str
    created_date: datetime.datetime
    created_by: str
    def __init__(self, calendar_approval_uid: str, calendar_approval_name: str, client_uid: str, account_uid: str, calendar_approval_type_uid: str, calendar_event_group_uid: str, calendar_type_uid: str, time_submit_type_name: str, created_date: datetime.datetime, created_by: str):
        self.calendar_approval_uid = calendar_approval_uid
        self.calendar_approval_name = calendar_approval_name
        self.client_uid = client_uid
        self.account_uid = account_uid
        self.calendar_approval_type_uid = calendar_approval_type_uid
        self.calendar_event_group_uid = calendar_event_group_uid
        self.calendar_type_uid = calendar_type_uid
        self.time_submit_type_name = time_submit_type_name
        self.created_date = created_date
        self.created_by = created_by


@dataclass(frozen=False)
class calendar_approval_type_normal_dto(base_read_dto, calendar_approval_type_write_dto):
    calendar_approval_type_uid: str
    calendar_approval_type_name: str
    created_date: datetime.datetime
    created_by: str
    def __init__(self, calendar_approval_type_uid: str, calendar_approval_type_name: str, created_date: datetime.datetime, created_by: str):
        self.calendar_approval_type_uid = calendar_approval_type_uid
        self.calendar_approval_type_name = calendar_approval_type_name
        self.created_date = created_date
        self.created_by = created_by


@dataclass(frozen=False)
class calendar_event_normal_dto(base_read_dto, calendar_event_write_dto):
    calendar_event_uid: str
    calendar_event_name: str
    client_uid: str
    account_uid: str
    calendar_event_group_uid: str
    calendar_type_uid: str
    created_date: datetime.datetime
    created_by: str
    def __init__(self, calendar_event_uid: str, calendar_event_name: str, client_uid: str, account_uid: str, calendar_event_group_uid: str, calendar_type_uid: str, created_date: datetime.datetime, created_by: str):
        self.calendar_event_uid = calendar_event_uid
        self.calendar_event_name = calendar_event_name
        self.client_uid = client_uid
        self.account_uid = account_uid
        self.calendar_event_group_uid = calendar_event_group_uid
        self.calendar_type_uid = calendar_type_uid
        self.created_date = created_date
        self.created_by = created_by


@dataclass(frozen=False)
class calendar_event_group_normal_dto(base_read_dto, calendar_event_group_write_dto):
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
    created_date: datetime.datetime
    created_by: str
    def __init__(self, calendar_event_group_uid: str, calendar_event_group_name: str, client_uid: str, account_uid: str, calendar_account_uid: str, calendar_event_type_uid: str, group_comment: str, event_start_date: datetime.datetime, event_end_date: datetime.datetime, is_approved: int, created_date: datetime.datetime, created_by: str):
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
        self.created_date = created_date
        self.created_by = created_by


@dataclass(frozen=False)
class calendar_event_type_normal_dto(base_read_dto, calendar_event_type_write_dto):
    calendar_event_type_uid: str
    calendar_event_type_name: str
    client_uid: str
    calendar_type_uid: str
    auto_approved: int
    created_date: datetime.datetime
    created_by: str
    def __init__(self, calendar_event_type_uid: str, calendar_event_type_name: str, client_uid: str, calendar_type_uid: str, auto_approved: int, created_date: datetime.datetime, created_by: str):
        self.calendar_event_type_uid = calendar_event_type_uid
        self.calendar_event_type_name = calendar_event_type_name
        self.client_uid = client_uid
        self.calendar_type_uid = calendar_type_uid
        self.auto_approved = auto_approved
        self.created_date = created_date
        self.created_by = created_by


@dataclass(frozen=False)
class calendar_type_normal_dto(base_read_dto, calendar_type_write_dto):
    calendar_type_uid: str
    calendar_type_name: str
    created_date: datetime.datetime
    created_by: str
    def __init__(self, calendar_type_uid: str, calendar_type_name: str, created_date: datetime.datetime, created_by: str):
        self.calendar_type_uid = calendar_type_uid
        self.calendar_type_name = calendar_type_name
        self.created_date = created_date
        self.created_by = created_by


@dataclass(frozen=False)
class client_normal_dto(base_read_dto, client_write_dto):
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
    created_date: datetime.datetime
    created_by: str
    def __init__(self, client_uid: str, client_name: str, tenant_uid: str, country_uid: str, client_type_uid: str, client_category_uid: str, account_uid: str | None, client_code: str, client_description: str, start_date: datetime.datetime, end_date: datetime.datetime | None, is_internal: int, is_system: int, is_test: int, created_date: datetime.datetime, created_by: str):
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
        self.created_date = created_date
        self.created_by = created_by


@dataclass(frozen=False)
class client_account_normal_dto(base_read_dto, client_account_write_dto):
    client_account_uid: str
    client_account_name: str
    tenant_uid: str
    client_uid: str
    account_uid: str
    client_role_uid: str
    created_date: datetime.datetime
    created_by: str
    def __init__(self, client_account_uid: str, client_account_name: str, tenant_uid: str, client_uid: str, account_uid: str, client_role_uid: str, created_date: datetime.datetime, created_by: str):
        self.client_account_uid = client_account_uid
        self.client_account_name = client_account_name
        self.tenant_uid = tenant_uid
        self.client_uid = client_uid
        self.account_uid = account_uid
        self.client_role_uid = client_role_uid
        self.created_date = created_date
        self.created_by = created_by


@dataclass(frozen=False)
class client_country_normal_dto(base_read_dto, client_country_write_dto):
    client_country_uid: str
    client_country_name: str
    tenant_uid: str
    client_uid: str
    country_uid: str
    created_date: datetime.datetime
    created_by: str
    def __init__(self, client_country_uid: str, client_country_name: str, tenant_uid: str, client_uid: str, country_uid: str, created_date: datetime.datetime, created_by: str):
        self.client_country_uid = client_country_uid
        self.client_country_name = client_country_name
        self.tenant_uid = tenant_uid
        self.client_uid = client_uid
        self.country_uid = country_uid
        self.created_date = created_date
        self.created_by = created_by


@dataclass(frozen=False)
class client_payment_normal_dto(base_read_dto, client_payment_write_dto):
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
    created_date: datetime.datetime
    created_by: str
    def __init__(self, client_payment_uid: str, client_payment_name: str, tenant_uid: str, client_uid: str, account_uid: str, currency_uid: str, start_date: datetime.datetime, end_date: datetime.datetime | None, payment_value: str, payment_type: str, source_number: str, source_reference: str, is_approved: int, created_date: datetime.datetime, created_by: str):
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
        self.created_date = created_date
        self.created_by = created_by


@dataclass(frozen=False)
class client_role_normal_dto(base_read_dto, client_role_write_dto):
    client_role_uid: str
    client_role_name: str
    role_description: str
    created_date: datetime.datetime
    created_by: str
    def __init__(self, client_role_uid: str, client_role_name: str, role_description: str, created_date: datetime.datetime, created_by: str):
        self.client_role_uid = client_role_uid
        self.client_role_name = client_role_name
        self.role_description = role_description
        self.created_date = created_date
        self.created_by = created_by


@dataclass(frozen=False)
class client_status_normal_dto(base_read_dto, client_status_write_dto):
    client_status_uid: str
    client_status_name: str
    client_status_description: str
    created_date: datetime.datetime
    created_by: str
    def __init__(self, client_status_uid: str, client_status_name: str, client_status_description: str, created_date: datetime.datetime, created_by: str):
        self.client_status_uid = client_status_uid
        self.client_status_name = client_status_name
        self.client_status_description = client_status_description
        self.created_date = created_date
        self.created_by = created_by


@dataclass(frozen=False)
class client_type_normal_dto(base_read_dto, client_type_write_dto):
    client_type_uid: str
    client_type_name: str
    client_type_description: str
    created_date: datetime.datetime
    created_by: str
    def __init__(self, client_type_uid: str, client_type_name: str, client_type_description: str, created_date: datetime.datetime, created_by: str):
        self.client_type_uid = client_type_uid
        self.client_type_name = client_type_name
        self.client_type_description = client_type_description
        self.created_date = created_date
        self.created_by = created_by


@dataclass(frozen=False)
class connection_engine_normal_dto(base_read_dto, connection_engine_write_dto):
    connection_engine_uid: str
    connection_engine_name: str
    start_date: datetime.datetime | None
    calls_count: int
    last_time: int
    host_count: int
    user_count: int
    token_count: int
    created_date: datetime.datetime
    created_by: str
    def __init__(self, connection_engine_uid: str, connection_engine_name: str, start_date: datetime.datetime | None, calls_count: int, last_time: int, host_count: int, user_count: int, token_count: int, created_date: datetime.datetime, created_by: str):
        self.connection_engine_uid = connection_engine_uid
        self.connection_engine_name = connection_engine_name
        self.start_date = start_date
        self.calls_count = calls_count
        self.last_time = last_time
        self.host_count = host_count
        self.user_count = user_count
        self.token_count = token_count
        self.created_date = created_date
        self.created_by = created_by


@dataclass(frozen=False)
class connection_host_normal_dto(base_read_dto, connection_host_write_dto):
    connection_host_uid: str
    connection_host_name: str
    connection_engine_uid: str
    host_ip: str
    calls_count: int | None
    start_time: int
    last_call_time: int
    user_count: int
    token_count: int
    created_date: datetime.datetime
    created_by: str
    def __init__(self, connection_host_uid: str, connection_host_name: str, connection_engine_uid: str, host_ip: str, calls_count: int | None, start_time: int, last_call_time: int, user_count: int, token_count: int, created_date: datetime.datetime, created_by: str):
        self.connection_host_uid = connection_host_uid
        self.connection_host_name = connection_host_name
        self.connection_engine_uid = connection_engine_uid
        self.host_ip = host_ip
        self.calls_count = calls_count
        self.start_time = start_time
        self.last_call_time = last_call_time
        self.user_count = user_count
        self.token_count = token_count
        self.created_date = created_date
        self.created_by = created_by


@dataclass(frozen=False)
class connection_user_normal_dto(base_read_dto, connection_user_write_dto):
    connection_user_uid: str
    connection_user_name: str
    connection_engine_uid: str
    account_uid: str
    call_count: int
    host_count: int
    token_count: int
    created_date: datetime.datetime
    created_by: str
    def __init__(self, connection_user_uid: str, connection_user_name: str, connection_engine_uid: str, account_uid: str, call_count: int, host_count: int, token_count: int, created_date: datetime.datetime, created_by: str):
        self.connection_user_uid = connection_user_uid
        self.connection_user_name = connection_user_name
        self.connection_engine_uid = connection_engine_uid
        self.account_uid = account_uid
        self.call_count = call_count
        self.host_count = host_count
        self.token_count = token_count
        self.created_date = created_date
        self.created_by = created_by


@dataclass(frozen=False)
class country_normal_dto(base_read_dto, country_write_dto):
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
    created_date: datetime.datetime
    created_by: str
    def __init__(self, country_uid: str, country_name: str, continent_name: str, continent_code: str, country_iso3: str, country_code: str, phone_code: str, currency_code: str, capital_name: str, region_name: str, subregion_name: str, region_code: str, latitude: str, longitude: str, currency_name: str, population: str, languages: str, area: str, bar_code: str, top_level_domain: str, is_focused: int, created_date: datetime.datetime, created_by: str):
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
        self.created_date = created_date
        self.created_by = created_by


@dataclass(frozen=False)
class currency_normal_dto(base_read_dto, currency_write_dto):
    currency_uid: str
    currency_name: str
    is_focused: int
    created_date: datetime.datetime
    created_by: str
    def __init__(self, currency_uid: str, currency_name: str, is_focused: int, created_date: datetime.datetime, created_by: str):
        self.currency_uid = currency_uid
        self.currency_name = currency_name
        self.is_focused = is_focused
        self.created_date = created_date
        self.created_by = created_by


@dataclass(frozen=False)
class event_acknowledge_normal_dto(base_read_dto, event_acknowledge_write_dto):
    event_acknowledge_uid: str
    event_acknowledge_name: str
    event_notification_uid: str
    tenant_uid: str
    account_uid: str
    created_date: datetime.datetime
    created_by: str
    def __init__(self, event_acknowledge_uid: str, event_acknowledge_name: str, event_notification_uid: str, tenant_uid: str, account_uid: str, created_date: datetime.datetime, created_by: str):
        self.event_acknowledge_uid = event_acknowledge_uid
        self.event_acknowledge_name = event_acknowledge_name
        self.event_notification_uid = event_notification_uid
        self.tenant_uid = tenant_uid
        self.account_uid = account_uid
        self.created_date = created_date
        self.created_by = created_by


@dataclass(frozen=False)
class event_channel_normal_dto(base_read_dto, event_channel_write_dto):
    event_channel_uid: str
    event_channel_name: str
    event_channel_type_uid: str
    channel_definition: str
    last_status_name: str
    tenant_uid: str
    account_uid: str
    created_date: datetime.datetime
    created_by: str
    def __init__(self, event_channel_uid: str, event_channel_name: str, event_channel_type_uid: str, channel_definition: str, last_status_name: str, tenant_uid: str, account_uid: str, created_date: datetime.datetime, created_by: str):
        self.event_channel_uid = event_channel_uid
        self.event_channel_name = event_channel_name
        self.event_channel_type_uid = event_channel_type_uid
        self.channel_definition = channel_definition
        self.last_status_name = last_status_name
        self.tenant_uid = tenant_uid
        self.account_uid = account_uid
        self.created_date = created_date
        self.created_by = created_by


@dataclass(frozen=False)
class event_channel_type_normal_dto(base_read_dto, event_channel_type_write_dto):
    event_channel_type_uid: str
    event_channel_type_name: str
    channel_type_description: str
    created_date: datetime.datetime
    created_by: str
    def __init__(self, event_channel_type_uid: str, event_channel_type_name: str, channel_type_description: str, created_date: datetime.datetime, created_by: str):
        self.event_channel_type_uid = event_channel_type_uid
        self.event_channel_type_name = event_channel_type_name
        self.channel_type_description = channel_type_description
        self.created_date = created_date
        self.created_by = created_by


@dataclass(frozen=False)
class event_instance_normal_dto(base_read_dto, event_instance_write_dto):
    event_instance_uid: str
    event_instance_name: str
    client_uid: str
    event_type: str
    event_object: str
    event_method: str
    event_parameters: str
    event_signature: str
    event_date: datetime.datetime
    published_count: int
    created_date: datetime.datetime
    created_by: str
    def __init__(self, event_instance_uid: str, event_instance_name: str, client_uid: str, event_type: str, event_object: str, event_method: str, event_parameters: str, event_signature: str, event_date: datetime.datetime, published_count: int, created_date: datetime.datetime, created_by: str):
        self.event_instance_uid = event_instance_uid
        self.event_instance_name = event_instance_name
        self.client_uid = client_uid
        self.event_type = event_type
        self.event_object = event_object
        self.event_method = event_method
        self.event_parameters = event_parameters
        self.event_signature = event_signature
        self.event_date = event_date
        self.published_count = published_count
        self.created_date = created_date
        self.created_by = created_by


@dataclass(frozen=False)
class event_notification_normal_dto(base_read_dto, event_notification_write_dto):
    event_notification_uid: str
    event_notification_name: str
    tenant_uid: str
    account_uid: str
    notification_type: str
    notification_topic: str
    notification_format: str
    notification_content: str
    sending_status: str
    created_date: datetime.datetime
    created_by: str
    def __init__(self, event_notification_uid: str, event_notification_name: str, tenant_uid: str, account_uid: str, notification_type: str, notification_topic: str, notification_format: str, notification_content: str, sending_status: str, created_date: datetime.datetime, created_by: str):
        self.event_notification_uid = event_notification_uid
        self.event_notification_name = event_notification_name
        self.tenant_uid = tenant_uid
        self.account_uid = account_uid
        self.notification_type = notification_type
        self.notification_topic = notification_topic
        self.notification_format = notification_format
        self.notification_content = notification_content
        self.sending_status = sending_status
        self.created_date = created_date
        self.created_by = created_by


@dataclass(frozen=False)
class event_observer_normal_dto(base_read_dto, event_observer_write_dto):
    event_observer_uid: str
    event_observer_name: str
    event_observer_definition: str
    created_date: datetime.datetime
    created_by: str
    def __init__(self, event_observer_uid: str, event_observer_name: str, event_observer_definition: str, created_date: datetime.datetime, created_by: str):
        self.event_observer_uid = event_observer_uid
        self.event_observer_name = event_observer_name
        self.event_observer_definition = event_observer_definition
        self.created_date = created_date
        self.created_by = created_by


@dataclass(frozen=False)
class event_subscription_normal_dto(base_read_dto, event_subscription_write_dto):
    event_subscription_uid: str
    event_subscription_name: str
    event_channel_uid: str
    tenant_uid: str
    account_uid: str
    subscription_filter: str
    subscription_topic: str
    subscription_template: str
    created_date: datetime.datetime
    created_by: str
    def __init__(self, event_subscription_uid: str, event_subscription_name: str, event_channel_uid: str, tenant_uid: str, account_uid: str, subscription_filter: str, subscription_topic: str, subscription_template: str, created_date: datetime.datetime, created_by: str):
        self.event_subscription_uid = event_subscription_uid
        self.event_subscription_name = event_subscription_name
        self.event_channel_uid = event_channel_uid
        self.tenant_uid = tenant_uid
        self.account_uid = account_uid
        self.subscription_filter = subscription_filter
        self.subscription_topic = subscription_topic
        self.subscription_template = subscription_template
        self.created_date = created_date
        self.created_by = created_by


@dataclass(frozen=False)
class event_template_normal_dto(base_read_dto, event_template_write_dto):
    event_template_uid: str
    event_template_name: str
    tenant_uid: str
    notification_type: str
    notification_topic: str
    notification_format: str
    created_date: datetime.datetime
    created_by: str
    def __init__(self, event_template_uid: str, event_template_name: str, tenant_uid: str, notification_type: str, notification_topic: str, notification_format: str, created_date: datetime.datetime, created_by: str):
        self.event_template_uid = event_template_uid
        self.event_template_name = event_template_name
        self.tenant_uid = tenant_uid
        self.notification_type = notification_type
        self.notification_topic = notification_topic
        self.notification_format = notification_format
        self.created_date = created_date
        self.created_by = created_by


@dataclass(frozen=False)
class event_type_normal_dto(base_read_dto, event_type_write_dto):
    event_type_uid: str
    event_type_name: str
    event_type_description: str
    created_date: datetime.datetime
    created_by: str
    def __init__(self, event_type_uid: str, event_type_name: str, event_type_description: str, created_date: datetime.datetime, created_by: str):
        self.event_type_uid = event_type_uid
        self.event_type_name = event_type_name
        self.event_type_description = event_type_description
        self.created_date = created_date
        self.created_by = created_by


@dataclass(frozen=False)
class invoice_action_normal_dto(base_read_dto, invoice_action_write_dto):
    invoice_action_uid: str
    invoice_action_name: str
    tenant_uid: str
    account_uid: str
    invoice_instance_uid: str
    invoice_action_type_uid: str
    created_date: datetime.datetime
    created_by: str
    def __init__(self, invoice_action_uid: str, invoice_action_name: str, tenant_uid: str, account_uid: str, invoice_instance_uid: str, invoice_action_type_uid: str, created_date: datetime.datetime, created_by: str):
        self.invoice_action_uid = invoice_action_uid
        self.invoice_action_name = invoice_action_name
        self.tenant_uid = tenant_uid
        self.account_uid = account_uid
        self.invoice_instance_uid = invoice_instance_uid
        self.invoice_action_type_uid = invoice_action_type_uid
        self.created_date = created_date
        self.created_by = created_by


@dataclass(frozen=False)
class invoice_action_type_normal_dto(base_read_dto, invoice_action_type_write_dto):
    invoice_action_type_uid: str
    invoice_action_type_name: str
    created_date: datetime.datetime
    created_by: str
    def __init__(self, invoice_action_type_uid: str, invoice_action_type_name: str, created_date: datetime.datetime, created_by: str):
        self.invoice_action_type_uid = invoice_action_type_uid
        self.invoice_action_type_name = invoice_action_type_name
        self.created_date = created_date
        self.created_by = created_by


@dataclass(frozen=False)
class invoice_category_normal_dto(base_read_dto, invoice_category_write_dto):
    invoice_category_uid: str
    invoice_category_name: str
    tenant_uid: str
    invoice_category_description: str
    created_date: datetime.datetime
    created_by: str
    def __init__(self, invoice_category_uid: str, invoice_category_name: str, tenant_uid: str, invoice_category_description: str, created_date: datetime.datetime, created_by: str):
        self.invoice_category_uid = invoice_category_uid
        self.invoice_category_name = invoice_category_name
        self.tenant_uid = tenant_uid
        self.invoice_category_description = invoice_category_description
        self.created_date = created_date
        self.created_by = created_by


@dataclass(frozen=False)
class invoice_entry_normal_dto(base_read_dto, invoice_entry_write_dto):
    invoice_entry_uid: str
    invoice_entry_name: str
    tenant_uid: str
    account_uid: str
    invoice_instance_uid: str
    entry_details: str
    entry_amount_net: str
    entry_amount_tax: str
    entry_amount_gross: str
    created_date: datetime.datetime
    created_by: str
    def __init__(self, invoice_entry_uid: str, invoice_entry_name: str, tenant_uid: str, account_uid: str, invoice_instance_uid: str, entry_details: str, entry_amount_net: str, entry_amount_tax: str, entry_amount_gross: str, created_date: datetime.datetime, created_by: str):
        self.invoice_entry_uid = invoice_entry_uid
        self.invoice_entry_name = invoice_entry_name
        self.tenant_uid = tenant_uid
        self.account_uid = account_uid
        self.invoice_instance_uid = invoice_instance_uid
        self.entry_details = entry_details
        self.entry_amount_net = entry_amount_net
        self.entry_amount_tax = entry_amount_tax
        self.entry_amount_gross = entry_amount_gross
        self.created_date = created_date
        self.created_by = created_by


@dataclass(frozen=False)
class invoice_flow_normal_dto(base_read_dto, invoice_flow_write_dto):
    invoice_flow_uid: str
    invoice_flow_name: str
    flow_description: str
    flow_definition_json: str
    created_date: datetime.datetime
    created_by: str
    def __init__(self, invoice_flow_uid: str, invoice_flow_name: str, flow_description: str, flow_definition_json: str, created_date: datetime.datetime, created_by: str):
        self.invoice_flow_uid = invoice_flow_uid
        self.invoice_flow_name = invoice_flow_name
        self.flow_description = flow_description
        self.flow_definition_json = flow_definition_json
        self.created_date = created_date
        self.created_by = created_by


@dataclass(frozen=False)
class invoice_flow_state_normal_dto(base_read_dto, invoice_flow_state_write_dto):
    invoice_flow_state_uid: str
    invoice_flow_state_name: str
    invoice_flow_uid: str
    created_date: datetime.datetime
    created_by: str
    def __init__(self, invoice_flow_state_uid: str, invoice_flow_state_name: str, invoice_flow_uid: str, created_date: datetime.datetime, created_by: str):
        self.invoice_flow_state_uid = invoice_flow_state_uid
        self.invoice_flow_state_name = invoice_flow_state_name
        self.invoice_flow_uid = invoice_flow_uid
        self.created_date = created_date
        self.created_by = created_by


@dataclass(frozen=False)
class invoice_instance_normal_dto(base_read_dto, invoice_instance_write_dto):
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
    created_date: datetime.datetime
    created_by: str
    def __init__(self, invoice_instance_uid: str, invoice_instance_name: str, tenant_uid: str, account_uid: str, invoice_flow_uid: str, invoice_status_uid: str, invoice_category_uid: str, invoice_type_uid: str, period_uid: str, currency_uid: str, invoice_number: str, invoice_details: str, invoice_amount_net: str, invoice_amount_tax: str, invoice_amount_gross: str, created_date: datetime.datetime, created_by: str):
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
        self.created_date = created_date
        self.created_by = created_by


@dataclass(frozen=False)
class invoice_status_normal_dto(base_read_dto, invoice_status_write_dto):
    invoice_status_uid: str
    invoice_status_name: str
    status_description: str
    created_date: datetime.datetime
    created_by: str
    def __init__(self, invoice_status_uid: str, invoice_status_name: str, status_description: str, created_date: datetime.datetime, created_by: str):
        self.invoice_status_uid = invoice_status_uid
        self.invoice_status_name = invoice_status_name
        self.status_description = status_description
        self.created_date = created_date
        self.created_by = created_by


@dataclass(frozen=False)
class invoice_type_normal_dto(base_read_dto, invoice_type_write_dto):
    invoice_type_uid: str
    invoice_type_name: str
    created_date: datetime.datetime
    created_by: str
    def __init__(self, invoice_type_uid: str, invoice_type_name: str, created_date: datetime.datetime, created_by: str):
        self.invoice_type_uid = invoice_type_uid
        self.invoice_type_name = invoice_type_name
        self.created_date = created_date
        self.created_by = created_by


@dataclass(frozen=False)
class monitor_normal_dto(base_read_dto, monitor_write_dto):
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
    created_date: datetime.datetime
    created_by: str
    def __init__(self, monitor_uid: str, monitor_name: str, tenant_uid: str, account_uid: str, monitor_type_uid: str, schedule_expression: str, monitor_protocol: str, monitor_url: str, monitor_user: str, monitor_priority: int, is_on_hold: int, last_status_name: str, last_run_time: str, last_exception_message: str, created_date: datetime.datetime, created_by: str):
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
        self.created_date = created_date
        self.created_by = created_by


@dataclass(frozen=False)
class monitor_run_normal_dto(base_read_dto, monitor_run_write_dto):
    monitor_run_uid: str
    monitor_run_name: str
    tenant_uid: str
    account_uid: str
    monitor_uid: str
    status_name: str
    run_time: str
    exception_message: str
    created_date: datetime.datetime
    created_by: str
    def __init__(self, monitor_run_uid: str, monitor_run_name: str, tenant_uid: str, account_uid: str, monitor_uid: str, status_name: str, run_time: str, exception_message: str, created_date: datetime.datetime, created_by: str):
        self.monitor_run_uid = monitor_run_uid
        self.monitor_run_name = monitor_run_name
        self.tenant_uid = tenant_uid
        self.account_uid = account_uid
        self.monitor_uid = monitor_uid
        self.status_name = status_name
        self.run_time = run_time
        self.exception_message = exception_message
        self.created_date = created_date
        self.created_by = created_by


@dataclass(frozen=False)
class monitor_type_normal_dto(base_read_dto, monitor_type_write_dto):
    monitor_type_uid: str
    monitor_type_name: str
    class_name: str
    parameters_json: str
    created_date: datetime.datetime
    created_by: str
    def __init__(self, monitor_type_uid: str, monitor_type_name: str, class_name: str, parameters_json: str, created_date: datetime.datetime, created_by: str):
        self.monitor_type_uid = monitor_type_uid
        self.monitor_type_name = monitor_type_name
        self.class_name = class_name
        self.parameters_json = parameters_json
        self.created_date = created_date
        self.created_by = created_by


@dataclass(frozen=False)
class period_normal_dto(base_read_dto, period_write_dto):
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
    created_date: datetime.datetime
    created_by: str
    def __init__(self, period_uid: str, period_name: str, period_number: int, period_type: str, period_start_time: datetime.datetime, period_end_time: datetime.datetime, period_year: int | None, period_quarter: int | None, period_month: int | None, period_week: int | None, period_day: int | None, created_date: datetime.datetime, created_by: str):
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
        self.created_date = created_date
        self.created_by = created_by


@dataclass(frozen=False)
class process_normal_dto(base_read_dto, process_write_dto):
    process_uid: str
    process_name: str
    tenant_uid: str
    account_uid: str
    process_type_uid: str
    created_date: datetime.datetime
    created_by: str
    def __init__(self, process_uid: str, process_name: str, tenant_uid: str, account_uid: str, process_type_uid: str, created_date: datetime.datetime, created_by: str):
        self.process_uid = process_uid
        self.process_name = process_name
        self.tenant_uid = tenant_uid
        self.account_uid = account_uid
        self.process_type_uid = process_type_uid
        self.created_date = created_date
        self.created_by = created_by


@dataclass(frozen=False)
class process_run_normal_dto(base_read_dto, process_run_write_dto):
    process_run_uid: str
    process_run_name: str
    tenant_uid: str
    account_uid: str
    process_uid: str
    created_date: datetime.datetime
    created_by: str
    def __init__(self, process_run_uid: str, process_run_name: str, tenant_uid: str, account_uid: str, process_uid: str, created_date: datetime.datetime, created_by: str):
        self.process_run_uid = process_run_uid
        self.process_run_name = process_run_name
        self.tenant_uid = tenant_uid
        self.account_uid = account_uid
        self.process_uid = process_uid
        self.created_date = created_date
        self.created_by = created_by


@dataclass(frozen=False)
class process_type_normal_dto(base_read_dto, process_type_write_dto):
    process_type_uid: str
    process_type_name: str
    class_name: str
    created_date: datetime.datetime
    created_by: str
    def __init__(self, process_type_uid: str, process_type_name: str, class_name: str, created_date: datetime.datetime, created_by: str):
        self.process_type_uid = process_type_uid
        self.process_type_name = process_type_name
        self.class_name = class_name
        self.created_date = created_date
        self.created_by = created_by


@dataclass(frozen=False)
class project_account_normal_dto(base_read_dto, project_account_write_dto):
    project_account_uid: str
    project_account_name: str
    tenant_uid: str
    client_uid: str
    account_uid: str
    project_instance_uid: str
    start_date: datetime.datetime | None
    end_date: datetime.datetime | None
    created_date: datetime.datetime
    created_by: str
    def __init__(self, project_account_uid: str, project_account_name: str, tenant_uid: str, client_uid: str, account_uid: str, project_instance_uid: str, start_date: datetime.datetime | None, end_date: datetime.datetime | None, created_date: datetime.datetime, created_by: str):
        self.project_account_uid = project_account_uid
        self.project_account_name = project_account_name
        self.tenant_uid = tenant_uid
        self.client_uid = client_uid
        self.account_uid = account_uid
        self.project_instance_uid = project_instance_uid
        self.start_date = start_date
        self.end_date = end_date
        self.created_date = created_date
        self.created_by = created_by


@dataclass(frozen=False)
class project_budget_normal_dto(base_read_dto, project_budget_write_dto):
    project_budget_uid: str
    project_budget_name: str
    tenant_uid: str
    client_uid: str
    project_instance_uid: str
    currency_uid: str
    budget_value: str
    is_approved: int
    is_current: int
    created_date: datetime.datetime
    created_by: str
    def __init__(self, project_budget_uid: str, project_budget_name: str, tenant_uid: str, client_uid: str, project_instance_uid: str, currency_uid: str, budget_value: str, is_approved: int, is_current: int, created_date: datetime.datetime, created_by: str):
        self.project_budget_uid = project_budget_uid
        self.project_budget_name = project_budget_name
        self.tenant_uid = tenant_uid
        self.client_uid = client_uid
        self.project_instance_uid = project_instance_uid
        self.currency_uid = currency_uid
        self.budget_value = budget_value
        self.is_approved = is_approved
        self.is_current = is_current
        self.created_date = created_date
        self.created_by = created_by


@dataclass(frozen=False)
class project_group_normal_dto(base_read_dto, project_group_write_dto):
    project_group_uid: str
    project_group_name: str
    tenant_uid: str
    project_group_description: str
    created_date: datetime.datetime
    created_by: str
    def __init__(self, project_group_uid: str, project_group_name: str, tenant_uid: str, project_group_description: str, created_date: datetime.datetime, created_by: str):
        self.project_group_uid = project_group_uid
        self.project_group_name = project_group_name
        self.tenant_uid = tenant_uid
        self.project_group_description = project_group_description
        self.created_date = created_date
        self.created_by = created_by


@dataclass(frozen=False)
class project_instance_normal_dto(base_read_dto, project_instance_write_dto):
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
    created_date: datetime.datetime
    created_by: str
    def __init__(self, project_instance_uid: str, project_instance_name: str, tenant_uid: str, client_uid: str, project_type_uid: str, manager_account_uid: str, project_group_uid: str, project_code: str, project_description: str, is_billable: int, start_date: datetime.datetime | None, end_date: datetime.datetime | None, current_billed: str, budget: str, created_date: datetime.datetime, created_by: str):
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
        self.created_date = created_date
        self.created_by = created_by


@dataclass(frozen=False)
class project_milestone_normal_dto(base_read_dto, project_milestone_write_dto):
    project_milestone_uid: str
    project_milestone_name: str
    tenant_uid: str
    client_uid: str
    project_instance_uid: str
    project_budget_uid: str | None
    start_date: datetime.datetime
    end_date: datetime.datetime
    status_name: str
    created_date: datetime.datetime
    created_by: str
    def __init__(self, project_milestone_uid: str, project_milestone_name: str, tenant_uid: str, client_uid: str, project_instance_uid: str, project_budget_uid: str | None, start_date: datetime.datetime, end_date: datetime.datetime, status_name: str, created_date: datetime.datetime, created_by: str):
        self.project_milestone_uid = project_milestone_uid
        self.project_milestone_name = project_milestone_name
        self.tenant_uid = tenant_uid
        self.client_uid = client_uid
        self.project_instance_uid = project_instance_uid
        self.project_budget_uid = project_budget_uid
        self.start_date = start_date
        self.end_date = end_date
        self.status_name = status_name
        self.created_date = created_date
        self.created_by = created_by


@dataclass(frozen=False)
class project_type_normal_dto(base_read_dto, project_type_write_dto):
    project_type_uid: str
    project_type_name: str
    project_type_description: str
    created_date: datetime.datetime
    created_by: str
    def __init__(self, project_type_uid: str, project_type_name: str, project_type_description: str, created_date: datetime.datetime, created_by: str):
        self.project_type_uid = project_type_uid
        self.project_type_name = project_type_name
        self.project_type_description = project_type_description
        self.created_date = created_date
        self.created_by = created_by


@dataclass(frozen=False)
class report_normal_dto(base_read_dto, report_write_dto):
    report_uid: str
    report_name: str
    tenant_uid: str
    account_uid: str
    report_status_uid: str
    report_query: str
    report_parameters: str
    created_date: datetime.datetime
    created_by: str
    def __init__(self, report_uid: str, report_name: str, tenant_uid: str, account_uid: str, report_status_uid: str, report_query: str, report_parameters: str, created_date: datetime.datetime, created_by: str):
        self.report_uid = report_uid
        self.report_name = report_name
        self.tenant_uid = tenant_uid
        self.account_uid = account_uid
        self.report_status_uid = report_status_uid
        self.report_query = report_query
        self.report_parameters = report_parameters
        self.created_date = created_date
        self.created_by = created_by


@dataclass(frozen=False)
class report_content_type_normal_dto(base_read_dto, report_content_type_write_dto):
    report_content_type_uid: str
    report_content_type_name: str
    created_date: datetime.datetime
    created_by: str
    def __init__(self, report_content_type_uid: str, report_content_type_name: str, created_date: datetime.datetime, created_by: str):
        self.report_content_type_uid = report_content_type_uid
        self.report_content_type_name = report_content_type_name
        self.created_date = created_date
        self.created_by = created_by


@dataclass(frozen=False)
class report_format_normal_dto(base_read_dto, report_format_write_dto):
    report_format_uid: str
    report_format_name: str
    created_date: datetime.datetime
    created_by: str
    def __init__(self, report_format_uid: str, report_format_name: str, created_date: datetime.datetime, created_by: str):
        self.report_format_uid = report_format_uid
        self.report_format_name = report_format_name
        self.created_date = created_date
        self.created_by = created_by


@dataclass(frozen=False)
class report_run_normal_dto(base_read_dto, report_run_write_dto):
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
    created_date: datetime.datetime
    created_by: str
    def __init__(self, report_run_uid: str, report_run_name: str, tenant_uid: str, account_uid: str, report_uid: str, report_format_uid: str, report_status_uid: str, report_content_type_uid: str, input_parameters_json: str, run_time_ms: int, returned_rows: int, content_size: int, created_date: datetime.datetime, created_by: str):
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
        self.created_date = created_date
        self.created_by = created_by


@dataclass(frozen=False)
class report_status_normal_dto(base_read_dto, report_status_write_dto):
    report_status_uid: str
    report_status_name: str
    created_date: datetime.datetime
    created_by: str
    def __init__(self, report_status_uid: str, report_status_name: str, created_date: datetime.datetime, created_by: str):
        self.report_status_uid = report_status_uid
        self.report_status_name = report_status_name
        self.created_date = created_date
        self.created_by = created_by


@dataclass(frozen=False)
class report_type_normal_dto(base_read_dto, report_type_write_dto):
    report_type_uid: str
    report_type_name: str
    created_date: datetime.datetime
    created_by: str
    def __init__(self, report_type_uid: str, report_type_name: str, created_date: datetime.datetime, created_by: str):
        self.report_type_uid = report_type_uid
        self.report_type_name = report_type_name
        self.created_date = created_date
        self.created_by = created_by


@dataclass(frozen=False)
class storage_normal_dto(base_read_dto, storage_write_dto):
    storage_uid: str
    storage_name: str
    storage_class: str
    storage_parameters_json: str
    created_date: datetime.datetime
    created_by: str
    def __init__(self, storage_uid: str, storage_name: str, storage_class: str, storage_parameters_json: str, created_date: datetime.datetime, created_by: str):
        self.storage_uid = storage_uid
        self.storage_name = storage_name
        self.storage_class = storage_class
        self.storage_parameters_json = storage_parameters_json
        self.created_date = created_date
        self.created_by = created_by


@dataclass(frozen=False)
class storage_connection_normal_dto(base_read_dto, storage_connection_write_dto):
    storage_connection_uid: str
    storage_connection_name: str
    storage_uid: str
    connection_type: str
    storage_parameters_json: str
    created_date: datetime.datetime
    created_by: str
    def __init__(self, storage_connection_uid: str, storage_connection_name: str, storage_uid: str, connection_type: str, storage_parameters_json: str, created_date: datetime.datetime, created_by: str):
        self.storage_connection_uid = storage_connection_uid
        self.storage_connection_name = storage_connection_name
        self.storage_uid = storage_uid
        self.connection_type = connection_type
        self.storage_parameters_json = storage_parameters_json
        self.created_date = created_date
        self.created_by = created_by


@dataclass(frozen=False)
class storage_query_normal_dto(base_read_dto, storage_query_write_dto):
    storage_connection_uid: str
    storage_connection_name: str
    storage_uid: str
    storage_parameters_json: str
    created_date: datetime.datetime
    created_by: str
    def __init__(self, storage_connection_uid: str, storage_connection_name: str, storage_uid: str, storage_parameters_json: str, created_date: datetime.datetime, created_by: str):
        self.storage_connection_uid = storage_connection_uid
        self.storage_connection_name = storage_connection_name
        self.storage_uid = storage_uid
        self.storage_parameters_json = storage_parameters_json
        self.created_date = created_date
        self.created_by = created_by


@dataclass(frozen=False)
class storage_type_normal_dto(base_read_dto, storage_type_write_dto):
    storage_type_uid: str
    storage_type_name: str
    storage_class: str
    storage_parameters_json: str
    created_date: datetime.datetime
    created_by: str
    def __init__(self, storage_type_uid: str, storage_type_name: str, storage_class: str, storage_parameters_json: str, created_date: datetime.datetime, created_by: str):
        self.storage_type_uid = storage_type_uid
        self.storage_type_name = storage_type_name
        self.storage_class = storage_class
        self.storage_parameters_json = storage_parameters_json
        self.created_date = created_date
        self.created_by = created_by


@dataclass(frozen=False)
class synchronization_normal_dto(base_read_dto, synchronization_write_dto):
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
    created_date: datetime.datetime
    created_by: str
    def __init__(self, synchronization_uid: str, synchronization_name: str, tenant_uid: str, synchronization_type_uid: str, storage_uid: str, sync_expression: str, sync_query: str, sync_definition: str, sync_priority: int, last_run_date: datetime.datetime | None, last_run_seconds: str | None, created_date: datetime.datetime, created_by: str):
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
        self.created_date = created_date
        self.created_by = created_by


@dataclass(frozen=False)
class synchronization_run_normal_dto(base_read_dto, synchronization_run_write_dto):
    synchronization_run_uid: str
    synchronization_run_name: str
    synchronization_uid: str
    run_status: str
    run_time_seconds: str
    copied_items: int
    created_date: datetime.datetime
    created_by: str
    def __init__(self, synchronization_run_uid: str, synchronization_run_name: str, synchronization_uid: str, run_status: str, run_time_seconds: str, copied_items: int, created_date: datetime.datetime, created_by: str):
        self.synchronization_run_uid = synchronization_run_uid
        self.synchronization_run_name = synchronization_run_name
        self.synchronization_uid = synchronization_uid
        self.run_status = run_status
        self.run_time_seconds = run_time_seconds
        self.copied_items = copied_items
        self.created_date = created_date
        self.created_by = created_by


@dataclass(frozen=False)
class synchronization_type_normal_dto(base_read_dto, synchronization_type_write_dto):
    synchronization_type_uid: str
    synchronization_type_name: str
    sync_type: str
    sync_class_came: str
    created_date: datetime.datetime
    created_by: str
    def __init__(self, synchronization_type_uid: str, synchronization_type_name: str, sync_type: str, sync_class_came: str, created_date: datetime.datetime, created_by: str):
        self.synchronization_type_uid = synchronization_type_uid
        self.synchronization_type_name = synchronization_type_name
        self.sync_type = sync_type
        self.sync_class_came = sync_class_came
        self.created_date = created_date
        self.created_by = created_by


@dataclass(frozen=False)
class system_attribute_normal_dto(base_read_dto, system_attribute_write_dto):
    system_attribute_uid: str
    system_attribute_name: str
    system_object_uid: str
    column_name: str
    attribute_type: str
    attribute_label: str
    attribute_description: str
    created_date: datetime.datetime
    created_by: str
    def __init__(self, system_attribute_uid: str, system_attribute_name: str, system_object_uid: str, column_name: str, attribute_type: str, attribute_label: str, attribute_description: str, created_date: datetime.datetime, created_by: str):
        self.system_attribute_uid = system_attribute_uid
        self.system_attribute_name = system_attribute_name
        self.system_object_uid = system_object_uid
        self.column_name = column_name
        self.attribute_type = attribute_type
        self.attribute_label = attribute_label
        self.attribute_description = attribute_description
        self.created_date = created_date
        self.created_by = created_by


@dataclass(frozen=False)
class system_database_normal_dto(base_read_dto, system_database_write_dto):
    system_database_uid: str
    system_database_name: str
    db_url: str
    db_host: str
    db_name: str
    db_user: str
    created_date: datetime.datetime
    created_by: str
    def __init__(self, system_database_uid: str, system_database_name: str, db_url: str, db_host: str, db_name: str, db_user: str, created_date: datetime.datetime, created_by: str):
        self.system_database_uid = system_database_uid
        self.system_database_name = system_database_name
        self.db_url = db_url
        self.db_host = db_host
        self.db_name = db_name
        self.db_user = db_user
        self.created_date = created_date
        self.created_by = created_by


@dataclass(frozen=False)
class system_exception_normal_dto(base_read_dto, system_exception_write_dto):
    system_exception_uid: str
    system_exception_name: str
    exception_class: str
    exception_message: str
    exception_stacktrace: str
    created_date: datetime.datetime
    created_by: str
    def __init__(self, system_exception_uid: str, system_exception_name: str, exception_class: str, exception_message: str, exception_stacktrace: str, created_date: datetime.datetime, created_by: str):
        self.system_exception_uid = system_exception_uid
        self.system_exception_name = system_exception_name
        self.exception_class = exception_class
        self.exception_message = exception_message
        self.exception_stacktrace = exception_stacktrace
        self.created_date = created_date
        self.created_by = created_by


@dataclass(frozen=False)
class system_instance_normal_dto(base_read_dto, system_instance_write_dto):
    system_instance_uid: str
    system_instance_name: str
    system_version_uid: str
    host_name: str
    host_ip: str
    local_path: str
    mode_name: str
    ticks_count: int
    created_date: datetime.datetime
    created_by: str
    def __init__(self, system_instance_uid: str, system_instance_name: str, system_version_uid: str, host_name: str, host_ip: str, local_path: str, mode_name: str, ticks_count: int, created_date: datetime.datetime, created_by: str):
        self.system_instance_uid = system_instance_uid
        self.system_instance_name = system_instance_name
        self.system_version_uid = system_version_uid
        self.host_name = host_name
        self.host_ip = host_ip
        self.local_path = local_path
        self.mode_name = mode_name
        self.ticks_count = ticks_count
        self.created_date = created_date
        self.created_by = created_by


@dataclass(frozen=False)
class system_license_normal_dto(base_read_dto, system_license_write_dto):
    system_license_uid: str
    system_license_name: str
    license_description: str
    created_date: datetime.datetime
    created_by: str
    def __init__(self, system_license_uid: str, system_license_name: str, license_description: str, created_date: datetime.datetime, created_by: str):
        self.system_license_uid = system_license_uid
        self.system_license_name = system_license_name
        self.license_description = license_description
        self.created_date = created_date
        self.created_by = created_by


@dataclass(frozen=False)
class system_lock_normal_dto(base_read_dto, system_lock_write_dto):
    system_lock_uid: str
    system_lock_name: str
    lock_account_uid: str
    lock_comment: str
    created_date: datetime.datetime
    created_by: str
    def __init__(self, system_lock_uid: str, system_lock_name: str, lock_account_uid: str, lock_comment: str, created_date: datetime.datetime, created_by: str):
        self.system_lock_uid = system_lock_uid
        self.system_lock_name = system_lock_name
        self.lock_account_uid = lock_account_uid
        self.lock_comment = lock_comment
        self.created_date = created_date
        self.created_by = created_by


@dataclass(frozen=False)
class system_module_normal_dto(base_read_dto, system_module_write_dto):
    system_module_uid: str
    system_module_name: str
    system_module_description: str
    created_date: datetime.datetime
    created_by: str
    def __init__(self, system_module_uid: str, system_module_name: str, system_module_description: str, created_date: datetime.datetime, created_by: str):
        self.system_module_uid = system_module_uid
        self.system_module_name = system_module_name
        self.system_module_description = system_module_description
        self.created_date = created_date
        self.created_by = created_by


@dataclass(frozen=False)
class system_object_normal_dto(base_read_dto, system_object_write_dto):
    system_object_uid: str
    system_object_name: str
    system_version_uid: str
    system_table_uid: str
    system_object_type_uid: str
    parent_system_object_uid: str | None
    object_type: str
    created_date: datetime.datetime
    created_by: str
    def __init__(self, system_object_uid: str, system_object_name: str, system_version_uid: str, system_table_uid: str, system_object_type_uid: str, parent_system_object_uid: str | None, object_type: str, created_date: datetime.datetime, created_by: str):
        self.system_object_uid = system_object_uid
        self.system_object_name = system_object_name
        self.system_version_uid = system_version_uid
        self.system_table_uid = system_table_uid
        self.system_object_type_uid = system_object_type_uid
        self.parent_system_object_uid = parent_system_object_uid
        self.object_type = object_type
        self.created_date = created_date
        self.created_by = created_by


@dataclass(frozen=False)
class system_object_type_normal_dto(base_read_dto, system_object_type_write_dto):
    system_object_type_uid: str
    system_object_type_name: str
    object_type_description: str
    created_date: datetime.datetime
    created_by: str
    def __init__(self, system_object_type_uid: str, system_object_type_name: str, object_type_description: str, created_date: datetime.datetime, created_by: str):
        self.system_object_type_uid = system_object_type_uid
        self.system_object_type_name = system_object_type_name
        self.object_type_description = object_type_description
        self.created_date = created_date
        self.created_by = created_by


@dataclass(frozen=False)
class system_query_normal_dto(base_read_dto, system_query_write_dto):
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
    created_date: datetime.datetime
    created_by: str
    def __init__(self, system_query_uid: str, system_query_name: str, time_start: int, total_query_time: int, query_seq: int, execution_counter: int, connection_counter: int, release_counter: int, current_active: int, current_idle: int, table_name: str, rows_count: int, sql: str, created_date: datetime.datetime, created_by: str):
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
        self.created_date = created_date
        self.created_by = created_by


@dataclass(frozen=False)
class system_request_normal_dto(base_read_dto, system_request_write_dto):
    system_request_uid: str
    system_request_name: str
    account_uid: str | None
    request_method: str
    request_url: str
    request_body_size: int
    request_host: str
    request_time: int
    response_code: int
    created_date: datetime.datetime
    created_by: str
    def __init__(self, system_request_uid: str, system_request_name: str, account_uid: str | None, request_method: str, request_url: str, request_body_size: int, request_host: str, request_time: int, response_code: int, created_date: datetime.datetime, created_by: str):
        self.system_request_uid = system_request_uid
        self.system_request_name = system_request_name
        self.account_uid = account_uid
        self.request_method = request_method
        self.request_url = request_url
        self.request_body_size = request_body_size
        self.request_host = request_host
        self.request_time = request_time
        self.response_code = response_code
        self.created_date = created_date
        self.created_by = created_by


@dataclass(frozen=False)
class system_setting_normal_dto(base_read_dto, system_setting_write_dto):
    system_setting_uid: str
    system_setting_name: str
    setting_value: str
    created_date: datetime.datetime
    created_by: str
    def __init__(self, system_setting_uid: str, system_setting_name: str, setting_value: str, created_date: datetime.datetime, created_by: str):
        self.system_setting_uid = system_setting_uid
        self.system_setting_name = system_setting_name
        self.setting_value = setting_value
        self.created_date = created_date
        self.created_by = created_by


@dataclass(frozen=False)
class system_setting_account_normal_dto(base_read_dto, system_setting_account_write_dto):
    system_setting_account_uid: str
    system_setting_account_name: str
    account_uid: str
    setting_value: str
    is_public: int
    created_date: datetime.datetime
    created_by: str
    def __init__(self, system_setting_account_uid: str, system_setting_account_name: str, account_uid: str, setting_value: str, is_public: int, created_date: datetime.datetime, created_by: str):
        self.system_setting_account_uid = system_setting_account_uid
        self.system_setting_account_name = system_setting_account_name
        self.account_uid = account_uid
        self.setting_value = setting_value
        self.is_public = is_public
        self.created_date = created_date
        self.created_by = created_by


@dataclass(frozen=False)
class system_state_normal_dto(base_read_dto, system_state_write_dto):
    system_state_uid: str
    system_state_name: str
    mem_free: int
    mem_max: int
    objects_count: int
    created_date: datetime.datetime
    created_by: str
    def __init__(self, system_state_uid: str, system_state_name: str, mem_free: int, mem_max: int, objects_count: int, created_date: datetime.datetime, created_by: str):
        self.system_state_uid = system_state_uid
        self.system_state_name = system_state_name
        self.mem_free = mem_free
        self.mem_max = mem_max
        self.objects_count = objects_count
        self.created_date = created_date
        self.created_by = created_by


@dataclass(frozen=False)
class system_table_normal_dto(base_read_dto, system_table_write_dto):
    system_table_uid: str
    system_table_name: str
    parent_system_table_uid: str | None
    key_name: str
    table_code: str
    table_comment: str
    created_date: datetime.datetime
    created_by: str
    def __init__(self, system_table_uid: str, system_table_name: str, parent_system_table_uid: str | None, key_name: str, table_code: str, table_comment: str, created_date: datetime.datetime, created_by: str):
        self.system_table_uid = system_table_uid
        self.system_table_name = system_table_name
        self.parent_system_table_uid = parent_system_table_uid
        self.key_name = key_name
        self.table_code = table_code
        self.table_comment = table_comment
        self.created_date = created_date
        self.created_by = created_by


@dataclass(frozen=False)
class system_thread_normal_dto(base_read_dto, system_thread_write_dto):
    system_thread_uid: str
    system_thread_name: str
    thread_name: str
    parent_object: str
    ticks_count: int
    sleep_time: int
    created_date: datetime.datetime
    created_by: str
    def __init__(self, system_thread_uid: str, system_thread_name: str, thread_name: str, parent_object: str, ticks_count: int, sleep_time: int, created_date: datetime.datetime, created_by: str):
        self.system_thread_uid = system_thread_uid
        self.system_thread_name = system_thread_name
        self.thread_name = thread_name
        self.parent_object = parent_object
        self.ticks_count = ticks_count
        self.sleep_time = sleep_time
        self.created_date = created_date
        self.created_by = created_by


@dataclass(frozen=False)
class system_version_normal_dto(base_read_dto, system_version_write_dto):
    system_version_uid: str
    system_version_name: str
    version_description: str
    created_date: datetime.datetime
    created_by: str
    def __init__(self, system_version_uid: str, system_version_name: str, version_description: str, created_date: datetime.datetime, created_by: str):
        self.system_version_uid = system_version_uid
        self.system_version_name = system_version_name
        self.version_description = version_description
        self.created_date = created_date
        self.created_by = created_by


@dataclass(frozen=False)
class tenant_normal_dto(base_read_dto, tenant_write_dto):
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
    created_date: datetime.datetime
    created_by: str
    def __init__(self, tenant_uid: str, tenant_name: str, country_uid: str, tenant_type_uid: str, tenant_category_uid: str, tenant_code: str, tenant_description: str, start_date: datetime.datetime, end_date: datetime.datetime | None, is_internal: int, is_system: int, is_test: int, account_uid: str | None, created_date: datetime.datetime, created_by: str):
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
        self.created_date = created_date
        self.created_by = created_by


@dataclass(frozen=False)
class tenant_account_normal_dto(base_read_dto, tenant_account_write_dto):
    tenant_account_uid: str
    tenant_account_name: str
    tenant_uid: str
    account_uid: str
    tenant_role_uid: str
    created_date: datetime.datetime
    created_by: str
    def __init__(self, tenant_account_uid: str, tenant_account_name: str, tenant_uid: str, account_uid: str, tenant_role_uid: str, created_date: datetime.datetime, created_by: str):
        self.tenant_account_uid = tenant_account_uid
        self.tenant_account_name = tenant_account_name
        self.tenant_uid = tenant_uid
        self.account_uid = account_uid
        self.tenant_role_uid = tenant_role_uid
        self.created_date = created_date
        self.created_by = created_by


@dataclass(frozen=False)
class tenant_category_normal_dto(base_read_dto, tenant_category_write_dto):
    tenant_category_uid: str
    tenant_category_name: str
    tenant_category_description: str
    created_date: datetime.datetime
    created_by: str
    def __init__(self, tenant_category_uid: str, tenant_category_name: str, tenant_category_description: str, created_date: datetime.datetime, created_by: str):
        self.tenant_category_uid = tenant_category_uid
        self.tenant_category_name = tenant_category_name
        self.tenant_category_description = tenant_category_description
        self.created_date = created_date
        self.created_by = created_by


@dataclass(frozen=False)
class tenant_country_normal_dto(base_read_dto, tenant_country_write_dto):
    tenant_country_uid: str
    tenant_country_name: str
    country_uid: str
    tenant_uid: str
    country_priority: int
    created_date: datetime.datetime
    created_by: str
    def __init__(self, tenant_country_uid: str, tenant_country_name: str, country_uid: str, tenant_uid: str, country_priority: int, created_date: datetime.datetime, created_by: str):
        self.tenant_country_uid = tenant_country_uid
        self.tenant_country_name = tenant_country_name
        self.country_uid = country_uid
        self.tenant_uid = tenant_uid
        self.country_priority = country_priority
        self.created_date = created_date
        self.created_by = created_by


@dataclass(frozen=False)
class tenant_license_normal_dto(base_read_dto, tenant_license_write_dto):
    tenant_license_uid: str
    tenant_license_name: str
    tenant_uid: str
    system_license_uid: str
    start_date: datetime.datetime
    end_date: datetime.datetime
    is_approved: int
    created_date: datetime.datetime
    created_by: str
    def __init__(self, tenant_license_uid: str, tenant_license_name: str, tenant_uid: str, system_license_uid: str, start_date: datetime.datetime, end_date: datetime.datetime, is_approved: int, created_date: datetime.datetime, created_by: str):
        self.tenant_license_uid = tenant_license_uid
        self.tenant_license_name = tenant_license_name
        self.tenant_uid = tenant_uid
        self.system_license_uid = system_license_uid
        self.start_date = start_date
        self.end_date = end_date
        self.is_approved = is_approved
        self.created_date = created_date
        self.created_by = created_by


@dataclass(frozen=False)
class tenant_payment_normal_dto(base_read_dto, tenant_payment_write_dto):
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
    created_date: datetime.datetime
    created_by: str
    def __init__(self, tenant_payment_uid: str, tenant_payment_name: str, tenant_uid: str, account_uid: str, currency_uid: str, tenant_payment_type_uid: str, start_date: datetime.datetime, end_date: datetime.datetime | None, payment_value: str, source_number: str, source_reference: str, is_approved: int, created_date: datetime.datetime, created_by: str):
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
        self.created_date = created_date
        self.created_by = created_by


@dataclass(frozen=False)
class tenant_payment_type_normal_dto(base_read_dto, tenant_payment_type_write_dto):
    tenant_payment_type_uid: str
    tenant_payment_type_name: str
    created_date: datetime.datetime
    created_by: str
    def __init__(self, tenant_payment_type_uid: str, tenant_payment_type_name: str, created_date: datetime.datetime, created_by: str):
        self.tenant_payment_type_uid = tenant_payment_type_uid
        self.tenant_payment_type_name = tenant_payment_type_name
        self.created_date = created_date
        self.created_by = created_by


@dataclass(frozen=False)
class tenant_role_normal_dto(base_read_dto, tenant_role_write_dto):
    tenant_role_uid: str
    tenant_role_name: str
    role_description: str
    created_date: datetime.datetime
    created_by: str
    def __init__(self, tenant_role_uid: str, tenant_role_name: str, role_description: str, created_date: datetime.datetime, created_by: str):
        self.tenant_role_uid = tenant_role_uid
        self.tenant_role_name = tenant_role_name
        self.role_description = role_description
        self.created_date = created_date
        self.created_by = created_by


@dataclass(frozen=False)
class tenant_status_normal_dto(base_read_dto, tenant_status_write_dto):
    tenant_status_uid: str
    tenant_status_name: str
    tenant_status_description: str
    created_date: datetime.datetime
    created_by: str
    def __init__(self, tenant_status_uid: str, tenant_status_name: str, tenant_status_description: str, created_date: datetime.datetime, created_by: str):
        self.tenant_status_uid = tenant_status_uid
        self.tenant_status_name = tenant_status_name
        self.tenant_status_description = tenant_status_description
        self.created_date = created_date
        self.created_by = created_by


@dataclass(frozen=False)
class tenant_type_normal_dto(base_read_dto, tenant_type_write_dto):
    tenant_type_uid: str
    tenant_type_name: str
    tenant_type_description: str
    created_date: datetime.datetime
    created_by: str
    def __init__(self, tenant_type_uid: str, tenant_type_name: str, tenant_type_description: str, created_date: datetime.datetime, created_by: str):
        self.tenant_type_uid = tenant_type_uid
        self.tenant_type_name = tenant_type_name
        self.tenant_type_description = tenant_type_description
        self.created_date = created_date
        self.created_by = created_by


@dataclass(frozen=False)
class time_approval_normal_dto(base_read_dto, time_approval_write_dto):
    time_approval_uid: str
    time_approval_name: str
    tenant_uid: str
    account_uid: str
    time_entry_uid: str
    approval_comment: str
    created_date: datetime.datetime
    created_by: str
    def __init__(self, time_approval_uid: str, time_approval_name: str, tenant_uid: str, account_uid: str, time_entry_uid: str, approval_comment: str, created_date: datetime.datetime, created_by: str):
        self.time_approval_uid = time_approval_uid
        self.time_approval_name = time_approval_name
        self.tenant_uid = tenant_uid
        self.account_uid = account_uid
        self.time_entry_uid = time_entry_uid
        self.approval_comment = approval_comment
        self.created_date = created_date
        self.created_by = created_by


@dataclass(frozen=False)
class time_entry_normal_dto(base_read_dto, time_entry_write_dto):
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
    created_date: datetime.datetime
    created_by: str
    def __init__(self, time_entry_uid: str, time_entry_name: str, time_submit_uid: str, tenant_uid: str, account_uid: str, project_instance_uid: str, project_milestone_uid: str, period_uid: str, invoice_instance_uid: str | None, entry_period: str, entry_note: str, lock_row: str | None, start_date: datetime.datetime | None, end_date: datetime.datetime | None, entry_minutes: int, is_approved: int, created_date: datetime.datetime, created_by: str):
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
        self.created_date = created_date
        self.created_by = created_by


@dataclass(frozen=False)
class time_entry_final_normal_dto(base_read_dto, time_entry_final_write_dto):
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
    created_date: datetime.datetime
    created_by: str
    def __init__(self, time_entry_final_uid: str, time_entry_final_name: str, tenant_uid: str, account_uid: str, project_instance_uid: str, project_milestone_uid: str, invoice_instance_uid: str | None, entry_period: str, entry_note: str, lock_uid: str | None, start_date: datetime.datetime | None, end_date: datetime.datetime | None, entry_minutes: int, is_approved: int, created_date: datetime.datetime, created_by: str):
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
        self.created_date = created_date
        self.created_by = created_by


@dataclass(frozen=False)
class time_entry_invoice_normal_dto(base_read_dto, time_entry_invoice_write_dto):
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
    created_date: datetime.datetime
    created_by: str
    def __init__(self, time_entry_invoice_uid: str, time_entry_invoice_name: str, tenant_uid: str, account_uid: str, time_submit_uid: str, time_entry_uid: str, project_instance_uid: str, project_milestone_uid: str, period_uid: str, invoice_instance_uid: str, entry_period: str, entry_note: str, lock_row: str | None, start_date: datetime.datetime | None, end_date: datetime.datetime | None, entry_minutes: int, is_approved: int, created_date: datetime.datetime, created_by: str):
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
        self.created_date = created_date
        self.created_by = created_by


@dataclass(frozen=False)
class time_rule_normal_dto(base_read_dto, time_rule_write_dto):
    time_rule_uid: str
    time_rule_name: str
    created_date: datetime.datetime
    created_by: str
    def __init__(self, time_rule_uid: str, time_rule_name: str, created_date: datetime.datetime, created_by: str):
        self.time_rule_uid = time_rule_uid
        self.time_rule_name = time_rule_name
        self.created_date = created_date
        self.created_by = created_by


@dataclass(frozen=False)
class time_rule_client_normal_dto(base_read_dto, time_rule_client_write_dto):
    time_rule_client_uid: str
    time_rule_client_name: str
    time_rule_definition: str
    created_date: datetime.datetime
    created_by: str
    def __init__(self, time_rule_client_uid: str, time_rule_client_name: str, time_rule_definition: str, created_date: datetime.datetime, created_by: str):
        self.time_rule_client_uid = time_rule_client_uid
        self.time_rule_client_name = time_rule_client_name
        self.time_rule_definition = time_rule_definition
        self.created_date = created_date
        self.created_by = created_by


@dataclass(frozen=False)
class time_submit_normal_dto(base_read_dto, time_submit_write_dto):
    time_submit_uid: str
    time_submit_name: str
    tenant_uid: str
    account_uid: str
    period_uid: str
    time_submit_description: str
    created_date: datetime.datetime
    created_by: str
    def __init__(self, time_submit_uid: str, time_submit_name: str, tenant_uid: str, account_uid: str, period_uid: str, time_submit_description: str, created_date: datetime.datetime, created_by: str):
        self.time_submit_uid = time_submit_uid
        self.time_submit_name = time_submit_name
        self.tenant_uid = tenant_uid
        self.account_uid = account_uid
        self.period_uid = period_uid
        self.time_submit_description = time_submit_description
        self.created_date = created_date
        self.created_by = created_by


@dataclass(frozen=False)
class time_submit_type_normal_dto(base_read_dto, time_submit_type_write_dto):
    time_submit_type_uid: str
    time_submit_type_name: str
    time_submit_type_description: str
    created_date: datetime.datetime
    created_by: str
    def __init__(self, time_submit_type_uid: str, time_submit_type_name: str, time_submit_type_description: str, created_date: datetime.datetime, created_by: str):
        self.time_submit_type_uid = time_submit_type_uid
        self.time_submit_type_name = time_submit_type_name
        self.time_submit_type_description = time_submit_type_description
        self.created_date = created_date
        self.created_by = created_by


# auto-generated - v_definition_python_dtos_normal - END