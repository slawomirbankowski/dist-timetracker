import datetime
from abc import abstractmethod
from dataclasses import dataclass

from dto.dtos import base_model

# list of all models defined in database to be used by DAOs, Services, Controllers
account_division_model = base_model('account_division', ['id', 'account_division_uid', 'division_name', 'division_description', 'row_guid', 'row_version', 'is_active', 'created_date', 'created_by', 'last_updated_date', 'last_updated_by', 'removed_date', 'removed_by', 'custom_attributes'], ['account_division_uid', 'division_name', 'division_description'])
account_group_model = base_model('account_group', ['id', 'account_group_uid', 'account_group_name', 'account_group_description', 'row_guid', 'row_version', 'is_active', 'created_date', 'created_by', 'last_updated_date', 'last_updated_by', 'removed_date', 'removed_by', 'custom_attributes'], ['account_group_uid', 'account_group_name', 'account_group_description'])
account_instance_model = base_model('account_instance', ['id', 'account_instance_uid', 'account_title_uid', 'account_division_uid', 'account_group_uid', 'auth_identity_uid', 'account_email', 'account_name', 'display_name', 'is_system', 'row_guid', 'row_version', 'is_active', 'created_date', 'created_by', 'last_updated_date', 'last_updated_by', 'removed_date', 'removed_by', 'custom_attributes'], ['account_instance_uid', 'account_title_uid', 'account_division_uid', 'account_group_uid', 'auth_identity_uid', 'account_email', 'account_name', 'display_name', 'is_system'])
account_title_model = base_model('account_title', ['id', 'account_title_uid', 'title_name', 'title_description', 'row_guid', 'row_version', 'is_active', 'created_date', 'created_by', 'last_updated_date', 'last_updated_by', 'removed_date', 'removed_by', 'custom_attributes'], ['account_title_uid', 'title_name', 'title_description'])
auth_identity_model = base_model('auth_identity', ['id', 'auth_identity_uid', 'identity_name', 'identity_type', 'identity_parameters', 'last_status_name', 'row_guid', 'row_version', 'is_active', 'created_date', 'created_by', 'last_updated_date', 'last_updated_by', 'removed_date', 'removed_by', 'custom_attributes'], ['auth_identity_uid', 'identity_name', 'identity_type', 'identity_parameters', 'last_status_name'])
auth_password_model = base_model('auth_password', ['id', 'auth_password_uid', 'account_instance_uid', 'password_hash', 'password_salt', 'date_from', 'date_to', 'usage_count', 'row_guid', 'row_version', 'is_active', 'created_date', 'created_by', 'last_updated_date', 'last_updated_by', 'removed_date', 'removed_by', 'custom_attributes'], ['auth_password_uid', 'account_instance_uid', 'password_hash', 'password_salt', 'date_from', 'date_to', 'usage_count'])
auth_permission_model = base_model('auth_permission', ['id', 'auth_permission_uid', 'account_instance_uid', 'auth_role_uid', 'client_instance_uid', 'project_instance_uid', 'valid_from_date', 'valid_till_date', 'row_guid', 'row_version', 'is_active', 'created_date', 'created_by', 'last_updated_date', 'last_updated_by', 'removed_date', 'removed_by', 'custom_attributes'], ['auth_permission_uid', 'account_instance_uid', 'auth_role_uid', 'client_instance_uid', 'project_instance_uid', 'valid_from_date', 'valid_till_date'])
auth_request_model = base_model('auth_request', ['id', 'auth_request_uid', 'by_account_instance_uid', 'account_instance_uid', 'reset_guid', 'valid_till_date', 'lock_guid', 'lock_by', 'lock_date', 'is_checked', 'is_used', 'check_date', 'use_date', 'row_guid', 'row_version', 'is_active', 'created_date', 'created_by', 'last_updated_date', 'last_updated_by', 'removed_date', 'removed_by', 'custom_attributes'], ['auth_request_uid', 'by_account_instance_uid', 'account_instance_uid', 'reset_guid', 'valid_till_date', 'lock_guid', 'lock_by', 'lock_date', 'is_checked', 'is_used', 'check_date', 'use_date'])
auth_role_model = base_model('auth_role', ['id', 'auth_role_uid', 'parent_auth_role_uid', 'role_name', 'role_description', 'access_uris', 'is_project', 'is_client', 'is_custom', 'row_guid', 'row_version', 'is_active', 'created_date', 'created_by', 'last_updated_date', 'last_updated_by', 'removed_date', 'removed_by', 'custom_attributes'], ['auth_role_uid', 'parent_auth_role_uid', 'role_name', 'role_description', 'access_uris', 'is_project', 'is_client', 'is_custom'])
auth_token_model = base_model('auth_token', ['id', 'auth_token_uid', 'account_instance_uid', 'token_seq', 'token_hash', 'token_salt', 'valid_till_date', 'last_use_date', 'is_last', 'row_guid', 'row_version', 'is_active', 'created_date', 'created_by', 'last_updated_date', 'last_updated_by', 'removed_date', 'removed_by', 'custom_attributes'], ['auth_token_uid', 'account_instance_uid', 'token_seq', 'token_hash', 'token_salt', 'valid_till_date', 'last_use_date', 'is_last'])
client_instance_model = base_model('client_instance', ['id', 'client_instance_uid', 'country_uid', 'client_name', 'client_code', 'client_description', 'start_date', 'end_date', 'is_internal', 'is_system', 'is_test', 'row_guid', 'row_version', 'is_active', 'created_date', 'created_by', 'last_updated_date', 'last_updated_by', 'removed_date', 'removed_by', 'custom_attributes'], ['client_instance_uid', 'country_uid', 'client_name', 'client_code', 'client_description', 'start_date', 'end_date', 'is_internal', 'is_system', 'is_test'])
country_model = base_model('country', ['id', 'country_uid', 'continent_name', 'continent_code', 'country_name', 'country_iso3', 'country_code', 'phone_code', 'currency_code', 'capital_name', 'region_name', 'subregion_name', 'region_code', 'latitude', 'longitude', 'currency_name', 'population', 'languages', 'area', 'bar_code', 'top_level_domain', 'is_focused', 'row_guid', 'row_version', 'is_active', 'created_date', 'created_by', 'last_updated_date', 'last_updated_by', 'removed_date', 'removed_by', 'custom_attributes'], ['country_uid', 'continent_name', 'continent_code', 'country_name', 'country_iso3', 'country_code', 'phone_code', 'currency_code', 'capital_name', 'region_name', 'subregion_name', 'region_code', 'latitude', 'longitude', 'currency_name', 'population', 'languages', 'area', 'bar_code', 'top_level_domain', 'is_focused'])
currency_model = base_model('currency', ['id', 'currency_uid', 'currency_name', 'is_focused', 'row_guid', 'row_version', 'is_active', 'created_date', 'created_by', 'last_updated_date', 'last_updated_by', 'removed_date', 'removed_by', 'custom_attributes'], ['currency_uid', 'currency_name', 'is_focused'])
entry_final_model = base_model('entry_final', ['id', 'entry_final_uid', 'account_instance_uid', 'project_instance_uid', 'project_milestone_uid', 'invoice_instance_uid', 'entry_period', 'entry_note', 'lock_uid', 'start_date', 'end_date', 'entry_minutes', 'is_approved', 'row_guid', 'row_version', 'is_active', 'created_date', 'created_by', 'last_updated_date', 'last_updated_by', 'removed_date', 'removed_by', 'custom_attributes'], ['entry_final_uid', 'account_instance_uid', 'project_instance_uid', 'project_milestone_uid', 'invoice_instance_uid', 'entry_period', 'entry_note', 'lock_uid', 'start_date', 'end_date', 'entry_minutes', 'is_approved'])
entry_save_model = base_model('entry_save', ['id', 'entry_save_uid', 'account_instance_uid', 'project_instance_uid', 'project_milestone_uid', 'invoice_instance_uid', 'entry_period', 'entry_note', 'lock_uid', 'start_date', 'end_date', 'entry_minutes', 'is_approved', 'row_guid', 'row_version', 'is_active', 'created_date', 'created_by', 'last_updated_date', 'last_updated_by', 'removed_date', 'removed_by', 'custom_attributes'], ['entry_save_uid', 'account_instance_uid', 'project_instance_uid', 'project_milestone_uid', 'invoice_instance_uid', 'entry_period', 'entry_note', 'lock_uid', 'start_date', 'end_date', 'entry_minutes', 'is_approved'])
event_channel_model = base_model('event_channel', ['id', 'event_channel_uid', 'channel_type', 'channel_name', 'channel_definition', 'row_guid', 'row_version', 'is_active', 'created_date', 'created_by', 'last_updated_date', 'last_updated_by', 'removed_date', 'removed_by', 'custom_attributes'], ['event_channel_uid', 'channel_type', 'channel_name', 'channel_definition'])
event_instance_model = base_model('event_instance', ['id', 'event_instance_uid', 'event_type', 'event_object', 'event_method', 'event_parameters', 'event_signature', 'published_count', 'event_date', 'row_guid', 'row_version', 'is_active', 'created_date', 'created_by', 'last_updated_date', 'last_updated_by', 'removed_date', 'removed_by', 'custom_attributes'], ['event_instance_uid', 'event_type', 'event_object', 'event_method', 'event_parameters', 'event_signature', 'published_count', 'event_date'])
event_subscription_model = base_model('event_subscription', ['id', 'event_subscription_uid', 'event_channel_uid', 'subscription_name', 'subscription_filter', 'subscription_topic', 'subscription_template', 'row_guid', 'row_version', 'is_active', 'created_date', 'created_by', 'last_updated_date', 'last_updated_by', 'removed_date', 'removed_by', 'custom_attributes'], ['event_subscription_uid', 'event_channel_uid', 'subscription_name', 'subscription_filter', 'subscription_topic', 'subscription_template'])
invoice_instance_model = base_model('invoice_instance', ['id', 'invoice_instance_uid', 'client_instance_uid', 'account_instance_uid', 'period_code', 'invoice_number', 'invoice_details', 'invoice_status', 'invoice_currency', 'invoice_amount', 'row_guid', 'row_version', 'is_active', 'created_date', 'created_by', 'last_updated_date', 'last_updated_by', 'removed_date', 'removed_by', 'custom_attributes'], ['invoice_instance_uid', 'client_instance_uid', 'account_instance_uid', 'period_code', 'invoice_number', 'invoice_details', 'invoice_status', 'invoice_currency', 'invoice_amount'])
notification_instance_model = base_model('notification_instance', ['id', 'notification_instance_uid', 'account_instance_uid', 'notification_type', 'notification_topic', 'notification_format', 'notification_content', 'sending_status', 'row_guid', 'row_version', 'is_active', 'created_date', 'created_by', 'last_updated_date', 'last_updated_by', 'removed_date', 'removed_by', 'custom_attributes'], ['notification_instance_uid', 'account_instance_uid', 'notification_type', 'notification_topic', 'notification_format', 'notification_content', 'sending_status'])
project_budget_model = base_model('project_budget', ['id', 'project_budget_uid', 'project_instance_uid', 'budget_name', 'budget_currency', 'budget_value', 'is_current', 'row_guid', 'row_version', 'is_active', 'created_date', 'created_by', 'last_updated_date', 'last_updated_by', 'removed_date', 'removed_by', 'custom_attributes'], ['project_budget_uid', 'project_instance_uid', 'budget_name', 'budget_currency', 'budget_value', 'is_current'])
project_group_model = base_model('project_group', ['id', 'project_group_uid', 'project_group_name', 'project_group_description', 'row_guid', 'row_version', 'is_active', 'created_date', 'created_by', 'last_updated_date', 'last_updated_by', 'removed_date', 'removed_by', 'custom_attributes'], ['project_group_uid', 'project_group_name', 'project_group_description'])
project_instance_model = base_model('project_instance', ['id', 'project_instance_uid', 'client_instance_uid', 'manager_account_instance_uid', 'project_group_uid', 'project_name', 'project_code', 'is_billable', 'start_date', 'end_date', 'current_billed', 'budget', 'row_guid', 'row_version', 'is_active', 'created_date', 'created_by', 'last_updated_date', 'last_updated_by', 'removed_date', 'removed_by', 'custom_attributes'], ['project_instance_uid', 'client_instance_uid', 'manager_account_instance_uid', 'project_group_uid', 'project_name', 'project_code', 'is_billable', 'start_date', 'end_date', 'current_billed', 'budget'])
project_milestone_model = base_model('project_milestone', ['id', 'project_milestone_uid', 'project_instance_uid', 'project_budget_uid', 'milestone_name', 'start_date', 'end_date', 'status_name', 'row_guid', 'row_version', 'is_active', 'created_date', 'created_by', 'last_updated_date', 'last_updated_by', 'removed_date', 'removed_by', 'custom_attributes'], ['project_milestone_uid', 'project_instance_uid', 'project_budget_uid', 'milestone_name', 'start_date', 'end_date', 'status_name'])
system_attribute_model = base_model('system_attribute', ['id', 'system_attribute_uid', 'system_object_uid', 'column_name', 'attribute_name', 'attribute_type', 'attribute_label', 'attribute_description', 'row_guid', 'row_version', 'is_active', 'created_date', 'created_by', 'last_updated_date', 'last_updated_by', 'removed_date', 'removed_by', 'custom_attributes'], ['system_attribute_uid', 'system_object_uid', 'column_name', 'attribute_name', 'attribute_type', 'attribute_label', 'attribute_description'])
system_change_model = base_model('system_change', ['id', 'system_change_uid', 'account_instance_uid', 'change_type', 'change_name', 'change_json', 'row_guid', 'row_version', 'is_active', 'created_date', 'created_by', 'last_updated_date', 'last_updated_by', 'removed_date', 'removed_by', 'custom_attributes'], ['system_change_uid', 'account_instance_uid', 'change_type', 'change_name', 'change_json'])
system_exception_model = base_model('system_exception', ['id', 'system_exception_uid', 'system_instance_uid', 'exception_class', 'exception_message', 'exception_stacktrace', 'row_guid', 'row_version', 'is_active', 'created_date', 'created_by', 'last_updated_date', 'last_updated_by', 'removed_date', 'removed_by', 'custom_attributes'], ['system_exception_uid', 'system_instance_uid', 'exception_class', 'exception_message', 'exception_stacktrace'])
system_instance_model = base_model('system_instance', ['id', 'system_instance_uid', 'host_name', 'host_ip', 'local_path', 'app_version', 'mode_name', 'row_guid', 'row_version', 'is_active', 'created_date', 'created_by', 'last_updated_date', 'last_updated_by', 'removed_date', 'removed_by', 'custom_attributes'], ['system_instance_uid', 'host_name', 'host_ip', 'local_path', 'app_version', 'mode_name'])
system_object_model = base_model('system_object', ['id', 'system_object_uid', 'object_name', 'object_type', 'table_name', 'key_name', 'parent_system_object_uid', 'row_guid', 'row_version', 'is_active', 'created_date', 'created_by', 'last_updated_date', 'last_updated_by', 'removed_date', 'removed_by', 'custom_attributes'], ['system_object_uid', 'object_name', 'object_type', 'table_name', 'key_name', 'parent_system_object_uid'])
system_setting_model = base_model('system_setting', ['id', 'system_setting_uid', 'account_instance_uid', 'setting_name', 'setting_value', 'row_guid', 'row_version', 'is_active', 'created_date', 'created_by', 'last_updated_date', 'last_updated_by', 'removed_date', 'removed_by', 'custom_attributes'], ['system_setting_uid', 'account_instance_uid', 'setting_name', 'setting_value'])
system_state_model = base_model('system_state', ['id', 'system_state_uid', 'system_instance_uid', 'host_name', 'host_ip', 'local_path', 'app_version', 'mode_name', 'row_guid', 'row_version', 'is_active', 'created_date', 'created_by', 'last_updated_date', 'last_updated_by', 'removed_date', 'removed_by', 'custom_attributes'], ['system_state_uid', 'system_instance_uid', 'host_name', 'host_ip', 'local_path', 'app_version', 'mode_name'])
