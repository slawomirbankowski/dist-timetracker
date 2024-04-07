# auto-generated - v_definition_python_daos_full - START at 2024-03-29 22:52:27.127868+01
from typing import TypeVar, Generic, List, Iterable
import logging
from logging import config
import dao.dao_connection
from dao.dao_base import base_dao
from dao.daos_read import *
from dto.dtos_models import db_models
db_connections = dao.dao_connection.db_connections


class account_full_dao(account_dao):
    def __init__(self):
        super().__init__()
    def get_account_by_name(self, username: str) -> account_read_dto | None:
        return self.select_rows_read_by_query("select * from account where account_uid=%s or account_name=%s or account_email=%s order by created_date desc limit 1", [username, username, username]).get_first()


class account_division_full_dao(account_division_dao):
    def __init__(self):
        super().__init__()


class account_division_template_full_dao(account_division_template_dao):
    def __init__(self):
        super().__init__()


class account_group_full_dao(account_group_dao):
    def __init__(self):
        super().__init__()


class account_hierarchy_full_dao(account_hierarchy_dao):
    def __init__(self):
        super().__init__()


class account_rate_full_dao(account_rate_dao):
    def __init__(self):
        super().__init__()


class account_skill_full_dao(account_skill_dao):
    def __init__(self):
        super().__init__()


class account_team_full_dao(account_team_dao):
    def __init__(self):
        super().__init__()


class account_title_full_dao(account_title_dao):
    def __init__(self):
        super().__init__()


class account_title_responsibility_full_dao(account_title_responsibility_dao):
    def __init__(self):
        super().__init__()


class account_type_full_dao(account_type_dao):
    def __init__(self):
        super().__init__()


class audit_change_full_dao(audit_change_dao):
    def __init__(self):
        super().__init__()


class audit_type_full_dao(audit_type_dao):
    def __init__(self):
        super().__init__()


class auth_attempt_full_dao(auth_attempt_dao):
    def __init__(self):
        super().__init__()


class auth_identity_full_dao(auth_identity_dao):
    def __init__(self):
        super().__init__()


class auth_identity_tenant_full_dao(auth_identity_tenant_dao):
    def __init__(self):
        super().__init__()


class auth_key_full_dao(auth_key_dao):
    def __init__(self):
        super().__init__()


class auth_key_type_full_dao(auth_key_type_dao):
    def __init__(self):
        super().__init__()


class auth_password_full_dao(auth_password_dao):
    def __init__(self):
        super().__init__()
    def set_password(self, tenant_uid: str, account_uid: str, password_hash: str, password_salt: str) -> int:
        #self.with_connection_commit()
        date_to = datetime.datetime.now() + datetime.timedelta(days=30)  # max valid time = 30 days
        self.execute_query("update auth_password set is_active=0, removed_by='', removed_date=now() where is_active=1 and account_uid=%d", [account_uid])
        return self.insert_row_random_uid("name", tenant_uid, account_uid,
                                                                  password_hash, password_salt, datetime.datetime.now(),
                                                                  date_to, 0)


class auth_password_current_full_dao(auth_password_current_dao):
    def __init__(self):
        super().__init__()


class auth_password_rule_full_dao(auth_password_rule_dao):
    def __init__(self):
        super().__init__()


class auth_permission_full_dao(auth_permission_dao):
    def __init__(self):
        super().__init__()


class auth_request_full_dao(auth_request_dao):
    def __init__(self):
        super().__init__()


class auth_role_full_dao(auth_role_dao):
    def __init__(self):
        super().__init__()


class auth_role_uri_full_dao(auth_role_uri_dao):
    def __init__(self):
        super().__init__()


class auth_session_full_dao(auth_session_dao):
    def __init__(self):
        super().__init__()


class auth_sso_full_dao(auth_sso_dao):
    def __init__(self):
        super().__init__()


class auth_token_full_dao(auth_token_dao):
    def __init__(self):
        super().__init__()


class calendar_account_full_dao(calendar_account_dao):
    def __init__(self):
        super().__init__()


class calendar_approval_full_dao(calendar_approval_dao):
    def __init__(self):
        super().__init__()


class calendar_approval_type_full_dao(calendar_approval_type_dao):
    def __init__(self):
        super().__init__()


class calendar_event_full_dao(calendar_event_dao):
    def __init__(self):
        super().__init__()


class calendar_event_group_full_dao(calendar_event_group_dao):
    def __init__(self):
        super().__init__()


class calendar_event_type_full_dao(calendar_event_type_dao):
    def __init__(self):
        super().__init__()


class calendar_type_full_dao(calendar_type_dao):
    def __init__(self):
        super().__init__()


class client_full_dao(client_dao):
    def __init__(self):
        super().__init__()


class client_account_full_dao(client_account_dao):
    def __init__(self):
        super().__init__()


class client_country_full_dao(client_country_dao):
    def __init__(self):
        super().__init__()


class client_payment_full_dao(client_payment_dao):
    def __init__(self):
        super().__init__()


class client_role_full_dao(client_role_dao):
    def __init__(self):
        super().__init__()


class client_status_full_dao(client_status_dao):
    def __init__(self):
        super().__init__()


class client_type_full_dao(client_type_dao):
    def __init__(self):
        super().__init__()


class connection_engine_full_dao(connection_engine_dao):
    def __init__(self):
        super().__init__()


class connection_host_full_dao(connection_host_dao):
    def __init__(self):
        super().__init__()


class connection_user_full_dao(connection_user_dao):
    def __init__(self):
        super().__init__()


class country_full_dao(country_dao):
    def __init__(self):
        super().__init__()


class currency_full_dao(currency_dao):
    def __init__(self):
        super().__init__()


class event_acknowledge_full_dao(event_acknowledge_dao):
    def __init__(self):
        super().__init__()


class event_channel_full_dao(event_channel_dao):
    def __init__(self):
        super().__init__()


class event_channel_type_full_dao(event_channel_type_dao):
    def __init__(self):
        super().__init__()


class event_instance_full_dao(event_instance_dao):
    def __init__(self):
        super().__init__()


class event_notification_full_dao(event_notification_dao):
    def __init__(self):
        super().__init__()


class event_observer_full_dao(event_observer_dao):
    def __init__(self):
        super().__init__()


class event_subscription_full_dao(event_subscription_dao):
    def __init__(self):
        super().__init__()


class event_template_full_dao(event_template_dao):
    def __init__(self):
        super().__init__()


class event_type_full_dao(event_type_dao):
    def __init__(self):
        super().__init__()


class invoice_action_full_dao(invoice_action_dao):
    def __init__(self):
        super().__init__()


class invoice_action_type_full_dao(invoice_action_type_dao):
    def __init__(self):
        super().__init__()


class invoice_category_full_dao(invoice_category_dao):
    def __init__(self):
        super().__init__()


class invoice_entry_full_dao(invoice_entry_dao):
    def __init__(self):
        super().__init__()


class invoice_flow_full_dao(invoice_flow_dao):
    def __init__(self):
        super().__init__()


class invoice_flow_state_full_dao(invoice_flow_state_dao):
    def __init__(self):
        super().__init__()


class invoice_instance_full_dao(invoice_instance_dao):
    def __init__(self):
        super().__init__()


class invoice_status_full_dao(invoice_status_dao):
    def __init__(self):
        super().__init__()


class invoice_type_full_dao(invoice_type_dao):
    def __init__(self):
        super().__init__()


class monitor_full_dao(monitor_dao):
    def __init__(self):
        super().__init__()


class monitor_run_full_dao(monitor_run_dao):
    def __init__(self):
        super().__init__()


class monitor_type_full_dao(monitor_type_dao):
    def __init__(self):
        super().__init__()


class period_full_dao(period_dao):
    def __init__(self):
        super().__init__()


class process_full_dao(process_dao):
    def __init__(self):
        super().__init__()


class process_run_full_dao(process_run_dao):
    def __init__(self):
        super().__init__()


class process_type_full_dao(process_type_dao):
    def __init__(self):
        super().__init__()


class project_account_full_dao(project_account_dao):
    def __init__(self):
        super().__init__()


class project_budget_full_dao(project_budget_dao):
    def __init__(self):
        super().__init__()


class project_group_full_dao(project_group_dao):
    def __init__(self):
        super().__init__()


class project_instance_full_dao(project_instance_dao):
    def __init__(self):
        super().__init__()


class project_milestone_full_dao(project_milestone_dao):
    def __init__(self):
        super().__init__()


class project_type_full_dao(project_type_dao):
    def __init__(self):
        super().__init__()


class report_full_dao(report_dao):
    def __init__(self):
        super().__init__()


class report_content_type_full_dao(report_content_type_dao):
    def __init__(self):
        super().__init__()


class report_format_full_dao(report_format_dao):
    def __init__(self):
        super().__init__()


class report_run_full_dao(report_run_dao):
    def __init__(self):
        super().__init__()


class report_status_full_dao(report_status_dao):
    def __init__(self):
        super().__init__()


class report_type_full_dao(report_type_dao):
    def __init__(self):
        super().__init__()


class storage_full_dao(storage_dao):
    def __init__(self):
        super().__init__()


class storage_connection_full_dao(storage_connection_dao):
    def __init__(self):
        super().__init__()


class storage_query_full_dao(storage_query_dao):
    def __init__(self):
        super().__init__()


class storage_type_full_dao(storage_type_dao):
    def __init__(self):
        super().__init__()


class synchronization_full_dao(synchronization_dao):
    def __init__(self):
        super().__init__()


class synchronization_run_full_dao(synchronization_run_dao):
    def __init__(self):
        super().__init__()


class synchronization_type_full_dao(synchronization_type_dao):
    def __init__(self):
        super().__init__()


class system_attribute_full_dao(system_attribute_dao):
    def __init__(self):
        super().__init__()


class system_database_full_dao(system_database_dao):
    def __init__(self):
        super().__init__()


class system_exception_full_dao(system_exception_dao):
    def __init__(self):
        super().__init__()


class system_instance_full_dao(system_instance_dao):
    def __init__(self):
        super().__init__()


class system_license_full_dao(system_license_dao):
    def __init__(self):
        super().__init__()


class system_lock_full_dao(system_lock_dao):
    def __init__(self):
        super().__init__()


class system_module_full_dao(system_module_dao):
    def __init__(self):
        super().__init__()


class system_object_full_dao(system_object_dao):
    def __init__(self):
        super().__init__()


class system_object_type_full_dao(system_object_type_dao):
    def __init__(self):
        super().__init__()


class system_query_full_dao(system_query_dao):
    def __init__(self):
        super().__init__()


class system_request_full_dao(system_request_dao):
    def __init__(self):
        super().__init__()


class system_setting_full_dao(system_setting_dao):
    def __init__(self):
        super().__init__()


class system_setting_account_full_dao(system_setting_account_dao):
    def __init__(self):
        super().__init__()


class system_state_full_dao(system_state_dao):
    def __init__(self):
        super().__init__()


class system_table_full_dao(system_table_dao):
    def __init__(self):
        super().__init__()


class system_thread_full_dao(system_thread_dao):
    def __init__(self):
        super().__init__()


class system_version_full_dao(system_version_dao):
    def __init__(self):
        super().__init__()


class tenant_full_dao(tenant_dao):
    def __init__(self):
        super().__init__()


class tenant_account_full_dao(tenant_account_dao):
    def __init__(self):
        super().__init__()


class tenant_category_full_dao(tenant_category_dao):
    def __init__(self):
        super().__init__()


class tenant_country_full_dao(tenant_country_dao):
    def __init__(self):
        super().__init__()


class tenant_license_full_dao(tenant_license_dao):
    def __init__(self):
        super().__init__()


class tenant_payment_full_dao(tenant_payment_dao):
    def __init__(self):
        super().__init__()


class tenant_payment_type_full_dao(tenant_payment_type_dao):
    def __init__(self):
        super().__init__()


class tenant_role_full_dao(tenant_role_dao):
    def __init__(self):
        super().__init__()


class tenant_status_full_dao(tenant_status_dao):
    def __init__(self):
        super().__init__()


class tenant_type_full_dao(tenant_type_dao):
    def __init__(self):
        super().__init__()


class time_approval_full_dao(time_approval_dao):
    def __init__(self):
        super().__init__()


class time_entry_full_dao(time_entry_dao):
    def __init__(self):
        super().__init__()


class time_entry_final_full_dao(time_entry_final_dao):
    def __init__(self):
        super().__init__()


class time_entry_invoice_full_dao(time_entry_invoice_dao):
    def __init__(self):
        super().__init__()


class time_rule_full_dao(time_rule_dao):
    def __init__(self):
        super().__init__()


class time_rule_client_full_dao(time_rule_client_dao):
    def __init__(self):
        super().__init__()


class time_submit_full_dao(time_submit_dao):
    def __init__(self):
        super().__init__()


class time_submit_type_full_dao(time_submit_type_dao):
    def __init__(self):
        super().__init__()

