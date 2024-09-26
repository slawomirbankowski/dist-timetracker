# auto-generated - v_definition_python_services_object - START at 2024-03-30 03:38:48.881308+01
import dao.dao_connection
from dao.daos_read import *
from backend.service import service_base
from backend.dao.daos import daos
from dao.daos_full import *

db_connections = dao.dao_connection.db_connections


class account_service(service_base):
    dao: account_full_dao = daos.account_dao_instance
    def __init__(self):
        super().__init__()


class account_division_service(service_base):
    dao: account_division_full_dao = daos.account_division_dao_instance
    def __init__(self):
        super().__init__()


class account_division_template_service(service_base):
    dao: account_division_template_full_dao = daos.account_division_template_dao_instance
    def __init__(self):
        super().__init__()


class account_group_service(service_base):
    dao: account_group_full_dao = daos.account_group_dao_instance
    def __init__(self):
        super().__init__()


class account_hierarchy_service(service_base):
    dao: account_hierarchy_full_dao = daos.account_hierarchy_dao_instance
    def __init__(self):
        super().__init__()


class account_rate_service(service_base):
    dao: account_rate_full_dao = daos.account_rate_dao_instance
    def __init__(self):
        super().__init__()


class account_skill_service(service_base):
    dao: account_skill_full_dao = daos.account_skill_dao_instance
    def __init__(self):
        super().__init__()


class account_team_service(service_base):
    dao: account_team_full_dao = daos.account_team_dao_instance
    def __init__(self):
        super().__init__()


class account_title_service(service_base):
    dao: account_title_full_dao = daos.account_title_dao_instance
    def __init__(self):
        super().__init__()


class account_title_responsibility_service(service_base):
    dao: account_title_responsibility_full_dao = daos.account_title_responsibility_dao_instance
    def __init__(self):
        super().__init__()


class account_type_service(service_base):
    dao: account_type_full_dao = daos.account_type_dao_instance
    def __init__(self):
        super().__init__()


class audit_change_service(service_base):
    dao: audit_change_full_dao = daos.audit_change_dao_instance
    def __init__(self):
        super().__init__()


class audit_type_service(service_base):
    dao: audit_type_full_dao = daos.audit_type_dao_instance
    def __init__(self):
        super().__init__()


class auth_attempt_service(service_base):
    dao: auth_attempt_full_dao = daos.auth_attempt_dao_instance
    def __init__(self):
        super().__init__()


class auth_identity_service(service_base):
    dao: auth_identity_full_dao = daos.auth_identity_dao_instance
    def __init__(self):
        super().__init__()


class auth_identity_tenant_service(service_base):
    dao: auth_identity_tenant_full_dao = daos.auth_identity_tenant_dao_instance
    def __init__(self):
        super().__init__()


class auth_key_service(service_base):
    dao: auth_key_full_dao = daos.auth_key_dao_instance
    def __init__(self):
        super().__init__()


class auth_key_type_service(service_base):
    dao: auth_key_type_full_dao = daos.auth_key_type_dao_instance
    def __init__(self):
        super().__init__()


class auth_password_service(service_base):
    dao: auth_password_full_dao = daos.auth_password_dao_instance
    def __init__(self):
        super().__init__()


class auth_password_current_service(service_base):
    dao: auth_password_current_full_dao = daos.auth_password_current_dao_instance
    def __init__(self):
        super().__init__()


class auth_password_rule_service(service_base):
    dao: auth_password_rule_full_dao = daos.auth_password_rule_dao_instance
    def __init__(self):
        super().__init__()


class auth_permission_service(service_base):
    dao: auth_permission_full_dao = daos.auth_permission_dao_instance
    def __init__(self):
        super().__init__()


class auth_request_service(service_base):
    dao: auth_request_full_dao = daos.auth_request_dao_instance
    def __init__(self):
        super().__init__()


class auth_role_service(service_base):
    dao: auth_role_full_dao = daos.auth_role_dao_instance
    def __init__(self):
        super().__init__()


class auth_role_uri_service(service_base):
    dao: auth_role_uri_full_dao = daos.auth_role_uri_dao_instance
    def __init__(self):
        super().__init__()


class auth_session_service(service_base):
    dao: auth_session_full_dao = daos.auth_session_dao_instance
    def __init__(self):
        super().__init__()


class auth_sso_service(service_base):
    dao: auth_sso_full_dao = daos.auth_sso_dao_instance
    def __init__(self):
        super().__init__()


class auth_token_service(service_base):
    dao: auth_token_full_dao = daos.auth_token_dao_instance
    def __init__(self):
        super().__init__()


class calendar_account_service(service_base):
    dao: calendar_account_full_dao = daos.calendar_account_dao_instance
    def __init__(self):
        super().__init__()


class calendar_approval_service(service_base):
    dao: calendar_approval_full_dao = daos.calendar_approval_dao_instance
    def __init__(self):
        super().__init__()


class calendar_approval_type_service(service_base):
    dao: calendar_approval_type_full_dao = daos.calendar_approval_type_dao_instance
    def __init__(self):
        super().__init__()


class calendar_event_service(service_base):
    dao: calendar_event_full_dao = daos.calendar_event_dao_instance
    def __init__(self):
        super().__init__()


class calendar_event_group_service(service_base):
    dao: calendar_event_group_full_dao = daos.calendar_event_group_dao_instance
    def __init__(self):
        super().__init__()


class calendar_event_type_service(service_base):
    dao: calendar_event_type_full_dao = daos.calendar_event_type_dao_instance
    def __init__(self):
        super().__init__()


class calendar_type_service(service_base):
    dao: calendar_type_full_dao = daos.calendar_type_dao_instance
    def __init__(self):
        super().__init__()


class client_service(service_base):
    dao: client_full_dao = daos.client_dao_instance
    def __init__(self):
        super().__init__()


class client_account_service(service_base):
    dao: client_account_full_dao = daos.client_account_dao_instance
    def __init__(self):
        super().__init__()


class client_country_service(service_base):
    dao: client_country_full_dao = daos.client_country_dao_instance
    def __init__(self):
        super().__init__()


class client_payment_service(service_base):
    dao: client_payment_full_dao = daos.client_payment_dao_instance
    def __init__(self):
        super().__init__()


class client_role_service(service_base):
    dao: client_role_full_dao = daos.client_role_dao_instance
    def __init__(self):
        super().__init__()


class client_status_service(service_base):
    dao: client_status_full_dao = daos.client_status_dao_instance
    def __init__(self):
        super().__init__()


class client_type_service(service_base):
    dao: client_type_full_dao = daos.client_type_dao_instance
    def __init__(self):
        super().__init__()


class connection_engine_service(service_base):
    dao: connection_engine_full_dao = daos.connection_engine_dao_instance
    def __init__(self):
        super().__init__()


class connection_host_service(service_base):
    dao: connection_host_full_dao = daos.connection_host_dao_instance
    def __init__(self):
        super().__init__()


class connection_user_service(service_base):
    dao: connection_user_full_dao = daos.connection_user_dao_instance
    def __init__(self):
        super().__init__()


class country_service(service_base):
    dao: country_full_dao = daos.country_dao_instance
    def __init__(self):
        super().__init__()


class currency_service(service_base):
    dao: currency_full_dao = daos.currency_dao_instance
    def __init__(self):
        super().__init__()


class event_acknowledge_service(service_base):
    dao: event_acknowledge_full_dao = daos.event_acknowledge_dao_instance
    def __init__(self):
        super().__init__()


class event_channel_service(service_base):
    dao: event_channel_full_dao = daos.event_channel_dao_instance
    def __init__(self):
        super().__init__()


class event_channel_type_service(service_base):
    dao: event_channel_type_full_dao = daos.event_channel_type_dao_instance
    def __init__(self):
        super().__init__()


class event_instance_service(service_base):
    dao: event_instance_full_dao = daos.event_instance_dao_instance
    def __init__(self):
        super().__init__()


class event_notification_service(service_base):
    dao: event_notification_full_dao = daos.event_notification_dao_instance
    def __init__(self):
        super().__init__()


class event_observer_service(service_base):
    dao: event_observer_full_dao = daos.event_observer_dao_instance
    def __init__(self):
        super().__init__()


class event_subscription_service(service_base):
    dao: event_subscription_full_dao = daos.event_subscription_dao_instance
    def __init__(self):
        super().__init__()


class event_template_service(service_base):
    dao: event_template_full_dao = daos.event_template_dao_instance
    def __init__(self):
        super().__init__()


class event_type_service(service_base):
    dao: event_type_full_dao = daos.event_type_dao_instance
    def __init__(self):
        super().__init__()


class invoice_action_service(service_base):
    dao: invoice_action_full_dao = daos.invoice_action_dao_instance
    def __init__(self):
        super().__init__()


class invoice_action_type_service(service_base):
    dao: invoice_action_type_full_dao = daos.invoice_action_type_dao_instance
    def __init__(self):
        super().__init__()


class invoice_category_service(service_base):
    dao: invoice_category_full_dao = daos.invoice_category_dao_instance
    def __init__(self):
        super().__init__()


class invoice_entry_service(service_base):
    dao: invoice_entry_full_dao = daos.invoice_entry_dao_instance
    def __init__(self):
        super().__init__()


class invoice_flow_service(service_base):
    dao: invoice_flow_full_dao = daos.invoice_flow_dao_instance
    def __init__(self):
        super().__init__()


class invoice_flow_state_service(service_base):
    dao: invoice_flow_state_full_dao = daos.invoice_flow_state_dao_instance
    def __init__(self):
        super().__init__()


class invoice_instance_service(service_base):
    dao: invoice_instance_full_dao = daos.invoice_instance_dao_instance
    def __init__(self):
        super().__init__()


class invoice_status_service(service_base):
    dao: invoice_status_full_dao = daos.invoice_status_dao_instance
    def __init__(self):
        super().__init__()


class invoice_type_service(service_base):
    dao: invoice_type_full_dao = daos.invoice_type_dao_instance
    def __init__(self):
        super().__init__()


class monitor_service(service_base):
    dao: monitor_full_dao = daos.monitor_dao_instance
    def __init__(self):
        super().__init__()


class monitor_run_service(service_base):
    dao: monitor_run_full_dao = daos.monitor_run_dao_instance
    def __init__(self):
        super().__init__()


class monitor_type_service(service_base):
    dao: monitor_type_full_dao = daos.monitor_type_dao_instance
    def __init__(self):
        super().__init__()


class period_service(service_base):
    dao: period_full_dao = daos.period_dao_instance
    def __init__(self):
        super().__init__()


class process_service(service_base):
    dao: process_full_dao = daos.process_dao_instance
    def __init__(self):
        super().__init__()


class process_run_service(service_base):
    dao: process_run_full_dao = daos.process_run_dao_instance
    def __init__(self):
        super().__init__()


class process_type_service(service_base):
    dao: process_type_full_dao = daos.process_type_dao_instance
    def __init__(self):
        super().__init__()


class project_account_service(service_base):
    dao: project_account_full_dao = daos.project_account_dao_instance
    def __init__(self):
        super().__init__()


class project_budget_service(service_base):
    dao: project_budget_full_dao = daos.project_budget_dao_instance
    def __init__(self):
        super().__init__()


class project_group_service(service_base):
    dao: project_group_full_dao = daos.project_group_dao_instance
    def __init__(self):
        super().__init__()


class project_instance_service(service_base):
    dao: project_instance_full_dao = daos.project_instance_dao_instance
    def __init__(self):
        super().__init__()


class project_milestone_service(service_base):
    dao: project_milestone_full_dao = daos.project_milestone_dao_instance
    def __init__(self):
        super().__init__()


class project_type_service(service_base):
    dao: project_type_full_dao = daos.project_type_dao_instance
    def __init__(self):
        super().__init__()


class report_service(service_base):
    dao: report_full_dao = daos.report_dao_instance
    def __init__(self):
        super().__init__()


class report_content_type_service(service_base):
    dao: report_content_type_full_dao = daos.report_content_type_dao_instance
    def __init__(self):
        super().__init__()


class report_format_service(service_base):
    dao: report_format_full_dao = daos.report_format_dao_instance
    def __init__(self):
        super().__init__()


class report_run_service(service_base):
    dao: report_run_full_dao = daos.report_run_dao_instance
    def __init__(self):
        super().__init__()


class report_status_service(service_base):
    dao: report_status_full_dao = daos.report_status_dao_instance
    def __init__(self):
        super().__init__()


class report_type_service(service_base):
    dao: report_type_full_dao = daos.report_type_dao_instance
    def __init__(self):
        super().__init__()


class storage_service(service_base):
    dao: storage_full_dao = daos.storage_dao_instance
    def __init__(self):
        super().__init__()


class storage_connection_service(service_base):
    dao: storage_connection_full_dao = daos.storage_connection_dao_instance
    def __init__(self):
        super().__init__()


class storage_query_service(service_base):
    dao: storage_query_full_dao = daos.storage_query_dao_instance
    def __init__(self):
        super().__init__()


class storage_type_service(service_base):
    dao: storage_type_full_dao = daos.storage_type_dao_instance
    def __init__(self):
        super().__init__()


class synchronization_service(service_base):
    dao: synchronization_full_dao = daos.synchronization_dao_instance
    def __init__(self):
        super().__init__()


class synchronization_run_service(service_base):
    dao: synchronization_run_full_dao = daos.synchronization_run_dao_instance
    def __init__(self):
        super().__init__()


class synchronization_type_service(service_base):
    dao: synchronization_type_full_dao = daos.synchronization_type_dao_instance
    def __init__(self):
        super().__init__()


class system_attribute_service(service_base):
    dao: system_attribute_full_dao = daos.system_attribute_dao_instance
    def __init__(self):
        super().__init__()


class system_database_service(service_base):
    dao: system_database_full_dao = daos.system_database_dao_instance
    def __init__(self):
        super().__init__()


class system_exception_service(service_base):
    dao: system_exception_full_dao = daos.system_exception_dao_instance
    def __init__(self):
        super().__init__()


class system_instance_service(service_base):
    dao: system_instance_full_dao = daos.system_instance_dao_instance
    def __init__(self):
        super().__init__()


class system_license_service(service_base):
    dao: system_license_full_dao = daos.system_license_dao_instance
    def __init__(self):
        super().__init__()


class system_lock_service(service_base):
    dao: system_lock_full_dao = daos.system_lock_dao_instance
    def __init__(self):
        super().__init__()


class system_module_service(service_base):
    dao: system_module_full_dao = daos.system_module_dao_instance
    def __init__(self):
        super().__init__()


class system_query_service(service_base):
    dao: system_query_full_dao = daos.system_query_dao_instance
    def __init__(self):
        super().__init__()


class system_request_service(service_base):
    dao: system_request_full_dao = daos.system_request_dao_instance
    def __init__(self):
        super().__init__()


class system_setting_service(service_base):
    dao: system_setting_full_dao = daos.system_setting_dao_instance
    def __init__(self):
        super().__init__()


class system_setting_account_service(service_base):
    dao: system_setting_account_full_dao = daos.system_setting_account_dao_instance
    def __init__(self):
        super().__init__()


class system_state_service(service_base):
    dao: system_state_full_dao = daos.system_state_dao_instance
    def __init__(self):
        super().__init__()


class system_table_service(service_base):
    dao: system_table_full_dao = daos.system_table_dao_instance
    def __init__(self):
        super().__init__()


class system_thread_service(service_base):
    dao: system_thread_full_dao = daos.system_thread_dao_instance
    def __init__(self):
        super().__init__()


class system_version_service(service_base):
    dao: system_version_full_dao = daos.system_version_dao_instance
    def __init__(self):
        super().__init__()


class tenant_service(service_base):
    dao: tenant_full_dao = daos.tenant_dao_instance
    def __init__(self):
        super().__init__()


class tenant_account_service(service_base):
    dao: tenant_account_full_dao = daos.tenant_account_dao_instance
    def __init__(self):
        super().__init__()


class tenant_category_service(service_base):
    dao: tenant_category_full_dao = daos.tenant_category_dao_instance
    def __init__(self):
        super().__init__()


class tenant_country_service(service_base):
    dao: tenant_country_full_dao = daos.tenant_country_dao_instance
    def __init__(self):
        super().__init__()


class tenant_license_service(service_base):
    dao: tenant_license_full_dao = daos.tenant_license_dao_instance
    def __init__(self):
        super().__init__()


class tenant_payment_service(service_base):
    dao: tenant_payment_full_dao = daos.tenant_payment_dao_instance
    def __init__(self):
        super().__init__()


class tenant_payment_type_service(service_base):
    dao: tenant_payment_type_full_dao = daos.tenant_payment_type_dao_instance
    def __init__(self):
        super().__init__()


class tenant_role_service(service_base):
    dao: tenant_role_full_dao = daos.tenant_role_dao_instance
    def __init__(self):
        super().__init__()


class tenant_status_service(service_base):
    dao: tenant_status_full_dao = daos.tenant_status_dao_instance
    def __init__(self):
        super().__init__()


class tenant_type_service(service_base):
    dao: tenant_type_full_dao = daos.tenant_type_dao_instance
    def __init__(self):
        super().__init__()


class time_approval_service(service_base):
    dao: time_approval_full_dao = daos.time_approval_dao_instance
    def __init__(self):
        super().__init__()


class time_entry_service(service_base):
    dao: time_entry_full_dao = daos.time_entry_dao_instance
    def __init__(self):
        super().__init__()


class time_entry_final_service(service_base):
    dao: time_entry_final_full_dao = daos.time_entry_final_dao_instance
    def __init__(self):
        super().__init__()


class time_entry_invoice_service(service_base):
    dao: time_entry_invoice_full_dao = daos.time_entry_invoice_dao_instance
    def __init__(self):
        super().__init__()


class time_rule_service(service_base):
    dao: time_rule_full_dao = daos.time_rule_dao_instance
    def __init__(self):
        super().__init__()


class time_rule_client_service(service_base):
    dao: time_rule_client_full_dao = daos.time_rule_client_dao_instance
    def __init__(self):
        super().__init__()



class time_submit_service(service_base):
    dao: time_submit_full_dao = daos.time_submit_dao_instance
    def __init__(self):
        super().__init__()


class time_submit_type_service(service_base):
    dao: time_submit_type_full_dao = daos.time_submit_type_dao_instance
    def __init__(self):
        super().__init__()

