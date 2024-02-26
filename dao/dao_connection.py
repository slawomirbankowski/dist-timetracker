import os
import psycopg2
import psycopg2.pool
from pyliquibase import Pyliquibase

class DaoConnection:
    db_url = "jdbc:postgresql://localhost:5432/disttimetracker"
    # os.environ.get('JDBC_URL')
    print('DaoConnection URL=' + db_url)
    db_user = os.environ.get('JDBC_USER')
    print('DaoConnection User=' + db_user)
    db_pass = os.environ.get('JDBC_PASS')
    print('DaoConnection Pass=' + db_pass)
    db_pool = psycopg2.pool.SimpleConnectionPool(
        2, 4, user=db_user, password=db_pass,
        host='localhost', port='5432', database='disttimetracker')

    def __init__(self):
        print("Nothing to be done here")

    def initializeSchema(self):
        print(os.environ.get('JAVA_HOME'))
        liquibase = Pyliquibase(defaultsFile="./changelogs/liquibase.properties", logLevel="DEBUG", jdbcDriversDir="./lib")
        print(type(liquibase))
        print(liquibase.version)
        liquibase.validate()
        liquibase.update()

    def getConnection(self):
        return self.db_pool.getconn()

    def close(self, db_conn):
        db_conn.close()

    def getUrl(self):
        return self.db_url;

daoConn = DaoConnection()




