import datetime
import os
import psycopg2
import psycopg2.pool
from pyliquibase import Pyliquibase

from base.base_objects import base_object


# DaoConnection with DBCP to Postgres database
class DaoConnection(base_object):
    db_url: str
    db_host: str
    db_name: str = "timetracker"
    db_user: str
    db_pass: str
    min_conns: int = 2
    max_conns: int = 20
    db_pool: psycopg2.pool.SimpleConnectionPool
    liquibase_prop_file: str

    def __init__(self):
        super().__init__()
    # get type of base object
    def get_base_object_type(self) -> str:
        return "Connection"

    # get name of base object
    def get_base_object_name(self) -> str:
        return self.db_name
    def initialize_connection(self, db_url: str, db_host: str, db_name: str, db_user: str, db_pass: str,
                              min_conns: int = 2, max_conns: int = 20):
        self.db_url = db_url
        self.db_host = db_host
        self.db_name = db_name
        self.db_user = db_user
        self.db_pass = db_pass
        self.min_conns = min_conns
        self.max_conns = max_conns
        self.liquibase_prop_file = "./changelogs/liquibase." + self.db_name + ".properties"
        print("Creating new DB connection pool, host: " + db_host + ", name: " + db_name + ", user: " + db_user)
        self.db_pool = psycopg2.pool.SimpleConnectionPool(min_conns, max_conns, user=db_user, password=db_pass,
                                                          host=db_host, port='5432', database=db_name)

    def get_base_dict_custom_info(self) -> dict[str, any]:
        return {
            "created_date": str(self.created_date),
            "db_url": self.db_url,
            "db_host": self.db_host,
            "db_name": self.db_name,
            "min_conns": self.min_conns,
            "max_conns": self.max_conns,
            "db_pool_class_name": type(self.db_pool).__name__,
            "db_pool_closed": self.db_pool.closed
        }

    def save_liquibase_properties(self):
        print("Saving Liquibase properties file")
        lpfile = open(self.liquibase_prop_file, "w")
        lpfile.writelines([
            "changeLogFile:./changelogs/masterchangelog.xml\n",
            "url: " + self.db_url + "\n",
            "username: " + self.db_user + "\n",
            "password: " + self.db_pass + "\n",
            "classpath:  postgresql-42.7.3.jar\n"
        ])
        lpfile.close()

    def delete_liquibase_properties(self):
        os.remove(self.liquibase_prop_file)

    def initialize_schema(self):
        self.save_liquibase_properties()
        liquibase = Pyliquibase(defaultsFile=self.liquibase_prop_file, jdbcDriversDir="./lib")
        print("Initializing Liquibase schema on database: " + self.db_url + ", file: " + self.liquibase_prop_file + ", version: " + liquibase.version)
        liquibase.validate()
        liquibase.update()
        self.delete_liquibase_properties()

    def get_connection(self):
        return self.db_pool.getconn()

    def close(self, db_conn):
        self.db_pool.putconn(db_conn)

    def get_url(self):
        return self.db_url


# DAO connections to main database and all other client databases
class DaoConnections(base_object):
    is_initialized: bool = False
    creation_time: datetime.datetime | None
    initialization_time: datetime.datetime | None
    db_url: str = "jdbc:postgresql://localhost:5432/disttimetracker"
    db_host: str = "localhost"
    db_name: str = "timetracker"
    db_user: str = "postgres"
    db_pass: str
    main_connection = DaoConnection()
    connections: dict[str, DaoConnection] = {}

    # initializing DB connections to main database and client databases
    def __init__(self):
        super().__init__()
        self.creation_time = datetime.datetime.now()

    # get name of base object
    def get_base_object_name(self) -> str:
        return "DaoConnections"
    # get type of base object
    def get_base_object_type(self) -> str:
        return "Connections"
    # initialize DB connection to main database
    def initialize_main_connection(self, db_url: str, db_host: str, db_name: str, db_user: str, db_pass: str):
        print("Initializing DaoConnections")
        self.main_connection.initialize_connection(db_url, db_host, db_name, db_user, db_pass)
        self.main_connection.initialize_schema()
        self.is_initialized = True
        self.db_url = db_url
        self.db_host = db_host
        self.db_name = db_name
        self.db_user = db_user
        self.db_pass = db_pass
        self.initialization_time = datetime.datetime.now()
    # handler for closing application
    def close(self):
        print("Closing Connections")

    def get_base_dict_custom_info(self):
        return {
            "is_initialized": self.is_initialized,
            "creation_time": self.creation_time,
            "initialization_time": self.initialization_time,
            "db_url": self.db_url,
            "db_host": self.db_host,
            "db_name": self.db_name,
            "db_user": self.db_user,
            "main_conn": self.main_connection.get_base_dict_custom_info(),
            "connections": list(map(lambda c: c.get_base_dict_custom_info(), self.connections.values()))
        }

    # create new connection to tenant database
    def create_tenant_connection(self, db_url: str, db_host: str, db_name: str, db_user: str, db_pass: str):
        print("Create tenant DB connection")
        tenant_connection = DaoConnection()
        tenant_connection.initialize_connection(db_url, db_host, db_name, db_user, db_pass)
        self.connections[db_name] = tenant_connection

    def get_connection(self):
        return self.main_connection.get_connection()

    def close(self, db_conn):
        self.main_connection.close(db_conn)

    def get_tenant_connection(self, db_name: str) -> DaoConnection:
        return self.connections[db_name]

    def close_tenant_connection(self, db_name: str, db_conn):
        return self.connections[db_name].close(db_conn)

# main object with all DB connection - main and tenants
db_connections = DaoConnections()
