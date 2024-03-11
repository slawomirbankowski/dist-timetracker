import dao.dao_connection
from typing import TypeVar, Generic, List, Iterable
from dao.daos import base_dao
from dto.dtos import *
from dto.dtos_read import *
from dto.dtos_read_list import *
from dto.dtos_write import *
from dto.dtos_write_list import *

class account_division_dao(base_dao):
    def __init__(self):
        super.__init__()
        print("Starting account_division DAO")
    def get_model(self) -> base_model:
        return account_division_model
    def get_items(self, sql: str) -> list[account_division_read_dto]:
        return list(map(lambda r: account_division_read_dto(*r), self.get_objects(sql)))
    def get_items_with_params(self, sql: str, params: Iterable) -> list[account_division_read_dto]:
        return list(map(lambda r: account_division_read_dto(*r), self.get_objects_by_params(sql, params)))
    def get_items_write(self, sql: str) -> list[account_division_write_dto]:
        return list(map(lambda r: account_division_write_dto(*r), self.get_objects(sql)))
    def get_items_write_with_params(self, sql: str, params: Iterable) -> list[account_division_write_dto]:
        return list(map(lambda r: account_division_write_dto(*r), self.get_objects_by_params(sql, params)))
    def get_items_all(self, n: int = 1000) -> account_division_read_dtos:
        return account_division_read_dtos(self.get_items(self.get_model().get_select_all_limit_sql(n)))
    def get_items_active(self, n: int = 1000) -> account_division_read_dtos:
        return account_division_read_dtos(self.get_items(self.get_model().get_select_active_limit_sql(n)))
    def get_items_all_latest(self, n: int = 1000) -> account_division_read_dtos:
        return account_division_read_dtos(self.get_items(self.get_model().get_select_all_latest_sql(n)))
    def get_items_active_latest(self, n: int = 1000) -> account_division_read_dtos:
        return account_division_read_dtos(self.get_items(self.get_model().get_select_active_latest_sql(n)))
    def get_items_write_all(self, n: int = 1000) -> account_division_write_dtos:
        return account_division_write_dtos(self.get_items_write(self.get_model().get_select_write_all_limit_sql(n)))
    def get_items_write_active(self, n: int = 1000) -> account_division_write_dtos:
        return account_division_write_dtos(self.get_items_write(self.get_model().get_select_write_active_limit_sql(n)))
    def get_items_write_all_latest(self, n: int = 1000) -> account_division_write_dtos:
        return account_division_write_dtos(self.get_items_write(self.get_model().get_select_write_all_latest_sql(n)))
    def get_items_write_active_latest(self, n: int = 1000) -> account_division_write_dtos:
        return account_division_write_dtos(self.get_items_write(self.get_model().get_select_write_active_latest_sql(n)))
    def get_item_by_uid(self, uid: str) -> account_division_read_dto | None:
        return account_division_read_dtos(self.get_items_with_params(self.get_model().get_select_by_key(), (uid,))).get_first()
    def get_item_by_id(self, id: int) -> account_division_read_dto | None:
        return account_division_read_dtos(self.get_items_with_params(self.get_model().get_select_by_id(), (id,))).get_first()
    def get_items_by_any_column(self, col_name: str, col_value: any, n: int = 1000) -> account_division_read_dtos:
        return account_division_read_dtos(self.get_items_with_params(self.get_model().get_select_active_by_any_column(col_name, n), (col_value,)))
    def get_uids(self, n: int = 1000) -> list[str]:
        return self.get_column_values_all(self.get_model().get_select_all_keys(n))
    def get_guids(self, n: int = 1000) -> list[str]:
        return self.get_column_values_all(self.get_model().get_select_all_guids(n))
    def count_all(self) -> int:
        return self.get_single_value_int_or_default(self.get_model().get_select_count_all_sql())
    def count_active(self) -> int:
        return self.get_single_value_int_or_default(self.get_model().get_select_count_active_sql())
    def count_by_any_column(self, col_name: str, col_value: any) -> int:
        return self.get_single_value_int_or_default_by_params(self.get_model().get_select_count_by_any_column_sql(col_name), (col_value,))
    def insert_dtos(self, dtos: list[account_division_write_dto], created_by: str):
        self.insert_many(dtos, created_by)
    def insert_write_dtos(self, dtos: account_division_write_dtos, created_by: str):
        self.insert_dtos(dtos.dtos, created_by)
    def insert_read_dtos(self, dtos: account_division_read_dtos, created_by: str):
        self.insert_dtos(dtos.get_write_dtos(), created_by)
    def delete_logical_dtos(self, dtos: list[account_division_write_dto], removed_by: str):
        uids = list(map(lambda dto: dto.get_uid(), dtos))
        return self.delete_logical_by_uids(uids, removed_by)
    def delete_logical_write_dtos(self, dtos: account_division_write_dtos, removed_by: str):
        return self.delete_logical_dtos(dtos.dtos, removed_by)


class account_group_dao(base_dao):
    def __init__(self):
        print("Starting account_group DAO")
    def get_model(self) -> base_model:
        return account_group_model
    def get_items(self, sql: str) -> list[account_group_read_dto]:
        return list(map(lambda r: account_group_read_dto(*r), self.get_objects(sql)))
    def get_items_with_params(self, sql: str, params: Iterable) -> list[account_group_read_dto]:
        return list(map(lambda r: account_group_read_dto(*r), self.get_objects_by_params(sql, params)))
    def get_items_write(self, sql: str) -> list[account_group_write_dto]:
        return list(map(lambda r: account_group_write_dto(*r), self.get_objects(sql)))
    def get_items_write_with_params(self, sql: str, params: Iterable) -> list[account_group_write_dto]:
        return list(map(lambda r: account_group_write_dto(*r), self.get_objects_by_params(sql, params)))
    def get_items_all(self, n: int = 1000) -> account_group_read_dtos:
        return account_group_read_dtos(self.get_items(self.get_model().get_select_all_limit_sql(n)))
    def get_items_active(self, n: int = 1000) -> account_group_read_dtos:
        return account_group_read_dtos(self.get_items(self.get_model().get_select_active_limit_sql(n)))
    def get_items_all_latest(self, n: int = 1000) -> account_group_read_dtos:
        return account_group_read_dtos(self.get_items(self.get_model().get_select_all_latest_sql(n)))
    def get_items_active_latest(self, n: int = 1000) -> account_group_read_dtos:
        return account_group_read_dtos(self.get_items(self.get_model().get_select_active_latest_sql(n)))
    def get_items_write_all(self, n: int = 1000) -> account_group_write_dtos:
        return account_group_write_dtos(self.get_items_write(self.get_model().get_select_write_all_limit_sql(n)))
    def get_items_write_active(self, n: int = 1000) -> account_group_write_dtos:
        return account_group_write_dtos(self.get_items_write(self.get_model().get_select_write_active_limit_sql(n)))
    def get_items_write_all_latest(self, n: int = 1000) -> account_group_write_dtos:
        return account_group_write_dtos(self.get_items_write(self.get_model().get_select_write_all_latest_sql(n)))
    def get_items_write_active_latest(self, n: int = 1000) -> account_group_write_dtos:
        return account_group_write_dtos(self.get_items_write(self.get_model().get_select_write_active_latest_sql(n)))
    def get_item_by_uid(self, uid: str) -> account_group_read_dto | None:
        return account_group_read_dtos(self.get_items_with_params(self.get_model().get_select_by_key(), (uid,))).get_first()
    def get_item_by_id(self, id: int) -> account_group_read_dto | None:
        return account_group_read_dtos(self.get_items_with_params(self.get_model().get_select_by_id(), (id,))).get_first()
    def get_items_by_any_column(self, col_name: str, col_value: any, n: int = 1000) -> account_group_read_dtos:
        return account_group_read_dtos(self.get_items_with_params(self.get_model().get_select_active_by_any_column(col_name, n), (col_value,)))
    def get_uids(self, n: int = 1000) -> list[str]:
        return self.get_column_values_all(self.get_model().get_select_all_keys(n))
    def get_guids(self, n: int = 1000) -> list[str]:
        return self.get_column_values_all(self.get_model().get_select_all_guids(n))
    def count_all(self) -> int:
        return self.get_single_value_int_or_default(self.get_model().get_select_count_all_sql())
    def count_active(self) -> int:
        return self.get_single_value_int_or_default(self.get_model().get_select_count_active_sql())
    def count_by_any_column(self, col_name: str, col_value: any) -> int:
        return self.get_single_value_int_or_default_by_params(self.get_model().get_select_count_by_any_column_sql(col_name), (col_value,))
    def insert_dtos(self, dtos: list[account_group_write_dto], created_by: str):
        self.insert_many(dtos, created_by)
    def insert_write_dtos(self, dtos: account_group_write_dtos, created_by: str):
        self.insert_dtos(dtos.dtos, created_by)
    def insert_read_dtos(self, dtos: account_group_read_dtos, created_by: str):
        self.insert_dtos(dtos.get_write_dtos(), created_by)
    def delete_logical_dtos(self, dtos: list[account_group_write_dto], removed_by: str):
        uids = list(map(lambda dto: dto.get_uid(), dtos))
        return self.delete_logical_by_uids(uids, removed_by)
    def delete_logical_write_dtos(self, dtos: account_group_write_dtos, removed_by: str):
        return self.delete_logical_dtos(dtos.dtos, removed_by)


class account_instance_dao(base_dao):
    def __init__(self):
        print("Starting account_instance DAO")
    def get_model(self) -> base_model:
        return account_instance_model
    def get_items(self, sql: str) -> list[account_instance_read_dto]:
        return list(map(lambda r: account_instance_read_dto(*r), self.get_objects(sql)))
    def get_items_with_params(self, sql: str, params: Iterable) -> list[account_instance_read_dto]:
        return list(map(lambda r: account_instance_read_dto(*r), self.get_objects_by_params(sql, params)))
    def get_items_write(self, sql: str) -> list[account_instance_write_dto]:
        return list(map(lambda r: account_instance_write_dto(*r), self.get_objects(sql)))
    def get_items_write_with_params(self, sql: str, params: Iterable) -> list[account_instance_write_dto]:
        return list(map(lambda r: account_instance_write_dto(*r), self.get_objects_by_params(sql, params)))
    def get_items_all(self, n: int = 1000) -> account_instance_read_dtos:
        return account_instance_read_dtos(self.get_items(self.get_model().get_select_all_limit_sql(n)))
    def get_items_active(self, n: int = 1000) -> account_instance_read_dtos:
        return account_instance_read_dtos(self.get_items(self.get_model().get_select_active_limit_sql(n)))
    def get_items_all_latest(self, n: int = 1000) -> account_instance_read_dtos:
        return account_instance_read_dtos(self.get_items(self.get_model().get_select_all_latest_sql(n)))
    def get_items_active_latest(self, n: int = 1000) -> account_instance_read_dtos:
        return account_instance_read_dtos(self.get_items(self.get_model().get_select_active_latest_sql(n)))
    def get_items_write_all(self, n: int = 1000) -> account_instance_write_dtos:
        return account_instance_write_dtos(self.get_items_write(self.get_model().get_select_write_all_limit_sql(n)))
    def get_items_write_active(self, n: int = 1000) -> account_instance_write_dtos:
        return account_instance_write_dtos(self.get_items_write(self.get_model().get_select_write_active_limit_sql(n)))
    def get_items_write_all_latest(self, n: int = 1000) -> account_instance_write_dtos:
        return account_instance_write_dtos(self.get_items_write(self.get_model().get_select_write_all_latest_sql(n)))
    def get_items_write_active_latest(self, n: int = 1000) -> account_instance_write_dtos:
        return account_instance_write_dtos(self.get_items_write(self.get_model().get_select_write_active_latest_sql(n)))
    def get_item_by_uid(self, uid: str) -> account_instance_read_dto | None:
        return account_instance_read_dtos(self.get_items_with_params(self.get_model().get_select_by_key(), (uid,))).get_first()
    def get_item_by_id(self, id: int) -> account_instance_read_dto | None:
        return account_instance_read_dtos(self.get_items_with_params(self.get_model().get_select_by_id(), (id,))).get_first()
    def get_items_by_any_column(self, col_name: str, col_value: any, n: int = 1000) -> account_instance_read_dtos:
        return account_instance_read_dtos(self.get_items_with_params(self.get_model().get_select_active_by_any_column(col_name, n), (col_value,)))
    def get_uids(self, n: int = 1000) -> list[str]:
        return self.get_column_values_all(self.get_model().get_select_all_keys(n))
    def get_guids(self, n: int = 1000) -> list[str]:
        return self.get_column_values_all(self.get_model().get_select_all_guids(n))
    def count_all(self) -> int:
        return self.get_single_value_int_or_default(self.get_model().get_select_count_all_sql())
    def count_active(self) -> int:
        return self.get_single_value_int_or_default(self.get_model().get_select_count_active_sql())
    def count_by_any_column(self, col_name: str, col_value: any) -> int:
        return self.get_single_value_int_or_default_by_params(self.get_model().get_select_count_by_any_column_sql(col_name), (col_value,))
    def insert_dtos(self, dtos: list[account_instance_write_dto], created_by: str):
        self.insert_many(dtos, created_by)
    def insert_write_dtos(self, dtos: account_instance_write_dtos, created_by: str):
        self.insert_dtos(dtos.dtos, created_by)
    def insert_read_dtos(self, dtos: account_instance_read_dtos, created_by: str):
        self.insert_dtos(dtos.get_write_dtos(), created_by)
    def delete_logical_dtos(self, dtos: list[account_instance_write_dto], removed_by: str):
        uids = list(map(lambda dto: dto.get_uid(), dtos))
        return self.delete_logical_by_uids(uids, removed_by)
    def delete_logical_write_dtos(self, dtos: account_instance_write_dtos, removed_by: str):
        return self.delete_logical_dtos(dtos.dtos, removed_by)


class account_title_dao(base_dao):
    def __init__(self):
        print("Starting account_title DAO")
    def get_model(self) -> base_model:
        return account_title_model
    def get_items(self, sql: str) -> list[account_title_read_dto]:
        return list(map(lambda r: account_title_read_dto(*r), self.get_objects(sql)))
    def get_items_with_params(self, sql: str, params: Iterable) -> list[account_title_read_dto]:
        return list(map(lambda r: account_title_read_dto(*r), self.get_objects_by_params(sql, params)))
    def get_items_write(self, sql: str) -> list[account_title_write_dto]:
        return list(map(lambda r: account_title_write_dto(*r), self.get_objects(sql)))
    def get_items_write_with_params(self, sql: str, params: Iterable) -> list[account_title_write_dto]:
        return list(map(lambda r: account_title_write_dto(*r), self.get_objects_by_params(sql, params)))
    def get_items_all(self, n: int = 1000) -> account_title_read_dtos:
        return account_title_read_dtos(self.get_items(self.get_model().get_select_all_limit_sql(n)))
    def get_items_active(self, n: int = 1000) -> account_title_read_dtos:
        return account_title_read_dtos(self.get_items(self.get_model().get_select_active_limit_sql(n)))
    def get_items_all_latest(self, n: int = 1000) -> account_title_read_dtos:
        return account_title_read_dtos(self.get_items(self.get_model().get_select_all_latest_sql(n)))
    def get_items_active_latest(self, n: int = 1000) -> account_title_read_dtos:
        return account_title_read_dtos(self.get_items(self.get_model().get_select_active_latest_sql(n)))
    def get_items_write_all(self, n: int = 1000) -> account_title_write_dtos:
        return account_title_write_dtos(self.get_items_write(self.get_model().get_select_write_all_limit_sql(n)))
    def get_items_write_active(self, n: int = 1000) -> account_title_write_dtos:
        return account_title_write_dtos(self.get_items_write(self.get_model().get_select_write_active_limit_sql(n)))
    def get_items_write_all_latest(self, n: int = 1000) -> account_title_write_dtos:
        return account_title_write_dtos(self.get_items_write(self.get_model().get_select_write_all_latest_sql(n)))
    def get_items_write_active_latest(self, n: int = 1000) -> account_title_write_dtos:
        return account_title_write_dtos(self.get_items_write(self.get_model().get_select_write_active_latest_sql(n)))
    def get_item_by_uid(self, uid: str) -> account_title_read_dto | None:
        return account_title_read_dtos(self.get_items_with_params(self.get_model().get_select_by_key(), (uid,))).get_first()
    def get_item_by_id(self, id: int) -> account_title_read_dto | None:
        return account_title_read_dtos(self.get_items_with_params(self.get_model().get_select_by_id(), (id,))).get_first()
    def get_items_by_any_column(self, col_name: str, col_value: any, n: int = 1000) -> account_title_read_dtos:
        return account_title_read_dtos(self.get_items_with_params(self.get_model().get_select_active_by_any_column(col_name, n), (col_value,)))
    def get_uids(self, n: int = 1000) -> list[str]:
        return self.get_column_values_all(self.get_model().get_select_all_keys(n))
    def get_guids(self, n: int = 1000) -> list[str]:
        return self.get_column_values_all(self.get_model().get_select_all_guids(n))
    def count_all(self) -> int:
        return self.get_single_value_int_or_default(self.get_model().get_select_count_all_sql())
    def count_active(self) -> int:
        return self.get_single_value_int_or_default(self.get_model().get_select_count_active_sql())
    def count_by_any_column(self, col_name: str, col_value: any) -> int:
        return self.get_single_value_int_or_default_by_params(self.get_model().get_select_count_by_any_column_sql(col_name), (col_value,))
    def insert_dtos(self, dtos: list[account_title_write_dto], created_by: str):
        self.insert_many(dtos, created_by)
    def insert_write_dtos(self, dtos: account_title_write_dtos, created_by: str):
        self.insert_dtos(dtos.dtos, created_by)
    def insert_read_dtos(self, dtos: account_title_read_dtos, created_by: str):
        self.insert_dtos(dtos.get_write_dtos(), created_by)
    def delete_logical_dtos(self, dtos: list[account_title_write_dto], removed_by: str):
        uids = list(map(lambda dto: dto.get_uid(), dtos))
        return self.delete_logical_by_uids(uids, removed_by)
    def delete_logical_write_dtos(self, dtos: account_title_write_dtos, removed_by: str):
        return self.delete_logical_dtos(dtos.dtos, removed_by)


class auth_identity_dao(base_dao):
    def __init__(self):
        print("Starting auth_identity DAO")
    def get_model(self) -> base_model:
        return auth_identity_model
    def get_items(self, sql: str) -> list[auth_identity_read_dto]:
        return list(map(lambda r: auth_identity_read_dto(*r), self.get_objects(sql)))
    def get_items_with_params(self, sql: str, params: Iterable) -> list[auth_identity_read_dto]:
        return list(map(lambda r: auth_identity_read_dto(*r), self.get_objects_by_params(sql, params)))
    def get_items_write(self, sql: str) -> list[auth_identity_write_dto]:
        return list(map(lambda r: auth_identity_write_dto(*r), self.get_objects(sql)))
    def get_items_write_with_params(self, sql: str, params: Iterable) -> list[auth_identity_write_dto]:
        return list(map(lambda r: auth_identity_write_dto(*r), self.get_objects_by_params(sql, params)))
    def get_items_all(self, n: int = 1000) -> auth_identity_read_dtos:
        return auth_identity_read_dtos(self.get_items(self.get_model().get_select_all_limit_sql(n)))
    def get_items_active(self, n: int = 1000) -> auth_identity_read_dtos:
        return auth_identity_read_dtos(self.get_items(self.get_model().get_select_active_limit_sql(n)))
    def get_items_all_latest(self, n: int = 1000) -> auth_identity_read_dtos:
        return auth_identity_read_dtos(self.get_items(self.get_model().get_select_all_latest_sql(n)))
    def get_items_active_latest(self, n: int = 1000) -> auth_identity_read_dtos:
        return auth_identity_read_dtos(self.get_items(self.get_model().get_select_active_latest_sql(n)))
    def get_items_write_all(self, n: int = 1000) -> auth_identity_write_dtos:
        return auth_identity_write_dtos(self.get_items_write(self.get_model().get_select_write_all_limit_sql(n)))
    def get_items_write_active(self, n: int = 1000) -> auth_identity_write_dtos:
        return auth_identity_write_dtos(self.get_items_write(self.get_model().get_select_write_active_limit_sql(n)))
    def get_items_write_all_latest(self, n: int = 1000) -> auth_identity_write_dtos:
        return auth_identity_write_dtos(self.get_items_write(self.get_model().get_select_write_all_latest_sql(n)))
    def get_items_write_active_latest(self, n: int = 1000) -> auth_identity_write_dtos:
        return auth_identity_write_dtos(self.get_items_write(self.get_model().get_select_write_active_latest_sql(n)))
    def get_item_by_uid(self, uid: str) -> auth_identity_read_dto | None:
        return auth_identity_read_dtos(self.get_items_with_params(self.get_model().get_select_by_key(), (uid,))).get_first()
    def get_item_by_id(self, id: int) -> auth_identity_read_dto | None:
        return auth_identity_read_dtos(self.get_items_with_params(self.get_model().get_select_by_id(), (id,))).get_first()
    def get_items_by_any_column(self, col_name: str, col_value: any, n: int = 1000) -> auth_identity_read_dtos:
        return auth_identity_read_dtos(self.get_items_with_params(self.get_model().get_select_active_by_any_column(col_name, n), (col_value,)))
    def get_uids(self, n: int = 1000) -> list[str]:
        return self.get_column_values_all(self.get_model().get_select_all_keys(n))
    def get_guids(self, n: int = 1000) -> list[str]:
        return self.get_column_values_all(self.get_model().get_select_all_guids(n))
    def count_all(self) -> int:
        return self.get_single_value_int_or_default(self.get_model().get_select_count_all_sql())
    def count_active(self) -> int:
        return self.get_single_value_int_or_default(self.get_model().get_select_count_active_sql())
    def count_by_any_column(self, col_name: str, col_value: any) -> int:
        return self.get_single_value_int_or_default_by_params(self.get_model().get_select_count_by_any_column_sql(col_name), (col_value,))
    def insert_dtos(self, dtos: list[auth_identity_write_dto], created_by: str):
        self.insert_many(dtos, created_by)
    def insert_write_dtos(self, dtos: auth_identity_write_dtos, created_by: str):
        self.insert_dtos(dtos.dtos, created_by)
    def insert_read_dtos(self, dtos: auth_identity_read_dtos, created_by: str):
        self.insert_dtos(dtos.get_write_dtos(), created_by)
    def delete_logical_dtos(self, dtos: list[auth_identity_write_dto], removed_by: str):
        uids = list(map(lambda dto: dto.get_uid(), dtos))
        return self.delete_logical_by_uids(uids, removed_by)
    def delete_logical_write_dtos(self, dtos: auth_identity_write_dtos, removed_by: str):
        return self.delete_logical_dtos(dtos.dtos, removed_by)


class auth_password_dao(base_dao):
    def __init__(self):
        print("Starting auth_password DAO")
    def get_model(self) -> base_model:
        return auth_password_model
    def get_items(self, sql: str) -> list[auth_password_read_dto]:
        return list(map(lambda r: auth_password_read_dto(*r), self.get_objects(sql)))
    def get_items_with_params(self, sql: str, params: Iterable) -> list[auth_password_read_dto]:
        return list(map(lambda r: auth_password_read_dto(*r), self.get_objects_by_params(sql, params)))
    def get_items_write(self, sql: str) -> list[auth_password_write_dto]:
        return list(map(lambda r: auth_password_write_dto(*r), self.get_objects(sql)))
    def get_items_write_with_params(self, sql: str, params: Iterable) -> list[auth_password_write_dto]:
        return list(map(lambda r: auth_password_write_dto(*r), self.get_objects_by_params(sql, params)))
    def get_items_all(self, n: int = 1000) -> auth_password_read_dtos:
        return auth_password_read_dtos(self.get_items(self.get_model().get_select_all_limit_sql(n)))
    def get_items_active(self, n: int = 1000) -> auth_password_read_dtos:
        return auth_password_read_dtos(self.get_items(self.get_model().get_select_active_limit_sql(n)))
    def get_items_all_latest(self, n: int = 1000) -> auth_password_read_dtos:
        return auth_password_read_dtos(self.get_items(self.get_model().get_select_all_latest_sql(n)))
    def get_items_active_latest(self, n: int = 1000) -> auth_password_read_dtos:
        return auth_password_read_dtos(self.get_items(self.get_model().get_select_active_latest_sql(n)))
    def get_items_write_all(self, n: int = 1000) -> auth_password_write_dtos:
        return auth_password_write_dtos(self.get_items_write(self.get_model().get_select_write_all_limit_sql(n)))
    def get_items_write_active(self, n: int = 1000) -> auth_password_write_dtos:
        return auth_password_write_dtos(self.get_items_write(self.get_model().get_select_write_active_limit_sql(n)))
    def get_items_write_all_latest(self, n: int = 1000) -> auth_password_write_dtos:
        return auth_password_write_dtos(self.get_items_write(self.get_model().get_select_write_all_latest_sql(n)))
    def get_items_write_active_latest(self, n: int = 1000) -> auth_password_write_dtos:
        return auth_password_write_dtos(self.get_items_write(self.get_model().get_select_write_active_latest_sql(n)))
    def get_item_by_uid(self, uid: str) -> auth_password_read_dto | None:
        return auth_password_read_dtos(self.get_items_with_params(self.get_model().get_select_by_key(), (uid,))).get_first()
    def get_item_by_id(self, id: int) -> auth_password_read_dto | None:
        return auth_password_read_dtos(self.get_items_with_params(self.get_model().get_select_by_id(), (id,))).get_first()
    def get_items_by_any_column(self, col_name: str, col_value: any, n: int = 1000) -> auth_password_read_dtos:
        return auth_password_read_dtos(self.get_items_with_params(self.get_model().get_select_active_by_any_column(col_name, n), (col_value,)))
    def get_uids(self, n: int = 1000) -> list[str]:
        return self.get_column_values_all(self.get_model().get_select_all_keys(n))
    def get_guids(self, n: int = 1000) -> list[str]:
        return self.get_column_values_all(self.get_model().get_select_all_guids(n))
    def count_all(self) -> int:
        return self.get_single_value_int_or_default(self.get_model().get_select_count_all_sql())
    def count_active(self) -> int:
        return self.get_single_value_int_or_default(self.get_model().get_select_count_active_sql())
    def count_by_any_column(self, col_name: str, col_value: any) -> int:
        return self.get_single_value_int_or_default_by_params(self.get_model().get_select_count_by_any_column_sql(col_name), (col_value,))
    def insert_dtos(self, dtos: list[auth_password_write_dto], created_by: str):
        self.insert_many(dtos, created_by)
    def insert_write_dtos(self, dtos: auth_password_write_dtos, created_by: str):
        self.insert_dtos(dtos.dtos, created_by)
    def insert_read_dtos(self, dtos: auth_password_read_dtos, created_by: str):
        self.insert_dtos(dtos.get_write_dtos(), created_by)
    def delete_logical_dtos(self, dtos: list[auth_password_write_dto], removed_by: str):
        uids = list(map(lambda dto: dto.get_uid(), dtos))
        return self.delete_logical_by_uids(uids, removed_by)
    def delete_logical_write_dtos(self, dtos: auth_password_write_dtos, removed_by: str):
        return self.delete_logical_dtos(dtos.dtos, removed_by)


class auth_permission_dao(base_dao):
    def __init__(self):
        print("Starting auth_permission DAO")
    def get_model(self) -> base_model:
        return auth_permission_model
    def get_items(self, sql: str) -> list[auth_permission_read_dto]:
        return list(map(lambda r: auth_permission_read_dto(*r), self.get_objects(sql)))
    def get_items_with_params(self, sql: str, params: Iterable) -> list[auth_permission_read_dto]:
        return list(map(lambda r: auth_permission_read_dto(*r), self.get_objects_by_params(sql, params)))
    def get_items_write(self, sql: str) -> list[auth_permission_write_dto]:
        return list(map(lambda r: auth_permission_write_dto(*r), self.get_objects(sql)))
    def get_items_write_with_params(self, sql: str, params: Iterable) -> list[auth_permission_write_dto]:
        return list(map(lambda r: auth_permission_write_dto(*r), self.get_objects_by_params(sql, params)))
    def get_items_all(self, n: int = 1000) -> auth_permission_read_dtos:
        return auth_permission_read_dtos(self.get_items(self.get_model().get_select_all_limit_sql(n)))
    def get_items_active(self, n: int = 1000) -> auth_permission_read_dtos:
        return auth_permission_read_dtos(self.get_items(self.get_model().get_select_active_limit_sql(n)))
    def get_items_all_latest(self, n: int = 1000) -> auth_permission_read_dtos:
        return auth_permission_read_dtos(self.get_items(self.get_model().get_select_all_latest_sql(n)))
    def get_items_active_latest(self, n: int = 1000) -> auth_permission_read_dtos:
        return auth_permission_read_dtos(self.get_items(self.get_model().get_select_active_latest_sql(n)))
    def get_items_write_all(self, n: int = 1000) -> auth_permission_write_dtos:
        return auth_permission_write_dtos(self.get_items_write(self.get_model().get_select_write_all_limit_sql(n)))
    def get_items_write_active(self, n: int = 1000) -> auth_permission_write_dtos:
        return auth_permission_write_dtos(self.get_items_write(self.get_model().get_select_write_active_limit_sql(n)))
    def get_items_write_all_latest(self, n: int = 1000) -> auth_permission_write_dtos:
        return auth_permission_write_dtos(self.get_items_write(self.get_model().get_select_write_all_latest_sql(n)))
    def get_items_write_active_latest(self, n: int = 1000) -> auth_permission_write_dtos:
        return auth_permission_write_dtos(self.get_items_write(self.get_model().get_select_write_active_latest_sql(n)))
    def get_item_by_uid(self, uid: str) -> auth_permission_read_dto | None:
        return auth_permission_read_dtos(self.get_items_with_params(self.get_model().get_select_by_key(), (uid,))).get_first()
    def get_item_by_id(self, id: int) -> auth_permission_read_dto | None:
        return auth_permission_read_dtos(self.get_items_with_params(self.get_model().get_select_by_id(), (id,))).get_first()
    def get_items_by_any_column(self, col_name: str, col_value: any, n: int = 1000) -> auth_permission_read_dtos:
        return auth_permission_read_dtos(self.get_items_with_params(self.get_model().get_select_active_by_any_column(col_name, n), (col_value,)))
    def get_uids(self, n: int = 1000) -> list[str]:
        return self.get_column_values_all(self.get_model().get_select_all_keys(n))
    def get_guids(self, n: int = 1000) -> list[str]:
        return self.get_column_values_all(self.get_model().get_select_all_guids(n))
    def count_all(self) -> int:
        return self.get_single_value_int_or_default(self.get_model().get_select_count_all_sql())
    def count_active(self) -> int:
        return self.get_single_value_int_or_default(self.get_model().get_select_count_active_sql())
    def count_by_any_column(self, col_name: str, col_value: any) -> int:
        return self.get_single_value_int_or_default_by_params(self.get_model().get_select_count_by_any_column_sql(col_name), (col_value,))
    def insert_dtos(self, dtos: list[auth_permission_write_dto], created_by: str):
        self.insert_many(dtos, created_by)
    def insert_write_dtos(self, dtos: auth_permission_write_dtos, created_by: str):
        self.insert_dtos(dtos.dtos, created_by)
    def insert_read_dtos(self, dtos: auth_permission_read_dtos, created_by: str):
        self.insert_dtos(dtos.get_write_dtos(), created_by)
    def delete_logical_dtos(self, dtos: list[auth_permission_write_dto], removed_by: str):
        uids = list(map(lambda dto: dto.get_uid(), dtos))
        return self.delete_logical_by_uids(uids, removed_by)
    def delete_logical_write_dtos(self, dtos: auth_permission_write_dtos, removed_by: str):
        return self.delete_logical_dtos(dtos.dtos, removed_by)


class auth_request_dao(base_dao):
    def __init__(self):
        print("Starting auth_request DAO")
    def get_model(self) -> base_model:
        return auth_request_model
    def get_items(self, sql: str) -> list[auth_request_read_dto]:
        return list(map(lambda r: auth_request_read_dto(*r), self.get_objects(sql)))
    def get_items_with_params(self, sql: str, params: Iterable) -> list[auth_request_read_dto]:
        return list(map(lambda r: auth_request_read_dto(*r), self.get_objects_by_params(sql, params)))
    def get_items_write(self, sql: str) -> list[auth_request_write_dto]:
        return list(map(lambda r: auth_request_write_dto(*r), self.get_objects(sql)))
    def get_items_write_with_params(self, sql: str, params: Iterable) -> list[auth_request_write_dto]:
        return list(map(lambda r: auth_request_write_dto(*r), self.get_objects_by_params(sql, params)))
    def get_items_all(self, n: int = 1000) -> auth_request_read_dtos:
        return auth_request_read_dtos(self.get_items(self.get_model().get_select_all_limit_sql(n)))
    def get_items_active(self, n: int = 1000) -> auth_request_read_dtos:
        return auth_request_read_dtos(self.get_items(self.get_model().get_select_active_limit_sql(n)))
    def get_items_all_latest(self, n: int = 1000) -> auth_request_read_dtos:
        return auth_request_read_dtos(self.get_items(self.get_model().get_select_all_latest_sql(n)))
    def get_items_active_latest(self, n: int = 1000) -> auth_request_read_dtos:
        return auth_request_read_dtos(self.get_items(self.get_model().get_select_active_latest_sql(n)))
    def get_items_write_all(self, n: int = 1000) -> auth_request_write_dtos:
        return auth_request_write_dtos(self.get_items_write(self.get_model().get_select_write_all_limit_sql(n)))
    def get_items_write_active(self, n: int = 1000) -> auth_request_write_dtos:
        return auth_request_write_dtos(self.get_items_write(self.get_model().get_select_write_active_limit_sql(n)))
    def get_items_write_all_latest(self, n: int = 1000) -> auth_request_write_dtos:
        return auth_request_write_dtos(self.get_items_write(self.get_model().get_select_write_all_latest_sql(n)))
    def get_items_write_active_latest(self, n: int = 1000) -> auth_request_write_dtos:
        return auth_request_write_dtos(self.get_items_write(self.get_model().get_select_write_active_latest_sql(n)))
    def get_item_by_uid(self, uid: str) -> auth_request_read_dto | None:
        return auth_request_read_dtos(self.get_items_with_params(self.get_model().get_select_by_key(), (uid,))).get_first()
    def get_item_by_id(self, id: int) -> auth_request_read_dto | None:
        return auth_request_read_dtos(self.get_items_with_params(self.get_model().get_select_by_id(), (id,))).get_first()
    def get_items_by_any_column(self, col_name: str, col_value: any, n: int = 1000) -> auth_request_read_dtos:
        return auth_request_read_dtos(self.get_items_with_params(self.get_model().get_select_active_by_any_column(col_name, n), (col_value,)))
    def get_uids(self, n: int = 1000) -> list[str]:
        return self.get_column_values_all(self.get_model().get_select_all_keys(n))
    def get_guids(self, n: int = 1000) -> list[str]:
        return self.get_column_values_all(self.get_model().get_select_all_guids(n))
    def count_all(self) -> int:
        return self.get_single_value_int_or_default(self.get_model().get_select_count_all_sql())
    def count_active(self) -> int:
        return self.get_single_value_int_or_default(self.get_model().get_select_count_active_sql())
    def count_by_any_column(self, col_name: str, col_value: any) -> int:
        return self.get_single_value_int_or_default_by_params(self.get_model().get_select_count_by_any_column_sql(col_name), (col_value,))
    def insert_dtos(self, dtos: list[auth_request_write_dto], created_by: str):
        self.insert_many(dtos, created_by)
    def insert_write_dtos(self, dtos: auth_request_write_dtos, created_by: str):
        self.insert_dtos(dtos.dtos, created_by)
    def insert_read_dtos(self, dtos: auth_request_read_dtos, created_by: str):
        self.insert_dtos(dtos.get_write_dtos(), created_by)
    def delete_logical_dtos(self, dtos: list[auth_request_write_dto], removed_by: str):
        uids = list(map(lambda dto: dto.get_uid(), dtos))
        return self.delete_logical_by_uids(uids, removed_by)
    def delete_logical_write_dtos(self, dtos: auth_request_write_dtos, removed_by: str):
        return self.delete_logical_dtos(dtos.dtos, removed_by)


class auth_role_dao(base_dao):
    def __init__(self):
        print("Starting auth_role DAO")
    def get_model(self) -> base_model:
        return auth_role_model
    def get_items(self, sql: str) -> list[auth_role_read_dto]:
        return list(map(lambda r: auth_role_read_dto(*r), self.get_objects(sql)))
    def get_items_with_params(self, sql: str, params: Iterable) -> list[auth_role_read_dto]:
        return list(map(lambda r: auth_role_read_dto(*r), self.get_objects_by_params(sql, params)))
    def get_items_write(self, sql: str) -> list[auth_role_write_dto]:
        return list(map(lambda r: auth_role_write_dto(*r), self.get_objects(sql)))
    def get_items_write_with_params(self, sql: str, params: Iterable) -> list[auth_role_write_dto]:
        return list(map(lambda r: auth_role_write_dto(*r), self.get_objects_by_params(sql, params)))
    def get_items_all(self, n: int = 1000) -> auth_role_read_dtos:
        return auth_role_read_dtos(self.get_items(self.get_model().get_select_all_limit_sql(n)))
    def get_items_active(self, n: int = 1000) -> auth_role_read_dtos:
        return auth_role_read_dtos(self.get_items(self.get_model().get_select_active_limit_sql(n)))
    def get_items_all_latest(self, n: int = 1000) -> auth_role_read_dtos:
        return auth_role_read_dtos(self.get_items(self.get_model().get_select_all_latest_sql(n)))
    def get_items_active_latest(self, n: int = 1000) -> auth_role_read_dtos:
        return auth_role_read_dtos(self.get_items(self.get_model().get_select_active_latest_sql(n)))
    def get_items_write_all(self, n: int = 1000) -> auth_role_write_dtos:
        return auth_role_write_dtos(self.get_items_write(self.get_model().get_select_write_all_limit_sql(n)))
    def get_items_write_active(self, n: int = 1000) -> auth_role_write_dtos:
        return auth_role_write_dtos(self.get_items_write(self.get_model().get_select_write_active_limit_sql(n)))
    def get_items_write_all_latest(self, n: int = 1000) -> auth_role_write_dtos:
        return auth_role_write_dtos(self.get_items_write(self.get_model().get_select_write_all_latest_sql(n)))
    def get_items_write_active_latest(self, n: int = 1000) -> auth_role_write_dtos:
        return auth_role_write_dtos(self.get_items_write(self.get_model().get_select_write_active_latest_sql(n)))
    def get_item_by_uid(self, uid: str) -> auth_role_read_dto | None:
        return auth_role_read_dtos(self.get_items_with_params(self.get_model().get_select_by_key(), (uid,))).get_first()
    def get_item_by_id(self, id: int) -> auth_role_read_dto | None:
        return auth_role_read_dtos(self.get_items_with_params(self.get_model().get_select_by_id(), (id,))).get_first()
    def get_items_by_any_column(self, col_name: str, col_value: any, n: int = 1000) -> auth_role_read_dtos:
        return auth_role_read_dtos(self.get_items_with_params(self.get_model().get_select_active_by_any_column(col_name, n), (col_value,)))
    def get_uids(self, n: int = 1000) -> list[str]:
        return self.get_column_values_all(self.get_model().get_select_all_keys(n))
    def get_guids(self, n: int = 1000) -> list[str]:
        return self.get_column_values_all(self.get_model().get_select_all_guids(n))
    def count_all(self) -> int:
        return self.get_single_value_int_or_default(self.get_model().get_select_count_all_sql())
    def count_active(self) -> int:
        return self.get_single_value_int_or_default(self.get_model().get_select_count_active_sql())
    def count_by_any_column(self, col_name: str, col_value: any) -> int:
        return self.get_single_value_int_or_default_by_params(self.get_model().get_select_count_by_any_column_sql(col_name), (col_value,))
    def insert_dtos(self, dtos: list[auth_role_write_dto], created_by: str):
        self.insert_many(dtos, created_by)
    def insert_write_dtos(self, dtos: auth_role_write_dtos, created_by: str):
        self.insert_dtos(dtos.dtos, created_by)
    def insert_read_dtos(self, dtos: auth_role_read_dtos, created_by: str):
        self.insert_dtos(dtos.get_write_dtos(), created_by)
    def delete_logical_dtos(self, dtos: list[auth_role_write_dto], removed_by: str):
        uids = list(map(lambda dto: dto.get_uid(), dtos))
        return self.delete_logical_by_uids(uids, removed_by)
    def delete_logical_write_dtos(self, dtos: auth_role_write_dtos, removed_by: str):
        return self.delete_logical_dtos(dtos.dtos, removed_by)


class auth_token_dao(base_dao):
    def __init__(self):
        print("Starting auth_token DAO")
    def get_model(self) -> base_model:
        return auth_token_model
    def get_items(self, sql: str) -> list[auth_token_read_dto]:
        return list(map(lambda r: auth_token_read_dto(*r), self.get_objects(sql)))
    def get_items_with_params(self, sql: str, params: Iterable) -> list[auth_token_read_dto]:
        return list(map(lambda r: auth_token_read_dto(*r), self.get_objects_by_params(sql, params)))
    def get_items_write(self, sql: str) -> list[auth_token_write_dto]:
        return list(map(lambda r: auth_token_write_dto(*r), self.get_objects(sql)))
    def get_items_write_with_params(self, sql: str, params: Iterable) -> list[auth_token_write_dto]:
        return list(map(lambda r: auth_token_write_dto(*r), self.get_objects_by_params(sql, params)))
    def get_items_all(self, n: int = 1000) -> auth_token_read_dtos:
        return auth_token_read_dtos(self.get_items(self.get_model().get_select_all_limit_sql(n)))
    def get_items_active(self, n: int = 1000) -> auth_token_read_dtos:
        return auth_token_read_dtos(self.get_items(self.get_model().get_select_active_limit_sql(n)))
    def get_items_all_latest(self, n: int = 1000) -> auth_token_read_dtos:
        return auth_token_read_dtos(self.get_items(self.get_model().get_select_all_latest_sql(n)))
    def get_items_active_latest(self, n: int = 1000) -> auth_token_read_dtos:
        return auth_token_read_dtos(self.get_items(self.get_model().get_select_active_latest_sql(n)))
    def get_items_write_all(self, n: int = 1000) -> auth_token_write_dtos:
        return auth_token_write_dtos(self.get_items_write(self.get_model().get_select_write_all_limit_sql(n)))
    def get_items_write_active(self, n: int = 1000) -> auth_token_write_dtos:
        return auth_token_write_dtos(self.get_items_write(self.get_model().get_select_write_active_limit_sql(n)))
    def get_items_write_all_latest(self, n: int = 1000) -> auth_token_write_dtos:
        return auth_token_write_dtos(self.get_items_write(self.get_model().get_select_write_all_latest_sql(n)))
    def get_items_write_active_latest(self, n: int = 1000) -> auth_token_write_dtos:
        return auth_token_write_dtos(self.get_items_write(self.get_model().get_select_write_active_latest_sql(n)))
    def get_item_by_uid(self, uid: str) -> auth_token_read_dto | None:
        return auth_token_read_dtos(self.get_items_with_params(self.get_model().get_select_by_key(), (uid,))).get_first()
    def get_item_by_id(self, id: int) -> auth_token_read_dto | None:
        return auth_token_read_dtos(self.get_items_with_params(self.get_model().get_select_by_id(), (id,))).get_first()
    def get_items_by_any_column(self, col_name: str, col_value: any, n: int = 1000) -> auth_token_read_dtos:
        return auth_token_read_dtos(self.get_items_with_params(self.get_model().get_select_active_by_any_column(col_name, n), (col_value,)))
    def get_uids(self, n: int = 1000) -> list[str]:
        return self.get_column_values_all(self.get_model().get_select_all_keys(n))
    def get_guids(self, n: int = 1000) -> list[str]:
        return self.get_column_values_all(self.get_model().get_select_all_guids(n))
    def count_all(self) -> int:
        return self.get_single_value_int_or_default(self.get_model().get_select_count_all_sql())
    def count_active(self) -> int:
        return self.get_single_value_int_or_default(self.get_model().get_select_count_active_sql())
    def count_by_any_column(self, col_name: str, col_value: any) -> int:
        return self.get_single_value_int_or_default_by_params(self.get_model().get_select_count_by_any_column_sql(col_name), (col_value,))
    def insert_dtos(self, dtos: list[auth_token_write_dto], created_by: str):
        self.insert_many(dtos, created_by)
    def insert_write_dtos(self, dtos: auth_token_write_dtos, created_by: str):
        self.insert_dtos(dtos.dtos, created_by)
    def insert_read_dtos(self, dtos: auth_token_read_dtos, created_by: str):
        self.insert_dtos(dtos.get_write_dtos(), created_by)
    def delete_logical_dtos(self, dtos: list[auth_token_write_dto], removed_by: str):
        uids = list(map(lambda dto: dto.get_uid(), dtos))
        return self.delete_logical_by_uids(uids, removed_by)
    def delete_logical_write_dtos(self, dtos: auth_token_write_dtos, removed_by: str):
        return self.delete_logical_dtos(dtos.dtos, removed_by)


class client_instance_dao(base_dao):
    def __init__(self):
        print("Starting client_instance DAO")
    def get_model(self) -> base_model:
        return client_instance_model
    def get_items(self, sql: str) -> list[client_instance_read_dto]:
        return list(map(lambda r: client_instance_read_dto(*r), self.get_objects(sql)))
    def get_items_with_params(self, sql: str, params: Iterable) -> list[client_instance_read_dto]:
        return list(map(lambda r: client_instance_read_dto(*r), self.get_objects_by_params(sql, params)))
    def get_items_write(self, sql: str) -> list[client_instance_write_dto]:
        return list(map(lambda r: client_instance_write_dto(*r), self.get_objects(sql)))
    def get_items_write_with_params(self, sql: str, params: Iterable) -> list[client_instance_write_dto]:
        return list(map(lambda r: client_instance_write_dto(*r), self.get_objects_by_params(sql, params)))
    def get_items_all(self, n: int = 1000) -> client_instance_read_dtos:
        return client_instance_read_dtos(self.get_items(self.get_model().get_select_all_limit_sql(n)))
    def get_items_active(self, n: int = 1000) -> client_instance_read_dtos:
        return client_instance_read_dtos(self.get_items(self.get_model().get_select_active_limit_sql(n)))
    def get_items_all_latest(self, n: int = 1000) -> client_instance_read_dtos:
        return client_instance_read_dtos(self.get_items(self.get_model().get_select_all_latest_sql(n)))
    def get_items_active_latest(self, n: int = 1000) -> client_instance_read_dtos:
        return client_instance_read_dtos(self.get_items(self.get_model().get_select_active_latest_sql(n)))
    def get_items_write_all(self, n: int = 1000) -> client_instance_write_dtos:
        return client_instance_write_dtos(self.get_items_write(self.get_model().get_select_write_all_limit_sql(n)))
    def get_items_write_active(self, n: int = 1000) -> client_instance_write_dtos:
        return client_instance_write_dtos(self.get_items_write(self.get_model().get_select_write_active_limit_sql(n)))
    def get_items_write_all_latest(self, n: int = 1000) -> client_instance_write_dtos:
        return client_instance_write_dtos(self.get_items_write(self.get_model().get_select_write_all_latest_sql(n)))
    def get_items_write_active_latest(self, n: int = 1000) -> client_instance_write_dtos:
        return client_instance_write_dtos(self.get_items_write(self.get_model().get_select_write_active_latest_sql(n)))
    def get_item_by_uid(self, uid: str) -> client_instance_read_dto | None:
        return client_instance_read_dtos(self.get_items_with_params(self.get_model().get_select_by_key(), (uid,))).get_first()
    def get_item_by_id(self, id: int) -> client_instance_read_dto | None:
        return client_instance_read_dtos(self.get_items_with_params(self.get_model().get_select_by_id(), (id,))).get_first()
    def get_items_by_any_column(self, col_name: str, col_value: any, n: int = 1000) -> client_instance_read_dtos:
        return client_instance_read_dtos(self.get_items_with_params(self.get_model().get_select_active_by_any_column(col_name, n), (col_value,)))
    def get_uids(self, n: int = 1000) -> list[str]:
        return self.get_column_values_all(self.get_model().get_select_all_keys(n))
    def get_guids(self, n: int = 1000) -> list[str]:
        return self.get_column_values_all(self.get_model().get_select_all_guids(n))
    def count_all(self) -> int:
        return self.get_single_value_int_or_default(self.get_model().get_select_count_all_sql())
    def count_active(self) -> int:
        return self.get_single_value_int_or_default(self.get_model().get_select_count_active_sql())
    def count_by_any_column(self, col_name: str, col_value: any) -> int:
        return self.get_single_value_int_or_default_by_params(self.get_model().get_select_count_by_any_column_sql(col_name), (col_value,))
    def insert_dtos(self, dtos: list[client_instance_write_dto], created_by: str):
        self.insert_many(dtos, created_by)
    def insert_write_dtos(self, dtos: client_instance_write_dtos, created_by: str):
        self.insert_dtos(dtos.dtos, created_by)
    def insert_read_dtos(self, dtos: client_instance_read_dtos, created_by: str):
        self.insert_dtos(dtos.get_write_dtos(), created_by)
    def delete_logical_dtos(self, dtos: list[client_instance_write_dto], removed_by: str):
        uids = list(map(lambda dto: dto.get_uid(), dtos))
        return self.delete_logical_by_uids(uids, removed_by)
    def delete_logical_write_dtos(self, dtos: client_instance_write_dtos, removed_by: str):
        return self.delete_logical_dtos(dtos.dtos, removed_by)


class country_dao(base_dao):
    def __init__(self):
        print("Starting country DAO")
    def get_model(self) -> base_model:
        return country_model
    def get_items(self, sql: str) -> list[country_read_dto]:
        return list(map(lambda r: country_read_dto(*r), self.get_objects(sql)))
    def get_items_with_params(self, sql: str, params: Iterable) -> list[country_read_dto]:
        return list(map(lambda r: country_read_dto(*r), self.get_objects_by_params(sql, params)))
    def get_items_write(self, sql: str) -> list[country_write_dto]:
        return list(map(lambda r: country_write_dto(*r), self.get_objects(sql)))
    def get_items_write_with_params(self, sql: str, params: Iterable) -> list[country_write_dto]:
        return list(map(lambda r: country_write_dto(*r), self.get_objects_by_params(sql, params)))
    def get_items_all(self, n: int = 1000) -> country_read_dtos:
        return country_read_dtos(self.get_items(self.get_model().get_select_all_limit_sql(n)))
    def get_items_active(self, n: int = 1000) -> country_read_dtos:
        return country_read_dtos(self.get_items(self.get_model().get_select_active_limit_sql(n)))
    def get_items_all_latest(self, n: int = 1000) -> country_read_dtos:
        return country_read_dtos(self.get_items(self.get_model().get_select_all_latest_sql(n)))
    def get_items_active_latest(self, n: int = 1000) -> country_read_dtos:
        return country_read_dtos(self.get_items(self.get_model().get_select_active_latest_sql(n)))
    def get_items_write_all(self, n: int = 1000) -> country_write_dtos:
        return country_write_dtos(self.get_items_write(self.get_model().get_select_write_all_limit_sql(n)))
    def get_items_write_active(self, n: int = 1000) -> country_write_dtos:
        return country_write_dtos(self.get_items_write(self.get_model().get_select_write_active_limit_sql(n)))
    def get_items_write_all_latest(self, n: int = 1000) -> country_write_dtos:
        return country_write_dtos(self.get_items_write(self.get_model().get_select_write_all_latest_sql(n)))
    def get_items_write_active_latest(self, n: int = 1000) -> country_write_dtos:
        return country_write_dtos(self.get_items_write(self.get_model().get_select_write_active_latest_sql(n)))
    def get_item_by_uid(self, uid: str) -> country_read_dto | None:
        return country_read_dtos(self.get_items_with_params(self.get_model().get_select_by_key(), (uid,))).get_first()
    def get_item_by_id(self, id: int) -> country_read_dto | None:
        return country_read_dtos(self.get_items_with_params(self.get_model().get_select_by_id(), (id,))).get_first()
    def get_items_by_any_column(self, col_name: str, col_value: any, n: int = 1000) -> country_read_dtos:
        return country_read_dtos(self.get_items_with_params(self.get_model().get_select_active_by_any_column(col_name, n), (col_value,)))
    def get_uids(self, n: int = 1000) -> list[str]:
        return self.get_column_values_all(self.get_model().get_select_all_keys(n))
    def get_guids(self, n: int = 1000) -> list[str]:
        return self.get_column_values_all(self.get_model().get_select_all_guids(n))
    def count_all(self) -> int:
        return self.get_single_value_int_or_default(self.get_model().get_select_count_all_sql())
    def count_active(self) -> int:
        return self.get_single_value_int_or_default(self.get_model().get_select_count_active_sql())
    def count_by_any_column(self, col_name: str, col_value: any) -> int:
        return self.get_single_value_int_or_default_by_params(self.get_model().get_select_count_by_any_column_sql(col_name), (col_value,))
    def insert_dtos(self, dtos: list[country_write_dto], created_by: str):
        self.insert_many(dtos, created_by)
    def insert_write_dtos(self, dtos: country_write_dtos, created_by: str):
        self.insert_dtos(dtos.dtos, created_by)
    def insert_read_dtos(self, dtos: country_read_dtos, created_by: str):
        self.insert_dtos(dtos.get_write_dtos(), created_by)
    def delete_logical_dtos(self, dtos: list[country_write_dto], removed_by: str):
        uids = list(map(lambda dto: dto.get_uid(), dtos))
        return self.delete_logical_by_uids(uids, removed_by)
    def delete_logical_write_dtos(self, dtos: country_write_dtos, removed_by: str):
        return self.delete_logical_dtos(dtos.dtos, removed_by)


class currency_dao(base_dao):
    def __init__(self):
        print("Starting currency DAO")
    def get_model(self) -> base_model:
        return currency_model
    def get_items(self, sql: str) -> list[currency_read_dto]:
        return list(map(lambda r: currency_read_dto(*r), self.get_objects(sql)))
    def get_items_with_params(self, sql: str, params: Iterable) -> list[currency_read_dto]:
        return list(map(lambda r: currency_read_dto(*r), self.get_objects_by_params(sql, params)))
    def get_items_write(self, sql: str) -> list[currency_write_dto]:
        return list(map(lambda r: currency_write_dto(*r), self.get_objects(sql)))
    def get_items_write_with_params(self, sql: str, params: Iterable) -> list[currency_write_dto]:
        return list(map(lambda r: currency_write_dto(*r), self.get_objects_by_params(sql, params)))
    def get_items_all(self, n: int = 1000) -> currency_read_dtos:
        return currency_read_dtos(self.get_items(self.get_model().get_select_all_limit_sql(n)))
    def get_items_active(self, n: int = 1000) -> currency_read_dtos:
        return currency_read_dtos(self.get_items(self.get_model().get_select_active_limit_sql(n)))
    def get_items_all_latest(self, n: int = 1000) -> currency_read_dtos:
        return currency_read_dtos(self.get_items(self.get_model().get_select_all_latest_sql(n)))
    def get_items_active_latest(self, n: int = 1000) -> currency_read_dtos:
        return currency_read_dtos(self.get_items(self.get_model().get_select_active_latest_sql(n)))
    def get_items_write_all(self, n: int = 1000) -> currency_write_dtos:
        return currency_write_dtos(self.get_items_write(self.get_model().get_select_write_all_limit_sql(n)))
    def get_items_write_active(self, n: int = 1000) -> currency_write_dtos:
        return currency_write_dtos(self.get_items_write(self.get_model().get_select_write_active_limit_sql(n)))
    def get_items_write_all_latest(self, n: int = 1000) -> currency_write_dtos:
        return currency_write_dtos(self.get_items_write(self.get_model().get_select_write_all_latest_sql(n)))
    def get_items_write_active_latest(self, n: int = 1000) -> currency_write_dtos:
        return currency_write_dtos(self.get_items_write(self.get_model().get_select_write_active_latest_sql(n)))
    def get_item_by_uid(self, uid: str) -> currency_read_dto | None:
        return currency_read_dtos(self.get_items_with_params(self.get_model().get_select_by_key(), (uid,))).get_first()
    def get_item_by_id(self, id: int) -> currency_read_dto | None:
        return currency_read_dtos(self.get_items_with_params(self.get_model().get_select_by_id(), (id,))).get_first()
    def get_items_by_any_column(self, col_name: str, col_value: any, n: int = 1000) -> currency_read_dtos:
        return currency_read_dtos(self.get_items_with_params(self.get_model().get_select_active_by_any_column(col_name, n), (col_value,)))
    def get_uids(self, n: int = 1000) -> list[str]:
        return self.get_column_values_all(self.get_model().get_select_all_keys(n))
    def get_guids(self, n: int = 1000) -> list[str]:
        return self.get_column_values_all(self.get_model().get_select_all_guids(n))
    def count_all(self) -> int:
        return self.get_single_value_int_or_default(self.get_model().get_select_count_all_sql())
    def count_active(self) -> int:
        return self.get_single_value_int_or_default(self.get_model().get_select_count_active_sql())
    def count_by_any_column(self, col_name: str, col_value: any) -> int:
        return self.get_single_value_int_or_default_by_params(self.get_model().get_select_count_by_any_column_sql(col_name), (col_value,))
    def insert_dtos(self, dtos: list[currency_write_dto], created_by: str):
        self.insert_many(dtos, created_by)
    def insert_write_dtos(self, dtos: currency_write_dtos, created_by: str):
        self.insert_dtos(dtos.dtos, created_by)
    def insert_read_dtos(self, dtos: currency_read_dtos, created_by: str):
        self.insert_dtos(dtos.get_write_dtos(), created_by)
    def delete_logical_dtos(self, dtos: list[currency_write_dto], removed_by: str):
        uids = list(map(lambda dto: dto.get_uid(), dtos))
        return self.delete_logical_by_uids(uids, removed_by)
    def delete_logical_write_dtos(self, dtos: currency_write_dtos, removed_by: str):
        return self.delete_logical_dtos(dtos.dtos, removed_by)


class entry_final_dao(base_dao):
    def __init__(self):
        print("Starting entry_final DAO")
    def get_model(self) -> base_model:
        return entry_final_model
    def get_items(self, sql: str) -> list[entry_final_read_dto]:
        return list(map(lambda r: entry_final_read_dto(*r), self.get_objects(sql)))
    def get_items_with_params(self, sql: str, params: Iterable) -> list[entry_final_read_dto]:
        return list(map(lambda r: entry_final_read_dto(*r), self.get_objects_by_params(sql, params)))
    def get_items_write(self, sql: str) -> list[entry_final_write_dto]:
        return list(map(lambda r: entry_final_write_dto(*r), self.get_objects(sql)))
    def get_items_write_with_params(self, sql: str, params: Iterable) -> list[entry_final_write_dto]:
        return list(map(lambda r: entry_final_write_dto(*r), self.get_objects_by_params(sql, params)))
    def get_items_all(self, n: int = 1000) -> entry_final_read_dtos:
        return entry_final_read_dtos(self.get_items(self.get_model().get_select_all_limit_sql(n)))
    def get_items_active(self, n: int = 1000) -> entry_final_read_dtos:
        return entry_final_read_dtos(self.get_items(self.get_model().get_select_active_limit_sql(n)))
    def get_items_all_latest(self, n: int = 1000) -> entry_final_read_dtos:
        return entry_final_read_dtos(self.get_items(self.get_model().get_select_all_latest_sql(n)))
    def get_items_active_latest(self, n: int = 1000) -> entry_final_read_dtos:
        return entry_final_read_dtos(self.get_items(self.get_model().get_select_active_latest_sql(n)))
    def get_items_write_all(self, n: int = 1000) -> entry_final_write_dtos:
        return entry_final_write_dtos(self.get_items_write(self.get_model().get_select_write_all_limit_sql(n)))
    def get_items_write_active(self, n: int = 1000) -> entry_final_write_dtos:
        return entry_final_write_dtos(self.get_items_write(self.get_model().get_select_write_active_limit_sql(n)))
    def get_items_write_all_latest(self, n: int = 1000) -> entry_final_write_dtos:
        return entry_final_write_dtos(self.get_items_write(self.get_model().get_select_write_all_latest_sql(n)))
    def get_items_write_active_latest(self, n: int = 1000) -> entry_final_write_dtos:
        return entry_final_write_dtos(self.get_items_write(self.get_model().get_select_write_active_latest_sql(n)))
    def get_item_by_uid(self, uid: str) -> entry_final_read_dto | None:
        return entry_final_read_dtos(self.get_items_with_params(self.get_model().get_select_by_key(), (uid,))).get_first()
    def get_item_by_id(self, id: int) -> entry_final_read_dto | None:
        return entry_final_read_dtos(self.get_items_with_params(self.get_model().get_select_by_id(), (id,))).get_first()
    def get_items_by_any_column(self, col_name: str, col_value: any, n: int = 1000) -> entry_final_read_dtos:
        return entry_final_read_dtos(self.get_items_with_params(self.get_model().get_select_active_by_any_column(col_name, n), (col_value,)))
    def get_uids(self, n: int = 1000) -> list[str]:
        return self.get_column_values_all(self.get_model().get_select_all_keys(n))
    def get_guids(self, n: int = 1000) -> list[str]:
        return self.get_column_values_all(self.get_model().get_select_all_guids(n))
    def count_all(self) -> int:
        return self.get_single_value_int_or_default(self.get_model().get_select_count_all_sql())
    def count_active(self) -> int:
        return self.get_single_value_int_or_default(self.get_model().get_select_count_active_sql())
    def count_by_any_column(self, col_name: str, col_value: any) -> int:
        return self.get_single_value_int_or_default_by_params(self.get_model().get_select_count_by_any_column_sql(col_name), (col_value,))
    def insert_dtos(self, dtos: list[entry_final_write_dto], created_by: str):
        self.insert_many(dtos, created_by)
    def insert_write_dtos(self, dtos: entry_final_write_dtos, created_by: str):
        self.insert_dtos(dtos.dtos, created_by)
    def insert_read_dtos(self, dtos: entry_final_read_dtos, created_by: str):
        self.insert_dtos(dtos.get_write_dtos(), created_by)
    def delete_logical_dtos(self, dtos: list[entry_final_write_dto], removed_by: str):
        uids = list(map(lambda dto: dto.get_uid(), dtos))
        return self.delete_logical_by_uids(uids, removed_by)
    def delete_logical_write_dtos(self, dtos: entry_final_write_dtos, removed_by: str):
        return self.delete_logical_dtos(dtos.dtos, removed_by)


class entry_save_dao(base_dao):
    def __init__(self):
        print("Starting entry_save DAO")
    def get_model(self) -> base_model:
        return entry_save_model
    def get_items(self, sql: str) -> list[entry_save_read_dto]:
        return list(map(lambda r: entry_save_read_dto(*r), self.get_objects(sql)))
    def get_items_with_params(self, sql: str, params: Iterable) -> list[entry_save_read_dto]:
        return list(map(lambda r: entry_save_read_dto(*r), self.get_objects_by_params(sql, params)))
    def get_items_write(self, sql: str) -> list[entry_save_write_dto]:
        return list(map(lambda r: entry_save_write_dto(*r), self.get_objects(sql)))
    def get_items_write_with_params(self, sql: str, params: Iterable) -> list[entry_save_write_dto]:
        return list(map(lambda r: entry_save_write_dto(*r), self.get_objects_by_params(sql, params)))
    def get_items_all(self, n: int = 1000) -> entry_save_read_dtos:
        return entry_save_read_dtos(self.get_items(self.get_model().get_select_all_limit_sql(n)))
    def get_items_active(self, n: int = 1000) -> entry_save_read_dtos:
        return entry_save_read_dtos(self.get_items(self.get_model().get_select_active_limit_sql(n)))
    def get_items_all_latest(self, n: int = 1000) -> entry_save_read_dtos:
        return entry_save_read_dtos(self.get_items(self.get_model().get_select_all_latest_sql(n)))
    def get_items_active_latest(self, n: int = 1000) -> entry_save_read_dtos:
        return entry_save_read_dtos(self.get_items(self.get_model().get_select_active_latest_sql(n)))
    def get_items_write_all(self, n: int = 1000) -> entry_save_write_dtos:
        return entry_save_write_dtos(self.get_items_write(self.get_model().get_select_write_all_limit_sql(n)))
    def get_items_write_active(self, n: int = 1000) -> entry_save_write_dtos:
        return entry_save_write_dtos(self.get_items_write(self.get_model().get_select_write_active_limit_sql(n)))
    def get_items_write_all_latest(self, n: int = 1000) -> entry_save_write_dtos:
        return entry_save_write_dtos(self.get_items_write(self.get_model().get_select_write_all_latest_sql(n)))
    def get_items_write_active_latest(self, n: int = 1000) -> entry_save_write_dtos:
        return entry_save_write_dtos(self.get_items_write(self.get_model().get_select_write_active_latest_sql(n)))
    def get_item_by_uid(self, uid: str) -> entry_save_read_dto | None:
        return entry_save_read_dtos(self.get_items_with_params(self.get_model().get_select_by_key(), (uid,))).get_first()
    def get_item_by_id(self, id: int) -> entry_save_read_dto | None:
        return entry_save_read_dtos(self.get_items_with_params(self.get_model().get_select_by_id(), (id,))).get_first()
    def get_items_by_any_column(self, col_name: str, col_value: any, n: int = 1000) -> entry_save_read_dtos:
        return entry_save_read_dtos(self.get_items_with_params(self.get_model().get_select_active_by_any_column(col_name, n), (col_value,)))
    def get_uids(self, n: int = 1000) -> list[str]:
        return self.get_column_values_all(self.get_model().get_select_all_keys(n))
    def get_guids(self, n: int = 1000) -> list[str]:
        return self.get_column_values_all(self.get_model().get_select_all_guids(n))
    def count_all(self) -> int:
        return self.get_single_value_int_or_default(self.get_model().get_select_count_all_sql())
    def count_active(self) -> int:
        return self.get_single_value_int_or_default(self.get_model().get_select_count_active_sql())
    def count_by_any_column(self, col_name: str, col_value: any) -> int:
        return self.get_single_value_int_or_default_by_params(self.get_model().get_select_count_by_any_column_sql(col_name), (col_value,))
    def insert_dtos(self, dtos: list[entry_save_write_dto], created_by: str):
        self.insert_many(dtos, created_by)
    def insert_write_dtos(self, dtos: entry_save_write_dtos, created_by: str):
        self.insert_dtos(dtos.dtos, created_by)
    def insert_read_dtos(self, dtos: entry_save_read_dtos, created_by: str):
        self.insert_dtos(dtos.get_write_dtos(), created_by)
    def delete_logical_dtos(self, dtos: list[entry_save_write_dto], removed_by: str):
        uids = list(map(lambda dto: dto.get_uid(), dtos))
        return self.delete_logical_by_uids(uids, removed_by)
    def delete_logical_write_dtos(self, dtos: entry_save_write_dtos, removed_by: str):
        return self.delete_logical_dtos(dtos.dtos, removed_by)


class event_channel_dao(base_dao):
    def __init__(self):
        print("Starting event_channel DAO")
    def get_model(self) -> base_model:
        return event_channel_model
    def get_items(self, sql: str) -> list[event_channel_read_dto]:
        return list(map(lambda r: event_channel_read_dto(*r), self.get_objects(sql)))
    def get_items_with_params(self, sql: str, params: Iterable) -> list[event_channel_read_dto]:
        return list(map(lambda r: event_channel_read_dto(*r), self.get_objects_by_params(sql, params)))
    def get_items_write(self, sql: str) -> list[event_channel_write_dto]:
        return list(map(lambda r: event_channel_write_dto(*r), self.get_objects(sql)))
    def get_items_write_with_params(self, sql: str, params: Iterable) -> list[event_channel_write_dto]:
        return list(map(lambda r: event_channel_write_dto(*r), self.get_objects_by_params(sql, params)))
    def get_items_all(self, n: int = 1000) -> event_channel_read_dtos:
        return event_channel_read_dtos(self.get_items(self.get_model().get_select_all_limit_sql(n)))
    def get_items_active(self, n: int = 1000) -> event_channel_read_dtos:
        return event_channel_read_dtos(self.get_items(self.get_model().get_select_active_limit_sql(n)))
    def get_items_all_latest(self, n: int = 1000) -> event_channel_read_dtos:
        return event_channel_read_dtos(self.get_items(self.get_model().get_select_all_latest_sql(n)))
    def get_items_active_latest(self, n: int = 1000) -> event_channel_read_dtos:
        return event_channel_read_dtos(self.get_items(self.get_model().get_select_active_latest_sql(n)))
    def get_items_write_all(self, n: int = 1000) -> event_channel_write_dtos:
        return event_channel_write_dtos(self.get_items_write(self.get_model().get_select_write_all_limit_sql(n)))
    def get_items_write_active(self, n: int = 1000) -> event_channel_write_dtos:
        return event_channel_write_dtos(self.get_items_write(self.get_model().get_select_write_active_limit_sql(n)))
    def get_items_write_all_latest(self, n: int = 1000) -> event_channel_write_dtos:
        return event_channel_write_dtos(self.get_items_write(self.get_model().get_select_write_all_latest_sql(n)))
    def get_items_write_active_latest(self, n: int = 1000) -> event_channel_write_dtos:
        return event_channel_write_dtos(self.get_items_write(self.get_model().get_select_write_active_latest_sql(n)))
    def get_item_by_uid(self, uid: str) -> event_channel_read_dto | None:
        return event_channel_read_dtos(self.get_items_with_params(self.get_model().get_select_by_key(), (uid,))).get_first()
    def get_item_by_id(self, id: int) -> event_channel_read_dto | None:
        return event_channel_read_dtos(self.get_items_with_params(self.get_model().get_select_by_id(), (id,))).get_first()
    def get_items_by_any_column(self, col_name: str, col_value: any, n: int = 1000) -> event_channel_read_dtos:
        return event_channel_read_dtos(self.get_items_with_params(self.get_model().get_select_active_by_any_column(col_name, n), (col_value,)))
    def get_uids(self, n: int = 1000) -> list[str]:
        return self.get_column_values_all(self.get_model().get_select_all_keys(n))
    def get_guids(self, n: int = 1000) -> list[str]:
        return self.get_column_values_all(self.get_model().get_select_all_guids(n))
    def count_all(self) -> int:
        return self.get_single_value_int_or_default(self.get_model().get_select_count_all_sql())
    def count_active(self) -> int:
        return self.get_single_value_int_or_default(self.get_model().get_select_count_active_sql())
    def count_by_any_column(self, col_name: str, col_value: any) -> int:
        return self.get_single_value_int_or_default_by_params(self.get_model().get_select_count_by_any_column_sql(col_name), (col_value,))
    def insert_dtos(self, dtos: list[event_channel_write_dto], created_by: str):
        self.insert_many(dtos, created_by)
    def insert_write_dtos(self, dtos: event_channel_write_dtos, created_by: str):
        self.insert_dtos(dtos.dtos, created_by)
    def insert_read_dtos(self, dtos: event_channel_read_dtos, created_by: str):
        self.insert_dtos(dtos.get_write_dtos(), created_by)
    def delete_logical_dtos(self, dtos: list[event_channel_write_dto], removed_by: str):
        uids = list(map(lambda dto: dto.get_uid(), dtos))
        return self.delete_logical_by_uids(uids, removed_by)
    def delete_logical_write_dtos(self, dtos: event_channel_write_dtos, removed_by: str):
        return self.delete_logical_dtos(dtos.dtos, removed_by)


class event_instance_dao(base_dao):
    def __init__(self):
        print("Starting event_instance DAO")
    def get_model(self) -> base_model:
        return event_instance_model
    def get_items(self, sql: str) -> list[event_instance_read_dto]:
        return list(map(lambda r: event_instance_read_dto(*r), self.get_objects(sql)))
    def get_items_with_params(self, sql: str, params: Iterable) -> list[event_instance_read_dto]:
        return list(map(lambda r: event_instance_read_dto(*r), self.get_objects_by_params(sql, params)))
    def get_items_write(self, sql: str) -> list[event_instance_write_dto]:
        return list(map(lambda r: event_instance_write_dto(*r), self.get_objects(sql)))
    def get_items_write_with_params(self, sql: str, params: Iterable) -> list[event_instance_write_dto]:
        return list(map(lambda r: event_instance_write_dto(*r), self.get_objects_by_params(sql, params)))
    def get_items_all(self, n: int = 1000) -> event_instance_read_dtos:
        return event_instance_read_dtos(self.get_items(self.get_model().get_select_all_limit_sql(n)))
    def get_items_active(self, n: int = 1000) -> event_instance_read_dtos:
        return event_instance_read_dtos(self.get_items(self.get_model().get_select_active_limit_sql(n)))
    def get_items_all_latest(self, n: int = 1000) -> event_instance_read_dtos:
        return event_instance_read_dtos(self.get_items(self.get_model().get_select_all_latest_sql(n)))
    def get_items_active_latest(self, n: int = 1000) -> event_instance_read_dtos:
        return event_instance_read_dtos(self.get_items(self.get_model().get_select_active_latest_sql(n)))
    def get_items_write_all(self, n: int = 1000) -> event_instance_write_dtos:
        return event_instance_write_dtos(self.get_items_write(self.get_model().get_select_write_all_limit_sql(n)))
    def get_items_write_active(self, n: int = 1000) -> event_instance_write_dtos:
        return event_instance_write_dtos(self.get_items_write(self.get_model().get_select_write_active_limit_sql(n)))
    def get_items_write_all_latest(self, n: int = 1000) -> event_instance_write_dtos:
        return event_instance_write_dtos(self.get_items_write(self.get_model().get_select_write_all_latest_sql(n)))
    def get_items_write_active_latest(self, n: int = 1000) -> event_instance_write_dtos:
        return event_instance_write_dtos(self.get_items_write(self.get_model().get_select_write_active_latest_sql(n)))
    def get_item_by_uid(self, uid: str) -> event_instance_read_dto | None:
        return event_instance_read_dtos(self.get_items_with_params(self.get_model().get_select_by_key(), (uid,))).get_first()
    def get_item_by_id(self, id: int) -> event_instance_read_dto | None:
        return event_instance_read_dtos(self.get_items_with_params(self.get_model().get_select_by_id(), (id,))).get_first()
    def get_items_by_any_column(self, col_name: str, col_value: any, n: int = 1000) -> event_instance_read_dtos:
        return event_instance_read_dtos(self.get_items_with_params(self.get_model().get_select_active_by_any_column(col_name, n), (col_value,)))
    def get_uids(self, n: int = 1000) -> list[str]:
        return self.get_column_values_all(self.get_model().get_select_all_keys(n))
    def get_guids(self, n: int = 1000) -> list[str]:
        return self.get_column_values_all(self.get_model().get_select_all_guids(n))
    def count_all(self) -> int:
        return self.get_single_value_int_or_default(self.get_model().get_select_count_all_sql())
    def count_active(self) -> int:
        return self.get_single_value_int_or_default(self.get_model().get_select_count_active_sql())
    def count_by_any_column(self, col_name: str, col_value: any) -> int:
        return self.get_single_value_int_or_default_by_params(self.get_model().get_select_count_by_any_column_sql(col_name), (col_value,))
    def insert_dtos(self, dtos: list[event_instance_write_dto], created_by: str):
        self.insert_many(dtos, created_by)
    def insert_write_dtos(self, dtos: event_instance_write_dtos, created_by: str):
        self.insert_dtos(dtos.dtos, created_by)
    def insert_read_dtos(self, dtos: event_instance_read_dtos, created_by: str):
        self.insert_dtos(dtos.get_write_dtos(), created_by)
    def delete_logical_dtos(self, dtos: list[event_instance_write_dto], removed_by: str):
        uids = list(map(lambda dto: dto.get_uid(), dtos))
        return self.delete_logical_by_uids(uids, removed_by)
    def delete_logical_write_dtos(self, dtos: event_instance_write_dtos, removed_by: str):
        return self.delete_logical_dtos(dtos.dtos, removed_by)


class event_subscription_dao(base_dao):
    def __init__(self):
        print("Starting event_subscription DAO")
    def get_model(self) -> base_model:
        return event_subscription_model
    def get_items(self, sql: str) -> list[event_subscription_read_dto]:
        return list(map(lambda r: event_subscription_read_dto(*r), self.get_objects(sql)))
    def get_items_with_params(self, sql: str, params: Iterable) -> list[event_subscription_read_dto]:
        return list(map(lambda r: event_subscription_read_dto(*r), self.get_objects_by_params(sql, params)))
    def get_items_write(self, sql: str) -> list[event_subscription_write_dto]:
        return list(map(lambda r: event_subscription_write_dto(*r), self.get_objects(sql)))
    def get_items_write_with_params(self, sql: str, params: Iterable) -> list[event_subscription_write_dto]:
        return list(map(lambda r: event_subscription_write_dto(*r), self.get_objects_by_params(sql, params)))
    def get_items_all(self, n: int = 1000) -> event_subscription_read_dtos:
        return event_subscription_read_dtos(self.get_items(self.get_model().get_select_all_limit_sql(n)))
    def get_items_active(self, n: int = 1000) -> event_subscription_read_dtos:
        return event_subscription_read_dtos(self.get_items(self.get_model().get_select_active_limit_sql(n)))
    def get_items_all_latest(self, n: int = 1000) -> event_subscription_read_dtos:
        return event_subscription_read_dtos(self.get_items(self.get_model().get_select_all_latest_sql(n)))
    def get_items_active_latest(self, n: int = 1000) -> event_subscription_read_dtos:
        return event_subscription_read_dtos(self.get_items(self.get_model().get_select_active_latest_sql(n)))
    def get_items_write_all(self, n: int = 1000) -> event_subscription_write_dtos:
        return event_subscription_write_dtos(self.get_items_write(self.get_model().get_select_write_all_limit_sql(n)))
    def get_items_write_active(self, n: int = 1000) -> event_subscription_write_dtos:
        return event_subscription_write_dtos(self.get_items_write(self.get_model().get_select_write_active_limit_sql(n)))
    def get_items_write_all_latest(self, n: int = 1000) -> event_subscription_write_dtos:
        return event_subscription_write_dtos(self.get_items_write(self.get_model().get_select_write_all_latest_sql(n)))
    def get_items_write_active_latest(self, n: int = 1000) -> event_subscription_write_dtos:
        return event_subscription_write_dtos(self.get_items_write(self.get_model().get_select_write_active_latest_sql(n)))
    def get_item_by_uid(self, uid: str) -> event_subscription_read_dto | None:
        return event_subscription_read_dtos(self.get_items_with_params(self.get_model().get_select_by_key(), (uid,))).get_first()
    def get_item_by_id(self, id: int) -> event_subscription_read_dto | None:
        return event_subscription_read_dtos(self.get_items_with_params(self.get_model().get_select_by_id(), (id,))).get_first()
    def get_items_by_any_column(self, col_name: str, col_value: any, n: int = 1000) -> event_subscription_read_dtos:
        return event_subscription_read_dtos(self.get_items_with_params(self.get_model().get_select_active_by_any_column(col_name, n), (col_value,)))
    def get_uids(self, n: int = 1000) -> list[str]:
        return self.get_column_values_all(self.get_model().get_select_all_keys(n))
    def get_guids(self, n: int = 1000) -> list[str]:
        return self.get_column_values_all(self.get_model().get_select_all_guids(n))
    def count_all(self) -> int:
        return self.get_single_value_int_or_default(self.get_model().get_select_count_all_sql())
    def count_active(self) -> int:
        return self.get_single_value_int_or_default(self.get_model().get_select_count_active_sql())
    def count_by_any_column(self, col_name: str, col_value: any) -> int:
        return self.get_single_value_int_or_default_by_params(self.get_model().get_select_count_by_any_column_sql(col_name), (col_value,))
    def insert_dtos(self, dtos: list[event_subscription_write_dto], created_by: str):
        self.insert_many(dtos, created_by)
    def insert_write_dtos(self, dtos: event_subscription_write_dtos, created_by: str):
        self.insert_dtos(dtos.dtos, created_by)
    def insert_read_dtos(self, dtos: event_subscription_read_dtos, created_by: str):
        self.insert_dtos(dtos.get_write_dtos(), created_by)
    def delete_logical_dtos(self, dtos: list[event_subscription_write_dto], removed_by: str):
        uids = list(map(lambda dto: dto.get_uid(), dtos))
        return self.delete_logical_by_uids(uids, removed_by)
    def delete_logical_write_dtos(self, dtos: event_subscription_write_dtos, removed_by: str):
        return self.delete_logical_dtos(dtos.dtos, removed_by)


class invoice_instance_dao(base_dao):
    def __init__(self):
        print("Starting invoice_instance DAO")
    def get_model(self) -> base_model:
        return invoice_instance_model
    def get_items(self, sql: str) -> list[invoice_instance_read_dto]:
        return list(map(lambda r: invoice_instance_read_dto(*r), self.get_objects(sql)))
    def get_items_with_params(self, sql: str, params: Iterable) -> list[invoice_instance_read_dto]:
        return list(map(lambda r: invoice_instance_read_dto(*r), self.get_objects_by_params(sql, params)))
    def get_items_write(self, sql: str) -> list[invoice_instance_write_dto]:
        return list(map(lambda r: invoice_instance_write_dto(*r), self.get_objects(sql)))
    def get_items_write_with_params(self, sql: str, params: Iterable) -> list[invoice_instance_write_dto]:
        return list(map(lambda r: invoice_instance_write_dto(*r), self.get_objects_by_params(sql, params)))
    def get_items_all(self, n: int = 1000) -> invoice_instance_read_dtos:
        return invoice_instance_read_dtos(self.get_items(self.get_model().get_select_all_limit_sql(n)))
    def get_items_active(self, n: int = 1000) -> invoice_instance_read_dtos:
        return invoice_instance_read_dtos(self.get_items(self.get_model().get_select_active_limit_sql(n)))
    def get_items_all_latest(self, n: int = 1000) -> invoice_instance_read_dtos:
        return invoice_instance_read_dtos(self.get_items(self.get_model().get_select_all_latest_sql(n)))
    def get_items_active_latest(self, n: int = 1000) -> invoice_instance_read_dtos:
        return invoice_instance_read_dtos(self.get_items(self.get_model().get_select_active_latest_sql(n)))
    def get_items_write_all(self, n: int = 1000) -> invoice_instance_write_dtos:
        return invoice_instance_write_dtos(self.get_items_write(self.get_model().get_select_write_all_limit_sql(n)))
    def get_items_write_active(self, n: int = 1000) -> invoice_instance_write_dtos:
        return invoice_instance_write_dtos(self.get_items_write(self.get_model().get_select_write_active_limit_sql(n)))
    def get_items_write_all_latest(self, n: int = 1000) -> invoice_instance_write_dtos:
        return invoice_instance_write_dtos(self.get_items_write(self.get_model().get_select_write_all_latest_sql(n)))
    def get_items_write_active_latest(self, n: int = 1000) -> invoice_instance_write_dtos:
        return invoice_instance_write_dtos(self.get_items_write(self.get_model().get_select_write_active_latest_sql(n)))
    def get_item_by_uid(self, uid: str) -> invoice_instance_read_dto | None:
        return invoice_instance_read_dtos(self.get_items_with_params(self.get_model().get_select_by_key(), (uid,))).get_first()
    def get_item_by_id(self, id: int) -> invoice_instance_read_dto | None:
        return invoice_instance_read_dtos(self.get_items_with_params(self.get_model().get_select_by_id(), (id,))).get_first()
    def get_items_by_any_column(self, col_name: str, col_value: any, n: int = 1000) -> invoice_instance_read_dtos:
        return invoice_instance_read_dtos(self.get_items_with_params(self.get_model().get_select_active_by_any_column(col_name, n), (col_value,)))
    def get_uids(self, n: int = 1000) -> list[str]:
        return self.get_column_values_all(self.get_model().get_select_all_keys(n))
    def get_guids(self, n: int = 1000) -> list[str]:
        return self.get_column_values_all(self.get_model().get_select_all_guids(n))
    def count_all(self) -> int:
        return self.get_single_value_int_or_default(self.get_model().get_select_count_all_sql())
    def count_active(self) -> int:
        return self.get_single_value_int_or_default(self.get_model().get_select_count_active_sql())
    def count_by_any_column(self, col_name: str, col_value: any) -> int:
        return self.get_single_value_int_or_default_by_params(self.get_model().get_select_count_by_any_column_sql(col_name), (col_value,))
    def insert_dtos(self, dtos: list[invoice_instance_write_dto], created_by: str):
        self.insert_many(dtos, created_by)
    def insert_write_dtos(self, dtos: invoice_instance_write_dtos, created_by: str):
        self.insert_dtos(dtos.dtos, created_by)
    def insert_read_dtos(self, dtos: invoice_instance_read_dtos, created_by: str):
        self.insert_dtos(dtos.get_write_dtos(), created_by)
    def delete_logical_dtos(self, dtos: list[invoice_instance_write_dto], removed_by: str):
        uids = list(map(lambda dto: dto.get_uid(), dtos))
        return self.delete_logical_by_uids(uids, removed_by)
    def delete_logical_write_dtos(self, dtos: invoice_instance_write_dtos, removed_by: str):
        return self.delete_logical_dtos(dtos.dtos, removed_by)


class notification_instance_dao(base_dao):
    def __init__(self):
        print("Starting notification_instance DAO")
    def get_model(self) -> base_model:
        return notification_instance_model
    def get_items(self, sql: str) -> list[notification_instance_read_dto]:
        return list(map(lambda r: notification_instance_read_dto(*r), self.get_objects(sql)))
    def get_items_with_params(self, sql: str, params: Iterable) -> list[notification_instance_read_dto]:
        return list(map(lambda r: notification_instance_read_dto(*r), self.get_objects_by_params(sql, params)))
    def get_items_write(self, sql: str) -> list[notification_instance_write_dto]:
        return list(map(lambda r: notification_instance_write_dto(*r), self.get_objects(sql)))
    def get_items_write_with_params(self, sql: str, params: Iterable) -> list[notification_instance_write_dto]:
        return list(map(lambda r: notification_instance_write_dto(*r), self.get_objects_by_params(sql, params)))
    def get_items_all(self, n: int = 1000) -> notification_instance_read_dtos:
        return notification_instance_read_dtos(self.get_items(self.get_model().get_select_all_limit_sql(n)))
    def get_items_active(self, n: int = 1000) -> notification_instance_read_dtos:
        return notification_instance_read_dtos(self.get_items(self.get_model().get_select_active_limit_sql(n)))
    def get_items_all_latest(self, n: int = 1000) -> notification_instance_read_dtos:
        return notification_instance_read_dtos(self.get_items(self.get_model().get_select_all_latest_sql(n)))
    def get_items_active_latest(self, n: int = 1000) -> notification_instance_read_dtos:
        return notification_instance_read_dtos(self.get_items(self.get_model().get_select_active_latest_sql(n)))
    def get_items_write_all(self, n: int = 1000) -> notification_instance_write_dtos:
        return notification_instance_write_dtos(self.get_items_write(self.get_model().get_select_write_all_limit_sql(n)))
    def get_items_write_active(self, n: int = 1000) -> notification_instance_write_dtos:
        return notification_instance_write_dtos(self.get_items_write(self.get_model().get_select_write_active_limit_sql(n)))
    def get_items_write_all_latest(self, n: int = 1000) -> notification_instance_write_dtos:
        return notification_instance_write_dtos(self.get_items_write(self.get_model().get_select_write_all_latest_sql(n)))
    def get_items_write_active_latest(self, n: int = 1000) -> notification_instance_write_dtos:
        return notification_instance_write_dtos(self.get_items_write(self.get_model().get_select_write_active_latest_sql(n)))
    def get_item_by_uid(self, uid: str) -> notification_instance_read_dto | None:
        return notification_instance_read_dtos(self.get_items_with_params(self.get_model().get_select_by_key(), (uid,))).get_first()
    def get_item_by_id(self, id: int) -> notification_instance_read_dto | None:
        return notification_instance_read_dtos(self.get_items_with_params(self.get_model().get_select_by_id(), (id,))).get_first()
    def get_items_by_any_column(self, col_name: str, col_value: any, n: int = 1000) -> notification_instance_read_dtos:
        return notification_instance_read_dtos(self.get_items_with_params(self.get_model().get_select_active_by_any_column(col_name, n), (col_value,)))
    def get_uids(self, n: int = 1000) -> list[str]:
        return self.get_column_values_all(self.get_model().get_select_all_keys(n))
    def get_guids(self, n: int = 1000) -> list[str]:
        return self.get_column_values_all(self.get_model().get_select_all_guids(n))
    def count_all(self) -> int:
        return self.get_single_value_int_or_default(self.get_model().get_select_count_all_sql())
    def count_active(self) -> int:
        return self.get_single_value_int_or_default(self.get_model().get_select_count_active_sql())
    def count_by_any_column(self, col_name: str, col_value: any) -> int:
        return self.get_single_value_int_or_default_by_params(self.get_model().get_select_count_by_any_column_sql(col_name), (col_value,))
    def insert_dtos(self, dtos: list[notification_instance_write_dto], created_by: str):
        self.insert_many(dtos, created_by)
    def insert_write_dtos(self, dtos: notification_instance_write_dtos, created_by: str):
        self.insert_dtos(dtos.dtos, created_by)
    def insert_read_dtos(self, dtos: notification_instance_read_dtos, created_by: str):
        self.insert_dtos(dtos.get_write_dtos(), created_by)
    def delete_logical_dtos(self, dtos: list[notification_instance_write_dto], removed_by: str):
        uids = list(map(lambda dto: dto.get_uid(), dtos))
        return self.delete_logical_by_uids(uids, removed_by)
    def delete_logical_write_dtos(self, dtos: notification_instance_write_dtos, removed_by: str):
        return self.delete_logical_dtos(dtos.dtos, removed_by)


class project_budget_dao(base_dao):
    def __init__(self):
        print("Starting project_budget DAO")
    def get_model(self) -> base_model:
        return project_budget_model
    def get_items(self, sql: str) -> list[project_budget_read_dto]:
        return list(map(lambda r: project_budget_read_dto(*r), self.get_objects(sql)))
    def get_items_with_params(self, sql: str, params: Iterable) -> list[project_budget_read_dto]:
        return list(map(lambda r: project_budget_read_dto(*r), self.get_objects_by_params(sql, params)))
    def get_items_write(self, sql: str) -> list[project_budget_write_dto]:
        return list(map(lambda r: project_budget_write_dto(*r), self.get_objects(sql)))
    def get_items_write_with_params(self, sql: str, params: Iterable) -> list[project_budget_write_dto]:
        return list(map(lambda r: project_budget_write_dto(*r), self.get_objects_by_params(sql, params)))
    def get_items_all(self, n: int = 1000) -> project_budget_read_dtos:
        return project_budget_read_dtos(self.get_items(self.get_model().get_select_all_limit_sql(n)))
    def get_items_active(self, n: int = 1000) -> project_budget_read_dtos:
        return project_budget_read_dtos(self.get_items(self.get_model().get_select_active_limit_sql(n)))
    def get_items_all_latest(self, n: int = 1000) -> project_budget_read_dtos:
        return project_budget_read_dtos(self.get_items(self.get_model().get_select_all_latest_sql(n)))
    def get_items_active_latest(self, n: int = 1000) -> project_budget_read_dtos:
        return project_budget_read_dtos(self.get_items(self.get_model().get_select_active_latest_sql(n)))
    def get_items_write_all(self, n: int = 1000) -> project_budget_write_dtos:
        return project_budget_write_dtos(self.get_items_write(self.get_model().get_select_write_all_limit_sql(n)))
    def get_items_write_active(self, n: int = 1000) -> project_budget_write_dtos:
        return project_budget_write_dtos(self.get_items_write(self.get_model().get_select_write_active_limit_sql(n)))
    def get_items_write_all_latest(self, n: int = 1000) -> project_budget_write_dtos:
        return project_budget_write_dtos(self.get_items_write(self.get_model().get_select_write_all_latest_sql(n)))
    def get_items_write_active_latest(self, n: int = 1000) -> project_budget_write_dtos:
        return project_budget_write_dtos(self.get_items_write(self.get_model().get_select_write_active_latest_sql(n)))
    def get_item_by_uid(self, uid: str) -> project_budget_read_dto | None:
        return project_budget_read_dtos(self.get_items_with_params(self.get_model().get_select_by_key(), (uid,))).get_first()
    def get_item_by_id(self, id: int) -> project_budget_read_dto | None:
        return project_budget_read_dtos(self.get_items_with_params(self.get_model().get_select_by_id(), (id,))).get_first()
    def get_items_by_any_column(self, col_name: str, col_value: any, n: int = 1000) -> project_budget_read_dtos:
        return project_budget_read_dtos(self.get_items_with_params(self.get_model().get_select_active_by_any_column(col_name, n), (col_value,)))
    def get_uids(self, n: int = 1000) -> list[str]:
        return self.get_column_values_all(self.get_model().get_select_all_keys(n))
    def get_guids(self, n: int = 1000) -> list[str]:
        return self.get_column_values_all(self.get_model().get_select_all_guids(n))
    def count_all(self) -> int:
        return self.get_single_value_int_or_default(self.get_model().get_select_count_all_sql())
    def count_active(self) -> int:
        return self.get_single_value_int_or_default(self.get_model().get_select_count_active_sql())
    def count_by_any_column(self, col_name: str, col_value: any) -> int:
        return self.get_single_value_int_or_default_by_params(self.get_model().get_select_count_by_any_column_sql(col_name), (col_value,))
    def insert_dtos(self, dtos: list[project_budget_write_dto], created_by: str):
        self.insert_many(dtos, created_by)
    def insert_write_dtos(self, dtos: project_budget_write_dtos, created_by: str):
        self.insert_dtos(dtos.dtos, created_by)
    def insert_read_dtos(self, dtos: project_budget_read_dtos, created_by: str):
        self.insert_dtos(dtos.get_write_dtos(), created_by)
    def delete_logical_dtos(self, dtos: list[project_budget_write_dto], removed_by: str):
        uids = list(map(lambda dto: dto.get_uid(), dtos))
        return self.delete_logical_by_uids(uids, removed_by)
    def delete_logical_write_dtos(self, dtos: project_budget_write_dtos, removed_by: str):
        return self.delete_logical_dtos(dtos.dtos, removed_by)


class project_group_dao(base_dao):
    def __init__(self):
        print("Starting project_group DAO")
    def get_model(self) -> base_model:
        return project_group_model
    def get_items(self, sql: str) -> list[project_group_read_dto]:
        return list(map(lambda r: project_group_read_dto(*r), self.get_objects(sql)))
    def get_items_with_params(self, sql: str, params: Iterable) -> list[project_group_read_dto]:
        return list(map(lambda r: project_group_read_dto(*r), self.get_objects_by_params(sql, params)))
    def get_items_write(self, sql: str) -> list[project_group_write_dto]:
        return list(map(lambda r: project_group_write_dto(*r), self.get_objects(sql)))
    def get_items_write_with_params(self, sql: str, params: Iterable) -> list[project_group_write_dto]:
        return list(map(lambda r: project_group_write_dto(*r), self.get_objects_by_params(sql, params)))
    def get_items_all(self, n: int = 1000) -> project_group_read_dtos:
        return project_group_read_dtos(self.get_items(self.get_model().get_select_all_limit_sql(n)))
    def get_items_active(self, n: int = 1000) -> project_group_read_dtos:
        return project_group_read_dtos(self.get_items(self.get_model().get_select_active_limit_sql(n)))
    def get_items_all_latest(self, n: int = 1000) -> project_group_read_dtos:
        return project_group_read_dtos(self.get_items(self.get_model().get_select_all_latest_sql(n)))
    def get_items_active_latest(self, n: int = 1000) -> project_group_read_dtos:
        return project_group_read_dtos(self.get_items(self.get_model().get_select_active_latest_sql(n)))
    def get_items_write_all(self, n: int = 1000) -> project_group_write_dtos:
        return project_group_write_dtos(self.get_items_write(self.get_model().get_select_write_all_limit_sql(n)))
    def get_items_write_active(self, n: int = 1000) -> project_group_write_dtos:
        return project_group_write_dtos(self.get_items_write(self.get_model().get_select_write_active_limit_sql(n)))
    def get_items_write_all_latest(self, n: int = 1000) -> project_group_write_dtos:
        return project_group_write_dtos(self.get_items_write(self.get_model().get_select_write_all_latest_sql(n)))
    def get_items_write_active_latest(self, n: int = 1000) -> project_group_write_dtos:
        return project_group_write_dtos(self.get_items_write(self.get_model().get_select_write_active_latest_sql(n)))
    def get_item_by_uid(self, uid: str) -> project_group_read_dto | None:
        return project_group_read_dtos(self.get_items_with_params(self.get_model().get_select_by_key(), (uid,))).get_first()
    def get_item_by_id(self, id: int) -> project_group_read_dto | None:
        return project_group_read_dtos(self.get_items_with_params(self.get_model().get_select_by_id(), (id,))).get_first()
    def get_items_by_any_column(self, col_name: str, col_value: any, n: int = 1000) -> project_group_read_dtos:
        return project_group_read_dtos(self.get_items_with_params(self.get_model().get_select_active_by_any_column(col_name, n), (col_value,)))
    def get_uids(self, n: int = 1000) -> list[str]:
        return self.get_column_values_all(self.get_model().get_select_all_keys(n))
    def get_guids(self, n: int = 1000) -> list[str]:
        return self.get_column_values_all(self.get_model().get_select_all_guids(n))
    def count_all(self) -> int:
        return self.get_single_value_int_or_default(self.get_model().get_select_count_all_sql())
    def count_active(self) -> int:
        return self.get_single_value_int_or_default(self.get_model().get_select_count_active_sql())
    def count_by_any_column(self, col_name: str, col_value: any) -> int:
        return self.get_single_value_int_or_default_by_params(self.get_model().get_select_count_by_any_column_sql(col_name), (col_value,))
    def insert_dtos(self, dtos: list[project_group_write_dto], created_by: str):
        self.insert_many(dtos, created_by)
    def insert_write_dtos(self, dtos: project_group_write_dtos, created_by: str):
        self.insert_dtos(dtos.dtos, created_by)
    def insert_read_dtos(self, dtos: project_group_read_dtos, created_by: str):
        self.insert_dtos(dtos.get_write_dtos(), created_by)
    def delete_logical_dtos(self, dtos: list[project_group_write_dto], removed_by: str):
        uids = list(map(lambda dto: dto.get_uid(), dtos))
        return self.delete_logical_by_uids(uids, removed_by)
    def delete_logical_write_dtos(self, dtos: project_group_write_dtos, removed_by: str):
        return self.delete_logical_dtos(dtos.dtos, removed_by)


class project_instance_dao(base_dao):
    def __init__(self):
        print("Starting project_instance DAO")
    def get_model(self) -> base_model:
        return project_instance_model
    def get_items(self, sql: str) -> list[project_instance_read_dto]:
        return list(map(lambda r: project_instance_read_dto(*r), self.get_objects(sql)))
    def get_items_with_params(self, sql: str, params: Iterable) -> list[project_instance_read_dto]:
        return list(map(lambda r: project_instance_read_dto(*r), self.get_objects_by_params(sql, params)))
    def get_items_write(self, sql: str) -> list[project_instance_write_dto]:
        return list(map(lambda r: project_instance_write_dto(*r), self.get_objects(sql)))
    def get_items_write_with_params(self, sql: str, params: Iterable) -> list[project_instance_write_dto]:
        return list(map(lambda r: project_instance_write_dto(*r), self.get_objects_by_params(sql, params)))
    def get_items_all(self, n: int = 1000) -> project_instance_read_dtos:
        return project_instance_read_dtos(self.get_items(self.get_model().get_select_all_limit_sql(n)))
    def get_items_active(self, n: int = 1000) -> project_instance_read_dtos:
        return project_instance_read_dtos(self.get_items(self.get_model().get_select_active_limit_sql(n)))
    def get_items_all_latest(self, n: int = 1000) -> project_instance_read_dtos:
        return project_instance_read_dtos(self.get_items(self.get_model().get_select_all_latest_sql(n)))
    def get_items_active_latest(self, n: int = 1000) -> project_instance_read_dtos:
        return project_instance_read_dtos(self.get_items(self.get_model().get_select_active_latest_sql(n)))
    def get_items_write_all(self, n: int = 1000) -> project_instance_write_dtos:
        return project_instance_write_dtos(self.get_items_write(self.get_model().get_select_write_all_limit_sql(n)))
    def get_items_write_active(self, n: int = 1000) -> project_instance_write_dtos:
        return project_instance_write_dtos(self.get_items_write(self.get_model().get_select_write_active_limit_sql(n)))
    def get_items_write_all_latest(self, n: int = 1000) -> project_instance_write_dtos:
        return project_instance_write_dtos(self.get_items_write(self.get_model().get_select_write_all_latest_sql(n)))
    def get_items_write_active_latest(self, n: int = 1000) -> project_instance_write_dtos:
        return project_instance_write_dtos(self.get_items_write(self.get_model().get_select_write_active_latest_sql(n)))
    def get_item_by_uid(self, uid: str) -> project_instance_read_dto | None:
        return project_instance_read_dtos(self.get_items_with_params(self.get_model().get_select_by_key(), (uid,))).get_first()
    def get_item_by_id(self, id: int) -> project_instance_read_dto | None:
        return project_instance_read_dtos(self.get_items_with_params(self.get_model().get_select_by_id(), (id,))).get_first()
    def get_items_by_any_column(self, col_name: str, col_value: any, n: int = 1000) -> project_instance_read_dtos:
        return project_instance_read_dtos(self.get_items_with_params(self.get_model().get_select_active_by_any_column(col_name, n), (col_value,)))
    def get_uids(self, n: int = 1000) -> list[str]:
        return self.get_column_values_all(self.get_model().get_select_all_keys(n))
    def get_guids(self, n: int = 1000) -> list[str]:
        return self.get_column_values_all(self.get_model().get_select_all_guids(n))
    def count_all(self) -> int:
        return self.get_single_value_int_or_default(self.get_model().get_select_count_all_sql())
    def count_active(self) -> int:
        return self.get_single_value_int_or_default(self.get_model().get_select_count_active_sql())
    def count_by_any_column(self, col_name: str, col_value: any) -> int:
        return self.get_single_value_int_or_default_by_params(self.get_model().get_select_count_by_any_column_sql(col_name), (col_value,))
    def insert_dtos(self, dtos: list[project_instance_write_dto], created_by: str):
        self.insert_many(dtos, created_by)
    def insert_write_dtos(self, dtos: project_instance_write_dtos, created_by: str):
        self.insert_dtos(dtos.dtos, created_by)
    def insert_read_dtos(self, dtos: project_instance_read_dtos, created_by: str):
        self.insert_dtos(dtos.get_write_dtos(), created_by)
    def delete_logical_dtos(self, dtos: list[project_instance_write_dto], removed_by: str):
        uids = list(map(lambda dto: dto.get_uid(), dtos))
        return self.delete_logical_by_uids(uids, removed_by)
    def delete_logical_write_dtos(self, dtos: project_instance_write_dtos, removed_by: str):
        return self.delete_logical_dtos(dtos.dtos, removed_by)


class project_milestone_dao(base_dao):
    def __init__(self):
        print("Starting project_milestone DAO")
    def get_model(self) -> base_model:
        return project_milestone_model
    def get_items(self, sql: str) -> list[project_milestone_read_dto]:
        return list(map(lambda r: project_milestone_read_dto(*r), self.get_objects(sql)))
    def get_items_with_params(self, sql: str, params: Iterable) -> list[project_milestone_read_dto]:
        return list(map(lambda r: project_milestone_read_dto(*r), self.get_objects_by_params(sql, params)))
    def get_items_write(self, sql: str) -> list[project_milestone_write_dto]:
        return list(map(lambda r: project_milestone_write_dto(*r), self.get_objects(sql)))
    def get_items_write_with_params(self, sql: str, params: Iterable) -> list[project_milestone_write_dto]:
        return list(map(lambda r: project_milestone_write_dto(*r), self.get_objects_by_params(sql, params)))
    def get_items_all(self, n: int = 1000) -> project_milestone_read_dtos:
        return project_milestone_read_dtos(self.get_items(self.get_model().get_select_all_limit_sql(n)))
    def get_items_active(self, n: int = 1000) -> project_milestone_read_dtos:
        return project_milestone_read_dtos(self.get_items(self.get_model().get_select_active_limit_sql(n)))
    def get_items_all_latest(self, n: int = 1000) -> project_milestone_read_dtos:
        return project_milestone_read_dtos(self.get_items(self.get_model().get_select_all_latest_sql(n)))
    def get_items_active_latest(self, n: int = 1000) -> project_milestone_read_dtos:
        return project_milestone_read_dtos(self.get_items(self.get_model().get_select_active_latest_sql(n)))
    def get_items_write_all(self, n: int = 1000) -> project_milestone_write_dtos:
        return project_milestone_write_dtos(self.get_items_write(self.get_model().get_select_write_all_limit_sql(n)))
    def get_items_write_active(self, n: int = 1000) -> project_milestone_write_dtos:
        return project_milestone_write_dtos(self.get_items_write(self.get_model().get_select_write_active_limit_sql(n)))
    def get_items_write_all_latest(self, n: int = 1000) -> project_milestone_write_dtos:
        return project_milestone_write_dtos(self.get_items_write(self.get_model().get_select_write_all_latest_sql(n)))
    def get_items_write_active_latest(self, n: int = 1000) -> project_milestone_write_dtos:
        return project_milestone_write_dtos(self.get_items_write(self.get_model().get_select_write_active_latest_sql(n)))
    def get_item_by_uid(self, uid: str) -> project_milestone_read_dto | None:
        return project_milestone_read_dtos(self.get_items_with_params(self.get_model().get_select_by_key(), (uid,))).get_first()
    def get_item_by_id(self, id: int) -> project_milestone_read_dto | None:
        return project_milestone_read_dtos(self.get_items_with_params(self.get_model().get_select_by_id(), (id,))).get_first()
    def get_items_by_any_column(self, col_name: str, col_value: any, n: int = 1000) -> project_milestone_read_dtos:
        return project_milestone_read_dtos(self.get_items_with_params(self.get_model().get_select_active_by_any_column(col_name, n), (col_value,)))
    def get_uids(self, n: int = 1000) -> list[str]:
        return self.get_column_values_all(self.get_model().get_select_all_keys(n))
    def get_guids(self, n: int = 1000) -> list[str]:
        return self.get_column_values_all(self.get_model().get_select_all_guids(n))
    def count_all(self) -> int:
        return self.get_single_value_int_or_default(self.get_model().get_select_count_all_sql())
    def count_active(self) -> int:
        return self.get_single_value_int_or_default(self.get_model().get_select_count_active_sql())
    def count_by_any_column(self, col_name: str, col_value: any) -> int:
        return self.get_single_value_int_or_default_by_params(self.get_model().get_select_count_by_any_column_sql(col_name), (col_value,))
    def insert_dtos(self, dtos: list[project_milestone_write_dto], created_by: str):
        self.insert_many(dtos, created_by)
    def insert_write_dtos(self, dtos: project_milestone_write_dtos, created_by: str):
        self.insert_dtos(dtos.dtos, created_by)
    def insert_read_dtos(self, dtos: project_milestone_read_dtos, created_by: str):
        self.insert_dtos(dtos.get_write_dtos(), created_by)
    def delete_logical_dtos(self, dtos: list[project_milestone_write_dto], removed_by: str):
        uids = list(map(lambda dto: dto.get_uid(), dtos))
        return self.delete_logical_by_uids(uids, removed_by)
    def delete_logical_write_dtos(self, dtos: project_milestone_write_dtos, removed_by: str):
        return self.delete_logical_dtos(dtos.dtos, removed_by)


class system_attribute_dao(base_dao):
    def __init__(self):
        print("Starting system_attribute DAO")
    def get_model(self) -> base_model:
        return system_attribute_model
    def get_items(self, sql: str) -> list[system_attribute_read_dto]:
        return list(map(lambda r: system_attribute_read_dto(*r), self.get_objects(sql)))
    def get_items_with_params(self, sql: str, params: Iterable) -> list[system_attribute_read_dto]:
        return list(map(lambda r: system_attribute_read_dto(*r), self.get_objects_by_params(sql, params)))
    def get_items_write(self, sql: str) -> list[system_attribute_write_dto]:
        return list(map(lambda r: system_attribute_write_dto(*r), self.get_objects(sql)))
    def get_items_write_with_params(self, sql: str, params: Iterable) -> list[system_attribute_write_dto]:
        return list(map(lambda r: system_attribute_write_dto(*r), self.get_objects_by_params(sql, params)))
    def get_items_all(self, n: int = 1000) -> system_attribute_read_dtos:
        return system_attribute_read_dtos(self.get_items(self.get_model().get_select_all_limit_sql(n)))
    def get_items_active(self, n: int = 1000) -> system_attribute_read_dtos:
        return system_attribute_read_dtos(self.get_items(self.get_model().get_select_active_limit_sql(n)))
    def get_items_all_latest(self, n: int = 1000) -> system_attribute_read_dtos:
        return system_attribute_read_dtos(self.get_items(self.get_model().get_select_all_latest_sql(n)))
    def get_items_active_latest(self, n: int = 1000) -> system_attribute_read_dtos:
        return system_attribute_read_dtos(self.get_items(self.get_model().get_select_active_latest_sql(n)))
    def get_items_write_all(self, n: int = 1000) -> system_attribute_write_dtos:
        return system_attribute_write_dtos(self.get_items_write(self.get_model().get_select_write_all_limit_sql(n)))
    def get_items_write_active(self, n: int = 1000) -> system_attribute_write_dtos:
        return system_attribute_write_dtos(self.get_items_write(self.get_model().get_select_write_active_limit_sql(n)))
    def get_items_write_all_latest(self, n: int = 1000) -> system_attribute_write_dtos:
        return system_attribute_write_dtos(self.get_items_write(self.get_model().get_select_write_all_latest_sql(n)))
    def get_items_write_active_latest(self, n: int = 1000) -> system_attribute_write_dtos:
        return system_attribute_write_dtos(self.get_items_write(self.get_model().get_select_write_active_latest_sql(n)))
    def get_item_by_uid(self, uid: str) -> system_attribute_read_dto | None:
        return system_attribute_read_dtos(self.get_items_with_params(self.get_model().get_select_by_key(), (uid,))).get_first()
    def get_item_by_id(self, id: int) -> system_attribute_read_dto | None:
        return system_attribute_read_dtos(self.get_items_with_params(self.get_model().get_select_by_id(), (id,))).get_first()
    def get_items_by_any_column(self, col_name: str, col_value: any, n: int = 1000) -> system_attribute_read_dtos:
        return system_attribute_read_dtos(self.get_items_with_params(self.get_model().get_select_active_by_any_column(col_name, n), (col_value,)))
    def get_uids(self, n: int = 1000) -> list[str]:
        return self.get_column_values_all(self.get_model().get_select_all_keys(n))
    def get_guids(self, n: int = 1000) -> list[str]:
        return self.get_column_values_all(self.get_model().get_select_all_guids(n))
    def count_all(self) -> int:
        return self.get_single_value_int_or_default(self.get_model().get_select_count_all_sql())
    def count_active(self) -> int:
        return self.get_single_value_int_or_default(self.get_model().get_select_count_active_sql())
    def count_by_any_column(self, col_name: str, col_value: any) -> int:
        return self.get_single_value_int_or_default_by_params(self.get_model().get_select_count_by_any_column_sql(col_name), (col_value,))
    def insert_dtos(self, dtos: list[system_attribute_write_dto], created_by: str):
        self.insert_many(dtos, created_by)
    def insert_write_dtos(self, dtos: system_attribute_write_dtos, created_by: str):
        self.insert_dtos(dtos.dtos, created_by)
    def insert_read_dtos(self, dtos: system_attribute_read_dtos, created_by: str):
        self.insert_dtos(dtos.get_write_dtos(), created_by)
    def delete_logical_dtos(self, dtos: list[system_attribute_write_dto], removed_by: str):
        uids = list(map(lambda dto: dto.get_uid(), dtos))
        return self.delete_logical_by_uids(uids, removed_by)
    def delete_logical_write_dtos(self, dtos: system_attribute_write_dtos, removed_by: str):
        return self.delete_logical_dtos(dtos.dtos, removed_by)


class system_change_dao(base_dao):
    def __init__(self):
        print("Starting system_change DAO")
    def get_model(self) -> base_model:
        return system_change_model
    def get_items(self, sql: str) -> list[system_change_read_dto]:
        return list(map(lambda r: system_change_read_dto(*r), self.get_objects(sql)))
    def get_items_with_params(self, sql: str, params: Iterable) -> list[system_change_read_dto]:
        return list(map(lambda r: system_change_read_dto(*r), self.get_objects_by_params(sql, params)))
    def get_items_write(self, sql: str) -> list[system_change_write_dto]:
        return list(map(lambda r: system_change_write_dto(*r), self.get_objects(sql)))
    def get_items_write_with_params(self, sql: str, params: Iterable) -> list[system_change_write_dto]:
        return list(map(lambda r: system_change_write_dto(*r), self.get_objects_by_params(sql, params)))
    def get_items_all(self, n: int = 1000) -> system_change_read_dtos:
        return system_change_read_dtos(self.get_items(self.get_model().get_select_all_limit_sql(n)))
    def get_items_active(self, n: int = 1000) -> system_change_read_dtos:
        return system_change_read_dtos(self.get_items(self.get_model().get_select_active_limit_sql(n)))
    def get_items_all_latest(self, n: int = 1000) -> system_change_read_dtos:
        return system_change_read_dtos(self.get_items(self.get_model().get_select_all_latest_sql(n)))
    def get_items_active_latest(self, n: int = 1000) -> system_change_read_dtos:
        return system_change_read_dtos(self.get_items(self.get_model().get_select_active_latest_sql(n)))
    def get_items_write_all(self, n: int = 1000) -> system_change_write_dtos:
        return system_change_write_dtos(self.get_items_write(self.get_model().get_select_write_all_limit_sql(n)))
    def get_items_write_active(self, n: int = 1000) -> system_change_write_dtos:
        return system_change_write_dtos(self.get_items_write(self.get_model().get_select_write_active_limit_sql(n)))
    def get_items_write_all_latest(self, n: int = 1000) -> system_change_write_dtos:
        return system_change_write_dtos(self.get_items_write(self.get_model().get_select_write_all_latest_sql(n)))
    def get_items_write_active_latest(self, n: int = 1000) -> system_change_write_dtos:
        return system_change_write_dtos(self.get_items_write(self.get_model().get_select_write_active_latest_sql(n)))
    def get_item_by_uid(self, uid: str) -> system_change_read_dto | None:
        return system_change_read_dtos(self.get_items_with_params(self.get_model().get_select_by_key(), (uid,))).get_first()
    def get_item_by_id(self, id: int) -> system_change_read_dto | None:
        return system_change_read_dtos(self.get_items_with_params(self.get_model().get_select_by_id(), (id,))).get_first()
    def get_items_by_any_column(self, col_name: str, col_value: any, n: int = 1000) -> system_change_read_dtos:
        return system_change_read_dtos(self.get_items_with_params(self.get_model().get_select_active_by_any_column(col_name, n), (col_value,)))
    def get_uids(self, n: int = 1000) -> list[str]:
        return self.get_column_values_all(self.get_model().get_select_all_keys(n))
    def get_guids(self, n: int = 1000) -> list[str]:
        return self.get_column_values_all(self.get_model().get_select_all_guids(n))
    def count_all(self) -> int:
        return self.get_single_value_int_or_default(self.get_model().get_select_count_all_sql())
    def count_active(self) -> int:
        return self.get_single_value_int_or_default(self.get_model().get_select_count_active_sql())
    def count_by_any_column(self, col_name: str, col_value: any) -> int:
        return self.get_single_value_int_or_default_by_params(self.get_model().get_select_count_by_any_column_sql(col_name), (col_value,))
    def insert_dtos(self, dtos: list[system_change_write_dto], created_by: str):
        self.insert_many(dtos, created_by)
    def insert_write_dtos(self, dtos: system_change_write_dtos, created_by: str):
        self.insert_dtos(dtos.dtos, created_by)
    def insert_read_dtos(self, dtos: system_change_read_dtos, created_by: str):
        self.insert_dtos(dtos.get_write_dtos(), created_by)
    def delete_logical_dtos(self, dtos: list[system_change_write_dto], removed_by: str):
        uids = list(map(lambda dto: dto.get_uid(), dtos))
        return self.delete_logical_by_uids(uids, removed_by)
    def delete_logical_write_dtos(self, dtos: system_change_write_dtos, removed_by: str):
        return self.delete_logical_dtos(dtos.dtos, removed_by)


class system_exception_dao(base_dao):
    def __init__(self):
        print("Starting system_exception DAO")
    def get_model(self) -> base_model:
        return system_exception_model
    def get_items(self, sql: str) -> list[system_exception_read_dto]:
        return list(map(lambda r: system_exception_read_dto(*r), self.get_objects(sql)))
    def get_items_with_params(self, sql: str, params: Iterable) -> list[system_exception_read_dto]:
        return list(map(lambda r: system_exception_read_dto(*r), self.get_objects_by_params(sql, params)))
    def get_items_write(self, sql: str) -> list[system_exception_write_dto]:
        return list(map(lambda r: system_exception_write_dto(*r), self.get_objects(sql)))
    def get_items_write_with_params(self, sql: str, params: Iterable) -> list[system_exception_write_dto]:
        return list(map(lambda r: system_exception_write_dto(*r), self.get_objects_by_params(sql, params)))
    def get_items_all(self, n: int = 1000) -> system_exception_read_dtos:
        return system_exception_read_dtos(self.get_items(self.get_model().get_select_all_limit_sql(n)))
    def get_items_active(self, n: int = 1000) -> system_exception_read_dtos:
        return system_exception_read_dtos(self.get_items(self.get_model().get_select_active_limit_sql(n)))
    def get_items_all_latest(self, n: int = 1000) -> system_exception_read_dtos:
        return system_exception_read_dtos(self.get_items(self.get_model().get_select_all_latest_sql(n)))
    def get_items_active_latest(self, n: int = 1000) -> system_exception_read_dtos:
        return system_exception_read_dtos(self.get_items(self.get_model().get_select_active_latest_sql(n)))
    def get_items_write_all(self, n: int = 1000) -> system_exception_write_dtos:
        return system_exception_write_dtos(self.get_items_write(self.get_model().get_select_write_all_limit_sql(n)))
    def get_items_write_active(self, n: int = 1000) -> system_exception_write_dtos:
        return system_exception_write_dtos(self.get_items_write(self.get_model().get_select_write_active_limit_sql(n)))
    def get_items_write_all_latest(self, n: int = 1000) -> system_exception_write_dtos:
        return system_exception_write_dtos(self.get_items_write(self.get_model().get_select_write_all_latest_sql(n)))
    def get_items_write_active_latest(self, n: int = 1000) -> system_exception_write_dtos:
        return system_exception_write_dtos(self.get_items_write(self.get_model().get_select_write_active_latest_sql(n)))
    def get_item_by_uid(self, uid: str) -> system_exception_read_dto | None:
        return system_exception_read_dtos(self.get_items_with_params(self.get_model().get_select_by_key(), (uid,))).get_first()
    def get_item_by_id(self, id: int) -> system_exception_read_dto | None:
        return system_exception_read_dtos(self.get_items_with_params(self.get_model().get_select_by_id(), (id,))).get_first()
    def get_items_by_any_column(self, col_name: str, col_value: any, n: int = 1000) -> system_exception_read_dtos:
        return system_exception_read_dtos(self.get_items_with_params(self.get_model().get_select_active_by_any_column(col_name, n), (col_value,)))
    def get_uids(self, n: int = 1000) -> list[str]:
        return self.get_column_values_all(self.get_model().get_select_all_keys(n))
    def get_guids(self, n: int = 1000) -> list[str]:
        return self.get_column_values_all(self.get_model().get_select_all_guids(n))
    def count_all(self) -> int:
        return self.get_single_value_int_or_default(self.get_model().get_select_count_all_sql())
    def count_active(self) -> int:
        return self.get_single_value_int_or_default(self.get_model().get_select_count_active_sql())
    def count_by_any_column(self, col_name: str, col_value: any) -> int:
        return self.get_single_value_int_or_default_by_params(self.get_model().get_select_count_by_any_column_sql(col_name), (col_value,))
    def insert_dtos(self, dtos: list[system_exception_write_dto], created_by: str):
        self.insert_many(dtos, created_by)
    def insert_write_dtos(self, dtos: system_exception_write_dtos, created_by: str):
        self.insert_dtos(dtos.dtos, created_by)
    def insert_read_dtos(self, dtos: system_exception_read_dtos, created_by: str):
        self.insert_dtos(dtos.get_write_dtos(), created_by)
    def delete_logical_dtos(self, dtos: list[system_exception_write_dto], removed_by: str):
        uids = list(map(lambda dto: dto.get_uid(), dtos))
        return self.delete_logical_by_uids(uids, removed_by)
    def delete_logical_write_dtos(self, dtos: system_exception_write_dtos, removed_by: str):
        return self.delete_logical_dtos(dtos.dtos, removed_by)


class system_instance_dao(base_dao):
    def __init__(self):
        print("Starting system_instance DAO")
    def get_model(self) -> base_model:
        return system_instance_model
    def get_items(self, sql: str) -> list[system_instance_read_dto]:
        return list(map(lambda r: system_instance_read_dto(*r), self.get_objects(sql)))
    def get_items_with_params(self, sql: str, params: Iterable) -> list[system_instance_read_dto]:
        return list(map(lambda r: system_instance_read_dto(*r), self.get_objects_by_params(sql, params)))
    def get_items_write(self, sql: str) -> list[system_instance_write_dto]:
        return list(map(lambda r: system_instance_write_dto(*r), self.get_objects(sql)))
    def get_items_write_with_params(self, sql: str, params: Iterable) -> list[system_instance_write_dto]:
        return list(map(lambda r: system_instance_write_dto(*r), self.get_objects_by_params(sql, params)))
    def get_items_all(self, n: int = 1000) -> system_instance_read_dtos:
        return system_instance_read_dtos(self.get_items(self.get_model().get_select_all_limit_sql(n)))
    def get_items_active(self, n: int = 1000) -> system_instance_read_dtos:
        return system_instance_read_dtos(self.get_items(self.get_model().get_select_active_limit_sql(n)))
    def get_items_all_latest(self, n: int = 1000) -> system_instance_read_dtos:
        return system_instance_read_dtos(self.get_items(self.get_model().get_select_all_latest_sql(n)))
    def get_items_active_latest(self, n: int = 1000) -> system_instance_read_dtos:
        return system_instance_read_dtos(self.get_items(self.get_model().get_select_active_latest_sql(n)))
    def get_items_write_all(self, n: int = 1000) -> system_instance_write_dtos:
        return system_instance_write_dtos(self.get_items_write(self.get_model().get_select_write_all_limit_sql(n)))
    def get_items_write_active(self, n: int = 1000) -> system_instance_write_dtos:
        return system_instance_write_dtos(self.get_items_write(self.get_model().get_select_write_active_limit_sql(n)))
    def get_items_write_all_latest(self, n: int = 1000) -> system_instance_write_dtos:
        return system_instance_write_dtos(self.get_items_write(self.get_model().get_select_write_all_latest_sql(n)))
    def get_items_write_active_latest(self, n: int = 1000) -> system_instance_write_dtos:
        return system_instance_write_dtos(self.get_items_write(self.get_model().get_select_write_active_latest_sql(n)))
    def get_item_by_uid(self, uid: str) -> system_instance_read_dto | None:
        return system_instance_read_dtos(self.get_items_with_params(self.get_model().get_select_by_key(), (uid,))).get_first()
    def get_item_by_id(self, id: int) -> system_instance_read_dto | None:
        return system_instance_read_dtos(self.get_items_with_params(self.get_model().get_select_by_id(), (id,))).get_first()
    def get_items_by_any_column(self, col_name: str, col_value: any, n: int = 1000) -> system_instance_read_dtos:
        return system_instance_read_dtos(self.get_items_with_params(self.get_model().get_select_active_by_any_column(col_name, n), (col_value,)))
    def get_uids(self, n: int = 1000) -> list[str]:
        return self.get_column_values_all(self.get_model().get_select_all_keys(n))
    def get_guids(self, n: int = 1000) -> list[str]:
        return self.get_column_values_all(self.get_model().get_select_all_guids(n))
    def count_all(self) -> int:
        return self.get_single_value_int_or_default(self.get_model().get_select_count_all_sql())
    def count_active(self) -> int:
        return self.get_single_value_int_or_default(self.get_model().get_select_count_active_sql())
    def count_by_any_column(self, col_name: str, col_value: any) -> int:
        return self.get_single_value_int_or_default_by_params(self.get_model().get_select_count_by_any_column_sql(col_name), (col_value,))
    def insert_dtos(self, dtos: list[system_instance_write_dto], created_by: str):
        self.insert_many(dtos, created_by)
    def insert_write_dtos(self, dtos: system_instance_write_dtos, created_by: str):
        self.insert_dtos(dtos.dtos, created_by)
    def insert_read_dtos(self, dtos: system_instance_read_dtos, created_by: str):
        self.insert_dtos(dtos.get_write_dtos(), created_by)
    def delete_logical_dtos(self, dtos: list[system_instance_write_dto], removed_by: str):
        uids = list(map(lambda dto: dto.get_uid(), dtos))
        return self.delete_logical_by_uids(uids, removed_by)
    def delete_logical_write_dtos(self, dtos: system_instance_write_dtos, removed_by: str):
        return self.delete_logical_dtos(dtos.dtos, removed_by)


class system_object_dao(base_dao):
    def __init__(self):
        print("Starting system_object DAO")
    def get_model(self) -> base_model:
        return system_object_model
    def get_items(self, sql: str) -> list[system_object_read_dto]:
        return list(map(lambda r: system_object_read_dto(*r), self.get_objects(sql)))
    def get_items_with_params(self, sql: str, params: Iterable) -> list[system_object_read_dto]:
        return list(map(lambda r: system_object_read_dto(*r), self.get_objects_by_params(sql, params)))
    def get_items_write(self, sql: str) -> list[system_object_write_dto]:
        return list(map(lambda r: system_object_write_dto(*r), self.get_objects(sql)))
    def get_items_write_with_params(self, sql: str, params: Iterable) -> list[system_object_write_dto]:
        return list(map(lambda r: system_object_write_dto(*r), self.get_objects_by_params(sql, params)))
    def get_items_all(self, n: int = 1000) -> system_object_read_dtos:
        return system_object_read_dtos(self.get_items(self.get_model().get_select_all_limit_sql(n)))
    def get_items_active(self, n: int = 1000) -> system_object_read_dtos:
        return system_object_read_dtos(self.get_items(self.get_model().get_select_active_limit_sql(n)))
    def get_items_all_latest(self, n: int = 1000) -> system_object_read_dtos:
        return system_object_read_dtos(self.get_items(self.get_model().get_select_all_latest_sql(n)))
    def get_items_active_latest(self, n: int = 1000) -> system_object_read_dtos:
        return system_object_read_dtos(self.get_items(self.get_model().get_select_active_latest_sql(n)))
    def get_items_write_all(self, n: int = 1000) -> system_object_write_dtos:
        return system_object_write_dtos(self.get_items_write(self.get_model().get_select_write_all_limit_sql(n)))
    def get_items_write_active(self, n: int = 1000) -> system_object_write_dtos:
        return system_object_write_dtos(self.get_items_write(self.get_model().get_select_write_active_limit_sql(n)))
    def get_items_write_all_latest(self, n: int = 1000) -> system_object_write_dtos:
        return system_object_write_dtos(self.get_items_write(self.get_model().get_select_write_all_latest_sql(n)))
    def get_items_write_active_latest(self, n: int = 1000) -> system_object_write_dtos:
        return system_object_write_dtos(self.get_items_write(self.get_model().get_select_write_active_latest_sql(n)))
    def get_item_by_uid(self, uid: str) -> system_object_read_dto | None:
        return system_object_read_dtos(self.get_items_with_params(self.get_model().get_select_by_key(), (uid,))).get_first()
    def get_item_by_id(self, id: int) -> system_object_read_dto | None:
        return system_object_read_dtos(self.get_items_with_params(self.get_model().get_select_by_id(), (id,))).get_first()
    def get_items_by_any_column(self, col_name: str, col_value: any, n: int = 1000) -> system_object_read_dtos:
        return system_object_read_dtos(self.get_items_with_params(self.get_model().get_select_active_by_any_column(col_name, n), (col_value,)))
    def get_uids(self, n: int = 1000) -> list[str]:
        return self.get_column_values_all(self.get_model().get_select_all_keys(n))
    def get_guids(self, n: int = 1000) -> list[str]:
        return self.get_column_values_all(self.get_model().get_select_all_guids(n))
    def count_all(self) -> int:
        return self.get_single_value_int_or_default(self.get_model().get_select_count_all_sql())
    def count_active(self) -> int:
        return self.get_single_value_int_or_default(self.get_model().get_select_count_active_sql())
    def count_by_any_column(self, col_name: str, col_value: any) -> int:
        return self.get_single_value_int_or_default_by_params(self.get_model().get_select_count_by_any_column_sql(col_name), (col_value,))
    def insert_dtos(self, dtos: list[system_object_write_dto], created_by: str):
        self.insert_many(dtos, created_by)
    def insert_write_dtos(self, dtos: system_object_write_dtos, created_by: str):
        self.insert_dtos(dtos.dtos, created_by)
    def insert_read_dtos(self, dtos: system_object_read_dtos, created_by: str):
        self.insert_dtos(dtos.get_write_dtos(), created_by)
    def delete_logical_dtos(self, dtos: list[system_object_write_dto], removed_by: str):
        uids = list(map(lambda dto: dto.get_uid(), dtos))
        return self.delete_logical_by_uids(uids, removed_by)
    def delete_logical_write_dtos(self, dtos: system_object_write_dtos, removed_by: str):
        return self.delete_logical_dtos(dtos.dtos, removed_by)


class system_setting_dao(base_dao):
    def __init__(self):
        print("Starting system_setting DAO")
    def get_model(self) -> base_model:
        return system_setting_model
    def get_items(self, sql: str) -> list[system_setting_read_dto]:
        return list(map(lambda r: system_setting_read_dto(*r), self.get_objects(sql)))
    def get_items_with_params(self, sql: str, params: Iterable) -> list[system_setting_read_dto]:
        return list(map(lambda r: system_setting_read_dto(*r), self.get_objects_by_params(sql, params)))
    def get_items_write(self, sql: str) -> list[system_setting_write_dto]:
        return list(map(lambda r: system_setting_write_dto(*r), self.get_objects(sql)))
    def get_items_write_with_params(self, sql: str, params: Iterable) -> list[system_setting_write_dto]:
        return list(map(lambda r: system_setting_write_dto(*r), self.get_objects_by_params(sql, params)))
    def get_items_all(self, n: int = 1000) -> system_setting_read_dtos:
        return system_setting_read_dtos(self.get_items(self.get_model().get_select_all_limit_sql(n)))
    def get_items_active(self, n: int = 1000) -> system_setting_read_dtos:
        return system_setting_read_dtos(self.get_items(self.get_model().get_select_active_limit_sql(n)))
    def get_items_all_latest(self, n: int = 1000) -> system_setting_read_dtos:
        return system_setting_read_dtos(self.get_items(self.get_model().get_select_all_latest_sql(n)))
    def get_items_active_latest(self, n: int = 1000) -> system_setting_read_dtos:
        return system_setting_read_dtos(self.get_items(self.get_model().get_select_active_latest_sql(n)))
    def get_items_write_all(self, n: int = 1000) -> system_setting_write_dtos:
        return system_setting_write_dtos(self.get_items_write(self.get_model().get_select_write_all_limit_sql(n)))
    def get_items_write_active(self, n: int = 1000) -> system_setting_write_dtos:
        return system_setting_write_dtos(self.get_items_write(self.get_model().get_select_write_active_limit_sql(n)))
    def get_items_write_all_latest(self, n: int = 1000) -> system_setting_write_dtos:
        return system_setting_write_dtos(self.get_items_write(self.get_model().get_select_write_all_latest_sql(n)))
    def get_items_write_active_latest(self, n: int = 1000) -> system_setting_write_dtos:
        return system_setting_write_dtos(self.get_items_write(self.get_model().get_select_write_active_latest_sql(n)))
    def get_item_by_uid(self, uid: str) -> system_setting_read_dto | None:
        return system_setting_read_dtos(self.get_items_with_params(self.get_model().get_select_by_key(), (uid,))).get_first()
    def get_item_by_id(self, id: int) -> system_setting_read_dto | None:
        return system_setting_read_dtos(self.get_items_with_params(self.get_model().get_select_by_id(), (id,))).get_first()
    def get_items_by_any_column(self, col_name: str, col_value: any, n: int = 1000) -> system_setting_read_dtos:
        return system_setting_read_dtos(self.get_items_with_params(self.get_model().get_select_active_by_any_column(col_name, n), (col_value,)))
    def get_uids(self, n: int = 1000) -> list[str]:
        return self.get_column_values_all(self.get_model().get_select_all_keys(n))
    def get_guids(self, n: int = 1000) -> list[str]:
        return self.get_column_values_all(self.get_model().get_select_all_guids(n))
    def count_all(self) -> int:
        return self.get_single_value_int_or_default(self.get_model().get_select_count_all_sql())
    def count_active(self) -> int:
        return self.get_single_value_int_or_default(self.get_model().get_select_count_active_sql())
    def count_by_any_column(self, col_name: str, col_value: any) -> int:
        return self.get_single_value_int_or_default_by_params(self.get_model().get_select_count_by_any_column_sql(col_name), (col_value,))
    def insert_dtos(self, dtos: list[system_setting_write_dto], created_by: str):
        self.insert_many(dtos, created_by)
    def insert_write_dtos(self, dtos: system_setting_write_dtos, created_by: str):
        self.insert_dtos(dtos.dtos, created_by)
    def insert_read_dtos(self, dtos: system_setting_read_dtos, created_by: str):
        self.insert_dtos(dtos.get_write_dtos(), created_by)
    def delete_logical_dtos(self, dtos: list[system_setting_write_dto], removed_by: str):
        uids = list(map(lambda dto: dto.get_uid(), dtos))
        return self.delete_logical_by_uids(uids, removed_by)
    def delete_logical_write_dtos(self, dtos: system_setting_write_dtos, removed_by: str):
        return self.delete_logical_dtos(dtos.dtos, removed_by)


class system_state_dao(base_dao):
    def __init__(self):
        print("Starting system_state DAO")
    def get_model(self) -> base_model:
        return system_state_model
    def get_items(self, sql: str) -> list[system_state_read_dto]:
        return list(map(lambda r: system_state_read_dto(*r), self.get_objects(sql)))
    def get_items_with_params(self, sql: str, params: Iterable) -> list[system_state_read_dto]:
        return list(map(lambda r: system_state_read_dto(*r), self.get_objects_by_params(sql, params)))
    def get_items_write(self, sql: str) -> list[system_state_write_dto]:
        return list(map(lambda r: system_state_write_dto(*r), self.get_objects(sql)))
    def get_items_write_with_params(self, sql: str, params: Iterable) -> list[system_state_write_dto]:
        return list(map(lambda r: system_state_write_dto(*r), self.get_objects_by_params(sql, params)))
    def get_items_all(self, n: int = 1000) -> system_state_read_dtos:
        return system_state_read_dtos(self.get_items(self.get_model().get_select_all_limit_sql(n)))
    def get_items_active(self, n: int = 1000) -> system_state_read_dtos:
        return system_state_read_dtos(self.get_items(self.get_model().get_select_active_limit_sql(n)))
    def get_items_all_latest(self, n: int = 1000) -> system_state_read_dtos:
        return system_state_read_dtos(self.get_items(self.get_model().get_select_all_latest_sql(n)))
    def get_items_active_latest(self, n: int = 1000) -> system_state_read_dtos:
        return system_state_read_dtos(self.get_items(self.get_model().get_select_active_latest_sql(n)))
    def get_items_write_all(self, n: int = 1000) -> system_state_write_dtos:
        return system_state_write_dtos(self.get_items_write(self.get_model().get_select_write_all_limit_sql(n)))
    def get_items_write_active(self, n: int = 1000) -> system_state_write_dtos:
        return system_state_write_dtos(self.get_items_write(self.get_model().get_select_write_active_limit_sql(n)))
    def get_items_write_all_latest(self, n: int = 1000) -> system_state_write_dtos:
        return system_state_write_dtos(self.get_items_write(self.get_model().get_select_write_all_latest_sql(n)))
    def get_items_write_active_latest(self, n: int = 1000) -> system_state_write_dtos:
        return system_state_write_dtos(self.get_items_write(self.get_model().get_select_write_active_latest_sql(n)))
    def get_item_by_uid(self, uid: str) -> system_state_read_dto | None:
        return system_state_read_dtos(self.get_items_with_params(self.get_model().get_select_by_key(), (uid,))).get_first()
    def get_item_by_id(self, id: int) -> system_state_read_dto | None:
        return system_state_read_dtos(self.get_items_with_params(self.get_model().get_select_by_id(), (id,))).get_first()
    def get_items_by_any_column(self, col_name: str, col_value: any, n: int = 1000) -> system_state_read_dtos:
        return system_state_read_dtos(self.get_items_with_params(self.get_model().get_select_active_by_any_column(col_name, n), (col_value,)))
    def get_uids(self, n: int = 1000) -> list[str]:
        return self.get_column_values_all(self.get_model().get_select_all_keys(n))
    def get_guids(self, n: int = 1000) -> list[str]:
        return self.get_column_values_all(self.get_model().get_select_all_guids(n))
    def count_all(self) -> int:
        return self.get_single_value_int_or_default(self.get_model().get_select_count_all_sql())
    def count_active(self) -> int:
        return self.get_single_value_int_or_default(self.get_model().get_select_count_active_sql())
    def count_by_any_column(self, col_name: str, col_value: any) -> int:
        return self.get_single_value_int_or_default_by_params(self.get_model().get_select_count_by_any_column_sql(col_name), (col_value,))
    def insert_dtos(self, dtos: list[system_state_write_dto], created_by: str):
        self.insert_many(dtos, created_by)
    def insert_write_dtos(self, dtos: system_state_write_dtos, created_by: str):
        self.insert_dtos(dtos.dtos, created_by)
    def insert_read_dtos(self, dtos: system_state_read_dtos, created_by: str):
        self.insert_dtos(dtos.get_write_dtos(), created_by)
    def delete_logical_dtos(self, dtos: list[system_state_write_dto], removed_by: str):
        uids = list(map(lambda dto: dto.get_uid(), dtos))
        return self.delete_logical_by_uids(uids, removed_by)
    def delete_logical_write_dtos(self, dtos: system_state_write_dtos, removed_by: str):
        return self.delete_logical_dtos(dtos.dtos, removed_by)




