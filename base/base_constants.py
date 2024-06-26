import datetime
import uuid
import random
import logging
from logging import config

application_start_date = datetime.datetime.now()
logging.config.fileConfig('logging.conf')
logging.info(f"=================================================== STARTING at {str(application_start_date)} ")
logging.info("Initializing Logging in application")


class SystemVersions:
    FirstVersion: str = "1.0.0"
    Latest: str = "1.0.0"


class SystemDatabases:
    timetracker: str = "timetracker"


class SystemObjectTypes:
    system: str = ""
    dictionary: str = "dictionary"
    data: str = "data"
    append: str = "append"
    m2m: str = "m2m"


class SystemSettings:
    dao_max_rows: str = "dao_max_rows"
    db_pool_min_connections: str = "db_pool_min_connections"
    db_pool_max_connections: str = "db_pool_max_connections"
    system_email: str = "system_email"
    test_email: str = "test_email"
    administrator_email: str = "administrator_email"


class AuditTypes:
    Update: str = "Update"
    Delete: str = "Delete"
    Deactivate: str = "Deactivate"
    Insert: str = "Insert"


class TenantTypes:
    Default: str = "Default"
    System: str = "System"
    Test: str = "Test"
    Individual: str = "Individual"
    Corporate: str = "Corporate"


class TenantCategories:
    Internal: str = "Internal"
    External: str = "External"
    Hybrid: str = "Hybrid"


class TenantStatuses:
    New: str = "New"
    Pending: str = "Pending"
    Active: str = "Active"
    Closing: str = "Closing"
    Closed: str = "Closed"


class Tenants:
    System: str = "System"
    Test: str = "Test"


class TenantRoles:
    Owner: str = "Owner"
    Administrator: str = "Administrator"
    HR: str = "HR"
    Manager: str = "Manager"
    Leader: str = "Leader"
    Reporter: str = "Reporter"
    Contractor: str = "Contractor"
    User: str = "User"
    Viewer: str = "Viewer"


class ClientTypes:
    Default: str = "Default"
    System: str = "System"
    Test: str = "Test"
    Individual: str = "Individual"
    Corporate: str = "Corporate"


class ClientStatuses:
    New: str = "New"
    Pending: str = "Pending"
    Active: str = "Active"
    Closing: str = "Closing"
    Closed: str = "Closed"


class Clients:
    System: str = "System"
    Test: str = "Test"


class AccountTypes:
    System: str = "System"
    Person: str = "Person"
    Client: str = "Client"
    Viewer: str = "Viewer"
    Application: str = "Application"


class Accounts:
    system: str = "system"
    administrator: str = "administrator"
    test_administrator: str = "test_administrator"
    test_manager: str = "test_manager"
    test_user: str = "test_user"
    test_viewer: str = "test_viewer"


class Groups:
    System = "System"


class Roles:
    SystemAdministrator: str = "SystemAdministrator"
    ClientAdministrator: str = "ClientAdministrator"
    TenantAdministrator: str = "TenantAdministrator"
    Supervisor: str = "Supervisor"
    DeliveryManager: str = "DeliveryManager"
    Employee: str = "Employee"
    StandardUser: str = "StandardUser"
    Everyone: str = "Everyone"
    AccountAdministrator: str = "AccountAdministrator"
    AccountManager: str = "AccountManager"
    AccountSupervisor: str = "AccountSupervisor"
    AccountOperator: str = "AccountOperator"
    AccountCreator: str = "AccountCreator"
    AccountEditor: str = "AccountEditor"
    AccountViewer: str = "AccountViewer"
    AuthAdministrator: str = "AuthAdministrator"
    AuthManager: str = "AuthManager"
    AuthSupervisor: str = "AuthSupervisor"
    AuthOperator: str = "AuthOperator"
    AuthCreator: str = "AuthCreator"
    AuthEditor: str = "AuthEditor"
    AuthViewer: str = "AuthViewer"
    ReportAdministrator: str = "ReportAdministrator"
    ReportManager: str = "ReportManager"
    ReportSupervisor: str = "ReportSupervisor"
    ReportCreator: str = "ReportCreator"
    ReportEditor: str = "ReportEditor"
    ReportViewer: str = "ReportViewer"
    ClientManager: str = "ClientManager"
    ClientSupervisor: str = "ClientSupervisor"
    TenantManager: str = "TenantManager"
    TenantSupervisor: str = "TenantSupervisor"
    TenantOperator: str = "TenantOperator"
    TenantCreator: str = "TenantCreator"
    TenantEditor: str = "TenantEditor"
    TenantViewer: str = "TenantViewer"
    InvoiceAdministrator: str = "InvoiceAdministrator"
    InvoiceManager: str = "InvoiceManager"
    InvoiceSupervisor: str = "InvoiceSupervisor"
    InvoiceOperator: str = "InvoiceOperator"
    InvoiceCreator: str = "InvoiceCreator"
    InvoiceEditor: str = "InvoiceEditor"
    InvoiceViewer: str = "InvoiceViewer"



