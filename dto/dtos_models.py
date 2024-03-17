import datetime
from abc import abstractmethod
from dataclasses import dataclass

from dto.dtos import base_model

# class to store all DB models - definition of tables and columns/attributes to generate SQL queries for CRUD operations
class model_list:
    # auto-generated - ModelList - START
    account_division_model: base_model = base_model('account_division', ['account_division_uid', 'system_version_uid', 'division_name', 'division_description'])
    account_group_model: base_model = base_model('account_group', ['account_group_uid', 'system_version_uid', 'account_group_name', 'account_group_description'])
    account_instance_model: base_model = base_model('account_instance', ['account_instance_uid', 'client_instance_uid', 'account_type_uid', 'account_title_uid', 'account_division_uid', 'account_group_uid', 'auth_identity_uid', 'account_email', 'account_name', 'display_name', 'is_system'])
    account_title_model: base_model = base_model('account_title', ['account_title_uid', 'system_version_uid', 'title_name', 'title_description'])
    account_type_model: base_model = base_model('account_type', ['account_type_uid', 'system_version_uid', 'account_type_name', 'account_type_description'])
    auth_identity_model: base_model = base_model('auth_identity', ['auth_identity_uid', 'client_instance_uid', 'identity_name', 'identity_type', 'identity_parameters', 'last_status_name'])
    auth_password_model: base_model = base_model('auth_password', ['auth_password_uid', 'account_instance_uid', 'system_instance_uid', 'password_hash', 'password_salt', 'date_from', 'date_to', 'usage_count'])
    auth_permission_model: base_model = base_model('auth_permission', ['auth_permission_uid', 'account_instance_uid', 'system_instance_uid', 'auth_role_uid', 'client_instance_uid', 'project_instance_uid', 'valid_from_date', 'valid_till_date'])
    auth_request_model: base_model = base_model('auth_request', ['auth_request_uid', 'by_account_instance_uid', 'account_instance_uid', 'system_instance_uid', 'reset_guid', 'valid_till_date', 'lock_guid', 'lock_by', 'lock_date', 'is_checked', 'is_used', 'check_date', 'use_date'])
    auth_role_model: base_model = base_model('auth_role', ['auth_role_uid', 'parent_auth_role_uid', 'role_name', 'role_description', 'access_uris', 'is_project', 'is_client', 'is_custom'])
    auth_token_model: base_model = base_model('auth_token', ['auth_token_uid', 'account_instance_uid', 'system_instance_uid', 'token_seq', 'token_hash', 'token_salt', 'valid_till_date', 'last_use_date', 'is_last'])
    client_instance_model: base_model = base_model('client_instance', ['client_instance_uid', 'country_uid', 'client_name', 'client_code', 'client_description', 'start_date', 'end_date', 'is_internal', 'is_system', 'is_test'])
    client_type_model: base_model = base_model('client_type', ['client_type_uid', 'system_version_uid', 'client_type_name'])
    country_model: base_model = base_model('country', ['country_uid', 'continent_name', 'continent_code', 'country_name', 'country_iso3', 'country_code', 'phone_code', 'currency_code', 'capital_name', 'region_name', 'subregion_name', 'region_code', 'latitude', 'longitude', 'currency_name', 'population', 'languages', 'area', 'bar_code', 'top_level_domain', 'is_focused'])
    currency_model: base_model = base_model('currency', ['currency_uid', 'currency_name', 'is_focused'])
    entry_final_model: base_model = base_model('entry_final', ['entry_final_uid', 'account_instance_uid', 'project_instance_uid', 'project_milestone_uid', 'invoice_instance_uid', 'entry_period', 'entry_note', 'lock_uid', 'start_date', 'end_date', 'entry_minutes', 'is_approved'])
    entry_save_model: base_model = base_model('entry_save', ['entry_save_uid', 'account_instance_uid', 'project_instance_uid', 'project_milestone_uid', 'invoice_instance_uid', 'entry_period', 'entry_note', 'lock_uid', 'start_date', 'end_date', 'entry_minutes', 'is_approved'])
    event_channel_model: base_model = base_model('event_channel', ['event_channel_uid', 'system_version_uid', 'channel_type', 'channel_name', 'channel_definition'])
    event_instance_model: base_model = base_model('event_instance', ['event_instance_uid', 'system_instance_uid', 'event_type', 'event_object', 'event_method', 'event_parameters', 'event_signature', 'published_count', 'event_date'])
    event_subscription_model: base_model = base_model('event_subscription', ['event_subscription_uid', 'event_channel_uid', 'subscription_name', 'subscription_filter', 'subscription_topic', 'subscription_template'])
    invoice_instance_model: base_model = base_model('invoice_instance', ['invoice_instance_uid', 'client_instance_uid', 'account_instance_uid', 'period_code', 'invoice_number', 'invoice_details', 'invoice_status', 'invoice_currency', 'invoice_amount'])
    notification_instance_model: base_model = base_model('notification_instance', ['notification_instance_uid', 'client_instance_uid', 'account_instance_uid', 'notification_type', 'notification_topic', 'notification_format', 'notification_content', 'sending_status'])
    project_budget_model: base_model = base_model('project_budget', ['project_budget_uid', 'project_instance_uid', 'budget_name', 'budget_currency', 'budget_value', 'is_current'])
    project_group_model: base_model = base_model('project_group', ['project_group_uid', 'project_group_name', 'project_group_description'])
    project_instance_model: base_model = base_model('project_instance', ['project_instance_uid', 'client_instance_uid', 'manager_account_instance_uid', 'project_group_uid', 'project_name', 'project_code', 'is_billable', 'start_date', 'end_date', 'current_billed', 'budget'])
    project_milestone_model: base_model = base_model('project_milestone', ['project_milestone_uid', 'project_instance_uid', 'project_budget_uid', 'milestone_name', 'start_date', 'end_date', 'status_name'])
    system_attribute_model: base_model = base_model('system_attribute', ['system_attribute_uid', 'system_object_uid', 'system_version_uid', 'column_name', 'attribute_name', 'attribute_type', 'attribute_label', 'attribute_description'])
    system_change_model: base_model = base_model('system_change', ['system_change_uid', 'account_instance_uid', 'system_instance_uid', 'change_type', 'change_name', 'change_json'])
    system_database_model: base_model = base_model('system_database', ['system_database_uid', 'db_url', 'db_host', 'db_name', 'db_user'])
    system_exception_model: base_model = base_model('system_exception', ['system_exception_uid', 'system_instance_uid', 'exception_class', 'exception_message', 'exception_stacktrace'])
    system_instance_model: base_model = base_model('system_instance', ['system_instance_uid', 'system_version_uid', 'host_name', 'host_ip', 'local_path', 'mode_name'])
    system_object_model: base_model = base_model('system_object', ['system_object_uid', 'system_version_uid', 'object_name', 'object_type', 'table_name', 'key_name', 'parent_system_object_uid'])
    system_object_type_model: base_model = base_model('system_object_type', ['system_object_type_uid', 'system_version_uid', 'system_object_uid', 'object_type_name', 'object_type_description'])
    system_setting_model: base_model = base_model('system_setting', ['system_setting_uid', 'account_instance_uid', 'setting_name', 'setting_value'])
    system_state_model: base_model = base_model('system_state', ['system_state_uid', 'system_instance_uid', 'mem_free', 'mem_max', 'objects_count'])
    system_version_model: base_model = base_model('system_version', ['system_version_uid', 'version_description'])
    # auto-generated - ModelList - END
    all_models: list[base_model] = []
    def __init__(self):
        print("Creating all DB models")

    def initialize(self):
        print("Initialize DB models")
        # auto-generated - ModelRegister - START
        self.all_models.append(self.account_division_model)
        self.all_models.append(self.account_group_model)
        self.all_models.append(self.account_instance_model)
        self.all_models.append(self.account_title_model)
        self.all_models.append(self.account_type_model)
        self.all_models.append(self.auth_identity_model)
        self.all_models.append(self.auth_password_model)
        self.all_models.append(self.auth_permission_model)
        self.all_models.append(self.auth_request_model)
        self.all_models.append(self.auth_role_model)
        self.all_models.append(self.auth_token_model)
        self.all_models.append(self.client_instance_model)
        self.all_models.append(self.client_type_model)
        self.all_models.append(self.country_model)
        self.all_models.append(self.currency_model)
        self.all_models.append(self.entry_final_model)
        self.all_models.append(self.entry_save_model)
        self.all_models.append(self.event_channel_model)
        self.all_models.append(self.event_instance_model)
        self.all_models.append(self.event_subscription_model)
        self.all_models.append(self.invoice_instance_model)
        self.all_models.append(self.notification_instance_model)
        self.all_models.append(self.project_budget_model)
        self.all_models.append(self.project_group_model)
        self.all_models.append(self.project_instance_model)
        self.all_models.append(self.project_milestone_model)
        self.all_models.append(self.system_attribute_model)
        self.all_models.append(self.system_change_model)
        self.all_models.append(self.system_database_model)
        self.all_models.append(self.system_exception_model)
        self.all_models.append(self.system_instance_model)
        self.all_models.append(self.system_object_model)
        self.all_models.append(self.system_object_type_model)
        self.all_models.append(self.system_setting_model)
        self.all_models.append(self.system_state_model)
        self.all_models.append(self.system_version_model)
        # auto-generated - ModelRegister - END

    # handler for closing application
    def close(self):
        print("Closing Models")


# class with all models
db_models = model_list()
