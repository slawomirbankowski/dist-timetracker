import dao.dao_connection
from typing import TypeVar, Generic, List, Iterable, Any

from dto.dtos import *
from dto.dtos_read import *
from dto.dtos_write import *

daoConn = dao.dao_connection.daoConn

class base_dao:
    executed_queries: int
    def __init__(self):
        print("Starting DAO")
        self.executed_queries = 0
    @abstractmethod
    def get_model(self) -> base_model:
        pass
    def get_objects(self, query: str) -> list[tuple]:
        print("Executing SQL query on database, Q=" + query)
        conn = daoConn.getConnection()
        cursor = conn.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        daoConn.close(conn)
        #self.executed_queries = self.executed_queries+1
        return results

    def get_objects_by_params(self, query: str, params: Iterable) -> list[tuple]:
        print("Executing SQL query on database with parameters, Q=" + query)
        conn = daoConn.getConnection()
        cursor = conn.cursor()
        cursor.execute(query, params)
        results = cursor.fetchall()
        daoConn.close(conn)
        #self.executed_queries = self.executed_queries+1
        return results
    def execute_query_no_results(self, query: str, params: Iterable):
        print("Executing SQL query on database with parameters, Q=" + query)
        conn = daoConn.getConnection()
        cursor = conn.cursor()
        cursor.execute(query, params)
        daoConn.close(conn)
        #self.executed_queries = self.executed_queries+1
    def execute_query_with_params(self, query: str, params: Iterable) -> int:
        print("Executing SQL query on database with parameters, Q=" + query)
        conn = daoConn.getConnection()
        cursor = conn.cursor()
        cursor.execute(query, params)
        conn.commit()
        results = cursor.rowcount
        daoConn.close(conn)
       # self.executed_queries = self.executed_queries+1
        return results
    def execute_queries_with_params(self, query: str, params: list[Iterable]) -> int:
        print("Executing SQL queries on database with many parameters, Q=" + query)
        conn = daoConn.getConnection()
        cursor = conn.cursor()
        for param in params:
            cursor.execute(query, param)
        conn.commit()
        results = cursor.rowcount
        daoConn.close(conn)
       # self.executed_queries = self.executed_queries+1
        return results
    def execute_query(self, query: str) -> int:
        print("Executing SQL query on database, Q=" + query)
        conn = daoConn.getConnection()
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
        results = cursor.rowcount
        daoConn.close(conn)
        #self.executed_queries = self.executed_queries+1
        return results

    def get_column_values_by_params(self, query: str, params: Iterable) -> list[str]:
        tuples = self.get_objects_by_params(query, params)
        return list(map(lambda x: str(x[0]), tuples))
    def get_column_values_all(self, query: str) -> list[str]:
        tuples = self.get_objects(query)
        return list(map(lambda x: str(x[0]), tuples))
    def get_column_by_params(self, query: str, params: Iterable, col_num: int=0) -> list[any]:
        tuples = self.get_objects_by_params(query, params)
        return list(map(lambda x: x[col_num], tuples))
    def get_column_all(self, query: str, col_num: int=0) -> list[any]:
        tuples = self.get_objects(query)
        return list(map(lambda x: x[col_num], tuples))
    def get_single_row(self, query: str) -> tuple | None:
        tuples = self.get_objects(query)
        if len(tuples)>0:
            return tuples[0]
        else:
            return None
    def get_single_row_by_params(self, query: str, params: Iterable) -> tuple | None:
        tuples = self.get_objects_by_params(query, params)
        if len(tuples)>0:
            return tuples[0]
        else:
            return None
    def get_single_value(self, query: str, col_num: int=0) -> Any | None:
        tuple = self.get_single_row(query)
        if tuple is None:
            return None
        else:
            return tuple[col_num]
    def get_single_value_or_default(self, query: str, default_value: any, col_num: int=0) -> Any:
        tuple = self.get_single_row(query)
        if tuple is None:
            return default_value
        else:
            return tuple[col_num]
    def get_single_value_or_default_by_params(self, query: str, params: Iterable, default_value: any, col_num: int = 0) -> Any:
        tuple = self.get_single_row_by_params(query, params)
        if tuple is None:
            return default_value
        else:
            return tuple[col_num]
    def get_single_value_int_or_default(self, query: str, default_value: int = 0, col_num: int=0) -> int:
        tuple = self.get_single_row(query)
        if tuple is None:
            return default_value
        else:
            return int(tuple[col_num])
    def get_single_value_int_or_default_by_params(self, query: str, params: Iterable, default_value: int = 0, col_num: int=0) -> int:
        tuple = self.get_single_row_by_params(query, params)
        if tuple is None:
            return default_value
        else:
            return int(tuple[col_num])
    def count_by_table_all(self, table_name: str):
        return self.get_single_value_int_or_default("select count(*) as cnt from " + table_name, 0)
    def count_by_table_active(self, table_name: str):
        return self.get_single_value_int_or_default("select count(*) as cnt from " + table_name + " where is_active=1", 0)
    def count_by_query(self, sql: str):
        return self.get_single_value_int_or_default(sql, 0)

    def insert_single(self, dto: base_write_dto, created_by: str = "system") -> int:
        return self.execute_query_with_params(dto.get_model().insert_attrs_sql, dto.get_list_write_insert(created_by))
    def insert_many_with_model(self, model: base_model, dtos: list[base_write_dto], created_by: str = "system") -> int:
        params = list(map(lambda x: x.get_list_write_insert(created_by), dtos))
        return self.execute_queries_with_params(model.insert_attrs_sql, params)
    def insert_many(self, dtos: list[base_write_dto], created_by: str = "system") -> int:
        if len(dtos) > 0:
            model = dtos[0].get_model()
            return self.insert_many_with_model(model, dtos, created_by)
        else:
            return 0

    def delete_logical_by_any_column(self, col_name: str, col_value: any, removed_by: str) -> int:
        m = self.get_model()
        return self.execute_query_with_params("update " + m.table_name + " set is_active=0, row_version=row_version+1, last_updated_date=now(), last_updated_by=%s, removed_date=now(), removed_by=%s  where " + col_name + "=%s", (removed_by, removed_by, col_value,))

    def delete_logical_by_uid(self, uid: str, removed_by: str) -> int:
        m = self.get_model()
        return self.delete_logical_by_any_column(m.key_column_name, uid, removed_by)
    def delete_logical_by_uids(self, uids: list[str], removed_by: str) -> int:
        m = self.get_model()
        sql = "update " + m.table_name + " set is_active=0, row_version=row_version+1, last_updated_date=now(), last_updated_by=%s, removed_date=now(), removed_by=%s  where " + m.key_column_name + "=%s"
        params = list(map(lambda uid: (removed_by, removed_by, uid,), uids))
        return self.execute_queries_with_params(sql, params)
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
        return self.execute_query_with_params("update " + m.table_name + " set is_active=0, row_version=row_version+1, last_updated_date=now(), last_updated_by=%s, removed_date=now(), removed_by=%s  where created_date < %s", (removed_by, removed_by, dt,))
    def delete_physical_by_uid(self, uid: str):
        m = self.get_model()
        return self.execute_query_with_params("delete from " + m.table_name + " where " + m.key_column_name + "=%s", (uid, ))
    def delete_physical_for_deleted_logical(self):
        m = self.get_model()
        return self.execute_query("delete from " + m.table_name + " where is_active=0")
    def delete_physical_before_created(self, dt: datetime.datetime):
        m = self.get_model()
        return self.execute_query_with_params("delete from " + m.table_name + " where created_date < %s", (dt, ))
    def update_single_column_by_uid(self, uid: str, col_name: str, col_value: str, updated_by: str = "system"):
        m = self.get_model()
        sql = "update " + m.table_name + " set " + col_name + "=%s, row_version=row_version+1, last_updated_date=now(), last_updated_by=%s where " + m.key_column_name + "=%s"
        return self.execute_query_with_params(sql, (col_value, updated_by, uid,))
    def update_single_column_by_id(self, id: int, col_name: str, col_value: str, updated_by: str = "system"):
        m = self.get_model()
        sql = "update " + m.table_name + " set " + col_name + "=%s, row_version=row_version+1, last_updated_date=now(), last_updated_by=%s where id=%s"
        return self.execute_query_with_params(sql, (col_value, updated_by, id,))
    def update_write_dto(self, dto: base_write_dto, updated_by: str = "system"):
        m = self.get_model()
        params = dto.get_list_write_update(updated_by)
        return self.execute_query_with_params(m.update_attrs_sql, params)
    def update_write_dtos(self, dtos: list[base_write_dto], updated_by: str = "system"):
        m = self.get_model()
        params = list(map(lambda dto: dto.get_list_write_update(updated_by), dtos))
        return self.execute_queries_with_params(m.update_attrs_sql, params)
    def upsert_write_dto(self, dto: base_write_dto, updated_by: str = "system"):
        m = self.get_model()
        params = dto.get_list_write_insert(updated_by)
        return self.execute_query_with_params(m.upsert_attrs_sql, params)
    def upsert_write_dtos(self, dtos: list[base_write_dto], updated_by: str = "system"):
        m = self.get_model()
        params = list(map(lambda dto: dto.get_list_write_insert(updated_by), dtos))
        return self.execute_queries_with_params(m.upsert_attrs_sql, params)



