# auto-generated - v_definition_python_daos_list - START at 2024-03-30 02:32:00.283524+01
import logging
from logging import config
from dao.daos_full import *


class DaosList(base_object):
    all_daos: dict[str, base_dao] = {}
    account_dao_instance = account_full_dao()
    account_division_dao_instance = account_division_full_dao()
    account_division_template_dao_instance = account_division_template_full_dao()
    account_group_dao_instance = account_group_full_dao()
    account_hierarchy_dao_instance = account_hierarchy_full_dao()
    account_rate_dao_instance = account_rate_full_dao()
    account_skill_dao_instance = account_skill_full_dao()
    account_team_dao_instance = account_team_full_dao()
    account_title_dao_instance = account_title_full_dao()
    account_title_responsibility_dao_instance = account_title_responsibility_full_dao()
    account_type_dao_instance = account_type_full_dao()
    audit_change_dao_instance = audit_change_full_dao()
    audit_type_dao_instance = audit_type_full_dao()
    auth_attempt_dao_instance = auth_attempt_full_dao()
    auth_identity_dao_instance = auth_identity_full_dao()
    auth_identity_tenant_dao_instance = auth_identity_tenant_full_dao()
    auth_key_dao_instance = auth_key_full_dao()
    auth_key_type_dao_instance = auth_key_type_full_dao()
    auth_password_dao_instance = auth_password_full_dao()
    auth_password_current_dao_instance = auth_password_current_full_dao()
    auth_password_rule_dao_instance = auth_password_rule_full_dao()
    auth_permission_dao_instance = auth_permission_full_dao()
    auth_request_dao_instance = auth_request_full_dao()
    auth_role_dao_instance = auth_role_full_dao()
    auth_role_uri_dao_instance = auth_role_uri_full_dao()
    auth_session_dao_instance = auth_session_full_dao()
    auth_sso_dao_instance = auth_sso_full_dao()
    auth_token_dao_instance = auth_token_full_dao()
    calendar_account_dao_instance = calendar_account_full_dao()
    calendar_approval_dao_instance = calendar_approval_full_dao()
    calendar_approval_type_dao_instance = calendar_approval_type_full_dao()
    calendar_event_dao_instance = calendar_event_full_dao()
    calendar_event_group_dao_instance = calendar_event_group_full_dao()
    calendar_event_type_dao_instance = calendar_event_type_full_dao()
    calendar_type_dao_instance = calendar_type_full_dao()
    client_dao_instance = client_full_dao()
    client_account_dao_instance = client_account_full_dao()
    client_country_dao_instance = client_country_full_dao()
    client_payment_dao_instance = client_payment_full_dao()
    client_role_dao_instance = client_role_full_dao()
    client_status_dao_instance = client_status_full_dao()
    client_type_dao_instance = client_type_full_dao()
    connection_engine_dao_instance = connection_engine_full_dao()
    connection_host_dao_instance = connection_host_full_dao()
    connection_user_dao_instance = connection_user_full_dao()
    country_dao_instance = country_full_dao()
    currency_dao_instance = currency_full_dao()
    event_acknowledge_dao_instance = event_acknowledge_full_dao()
    event_channel_dao_instance = event_channel_full_dao()
    event_channel_type_dao_instance = event_channel_type_full_dao()
    event_instance_dao_instance = event_instance_full_dao()
    event_notification_dao_instance = event_notification_full_dao()
    event_observer_dao_instance = event_observer_full_dao()
    event_subscription_dao_instance = event_subscription_full_dao()
    event_template_dao_instance = event_template_full_dao()
    event_type_dao_instance = event_type_full_dao()
    invoice_action_dao_instance = invoice_action_full_dao()
    invoice_action_type_dao_instance = invoice_action_type_full_dao()
    invoice_category_dao_instance = invoice_category_full_dao()
    invoice_entry_dao_instance = invoice_entry_full_dao()
    invoice_flow_dao_instance = invoice_flow_full_dao()
    invoice_flow_state_dao_instance = invoice_flow_state_full_dao()
    invoice_instance_dao_instance = invoice_instance_full_dao()
    invoice_status_dao_instance = invoice_status_full_dao()
    invoice_type_dao_instance = invoice_type_full_dao()
    monitor_dao_instance = monitor_full_dao()
    monitor_run_dao_instance = monitor_run_full_dao()
    monitor_type_dao_instance = monitor_type_full_dao()
    period_dao_instance = period_full_dao()
    process_dao_instance = process_full_dao()
    process_run_dao_instance = process_run_full_dao()
    process_type_dao_instance = process_type_full_dao()
    project_account_dao_instance = project_account_full_dao()
    project_budget_dao_instance = project_budget_full_dao()
    project_group_dao_instance = project_group_full_dao()
    project_instance_dao_instance = project_instance_full_dao()
    project_milestone_dao_instance = project_milestone_full_dao()
    project_type_dao_instance = project_type_full_dao()
    report_dao_instance = report_full_dao()
    report_content_type_dao_instance = report_content_type_full_dao()
    report_format_dao_instance = report_format_full_dao()
    report_run_dao_instance = report_run_full_dao()
    report_status_dao_instance = report_status_full_dao()
    report_type_dao_instance = report_type_full_dao()
    storage_dao_instance = storage_full_dao()
    storage_connection_dao_instance = storage_connection_full_dao()
    storage_query_dao_instance = storage_query_full_dao()
    storage_type_dao_instance = storage_type_full_dao()
    synchronization_dao_instance = synchronization_full_dao()
    synchronization_run_dao_instance = synchronization_run_full_dao()
    synchronization_type_dao_instance = synchronization_type_full_dao()
    system_attribute_dao_instance = system_attribute_full_dao()
    system_database_dao_instance = system_database_full_dao()
    system_exception_dao_instance = system_exception_full_dao()
    system_instance_dao_instance = system_instance_full_dao()
    system_license_dao_instance = system_license_full_dao()
    system_lock_dao_instance = system_lock_full_dao()
    system_module_dao_instance = system_module_full_dao()
    system_object_dao_instance = system_object_full_dao()
    system_object_type_dao_instance = system_object_type_full_dao()
    system_query_dao_instance = system_query_full_dao()
    system_request_dao_instance = system_request_full_dao()
    system_setting_dao_instance = system_setting_full_dao()
    system_setting_account_dao_instance = system_setting_account_full_dao()
    system_state_dao_instance = system_state_full_dao()
    system_table_dao_instance = system_table_full_dao()
    system_thread_dao_instance = system_thread_full_dao()
    system_version_dao_instance = system_version_full_dao()
    tenant_dao_instance = tenant_full_dao()
    tenant_account_dao_instance = tenant_account_full_dao()
    tenant_category_dao_instance = tenant_category_full_dao()
    tenant_country_dao_instance = tenant_country_full_dao()
    tenant_license_dao_instance = tenant_license_full_dao()
    tenant_payment_dao_instance = tenant_payment_full_dao()
    tenant_payment_type_dao_instance = tenant_payment_type_full_dao()
    tenant_role_dao_instance = tenant_role_full_dao()
    tenant_status_dao_instance = tenant_status_full_dao()
    tenant_type_dao_instance = tenant_type_full_dao()
    time_approval_dao_instance = time_approval_full_dao()
    time_entry_dao_instance = time_entry_full_dao()
    time_entry_final_dao_instance = time_entry_final_full_dao()
    time_entry_invoice_dao_instance = time_entry_invoice_full_dao()
    time_rule_dao_instance = time_rule_full_dao()
    time_rule_client_dao_instance = time_rule_client_full_dao()
    time_submit_dao_instance = time_submit_full_dao()
    time_submit_type_dao_instance = time_submit_type_full_dao()
    def register_all_standard_daos(self):
        self.all_daos["account_dao"] = self.account_dao_instance
        self.all_daos["account_division_dao"] = self.account_division_dao_instance
        self.all_daos["account_division_template_dao"] = self.account_division_template_dao_instance
        self.all_daos["account_group_dao"] = self.account_group_dao_instance
        self.all_daos["account_hierarchy_dao"] = self.account_hierarchy_dao_instance
        self.all_daos["account_rate_dao"] = self.account_rate_dao_instance
        self.all_daos["account_skill_dao"] = self.account_skill_dao_instance
        self.all_daos["account_team_dao"] = self.account_team_dao_instance
        self.all_daos["account_title_dao"] = self.account_title_dao_instance
        self.all_daos["account_title_responsibility_dao"] = self.account_title_responsibility_dao_instance
        self.all_daos["account_type_dao"] = self.account_type_dao_instance
        self.all_daos["audit_change_dao"] = self.audit_change_dao_instance
        self.all_daos["audit_type_dao"] = self.audit_type_dao_instance
        self.all_daos["auth_attempt_dao"] = self.auth_attempt_dao_instance
        self.all_daos["auth_identity_dao"] = self.auth_identity_dao_instance
        self.all_daos["auth_identity_tenant_dao"] = self.auth_identity_tenant_dao_instance
        self.all_daos["auth_key_dao"] = self.auth_key_dao_instance
        self.all_daos["auth_key_type_dao"] = self.auth_key_type_dao_instance
        self.all_daos["auth_password_dao"] = self.auth_password_dao_instance
        self.all_daos["auth_password_current_dao"] = self.auth_password_current_dao_instance
        self.all_daos["auth_password_rule_dao"] = self.auth_password_rule_dao_instance
        self.all_daos["auth_permission_dao"] = self.auth_permission_dao_instance
        self.all_daos["auth_request_dao"] = self.auth_request_dao_instance
        self.all_daos["auth_role_dao"] = self.auth_role_dao_instance
        self.all_daos["auth_role_uri_dao"] = self.auth_role_uri_dao_instance
        self.all_daos["auth_session_dao"] = self.auth_session_dao_instance
        self.all_daos["auth_sso_dao"] = self.auth_sso_dao_instance
        self.all_daos["auth_token_dao"] = self.auth_token_dao_instance
        self.all_daos["calendar_account_dao"] = self.calendar_account_dao_instance
        self.all_daos["calendar_approval_dao"] = self.calendar_approval_dao_instance
        self.all_daos["calendar_approval_type_dao"] = self.calendar_approval_type_dao_instance
        self.all_daos["calendar_event_dao"] = self.calendar_event_dao_instance
        self.all_daos["calendar_event_group_dao"] = self.calendar_event_group_dao_instance
        self.all_daos["calendar_event_type_dao"] = self.calendar_event_type_dao_instance
        self.all_daos["calendar_type_dao"] = self.calendar_type_dao_instance
        self.all_daos["client_dao"] = self.client_dao_instance
        self.all_daos["client_account_dao"] = self.client_account_dao_instance
        self.all_daos["client_country_dao"] = self.client_country_dao_instance
        self.all_daos["client_payment_dao"] = self.client_payment_dao_instance
        self.all_daos["client_role_dao"] = self.client_role_dao_instance
        self.all_daos["client_status_dao"] = self.client_status_dao_instance
        self.all_daos["client_type_dao"] = self.client_type_dao_instance
        self.all_daos["connection_engine_dao"] = self.connection_engine_dao_instance
        self.all_daos["connection_host_dao"] = self.connection_host_dao_instance
        self.all_daos["connection_user_dao"] = self.connection_user_dao_instance
        self.all_daos["country_dao"] = self.country_dao_instance
        self.all_daos["currency_dao"] = self.currency_dao_instance
        self.all_daos["event_acknowledge_dao"] = self.event_acknowledge_dao_instance
        self.all_daos["event_channel_dao"] = self.event_channel_dao_instance
        self.all_daos["event_channel_type_dao"] = self.event_channel_type_dao_instance
        self.all_daos["event_instance_dao"] = self.event_instance_dao_instance
        self.all_daos["event_notification_dao"] = self.event_notification_dao_instance
        self.all_daos["event_observer_dao"] = self.event_observer_dao_instance
        self.all_daos["event_subscription_dao"] = self.event_subscription_dao_instance
        self.all_daos["event_template_dao"] = self.event_template_dao_instance
        self.all_daos["event_type_dao"] = self.event_type_dao_instance
        self.all_daos["invoice_action_dao"] = self.invoice_action_dao_instance
        self.all_daos["invoice_action_type_dao"] = self.invoice_action_type_dao_instance
        self.all_daos["invoice_category_dao"] = self.invoice_category_dao_instance
        self.all_daos["invoice_entry_dao"] = self.invoice_entry_dao_instance
        self.all_daos["invoice_flow_dao"] = self.invoice_flow_dao_instance
        self.all_daos["invoice_flow_state_dao"] = self.invoice_flow_state_dao_instance
        self.all_daos["invoice_instance_dao"] = self.invoice_instance_dao_instance
        self.all_daos["invoice_status_dao"] = self.invoice_status_dao_instance
        self.all_daos["invoice_type_dao"] = self.invoice_type_dao_instance
        self.all_daos["monitor_dao"] = self.monitor_dao_instance
        self.all_daos["monitor_run_dao"] = self.monitor_run_dao_instance
        self.all_daos["monitor_type_dao"] = self.monitor_type_dao_instance
        self.all_daos["period_dao"] = self.period_dao_instance
        self.all_daos["process_dao"] = self.process_dao_instance
        self.all_daos["process_run_dao"] = self.process_run_dao_instance
        self.all_daos["process_type_dao"] = self.process_type_dao_instance
        self.all_daos["project_account_dao"] = self.project_account_dao_instance
        self.all_daos["project_budget_dao"] = self.project_budget_dao_instance
        self.all_daos["project_group_dao"] = self.project_group_dao_instance
        self.all_daos["project_instance_dao"] = self.project_instance_dao_instance
        self.all_daos["project_milestone_dao"] = self.project_milestone_dao_instance
        self.all_daos["project_type_dao"] = self.project_type_dao_instance
        self.all_daos["report_dao"] = self.report_dao_instance
        self.all_daos["report_content_type_dao"] = self.report_content_type_dao_instance
        self.all_daos["report_format_dao"] = self.report_format_dao_instance
        self.all_daos["report_run_dao"] = self.report_run_dao_instance
        self.all_daos["report_status_dao"] = self.report_status_dao_instance
        self.all_daos["report_type_dao"] = self.report_type_dao_instance
        self.all_daos["storage_dao"] = self.storage_dao_instance
        self.all_daos["storage_connection_dao"] = self.storage_connection_dao_instance
        self.all_daos["storage_query_dao"] = self.storage_query_dao_instance
        self.all_daos["storage_type_dao"] = self.storage_type_dao_instance
        self.all_daos["synchronization_dao"] = self.synchronization_dao_instance
        self.all_daos["synchronization_run_dao"] = self.synchronization_run_dao_instance
        self.all_daos["synchronization_type_dao"] = self.synchronization_type_dao_instance
        self.all_daos["system_attribute_dao"] = self.system_attribute_dao_instance
        self.all_daos["system_database_dao"] = self.system_database_dao_instance
        self.all_daos["system_exception_dao"] = self.system_exception_dao_instance
        self.all_daos["system_instance_dao"] = self.system_instance_dao_instance
        self.all_daos["system_license_dao"] = self.system_license_dao_instance
        self.all_daos["system_lock_dao"] = self.system_lock_dao_instance
        self.all_daos["system_module_dao"] = self.system_module_dao_instance
        self.all_daos["system_object_dao"] = self.system_object_dao_instance
        self.all_daos["system_object_type_dao"] = self.system_object_type_dao_instance
        self.all_daos["system_query_dao"] = self.system_query_dao_instance
        self.all_daos["system_request_dao"] = self.system_request_dao_instance
        self.all_daos["system_setting_dao"] = self.system_setting_dao_instance
        self.all_daos["system_setting_account_dao"] = self.system_setting_account_dao_instance
        self.all_daos["system_state_dao"] = self.system_state_dao_instance
        self.all_daos["system_table_dao"] = self.system_table_dao_instance
        self.all_daos["system_thread_dao"] = self.system_thread_dao_instance
        self.all_daos["system_version_dao"] = self.system_version_dao_instance
        self.all_daos["tenant_dao"] = self.tenant_dao_instance
        self.all_daos["tenant_account_dao"] = self.tenant_account_dao_instance
        self.all_daos["tenant_category_dao"] = self.tenant_category_dao_instance
        self.all_daos["tenant_country_dao"] = self.tenant_country_dao_instance
        self.all_daos["tenant_license_dao"] = self.tenant_license_dao_instance
        self.all_daos["tenant_payment_dao"] = self.tenant_payment_dao_instance
        self.all_daos["tenant_payment_type_dao"] = self.tenant_payment_type_dao_instance
        self.all_daos["tenant_role_dao"] = self.tenant_role_dao_instance
        self.all_daos["tenant_status_dao"] = self.tenant_status_dao_instance
        self.all_daos["tenant_type_dao"] = self.tenant_type_dao_instance
        self.all_daos["time_approval_dao"] = self.time_approval_dao_instance
        self.all_daos["time_entry_dao"] = self.time_entry_dao_instance
        self.all_daos["time_entry_final_dao"] = self.time_entry_final_dao_instance
        self.all_daos["time_entry_invoice_dao"] = self.time_entry_invoice_dao_instance
        self.all_daos["time_rule_dao"] = self.time_rule_dao_instance
        self.all_daos["time_rule_client_dao"] = self.time_rule_client_dao_instance
        self.all_daos["time_submit_dao"] = self.time_submit_dao_instance
        self.all_daos["time_submit_type_dao"] = self.time_submit_type_dao_instance
# auto-generated - v_definition_python_daos_list - END