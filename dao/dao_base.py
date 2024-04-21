from typing import TypeVar, Generic, List, Iterable, Any, Callable, Dict
import logging
from logging import config
from psycopg2.extensions import connection, cursor
import dao.dao_connection
from base.base_utils import tuple_to_dict
from dto.dtos import *
from dto.dtos_read import *
from dto.dtos_write import *
from base.base_objects import base_object

db_connections = dao.dao_connection.db_connections


class ConnectionCursorWrapper:
    db_connection: connection
    db_cursor: cursor
    def __init__(self, db_connection: connection, db_cursor: cursor):
        self.db_connection = db_connection
        self.db_cursor = db_cursor


class QueryWithParams:
    query: str
    params: Iterable
    def __init__(self, query: str, params: Iterable = []):
        self.query = query
        self.params = params


class QueriesWithParams:
        queries: list[QueryWithParams]


class simple_dao(base_object):
    executed_queries: int  # number of executed queries in this DAO
    def __init__(self):
        super().__init__()
        self.executed_queries = 0
    # get name of base object
    def get_base_object_name(self) -> str:
        return "simple_dao"
    # get type of base object
    def get_base_object_type(self) -> str:
        return "Dao"
    def with_connection_commit(self, execution: Callable[[ConnectionCursorWrapper], any]) -> any:
        conn = db_connections.get_connection()
        db_cursor = conn.cursor()
        wrp = ConnectionCursorWrapper(conn, db_cursor)
        result = execution(wrp)
        conn.commit()
        db_connections.close(conn)
        return result

    def with_connection_select(self, execution: Callable[[ConnectionCursorWrapper], any]) -> any:
        conn = db_connections.get_connection()
        db_cursor = conn.cursor()
        wrp = ConnectionCursorWrapper(conn, db_cursor)
        result = execution(wrp)
        db_connections.close(conn)
        return result

    def get_objects(self, query: str, params: Iterable = []) -> list[tuple]:
        logging.debug("Executing SQL query on database, Q=" + query)
        conn = db_connections.get_connection()
        db_cursor = conn.cursor()
        db_cursor.execute(query, params)
        # print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        # print(str(type(db_cursor)))
        # print(str(type(db_cursor).__name__))
        results = db_cursor.fetchall()
        db_connections.close(conn)
        self.executed_queries = self.executed_queries+1
        return results

    def execute_query(self, query: str, params: Iterable = []) -> int:
        logging.debug("Executing SQL query on database with parameters, Q=" + query)
        #self.with_connection_commit(lambda conn, curs: cursor.execute(query, params))
        conn = db_connections.get_connection()
        db_cursor = conn.cursor()
        db_cursor.execute(query, params)
        conn.commit()
        results = db_cursor.rowcount
        db_connections.close(conn)
        self.executed_queries = self.executed_queries+1
        return results

    def execute_queries(self, query: str, params: list[Iterable]) -> int:
        logging.debug("Executing SQL queries on database with many parameters, Q=" + query)
        conn: connection = db_connections.get_connection()
        db_cursor = conn.cursor()
        for param in params:
            db_cursor.execute(query, param)
        conn.commit()
        results = db_cursor.rowcount
        db_connections.close(conn)
        # self.executed_queries = self.executed_queries+1
        return results

    def execute_queries_no_params(self, queries: list[str], do_commit: bool = False) -> int:
        logging.debug("Executing SQL queries on database without parameters, cnt=" + str(len(queries)))
        conn: connection = db_connections.get_connection()
        db_cursor = conn.cursor()
        for query in queries:
            logging.info("Executing NEXT query: \n" + query)
            db_cursor.execute(query)
        if do_commit:
            conn.commit()
        results = db_cursor.rowcount
        db_connections.close(conn)
        # self.executed_queries = self.executed_queries+1
        return results

    def get_single_row(self, query: str, params: Iterable = []) -> tuple | None:
        tuples = self.get_objects(query, params)
        if len(tuples)>0:
            return tuples[0]
        else:
            return None
    def get_single_row_as_dict(self, query: str, params: Iterable = []) -> dict | None:
        row = self.get_single_row(query, params)
        if row is None:
            return None
        else:
            return tuple_to_dict(row)

    def get_single_value_int_or_default(self, query: str, default_value: int = 0, params: Iterable = [], col_num: int=0) -> int:
        t: tuple = self.get_single_row(query, params)
        if t is None:
            return default_value
        else:
            return int(t[col_num])
    def get_single_value(self, query: str, col_num: int=0) -> Any | None:
        t: tuple = self.get_single_row(query)
        if t is None:
            return None
        else:
            return t[col_num]
    # get single column
    def get_column_values_by_params(self, query: str, params: Iterable = [], col_num: int = 0) -> list[str]:
        tuples = self.get_objects(query, params)
        return list(map(lambda x: str(x[col_num]), tuples))
    # get all values for given query and column number
    def get_column_values_all(self, query: str, params: Iterable = [], col_num: int = 0) -> list[any]:
        tuples = self.get_objects(query, params)
        return list(map(lambda x: str(x[col_num]), tuples))
    def get_single_value_or_default(self, query: str, default_value: any, params: Iterable = [], col_num: int=0) -> Any:
        t: tuple = self.get_single_row(query, params)
        if t is None:
            return default_value
        else:
            return t[col_num]

    def create_rich_views(self) -> None:
        """create rich views in main database - rich views are from objects and foreign tables"""
        logging.info("Applying RICH views SQL DDL to database")
        views_ddls = db_models.generate_all_rich_views_sql_ddl()
        self.execute_queries_no_params(views_ddls, True)
    def drop_rich_views(self) -> None:
        drop_ddls = db_models.generate_rich_view_drops()
        logging.info("Dropping RICH views SQL DDL on database")
        self.execute_queries_no_params(drop_ddls, True)
    def replace_rich_views(self) -> None:
        logging.info("Replacing RICH views SQL DDL on database - DROP then CREATE")
        self.drop_rich_views()
        self.create_rich_views()

# base DAO class for all DAOs
class base_dao(simple_dao):
    executed_queries: int  # number of executed queries in this DAO
    def __init__(self):
        super().__init__()
        self.executed_queries = 0

    # get name of base object
    def get_base_object_name(self) -> str:
        return self.get_model().table_name
    # get type of base object
    def get_base_object_type(self) -> str:
        return "Dao"
    @abstractmethod
    def get_model(self) -> db_model:
        pass

    def select_uids_all(self, n: int = 1000) -> list[str]:
        return self.get_column_values_all(self.get_model().get_select_all_uids(n))
    def select_uids_active(self, n: int = 1000) -> list[str]:
        return self.get_column_values_all(self.get_model().get_select_active_uids(n))

    def select_guids_all(self, n: int = 1000) -> list[str]:
        return self.get_column_values_all(self.get_model().get_select_all_guids(n))
    def select_guids_active(self, n: int = 1000) -> list[str]:
        return self.get_column_values_all(self.get_model().get_select_active_guids(n))

    # count all rows in table associated with this DAO
    def count_all(self) -> int:
        return self.get_single_value_int_or_default(self.get_model().get_select_count_all_sql())
    # count active rows in table associated with this DAO
    def count_active(self) -> int:
        return self.get_single_value_int_or_default(self.get_model().get_select_count_active_sql())
    # count all rows for given column in given values
    def count_by_any_column_values(self, col_name: str, col_values: list[any]) -> int:
        return self.get_single_value_int_or_default(self.get_model().get_select_count_by_any_column_sql(col_name), 0, col_values)
    # count all rows for table
    def count_by_table_all(self, table_name: str):
        return self.get_single_value_int_or_default("select count(*) as cnt from " + table_name, 0)
    # count active rows for table
    def count_by_table_active(self, table_name: str):
        return self.get_single_value_int_or_default("select count(*) as cnt from " + table_name + " where is_active=1", 0)
    # count rows using query - query must return one row one column
    def count_by_query(self, sql: str):
        return self.get_single_value_int_or_default(sql, 0)
    # count rows by two column/value pairs
    def count_by_two_columns(self, name1: str, value1: any, name2: str, value2: any) -> int:
        return self.get_single_value_int_or_default(self.get_model().get_select_count_by_two_columns_sql(name1, name2), 0, (value1,value2,))

    # get all row_guid values for table associated with this DAO
    def get_guids(self, n: int = 1000) -> list[str]:
        return self.get_column_values_all(self.get_model().get_select_all_guids(n))

    # get all UIDs for table associated with this DAO
    def get_uids(self, n: int = 1000) -> list[str]:
        return self.get_column_values_all(self.get_model().get_select_all_keys(n))

    # get  UIDs for given column=value for table associated with this DAO
    def get_uids_by_column(self, col_name: str, col_value: any, n: int = 1000) -> list[str]:
        return self.get_column_values_all(self.get_model().get_select_keys_by_column_name(col_name, n), (col_value,))

    # group table by column or expression
    def group_by_column(self, column_or_expression: str, sql_where: str = "1=1", params: Iterable = [], max_rows: int = 1000) -> list[group_dto]:
        sql = "select " + column_or_expression + " as value, count(*) as rows_count from " + self.get_model().table_name + " where " + sql_where + " group by " + column_or_expression + " limit " + str(max_rows)
        return list(map(lambda x: group_dto(*x), self.get_objects(sql, params)))

    def insert_single(self, dto: base_write_dto, created_by: str = "system") -> int:
        return self.execute_query(dto.get_model().insert_attrs_sql, dto.get_list_write_insert(created_by))
    def insert_many_with_model(self, model: db_model, dtos: list[base_write_dto], created_by: str = "system") -> int:
        params = list(map(lambda x: x.get_list_write_insert(created_by), dtos))
        return self.execute_queries(model.insert_attrs_sql, params)
    def insert_many(self, dtos: list[base_write_dto], created_by: str = "system") -> int:
        if len(dtos) > 0:
            model = dtos[0].get_model()
            return self.insert_many_with_model(model, dtos, created_by)
        else:
            return 0

    def delete_logical_by_any_column(self, col_name: str, col_value: any, removed_by: str) -> int:
        m = self.get_model()
        return self.execute_query("update " + m.table_name + " set is_active=0, row_version=row_version+1, last_updated_date=now(), last_updated_by=%s, removed_date=now(), removed_by=%s  where " + col_name + "=%s", (removed_by, removed_by, col_value,))
    def delete_logical_by_uid(self, uid: str, removed_by: str) -> int:
        m = self.get_model()
        return self.delete_logical_by_any_column(m.key_column_name, uid, removed_by)
    def delete_logical_by_uids(self, uids: list[str], removed_by: str) -> int:
        m = self.get_model()
        sql = "update " + m.table_name + " set is_active=0, row_version=row_version+1, last_updated_date=now(), last_updated_by=%s, removed_date=now(), removed_by=%s  where " + m.key_column_name + "=%s"
        params = list(map(lambda uid: (removed_by, removed_by, uid,), uids))
        return self.execute_queries(sql, params)
    def delete_logical_by_objects(self, dtos: list[base_write_dto], removed_by: str) -> int:
        uids = list(map(lambda dto: dto.get_uid(), dtos))
        return self.delete_logical_by_uids(uids, removed_by)
    def delete_logical_by_object(self, obj: base_read_dto, removed_by: str) -> int:
        m = self.get_model()
        return self.delete_logical_by_any_column(m.key_column_name, obj.get_key(), removed_by)
    def delete_logical_by_id(self, id: int, removed_by: str) -> int:
        return self.delete_logical_by_any_column("id", id, removed_by)
    def delete_logical_before_created(self, removed_by: str, dt: datetime.datetime) -> int:
        m = self.get_model()
        return self.execute_query("update " + m.table_name + " set is_active=0, row_version=row_version+1, last_updated_date=now(), last_updated_by=%s, removed_date=now(), removed_by=%s  where created_date < %s", (removed_by, removed_by, dt,))
    def delete_physical_by_uid(self, uid: str):
        m = self.get_model()
        # consider moving data to another table with changes
        return self.execute_query("delete from " + m.table_name + " where " + m.key_column_name + "=%s", (uid,))
    def delete_physical_for_deleted_logical(self):
        m = self.get_model()
        # consider moving data to another table with changes
        return self.execute_query("delete from " + m.table_name + " where is_active=0")
    def delete_physical_before_created(self, dt: datetime.datetime):
        m = self.get_model()
        # consider moving data to another table with changes
        return self.execute_query("delete from " + m.table_name + " where created_date < %s", (dt,))
    def update_single_column_by_uid(self, uid: str, col_name: str, col_value: str, updated_by: str = "system"):
        m = self.get_model()
        sql = "update " + m.table_name + " set " + col_name + "=%s, row_version=row_version+1, last_updated_date=now(), last_updated_by=%s where " + m.key_column_name + "=%s"
        return self.execute_query(sql, (col_value, updated_by, uid,))
    def update_single_column_by_id(self, id: int, col_name: str, col_value: str, updated_by: str = "system"):
        m = self.get_model()
        sql = "update " + m.table_name + " set " + col_name + "=%s, row_version=row_version+1, last_updated_date=now(), last_updated_by=%s where id=%s"
        return self.execute_query(sql, (col_value, updated_by, id,))
    # update one row by UID - just row_version, last_updated_date and last_updated_by
    def update_touch_by_uid(self, uid: str, updated_by: str = "system"):
        m = self.get_model()
        sql = "update " + m.table_name + " set row_version=row_version+1, last_updated_date=now(), last_updated_by=%s where " + m.key_column_name + "=%s"
        return self.execute_query(sql, (updated_by, uid,))

    def update_write_dto(self, dto: base_write_dto, updated_by: str = "system"):
        m = self.get_model()
        params = dto.get_list_write_update(updated_by)
        return self.execute_query(m.update_attrs_sql, params)
    def update_write_dtos(self, dtos: list[base_write_dto], updated_by: str = "system"):
        m = self.get_model()
        params = list(map(lambda dto: dto.get_list_write_update(updated_by), dtos))
        return self.execute_queries(m.update_attrs_sql, params)

    # update or insert row
    def upsert_write_dto(self, dto: base_write_dto, updated_by: str = "system"):
        params = dto.get_list_write_insert(updated_by)
        return self.execute_query(self.get_model().upsert_attrs_sql, params)
    def upsert_write_dtos(self, dtos: list[base_write_dto], updated_by: str = "system"):
        m = self.get_model()
        params = list(map(lambda dto: dto.get_list_write_insert(updated_by), dtos))
        return self.execute_queries(m.upsert_attrs_sql, params)

    @abstractmethod
    def select_rows_read_by_query(self, sql: str, params: Iterable = []) -> base_read_dtos:
        pass
    @abstractmethod
    def select_rows_write_by_query(self, sql: str, params: Iterable = []) -> base_write_dtos:
        pass
    @abstractmethod
    def select_rows_thin_by_query(self, sql: str, params: Iterable = []) -> base_dtos:
        pass
    @abstractmethod
    def select_rows_rich_by_query(self, sql: str, params: Iterable = []) -> base_write_dtos:
        pass
    @abstractmethod
    def select_row_first_by_query(self, sql: str, params: Iterable = []) -> account_read_dto | None:
        pass
    @abstractmethod
    def select_rows_read_order_by_column(self, col_name: str, params: Iterable = [], n: int = 1000) -> base_read_dtos:
        pass
    @abstractmethod
    def select_rows_read_all(self, n: int = 1000) -> base_read_dtos:
        pass
    @abstractmethod
    def select_rows_read_active(self, n: int = 1000) -> base_read_dtos:
        pass
    @abstractmethod
    def select_rows_read_all_latest(self, n: int = 1000) -> base_read_dtos:
        pass
    @abstractmethod
    def select_rows_read_active_latest(self, n: int = 1000) -> base_read_dtos:
        pass
    @abstractmethod
    def select_rows_write_all(self, n: int = 1000) -> base_write_dtos:
        pass
    @abstractmethod
    def select_rows_write_active(self, n: int = 1000) -> base_write_dtos:
        pass
    @abstractmethod
    def select_rows_write_all_latest(self, n: int = 1000) -> base_write_dtos:
        pass
    @abstractmethod
    def select_rows_write_active_latest(self, n: int = 1000) -> base_write_dtos:
        pass
    @abstractmethod
    def select_row_read_by_uid(self, uid: str) -> account_read_dto | None:
        pass
    @abstractmethod
    def select_row_read_by_id(self, id: int) -> account_read_dto | None:
        pass
    @abstractmethod
    def select_rows_read_by_any_column(self, col_name: str, col_value: any, n: int = 1000) -> base_read_dtos:
        pass
    @abstractmethod
    def select_rows_read_by_any_column_values(self, col_name: str, col_values: Iterable, n: int = 1000) -> base_read_dtos:
        pass
    @abstractmethod
    def select_rows_thin_all(self, n: int = 1000) -> base_dtos:
        pass

