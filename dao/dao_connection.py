import datetime
import os
import logging
from typing import TypeVar, Generic, List, Iterable, Any, Callable, Dict
from psycopg2.extensions import connection
from logging import config
import psycopg2
import psycopg2.pool
from pyliquibase import Pyliquibase

from base.base_objects import base_object, DaoConnectionBase, DaoConnectionsBase, objects
from base.base_utils import create_empty_list


class DaoConnection(DaoConnectionBase):
    """DaoConnection with DBCP to Postgres database"""
    db_url: str
    db_host: str
    db_name: str = "timetracker"
    db_user: str
    db_pass: str
    min_conns: int = 2
    max_conns: int = 20
    connections_opened: int = 0
    connections_closed: int = 0
    db_pool: psycopg2.pool.SimpleConnectionPool
    liquibase_prop_file: str
    pool_created_date: datetime.datetime

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
        """initialize new DB connection and connect to given URL, host, name with user and password; this is creating new connection pool"""
        self.db_url = db_url
        self.db_host = db_host
        self.db_name = db_name
        self.db_user = db_user
        self.db_pass = db_pass
        self.min_conns = min_conns
        self.max_conns = max_conns
        self.connections_opened = 0
        self.connections_closed = 0
        self.liquibase_prop_file = "./changelogs/liquibase." + self.db_name + ".properties"
        logging.info("Creating new DB connection pool, host: " + db_host + ", name: " + db_name + ", user: " + db_user)
        self.db_pool = psycopg2.pool.SimpleConnectionPool(min_conns, max_conns, user=db_user, password=db_pass,
                                                          host=db_host, port='5432', database=db_name)
        self.pool_created_date = datetime.datetime.now()

    def get_base_dict_custom_info(self) -> dict[str, any]:
        return {
            "created_date": str(self.created_date),
            "db_url": self.db_url,
            "db_host": self.db_host,
            "db_name": self.db_name,
            "db_user": self.db_user,
            "min_conns": self.min_conns,
            "max_conns": self.max_conns,
            "connections_opened": self.connections_opened,
            "connections_closed": self.connections_closed,
            "db_pool_class_name": type(self.db_pool).__name__,
            "db_pool_closed": self.db_pool.closed
        }

    def save_liquibase_properties(self) -> None:
        logging.info("Saving Liquibase properties file")
        lpfile = open(self.liquibase_prop_file, "w")
        lpfile.writelines([
            "changeLogFile:./changelogs/masterchangelog.xml\n",
            "url: " + self.db_url + "\n",
            "username: " + self.db_user + "\n",
            "password: " + self.db_pass + "\n",
            "classpath:  postgresql-42.7.3.jar\n"
        ])
        lpfile.close()

    def delete_liquibase_properties(self) -> None:
        os.remove(self.liquibase_prop_file)

    def initialize_schema(self) -> None:
        """initialize new Liquibase schema with validating and updating"""
        self.save_liquibase_properties()
        liquibase = Pyliquibase(defaultsFile=self.liquibase_prop_file, jdbcDriversDir="./lib")
        logging.info("Initializing Liquibase schema on database: " + self.db_url + ", file: " + self.liquibase_prop_file + ", version: " + liquibase.version)
        liquibase.validate()
        logging.info("Updating schema - Liquibase")
        liquibase.update()
        self.delete_liquibase_properties()

    def get_connection(self) -> connection:
        """get new DB connection; consider using with_connection instead"""
        self.connections_opened += 1
        return self.db_pool.getconn()

    def close(self, db_conn) -> None:
        """close this connection; consider using with_connection instead"""
        self.connections_closed += 1
        self.db_pool.putconn(db_conn)

    def get_url(self) -> str:
        """get JDBC URL to this DB connection"""
        return self.db_url

    def get_objects(self, query: str, params: Iterable = create_empty_list()) -> list[tuple]:
        """execute query with parameters and get list of rows as tuples"""
        logging.debug("Executing SQL query on database, Q=" + query)
        conn = db_connections.get_connection()
        db_cursor = conn.cursor()
        db_cursor.execute(query, params)
        results = db_cursor.fetchall()
        db_connections.close(conn)
        #self.executed_queries = self.executed_queries+1
        return results

    def with_connection(self, exec: Callable[[connection], any]) -> any:
        """execute exec method with connection"""
        conn = self.get_connection()
        res = exec(conn)
        self.close(conn)
        return res
















# DAO connections to main database and all other client databases
class DaoConnections(DaoConnectionsBase):
    is_initialized: bool = False
    creation_time: datetime.datetime | None
    initialization_time: datetime.datetime | None
    db_url: str = "jdbc:postgresql://localhost:5432/disttimetracker"
    db_host: str = "localhost"
    db_name: str = "timetracker"
    db_user: str = "postgres"
    db_pass: str
    connections_opened: int = 0
    connections_closed: int = 0
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
    def initialize_main_connection(self, db_url: str, db_host: str, db_name: str, db_user: str, db_pass: str) -> None:
        logging.debug("Initializing DaoConnections: main connection, object_id: " + self.object_id)
        self.main_connection.initialize_connection(db_url, db_host, db_name, db_user, db_pass)
        self.main_connection.initialize_schema()
        self.is_initialized = True
        self.db_url = db_url
        self.db_host = db_host
        self.db_name = db_name
        self.db_user = db_user
        self.db_pass = db_pass
        self.initialization_time = datetime.datetime.now()

    def initialize_main_connection_from_env(self) -> None:
        db_url = os.environ.get('JDBC_URL')
        db_host = os.environ.get('JDBC_HOST')
        db_name = os.environ.get('JDBC_NAME')
        db_user = os.environ.get('JDBC_USER')
        db_pass = os.environ.get('JDBC_PASS')
        logging.info(f"Main database URL ={db_url}, HOST={db_host}, NAME={db_name}, USER={db_user}" )
        self.initialize_main_connection(db_url, db_host, db_name, db_user, db_pass)

    def read_python_code(self) -> str | None:
        #self.main_connection.get_connection()
        return ""

    # handler for closing application
    def close_connections(self) -> None:
        #TODO: close all connections

        logging.info("Closing ALL Connections, object_id: " + self.object_id)

    def get_base_dict_custom_info(self) -> dict:
        return {
            "is_initialized": self.is_initialized,
            "creation_time": self.creation_time,
            "initialization_time": self.initialization_time,
            "db_url": self.db_url,
            "db_host": self.db_host,
            "db_name": self.db_name,
            "db_user": self.db_user,
            "connections_opened": self.connections_opened,
            "connections_closed": self.connections_closed,
            "main_conn": self.main_connection.get_base_dict_custom_info(),
            "connections": list(map(lambda c: c.get_base_dict_custom_info(), self.connections.values()))
        }

    # create new connection to tenant database
    def create_tenant_connection(self, db_url: str, db_host: str, db_name: str, db_user: str, db_pass: str):
        logging.info("Create tenant DB connection, object_id: " + self.object_id)
        tenant_connection = DaoConnection()
        tenant_connection.initialize_connection(db_url, db_host, db_name, db_user, db_pass)
        self.connections[db_name] = tenant_connection

    def get_connection(self):
        self.connections_opened += 1
        return self.main_connection.get_connection()

    def close(self, db_conn):
        self.connections_closed += 1
        self.main_connection.close(db_conn)

    def get_tenant_connection(self, db_name: str) -> DaoConnection:
        return self.connections[db_name]

    def close_tenant_connection(self, db_name: str, db_conn):
        return self.connections[db_name].close(db_conn)


# main object with all DB connection - main and tenants
db_connections = DaoConnections()
objects.register_connections(db_connections)
