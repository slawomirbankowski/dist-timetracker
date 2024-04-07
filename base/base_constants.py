import datetime
import uuid
import random


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

